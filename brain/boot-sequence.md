# Boot Sequence

Spark Brain provides two startup modes. Use the smallest mode that safely supports the work.

## Quick Resume

Use for normal continuation when no architectural or governance decision is expected.

Read in order:

1. [`constitution.md`](constitution.md)
2. [`current-state.md`](current-state.md)
3. [`session.md`](session.md)
4. The authoritative files linked by the Current Priority or Next Task
5. ADRs changed since the last verified commit recorded in `session.md`

Then confirm:

- the referenced paths exist
- the current branch or working context is understood
- the Next Task still matches repository reality
- no unresolved integrity failure blocks work

Quick Resume must not load the entire Canon by default.

## Full Architectural Boot

Use before changing authority, governance, repository structure, Philosophy boundaries, Canon boundaries, AI roles, boot behavior, or system architecture.

Read in order:

1. [`../README.md`](../README.md)
2. [`constitution.md`](constitution.md)
3. [`../CONTRIBUTING.md`](../CONTRIBUTING.md)
4. [`repository-map.md`](repository-map.md)
5. [`../02-governance/ai-governance/AI_GOVERNANCE.md`](../02-governance/ai-governance/AI_GOVERNANCE.md)
6. [`../01-philosophy/README.md`](../01-philosophy/README.md)
7. [`../02-governance/architecture-decisions/`](../02-governance/architecture-decisions/), including all relevant accepted ADRs
8. [`current-state.md`](current-state.md)
9. [`session.md`](session.md)
10. The authoritative documents affected by the proposed change
11. [`health.md`](health.md)

Before writing, state:

- which authority is affected
- whether an ADR is required
- what downstream documents may need review
- whether the change creates a new source of truth

## Dynamic ADR Loading

The manifest identifies the canonical ADR directory. During startup:

- read every accepted ADR that defines the area being changed
- read every ADR created or modified after the last verified commit
- do not assume ADR numbers imply current authority; check status and supersession metadata

## Failure Behavior

Stop architectural work and report the conflict when:

- a required boot file is missing
- two locations claim the same authority
- the manifest and repository map disagree
- current state references a missing file or retired authority
- repository integrity validation fails
- an ADR path or number is ambiguous

Do not silently repair authority conflicts during ordinary feature work.