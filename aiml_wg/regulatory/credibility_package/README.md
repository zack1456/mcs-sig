# Credibility Evidence Package

This package is a practical companion to the working group's papers. It helps a team make the evidence for an AI/ML-augmented pharmacometric model inspectable before the model is used to support a consequential decision.

## Intended use

Use the four templates together for a bounded **Context of Use (COU)**. They apply to hybrid mechanistic–ML PK/PD models and offline RL precision-dosing analyses; they are not a claim of regulatory compliance or a substitute for sponsor–regulator interaction.

## Contents

| File | Purpose |
| --- | --- |
| `context_of_use_template.md` | States the decision, population, model role, and consequence of being wrong. |
| `data_model_card_template.md` | Records data lineage, model structure, assumptions, and limitations. |
| `validation_evidence_matrix_template.md` | Maps claims to verification/validation evidence and acceptance criteria. |
| `lifecycle_change_log_template.md` | Records versioned changes, impact assessment, and requalification decisions. |
| `example_hybrid_pkpd.md` | Illustrative completed outline for an embedded neural-ODE PK/PD model. |
| `example_offline_rl.md` | Illustrative completed outline for an offline precision-dosing policy. |

## Alignment

The package operationalizes, rather than replaces, the risk-based credibility ideas in ASME V&V 40, ICH M15, FDA's draft AI guidance, and the FDA–EMA good-AI-practice principles. Evidence expectations should increase with model influence and decision consequence.
