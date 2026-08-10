# Spark OS Philosophy Glossary

**Status:** Accepted — active
**Authority:** Canonical definitions for foundational Spark OS language
**Approved by:** Sheldon Phillips
**Approval date:** 2026-08-09

## Purpose

The Glossary protects shared meaning across Spark OS.

It defines important terms used in the Manifesto, Values, Principles, Mental Models, Governance, Canon, Academy, operations, AI instructions, and future software.

The goal is not to define every word. The goal is to prevent important concepts from becoming ambiguous, inconsistent, or tool-dependent.

## Relationship to Other Philosophy Documents

- [`manifesto.md`](manifesto.md) introduces the purpose and ambition of Spark OS.
- [`values.md`](values.md) defines non-negotiable commitments.
- [`principles.md`](principles.md) establishes durable decision rules.
- [`mental-models.md`](mental-models.md) provides reusable reasoning frameworks.
- This document defines the foundational language those documents depend upon.

A definition should clarify accepted meaning. It should not quietly introduce a new Value, Principle, or architectural decision.

## What Belongs Here

- terms with a specific meaning inside Spark OS
- words that are commonly confused or used inconsistently
- distinctions that affect authority, workflow, learning, or decision-making
- approved abbreviations and naming conventions
- links to the authoritative documents that establish a concept
- deprecated terms and their preferred replacements, when useful

## What Does Not Belong Here

- a complete mortgage dictionary
- lender-specific terminology better handled in the Canon
- long essays that belong in another document
- definitions copied from external sources without context
- duplicate entries that create competing meanings
- speculative terminology not yet used by Spark OS
- definitions that conceal unresolved disagreements

## Definition Standard

Each accepted glossary entry should eventually include:

1. **Term** — the preferred name
2. **Definition** — concise meaning in Spark OS
3. **Distinction** — what the term should not be confused with
4. **Authority** — the document or decision that establishes it
5. **Related terms** — links to nearby concepts
6. **Status** — active, proposed, deprecated, or retired when needed

## Acceptance Test

Before adding a term, ask:

- Does inconsistent use of this term create meaningful risk?
- Is the definition specific to Spark OS or necessary for its work?
- Is there one authoritative meaning?
- Does the entry clarify rather than duplicate another document?
- Can the definition be understood without circular language?
- Is the term actually in use or about to become durable?

## Foundational Terms

### Authority (decision authority)

1. **Term** — Authority (decision authority)
2. **Definition** — The assigned scope within which a person or role may make or direct a decision or action.
3. **Distinction** — Decision authority does not by itself establish competence, practical ability, correctness, responsibility for every related task, or sole accountability. Repository and source authority are separate meanings defined by Governance.
4. **Authority** — Constrained by the accepted Manifesto, `Accountability Must Remain Clear`, `Match Accountability to Authority and Ability`, and Governance authority rules.
5. **Related terms** — [Accountability](#accountability), [Responsibility](#responsibility), [Competence](#competence), [Readiness](#readiness)
6. **Status** — Active

### Accountability

1. **Term** — Accountability
2. **Definition** — Accountability means being identifiable as answerable for a decision, duty, outcome, or operating condition.
3. **Distinction** — Accountability may be individual, organizational, or explicitly shared. It is not the same as responsibility, fault, liability, punishment, authorship, or causal contribution, and it must not become ownerless through delegation, automation, vendors, systems, or committees.
4. **Authority** — Constrained by the accepted Manifesto, `Accountability Must Remain Clear`, and `Match Accountability to Authority and Ability`.
5. **Related terms** — [Authority (decision authority)](#authority-decision-authority), [Responsibility](#responsibility), [Capability](#capability)
6. **Status** — Active

### Responsibility

1. **Term** — Responsibility
2. **Definition** — The decisions, actions, oversight, or response that fall to a person or organization within an assigned role and relevant circumstances.
3. **Distinction** — Responsibility may exist without final decision authority or sole accountability. The term does not itself prescribe a universal duty to explain, review, pause, refuse, escalate, or correct; applicable sources determine what response is required.
4. **Authority** — Constrained by the accepted Manifesto, `The Client Before the Deal`, `Accountability Must Remain Clear`, and accepted Principles governing evidence, informed choice, conflicting benefit, accountability, and readiness.
5. **Related terms** — [Authority (decision authority)](#authority-decision-authority), [Accountability](#accountability), [Judgment](#judgment), [Readiness](#readiness)
6. **Status** — Active

### Evidence

1. **Term** — Evidence
2. **Definition** — Information, observation, experience, absence, or a result that bears on a claim, question, judgment, or decision.
3. **Distinction** — Relevance does not by itself establish truth, credibility, sufficiency, currency, authority, or permission to use the evidence. Absence is evidence only where the missing observation, information, or result was reasonably expected under the relevant conditions.
4. **Authority** — Constrained by `Represent Reality Honestly`, `Make the Basis of Judgment Clear`, `Reconsider When Evidence Warrants It`, and `Preserve What Future Judgment Requires`.
5. **Related terms** — [Judgment](#judgment), [Proportionate](#proportionate), [Material](#material)
6. **Status** — Active

### Judgment

1. **Term** — Judgment
2. **Definition** — Context-sensitive evaluation of what conclusion, priority, recommendation, or course is warranted when relevant information, uncertainty, values, obligations, and trade-offs must be weighed.
3. **Distinction** — Judgment is not intuition alone, personal preference, authority, competence, unrestricted discretion, or an automated output. Professional judgment is this evaluation exercised within an applicable professional role, scope, competence, and obligations; it is not a separate foundational term.
4. **Authority** — Constrained by the accepted Manifesto, Values, Principles, and Mental Models scaffold, which support judgment without replacing it.
5. **Related terms** — [Evidence](#evidence), [Competence](#competence), [Readiness](#readiness), [Proportionate](#proportionate)
6. **Status** — Active

### Capability

1. **Term** — Capability
2. **Definition** — The capacity of a person, team, system, or organization to produce an outcome under specified conditions.
3. **Distinction** — Capability may depend on people, systems, resources, and support and does not by itself establish competence, readiness, authority, or responsible purpose. For a system, capability describes what it can produce under specified conditions; it does not imply human competence, judgment, responsibility, accountability, or moral agency.
4. **Authority** — Constrained by the accepted Manifesto, `Grow Without Becoming Fragile`, and `Match Readiness to Consequence`.
5. **Related terms** — [Competence](#competence), [Readiness](#readiness), [Responsibility](#responsibility), [Accountability](#accountability)
6. **Status** — Active

### Competence

1. **Term** — Competence
2. **Definition** — Demonstrated ability to perform or decide within a defined role, domain, and context to the applicable standards.
3. **Distinction** — Competence is not established by training, credentials, confidence, knowledge, authority, or isolated success alone and may change over time. Applicable standards come from legitimate external or downstream sources; this definition neither creates them nor decides which apply. Supported participation does not by itself establish complete independent competence.
4. **Authority** — Constrained by the accepted Manifesto, `The Client Before the Deal`, `Grow Without Becoming Fragile`, `Support Informed Choice`, `Match Accountability to Authority and Ability`, and applicable external or downstream standards.
5. **Related terms** — [Capability](#capability), [Judgment](#judgment), [Readiness](#readiness), [Authority (decision authority)](#authority-decision-authority)
6. **Status** — Active

### Readiness

1. **Term** — Readiness
2. **Definition** — The situational sufficiency of preparation, safeguards, and practical response capacity for the consequences involved.
3. **Distinction** — Readiness does not require perfect preparation or complete independent competence in every case, does not by itself compel action, and is not a permanent status. A competent person may be unready, while supported or supervised participation may be ready. Specific criteria and thresholds remain downstream.
4. **Authority** — Constrained by the accepted Manifesto, `Grow Without Becoming Fragile`, and `Match Readiness to Consequence`.
5. **Related terms** — [Capability](#capability), [Competence](#competence), [Authority (decision authority)](#authority-decision-authority), [Proportionate](#proportionate)
6. **Status** — Active

### Proportionate

1. **Term** — Proportionate
2. **Definition** — Matched in kind and degree to the relevant context and what could materially be affected.
3. **Distinction** — A proportionate response may require escalation or restraint in light of relevant evidence, uncertainty, consequences, rights, applicable obligations, legitimate authority, and practical constraints. Proportionality neither determines which sources apply nor overrides an applicable binding requirement. It is not a formula, equal-balancing rule, or permission to default to convenience; specific thresholds remain with applicable authoritative sources.
4. **Authority** — Constrained by the accepted Values and all seven accepted Principles; more specific requirements remain with applicable authoritative external or downstream sources.
5. **Related terms** — [Material](#material), [Evidence](#evidence), [Judgment](#judgment), [Accountability](#accountability), [Readiness](#readiness)
6. **Status** — Active

### Material

1. **Term** — Material
2. **Definition** — “Material matters are those that could reasonably affect a client’s understanding or choice, professional advice, risk, legal or contractual obligations, organizational judgment, or the reliability of Spark’s work.”
3. **Distinction** — This is a navigation entry reproducing the accepted Values definition exactly, not an independent Glossary definition. Material identifies potential significance; it does not require maximum process or establish a context-specific threshold.
4. **Authority** — [`Represent Reality Honestly`](values.md#represent-reality-honestly) in the accepted Spark OS Values.
5. **Related terms** — [Proportionate](#proportionate), [Evidence](#evidence), [Judgment](#judgment)
6. **Status** — Active — navigation
