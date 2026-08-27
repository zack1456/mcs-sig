# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a research and content development project for the **AI/ML Working Group** of the **Mathematical and Computational Sciences (MCS) Special Interest Group** of the International Society of Pharmacometrics (ISoP). The goal is to develop ideas, content, and initiatives for the working group based on the primary planning document and background literature.

There is no software to build or test. Work here is primarily reading, synthesizing, and drafting documents.

## Key Terminology

- **ISoP**: International Society of Pharmacometrics
- **MCS SIG**: Mathematical and Computational Sciences Special Interest Group (founded 2016, ~70 members). Sister SIGs: QSP (Quantitative Systems Pharmacology), SxP (Statistics and Pharmacometrics), Clin PMx (Clinical Pharmacometrics), PMxP (Pharmacometrics Data Programming)
- **MIDD**: Model-Informed Drug Development — the overarching framework all SIGs work within
- **PMx / pharmacometrics**: Pharmacometric modeling & simulation (PK/PD, nonlinear mixed-effects models, etc.)
- **PK/PD**: Pharmacokinetics/Pharmacodynamics
- **ACoP**: American Conference on Pharmacometrics (annual ISoP conference)
- **MCS SIG working groups**: Modeling Delays in PKPD; Optimal Control; Sensitivity Analysis/Uncertainty Quantification; AI/Machine Learning (this project's focus)

## Document Structure

```
aiml_wg/
  MCS SIG AI working group 2026v0.3.docx   ← PRIMARY WORKING DOCUMENT (binary, use Word/LibreOffice)
  background/
    CPT Pharmacom...Moore.pdf              ← MCS SIG origin story (2019), foundational context
    crossSIG paper.pdf                     ← Cross-SIG collaboration paper (2025), all SIG missions/working groups
    ai_ml_pharma_RD_fromChatGPT.pdf        ← AI/ML survey across pharma R&D (ChatGPT-generated)
    ai_ml_pharma_workflows_fromClaude.pdf  ← AI/ML survey grounded in 2023–2026 PubMed literature (Claude-generated)
```

The `.docx` file cannot be read directly by Claude Code tools — use external tools or export to text/PDF first.

## Domain Context

The MCS SIG AI working group sits at the intersection of:
- **Traditional pharmacometrics** (ODE-based compartmental models, NONMEM/Monolix/Phoenix, nonlinear mixed-effects)
- **Mathematical methods** promoted by MCS: dynamical systems, optimal control, sensitivity/identifiability analysis, delay/stochastic DEs
- **AI/ML methods** now transforming the pharma pipeline end-to-end

Key AI/ML application areas for the working group (from background literature):
1. **Literature mining**: NLP, LLMs (RAG), knowledge graphs (BioBERT, PubMedBERT) for target ID and evidence synthesis
2. **Target ID & lead discovery**: GNNs for drug–target interaction, AlphaFold integration, generative molecular design (VAEs, GANs, diffusion)
3. **Model building**: Hybrid mechanistic–ML PK/PD (NeuralODEs, ML-augmented compartmental models), QSAR/ADMET prediction
4. **Clinical trial optimization**: Patient stratification via ML, synthetic control arms, adaptive trial design
5. **Pharmacovigilance**: Automated ADR signal detection, Bayesian network causality tools
6. **Explainable AI (XAI)**: SHAP, attention visualization — critical for regulatory acceptance

Cross-cutting themes across all stages: multi-modal data integration, transfer learning from foundation models, uncertainty quantification, model interpretability for regulatory contexts, data standardization (CDISC).

## Working Group Positioning

The MCS SIG AI/ML working group should differentiate from similar AI/ML efforts in other SIGs (QSP, SxP) by emphasizing **mathematical rigor**: uncertainty quantification, model identifiability, hybrid mechanistic–ML approaches, and optimal control — areas where MCS expertise is distinctive. All SIGs share interest in AI/ML; MCS's value-add is the mathematical and computational depth.

The MCS SIG website is at: https://sites.google.com/view/mcssig/
