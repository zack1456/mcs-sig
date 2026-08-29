# Example Outline — Offline RL Precision-Dosing Policy

**Illustrative only; not a validated policy.**

- **COU:** Rank candidate dosing policies for further simulation/prospective study; not autonomous clinical recommendation.
- **Data boundary:** Historical treatment trajectories or a qualified PK/PD simulator; the behavior policy and action support must be described.
- **Evidence needed:** State/MDP definition; confounding and positivity assessment; policy constraints; OPE using more than one estimator where feasible; uncertainty bounds; patient-level policy inspection; prospective-validation trigger.
- **Risk control:** Restrict actions to clinically permissible ranges and reject policies that rely on poorly supported actions or fail uncertainty/safety thresholds.
