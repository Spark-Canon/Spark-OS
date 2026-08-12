# Source-Chat Historical Capture Prompt

**Status:** Non-authoritative Workbench utility
**Repository status:** Not accepted, installed, or active as an AI instruction
**Purpose:** Preserve a reusable prompt for asking a context-heavy source conversation to prepare a candidate historical capture for later independent Spark OS review.

## Intended Use

This prompt is a transfer aid, not an archive-admission decision or replacement for the canonical [Design History summary template](../../99-archive/design-history/SUMMARY-TEMPLATE.md).

The source conversation produces a non-authoritative candidate. A later Spark OS review must independently:

- decide whether the Design History admission threshold is met;
- verify reported repository actions and references;
- apply the then-current Governance and canonical template;
- determine the appropriate destination, which may be a conversation summary, another historical record type, Workbench evidence, or no repository record; and
- approve and install any qualifying record through the normal repository workflow.

Do not use this prompt as an automatic session-closeout step. Do not treat its output as accepted history or current guidance.

## Reusable Prompt

```markdown
Create a non-authoritative candidate historical capture of this conversation for later independent review.

This output is not an accepted Design History record. Do not assume the conversation qualifies for repository preservation. A later Codex task will verify repository references, apply current Governance, determine the appropriate historical record type, and decide whether anything should be installed.

Requirements:

1. Summarize the entire relevant conversation, not merely the latest exchange.
2. Compress repetition, conversational filler, and transient execution narration.
3. Preserve reasoning that materially shaped, challenged, clarified, or tested long-term Spark OS architecture, Philosophy, Governance, Canon, Academy, or institutional design.
4. Clearly distinguish:
   - exploration from acceptance;
   - candidates from authoritative content;
   - conversation outcomes from repository implementation; and
   - historical next steps from current instructions.
5. Include meaningful alternatives, objections, rejected directions, protected distinctions, boundary decisions, challenge tests, audit findings, unresolved questions, and lessons learned.
6. Do not invent approvals, repository paths, pull requests, commits, installations, or implementation results.
7. Treat repository actions described only within the conversation as: `Conversation-reported — requires independent repository verification.`
8. Use `Not available` where dates or repository references are unknown. Do not guess.
9. Exclude credentials, unnecessary personal information, sensitive client information, and restricted material.
10. Do not recommend a repository destination or convert proposed ideas into current guidance.

Use this Markdown structure:

# <Conversation Topic>

**Date or range:** <YYYY-MM-DD, date range, or Not available>
**Capture status:** Non-authoritative candidate historical capture
**Repository status:** Not installed or verified

## Purpose

## Context

## Major Milestones

## Alternatives and Concerns

## Architectural Principles Discussed

## Outcome

## Lessons Learned

## Repository References

### Authoritative Documents

### Pull Requests

### Commits

### Related Historical Records

## Unresolved Questions

## Next Milestone at Time of Conversation

State explicitly that this is historical context, not a current instruction.

## Fidelity Notes

Identify chronology uncertainty, claims requiring repository verification, privacy omissions, and whether the complete transcript may have exceptional historical value.

Return only the finished Markdown document.
```

## Reconsideration Trigger

Review this utility during a future design, workflow, or AI-systems audit when related improvements are already in scope. Consider explicit prompt invocation only if repeated use shows that manual retrieval is unreliable or inconsistent.

Any later proposal must compare this utility with current Design History Governance and templates, preserve explicit invocation, avoid automatic archive creation, and remove the utility if the accepted process makes it redundant.
