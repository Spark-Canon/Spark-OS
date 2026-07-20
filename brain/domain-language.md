# Domain Language

This file defines canonical Spark-OS terminology. New terms should not be introduced casually.

## Client

A person or household receiving mortgage services.

Avoid using `client` to mean an employee, partner, lender, or software consumer.

## Borrower

A person whose income, credit, assets, liabilities, or covenant supports a mortgage application.

A client may include one or more borrowers.

## Contact

A person or organization known to the system that is not necessarily a borrower.

## Application

A mortgage financing request being evaluated or processed.

An application is not a person.

## Mortgage File

The operational record that coordinates an application, participants, documents, workflow state, communications, conditions, and decisions.

## Deal

A business-facing term for a mortgage opportunity or transaction. Use carefully; prefer `Mortgage File` in the canonical domain model unless an ADR defines otherwise.

## Workflow

A reusable definition of states, steps, rules, responsibilities, triggers, and permitted transitions.

## Workflow Instance

A workflow applied to a specific record.

## Milestone

A meaningful business state reached by a workflow instance.

A milestone is not merely a visual progress indicator.

## Step

A unit of work or required action inside a workflow.

## Task

An actionable assignment with responsibility, status, and timing.

## Responsibility

The obligation to produce or maintain a defined outcome.

## Owner

The person or system currently accountable for a responsibility.

## Document

A stored file or generated artifact associated with a business record.

## Condition

A requirement that must be satisfied, waived, or otherwise resolved.

## Submission

A structured package sent to a lender or adjudication destination.

## Lender

An institution or lending channel evaluating or funding a mortgage.

## Partner

An external professional or organization participating in the client journey, such as a builder, Realtor, financial advisor, or lawyer.

## Integration

A boundary connecting Spark-OS to an external system.

## Event

A recorded fact that something happened.

## Command

A request to perform an action.

## Decision

A material conclusion with reasoning, authority, and consequences.
