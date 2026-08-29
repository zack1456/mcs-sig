# Generative AI Benchmark Pilot Readiness

**Assessment date:** 2026-08-29
**Current decision:** Do not begin comparative data collection yet. The design artifacts exist, but expert sign-off and product-configuration registration remain mandatory gates.

## Completed

- [x] Activities use consistent M4.5-A1 through A11 identifiers in the plan and Codex scope.
- [x] A8 is bounded to a locked evidence packet with AI/ML, QSP, and MCS ownership defined.
- [x] A6 acknowledges the prior NONMEM-output benchmark and states the intended extension.
- [x] Five new literature records are enriched, indexed, and linked to their activities.
- [x] Focused-search queries, inclusion/exclusion criteria, included sources, and limitations are recorded.
- [x] Common protocol, Phase 1 prompts, adjudication keys, scoring card, and run-manifest schema are drafted.
- [x] Repository JSON parsing, source-index resolution, required-field checks, citation-ID resolution, and whitespace checks pass.

## Required before the Phase 1 design pilot

- [ ] Two pharmacometricians approve or amend all A2 and A6 adjudication keys.
- [ ] Reviewers confirm that no prompt has an unintended alternative interpretation.
- [ ] Exact Claude product/model/interface/tool configuration is recorded.
- [ ] Exact Codex product/model/interface/tool configuration is recorded.
- [ ] Exact Antigravity product name, model/version, interface, and tool configuration is recorded.
- [ ] Product data-retention and training terms are acceptable for the constructed benchmark inputs.
- [ ] A randomization/blinding custodian is named.
- [ ] Run time limits and collection dates are fixed.

## Required before a definitive Phase 1 comparison

- [ ] Conduct a quarantined dry run and revise only ambiguous wording or broken formatting.
- [ ] Freeze prompts, keys, scoring card, run-manifest schema, and analysis plan as v1.0.
- [ ] Calibrate reviewers and obtain weighted kappa of at least 0.60 on ordinal domains.
- [ ] Resolve all critical-failure scoring disagreements before unblinding.
- [ ] Decide whether the study is descriptive or powered for specified pairwise comparisons.
- [ ] Register any confirmatory hypotheses and multiplicity approach before collecting definitive outputs.

## Later-phase dependencies

- [ ] NONMEM license or approved open-source equivalent plus fixed A1/A7 fixtures.
- [ ] PBPK expert, reference midazolam model, and qualification evidence packet for A3/A9.
- [ ] QSP and identifiability experts plus a verified reference system for A5.
- [ ] Jointly curated and adjudicated evidence packet for A8.
- [ ] Pinned Julia/Python environment and reference trajectories for A4.
- [ ] Governed dataset, provenance/license approval, and privacy-attack specification for A10.
- [ ] Regulatory reviewer approval of the A11 credibility rubric.
- [ ] Licensed full-text review of `jiang_2024_synthetic_pkpd`, if available, before publication-facing synthesis.

## Repository handoff

The new Codex scoping file, five source records, search record, and benchmark package are currently working-tree changes. Stage and commit them only after review; no commit was created during protocol development.
