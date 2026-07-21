# Repository Map

This map identifies where each class of repository knowledge is authoritative. It is navigation, not a replacement for the linked sources.

| Area | Canonical location | Authority |
|---|---|---|
| Exploration | [`../00-workbench/`](../00-workbench/) | Drafts, proposals, unresolved questions, and work awaiting acceptance |
| Philosophy | [`../01-philosophy/`](../01-philosophy/) | Foundational beliefs, values, principles, mental models, and philosophical language |
| Governance | [`../02-governance/`](../02-governance/) | Repository rules, AI roles, standards, review processes, and architecture decisions |
| Architecture decisions | [`../02-governance/architecture-decisions/`](../02-governance/architecture-decisions/) | The only canonical ADR system |
| Canon | [`../03-canon/`](../03-canon/) | Accepted mortgage, operational, and institutional knowledge |
| Academy | [`../04-academy/`](../04-academy/) | Learning experiences derived from Philosophy, Governance, and Canon |
| Archive | [`../99-archive/`](../99-archive/) | Retired material preserved for traceability but no longer authoritative |
| Spark Brain | [`./`](./) | Startup, navigation, current state, session continuity, and integrity validation |

## Authority Rules

1. Brain links to authoritative knowledge; it does not restate it as a competing source.
2. A document belongs in Governance when it defines how Spark OS operates or changes.
3. A document belongs in Canon when it represents accepted business or operational knowledge.
4. A document belongs in Philosophy when it defines enduring beliefs or decision principles.
5. Architectural decisions belong only in the canonical architecture-decisions directory.
6. Retired systems are preserved through Git history and concise archive records, not copied into active navigation.

## Knowledge Lifecycle

The lifecycle remains the one defined by the root README and CONTRIBUTING guide:

```text
Idea → Workbench → review and challenge → accepted destination → derivative outputs
```

Spark Brain participates by loading and validating that lifecycle. It does not create an additional acceptance state.

## Machine-Readable Source

[`manifest.yaml`](manifest.yaml) is the machine-readable form of this map. If this document and the manifest disagree, validation must fail and the conflict must be resolved before architectural work continues.