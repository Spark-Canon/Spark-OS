# Design History

The Design History archive preserves important conversations that explain how Spark OS ideas, trade-offs, and architecture evolved.

> Repository documents are authoritative.
> Archived conversations are historical reference only.

## Purpose

Use this archive when the reasoning behind an important design direction may help future contributors understand context that is not appropriate to reproduce in an active repository document.

The archive supports traceability. It is not an approval mechanism, a project-memory layer, or a source of current instructions. Future human and AI contributors should read the active repository first and consult this archive only when historical context is needed.

## Authority Boundaries

- Active repository documents outrank every archived conversation.
- [`../../02-governance/architecture-decisions/`](../../02-governance/architecture-decisions/) is the only canonical ADR system.
- [`../../02-governance/`](../../02-governance/) governs how Spark OS operates and changes.
- [`../../01-philosophy/`](../../01-philosophy/) contains accepted foundational beliefs.
- [`../../03-canon/`](../../03-canon/) contains accepted business, mortgage, operational, and institutional knowledge.
- [`../../00-workbench/`](../../00-workbench/) contains active exploration and unresolved proposals.
- Archived summaries, transcripts, and decision context cannot supersede or amend any of those sources.

If an archived conversation conflicts with an active repository document, follow the active document. If the conflict reveals a genuine problem, open new work in the Workbench and use the normal governance process to resolve it.

## Relationship to ADRs

Architectural decisions belong in canonical ADRs, not in this archive. A conversation summary may explain alternatives, uncertainty, and reasoning around an ADR, but it must link to the ADR and must not restate itself as the accepted decision.

The [`decisions/`](decisions/) directory may preserve historical decision context that helps reconstruct how an outcome emerged. It is not a second ADR directory, does not use ADR numbering, and has no decision authority.

## Relationship to Governance

Governance defines the rules, roles, standards, and acceptance process for Spark OS. Conversation archives may show how governance was discussed, but only accepted documents under [`../../02-governance/`](../../02-governance/) govern the repository.

## Relationship to Canon

Canon contains accepted knowledge. A conversation may contain hypotheses, incomplete explanations, or rejected suggestions. None of that becomes Canon until it is deliberately reviewed and accepted into [`../../03-canon/`](../../03-canon/).

Never use this archive to duplicate accepted Canon. Link to the canonical document instead.

## Directory Structure

- [`chat-summaries/`](chat-summaries/) contains concise historical summaries of major conversations.
- [`transcripts/`](transcripts/) contains optional raw or lightly formatted transcripts.
- [`decisions/`](decisions/) contains optional historical decision context that is useful alongside, but never instead of, canonical ADRs or Governance.

## Naming

Use lowercase kebab-case topics and ISO dates:

```text
YYYY-MM-DD-topic-summary.md
YYYY-MM-DD-topic-transcript.md
```

When a separate historical decision-context file is useful, name it:

```text
YYYY-MM-DD-topic-decision-context.md
```

The date should represent the conversation date or, for a multi-session conversation, the date it concluded.

## Summary Content

Every summary must be created from [`SUMMARY-TEMPLATE.md`](SUMMARY-TEMPLATE.md). Required sections may state `None` or `Not available` when they do not apply; they must not be silently removed.

Whenever possible, a summary should include:

- the conversation date and topic
- its historical status and scope
- major questions and alternatives considered
- major architectural decisions discussed
- links to resulting or related ADRs
- related pull request numbers and links
- relevant commit SHAs
- links to related repository documents
- unresolved questions or rejected directions when historically useful
- a link to the raw transcript when one is stored

Summaries should describe the reasoning without copying accepted knowledge from its authoritative repository location.

## Workflow

For every major architectural conversation:

1. Produce a concise summary.
2. Copy [`SUMMARY-TEMPLATE.md`](SUMMARY-TEMPLATE.md), complete every required section, and remove all template guidance.
3. Store it under [`chat-summaries/`](chat-summaries/) using the required naming convention.
4. Link to any ADRs created or affected.
5. Record relevant pull requests, commits, and repository documents whenever available.
6. Store the raw transcript separately under [`transcripts/`](transcripts/) only when its historical value justifies retention.
7. Store separate decision context under [`decisions/`](decisions/) only when it adds useful history beyond the summary and ADR.
8. Record accepted outcomes in their authoritative repository locations.
9. Never duplicate accepted repository knowledge in the archive.

## Reading Order for Future AI

Future AI should use this order:

1. Read the active repository documents relevant to the task.
2. Read applicable ADRs.
3. Read relevant Governance and Philosophy.
4. Consult Design History only when historical reasoning is needed.
5. Treat every archived claim as non-authoritative unless confirmed by an active repository source.

Archived conversations must never be loaded as default canonical context.
