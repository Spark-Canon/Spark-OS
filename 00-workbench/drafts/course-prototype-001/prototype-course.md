# Insured, Insurable, and Uninsurable Mortgages — Course Prototype

> **Workbench learning prototype. Non-authoritative. Not approved for operational, client, compliance, licensing, or training reliance.**

This is Spark OS Workbench experimental material created under `00-workbench/drafts/course-prototype-001/`. It exists to test course-development mechanics, not to teach current mortgage rules. It has not been reviewed by a subject-matter expert, is not Canon, and is not accepted Academy content. See [`prototype-findings.md`](prototype-findings.md) for what this exercise revealed about the process itself.

---

## Prototype Brief

**Purpose.** Test what a narrow, real-feeling Academy lesson actually requires — source material, traceability, simplification limits, assessment design, and the boundary between what AI can safely draft and what needs a human subject-matter expert — using a genuine mortgage topic rather than a synthetic exercise.

**Intended learner.** A new or developing Spark Mortgages agent, before they classify a file independently. Provisional; does not establish an accepted role, curriculum, or prerequisite structure.

**Assumed prerequisites.** None from Spark Academy — no prior Academy content exists yet to assume as completed. Assumes only general familiarity with basic mortgage vocabulary (down payment, amortization, purchase vs. refinance) from onboarding conversation, not from any verified Spark source.

**Scope.** The conceptual distinction between Insured, Insurable, and Uninsurable mortgage categories; why the distinction affects how a file should be worked; and when a new agent should stop and verify rather than commit to a classification.

**Explicit exclusions.** Exact current numeric thresholds (loan-to-value bands, purchase-price caps, amortization limits), premium rates, lender-specific program variation, qualifying-rate/stress-test mechanics, compliance or regulatory citations, and any client-facing script. These are excluded because no Spark Canon source exists yet to state them accurately (see Source Map).

**Estimated learning time.** 30–45 minutes. This is an unverified prototype estimate with no basis in observed learner behavior.

**Source limitations.** As of 2026-07-27, `03-canon/` contains only a scope-defining README and no mortgage domain content. Every specific regulatory figure below is marked as a placeholder rather than stated. The general conceptual structure of the three categories is presented as a **prototype assumption** — drafted from general familiarity with how the Canadian residential mortgage market is structured, not from a verified current source, Sheldon's confirmation, or Spark Canon — and requires subject-matter validation before any further use.

**Non-authoritative status.** Nothing in this document is accepted Academy content, Canon, or a compliance position. It must not be used with a client, cited as training completed, or relied on operationally.

---

## Learning Outcomes

Working design tool only — not an accepted Spark taxonomy.

- **Know:** The names of the three categories and the general factors that distinguish them (down payment level, property price, amortization length, occupancy/use, and transaction type).
- **Understand:** Why two files with the same down payment percentage can fall into different categories, and why the distinction affects pricing, required documentation, and which lenders/programs are available.
- **Judge:** Given a file's known facts, decide whether a classification can be made confidently or whether a specific gap requires verification before proceeding.
- **Perform:** *(Not exercised by this prototype.)* Correctly classifying a live file and documenting the reasoning is a practice-and-supervision outcome, not something a self-contained lesson can establish. Completing this prototype does not establish competence at Know, Understand, Judge, or Perform level.

---

## Learn

> Everything below the line is a **prototype assumption**, not confirmed Spark Canon. Bracketed items are explicit source gaps.

### Why the categories exist

Canadian residential mortgages are generally grouped into three categories because mortgage default insurance changes who bears the risk if a borrower defaults, and that risk allocation affects the rate and terms a lender is willing to offer. `[PLACEHOLDER — requires Canon-confirmed regulatory framing]`

### Insured

A mortgage where default insurance is required and obtained. This is generally associated with a lower down payment (a "high-ratio" purchase) on an owner-occupied property. The borrower typically bears the cost of the insurance premium. `[PLACEHOLDER — exact down payment threshold, price cap, and amortization limit that currently apply]`

### Insurable

A mortgage where the borrower has put down enough that insurance isn't required for the borrower's sake, but the file still meets an insurer's eligibility rules — so a lender can choose to insure it for their own funding purposes. The borrower does not carry the insurance cost in this category. `[PLACEHOLDER — exact eligibility criteria that currently apply]`

### Uninsurable

A mortgage that doesn't meet insurer eligibility rules regardless of down payment size. This is usually driven by **transaction type or property use**, not down payment — for example, refinances and non-owner-occupied (rental/investment) properties are generally excluded from insurer eligibility on that basis alone. `[PLACEHOLDER — complete and current list of exclusion criteria]`

### Why it matters to an agent

The category affects: the rate a lender is likely to offer (lower perceived lender risk generally supports better pricing); whether the client pays an insurance premium; which lenders and programs are realistically available; and what the file needs to demonstrate for the classification to hold up. Getting it wrong isn't just a technical labelling error — it can mean presenting a client with a rate or program that was never actually available to them.

### A common new-agent misreading

Down payment size is the most visible number on a file, so it's tempting to treat it as the whole answer: "20% down, so it's Insurable." Case 4 below is built specifically to break that assumption — down payment alone does not decide the category when occupancy or transaction type independently disqualifies the file.

---

## Apply

Fictional cases only. No real client information. Numbers are illustrative, not current figures — see Source Map.

**Case 1.**
Purchase, owner-occupied single-family home, price $450,000, down payment 10% ($45,000), 25-year amortization requested, stable salaried income, no other properties owned.

**Case 2.**
Purchase, owner-occupied condo, price $600,000, down payment 25% ($150,000), 25-year amortization requested, primary residence.

**Case 3.**
Refinance of an existing owner-occupied home to consolidate debt. Client has roughly 35% equity. 25-year amortization requested.

**Case 4.**
Purchase, non-owner-occupied rental/investment property, down payment 25% ($112,500 on a $450,000 purchase), 25-year amortization requested.

**Case 5.**
Purchase, owner-occupied duplex — client will live in one unit and rent the other. Purchase price is close to what the agent believes may be near a relevant price threshold, but isn't certain of the current figure. Down payment 15%. 25-year amortization requested. Client is self-employed with 1.5 years of documented income.

**For each case, before looking at the feedback:**
1. Which category does this file point toward — Insured, Insurable, Uninsurable, or *cannot classify with confidence yet*?
2. What fact in the case drove that answer?
3. What, if anything, would you still need to verify before committing to that classification with a client?
4. Would you escalate this file to a supervisor or more experienced agent before proceeding? Why or why not?

---

## Feedback and Rationale

**Case 1 — points toward Insured.** Down payment is below the low-ratio range, and the property is a standard owner-occupied purchase — the pattern that generally drives the Insured category. `[PLACEHOLDER — this still depends on the price and amortization sitting inside current insurer limits, which are not confirmed here]`. A defensible alternative answer: "likely Insured, pending price/amortization confirmation" — treating it as fully settled without that check is the weaker answer.

**Case 2 — points toward Insurable, not Insured.** Down payment is high enough that insurance isn't required for the borrower's sake, but that doesn't mean the file is exempt from every eligibility rule — it means the *cost* falls differently. The most common error here is concluding "high down payment = no insurance considerations at all," which conflates *Insured* and *Insurable* as if only one of them involves insurance eligibility.

**Case 3 — Uninsurable, and down payment/equity is irrelevant to that answer.** This is the case most likely to be misjudged by someone anchored on down payment size: 35% equity looks strong, but refinances are generally excluded by **transaction type**, independent of how much equity exists. The lesson here is specifically that not every factor is a spectrum — some are a hard structural gate.

**Case 4 — Uninsurable, for a different structural reason than Case 3.** 25% down looks identical to Case 2's down payment profile, but occupancy (non-owner-occupied) independently disqualifies it. Two cases with the same down payment percentage landing in different categories is the clearest demonstration in this set of why down payment alone is not the whole answer.

**Case 5 — cannot classify with confidence; this is the escalation case.** At least three things are unresolved: whether a mixed owner-occupied/rental duplex meets current insurer occupancy rules, whether the price sits under or over a threshold the agent isn't certain of, and how self-employment income documentation interacts with qualification (a related but separate question from category classification, worth flagging so it isn't collapsed into the same question). The defensible answer is not a guess in either direction — it's identifying exactly what's unverified and escalating or checking before telling the client anything definite. Treating this like Case 1 or Case 2 and picking a category anyway is the failure mode this case is designed to surface.

---

## Assessment

**1. Recall.** Which of the three categories involves the borrower paying a mortgage default insurance premium?
*Assesses:* basic recall. *Expected reasoning:* Insured, by definition. *Acceptable alternatives:* none — this is a definitional fact. *Common error:* confusing Insured and Insurable, since both involve insurance eligibility. *Why it matters:* this specific confusion is the most common one in the Learn section's callout.

**2. Explanation.** Why can two files with the same down payment percentage land in different categories?
*Assesses:* understanding beyond recall. *Expected reasoning:* down payment determines eligibility for the Insured/Insurable split, but occupancy and transaction type can independently push a file to Uninsurable regardless of down payment. *Acceptable alternatives:* any answer that correctly names at least one non-down-payment factor (occupancy, transaction type). *Common error:* restating that down payment matters without identifying what else matters. *Why it matters:* this is the core distinction Cases 3 and 4 are built to teach.

**3. Scenario application.** Purchase, owner-occupied, 5% down payment, standard single-family property, 25-year amortization. Classify it, and state what you'd still want to confirm before treating that classification as settled.
*Assesses:* applying the pattern to a new case. *Expected reasoning:* points toward Insured (low down payment, owner-occupied purchase); price and amortization still need confirming against current limits. *Acceptable alternatives:* "likely Insured, pending confirmation" is the strongest answer; a flat "Insured" without naming what's unconfirmed is weaker but not wrong. *Common error:* treating the classification as fully certain with no remaining unknowns. *Why it matters:* tests whether the learner internalized that even a clean-looking case has unverified specifics in this prototype.

**4. Scenario application.** Refinance, owner-occupied, strong equity position. Classify it.
*Assesses:* whether the structural-gate lesson from Case 3 transferred to a new instance. *Expected reasoning:* Uninsurable, on transaction type, independent of equity. *Acceptable alternatives:* none reasonable — this is the clearest structural-gate case in the set. *Common error:* reasoning from equity/down payment instead of transaction type. *Why it matters:* directly re-tests the single highest-value distinction in this lesson.

**5. Professional judgment.** A file shows 22% down payment. The agent is confident that clears the bar for Insurable and moves forward without checking anything else. What's missing from that judgment, and would you escalate?
*Assesses:* judgment under a realistic overconfidence trap, not just knowledge. *Expected reasoning:* down payment alone doesn't confirm eligibility — price cap, amortization, occupancy, and transaction type all still need checking; the honest answer is to verify those before treating the file as settled, which may mean a brief check rather than a full escalation depending on how confirmable the remaining facts are. *Acceptable alternatives:* "escalate" and "verify the remaining facts independently" are both defensible depending on the agent's stated confidence and access to current thresholds — this prototype does not have enough Spark-specific guidance yet to say which threshold of doubt requires supervisor escalation versus self-verification (see Findings). *Common error:* treating "down payment clears the bar" as sufficient on its own. *Why it matters:* this is the same reasoning error as Cases 3 and 4, tested without the structural-gate scaffolding spelled out — it checks whether the learner generalized the lesson or just pattern-matched the earlier cases.

---

## Knowledge Check (Multiple Choice)

This is a supplementary instrument, not a replacement for the Assessment above. It targets **Know** and **Understand** only — multiple choice is a poor format for testing **Judge**, and treating a score on it as evidence of judgment would misrepresent what it can show. A perfect score here does not establish competence, and a missed question does not by itself indicate one. Several items deliberately include "cannot be determined / verify" as the correct choice, so the format doesn't quietly train learners toward false confidence.

**1.** Which category involves the borrower paying a mortgage default insurance premium?
A) Insured B) Insurable C) Uninsurable D) All three
*Answer: A.*

**2.** In the Insurable category, who typically decides whether default insurance is obtained on the mortgage?
A) The client, for their own protection B) The lender, for their own funding purposes C) The insurer, automatically D) Insurance is never obtained on an Insurable file
*Answer: B.*

**3.** Which factor most directly determines whether a purchase is generally excluded from insurer eligibility, regardless of down payment size?
A) The client's credit score B) The property's occupancy/use and the transaction type C) The lender's internal volume targets D) The client's age
*Answer: B.*

**4.** Two files have identical 25% down payments. One is Insurable, one is Uninsurable. What's the most likely explanation?
A) A data entry error — down payment always determines the category B) They differ on a structural factor such as occupancy or transaction type C) The Insurable file must have a higher credit score D) The Uninsurable file must have a shorter amortization
*Answer: B.*

**5.** Purchase, owner-occupied townhouse, 8% down payment, 25-year amortization. Strongest classification?
A) Uninsurable, because 8% is too low B) Insurable, because the client is a first-time buyer C) Likely Insured, pending confirmation of price and amortization limits D) Cannot be classified — occupancy is unclear
*Answer: C.*

**6.** Purchase of a second home the client will occupy only part of the year — not a rental, not the primary residence — with 30% down. What should an agent do first?
A) Classify as Insurable — 30% clearly clears the low-ratio threshold B) Classify as Uninsurable — it isn't the primary residence C) Recognize that occupancy type here is ambiguous and verify current eligibility treatment before classifying D) Classify as Insured — insurance is always the safest default
*Answer: C.*

**7.** Refinance to consolidate debt, 40% equity position. Classify it.
A) Insured, because of the large equity cushion B) Insurable, because 40% is well above any low-ratio threshold C) Uninsurable, because refinances are generally excluded by transaction type regardless of equity D) Cannot be determined without more information
*Answer: C.*

**8.** Purchase of a rental property, 35% down payment, strong tenant history on the client's other properties. Classify it.
A) Insurable — 35% down is well above the low-ratio threshold B) Uninsurable — occupancy (non-owner-occupied) independently excludes it regardless of down payment C) Insured — rental income supports qualification D) Cannot be determined without a credit check
*Answer: B.*

**9.** An agent says: "The down payment is 25%, so this file is Insurable." What's the strongest critique of that reasoning, per this lesson?
A) 25% isn't actually above the low-ratio threshold B) Down payment alone doesn't confirm eligibility — occupancy, transaction type, price, and amortization can independently affect the category C) The agent should have said "Insured" instead D) There's no flaw — that reasoning is sufficient
*Answer: B.*

**10.** A file's price is close to a threshold the agent isn't fully certain is still current. What's the most defensible next step?
A) Proceed with the classification that seems most likely and correct it later if needed B) Verify the current threshold, or escalate, before treating the classification as settled C) Avoid mentioning the category to the client until every detail is finalized D) Default to Uninsurable — the safest assumption under uncertainty
*Answer: B.*

**11.** Which of the following is the best reason to escalate or verify a file's classification, per this lesson?
A) The file involves a first-time buyer B) A structural factor is unclear, or a numeric threshold is uncertain, and the classification would affect what the agent tells the client C) The loan amount is large D) The client asked a question the agent didn't expect
*Answer: B.*

**12.** Why does the Insured/Insurable/Uninsurable distinction matter practically to an agent, beyond naming the category correctly?
A) It's a required field in the file management system B) It affects likely pricing, required documentation, and which lenders/programs are realistically available C) It determines the agent's commission structure D) It has no practical effect beyond terminology
*Answer: B.*

---

## Facilitator / Reviewer Notes

- **Discussion beats automated grading for:** Question 5 and Case 5. Both have genuinely defensible alternative answers depending on judgment Spark hasn't yet operationalized (see Findings — "what threshold of doubt requires escalation").
- **Requires subject-matter validation before any further use:** every bracketed placeholder in Learn; the general three-category framing itself; all five Apply cases' numbers, to confirm they land where intended relative to *current* thresholds rather than the illustrative ones assumed here.
- **What a supervisor should observe later, in practice, not here:** whether a new agent correctly flags an occupancy- or transaction-type override on a live file (the Case 3/Case 4 pattern) rather than anchoring on down payment; whether they escalate appropriately on genuinely ambiguous files rather than guessing.
- **What this prototype cannot establish:** that the learner can classify a real file, that the underlying facts stated are currently accurate, or that completing it constitutes any form of training credit.
- **On the Knowledge Check specifically:** a high score shows the learner can apply the taught patterns to new fact patterns in a low-stakes format — it does not show they'll do so under real client pressure, and it should never be reported or reviewed as a standalone competence signal separate from this caveat.

---

## Source Map

| Content | Category |
|---|---|
| Philosophy alignment (Principles 1, 2, 3, 5, 6, 7 as applied throughout) | Accepted Spark Philosophy — `01-philosophy/principles.md` |
| "Canon currently has no mortgage domain content" | Existing repository source — `03-canon/README.md`, confirmed 2026-07-27 |
| General three-category conceptual structure (Learn section) | Prototype assumption — drafted from general market-structure familiarity, not a Spark or externally cited source |
| All numeric thresholds, price caps, percentages, amortization limits, premium mechanics | Unresolved claim requiring verification — explicitly bracketed above |
| Case 1–5 facts, names, dollar figures | Fictional scenario content — illustrative only, not current figures |
| Knowledge Check items 1–12 (facts, figures, and correct answers) | Fictional scenario content, built directly from the Learn/Apply content above — not an independent source |
| Sheldon's experience or organizational judgment | **Not used in this draft** — no input from Sheldon was available; flagged in Findings as a gap, not assumed |
| External authoritative source (e.g., regulator or insurer publication) | **Not used in this draft** — per your direction, specifics were placeheld rather than externally cited |

Every consequential mortgage claim in this document is either tagged above or bracketed inline as a placeholder. None should be treated as verified.
