# Retired Spark Brain v1 Architecture

**Date retired:** 2026-07-20
**Archive status:** Historical reference only
**Authority:** Non-authoritative retired-architecture record

> This architecture is superseded. Current repository documents always win.

## Retired Design

Spark Brain v1 combined repository startup and continuity with vision, principles, domain language, responsibility mapping, architecture, roadmap, open questions, and a separate ADR system.

The design attempted to make project memory durable across AI conversations. Its operating goal was valuable, but its knowledge hierarchy overlapped with the existing numbered repository architecture.

## Why It Was Retired

Spark Brain v1 created or risked creating competing authorities for Philosophy, Governance, architecture and ADRs, product-domain language, and repository direction. That duplication made it unclear which document future contributors and AI should trust.

## Replacement

Spark Brain v2 replaced the knowledge hierarchy with a control-plane model. Brain now owns startup, navigation, continuity, manifest data, health, and integrity validation. Current knowledge remains authoritative in its numbered repository locations.

The replacement is defined by [ADR-0002](../../../02-governance/architecture-decisions/ADR-0002-spark-brain-control-plane.md).

## Preserved Lessons

- Repository memory should survive individual tools and conversations.
- Operating context must not become knowledge authority.
- File contents must be verified, not inferred from path existence.
- Architectural experiments should remain traceable through Git and concise historical explanation.

## Related History

- [Original Spark Brain v1 archive record](../../spark-brain-v1/README.md)
- [Spark Brain evolution](../evolution/2026-07-20-spark-brain-evolution.md)
- [Spark Brain v2 milestone](../major-milestones/2026-07-20-spark-brain-v2-milestone.md)
- [Spark Brain v1 to v2 conversation summary](../conversation-summaries/2026-07-20-spark-brain-v1-to-v2-summary.md)
- [PR #2](https://github.com/Spark-Canon/Spark-OS/pull/2)
- Merge commit `02c07f27ff107a98278b41dd3e5853fa2a76efec`
