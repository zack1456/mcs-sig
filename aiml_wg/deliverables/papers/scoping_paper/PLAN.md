# Deliverable · Scoping Paper (Internal Landscape Survey)

**What:** ~10-page internal landscape paper synthesizing the state of ML-MIDD, the regulatory context, and the gap analysis that justifies MCS WG's four pillars. This is a Phase 1 prerequisite — it informs the white paper and positions the WG with the ISoP steering committee.

**Audience:** ISoP MCS SIG steering committee; working group members
**Format:** Internal document (Word/PDF); not submitted to a journal
**Target:** Draft by Month 4 · Shared with steering committee Month 5

---

## Sub-tasks

### Authorship and structure
- [ ] Assign section leads at kickoff meeting
- [ ] Set review timeline: draft → internal review → steering committee version
- [ ] **Deliverable:** `drafts/scoping_paper_v1.docx`

### Section A — What hybrid mechanistic-ML models exist in pharmacometrics
- [ ] Draw on `methods/01_hybrid_models/` M1.1 working notes
- [ ] Cover: neural ODE, PBPK-ML surrogate, VAE for NLME, ML residual corrector
- [ ] Quantitative anchor: 560 ML-MIDD publications 2015–2025 (dermawan_2026); 22-fold growth
- [ ] Key sources: `dermawan_2026`, `baran_gaburro_2026`, `aiml_claude_background`

### Section B — Identifiability and UQ: where the field stands
- [ ] Draw on `methods/01_hybrid_models/` M1.2–M1.3 and `methods/02_uq/` M2.1–M2.3 working notes
- [ ] Key gap: no community standard for identifiability of neural ODE components; UQ approaches not compared
- [ ] Key sources: `baran_gaburro_2026`, `gerard_2025`, `aiml_claude_background`

### Section C — RL for precision dosing: state of the art
- [ ] Draw on `methods/03_rl_dosing/` M3.5 case study analysis
- [ ] Cover: Ribba 2023 framing, De Carlo 2024 (erdafitinib), De Carlo 2025 (givinostat)
- [ ] Key gap: no generalizable pharmacometric RL framework; computational cost barrier
- [ ] Key sources: `ribba_2023`, `de_carlo_2024`, `de_carlo_2025`

### Section D — Regulatory landscape
- [ ] FDA 7-step credibility framework (fda_ai_guidance_2025) — no mathematical operationalization yet
- [ ] FDA submission trend: 1 submission in 2016 → 132 in 2021 (liu_2023)
- [ ] No standalone regulatory ML-MIDD endorsement (dermawan_2026)
- [ ] Key sources: `fda_ai_guidance_2025`, `liu_2023`, `crosssig_fostvedt_2025`

### Section E — MCS gap analysis and four-pillar positioning
- [ ] Draw directly from `working_group_plan.md §2` gap analysis table
- [ ] Differentiate from AI/ML SIG (applied education), QSP SIG (QSP-specific credibility), SxP SubSIG (statistical ML)
- [ ] Articulate four pillars as MCS's answer to the documented gaps
- [ ] Key source: `crosssig_fostvedt_2025`, `mcs_wg_2026v03`

---

## Key sources
| Source | Section |
|---|---|
| `sources/papers/dermawan_2026.json` | A, D |
| `sources/papers/baran_gaburro_2026.json` | A, B |
| `sources/papers/gerard_2025.json` | B |
| `sources/papers/ribba_2023.json` | C |
| `sources/papers/de_carlo_2024.json` | C |
| `sources/papers/de_carlo_2025.json` | C |
| `sources/web/fda_ai_guidance_2025.json` | D |
| `sources/papers/liu_2023.json` | D |
| `sources/background/crosssig_fostvedt_2025.json` | D, E |
| `sources/working_docs/mcs_wg_2026v03.json` | E |

## Dependencies
- `community/` kickoff decisions: scope of hybrid models, RL priority, GenAI angle must be settled before Section E can be finalized
- Unblocks: `deliverables/papers/whitepaper_hybrid/` (Section A of white paper extends this)
