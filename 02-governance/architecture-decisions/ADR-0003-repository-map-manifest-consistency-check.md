# ADR-0003: Enforce Repository Map and Manifest Consistency in the Validator

**Status:** Accepted
**Date:** 2026-07-22
**Decision owners:** Sheldon Phillips
**Supersedes:** None
**Superseded by:** None

## Context

`README.md` and `brain/repository-map.md` both state that if `brain/repository-map.md` and `brain/manifest.yaml` disagree about authority, "validation must fail." `brain/boot-sequence.md` independently lists "the manifest and repository map disagree" as one of the documented Failure Behavior conditions for Full Architectural Boot.

Until now, `tools/validate_repository.py` did not implement this comparison. `validate_authority()` checked `manifest.yaml` against the filesystem, but nothing checked `manifest.yaml` against `brain/repository-map.md`. The documented guarantee existed in prose only; the two files could silently diverge and no automated check would detect it.

## Decision

`tools/validate_repository.py` now includes `validate_map_manifest_consistency()`, which:

1. Parses the authority table in `brain/repository-map.md` — specifically, the Markdown table rows under the "Repository Map" heading that pair an area name with a canonical-location link — and extracts each declared canonical path.
2. Normalizes those paths against the manifest's own relative-path convention (stripping the `../` prefix used because `repository-map.md` lives inside `brain/`, and resolving `./` to `brain`).
3. Compares the resulting set of paths against the set of values in `manifest.yaml`'s `authority` map.
4. Fails validation if either side declares a canonical path the other does not.

This makes the previously documented guarantee an enforced one.

## Rationale

The Repository Map's authority table was chosen as the comparison source because it is the repository's existing human-readable counterpart to the manifest — `README.md` already describes `manifest.yaml` as "the machine-readable form of this map." Comparing against it, rather than against free-form prose elsewhere in the repository, keeps the check anchored to the one document that is explicitly positioned as the manifest's human-readable equivalent.

## Alternatives Considered

### Do Nothing (Leave the Guarantee Undocumented in Code)

Leaves a real gap between what the repository claims about itself and what is actually verified. Rejected because it allows exactly the kind of silent authority drift the numbered repository architecture and Spark Brain v2 (ADR-0002) exist to prevent.

### Parse All of Repository Map's Prose

A more ambitious check could attempt to interpret the "Authority Rules" numbered list and other narrative text in `brain/repository-map.md`, not just the table. Rejected for this decision: prose interpretation is not deterministic, would require guessing at intent, and risks false failures whenever the wording is edited without changing meaning. The table is the only part of the document that is already structured data.

## Consequences

### Benefits

- The documented map/manifest agreement guarantee is now mechanically enforced, not aspirational.
- Divergence is caught at PR time via the existing `repository-integrity.yml` workflow, before it reaches `main`.

### Costs and Trade-offs

- Any future edit to the Repository Map's authority table or to `manifest.yaml`'s `authority` map must keep both in agreement, or validation fails. This is a deliberate constraint, not a defect.
- The check depends on the Repository Map table keeping its current Markdown structure (a pipe table with a Markdown link in the second column). A structural rewrite of that table would require updating the parser alongside it.

### Risks

- The check is intentionally narrow: it confirms the same **set of canonical paths** is declared in both documents. It does not, and cannot, confirm that the prose descriptions in the table's "Authority" column, or elsewhere in either document, are semantically accurate. It validates structural agreement, not semantic correctness — consistent with the existing limitation recorded in `brain/health.md`: "The validator cannot prove that prose is philosophically correct." Human review remains required for that.

## Implementation

- Add `validate_map_manifest_consistency()`, `parse_repository_map_targets()`, and `normalize_map_target()` to `tools/validate_repository.py`.
- Call the new check from `main()`, alongside the other manifest-dependent checks.
- Add `brain/health.md` Required Checks entry: "the Repository Map and manifest.yaml disagree on declared authority roots."
- Add fixture-based tests in `tests/test_validate_repository.py` covering agreement, disagreement, and a missing Repository Map file.

## Review Trigger

Reconsider this decision if:

- the Repository Map's authority table changes to a structure the parser cannot reliably read, producing false failures;
- an authority root needs to be represented with more than a single canonical path, which the current set-based comparison cannot express;
- the manifest or the Repository Map is retired or replaced as the authority representation for Spark Brain.
