# Source library maintenance

This is the provider-neutral maintenance contract for people and AI assistants working with the literature library. Claude commands, Codex skills, and other agent instructions should point here instead of maintaining separate versions of these rules.

## Contribution paths

1. **Intake:** A contributor submits a DOI, PMID, URL, PDF reference, or citation using `python scripts/literature.py add`. A maintainer completes the extraction later.
2. **Guided extraction:** An AI assistant or maintainer creates the source record from material it actually accessed.
3. **Direct maintenance:** An experienced contributor edits source JSON and runs `fix` followed by `check`.

## Canonical and generated files

- Source JSON records and `_schema.json` are canonical.
- `index.json` mirrors selected record metadata and preserves its curated `title_short` values.
- `reader.html` is generated from the index and source records.
- `STATUS.md` and the current source-library statement in `WORKPLAN.md` must agree with the number of indexed records.

Do not ask contributors to hand-maintain derived fields. `python scripts/literature.py fix` synchronizes them.

## Evidence rules

- Search for duplicate DOI, PMID, and near-matching titles before creating a record.
- Use canonical metadata from authoritative sources when available.
- Record the material actually accessed in `provenance.notes` and set `read_depth` honestly.
- Do not introduce a numerical finding unless the value appears in the accessed material.
- Give extracted claims and numerical findings a location that is reachable at the recorded reading depth.
- Mark genuinely inferred findings with `[inferred]`.
- Do not silently upgrade an abstract-only record to `sections_key` or `full_text`.
- New LLM-assisted records use `review_status: "draft"`. Only human scientific review can change it to `"reviewed"`.
- A reviewed record must also identify the human reviewer in `reviewed_by` and record the ISO review date in `reviewed_date`; `review_notes` can capture scope or caveats.

## Required workflow after an extraction or update

1. Update the source record.
2. Update meaningful relationships to existing library IDs.
3. Add or update the focused search record when the source came from a literature search.
4. Reassess dependent novelty, gap, or regulatory claims in documents that cite the source.
5. Run `python scripts/literature.py fix`.
6. Run `python scripts/literature.py check` and resolve all errors.
7. Report warnings and evidence limitations to the user or reviewer.

The offline checker never contacts external services. Maintainers can separately run `python scripts/validate_sources.py --all` when network metadata verification is appropriate.

## What automation means

Errors are deterministic problems that must be fixed, such as malformed records, duplicate identifiers, stale index metadata, or relationships to missing records. Warnings identify review work, such as asymmetric relationships, possible unresolved Markdown citations, or stale generated files. Draft records are shown as a separate human-review queue rather than as structural warnings. Passing checks does not establish scientific correctness or regulatory suitability.
