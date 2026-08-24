# Agent-Team Evolution Devil's-Advocate Review 001

**Date:** 2026-08-21
**Archive status:** Historical reference only
**Authority:** Non-authoritative conversation summary

> Repository documents are authoritative. Archived conversations are historical reference only.

## Purpose

A single long conversation with Claude, requested explicitly as a devil's-advocate architectural review of the `agent-team-evolution` Workbench concept — a proposal, originating in a separate Codex/audit-chat conversation, to evolve Spark OS toward repo-native specialist agents (Researcher, Designer, Auditor, Editor, Reporter, Publisher, Manager). The user built a 24-point structured list to work through systematically, with the explicit instruction not to concede points without genuine grounds and to hold opposition where warranted. The conversation grew to include live testing of a newly built shared cross-platform coordination system (the Google Drive Shared Workbench) and two real pickup sessions on task T-006.

## Context

At the start of this conversation, `00-workbench/agent-team-evolution.md` did not exist anywhere in the canonical repository, on any branch, or in any pull request, despite a third-party (Codex) conversation claiming to have created it. This absence became the review's opening finding and shaped its method throughout: verify claims against primary sources rather than trust summaries, including summaries the reviewer itself produces.

## Major Milestones

### Headline finding — the missing Workbench file

Extensive investigation (git history, all branches, all PRs, GitHub code search) found no trace of the claimed file. The user later located it in a Google Drive-hosted "cloud workbench" that a GPT-desktop (Codex) session maintains alongside a local clone of the repository, pushing to GitHub `main` only on deliberate action. The file was real and well-formed — never fabricated — but had never crossed into the canonical repository. Supporting evidence found independently: PR #16's description explicitly excludes "S-122... post-checkpoint research-agent material," and the canonical audit log (`foundational-conversation-audit.md`) stops at S-121, consistent with material existing outside the canonical trail at the time. The standing lesson: a claim can be true in its own storage context and still never reconcile with the source of truth unless something forces that reconciliation.

### Twenty-four-point structured review

The user's list covered: the headline finding; the proposal's actual strength; the current two-role AI Governance model; duplicate authority via a proposed Manager; AI-vendor portability; the intake-folder concept; ADR triggers; the evidence gap; the absence of a stop condition; cost accounting; evidence of necessity for the seven-role hypothesis; the "park it, don't build it" recommendation; one falsifiable historical-evidence question; sequencing; repository age; governance's deliberate strictness; priority ordering; whether a benefit case exists; the AI Governance four-part new-role test; the craft/authority enforcement mechanism; autonomy-tier drift; human-role erosion as a governance decision; the OneDrive storage layer; and deliberate multi-chat separation as an existing practice. All twenty-four were closed, materially revised, or deliberately deferred with a stated trigger by the conversation's end. Two closed points (11 and 13) were later reopened and corrected after the reviewer recognized its own audit sample had been biased by the narrow task scope it was run under.

### The Shared Workbench — built and live-tested mid-conversation

The user built a real cross-platform coordination system in Google Drive (`START-HERE.md`, `task-register.md`, per-task `status.md`/`handoff.md`/`session-register.md`/`platform-returns/`/`artifacts/`/`closeout/`) partway through the conversation, independently incorporating several lessons already surfaced by the review — an explicit authority-conflict rule, "do not infer authority from placement," read-only-by-default access, single-writer-per-task concurrency control, and an explicit disclaimer that actor labels are procedural identifiers, not durable AI identities. Claude performed a live read-only pickup of task T-006 per the system's own documented procedure, including a deliberate fail test (an intentionally mismatched actor label, `Claude-T006-Cold-Auditor` vs. the recorded `Claude-T006-Auditor`) that was correctly caught and halted rather than resolved unilaterally, and a genuine tool-capability limitation was discovered live: the Drive connector available could create files and update metadata but had no in-place content-update capability, so proposed control-file changes were returned as text rather than applied directly.

### T-006 — two real audit sessions

Session 01 produced a six-signal responsibility-audit reconciliation using the task's Role-exploration lens; none of the six signals cleared the bar for a durable role. Session 02, triggered by an independent review from the Codex/audit-chat side, delivered six bounded corrections after Claude independently reverified two of the handoff's load-bearing claims against live GitHub state (PR #12 and PR #17, both confirmed merged; a direct diff of `AI_GOVERNANCE.md` and `CLAUDE_ROLE.md` against current `main` showing zero change despite Governance Fit Audit 001 being complete). The correction materially changed two findings: the content-research and content-audit signals had more real evidence than session 01 credited, given the merged Training Research Pilot 001 skill and the preserved Course Prototype 001 review package; and the Manager signal's strongest existing-owner candidate turned out to be the Shared Workbench's own live "Coordinator" function (observed operating in practice that same evening), not an updated AI Governance document.

### The role-bleed reframe

The user proposed reframing the entire role-exploration question from "is there evidence to justify a new role" to "where are already-blended responsibilities creating a real conflict that would benefit from separation" — noting this sidesteps the evidence-gap bottleneck that recurred throughout the review, since it can be tested against already-observed behavior rather than requiring new operational history to accumulate. Applied immediately, it surfaced two real instances: the Codex audit chat acting as both Coordinator and Architectural Auditor for the same task, and Claude's own dual role that evening as both auditor of the agent-team concept and the live test subject for the Workbench mechanics being audited — a structural echo of the self-certification conflict ("an implementer must not verify its own work") already named in the T-006 correction.

### Two live self-corrections on checkable facts

The reviewer twice cited claims from memory or from an earlier read that turned out to be stale when re-verified against primary sources: the origin of the `S-###` audit-numbering convention (recalled by the user as recently adopted; verified present since the very first commit of the audit file), and the status of pull request #12 (cited repeatedly throughout the review as still stalled; verified merged on 2026-08-18, predating the conversation, with `task-notepad.md` simply not yet reflecting it at the time it was first read). Both corrections were made directly rather than defended, consistent with the review's stated standard of verifying claims — including its own — against primary sources.

## Alternatives and Concerns

- Building durable agent identity, repo-native state, or orchestration now was consistently rejected as premature given the repository's actual operational history (approximately five working days of substantive progress at the time of review, not the three calendar weeks the repository's age suggested).
- A standalone or per-role GitHub repository for agent infrastructure was considered and deferred: judged a legitimate future mitigation for one specific risk (protecting the canonical repository from a misbehaving agent's writes) but not for external side effects, prompt injection, or self-editing instructions, and premature regardless while zero agents exist to scope the isolation boundary around.
- Real client and case data (Granola meeting notes, and a later-proposed structured "file closeout" extraction from completed mortgage transactions) were flagged as needing genuine privacy review — the file-closeout case specifically judged materially higher risk than the meeting-notes case, since specific property, amount, obstacle, and lender details together are plausibly re-identifiable even without a name attached.
- A proposed unattended, scheduled ("sleeping hours") research pipeline was rejected for the near term: the efficiency case for idle-capacity usage was judged real but in direct tension with the highest-risk scenario (unsupervised operation), and "continuous output for later review" was noted to relocate rather than reduce total review burden unless production is rate-limited to actual review capacity.

## Architectural Principles Discussed

- Agents should have independent operational state without becoming independent sources of truth; Spark OS retains shared truth and authority regardless of any agent's accumulated craft.
- A role name is not evidence that an agent should exist; responsibility signals should be clustered from observed evidence before being assigned names, not sorted into names decided in advance.
- Sequencing a plan correctly (what comes before what) is not the same as defining thresholds (what would make a stage count as passed or failed); both are required before treating an exploration as adequately gated.
- Portability applies to the knowledge and process (durable markdown, git), not to any given model's particular performance of a role — durable "identity" or "voice" is the least portable thing that could be built toward, and building toward it would work against Spark OS's own stated portability principle.
- Any expansion of AI role scope should be evaluated against the existing AI Governance four-part test (repeatedly needed, materially distinct, reduces ambiguity, survives tool replacement) rather than argued for in the abstract; running the test concretely against a real candidate can surface real dependencies between criteria that citing it abstractly does not.
- A blended responsibility only needs separating when the blend creates an actual conflict (self-certification, or role-drift risk) — not merely because one entity is performing more than one function.

These principles are historical observations unless confirmed by the authoritative documents linked below.

## Outcome

No agent, role, skill, schema, or orchestration mechanism was created or installed. The reviewed concept remains a non-authoritative Workbench exploration (`00-workbench/drafts/agent-team-evolution-notes-consolidated.md`, already preserved on `main`). The standing recommendation from the review is to continue documentation- and workflow-level separation (packet structure, boot-mode design, the weekly-reconciliation Auditor pattern) rather than agent identity, pending further evidence generated by the Shared Workbench's own ongoing operation. Concrete real action items identified but not yet completed as of this summary: updating the stale role descriptions in `AI_GOVERNANCE.md` and `CLAUDE_ROLE.md` to reflect actual current practice; separating the Coordinator and Auditor functions currently blended in the audit-chat platform; designing a staleness/keep-or-close check for paused Workbench tasks; and further developing the lender-portal-sourcing and file-closeout production concept, gated on an anonymization design and a review of the lender portal's own terms of use.

## Lessons Learned

- A claim can be accurate in the storage context it was made in and still never reach the canonical source of truth unless something forces that reconciliation; this is a coordination property, not a truthfulness property, and it recurred at least twice in this review at different scales (the original missing file, and a stale citation the reviewer itself carried forward).
- An audit performed entirely within a narrowly bound task scope will only find evidence for what that scope actually exercises; absence of evidence for out-of-scope responsibilities should be reported as untested, not as evidence of unnecessity.
- Reframing an evidence-seeking question around already-observed behavior, rather than hypothetical future behavior, can produce real findings immediately where the original framing was bottlenecked on evidence that does not yet exist.
- Independent verification against primary sources (git diffs, live GitHub state, direct API queries) caught real, materially significant errors that a purely conversational or memory-based review would not have caught, including two errors made by the reviewer itself.

## Repository References

### Authoritative Documents

- [`02-governance/ai-governance/AI_GOVERNANCE.md`](../../../02-governance/ai-governance/AI_GOVERNANCE.md)
- [`02-governance/ai-governance/CLAUDE_ROLE.md`](../../../02-governance/ai-governance/CLAUDE_ROLE.md)
- [`02-governance/design-history-workflow.md`](../../../02-governance/design-history-workflow.md)
- [`CONTRIBUTING.md`](../../../CONTRIBUTING.md)

### Pull Requests

- PR #12 — Course Prototype 001 preservation (merged)
- PR #16 — Preserve reviewed Workbench state (merged)
- PR #17 — Install approved Training Research Pilot 001 skill (merged)
- PR #21 — Implement Governance Fit Audit 001 bounded clarification (merged)
- PR #24 — Reconcile Workbench continuity (merged)

### Commits

- `018f02a7f01d06e19d701bfb0e2474dd6fe943b2` — current `main` at the time this summary was written

### Related Archive Records

- [`00-workbench/drafts/agent-team-evolution-notes-consolidated.md`](../../../00-workbench/drafts/agent-team-evolution-notes-consolidated.md)
- [`2026-08-17-governance-fit-audit-001-summary.md`](2026-08-17-governance-fit-audit-001-summary.md)

## Unresolved Questions

- Whether the Manager responsibility signal is already substantially covered by the Shared Workbench's live Coordinator function, or whether it warrants a distinct future role — the existing-owner and overlap tests were explicitly left incomplete pending the Coordinator/Auditor separation.
- Whether reducing the human owner's operational involvement over time should ever become an explicit, evidence-gated governance decision, and under what category-specific, reversible terms.
- Whether a durable process for reconciling the Shared Workbench's coordination state against the canonical repository (beyond the two live pickups tested in this conversation) is reliable at higher task volume than was exercised here.

## Next Milestone at Time of Conversation

Produce this Design History summary (completed by this record), then proceed to the four outstanding action items in an order to be chosen by the repository owner: updating the stale AI Governance role documents, separating the Coordinator and Auditor functions, designing a staleness check for the weekly-reconciliation pattern, and scoping the lender-portal and file-closeout production direction.
