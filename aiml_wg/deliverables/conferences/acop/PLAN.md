# Deliverable · ACoP Session

**What:** Workshop or symposium at ACoP 2026 (October 2026, National Harbor) or ACoP 2027, establishing MCS WG's public presence with a session on mathematical foundations of AI/ML in pharmacometrics.

**Target:** ACoP 2026 if deadline permits; ACoP 2027 as primary target if 2026 deadline has passed
**Format options:** 90-minute symposium (4 talks + panel) or half-day workshop

---

## Sub-tasks

### Logistics
- [ ] Check ACoP 2026 workshop/symposium proposal deadline (ISoP website; typically 6–9 months before conference)
- [ ] If open: submit by deadline
- [ ] If closed: target ACoP 2027 as primary; submit poster or contributed talk to ACoP 2026 as placeholder

### Proposal draft
- [ ] Title: "Mathematical Foundations of AI/ML in Pharmacometrics: Identifiability, UQ, and Credibility" (or variation)
- [ ] Rationale: 132 AI/ML submissions to FDA in 2021 alone (liu_2023); no mathematical standards exist; MCS WG is uniquely positioned
- [ ] Format: 4 talks (one per pillar) + 15-min panel on regulatory and cross-SIG implications
- [ ] **Deliverable:** `proposal_draft.md` → submitted abstract/proposal

### Speaker identification
- [ ] Talk 1 (Pillar 1): MCS WG member leading `methods/01_hybrid_models/` identifiability work
- [ ] Talk 2 (Pillar 2): SAUQ WG liaison or `methods/02_uq/` lead
- [ ] Talk 3 (Pillar 3): MCS Optimal Control WG joint author / `methods/03_rl_dosing/` lead
- [ ] Talk 4 (Pillar 4): `methods/04_generative_ai/` lead
- [ ] Panel moderator: co-chair (Chakravarty or Kenz)
- [ ] Panel guests: ISoP AI/ML SIG representative (cross-SIG visibility); 1 FDA/industry perspective

### Slide content
- [ ] Each talk should draw from the corresponding deliverable paper draft at whatever stage it is
- [ ] Panel discussion questions prepared in advance
- [ ] **Deliverable:** `slides/` subfolder with one deck per talk

---

## Key sources (for motivation slides)
| Source | Use |
|---|---|
| `sources/papers/liu_2023.json` | 132 FDA submissions in 2021 — stakes |
| `sources/papers/dermawan_2026.json` | 22-fold growth, no regulatory endorsement yet |
| `sources/web/fda_ai_guidance_2025.json` | 7-step framework — what MCS is operationalizing |
| `sources/background/crosssig_fostvedt_2025.json` | Cross-SIG landscape context |

## Dependencies
- `community/` kickoff: WG must exist and have charter before a session can be proposed
- Paper outlines (`deliverables/papers/`) should exist before slide content is developed
