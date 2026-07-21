# Design History Workflow

**Status:** Active
**Authority:** Repository governance

## Purpose

This workflow defines when historical documentation should be created and how it relates to canonical Spark OS documents.

Design History preserves enduring architectural reasoning while keeping the repository concise, navigable, and free of competing sources of truth.

## Authority Order

1. Current repository documents describe the accepted state.
2. ADRs record accepted architectural decisions.
3. Design History explains how and why that state emerged.

Design History has no authority to amend current documents or ADRs. Whenever a conflict exists, current repository documents win.

## Document Types

### Conversation Transcript

Preserves a complete discussion when the original exchange has exceptional historical value.

- **Authority:** None
- **Creation:** Optional
- **Location:** `99-archive/design-history/transcripts/`
- **Standard:** Preserve the discussion faithfully, identify its date and participants when appropriate, label it non-authoritative, and remove secrets or sensitive personal information before committing it.

### Conversation Summary

Captures enduring architectural insights from a conversation without reproducing the complete exchange.

- **Authority:** Historical only
- **Creation:** Only when a conversation materially shaped, challenged, or clarified long-term Spark OS architecture
- **Location:** `99-archive/design-history/conversation-summaries/`
- **Standard:** Use `99-archive/design-history/SUMMARY-TEMPLATE.md` and link accepted outcomes to current repository documents.

### Major Milestone

Documents completion of an important architectural phase or permanent change in direction.

- **Authority:** Historical only
- **Creation:** When a material architectural milestone is accepted and complete
- **Location:** `99-archive/design-history/major-milestones/`
- **Examples:** Spark Brain v2, Repository Memory, Deterministic Boot, Repository Integrity, or an AI Governance revision

### Architectural Evolution

Maintains the curated chronological narrative of how Spark OS evolved over time.

- **Authority:** Historical only
- **Creation:** One living narrative, updated incrementally
- **Location:** `99-archive/design-history/evolution/README.md`
- **Update trigger:** A milestone changes the long-term direction or interpretation of the architecture

### Retired Architecture

Explains a superseded design, why it was replaced, and which current documents define its replacement.

- **Authority:** Historical only
- **Creation:** When a meaningful architecture is formally retired or superseded
- **Location:** `99-archive/design-history/retired-architectures/`
- **Preservation:** Never delete a valid retired-architecture record merely because the design is obsolete

### Architectural Decision Record

Records an accepted architectural decision.

- **Authority:** Canonical
- **Creation:** According to the ADR criteria in [`../CONTRIBUTING.md`](../CONTRIBUTING.md)
- **Location:** [`architecture-decisions/`](architecture-decisions/)

### Repository Documents

Describe Spark OS as it currently exists.

- **Authority:** Canonical within their assigned repository area
- **Update trigger:** Whenever accepted architecture changes

## End-of-Session Review

Before concluding significant architectural work, evaluate whether enduring value requires updates to:

1. affected authoritative repository documents
2. applicable ADRs
3. Spark Brain operating documents when operating behavior changed
4. `brain/current-state.md`
5. `brain/session.md`
6. the Architectural Evolution narrative
7. a Major Milestone record
8. a qualifying Conversation Summary
9. a Retired Architecture record
10. an optional Conversation Transcript

Create only the records that add enduring value. Routine implementation work does not require Design History. Prefer fewer, higher-quality historical records over numerous low-value summaries.

## Required Sequence

1. Update or create authoritative repository documents.
2. Create or update ADRs when required.
3. Verify the accepted implementation.
4. Update Current State and Session Continuity.
5. Add only the Design History records justified by the completed work.
6. Cross-link history to authoritative sources, pull requests, full commit SHAs, and related history.

Historical documentation cannot complete or accept architecture by itself.

## Spark Brain Boundary

Design History is not Quick Resume or operational context. Consult it only for historical investigation, architectural evolution, retired approaches, long-term onboarding, ADR preparation, or apparent contradictions. Confirm every current claim against active repository documents before acting.
