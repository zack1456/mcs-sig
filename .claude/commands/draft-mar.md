---
description: Draft a Model Analysis Report (MAR) structured per ICH M15 / ASME V&V 40 for a source record in the library. Example mode (default) produces a worked MAR suitable for white paper inclusion; guidance mode drafts white paper Section E (regulatory alignment).
---

Draft a Model Analysis Report for a source in `aiml_wg/sources/`.

## Arguments

`$ARGUMENTS` is a source ID optionally followed by a mode: `example` (default) or `guidance`.

Examples: `elmokadem_2024` · `janssen_2024 guidance` · `giacometti_2025 example`

If no source ID is given, list `hybrid_foundations` paper records from `aiml_wg/sources/index.json` and ask the user to pick one. If no mode is given, use `example`.

---

## Steps

**1. Parse arguments and load primary record**

Read `aiml_wg/sources/_schema.json` (confirm field names). Then read the primary source record from `aiml_wg/sources/papers/{source_id}.json` (or the appropriate subfolder).

Note the `read_depth`: if `abstract_only`, surface this prominently — several MAR sections will be data-limited and must be flagged. If `sections_key` or `full_text`, proceed normally.

**2. Load related records**

For each ID in `relationships.cites`, `relationships.extends`, and `relationships.cited_by`, read the corresponding JSON record from `aiml_wg/sources/`. These form the supporting evidence base — especially for §7 validation activities and §6 model risk.

Also read these regulatory context records if present in the library:
- `aiml_wg/sources/papers/chenel_2026.json` (ICH M15 / PBPK best practices)
- `aiml_wg/sources/web/fda_ai_guidance_2025.json` (FDA 7-step credibility framework)
- `aiml_wg/sources/papers/liu_2023.json` (regulatory stakes)
- `aiml_wg/sources/papers/raue_2009.json` (profile likelihood — structural identifiability)
- `aiml_wg/sources/papers/najjar_2024_gsa.json` (GSA for PBPK — parametric uncertainty)

For identifiability evidence, also check for any of: `villaverde_2016_strikegodd`, `diazseoane_2023_strikegodd4`, `janzen_2017`, `campo_manzanares_2026`.

**3. Clarify context of use and model influence (required human input)**

Before writing any section, ask the user two questions:

> **A. Context of use:** In one sentence, what decision or analysis is this model being used to support? (e.g., "Predict individual PK trajectories for sparse-data dose optimization in early-phase oncology trials")
>
> **B. Model influence level:** How much does the model's output control the downstream action?
> - **Low** — one input among several; no clinical action taken on model output alone
> - **Low–Medium** — informs study design or dose range; clinical team retains full discretion
> - **Medium** — model output is a primary input to a regulatory or clinical decision; human review required before action
> - **High** — model output directly determines clinical action with minimal human override

If the user is unsure, suggest: for exploratory pharmacometrics research, **Low–Medium** is typically appropriate. For regulatory submissions, **Medium** is the minimum honest assessment.

Record the user's answers as `[CoU]` and `[INFLUENCE]`. These anchor §2, §4, and §9.

---

**4. Generate the MAR — section by section**

Use the field mapping below. For each section, write complete prose — not bullet notes. Wrap any statement where the source record is `abstract_only` and the specific claim is not confirmed in the abstract text with `⚠️ [DATA LIMITED — upgrade to full_text to confirm]`.

---

### §1 Purpose and scope

State: this document is an ICH M15 Model Analysis Report (MAR) for the model described in `{title}` (`{source_id}`, `{year}`). In `example` mode, add: "This is a worked illustrative example produced by the MCS SIG AI/ML Working Group to demonstrate credibility assessment for hybrid pharmacometric models; it does not constitute a regulatory submission." In `guidance` mode, omit the illustrative qualifier.

Name ASME V&V 40-2018 as a complementary engineering standard applied in Appendix A. Describe what each appendix adds: Appendix A adds Credibility Matrix, A–D risk taxonomy, and completeness audit; Appendix B documents MAP status and totality-of-evidence statement.

---

### §2 Question of interest

Derive from `[CoU]`, `content.gaps_addressed`, and `content.key_findings`. State one specific bounded question:

> *For [the model's unit of analysis], does [the method/intervention] produce [primary output] relative to [comparator]? Under what conditions (sample size, disease, data richness) does the hybrid approach improve on the mechanistic baseline?*

The question must be specific enough to bound the context of use. If `gaps_addressed` is empty, flag this and ask the user to supply it.

---

### §3 Context of use

**§3.1 Primary CoU** — one paragraph blockquote using `[CoU]`:
> **Primary CoU:** [user-supplied CoU statement]. The model outputs [list from `content.methods_discussed` what the model produces]. This CoU is [exploratory / regulatory support / submission-grade] and does not extend to [select 1–2 first items from `content.limitations`].

**§3.2 In scope** — bullet list drawn from `content.methods_discussed` and `content.key_findings`. Each bullet should name a specific capability, not a broad topic.

**§3.3 Out of scope** — one bolded bullet per entry in `content.limitations`, with a one-sentence explanation of *why* each is out of scope. Include:
- Any paradigm boundary (no real-world validation, species boundary, etc.)
- Regulatory scope exclusion if `[INFLUENCE]` is Low or Low–Medium ("This CoU is exploratory research, not a primary evidence package for IND/NDA")
- Any identifiability limitation flagged in related records or the record's own limitations

---

### §4 Model influence

Produce a table:

| Decision slot | What the model output drives | Influence |
|---|---|---|
| [specific use case 1] | [specific downstream action] | [INFLUENCE] |
| [specific use case 2] | [specific downstream action] | [INFLUENCE or lower] |

Derive decision slots from `[CoU]` and `content.gaps_addressed`. After the table:

> **Overall influence level: [INFLUENCE].** [Justify: e.g., "No clinical action is taken solely on this model's output; each prediction would be followed by empirical measurement before patient-level decisions are made."] This [INFLUENCE] influence level calibrates the validation burden: the standard is [sufficiency for exploratory triage / regulatory evidentiary strength].

---

### §5 Consequence of a wrong decision

Produce a table with one row per decision slot from §4:

| Decision | Wrong-answer consequence | Catch mechanism | Residual risk |
|---|---|---|---|
| [slot] | [specific harm: e.g., underdosing risk, failed trial design] | [empirical check: TDM, safety monitoring, independent PK study] | [Low/Medium/High] |

For pharmacometric models, standard catch mechanisms include: therapeutic drug monitoring, PK sampling at early clinical stages, independent cohort validation. Pull any catch mechanisms mentioned in `content.limitations` or `content.key_findings`.

---

### §6 Model risk

**§6.1 Sources of model risk** — three paragraphs:

*Parametric uncertainty:* Which parameters dominate the model output? If a sensitivity analysis is in `content.numerical_findings`, reference it here with the specific metric and value. If related records include GSA (`najjar_2024_gsa`) or profile likelihood (`raue_2009`), cite the method class and note whether it was applied to this model. If no SA was performed, flag: ⚠️ `[DATA LIMITED — no sensitivity analysis found; parametric uncertainty uncharacterised]`.

*Structural uncertainty:* What cannot the model represent? Draw directly from `content.limitations`. If related identifiability records are loaded (STRIKE-GOLDD, `janzen_2017`, `campo_manzanares_2026`), state whether structural identifiability of the hybrid components was assessed and what the result was. If not assessed, flag: ⚠️ `[Structural identifiability of neural/ML components not assessed — see M1.2 workstream]`.

*Extrapolation uncertainty:* Identify any predictions beyond the calibration domain. Common examples for hybrid PK/PD models: novel drug classes, pediatric populations, sparse vs. dense data regimes, disease populations not represented in training. Draw from `content.limitations` and any `[inferred]`-tagged `content.key_findings`.

**§6.2 Risk-mitigating design choices** — numbered list of decisions made specifically to reduce model risk. Draw from `content.methods_discussed`, `content.tools_software`, and `content.key_findings`. Examples of what qualifies: Bayesian priors on NN weights (prevents overfitting at small N), IIV estimation jointly with NN weights (prevents misspecification), mechanistic constraints on neural ODE structure. Each item must name the design choice and state what risk it mitigates. Include 3–6 items; skip generic good-practice items not specific to this model.

---

### §7 Model evaluation

**§7.1 Verification** — bullet list of checks confirming implementation correctness. Draw from `content.tools_software` (e.g., Julia/Turing.jl: MCMC convergence diagnostics; PyTorch: gradient checks). If a test suite is mentioned in `provenance.notes`, cite it. If none is mentioned, flag: ⚠️ `[No automated verification suite documented — recommended for regulatory-grade use]`.

**§7.2 Validation activities** — table with one row per quantitative result in `content.numerical_findings` where `is_primary_finding: true`. Also include any validation activities from related records that directly tested the same model class.

| Activity | Type | Specific quantitative standard | CoU element |
|---|---|---|---|
| [description from numerical_findings] | [V / Val / UQ] | [value from numerical_findings, e.g. "RMSE 4.2 vs baseline 6.1 on held-out dalbavancin cohort N=218"] | [§3 CoU element it addresses] |

Classification:
- **V** — Verification: code matches specification
- **Val** — Validation: model output agrees with independent experimental data
- **UQ** — Uncertainty quantification: range of outputs under realistic parameter variation

The standard must be a specific, checkable criterion. "Model was validated" is not a standard; "RMSE on held-out cohort ≤ X" is.

For `abstract_only` records with no numerical findings: ⚠️ `[DATA LIMITED — no quantitative validation standards available from abstract; upgrade to full_text before regulatory use]`.

**§7.3 Open validation items** — table of unresolved items. Draw from `content.limitations` entries not already addressed by a §7.2 row, and from `⚠️ DATA LIMITED` flags above.

| Item | What it would add | Status |
|---|---|---|
| [limitation] | [what addressing it would establish] | [Not yet done / Awaiting data / Out of scope] |

---

### §8 Residual uncertainties and limitations

One subsection per entry in `content.limitations`. Each subsection:

1. What is limited (direct quote or close paraphrase of the limitation)
2. Why (root cause: structural, parametric, paradigm boundary, or documented assumption)
3. **Consequence for decisions:** One paragraph starting with this exact label — what this means for each decision slot in §4, and whether it materially affects any in-scope CoU element.

---

### §9 Model impact and credibility summary

**§9.1 Totality of evidence statement** — required by ICH M15:
> "The model described in `{title}` is one input to a structured human expert judgment within a broader experimental evidence package. At [INFLUENCE] decision influence, model predictions inform but do not independently determine [downstream action]. Each model-supported conclusion is expected to be corroborated by [empirical check from §5 catch mechanisms] before clinical or regulatory action."

**§9.2 ICH M15 credibility summary table**

| ICH M15 element | Assessment | Section |
|---|---|---|
| Question of interest | [one sentence] | §2 |
| Context of use | [one sentence] | §3 |
| Model influence | [INFLUENCE level + brief rationale] | §4 |
| Consequence of wrong decision | [highest-residual-risk decision slot] | §5 |
| Model risk | [dominant risk source from §6.1] | §6 |
| Model evaluation | [validation sufficiency statement] | §7 |

End with:
> **Overall credibility assessment:** This model is fit for its stated purpose — [CoU] at [INFLUENCE] decision influence. The model is not positioned as [next-level use, e.g. a primary regulatory submission package] and should not be used as one without [what would be needed: prospective MAP, cross-functional sign-off, held-out validation on an independent cohort].

**§9.3 MAR-readiness for future regulatory use** — state the three procedural steps needed to upgrade this document to full regulatory submission grade:
1. Prospective Model Analysis Plan (MAP) filed before analysis begins
2. Cross-functional credibility sign-off (clinical pharmacology, statistics, clinical team)
3. MAR reformatting to ICH M15 required structure with institutional attribution

State explicitly: these are procedural steps, not technical gaps.

---

**5. Generate Appendix A — ASME V&V 40 analysis**

**A.1 V&V 40 workflow mapping** — table showing how each V&V 40 step maps to the MAR section where it is addressed. Draw from the ICH M15 element table in §9.2.

**A.2 Credibility Matrix** — reproduce the §4 decision influence table. Add a "Sufficient?" column (Yes / Conditional / No / N/A) for each row. "Conditional" means: sufficient given the stated caveat from §7.3 open items. Never mark all rows "Yes" if any §7.3 open item touches an in-scope CoU element.

**A.3 Risk-category A–D taxonomy** — for each distinct failure mode identified in §6.1 and §8, write one paragraph:
- Category label (A = most severe, D = least)
- One-sentence description of the failure mode
- Likelihood (Low / Medium / High) with justification referencing specific validation evidence from §7.2 — not bare assertion
- Catch mechanism

**A.4 Behaviour-coverage completeness audit** — state which model behaviours were checked against reference data (experimental or published models). Use `content.numerical_findings` as the evidence base. For each behaviour: REPRESENTED (addressed by a §7.2 row) / PARTIAL (addressed but with a §7.3 open item) / ABSENT (not tested). State overall: "N REPRESENTED, M PARTIAL, K ABSENT." If all relevant behaviours are REPRESENTED, the completeness claim stands; if any ABSENT item is in-scope for the CoU, flag it.

**A.5 V&V 40 elements that exceed ICH M15 minimum** — list which V&V 40 tools were applied and why each goes beyond what M15 alone requires.

---

**6. Generate Appendix B — ICH M15 elements beyond V&V 40**

**B.1 Model Analysis Plan (MAP)** — state whether a prospective MAP exists. For library records representing published research (not an active submission), write: "No prospective MAP was filed; this model was developed iteratively as a research tool. Retrospective equivalents include: [list any development plan documents mentioned in provenance.notes or methods]. A prospective MAP would be required before regulatory submission."

**B.2 Cross-functional credibility sign-off** — state whether cross-functional review has been conducted. For a published research paper: "Cross-functional review has not been conducted outside the peer review process. A regulatory submission would require sign-off from [clinical pharmacology, biostatistics, clinical team]."

**B.3 Totality of evidence** — restate §9.1 in explicit ICH M15 language.

---

**7. Write output**

Determine the output path:
- `example` mode → `aiml_wg/deliverables/papers/whitepaper_hybrid/mar_example_{source_id}.md`
- `guidance` mode → `aiml_wg/deliverables/papers/whitepaper_hybrid/section_e_regulatory_draft.md`

Write the complete document with all sections and both appendices.

---

**8. Append ICH M15 completeness checklist**

After the document body, append a checklist. Mark each item:
- ✅ Complete — section present and populated from source data
- ⚠️ Data-limited — section present but flagged `[DATA LIMITED]`
- ❌ Missing — section absent or not attempted

```
## ICH M15 MAR Completeness Checklist

- [ ] §2 Question of interest: specific, bounded, anchored to CoU
- [ ] §3.1 CoU: one-paragraph blockquote
- [ ] §3.2 In scope: bullet list of model capabilities
- [ ] §3.3 Out of scope: bolded items with root-cause explanations
- [ ] §4 Model influence: decision table; overall level stated; validation burden calibrated
- [ ] §5 Consequence table: decision | consequence | catch mechanism | residual risk
- [ ] §6.1 Sources of model risk: parametric, structural, extrapolation addressed
- [ ] §6.2 Risk-mitigating design choices: 3–6 model-specific items
- [ ] §7.1 Verification: implementation correctness checks
- [ ] §7.2 Validation table: Activity | Type | Specific quantitative standard | CoU element
- [ ] §7.3 Open items: honest; each with status
- [ ] §8 Residual uncertainties: one subsection per limitation; consequence paragraph per slot
- [ ] §9.1 Totality of evidence: explicit ICH M15 statement
- [ ] §9.2 ICH M15 summary table: one row per element; overall credibility sentence
- [ ] §9.3 MAR-readiness: three procedural steps for regulatory upgrade
- [ ] Appendix A: Credibility Matrix; A–D taxonomy; completeness audit; V&V 40 exceedances
- [ ] Appendix B: MAP status; cross-functional sign-off status; totality of evidence restatement
```

---

**9. Confirm**

Report:
- Output file path
- Mode used
- Source record read depth (and whether DATA LIMITED flags were inserted)
- Count of §7.2 validation rows populated vs. open items in §7.3
- Any sections where user input is still needed to complete the draft
