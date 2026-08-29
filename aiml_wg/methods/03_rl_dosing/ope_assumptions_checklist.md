# Offline RL / OPE Assumptions Checklist

- [ ] Is the Context of Use research-only, development-supporting, or clinically consequential?
- [ ] Are the target population, policy, outcome, horizon, and estimand specified?
- [ ] Are clinically relevant state variables measured sufficiently to address time-varying confounding?
- [ ] Does logged data support every action the proposed policy may take (positivity/support)?
- [ ] Are action bounds and hard safety constraints encoded before policy optimization?
- [ ] Are OPE estimator selection, uncertainty intervals, and sensitivity analyses prespecified?
- [ ] Is policy performance inspected across meaningful patient/site/time strata?
- [ ] Is a next-stage validation trigger stated before results are interpreted as actionable?
