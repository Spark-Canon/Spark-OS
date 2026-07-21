# Design History

Design History preserves the architectural evolution of Spark OS: how the repository reached its current state, why major decisions were made, which alternatives were rejected, and what earlier designs taught us.

> Repository documentation remains authoritative.
> Design History is explanatory only.
> Whenever a conflict exists, current repository documents always win.

## Purpose

Repository memory describes what is currently accepted through Philosophy, Governance, Canon, ADRs, and Spark Brain. Design History explains how and why that accepted state emerged.

Design History is historical, explanatory, and non-authoritative. It cannot approve a proposal, amend an ADR, redefine Governance, change Canon, or direct current operations. The canonical creation rules are defined in the [Design History Workflow](../../02-governance/design-history-workflow.md).

## Directory Structure

### Evolution

[`evolution/README.md`](evolution/README.md) is the single living chronological narrative of Spark OS architecture. Update it incrementally when a completed milestone changes the project's long-term direction.

### Transcripts

[`transcripts/`](transcripts/) contains optional complete conversations with exceptional historical value. Transcripts have no authority, must be clearly labeled, and must be reviewed for secrets or sensitive personal information before being committed.

### Conversation Summaries

[`conversation-summaries/`](conversation-summaries/) contains one summary for each conversation that permanently changed Spark OS architecture. Not every conversation belongs here. Use [`SUMMARY-TEMPLATE.md`](SUMMARY-TEMPLATE.md).

### Major Milestones

[`major-milestones/`](major-milestones/) contains one record for each completed architectural milestone. Milestone records summarize what was completed, why it mattered, how it was verified, and where the authoritative result lives.

### Retired Architectures

[`retired-architectures/`](retired-architectures/) explains superseded designs and why they were replaced. Preserve these records because rejected and retired approaches help future contributors understand current constraints. They are not active guidance and must link to their authoritative replacement whenever one exists.

## Authority Boundaries

- [`../../01-philosophy/`](../../01-philosophy/) contains accepted foundational beliefs.
- [`../../02-governance/`](../../02-governance/) governs how Spark OS operates and changes.
- [`../../02-governance/architecture-decisions/`](../../02-governance/architecture-decisions/) is the only canonical ADR system.
- [`../../03-canon/`](../../03-canon/) contains accepted business, mortgage, operational, and institutional knowledge.
- [`../../04-academy/`](../../04-academy/) contains learning experiences derived from authoritative sources.
- [`../../brain/`](../../brain/) is the repository control plane.
- Design History records historical reasoning only and cannot supersede any active repository document.

## Relationship to Spark Brain

Design History is separate from Spark Brain.

Spark Brain must not load Design History during Quick Resume and must not use it as operational context. Design History may be consulted only when:

- investigating previous decisions
- understanding architectural evolution
- reviewing retired approaches
- onboarding long-term contributors
- preparing a new ADR
- resolving an apparent contradiction

After consulting Design History, confirm every current claim against active repository documents.

## Naming

Use ISO dates and lowercase kebab-case topics:

```text
conversation-summaries/YYYY-MM-DD-topic-summary.md
major-milestones/YYYY-MM-DD-topic-milestone.md
retired-architectures/YYYY-MM-DD-topic-retired.md
transcripts/YYYY-MM-DD-topic-transcript.md
```

The living evolution narrative remains `evolution/README.md`. For multi-session summaries or transcripts, use the date the work concluded.

## Cross-Linking

Whenever available, link to applicable ADRs, pull requests, full commit SHAs, authoritative repository documents, and related Design History records. Links should make the history navigable without reproducing accepted knowledge.

## Milestone Closeout Workflow

Follow the canonical [Design History Workflow](../../02-governance/design-history-workflow.md).

After every major architectural milestone, determine whether:

1. authoritative repository documents require updating
2. ADRs require creating, superseding, or updating
3. `brain/current-state.md` and `brain/session.md` require updating
4. Design History should receive a new milestone record
5. a qualifying conversation summary should be created
6. an evolution narrative or retired-architecture explanation requires updating

Current repository documents and ADRs must be updated before or alongside Design History. A historical record cannot complete an architectural milestone by itself.

## Reading Order

When historical context is necessary:

1. Read the active repository documents relevant to the task.
2. Read applicable ADRs and Governance.
3. Consult related milestones or evolution records.
4. Consult conversation summaries or retired architectures only as needed.
5. Return to current repository documents before making a recommendation.

Design History must never become default operational or canonical context.
