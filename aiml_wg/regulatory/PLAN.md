# Regulatory · FDA Engagement and Guidance Monitoring

**What:** MCS WG's regulatory engagement — a formal comment on the FDA Jan 2025 AI draft guidance, and ongoing monitoring of FDA/EMA AI guidance developments.

---

## Sub-tasks

### ASME V&V 40 & FDA Credibility Framework Operationalization
*Translating risk-informed computational credibility standards into hybrid pharmacometric practice* <!-- Added 2026-08-29 (Antigravity review) -->

- [ ] **ASME V&V 40 Standard Alignment:** Formally map ASME V&V 40-2018 (*Assessing Credibility of Computational Models through Verification and Validation*) and its MIDD translation (`kuemmel_2020_credibility`) to the FDA 2025 7-step AI/ML credibility framework
- [ ] **Model Risk Formulation:** Quantify *Model Risk = Model Influence × Decision Consequence* for embedded neural components vs. mechanistic compartments
- [ ] **Code & Calculation Verification:** Define standards for verifying stiff numerical ODE solvers, adjoint sensitivity gradient accuracy, and tolerance convergence in regulatory packages (`kim_2021_stiff_node`)
- [ ] **Context of Use (COU) Templates:** Create standardized COU templates for hybrid mechanistic-ML models and offline RL precision dosing algorithms
- [ ] Note: per DECISION-8, the FDA AI draft guidance comment period closed April 7, 2025; this workstream is reframed as an untimed operationalization deliverable folded into `deliverables/papers/whitepaper_hybrid/` Section E and a potential ISoP position paper

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
| Source | Role | Added / Role |
|---|---|---|
| `sources/web/fda_ai_guidance_2025.json` | Regulatory credibility framework | Primary 7-step framework |
| `sources/papers/kuemmel_2020_credibility.json` | ASME V&V 40 translation to MIDD | Added 2026-08-29 (Antigravity review): Model influence & risk |
| `sources/papers/liu_2023.json` | Evidence base | 132 AI/ML submissions in 2021 — establishes stakes |
| `sources/papers/dermawan_2026.json` | Evidence base | No standalone ML-MIDD regulatory endorsement yet |
| `sources/papers/chenel_2026.json` | Regulatory PBPK / ICH M15 | PBPK best practices and M15 alignment |
| `sources/background/crosssig_fostvedt_2025.json` | ISoP institutional context | Cross-SIG alignment |

## Dependencies
- `deliverables/papers/whitepaper_hybrid/` Section E — provides technical basis for regulatory credibility framework
- `community/` cross-SIG alignment — co-authors identified through alignment meetings

## Open questions
- [ ] How will the upcoming finalized FDA AI guidance (post-April 2025 comment period) adjust the 7-step credibility framework for generative vs. predictive models?
- [ ] FDA-EMA Joint Principles (Jan 2026): track pilot programs or companion operationalization guides.
