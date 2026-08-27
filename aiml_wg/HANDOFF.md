# Handoff

> **Instructions for any editor (human or LLM):** Read this file first. Update it when you finish a session — the "Current focus" and "Suggested next action" sections are the most important to keep current. Keep entries brief; commit history has the details.

---

## Last updated
**Date:** 2026-08-27
**By:** Claude (Sonnet 4.6) + Zack Kenz

---

## Current focus
Pre-kickoff preparation is complete. The kickoff meeting is **tomorrow, August 28, 2026**. No further pre-meeting work needed unless the user requests it.

After the meeting, the immediate focus shifts to:
1. Locking the 6 scoping decisions (update DECISIONS.md with confirmed stances)
2. Assigning pillar leads and workstream owners (update TASKS.md)
3. Drafting the WG charter (`community/charter.md`)

---

## What was completed this session
- `zhang_2022.json` upgraded from `abstract_only` → `full_text` (PDF provided by user; 14 pages read in full)
- `campo_manzanares_2026.json` created (`sections_key`, arXiv 2608.13044, iNODE framework)
- `zhang_2022` and `campo_manzanares_2026` added to `sources/index.json`
- `community/kickoff_agenda.md` written (90-min agenda with 6 scoping decisions + recommended stances)
- `community/kickoff_preread.md` written (~15-min participant pre-read)
- `TASKS.md`, `HANDOFF.md`, `DECISIONS.md` created (this session)
- `CLAUDE.md` updated to reference HANDOFF.md
- **Round 1 literature search completed** (9 new records, filling M1.1/M1.2/M2/M4.1 gaps):
  - `lu_2021` — first neural ODE for PK (trastuzumab emtansine, Genentech)
  - `raue_2009` — profile likelihood identifiability (structural vs. practical), foundational reference
  - `janssen_2024` — deep compartment models + physiological inductive biases (haemophilia A, SHAP)
  - `baaz_2026` — empirical Bayes VAE + neural ODE for population PK (CPT:PSP 2026)
  - `aslanimoghankou_2026` — latent neural SDEs for clinical time series + uncertainty calibration (J Biomed Inform)
  - `giacometti_2025` — neural ODE vs. NLME head-to-head on real dalbavancin PK data (218 patients)
  - `cminns_2024` — CMINNs with fractional calculus, Karniadakis/Brown (Comput Biol Med 2024)
  - `chhetri_2026` — CBINN with FIM-based structural + practical identifiability (Bull Math Biol 2026)
  - `upinn_2025` — UPINNs for chemotherapy drug action, gray-box ODE identification (Pharm Res 2025)
- `sources/index.json` updated to 25 records

---

## Blocked / waiting
- **C-01 (kickoff):** Meeting is tomorrow — all pre-meeting work done
- **C-02 (charter):** Can't draft until scoping decisions are locked at kickoff
- **L-01 (gerard_2025 upgrade):** Need PDF; PMID not yet retrieved
- **R-01 (FDA docket):** Time-sensitive — check whether the 2025 AI/ML draft guidance comment period is still open
- **M1.1–M4.4 (method workstreams):** All pending pillar lead assignment at kickoff
- **D-SC-A–E (scoping paper):** Pending section lead assignment at kickoff

---

## Key files to read first (for any new editor)
1. `CLAUDE.md` — project overview, terminology, domain context
2. This file (`HANDOFF.md`) — where we are and what's next
3. `TASKS.md` — full task list with status
4. `DECISIONS.md` — scoping decisions and rationale
5. `WORKPLAN.md` — 18-month milestone map and methods→deliverables mapping
6. `sources/index.json` — 25-record source library index

---

## Suggested next action
**Post-kickoff (after Aug 28):**
1. Update DECISIONS.md — change all 6 decisions from `tentative` to `confirmed` (or `revised` if the group changed a stance)
2. Update TASKS.md — fill in `Owner` fields for M1.1, M1.2, M2.1, D-SC-A after pillar leads are assigned
3. Mark C-01 as `done` in TASKS.md
4. Start C-02: draft `community/charter.md`

**Literature search Round 2 (when ready):** Deepen Pillar 1 and 3 coverage — PBPK-ML surrogates, ML covariate pharmacometrics, VAE for NLME, POMDP dosing, HJB optimal control, RL drug dosing case studies.

**Pre-kickoff remaining (Aug 27):**
- Check FDA comment docket (R-01) — potentially time-sensitive
- Retrieve PMID for gerard_2025 and upgrade to full_text if PDF is available

---

## Notes for LLMs
- The `.docx` primary planning document cannot be read by Claude Code tools — a `.txt` export exists at `aiml_wg/MCS SIG AI working group 2026v0.3.txt`; the JSON record is at `sources/working_docs/mcs_wg_2026v03.json`
- Source library schema is at `sources/_schema.json` — read before adding or editing any JSON record
- `read_depth` field must be one of: `abstract_only` | `sections_key` | `full_text`
- PMC full text fetch (`mcp__claude_ai_PubMed__get_full_text_article`) has a known parameter error — pass PMID as an array; even so it may fail for paywalled articles
- The 4 pillars: `hybrid_foundations` · `uq_identifiability` · `optimal_control_rl` · `generative_ai`
- Skills available: `/add-source`, `/upgrade-source`, `/search-add-pubmed`, `/prep-journal-club`
- Agents available: `source-consistency-checker`, `literature-discovery`
