# Project Memory — Generative AI Pharmacometric Benchmark

**Updated:** 2026-08-29
**Purpose:** Durable, checked-in context for future work on the Claude × Codex × Antigravity comparison. This is project documentation, not a substitute for the frozen protocol or expert decisions.

## Decisions already made

- Compare exact dated product configurations, not model brands in the abstract.
- Keep reasoning-only and execution-capable configurations distinguishable.
- Use naive and fixed scaffolded prompt conditions.
- Treat mathematical and pharmacological validity as primary; prose style is not a scientific endpoint.
- Use blinded expert review and preserve every independent run rather than selecting the best output.
- Keep open-ended literature discovery outside MCS. A8 starts from a locked, jointly curated evidence packet; AI/ML owns extraction methodology, QSP owns biological adjudication, and MCS owns mathematical translation and verification.
- A6 extends prior NONMEM-output work through engineered diagnostic traps, current product configurations, blinded review, and unsafe-recommendation scoring.
- Do not begin comparative data collection until the gates in `pilot_readiness.md` are satisfied.

## Considerations to retain

1. **Expert ambiguity review:** PBPK flow accounting and dual-compartment elimination prompts need specialist confirmation that the intended defect is unambiguous.
2. **Two comparison questions:** Report reasoning-only performance separately from workflow performance with product-specific execution and agent tools.
3. **Private holdout set:** Maintain unreleased prompt variants for definitive evaluation; publish them only after collection to reduce contamination risk.
4. **Human correction burden:** Capture modeler time, edit type/count, reruns, and whether errors are conspicuous or persuasive and hidden.
5. **Operational tooling:** Implement randomization, opaque-ID blinding, manifest capture, scoring ingestion, confidence intervals, and reviewer-agreement scripts before the pilot.
6. **Transpilation scope:** Decide whether the optional cross-platform transpilation task becomes M4.5-A12, remains explicitly deferred, or is removed from the formal portfolio.
7. **Adversarial provenance:** Add locked evidence packets containing conflicting claims, stale/retracted evidence, unsupported assertions, and document-level prompt injection.
8. **Model drift:** Freeze collection dates and preserve anchor tasks for later reruns; never generalize results beyond the dated configuration.
9. **Statistical intent:** Decide whether the first comparison is descriptive or confirmatory before fixing replicate counts, hypotheses, multiplicity, and mixed-effects analyses.
10. **Governance:** Name the benchmark owner, prompt custodian, blinded-output custodian, adjudicator, analysis owner, and version-maintenance owner.

## Recommended next work

1. Obtain two-pharmacometrician calibration and sign-off for A2/A6.
2. Resolve prompt ambiguity and freeze Phase 1 materials as v1.0.
3. Implement the run, randomization, blinding, and analysis utilities.
4. Register exact Claude, Codex, and Antigravity configurations.
5. Conduct a quarantined design pilot before any comparative claim.

## Evidence caveat

`jiang_2024_synthetic_pkpd` remains abstract-only pending licensed full-text access. Do not upgrade claims from that record without recording the additional reading depth and evidence location.
