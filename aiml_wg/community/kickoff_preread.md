# MCS SIG AI/ML Working Group — Kickoff Pre-Read
**For:** Working group members, kickoff meeting August 28, 2026
**Prepared by:** Chakravarty S, Kenz Z (co-chairs)
**Reading time:** ~15 minutes

---

## 1. Why this working group, and why now

AI and machine learning have reached every stage of the pharmaceutical pipeline. Drug discovery, trial design, pharmacovigilance, regulatory submissions — AI/ML methods are being applied across all of them. In 2021 alone, approximately 132 regulatory submissions to the FDA mentioned AI/ML methods, a roughly 10-fold jump from 14 in 2020 (Liu et al. 2023). That number understates the true adoption; regulatory use likely represents a fraction of actual deployment in R&D.

For pharmacometricians and quantitative scientists, this creates both opportunity and risk. The opportunity: AI/ML can augment mechanistic models, speed up trial analysis, and enable truly individualized dosing. The risk: methods adopted without mathematical rigor — without attention to identifiability, uncertainty quantification, and interpretability — will produce models that look good on training data and fail in clinical contexts, or fail regulatory review, or both.

The MCS SIG AI/ML Working Group exists to address that risk. Our role is not to survey AI/ML broadly (other groups and SIGs do that) but to bring mathematical depth — the tools of dynamical systems, identifiability analysis, optimal control, and uncertainty quantification — to the specific problems where AI/ML meets pharmacometrics.

---

## 2. How we fit in the ISoP ecosystem

ISoP has several SIGs and working groups active in AI/ML:
- **QSP SIG**: AI/ML for quantitative systems pharmacology (systems-scale mechanistic models, omics data). Published a white paper in 2022 (Zhang et al., JPKPD 49:5–18).
- **SxP SIG**: Statistics and pharmacometrics — Bayesian inference, model selection, adaptive designs.
- **PMxP SIG**: Data programming — NLP/LLMs for data pipelines.

The MCS SIG AI/ML WG is differentiated by its emphasis on **mathematical rigor at the model level**: identifiability of hybrid mechanistic-ML components, uncertainty quantification for AI-augmented PK/PD, optimal control and RL formulations for dosing, and physics-constrained generative models. We are peers with the other groups, not competitors — and we expect to collaborate, especially with the MCS Optimal Control WG.

---

## 3. Our four pillars

The working group organizes its activity around four technical pillars. Each pillar corresponds to a set of mathematical and computational questions that are either unanswered or underserved in the current literature.

### Pillar 1 — Hybrid mechanistic-ML models

Neural ODEs and related architectures embed ML components inside differential equation systems. Used in pharmacometrics, they can learn residual dynamics or augment compartmental models. The mathematical gap: **how do you know the ML component is identifiable from the available clinical data?** A non-identifiable ML module produces confident-looking but meaningless parameter estimates. A very recent preprint (Campo-Manzanares & Balsa-Canto, arXiv 2608.13044, August 2026) proposes the first architecture-level solution — identifiability-aware design reduces parameter confidence intervals from 881% to 84% and cuts model size by 20–50× — but this work needs community scrutiny and extension to NLME settings.

**Phase 1 focus:** Architecture taxonomy; structural identifiability of neural ODE components; hybrid vs. pure-mechanistic decision criteria.

### Pillar 2 — Uncertainty quantification for AI/ML-pharmacometrics

Regulatory bodies and clinical decision-makers need to know not just what a model predicts, but how confident that prediction is. For AI/ML-augmented PK/PD models, standard frequentist confidence intervals are inadequate — they don't capture model-form uncertainty in the ML component. This pillar develops rigorous UQ approaches: Bayesian methods for hybrid models, conformal prediction for individual patient forecasts, ensemble uncertainty for pharmacometric applications.

**Phase 1 focus:** Bayesian UQ for hybrid mechanistic-ML; comparative assessment of UQ methods; coordination with SxP SIG's Bayesian expertise.

### Pillar 3 — Optimal control and RL for precision dosing

Reinforcement learning has been used to design individualized dosing protocols, with promising results (De Carlo et al. 2024: Q-learning-based erdafitinib dosing achieves 97.87% vs. 70.21% efficacy at month 4, vs. FDA protocol). But the mathematical underpinnings — reward function design, POMDP for partially observed patient state, connections to classical Hamilton-Jacobi-Bellman optimal control theory — are underexplored in pharmacometrics. This pillar maps the mathematical landscape and identifies where RL and classical control converge.

**Phase 1 focus:** Lighter effort in Phase 1; one member tracks literature and contributes to scoping paper; joint paper with Optimal Control WG in Phase 2.

### Pillar 4 — Generative AI foundations for pharmacometrics

Generative models (VAEs, diffusion models, LLMs) are being applied to drug design, patient simulation, and model generation. For pharmacometrics specifically: physics-constrained generative models that respect ODE structure are the most mathematically tractable entry point, and validation frameworks for synthetic patient populations are essentially missing. LLMs for pharmacometric model generation are a second frontier — with known failure modes that the WG should document.

**Phase 1 focus:** Physics-constrained generative models; synthetic patient validation; LLM failure modes position paper.

---

## 4. What we plan to produce

Over 18 months, the working group aims to produce:

**Phase 1 (months 1–6):**
- Scoping paper: ~10 pages, internal, mapping the 4 pillars to the literature and to gaps — this becomes the foundation for all external outputs
- Pillar 1 technical review: structural identifiability of neural ODE components in pharmacometrics
- Webinar #1: Hybrid mechanistic-ML in pharmacometrics (Pillar 1)

**Phase 2 (months 7–12):**
- White paper (Pillars 1+2): flagship external output targeting CPT:Pharmacometrics & Systems Pharmacology or JPKPD, co-authored across the WG
- ACoP session: workshop or tutorial session (proposal due ~Q1 2027)
- Pillar 3 paper: joint with MCS Optimal Control WG
- Webinars #2 and #3

**Phase 3 (months 13–18):**
- Pillar 4 position paper (generative AI)
- Webinar #4
- Reproducible benchmark repository (stretch goal)
- Regulatory comment / input if FDA docket is still open

---

## 5. Six decisions to make at the kickoff

The meeting will work through six scoping decisions. Each is described in detail in the [kickoff agenda](kickoff_agenda.md). The short version:

| # | Decision | Recommended stance |
| --- | --- | --- |
| 1 | Hybrid model scope | Neural ODEs first, then broaden |
| 2 | First external deliverable | White paper first, ACoP in parallel |
| 3 | Pillar 3 (RL) bandwidth | Parallel but lighter in Phase 1 |
| 4 | Pillar 4 GenAI scope | Physics-constrained first; LLMs = position paper |
| 5 | Cross-SIG relationship | Coordinate Phase 1, co-author Phase 2 |
| 6 | Benchmarks | Phase 3 / stretch goal |

These stances are recommendations, not mandates. The kickoff is the right moment to revise them based on member expertise and interest.

---

## 6. Background reading (optional, prioritized)

If you have 30–60 minutes before the meeting, the most useful background reads are:

1. **Liu et al. 2023** — FDA landscape of AI/ML in regulatory submissions 2016–2021. Establishes the regulatory context for everything we do. (Journal of Clinical Pharmacology)
2. **Zhang et al. 2022** — QSP SIG white paper on QSP+ML integration. The model for our own white paper; also shows what the sister SIG has already covered. (JPKPD 49:5–18)
3. **De Carlo et al. 2024** — RL + PK/PD for erdafitinib precision dosing. The clearest worked example of Pillar 3 methods. (Clin Pharmacol Ther)
4. **Campo-Manzanares & Balsa-Canto 2026** — iNODE preprint. The most directly relevant recent work for Pillar 1. (arXiv 2608.13044)

---

*Questions before the meeting? Contact the co-chairs: Shreyas Chakravarty and Zack Kenz.*
