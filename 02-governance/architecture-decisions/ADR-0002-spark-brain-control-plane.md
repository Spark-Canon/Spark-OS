# ADR-0002: Spark Brain Is the Repository Control Plane

**Status:** Accepted  
**Date:** 2026-07-20  
**Decision owners:** Sheldon Phillips and the Spark OS Knowledge & Learning Architecture function  
**Supersedes:** The authority model introduced by `/brain`, `/meta`, and `/adr` in commits `8956d807fc851af671f7725db1383749d8d82000` through `b61b3e52947d0b592c379ca26ddc79b252bf40b1`  
**Superseded by:** None

## Context

Spark OS already had a deliberate knowledge architecture:

- Philosophy in `01-philosophy`
- Governance and ADRs in `02-governance`
- accepted business knowledge in `03-canon`
- learning content in `04-academy`
- exploratory work in `00-workbench`
- retired material in `99-archive`

Spark Brain v1 added project memory under `/brain`, working agreements under `/meta`, and a second ADR system under `/adr`. Its contents were complete, but its authority model duplicated principles, terminology, architecture, open questions, and architectural decisions that belonged in the existing repository hierarchy.

The repository needs deterministic startup and session continuity without creating a second knowledge system.

## Decision

Spark Brain is the repository control plane.

It owns:

- deterministic startup
- repository navigation
- current working state
- session continuity
- machine-readable authority mapping
- repository health and integrity validation

It does not own:

- Philosophy
- Governance
- business or mortgage knowledge
- Academy content
- architectural decisions
- product-domain definitions

Those remain authoritative in their existing numbered locations.

The canonical ADR location remains `02-governance/architecture-decisions` and uses four-digit numbering.

The active `/meta` and `/adr` roots are retired. Brain v1 business-knowledge files are removed from the active Brain. Git history and `99-archive/spark-brain-v1/README.md` preserve their historical significance without retaining duplicate active authorities.

## Rationale

A control plane can load and validate knowledge without competing with it. This preserves the original repository lifecycle while giving humans and AI a reliable bootloader.

In-place migration was selected over resetting `main` because:

- Git history accurately records the failed architectural experiment
- later work can understand why the design changed
- destructive history rewriting would weaken traceability
- the existing numbered architecture does not need rebuilding
- explicit retirement is clearer than pretending Brain v1 never existed

## Alternatives Considered

### Roll Back to the Commit Before Brain v1

This would produce a clean tree quickly, but would discard visible migration history from the active branch and obscure the reason Spark Brain v2 exists.

### Repair Brain v1 as a Parallel Knowledge Hierarchy

This would preserve duplicate principles, ADRs, terminology, and architecture. It was rejected because it violates the one-source-of-truth design.

### Move All Existing Knowledge Under `/brain`

This would turn Brain into a replacement repository architecture rather than an operating layer. It was rejected because the numbered hierarchy already expresses knowledge state and authority well.

## Consequences

### Benefits

- one canonical authority for each information type
- deterministic human and AI startup
- preserved repository history
- no competing ADR or principle systems
- machine-readable authority and boot configuration
- executable integrity checks
- smaller and more stable Brain surface

### Costs and Trade-offs

- Brain documents must remain navigational and resist scope growth
- current state and session records require disciplined maintenance
- integrity validation must evolve with legitimate repository changes
- old links to `/meta`, `/adr`, or retired Brain v1 files must be corrected

### Risks

- summaries in Brain could gradually become duplicated knowledge
- validator checks may provide false confidence about semantic correctness
- stale current-state prose may remain technically valid while misleading

## Implementation

- install Spark Brain v2 operational files under `brain/`
- add `brain/manifest.yaml`
- add `tools/validate_repository.py`
- add a repository-integrity GitHub Actions workflow
- update root and governance navigation
- remove active `/meta` and `/adr` roots
- remove Brain v1 business-knowledge files
- add a concise archive record

## Review Trigger

Reconsider this decision if the control-plane model prevents reliable startup, navigation, validation, or session continuity, or if the numbered repository architecture can no longer express authority without persistent ambiguity.