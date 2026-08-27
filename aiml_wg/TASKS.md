# MCS SIG AI/ML WG — Task List

**How to use:**
- `Status`: `todo` · `active` · `blocked` · `done`
- `Owner`: initials or role (SK = Shreyas Chakravarty, ZK = Zack Kenz, WG = working group, Claude = AI assistant)
- Edit this file directly; keep IDs stable (they cross-reference PLAN.md files and DECISIONS.md)
- Update HANDOFF.md whenever you change status on an active task

---

## Phase 1 (Months 1–6)

### Community & Governance

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| C-01 | active | Kickoff meeting (Aug 28 2026) — resolve 6 scoping decisions, assign pillar leads | SK, ZK | Agenda: `community/kickoff_agenda.md`; pre-read: `community/kickoff_preread.md` |
| C-02 | todo | Draft WG charter (mission, pillars, out-of-scope, membership, cadence) | SK, ZK | Blocked until C-01. Due: Month 2. Deliverable: `community/charter.md` |
| C-03 | todo | Submit charter to ISoP MCS SIG steering committee | SK | Blocked until C-02 |
| C-04 | todo | Schedule cross-SIG alignment meetings (AI/ML SIG, QSP SIG, SxP, Optimal Control WG, SAUQ WG) | ZK | Blocked until C-01. See `community/PLAN.md` for specific scope boundary per SIG |
| C-05 | todo | Journal club: confirm format (sync/async) and launch Month 3 | WG | First session: `baran_gaburro_2026`. Deliverable: `community/journal_club/schedule.md` |
| C-06 | todo | MCS SIG website: create WG page | SK | Due: Month 6. URL: https://sites.google.com/view/mcssig/ |

### Source Library

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| L-01 | active | Upgrade `gerard_2025` from abstract_only to full_text | ZK/Claude | Need PDF. PMID unknown — check PubMed for Gérard et al. 2025 AI in PK/PD/pharmacovigilance |
| L-02 | done | Run `/literature-discovery` agent across all 4 pillars | Claude | Completed through 5 systematic rounds (PubMed); 43-record library covers all 4 pillars + regulatory context + identifiability tools |
| L-03 | done | Add campo_manzanares_2026 cross-references once it cites or is cited by other library records | Claude | No PubMed-traceable citations yet; noted in provenance |
| L-04 | done | Update WORKPLAN.md source library table | Claude | Table updated to reflect all 43 records |

### Pillar 1 — Hybrid Models

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| M1.1 | todo | Architecture taxonomy: serial / parallel / embedded / surrogate / VAE-NLME | WG lead TBD | Signal interest at kickoff. Working notes: `methods/01_hybrid_models/architecture_notes.md` |
| M1.2 | todo | Structural identifiability of neural ODE components | WG lead TBD | Key sources: `campo_manzanares_2026` (iNODE), `janzen_2017` (NLME extension), `villaverde_2016_strikegodd` (STRIKE-GOLDD method), `diazseoane_2023_strikegodd4` (current tool), `raue_2009` (profile likelihood). Notes: `structural_identifiability_notes.md` |
| M1.3 | todo | Practical identifiability for hybrid models (profile likelihood, GSA) | WG lead TBD | Coordinate with SAUQ WG (see C-04). Key sources: `baran_gaburro_2026`, `najjar_2024_gsa` (GSA for PBPK, OSP Suite), `chenel_2026` (regulatory GSA requirements) |
| M1.4 | todo | When do hybrids help vs. hurt? (decision criteria) | WG lead TBD | Integrates M1.1–M1.3. Feeds white paper §B |

### Pillar 2 — UQ / Identifiability

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| M2.1 | todo | Bayesian UQ framework literature review for hybrid models | WG lead TBD | Key sources: `elmokadem_2024` (HDCM: Bayesian IIV+RUV+UQ for hybrid PK), `aslanimoghankou_2026` (neural SDEs + uncertainty), `baaz_2026` (VAE+neural ODE population PK) |
| M2.2 | todo | Conformal prediction in PK/PD — concept note | WG lead TBD | **Confirmed white space**: zero papers found across 3 PubMed search strategies. Task: write a 1–2 page concept note answering (1) what conformal prediction is, (2) where it fits relative to profile likelihood (raue_2009) and Bayesian UQ (elmokadem_2024), (3) what a PK/PD application would look like. This note becomes the seed of a WG-original contribution, not a literature synthesis. |
| M2.3 | todo | Ensemble uncertainty for pharmacometric applications | WG lead TBD | After M2.1 |
| M2.4 | todo | Comparative assessment of UQ methods | WG | Feeds white paper §C |
| M2.5 | todo | Coordinate with SAUQ WG on overlapping scope | ZK | Depends on C-04 |

### Pillar 3 — RL / Optimal Control (lighter in Phase 1)

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| M3.1 | todo | Track RL dosing literature; contribute to scoping paper §C | WG liaison TBD | Signal interest at kickoff. DECISION-3 sets lighter bandwidth |
| M3.2 | todo | Identify Optimal Control WG liaison for joint paper (Phase 2) | ZK | Depends on C-04 |

### Pillar 4 — Generative AI (lighter in Phase 1)

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| M4.1 | todo | Physics-constrained generative models: literature scoping | WG lead TBD | Signal interest at kickoff. DECISION-4 scopes this first |
| M4.4 | todo | LLM failure modes in pharmacometrics — position paper scoping | WG lead TBD | Key sources: `shin_2024_llm` (ChatGPT/Gemini for NONMEM — errors persist), `zheng_2025_llm` (7 LLMs × 13 tasks — o1/gpt-4.1 near-perfect with optimized prompt), `androulakis_2025_qsp` (QSP SIG AI/ML vision, LLM framing), `bejan_2026_iraegpt` (GPT-4o pharmacovigilance — causal attribution failure). Capability trajectory steep 2024→2025; failure modes now concentrated in complex models + causal reasoning |

### Deliverables — Scoping Paper

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| D-SC-A | todo | Scoping paper §A: landscape (what is AI/ML doing in pharmacometrics?) | WG lead TBD | Assign at kickoff. Key sources: `liu_2023`, `dermawan_2026`, `aiml_claude_background` |
| D-SC-B | todo | Scoping paper §B: pillar-by-pillar gap analysis | ZK + pillar leads | Depends on M1.1, M2.1, M3.1, M4.1 starting |
| D-SC-C | todo | Scoping paper §C: MCS differentiation vs. QSP/SxP/AI-ML SIG | SK | Key source: `zhang_2022`, `crosssig_fostvedt_2025` |
| D-SC-D | todo | Scoping paper §D: 18-month plan with milestones | SK, ZK | Already in WORKPLAN.md — synthesize |
| D-SC-E | todo | Scoping paper §E: regulatory context | ZK | Key sources: `liu_2023`, `fda_ai_guidance_2025` |

### Regulatory

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| R-01 | active | Check FDA AI/ML docket for open comment periods | ZK/Claude | **Potentially time-sensitive.** Guidance published 2025; comment window may still be open |
| R-02 | todo | Draft FDA comment (if docket open) | ZK + WG | Due: Month 10. Depends on R-01 |

---

## Phase 2 (Months 7–12)

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| D-WP-A | todo | White paper outline agreed; author roles assigned | SK, ZK | Month 7. Feeds Pillars 1+2 |
| D-WP-B | todo | ACoP session proposal submitted | WG | Month 8. Blocked until C-02 (charter) |
| D-RL-A | todo | RL framework paper: joint with Optimal Control WG | WG + OC WG | Month 10–11 draft |
| D-WP-C | todo | White paper first draft | WG | Month 10–11 |
| D-WP-D | todo | White paper preprint posted | WG | Month 12 |
| C-07 | todo | Cross-SIG hub established (quarterly coordination meetings) | SK | Month 12. Depends on C-04 progressing |

---

## Phase 3 (Months 13–18)

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| D-GEN-A | todo | GenAI position paper preprint | WG | Month 14. Depends on C-04 (cross-SIG scope agreement) |
| D-WP-E | todo | White paper submitted to journal | WG | Month 15 |
| D-RL-B | todo | RL framework paper submitted | WG + OC WG | Month 15 |
| BM-01 | todo | Benchmarks repo (stretch): ≥2 datasets, reproducible eval | WG | Month 15+. DECISION-6 defers this |

---

## Done

| ID | Task | Completed |
| --- | --- | --- |
| L-done-1 | Source library initial build (10 records) | 2026-08 |
| L-done-2 | Upgrade `de_carlo_2024` to full_text | 2026-08 |
| L-done-3 | Upgrade `liu_2023` to full_text | 2026-08 |
| L-done-4 | Upgrade `mcs_wg_2026v03` to full_text | 2026-08 |
| L-done-5 | Upgrade `zhang_2022` to full_text | 2026-08-27 |
| L-done-6 | Add `campo_manzanares_2026` (sections_key) | 2026-08-26 |
| L-done-7 | Fix `index.json` (add liu_2023, fix dermawan_2026 pillars) | 2026-08-26 |
| L-done-8 | Round 1 literature search — 9 records (lu_2021, raue_2009, janssen_2024, baaz_2026, aslanimoghankou_2026, giacometti_2025, cminns_2024, chhetri_2026, upinn_2025) | 2026-08-27 |
| L-done-9 | Round 2 literature search — 4 records + 3 full-text upgrades (karlsen_2025, kekic_2026, tosca_2024, irie_2025; upgraded lu_2021, janssen_2024, giacometti_2025) | 2026-08-27 |
| L-done-10 | Round 3 literature search — 5 records (chenel_2026, goryanin_2025, krishna_2025, dette_2025, chen_2024_amd) | 2026-08-27 |
| L-done-11 | Round 4 literature search — 6 records (elmokadem_2024, shin_2024_llm, androulakis_2025_qsp, najjar_2024_gsa, janzen_2017, bejan_2026_iraegpt) | 2026-08-27 |
| L-done-12 | Round 5 literature search — 3 records (zheng_2025_llm, villaverde_2016_strikegodd, diazseoane_2023_strikegodd4); confirmed 3 white spaces (conformal prediction, Pontryagin OC, synthetic data/GANs) | 2026-08-27 |
| REPO-1 | Repo structure (methods/deliverables/benchmarks/community/regulatory) | 2026-08 |
| REPO-2 | WORKPLAN.md | 2026-08 |
| REPO-3 | All method and deliverable PLAN.md files | 2026-08 |
| REPO-4 | Skills (add-source, upgrade-source, search-add-pubmed, prep-journal-club) | 2026-08 |
| REPO-5 | Agents (source-consistency-checker, literature-discovery) | 2026-08 |
| C-done-1 | Kickoff agenda drafted (`community/kickoff_agenda.md`) | 2026-08-26 |
| C-done-2 | Kickoff pre-read drafted (`community/kickoff_preread.md`) | 2026-08-26 |
