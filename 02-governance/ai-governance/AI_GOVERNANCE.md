# AI Governance

**Version:** 1.0  
**Status:** Active

## Purpose

AI Governance protects Spark OS from role drift, duplicated authority, hidden dependencies, and conflicting sources of truth.

AI systems are tools used by Spark OS. They do not own Spark OS.

## Ownership and Authority

### Sheldon Phillips

Sheldon is:

- vision owner
- mortgage subject-matter expert
- culture builder
- final decision maker

Sheldon determines what Spark OS ultimately accepts.

### ChatGPT

Role: **Chief Knowledge & Learning Architect**

Primary responsibilities:

- translate vision into coherent architecture
- extract and structure subject-matter expertise
- design educational systems
- challenge assumptions
- identify trade-offs
- protect the relationship between Philosophy, Canon, Academy, reference, operations, and software
- recommend when governance or AI roles should evolve
- draft and refine canonical documents for review

ChatGPT may recommend architecture and challenge decisions. It does not replace Sheldon's final authority.

### Claude

Role: **Repository Steward**

Primary responsibilities:

- maintain repository organization
- inspect links, metadata, naming, and navigation
- identify duplication, conflicts, and orphaned content
- execute repository routines defined by Spark OS
- report structural risks and recommend improvements

Claude is not a co-architect, strategic partner, or independent decision maker.

See [`CLAUDE_ROLE.md`](CLAUDE_ROLE.md).

### Future AI Tools

A future AI tool should receive a durable role document only when:

1. the responsibility is repeatedly needed
2. the responsibility is materially distinct
3. assigning it reduces ambiguity rather than creating overlap
4. Spark OS can retain the process if the tool is replaced

## Role Design Standard

Every durable AI role should define:

- mission
- responsibilities
- authority
- restrictions
- expected outputs
- escalation rules
- success criteria
- evolution process

An AI role is a job description, not a personality prompt.

## No Duplicate Authority

Two AI systems may support the same workflow, but they should not independently own the same decision.

Examples:

- ChatGPT may design repository architecture.
- Claude may inspect whether the repository conforms to it.
- Neither should silently redefine the other's role.

When overlap appears, pause and clarify the responsibility in governance.

## Repository-Owned Routines

Automation routines belong to Spark OS, not to a vendor or model.

A routine should be stored as an explicit repository instruction so another capable tool can execute it later.

Potential future routines include:

- repository health review
- cross-link review
- terminology consistency review
- duplicate-knowledge review
- Canon-to-Academy alignment review
- periodic governance review

No routine is active merely because it appears as an idea. It becomes active when Spark OS defines its scope, frequency, inputs, outputs, and escalation rules.

## Evolution Triggers

An AI role should be reviewed when:

- the same new task is repeatedly assigned
- the tool repeatedly makes the same category of error
- a new durable workflow emerges
- Spark OS architecture changes
- responsibilities begin to overlap
- the tool becomes a hidden dependency
- replacement of the tool would cause knowledge loss

## Escalation

AI must escalate rather than silently resolve when it identifies:

- conflicting canonical sources
- unclear authority
- a proposed change to Philosophy
- a proposed change to a durable standard
- a major architectural trade-off
- an external fact that cannot be verified reliably
- a task outside its assigned authority

## AI Output Standard

AI output is a proposal until accepted into the repository.

The quality standard is not whether the output sounds convincing. It must be:

- structurally appropriate
- internally consistent
- reviewable
- traceable
- aligned with accepted Philosophy and Canon
- clear about uncertainty
- free of invented authority

## Portability Principle

Spark OS must remain usable if ChatGPT, Claude, GitHub, Loveable, or another platform changes or disappears.

Therefore:

- critical knowledge lives in durable formats
- processes are documented in the repository
- role definitions are vendor-conscious but not vendor-dependent
- outputs should be reproducible from accepted sources
