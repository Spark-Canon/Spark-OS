# Repository Health

Repository health is an architectural guarantee, not a cosmetic check.

## Validation Command

From the repository root, run:

```bash
python tools/validate_repository.py
```

The same validator runs in GitHub Actions through `.github/workflows/repository-integrity.yml`.

## Required Checks

Validation must fail when any of the following is detected:

- a required file is missing
- a required heading is missing
- a relative Markdown link is broken
- a Markdown heading anchor does not resolve to an existing heading
- a boot path does not resolve
- the same path appears twice in one boot sequence
- an authority root is missing or duplicated
- the Repository Map and manifest.yaml disagree on declared authority roots
- a retired Brain v1 authority path still exists
- an ADR filename does not follow the canonical numbering pattern
- two ADRs use the same number
- the accepted ADR sequence contains a numbering gap
- a non-template active document contains unresolved placeholders
- current-state or session navigation refers to a missing path
- the manifest cannot be parsed

## Manifest Format Contract

`brain/manifest.yaml` uses a `.yaml` extension but is parsed exclusively through Python's `json.loads()` (see `tools/validate_repository.py`). Its actual syntax contract is JSON, not general YAML: comments, anchors, and other non-JSON YAML constructs are not supported and will fail parsing.

This parsing contract is now documented here. `brain/manifest.yaml` remains the accepted current path; no rename or format migration has occurred. A possible future filename or format migration remains an open question, and any such migration of this canonical Brain path would require a separate ADR under the Brain Constitution's Change Discipline.

## Authority Integrity

The validator enforces these canonical roots:

- Philosophy: `01-philosophy`
- Governance: `02-governance`
- ADRs: `02-governance/architecture-decisions`
- Canon: `03-canon`
- Academy: `04-academy`
- Brain: `brain`

The validator cannot prove that prose is philosophically correct. Human review remains required for semantic conflicts, misleading summaries, and disguised duplication.

## Current-State Accuracy

Machine validation confirms that required state fields and referenced paths exist. Reviewers must additionally confirm that status claims match Git history and current repository contents.

## Failure Policy

A failed integrity check blocks architectural completion.

Do not mark a migration or structural change complete until:

1. the validator passes
2. modified files have been re-read
3. authority boundaries have been reviewed
4. current state matches repository reality
5. unresolved semantic concerns are recorded

## Extending Validation

Add checks only when they protect an observed architectural requirement. New checks should be deterministic, portable, and documented in the manifest or validator.

Heading-anchor validation approximates GitHub's anchor-slug algorithm and is proportionate for the repository's current content, but does not guarantee full fidelity for every Unicode edge case (for example, combining diacritics). Treat an anchor failure as a strong signal, and confirm manually before trusting the check against a heading with unusual non-ASCII characters.