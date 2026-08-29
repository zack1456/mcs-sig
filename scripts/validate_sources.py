#!/usr/bin/env python3
"""
validate_sources.py
-------------------
Validates every JSON file under aiml_wg/sources/papers/ against the CrossRef
and NCBI PubMed APIs to detect hallucinated DOIs or PMIDs.

A hallucinated DOI can resolve to a REAL but WRONG paper (HTTP 200), so
existence alone is not sufficient. This script cross-checks:

  1. DOI resolution  (HTTP 404 = hallucinated ID, hard fail)
  2. Title similarity between JSON record and what CrossRef/PubMed returns
     (token-overlap Jaccard >= 0.5 required; below threshold = hard fail)
  3. Author family-name overlap between JSON and CrossRef/PubMed response
     (at least 1 family name must match; zero overlap = hard fail)

Confirmed identifier and metadata mismatches are hard failures (exit 1).
Transient network, rate-limit, and metadata-service failures are review
warnings and do not falsely classify an identifier as hallucinated. Set
doi/pmid to null for unconfirmed preprints rather than guessing identifiers.

Usage:
    python scripts/validate_sources.py               # checks all files
    python scripts/validate_sources.py --files a.json b.json

Exit codes:
    0  All checks passed
    1  One or more hard failures detected
"""

import argparse
import glob
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

CROSSREF_BASE = "https://api.crossref.org/works/"
PUBMED_ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PUBMED_ESEARCH  = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
USER_AGENT = "MCS-SIG-Source-Validator/1.1 (mailto:mcs-sig@isop.org)"
RETRY_DELAYS = (0.0, 0.5, 1.5)
_RESPONSE_CACHE: dict[str, dict] = {}

if sys.stdout.isatty():
    PASS = "\033[92m[PASS]\033[0m"
    WARN = "\033[93m[WARN]\033[0m"
    FAIL = "\033[91m[FAIL]\033[0m"
    INFO = "\033[94m[INFO]\033[0m"
else:
    PASS, WARN, FAIL, INFO = "[PASS]", "[WARN]", "[FAIL]", "[INFO]"

TITLE_JACCARD_THRESHOLD = 0.50  # token overlap required to consider titles equivalent


# ---------------------------------------------------------------------------
# HTTP helper
# ---------------------------------------------------------------------------

class IdentifierNotFound(Exception):
    """The remote service definitively reported that an identifier is absent."""


class MetadataServiceUnavailable(Exception):
    """Metadata could not be checked because the remote service was unavailable."""


def _get(url: str, timeout: int = 8) -> dict:
    if url in _RESPONSE_CACHE:
        return _RESPONSE_CACHE[url]
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last_error: Exception | None = None
    for attempt, delay in enumerate(RETRY_DELAYS):
        if delay:
            time.sleep(delay)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = json.loads(r.read().decode())
                _RESPONSE_CACHE[url] = data
                return data
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise IdentifierNotFound from e
            last_error = e
            if e.code != 429 and e.code < 500:
                break
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last_error = e
        if attempt == len(RETRY_DELAYS) - 1:
            break
    detail = f"HTTP {last_error.code}" if isinstance(last_error, urllib.error.HTTPError) else str(last_error)
    raise MetadataServiceUnavailable(detail) from last_error


# ---------------------------------------------------------------------------
# Similarity helpers
# ---------------------------------------------------------------------------

def _token_set(s: str) -> set[str]:
    """Lowercase word tokens, stripping punctuation. Ignores stop-words."""
    STOP = {"a", "an", "the", "of", "for", "in", "on", "with", "and", "to",
            "by", "from", "at", "is", "are", "via", "using", "based"}
    return {w for w in "".join(c if c.isalnum() else " " for c in s.lower()).split()
            if w not in STOP and len(w) > 1}


def _title_jaccard(a: str, b: str) -> float:
    """Jaccard similarity on word-token sets (ignores stop words)."""
    sa, sb = _token_set(a), _token_set(b)
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def _author_family_names(authors_json: list) -> set[str]:
    """Extract lowercase family names from the JSON authors array.
    Accepts 'Last F', 'Last, First', or 'Last' formats."""
    names = set()
    for a in authors_json:
        if not a:
            continue
        # Take the first token as the family name (handles 'Dunn R', 'Dunn Robin', 'Dunn')
        family = a.split(",")[0].split()[0].lower()
        if len(family) > 1:
            names.add(family)
    return names


def _crossref_family_names(cr_authors: list[dict]) -> set[str]:
    return {a.get("family", "").lower() for a in cr_authors if a.get("family")}


def _pubmed_author_names(pm_authors: list[dict]) -> set[str]:
    """PubMed returns authors as {'name': 'Dunn R'} — take first token."""
    names = set()
    for a in pm_authors:
        parts = a.get("name", "").split()
        if parts:
            names.add(parts[0].lower())
    return names


# ---------------------------------------------------------------------------
# API checks
# ---------------------------------------------------------------------------

def check_doi(doi: str, json_title: str, json_authors: list) -> list[dict]:
    """
    Returns list of issue dicts. Empty list = all clear.
    Checks: (1) DOI resolves, (2) title similarity, (3) author overlap.
    """
    issues = []
    url = CROSSREF_BASE + urllib.parse.quote(doi, safe="")
    try:
        data = _get(url)
    except IdentifierNotFound:
        issues.append({
            "level": "fail",
            "field": "doi_not_found",
            "message": f"DOI {doi!r} → HTTP 404 from CrossRef. ID does not exist — likely hallucinated.",
        })
        return issues  # Can't do further checks without data
    except MetadataServiceUnavailable as exc:
        issues.append({
            "level": "warn",
            "field": "doi_unverified",
            "message": f"DOI {doi!r} could not be checked because CrossRef was unavailable ({exc}).",
        })
        return issues

    msg = data.get("message", {})
    cr_titles = msg.get("title", [])
    cr_title = cr_titles[0] if cr_titles else ""
    cr_authors = msg.get("author", [])

    # (2) Title similarity
    if json_title and cr_title:
        score = _title_jaccard(json_title, cr_title)
        if score < TITLE_JACCARD_THRESHOLD:
            issues.append({
                "level": "fail",
                "field": "doi_title_mismatch",
                "message": (
                    f"DOI resolves to a DIFFERENT paper (Jaccard={score:.2f} < {TITLE_JACCARD_THRESHOLD}).\n"
                    f"    JSON title:     {json_title[:90]}\n"
                    f"    CrossRef title: {cr_title[:90]}"
                ),
            })

    # (3) Author overlap
    if json_authors and cr_authors:
        json_names = _author_family_names(json_authors)
        cr_names = _crossref_family_names(cr_authors)
        if json_names and cr_names and not (json_names & cr_names):
            issues.append({
                "level": "fail",
                "field": "doi_author_mismatch",
                "message": (
                    f"DOI author list has ZERO overlap with JSON authors.\n"
                    f"    JSON authors:     {sorted(json_names)}\n"
                    f"    CrossRef authors: {sorted(cr_names)}"
                ),
            })

    return issues


def check_pmid(pmid: int, json_title: str, json_authors: list) -> list[dict]:
    """
    Returns list of issue dicts. Checks: (1) PMID resolves, (2) title, (3) authors.
    """
    issues = []
    url = f"{PUBMED_ESUMMARY}?db=pubmed&id={pmid}&retmode=json"
    try:
        data = _get(url)
    except (IdentifierNotFound, MetadataServiceUnavailable) as exc:
        issues.append({
            "level": "warn",
            "field": "pmid_unverified",
            "message": f"PMID {pmid} could not be checked because PubMed was unavailable ({exc}).",
        })
        return issues

    summary = data.get("result", {}).get(str(pmid), {})
    pm_title = summary.get("title", "").strip()
    pm_authors = summary.get("authors", [])

    if not pm_title:
        issues.append({
            "level": "fail",
            "field": "pmid_not_found",
            "message": f"PMID {pmid} not found in PubMed — likely hallucinated.",
        })
        return issues

    # (2) Title similarity
    if json_title:
        score = _title_jaccard(json_title, pm_title)
        if score < TITLE_JACCARD_THRESHOLD:
            issues.append({
                "level": "fail",
                "field": "pmid_title_mismatch",
                "message": (
                    f"PMID resolves to a DIFFERENT paper (Jaccard={score:.2f} < {TITLE_JACCARD_THRESHOLD}).\n"
                    f"    JSON title:  {json_title[:90]}\n"
                    f"    NCBI title:  {pm_title[:90]}"
                ),
            })

    # (3) Author overlap
    if json_authors and pm_authors:
        json_names = _author_family_names(json_authors)
        pm_names = _pubmed_author_names(pm_authors)
        if json_names and pm_names and not (json_names & pm_names):
            issues.append({
                "level": "fail",
                "field": "pmid_author_mismatch",
                "message": (
                    f"PMID author list has ZERO overlap with JSON authors.\n"
                    f"    JSON authors: {sorted(json_names)}\n"
                    f"    NCBI authors: {sorted(pm_names)}"
                ),
            })

    return issues


# ---------------------------------------------------------------------------
# Per-file validation
# ---------------------------------------------------------------------------

def validate_file(path: Path) -> list[dict]:
    issues = []
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        issues.append({"level": "fail", "field": "json_parse", "message": f"Invalid JSON: {e}"})
        return issues

    json_title   = data.get("title", "").strip()
    json_authors = data.get("authors", [])
    doi          = data.get("doi")
    pmid         = data.get("pmid")

    if doi:
        issues.extend(check_doi(doi, json_title, json_authors))
        time.sleep(0.05)

    if pmid is not None:
        issues.extend(check_pmid(pmid, json_title, json_authors))
        time.sleep(0.05)

    return issues


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import sys
    sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Validate source JSON DOIs and PMIDs.")
    parser.add_argument("--all", action="store_true", help="Check all files in aiml_wg/sources/papers/")
    parser.add_argument("--files", nargs="+", help="Specific files to check")
    args = parser.parse_args()

    repo_root  = Path(__file__).resolve().parent.parent
    papers_dir = repo_root / "aiml_wg" / "sources" / "papers"

    if args.files:
        files = [Path(f) for f in args.files]
    else:
        files = sorted(papers_dir.glob("*.json"))

    if not files:
        print(f"{INFO} No files to validate.")
        sys.exit(0)

    print(f"{INFO} Validating {len(files)} source file(s) ...\n"
          f"     Checks: (1) DOI/PMID resolves  (2) title Jaccard >= {TITLE_JACCARD_THRESHOLD}"
          f"  (3) author family-name overlap >= 1\n")

    total_fails = 0
    total_warnings = 0

    for path in files:
        issues = validate_file(path)
        fails  = [i for i in issues if i["level"] == "fail"]
        warnings = [i for i in issues if i["level"] == "warn"]
        total_fails += len(fails)
        total_warnings += len(warnings)

        if not fails and not warnings:
            print(f"{PASS} {path.name}")
        else:
            print(f"{FAIL if fails else WARN} {path.name}")
            for iss in fails:
                print(f"   ✗ [{iss['field']}] {iss['message']}")
            for iss in warnings:
                print(f"   ! [{iss['field']}] {iss['message']}")

    print(f"\n{'='*64}")
    print(f"  Files checked : {len(files)}")
    print(f"  Hard failures : {total_fails}")
    print(f"  Review warnings: {total_warnings}")
    print(f"{'='*64}")

    if total_fails > 0:
        print(f"\n{FAIL} Validation FAILED. Fix identifiers before committing.")
        print("  Rule: set doi/pmid to null if the correct ID is not confirmed.")
        sys.exit(1)
    elif total_warnings > 0:
        print(f"\n{WARN} Verification completed with review warnings and no hard failures.")
    else:
        print(f"\n{PASS} All source records validated successfully.")


if __name__ == "__main__":
    main()
