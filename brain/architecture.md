# Architecture

## System View

```text
Spark-OS
├── Client and Borrower Domain
├── Mortgage Files
├── Applications
├── Workflow Engine
├── Tasks
├── Documents
├── Underwriting
├── Submissions
├── Communications
├── Compliance and Audit
├── Reporting
├── AI Services
└── Integrations
```

## Architectural Style

Spark-OS should begin as a modular system with explicit domain boundaries.

A modular monolith is the preferred default until scale, deployment isolation, security boundaries, or team ownership justify separate services.

## Major Rules

- Domain logic should not depend directly on vendor APIs.
- Integrations should adapt external systems to Spark concepts.
- Reporting should derive from operational records rather than become a second source of truth.
- Workflow configuration should be data-driven where practical.
- Important transitions should produce events.
- Material decisions should be auditable.
- Access controls should align with roles, responsibilities, and data sensitivity.
- AI features should use explicit context boundaries and permissions.

## Expected Future Structure

```text
/brain
/meta
/adr
/docs
/domain
/modules
/services
/workflows
/integrations
/ui
/api
/tests
```

This structure is directional, not authorization to create empty folders or premature abstractions.
