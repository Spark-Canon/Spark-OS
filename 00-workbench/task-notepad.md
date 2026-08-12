# Spark OS Working Notepad

**Status:** Active working list
**Authority:** Non-authoritative Workbench material
**Last reviewed:** 2026-08-11
**Purpose:** Keep the current cross-chat queue concise while detailed reasoning remains in the [foundational audit](drafts/foundational-conversation-audit.md) and qualifying Design History.

## Current Priority Queue

1. [ ] **Close the bounded post-checkpoint Workbench preservation.**
   - Branch `agent/preserve-post-s121-workbench` starts from current `main` and appends a sanitized and correctly ordered S-122 through S-135 continuation, updates this notepad and the parking-lot index, and adds the source-chat historical capture utility.
   - Do not copy the historical local audit file wholesale: its pre-S-122 content predates PR #16 privacy corrections, and S-125 through S-130 require chronological relocation after S-124.
   - Do not widen the update into authoritative content, skill invocation, research, or superseded candidate preservation.
   - Independently audit the exact four-file branch diff before merge.

2. [ ] **Complete Governance Fit Audit 001.**
   - Test whether current [`CONTRIBUTING.md`](../CONTRIBUTING.md) already provides sufficient design-time Philosophy application and post-design/pre-acceptance review.
   - Compare it with accepted Philosophy, Governance, Spark Brain boot paths, Canon authority, and applicable external constraints.
   - Identify concrete recurring decisions the current workflow does not guide.
   - Recommend no change when the existing workflow is sufficient; otherwise propose the smallest coherent edit and likely owner.
   - Do not create an ADR, new Governance file, checklist system, schema, or automation during the audit.

3. [ ] **Explore a minimum Canon sourcing and entry standard.**
   - Define only the minimum needed to distinguish accepted claims, provenance, currency, scope, uncertainty, and authority.
   - Use Course Prototype 001 failures as evidence without treating the prototype as authoritative.
   - Treat the installed but uninvoked Training Research Pilot 001 as bounded instructional-design evidence infrastructure, not a Canon standard or authority. Any later domain research still requires separate review and authorization.
   - Preserve legal, regulatory, professional, insurer, lender, and organizational ownership boundaries.
   - Do not design a comprehensive schema or create mortgage Canon or Academy content during this exploration.

4. [ ] **Run one bounded Canon pilot after the minimum standard is credible.**
   - Select a narrow topic with accessible current sources and meaningful operational use.
   - Test sourcing, retrieval, change handling, downstream teaching implications, and evidence for future Mental Models.
   - Do not generalize repository architecture from one pilot.

## Parallel and Evidence-Gated Work

- [ ] **Obtain licensed-practitioner review of Course Prototype 001.**
  - Draft PR [#12](https://github.com/Spark-Canon/Spark-OS/pull/12) remains the frozen, non-authoritative review package.
  - It is currently conflicted with `main`; do not refresh, repair, or merge it merely to remove the conflict.
  - After practitioner findings return, reconcile them here before authorizing any successor prototype, Canon, or Academy work.

- [ ] **Continue observing `Representation Is Not Capability`.**
  - The Mental Models evidence checkpoint found insufficient independent evidence for Distill.
  - Reopen only when repeated non-lineage-biased use demonstrates a recurring reasoning benefit.
  - `What Changes When We Simplify?` remains reallocated to possible future Academy or editorial guidance, not foundational Mental Models.

## Parked

See the [parking-lot index](parking-lot/README.md).

- Bookmarks and links repository
- Established knowledge over reinvention
- Source-chat historical capture invocation

Reopen either only when the recorded evidence trigger occurs. Parking is not rejection and does not create an active design task.

## Current Repository Reconciliation

- PR #8 repository-integrity hardening and ADR-0003 merged at `aef0b29ccc228bdba5b12ae1a6160b5e2f3edf31`.
- PR #11 Principles Exploration archive merged at `2b467953d84efa631655113549c0353e22b4bc5a`.
- PR #13 installed the accepted Foundational Glossary at merge `f2ce678ae65de1dd24c1fea237fd208fce2e454a`.
- PR #14 archived the Glossary exploration as non-authoritative Design History at `a9178a17c57684c425ffb3cc8854e5f638a48097`.
- PR #15 completed the verified Glossary closeout at `ec177993bbd55efe29bbaf14daddc132ddc3e055`; its branch and temporary checkout are retired.
- PR #16 preserved the reviewed pre-research Workbench checkpoint at `8982dc00215b4083afcf33dcf1762a8de261d943`.
- PR #17 installed the approved Training Research Pilot 001 skill and merged at `25dc8446ee55dcff1eba3027b47f277315b767cf`; post-merge fingerprints and validation pass. The skill remains uninvoked, and its completed feature branch and dedicated worktree are retired.
- PR #12 remains draft, open, unmerged, and non-authoritative pending practitioner review.
- No known architectural or repository-integrity blocker prevents Governance Fit Audit 001.

## Workbench Artifact Dispositions

| Artifact | Disposition | Reason |
|---|---|---|
| `drafts/foundational-conversation-audit.md` | Retain — active | Primary local audit and continuity record |
| `drafts/mental-models-evidence-checkpoint-001.md` | Retain — observation | One candidate remains evidence-gated |
| `drafts/source-chat-historical-capture-prompt.md` | Retain — parked utility | Reusable non-authoritative transfer prompt awaiting evidence for an explicit invocation mechanism |
| PR #12 curated practitioner brief | Retain on PR #12 | Active external-review input |
| Local `course-prototype-001-practitioner-review-brief.md` | Superseded | PR #12 contains the curated active brief |
| Local `spark-os-principles-candidate.md.txt` | Superseded | Accepted Principles and Design History preserve the outcome and provenance |
| Local `foundational-glossary-candidate-001.md.txt` | Superseded | Accepted Glossary, approval fingerprint, audit, and Design History preserve the outcome |
| Local `foundational-glossary-exploration-001.md` | Superseded for active use | Accepted Glossary, foundational audit, and merged Design History preserve durable findings |

Do not delete a superseded local file until the clean preservation branch has been audited and its exclusion is confirmed.

## Feedback Intake

For each new item, record:

- the proposal and source;
- the problem it is trying to solve;
- the affected authority or destination;
- whether it is a correction, conflict, clarification, proposal, or new task;
- the evidence and decision; and
- the final disposition or reconsideration trigger.

## Feedback Review Method

1. **Capture** without treating the item as accepted.
2. **Locate** the current authoritative owner.
3. **Compare** for duplication, contradiction, and scope drift.
4. **Classify** as accept, refine, merge, reject, defer, park, or needs discussion.
5. **Draft** only the smallest coherent non-authoritative change when judgment remains.
6. **Validate** terminology, links, authority, and downstream effects.
7. **Promote** only after explicit acceptance and coordinated installation.
8. **Close** with a durable result and next trigger.

## Completed Foundation

- Spark OS Manifesto and five Values approved, installed, independently verified, and merged through PR #6.
- Seven Principles approved, installed, independently verified, and merged through PR #9; milestone closeout completed through PR #10.
- Foundational Glossary approved, installed, audited, closed, and merged through PRs #13–#15.
- Mental Models Evidence Checkpoint 001 closed without forcing a candidate into Distill.
- Governing Explore → Challenge → Audit → Close → Distill method installed in [`CONTRIBUTING.md`](../CONTRIBUTING.md).

## Next Action

Independently audit and merge the bounded post-S-121 Workbench preservation branch. After closeout, begin Governance Fit Audit 001 as non-authoritative Workbench analysis.
