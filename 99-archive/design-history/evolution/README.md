# Spark OS Architectural Evolution

**Last updated:** 2026-07-22
**Archive status:** Historical reference only
**Authority:** Non-authoritative evolution narrative

> Current repository documents always win.

## Spark Brain v1 to Spark Brain v2

Spark Brain began as a repository-backed memory hierarchy intended to preserve continuity across AI conversations. Spark Brain v1 combined operating memory with vision, principles, terminology, architecture, open questions, responsibility mapping, roadmap content, and a separate ADR system.

An architectural audit compared that design with the existing numbered Spark OS repository. The audit found overlapping authority across Philosophy, Governance, Canon, and architectural decisions. Although a preliminary file-truncation concern was later disproven, the authority conflicts were real.

The repository preserved the experiment and migrated in place. Spark Brain v2 retained deterministic startup, navigation, state continuity, health checks, and integrity validation while returning knowledge authority to the numbered repository.

```text
Spark Brain v1
    ↓
Repository audit
    ↓
Authority reconciliation
    ↓
Spark Brain v2 control plane
    ↓
Future evolution through Governance and ADRs
```

## Why the Architecture Changed

The redesign separated current knowledge from the mechanism used to load and validate it. This removed competing sources of truth while preserving durable repository memory and deterministic AI startup.

## Authoritative Outcome

The accepted architecture is defined by [ADR-0002](../../../02-governance/architecture-decisions/ADR-0002-spark-brain-control-plane.md), the [Spark Brain Constitution](../../../brain/constitution.md), and the [Repository Map](../../../brain/repository-map.md).

## Repository Foundation to Accepted Philosophy

After the repository control plane and Design History boundaries stabilized, Spark OS moved from structural Philosophy placeholders to accepted foundational content for Spark Mortgages.

The Manifesto and Values were developed through open exploration, deliberate challenge, independent audit, explicit human approval, bounded installation, and post-install verification. The resulting canonical architecture remained the original five-document Philosophy structure rather than expanding to match every exploratory topic.

This milestone established a durable pattern: exploratory detail may remain broad, but accepted repository knowledge should be distilled into the smallest coherent authoritative form. The full Explore → Challenge → Audit → Close → Distill method was placed in `CONTRIBUTING.md` as a proportionate working method rather than another authority or lifecycle.

The authoritative Philosophy now begins with the accepted [Manifesto](../../../01-philosophy/manifesto.md) and [Values](../../../01-philosophy/values.md). Principles remain the next deliberately authorized development phase.

## Related History

- [Spark Brain v1 to v2 conversation summary](../conversation-summaries/2026-07-20-spark-brain-v1-to-v2-summary.md)
- [Spark Brain v2 milestone](../major-milestones/2026-07-20-spark-brain-v2-milestone.md)
- [Foundational Philosophy milestone](../major-milestones/2026-07-22-foundational-philosophy-milestone.md)
- [Retired Spark Brain v1 architecture](../retired-architectures/2026-07-20-spark-brain-v1-retired.md)
- [PR #2](https://github.com/Spark-Canon/Spark-OS/pull/2)
- [PR #6](https://github.com/Spark-Canon/Spark-OS/pull/6)
- Merge commit `02c07f27ff107a98278b41dd3e5853fa2a76efec`
- Merge commit `ceedf64d0ec1bf504ccb408c81cd2986be517e37`
