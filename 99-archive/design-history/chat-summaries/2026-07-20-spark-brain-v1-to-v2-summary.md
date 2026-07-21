# Spark Brain v1 to Spark Brain v2

**Date:** 2026-07-20
**Archive status:** Historical reference only
**Authority:** Non-authoritative conversation summary

> Repository documents are authoritative. Archived conversations are historical reference only.

## Purpose

This conversation developed the architectural model that transformed Spark Brain from a competing documentation hierarchy into the repository operating layer for Spark OS.

## Context

Spark OS already had a numbered knowledge architecture for Philosophy, Governance, Canon, Academy, exploration, and retired material. Spark Brain v1 was introduced as a repository-backed memory system, but its scope overlapped with those existing authorities.

The conversation and subsequent audit explored how to retain deterministic AI startup and durable repository memory without creating another source of truth.

## Major Milestones

### Spark Brain v1

Spark Brain v1 was designed as a repository-backed memory system containing:

- Constitution
- Current State
- Vision
- Principles
- Domain Language
- Responsibility Map
- Architecture
- Roadmap
- Open Questions
- ADRs

An initial GitHub installation package was prepared.

### Repository Audit

An independent architectural audit reviewed the implementation and identified concerns including:

- duplicate knowledge systems
- competing principle systems
- competing ADR systems
- competing governance
- competing source-of-truth hierarchies

The audit ultimately led to a major architectural redesign. An early audit conclusion about truncated Brain v1 files was later rejected after complete file reads showed that the prepared contents were present; the authority-conflict findings remained valid.

### Spark Brain v2

The key realization was:

> Spark Brain should not own knowledge. Spark Brain should own navigation.

Repository knowledge remained authoritative within Philosophy, Governance, Canon, Academy, and the canonical ADR system. Spark Brain became responsible for:

- boot sequence
- repository navigation
- session continuity
- current state
- repository health
- integrity validation
- deterministic AI startup

### GitHub Migration

The migration was performed on the `spark-brain-v2-migration` feature branch through [pull request #2](https://github.com/Spark-Canon/Spark-OS/pull/2). Repository integrity checks and cold-start review confirmed the design, and Sheldon completed the semantic review and merge into `main`.

## Alternatives and Concerns

The migration considered rolling back to the pre-Brain commit, repairing Brain v1 as a parallel knowledge hierarchy, and moving the numbered repository architecture under Brain. These approaches were rejected in favor of an in-place migration that preserved Git history while restoring one canonical authority for each information type.

The primary risk was allowing repository memory and startup guidance to become a second knowledge system rather than a control plane.

## Architectural Principles Discussed

- Repository owns knowledge.
- Spark Brain owns navigation.
- One canonical authority should exist for every type of information.
- Sources of truth should not be duplicated.
- AI startup should be deterministic.
- Repository-backed memory should survive individual conversations and tools.

These principles are historical observations unless confirmed by the authoritative documents linked below.

## Outcome

Spark OS adopted Spark Brain v2 as a repository control plane:

- the repository provides durable, authoritative long-term memory
- Spark Brain starts, navigates, resumes, and validates that memory
- conversations remain temporary working sessions unless preserved as non-authoritative history

The accepted architectural outcome is recorded in [ADR-0002](../../../02-governance/architecture-decisions/ADR-0002-spark-brain-control-plane.md), not in this summary.

## Lessons Learned

- Verify file contents, not merely file existence.
- Repository history is valuable and should generally be preserved.
- Repository memory should survive individual AI conversations.
- Spark Brain should function as the repository control plane rather than another documentation hierarchy.
- Automated integrity checks do not replace human semantic review.

## Repository References

### Authoritative Documents

- [ADR-0001: Markdown Is the Canonical Source of Truth](../../../02-governance/architecture-decisions/ADR-0001-markdown-source-of-truth.md)
- [ADR-0002: Spark Brain Is the Repository Control Plane](../../../02-governance/architecture-decisions/ADR-0002-spark-brain-control-plane.md)
- [Spark Brain Constitution](../../../brain/constitution.md)
- [Repository Map](../../../brain/repository-map.md)
- [AI Governance](../../../02-governance/ai-governance/AI_GOVERNANCE.md)
- [Archived Spark Brain v1 record](../../spark-brain-v1/README.md)

### Pull Requests

- [PR #2 — Migrate Spark Brain to repository control plane](https://github.com/Spark-Canon/Spark-OS/pull/2)

### Commits

- `b61b3e52947d0b592c379ca26ddc79b252bf40b1` — final `main` commit before the Spark Brain v2 migration branch
- `a40fc7e8740e56db2021c8266a8b60d5a1e8e825` — installed the Spark Brain v2 operating layer index and verified migration state
- `be831b6360833d60cbe38a6db77feff740b2d697` — closed the Spark Brain v2 migration session
- `02c07f27ff107a98278b41dd3e5853fa2a76efec` — merged pull request #2 into `main`

### Related Archive Records

- [Spark Brain v1 archive record](../../spark-brain-v1/README.md)
- Raw transcript: None archived

## Unresolved Questions

- None recorded for the accepted control-plane architecture.

## Next Milestone at Time of Conversation

Complete the Philosophy foundation in sequence—Manifesto, Values, Principles, Mental Models, and Glossary—before resuming deeper domain architecture.
