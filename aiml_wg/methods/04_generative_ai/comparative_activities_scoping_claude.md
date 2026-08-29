# Comparative Activities: Claude × Codex × Antigravity in Pharma Modeling

**Pillar:** Generative AI (Pillar 4)  
**Feeds into:** M4.3 (LLM failure mode taxonomy), M4.4 (scope differentiation memo), `deliverables/papers/genai_position/`  
**Drafted:** 2026-08-29 (Claude)  
**Updated:** 2026-08-29 (Claude — detailed protocols + literature search)  
**Status:** Draft plan — not yet assigned task IDs

---

## Systems Under Comparison

| System | Developer | Execution mode | Key uncertainty |
|---|---|---|---|
| **Claude** (Sonnet 4.6 / Opus 4.8) | Anthropic | Chat API / VSCode | —  |
| **Codex** | OpenAI | Cloud agent (can execute code, clone repos, run NONMEM) | Confirm product version before running — the 2025 cloud agent is categorically different from a GPT-4 chat call |
| **Antigravity** | — | TBD | Confirm product name, version, and whether code execution is available |

> **Critical design note — agent vs. chat:** If Codex is the 2025 cloud coding agent (execute-capable), Activities 1 and 4 need a separate sub-protocol where Codex can iterate on runtime errors. A chat-based model that cannot execute produces one static output; an agent that can run NONMEM and read the error log is a fundamentally different experimental unit. Design the rubric to credit both, but report them separately.

---

## Literature Context

The existing pharmacometrics LLM benchmark literature:

| Source | Models | Tasks | Key gap |
|---|---|---|---|
| shin_2024_llm | ChatGPT 4.0, Gemini Ultra 1.0 | 2 NONMEM tasks | Only 2 models, 2 tasks; no Claude; no MCS scoring criteria |
| zheng_2025_llm | 7 LLMs (incl. o1, gpt-4.1) | 13 NONMEM tasks | Best model achieves near-perfect accuracy with optimized prompt; still no Claude, no plausibility/identifiability scoring |
| pkgpt_2026 | LLM agent (closed-loop) | NONMEM (automated) | No human benchmark; Chen et al. version |
| kwack_2026_pkgpt | Gemini 3.0 Flash agent | 3 datasets vs. human expert | **V2=149 L vs. 13.2 L plausibility failure documented**; covariate analysis fails |
| scigym_2025 | Frontier LLM agents | Biological ODE discovery | Biochemical networks, not clinical pharmacometrics |

**White space confirmed by this search:**
- No existing benchmark includes Claude, Codex, or Antigravity
- No benchmark scores physiological plausibility systematically (kwack_2026 notes it qualitatively)
- No benchmark covers PBPK structure generation by LLMs
- No benchmark covers QSP ODE + identifiability by LLMs
- No benchmark covers hybrid neural ODE implementation by LLMs

---

## Activity 1 — Pop PK NONMEM Code Generation

**Domain:** Population pharmacokinetics  
**Study type:** Formal benchmark, paper-quality  
**MCS differentiation:** Medium — extends zheng_2025 + kwack_2026 with new models and new MCS scoring criteria  
**Estimated effort:** 3–4 person-days for a 3-dataset × 3-model run + expert scoring

### Benchmark datasets

Use the same three public NONMEM example datasets as kwack_2026_pkgpt — this enables direct comparison:

| Dataset | Drug | Structure | PK complexity |
|---|---|---|---|
| warfarin | Warfarin | 1-cpt oral, Emax PD | Moderate — nonlinear PD adds difficulty |
| theophylline | Theophylline | 1-cpt oral | Low — canonical teaching dataset |
| tobramycin | Tobramycin | 2-cpt IV | Moderate — V2 plausibility is the known trap |

Add a fourth dataset as MCS extension:
- **vancomycin** (Revilla 2010 or Llopis-Salvia 2006 — well-characterized, M3 BLQ data available): 2-cpt IV with BLQ observations, tests M3 method handling not covered by zheng_2025 or kwack_2026.

### Task prompt template

Each AI receives this prompt, with `[DATASET]`, `[STRUCTURE]`, and `[COMPLEXITY_FLAGS]` filled in:

```
You are an expert pharmacometrician. Write a complete, executable NONMEM control stream for a population pharmacokinetic analysis with the following specification:

Drug: [DRUG_NAME]
Dataset format: [DATASET_COLUMN_DESCRIPTION]
Structural model: [STRUCTURE_DESCRIPTION]
Variability: Between-subject variability (ETA) on [CL, Vd, ...]; proportional residual error
Additional requirements: [e.g., "Handle BLQ observations using the M3 method" / "Use ADVAN4 TRANS4"]

Requirements:
1. The control stream must be executable in NONMEM 7.5 without modification
2. Use the SAEM estimation method
3. Specify initial estimates physiologically consistent with the drug class
4. Include the $OMEGA matrix structure appropriate for the number of ETAs
5. Output the complete $PROB, $DATA, $INPUT, $SUBROUTINE, $PK, $ERROR, $THETA, $OMEGA, $SIGMA, $ESTIMATION, $COVARIANCE, $TABLE blocks

After the code, provide a one-paragraph justification of your structural model choice and initial estimate strategy.
```

### Scoring rubric (100 points total)

**A. Executability (20 pts)**
- Code runs in NONMEM without syntax error: 20 pts
- Code runs with minor fixable errors (1–2 syntax corrections): 10 pts
- Code does not run: 0 pts

**B. Structural correctness (25 pts)**
- Correct compartment count and topology: 8 pts
- Correct absorption/elimination parameterization (ADVAN/TRANS correct): 7 pts
- Correct ETA placement on specified parameters: 5 pts
- $ERROR block correct (proportional RUV implemented as specified): 5 pts

**C. Mass balance (15 pts)**
- Amounts conserved across all compartments: 10 pts
- No negative concentration outputs possible from generated equations: 5 pts

**D. Physiological plausibility of initial estimates (20 pts)**
- CL initial estimate within 5-fold of published population mean: 8 pts
- Vd initial estimate within 5-fold of published population mean: 7 pts
- V2 (if 2-cpt) within 5-fold of published population mean (kwack_2026 failure: 149 vs 13.2 L): 5 pts

**E. MCS-specific criteria (20 pts)**
- Identifiability: no IIV parameters confounded or redundant in $OMEGA block: 8 pts
- BLQ handling: M3 method correctly implemented if specified (or correctly flagged as not applicable): 7 pts
- Self-flagging: AI explicitly notes any identifiability or plausibility uncertainty without being asked: 5 pts

### Execution protocol

1. **Runs per condition:** n=5 independent runs per task per model (temperature=1.0 default; do not fix seed)
2. **Blinding:** Human expert scorers receive code without model identity label
3. **Expert review panel:** 2 pharmacometricians each independently score B–E; use mean; flag disagreements >5 pts for discussion
4. **Reproducibility metric:** Report coefficient of variation (CV%) across 5 runs for total score per task per model
5. **Agentic Codex protocol:** If Codex can execute NONMEM, allow up to 3 self-correction iterations. Record (a) whether iteration was needed, (b) score after iteration 1 vs. final
6. **Comparison anchor:** Report all scores against kwack_2026_pkgpt's documented OFV and V2 for the same three datasets

### Expected hypotheses

- H1: Claude and Antigravity will match or exceed zheng_2025's best chat models (o1, gpt-4.1) on executability (A) but MCS criteria (E) will discriminate
- H2: V2 plausibility failure (kwack_2026's documented gap) will appear in at least one model on tobramycin
- H3: Agentic Codex will outperform chat models on executability (A) through self-correction but may not improve identifiability scoring (E)
- H4: Reproducibility CV will be high (>30%) for all models — consistent with shin_2024_llm

### Publication target

Extension of zheng_2025_llm methodology. Target: *CPT: Pharmacometrics & Systems Pharmacology* as a brief report / letter. Frame as "closing the Claude/Antigravity gap in the LLM pharmacometrics benchmark + adding MCS rigor criteria."

---

## Activity 2 — LLM Failure Mode Elicitation

**Domain:** Pop PK, PBPK, QSP  
**Study type:** Structured elicitation; can be run as WG workshop — feeds M4.3 taxonomy directly  
**MCS differentiation:** High — no existing benchmark systematically tests for identifiability violations or mass-balance failures  
**Estimated effort:** 1–2 person-days; 5 runs per prompt per model; automated scoring possible for most categories

### Six failure categories and prompt designs

Each prompt is crafted to maximize the probability of triggering the failure mode. The key variable is whether the AI generates the problem silently, or flags it.

---

**Category 1 — Structural error**

Prompt:
```
Write a two-compartment IV PK model where drug is eliminated from BOTH the central and peripheral compartment simultaneously. 
Use NONMEM ADVAN3 syntax. Specify distinct elimination rate constants ke_central and ke_peripheral.
```

Expected failure: Elimination from peripheral compartment is pharmacologically incorrect for virtually all drugs; it would require a saturable peripheral sink. A sophisticated model should either refuse, request clarification, or generate the code with an explicit caveat.

Scoring:
- Generates code silently with dual elimination (no caveat): FAIL (0 pts)
- Generates code with a warning that this is atypical: PARTIAL (5 pts)  
- Asks for clarification or explains why dual elimination is unusual before generating: PASS (10 pts)

---

**Category 2 — Identifiability violation**

Prompt:
```
I am building a three-compartment PK model. I want to estimate all six intercompartmental clearance parameters independently:
CL12, CL21, CL13, CL31, CL23, CL32. Write the $PK block for NONMEM with all six as separate THETAs with BSV.
```

Expected failure: A 3-cpt model with separate in- and out-clearances for each pair is typically not structurally identifiable from PK data — CL12 and CL21 are confounded unless a ratio constraint is applied. A pharmacometrician would immediately flag this.

Scoring:
- Generates code with 6 independent THETAs, no identifiability warning: FAIL (0 pts)
- Generates code, notes some clearances may be difficult to estimate: PARTIAL (5 pts)
- Explains identifiability issue and suggests constraint (e.g., CL12=CL21 or micro-constant reparameterization): PASS (10 pts)

---

**Category 3 — Unit inconsistency**

Prompt:
```
A drug has CL = 45 mL/min, Vd = 12 liters, and is dosed at 500 mg every 8 hours. 
Write a NONMEM $PK block. The dataset uses TIME in hours and DV in ng/mL.
Use the parameter values as given above.
```

Expected failure: CL is in mL/min but the model uses hours; conversion factor (×60) is required. Failing to convert means CL is 60-fold wrong.

Scoring:
- Generates code without unit conversion: FAIL (0 pts)
- Converts CL to L/h (= 2.7 L/h) without comment: PARTIAL (5 pts)
- Converts CL to L/h and explicitly notes the unit conversion performed: PASS (10 pts)

---

**Category 4 — Mass non-conservation**

Prompt:
```
Add a transit absorption compartment chain of 5 transit compartments to a one-compartment PK model.
Each transit compartment should have its own first-order rate constant: ktr1, ktr2, ktr3, ktr4, ktr5.
Write the $DES block with all five transit ODEs and the central compartment ODE.
```

Expected failure: A general transit chain has a single mean transit time (MTT) with all k_tr equal; separate unconstrained ktr1–ktr5 will typically produce a non-conservation-of-mass ODE system unless input and output of each compartment balance. A correct implementation uses ktr = (n+1)/MTT for each compartment.

Scoring:
- Generates 5 independent rate constants without mass balance check: FAIL (0 pts)
- Generates with note that ktr parameters should be constrained: PARTIAL (5 pts)
- Generates correctly with single MTT parameter and ktr = (n+1)/MTT: PASS (10 pts)

---

**Category 5 — Sign error**

Prompt:
```
I want to model competitive inhibition of drug clearance. As inhibitor concentration increases, 
clearance should DECREASE. Write the $PK block in NONMEM with CL = CL_baseline * (1 + IMAX * CONC_I / (IC50 + CONC_I)).
```

Expected failure: The formula `CL * (1 + IMAX * C/(IC50+C))` would INCREASE clearance — it's an Emax activation model applied to inhibition. Competitive inhibition should use `CL / (1 + C/IC50)` or `CL * (1 - IMAX * C/(IC50+C))`.

Scoring:
- Uses the formula as given without flagging the sign error: FAIL (0 pts)
- Uses formula but notes it will increase rather than decrease CL: PARTIAL (5 pts)
- Corrects the formula and explains the pharmacological error in the prompt: PASS (10 pts)

---

**Category 6 — Plausibility bounds**

Prompt:
```
I am building a population PK model for a typical oral small-molecule drug in a 70 kg adult.
Please suggest initial estimates for: CL (L/h), Vd (L), ka (h⁻¹), and F (fraction absorbed).
Also provide typical between-subject variability (omega, CV%) for each parameter.
```

Expected failure: There is no single trap here — the failure mode is returning values wildly outside physiological ranges. Reference ranges: CL ∈ [0.1, 300] L/h; Vd ∈ [3, 7000] L; ka ∈ [0.1, 5] h⁻¹; F ∈ (0,1].

Scoring metric: Count parameters outside the physiological range above. Score = 10 − (2 × number_out_of_range).

---

### Aggregate scoring and analysis

For each model, compute:
- **Category pass rate** (0/5 pts average per category; 10 pts = full pass, 5 = partial, 0 = fail)
- **Self-flagging rate**: proportion of failures that were flagged by the AI without explicit prompting
- **Failure profile**: radar chart across 6 categories per model

The MCS hypothesis: identifiability violations (Category 2) will be the mode most often missed silently, because LLMs have been trained on pharmacometrics code that rarely includes identifiability warnings. This would directly motivate the automated checker proposed in M4.3.

### Execution protocol

1. **Runs per condition:** n=5 per prompt per model
2. **Scoring:** Categories 1–5 can be scored algorithmically (check for presence of caveat language); Category 6 requires pharmacometrician to read parameter values
3. **No blinding required** — scoring criteria are pre-specified and semi-automated
4. **Workshop format:** This activity can be run in a 90-minute WG session — 6 prompts × 3 models = 18 outputs. Participants score live.

---

## Activity 3 — PBPK Model Structure Specification

**Domain:** Physiologically-based pharmacokinetics  
**Study type:** Exploratory benchmark — no published LLM benchmark for PBPK exists; paper-quality if combined with Activity 1  
**MCS differentiation:** High — confirmed white space; existing ML+PBPK literature (chen_2026_pbpkml) addresses parameter *prediction*, not structural *generation*  
**Estimated effort:** 2–3 person-days; requires 1 PBPK expert reviewer

### Test drug selection

Use **midazolam** as the primary test case:
- Extensively characterized PBPK in the literature (Rodgers & Rowland 2006, Simcyp/Simulations Plus validation studies)
- CYP3A4 substrate — well-defined hepatic and intestinal first-pass
- Moderate lipophilicity (logP ~3.9), basic compound (pKa ~6.2) — tests ionization-dependent partition
- FDA frequently requests midazolam DDI PBPK — regulatory relevance
- chenel_2026 discusses midazolam as a canonical PBPK example

Secondary drug: **warfarin** (for continuity with Activity 1; acidic compound; different partition method required).

### Task prompt

Part A — Model structure:
```
You are building a PBPK model for midazolam in a healthy 70 kg adult male.

Drug physicochemical properties:
- Molecular weight: 325.8 g/mol
- logP (octanol-water): 3.89
- pKa (base): 6.15 (weak base)
- fu (plasma unbound fraction): 0.034
- Blood-to-plasma ratio (B/P): 0.67

Task:
1. Select the minimal set of tissue compartments appropriate for a well-stirred PBPK model for this compound
2. Write the system of ODEs for each compartment using the perfusion-limited assumption
3. For the tissue partition coefficients (Kp), specify which prediction method is appropriate for a basic compound and write the equation for at least one tissue (lung or liver)
4. Specify hepatic CL using the well-stirred liver model (provide the equation with fu, Rb, Q_H, CL_int)
5. List the numerical values for physiological parameters (Q, V) for each tissue you selected, citing their source

Your answer should include: (a) compartment list with justification, (b) ODE system, (c) Kp method + sample equation, (d) hepatic CL equation, (e) physiological parameter table.
```

Part B — Mass balance check (given to same AI as a follow-up):
```
Verify that the total blood flow across all tissue compartments in your model sums to cardiac output. 
What is the total cardiac output and does your model conserve it?
```

### Scoring rubric (90 points)

**A. Compartment selection (20 pts)**
- Includes mandatory compartments (lung, liver, kidney, gut, muscle, adipose, richly perfused tissues): 12 pts (2 pts each for lung, liver, kidney, gut; 4 pts for at least one of muscle/adipose/richly-perfused)
- Justification references lipophilicity and distribution for compartment choice: 8 pts

**B. ODE structure (25 pts)**
- Perfusion-limited ODE form correct: dA_tissue/dt = Q*(C_arterial − C_venous_tissue): 10 pts
- Venous concentration defined correctly: C_venous = C_tissue / Kp: 8 pts
- Lung compartment handles arterio-venous mixing correctly: 7 pts

**C. Kp method and equation (15 pts)**
- Identifies Rodgers-Rowland method as appropriate for basic compound: 8 pts
- Equation for sample tissue (lung or liver) uses correct mechanistic form (lipid, water, albumin terms): 7 pts

**D. Hepatic CL — well-stirred model (15 pts)**
- CL_H = Q_H × fu × CL_int / (Q_H + fu × CL_int): equation correct: 10 pts
- B/P ratio applied correctly to convert CL_int to blood-based CL: 5 pts

**E. Physiological parameter plausibility (15 pts)**
- Blood flows (Q) for each tissue within ±30% of published human physiology (Davies 1993): 8 pts
- Tissue volumes within ±30% of published values: 7 pts

**F. Mass balance verification (Part B) (bonus, up to 10 pts)**
- Correctly sums tissue flows and compares to cardiac output (5.6 L/min reference): 10 pts
- Identifies any discrepancy: partial credit 5 pts

### Reference values for scoring

| Parameter | Reference value | Source |
|---|---|---|
| Q_H (hepatic blood flow) | 1.45 L/min | Davies 1993 |
| V_liver | 1.69 L | Davies 1993 |
| Q_kidney | 1.24 L/min | Davies 1993 |
| Cardiac output | 5.6 L/min | Davies 1993 |
| Kp_liver (midazolam, Rodgers-Rowland) | ~11.4 | Simcyp literature |

### Execution protocol

1. **Runs per condition:** n=3 per task per model (lower because expert review time is high)
2. **Expert review:** 1 PBPK specialist scores B–E; 2nd independent scorer for D (well-stirred model equation)
3. **Part B** run as a separate prompt in the same session context (tests in-context reasoning, not just template recall)

---

## Activity 4 — Hybrid Neural ODE Implementation

**Domain:** Hybrid mechanistic–ML (Pillar 1 × Pillar 4)  
**Study type:** Formal benchmark — no existing LLM benchmark for hybrid model code generation; paper-quality  
**MCS differentiation:** Very high — squarely in MCS lane; unknown whether any current LLM produces valid diffrax/Lux.jl adjoint-compatible code  
**Estimated effort:** 3–4 person-days; requires Python/Julia execution environment + 1 hybrid model expert

### Target implementation

One-compartment PK model with ML-augmented clearance (the canonical hybrid architecture from lu_2021 / janssen_2024 / elmokadem_2024 lineage):

```
dA/dt = -CL(phi, t) * A / Vd + D(t)

where CL(phi, t) = CL_base * f_NN(weight, SCr, ALT; theta_NN)
      f_NN is a feedforward neural network
      phi = [A(t)] (state)
      theta_NN = learnable parameters
```

Population structure: log-normal IIV on CL_base and Vd (standard NLME hierarchy).

### Task prompt

```
You are an expert in mechanistic-ML hybrid pharmacokinetic modeling using neural ODEs.

Task: Implement a one-compartment population PK model where drug clearance (CL) is augmented by a 
3-layer feedforward neural network that takes patient covariates as input: 
  - body weight (WT, kg)
  - serum creatinine (SCr, mg/dL)  
  - alanine aminotransferase (ALT, U/L)

The mechanistic ODE is:
  dA/dt = -(CL_base * f_NN(WT, SCr, ALT)) / Vd * A + dose_rate(t)

Requirements:
1. Implement in Python using diffrax (for JAX-based ODE solving)
2. CL_base and Vd should have log-normal between-subject variability (sample from a population distribution)
3. The neural network f_NN should output a strictly positive scalar (enforced via softplus or exp)
4. The ODE solver must use a method suitable for stiff systems (Kvaerno5 or Dopri8 with adaptive step size)
5. The implementation should be trainable end-to-end via gradient descent through the ODE solver (adjoint method or direct backpropagation)
6. Include a forward() function that takes covariates + initial dose and returns the simulated concentration-time profile
7. Include a brief comment on any numerical stability concerns with adjoint-based gradients in this context

Provide complete, executable Python code. Import all required packages.
```

### Scoring rubric (100 points)

**A. Executability (20 pts)**
- Code imports are valid and complete: 5 pts
- Code runs without error on a test call: 15 pts
  - If Codex (agent): test by actually running; others: expert manually reviews
  - Partial credit (8 pts) if code structure is correct but minor import/syntax fix needed

**B. Mechanistic skeleton correctness (20 pts)**
- One-compartment ODE structure intact: A/Vd → concentration, elimination correct: 10 pts
- Dose rate input handled correctly (bolus, infusion, or oral as specified): 10 pts

**C. ML component integration (25 pts)**
- f_NN takes covariates as input (not states or time): 8 pts
- Output is strictly positive (softplus or exp applied): 7 pts
- Network is differentiable and connected to ODE via correct gradient path: 10 pts

**D. Population hierarchy (15 pts)**
- CL_base and Vd sampled from log-normal distributions: 8 pts
- Individual parameters correctly used inside ODE (not population means): 7 pts

**E. Numerical stability (10 pts)**
- Stiff-capable solver selected (Kvaerno5, Dopri8, or equivalent): 5 pts
- AI mentions adjoint gradient instability risk for stiff systems (kim_2021_stiff_node knowledge): 5 pts

**F. Completeness (10 pts)**
- forward() function implemented as specified: 5 pts
- Code produces a plausible concentration-time profile shape on a test run: 5 pts

### Execution protocol

1. **Runs per condition:** n=3 per model
2. **For Codex (agent):** Allow execution and self-correction up to 3 iterations. Record whether adjoint instability was encountered and how (or whether) the agent handled it
3. **For chat models (Claude, Antigravity):** Expert manually attempts to execute the generated code on a standard theophylline dataset (1-cpt reference)
4. **Key diagnostic:** Does any model spontaneously flag the adjoint stability risk described in kim_2021_stiff_node? This is the MCS-distinctive criterion

---

## Activity 5 — QSP ODE Generation + Identifiability Assessment

**Domain:** Quantitative Systems Pharmacology / systems biology  
**Study type:** Exploratory benchmark; positions MCS relative to QSP SIG; paper-quality with MCS framing  
**MCS differentiation:** High — biology generation is QSP SIG's domain; identifiability analysis is MCS's unique contribution  
**Estimated effort:** 3–4 person-days; requires both a systems biologist and a structural identifiability expert  
**Framework:** SciGym (scigym_2025) provides SBML-to-ODE simulation harness; consider adapting it for pharmacometric context

### Pathway and observation design

**Target pathway:** TNF-α / IL-6 bidirectional loop (IBD/autoimmune context — directly relevant to irie_2025 infliximab case study)

Biological specification:
- TNF-α activates IL-6 production (first-order induction term)
- IL-6 feeds back to suppress TNF-α production (inhibitory Hill term)
- Drug (infliximab-like anti-TNF) binds TNF-α with competitive antagonism
- Drug PK: first-order absorption + elimination (one-compartment)

Observation design (what a typical clinical study measures):
- Drug concentration: observed
- TNF-α: NOT observed (serum cytokines rarely measured in trials)
- IL-6: observed
- Baseline/steady-state known from pre-dose samples

### Task prompt

Part A — ODE generation:
```
You are building a quantitative systems pharmacology (QSP) model of anti-TNF drug pharmacodynamics.

Biological pathway:
1. TNF-α is produced at a baseline rate (k_prod_TNF) and degrades with rate k_deg_TNF
2. IL-6 is produced at a rate induced by TNF-α: production = k_prod_IL6 * TNF / (K_TNF + TNF)
3. IL-6 degrades with rate k_deg_IL6
4. IL-6 feeds back to suppress TNF-α production: the baseline production is multiplied by (1 - IMAX_IL6 * IL6 / (IC50_IL6 + IL6))
5. Drug (anti-TNF) competes with TNF-α for receptor binding: effective free TNF = TNF / (1 + Drug / IC50_drug)

Drug PK: one-compartment model, IV bolus, CL and Vd are known parameters.

Tasks:
1. Write the complete ODE system with all species and parameters explicitly defined
2. State which parameters are at steady state before drug dosing and derive the algebraic constraint(s)
3. List all unknown parameters that must be estimated
4. State which parameters are STRUCTURALLY IDENTIFIABLE given the observation design above (Drug concentration and IL-6 are observed; TNF-α is NOT observed)
5. For any unidentifiable parameter combinations, suggest the minimal experimental change that would resolve identifiability
```

Part B — Numerical identifiability check:
```
Using the ODE system you generated, assign nominal parameter values (physiologically plausible for a cytokine system) 
and simulate the observable outputs (Drug concentration, IL-6) over 4 weeks after a single IV dose.

Then: if you varied k_prod_TNF and k_deg_TNF simultaneously while keeping k_prod_TNF/k_deg_TNF constant 
(i.e., keeping steady-state TNF-α unchanged), would the observable IL-6 trajectory change?
What does this imply about practical identifiability?
```

### Scoring rubric (90 points)

**A. ODE topology correctness (30 pts)**  
Scored by systems biologist:
- Correct bidirectional coupling (TNF→IL6 induction, IL6→TNF suppression): 12 pts
- Drug competition term mechanistically correct (not additive — multiplicative scaling on free TNF): 10 pts
- Non-negativity ensured (all rates ≥ 0 at all times): 8 pts

**B. Steady-state constraint derivation (10 pts)**
- Sets dTNF/dt = 0 and dIL6/dt = 0 and solves algebraically: 10 pts
- Notes the constraint but doesn't solve: 5 pts

**C. Structural identifiability assessment (35 pts)**  
Scored by identifiability expert; reference standard: STRIKE-GOLDD analysis (villaverde_2016_strikegodd)
- Correctly identifies that k_prod_TNF and k_deg_TNF are not individually identifiable given TNF unobserved: 15 pts
- Identifies which parameter combinations ARE identifiable (e.g., ratio k_prod_TNF/k_deg_TNF): 10 pts
- Proposes correct experimental fix (e.g., measure TNF-α at baseline or add a TNF-α inhibition assay): 10 pts

**D. Part B — Practical identifiability reasoning (15 pts)**
- Correctly recognizes that varying k_prod_TNF/k_deg_TNF at fixed ratio does NOT change IL-6 trajectory: 10 pts
- Draws correct conclusion: the two parameters are practically unidentifiable, not just structurally: 5 pts

### Scope note for M4.4

Before publishing, consult scope differentiation memo (M4.4). The biology content of this activity overlaps with QSP SIG's domain (androulakis_2025_qsp). MCS's unique frame is the identifiability layer — emphasize that in any presentation or paper.

---

## Activity 6 — Model Diagnostics and Output Interpretation

**Domain:** Population PK  
**Study type:** Workshop-suitable; informal comparison; high community relevance  
**MCS differentiation:** Medium — novel relative to existing benchmarks (zheng_2025 tests only code generation); tests pharmacometric reasoning  
**Estimated effort:** 1 person-day; can be run without NONMEM access

### Simulated output scenarios

Create three representative NONMEM output scenarios covering common diagnostic pitfalls. These are constructed (not from real data), so no data-sharing concerns.

---

**Scenario A — High shrinkage + missed covariate**

```
=== NONMEM OUTPUT SUMMARY ===
Dataset: 89 patients, 712 observations, sparse sampling (median 4 samples/patient)
Structural model: 2-compartment, first-order absorption (ADVAN4)
Estimation: SAEM + IMP

OBJECTIVE FUNCTION VALUE: 4213.7

PARAMETER ESTIMATES:
  THETA(1) = CL = 4.21 L/h  (RSE = 8.2%)
  THETA(2) = Vd = 28.4 L    (RSE = 12.4%)
  THETA(3) = ka = 0.91 h⁻¹  (RSE = 18.7%)
  THETA(4) = V2 = 67.2 L    (RSE = 31.4%)
  THETA(5) = Q  = 2.14 L/h  (RSE = 28.9%)

OMEGA (BSV):
  ETA(1) on CL:  39.2% CV  (shrinkage: 52%)
  ETA(2) on Vd:  28.1% CV  (shrinkage: 18%)
  ETA(3) on ka:  87.4% CV  (shrinkage: 71%)

SIGMA (RUV):
  Proportional error: 0.187 (18.7% CV)
  Additive error: 0.041 (SD = 0.20 ng/mL)

GOODNESS OF FIT (description):
  DV vs PRED: acceptable, slight underprediction above 100 ng/mL
  CWRES vs TIME: slight positive trend at 24-48h post-dose
  CWRES vs PRED: slight fan shape at high concentrations
  ETA(CL) vs weight: strong positive trend (r ≈ 0.55, n=89)
  ETA(CL) vs renal function (eGFR): strong negative trend (r ≈ −0.61, n=89)
```

Questions to each model:
1. What do the shrinkage values tell you about the reliability of each ETA for covariate analysis?
2. What do the GOF plots suggest about the structural model?
3. Based on the ETA relationships, what covariates would you prioritize and why?

**Gold-standard answers:**
1. ETA(CL) shrinkage=52% and ETA(ka) shrinkage=71% are above the 30% threshold (savic_2009_shrinkage) — individual ETA estimates are unreliable for covariate analysis; ETA(Vd) at 18% is reliable
2. CWRES trend at 24–48h suggests missed absorption phase or flip-flop kinetics; fan shape suggests proportional error model may be insufficient
3. Both weight and eGFR should be tested on CL (strong ETA correlations suggest they explain BSV); BUT shrinkage=52% means the covariate model may appear significant even if spurious — validation with a reduced dataset or bootstrap is warranted

---

**Scenario B — Misspecified error model**

Simpler scenario: a model with dominant additive error where concentration ranges are 0.1–2000 ng/mL. The additive error term dominates at low concentrations.

---

**Scenario C — Overparameterized covariate model**

Outputs from a model that included weight on all three parameters simultaneously with high parameter uncertainty. Tests whether AI identifies the overparameterization.

### Scoring rubric

For each scenario, expert pharmacometrician uses 3-point scale per question:
- 2: Correct, complete, and at appropriate level of nuance
- 1: Partially correct or lacks key nuance (e.g., identifies shrinkage is high but does not cite the 30% threshold or its covariate implication)
- 0: Incorrect or silent

Report: mean score per scenario per model; rate of citing savic_2009_shrinkage-consistent thresholds (tests whether LLM has internalized the specific 30% criterion vs. generic "high shrinkage" language).

### Execution protocol

1. **Runs per condition:** n=3 per scenario per model
2. **Blinding:** Scorer does not know model identity
3. **Format:** Provide scenario text in a single prompt; do not chain questions
4. **Workshop use:** This activity can be embedded in a journal club session — scenario A is rich enough for a 30-minute facilitated discussion

---

## Cross-Activity Prioritization and Sequencing

| Activity | MCS differentiator | Novel vs. lit | Effort | Standalone pub? | Recommended order |
|---|---|---|---|---|---|
| 2 — Failure modes | High (M4.3) | Med | Low | Workshop paper / Commentary | **1st** |
| 6 — Diagnostics | Med | Med | Low | Combined with Activity 2 | **2nd (same session)** |
| 1 — NONMEM bench | Med | Med | Med | Brief report in CPT:PSP | **3rd** |
| 3 — PBPK structure | High | Very high | Med | Part of larger paper | **4th** |
| 4 — Hybrid neural ODE | Very high | Very high | High | Full paper, MCS flagship | **5th** |
| 5 — QSP + identifiability | High (with MCS frame) | High | High | After M4.4 scope memo locked | **6th** |

### Phase 1 pilot (can run with 3 people, no NONMEM required)

Activities 2 and 6 require only a text editor and pharmacometric expertise — no software installation, no datasets. Run these as a 90-minute WG workshop in Month 2–3:
1. Before the session: prepare the 6 failure prompts and 3 diagnostic scenarios
2. During the session: run prompts live against Claude, Codex, and Antigravity
3. After the session: score outputs; compile results into a short commentary draft

### Phase 2 benchmark (requires NONMEM + 2 pharmacometricians)

Activities 1 and 3 require NONMEM execution and expert review. Run after Phase 1, Month 4–6.

### Phase 3 hybrid + QSP (requires specialist contributors)

Activities 4 and 5 require neural ODE and identifiability expertise respectively. Assign to domain leads after kickoff decision on pillar leads.

---

## Open Design Questions

1. **Antigravity identity:** Confirm the product name, version, and execution capability before designing Phase 1. If Antigravity has code execution, treat it equivalently to Codex agent in Activities 1 and 4.
2. **Reproducibility reporting:** Following shin_2024_llm, explicitly compute CV% across n runs for all activities. Propose this as a standard reporting metric for future pharmacometrics LLM benchmarks.
3. **Prompt engineering as a variable:** zheng_2025_llm shows that prompt engineering substantially changes outcomes. Decide whether to (a) use naive prompts only, (b) use optimized prompts only, or (c) test both. Option (c) is most informative but doubles the workload.
4. **Expert review calibration:** For Activities 1 and 5, run a calibration exercise with two scorers on 2–3 outputs before the main study to establish inter-rater reliability.
5. **SBML/SciGym integration for Activity 5:** scigym_2025 provides an ODE discovery framework in SBML. Evaluate whether their simulation harness can be adapted to score structural completeness of LLM-generated TNF/IL-6 models.

---

## Key Sources by Activity

| Source | Activity | Role |
|---|---|---|
| shin_2024_llm | 1, 2, 6 | Baseline benchmark (ChatGPT/Gemini 2024) |
| zheng_2025_llm | 1 | Extends to 7 LLMs × 13 tasks; scoring rubric |
| kwack_2026_pkgpt | 1, 2 | Human benchmarking data; V2 plausibility failure anchor |
| pkgpt_2026 | 1 | Agentic loop architecture reference |
| savic_2009_shrinkage | 1, 6 | η-shrinkage scoring threshold (30%) |
| kim_2021_stiff_node | 4 | Adjoint instability in stiff neural ODEs |
| chenel_2026 | 3 | PBPK best practices + ICH M15 scoring anchor |
| chen_2026_pbpkml | 3 | ML+PBPK white space confirmation |
| villaverde_2016_strikegodd | 5 | Structural identifiability reference method |
| diazseoane_2023_strikegodd4 | 5 | STRIKE-GOLDD 4.0 toolbox |
| scigym_2025 | 5 | SBML-to-ODE simulation harness |
| androulakis_2025_qsp | 5 | QSP SIG scope boundary |
| janssen_2024 | 4 | Neural ODE worst-case on sparse data; SHAP |
| lu_2021 | 4 | First neural ODE for PK; failure modes |
