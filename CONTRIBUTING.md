# Contributing to Spark OS

This document defines how Spark OS should change without becoming disorganized, duplicated, or internally inconsistent.

## Core Rule

A conversation is where ideas may begin.

The repository is where ideas become accepted.

Nothing becomes authoritative merely because it was written by Sheldon, ChatGPT, Claude, another AI, or a subject-matter expert. Authority comes from deliberate acceptance into the correct repository location.

## Before Adding a File

Ask:

1. What single purpose does this file serve?
2. Is this exploratory, governing, canonical, educational, or archived?
3. Does this knowledge already exist elsewhere?
4. Is a new file necessary, or should an existing source be improved?
5. What other files will depend on this decision?

## Knowledge States

### Exploration

Location: `00-workbench/`

Use for:

- unfinished ideas
- questions
- alternative models
- drafts
- architectural debates
- future possibilities

Workbench content is not authoritative.

### Governance

Location: `02-governance/`

Use for:

- repository rules
- AI roles
- document and writing standards
- review processes
- architectural decision records

Governance explains how Spark OS operates and changes.

### Canon

Location: `03-canon/`

Use for accepted, authoritative knowledge.

Canon should be:

- trustworthy
- clearly scoped
- sufficiently sourced when external facts are involved
- structured for reuse
- separated from temporary teaching activities
- changed deliberately

### Academy

Location: `04-academy/`

Use for teaching experiences derived from philosophy, standards, and Canon.

Academy material may add examples, sequencing, exercises, assessments, and explanation, but should not invent a separate version of the underlying truth.

### Archive

Location: `99-archive/`

Use for material that is no longer active but should remain traceable.

Do not archive something merely because it is unfinished; unfinished work normally belongs in the Workbench.

## Change Workflow

For small foundation-stage changes:

1. Identify the correct file.
2. Make one coherent change.
3. Review the diff.
4. Commit with an intent-based message.

For material changes after the foundation is stable:

1. Create a branch.
2. Make the proposed changes.
3. Open a pull request.
4. Review the diff, reasoning, and downstream effects.
5. Merge only after acceptance.

## Commit Messages

A commit should describe a meaningful checkpoint or decision.

Good:

```text
Establish Spark OS foundational architecture
Define Claude as repository steward
Clarify Canon-to-Academy knowledge flow
```

Weak:

```text
Update files
Changes
More work
```

Prefer an imperative phrase that explains the intent of the change.

## Architectural Decision Records

Create an ADR when a decision:

- affects multiple areas of Spark OS
- establishes a durable constraint
- creates a meaningful trade-off
- would be difficult to reconstruct later
- changes the architecture or governance model

Do not create ADRs for routine wording edits.

Use the template in:

`02-governance/architecture-decisions/ADR-TEMPLATE.md`

## File Naming

Use:

- descriptive file names
- lowercase kebab-case for general repository files
- uppercase conventional names only when GitHub convention improves discoverability, such as `README.md` and `CONTRIBUTING.md`
- stable names that describe the concept rather than a temporary project phase

Examples:

```text
assessment-philosophy.md
mortgage-qualification-principles.md
ADR-0001-markdown-source-of-truth.md
```

## Linking

Prefer relative Markdown links.

Link to the authoritative source instead of repeating large blocks of knowledge.

When a concept has one canonical definition, other documents should summarize it only as needed and link back to the source.

## Review Questions

Before accepting a meaningful change, ask:

- Does this preserve Spark philosophy?
- Does it contradict accepted Canon?
- Does it create a second source of truth?
- Does it improve competence, judgment, trust, or retrieval?
- Does it make Spark OS simpler or merely larger?
- What downstream outputs need revision?

## AI Contributions

AI-generated content must be reviewed according to the same standards as human-generated content.

AI may:

- draft
- restructure
- compare
- identify conflicts
- propose links
- identify missing assumptions
- execute approved repository routines

AI may not independently decide what Spark believes or what becomes Canon.

## Definition of Done

A change is complete when:

- it is in the correct location
- its purpose is clear
- links work
- duplication has been considered
- major trade-offs are documented
- the commit message explains the intent
- affected navigation is updated
