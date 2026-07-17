# ADR-0001: Markdown Is the Canonical Source of Truth

**Status:** Accepted  
**Date:** 2026-07-16  
**Decision owners:** Sheldon Phillips and the Spark OS Knowledge & Learning Architecture function  
**Supersedes:** None  
**Superseded by:** None

## Context

Spark OS will eventually support courses, reference cards, PDFs, mentor guides, AI context, operating procedures, client resources, and software experiences.

If each output is maintained independently, Spark OS will develop conflicting versions of the same knowledge. Vendor-specific formats would also make the system difficult to preserve or migrate.

Spark OS requires a durable, portable, reviewable format that supports version history, internal linking, AI use, and generation of multiple outputs.

## Decision

Markdown files stored in the Spark OS Git repository are the canonical source of truth.

Accepted knowledge, governance, philosophy, and educational source material should be maintained in Markdown.

Derivative outputs should be generated from or explicitly traceable to those sources.

GitHub is the current collaboration and version-control platform, but GitHub itself is not the Canon. The Markdown repository content is the durable knowledge asset.

## Rationale

Markdown is:

- plain text
- human-readable
- machine-readable
- portable
- easy to compare through diffs
- well supported by Git
- suitable for links and metadata
- usable by multiple AI systems
- independent of a single course platform or document editor

This choice separates Spark knowledge from the software used to display it.

## Alternatives Considered

### Google Drive Documents as the Primary Source

Google Drive is accessible and convenient, but document-level editing encourages scattered formats and makes structured reuse, systematic linking, and repository-wide review more difficult.

Google Drive may still hold exports, backups, source attachments, and collaborative working documents.

### Loveable Database as the Primary Source

A database may eventually power the product experience, but making it the only source would bind Spark knowledge to an application implementation.

Loveable should consume or synchronize with the Canon rather than silently redefine it.

### AI Conversation History as the Primary Source

Conversations preserve useful exploration but contain unfinished thinking, contradictions, and unaccepted suggestions.

A conversation is not authoritative until its accepted result is documented in the repository.

## Consequences

### Benefits

- one durable source of truth
- traceable version history
- easier review through diffs
- reusable content
- reduced platform dependence
- clearer AI grounding
- easier migration and backup

### Costs and Trade-offs

- contributors must learn basic Markdown and GitHub concepts
- generated outputs may require build or synchronization workflows
- repository discipline is required
- visually rich artifacts may need separate storage

### Risks

- duplicate knowledge may still emerge if linking and review are neglected
- derivative systems may drift if synchronization is informal
- contributors may treat GitHub as merely storage instead of governance

## Implementation

Sprint 0 establishes:

- the Git repository structure
- README navigation
- contribution rules
- AI governance
- this ADR

Future work should define:

- document metadata standards
- generated-output conventions
- external source and citation handling
- repository review routines
- synchronization with Loveable

## Review Trigger

Reconsider this decision only if Markdown materially prevents Spark OS from preserving, reviewing, reusing, or publishing its knowledge.

A new interface, database, or AI capability alone is not sufficient reason to replace the canonical format.
