# Design Principles

## 1. Responsibility Over Ownership

Every module, workflow, service, task, and record must exist because it owns a defined responsibility.

## 2. Causes Over Outcomes

Spark manages controllable causes. Metrics and results are outputs, not substitutes for process design.

## 3. Workflows Over Departments

The system should model how work moves, not merely mirror an organizational chart.

## 4. Architecture Before Implementation

Implementation should follow agreed responsibilities, domain language, interfaces, and decisions.

## 5. Documentation Is Executable Knowledge

Documentation should guide real work, design, reviews, onboarding, and AI behavior.

## 6. AI Augments Humans

AI may analyze, recommend, draft, classify, and automate bounded work. Humans retain authority over material decisions.

## 7. Canonical Language

One business concept should have one canonical name.

## 8. Explicit State

Important workflow state, decisions, exceptions, and responsibility changes should be inspectable.

## 9. Simplicity Before Optimization

Prefer the smallest coherent design that preserves future flexibility.

## 10. Privacy and Compliance by Design

Access, retention, consent, auditability, and data minimization are architectural concerns.

## 11. Replaceable Integrations

External services should be connected through clear boundaries so they can be replaced without redesigning the domain.

## 12. No Undocumented Architectural Drift

Meaningful architectural change must update documentation and, when appropriate, an ADR.
