---
name: training-research
description: Conduct the bounded, public-source Pilot 001 instructional-design research task about the effects, limitations, and conditions of worked examples for novice learners in professional or comparable education. Use only when explicitly invoked as $training-research for the fixed Pilot 001 question; create one new non-authoritative Workbench brief and do not perform domain, mortgage, legal, regulatory, lender, insurer, product, underwriting, qualification, or operational research.
---

# Training Research Pilot 001

Perform only the fixed Pilot 001 instructional-design research task.

## Required invocation

Proceed only when the caller explicitly invokes `$training-research`.

Reject implicit, inferred, or adjacent use.

Require the invocation task to receive or confirm:

- `repository`: `Spark-Canon/Spark-OS`
- `approved_base_commit`: a caller-approved full commit SHA

Read `references/research-brief-standard.md` completely and validate the invocation against the exact fixed Pilot 001 inputs defined there.

Reject:

- any altered lane, question, topic slug, intended use, scope, exclusions, jurisdiction direction, source boundary, or source-quality direction;
- `domain` or `mixed` research lanes;
- requests that assume worked examples improve learning;
- mortgage-domain, legal, regulatory, lender, insurer, product, underwriting, qualification, or operational research;
- requests to create or revise course content;
- requests to make Canon, Academy, Philosophy, Governance, or architectural decisions.

Domain research is outside Pilot 001 and requires separate future review and authorization.

## Repository-safety preflight

Before conducting research:

1. Read `CONTRIBUTING.md` completely.
2. Read `02-governance/ai-governance/AI_GOVERNANCE.md` completely.
3. Identify the Git repository root.
4. Verify that the repository is `Spark-Canon/Spark-OS`.
5. Inspect the current branch, HEAD, and working-tree status.
6. Verify that HEAD exactly matches `approved_base_commit`.
7. Verify that the current branch is a dedicated pilot branch and is not `main`.
8. Verify that HEAD is not detached.
9. Verify that the worktree contains no unrelated changes.

If any check fails or cannot be established, stop without conducting research or writing a brief.

Do not:

- fetch;
- pull;
- create or switch branches;
- create a worktree;
- commit;
- push;
- open a pull request;
- repair repository state.

Treat repository preparation and later publication as separate tasks.

Do not put the repository name or approved base commit in the research brief unless explicitly required for the pilot audit. They are execution provenance, not research evidence.

## Required standard

Read `references/research-brief-standard.md` completely before beginning research.

Follow that file as the complete operational standard for the fixed research inputs, evidence, sources, metadata, citations, dates, uncertainty, contrary evidence, copyright, privacy, access limitations, authority boundaries, and brief structure.

Do not begin research if the standard cannot be read completely.

## Execution

1. Confirm explicit invocation, `repository`, and `approved_base_commit`.
2. Complete the repository-safety preflight.
3. Read the research-brief standard completely.
4. Validate the invocation against every fixed Pilot 001 input defined in the standard.
5. Confirm that the request contains only the instructional-design lane.
6. Reject any prohibited domain or downstream request.
7. Check whether permitted public research access is available.
8. Record all access and verification limitations accurately.
9. Research the fixed question without presuming a positive effect.
10. Allow for positive, null, adverse, weak, context-dependent, or conflicting findings.
11. Determine the research date using the `America/Edmonton` timezone.
12. Inspect `00-workbench/training-research/` for filename collisions.
13. Select the first unused filename:

    `YYYY-MM-DD-worked-examples-novice-professional-learning-01.md`

    Increment the two-digit suffix when necessary.
14. Create exactly one new brief following the required standard.
15. Never overwrite or edit an existing file.
16. Report the created path and the brief’s `research_status`.
17. Stop.

## Write boundary

Write only the single new brief inside:

`00-workbench/training-research/`

Do not edit:

- this skill;
- `agents/openai.yaml`;
- `references/research-brief-standard.md`;
- `00-workbench/training-research/README.md`;
- an existing research brief;
- any other repository file or directory.

Do not create source downloads, scripts, templates, indexes, assets, archives, topic folders, or additional files.

A correctly handled `limited` or `failed` research result may still constitute a successful skill pilot. Never fabricate evidence to obtain a completed result.
