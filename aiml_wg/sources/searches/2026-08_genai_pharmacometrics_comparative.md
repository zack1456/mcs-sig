# Focused Search — Comparative Generative AI in Pharmacometrics

**Date:** 2026-08-29
**Purpose:** Identify empirical and regulatory sources supporting comparative activities for Claude, Codex, and Antigravity in PopPK, PBPK, QSP, synthetic-data validation, and model credibility.
**Search type:** Focused scoping search, not a systematic review.
**Sources searched:** PubMed, PMC, publisher pages, Crossref/OpenAlex metadata surfaced through web search, FDA, and EMA.

## Search concepts and exact queries

```text
site:pubmed.ncbi.nlm.nih.gov large language models pharmacometrics PBPK QSP benchmark 2024 2025
site:pubmed.ncbi.nlm.nih.gov large language model NONMEM pharmacokinetics 2024 2025
site:pubmed.ncbi.nlm.nih.gov generative AI synthetic clinical trial data pharmacometrics validation causal 2024 2025
site:pubmed.ncbi.nlm.nih.gov large language models systems pharmacology QSP 2024 2025
site:pubmed.ncbi.nlm.nih.gov pharmacometrics SBML model exchange reproducibility benchmark 2024 2025
site:pubmed.ncbi.nlm.nih.gov large language model scientific code uncertainty calibration benchmark 2024 2025
site:pubmed.ncbi.nlm.nih.gov large language models literature extraction biomedical causal knowledge graph evaluation 2024 2025
FDA artificial intelligence drug development guidance credibility model informed drug development synthetic data 2025
"PKGPT" pharmacometrics agentic NONMEM
site:pubmed.ncbi.nlm.nih.gov pharmacometrics model reproducibility code validation NLME 2024 2025
site:pubmed.ncbi.nlm.nih.gov drug drug interaction PBPK model qualification external validation 2024 2025
10.1002/psp4.70127 full text QSP-Copilot
10.1007/s10928-025-09982-7 full text NONMEM output interpretation
10.1007/s10928-024-09935-6 full text synthetic PK PD data
PMID 39748538 "Current Use of Physiologically Based Pharmacokinetic" DOI authors
10.1002/psp4.70021 full text
"Synthetic Data in Healthcare and Drug Development" full text
```

## Inclusion criteria

- Peer-reviewed empirical work directly evaluating an LLM or agentic workflow on pharmacometric/QSP tasks.
- Peer-reviewed synthetic-data work using PK/PD endpoints or pharmacometrics-specific validation.
- Primary regulator-authored analysis or official guidance defining PBPK/AI context-of-use credibility requirements.
- Sources that identify a testable failure mode, comparator, endpoint, or qualification criterion for M4.5.
- English-language sources with sufficient metadata and at least an abstract available.

## Exclusion criteria

- Molecular generation, target discovery, generic ADMET prediction, protocol drafting, or broad pharmaceutical AI reviews without a direct M4.5 evaluation endpoint.
- Commentary without an empirical benchmark or an authoritative regulatory framework.
- Duplicate preprint/version-of-record records; the version of record is preferred, with an accessible author preprint used only for detailed extraction when necessary.
- Sources already represented in the library, unless used for citation chaining or comparison.

## Included new records

- `saini_2025_qsp_copilot` — empirical evidence-to-QSP workflow; supports A8 precision/recall, provenance, variability, and expert-review endpoints.
- `cha_2025_nonmem_interpretation` — prior NONMEM-output interpretation and simulation benchmark; narrows the novelty claim for A6 and informs A7 failure cases.
- `jiang_2024_synthetic_pkpd` — synthetic PK/PD benchmark using ML, statistical, and pharmacometrics-specific metrics; supports A10.
- `pasculli_2025_synthetic_data_regulation` — terminology, provenance, and regulatory distinctions for synthetic data; supports A10 and A11.
- `ema_2025_pbpk_approvals` — regulator-authored analysis of PBPK intended uses and qualification outcomes; supports A9.

## Relevant records already in the library

- `kwack_2026_pkgpt` — closed-loop NONMEM execution, repair, plausibility, covariate-selection, and reproducibility gaps.
- `fda_ai_guidance_2025` — risk-based AI credibility assessment organized around context of use.
- `fda_ema_good_ai_principles_2026` — lifecycle, data-governance, transparency, and performance principles.
- `shin_2024_llm`, `zheng_2025_llm` — existing NONMEM code-generation benchmarks.
- `chen_2026_pbpkml` — PBPK/ML landscape and structure-generation white-space context.
- `scigym_2025`, `villaverde_2016_strikegodd`, `kim_2021_stiff_node` — QSP execution, identifiability, and hybrid neural-ODE verification anchors.

## Not included after screening

- `PharmaBench` — focuses on molecular ADMET benchmarks rather than pharmacometric model construction or verification.
- Broad AI/QSP and biomedical-RAG reviews — retained as background candidates but did not add a unique comparative endpoint beyond the included empirical sources.
- News and social-media reports about regulatory AI adoption — not primary evidence for the proposed benchmark.
- Preprint duplicates of published papers — used only to inspect accessible Methods/Results and not entered as separate library records.

## Citation chaining and metadata verification

- PubMed, PMC, publisher, and OpenAlex/Crossref-style metadata were compared for title, year, DOI, journal, and author consistency.
- QSP-Copilot and the EMA PBPK review were inspected through open full text.
- The Cha et al. published metadata were verified through PubMed; targeted Methods and Results were extracted from the openly accessible author preprint corresponding to the version of record.
- Pasculli et al. was inspected through open PMC full text.
- Jiang et al. remained abstract-only; an associated PAGE abstract was consulted for study-design context and is clearly identified in the source provenance.

## Search limitations and update rule

This was a focused scoping search, not PRISMA-compliant. Embase, Scopus, and Web of Science were not directly searched because subscription access was not available in this session. Before a journal submission, rerun the strategy in available bibliographic databases, record result counts and deduplication, perform formal backward/forward citation screening, and update model/product names because this literature changes rapidly.
