# ADR-002: Responsibility-First Architecture

**Status:** Accepted  
**Date:** 2026-07-20

## Context

Organizing software around screens, departments, or current vendors produces fragile boundaries.

## Decision

Define modules, services, workflows, and permissions around explicit responsibilities.

## Consequences

- Each component must state what it owns.
- Duplicate responsibility is an architectural warning.
- Responsibility mapping precedes detailed implementation.
