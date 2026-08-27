# MCS SIG AI/ML Working Group — Workplan Overview

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

| Record | Status | Pillar |
| --- | --- | --- |
| `papers/baran_gaburro_2026` | full_text | 1, 2 |
| `papers/de_carlo_2024` | full_text | 3 |
| `papers/de_carlo_2025` | full_text | 3 |
| `papers/dermawan_2026` | full_text | 1, 2, 3, 4 |
| `papers/gerard_2025` | abstract_only | 1, 2 |
| `papers/liu_2023` | full_text | regulatory |
| `papers/ribba_2023` | full_text | 3 |
| `web/fda_ai_guidance_2025` | full_text | regulatory |
| `web/aiml_sig_page2026` | full_text | positioning |
| `background/cpt_moore_2019` | full_text | context |
| `background/crosssig_fostvedt_2025` | full_text | context |
| `background/aiml_claude_background` | full_text | 1, 2, 4 |
| `background/aiml_chatgpt_background` | full_text | 4 |
| `working_docs/mcs_wg_2026v03` | full_text | planning |

---

## Success metrics (18-month horizon)

- [ ] White paper submitted (Pillars 1+2)
- [ ] RL/optimal control framework paper submitted (Pillar 3)
- [ ] GenAI position paper preprint posted (Pillar 4)
- [ ] ACoP or PAGE session delivered
- [ ] FDA regulatory comment submitted
- [ ] ≥4 webinars delivered
- [ ] Cross-SIG coordination group established
- [ ] WG membership: 15+ active members
- [ ] Journal club: ≥6 sessions held
- [ ] Benchmarks repository with ≥2 datasets (stretch)
