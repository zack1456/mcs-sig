# Benchmarks · Hybrid Mechanistic-ML PK/PD Model Evaluation Repository

<!-- Updated 2026-08-29 by Codex: added Phase 0 validation-pilot design and transportability/decision-validation criteria. -->

**What:** Public, reproducible benchmark giving the community a shared evaluation standard for hybrid mechanistic-ML pharmacometric models — currently nonexistent. Hosted on GitHub.

**Status:** Stretch goal; pursue once `deliverables/papers/whitepaper_hybrid/` Section D (validation criteria) is drafted.
**Timeline:** Public launch Month 15 if resourced; Month 18+ if deferred.

---

## Sub-tasks

### Phase 0 — Validation-pilot design (start before public benchmark commitment)
- [ ] Use one simulated PK/PD dataset with known truth and one openly licensed clinical PK dataset
- [ ] Compare a mechanistic baseline against one bounded hybrid implementation; do not promise a public repository at this stage
- [ ] Define an evaluation card containing numerical verification, identifiability, error, calibration/sharpness, temporal/external validation, applicability-domain/shift checks, subgroup reporting where meaningful, decision-level safety/utility, and reproducibility metadata
- [ ] Record dataset provenance, license, preprocessing, solver tolerances, software versions, random seeds, and hardware
- [ ] **Deliverables:** `pilot_protocol.md`, `evaluation_card_template.md`, `datasets/provenance_and_license_matrix.md`

### Phase 1 — Criteria (depends on whitepaper_hybrid Section D)
- [ ] Lock evaluation criteria from white paper Section D:
  - Prediction accuracy: test-set RMSE, 90% PI coverage
  - Identifiability: practical (profile likelihood width); structural (sensitivity matrix rank)
  - UQ calibration: coverage probability of credible/conformal intervals
  - Computational cost: training + inference time, hardware spec
  - Regulatory documentation: checklist based on FDA 7-step framework
  - Transportability: temporal/external performance, applicability-domain or shift diagnostics, and prespecified subgroup reporting
  - Decision validation: unsafe-action rate and utility/regret where the COU is a dosing decision
- [ ] **Deliverable:** `criteria/evaluation_criteria_v1.md`

### Phase 2 — Datasets
- [ ] **Dataset 1:** Public clinical PK data with known ground truth (Warfarin, Theophylline from NONMEM examples — open license)
- [ ] **Dataset 2:** Simulated PK/PD with known ODE parameters (simulate from published model; provide both truth and observations)
- [ ] **Dataset 3:** Erdafitinib virtual patients (De Carlo 2024) — contact authors for permission or recreate from published PopPK-PD model
- [ ] **Dataset 4:** Givinostat virtual patients (De Carlo 2025) — same
- [ ] For each: document provenance, license, identifiability properties
- [ ] **Deliverable:** `datasets/README.md` with provenance table

### Phase 3 — Reference implementations
- [ ] Implement 2–3 hybrid architectures in R and Python:
  - Neural ODE embedded in 2-compartment PK model
  - ML residual corrector on mechanistic ODE
  - PBPK-ML neural surrogate (simple case)
- [ ] Run each against each dataset; record evaluation criteria
- [ ] Fully reproducible: Docker or renv/conda, version-pinned dependencies
- [ ] **Deliverable:** GitHub repository with README, datasets/, implementations/, results/

### Phase 4 — Community launch
- [ ] Announce at ACoP session (`deliverables/conferences/acop/`)
- [ ] Define community contribution format: how to submit a new model implementation
- [ ] Governance: who reviews new submissions? How are datasets updated?

---

## Key sources
| Source | Role |
|---|---|
| `sources/web/fda_ai_guidance_2025.json` | Evaluation criteria — 7-step checklist template |
| `sources/papers/baran_gaburro_2026.json` | Reference hybrid implementations to benchmark |
| `sources/papers/de_carlo_2024.json` | Dataset 3 candidate |
| `sources/papers/de_carlo_2025.json` | Dataset 4 candidate |

## Dependencies
- `deliverables/papers/whitepaper_hybrid/` Section D — criteria must be defined first
- `community/` — GitHub org and website hosting decisions
- Resourcing decision: needs 1–2 members with strong computational background (R and/or Python)

## Open questions
- [ ] GitHub org: ISoP/MCS SIG org or personal repo that transfers later?
- [ ] Is this a living benchmark (updated as field evolves) or a fixed snapshot? Living is higher-impact but requires governance
- [ ] Dataset licenses: confirm open licensing for all included data before launch
