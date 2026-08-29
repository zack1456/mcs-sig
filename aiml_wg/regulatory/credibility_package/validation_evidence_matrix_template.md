# Validation Evidence Matrix Template

| Claim | Evidence type | Dataset / scenario | Metric and acceptance criterion | Result | Limitation / residual risk | Reviewer | Version |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Numerical solution and gradients are reliable | Verification | Stiff and non-stiff test cases | Tolerance-convergence and independent-gradient agreement |  |  |  |  |
| Parameters/components are estimable | Structural/practical identifiability | Simulated truth + intended data design | Rank/profile/FIM criterion defined in advance |  |  |  |  |
| Predictions are calibrated for the COU | Validation | Held-out internal, temporal, and external cohorts | Error, calibration, and interval coverage/sharpness |  |  |  |  |
| Model remains applicable across relevant groups | Transportability | Prespecified site/time/subgroup strata | Shift diagnostics plus stratified performance |  |  |  |  |
| Recommended decisions are acceptably safe | Decision validation | Policy simulation or logged data | Unsafe-action rate, regret/utility, OPE uncertainty bound |  |  |  |  |
