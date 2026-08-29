#!/usr/bin/env python3
"""Friendly, dependency-free maintenance CLI for the source library.

Commands:
    literature.py add <DOI-or-PMID-or-URL>  Create a draft intake note.
    literature.py check                    Run deterministic offline checks.
    literature.py fix                      Repair deterministic derived data.

The checker intentionally does not access the network. External identifier
verification remains available through scripts/validate_sources.py.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = REPO_ROOT / "aiml_wg" / "sources"
SCHEMA_PATH = SOURCES_DIR / "_schema.json"
INDEX_PATH = SOURCES_DIR / "index.json"
READER_BUILDER = SOURCES_DIR / "build_reader.py"
RECORD_DIRS = ("papers", "web", "background", "working_docs")
SOURCE_ID_RE = re.compile(r"(?<![A-Za-z0-9_])([a-z][a-z0-9_]+_(?:19|20)\d{2}[a-z0-9_]*)(?![A-Za-z0-9_])")


@dataclass(frozen=True)
class Issue:
    level: str
    code: str
    message: str
    path: str | None = None
    fixable: bool = False


def rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def compact_scalar_arrays(text: str) -> str:
    """Keep arrays of scalar values on one line to minimize maintenance diffs."""
    lines = text.splitlines()
    output: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.rstrip().endswith("["):
            closing = index + 1
            items: list[str] = []
            while closing < len(lines) and not lines[closing].lstrip().startswith("]"):
                items.append(lines[closing].strip())
                closing += 1
            if (
                closing < len(lines)
                and items
                and all(item and item[0] not in "[{" for item in items)
                and all(not item.endswith("{") and not item.endswith("[") for item in items)
            ):
                prefix = line[: line.rfind("[")]
                suffix = lines[closing].strip()[1:]
                output.append(prefix + "[" + " ".join(items) + "]" + suffix)
                index = closing + 1
                continue
        output.append(line)
        index += 1
    return "\n".join(output)


def write_json(path: Path, value: Any) -> None:
    rendered = compact_scalar_arrays(json.dumps(value, ensure_ascii=False, indent=2))
    path.write_text(rendered + "\n", encoding="utf-8", newline="\n")


def record_paths() -> list[Path]:
    paths: list[Path] = []
    for dirname in RECORD_DIRS:
        directory = SOURCES_DIR / dirname
        if directory.exists():
            paths.extend(directory.glob("*.json"))
    return sorted(paths)


def normalize_doi(value: str) -> str:
    value = value.strip().lower()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if value.startswith(prefix):
            value = value[len(prefix):]
    return value.rstrip(".")


def normalize_title(value: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", value.lower()))


def json_type_matches(value: Any, expected: str) -> bool:
    if expected == "null":
        return value is None
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    return True


def schema_issues(value: Any, schema: dict[str, Any], location: str, path: Path) -> list[Issue]:
    """Validate the Draft-07 features used by this repository's schema."""
    issues: list[Issue] = []
    expected = schema.get("type")
    if expected is not None:
        allowed = expected if isinstance(expected, list) else [expected]
        if not any(json_type_matches(value, item) for item in allowed):
            return [Issue("error", "schema_type", f"{location} must be {' or '.join(allowed)}.", rel(path))]

    if "enum" in schema and value not in schema["enum"]:
        issues.append(Issue("error", "schema_enum", f"{location} has unsupported value {value!r}.", rel(path)))
    if isinstance(value, str):
        if "pattern" in schema and not re.search(schema["pattern"], value):
            issues.append(Issue("error", "schema_pattern", f"{location} has an invalid format.", rel(path)))
        if len(value) < schema.get("minLength", 0):
            issues.append(Issue("error", "schema_min_length", f"{location} cannot be empty.", rel(path)))
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            issues.append(Issue("error", "schema_min_items", f"{location} has too few entries.", rel(path)))
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            issues.append(Issue("error", "schema_max_items", f"{location} has too many entries.", rel(path)))
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                issues.extend(schema_issues(item, item_schema, f"{location}[{index}]", path))
    if isinstance(value, dict):
        properties = schema.get("properties", {})
        for name in schema.get("required", []):
            if name not in value:
                issues.append(Issue("error", "schema_required", f"{location}.{name} is required.", rel(path)))
        if schema.get("additionalProperties") is False:
            for name in value:
                if name not in properties:
                    issues.append(Issue("error", "schema_extra_field", f"{location}.{name} is not in the schema.", rel(path)))
        for name, child in value.items():
            if name in properties:
                issues.extend(schema_issues(child, properties[name], f"{location}.{name}", path))
    return issues


def load_records() -> tuple[dict[str, dict[str, Any]], dict[str, Path], list[Issue]]:
    records: dict[str, dict[str, Any]] = {}
    paths: dict[str, Path] = {}
    issues: list[Issue] = []
    schema = load_json(SCHEMA_PATH)
    dois: dict[str, str] = {}
    pmids: dict[int, str] = {}
    titles: dict[str, str] = {}

    for path in record_paths():
        try:
            record = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            issues.append(Issue("error", "json_parse", f"Cannot read valid JSON: {exc}", rel(path)))
            continue
        issues.extend(schema_issues(record, schema, "$", path))
        source_id = record.get("id")
        if not isinstance(source_id, str):
            continue
        if source_id in records:
            issues.append(Issue("error", "duplicate_id", f"ID {source_id!r} is also used by {rel(paths[source_id])}.", rel(path)))
        records[source_id] = record
        paths[source_id] = path
        if path.stem != source_id:
            issues.append(Issue("error", "filename_id", f"Filename must be {source_id}.json.", rel(path)))

        doi = record.get("doi")
        if isinstance(doi, str) and doi.strip():
            normalized = normalize_doi(doi)
            if normalized in dois:
                issues.append(Issue("error", "duplicate_doi", f"DOI duplicates {dois[normalized]}.", rel(path)))
            else:
                dois[normalized] = source_id
            if doi != normalized:
                issues.append(Issue("warning", "doi_normalization", f"Store DOI as {normalized!r} without a URL prefix.", rel(path)))
        pmid = record.get("pmid")
        if isinstance(pmid, int):
            if pmid in pmids:
                issues.append(Issue("error", "duplicate_pmid", f"PMID duplicates {pmids[pmid]}.", rel(path)))
            else:
                pmids[pmid] = source_id
        title = record.get("title")
        if isinstance(title, str) and title.strip():
            normalized_title = normalize_title(title)
            if normalized_title in titles:
                issues.append(Issue("error", "duplicate_title", f"Title duplicates {titles[normalized_title]}.", rel(path)))
            else:
                for prior_title, prior_id in titles.items():
                    similarity = difflib.SequenceMatcher(None, normalized_title, prior_title).ratio()
                    if similarity >= 0.94:
                        issues.append(Issue("warning", "similar_title", f"Title is {similarity:.0%} similar to {prior_id}; confirm these are different sources.", rel(path)))
                titles[normalized_title] = source_id
    return records, paths, issues


def same_list(left: Iterable[Any], right: Iterable[Any]) -> bool:
    return sorted(left) == sorted(right)


def check_index(records: dict[str, dict[str, Any]], paths: dict[str, Path]) -> list[Issue]:
    issues: list[Issue] = []
    try:
        index = load_json(INDEX_PATH)
    except (OSError, json.JSONDecodeError) as exc:
        return [Issue("error", "index_parse", f"Cannot read index.json: {exc}", rel(INDEX_PATH))]
    entries = index.get("sources", [])
    by_id: dict[str, dict[str, Any]] = {}
    for entry in entries:
        source_id = entry.get("id")
        if source_id in by_id:
            issues.append(Issue("error", "index_duplicate", f"Index contains {source_id!r} more than once.", rel(INDEX_PATH), True))
        by_id[source_id] = entry

    for source_id, record in records.items():
        if source_id not in by_id:
            issues.append(Issue("error", "index_missing", f"Index is missing {source_id}.", rel(INDEX_PATH), True))
            continue
        entry = by_id[source_id]
        expected_file = paths[source_id].relative_to(SOURCES_DIR).as_posix()
        comparisons = {
            "file": (entry.get("file"), expected_file),
            "source_type": (entry.get("source_type"), record.get("source_type")),
            "relevance": (entry.get("relevance"), record.get("relevance", {}).get("relevance_score")),
        }
        for field, (actual, expected) in comparisons.items():
            if actual != expected:
                issues.append(Issue("error", "index_mismatch", f"Index {field} for {source_id} is {actual!r}; expected {expected!r}.", rel(INDEX_PATH), True))
        if not same_list(entry.get("pillars", []), record.get("relevance", {}).get("pillars", [])):
            issues.append(Issue("error", "index_mismatch", f"Index pillars for {source_id} do not match the record.", rel(INDEX_PATH), True))
    for source_id in by_id.keys() - records.keys():
        issues.append(Issue("error", "index_orphan", f"Index points to missing record {source_id}.", rel(INDEX_PATH), True))
    return issues


def check_relationships(records: dict[str, dict[str, Any]], paths: dict[str, Path]) -> list[Issue]:
    issues: list[Issue] = []
    for source_id, record in records.items():
        relationships = record.get("relationships", {})
        for relation in ("cites", "extends", "contradicts", "cited_by"):
            for target in filter(None, relationships.get(relation, [])):
                if target not in records:
                    issues.append(Issue("warning", "relationship_missing", f"{source_id}.{relation} points to unknown source {target}.", rel(paths[source_id])))
        reverse_citation_targets = set(filter(None, relationships.get("cites", []))) | set(filter(None, relationships.get("extends", [])))
        for target in reverse_citation_targets:
            if target in records and source_id not in records[target].get("relationships", {}).get("cited_by", []):
                issues.append(Issue("warning", "relationship_reciprocity", f"{target}.cited_by does not include {source_id}.", rel(paths[target]), True))
        for target in filter(None, relationships.get("contradicts", [])):
            if target in records and source_id not in records[target].get("relationships", {}).get("contradicts", []):
                issues.append(Issue("warning", "relationship_reciprocity", f"{target}.contradicts does not include {source_id}.", rel(paths[target]), True))
    return issues


def check_review_metadata(records: dict[str, dict[str, Any]], paths: dict[str, Path]) -> list[Issue]:
    """Require an auditable reviewer and date before a record can be reviewed."""
    issues: list[Issue] = []
    for source_id, record in records.items():
        status = record.get("review_status")
        reviewer = record.get("reviewed_by")
        reviewed_date = record.get("reviewed_date")
        if status == "reviewed":
            missing = [name for name, value in (("reviewed_by", reviewer), ("reviewed_date", reviewed_date)) if not value]
            if missing:
                issues.append(Issue(
                    "error",
                    "review_metadata_missing",
                    f"{source_id} is reviewed but lacks {', '.join(missing)}.",
                    rel(paths[source_id]),
                ))
        elif reviewer or reviewed_date:
            issues.append(Issue(
                "error",
                "review_metadata_without_status",
                f"{source_id} has reviewer metadata but review_status is not 'reviewed'.",
                rel(paths[source_id]),
            ))
    return issues


def check_markdown_citations(records: dict[str, dict[str, Any]]) -> list[Issue]:
    issues: list[Issue] = []
    ignored_dirs = {".git", ".venv", "node_modules"}
    for path in (REPO_ROOT / "aiml_wg").rglob("*.md"):
        if any(part in ignored_dirs for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for source_id in sorted(set(SOURCE_ID_RE.findall(text))):
            if source_id not in records:
                issues.append(Issue("warning", "citation_unresolved", f"Possible source citation {source_id!r} is not in the library.", rel(path)))
    return issues


def check_reader() -> list[Issue]:
    result = subprocess.run(
        [sys.executable, str(READER_BUILDER), "--check"],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        encoding="utf-8",
    )
    if result.returncode:
        detail = (result.stdout + result.stderr).strip() or "reader.html is not current."
        return [Issue("warning", "reader_stale", detail, rel(SOURCES_DIR / "reader.html"), True)]
    return []


def check_documented_counts(count: int) -> list[Issue]:
    issues: list[Issue] = []
    for path in (REPO_ROOT / "aiml_wg" / "STATUS.md", REPO_ROOT / "aiml_wg" / "WORKPLAN.md"):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        matches = re.findall(r"(?:Source library:\*\* |Authoritative record: `sources/index\.json` \()([0-9]+)(?: indexed)? records", text)
        for stated in matches:
            if int(stated) != count:
                issues.append(Issue("warning", "source_count_stale", f"Reports {stated} sources; the library contains {count}.", rel(path), True))
    return issues


def run_checks() -> tuple[list[Issue], dict[str, dict[str, Any]], dict[str, Path]]:
    records, paths, issues = load_records()
    issues.extend(check_index(records, paths))
    issues.extend(check_relationships(records, paths))
    issues.extend(check_review_metadata(records, paths))
    issues.extend(check_markdown_citations(records))
    issues.extend(check_reader())
    issues.extend(check_documented_counts(len(records)))
    return issues, records, paths


def display(issues: list[Issue], records: dict[str, dict[str, Any]], output_format: str) -> None:
    errors = [issue for issue in issues if issue.level == "error"]
    warnings = [issue for issue in issues if issue.level == "warning"]
    drafts = sorted(source_id for source_id, record in records.items() if record.get("review_status") == "draft")
    if output_format == "json":
        print(json.dumps({
            "records": len(records),
            "draft_records": len(drafts),
            "draft_ids": drafts,
            "errors": len(errors),
            "warnings": len(warnings),
            "issues": [asdict(issue) for issue in issues],
        }, indent=2))
        return
    print(f"Source library: {len(records)} records | {len(errors)} errors | {len(warnings)} warnings | {len(drafts)} drafts")
    for issue in issues:
        marker = "ERROR" if issue.level == "error" else "REVIEW"
        location = f" ({issue.path})" if issue.path else ""
        fix = " Run `python scripts/literature.py fix`." if issue.fixable else ""
        print(f"[{marker}] {issue.message}{location}{fix}")
    if errors:
        print("\nCannot submit yet: fix the ERROR items above. Your files have not been deleted or reverted.")
    elif warnings:
        print("\nSafe to commit, with review items noted above.")
    else:
        print("\nSafe to submit: all offline structural checks passed.")
    if drafts:
        print(f"Human review remains: {len(drafts)} draft record(s). Use the reader's Draft filter to inspect them.")


def index_entry(record: dict[str, Any], path: Path, previous: dict[str, Any] | None) -> dict[str, Any]:
    title_short = (previous or {}).get("title_short") or record.get("title", "Untitled")
    record_pillars = record["relevance"]["pillars"]
    previous_pillars = (previous or {}).get("pillars", [])
    pillars = previous_pillars if same_list(previous_pillars, record_pillars) else record_pillars
    return {
        "id": record["id"],
        "file": path.relative_to(SOURCES_DIR).as_posix(),
        "source_type": record["source_type"],
        "title_short": title_short,
        "pillars": pillars,
        "relevance": record["relevance"]["relevance_score"],
    }


def fix_library() -> None:
    records, paths, parse_issues = load_records()
    if any(issue.level == "error" for issue in parse_issues):
        print("Cannot repair derived files until all source-record errors are fixed.")
        display(parse_issues, records, "text")
        raise SystemExit(1)

    index = load_json(INDEX_PATH)
    old_entries = {entry.get("id"): entry for entry in index.get("sources", [])}
    ordered_ids = [entry.get("id") for entry in index.get("sources", []) if entry.get("id") in records]
    ordered_ids.extend(sorted(set(records) - set(ordered_ids)))
    index["sources"] = [index_entry(records[source_id], paths[source_id], old_entries.get(source_id)) for source_id in ordered_ids]
    write_json(INDEX_PATH, index)

    for source_id, record in records.items():
        doi = record.get("doi")
        if isinstance(doi, str) and doi.strip():
            normalized = normalize_doi(doi)
            if doi != normalized:
                record["doi"] = normalized
                write_json(paths[source_id], record)

    changed_records: set[str] = set()
    for source_id, record in records.items():
        relationships = record.setdefault("relationships", {})
        for target in filter(None, relationships.get("cites", [])):
            if target in records:
                reverse = records[target].setdefault("relationships", {}).setdefault("cited_by", [])
                if source_id not in reverse:
                    reverse.append(source_id)
                    changed_records.add(target)
        for target in filter(None, relationships.get("extends", [])):
            if target in records:
                reverse = records[target].setdefault("relationships", {}).setdefault("cited_by", [])
                if source_id not in reverse:
                    reverse.append(source_id)
                    changed_records.add(target)
        for target in filter(None, relationships.get("contradicts", [])):
            if target in records:
                reverse = records[target].setdefault("relationships", {}).setdefault("contradicts", [])
                if source_id not in reverse:
                    reverse.append(source_id)
                    changed_records.add(target)
    for source_id in changed_records:
        write_json(paths[source_id], records[source_id])

    count = len(records)
    for path in (REPO_ROOT / "aiml_wg" / "STATUS.md", REPO_ROOT / "aiml_wg" / "WORKPLAN.md"):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"(Source library:\*\* )[0-9]+( indexed records)", rf"\g<1>{count}\g<2>", text)
        text = re.sub(r"(Authoritative record: `sources/index\.json` \()[0-9]+( records)", rf"\g<1>{count}\g<2>", text)
        path.write_text(text, encoding="utf-8", newline="\n")

    subprocess.run([sys.executable, str(READER_BUILDER)], cwd=REPO_ROOT, check=True)
    print(f"Repaired index metadata, {len(changed_records)} reciprocal relationship record(s), reader.html, and current source counts.")


def slugify_identifier(identifier: str) -> str:
    slug = re.sub(r"^https?://", "", identifier.strip().lower())
    slug = re.sub(r"[^a-z0-9]+", "_", slug).strip("_")
    return (slug[:60] or "source").rstrip("_")


def create_intake(args: argparse.Namespace) -> None:
    intake_dir = SOURCES_DIR / "intake"
    intake_dir.mkdir(parents=True, exist_ok=True)
    base = f"{date.today().isoformat()}_{slugify_identifier(args.identifier)}"
    path = intake_dir / f"{base}.md"
    counter = 2
    while path.exists():
        path = intake_dir / f"{base}_{counter}.md"
        counter += 1
    contributor = args.contributor or "Not provided"
    title = args.title or "To be confirmed"
    notes = args.notes or "None provided"
    content = f"""# Literature source intake

- **Identifier or URL:** {args.identifier}
- **Working title:** {title}
- **Submitted by:** {contributor}
- **Date submitted:** {date.today().isoformat()}
- **Notes:** {notes}

## Maintainer review

- [ ] Confirm canonical DOI, PMID, title, authors, year, and venue.
- [ ] Check for duplicate DOI, PMID, or title.
- [ ] Obtain and record the actual reading depth.
- [ ] Create a schema-valid source record with `review_status: "draft"`.
- [ ] Review claims and numerical findings against the accessed text.
- [ ] Run `python scripts/literature.py fix` and then `check`.
- [ ] Mark the record reviewed only after human scientific review.
"""
    path.write_text(content, encoding="utf-8", newline="\n")
    print(f"Draft intake created: {rel(path)}")
    print("No source JSON was published. A maintainer or the literature-maintainer skill can complete the extraction.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Friendly maintenance tools for the MCS SIG literature library.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    check_parser = subparsers.add_parser("check", help="Run fast offline checks; never contacts external services.")
    check_parser.add_argument("--format", choices=("text", "json"), default="text")
    check_parser.add_argument("--strict-warnings", action="store_true", help="Treat review warnings as failures (intended for maintainers).")
    subparsers.add_parser("fix", help="Repair index metadata, reciprocal links, reader.html, and current counts.")
    add_parser = subparsers.add_parser("add", help="Create a safe draft intake from a DOI, PMID, URL, or citation.")
    add_parser.add_argument("identifier")
    add_parser.add_argument("--title")
    add_parser.add_argument("--contributor")
    add_parser.add_argument("--notes")
    args = parser.parse_args()

    if args.command == "add":
        create_intake(args)
        return
    if args.command == "fix":
        fix_library()
    issues, records, _ = run_checks()
    display(issues, records, getattr(args, "format", "text"))
    has_errors = any(issue.level == "error" for issue in issues)
    has_warnings = any(issue.level == "warning" for issue in issues)
    if has_errors or (getattr(args, "strict_warnings", False) and has_warnings):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
