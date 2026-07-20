# ADR-001: AI Architectural Memory

**Status:** Accepted  
**Date:** 2026-07-20

## Context

AI conversations are useful working spaces but are not dependable long-term memory.

## Decision

Store project context, decisions, terminology, architecture, current state, and unresolved questions inside the repository.

## Consequences

- AI must reload context from repository documents.
- Conversation summaries may assist but do not override repository truth.
- Meaningful work sessions must update the resume point.
