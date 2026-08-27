---
description: Search PubMed by keyword or PMID and add matching papers as new source records
---

Search PubMed and add one or more results as new source records in `aiml_wg/sources/papers/`.

## Arguments
`$ARGUMENTS` is either:
- A PMID or list of PMIDs (e.g. `35707940` or `35707940 40325832`)
- A keyword search string (e.g. `neural ODE pharmacokinetics identifiability`)
- Nothing → ask the user for a query

## Steps

**1. Parse arguments**
If `$ARGUMENTS` looks like one or more integers, treat as PMID(s). Otherwise treat as a keyword search.

**2a. PMID path**
For each PMID, call `mcp__claude_ai_PubMed__get_article_metadata` with that PMID.

**2b. Keyword search path**
Call `mcp__claude_ai_PubMed__search_articles` with `$ARGUMENTS` as the query. Use `max_results: 10` and `sort: relevance`. Present the results to the user (title, authors, year, journal, PMID) and ask which ones to add. Wait for user selection before proceeding.

**3. Duplicate check**
For each selected paper, glob `aiml_wg/sources/**/*.json` and check all existing records for a matching `doi` or `pmid`. If a match exists, skip that paper and tell the user (suggest `/upgrade-source` if it's `abstract_only`).

**4. Attempt full text**
For each new paper, try `mcp__claude_ai_PubMed__get_full_text_article` using the PMID. If full text is returned, set `read_depth: "full_text"`. If only metadata is available, set `read_depth: "abstract_only"` and note the paywall or access limitation.

**5. Create records**
For each paper, extract all schema fields (same as `/add-source` step 4). Determine relevance to WG pillars:

| Pillar | Key indicators in abstract/title |
|---|---|
| `hybrid_foundations` | neural ODE, hybrid mechanistic-ML, PBPK-ML, NLME, identifiability |
| `uq_identifiability` | uncertainty quantification, conformal, Bayesian, sensitivity analysis, structural identifiability |
| `optimal_control_rl` | reinforcement learning, Q-learning, MDP, optimal control, precision dosing, adaptive dosing |
| `generative_ai` | generative model, VAE, diffusion, LLM, synthetic data, physics-constrained |

**6. Check cross-references**
For each new paper, scan its reference list (if full text was obtained) for DOIs/titles matching existing library records. Add appropriate `cites` entries and update `cited_by` in referenced records.

**7. Write records**
Write each new record to `aiml_wg/sources/papers/{id}.json`.

**8. Confirm**
Report a table: paper, PMID, read_depth achieved, pillars assigned, and any cross-references linked.
