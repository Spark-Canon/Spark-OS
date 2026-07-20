# Architectural Journal

This journal records significant architectural thinking chronologically. Accepted decisions should also have ADRs.

---

## 2026-07-20 — Repository-Backed Project Memory

### Problem

Chat conversation history and connector sessions are not reliable long-term project memory.

### Decision

Create a Spark Brain inside the repository, with a Constitution as the canonical bootloader and `current-state.md` as the resume point.

### Reasoning

Any future human or AI collaborator should be able to recover project context from the repository itself.

### Consequences

- Repository documentation becomes mandatory.
- Meaningful sessions require closeout updates.
- Conversation history becomes secondary.
- The project gains a stable resume command and reading sequence.

### Future Follow-up

Install the prepared `/brain`, `/meta`, and `/adr` files in GitHub and verify them.

---

## 2026-07-20 — Responsibility-First Architecture

### Problem

Software organized primarily around screens, departments, or vendor tools tends to duplicate concepts and obscure accountability.

### Decision

Model Spark-OS around explicit business and system responsibilities.

### Reasoning

Responsibility boundaries provide a durable basis for domain modules, workflows, permissions, tests, and AI context.

### Consequences

Every major component should state what it owns and what it does not own.

### Future Follow-up

Refine the responsibility map during domain modeling.

---

## 2026-07-20 — Spark Brain Installation Completed

### Problem

The prepared repository-memory package existed outside the repository, while only two earlier `meta/` documents had been committed. Continuing without reconciliation risked duplicate canonical documents and false assumptions about prior writes.

### Decision

Install the prepared `/brain`, `/meta`, and `/adr` structure on `main`. Preserve one canonical source for principles in `brain/principles.md`, use `meta/design-principles.md` only as a compatibility pointer, and update the existing AI working agreement in place.

### Verification

- Inspected commits `043a789ca6a397467bfae88a67af5010d45883c4` and `e4f50eb20acccc63120b8f91c79beeb0449fbea9`.
- Confirmed the commits created `meta/ai-working-agreement.md` and `meta/design-principles.md`, respectively.
- Created all missing package files.
- Updated both existing files using their current blob SHAs.
- Fetched every target file from `main` after writing.

### Consequences

- The repository now contains its own boot sequence, current resume point, domain vocabulary, architecture, roadmap, open questions, working agreement, journal, and initial ADRs.
- Conversation history is no longer required to recover the project state.
- The next architectural task is to resolve the canonical transaction aggregate.
