# Spark-OS Constitution

**Project:** Spark-OS  
**Repository:** `Spark-Canon/Spark-OS`  
**Role:** Project bootloader and canonical entry point  
**Status:** Foundational  
**Last updated:** 2026-07-20

## Purpose

This file is the first document that any human or AI collaborator must read before changing Spark-OS.

Spark-OS is intended to become the operating system for a modern mortgage brokerage. It is not merely CRM software. It is an operational platform organized around responsibilities, workflows, institutional knowledge, compliance, and AI-supported execution.

The repository is the project's long-term memory. Conversation history is not the source of truth.

## Resume Commands

The following phrases all mean the same thing:

- `Resume Spark-OS`
- `Open Spark Constitution`
- `Continue Spark Architecture`
- `Work on Spark`

When one of these commands is given, begin the boot sequence below.

## Boot Sequence

1. Read this file.
2. Read `brain/current-state.md`.
3. Read `brain/vision.md`.
4. Read `brain/principles.md`.
5. Read `brain/domain-language.md`.
6. Read `brain/responsibility-map.md`.
7. Read `brain/architecture.md`.
8. Read `brain/roadmap.md`.
9. Read `brain/open-questions.md`.
10. Read all ADRs created or changed since the last recorded session.
11. Continue from the `Next Task` in `brain/current-state.md`.

Do not redesign the project before completing this sequence.

## Source-of-Truth Hierarchy

When documents disagree, use this order:

1. This Constitution
2. Accepted ADRs
3. Domain language
4. Architecture and responsibility map
5. Current state
6. Roadmap
7. Other documentation
8. Conversation history

Conversation history may explain context, but it does not override repository documentation.

## Core Rules

- Architecture precedes implementation.
- Important decisions must be documented.
- Architectural changes require an ADR.
- Domain terms must retain their canonical meanings.
- Every major component must own a clear responsibility.
- Prefer consistency over cleverness.
- Prefer simple, inspectable systems over hidden complexity.
- Do not create duplicate concepts under different names.
- Update `current-state.md` before ending meaningful work.
- Update the architectural journal after significant decisions.
- Never claim a repository change was made unless it was verified.

## Required Session Closeout

Before ending a meaningful Spark-OS work session:

1. Update `brain/current-state.md`.
2. Record decisions in `meta/architectural-journal.md`.
3. Create or update ADRs when architecture changed.
4. Update `brain/open-questions.md`.
5. Report exactly what changed.
6. Record any failed or unverified actions.

## Human and AI Collaboration

AI acts as a senior architectural partner. It should:

- preserve architectural consistency
- identify duplicated concepts
- surface hidden assumptions
- recommend ADRs
- update documentation with architectural changes
- separate facts, decisions, assumptions, and proposals
- avoid undocumented design drift
- avoid treating generated code as authoritative without review

Humans retain final authority over product direction, business rules, compliance interpretation, and accepted architecture.

## Repository Memory Principle

The project must remember itself.

A future collaborator should be able to understand why Spark exists, what it means, how it is structured, what is currently happening, what remains unresolved, and what to do next without relying on a previous chat.
