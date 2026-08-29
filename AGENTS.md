# Repository guidance

When adding, extracting, upgrading, or auditing literature under `aiml_wg/sources/`, use the `literature-maintainer` skill when available and follow `aiml_wg/sources/MAINTENANCE.md`.

After changing a source record, source citation, schema, index, or reader, run:

```text
python scripts/literature.py fix
python scripts/literature.py check
```

Treat automated structural success as distinct from human scientific review. New LLM-assisted source records must use `review_status: "draft"` until a person reviews the extraction against the accessed source.
