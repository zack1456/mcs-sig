# Methods · Hybrid Mechanistic-ML Models (Pillar 1)

**What this folder is:** Working notes, literature synthesis, and mathematical development for hybrid mechanistic-ML PK/PD models — the raw intellectual content that feeds into `deliverables/papers/whitepaper_hybrid/`.

**Scope:** Serial, parallel, and embedded (neural ODE) hybrid architectures in pharmacometric models. Identifiability of ML components. When hybrid augmentation helps vs. hurts.

---

## Method workstreams

### M1.1 — Hybrid architecture taxonomy
*What kinds of hybrids exist and when does each apply?*

- [ ] **Serial:** ML as covariate generator → feeds mechanistic ODE (e.g., ML predicts CL from omics)
- [ ] **Parallel (residual corrector):** Mechanistic ODE runs first; ML corrects residuals
- [ ] **Embedded (neural ODE):** Neural network replaces or augments ODE right-hand side
- [ ] **Surrogate:** ML approximates a computationally expensive mechanistic submodel (e.g., PBPK surrogate)
- [ ] **VAE for NLME:** Variational autoencoder jointly estimates parameters and selects covariates

For each: identify pharmacometric examples in the literature, articulate decision criteria

Key sources: `dermawan_2026` (neural PBPK surrogate for 106 drugs; VAE for NLME), `baran_gaburro_2026` (hybrid PK/PD with digital biomarkers)

**Working notes file:** `architecture_notes.md`

---

### M1.2 — Structural identifiability of hybrid models
*When is a hybrid model structurally identifiable — i.e., can its parameters be uniquely determined even with perfect infinite data?*

- [ ] Review classical structural identifiability methods (differential algebra, transfer function, Taylor series)
- [ ] Map classical theory to neural ODE components: where does it break?
  - Neural components introduce redundancy: multiple weight configurations give identical input-output behavior
  - Key claim: *"neural components are generally nonidentifiable due to redundancy"* (arXiv 2608.13044)
- [ ] What can be done? Regularization strategies, architectural constraints (e.g., monotonic nets), reduced parameterizations
- [ ] Distinguish: identifiability of mechanistic ODE parameters vs. identifiability of neural component weights

**Working notes file:** `structural_identifiability_notes.md`

---

### M1.3 — Practical identifiability for hybrid models
*Given real (finite, noisy) data, can we reliably estimate the parameters?*

- [ ] Profile likelihood for hybrid model parameters — feasible at what scales?
- [ ] Sensitivity analysis (GSA) for ML-augmented models: which parameters matter?
- [ ] Connection to SAUQ WG methods — coordinate, don't duplicate
- [ ] Practical criteria: when is adding an ML layer justified given N patients and T timepoints?
- [ ] The Baran & Gaburro finding: *"When mechanistic models fit well and sample sizes are small, adding an ML layer risks overfitting without measurable gain"* — formalize this as a criterion

Key source: `baran_gaburro_2026`

**Working notes file:** `practical_identifiability_notes.md`

---

### M1.4 — When do hybrids help vs. hurt?
*Mathematical criteria for deciding whether to augment a mechanistic model with ML*

- [ ] Collect empirical evidence from literature: cases where hybrid outperformed pure mechanistic, and cases where it didn't
- [ ] Formal criterion candidates:
  - Model misspecification test: does mechanistic residual have exploitable structure?
  - Sample size threshold: minimum N for reliable hybrid estimation
  - Regularization requirement: what penalty is needed to prevent overfitting?
- [ ] This becomes the practical decision framework published in the white paper

**Working notes file:** `hybrid_decision_criteria.md`

---

## Key sources
| Source | Workstream |
|---|---|
| `sources/papers/baran_gaburro_2026.json` | M1.2, M1.3, M1.4 |
| `sources/papers/dermawan_2026.json` | M1.1 (surrogate, VAE for NLME) |
| `sources/papers/gerard_2025.json` | M1.4 (black-box limitations) |
| `sources/background/aiml_claude_background.json` | M1.1, M1.2 (NeuralODE survey) |

## Feeds into deliverables
- `deliverables/papers/whitepaper_hybrid/` — Sections A (M1.1) and B (M1.2, M1.3, M1.4)
- `benchmarks/` — evaluation criteria for M1.3 (identifiability metrics)
- `deliverables/conferences/webinars/` — Webinar 1 content
