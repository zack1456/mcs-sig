---
name: literature-maintainer
description: Add, upgrade, audit, or repair literature records in the MCS SIG source library, including evidence extraction, provenance, index synchronization, and newcomer-safe source intake.
---

# Literature maintainer

Maintain `aiml_wg/sources/` without treating automated consistency as scientific review.

Before changing a source record, read `aiml_wg/sources/MAINTENANCE.md` and `_schema.json`. Use `python scripts/literature.py add` for identifier-only intake, or edit a source record when the requested evidence has actually been accessed.

For extraction or upgrades:

- Check the existing library for duplicate DOI, PMID, and title before writing.
- Preserve the boundary imposed by `provenance.read_depth`.
- Do not invent metadata, claims, numbers, evidence locations, or relationship targets.
- Keep every extracted source record at `review_status: "draft"` until a human scientific reviewer documents the review; do not mark a record reviewed on the model's own authority.
- Reconsider documents that cite the record when new evidence narrows a novelty, gap, safety, or regulatory claim.

After modifications, run `python scripts/literature.py fix`, then `python scripts/literature.py check`. Resolve errors. Report warnings, accessed evidence, reading depth, files changed, and the remaining human-review requirement.

Use `python scripts/validate_sources.py --pending` for routine online metadata verification and `--all` for a complete recheck. Add `--record-results --verified-by "agent-or-person"` only when the successful results should update source records. Network unavailability is not evidence that an identifier is false and must not overwrite a previous successful verification. Identifier verification is distinct from human scientific review.
