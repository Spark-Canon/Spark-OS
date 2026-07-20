# Responsibility Map

This is the initial responsibility map. It will evolve through ADRs.

## Client and Borrower Domain

Owns:

- people and household relationships
- consent and communication preferences
- borrower identity
- borrower-provided information
- declared financial position

## Mortgage File

Owns:

- the operational record for one financing journey
- participants and roles
- current lifecycle state
- links to applications, documents, conditions, submissions, and communications

## Application

Owns:

- requested financing
- property and loan details
- borrower qualification inputs
- product and strategy assumptions
- application versions

## Workflow Engine

Owns:

- workflow definitions
- workflow instances
- milestones
- steps
- transitions
- triggers
- assignments
- deadlines
- exception paths

## Task System

Owns:

- actionable work
- assignee
- due date
- status
- completion evidence
- relationship to the originating responsibility or workflow

## Document System

Owns:

- document metadata
- storage references
- document categories
- versions
- request status
- access controls
- retention rules

## Underwriting

Owns:

- qualification calculations
- policy interpretations
- exceptions
- conditions
- supporting evidence
- underwriting decisions

## Submission

Owns:

- lender-facing packages
- submission versions
- destinations
- responses
- lender conditions
- submission status

## Communication

Owns:

- messages
- communication history
- templates
- channels
- delivery state
- consent-aware outreach

## Compliance and Audit

Owns:

- consent evidence
- access history
- material decision records
- retention
- privacy controls
- compliance checkpoints

## Reporting

Owns:

- derived metrics
- operational views
- performance analysis
- traceability to source records

Reporting does not own transactional truth.

## AI Services

Owns:

- bounded assistance
- recommendations
- classification
- summarization
- drafting
- reasoning traces appropriate for audit

AI does not own final regulated or material business decisions.

## Integrations

Owns:

- adapters to external systems
- synchronization rules
- external identifiers
- retries and error handling
- boundary-specific mappings
