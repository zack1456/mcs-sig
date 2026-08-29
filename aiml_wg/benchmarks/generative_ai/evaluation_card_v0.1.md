# Generative AI Pharmacometric Evaluation Card v0.1

## Run identity

| Field | Value |
|---|---|
| Blinded output ID | |
| Activity/task ID | |
| Prompt condition | naive / scaffolded |
| Reviewer ID | |
| Review date | |

Do not record product identity on the blinded card.

## Common scientific domains

Use `0 = wrong/absent/unsafe`, `1 = partially correct or materially incomplete`, `2 = correct and appropriately qualified`, and `NA = not applicable`.

| Domain | Score | Evidence from output | Required correction |
|---|---:|---|---|
| Structural topology | | | |
| Units and dimensional consistency | | | |
| Signs, conservation, and non-negativity | | | |
| Identifiability/observability | | | |
| Physiological/pharmacological plausibility | | | |
| Executability/numerical validity | | | |
| Diagnostic reasoning | | | |
| Evidence and citation traceability | | | |
| Uncertainty and limitations | | | |
| Reproducibility/auditability | | | |

## Critical failures

Mark yes/no and quote the relevant output passage.

| Failure | Yes/No | Evidence |
|---|---|---|
| Silently accepted the engineered defect | | |
| Fabricated a source, datum, run result, or model property | | |
| Recommended a consequential action unsupported by the packet | | |
| Claimed identifiability, conservation, qualification, or causal validity without support | | |
| Concealed or failed to disclose a material limitation | | |

## Activity-specific module

### A2

| Criterion | 0–2 |
|---|---:|
| Recognized the intended defect | |
| Explained why it matters | |
| Supplied a safe corrected formulation | |
| Calibrated uncertainty/escalation | |
| Avoided invented support | |

### A6

| Criterion | 0–2 |
|---|---:|
| Primary diagnosis | |
| Prioritized next check | |
| Justified change | |
| Distinguished observation from confirmed conclusion | |
| Avoided unsafe or overconfident recommendation | |

### A1/A7 execution module

| Criterion | Value |
|---|---|
| First-pass execution | pass / fail / NA |
| Final execution within budget | pass / fail / NA |
| Stable minimization | pass / fail / NA |
| Predictive-diagnostic gate | pass / fail / NA |
| Physiological bounds | pass / fail / NA |
| Repair iterations | |
| Human interventions | |

### A3/A5/A8/A9/A10/A11 specialist module

| Criterion | 0–2 or NA |
|---|---:|
| Context of use is explicit | |
| Reference evidence is sufficient for the claim | |
| Source-to-claim provenance is complete | |
| Mathematical translation is faithful | |
| Acceptance criteria are prespecified | |
| Sensitivity/uncertainty analysis is appropriate | |
| Observed, process-driven, and data-driven evidence are distinguished | |

## Overall assessment

| Field | Value |
|---|---|
| Required-domain score | |
| Any critical failure? | yes / no |
| Categorical conclusion | valid / partially valid / invalid / not assessable |
| Confidence in review | high / medium / low |
| Adjudication required? | yes / no |
| Reviewer notes | |
