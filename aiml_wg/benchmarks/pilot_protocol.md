# Validation Pilot Protocol

## Purpose

Test the working group's evaluation framework before committing to a public benchmark. This is a design pilot, not a claim of clinical readiness.

## Scope

| Element | Pilot choice |
| --- | --- |
| Known-truth case | Simulated one- or two-compartment PK/PD model with parameters, dosing, and observation process retained |
| Clinical case | One openly licensed PK dataset, selected only after provenance and license review |
| Comparator | Mechanistic baseline and one bounded hybrid residual/neural-ODE model |
| Outputs | Evaluation cards, provenance record, and a short lessons-learned note |

## Prespecified evaluation domains

1. **Verification:** solution/tolerance convergence and, where gradients are used, agreement with an independent numerical check.
2. **Identifiability:** structural argument where feasible; practical profile/FIM/sensitivity assessment under the proposed sampling design.
3. **Predictive validity:** held-out error and calibration/interval coverage with sharpness.
4. **Transportability:** temporal or site split where the data allow; otherwise an explicitly constructed covariate-shift stress test.
5. **Decision relevance:** for a dosing COU, report unsafe-action rate and utility/regret relative to the mechanistic baseline; otherwise mark this domain not applicable.
6. **Reproducibility:** data version, preprocessing, solver/tolerances, software, seed, hardware, and exact model version.

## Gates

- Dataset license and provenance are recorded before analysis begins.
- The mechanistic baseline is defined before hybrid tuning.
- Acceptance criteria are written before results are inspected.
- A public benchmark is considered only after the pilot is reviewed and a computational maintainer is named.
