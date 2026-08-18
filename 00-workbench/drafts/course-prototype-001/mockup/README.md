# Course Prototype 001 — Interactive Mock-Up Export

**Export date:** 2026-07-28
**Original platform:** Claude Code (Claude Artifact publishing feature, Anthropic) — a private, unlisted preview surface external to this repository.

## What this is

`course-prototype-001-mockup.html` is the **exact authored source file** submitted to the Artifact publishing tool to produce the interactive preview — confirmed via SHA-256 against the file used at the time of the most recent publish, with no edits in between. It is a self-contained HTML file (inline CSS, no external requests) reflecting the content in `../prototype-course.md` as of 2026-07-28.

## What could not be verified

The live, served preview page could **not** be independently compared against this source during preservation. Attempting to load the private preview URL from the tooling available in this session returned an authentication-gated "page not found" response — the preview requires the original authoring session's own signed-in access, which was not available here. This is an expected limitation of a private, unlisted preview surface, not evidence of a discrepancy.

Known, expected differences between this source and whatever is actually served live (based on how the publishing feature is documented to work, not on direct inspection):

- The published page wraps this file's content in an outer `<!doctype html>`/`<head>`/`<body>` skeleton not present in this source file.
- Platform-level chrome (e.g., a light/dark theme toggle, any injected viewport or security headers) may be added at publish time.

No difference beyond that wrapping is expected, but this has **not** been confirmed by direct comparison. Treat this file as the authored intent, not a verified byte-for-byte mirror of the live page.

## How to inspect it

Open `course-prototype-001-mockup.html` directly in any modern browser — it is fully self-contained (no build step, no external network requests, no dependency on this repository or any server). It renders the same ledger/case-file styled interactive lesson described in `../README.md` and `../prototype-course.md`: Learn, Apply (five reveal-style cases), the original open-ended Assessment, and the 12-item Knowledge Check, each using native `<details>`/`<summary>` disclosure — no JavaScript is required for any interaction.

## Relationship to the private URL

The private preview's URL is deliberately **not recorded anywhere in this repository**, per instruction — it has not been separately approved for publication. If a live, shareable link is wanted for cross-platform review, that requires a separate, explicit decision outside this preservation task.
