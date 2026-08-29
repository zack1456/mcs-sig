# MCS SIG AI/ML Working Group: Positioning Plan & Initial Tasks

*Prepared August 2026. Based on web research, literature review (PubMed), and analysis of the ISoP SIG landscape.*

---

## 1. The Landscape: What Already Exists

The ISoP AI/ML space has become crowded since the primary working document was drafted. Understanding who is doing what is essential before defining MCS's lane.

### ISoP AI/ML SIG (launched December 2023)
A standalone SIG dedicated specifically to AI/ML in pharmacometrics. Their activities:
- PAGE 2026 satellite workshop (June 2026, Dubrovnik): hands-on Neural ODEs in Julia/R, XGBoost + SHAP for covariate selection, GenAI coding tools (GitHub Copilot), regulatory panel (FDA/EMA/industry)
- ACoP 2025: tutorial on ML for explanatory variable selection in exposure–response
- ACoP 2024: panel on future impact of AI/ML across SIGs
- JSM 2026 accepted session: Applications of ML in Pharmacometrics and Statistics
- LinkedIn group and podcast for community building
- Stated focus: "practical education," "hands-on experience," "rigorous and reproducible AI approaches"

**[ISoP AI/ML SIG](https://www.isop.org/special-interest-groups/aiml-sig)** | **[PAGE 2026 Workshop](https://aiml-sig.github.io/2026-page-workshop/)**

### SxP AI/ML SubSIG
A sub-group under the Statistics and Pharmacometrics SIG. Focus: statistical ML methods — covariate selection, exposure–response, ML for population PK. Chartered jointly with ASA.

### QSP SIG AI/ML Working Group
Produced a white paper (2022): "Two heads are better than one: current landscape of integrating QSP and machine learning." Updated 2025 publications on LLMs for QSP modeling. Focus: hybrid mechanistic-ML from a QSP angle, surrogate models, virtual patient generation.

### MCS SIG — Current Working Groups
- **SAUQ** (Sensitivity Analysis/Uncertainty Quantification): active but last public update 2021
- **Optimal Control**: listed working group
- **Modeling Delays in PKPD**: listed working group
- **AI/ML**: listed but no dedicated web presence or published outputs yet — this is what we are building

### Regulatory Landscape
- **FDA draft guidance** (Jan 2025): "Considerations for the Use of Artificial Intelligence to Support Regulatory Decision Making" — introduces a 7-step risk-based credibility framework
- **FDA–EMA Joint Principles** (Jan 2026): "Guiding Principles of Good AI Practice in Drug Development" — 10 principles covering the full lifecycle
- **M15 MIDD Guidance** (finalized 2025): General principles for model-informed drug development
- None of these frameworks have been operationalized mathematically for hybrid mechanistic-ML models yet

---

## 2. The Gap Analysis: Where MCS Is Uniquely Positioned

The AI/ML SIG fills the "learn to do it" space well. The gap is in the **mathematical foundations** that make hybrid AI/ML-pharmacometric models credible, identifiable, and regulatorily defensible. No group is systematically owning this.

| Problem | Who's touching it | What's missing |
|---|---|---|
| Hybrid mechanistic-ML model architectures | AI/ML SIG (applied), QSP SIG (QSP angle) | Mathematical theory of identifiability, when hybrids help vs. hurt |
| Uncertainty quantification for ML in PK/PD | SAUQ (UQ in general), AI/ML SIG (SHAP) | Principled UQ frameworks for hybrid models; Bayesian vs. conformal vs. ensemble — no consensus |
| Identifiability of neural ODE components | Emerging academic literature (arXiv) | Not yet landed in pharmacometrics practice; no community standard |
| RL for optimal dosing | Emerging publications (De Carlo et al., Ribba) | No pharmacometric framework for reward design, safety constraints, or connection to optimal control theory |
| FDA credibility framework operationalization | QSP SIG (regulatory credibility WG, 2024) | Specific to QSP; no equivalent for hybrid ML-mechanistic PMx models |
| Benchmark datasets/protocols for hybrid models | None | Community has no agreed evaluation standard |

### Key Published Evidence of Gaps

Based on articles retrieved from PubMed:

- **Baran & Gaburro (2026)** review hybrid mechanistic-ML PK/PD models and conclude: *"The credibility of hybrid models depends on validation rigor, interpretability, and regulatory alignment rather than on algorithmic novelty. When mechanistic models fit well and sample sizes are small, adding an ML layer risks overfitting without measurable gain."* — The field needs mathematical criteria for when to use hybrids. [DOI](https://doi.org/10.3389/fphar.2026.1815118)

- **Dermawan et al. (2026)** systematic review of ML-MIDD (2015–2025, 770 records): *"ML-MIDD is a rapidly maturing interdisciplinary field... indicating growing translational relevance but continued need for validation and regulatory clarity."* [DOI](https://doi.org/10.3390/pharmaceutics18050542)

- **Gérard et al. (2025)** review AI in PK/PD/pharmacovigilance: *"Despite their potential, AI models face limitations including the quality of training data, limited explainability due to the 'black box' effect and a lack of external validation."* [DOI](https://doi.org/10.1016/j.therap.2025.09.002)

- **De Carlo et al. (2025)** RL + PK-PD for givinostat (polycythemia vera): demonstrates RL+PMx can outperform clinical protocols but the framework is still case-by-case with no generalizable pharmacometric formulation. [DOI](https://doi.org/10.1002/psp4.70012)

- **Identifiability-aware NeuralODEs (arXiv 2608.13044)**: Confidence intervals from identifiability-aware pipelines are achievable, but *"neural components are generally nonidentifiable due to redundancy"* — a direct mathematical problem needing community standards.

---

## 3. Working Group Positioning

### Core Positioning Statement
The MCS SIG AI/ML Working Group advances the **mathematical and theoretical foundations** needed for AI/ML methods to be credible, identifiable, and regulatorily acceptable in pharmacometrics. We complement—not duplicate—the AI/ML SIG's applied education work by providing the mathematical scaffolding those applications require.

### Four Differentiating Pillars

**Pillar 1 — Mathematical Rigor for Hybrid Models**
Identifiability, structural vs. practical, regularization, when to trust ML augmentation of mechanistic models. Outputs: white papers, mathematical frameworks, benchmarks.

**Pillar 2 — Principled UQ for AI/ML-Pharmacometrics**
Building on the SAUQ working group: extending sensitivity analysis and UQ methods to ML components. Bayesian, conformal, and ensemble approaches evaluated rigorously for pharmacometric contexts.

**Pillar 3 — Optimal Control ↔ Reinforcement Learning Bridge**
Leveraging MCS's existing Optimal Control working group to create a principled pharmacometric formulation of RL-based dosing: reward function design grounded in pharmacology, safety constraints from PK/PD, connection to continuous optimal control theory.

**Pillar 4 — Generative AI: Mathematical Foundations for Pharmacometrics**
Generative AI is already being used for literature review (LLMs), coding assistance, and molecular design across ISoP. MCS's distinctive contribution is the *mathematical* layer those applications lack:

- **Physics-constrained generative models** — forcing VAEs, diffusion models, and LLM-generated model code to respect mechanistic PK/PD constraints (mass balance, dose-response, identifiability). A mathematical problem no other group is systematically addressing.
- **Mathematical validation of synthetic outputs** — virtual patients generated by GANs, synthetic control arms, LLM-written differential equations. Certifying these are mathematically valid, not just plausible-looking. Connects directly to Pillar 2 (UQ).
- **LLM failure modes for mathematical model building** — structural and identifiability failure modes when LLMs generate PKPD model code or ODEs. When and why LLM-generated models violate biological or mathematical constraints.

*Out of scope for Pillar 4 (handled by AI/ML SIG / QSP SIG):* LLM literature mining, AI-assisted coding workflows, GenAI for trial protocol drafting. MCS coordinates with those groups rather than duplicating.

### Division of Labor with Other SIGs

| Activity | Lead | MCS Role |
|---|---|---|
| ML tutorials, coding workshops | AI/ML SIG | Supply mathematical content on identifiability/UQ |
| Statistical ML methods (covariate selection) | SxP AI/ML SubSIG | Advise on mathematical model selection theory |
| QSP + ML hybrids | QSP SIG | Collaborate on hybrid model validation frameworks |
| Mathematical foundations, benchmarking, credibility | **MCS SIG AI/ML WG** | Lead |
| Regulatory credibility frameworks | QSP SIG (QSP-specific), **MCS SIG AI/ML WG** (PMx-general) | Lead for PMx-general |
| GenAI coding tools, LLM literature mining | AI/ML SIG, QSP SIG | Coordinate; MCS contributes failure-mode/validation analysis |
| Physics-constrained generation, synthetic data validation | **MCS SIG AI/ML WG** | Lead |

---

## 4. Key Questions to Resolve (Working Group Scoping)

These questions should structure the first 1–2 working group meetings:

1. **Scope of hybrid models**: Focus on neural ODEs embedded in PK/PD? Or broader (QSAR, patient stratification, covariate discovery)? Recommend starting narrowest: neural ODE/hybrid mechanistic-ML PK/PD, then expanding.

2. **Benchmark standard**: Should MCS develop and host a benchmark dataset/challenge (like a pharmacometrics equivalent of MOSES for molecules)? This would be high-impact but resource-intensive.

3. **Relationship to AI/ML SIG**: Formal cross-SIG collaboration agreement? Joint sessions at ACoP? Shared membership tracking?

4. **Output format**: White paper first (like QSP SIG's 2022 paper) vs. starting with conference sessions to build community vs. a code/software deliverable.

5. **RL for dosing**: Is this a near-term priority, or does it follow once hybrid model foundations are established?

6. **Generative AI scope**: Start with physics-constrained generation (most mathematical) or LLM failure modes (more accessible/topical)? Recommend physics-constrained first as it is most distinctively MCS.

---

## 5. Initial Working Group Tasks

Organized into three phases over ~18 months.

---

### Phase 1: Foundation (Months 1–6)

**Task 1.1 — Kickoff and Scoping Meeting**
- Convene working group members (solicit from MCS SIG membership, ISoP AI/ML SIG, academic math departments)
- Decide on scope (Q4 above), output format, and collaboration agreements
- Assign leads for each pillar
- *Milestone: Charter document and working group web page live*

**Task 1.2 — Landscape Survey / Scoping Paper**
- Structured literature review: what hybrid mechanistic-ML models exist in pharmacometrics, what identifiability/UQ methods have been applied, what regulatory guidance says
- Build on existing work (ChatGPT and Claude background docs in this repo, arXiv/PubMed literature)
- Target: 10-page internal scoping paper by Month 4
- *Milestone: Scoping paper shared with ISoP MCS SIG steering committee*

**Task 1.3 — Cross-SIG Alignment Meeting**
- Joint meeting with AI/ML SIG leadership to align on division of labor
- Joint meeting with QSP SIG credibility WG (launched 2024) to avoid duplication and find collaboration opportunities
- *Milestone: Documented agreement on scope boundaries*

**Task 1.4 — Revive / Coordinate with SAUQ Working Group**
- Assess current SAUQ WG activity level (last public update 2021)
- If active: create formal coordination mechanism — SAUQ methods are directly relevant to Pillar 2
- If dormant: consider merging expertise into AI/ML WG
- *Milestone: Coordination plan with SAUQ*

---

### Phase 2: Core Deliverables (Months 6–15)

**Task 2.1 — White Paper: Mathematical Foundations of Hybrid Mechanistic-ML PK/PD Models**
- Target journal: CPT: Pharmacometrics & Systems Pharmacology or J Pharmacokinet Pharmacodyn
- Sections: (a) taxonomy of hybrid architectures, (b) structural and practical identifiability challenges for neural ODE components, (c) UQ approaches and their mathematical properties, (d) validation and benchmarking criteria, (e) regulatory alignment with FDA 7-step credibility framework
- Model on QSP SIG's 2022 white paper in scope and format
- *Milestone: Preprint by Month 12; submitted by Month 15*

**Task 2.2 — Mathematical Framework for RL-Based Precision Dosing**
- Joint task force with Optimal Control WG
- Map the mathematical equivalences and differences between: classical optimal control (Pontryagin, HJB), model predictive control, and reinforcement learning (Q-learning, policy gradient)
- Define pharmacometric requirements: PK/PD-derived state spaces, pharmacologically grounded reward functions, safety constraint formulation, handling of uncertainty
- Build on De Carlo et al. 2025 (givinostat, Q-learning) and Ribba 2023 framework
- Output: perspective/framework paper or tutorial in CPT:PSP
- *Milestone: Submitted by Month 15*

**Task 2.3 — ACoP 2026 / ACoP 2027 Session**
- ACoP 2026 (Oct 2026, National Harbor): Submit a workshop or symposium proposal on "Mathematical Foundations of AI/ML in Pharmacometrics: Identifiability, UQ, and Credibility"
- Invite speakers from MCS WG + academic math (SIAM, SMB community)
- If ACoP 2026 deadline has passed: target ACoP 2027 or PAGE 2027
- *Milestone: Session accepted and delivered*

**Task 2.4 — Benchmark Dataset/Protocol (Stretch Goal)**
- Define evaluation criteria for hybrid mechanistic-ML PK/PD models: prediction accuracy, identifiability, UQ calibration, computational cost, regulatory documentation quality
- Identify or create 2–3 benchmark datasets (public clinical PK data; simulated data with known ground truth)
- Host as reproducible analysis on GitHub
- *Milestone: Public benchmark repository launched by Month 15*

**Task 2.5 — Pillar 4: Position Paper on Generative AI for Pharmacometrics (MCS Perspective)**

- Scoping paper distinguishing MCS's focus from AI/ML SIG and QSP SIG GenAI work
- Section A: Physics-constrained generative models — mathematical approaches to enforcing mechanistic constraints (mass balance, dose-response) in VAEs, diffusion models, and LLM-generated ODEs
- Section B: Mathematical validation of synthetic pharmacometric data — criteria for virtual patient fidelity, synthetic control arm validity, distributional coverage
- Section C: LLM failure modes for model building — taxonomy of identifiability and structural errors in LLM-generated PK/PD model code, with illustrative examples
- Target: perspective article in CPT:PSP or Frontiers in Pharmacology; preprint first
- *Milestone: Preprint by Month 14*

---

### Phase 3: Community and Regulatory Engagement (Months 12–18)

**Task 3.1 — Regulatory Comment / Position Paper**
- Respond to FDA draft guidance "Considerations for the Use of AI to Support Regulatory Decision Making" with an ISoP MCS SIG perspective
- Focus on mathematical operationalization of the 7-step credibility framework for hybrid mechanistic-ML models
- Coordinate with ISoP regulatory affairs; co-author with QSP SIG and SxP SIG where relevant
- *Milestone: Comment submitted to FDA docket; published as ISoP position paper*

**Task 3.2 — Webinar Series**
- Minimum 3 webinars targeted at ISoP members; differentiated from AI/ML SIG's applied workshops
- Topics: (1) Identifiability of neural components in mechanistic PK/PD models, (2) UQ methods for hybrid models: a mathematical comparison, (3) From optimal control to reinforcement learning in pharmacometrics, (4) Physics-constrained generative models: what MCS brings to GenAI
- Invite academic collaborators from SIAM, SMB — consistent with MCS SIG's historical bridge-building mission
- *Milestone: Series launched by Month 14*

**Task 3.3 — Cross-SIG AI/ML Coordination Hub**
- Propose a standing cross-SIG AI/ML coordination group (MCS, AI/ML SIG, QSP, SxP) to prevent duplication and share outputs
- Build on the ACoP 2023 cross-SIG session precedent
- *Milestone: Coordination group formally established*

---

## 6. Resource Requirements

| Resource | Needed for |
|---|---|
| 1 WG Co-Chair with strong math background (ODE theory, UQ) | All tasks |
| 1 WG Co-Chair with pharmacometrics background (NONMEM/Monolix experience) | Grounding tasks in practice |
| 4–6 steering committee members spanning: neural ODEs, optimal control/RL, UQ/SA, regulatory science | Task leads |
| Academic liaisons (SIAM Life Sciences, SMB) | Task 1.1, webinar series |
| ISoP communications support | ACoP session, webinars, white paper PR |
| GitHub repository | Benchmark task (2.4) |

---

## 7. Success Metrics (18-Month Horizon)

- White paper submitted (Pillar 1/2: hybrid model mathematical foundations)
- RL/optimal control framework paper submitted (Pillar 3)
- Generative AI position paper preprint posted (Pillar 4)
- ACoP/PAGE session delivered
- FDA regulatory comment submitted
- ≥4 webinars delivered (one per pillar)
- Cross-SIG coordination group established
- Working group membership: 15+ active members
- Benchmark repository with ≥2 datasets and reproducible analysis

---

## Sources Consulted

**Web:**
- [ISoP AI/ML SIG](https://www.isop.org/special-interest-groups/aiml-sig)
- [PAGE 2026 AI/ML Workshop](https://aiml-sig.github.io/2026-page-workshop/)
- [ISoP MCS SIG](https://sites.google.com/view/mcssig/mcs-sig)
- [MCS SAUQ Working Group](https://sites.google.com/view/mcs-sauq-wg)
- [SxP AI/ML SubSIG at PAGE](https://www.page-meeting.org/Abstracts/artificial-intelligence-machine-learning-ai-ml-subsig-of-sxp-a-collaboration-to-advance-pharmacometrics-using-ai-ml-methods-2/)
- [FDA AI Drug Development](https://www.fda.gov/about-fda/center-drug-evaluation-and-research-cder/artificial-intelligence-drug-development)
- [ACoP 2026 Hackathon](https://www.isop.org/blogs/isop/2025/10/01/hackathon-new-for-acop-2026)
- [AI in Pharmacometrics: Strategic Vision (ACoP 2026 event)](https://www.eventbrite.com/e/ai-in-pharmacometrics-a-strategic-vision-for-the-next-five-years-md-usa-tickets-1993618338116)
- [Identifiability-aware NeuralODEs (arXiv)](https://arxiv.org/html/2608.13044)
- [QSP+ML White Paper (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8837505/)
- [QSP+ML LLM 2025 update (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12170689/)

**Literature (PubMed) — full, current library in `sources/index.json`. Key papers by pillar:**

*Pillar 1 — Hybrid Models:*

- Baran & Gaburro (2026). Hybrid mechanistic-ML PK/PD with digital biomarkers. [DOI](https://doi.org/10.3389/fphar.2026.1815118)
- Dermawan et al. (2026). Global trends in integrating ML with MIDD. [DOI](https://doi.org/10.3390/pharmaceutics18050542)
- Janssen et al. (2024). Deep compartment models + physiological constraints; neural-ODE underperforms on sparse data. [DOI](https://doi.org/10.1007/s10928-024-09906-x)
- Elmokadem et al. (2024). HDCM: Bayesian IIV+RUV+UQ for hybrid PK (Metrum). [DOI](https://doi.org/10.1111/cts.70045)
- Karlsen et al. (2025). Systematic review: pop PK covariate selection SCM→AI. [DOI](https://doi.org/10.1002/psp4.70032)

*Pillar 2 — UQ / Identifiability:*

- Raue et al. (2009). Profile likelihood: structural vs. practical identifiability. [DOI](https://doi.org/10.1093/bioinformatics/btp358)
- Janzén et al. (2017). Structural identifiability for NLME mixed-effects models. [DOI](https://doi.org/10.1016/j.mbs.2017.10.009)
- Villaverde et al. (2016). STRIKE-GOLDD: Lie derivative identifiability method. [DOI](https://doi.org/10.1371/journal.pcbi.1005153)
- Díaz-Seoane et al. (2023). STRIKE-GOLDD 4.0: ProbObsTest + GUI. [DOI](https://doi.org/10.1093/bioinformatics/btac748)
- Najjar et al. (2024). GSA tutorial for OSP Suite PBPK: Morris, Sobol, EFAST. [DOI](https://doi.org/10.1002/psp4.13256)
- Chenel et al. (2026). PBPK best practices + ICH M15 regulatory framework. [DOI](https://doi.org/10.1002/psp4.13299)

*Pillar 3 — RL / Optimal Control:*

- De Carlo et al. (2025). RL + PK-PD for givinostat. [DOI](https://doi.org/10.1002/psp4.70012)
- De Carlo et al. (2024). RL + PK-PD for erdafitinib. [DOI](https://doi.org/10.1002/cpt.3176)
- Ribba (2023). Reinforcement learning for precision dosing. [DOI](https://doi.org/10.3389/fphar.2022.1094281)
- Irie et al. (2025). DQN for infliximab in pediatric Crohn's: first real-world RL validation. [DOI](https://doi.org/10.1002/cpt.3589)

*Pillar 4 — Generative AI / LLMs:*

- Gérard et al. (2025). AI in PK/PD/pharmacovigilance. [DOI](https://doi.org/10.1016/j.therap.2025.09.002)
- Shin et al. (2024). ChatGPT and Gemini for NONMEM coding: errors persist. [DOI](https://doi.org/10.1007/s10928-024-09921-y)
- Zheng et al. (2025). 7 LLMs × 13 NONMEM tasks; o1/gpt-4.1 near-perfect with optimized prompt. [DOI](https://doi.org/10.1002/psp4.70125)
- Androulakis et al. / ISoP QSP SIG (2025). ML and LLMs for QSP: QSP SIG's AI/ML roadmap. [DOI](https://doi.org/10.1007/s10928-025-09984-5)
- Dette et al. (2025). Digital twin systematic review; generative DTs. [DOI](https://doi.org/10.1016/j.csbj.2025.11.047)

*Confirmed literature white spaces (0 PubMed results across multiple searches):*

- Conformal prediction for PK/PD — genuine first-mover opportunity for MCS WG
- Pontryagin/HJB optimal control for pharmacokinetics — math journals not in PubMed
- Synthetic data / GAN-based virtual patients — query expansion intractable
