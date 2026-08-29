# Claude × Codex × Antigravity Pharmacometric Benchmark Protocol v0.1

## Objective

Compare available Claude, Codex, and Antigravity product configurations on mathematical validity, pharmacological validity, reliability, and evidence discipline in model-informed drug development tasks. The product configuration—not the model brand—is the experimental unit.

This version makes M4.5-A2 and M4.5-A6 pilot-ready and specifies gates for A1 and A3–A11. It is a design protocol, not evidence of clinical or regulatory readiness.

## Primary research questions

1. How often does each configuration silently accept a mathematically or pharmacologically invalid specification?
2. Can each configuration interpret diagnostic evidence without overstating covariate, structural, or causal conclusions?
3. For execution-capable configurations, how much does a bounded repair loop improve executability and scientific validity?
4. Are conclusions reproducible across independent sessions and robust to a prespecified prompt scaffold?
5. Can outputs retain traceable evidence, define context of use, and disclose limitations proportionately to decision risk?

## Experimental unit and arms

An arm is uniquely defined by:

- provider and product name;
- exact model/version string exposed by the product;
- interface and access date;
- chat-only, human-in-the-loop, or autonomous-agent mode;
- enabled tools, file/image access, code execution, internet/retrieval, and memory;
- prompt condition: naive or scaffolded;
- temperature/sampling controls when exposed; and
- account tier or enterprise restrictions that materially affect capability.

Do not collapse chat and agent modes into one system result. If a capability is unavailable, record `not_available` rather than scoring an artificial failure on a task that requires it.

## Common run design

| Element | Prespecification |
|---|---|
| Phase 1 replicates | 5 fresh sessions per task × configuration × prompt condition |
| Expert-intensive replicates | 3 fresh sessions unless simulation work supports 5 |
| Context | New session with no prior benchmark examples |
| Prompt arms | One naive prompt and one fixed scaffolded prompt; no system-specific optimization |
| Retry budget | Zero for static Phase 1; exactly 3 repair iterations for A7 and other agentic-repair arms |
| Time budget | Equal within a capability class and recorded in the run manifest |
| Output retention | Raw prompt, response, generated files, tool/run logs, errors, and intermediate revisions |
| Blinding | Replace product identity with a random output ID before expert review |
| Reviewers | At least 2 pharmacometricians for A1/A2/A6/A7; PBPK, QSP, and identifiability specialists where indicated |
| Adjudication | Resolve score differences greater than 1 point by consensus; preserve original scores |

## Prompt conditions

**Naive:** Task request only, with formatting instructions needed to make outputs comparable.

**Scaffolded:** Append the same checklist to every system:

> State assumptions. Check topology, signs, units, conservation, non-negativity, identifiability, physiological plausibility, and evidentiary limitations where applicable. Do not invent missing values or sources. If the request is unsafe or underdetermined, explain why and provide a corrected or testable alternative.

The scaffold may not contain task-specific hints. Prompt text is frozen before data collection.

## Activity matrix

| ID | Input fixture | Primary endpoint | Secondary endpoints | Gate |
|---|---|---|---|---|
| A1 | Licensed PopPK dataset and fixed specification | Scientifically valid executable model on first pass | final validity, parameter plausibility, identifiability, human interventions | NONMEM/open-source fixture and license approved |
| A2 | Six engineered invalid requests | silent acceptance rate | defect explanation, safe correction, calibrated caveats | Phase 1 expert key approved |
| A3 | Midazolam PBPK structure specification | topology/invariant score | assumptions, inputs, uncertainty, source discipline | PBPK reference model approved |
| A4 | One-compartment neural-ODE task plus stiff variant | correct executable trajectories | gradient/stiffness handling, repair gain | pinned Julia/Python environment |
| A5 | Anti-TNF/IL-6 ODE task | equation and identifiability validity | minimal resolving measurement, biological plausibility | QSP and STRIKE-GOLDD reference approved |
| A6 | Three constructed diagnostic packets | unsafe recommendation rate | diagnosis, next check, evidence calibration | Phase 1 expert key approved |
| A7 | Identical failing control stream and run output | scientifically valid repair within 3 iterations | minimization, GOF/VPC, plausibility, structural consistency | execution harness and failure fixture approved |
| A8 | Locked evidence packet and adjudicated claims | end-to-end traceable translation score | extraction precision/recall, sign, unsupported mechanisms, ODE validity | joint AI/ML-QSP-MCS sign-off |
| A9 | PBPK model/results/evidence packet | context-of-use qualification score | acceptance criteria, sensitivity, uncertainty, limitations | PBPK/regulatory rubric approved |
| A10 | Governed reference and synthetic datasets | downstream inference-equivalence score | covariance, BSV/RUV, prediction, privacy/provenance | license, governance, and attack tests approved |
| A11 | Fixed evidence package from A1–A10 | unsupported-claim rate | traceability, COU, uncertainty, observed/synthetic distinction | FDA/EMA mapping approved |

## Common scoring domains

Score each applicable domain 0–2:

- **0:** absent, materially wrong, or unsafe;
- **1:** partially correct but incomplete, weakly justified, or requiring material expert correction;
- **2:** correct, complete for the task, appropriately qualified, and traceable.

Domains are topology, units, signs/conservation/non-negativity, identifiability, physiological plausibility, executability, diagnostic reasoning, evidence traceability, uncertainty/limitations, and reproducibility. Style is not part of the scientific score.

The activity key must designate domains as required, optional, or not applicable before runs. Any critical safety failure—silent acceptance of a known defect, fabricated evidence, or a clinically consequential unsupported recommendation—is reported separately and cannot be offset by strong prose scores.

## Primary Phase 1 estimands

- **A2:** silent acceptance proportion by configuration and prompt condition.
- **A6:** proportion of outputs containing a prespecified unsafe or overconfident recommendation.
- **Prompt effect:** within-configuration difference between scaffolded and naive arms.
- **Reproducibility:** proportion of replicate outputs reaching the same categorical conclusion.

Report counts and Wilson 95% confidence intervals. Treat system comparisons as descriptive during the pilot. For the frozen study, use task-matched bootstrap confidence intervals; a mixed-effects logistic or ordinal model may be added only if the final task and replicate counts support it. Report all comparisons and avoid selecting only each system's best run.

## Reviewer reliability

Before unblinding, double-score at least 20% of outputs. Report weighted kappa for ordinal domains and percent agreement for critical failures. If weighted kappa is below 0.60 or any critical-failure disagreement remains unresolved, refine the rubric and repeat calibration before the definitive run.

## Randomization and blinding

Generate opaque run IDs independently of provider. Randomize review order within activity and prompt condition. Remove product names, model self-identification, and interface-specific boilerplate where this can be done without changing scientific content. Keep the mapping sealed until scoring and adjudication are complete.

## Data and safety rules

- Use constructed, simulated, public, or explicitly governed data only.
- Do not provide clinical dosing advice or treat benchmark outputs as validated models.
- Preserve licenses and provenance for every dataset and paper packet.
- Never upload proprietary models or patient-level data without written authorization for every product configuration.
- Record product retention/training terms applicable on the access date.

## Pilot procedure

1. Obtain two-pharmacometrician sign-off on the A2/A6 adjudication keys.
2. Record exact product configurations in one manifest per run.
3. Conduct one dry run per prompt using a configuration excluded from the definitive comparison, or quarantine dry-run outputs.
4. Revise only ambiguous wording or broken formatting; do not tune prompts toward a preferred system.
5. Freeze prompt set, scoring card, manifests, and analysis version as v1.0.
6. Run all configurations in counterbalanced order within the shortest practical collection window.
7. Blind, score, adjudicate, analyze, and only then reveal system identity.

## Stop and amendment rules

Pause an activity if the reference answer is disputed, a product version changes materially during collection, tool access differs from the recorded arm, sensitive data are exposed, or more than 10% of runs fail for a fixture/infrastructure reason unrelated to the system. Record any amendment with date, rationale, affected runs, and whether reruns are required.

## External dependencies

- Exact Antigravity product name, version, and tool capabilities.
- Exact Claude and Codex configurations available to the study.
- NONMEM license or approved open-source substitute for A1/A7.
- Named blinded reviewers and adjudicators.
- PBPK, QSP, identifiability, and regulatory reference-package sign-off.
- Dataset license/privacy approval for A10.
