# Spark Financial HUB — Build Audit and Improvement Suggestions

Draft for review, not yet authoritative. Based on live inspection of https://sparkfinancialhub.com on 2026-07-24.

## Findings

Data fetching: the app re-runs the same set of global Supabase queries (lessons, sections, quizzes, onboarding_tasks, profiles, and more) on nearly every route navigation rather than caching them. This adds unnecessary load and latency. Suggest introducing a shared data-fetching layer with caching, for example reusing a TanStack Query cache across routes instead of refetching per page.

Onboarding automation: the auto_complete_onboarding RPC fires on every navigation and silently changes state with no visible confirmation. This could confuse users or make onboarding progress feel unpredictable. Suggest surfacing a toast or activity-log entry when it fires.

Activity Targets persistence: the page claims data "persists locally," but no dedicated Supabase table was observed backing it during testing. If it is genuinely only in browser storage, KPI history would be lost on a new device or cleared cache, and managers could not see rep-level activity data centrally the way they can for training and onboarding. Suggest moving this into its own Supabase table for durability and reporting.

Security: row-level security policies could not be verified from the browser by design. Worth explicitly auditing that brokers can only write their own lesson_progress, onboarding_progress, and quiz_attempts rows and not each other's, and that the user_roles check gating manager-only pages (Team Progress, Team Onboarding) is enforced server-side via RLS, not just hidden client-side navigation.

Content freshness: SOPs, Forms and Checklists, and Compliance sections are static reference lists with only a "v1" tag and no visible last-updated metadata. Suggest adding visible last-reviewed dates so brokers can trust that compliance content is current.

Content model alignment: since this hub is meant to become the foundation for Spark-OS training, worth deciding now whether lesson body content should live as Markdown (matching the GitHub Canon's own source-of-truth principle) rather than embedded rich text or HTML, so the same canonical content can drive both the GitHub knowledge base and the HUB without duplication.

## Source
Compiled by Claude via live inspection of the app's page content, DOM, JS bundle manifest, network requests, and CSS variables.
