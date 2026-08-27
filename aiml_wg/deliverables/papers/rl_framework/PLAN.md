# Deliverable · Framework Paper: Optimal Control ↔ RL for Precision Dosing

**What:** Framework paper establishing a principled pharmacometric formulation of RL-based precision dosing, connecting RL to classical optimal control theory and grounding reward/state design in pharmacology. Covers Pillar 3.

**Target journal:** CPT: Pharmacometrics & Systems Pharmacology *or* Frontiers in Pharmacology
**Joint with:** MCS Optimal Control WG (coordinate authorship)
**Timeline:** Outline Month 7 · First draft Month 10 · Submitted Month 15

---

## Sub-tasks

### Setup
- [ ] Coordinate with MCS Optimal Control WG: joint paper or AI/ML WG paper with OC WG co-authors?
- [ ] Assign section leads
- [ ] Agree on level of mathematical depth — framework paper or full technical paper?

### Section A — Mathematical mapping: classical control ↔ RL
*Draws from `methods/03_rl_dosing/` M3.1*
- [ ] Central figure/table: state · action · value function · optimality condition for each approach
- [ ] Approaches: Pontryagin, HJB, MPC, tabular Q-learning, policy gradient
- [ ] Key insight for pharmacometrics: Q-learning is a discretized, model-free approximation to HJB; MPC is model-based but myopic

### Section B — Pharmacometric requirements for MDP design
*Draws from `methods/03_rl_dosing/` M3.2 and M3.3*
- [ ] State space design principles: biomarker selection, discretization criteria, dimension management
- [ ] Reward function design: connecting clinical endpoints to reward signal; multiobjective reward aggregation
- [ ] Action space: dose levels vs. dose adjustments; hard constraint enforcement

### Section C — Safety constraints and POMDP extension
*Draws from `methods/03_rl_dosing/` M3.4*
- [ ] Hard vs. soft constraints: CMDP (constrained MDP) formulation
- [ ] POMDP for measurement uncertainty: when patient state is not directly observed
- [ ] Bayesian online updating: progressively estimating individual PK-PD parameters during treatment

### Section D — Case studies
*Draws from `methods/03_rl_dosing/` M3.5*
- [ ] Erdafitinib (De Carlo 2024): what generalizes from the 86-state MDP design
- [ ] Givinostat (De Carlo 2025): what multiobjective extension teaches about reward design and computational cost
- [ ] Propofol (Ribba 2023): the motivating scale argument (>16M solution space)
- [ ] Synthesis: what principles are drug-specific vs. pharmacometrically generalizable?

### Section E — Open problems and research agenda
- [ ] Computational scalability: surrogate simulation (faster than NONMEM/Simulx) for RL training
- [ ] Transfer learning: train on one drug, adapt to another
- [ ] Clinical trial design for RL dosing protocols (MRT, adaptive platform trials)
- [ ] Regulatory pathway: connecting to FDA 7-step framework for RL-based dosing decisions

### Review and submission
- [ ] Outline: Month 7
- [ ] First draft: Month 10
- [ ] Review: Month 12–13
- [ ] Submission: Month 15

---

## Key sources
| Source | Section(s) |
|---|---|
| `sources/papers/ribba_2023.json` | A, D (RL as optimal control; propofol) |
| `sources/papers/de_carlo_2024.json` | B, C, D (MDP design, reward function) |
| `sources/papers/de_carlo_2025.json` | B, D (multiobjective, computational cost) |
| `sources/web/fda_ai_guidance_2025.json` | E (regulatory pathway) |

## Dependencies
- `methods/03_rl_dosing/` M3.1–M3.5 working notes must be substantively complete before Section A–D drafting
- MCS Optimal Control WG coordination (via `community/`) — resolve joint vs. credited authorship
- `regulatory/` — Section E regulatory pathway connects to FDA comment

## Open questions
- [ ] Is tabular Q-learning (De Carlo) the right entry point, or should Section A lead with the HJB/continuous-control framing that is more natural for pharmacometricians trained in optimal control?
- [ ] POMDP extension (Section C): include in this paper or a follow-on? Recommend include — it's the most important open problem
- [ ] Joint paper with Optimal Control WG: if yes, who is corresponding author? Agree before outline is circulated
