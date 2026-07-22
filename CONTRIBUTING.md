# Contributing to Spark OS

This document defines how Spark OS should change without becoming disorganized, duplicated, or internally inconsistent.

## Core Rule

A conversation is where ideas may begin. The repository is where ideas become accepted.

Nothing becomes authoritative merely because it was written by Sheldon, ChatGPT, Claude, another AI, or a subject-matter expert. Authority comes from deliberate acceptance into the correct repository location.

Spark Brain is the repository control plane. It records state, navigation, and integrity requirements but does not create another knowledge state.

## Before Adding or Changing a File

Ask:

1. What single purpose does this file serve?
2. Is this operational metadata, exploratory, philosophical, governing, canonical, educational, or archived?
3. Where does the repository map assign authority for this information?
4. Does this knowledge already exist elsewhere?
5. Is a new file necessary, or should an existing source be improved?
6. What other files depend on this decision?
7. Does the change require an ADR?

Use [`brain/repository-map.md`](brain/repository-map.md) and [`brain/manifest.yaml`](brain/manifest.yaml) to locate authority.

## Repository Operating Layer

Location: `brain/`

Use only for:

- startup and resume instructions
- repository navigation
- machine-readable authority mapping
- current work state
- session continuity
- repository health and integrity validation

Do not place business knowledge, Philosophy, Governance, Canon, learning content, domain models, or ADRs in Brain.

## Knowledge States

### Exploration

Location: `00-workbench/`

Use for unfinished ideas, questions, alternative models, drafts, architectural debates, future possibilities, and work awaiting validation. Workbench content is not authoritative.

### Philosophy

Location: `01-philosophy/`

Use for foundational beliefs, values, principles, mental models, and philosophical language.

### Governance

Location: `02-governance/`

Use for repository rules, AI roles, standards, review processes, and architectural decision records.

### Canon

Location: `03-canon/`

Use for accepted, authoritative business, mortgage, operational, and institutional knowledge.

Canon should be trustworthy, clearly scoped, sufficiently sourced when external facts are involved, structured for reuse, separated from temporary teaching activities, and changed deliberately.

### Academy

Location: `04-academy/`

Use for teaching experiences derived from Philosophy, Governance, and Canon. Academy may add examples, sequencing, exercises, assessments, and explanation, but must not invent a separate version of the underlying truth.

### Archive

Location: `99-archive/`

Use for material that is no longer active but should remain traceable. Do not archive unfinished work merely because it is incomplete; unfinished work normally belongs in the Workbench.

Design History under [`99-archive/design-history/`](99-archive/design-history/) preserves architectural evolution, qualifying conversation summaries, completed milestones, and retired architectures. It is explanatory only. Current repository documents always win, and accepted outcomes must be recorded in the appropriate Philosophy, Governance, Canon, or ADR document.

The canonical creation and closeout rules are defined in [`02-governance/design-history-workflow.md`](02-governance/design-history-workflow.md).

#### Conversation Summary Rule

Every archived conversation summary must:

1. use [`99-archive/design-history/SUMMARY-TEMPLATE.md`](99-archive/design-history/SUMMARY-TEMPLATE.md)
2. be stored under `99-archive/design-history/conversation-summaries/`
3. follow `YYYY-MM-DD-topic-summary.md` naming
4. retain the historical-reference and non-authoritative notices
5. complete every template section, using `None` or `Not available` where necessary
6. link accepted outcomes to their authoritative repository documents rather than duplicating them
7. include applicable ADRs, pull requests, commit SHAs, and related archive records

A summary that does not meet these requirements is not ready to be added to the archive.

#### Design History Closeout Rule

After every major architectural milestone, review whether current repository documents, ADRs, Brain continuity, a milestone record, a qualifying conversation summary, an evolution narrative, or a retired-architecture explanation require updates.

Not every conversation belongs in Design History. Add a summary only when the conversation produced enduring insight that materially shaped, challenged, or clarified long-term architecture. Add a full transcript only when the complete exchange has exceptional historical value and has been reviewed for secrets and sensitive personal information. Design History must never be loaded as default Spark Brain context or used to establish current authority.

## Governing Work Method

Spark OS uses **Explore → Challenge → Audit → Close → Distill** inside the existing repository lifecycle:

- **Explore:** investigate an idea freely enough to expose its possibilities, assumptions, and implications.
- **Challenge:** test it with trade-offs, counterexamples, edge cases, obligations, and credible contrary evidence.
- **Audit:** check conceptual coherence, repository fit, authority, duplication, scope, downstream ownership, and over-complexity.
- **Close:** declare the exploration sufficiently tested and mapped to serve as source material. Closure does not make conclusions accepted, complete, or canonical.
- **Distill:** carry only the durable, appropriately owned content into a concise candidate for deliberate acceptance.

This cycle is a working method inside the existing repository lifecycle, not another knowledge state, acceptance layer, authority, or required set of new files. Apply it proportionately; trivial mechanical changes do not require ceremonial execution of every stage.

## Change Workflow

For a small non-architectural change:

1. Perform Quick Resume.
2. Identify the authoritative file.
3. Make one coherent change.
4. Review the diff and downstream effects.
5. Run repository integrity validation when navigation or structure changed.
6. Commit with an intent-based message.
7. Update Brain state when the work changes the active continuation point.

For a material, architectural, or governance change:

1. Perform Full Architectural Boot.
2. Create a branch.
3. Identify affected authorities and whether an ADR is required.
4. Make the proposed changes.
5. Update navigation, current state, and session continuity.
6. Run `python tools/validate_repository.py`.
7. Open a pull request.
8. Review the complete diff, reasoning, integrity result, and downstream effects.
9. Merge only after acceptance.

## Architectural Decision Records

Create an ADR when a decision:

- affects multiple areas of Spark OS
- establishes a durable constraint
- creates a meaningful trade-off
- would be difficult to reconstruct later
- changes architecture, governance, authority, boot behavior, or integrity guarantees

The only canonical ADR location is:

`02-governance/architecture-decisions/`

Use the template:

`02-governance/architecture-decisions/ADR-TEMPLATE.md`

Do not create another ADR directory or numbering system.

## Commit Messages

A commit should describe a meaningful checkpoint or decision. Prefer an imperative phrase that explains intent.

Good examples:

```text
Establish Spark OS foundational architecture
Define Claude as repository steward
Adopt Spark Brain as repository control plane
```

Avoid generic messages such as `Update files` or `Changes`.

## File Naming

Use descriptive names, lowercase kebab-case for general repository files, conventional uppercase names only where GitHub convention improves discovery, and stable names that describe the concept rather than a temporary project phase.

ADRs use four-digit numbering:

```text
ADR-0002-spark-brain-control-plane.md
```

## Linking

Prefer relative Markdown links. Link to the authoritative source instead of repeating large blocks of knowledge.

When a concept has one canonical definition, other documents should summarize it only when navigation requires context and must link back to the source.

## Review Questions

Before accepting a meaningful change, ask:

- Does this preserve Spark Philosophy?
- Does it contradict accepted Governance or Canon?
- Does it create a second source of truth?
- Is the file in the authority location named by the repository map?
- Does it improve competence, judgment, trust, retrieval, or continuity?
- Does it make Spark OS simpler or merely larger?
- What downstream outputs need revision?
- Do the integrity checks pass?

## AI Contributions

AI-generated content must be reviewed according to the same standards as human-generated content.

AI may draft, restructure, compare, identify conflicts, propose links, identify missing assumptions, and execute approved repository routines.

AI may not independently decide what Spark believes, what becomes Canon, or whether a major architectural decision is accepted.

See [`02-governance/ai-governance/AI_GOVERNANCE.md`](02-governance/ai-governance/AI_GOVERNANCE.md).

## Definition of Done

A change is complete when:

- it is in the correct authority location
- its purpose is clear
- links work
- duplication has been considered
- major trade-offs are documented
- affected navigation is updated
- current state and session continuity are accurate when applicable
- every modified file has been re-read
- repository integrity validation passes
- the commit message explains the intent
- failed or unverified actions are recorded
