# Focused Search — Causal Offline RL and OPE Safety

**Date:** 2026-08-29  
**Purpose:** Support M3.7 and the RL framework paper.  
**Databases:** PubMed and primary full-text sources.

## Search concepts

```text
(offline reinforcement learning OR off-policy evaluation OR dynamic treatment policy)
AND (clinical OR healthcare OR dosing)
AND (safety OR confounding OR policy restriction OR transportability)
```

## Inclusion criteria

- Addresses evaluation or safety of learned policies from logged healthcare data.
- Adds a concrete concept missing from M3.6: policy restriction, cross-OPE, transportability, or causal identification assumptions.
- Does not substitute a generic RL result for pharmacometric evidence.

## Included records

- `roggeveen_2024_clinical_rl_ope` — cross-OPE, policy restriction, and individual-policy inspection.
- `adamson_2026_transportability` — transparent assumptions and uncertainty communication when extending evidence across settings.

## Processing

Roggeveen was processed to targeted sections because full text is available; Adamson was processed from the abstract. These sources augment rather than replace the existing healthcare-RL and OPE foundations.
