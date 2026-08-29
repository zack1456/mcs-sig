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
| C-01b | active | Right-size Phase 1 for 3-person founding team | SK, ZK | Scope doc: `community/phase1_scope.md`; chair notes: `community/kickoff_facilitation_notes.md`. See DECISION-7. |
| C-02 | todo | Draft WG charter (mission, pillars, out-of-scope, membership, cadence) | SK, ZK | Blocked until C-01. Due: Month 2. Deliverable: `community/charter.md`. Mission one-liner drafted in `phase1_scope.md §6` |
| C-08 | todo | **Recruiting: grow 3 → 6+ active members by Month 2** (primary Phase 1 deliverable) | Owner TBD at kickoff | Channels + plan in `phase1_scope.md §4`. Tool = Scope & Call brief; funnel = journal club |
| C-09 | todo | Draft "Scope & Call for Participation" brief (2–4 pp) | SK | Recruiting magnet; becomes front half of scoping paper. See `phase1_scope.md §3a` |
| C-10 | todo | Draft technical seed note (conformal-prediction OR neural-ODE identifiability — pick one) | ZK or MC | `phase1_scope.md §3b`. Decided by kickoff Decisions 1 & 4 (MC expertise) |
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
| L-04 | done | Update WORKPLAN.md source library table | Antigravity | Table updated to reflect all 54 records (added 11 records on 2026-08-29) |

### Pillar 1 — Hybrid Models

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| M1.1 | todo | Architecture taxonomy: serial / parallel / embedded / surrogate / VAE-NLME / HDCM | WG lead TBD | Signal interest at kickoff. Includes population hierarchy (`elmokadem_2024`, `baaz_2026`). Notes: `methods/01_hybrid_models/architecture_notes.md` |
| M1.2 | todo | Structural identifiability of neural ODE components & shrinkage | WG lead TBD | Key sources: `campo_manzanares_2026` (iNODE), `janzen_2017` (NLME extension), `savic_2009_shrinkage` ($\eta$-shrinkage), `villaverde_2016_strikegodd`, `diazseoane_2023_strikegodd4`, `raue_2009`. Notes: `structural_identifiability_notes.md` |
| M1.3 | todo | Practical identifiability & numerical solver verification for hybrid models | WG lead TBD | Coordinate with SAUQ WG (see C-04). Key sources: `baran_gaburro_2026`, `kim_2021_stiff_node` (stiff Neural ODE solver stability), `najjar_2024_gsa`, `chenel_2026` |
| M1.4 | todo | When do hybrids help vs. hurt? (decision criteria) | WG lead TBD | Integrates M1.1–M1.3. Feeds white paper §B |

### Pillar 2 — UQ / Identifiability

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| M2.1 | todo | Bayesian UQ framework literature review for hybrid models | WG lead TBD | Key sources: `elmokadem_2024` (HDCM: Bayesian IIV+RUV+UQ for hybrid PK), `aslanimoghankou_2026` (neural SDEs + uncertainty), `baaz_2026` (VAE+neural ODE population PK) |
| M2.2 | todo | Conformal prediction in PK/PD — concept note (non-exchangeable / hierarchical) | WG lead TBD / ZK | **Confirmed white space in PMx**. Task: write 1–2 page concept note addressing longitudinal/clustered PK non-exchangeability (`dunn_2022_clustered_conformal`, `gibbs_2021_timeseries_conformal`, `barber_2023_conformal`) vs Bayesian UQ. Target: *CPT:PSP* Commentary or ISoP Memo. |
| M2.3 | todo | Ensemble uncertainty for pharmacometric applications | WG lead TBD | After M2.1 |
| M2.4 | todo | Comparative assessment of UQ methods | WG | Feeds white paper §C; connects to ASME V&V 40 (`kuemmel_2020_credibility`) |
| M2.5 | todo | Coordinate with SAUQ WG on overlapping scope | ZK | Depends on C-04 |

### Pillar 3 — RL / Optimal Control (lighter in Phase 1)

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| M3.1 | todo | Track RL dosing literature; contribute to scoping paper §C | WG liaison TBD | Signal interest at kickoff. DECISION-3 sets lighter bandwidth |
| M3.2 | todo | Identify Optimal Control WG liaison for joint paper (Phase 2) | ZK | Depends on C-04 |
| M3.6 | todo | Offline (Batch) RL & Off-Policy Evaluation (OPE) framework | WG liaison TBD | Added 2026-08-29 (Antigravity review). Key sources: `gottesman_2019_rl_healthcare`, `levine_2020_offline_rl`, `thomas_2016_ope`. Feeds regulatory & white paper |

### Pillar 4 — Generative AI (lighter in Phase 1)

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| M4.1 | todo | Physics-constrained generative models: literature scoping | WG lead TBD | Signal interest at kickoff. DECISION-4 scopes this first |
| M4.2 | todo | Mathematical & causal validation of synthetic data / digital twins | WG lead TBD | Added 2026-08-29 (Antigravity review). Key sources: `richens_2020_causal_med`, `sanchez_2022_causal_precision`, Pearl 2009. SCMs and counterfactual validity |
| M4.4 | todo | LLM failure modes in pharmacometrics — position paper scoping | WG lead TBD | Key sources: `shin_2024_llm`, `zheng_2025_llm`, `androulakis_2025_qsp`, `bejan_2026_iraegpt` |

### Deliverables — Scoping Paper

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| D-SC-A | todo | Scoping paper §A: landscape (what is AI/ML doing in pharmacometrics?) | WG lead TBD | Assign at kickoff. Key sources: `liu_2023`, `dermawan_2026`, `aiml_claude_background` |
| D-SC-B | todo | Scoping paper §B: pillar-by-pillar gap analysis | ZK + pillar leads | Depends on M1.1, M2.1, M3.1, M4.1 starting |
| D-SC-C | todo | Scoping paper §C: MCS differentiation vs. QSP/SxP/AI-ML SIG | SK | Key source: `zhang_2022`, `crosssig_fostvedt_2025` |
| D-SC-D | todo | Scoping paper §D: 18-month plan with milestones | SK, ZK | Already in WORKPLAN.md — synthesize |
| D-SC-E | todo | Scoping paper §E: regulatory context & ASME V&V 40 | ZK | Key sources: `liu_2023`, `fda_ai_guidance_2025`, `kuemmel_2020_credibility` |

### Regulatory

| ID | Status | Task | Owner | Notes / Dependencies |
| --- | --- | --- | --- | --- |
| R-01 | done | Check FDA AI/ML docket for open comment periods | ZK/Claude | **Resolved 2026-08-27:** comment period (Docket FDA-2024-D-4689) closed April 7, 2025; final guidance expected Q2 2026 (now finalized/imminent). No open docket. See DECISION-8. |
| R-02 | todo | Operationalize ASME V&V 40 + 7-step credibility framework + FDA–EMA Joint Principles | ZK + WG | Reframed per DECISION-8 & updated 2026-08-29 Antigravity review (`kuemmel_2020_credibility`). Untimed; folds into white-paper §E / D-SC-E. |

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
