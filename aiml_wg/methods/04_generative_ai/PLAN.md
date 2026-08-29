# Methods · Generative AI: Mathematical Foundations for Pharmacometrics (Pillar 4)

**What this folder is:** Working notes and mathematical development for MCS's distinctive contribution to GenAI in pharmacometrics — physics constraints, synthetic data validation, and LLM failure modes. Feeds into `deliverables/papers/genai_position/`.

**Out of scope here (handled by AI/ML SIG or QSP SIG):** open-ended LLM literature discovery/mining, general AI coding workflows, molecular generative design, and trial protocol drafting by GenAI. M4.5-A8 is deliberately narrower: MCS evaluates the traceable mathematical translation of a locked, jointly curated evidence packet into an effect diagram and ODE model; literature discovery remains with the AI/ML SIG and biological adjudication with the QSP SIG.

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

### M4.2 — Mathematical validation of synthetic pharmacometric data & digital twins
*Criteria for certifying that synthetic patients / synthetic control arms are pharmacologically and causally valid*

**Why standard statistical tests are insufficient:**
- [ ] A synthetic patient population can have correct marginal distributions on PK parameters but incorrect joint correlations (e.g., CL and Vd are biologically correlated via body weight)
- [ ] A synthetic control arm can pass distributional tests but have unrealistic dose-response trajectories
- [ ] **Associative vs. Causal Failure Modes:** <!-- Added 2026-08-29 (Antigravity review) --> Purely associative deep generative models (VAEs/GANs) model $P(X, Y)$ but fail under counterfactual interventions $P(Y|\text{do}(X))$ (`richens_2020_causal_med`, `sanchez_2022_causal_precision`)

**Proposed validation framework:**
- [ ] *Statistical layer:* Maximum Mean Discrepancy (MMD), Wasserstein distance between synthetic and real distributions
- [ ] *Pharmacological layer:* dose-response shape preservation, PK parameter correlation structure, variability decomposition (BSV vs. RUV)
- [ ] *Causal & Counterfactual layer:* <!-- Added 2026-08-29 (Antigravity review) --> Structural Causal Models (SCMs) for individual treatment effect simulation and counterfactual consistency checks (`sanchez_2022_causal_precision`)
- [ ] *Identifiability layer:* are synthetic datasets informative enough to identify the generating model's parameters? (Fisher information criterion)
- [ ] *Regulatory layer:* does synthetic data meet FDA's definition of acceptable external control? (Map to `fda_ai_guidance_2025` and ASME V&V 40)

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

**Working notes files:** `llm_failure_modes_notes.md`, `comparitive_activities_scoping_gemini.md`, `comparative_activities_scoping_claude.md`

---

### M4.4 — Scope differentiation memo
*One-page document clarifying MCS's GenAI lane relative to other SIGs*

- [ ] Write before paper outline is locked (needs cross-SIG alignment from `community/`)
- [ ] Table format: topic × (MCS lead / AI-ML SIG lead / QSP SIG lead / out of scope)
- [ ] Use this to write the position paper's scope statement and abstract

**Working notes file:** `scope_differentiation.md`

---

### M4.5 — Comparative evaluation: Claude × Codex × Antigravity

Empirical benchmark of AI systems on pharmacometric modeling tasks — directly feeds M4.3 taxonomy and M4.4 scope memo.

**Detailed protocols:** `comparative_activities_scoping_claude.md` (Claude, 2026-08-29) and `comparitive_activities_scoping_gemini.md` (Antigravity, 2026-08-29)

**Core six activities (in recommended execution order):**

- [ ] **M4.5-A2 — Failure mode elicitation** (Phase 1, no NONMEM required): 6 engineered prompts × 3 models; scores each of the M4.3 failure categories; can run as WG workshop in Month 2–3
- [ ] **M4.5-A6 — Model diagnostics interpretation** (Phase 1, no NONMEM required): 3 simulated NONMEM output scenarios extending prior output-translation work with engineered shrinkage, covariate, residual-error, and overparameterization traps; current-product comparison and blinded pharmacometrician scoring are the intended contributions (`cha_2025_nonmem_interpretation`); pair with A2 in the same workshop session
- [ ] **M4.5-A1 — Pop PK NONMEM code generation** (Phase 2, NONMEM required): warfarin / theophylline / tobramycin / vancomycin; extends zheng_2025_llm + kwack_2026_pkgpt with Claude/Codex/Antigravity and MCS identifiability + plausibility scoring; n=5 runs per task per model
- [ ] **M4.5-A3 — PBPK model structure specification** (Phase 2, PBPK expert required): midazolam primary test drug; no existing LLM PBPK benchmark; confirmed white space (chen_2026_pbpkml covers only parameter prediction, not structure generation)
- [ ] **M4.5-A4 — Hybrid neural ODE implementation** (Phase 3, Julia/Python + hybrid expert): one-compartment with ML-augmented CL in diffrax; tests adjoint stability awareness (kim_2021_stiff_node); MCS-distinctive, highest novelty
- [ ] **M4.5-A5 — QSP ODE generation + identifiability** (Phase 3, after M4.4 scope memo): TNF-α / IL-6 pathway; identifiability assessment via STRIKE-GOLDD logic; consider SciGym (scigym_2025) harness for ODE evaluation

**Additional comparative activities identified by literature search (2026-08-29):**

- [ ] **M4.5-A7 — Closed-loop PopPK model repair** (Phase 2, NONMEM required): provide each system an identical failing control stream and its run output; allow a fixed number of generate-run-diagnose-repair cycles. Score successful minimization *and* physiological plausibility, covariate selection, GOF/VPC acceptance, and run-to-run structural consistency. This distinguishes agentic execution from one-shot code generation and directly tests the remaining failure modes documented for PKGPT and NONMEM-output interpretation studies (`kwack_2026_pkgpt`, `cha_2025_nonmem_interpretation`).
- [ ] **M4.5-A8 — Evidence-to-QSP mathematical translation** (Phase 2/3, joint AI/ML-QSP-MCS activity): from a locked, jointly curated evidence packet and adjudicated claim set, extract signed biological interactions with passage-level provenance, construct an effect diagram, and specify the associated ODE system. AI/ML owns evidence-extraction methodology, QSP owns biological adjudication, and MCS owns mathematical translation and verification. Score claim precision/recall, causal-direction correctness, unsupported mechanisms, expert curation burden, and resulting model validity (`saini_2025_qsp_copilot`).
- [ ] **M4.5-A9 — PBPK context-of-use qualification package** (Phase 2, PBPK and regulatory experts required): extend A3 from model structure to a decision-specific package, initially CYP3A DDI prediction using midazolam. Require the context of use, qualification datasets, verification and sensitivity plan, predictive acceptance criteria, uncertainty statement, and limitations. Score whether the proposed evidence is sufficient and correctly matched to the intended decision (`ema_2025_pbpk_approvals`, `fda_ai_guidance_2025`).
- [ ] **M4.5-A10 — Synthetic PopPK/PKPD-data downstream validity** (Phase 3, access to a de-identified reference dataset required): have each system implement and audit a synthetic-data workflow, then refit the reference model to real and synthetic data. Compare structural/covariate conclusions, BSV/RUV and correlation preservation, predictive diagnostics, and privacy/disclosure treatment. Do not treat marginal distribution agreement as sufficient; score model-based inference equivalence and provenance explicitly (`jiang_2024_synthetic_pkpd`, `pasculli_2025_synthetic_data_regulation`).
- [ ] **M4.5-A11 — Evidence-grounded credibility dossier** (cross-cutting; apply to A1-A10): give the system a fixed model, results, and evidence pack and ask for a concise, traceable credibility dossier. Score context-of-use definition, linkage of claims to supplied evidence, disclosure of uncertainty and limitations, distinction between observed and synthetic evidence, and unsupported regulatory assertions (`fda_ai_guidance_2025`, `fda_ema_good_ai_principles_2026`, `pasculli_2025_synthetic_data_regulation`).

**Suggested sequencing for additions:** A7 and A8 after Phase 1; A9 after A3; A10 with M4.2 synthetic-data work; and A11 as the shared reporting and credibility layer. A7-A11 should use the same model/version capture, prompt-policy conditions, independent-run count, and blinded expert scoring policy as A1-A6.

**Open questions before running:**

- [ ] Confirm Antigravity product name, version, and code-execution capability (determines agent vs. chat protocol for A1/A4)
- [ ] Confirm Codex version (2025 cloud agent vs. GPT-4o chat — categorically different for A1/A4)
- [ ] Decide prompt engineering policy: naive only / optimized only / both (changes study interpretation)
- [ ] Establish expert review panel (2 pharmacometricians for A1, A3; 1 PBPK specialist for A3; 1 identifiability expert for A5)

**Publication target:** Phase 1 results → CPT:PSP Commentary or ISoP newsletter. Phase 2+3 → full paper, *CPT:PSP* or *Journal of Pharmacokinetics and Pharmacodynamics*.

---

## Key sources
| Source | Workstream | Added / Role |
|---|---|---|
| `sources/papers/dermawan_2026.json` | M4.1 | VAE for NLME, neural PBPK surrogate |
| `sources/background/aiml_claude_background.json` | M4.1, M4.3 | GenAI survey |
| `sources/background/aiml_chatgpt_background.json` | M4.1 | Pharma R&D GenAI landscape |
| `sources/papers/de_carlo_2024.json` | M4.2 | Virtual patient validation |
| `sources/papers/de_carlo_2025.json` | M4.2 | Virtual patient validation |
| `sources/papers/richens_2020_causal_med.json` | M4.2 | Added 2026-08-29 (Antigravity review): Causal ML in medical decision support |
| `sources/papers/sanchez_2022_causal_precision.json` | M4.2 | Added 2026-08-29 (Antigravity review): SCMs and counterfactual digital twins |
| `sources/web/fda_ai_guidance_2025.json` | M4.2 | Regulatory criteria for synthetic data |
| `sources/papers/shin_2024_llm.json` | M4.3, M4.5 | Baseline LLM NONMEM benchmark (ChatGPT/Gemini 2024) |
| `sources/papers/zheng_2025_llm.json` | M4.3, M4.5 | 7 LLMs × 13 tasks; scoring rubric; near-perfect with optimized prompt |
| `sources/papers/pkgpt_2026.json` | M4.3, M4.5 | Agentic closed-loop NONMEM (Antigravity-sourced) |
| `sources/papers/kwack_2026_pkgpt.json` | M4.3, M4.5 | Added 2026-08-29 (Claude): Human benchmarking; V2=149 vs 13.2 L plausibility failure |
| `sources/papers/chen_2026_pbpkml.json` | M4.5-A3 | Added 2026-08-29 (Claude): ML+PBPK white-space confirmation |
| `sources/papers/scigym_2025.json` | M4.5-A5 | SBML-to-ODE simulation harness for agentic benchmarking |
| `sources/papers/kim_2021_stiff_node.json` | M4.5-A4 | Adjoint instability in stiff neural ODEs |
| `sources/papers/savic_2009_shrinkage.json` | M4.5-A1, M4.5-A6 | η-shrinkage threshold (30%) for diagnostic scoring |
| `sources/papers/villaverde_2016_strikegodd.json` | M4.5-A5 | Structural identifiability reference method |
| `sources/papers/androulakis_2025_qsp.json` | M4.4, M4.5-A5 | QSP SIG scope boundary |
| `sources/papers/saini_2025_qsp_copilot.json` | M4.5-A8 | Evidence-to-QSP workflow and literature-extraction benchmark anchor |
| `sources/papers/cha_2025_nonmem_interpretation.json` | M4.5-A6, A7 | NONMEM-output interpretation, simulation, tables, and reporting evaluation |
| `sources/papers/jiang_2024_synthetic_pkpd.json` | M4.2, M4.5-A10 | Generative synthetic PK/PD-data benchmark and pharmacometrics-specific validation |
| `sources/papers/pasculli_2025_synthetic_data_regulation.json` | M4.2, M4.5-A10, A11 | Synthetic-data definitions, provenance, external controls, and regulatory issues |
| `sources/papers/ema_2025_pbpk_approvals.json` | M4.5-A9 | EMA review of PBPK qualification and intended uses in marketing-authorisation applications |

## Feeds into deliverables
- `deliverables/papers/genai_position/` — all workstreams
- `deliverables/conferences/webinars/` — Webinar 4 content
- `deliverables/papers/whitepaper_hybrid/` — Section D (synthetic data and causal validation in benchmark evaluation)
