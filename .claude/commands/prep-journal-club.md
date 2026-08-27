---
description: Generate a structured journal club discussion guide from a source record in the library
---

Generate a journal club discussion guide for a source in `aiml_wg/sources/`.

## Arguments
`$ARGUMENTS` is a source ID (e.g. `de_carlo_2025`) or a partial title/author name. If empty or ambiguous, list available sources and ask the user to pick one.

## Steps

**1. Find and read the record**
Glob `aiml_wg/sources/**/*.json` to find the file matching `$ARGUMENTS`. Read the JSON record.

If `read_depth` is `abstract_only`, note this prominently in the output — discussion questions should be framed around what the abstract reveals and what remains unknown without the full text.

**2. Read related records**
Read any records listed in `relationships.cites`, `relationships.cited_by`, and `relationships.extends` to understand how this source connects to the rest of the library.

**3. Generate the discussion guide**

Output a markdown document with these sections:

---

### [Title] — Journal Club Discussion Guide
*[Authors] · [Journal] · [Year] · [DOI link]*
*Source record: `[id]` · Read depth: [read_depth]*

---

#### Paper in 3 sentences
[A tight, accessible summary: what problem, what approach, what result. No jargon unexplained.]

#### Why this matters for the WG
[1–3 bullet points connecting to specific WG pillars and gaps. Reference specific workstreams from `methods/` where applicable — e.g., "Directly informs M3.2 (MDP formulation for PK/PD precision dosing)."]

#### Key claims to examine
[3–5 specific claims from `extracted_claims` or `key_findings`, each framed as a question for group evaluation:]
- **Claim:** "[exact quote or close paraphrase]"
  - *Does the evidence support this? What would strengthen or weaken it?*

#### Quantitative results worth scrutinizing
[Pull 3–5 items from `numerical_findings` where `is_primary_finding: true`. For each:]
- **[metric description]:** [value] vs. [baseline if any]
  - *What assumptions underlie this number? How sensitive is it?*

#### Connections to our library
[List related records and state the relationship in one sentence each. Include whether the related record supports, extends, or challenges this paper's claims.]

#### Limitations the authors acknowledge
[List from `limitations`; add 1–2 limitations the authors did NOT mention if apparent from the methods.]

#### Discussion questions
[5–7 questions, graduated from factual to speculative:]
1. [Factual: can be answered from the paper]
2. [Methodological: questions about design choices]
3. [Mathematical: relevant to MCS pillars — identifiability, UQ, RL formulation, physics constraints]
4. [Generalizability: does this apply beyond the specific drug/disease?]
5. [Regulatory: how would FDA evaluate this work under the 7-step credibility framework?]
6. [Practical: what would it take to implement this in a real clinical setting?]
7. [Research agenda: what should be done next? Does this suggest a task for the WG?]

#### Pre-reading recommendation
[1–2 sentences on what background knowledge would help. Point to a related record in the library if relevant.]

---

**4. Confirm**
After outputting the guide, ask: "Should I save this as `aiml_wg/community/journal_club/notes/{id}_guide.md`?"
If yes, write the file.
