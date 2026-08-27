# MCS SIG AI/ML Working Group — Kickoff Meeting Agenda
**Date:** Friday, August 28, 2026
**Co-chairs:** Shreyas Chakravarty, Zack Kenz
**Format:** [Virtual / In-person — confirm before meeting]

---

## Agenda (suggested 90 min)

| Time | Item | Lead | Notes |
| --- | --- | --- | --- |
| 0:00–0:10 | Welcome and introductions | Chakravarty | Each attendee: name, affiliation, 1 sentence on what drew them to the WG |
| 0:10–0:25 | WG mission and four pillars | Kenz | Refer to pre-read; walk Table 1 (pillar → methods map) |
| 0:25–0:55 | Six scoping decisions (see below) | Both | ~5 min per decision; go around for input; chairs announce stance |
| 0:55–1:05 | 18-month plan and workstream ownership | Chakravarty | Who wants to lead what? Signal intent, not commitment |
| 1:05–1:15 | Deliverables and visibility | Kenz | Papers, webinars, ACoP; how we relate to other SIG AI/ML efforts |
| 1:15–1:25 | Operations: cadence, tools, norms | Both | Meeting frequency, async communication, GitHub or shared drive |
| 1:25–1:30 | Next steps and close | Chakravarty | Assign: M1.1 kickoff owner, scoping paper section leads |

---

## Six Scoping Decisions — Co-chair Recommended Stances

These decisions define the WG's operating scope for Phase 1 (months 1–6). Each is a genuine tradeoff; the recommended stance reflects our read of where the group can add the most distinctive value. Members should push back if they disagree.

---

### Decision 1: Hybrid model depth — start narrow or broad?

**Question:** Does Pillar 1 start with neural ODEs specifically, or does it survey all hybrid mechanistic-ML architectures simultaneously?

**Recommended stance: Start narrow — neural ODEs first.**

**Rationale:** Neural ODEs sit at the intersection of identifiability, UQ, and mechanistic modeling — they are both the highest-impact and the most mathematically tractable entry point. The iNODE preprint (Campo-Manzanares & Balsa-Canto, arXiv 2608.13044) was submitted two weeks ago and shows exactly the kind of gap the WG should fill: identifiability-integrated architecture design. Starting there lets us produce a concrete technical contribution (M1.1–M1.2) quickly, before broadening to PBPK-ML and other hybrid forms in Phase 2. Broad-first risks 6 months of taxonomy work with no clear output.

**What would change this stance:** If a member has an active dataset or collaboration that makes a different hybrid architecture (e.g., PBPK-ML) the right first case study.

---

### Decision 2: First external deliverable — white paper or ACoP session?

**Question:** Do we target a journal white paper first, or anchor Phase 1 around a visible ACoP presence?

**Recommended stance: White paper first (Pillars 1+2), with ACoP session proposed in parallel.**

**Rationale:** A white paper in CPT:PSP or JPKPD is a durable credibility signal for the WG and for ISoP membership. The QSP SIG's "Two heads" white paper (Zhang et al. 2022, JPKPD 49:5–18) is the model to emulate. ACoP preparation tends to consume co-chair bandwidth without producing citable output. Running both in parallel is feasible if we divide the labor: one lead for paper sections, one lead for ACoP proposal. The ACoP session proposal (due ~Q1 2027) can be drafted in parallel without diverting the core writing team.

**What would change this stance:** If the ACoP session would unlock a collaboration or industry partnership that funds the WG's work.

---

### Decision 3: Optimal control / RL (Pillar 3) — active or light?

**Question:** Does Pillar 3 run at full bandwidth alongside Pillars 1+2, or does it run lighter in Phase 1?

**Recommended stance: Run parallel but lighter — Pillar 3 is Phase 2 primary.**

**Rationale:** The De Carlo papers (2024, 2025) provide excellent worked examples, but the mathematical gap the WG can fill — reward function design under clinical constraints, POMDP for partially observed patient state — requires Pillar 1 foundations to be in place (specifically: what makes a PK/PD digital twin reliable enough to train an RL agent on?). Running Pillar 3 light in Phase 1 means one person tracks the RL literature, co-authors the Pillar 3 section of the scoping paper, and identifies the Optimal Control WG liaison. Full Pillar 3 effort starts in Phase 2 with a joint paper with that WG.

**What would change this stance:** If a member has a live clinical RL collaboration and needs WG backing to move it forward faster.

---

### Decision 4: Generative AI (Pillar 4) — physics-constrained or broad GenAI?

**Question:** Does Pillar 4 scope to physics-constrained generative models (VAEs, diffusion with ODE constraints), or does it include LLMs for pharmacometrics?

**Recommended stance: Physics-constrained GenAI first; LLMs scoped to a position paper.**

**Rationale:** LLMs for pharmacometrics is a crowded, fast-moving space where the WG's mathematical differentiation is hardest to assert. Physics-constrained generative models (constrained VAEs, diffusion models with ODE priors, synthetic patient generation) are methodologically closer to the WG's core competency and have a clearer gap: validation frameworks for synthetic patients are essentially missing from the literature. The LLM failure modes analysis (M4.4) is tractable as a short position paper and can be done by one person in parallel. This keeps Pillar 4 tractable without abandoning the LLM space entirely.

**What would change this stance:** If member expertise is concentrated in LLMs and there's no one to drive the physics-constrained work.

---

### Decision 5: Cross-SIG relationship — coordinate first, co-author later?

**Question:** Should we approach QSP SIG, SxP SIG, and Optimal Control WG as coordination partners or as immediate co-authors?

**Recommended stance: Coordinate first (Phase 1), co-author when scope is clear (Phase 2+).**

**Rationale:** The crossSIG paper (Fostvedt et al. 2025) documents that each SIG's AI/ML effort has distinct emphasis; our differentiation is mathematical rigor, not subject matter. Co-authoring too early risks scope creep and authorship friction. The right Phase 1 move is: attend the relevant WG meetings, share our scoping paper draft for comment, and identify 1–2 natural co-author opportunities (likely the RL paper with Optimal Control WG, and possibly a UQ paper with SxP SIG). Formal co-authorship starts in Phase 2.

**What would change this stance:** If a co-chair has an existing collaboration with QSP or SxP leads that makes immediate co-authorship natural and low-friction.

---

### Decision 6: Benchmarks — when?

**Question:** Should we build a reproducible evaluation repository (benchmarks workstream) in Phase 1?

**Recommended stance: Defer to Phase 3 (months 13–18) — list as a stretch goal.**

**Rationale:** Benchmark repos require infrastructure, maintenance, and community buy-in that is premature in Phase 1. The WG's first job is to establish what we are benchmarking and why — that comes from the scoping paper and white paper. The benchmarks workstream (in `aiml_wg/benchmarks/`) is already planned; it just needs a Phase 3 start date. If a member has existing infrastructure (e.g., a Julia/Python package already under development), we revisit this in Phase 2.

**What would change this stance:** An industry partner willing to co-develop and maintain the benchmark infrastructure.

---

## Ownership Signals — Ask the Room

At the 0:55 mark, ask each member to signal (not commit) interest in leading:

| Workstream | Phase 1 task | Signal? |
| --- | --- | --- |
| Pillar 1 — Hybrid Models | M1.1 architecture taxonomy (lead author) | |
| Pillar 1 — Identifiability | M1.2 structural identifiability review | |
| Pillar 2 — UQ | M2.1 Bayesian UQ framework literature review | |
| Pillar 3 — RL liaison | Optimal Control WG point of contact | |
| Pillar 4 — Physics GenAI | M4.1 physics-constrained generative models | |
| Scoping paper | Section B (landscape) lead | |
| Cross-SIG coordination | QSP SIG and SxP SIG liaison | |
| ACoP proposal | Session proposal draft (due ~Q1 2027) | |

---

## Operations Items

- **Meeting cadence:** Monthly 60-min calls recommended; monthly async update in shared channel
- **Async tool:** [Slack / Teams / email list — confirm with ISoP infrastructure]
- **Shared repo:** This git repository; members can contribute via pull request or by sending files to co-chairs
- **Source library:** `aiml_wg/sources/` — members can suggest papers via the `/add-source` skill or by sharing PDFs with co-chairs
- **Journal club:** Propose quarterly; first session in ~month 2 once the WG has settled on a rhythm

---

## Next Steps (assign before close)

1. Send pre-read document to all members who did not receive it before the meeting
2. Assign M1.1 lead (architecture taxonomy) by end of meeting or within 1 week
3. Assign scoping paper section leads by end of month 1
4. Co-chairs draft a brief mission statement paragraph for the ISoP website update (due TBD)
5. Check FDA AI/ML docket for open comment opportunities (current draft guidance 2025 — public comment period may still be open)
