# Example Outline — Hybrid PK/PD Model

**Illustrative only; not a validated model.**

- **COU:** Support exploratory dose-scenario comparisons in a development team; not direct patient dosing.
- **Model role:** A mechanistic two-compartment PK/PD model with a constrained neural residual component for persistent, structured error.
- **Evidence needed:** Mass-balance and solver verification; parameter and neural-component identifiability assessment; held-out calibration; temporal/site sensitivity analysis; comparison against the mechanistic baseline.
- **Risk control:** The neural component is disabled or escalated for review outside its documented applicability domain; no decision is based on a point prediction without uncertainty reporting.
