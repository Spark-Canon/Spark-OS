# Repository Memory, Design History, and Controlled Skill Installation

**Date:** 2026-08-14
**Archive status:** Historical reference only
**Authority:** Non-authoritative conversation summary

> Repository documents are authoritative. Archived conversations are historical reference only.

## Purpose

This multi-session conversation connected three stages of Spark OS development: resuming Spark Brain v2 after authority reconciliation, establishing Design History without creating historical authority, and installing a tightly bounded Training Research Pilot 001 skill without invoking it.

The recurring problem was how to preserve durable memory, reasoning, and reusable execution capability without creating duplicate knowledge authority or silently expanding authorization.

## Context

Spark OS already used a numbered authority architecture for Philosophy, Governance, Canon, Academy, Workbench, and Archive. Spark Brain v2 was intended to provide startup, navigation, continuity, and integrity validation without owning repository knowledge.

Pull request #2 had migrated Spark Brain from a competing knowledge hierarchy into that control-plane role. Repository continuity initially described the pull request as awaiting review, but GitHub inspection and explicit user confirmation established that it had already been reviewed and merged.

The Philosophy foundation remained incomplete at the beginning of the conversation. Its planned sequence was Manifesto, Values, Principles, Mental Models, and Glossary.

## Major Milestones

### Spark Brain v2 Resume

Repository inspection re-established the actual state after pull request #2. A local checkout was restored, the Spark Brain resume sequence and repository health instructions were followed, and repository integrity validation passed.

The inspection showed that continuity prose can remain structurally valid while becoming semantically stale. The continuation point was corrected conceptually:

- Spark Brain v2 was active as the repository control plane
- repository foundation work was substantially complete
- Philosophy development was next
- domain-software architecture remained deferred until Philosophy could constrain it

The detailed authority reconciliation is preserved in the existing [Spark Brain v1 to v2 conversation summary](2026-07-20-spark-brain-v1-to-v2-summary.md) and related milestone records rather than repeated here.

### Initial Conversation Archive

The conversation developed a permanent archive for consequential design discussions while preserving the rule that repository documents remain authoritative and archived conversations remain historical reference only.

The initial archive introduced:

- curated conversation summaries
- optional complete transcripts
- explicit non-authoritative notices
- a required summary template
- contribution rules and cross-linking to applicable ADRs, pull requests, full commit SHAs, authoritative documents, and related history

The first summary documented the Spark Brain v1-to-v2 migration. Pull request #3 installed the initial archive system and was later merged.

### Philosophy Handoff Boundary

After the initial archive was merged, the repository handoff clarified that regular GPT conversations could help develop Philosophy drafts, but conversation output remained a proposal until separately reviewed and installed.

Codex was expected to wait for completed drafts and explicit installation instructions. Conversation drafting, human approval, repository installation, verification, and merge remained distinct events.

### Expanded Design History

The archive model expanded into a broader Design History system with separate treatment for:

- one curated living Architectural Evolution narrative
- qualifying conversation summaries
- major milestone records
- retired-architecture explanations
- optional complete transcripts

The existing Spark Brain summary was relocated rather than duplicated. Candidate records described the Spark Brain evolution, the completed v2 milestone, and the retired v1 architecture.

Reconciliation with a separately prepared workflow produced three durable refinements:

1. Complete transcripts remained an optional, authority-free record type.
2. Architectural Evolution became one living chronology rather than multiple dated narratives.
3. Rules governing historical-document creation moved into Governance because a non-authoritative archive cannot govern repository behaviour.

Pull request #4 installed this expanded system and was later reviewed and merged.

### Controlled Training Research Skill Installation

The conversation later received an approved four-file Training Research Pilot 001 artifact for installation only.

The authorization explicitly excluded:

- invoking the skill
- conducting research
- creating a research brief
- changing course content
- changing Philosophy, Governance, Canon, Academy, Brain, Design History, navigation, or repository architecture
- creating any fifth repository file
- merging the pull request

A clean checkout separate from the historical audit workspace was verified against the approved base commit. Four source bodies were normalized to UTF-8 without BOM, LF line endings, and one final LF. Each approved file and the deterministic manifest matched its expected SHA-256.

Current Skill Creator tooling was run only in an isolated staging location. Generated placeholders did not enter the repository.

Exactly four files were installed:

- the `training-research` skill
- its OpenAI interface metadata
- the Pilot 001 research-brief standard
- a non-authoritative Workbench README

The skill remained invocation-only. Its interface disabled implicit invocation and its default prompt named `$training-research` explicitly.

Official skill validation initially could not start because PyYAML was unavailable. Rather than changing the global or repository environment, the dependency was installed into an isolated temporary environment and the unmodified validator passed there.

Draft pull request #17 was opened without invoking the skill or creating research output. GitHub Actions passed. The pull request was later merged after the conversation endpoint.

## Alternatives and Concerns

The conversation rejected:

- retaining Spark Brain as a parallel knowledge hierarchy
- erasing the Spark Brain v1 experiment rather than preserving Git history and explaining its retirement
- treating conversation history as repository memory or current authority
- storing Design History creation rules only inside the non-authoritative archive
- maintaining multiple dated evolution narratives
- archiving every conversation regardless of enduring value
- deleting retired-architecture explanations
- loading Design History during Spark Brain startup
- installing the Training Research skill in a workspace containing unrelated changes
- installing validation dependencies globally
- interpreting successful installation as permission to invoke the skill, conduct research, or change course content

The principal risks were duplicate authority, stale historical context influencing current decisions, hidden expansion of scope, contamination from unrelated local changes, and conflating implementation success with substantive authorization.

## Architectural Principles Discussed

- Spark OS owns knowledge; Spark Brain owns startup, navigation, continuity, and validation.
- Current repository documents describe accepted truth; Design History explains how that state emerged.
- Governance rules belong in Governance even when they govern non-authoritative historical material.
- Conversation exploration, human approval, repository installation, verification, and merge are distinct authority events.
- Historical summaries explain reasoning; ADRs record accepted architectural decisions.
- Installation, invocation, research execution, evidence consultation, and content acceptance require separate authorization.
- Research evidence remains distinct from Canon, Academy content, and Academy decisions.
- Draft pull requests preserve review boundaries and do not create accepted repository state.
- Exact-scope implementation benefits from deterministic fingerprints and isolated working environments.

These principles are historical observations unless confirmed by the authoritative documents linked below.

## Outcome

The conversation confirmed Spark Brain v2 as the repository control plane, developed the archive and expanded Design History model, and installed the approved Training Research Pilot 001 skill on a dedicated branch without invoking it.

Repository verification after the conversation established that:

- pull request #3 merged the initial archive system
- pull request #4 merged the expanded Design History system and Governance workflow
- pull request #17 merged the four-file Training Research Pilot 001 installation

The current repository implementation is defined by the linked active documents and skill files, not by this summary. The Training Research skill installation did not itself authorize research, create a brief, or make any research evidence authoritative.

## Lessons Learned

- Durable memory depends on explicit authority boundaries, not merely persistent files.
- A repository control plane should load and validate knowledge without owning it.
- Historical reasoning remains useful only while subordinate to current repository truth.
- Non-authoritative areas cannot be the sole authority for rules governing their own creation.
- One curated evolution narrative is clearer than fragmented histories.
- Fewer high-quality historical records are preferable to indiscriminate archiving.
- Semantic review remains necessary even when automated integrity validation passes.
- Deterministic source fingerprints and isolated checkouts make exact installation auditable.
- Tool installation, tool invocation, research, and downstream adoption are separate authorization events.
- Tooling dependencies should be isolated when repository purity and reproducibility matter.

## Repository References

### Authoritative Documents

- [Spark OS README](../../../README.md)
- [Contributing to Spark OS](../../../CONTRIBUTING.md)
- [Spark Brain Constitution](../../../brain/constitution.md)
- [Boot Sequence](../../../brain/boot-sequence.md)
- [Repository Map](../../../brain/repository-map.md)
- [Current State](../../../brain/current-state.md)
- [Repository Health](../../../brain/health.md)
- [AI Governance](../../../02-governance/ai-governance/AI_GOVERNANCE.md)
- [Design History Workflow](../../../02-governance/design-history-workflow.md)
- [ADR-0001: Markdown Is the Canonical Source of Truth](../../../02-governance/architecture-decisions/ADR-0001-markdown-source-of-truth.md)
- [ADR-0002: Spark Brain Is the Repository Control Plane](../../../02-governance/architecture-decisions/ADR-0002-spark-brain-control-plane.md)
- [Training Research Pilot 001 skill](../../../.agents/skills/training-research/SKILL.md)
- [Training Research interface metadata](../../../.agents/skills/training-research/agents/openai.yaml)
- [Pilot 001 research-brief standard](../../../.agents/skills/training-research/references/research-brief-standard.md)
- [Training Research Workbench boundary](../../../00-workbench/training-research/README.md)

### Pull Requests

- [PR #2 — Migrate Spark Brain to repository control plane](https://github.com/Spark-Canon/Spark-OS/pull/2)
- [PR #3 — Install conversation archive system](https://github.com/Spark-Canon/Spark-OS/pull/3)
- [PR #4 — Expand Spark OS Design History](https://github.com/Spark-Canon/Spark-OS/pull/4)
- [PR #17 — Install approved Training Research Pilot 001 skill](https://github.com/Spark-Canon/Spark-OS/pull/17)

### Commits

- `02c07f27ff107a98278b41dd3e5853fa2a76efec` — merged the Spark Brain v2 migration through pull request #2
- `0468dedb6f4296b9af896405e09c185de43c8a1d` — merged the initial Conversation Archive System through pull request #3
- `44a884e906701d6b3ab0faa3ea92202ed2617d2f` — refined the Design History workflow
- `316627d944696c680b2615b02ca7578e618da065` — merged the expanded Design History system through pull request #4
- `91fc6d2c0fb490d56b64d15f715f147ffa9d050b` — installed the approved Training Research Pilot 001 skill
- `25dc8446ee55dcff1eba3027b47f277315b767cf` — merged the skill installation through pull request #17

### Related Archive Records

- [Spark Brain v1 to v2 conversation summary](2026-07-20-spark-brain-v1-to-v2-summary.md)
- [Spark OS Architectural Evolution](../evolution/README.md)
- [Spark Brain v2 milestone](../major-milestones/2026-07-20-spark-brain-v2-milestone.md)
- [Retired Spark Brain v1 architecture](../retired-architectures/2026-07-20-spark-brain-v1-retired.md)
- Raw transcript: None archived

## Unresolved Questions

- Will Pilot 001 be explicitly invoked under its fixed repository and base-commit preconditions?
- How will a future research brief be reviewed before any separately authorized Academy consultation?
- Will domain research later receive a separately governed skill and authorization model?
- Should future evidence justify additional Design History templates or automated naming validation?

## Next Milestone at Time of Conversation

Review draft pull request #17 while leaving it unmerged and without invoking `$training-research`. This was the historical continuation point at the end of the conversation; pull request #17 has since been merged, but no invocation or research activity is implied by that merge.
