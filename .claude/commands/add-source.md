---
description: Add a new source to the aiml_wg JSON library from a PDF, URL, or PMC ID
---

Add a new source record to `aiml_wg/sources/` following the project schema.

## Arguments
`$ARGUMENTS` may contain: a file path to a PDF, a URL, a PMID, a PMC ID, or nothing (ask the user).

## Steps

**1. Identify the source**
If `$ARGUMENTS` is empty, ask: "What source should I add? Provide a file path, URL, PMID, or PMC ID."

**2. Determine source type and obtain content**
- PDF file path → use the Read tool to read it
- PMC ID (e.g. PMC12345) → fetch full text via `mcp__claude_ai_PubMed__get_full_text_article`
- PMID → fetch metadata via `mcp__claude_ai_PubMed__get_article_metadata`; try to get PMC full text if open access
- URL → fetch via WebFetch
- Always also run `mcp__claude_ai_PubMed__get_article_metadata` for any paper to get the canonical PMID/DOI/author list

**3. Check for duplicates**
Glob `aiml_wg/sources/**/*.json` and check whether any existing record has the same DOI or PMID. If a duplicate exists, tell the user and stop — suggest `/upgrade-source` instead.

**4. Determine schema fields**
Read `aiml_wg/sources/_schema.json` to confirm the current schema. Then extract:

- `id`: lowercase_authorlastname_year (e.g. `smith_2024`); if multiple first authors use primary only
- `source_type`: `paper` | `web` | `background` | `working_doc`
- `title`, `authors` (Last F format), `year`, `doi`, `pmid`, `url`, `journal_or_venue`
- `abstract_summary`: 3–5 sentence synthesis (not a copy of the abstract)
- `key_findings`: 5–8 bullet strings, each a complete sentence; emphasize quantitative results and novel claims
- `methods_discussed`: array of snake_case method names
- `datasets_referenced`: array of descriptive dataset names
- `tools_software`: array of tool names with versions where available
- `limitations`: array drawn from the paper's own Discussion section wherever possible
- `extracted_claims`: up to 6 direct quotes with `location` and `evidence_type` (`empirical` | `opinion` | `review` | `regulatory`)
- `numerical_findings`: up to 15 items; each needs `metric_type` (`performance_metric` | `effect_size` | `study_statistic` | `computational_metric` | `count`), `description`, `value` (always a string), optional `value_numeric`, `unit`, `comparison_baseline`, `location`, and `is_primary_finding` (boolean)
- `pillars`: one or more of `hybrid_foundations` | `uq_identifiability` | `optimal_control_rl` | `generative_ai`
- `relevance_score`: `high` | `medium` | `low`
- `gaps_addressed`: 2–4 bullet strings explaining what WG gap this source addresses
- `topics`: array of keyword strings
- `relationships`: `cites`, `cited_by`, `extends`, `contradicts` — IDs of other records in the library; check existing records for cross-references
- `how_obtained`: `pubmed_search` | `biorxiv_search` | `web_search` | `web_fetch` | `provided_by_user` | `background_doc`
- `read_depth`: `abstract_only` | `sections_key` | `full_text`
- `date_read`: today's date (YYYY-MM-DD)

**5. Determine target folder**

- `aiml_wg/sources/papers/` — peer-reviewed journal articles and preprints
- `aiml_wg/sources/web/` — web pages, guidance documents, SIG pages
- `aiml_wg/sources/background/` — broad survey or context documents
- `aiml_wg/sources/working_docs/` — internal WG documents

**6. Write the record**

Write to `aiml_wg/sources/{folder}/{id}.json`. Use the exact schema structure — do not add or omit top-level fields.

Apply these record-writing discipline rules before writing:

- **No hallucinated numerics.** Values in `numerical_findings` may only be written if they appear in the retrieved text. Omit any entry where the specific number is absent — do not estimate.
- **Tag inferred claims.** In `key_findings`, append `[inferred]` to any claim not explicitly stated in the source text.
- **State the evidence base in notes.** In `provenance.notes`, include a sentence describing what was read, e.g. `"Key findings from PubMed abstract only; numerical claims not independently confirmed."` or `"Full text read via PMC; all findings directly extracted."`
- **Apply the relevance_score rubric.** `high` = would justify a white paper citation or journal club session; `medium` = useful background; `low` = tangential. Do not default to high.

**7. Update index**
Read `aiml_wg/sources/index.json`. Append a new entry for this record with at minimum: `id`, `source_type`, `title`, `year`, `pillars`, `relevance_score`, `read_depth`. Write the updated index back.

**8. Update relationships in existing records**
For any existing record that should now reference this new record (e.g., it was already in `cites` of another record), read and update that record's `cited_by` or other relationship field to include the new `id`.

**9. Confirm**
Report: the new file path, `read_depth`, `relevance_score`, pillars, any cross-references updated, and confirmation that `index.json` was updated.
