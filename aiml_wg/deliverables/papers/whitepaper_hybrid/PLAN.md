# Deliverable · White Paper: Mathematical Foundations of Hybrid Mechanistic-ML PK/PD Models

<!-- Updated 2026-08-29 by Codex: added transportability, decision-validation, reproducibility, and credibility-package scope. -->

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

### Section B — Structural and practical identifiability & numerical stability
*Draws from `methods/01_hybrid_models/` M1.2 and M1.3*
- [ ] Classical identifiability theory: what it guarantees, how neural components disrupt it
- [ ] Population-level identifiability & $\eta$-shrinkage: <!-- Added 2026-08-29 (Antigravity review) --> how ML layers interact with random effects and mask misspecification (`janzen_2017`, `savic_2009_shrinkage`)
- [ ] Practical identifiability: profile likelihood, sensitivity analysis for hybrid models
- [ ] Numerical verification: <!-- Added 2026-08-29 (Antigravity review) --> stiff ODE solver stability and adjoint gradient reliability (`kim_2021_stiff_node`)
- [ ] The "when hybrids help" criterion: formalize Baran & Gaburro's empirical finding mathematically
- [ ] Coordinate with SAUQ WG to avoid duplication (see `methods/02_uq/` M2.5)

### Section C — UQ approaches and comparative assessment
*Draws from `methods/02_uq/` M2.1–M2.4*
- [ ] Bayesian (NUTS MCMC, HDCM; `elmokadem_2024`), hierarchical/non-exchangeable conformal prediction (`dunn_2022_clustered_conformal`, `barber_2023_conformal`), and ensemble methods: mathematical properties side-by-side <!-- Added 2026-08-29 (Antigravity review) -->
- [ ] Pharmacometric context criteria for method selection (sample size, model complexity, regulatory need)
- [ ] Map to FDA model risk framework: how does UQ quantify "model influence" under ASME V&V 40? (`kuemmel_2020_credibility`)

### Section D — Validation and benchmarking
*Draws from `methods/01_hybrid_models/` M1.4 and `benchmarks/`*
- [ ] Identifiability-aware validation metrics (beyond RMSE)
- [ ] Criteria: prediction accuracy, identifiability, UQ calibration, computational cost, documentation quality
- [ ] Transportability: pre-specified temporal/external cohorts, applicability-domain or shift diagnostics, and subgroup reporting where relevant to the COU
- [ ] Decision relevance: when the model informs dosing, include decision-level safety and utility/regret metrics rather than accuracy alone
- [ ] Reproducibility: record solver tolerance/convergence, software/model versions, seeds, data lineage, and compute environment
- [ ] Illustrative examples using benchmark datasets from `benchmarks/` (if available by draft deadline)

### Section E — Regulatory alignment
*Draws from `methods/02_uq/` M2.4 and `regulatory/`*
- [ ] Map paper framework to ASME V&V 40 standard and FDA 7-step credibility assessment (`fda_ai_guidance_2025`, `kuemmel_2020_credibility`) <!-- Added 2026-08-29 (Antigravity review) -->
- [ ] Operationalize "Context of Use" for hybrid PMx models
- [ ] Quantify "model risk = model influence × decision consequence" for ML components
- [ ] Position relative to QSP SIG credibility WG: complementary, not duplicative
- [ ] Release the `regulatory/credibility_package/` templates as a practical companion to the paper

### Review and submission
- [ ] First draft: Month 10
- [ ] Internal WG review: Month 11
- [ ] External review (1 FDA contact, 1 academic mathematician): Month 11–12
- [ ] Preprint (bioRxiv): Month 12
- [ ] Revision: Month 13–14
- [ ] Journal submission: Month 15

---

## Key sources
| Source | Section(s) | Added / Role |
|---|---|---|
| `sources/papers/baran_gaburro_2026.json` | A, B, D | Hybrid PK/PD baseline |
| `sources/papers/dermawan_2026.json` | A, D | Landscape context, hybrid PBPK |
| `sources/papers/gerard_2025.json` | B, D | Black-box limitations |
| `sources/papers/elmokadem_2024.json` | A, B, C | Bayesian HDCM |
| `sources/papers/savic_2009_shrinkage.json` | B | Added 2026-08-29 (Antigravity review): $\eta$-shrinkage diagnostics |
| `sources/papers/kim_2021_stiff_node.json` | B | Added 2026-08-29 (Antigravity review): Stiff Neural ODE stability |
| `sources/papers/barber_2023_conformal.json` | C | Added 2026-08-29 (Antigravity review): Non-exchangeable conformal |
| `sources/papers/dunn_2022_clustered_conformal.json` | C | Added 2026-08-29 (Antigravity review): Clustered conformal |
| `sources/papers/kuemmel_2020_credibility.json` | C, E | Added 2026-08-29 (Antigravity review): ASME V&V 40 for MIDD |
| `sources/web/fda_ai_guidance_2025.json` | C, E | FDA 7-step credibility framework |
| `sources/papers/liu_2023.json` | E | Regulatory stakes |
| `sources/background/aiml_claude_background.json` | A, B | NeuralODE survey |
| `sources/background/crosssig_fostvedt_2025.json` | E | Positioning |

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
