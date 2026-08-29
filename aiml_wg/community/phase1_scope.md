# Phase 1 Scope — Right-Sized for the Founding Team

**Status:** Draft for kickoff (Aug 28, 2026)
**Reality this document plans around:** 3 active people — co-chairs Shreyas Chakravarty (SK) and Zack Kenz (ZK) plus one highly involved member (MC) — for roughly the next 2 months, then deliberate recruiting to grow the group before scope expands.

This document sits between `working_group_plan.md` (the full 18-month ambition) and `WORKPLAN.md` (the milestone map). Those describe the destination assuming a staffed WG. This describes **what 3 people actually do first**, and how scope scales as members join. Read this as the operative near-term plan; the others remain the target once the group is staffed.

---

## 1. The core constraint

Four pillars cannot be run by three people. Attempting it produces four shallow, stalled workstreams and a WG that looks inactive to exactly the people we want to recruit. The founding-team job is different from the staffed-WG job:

> **Ship one credible artifact that doubles as a recruiting magnet, and use it to grow from 3 to ~6–8 active members. Everything else is "track, don't build."**

Depth in one place is what signals to a prospective member "this group is serious and I want in." Breadth across four half-built pillars signals the opposite.

---

## 2. Members → pillars: the scaling rule

Scope should expand only as headcount justifies it. This is the sizing table to govern the next 6 months:

| Active members | Pillars run at depth | Everything else |
| --- | --- | --- |
| **3 (now)** | **Pillar 1 only** (neural-ODE identifiability), plus one Pillar 2 seed note | Pillars 3 & 4: track literature, no build |
| 5–6 | Pillars 1 **+** 2 | Pillars 3 & 4: track; scope RL joint effort |
| 8+ | Add Pillar 3 (joint with Optimal Control WG) | Pillar 4: scope |
| 10+ | Add Pillar 4 | — |

Decisions 3, 5, and 6 in the kickoff agenda (RL light, coordinate-don't-co-author, defer benchmarks) are not really open choices at 3 people — **headcount forces them.** Present them as consequences of team size, not as debates. The only genuinely live scoping questions for the founding team are Decisions 1 and 4 (see §5).

---

## 3. What the founding team ships in the next ~8 weeks

One primary artifact, one technical seed, one funnel. Not more.

### 3a. Primary artifact — "Scope & Call for Participation" brief (2–4 pages)
The recruiting magnet. Public-facing, member-facing. Not the 10-page scoping paper (too big for 3 people) and not the white paper (Phase 2). It states: the problem, the four-pillar vision, the two concrete wedges (below), and an explicit invitation to join with named entry points. This brief is what gets circulated to MCS SIG members, cross-posted to sister SIGs, and used at ACoP.
- **Owner:** SK
- **Later becomes:** the front half of the scoping paper (`deliverables/papers/scoping_paper/`), so it is not throwaway work.

### 3b. Technical seed — conformal-prediction-for-PK/PD concept note (1–2 pages)
This is the sharpest "we are staking new ground" signal we have. Conformal prediction returned **zero PubMed hits** across three search strategies — a genuine white space. 
- **The Core Mathematical Angle:** <!-- Added 2026-08-29 (Antigravity review) --> Address the **hierarchical & non-exchangeable** nature of clinical trial PK data (longitudinal repeated measures per subject, cohort shifts) leveraging group-conformal (`dunn_2022_clustered_conformal`) and time-series adaptive conformal inference (`gibbs_2021_timeseries_conformal`, `barber_2023_conformal`).
- **Content:** (a) what conformal prediction is, (b) where it sits relative to profile likelihood (`raue_2009`) and Bayesian UQ (`elmokadem_2024`), (c) what a distribution-free PK/PD coverage guarantee means for individual patient dosing bounds.
- **Dissemination Target:** <!-- Added 2026-08-29 (Antigravity review) --> Targeted as a high-visibility *CPT:PSP* Commentary / Tutorial or ISoP Technical Memo to establish early citable priority.
- **Owner:** ZK (or MC if MC's background is UQ/stats-leaning)
- **Alternative seed** if the team's expertise points that way: a neural-ODE structural-identifiability mini-review anchored on the iNODE preprint (M1.2). Pick one seed, not both.

### 3c. Funnel — journal club as low-commitment on-ramp
Journal club is the recruiting funnel, not just an internal activity. A prospective member will join a 45-minute paper discussion long before they will commit to co-authoring. Start it in month 2 with the 3 founders + invitees; first session on `baran_gaburro_2026` (hybrid-model credibility) or the iNODE preprint.
- **Owner:** MC (rotating thereafter)

Everything in `methods/03_rl_dosing/` and `methods/04_generative_ai/` stays in "track" mode: one of the three keeps an eye on new papers via the source library, nothing is built.

---

## 4. Recruiting plan (the actual Phase 1 priority)

For a 3-person team, **growing to 6–8 is the primary Phase 1 deliverable** — more important than any paper, because every paper depends on it. Channels, in rough priority:

1. **MCS SIG membership (~70 people)** — direct ask via the SIG list; the Scope & Call brief is the attachment.
2. **Sister MCS working groups** — Optimal Control WG and SAUQ WG have the most natural methodological overlap; their members are the highest-yield targets and align with Pillars 2 and 3.
3. **ISoP AI/ML SIG cross-post** — coordinate (not compete) per DECISION-5; a cross-post also opens the cross-SIG relationship.
4. **ACoP 2026 (Oct 2026, National Harbor)** — a birds-of-a-feather table or informal meetup as an in-person recruiting event; timing is ideal, ~6–8 weeks out.
5. **Academic bridge (SIAM / SMB / Math & Biostats Depts)** — <!-- Added 2026-08-29 (Antigravity review) --> Active outreach to SIAM Life Sciences, Society for Mathematical Biology (SMB), and university applied math/biostats groups (researchers working on dynamical systems, UQ, and scientific ML who lack direct pharma domain exposure); consistent with MCS's historical founding mission (`cpt_moore_2019`).

Set a concrete target and name owners at kickoff, e.g. *"reach 6 active members by end of Month 2; each co-chair personally invites 5 named people this week."* Recruiting fails when it's everyone's job; give it an owner.

---

## 5. What tomorrow's kickoff actually decides

With 3 people the meeting is not a group vote — it's the three founders aligning and stress-testing against MC's expertise. Three things genuinely need to come out of it:

1. **Which pillar is the spearhead, and which technical seed** (§3b) — this depends on MC's background. Math/dynamical-systems-leaning → neural-ODE identifiability. Stats/UQ-leaning → conformal-prediction note. *This is Decisions 1 and 4 made real.*
2. **The 8-week deliverable and who owns each piece** — the Scope & Call brief, the seed note, the journal club (§3).
3. **The recruiting commitment** — target number, channels, and who owns outreach (§4).

Everything else in the six-decision agenda is either forced by headcount (D3, D5, D6) or a chair default the group can accept in minutes (D2, noting that even the white paper is a Phase-2-once-staffed item).

---

## 6. Mission one-liner (draft options for the charter)

The group still lacks a single repeatable sentence. Candidates:

- *"We build the mathematical foundations — identifiability, uncertainty quantification, and control theory — that make AI/ML-augmented pharmacometric models credible enough to trust and defensible enough to submit."*
- *"The math the applied AI/ML community skips: we make AI/ML-augmented pharmacometric models identifiable, uncertainty-aware, and regulatorily defensible."*
- *"Mathematical rigor for AI/ML in pharmacometrics — so hybrid models are not just accurate on training data, but identifiable, quantified, and credible."*

Pick and refine one at kickoff; it goes at the top of the charter and the Scope & Call brief.

---

## 7. What this does *not* change

The full four-pillar structure, the 18-month milestone map, and the source library remain the target and the foundation. This document is a sequencing and staffing overlay for the founding period, not a rescoping of the WG's ambition. As the scaling table (§2) fills in, the workstreams in `methods/` and `deliverables/` activate on schedule.
