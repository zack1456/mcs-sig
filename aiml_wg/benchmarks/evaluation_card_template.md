# Evaluation Card

| Domain | Question | Metric / evidence | Prespecified criterion | Result | Caveat |
| --- | --- | --- | --- | --- | --- |
| Verification | Does the numerical implementation solve the intended system reliably? | tolerance/gradient checks |  |  |  |
| Identifiability | Can the claimed parameters/components be distinguished? | structural + practical analysis |  |  |  |
| Accuracy | Are predictions useful on held-out data? | error metric against baseline |  |  |  |
| Calibration | Does stated uncertainty match observed error? | coverage and sharpness |  |  |  |
| Transportability | Does performance hold under a prespecified shift? | temporal/external/shift analysis |  |  |  |
| Decision safety | Does use change a consequential decision safely? | unsafe action, utility, regret, or N/A |  |  |  |
| Reproducibility | Can the result be recreated? | provenance/version/environment record |  |  |  |
