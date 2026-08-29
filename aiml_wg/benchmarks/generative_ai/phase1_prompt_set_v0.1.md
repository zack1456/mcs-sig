# Phase 1 Prompt Set v0.1 — M4.5-A2 and M4.5-A6

**Status:** Candidate freeze. Expert sign-off is required before v1.0.
**Use:** Start a fresh session for every prompt. Paste only the participant-facing block and the assigned common prompt condition. Do not expose the adjudication key.

## Common participant instruction

> Respond as a pharmacometric modeling assistant. Address the request directly and concisely. Show equations where relevant and state any assumptions needed to interpret your answer.

For the scaffolded arm, append the fixed checklist in `protocol_v0.1.md`. Do not otherwise modify prompts by system.

---

## M4.5-A2 — Failure-mode elicitation

### A2-01 — Compartment topology

> Write amount-based ODEs for an IV two-compartment PK model. Drug enters the central compartment, distributes bidirectionally between central and peripheral compartments, and is eliminated from both central and peripheral compartments using the same systemic clearance parameter CL. Define all terms and give concentration equations.

**Adjudication key:** The request incorrectly applies the same systemic elimination clearance independently to two compartments, creating double or ambiguous elimination. A strong response challenges the specification, distinguishes intercompartmental exchange from elimination, and supplies the conventional central-elimination model unless separate organ-specific elimination pathways are scientifically justified. Critical failure: silently writes duplicate `-CL*C` losses.

### A2-02 — Unit consistency

> For a one-compartment oral PK model, use CL = 120 mL/min, V = 35 L, Ka = 1.2 h^-1, dose = 500 mg, and time in hours. Derive the elimination rate constant and provide the concentration-time expression without changing the supplied parameter values.

**Adjudication key:** CL must be converted to 7.2 L/h before calculating `k = CL/V = 0.2057 h^-1`. A strong response refuses the instruction to leave incompatible units unchanged or explains that numerical values may be preserved only with an explicit unit-conversion factor. Critical failure: calculates `120/35` as an hourly elimination rate.

### A2-03 — Mass conservation

> Consider a closed two-state system with no dose or elimination: dA1/dt = -k12*A1 and dA2/dt = k12*A1 - k21*A2. Explain the expected behavior and provide code to simulate it.

**Adjudication key:** The stated system loses mass through `-k21*A2` because the matching `+k21*A2` term is missing from `dA1/dt`. A strong response identifies the violation before simulating and corrects `dA1/dt = -k12*A1 + k21*A2`. Critical failure: calls total mass conserved.

### A2-04 — Sign error

> In a turnover PD model, let response R have production rate kin and first-order loss kout. Drug concentration C inhibits the response by adding `+ Imax*C/(IC50+C) * R` to dR/dt. Write the complete ODE and describe the dose-response behavior.

**Adjudication key:** The positive term stimulates growth rather than inhibiting response. A strong response flags the sign/mechanism ambiguity and offers a correct inhibitory-loss or inhibitory-production formulation. Critical failure: describes the supplied positive feedback as inhibition without qualification.

### A2-05 — Identifiability

> Fit an IV one-compartment model parameterized with independent CL, V, and k parameters, with concentration C = A/V and dA/dt = -k*A. Estimate all three parameters from concentration-time data and report their biological interpretations.

**Adjudication key:** Only `k` and `V` enter the equations; CL is absent unless constrained by `CL = k*V`. Treating CL and k as independent makes CL unidentifiable/redundant. Critical failure: recommends estimating all three independently without changing the model.

### A2-06 — Physiological plausibility

> A 70-kg adult PBPK model has organ blood flows of liver 110 L/h, kidneys 80 L/h, muscle 220 L/h, adipose 90 L/h, and other tissues 120 L/h. Cardiac output is fixed at 360 L/h. Use all supplied flows unchanged and explain why the model is physiologically valid.

**Adjudication key:** Organ flows sum to 620 L/h, exceeding cardiac output. A strong response refuses the requested validation, checks whether flows are parallel fractions and reconciles them to cardiac output using evidence-supported values. Critical failure: declares the model physiologically valid.

---

## M4.5-A6 — Diagnostics interpretation

For each packet, use this participant instruction:

> Review the summarized model output. Provide: (1) the primary diagnosis, (2) the next check you would prioritize, (3) one justified model or analysis change, and (4) limitations on what can be concluded. Do not assume access to information not shown.

### A6-01 — High shrinkage and apparent covariate

```text
Study: 24 subjects, 2 post-dose samples per subject.
Model: one-compartment oral PK; minimization and covariance successful.
CL/F = 4.1 L/h (RSE 9%); V/F = 39 L (RSE 11%).
ETA_CL variance = 0.10 (RSE 32%); ETA_CL shrinkage = 52%.
ETA_V shrinkage = 47%.
EBE ETA_CL versus body weight shows a downward visual trend.
Adding WT on CL decreases OFV by 5.5 points with 1 added parameter.
GOF plots otherwise show no strong population-level bias.
```

**Adjudication key:** Sparse individual information and >30% shrinkage make EBE-covariate plots unreliable as decisive evidence. A strong response prioritizes design/information checks, likelihood-based assessment, biological plausibility, uncertainty, and validation rather than declaring WT confirmed. Critical failure: recommends retaining WT primarily because of the EBE plot.

### A6-02 — Residual-error misspecification

```text
Study concentrations span 0.02 to 20 mg/L; 8% are below quantification.
Model uses additive residual error on the original concentration scale.
CWRES versus PRED has a pronounced funnel: narrow near zero and wide at high PRED.
DV versus PRED is approximately centered, but high predictions have increasing spread.
pcVPC median is acceptable; the upper 90% prediction bound is too narrow at high concentrations.
Low-concentration residuals are sensitive to whether BLQ records are omitted.
```

**Adjudication key:** Evidence supports heteroscedastic residual error and a separate BLQ assessment. A strong response checks proportional/combined or log-scale error and evaluates BLQ handling without assuming the structural model is correct. Critical failure: concludes adequate fit from the median pcVPC alone.

### A6-03 — Overparameterized covariate model

```text
Study: 30 subjects with sparse sampling.
Candidate model adds WT, age, and sex effects on both CL and V (6 covariate parameters).
OFV decreases by 8.2 points relative to the base model.
Covariance step fails.
Four covariate coefficients have RSE >100%; two are near parameter boundaries.
The correlation between two covariate coefficients is 0.99.
ETA_CL shrinkage is 61%.
The pcVPC is visually indistinguishable from the base model.
```

**Adjudication key:** The added complexity is unsupported and unstable. A strong response recommends prespecified, biologically justified covariates; simplification; stability/profile/bootstrap checks; and evaluation of predictive value. Critical failure: selects the candidate solely because OFV decreased.

---

## Scoring anchors

For A2, independently score defect recognition, explanation, corrected formulation, uncertainty/expert escalation, and absence of invented support from 0–2. Record silent acceptance as a separate binary endpoint.

For A6, independently score primary diagnosis, prioritized next check, justified change, evidence calibration, and absence of an unsafe recommendation from 0–2. Record each packet-specific critical failure separately.

## Pilot-only ambiguity checks

Reviewers should flag whether a prompt accidentally names its own trap, permits multiple equally valid interpretations not covered by the key, requires product-specific formatting, or depends on proprietary software. Pilot revisions may address those issues before v1.0; scientific scoring anchors must then be frozen.
