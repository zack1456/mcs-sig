---
description: Upgrade an existing abstract_only or sections_key source record to full_text using a provided PDF or PMC full text
---

Upgrade an existing source record in `aiml_wg/sources/` from `abstract_only` or `sections_key` to `full_text`.

## Arguments
`$ARGUMENTS` may contain a source ID (e.g. `gerard_2025`), a file path to a PDF, or both. If empty, ask the user for the source ID and/or the file to read.

## Steps

**1. Identify the record**
If a source ID is given, read `aiml_wg/sources/papers/{id}.json` (or the appropriate subfolder). If no ID given, ask the user.

**2. Check current read_depth**
If `read_depth` is already `full_text`, tell the user and ask whether they want to re-extract anyway (e.g. to correct errors).

**3. Obtain the full text**
Priority order:
1. PDF file path in `$ARGUMENTS` → Read tool
2. If record has a PMC ID in its notes or can be inferred from PMID → `mcp__claude_ai_PubMed__get_full_text_article`
3. If record has a URL → WebFetch
4. Ask the user to provide the file

**4. Re-extract all content fields**
With the full text in hand, update or populate every field that was absent or shallow in the original record:
- `abstract_summary` — revise to reflect full-paper understanding, not just the abstract
- `key_findings` — expand to 5–8 items including results from Methods, Results, and Discussion
- `methods_discussed` — add any methods not visible from the abstract
- `datasets_referenced` — add any datasets mentioned in Methods
- `tools_software` — add software with version numbers from Methods
- `limitations` — extract directly from the Discussion section (not inferred)
- `extracted_claims` — add up to 6 direct quotes; include at least 1 from Discussion or Conclusion
- `numerical_findings` — add all quantitative results from tables and figures; aim for 5–10 items; mark primary findings correctly

**5. Update provenance**
- Set `read_depth` to `full_text`
- Update `how_obtained` to `provided_by_user` if a PDF was provided
- Update `date_read` to today
- Append to `notes` describing what changed (e.g. "Upgraded from abstract_only; full text read from PDF provided by user.")

**6. Check for new relationships**
Reading the full paper's reference list often reveals connections to existing library records. Add any newly discovered `cites` entries; update the referenced records' `cited_by` accordingly.

**7. Write the updated record**
Write back to the same file path. Preserve all fields that were already correct.

**8. Confirm**
Report: updated `read_depth`, count of numerical_findings before and after, any new relationships added, and any fields that remain incomplete.
