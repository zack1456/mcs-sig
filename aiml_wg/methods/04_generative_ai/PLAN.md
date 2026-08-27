# Methods · Generative AI: Mathematical Foundations for Pharmacometrics (Pillar 4)

**What this folder is:** Working notes and mathematical development for MCS's distinctive contribution to GenAI in pharmacometrics — physics constraints, synthetic data validation, and LLM failure modes. Feeds into `deliverables/papers/genai_position/`.

**Out of scope here (handled by AI/ML SIG or QSP SIG):** LLM literature mining, AI coding workflows, molecular generative design, trial protocol drafting by GenAI.

---

## Method workstreams

### M4.1 — Physics-constrained generative models
*Forcing generative models to respect mechanistic PK/PD constraints*

**What constraints matter in pharmacometrics?**
- [ ] Mass balance: compartmental PK (amount in = amount out + amount eliminated)
- [ ] Dose-response monotonicity: efficacy should be non-decreasing in dose within therapeutic range
- [ ] Physiological plausibility bounds: Vd ∈ [0.04, 100] L/kg; CL ∈ [0, 300] L/h/70kg; F ∈ [0,1]
- [ ] Identifiability of generated model code: generated ODE systems must be structurally identifiable
- [ ] Non-negativity: concentrations, amounts, and doses must be ≥ 0

**Enforcement strategies — by model type:**
- [ ] **VAEs:** constraint as regularization term in ELBO (penalize constraint violations in latent space); physics-informed decoder
- [ ] **Diffusion models:** constraint projection at each denoising step; classifier guidance toward constraint-satisfying region
- [ ] **LLM-generated ODE code:** post-generation verification (automated constraint checker); constrained decoding (token-level filtering)

**Research agenda:**
- [ ] Formalize each constraint type mathematically
- [ ] Assess what is tractable to enforce (mass balance: easy; identifiability: hard)
- [ ] Identify existing physics-constrained generation literature (physics-informed neural networks, PINN) and map to pharmacometrics

**Working notes file:** `physics_constraints_notes.md`

---

### M4.2 — Mathematical validation of synthetic pharmacometric data
*Criteria for certifying that synthetic patients / synthetic control arms are pharmacologically valid*

**Why standard statistical tests are insufficient:**
- [ ] A synthetic patient population can have correct marginal distributions on PK parameters but incorrect joint correlations (e.g., CL and Vd are biologically correlated via body weight)
- [ ] A synthetic control arm can pass distributional tests but have unrealistic dose-response trajectories

**Proposed validation framework:**
- [ ] *Statistical layer:* Maximum Mean Discrepancy (MMD), Wasserstein distance between synthetic and real distributions
- [ ] *Pharmacological layer:* dose-response shape preservation, PK parameter correlation structure, variability decomposition (BSV vs. RUV)
- [ ] *Identifiability layer:* are synthetic datasets informative enough to identify the generating model's parameters? (Fisher information criterion)
- [ ] *Regulatory layer:* does synthetic data meet FDA's definition of acceptable external control? (Map to `fda_ai_guidance_2025`)

**Case study material:**
- De Carlo 2024: 141 virtual patients (96 + 45) — how were they validated? What criteria were used?
- De Carlo 2025: 98 virtual patients per set, 10 test sets — population-level replication vs. individual-level validation

**Working notes file:** `synthetic_data_validation_notes.md`

---

### M4.3 — LLM failure mode taxonomy for pharmacometric model building
*When and why do LLMs produce mathematically or pharmacologically invalid PK/PD models*

**Failure mode categories:**
- [ ] **Structural errors:** wrong compartment connections (e.g., elimination from wrong compartment); missing first-pass effect; incorrect absorption lag
- [ ] **Identifiability violations:** overparameterized ODE systems where two parameters are confounded — LLMs don't flag this
- [ ] **Unit inconsistencies:** parameter values with incompatible units (e.g., CL in L/h vs. mL/min mixed in same model)
- [ ] **Non-conservation of mass:** generated ODE where amounts don't sum correctly across compartments
- [ ] **Sign errors:** positive feedback where negative is pharmacologically required; wrong sign on elimination term
- [ ] **Plausibility errors:** generated parameter values outside physiological range (Vd = 0.001 L/kg, CL = 500 L/h)

**Approach:**
- [ ] Generate illustrative examples of each failure mode using Claude / GPT-4 (can construct these deliberately)
- [ ] Design an automated checker: given an LLM-generated ODE system, flag each category
- [ ] Assess: how often do these failures occur? Are they model-specific or prompt-dependent?
- [ ] This is directly actionable for the community — tool could be released with the paper

**Working notes file:** `llm_failure_modes_notes.md`

---

### M4.4 — Scope differentiation memo
*One-page document clarifying MCS's GenAI lane relative to other SIGs*

- [ ] Write before paper outline is locked (needs cross-SIG alignment from `community/`)
- [ ] Table format: topic × (MCS lead / AI-ML SIG lead / QSP SIG lead / out of scope)
- [ ] Use this to write the position paper's scope statement and abstract

**Working notes file:** `scope_differentiation.md`

---

## Key sources
| Source | Workstream |
|---|---|
| `sources/papers/dermawan_2026.json` | M4.1 (VAE for NLME, neural PBPK surrogate) |
| `sources/background/aiml_claude_background.json` | M4.1, M4.3 (GenAI survey) |
| `sources/background/aiml_chatgpt_background.json` | M4.1 (pharma R&D GenAI landscape) |
| `sources/papers/de_carlo_2024.json` | M4.2 (virtual patient validation) |
| `sources/papers/de_carlo_2025.json` | M4.2 (virtual patient validation) |
| `sources/web/fda_ai_guidance_2025.json` | M4.2 (regulatory criteria for synthetic data) |

## Feeds into deliverables
- `deliverables/papers/genai_position/` — all workstreams
- `deliverables/conferences/webinars/` — Webinar 4 content
- `deliverables/papers/whitepaper_hybrid/` — Section D (synthetic data in benchmark validation)
