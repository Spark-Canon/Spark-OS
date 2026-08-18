# Coordinated Installation Package Workflow

**Status:** Non-authoritative Workbench process candidate
**Authority:** None
**Current effect:** Does not authorize installation, invocation, merge, or repository change
**Likely owner if accepted:** Existing repository Governance or contribution workflow
**Purpose:** Capture the repeated, vendor-portable process used to install approved Spark OS artifacts faithfully and verify the result independently.

## Why This Candidate Exists

Spark OS has repeatedly used the same coordinated installation pattern for foundational Philosophy, supporting closeouts, and the Training Research skill:

1. distill an exact candidate;
2. audit it independently;
3. obtain Sheldon Phillips' explicit approval;
4. install it mechanically on a dedicated branch;
5. inspect the actual pull-request diff independently;
6. merge only after verification;
7. verify merged `main`; and
8. retire the completed branch and worktree safely.

This is now a durable routine rather than an isolated technique. AI Governance requires repository-owned routines to be explicit and portable so Spark OS does not depend on one conversation, model, operator, or person's memory.

The candidate records the observed process for later Challenge and Audit. It does not presume whether the final instruction belongs in `CONTRIBUTING.md`, AI Governance, another existing Governance document, or no separate document after consolidation.

## Routine Contract

- **Trigger:** Sheldon explicitly approves an exact artifact and controlling fingerprint for coordinated installation.
- **Frequency:** Event-driven only; once per approved artifact or separately approved bounded correction. It is not a scheduled routine.
- **Inputs:** Approved artifact, fingerprints, target authority and paths, authorized transformations, required base, validation requirements, and explicit prohibitions.
- **Outputs:** Installation commit, draft pull request, installation report, independent audit disposition, merge verification, retirement result, and proportionate continuity record.
- **Decision owner:** Sheldon Phillips retains approval and merge authority.
- **Execution:** Any capable, authorized repository tool may execute the bounded package. The process must not depend on ChatGPT, Claude, Codex, or another named vendor.
- **Independent verification:** A separate task or context verifies the actual implementation against the approved package.
- **Escalation:** Stop on source mismatch, ambiguity, stale base, unrelated changes, validation failure, authority conflict, sensitive information, or deletion risk.

## Operating Principles

- Human approval and repository installation are separate events.
- Approval identifies the exact artifact; it does not modify files or authorize unrelated work.
- Installation implements the approved artifact without redesign.
- The implementation task and independent audit task remain role-separated.
- Repository presence does not establish authority unless installation places accepted content in its proper authority location.
- Every package is bounded to named files, transformations, validation, and prohibitions.
- Current `main`, not a historical or dirty checkout, supplies the installation base.
- GitHub preserves implementation provenance; Spark OS should not commit a duplicate installation packet by default.
- Post-merge verification and branch retirement are part of closeout, not optional housekeeping.
- A failed or limited installation report must remain honest and must not be converted into a claimed pass.

## Package Format

An installation package should contain the following fields. `Not applicable` or `None` should be used when a field genuinely does not apply.

```markdown
# Coordinated Installation Package — <Artifact Name>

**Package status:** Approved for bounded installation
**Artifact ID:** <stable identifier or descriptive artifact name>
**Artifact version:** <version or Not applicable>
**Approved by:** Sheldon Phillips
**Approval date:** <YYYY-MM-DD>
**Authority after installation:** <target authority and status>

## Approved Source

- Source location: <durable source or exact supplied artifact>
- Source SHA-256: <single-file fingerprint, if applicable>
- Per-file SHA-256: <path and hash for each file, if applicable>
- Deterministic manifest SHA-256: <multi-file package fingerprint, if applicable>
- Fingerprint method: <encoding, line endings, path ordering, manifest construction>

## Installation Base

- Repository: `Spark-Canon/Spark-OS`
- Required base: <full current-main commit SHA>
- Required checkout: fresh, clean, dedicated branch/worktree

## Authorized Scope

- Target files: <complete repository-relative list>
- Authorized transformations: <complete list>
- Required supporting updates: <complete list or None>

## Prohibited Scope

- No substantive reinterpretation or improvement.
- No unrelated files or authority areas.
- No merge.
- No branch or worktree retirement before post-merge verification.
- No downstream invocation, research, publication, or operational use unless separately authorized.

## Validation Requirements

- Source fidelity after reversing only authorized transformations.
- Exact changed-file scope.
- Required structure, order, links, anchors, and statuses.
- Repository integrity validation.
- Existing validator tests.
- `git diff --check`.
- Credential, private-locator, sensitive-information, and unintended-path review.
- Remote/local head match.
- GitHub Actions result.

## Required Installation Report

- Repository and clean checkout identity.
- Base, branch, installation commit, and draft PR.
- Complete changed-file list.
- Approved-source and installed fingerprints.
- Exact authorized transformations applied.
- Validation results.
- Limitations and deviations.
- Confirmation that prohibited actions did not occur.
```

## Fingerprint Standard

### Single-file artifact

Record the SHA-256 of the exact approved source bytes. If installation requires authorized acceptance transformations, also record the canonical installed Git-blob SHA-256 and explain why it differs.

### Multi-file artifact

Record:

- one SHA-256 per approved file;
- exact repository-relative forward-slash paths;
- the stated encoding and line-ending convention;
- the exact path-ordering rule; and
- one deterministic manifest SHA-256.

The manifest algorithm must be written explicitly. Terms such as `sorted normally` or `ordinally` are insufficient when case or locale could change ordering.

### Canonical versus working-copy hashes

Canonical Git-blob or explicitly normalized source fingerprints should control. CRLF, LF, or mixed-line-ending working-copy fingerprints may be recorded for diagnosis but must not be presented as stable repository fingerprints.

## Coordinated Process

### 1. Candidate preparation

- Complete the applicable Explore → Challenge → Audit → Close → Distill work.
- Produce the exact proposed artifact or exact file bodies.
- Keep the candidate non-authoritative.
- Identify intended destination, authority effect, and downstream implications.

### 2. Artifact audit and fingerprinting

- Audit the complete candidate independently.
- Resolve defects before approval.
- Materialize exact bytes outside the authoritative repository when necessary.
- Calculate the controlling single-file or multi-file fingerprints.
- Confirm approval readiness without installing anything.

### 3. Human approval

Sheldon approves the named artifact and controlling fingerprint explicitly.

Approval should state:

> I, Sheldon Phillips, approve <Artifact Name> at <controlling SHA-256> for coordinated installation into <destination>.

Any additional authority—such as skill invocation, research, publication, operational use, or merge—must be stated separately. Silence does not authorize it.

### 4. Installation preparation

- Verify GitHub `main` and record its full SHA.
- Create a fresh, clean, dedicated worktree and branch.
- Do not use a historical, dirty, detached, or unrelated checkout.
- Confirm repository identity, branch, HEAD, status, and package source.
- Stop if the approved base has changed in a way that could affect installation.

### 5. Mechanical installation

- Apply only the named files and authorized transformations.
- Preserve exact approved wording and ordering where required.
- Update navigation, Brain continuity, or related references only when expressly authorized.
- Do not improve, reinterpret, expand, or silently repair the artifact.

### 6. Local validation and publication

- Run every package validation requirement.
- Stage only the authorized paths.
- Commit with an intent-based message.
- Push the dedicated branch.
- Open a draft pull request.
- Keep the pull request unmerged pending independent audit.

### 7. Independent installation audit

The audit task should independently verify:

- base and head identities;
- exact scope and diff;
- source and installed fingerprints;
- authorized transformations;
- authority boundaries;
- validation results and GitHub Actions;
- prohibited-action compliance; and
- whether any correction is required.

The audit may return `pass`, `bounded correction required`, or `blocked`. It does not merge the pull request or redesign the approved artifact.

### 8. Human merge

After a passing audit, Sheldon marks the draft ready and merges it through the repository's normal method.

### 9. Post-merge verification

Verify:

- pull-request merge status and merge commit;
- current `main` relationship to the merge;
- merge-tree equality with the accepted PR head, or explain any legitimate difference;
- exact merged scope;
- installed canonical fingerprints;
- successful post-merge GitHub Actions;
- current continuity and navigation; and
- feature-branch ancestry and retirement readiness.

### 10. Safe retirement

Before deletion, confirm:

- the feature tip is fully contained in current `main`;
- the dedicated worktree is clean;
- repository identity, branch, HEAD, and resolved path are exact;
- no unique work would be discarded; and
- Sheldon has authorized retirement when required by the operating context.

Delete only the verified feature branch and dedicated worktree. Preserve GitHub PR, commit, Actions, fingerprints, and audit history.

### 11. Closeout

- Record the final outcome in the audit trail.
- Update Brain continuity only when the active repository continuation point changed.
- Determine proportionately whether Design History warrants a milestone, summary, evolution entry, retired-architecture record, or nothing.
- Record any future invocation or drift-review requirement separately; installation alone does not authorize use.

## GitHub Location and Naming

### Repository

All coordinated installations target:

`Spark-Canon/Spark-OS`

### Branch

Preferred vendor-neutral format:

`agent/install-<artifact-slug>`

Use a distinct bounded closeout branch only when a verified merge leaves necessary continuity or status corrections:

`agent/close-<artifact-slug>`

Do not reuse a retired branch name when doing so could confuse provenance.

### Pull request

Open against `main` as a draft.

Preferred title:

`Install approved <Artifact Name>`

The PR body should contain the installation report rather than committing a duplicate package file. A separate repository package record should be created only if later evidence demonstrates retrieval or governance value beyond GitHub and the audit trail.

### Artifact destinations

The installed artifact belongs in its assigned authority location—Philosophy, Governance, Canon, Academy, Brain, a repository skill location, or Workbench—not in a generic installation-package directory.

## Audit Trail Format

Use the next unused sequential audit identifier. `S-####` is a placeholder for the sequence number; existing entries should not be renumbered or zero-padded retroactively.

Heading format:

```markdown
### S-#### — YYYY-MM-DD — <Concise event title>
```

Recommended installation lifecycle titles:

```markdown
### S-#### — YYYY-MM-DD — Artifact audit of <Artifact Name>
### S-#### — YYYY-MM-DD — Materialization and fingerprint audit of <Artifact Name>
### S-#### — YYYY-MM-DD — Human approval of <Artifact Name>
### S-#### — YYYY-MM-DD — Independent audit of <Artifact Name> installation PR #<number>
### S-#### — YYYY-MM-DD — Bounded re-audit of corrected <Artifact Name> installation PR #<number>
### S-#### — YYYY-MM-DD — Post-merge verification of <Artifact Name> installation PR #<number>
### S-#### — YYYY-MM-DD — PR #<number> branch and worktree retirement
```

Each entry should include only the fields material to that event, normally:

- **Intake** or **Human direction**;
- **Authority/status boundary**;
- **Source or fingerprint result**;
- **Scope**;
- **Verification/findings**;
- **Limitations/deviations**;
- **Disposition**; and
- the next intake when another step remains.

Do not create empty ceremonial entries. A bounded correction and re-audit receive separate entries only when preserving the defect and its verified resolution improves traceability.

## Escalation and Stop Conditions

Stop and return to the appropriate authority when:

- the approved source or fingerprint cannot be reproduced;
- current `main` changed materially after package preparation;
- authorized transformations are incomplete or ambiguous;
- implementation requires substantive judgment;
- unrelated changes are present;
- a target authority or repository owner is unclear;
- validation fails;
- sensitive information would enter the repository;
- the installed artifact would create an unapproved downstream action; or
- branch/worktree deletion could discard unique work.

## Questions for Challenge and Audit

1. Should this routine be integrated into `CONTRIBUTING.md`, AI Governance, or another existing Governance document?
2. Is the package format proportionate for both single-file and multi-file artifacts?
3. Which steps may be compressed for low-risk non-authoritative installations without weakening traceability?
4. Should branch retirement always require explicit human confirmation, or may a verified routine retire automatically?
5. Does GitHub plus the audit trail preserve sufficient provenance without a permanent package directory?
6. Should a reusable installation-package template be canonical, or is a structured instruction sufficient?
7. Which validation checks are universal, and which must remain artifact-specific?

## Candidate Disposition

**Explore and Challenge before acceptance.** The repeated process is established strongly enough to require documentation, but its final owner, compression level, and degree of standardization still require Governance Fit review. Until accepted, this file is reference material only and cannot authorize or control an installation.
