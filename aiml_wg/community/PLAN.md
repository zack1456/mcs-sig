# Community · Governance, Engagement, and Cross-SIG Coordination

**What:** WG operating infrastructure — kickoff and charter, cross-SIG alignment agreements, journal club, MCS SIG website content, and the standing cross-SIG AI/ML coordination hub.

---

## Sub-tasks

### Kickoff and charter
- [ ] Schedule kickoff meeting (co-chairs + active members; solicit additional members from MCS SIG)
- [ ] Agenda: resolve 6 scoping decisions (below); assign pillar leads; set meeting cadence
- [ ] Draft WG charter: mission, four pillars, out-of-scope statement, membership process, meeting cadence
- [ ] Submit charter to ISoP MCS SIG steering committee for approval
- [ ] **Deliverable:** `charter.md` — approved by Month 2

**6 scoping decisions for kickoff:**
- [ ] Hybrid model scope: neural ODEs in PK/PD only, or broader (QSAR, covariate discovery)?
- [ ] Output priority: white paper first, or conference session to build community first?
- [ ] RL: near-term priority alongside Pillars 1/2, or follow?
- [ ] GenAI angle: physics-constrained generation first (most MCS-distinctive) or LLM failure modes first (more topical)?
- [ ] Cross-SIG agreements: formal co-authorship, or coordination only?
- [ ] Benchmarks: pursue in Phase 2, or defer to Phase 3?

### Cross-SIG alignment
- [ ] AI/ML SIG: agree on scope boundary (MCS = mathematical foundations; AI/ML SIG = applied education)
- [ ] QSP SIG credibility WG: align on hybrid model credibility scope (QSP-specific vs. PMx-general)
- [ ] SxP AI/ML SubSIG: coordinate on statistical ML boundary
- [ ] MCS Optimal Control WG: coordinate on Pillar 3 joint authorship
- [ ] MCS SAUQ WG: assess activity level; establish liaison for Pillar 2 UQ methods
- [ ] **Deliverable:** `crosssig_alignment_memo.md` — signed agreements by Month 6

### Standing cross-SIG coordination hub
- [ ] Propose to ISoP leadership: quarterly cross-SIG AI/ML coordination meetings (MCS + AI/ML SIG + QSP + SxP)
- [ ] Build on precedent: ACoP 2023 cross-SIG session + Fostvedt et al. 2025 cross-SIG paper
- [ ] Draft 1-page coordination charter
- [ ] Secure buy-in from other SIG chairs before formally proposing to ISoP
- [ ] **Deliverable:** `crosssig_hub_charter.md` — established by Month 12

### Journal club
- [ ] Start Month 3; monthly or bi-monthly cadence; rotate leadership
- [ ] Format: synchronous (Zoom) or async (Slack/GitHub discussion)? Decide based on time zones of members
- [ ] **Priority reading list for Months 3–8:**
  - `baran_gaburro_2026` — hybrid model identifiability and credibility (Month 3)
  - `de_carlo_2025` — RL+PK-PD multiobjective dosing (Month 4)
  - `fda_ai_guidance_2025` — FDA 7-step credibility framework (Month 5)
  - `ribba_2023` — RL as optimal control (Month 6)
  - `dermawan_2026` — ML-MIDD landscape 2015–2025 (Month 7)
  - arXiv 2608.13044 — identifiability-aware NeuralODEs (Month 8)
- [ ] **Deliverable:** `journal_club/schedule.md` + `journal_club/notes/` (one file per session)

### MCS SIG website
- [ ] Create WG page on MCS SIG website (https://sites.google.com/view/mcssig/)
- [ ] Content: mission, four pillars, member list, deliverables with links, webinar recordings
- [ ] Keep updated as preprints and papers ship
- [ ] **Deliverable:** Website page live by Month 6

---

## Dependencies
- Charter approval gates: website page, cross-SIG alignment proposals, ACoP session proposal
- Cross-SIG alignment memo gates: `deliverables/papers/genai_position/` scope statement
- SAUQ coordination gates: `methods/02_uq/` M2.5
