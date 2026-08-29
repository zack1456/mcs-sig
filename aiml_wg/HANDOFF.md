# Handoff

<!-- Updated 2026-08-29 by Codex: reconciled current regulatory and source-library status; did not alter kickoff outcomes. -->

> **Instructions for any editor (human or LLM):** Read this file first. Update it when you finish a session — the "Current focus" and "Suggested next action" sections are the most important to keep current. Keep entries brief; commit history has the details.

---

## Last updated

**Date:** 2026-08-29 (Antigravity comprehensive scope review + literature additions)
**By:** Antigravity + Zack Kenz

---

## Current focus

Kickoff and founding-team execution. Confirmed reality: **3 active people** (co-chairs SK + ZK, plus one highly involved member MC); recruiting to grow the group over the next ~2 months. Phase 1 has been right-sized to that team.

**Read before the meeting:** `community/phase1_scope.md` (the operative near-term plan) and `community/kickoff_facilitation_notes.md` (chair run-of-show).

Key reframes:

1. **3 people = 1 pillar at depth** (Pillar 1) + 1 seed note, not 4 pillars. Growing to 6–8 members is the primary Phase 1 deliverable. (DECISION-7)
2. **Only Decisions 1 & 4 are genuinely open** at kickoff (depend on MC's expertise); 3/5/6 are forced by headcount; 2 is a fast default.
3. **8-week deliverables:** Scope & Call brief (SK), one technical seed note (ZK/MC), journal club as recruiting funnel (MC).
4. **FDA docket resolved (R-01):** comment period closed April 7, 2025; no open docket. Regulatory work reframed to untimed operationalization → white-paper §E and ASME V&V 40 integration. (DECISION-8)
5. **Literature & Method Additions (2026-08-29 Antigravity review):** 11 new peer-reviewed records added, integrating ASME V&V 40, non-exchangeable/hierarchical conformal prediction, offline RL/OPE, structural causal models, stiff ODE stability, and NLME $\eta$-shrinkage.

After the meeting: lock DECISIONS 1/4/7/8, name the recruiting owner (C-08), start the Scope & Call brief (C-09).

---

## What was completed this session (2026-08-29 Antigravity review)

- **13 new peer-reviewed sources created and indexed** in `sources/index.json` (bringing library to **56 records**):
  - `pkgpt_2026` (Pharmaceutics) — agentic closed-loop PopPK modeling in NONMEM
  - `scigym_2025` (NeurIPS) — benchmark for biological ODE discovery via LLM agents
  - `barber_2023_conformal` (Annals of Statistics) — non-exchangeable conformal prediction
  - `dunn_2022_clustered_conformal` (JASA) — clustered/hierarchical conformal prediction for longitudinal data
  - `gibbs_2021_timeseries_conformal` (NeurIPS) — adaptive conformal inference for time series
  - `gottesman_2019_rl_healthcare` (Nature Medicine) — clinical RL guidelines and OPE rationale
  - `levine_2020_offline_rl` (arXiv) — offline (batch) RL tutorial & algorithms
  - `thomas_2016_ope` (ICML) — data-efficient off-policy evaluation & safety bounds
  - `richens_2020_causal_med` (Nature) — causal machine learning in clinical decision support
  - `sanchez_2022_causal_precision` (Roy Soc Open Sci) — SCMs and counterfactual digital twins
  - `kuemmel_2020_credibility` (CPT:PSP) — ASME V&V 40 translation to MIDD credibility assessment
  - `kim_2021_stiff_node` (Chaos) — stiff Neural ODE solver stability & adjoint failure modes
  - `savic_2009_shrinkage` (AAPS J) — $\eta$-shrinkage diagnostics in population mixed-effects
- **Updated Method Plans (`methods/01_hybrid_models/`, `methods/02_uq/`, `methods/03_rl_dosing/`, `methods/04_generative_ai/`)**:
  - Pillar 1: Added population hierarchy (HDCM), $\eta$-shrinkage, stiff numerical verification, and software interoperability.
  - Pillar 2: Grounded conformal prediction in non-exchangeable / hierarchical longitudinal PK/PD data.
  - Pillar 3: Added Offline (Batch) RL and Off-Policy Evaluation (OPE) (M3.6).
  - Pillar 4: Added Structural Causal Models (SCMs) and counterfactual validation for synthetic data / digital twins.
- **Updated Regulatory Plan (`regulatory/PLAN.md`)**:
  - Integrated ASME V&V 40 alongside the FDA 7-step credibility framework; added numerical calculation verification.
- **Updated Phase 1 Scope (`community/phase1_scope.md`)**:
  - Refined Conformal Prediction seed note, specified dissemination channels (*CPT:PSP* Commentary / ISoP Memo), and expanded academic bridge recruitment (SIAM / SMB).
- **Updated Deliverables Plan (`deliverables/papers/whitepaper_hybrid/PLAN.md`)**:
  - Mapped all new foundations into Sections B, C, and E.

- `zhang_2022.json` upgraded from `abstract_only` → `full_text` (PDF provided by user; 14 pages read in full)
- `campo_manzanares_2026.json` created (`sections_key`, arXiv 2608.13044, iNODE framework)
- `zhang_2022` and `campo_manzanares_2026` added to `sources/index.json`
- `community/kickoff_agenda.md` written (90-min agenda with 6 scoping decisions + recommended stances)
- `community/kickoff_preread.md` written (~15-min participant pre-read)
- `TASKS.md`, `HANDOFF.md`, `DECISIONS.md` created (this session)
- `CLAUDE.md` updated to reference HANDOFF.md

**Round 1 literature search** (9 new records, filling M1.1/M1.2/M2/M4.1 gaps):

- `lu_2021` — first neural ODE for PK (trastuzumab emtansine, Genentech)
- `raue_2009` — profile likelihood identifiability (structural vs. practical), foundational reference
- `janssen_2024` — deep compartment models + physiological inductive biases (haemophilia A, SHAP)
- `baaz_2026` — empirical Bayes VAE + neural ODE for population PK (CPT:PSP 2026)
- `aslanimoghankou_2026` — latent neural SDEs for clinical time series + uncertainty calibration (J Biomed Inform)
- `giacometti_2025` — neural ODE vs. NLME head-to-head on real dalbavancin PK data (218 patients)
- `cminns_2024` — CMINNs with fractional calculus, Karniadakis/Brown (Comput Biol Med 2024)
- `chhetri_2026` — CBINN with FIM-based structural + practical identifiability (Bull Math Biol 2026)
- `upinn_2025` — UPINNs for chemotherapy drug action, gray-box ODE identification (Pharm Res 2025)

**Round 2 literature search** (4 new records + 3 full-text upgrades, filling M1.3 and M3 gaps):

- `karlsen_2025` — systematic review of pop PK covariate selection (SCM to AI), Sanofi + Montpellier, CPT:PSP 2025 (sections_key)
- `kekic_2026` — stochastic gates for ML covariate selection, AstraZeneca, CPT:PSP 2026 (full_text)
- `tosca_2024` — model-informed RL for precision dosing tutorial review, U Pavia, CPT 2024 (abstract_only)
- `irie_2025` — DQN for infliximab in pediatric Crohn's with real-world validation, Cincinnati Children's, CPT 2025 (full_text)
- `lu_2021` upgraded abstract_only → full_text (cross-regimen RMSE numbers, dosing-stop failure example, tools)
- `janssen_2024` upgraded abstract_only → full_text (neural-ODE WORST on sparse data: RMSE 19.5 vs multi-branch DCM 13.0, divergence rates)
- `giacometti_2025` upgraded abstract_only → full_text (data augmentation required, KS test results, SHAP interpretation)

`sources/index.json` updated to 29 records.

**Round 3 literature search** (5 new records, filling regulatory/cross-SIG gaps):

- `chenel_2026` — PBPK best practices + ICH M15 regulatory framework, Pharmetheus/Bayer/Novartis/Sanofi, CPT:PSP 2026 (full_text); documents EMA gap in PBPK quality vs. regulatory expectations
- `goryanin_2025` — AI+QSP integration: surrogate modeling, virtual patients, digital twins, regulatory acceptance; U Edinburgh/InSysBio, Drug Discovery Today 2025 (abstract_only, paywalled)
- `krishna_2025` — state-of-the-art MIDD for pediatric rare diseases; 6 FDA approval case studies; AI future directions (synthetic controls, digital twins, generative AI); Certara/Sarepta/Takeda, CPT:PSP 2025 (sections_key, full_text retrieved PMC12625129)
- `dette_2025` — digital twin systematic review (16 studies): no paper yet achieves true DT; generative DTs (GDTs) as next step; QSP model accepted as FDA confirmatory evidence (rADAMTS13); Saarland University, CSBJ 2025 (sections_key, full_text retrieved PMC12703978)
- `chen_2024_amd` — AMD automated pop PK model builder in Pharmpy (open-source); AMD models lower BIC than published; Uppsala/Karlsson group, CPT:PSP 2024 (abstract_only, PMC11494844 available)
- `janssen_2024` cited_by updated to add `dette_2025`

`sources/index.json` updated to 34 records.

**Round 4 literature search** (6 new records, filling M2.1/M4.4/M1.2/UQ work stream gaps):

- `elmokadem_2024` — HDCM: hierarchical deep compartment modeling; Bayesian IIV + RUV + UQ via NUTS/Turing.jl; extends DCM line; Metrum Research Group, CTS 2024 (full_text, PMC11473376); M2.1
- `shin_2024_llm` — ChatGPT 4.0 + Gemini Ultra 1.0 for NONMEM coding: LLMs generate templates but contain errors; non-reproducible; U Buffalo, JPKPD 2024 (abstract_only, paywalled); M4.4
- `androulakis_2025_qsp` — QSP SIG's AI/ML vision: four-task taxonomy (mining → surrogates/DTs → network inference → hybrid); LLMs as 'active partner'; all 7 authors are ISoP QSP SIG members; JPKPD 2025 (full_text, PMC12170689); cross-SIG competitive intelligence
- `najjar_2024_gsa` — GSA tutorial for OSP Suite PBPK: Morris + Sobol + EFAST R package with GUI; WHO IPCS regulatory formatting; OAT vs. GSA discrepancy demonstrated empirically; Edginton group, CPT:PSP 2024 (full_text, PMC11646943); M2.x Sobol gap
- `janzen_2017` — Structural identifiability for NLME mixed-effects models: extends Taylor series + input-output form to mixed-effects; foundational M1.2 paper; AstraZeneca + Warwick (Chappell group), Math Biosci 2017 (abstract_only, paywalled)
- `bejan_2026_iraegpt` — irAE-GPT: GPT-4o zero-shot for pharmacovigilance irAE detection; 442 patients across 3 institutions + 7 clinical trials; causal attribution failure documented; Vanderbilt + Roche, EBioMedicine 2026 (abstract_only, PMC13174231 available); M4.4
- `shin_2024_llm` cited_by updated: `androulakis_2025_qsp` cites it (confirmed from full text)

`sources/index.json` updated to 40 records.

**Round 5 literature search** (4 new records, following up on identified gaps):

- `zheng_2025_llm` — 7 LLMs × 13 NONMEM tasks + scoring rubric + optimized prompt; o1/gpt-4.1 near-perfect accuracy with optimized prompt; extends shin_2024_llm; UNC + Monash, CPT:PSP 2025 (abstract_only, PMC12706393 available); M4.4
- `villaverde_2016_strikegodd` — original STRIKE-GOLDD paper: structural identifiability via Lie derivatives + observability for nonlinear ODE models; foundational M1.2 tool reference; U Oxford + U Vigo (Villaverde, Papachristodoulou), PLoS Comp Biol 2016 (abstract_only, PMC5085250 available)
- `diazseoane_2023_strikegodd4` — STRIKE-GOLDD 4.0 update: ProbObsTest algorithm (faster for rational models) + GUI; U Vigo (Villaverde group), Bioinformatics 2023 (abstract_only, PMC9805590 available)
- Note: `shin_2024_llm` cited_by extended by `zheng_2025_llm`; `villaverde_2016_strikegodd` cited_by `diazseoane_2023_strikegodd4`

`sources/index.json` updated to 43 records.

**Confirmed PubMed dead ends (not indexable via PubMed):**

- Classical optimal control for PK (Pontryagin/HJB) — exists in J. Math. Biol., Bull. Math. Biol., SIAM journals, not PubMed-indexed under these terms
- Conformal prediction for pharmacometrics — zero results across multiple search strategies; confirmed white space in the field
- Synthetic data/GAN/VAE for virtual patients in drug development — PubMed query expansion makes these searches intractable
- These are genuine frontier opportunities for MCS SIG WG, not gaps to fill with existing papers

---

## Blocked / waiting

- **C-01 (kickoff):** Meeting is tomorrow — all pre-meeting work done
- **C-02 (charter):** Can't draft until scoping decisions are locked at kickoff
- **L-01 (gerard_2025 upgrade):** Need PDF; PMID not yet retrieved
- **R-01 (FDA docket):** Resolved. The comment period closed April 7, 2025; the January 2025 guidance remains draft as of 2026-08-29. Monitor through the regulatory workstream rather than treating it as a time-bound deliverable.
- **M1.1–M4.4 (method workstreams):** All pending pillar lead assignment at kickoff
- **D-SC-A–E (scoping paper):** Pending section lead assignment at kickoff

---

## Key files to read first (for any new editor)

1. `CLAUDE.md` — project overview, terminology, domain context
2. This file (`HANDOFF.md`) — where we are and what's next
3. `TASKS.md` — full task list with status
4. `DECISIONS.md` — scoping decisions and rationale
5. `WORKPLAN.md` — 18-month milestone map and methods→deliverables mapping
6. `sources/index.json` — 54-record source library index

---

## What was completed this session (2026-08-29 Claude session)

- **Comparative activity plans generated** for Claude × Codex × Antigravity across 6 pharma modeling tasks (Pop PK NONMEM, failure mode elicitation, PBPK structure, hybrid neural ODE, QSP ODE + identifiability, model diagnostics). Both Claude and Antigravity have generated independent scoping plans; Claude's is at `methods/04_generative_ai/comparative_activities_scoping_claude.md`.
- **M4.5 workstream added** to `methods/04_generative_ai/PLAN.md` with task IDs M4.5-A1 through M4.5-A6 and open design questions (Antigravity/Codex identity, prompt engineering policy, expert panel).
- **2 new source records added** to library (now 56 records): `kwack_2026_pkgpt` (human benchmarking data; V2 plausibility failure) and `chen_2026_pbpkml` (ML+PBPK white-space confirmation).

---

## Suggested next action

**Post-kickoff (after Aug 28) — PRIMARY PRIORITY:**

1. Update DECISIONS.md — change all 6 decisions from `tentative` to `confirmed` (or `revised` if the group changed a stance)
2. Update TASKS.md — fill in `Owner` fields for M1.1, M1.2, M2.1, D-SC-A after pillar leads are assigned
3. Mark C-01 as `done` in TASKS.md
4. Start C-02: draft `community/charter.md`

**Literature search status:** 63 indexed records. The library now includes focused evidence on external validation/transportability, clinical offline-RL OPE, MIDD documentation, final ICH M15, and the FDA–EMA AI principles. `sources/index.json` is authoritative.

**Round 4 coverage summary by work stream:**

- M2.1 (Bayesian DL for PK): filled by `elmokadem_2024` (HDCM, Metrum)
- M4.4 (LLMs for pharmacometrics): filled by `shin_2024_llm` + `androulakis_2025_qsp` + `bejan_2026_iraegpt`
- M2.x (GSA/Sobol for PBPK): filled by `najjar_2024_gsa`
- M1.2 (structural identifiability for NLME): filled by `janzen_2017`
- Cross-SIG intelligence: `androulakis_2025_qsp` documents QSP SIG's AI/ML roadmap

**Remaining open items:**

- Check FDA comment docket (R-01) — potentially time-sensitive
- Retrieve PMID for gerard_2025 and upgrade to full_text if PDF is available
- chen_2024_amd full text available at PMC11494844 — upgrade from abstract_only if useful
- goryanin_2025 paywalled — upgrade from abstract_only if PDF obtained

---

## Notes for LLMs

- The `.docx` primary planning document cannot be read by Claude Code tools — a `.txt` export exists at `aiml_wg/MCS SIG AI working group 2026v0.3.txt`; the JSON record is at `sources/working_docs/mcs_wg_2026v03.json`
- Source library schema is at `sources/_schema.json` — read before adding or editing any JSON record
- `read_depth` field must be one of: `abstract_only` | `sections_key` | `full_text`
- PMC full text fetch (`mcp__claude_ai_PubMed__get_full_text_article`) has a known parameter error — pass PMID as an array; even so it may fail for paywalled articles
- The 4 pillars: `hybrid_foundations` · `uq_identifiability` · `optimal_control_rl` · `generative_ai`
- Skills available: `/add-source`, `/upgrade-source`, `/search-add-pubmed`, `/prep-journal-club`
- Agents available: `source-consistency-checker`, `literature-discovery`
