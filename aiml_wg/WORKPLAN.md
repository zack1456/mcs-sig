# MCS SIG AI/ML Working Group — Workplan Overview

<!-- Updated 2026-08-29 by Codex: reconciled source count and replaced the obsolete FDA-comment success metric. -->

*See `working_group_plan.md` for full strategic context, gap analysis, and positioning.*

---

## Structure

```text
methods/          intellectual content development — one folder per method area (Pillars 1–4)
deliverables/     output packaging — papers/ and conferences/ subfolders
benchmarks/       reproducible evaluation repository (stretch goal)
community/        governance, journal club, cross-SIG coordination
regulatory/       FDA comment, guidance monitoring
sources/          structured JSON source library (schema: sources/_schema.json)
background/       raw PDFs
```

The **methods/** folders are where the math gets worked out; **deliverables/** folders are where that content is assembled into papers and presentations. A method workstream feeds multiple deliverables without those deliverables duplicating working content.

---

## Methods → Deliverables mapping

| Method folder | Primary deliverable | Also feeds |
| --- | --- | --- |
| `methods/01_hybrid_models/` | `deliverables/papers/whitepaper_hybrid/` §A–B | `benchmarks/`, `deliverables/conferences/webinars/` Webinar 1 |
| `methods/02_uq/` | `deliverables/papers/whitepaper_hybrid/` §C | `benchmarks/`, `deliverables/conferences/webinars/` Webinar 2 |
| `methods/03_rl_dosing/` | `deliverables/papers/rl_framework/` | `deliverables/conferences/webinars/` Webinar 3, `regulatory/` |
| `methods/04_generative_ai/` | `deliverables/papers/genai_position/` | `deliverables/conferences/webinars/` Webinar 4 |

---

## 18-month milestone summary

| Month | Milestone |
| --- | --- |
| 1–2 | Kickoff · Charter approved · Scoping decisions locked |
| 3 | Journal club starts · Cross-SIG alignment meetings scheduled |
| 4 | Scoping paper draft circulated internally |
| 5–6 | Cross-SIG alignment memos signed · WG website page live |
| 7 | White paper and RL framework paper outlines agreed; author roles assigned |
| 8 | ACoP 2026/2027 proposal submitted · GenAI paper scope confirmed (cross-SIG memo prerequisite) |
| 10 | FDA comment draft (if docket open — check immediately) |
| 10–11 | White paper and RL framework first drafts |
| 12 | FDA comment submitted · Cross-SIG hub established · White paper preprint |
| 14 | GenAI position paper preprint · Webinar series launches |
| 15 | White paper submitted · RL framework paper submitted |
| 15+ | Benchmarks launch (if resourced) |

---

## Source library status

**Authoritative record: `sources/index.json` (63 records as of 2026-08-29).** The table below is a summary; `index.json` is the ground truth.

### Background & Context

| Record | Status | Pillar |
| --- | --- | --- |
| `background/cpt_moore_2019` | full_text | context |
| `background/crosssig_fostvedt_2025` | full_text | context |
| `background/aiml_claude_background` | full_text | 1, 2, 4 |
| `background/aiml_chatgpt_background` | full_text | 4 |
| `working_docs/mcs_wg_2026v03` | full_text | planning |
| `web/fda_ai_guidance_2025` | full_text | regulatory |
| `web/aiml_sig_page2026` | full_text | positioning |

### Pillar 1 — Hybrid Mechanistic-ML Models

| Record | Status | Notes |
| --- | --- | --- |
| `papers/baran_gaburro_2026` | full_text | Hybrid PK/PD review + digital biomarkers |
| `papers/dermawan_2026` | full_text | Bibliometric review ML-MIDD 2015–2025 |
| `papers/gerard_2025` | abstract_only | AI in PK/PD/pharmacovigilance review |
| `papers/zhang_2022` | full_text | QSP+ML white paper (QSP SIG 2022) |
| `papers/lu_2021` | full_text | First neural ODE for PK (trastuzumab emtansine) |
| `papers/janssen_2024` | full_text | Deep compartment models + physiological constraints; neural-ODE underperforms on sparse data |
| `papers/elmokadem_2024` | full_text | HDCM: Bayesian IIV+RUV+UQ for hybrid PK (Metrum) |
| `papers/baaz_2026` | sections_key | VAE + neural ODE for population PK |
| `papers/giacometti_2025` | full_text | Neural ODE vs. NLME head-to-head (dalbavancin, 218 patients) |
| `papers/cminns_2024` | sections_key | CMINNs with fractional calculus (Karniadakis group) |
| `papers/upinn_2025` | sections_key | UPINNs for chemotherapy drug action |
| `papers/campo_manzanares_2026` | sections_key | iNODE: identifiability-aware neural ODEs |
| `papers/kim_2021_stiff_node` | sections_key | Stiff neural ODEs and solver stability (Added 2026-08-29 Antigravity) |
| `papers/savic_2009_shrinkage` | full_text | Importance of eta-shrinkage in NLME empirical Bayes (Added 2026-08-29 Antigravity) |

### Pillar 1 — Covariate Selection & Automation

| Record | Status | Notes |
| --- | --- | --- |
| `papers/karlsen_2025` | sections_key | Systematic review: pop PK covariate selection SCM→AI |
| `papers/kekic_2026` | full_text | Stochastic gates for ML covariate selection (AstraZeneca) |
| `papers/chen_2024_amd` | abstract_only | AMD automated pop PK in Pharmpy (Uppsala) |

### Pillar 2 — UQ / Identifiability

| Record | Status | Notes |
| --- | --- | --- |
| `papers/raue_2009` | sections_key | Profile likelihood: structural vs. practical identifiability |
| `papers/chhetri_2026` | sections_key | CBINN with FIM-based identifiability analysis |
| `papers/aslanimoghankou_2026` | sections_key | Neural SDEs for clinical time series + uncertainty calibration |
| `papers/janzen_2017` | abstract_only | Structural identifiability for NLME mixed-effects models |
| `papers/villaverde_2016_strikegodd` | abstract_only | STRIKE-GOLDD: Lie derivative identifiability method |
| `papers/diazseoane_2023_strikegodd4` | abstract_only | STRIKE-GOLDD 4.0: ProbObsTest + GUI |
| `papers/najjar_2024_gsa` | full_text | GSA tutorial for OSP Suite PBPK: Morris, Sobol, EFAST |
| `papers/chenel_2026` | full_text | PBPK best practices + ICH M15 regulatory framework |
| `papers/barber_2023_conformal` | sections_key | Conformal prediction beyond exchangeability (Added 2026-08-29 Antigravity) |
| `papers/dunn_2022_clustered_conformal` | sections_key | Distribution-free prediction sets for clustered data (Added 2026-08-29 Antigravity) |
| `papers/gibbs_2021_timeseries_conformal` | sections_key | Adaptive conformal inference for time series (Added 2026-08-29 Antigravity) |
| `papers/kuemmel_2020_credibility` | full_text | ASME V&V 40 credibility assessment for MIDD (Added 2026-08-29 Antigravity) |

### Pillar 3 — RL / Optimal Control

| Record | Status | Notes |
| --- | --- | --- |
| `papers/de_carlo_2024` | full_text | RL + PK-PD for erdafitinib |
| `papers/de_carlo_2025` | full_text | RL + PK-PD for givinostat (polycythemia vera) |
| `papers/ribba_2023` | full_text | RL as innovative model-based approach (dosing, digital health) |
| `papers/tosca_2024` | abstract_only | Model-informed RL for precision dosing: tutorial review |
| `papers/irie_2025` | full_text | DQN for infliximab in pediatric Crohn's (real-world validation) |
| `papers/gottesman_2019_rl_healthcare` | sections_key | Guidelines for RL in healthcare & OPE rationale (Added 2026-08-29 Antigravity) |
| `papers/levine_2020_offline_rl` | sections_key | Offline reinforcement learning tutorial & review (Added 2026-08-29 Antigravity) |
| `papers/thomas_2016_ope` | sections_key | Data-efficient off-policy policy evaluation (Added 2026-08-29 Antigravity) |

### Pillar 4 — Generative AI / LLMs

| Record | Status | Notes |
| --- | --- | --- |
| `papers/dette_2025` | sections_key | Digital twin systematic review; generative DTs |
| `papers/goryanin_2025` | abstract_only | AI+QSP: surrogate models, virtual patients, QSPaaS |
| `papers/krishna_2025` | sections_key | MIDD for pediatric rare diseases; digital twins + synthetic controls |
| `papers/shin_2024_llm` | abstract_only | ChatGPT/Gemini for NONMEM (2024 baseline; errors persist) |
| `papers/zheng_2025_llm` | abstract_only | 7 LLMs × 13 NONMEM tasks; o1/gpt-4.1 near-perfect with optimized prompt |
| `papers/androulakis_2025_qsp` | full_text | QSP SIG AI/ML vision: LLMs as active partner (cross-SIG intel) |
| `papers/bejan_2026_iraegpt` | abstract_only | GPT-4o for pharmacovigilance irAE detection (Vanderbilt+Roche) |
| `papers/richens_2020_causal_med` | sections_key | Improving medical diagnosis with causal ML (Added 2026-08-29 Antigravity) |
| `papers/sanchez_2022_causal_precision` | sections_key | Causal ML and counterfactual digital twins (Added 2026-08-29 Antigravity) |

### Regulatory & Cross-Cutting

| Record | Status | Notes |
| --- | --- | --- |
| `papers/liu_2023` | full_text | FDA landscape: AI/ML in regulatory submissions 2016–2021 |

---

## Success metrics (18-month horizon)

- [ ] White paper submitted (Pillars 1+2)
- [ ] RL/optimal control framework paper submitted (Pillar 3)
- [ ] GenAI position paper preprint posted (Pillar 4)
- [ ] ACoP or PAGE session delivered
- [ ] Credibility Evidence Package v1 published and maintained
- [ ] ≥4 webinars delivered
- [ ] Cross-SIG coordination group established
- [ ] WG membership: 15+ active members
- [ ] Journal club: ≥6 sessions held
- [ ] Benchmarks repository with ≥2 datasets (stretch)
