# Open Questions

Use this file for unresolved architectural questions. Accepted decisions belong in ADRs.

## Q-001 — Canonical Transaction Aggregate

**Question:** Should `Mortgage File` or `Application` be the primary transaction aggregate?

**Why it matters:** This affects lifecycle design, multiple applications, refinances, renewals, submissions, and document relationships.

**Possible approaches:**
- Mortgage File is primary; applications are versioned financing requests.
- Application is primary; operational workflow attaches directly to it.
- A Case/File aggregate coordinates one or more applications.

**Priority:** Critical  
**Decision status:** Open

## Q-002 — Configurable Workflow Scope

**Question:** Which workflow elements must be configurable in the MVP?

**Why it matters:** Excessive configurability increases complexity; insufficient configurability recreates rigid software.

**Possible approaches:**
- Milestones and tasks only
- States, transitions, rules, tasks, and notifications
- Full visual workflow builder

**Priority:** High  
**Decision status:** Open

## Q-003 — Multi-Tenancy

**Question:** Is the initial architecture single-brokerage, multi-branch, or fully multi-tenant?

**Why it matters:** It affects identity, data boundaries, configuration inheritance, integrations, and deployment.

**Priority:** Critical  
**Decision status:** Open

## Q-004 — Document Storage

**Question:** Should Spark store document bytes or initially store references to an external document provider?

**Why it matters:** Security, retention, cost, performance, and compliance are affected.

**Priority:** High  
**Decision status:** Open

## Q-005 — AI Auditability

**Question:** Which AI outputs require preserved inputs, model metadata, recommendations, approvals, and final decisions?

**Why it matters:** Mortgage work includes privacy-sensitive and potentially regulated decisions.

**Priority:** Critical  
**Decision status:** Open

## Q-006 — Integration Priority

**Question:** Which external system is the first authoritative integration target?

**Why it matters:** The answer influences the initial data model and MVP workflow.

**Priority:** High  
**Decision status:** Open
