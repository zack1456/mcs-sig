# Regulatory · FDA Engagement and Guidance Monitoring

**What:** MCS WG's regulatory engagement — a formal comment on the FDA Jan 2025 AI draft guidance, and ongoing monitoring of FDA/EMA AI guidance developments.

---

## Sub-tasks

### FDA comment on Jan 2025 AI draft guidance
- [ ] **First: confirm docket status** — check regulations.gov for docket number and whether comment period is still open
  - FDA draft guidance: "Considerations for the Use of Artificial Intelligence to Support Regulatory Decision Making" (Jan 2025)
  - If open: comment is time-sensitive — may need to advance ahead of other deliverables
  - If closed: publish as ISoP MCS SIG position paper instead (still valuable; submit to CPT:PSP or similar)
- [ ] Coordinate with ISoP regulatory affairs: institutional comment (under ISoP name) or named-individual comment?
- [ ] Identify co-authors: MCS AI/ML WG (lead) + QSP SIG credibility WG + SxP AI/ML SubSIG reps
- [ ] **Scope of MCS comment:**
  - Mathematical operationalization of the 7-step credibility framework for hybrid mechanistic-ML PMx models
  - Feedback on "model risk = model influence × decision consequence" — how to quantify ML model influence
  - Request for COU (context of use) guidance specific to hybrid mechanistic-ML models
  - Request for a pilot program with sponsors submitting hybrid mechanistic-ML models under the new framework
- [ ] Draft: Month 10 (or earlier if docket is closing)
- [ ] ISoP review and sign-off: Month 11
- [ ] Submit: Month 12
- [ ] **Deliverable:** `fda_comment/comment_draft.md` → submitted PDF

### FDA-EMA Joint Principles monitoring
- [ ] Map each of the 10 FDA-EMA Joint Principles (Jan 2026, "Good AI Practice in Drug Development") to MCS WG pillar deliverables
- [ ] Identify which principles MCS WG most directly addresses; use in paper introductions and regulatory sections
- [ ] Track follow-up implementation guidance from FDA/EMA (quarterly check)
- [ ] **Deliverable:** `monitoring/fda_ema_principles_mapping.md` (living document, updated quarterly)

### M15 MIDD Guidance alignment
- [ ] Review finalized ICH M15 MIDD Guidance (2025) for AI/ML implications
- [ ] Identify gaps: where does M15 leave hybrid ML-mechanistic models ambiguous?
- [ ] Incorporate M15 alignment into `deliverables/papers/whitepaper_hybrid/` Section E
- [ ] **Deliverable:** `monitoring/m15_gaps.md`

---

## Key sources
| Source | Role |
|---|---|
| `sources/web/fda_ai_guidance_2025.json` | Primary subject of FDA comment — full 7-step framework |
| `sources/papers/liu_2023.json` | Evidence base: 132 AI/ML submissions in 2021 — establishes stakes |
| `sources/papers/dermawan_2026.json` | No standalone ML-MIDD regulatory endorsement yet — urgency argument |
| `sources/background/crosssig_fostvedt_2025.json` | ISoP cross-SIG institutional context for comment authorship |

## Dependencies
- `deliverables/papers/whitepaper_hybrid/` Section E — provides technical basis for FDA comment content
- `community/` cross-SIG alignment — co-authors for FDA comment identified through alignment meetings
- Docket status: check immediately — if open, this may need to advance in priority

## Open questions
- [ ] Is the FDA docket still open? (Check regulations.gov now — this is time-sensitive)
- [ ] ISoP institutional comment vs. named-individual: which carries more regulatory weight in the pharmacometrics context?
- [ ] FDA-EMA Joint Principles (Jan 2026): is there a separate comment opportunity, or finalized?
- [ ] Who at ISoP handles regulatory affairs contacts?
