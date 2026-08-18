# Course Prototype 001 — Preservation Record

**Artifact ID:** `COURSE-PROTOTYPE-001`
**Status:** Exploratory, non-authoritative Workbench prototype. Not Canon, not accepted Academy content, not approved for operational, client, compliance, licensing, or training reliance.
**Intended destination:** Possible future `04-academy/` content, *only* after review, revision, sourcing against Canon, and explicit acceptance. Placement in this directory does not constitute progress toward that destination by itself.

This preservation does not approve, install, or promote this prototype. It exists so multiple review platforms can examine an identical, frozen revision without needing to reconstruct context or trust an informal hand-off.

## Authoring

- **Platform:** Claude (Claude Code / Anthropic), single continuous conversation.
- **Dates:** Originally authored 2026-07-27. Revised 2026-07-28 to add the 12-item multiple-choice Knowledge Check.
- **Base commit used for preservation:** `37fcc16790c88606934e0a4616ae83eaee2f53b6` (`origin/main`, "Merge pull request #10 from Spark-Canon/agent/close-principles-installation", 2026-07-27).

## Philosophy source revision used during authoring

**Verified:** `01-philosophy/manifesto.md`, `values.md`, `principles.md`, `mental-models.md`, `glossary.md`, and `CONTRIBUTING.md` were read from a clone of this same repository at commit `37fcc16790c88606934e0a4616ae83eaee2f53b6` — the identical commit used as this preservation's base. That clone was pulled and confirmed at this SHA at the time those files were read, and confirmed unchanged (`git pull --ff-only` → already up to date at this SHA) at multiple later checkpoints in the same authoring session, including immediately before this preservation task began. This is a verified match, not an inference.

## Canon assumption

**Assumed and confirmed:** `03-canon/` contained only its scope-defining `README.md` and no domain content at commit `37fcc16790c88606934e0a4616ae83eaee2f53b6`. Every numeric or regulatory mortgage claim in this prototype is therefore either a bracketed placeholder or an explicitly labeled prototype assumption — see `prototype-course.md`'s own Source Map section. Nothing here should be read as sourced from Canon, because none currently exists for this domain.

## Files in this review packet

- [`prototype-course.md`](prototype-course.md) — the prototype itself (brief, outcomes, Learn, Apply, Feedback, Assessment, 12-item Knowledge Check, facilitator notes, source map).
- [`prototype-findings.md`](prototype-findings.md) — process findings recorded during authoring (missing Canon sources, terminology problems, simplification risks, assessment difficulties, and more, each tagged with a likely repository owner).
- [`author-self-review.md`](author-self-review.md) — the four-lens review (Content, Philosophy, Learning, Operational) performed by the authoring platform before this preservation.
- [`review-brief.md`](review-brief.md) — the shared review questions every reviewing platform should apply to this same frozen revision.
- [`mockup/`](mockup/) — the authored source of a separate interactive mock-up; see that folder's own README for what is and isn't verified about it.

## Unresolved questions already identified

The full list lives in `prototype-findings.md` under "Questions requiring Sheldon's direction." In summary:

1. What are the actual current thresholds/figures Spark wants treated as canonical for this topic, and how should they be sourced and dated?
2. What terminology does Spark want for the middle category ("insurable" vs. alternatives)?
3. What threshold of uncertainty should trigger escalation to a supervisor versus self-directed verification for a new agent?

Additional lower-priority findings, each tagged with a likely owner (Canon, Governance, Glossary, Academy, or continued Workbench observation), are recorded in full in `prototype-findings.md`.

## Relationship between this Markdown course and the private interactive mock-up

A separate interactive HTML mock-up was built from this content and published as a private, unlisted preview surface outside this repository (not on GitHub, not linked from here). The mock-up's authored source is preserved in `mockup/` for inspection. Its exact live-served rendering could **not** be independently verified against that source during this preservation — the live preview requires the authoring session's own authenticated access, which was not reachable from the tooling used to prepare this packet. The relationship between the two should therefore be treated as **author-asserted, not independently verified**: the mock-up was manually built to reflect this Markdown content at the time of each revision, with no automated link, diffing, or version lock between them. Do not assume future edits to either file are reflected in the other.

## What this preservation is not

- Not an approval, endorsement, or quality judgment of the prototype's content.
- Not a move into `04-academy/`.
- Not an Architectural Decision — no ADR accompanies this change.
- Not a change to any authoritative repository area (`01-philosophy/`, `02-governance/`, `03-canon/`, `04-academy/`, `brain/`, or any other existing Workbench file).
