# Course Prototype 001 — Findings

> **Workbench learning prototype. Non-authoritative. Not approved for operational, client, compliance, licensing, or training reliance.**

Companion to [`prototype-course.md`](prototype-course.md). Records what building this specific lesson revealed about the development process, not conclusions to implement now.

---

## Missing Canon sources

Every numeric fact needed to make the Learn section and all five Apply cases fully confident — down payment thresholds, price caps, amortization limits, occupancy eligibility rules, transaction-type exclusions, premium mechanics — is missing from Canon. `03-canon/` currently has only a scope-defining README. **Likely owner: Canon.**

## Unverified factual claims

Even the *general conceptual structure* of the three-category system (not just the numbers) is presented in the prototype as an unverified assumption, not a confirmed fact. Mortgage insurance rules have changed multiple times historically, and nothing in this exercise confirms the framing used is current. This is a broader gap than "we need some numbers filled in" — the shape of the explanation itself needs SME sign-off. **Likely owner: Canon, pending SME/Sheldon review.**

## Terminology problems

Industry sources use inconsistent labels for the middle category (e.g., "insurable," "low-ratio insured," "portfolio insured"). Spark hasn't picked a canonical term. Using the wrong one in a course consistently would be a low-cost content decision to get wrong once — but only once Canon settles it. **Likely owner: Glossary, once Canon confirms the underlying concept.**

## Simplification risks

Presenting three categories as a clean, mutually exclusive partition is a simplification. Real files have edge cases (mixed-use properties, hybrid occupancy, transitional refinances) that don't sort cleanly — Case 5 was built specifically to surface this, but a full course would need to decide how much edge-case nuance belongs in an introductory lesson versus a later, more advanced one. **Likely owner: Academy (sequencing decision), informed by Canon once it exists.**

## Assessment difficulties

Question 5 and Case 5 both have genuinely defensible alternative answers ("escalate" vs. "verify independently") because Spark hasn't yet defined what threshold of uncertainty requires supervisor escalation versus self-directed verification for a new agent. Without that, grading either "correct" or "incorrect" would be arbitrary. **Likely owner: Governance or Canon — this is really a Match Accountability to Authority and Ability question that hasn't been operationalized yet.**

Adding the 12-item Knowledge Check surfaced a related but distinct difficulty: multiple choice can't honestly represent a judgment question the way the open-ended Assessment can, so the MCQ items were deliberately scoped down to Know/Understand, with a few Apply-level items that stay just short of genuine judgment by keeping the ambiguity resolvable from facts already given. Two items (6 and 10) still needed "verify before classifying" as the correct choice rather than a forced pick between the three categories — without that option, the format would have quietly trained toward false confidence on exactly the cases the rest of the prototype is trying to guard against. **Likely owner: Academy — this is a reusable assessment-design constraint (MCQ format ceiling), not specific to this topic.**

## Alternative defensible answers

Beyond Question 5: Case 1's "likely Insured, pending confirmation" vs. a flat "Insured" is a real judgment call about how much hedging an introductory lesson should require learners to state explicitly. This exercise defaulted to rewarding the hedged answer as stronger, which is a design choice worth someone deliberately confirming rather than inheriting silently from this prototype.

## Traceability needs

Every bracketed placeholder in `prototype-course.md` needs a mechanism to become a real, dated citation once Canon has the content (e.g., "as of [date], per [Canon source]") — no such citation pattern currently exists in the repository. Without it, a future editor won't know whether a stated figure is current or five years stale. **Likely owner: Canon (a source/date convention) and possibly technology (if this should be structured data rather than prose).**

## Maintenance and currency concerns

Mortgage insurance thresholds and eligibility rules change periodically and outside of Spark's control. This is a fundamentally different maintenance problem from Philosophy (which changes only when Spark deliberately decides) — it needs an active review cadence and an owner responsible for noticing when the outside world changes, not just when Spark decides to change something. No such mechanism currently exists in Governance. **Likely owner: Governance, as a new currency/review-cadence pattern distinct from the deliberate-change model Philosophy uses.**

## Human-review requirements

Everything with a number requires SME sign-off before this leaves prototype status. So does the general category framing, since it wasn't drafted from a verified current source. This is close to a full-content review, not a light pass. **Likely owner: Sheldon or a licensed/current-practicing broker reviewer, before Canon or Academy status.**

## AI limitations

I cannot certify current Canadian mortgage-insurance regulatory accuracy, and my knowledge may be imprecise or outdated on exact figures — which is exactly why the placeholder discipline mattered here rather than being optional caution. I also can't observe real agent behavior, so the Perform-level outcome and the facilitator's "what a supervisor should observe later" notes are educated design guesses, not validated against actual new-agent errors. **Likely owner: continued Workbench exploration until real observation data exists (Academy/field practice).**

## Potential Academy structure needs

A dated, single-source-of-truth Canon block for regulated numeric facts that Academy content links to rather than restates, so a threshold update propagates everywhere it's used instead of requiring a manual find-and-fix across every lesson that mentions it. **Likely owner: Academy structure + Canon, jointly — this is close to the "Canon-to-Academy alignment review" routine `AI_GOVERNANCE.md` already lists as a potential future routine.**

## Potential Governance or Canon implications

Canon's `Change Discipline` section already requires reviewing downstream Academy content when Canon changes — but it doesn't yet distinguish *Spark-deliberate* changes from *external-regulatory* changes that Spark didn't initiate and needs to actively notice. That distinction seems worth a explicit Governance note, since the review trigger is different (Spark controls the timing of one, not the other). **Likely owner: Governance.**

## Unnecessary complexity encountered

The originally proposed "fictional client file requiring facts/assumptions/missing-information classification" device (from the initial course-prototype prompt) was dropped in favor of teaching the three categories directly. In hindsight that was the right call for this specific topic: the category distinction is concrete and rule-based enough that a direct compare/contrast + practice-case design taught it more efficiently than wrapping it in a general epistemic-reasoning framing would have. That framing may still be the right tool for a different, more genuinely ambiguous topic — it wasn't a bad idea, just a mismatch for this one.

## Questions requiring Sheldon's direction

1. What are the actual current thresholds and figures Spark wants treated as canonical for this topic, and how should they be sourced and dated?
2. What terminology does Spark want to use for the middle category ("insurable" vs. alternatives)?
3. What threshold of uncertainty should trigger escalation to a supervisor versus self-directed verification for a new agent — this affects Question 5 and Case 5 directly and can't be resolved inside this prototype.

## Recommendations for the next prototype

Run a second vertical slice on a topic that does **not** depend on externally-changing regulatory facts — something rooted in Spark's own values-driven practice (e.g., how to handle a client who wants to proceed against Spark's recommendation, tying directly to Support Informed Choice) rather than a Canon-empty regulated-facts topic. Comparing how much easier authoring is when the subject matter is Spark's own judgment versus external regulation would directly test how much of today's difficulty was "Canon is empty" versus "regulated topics are inherently harder to author safely" — that distinction matters for deciding what Canon needs to build first.
