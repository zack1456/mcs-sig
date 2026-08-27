# Deliverable · White Paper: Mathematical Foundations of Hybrid Mechanistic-ML PK/PD Models

**What:** Flagship WG publication establishing mathematical criteria for hybrid mechanistic-ML pharmacometric models — identifiability, UQ, validation, and regulatory alignment. Covers Pillars 1 and 2.

**Target journal:** CPT: Pharmacometrics & Systems Pharmacology *or* Journal of Pharmacokinetics and Pharmacodynamics
**Model:** QSP SIG's 2022 "Two heads are better than one" white paper in scope and ambition
**Timeline:** Outline Month 7 · First draft Month 10 · Preprint Month 12 · Submitted Month 15

---

## Sub-tasks

### Setup
- [ ] Agree section structure (see below) at kickoff or dedicated paper meeting
- [ ] Assign section leads — one per section, drawn from WG members + external co-authors
- [ ] Identify 1–2 academic co-authors from SIAM Life Sciences or SMB for identifiability sections
- [ ] Set internal review schedule and target journal

### Section A — Taxonomy of hybrid architectures
*Draws from `methods/01_hybrid_models/` M1.1*
- [ ] Four architecture types: serial, parallel (residual corrector), embedded (neural ODE), surrogate
- [ ] Pharmacometric examples for each type
- [ ] Decision guide: which architecture for which pharmacometric problem?

### Section B — Structural and practical identifiability
*Draws from `methods/01_hybrid_models/` M1.2 and M1.3*
- [ ] Classical identifiability theory: what it guarantees, how neural components disrupt it
- [ ] Practical identifiability: profile likelihood, sensitivity analysis for hybrid models
- [ ] The "when hybrids help" criterion: formalize Baran & Gaburro's empirical finding mathematically
- [ ] Coordinate with SAUQ WG to avoid duplication (see `methods/02_uq/` M2.5)

### Section C — UQ approaches and comparative assessment
*Draws from `methods/02_uq/` M2.1–M2.4*
- [ ] Bayesian, conformal, and ensemble methods: mathematical properties side-by-side
- [ ] Pharmacometric context criteria for method selection (sample size, model complexity, regulatory need)
- [ ] Map to FDA model risk framework: how does UQ quantify "model influence"?

### Section D — Validation and benchmarking
*Draws from `methods/01_hybrid_models/` M1.4 and `benchmarks/`*
- [ ] Identifiability-aware validation metrics (beyond RMSE)
- [ ] Criteria: prediction accuracy, identifiability, UQ calibration, computational cost, documentation quality
- [ ] Illustrative examples using benchmark datasets from `benchmarks/` (if available by draft deadline)

### Section E — Regulatory alignment
*Draws from `methods/02_uq/` M2.4 and `regulatory/`*
- [ ] Map paper framework to FDA 7-step credibility assessment (fda_ai_guidance_2025)
- [ ] Operationalize "Context of Use" for hybrid PMx models
- [ ] Quantify "model risk = model influence × decision consequence" for ML components
- [ ] Position relative to QSP SIG credibility WG: complementary, not duplicative

### Review and submission
- [ ] First draft: Month 10
- [ ] Internal WG review: Month 11
- [ ] External review (1 FDA contact, 1 academic mathematician): Month 11–12
- [ ] Preprint (bioRxiv): Month 12
- [ ] Revision: Month 13–14
- [ ] Journal submission: Month 15

---

## Key sources
| Source | Section(s) |
|---|---|
| `sources/papers/baran_gaburro_2026.json` | A, B, D |
| `sources/papers/dermawan_2026.json` | A, D (landscape context, hybrid PBPK) |
| `sources/papers/gerard_2025.json` | B, D (black-box limitations) |
| `sources/web/fda_ai_guidance_2025.json` | C, E |
| `sources/papers/liu_2023.json` | E (regulatory stakes) |
| `sources/background/aiml_claude_background.json` | A, B |
| `sources/background/crosssig_fostvedt_2025.json` | E (positioning) |

## Dependencies
- `methods/01_hybrid_models/` working notes: M1.1–M1.4 → Sections A–B–D
- `methods/02_uq/` working notes: M2.1–M2.4 → Section C; M2.5 (SAUQ coordination) → Section B
- `deliverables/papers/scoping_paper/` — scoping paper Section A provides the literature foundation for Section A here
- `benchmarks/` — evaluation criteria needed for Section D examples (can use placeholder if benchmarks not ready)
- `community/` kickoff: scope decisions must be locked before Section A is written

## Open questions
- [ ] Target CPT:PSP (pharmacometrics audience) or JPKPD (more mathematical)?
- [ ] Are Pillars 1 and 2 one white paper or two papers? One is recommended for efficiency and impact; split only if content exceeds journal limits
- [ ] SAUQ WG co-authorship on Section C — yes or no? Decide at Month 6
