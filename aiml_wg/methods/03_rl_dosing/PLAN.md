# Methods · Optimal Control ↔ Reinforcement Learning for Precision Dosing (Pillar 3)

<!-- Updated 2026-08-29 by Codex: added M3.7 on causal validity and safety for offline RL. -->

**What this folder is:** Working notes and mathematical development for the RL-as-optimal-control framework in pharmacometric precision dosing. Feeds into `deliverables/papers/rl_framework/`.

**Scope:** The mathematical connection between classical optimal control and RL; pharmacometric requirements for MDP formulation (states, actions, rewards, safety); case study analysis of De Carlo et al. and Ribba.

---

## Method workstreams

### M3.1 — Mathematical relationship: classical optimal control ↔ RL
*RL is not just "trial and error" — it is a computational approach to the same problem classical optimal control solves analytically*

- [ ] **Classical optimal control:** Pontryagin's minimum principle (necessary conditions), Hamilton-Jacobi-Bellman (HJB) equation (sufficient, dynamic programming)
- [ ] **Model Predictive Control (MPC):** receding horizon, explicit model required — current PMx precision dosing standard
- [ ] **Tabular Q-learning:** discretized state/action spaces; Bellman equation as finite approximation to HJB; convergence theorem (Watkins & Dayan 1992)
- [ ] **Policy gradient methods:** continuous state/action; differentiable policy; connects to gradient descent on the value function
- [ ] **Key mapping to produce:** table showing state/action/value function/optimality condition for each approach — the central figure of the framework paper

Key source: `ribba_2023` ("RL is at the crossroads of trial-and-error learning and optimal control")

**Working notes file:** `control_rl_mapping.md`

---

### M3.2 — MDP formulation for PK/PD precision dosing
*How do pharmacometric concepts translate into MDP components?*

- [ ] **State space:** what biomarkers to include; discretization vs. continuous; how does state dimension affect tractability?
  - De Carlo 2024 (erdafitinib): 86 states, 1 biomarker ([PO4]serum, 6 levels) × dose × interruption flag
  - De Carlo 2025 (givinostat): 487 states, 3 biomarkers (PLT, WBC, HCT) — multiobjective
  - State explosion: how to handle high-dimensional biomarker spaces without 487 → 10^6+ states?
- [ ] **Action space:** dose levels vs. dose adjustments; continuous vs. discrete; constraint handling
- [ ] **Transition dynamics:** PK/PD model as environment; stochastic vs. deterministic transitions; role of RUV
- [ ] **Mathematical analysis:** what properties of the PK/PD ODE determine tractability of the MDP?

**Working notes file:** `mdp_formulation_notes.md`

---

### M3.3 — Reward function design grounded in pharmacology
*Current reward functions are designed ad hoc — what are the mathematical principles?*

- [ ] De Carlo 2024 reward: `R = β₁·g([PO4]) + β₂·h([PO4])` (piecewise biomarker level + % time in range)
  - β₁=10, β₂=5 chosen by authors — what mathematical principle guides this?
- [ ] De Carlo 2025: multiobjective reward (3 simultaneous endpoints) — reward aggregation problem
- [ ] Connection to pharmacological objective functions: time in therapeutic range, AUC targets, toxicity avoidance as constraint vs. penalty
- [ ] Formal candidates:
  - Utility theory: patient-level utility function over health outcomes → reward
  - Lexicographic optimization: safety first, efficacy second (constraint hierarchy)
  - Pareto front: multiobjective Q-learning without reward aggregation
- [ ] Open problem: can reward function design be made systematic from a PK/PD target product profile?

**Working notes file:** `reward_design_notes.md`

---

### M3.4 — Safety constraints and POMDP extension
*How to enforce pharmacological safety constraints; how to handle uncertainty in patient state*

- [ ] Safety constraints: dose limits, washout requirements, toxicity hard stops
  - As penalty terms in reward (soft constraint — can be violated)
  - As constraint sets on the MDP action space (hard constraint — never violated)
  - Constrained MDP (CMDP) formulation: Lagrangian relaxation
- [ ] POMDP (Partially Observable MDP): needed when patient state is not fully observed
  - De Carlo 2024 limitation: *"Individual PK-PD parameters assumed fully known from treatment start"*
  - POMDP approach: patient state is a hidden variable; observations are monitoring measurements
  - Bayesian filtering (Kalman, particle filter) for online state estimation
- [ ] Connection to Pillar 2 (UQ): state uncertainty is an epistemic UQ problem — feeds `methods/02_uq/`

**Working notes file:** `safety_pomdp_notes.md`

---

### M3.5 — Case study analysis: De Carlo & Ribba papers
*Extract generalizable lessons from existing RL+PMx implementations*

- [ ] **Erdafitinib (De Carlo 2024):**
  - What generalizes: 86-state design methodology, two-term reward structure, digital twin training paradigm
  - What doesn't generalize: β1/β2 values, state discretization levels — drug-specific
  - Key finding: QL chose 8 mg/day starting dose in only 23.40% — personalization of initial dose critical

- [ ] **Givinostat (De Carlo 2025):**
  - What generalizes: population QL-agent as a weaker baseline (79% vs 93% CHR); personal agents dominate
  - Computational barrier: 26–52 days training on 8-core i7 — what architectural changes would reduce this?
  - Key finding: QL-pop learned the same rule as clinical protocol for in-range patients — RL can rediscover clinical knowledge

- [ ] **Ribba 2023:**
  - Propofol >16M solution space justifies RL over heuristic search
  - Three-domain framing (dosing, digital health, computational psychiatry) — broadens Pillar 3 scope

**Working notes file:** `case_study_analysis.md`

---

### M3.6 — Offline (Batch) RL and Off-Policy Evaluation (OPE)
*Learning and validating precision dosing policies without live clinical exploration* <!-- Added 2026-08-29 (Antigravity review) -->

- [ ] **Ethical & Clinical Imperative:** Live exploration on patients is unethical; dosing policies must be learned offline from historical trial/EHR logs or validated mechanistic simulators (`gottesman_2019_rl_healthcare`)
- [ ] **Offline RL Algorithms for Dosing:** Mitigating distributional shift and out-of-distribution action extrapolation using Conservative Q-Learning (CQL) and policy-constrained actor-critic (`levine_2020_offline_rl`)
- [ ] **Off-Policy Evaluation (OPE):** Statistically evaluating proposed dosing policies from logged observational data via Doubly Robust (DR) and Weighted Doubly Robust estimators with high-confidence safety bounds (`thomas_2016_ope`)
- [ ] Connection to Regulatory: OPE as a formal mathematical submission artifact proving policy safety before prospective trial initiation

Key sources: `gottesman_2019_rl_healthcare`, `levine_2020_offline_rl`, `thomas_2016_ope`

**Working notes file:** `offline_rl_ope_notes.md`

---

### M3.7 — Causal validity and safety of offline RL
*When can evidence from historical treatment trajectories support a proposed dosing policy?*

- [ ] Define the target policy, target population, decision horizon, and estimand before choosing an RL algorithm
- [ ] Diagnose treatment-confounding risks, missing state information, and positivity/action-support failures in logged data
- [ ] Specify clinically permissible action constraints and reject policies that depend on unsupported actions
- [ ] Use OPE uncertainty intervals and sensitivity analyses; compare estimators where feasible rather than treating one estimate as proof
- [ ] Define prospective-validation or simulation-qualification triggers before a policy can advance beyond research use

Key sources: `gottesman_2019_rl_healthcare`, `thomas_2016_ope`, `roggeveen_2024_clinical_rl_ope`, `adamson_2026_transportability`

**Working notes files:** `causal_offline_rl_notes.md`, `ope_assumptions_checklist.md`

---

## Key sources
| Source | Workstream | Added / Role |
|---|---|---|
| `sources/papers/ribba_2023.json` | M3.1, M3.5 | RL in precision dosing framework |
| `sources/papers/de_carlo_2024.json` | M3.2, M3.3, M3.4, M3.5 | Erdafitinib RL case study |
| `sources/papers/de_carlo_2025.json` | M3.2, M3.3, M3.5 | Givinostat multiobjective RL case study |
| `sources/papers/gottesman_2019_rl_healthcare.json` | M3.6 | Added 2026-08-29 (Antigravity review): Healthcare RL guidelines |
| `sources/papers/levine_2020_offline_rl.json` | M3.6 | Added 2026-08-29 (Antigravity review): Offline RL tutorial & algorithms |
| `sources/papers/thomas_2016_ope.json` | M3.6 | Added 2026-08-29 (Antigravity review): Off-policy evaluation & safety bounds |
| `sources/web/fda_ai_guidance_2025.json` | M3.4, M3.6 | Regulatory pathway for RL dosing |

## Feeds into deliverables
- `deliverables/papers/rl_framework/` — all workstreams
- `deliverables/conferences/webinars/` — Webinar 3 content
- `regulatory/` — clinical trial design and OPE safety validation for RL dosing (M3.4, M3.6)
