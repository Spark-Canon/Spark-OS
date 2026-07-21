# Resume Spark OS

Use this workflow whenever a human or AI collaborator continues repository work after context loss or a session boundary.

## 1. Select a Boot Mode

- Use **Quick Resume** for ordinary continuation with no expected architecture or governance change.
- Use **Full Architectural Boot** before changing authority, structure, governance, Philosophy boundaries, Canon boundaries, AI roles, or architecture.

Follow the exact sequence in [`boot-sequence.md`](boot-sequence.md).

## 2. Establish Repository Reality

Before proposing work:

1. Confirm the repository and branch.
2. Read [`current-state.md`](current-state.md).
3. Read [`session.md`](session.md).
4. Inspect commits after the recorded verified commit when available.
5. Confirm that every path named by the Current Priority and Next Task exists.
6. Check whether relevant ADRs were created, superseded, or changed.
7. Review the latest repository-integrity result.

Git history and current file contents outrank stale session prose.

## 3. State the Continuation Point

Briefly identify:

- the current phase
- the current milestone
- the last completed work
- the next task
- known blockers
- the authority that governs the intended work

Do not continue from a missing, retired, or contradictory reference.

## 4. Work Within Authority

- Follow links to the canonical source.
- Keep proposals in the Workbench until accepted.
- Use the canonical ADR directory for architectural decisions.
- Do not introduce a second source of truth.
- Do not expand Brain into business documentation.

## 5. Verify Before Closeout

After meaningful work:

1. Fetch and read every modified file.
2. Check links and authority boundaries.
3. Run the repository validator.
4. Update `current-state.md` and `session.md`.
5. Report failed or unverified actions.

## Recovery Rule

When the resume trail is inconsistent, stop normal work and perform a Full Architectural Boot plus repository integrity validation. Repair the memory system before relying on its Next Task.