# Spark Brain Constitution

**Version:** 2.0  
**Status:** Active  
**Repository:** `Spark-Canon/Spark-OS`  
**Authority:** Repository operating layer

## Purpose

Spark Brain is the control plane for Spark OS. It gives humans and AI a deterministic way to start, resume, navigate, and validate repository work.

Spark Brain does not own Philosophy, Governance, Canon, Academy content, or architectural decisions. Those remain authoritative in their existing repository locations.

## Foundational Rule

> Spark Brain owns navigation. The repository owns knowledge.

Brain files may summarize a path or loading rule, but they must link to the authoritative source instead of redefining its substance.

## Authority Boundaries

- Philosophy: [`../01-philosophy/`](../01-philosophy/)
- Governance: [`../02-governance/`](../02-governance/)
- Architecture decisions: [`../02-governance/architecture-decisions/`](../02-governance/architecture-decisions/)
- Business knowledge: [`../03-canon/`](../03-canon/)
- Learning design and instruction: [`../04-academy/`](../04-academy/)
- Exploratory work: [`../00-workbench/`](../00-workbench/)
- Retired material: [`../99-archive/`](../99-archive/)
- Repository startup, navigation, session continuity, and health: [`./`](./)

The machine-readable authority map is [`manifest.yaml`](manifest.yaml).

## Operating Rules

1. Read before writing.
2. Load only the context required by the selected boot mode.
3. Follow links to authoritative sources; do not copy their content into Brain.
4. Use the canonical ADR process for architectural changes.
5. Keep `current-state.md` factual and current.
6. Record session continuity in `session.md`.
7. Run repository integrity validation after structural changes.
8. Never claim success from path existence alone.
9. Record failed or unverified actions explicitly.
10. Escalate conflicts between authoritative sources instead of silently resolving them.

## Boot Modes

- Use [`boot-sequence.md#quick-resume`](boot-sequence.md#quick-resume) for normal continuation.
- Use [`boot-sequence.md#full-architectural-boot`](boot-sequence.md#full-architectural-boot) before architectural or governance decisions.

## Resume Commands

The following phrases invoke Spark Brain:

- `Resume Spark OS`
- `Open Spark Brain`
- `Continue Spark Architecture`
- `Work on Spark`

Start with [`resume.md`](resume.md).

## Change Discipline

A Brain change requires an ADR when it changes:

- authority boundaries
- boot order
- repository lifecycle
- canonical locations
- integrity guarantees
- governance relationships

Routine state and session updates do not require an ADR.

## Session Closeout

Before ending meaningful repository work:

1. Update [`current-state.md`](current-state.md).
2. Update [`session.md`](session.md).
3. Update affected navigation.
4. Create or update an ADR when required.
5. Run the integrity validator described in [`health.md`](health.md).
6. Report changed paths, verification results, and unresolved concerns.

## Portability

Spark Brain must remain usable without dependence on a particular AI model, chat history, or proprietary interface. Markdown, Git history, and the machine-readable manifest are the durable memory substrate.