# Spark OS

Spark OS is the knowledge operating system for Spark Mortgages.

It exists to turn the company’s principles, mortgage expertise, operating knowledge, educational methods, and institutional decisions into a reliable system that can be taught, referenced, improved, and used by people and software.

Spark OS is not a folder of training documents. It is the authoritative knowledge system from which training, reference material, operating procedures, AI instructions, and future software experiences are derived.

## Start Here

Spark Brain is the repository control plane. It loads and validates repository context without replacing the authoritative knowledge structure.

- Resume work: [`brain/resume.md`](brain/resume.md)
- Boot sequence: [`brain/boot-sequence.md`](brain/boot-sequence.md)
- Current state: [`brain/current-state.md`](brain/current-state.md)
- Repository map: [`brain/repository-map.md`](brain/repository-map.md)
- Integrity checks: [`brain/health.md`](brain/health.md)

Before architectural or governance work, use the Full Architectural Boot.

## Why Spark OS Exists

Traditional mortgage training is often long, fragmented, difficult to trust as a reference, and overly dependent on memorization or mentor availability.

Spark OS is designed to:

- reduce time to genuine competence
- teach judgment rather than isolated facts
- explain why before how
- preserve institutional knowledge
- reduce unnecessary mentor dependence
- keep training, operations, reference material, and software aligned
- make important decisions traceable over time

## Source-of-Truth Principle

Markdown in this repository is the canonical source of truth for Spark OS.

Courses, reference cards, PDFs, software screens, AI context, mentor guides, and client-facing resources should derive from accepted repository knowledge rather than becoming competing sources of truth.

See [ADR-0001](02-governance/architecture-decisions/ADR-0001-markdown-source-of-truth.md).

Spark Brain owns navigation and continuity. It does not own Philosophy, Governance, Canon, Academy content, or ADRs. See [ADR-0002](02-governance/architecture-decisions/ADR-0002-spark-brain-control-plane.md).

## Repository Map

| Area | Question it answers |
|---|---|
| [`brain`](brain/) | How do we start, resume, navigate, and validate the repository? |
| [`00-workbench`](00-workbench/) | What are we currently exploring? |
| [`01-philosophy`](01-philosophy/) | What do we believe? |
| [`02-governance`](02-governance/) | How does Spark OS govern and change itself? |
| [`03-canon`](03-canon/) | What has Spark OS accepted as authoritative knowledge? |
| [`04-academy`](04-academy/) | How do we teach the Canon? |
| [`99-archive`](99-archive/) | What has been retired but intentionally preserved? |

The detailed authority map is maintained in [`brain/repository-map.md`](brain/repository-map.md) and [`brain/manifest.yaml`](brain/manifest.yaml).

## Knowledge Lifecycle

```text
Idea
  ↓
Workbench
  ↓
Discussion and challenge
  ↓
Accepted destination
  ↓
Philosophy, Governance, or Canon
  ↓
Academy, reference, operations, AI, and software outputs
```

Exploratory material is not authoritative. Canonical material should not be changed casually. Outputs should be corrected by updating their source knowledge first whenever practical.

## Roles

### Sheldon Phillips

Vision owner, mortgage subject-matter expert, culture builder, and final decision maker.

### ChatGPT

Chief Knowledge & Learning Architect. Helps convert vision and expertise into principles, architecture, canonical knowledge, and effective learning systems. Challenges weak assumptions and protects coherence.

### Claude

Repository Steward. Executes repository-maintenance responsibilities defined by Spark OS. Claude supports organization, consistency, metadata, links, and repository health, but does not own strategy or architecture.

See [AI Governance](02-governance/ai-governance/AI_GOVERNANCE.md).

## How Work Enters Spark OS

1. New thinking begins in the Workbench.
2. Important trade-offs are discussed and documented.
3. Major architectural decisions receive an ADR.
4. Accepted knowledge moves to its canonical destination.
5. Educational and operational outputs derive from accepted sources.
6. Material that is no longer active is archived rather than silently erased.
7. Spark Brain records current work and validates navigation; it does not create another acceptance layer.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Current Status

Spark OS is in **Repository Foundation and Philosophy Development**.

The repository currently establishes:

- the numbered knowledge architecture
- the knowledge lifecycle
- AI role boundaries
- contribution rules
- the canonical ADR system
- Spark Brain v2 startup, navigation, continuity, and integrity controls
- the Philosophy framework and document boundaries

The next content milestone is to complete the Philosophy foundation in the sequence defined by [`01-philosophy/README.md`](01-philosophy/README.md), beginning with the Manifesto.

## Design North Star

Spark OS should help people become capable faster, make better decisions, find trustworthy answers, and understand why the system works the way it does.