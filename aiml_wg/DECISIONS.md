# MCS SIG AI/ML WG — Decision Log

**How to use:**
- Add an entry whenever a scoping, strategic, or design decision is made
- `Status`: `tentative` (proposed, not yet confirmed) · `confirmed` (agreed by WG or co-chairs) · `revised` (changed — add a new entry rather than editing the old one) · `superseded` (replaced by a later decision)
- Reference decisions by ID in TASKS.md and HANDOFF.md

---

## DECISION-1 · Hybrid model scope

| Field | Value |
| --- | --- |
| **ID** | DECISION-1 |
| **Date** | 2026-08-26 (proposed) |
| **Status** | tentative — confirm at kickoff (Aug 28) |
| **Decision** | Start with neural ODEs specifically before broadening to all hybrid mechanistic-ML architectures |
| **Rationale** | Neural ODEs sit at the intersection of identifiability, UQ, and mechanistic modeling — highest-impact and most mathematically tractable entry point. The iNODE preprint (campo_manzanares_2026, Aug 13 2026) shows a directly addressable gap. Broad-first risks 6 months of taxonomy work with no clear output. |
| **What would change this** | A member has an active dataset or collaboration making a different hybrid architecture (e.g., PBPK-ML) the better first case study |
| **Affects tasks** | M1.1, M1.2, M1.3, M1.4 |

---

## DECISION-2 · First external deliverable

| Field | Value |
| --- | --- |
| **ID** | DECISION-2 |
| **Date** | 2026-08-26 (proposed) |
| **Status** | tentative — confirm at kickoff (Aug 28) |
| **Decision** | White paper (Pillars 1+2) as first external deliverable; ACoP session proposal drafted in parallel |
| **Rationale** | A white paper in CPT:PSP or JPKPD is a durable credibility signal. The QSP SIG "Two heads" white paper (zhang_2022, JPKPD 49:5–18) is the model. ACoP preparation consumes bandwidth without citable output. |
| **What would change this** | ACoP session unlocks a collaboration or industry partnership that funds WG work |
| **Affects tasks** | D-WP-A, D-WP-B, D-SC-A–E |

---

## DECISION-3 · Pillar 3 (RL/Optimal Control) bandwidth in Phase 1

| Field | Value |
| --- | --- |
| **ID** | DECISION-3 |
| **Date** | 2026-08-26 (proposed) |
| **Status** | tentative — confirm at kickoff (Aug 28) |
| **Decision** | Pillar 3 runs lighter in Phase 1 (one person tracks literature + contributes to scoping paper); full effort in Phase 2 with joint Optimal Control WG paper |
| **Rationale** | RL dosing mathematical gaps (reward design, POMDP, HJB connections) require Pillar 1 foundations first — need a reliable PK/PD digital twin before training RL agents on it |
| **What would change this** | A member has a live clinical RL collaboration needing WG backing faster |
| **Affects tasks** | M3.1, M3.2, D-RL-A |

---

## DECISION-4 · Generative AI scope

| Field | Value |
| --- | --- |
| **ID** | DECISION-4 |
| **Date** | 2026-08-26 (proposed) |
| **Status** | tentative — confirm at kickoff (Aug 28) |
| **Decision** | Physics-constrained generative models first (VAEs, diffusion with ODE constraints, synthetic patient validation); LLMs scoped to a position paper only |
| **Rationale** | Physics-constrained generative models are closer to WG core competency and have a clear gap: synthetic patient validation frameworks are essentially missing from the literature. For LLMs: the 2024–2025 capability trajectory (shin_2024_llm → zheng_2025_llm) shows standard NONMEM coding is now near-solved; remaining failure modes are causal reasoning and complex ODE structure — exactly where MCS mathematical rigor adds value. A position paper scoped to these failure modes is more differentiating than broad LLM coverage. |
| **What would change this** | Member expertise concentrated in LLMs and no one available to drive physics-constrained work |
| **Affects tasks** | M4.1, M4.4, D-GEN-A |

---

## DECISION-5 · Cross-SIG relationship mode

| Field | Value |
| --- | --- |
| **ID** | DECISION-5 |
| **Date** | 2026-08-26 (proposed) |
| **Status** | tentative — confirm at kickoff (Aug 28) |
| **Decision** | Coordinate with QSP SIG, SxP SIG, Optimal Control WG, and AI/ML SIG in Phase 1; formal co-authorship only when scope is clear (Phase 2+) |
| **Rationale** | Cross-SIG paper (Fostvedt et al. 2025) documents each SIG's distinct emphasis; co-authoring too early risks scope creep and authorship friction |
| **What would change this** | A co-chair has an existing collaboration with QSP or SxP leads making immediate co-authorship natural |
| **Affects tasks** | C-04, C-07, M2.5, D-RL-A |

---

## DECISION-6 · Benchmarks timing

| Field | Value |
| --- | --- |
| **ID** | DECISION-6 |
| **Date** | 2026-08-26 (proposed) |
| **Status** | tentative — confirm at kickoff (Aug 28) |
| **Decision** | Benchmarks repository deferred to Phase 3 (Month 15+); listed as stretch goal |
| **Rationale** | Benchmark repos require infrastructure and community buy-in premature in Phase 1. WG must first establish what is being benchmarked (from scoping and white papers) before building the infrastructure |
| **What would change this** | Industry partner willing to co-develop and maintain benchmark infrastructure |
| **Affects tasks** | BM-01 |

---

## DECISION-7 · Founding-team scope (3 people)

| Field | Value |
| --- | --- |
| **ID** | DECISION-7 |
| **Date** | 2026-08-27 (proposed) |
| **Status** | tentative — confirm at kickoff (Aug 28) |
| **Decision** | Run **one pillar at depth** (Pillar 1, neural-ODE identifiability) plus one Pillar 2 seed note while the team is 3 people; treat growing to ~6–8 active members as the primary Phase 1 deliverable. Expand pillars per the scaling table in `community/phase1_scope.md §2`. |
| **Rationale** | Four pillars cannot be run by three people without producing four stalled workstreams that make the WG look inactive to the exact people it wants to recruit. Depth in one place is the recruiting signal. Decisions 3/5/6 (RL light, coordinate-not-co-author, defer benchmarks) are forced by headcount, not independent choices. |
| **What would change this** | Faster-than-expected recruiting (hit 6+ active members before Month 2) unlocks Pillar 2 at depth sooner. |
| **Affects tasks** | All M-series; C-05 (journal club as funnel); new recruiting task |

---

## DECISION-8 · Regulatory workstream reframe

| Field | Value |
| --- | --- |
| **ID** | DECISION-8 |
| **Date** | 2026-08-27 (proposed) |
| **Status** | tentative — confirm at kickoff (Aug 28) |
| **Decision** | Reframe the regulatory workstream from an FDA docket comment to an **untimed operationalization** of the finalized 7-step credibility framework + Jan 2026 FDA–EMA Joint Principles, folded into white-paper §E. |
| **Rationale** | Confirmed 2026-08-27: comment period on the AI draft guidance (Docket FDA-2024-D-4689) closed April 7, 2025; final guidance expected Q2 2026 (now finalized/imminent). No open docket exists. Removes an artificial deadline and produces a more durable, citable contribution. |
| **What would change this** | FDA opens a new docket (e.g., on a revised or companion guidance) with a live comment window. |
| **Affects tasks** | R-01, R-02, D-SC-E, D-WP (§E) |

---

## Template for new decisions

```
## DECISION-N · [Short title]

| Field | Value |
| --- | --- |
| **ID** | DECISION-N |
| **Date** | YYYY-MM-DD |
| **Status** | tentative / confirmed / revised / superseded |
| **Decision** | [One sentence: what was decided] |
| **Rationale** | [Why — the constraint, tradeoff, or evidence that drove this] |
| **What would change this** | [The condition under which this decision should be revisited] |
| **Affects tasks** | [Task IDs from TASKS.md] |
```
