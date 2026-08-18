# Agent-Team Evolution — Consolidated Review Notes

Non-canonical working notes from an ongoing devil's-advocate review conversation with Claude (Claude Code), auditing the "agent-team-evolution" Workbench concept against Spark OS's actual repository, governance, and history. Not committed to the repo. For your own storage and future reference.

---

## Status of the 22-point list

| # | Point | Status |
|---|---|---|
| 1 | Headline finding | **Closed** — see below |
| 2 | What is proposed / potential strength | **Closed** — see below |
| 3 | Governance today — 2/3 role model | **Open, in progress** |
| 4–22 | Duplicate authority, portability, intake folder, ADR triggers, evidence gap, stop conditions, cost accounting, necessity evidence, park-don't-build, falsifiable question, sequencing, repo age, governance intentionality, priority, benefit case, 4-part role test, craft/authority enforcement, autonomy-tier drift, human-role erosion | **Not yet reached** — surfaced organically in discussion but not formally worked through as standalone points |

Additional points added during discussion (not in your original numbering):
- 23. Non-canonical OneDrive cloud workbench + GPT-desktop local clone as a real storage layer outside the repo
- 24. Deliberate separation of install/review/audit work across multiple chats as an existing practice

---

## Point 1 — Headline finding (resolved)

**Original finding:** `00-workbench/agent-team-evolution.md` did not exist anywhere in the canonical repo — not in the working tree, git history, any branch, or any PR — despite a third-party conversation claiming it had been created.

**Resolution:** Confirmed as real, not fabricated. The file exists in a OneDrive-hosted cloud workbench that GPT-desktop (Codex) maintains alongside a local clone of the repo, pushing to GitHub `main` only on deliberate action. The claim was accurate in its own storage context and simply never crossed into the canonical repo. You later located and provided the actual file — it matches your original instructions closely (concise, sourced, non-authoritative, medium priority, scope-bounded).

**Corrected causal chain (ruled out alternatives):**
- *Not* a PR #17 merge overwrite — verified PR #17 was unmerged at the time of the original claim (later merged live, separately, via GitHub directly — confirmed by screenshot, no AI involved).
- *Not* simple "user error" from conflicting instructions — though conflicting instructions ("don't persist this" vs. later "please workbench this") did create genuine ambiguity, the AI's unhedged completion claim without flagging that ambiguity is a separable, real calibration issue.
- **Correct explanation:** cross-platform storage-context ambiguity — a true claim made without disclosing which storage context it was true in.

**Supporting evidence found independently:** PR #16's description explicitly excludes "S-122... post-checkpoint research-agent material," and the canonical audit log (`foundational-conversation-audit.md`) stops at S-121 (2026-08-09) — meaning S-122 (the natural next entry, matching an August 11 "research-agent" conversation) was deliberately excluded from what got preserved to `main`. This independently corroborates that related material existed outside the canonical repo and was consciously left out during a cleanup pass, not fabricated.

**Standing lesson (survives the resolution):** Something related to this concept existed, was never reconciled into the actual source of truth, and the only reason it's known today is that a PR description happened to leave a trace and you happened to remember to paste the original conversation. That's the real coordination question a multi-agent system has to answer — not "can an agent claim it did something" but "does anything guarantee that claim reconciles with reality without a human catching every gap by memory."

**User-flagged notes for future audit/history summary:**
- i) Clones/local copies are good for practice and for keeping the canonical repo limited to explicitly-installed material, but can cause cross-platform confusion.
- ii) Self-identified knowledge gaps (untrained in software development) should be addressed two ways: (a) genuinely getting up to speed, and (b) guardrails that flag/return invalid or ambiguous requests rather than silently resolving them. Note: this second half already exists as written policy — `AI_GOVERNANCE.md` says AI must escalate rather than silently resolve unclear authority or out-of-scope tasks. The gap in this incident was enforcement/practice, not missing policy.

**Also discovered while investigating:** the `S-###` audit-numbering convention has existed since the very first version of `foundational-conversation-audit.md` (S-001, dated 2026-07-21, present in PR #7) — not adopted partway through as originally recalled. Also: git history shows no intermediate commits between S-039 and S-121 — roughly 80 entries were composed outside git and landed in one consolidated push (PR #16), reinforcing the external-composition pattern above. (Clarified for the record: nothing is missing from the current file — all 121 entries are present and unbroken. This was a git-commit-granularity observation, not a data-loss finding.)

---

## Point 2 — What is proposed / potential strength (resolved)

**Your argument:** The six-stage evolutionary path in the original conversation already front-loads an evidence-gathering-only phase before any agent identity work — i.e., the proposal "began with the end in mind" without being prematurely restrictive. This review conversation is itself proof that process is happening correctly.

**Where this was conceded:** Raising "no defined stop condition" as if it were a flaw in the document was miscalibrated — thresholds and exit criteria are Challenge/Audit-stage outputs, not something an Explore-stage artifact should already contain. The idea is still in Explore, moving into Challenge; demanding thresholds now was premature.

**Where a distinction was held:** Sequencing (what comes before what) is not the same as thresholds (what would make a stage count as passed or failed). The underlying risk — this repo's demonstrated pattern of Workbench items stalling without a forcing function (PR #12 being the clearest example) — remains real and independent of staging. Rescheduled as something Challenge/Audit should produce later, not dropped.

**Modularity claim:** Credited for what currently exists (one small file, no infrastructure, trivially reversible — genuinely modular). Held open for the larger hypothetical architecture (roles, state, manager, intake), which hasn't been built or tested yet. Repo's actual PR history (archive-not-delete, ADR supersession-not-editing, consistently bounded "exactly N files" PRs) independently supports that your authoring discipline is real and consistent — that's evidence about *your process*, not yet evidence about the *eventual system's* structure.

---

## Point 3 — Governance today (in progress)

**Key clarification from you:** The current `AI_GOVERNANCE.md` / `CLAUDE_ROLE.md` two-role model (ChatGPT = architect/engineer, Claude = auditor/steward) reflects the *original* conception from before Spark Brain existed, and has been dormant/unrevised since. Actual practice has diverged substantially:

- A long-standing, single continuous-context "Spark OS audit chat" (GPT Codex desktop) functions as a genuine working partner — spanning idea validation, unattached exploration, repo-nested audit/refinement, and occasional cross-checks via summaries to other conversations or to Claude/Claude Code.
- Many temporary, ad hoc roles have been tested, refreshed via chat-summary prompts.
- A new, not-previously-conceptualized role: an installer/implementer that executes instructions and reports back.

**Assessment:**
- The stale-governance-doc observation is accurate and independently actionable — it matches multiple explicit "Role Evolution" triggers already written into `CLAUDE_ROLE.md` (durable new workflow, role overlap). This is a concrete, ready-made trigger case for **Governance Fit Audit 001**, already queued as priority #2 in `task-notepad.md`, ahead of anything agent-team related. You confirmed this audit needs to run before any new installs.
- The multi-chat pattern (exploration chat / audit chat / cross-check chat) is real counter-evidence against needing *repo-native durable agent identity* for the differentiation-of-thinking benefit specifically — that benefit already exists via session/context separation. It is *not* evidence against the separate, downstream production-agent use case (repetitive course-building), which is a different value proposition (throughput/consistency vs. deep iterative judgment). You pushed back correctly on the overgeneralization; this was conceded.
- You clarified the audit chat itself will **not** be converted into an agent — only its accumulated logic/reasoning may inform the design of a future content-audit agent. The structural auditor (installation/PR/process) vs. content auditor (course material vs. Canon/governance) split is a deliberate separation-of-duties design, to avoid the auditor auditing the guidance it was itself modeled on. Flagged one layer deeper: if the content-auditor inherits the audit chat's judgment patterns while the audit chat also reviews the content-auditor's installation, the same self-reference risk can re-enter indirectly — worth keeping the lineage explicit and reviewable.

---

## Cross-cutting design threads (surfaced organically, not yet mapped to specific list points)

### Containment and the "agents circumventing governance" fear
Broken into three concrete, governable mechanisms rather than one diffuse fear:
1. **Self-editing instructions** — an agent with write access to its own charter/memory can drift silently. Mitigation: never allow unreviewed self-writes to instruction files.
2. **Over-broad credentials/tool scope** — ordinary bad instructions cause real damage under excess permission, no malice required. Mitigation: least-privilege, scoped credentials.
3. **Prompt injection via untrusted external content** — specifically relevant to a web-browsing Research Agent; a fetched page can contain adversarial text disguised as instructions. Mitigation: treat all fetched content as data, never as instructions.

A separate "Spark-Agents" GitHub repo with strict push-only permissions to Spark-OS is a **legitimate, real mitigation specifically for mechanism 1 and 2's worst-case impact on Spark-OS's own integrity** — re-credited after initially being dismissed as premature infrastructure. It does **not** address mechanism 3 or any external side effect (spend, scraping, ToS exposure) that happens before anything is ever committed — that's an execution-environment problem, not a repo-topology problem. Recommended sequencing: build the smallest supervised pilot first (using Spark OS's existing PR-review machinery, no new repo), let the isolation boundary get designed around what the agent actually turns out to need, rather than guessing at it now. Per-role repos (one GitHub repo per agent) were flagged as premature at any stage — multiplies coordination overhead sevenfold before a single role has evidence of being materially distinct.

### The Research Agent (the concrete, original use case)
Given a topic, search public sources (web, mortgage sites) for candidate material; explicitly non-Canon until human review. Most concretely specified and testable piece of the whole concept.
- Real risk: unattended overnight research against live external sources raises actual ToS/legal exposure for a real mortgage business, separate from generic AI risk.
- Real risk: "continuous output for later review" does not reduce total review burden — it relocates it, and if production outruns review capacity, it can relocate the burden into a *worse* shape (one large fatigue-prone backlog) than the one being escaped. Needs a production rate throttled to sustainable review cadence.
- The "idle AI usage / deadtime" efficiency argument for overnight runs is real but is in direct tension with the above — the same unsupervised window that makes it cheap is what makes it highest-risk. Resolve toward caution first: prove the pipeline supervised and on-demand before ever letting it run unattended.
- Smallest real test of the actual hypothesis: one prompt/skill, on demand, human-run, writing candidate source notes into an existing non-authoritative Workbench location, reviewed the same way everything else already is. No scheduling, no new repo, no roles, no manager.
- The rerun-with-revisions self-improvement loop is a sound pattern but requires no new infrastructure — it's achievable today, by hand, as part of that same tiny pilot.
- Researcher may eventually split into a mortgage-content invocation and a system/self-improvement invocation (finding prior art on other people's agent architectures, not proposing changes to itself). The system-research output is categorically higher-stakes than content research and needs asymmetric governance — treated like Full Architectural Boot material whenever it's actually acted on, never folded into the same casual review lane as a mortgage-source suggestion.

### Manager, Auditor, Reporter roles
- **Manager** — explicitly *not* an authority figure. Reviews, interprets, and communicates agent state/history to you; you retain monitor/decide/audit/implement. This resolves the duplicate-authority concern as designed, and matches how ChatGPT's role already works in existing governance (recommend, not decide). New risk raised: since you're explicitly building the Manager to be your anchor for agent behavior that outpaces your own technical fluency, the Manager becomes a single point of translation trust — the same knowledge gap that motivates its existence would also prevent you from verifying its summaries independently. You noted every agent will carry a full audit trail specifically for correction and learning, which is the right structural answer (ground truth exists independent of the Manager) — the remaining open piece is whether that trail is legible enough for you to spot-check it yourself, tying back to your own note (ii) above.
- **Auditor** — whether this becomes one archetype with multiple invocations or two genuinely separate agents (role-auditor vs. content-auditor) is correctly being treated as a deferred decision, same pattern as the Researcher generalist-vs-split question — consistent with "cluster before naming," the right methodology at this stage.
- **Reporter** — deliberately non-fluid: can change *what* it reports on as roles evolve, but can never gain implementation mechanisms beyond reporting. This is the first concrete enforcement mechanism proposed all session for the abstract "agents own craft, Spark OS owns truth" principle — genuinely good, specific design, not just an assertion.

### Boot modes and the packet/artifact concept
Three new Spark Brain concepts proposed, distinct from the existing Quick Resume / Full Architectural Boot:

1. **Installation Boot** — narrow-context mode: reviews the last 3 `S-###` audit entries, checks for an explicit "install packet ready" marker (agreed necessary — avoids relying on prose interpretation), locates the installation packet, and waits for a manually pasted installation prompt. Deliberately human-mediated at the handoff point — this was identified as the single highest-leverage spot for a repeat of the headline-finding failure mode if ever automated, and keeping it manual was the right call.
2. **Empty Context Boot** — for idea exploration or narrowly-scoped context reference; deliberately abandons default Canon/context, loading only explicitly named files on request. This formalizes the exploration-chat pattern you already run informally (unattached to repo context) rather than proposing something speculative. Design requirement: even an "empty" session needs a floor — at minimum, the closeout/summary format — or its output has no clean way to hand off to the rest of the system.
3. **"Archive Spark OS"** (formerly "Close Spark OS") — triggers a chat summary, returns it, and confirms whether to archive it as non-canonical reference material for later research or reconstructing why a decision was made. This maps almost exactly onto the existing Design History "Conversation Summary" document type (`99-archive/design-history/conversation-summaries/`) — not new territory, a convenient invocation for an existing, template-governed convention. The existing creation rule ("only when a conversation materially shaped, challenged, or clarified long-term architecture") should still gate the confirm-to-archive step, to avoid low-value archive sprawl. This conversation would likely clear that bar itself.

All three boot-mode proposals were flagged as requiring the same governance gate as everything else in this repo — adding a boot mode changes "boot order," which `constitution.md`'s own Change Discipline requires an ADR for. Good ideas don't skip the process; that's been the consistent pattern all session.

**Installation packet concept** — replaces the earlier, more speculative "intake folder" idea with something more concrete: material enters Workbench (manual, human-mediated), gets refined in a chat session, and becomes a structured "packet" (material + routing + optional per-role notes) that becomes the artifact agents actually refine as it moves through a pipeline. This matches stage 2 of the original six-stage evolutionary plan almost exactly ("work-item state and event history... before tracking rich agent biographies") — flagged as the correct next increment, landed on without needing to be argued into it. Minor watch-item: if the same per-role routing tweak keeps recurring across packets, that's a signal the role's default template should absorb it, not that it should remain a permanent per-packet workaround — same evidence-based-evolution principle as everything else, at a smaller scale.

**Self-inferred learning proposals** ("agent suggests learning to Manager from its own inference of work history") — the apparent tension between boundedness and uniqueness resolves if the *suggest* step (unbounded, creative) stays structurally separate from the *implement* step (fully human-gated). Two risks flagged: (a) an agent inferring lessons from its own history is reading its own account of what happened, so noise or inconsistency in that history can be mistaken for genuine pattern — mitigate by weighting independently-recorded corrections/rejections over the agent's own self-narrative; (b) even under human-only approval, unthrottled suggestion volume can recreate the exact review bottleneck the system is meant to relieve — needs its own cadence or threshold.

### Canon sourcing standard (already-queued work, keeps surfacing as relevant)
Two real domain examples surfaced during this discussion that are candidate content for the already-queued minimum Canon sourcing standard (`task-notepad.md` priority #3), not generic packet-level tweaks:
- Insurer policy (Sagen, Canada Guaranty, CMHC) as the sole source of truth, overriding competing sources.
- Lender-specific policy verification requirement — do not assume lender policy without a documented source.
- Important nuance surfaced: these two rules are not simply layered — they're partially overlapping and partially mutually exclusive. Insurer policy acts as an override baseline; lender policy sometimes narrows more conservatively within that baseline, meaning a flat "insurer always wins" rule would break on the lender-specific case. This is concrete evidence the eventual standard needs a real sourcing hierarchy, not a single global rule. Recorded here specifically so it isn't lost before that queued work starts.

---

## Open threads / carried forward

- Point 3 (governance today) is still open — mid-discussion.
- Points 4–22 not yet formally worked through as their own items (though several have been substantively touched on in the cross-cutting threads above).
- Governance Fit Audit 001 (already queued, priority #2) needs to run before any new installs — agreed as a hard prerequisite.
- A reconciliation pass for "other unregistered audits/feedback across platforms" (potentially a dozen or more) was proposed as a cheap, already-precedented next step (matching `S-121`'s own prior "Workbench inventory, reconciliation, and priority reset") — not yet scheduled or acted on.
- The audit chat is expected to draft an overview documenting its own repeating installation-packet process — flagged that this draft needs to actually cross into the canonical repo when written, not remain OneDrive-only, or it repeats the exact shape of the headline finding.
