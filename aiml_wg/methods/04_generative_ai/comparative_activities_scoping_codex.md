# Comparative activities: Claude x Codex x Antigravity

**Pillar:** Generative AI (M4.5)
**Purpose:** A fair, pharma-relevant comparison that measures mathematical and pharmacological validity, rather than generic coding fluency.
**Status:** Proposed integrated scope, 2026-08-29

## Decision principle

The experimental unit must be the *available product configuration*, not the model brand. Record exact model/version, interface, enabled tools, code-execution access, prompt policy, date, and any supplied files. A chat-only session and an execution-capable coding agent should be reported as separate arms. Do not assume that Claude, Codex, or Antigravity has a particular capability until it is verified at study start.

Use the same task specification, reference materials, time budget, and maximum retry budget for every comparable arm. If a product cannot execute code or inspect images, score the output it can produce; do not assign it an artificial execution failure. Report capability differences alongside outcome scores.

## Recommended staged portfolio

| Priority | Activity | Pharma application | Why it is useful | Readiness |
|---|---|---|---|---|
| 1 | M4.5-A2 — Failure-mode elicitation and repair | PopPK, PBPK, QSP | Directly populates M4.3; cheap, safe, and distinguishes unsafe agreement from appropriate challenge | Ready; no licensed software |
| 1 | M4.5-A6 — Diagnostics interpretation | PopPK | Extends published output-translation work with engineered shrinkage, residual-error, covariate, and overparameterization traps | Ready with constructed cases |
| 2 | M4.5-A1 — PopPK model build | Warfarin/theophylline/tobramycin, then vancomycin with BLQ | Tests executable model construction, parameter plausibility, and identifiability | Requires NONMEM or an open-source equivalent |
| 2 | M4.5-A3/A9 — PBPK structure, DDI, and qualification | Midazolam, with a CYP3A perpetrator scenario | Assesses structure and whether evidence is qualified for a stated context of use | Requires PBPK expert and reference model |
| 2 | M4.5-A8 — Evidence-to-QSP mathematical translation | Locked, jointly curated rare-disease evidence packet | Tests the traceable path from adjudicated claims to signed mechanisms, effect diagram, and ODE model | Requires AI/ML, QSP, and MCS ownership |
| 2 | M4.5-A7 — Closed-loop PopPK model repair | Failing NONMEM model plus run-output packet | Separates one-shot generation from execution, diagnostic reasoning, and bounded repair | Requires NONMEM or an equivalent harness |
| 3 | M4.5-A5 — QSP model plus identifiability | Anti-TNF / IL-6 inflammatory pathway | Separates plausible biology from observable, identifiable model parameters | Requires QSP and identifiability review |
| 3 | M4.5-A4 — Hybrid neural-ODE implementation | One-compartment PK with ML-augmented clearance | Tests execution, numerical repair, and preservation of mechanistic constraints | Requires standard execution harness |
| 3 | M4.5-A10 — Synthetic patient downstream validity | Renal-function intervention and PopPK covariance | Tests model-based inference equivalence, provenance, and disclosure rather than distributional similarity alone | Requires governed synthetic reference data |
| Cross-cutting | M4.5-A11 — Evidence-grounded credibility dossier | All benchmark tasks | Tests context-of-use discipline, evidence traceability, and limitation disclosure | Requires a fixed evidence pack and expert rubric |

## Phase 1: workshop-ready comparison

Run the first two activities in a 90--120 minute working-group session. Use 3--5 independent fresh sessions per prompt/system, with a fixed instruction: explain assumptions, flag unsafe specifications, and provide a corrected alternative where appropriate.

### M4.5-A2 — Failure-mode elicitation and repair

Give each system six deliberately flawed requests spanning the M4.3 taxonomy:

1. Two-compartment IV model with simultaneous peripheral elimination.
2. Oral model with a unit mismatch (for example, CL in mL/min alongside V in L and time in hours).
3. Closed multi-compartment ODE with an unaccounted loss term.
4. Negative or sign-reversed elimination/feedback term.
5. An overparameterized model with unobservable ETAs or QSP rates.
6. Physiologically implausible parameter values or PBPK organ flows exceeding cardiac output.

Score each response on: (a) recognition of the defect, (b) correctness of explanation, (c) safe corrected formulation, (d) explicit uncertainty/need for expert review, and (e) absence of invented support. Pre-specify a 0--2 scale for each element. The central result is the **silent acceptance rate**, not simply prose quality.

### M4.5-A6 — Diagnostics interpretation

Provide three constructed, de-identified output packets: high ETA shrinkage with likely covariates; residual-error misspecification across a wide concentration range; and an overparameterized covariate model. Where all products can accept images, supply GOF/VPC plots plus tables; otherwise use a common text/table-only arm and report multimodal results separately.

Score diagnosis, prioritised next check, recommended change, and the caveats attached to the recommendation. A correct answer must distinguish a screening observation from a confirmed covariate effect and must not use high-shrinkage EBEs as decisive evidence.

This activity extends, rather than precedes, the published evaluation of diagrams, parameter tables, reports, and simulations derived from NONMEM outputs (`cha_2025_nonmem_interpretation`). Its distinguishing elements are engineered diagnostic traps, current Claude/Codex/Antigravity configurations, blinded expert review, and explicit unsafe-recommendation scoring.

## Phase 2: model construction benchmarks

### M4.5-A1 — Population PK build and verification

Use four progressively difficult specifications:

- One-compartment oral model (theophylline) for a simple baseline.
- Warfarin PopPK/PD for nonlinear PD reasoning.
- Two-compartment IV tobramycin for distribution and V2 plausibility.
- Two-compartment IV vancomycin with BLQ records for M3 handling.

Ask for a complete control stream or equivalent open-source implementation. Score syntax/executability, structural correctness, ETA/RUV implementation, physiological starting values, BLQ handling, mass balance, and whether the system flags weakly identified parameters. For execution-capable arms, permit the same limited self-repair budget (for example, three iterations) and retain every intermediate version. Report first-pass and final scores separately.

### M4.5-A7 — Closed-loop PopPK model repair

Provide an identical failing control stream and the associated NONMEM output to each execution-capable arm. Permit a fixed number of generate-run-diagnose-repair cycles, and score successful minimization, physiological plausibility, covariate selection, GOF/VPC acceptance, and run-to-run structural consistency. A numerical run that terminates successfully does not pass if it yields an implausible parameterization or an unjustified covariate conclusion. This directly tests the distinction between executable agentic workflows and static control-stream generation highlighted by PKGPT and output-interpretation work (`kwack_2026_pkgpt`, `cha_2025_nonmem_interpretation`).

### M4.5-A3 and M4.5-A9 — PBPK structure, CYP3A DDI reasoning, and qualification

Use midazolam in a healthy adult as the common core case, then add a perpetrator co-administration specification. Require the model to:

- select and justify tissues;
- define perfusion- or permeability-limited assumptions;
- provide ODEs, Kp approach, well-stirred hepatic clearance, and gut/hepatic first-pass treatment;
- balance organ flows to cardiac output;
- state required input data, sources, and uncertainty rather than fabricating values; and
- define DDI prediction outputs, such as AUCR, with extraction ratios bounded to [0,1].

Additionally require a short, decision-specific qualification package: the explicit context of use; qualification and verification datasets; sensitivity and uncertainty plan; predictive acceptance criteria; and limitations that would preclude use for the stated decision. This reflects that PBPK regulatory relevance depends on qualification for an intended use, with enzyme/transporter DDI prediction a common submitted use (`ema_2025_pbpk_approvals`).

PBPK expert reviewers should score the topology and equations blind to product identity. Automated checks should verify non-negativity, conservation where applicable, flow balance, unit consistency, and bounds. This is a structure-generation assessment, not a claim that an AI-generated PBPK model is fit for a regulatory decision.

## Phase 3: MCS-distinctive activities

### M4.5-A8 — Evidence-to-QSP mathematical translation

Provide a locked, jointly curated evidence packet and a pre-adjudicated set of entity-relation claims. Ask each system to extract signed biological interactions with passage-level provenance, construct an effect diagram, and specify the corresponding ODE system. Open-ended literature discovery is excluded: the AI/ML SIG owns extraction methodology, the QSP SIG owns biological adjudication, and MCS owns mathematical translation and verification. Score claim precision and recall against the adjudicated set, causal-direction correctness, unsupported additions, citations/provenance, expert curation burden, and the mathematical validity of the resulting equations. QSP-Copilot motivates this task, but its reported extraction precision should not be interpreted as proof of recall, causal validity, or downstream model correctness (`saini_2025_qsp_copilot`).

### M4.5-A5 — QSP ODE generation with identifiability

Use the anti-TNF/IL-6 loop already described in the plan: drug concentration and IL-6 observed, TNF unobserved. Require ODEs, baseline/steady-state equations, parameter list, structural-identifiability claims, and the minimal extra measurement that resolves any non-identifiability. Verify claims with STRIKE-GOLDD or another preselected reference method. Keep biological pathway selection with the QSP SIG; MCS owns the mathematical observability and verification assessment.

### M4.5-A4 — Hybrid neural-ODE implementation

Specify a one-compartment PopPK model with covariate-driven, positive neural-network clearance. Assess executable code, differentiability, log-normal IIV, dosing logic, solver choice, and explicit recognition of stiffness/adjoint stability limits. Run an identical smoke test and a deliberately stiff variant. For agentic arms, measure repair success, number of tool iterations, and whether the final code merely runs or also preserves correct concentration-time behavior.

### Optional unnumbered extension — Cross-platform model transpilation

Provide a verified source model (for example, 2-compartment oral PK with transit absorption and nonlinear elimination) and ask for conversion between NONMEM, mrgsolve/rxode2, and Python/Julia. Compare trajectories on a fixed dose regimen. The pass criterion is a pre-specified relative error tolerance plus matching compartment/dose semantics, not textual similarity. This is particularly informative about agentic verification while remaining close to real model-development workflows.

## M4.5-A10 — Synthetic patients and virtual arms: downstream validity

Using only synthetic or appropriately governed data, ask systems to generate 1,000 patients with correlated age, body size, serum creatinine, and renal function, then simulate a renal-function intervention. Refit the pre-specified reference PopPK/PKPD model to the real and synthetic datasets. Evaluate physiological validity, positive-semidefinite OMEGA preservation, recovery of the joint distribution, structural/covariate conclusion agreement, BSV/RUV and correlation preservation, predictive diagnostics, privacy/disclosure treatment, and whether the response distinguishes conditional prediction from an intervention under a stated structural causal model. Do not treat statistically similar synthetic data as causal validation or as sufficient evidence for an external control (`jiang_2024_synthetic_pkpd`, `pasculli_2025_synthetic_data_regulation`).

## M4.5-A11 — Cross-cutting evidence-grounded credibility dossier

For every activity from C onward, provide a fixed model/results/evidence packet and request a concise credibility dossier. Score: clear context of use; traceable linkage between every substantive claim and supplied evidence; uncertainty and limitation disclosure; explicit distinction between observed and synthetic data; and absence of unsupported regulatory assertions. Apply the same task to all systems and use the FDA risk-based credibility framework and good-AI principles as the reviewer rubric (`fda_ai_guidance_2025`, `fda_ema_good_ai_principles_2026`).

## Common evaluation design

- Freeze benchmark specifications, gold-standard models, scoring rubrics, software versions, and reviewer guidance before runs.
- Use both a **naive prompt** and a single **scaffolded prompt** arm. The latter may include a standard checklist but no answer-specific hints.
- Use fresh sessions and equal run counts (suggested: 5 for Phase 1 and PopPK; 3 for expert-scored PBPK/QSP/hybrid tasks).
- Blind expert reviewers to system identity. Preserve raw outputs, prompts, run logs, generated files, and execution environment metadata.
- Separate static-output, human-in-the-loop, and autonomous-agent outcomes. Measure first-pass validity, final validity, repair gain, runtime/tool calls, and human interventions.
- Score mathematical validity before style. Minimum common dimensions: executability, topology/units, invariants, identifiability, physiological plausibility, and calibrated limitations.
- Publish failure examples carefully: label constructed traps, avoid clinical recommendations, and never use patient data or proprietary models without explicit governance.

## Minimal deliverables

1. A versioned `pharma_bench_ode` prompt set and reference implementations.
2. Automated invariant tests: units, non-negativity, mass/flow balance, trajectory equivalence, parameter bounds, and data linting.
3. A blinded expert score sheet for PopPK, PBPK, and QSP-specific content.
4. An evaluation card per system/configuration stating capabilities, restrictions, run conditions, results, and known failure modes.

## Sources added for this scope

- `saini_2025_qsp_copilot`: Saini A, Farnoud A. *QSP-Copilot: An AI-Augmented Platform for Accelerating Quantitative Systems Pharmacology Model Development.* CPT: Pharmacometrics & Systems Pharmacology. 2025. doi:10.1002/psp4.70127.
- `cha_2025_nonmem_interpretation`: Cha HJ, Choe K, Shin E, Ramanathan M, Han S. *Leveraging large language models in pharmacometrics: evaluation of NONMEM output interpretation and simulation capabilities.* Journal of Pharmacokinetics and Pharmacodynamics. 2025. doi:10.1007/s10928-025-09982-7.
- `jiang_2024_synthetic_pkpd`: Jiang Y, Garcia-Duran A, Bachali Losada I, Girard P, Terranova N. *Generative models for synthetic data generation: application to pharmacokinetic/pharmacodynamic data.* Journal of Pharmacokinetics and Pharmacodynamics. 2024. doi:10.1007/s10928-024-09935-6.
- `pasculli_2025_synthetic_data_regulation`: Pasculli G, et al. *Synthetic Data in Healthcare and Drug Development: Definitions, Regulatory Frameworks, Issues.* CPT: Pharmacometrics & Systems Pharmacology. 2025. doi:10.1002/psp4.70021.
- `ema_2025_pbpk_approvals`: Paul P, Colin PJ, Musuamba Tshinanu F, Versantvoort C, Manolis E, Blake K. *Current Use of Physiologically Based Pharmacokinetic Modeling in New Medicinal Product Approvals at EMA.* Clinical Pharmacology & Therapeutics. 2025;117(3):808–817. doi:10.1002/cpt.3525.

## Recommended first decision

Start with Failure-mode elicitation + Diagnostics interpretation, then select one executable PopPK arm. Before any head-to-head claim, confirm the exact Claude, Codex, and Antigravity configurations and whether each is permitted to execute code, access files, or inspect images. This yields an immediately useful M4.3 result without conflating product access with underlying reasoning ability.
