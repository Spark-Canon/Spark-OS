# Governance

Governance answers:

> How does Spark OS operate and change itself?

This area defines authority, decision processes, repository standards, AI responsibilities, and the reasoning behind important architectural choices.

## Structure

- [`ai-governance`](ai-governance/) — AI roles, authority, boundaries, and evolution
- [`architecture-decisions`](architecture-decisions/) — the only canonical Architectural Decision Record system
- [`design-history-workflow.md`](design-history-workflow.md) — rules for creating non-authoritative architectural history
- Future standards may include:
  - document standards
  - writing standards
  - assessment standards
  - repository review routines

## Relationship to Spark Brain

Spark Brain is the repository control plane. It loads, navigates, and validates Governance but does not redefine it.

- Brain authority map: [`../brain/repository-map.md`](../brain/repository-map.md)
- Machine-readable manifest: [`../brain/manifest.yaml`](../brain/manifest.yaml)
- Control-plane decision: [`architecture-decisions/ADR-0002-spark-brain-control-plane.md`](architecture-decisions/ADR-0002-spark-brain-control-plane.md)
- Design History workflow: [`design-history-workflow.md`](design-history-workflow.md)

Governance remains authoritative for repository rules, AI roles, standards, review processes, and ADRs.

## Governance Principle

Spark OS owns its processes.

Tools and AI systems execute responsibilities defined here. No tool should become the hidden owner of a workflow that Spark OS depends upon.

## Change Discipline

Governance should evolve when repeated experience reveals a genuine need.

Do not add policies merely because they sound professional. Governance should reduce ambiguity and protect quality without creating unnecessary bureaucracy.

Material governance changes require Full Architectural Boot, an ADR when appropriate, and repository integrity validation.
