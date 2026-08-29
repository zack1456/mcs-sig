# Methods · Uncertainty Quantification for AI/ML-Pharmacometrics (Pillar 2)

**What this folder is:** Working notes and mathematical development for UQ methods applied to hybrid mechanistic-ML PK/PD models. Feeds into `deliverables/papers/whitepaper_hybrid/` Section C, and into `benchmarks/` evaluation criteria.

**Scope:** Bayesian, conformal, and ensemble UQ methods — assessed for their mathematical properties and pharmacometric applicability. Coordinated with (not duplicating) SAUQ WG.

---

## Method workstreams

### M2.1 — Bayesian UQ for hybrid models
*What does posterior uncertainty mean when a model has both ODE parameters and neural network weights?*

- [ ] Posterior inference for mechanistic ODE parameters (e.g., CL, Vd): established via NLME / MCMC
- [ ] Posterior inference for neural component weights: intractable for large networks; approximations needed
  - Laplace approximation
  - Variational inference (ELBO)
  - MCMC for small neural components (feasible for 1–3 hidden layers)
- [ ] How to propagate uncertainty from neural weights through ODE solution to PK/PD predictions
- [ ] What does a credible interval on a hybrid model prediction actually certify?

**Working notes file:** `bayesian_uq_notes.md`

---

### M2.2 — Conformal prediction for ML components
*Distribution-free, finite-sample coverage guarantees — can these apply to pharmacometric hybrid models?*

- [ ] Conformal prediction basics: coverage guarantee regardless of model and data distribution
- [ ] **The Non-Exchangeability Challenge in PK/PD:** <!-- Added 2026-08-29 (Antigravity review) --> Standard split conformal requires strict exchangeability ($i.i.d.$); pharmacometric data violate this via longitudinal autocorrelation and dosing cohort shifts (`barber_2023_conformal`)
- [ ] **Clustered & Hierarchical Conformal Prediction:** <!-- Added 2026-08-29 (Antigravity review) --> Apply group-level and clustered conformal prediction (`dunn_2022_clustered_conformal`) where patients are exchangeable clusters with repeated internal measures
- [ ] **Adaptive Conformal Inference for Longitudinal Time-Series:** <!-- Added 2026-08-29 (Antigravity review) --> Dynamic non-conformity threshold updating (`gibbs_2021_timeseries_conformal`) for PK concentration time-series trajectories
- [ ] Advantage over Bayesian: distribution-free valid coverage without prior specification on neural network weights
- [ ] Key open question: what does 90% conformal coverage mean for an individual patient's dosing bounds? Translating finite-sample coverage to regulatory and clinical risk guarantees

Key sources: `barber_2023_conformal`, `dunn_2022_clustered_conformal`, `gibbs_2021_timeseries_conformal`

**Working notes file:** `conformal_notes.md`

---

### M2.3 — Ensemble methods
*Epistemic vs. aleatoric uncertainty separation via ensembles*

- [ ] Deep ensembles: train N instances of hybrid model; variance = epistemic uncertainty
- [ ] MC Dropout: stochastic forward passes as approximate posterior samples
- [ ] Pharmacometric calibration: does ensemble spread match observed prediction error?
- [ ] Comparison to Bayesian: ensembles are computationally cheaper; are coverage properties similar?
- [ ] When to use: large sample sizes where MCMC is intractable; covariate-sparse regions

**Working notes file:** `ensemble_notes.md`

---

### M2.4 — Comparative assessment
*Which UQ method is appropriate when — a pharmacometrician's decision guide*

- [ ] Build comparison table: method × (pharmacometric context criteria)
  - Criteria: sample size, model complexity, regulatory acceptability, computational cost, coverage guarantee type
- [ ] Regulatory context: which UQ approach maps most naturally to FDA 7-step credibility assessment and "model influence" quantification? (Connecting to ASME V&V 40 and `kuemmel_2020_credibility`)
- [ ] This becomes the core contribution of white paper Section C

Key source: `fda_ai_guidance_2025` (model risk = influence × consequence; how does UQ inform "influence"?), `kuemmel_2020_credibility`

**Working notes file:** `uq_comparison_table.md`

---

### M2.5 — Coordination with SAUQ WG
*Avoid duplicating SAUQ WG's existing UQ work; identify the AI/ML-specific gap*

- [ ] Inventory what SAUQ WG has produced: methods for sensitivity analysis and UQ in mechanistic PMx models
- [ ] Identify the AI/ML-specific gap: SAUQ methods assume mechanistic model structure; what breaks when a neural component is added?
- [ ] Formalize the distinction: SAUQ = UQ for mechanistic models; MCS AI/ML WG = UQ for ML components *within* mechanistic models
- [ ] Decide: formal co-authorship on white paper Section C with SAUQ WG members, or coordination only?

**Working notes file:** `sauq_coordination_notes.md`

---

## Key sources
| Source | Workstream | Added / Role |
|---|---|---|
| `sources/papers/baran_gaburro_2026.json` | M2.1 | UQ in hybrid model context |
| `sources/papers/elmokadem_2024.json` | M2.1 | Bayesian IIV+RUV with NUTS MCMC |
| `sources/papers/barber_2023_conformal.json` | M2.2 | Added 2026-08-29 (Antigravity review): Non-exchangeable conformal prediction |
| `sources/papers/dunn_2022_clustered_conformal.json` | M2.2 | Added 2026-08-29 (Antigravity review): Clustered/hierarchical conformal prediction |
| `sources/papers/gibbs_2021_timeseries_conformal.json` | M2.2 | Added 2026-08-29 (Antigravity review): Time-series adaptive conformal inference |
| `sources/papers/kuemmel_2020_credibility.json` | M2.4 | Added 2026-08-29 (Antigravity review): ASME V&V 40 MIDD credibility framework |
| `sources/web/fda_ai_guidance_2025.json` | M2.4 | Model influence quantification |
| `sources/background/aiml_claude_background.json` | M2.1–M2.3 | UQ survey |

## Feeds into deliverables
- `deliverables/papers/whitepaper_hybrid/` — Section C
- `benchmarks/` — UQ calibration metrics (coverage probability, interval sharpness)
- `deliverables/conferences/webinars/` — Webinar 2 content
