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
| **Rationale** | LLMs for pharmacometrics is crowded and hard to differentiate mathematically. Physics-constrained generative models are closer to WG core competency and have a clear gap: synthetic patient validation frameworks are essentially missing from the literature |
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
