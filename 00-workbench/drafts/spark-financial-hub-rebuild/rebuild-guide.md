# Spark Financial HUB — Structure & Rebuild Guide

## Overview
An internal onboarding/training/reference platform for Spark Financial Group brokers and agents. React SPA + Supabase backend, generated on Lovable.

## Tech Stack
- Frontend: React, TanStack Router (file-based, code-split routes, an `_authenticated` pathless layout guarding all internal pages)
- UI: shadcn/ui components (button, input, badge, card, progress, page-header) + Lucide icons
- Styling: Tailwind CSS v4, OKLCH color tokens, light (`:root`) + dark (`.dark`) themes, custom `--spark` brand token layered on the standard shadcn palette
- Backend: Supabase (Postgres + Auth + PostgREST + RPC)
- Hosting/build: Lovable platform (built-in analytics beacon, asset CDN)
## Routes
| Route | Purpose |
|---|---|
| `/` | Dashboard: progress widgets, quick links, announcements |
| `/onboarding` | Personal 4-week / 18-task checklist, auto + manual items |
| `/onboarding/team` | Manager view of every broker's onboarding percent |
| `/training` | 13 sections / 50 lessons / 38 required, filter tabs |
| `/training/:lessonId` | Individual lesson (rich text or video), quiz links |
| `/mortgage-guides` | Tabs: Lender Matrix, Product Guides, Rate and Qualifying Tools, Deal Scenarios |
| `/prospecting` | Tabs: Playbooks, Scripts Library |
| `/sops` | Standard operating procedures, filterable by category |
| `/forms-checklists` | Downloadable reference docs |
| `/compliance` | Non-negotiable rules plus per-province regulator and licensing table |
| `/activity-targets` | Weekly KPI tracker by category |
| `/team` | Team directory |
| `/announcements` | Leadership announcement feed |
| `/team-progress` | Manager view: training/onboarding/quiz completion per user |

## Data Model (Supabase tables, inferred from observed API calls)
- profiles: id, email, full_name
- user_roles: user_id, role
- sections: id, title, description, sort_order, is_published
- lessons: id, title, content_type (rich_text/video), is_required, sort_order, body, section_id, is_published
- quizzes: id, title, section_id
- quiz_attempts: user_id, quiz_id, score, passed, created_at
- lesson_progress: user_id, lesson_id, completed
- onboarding_tasks: id, is_active
- onboarding_progress: user_id, task_id
- RPC auto_complete_onboarding: server-side function that ticks onboarding tasks as a user navigates related sections

## Design Tokens (light theme sample)
```
--background: oklch(98.5% .002 270)
--foreground: oklch(18% .025 265)
--primary: oklch(20% .03 265)
--secondary/--muted/--accent: oklch(93-95% ... 265)
--destructive: oklch(55% .2 25)
--spark: oklch(20% .03 265)
```
Dark theme mirrors the same variable set with inverted lightness.

## Content Model Notes
- Training content is fully data-driven (not hardcoded); new lessons and quizzes can be added via rows, not code changes.
- Activity Targets appear to be client-persisted rather than backed by a dedicated Supabase table (not confirmed; no matching table observed in network calls during testing).

## Source
Compiled by Claude via live inspection of https://sparkfinancialhub.com (page content, DOM, JS bundle manifest, network requests, CSS variables) on 2026-07-24. Draft for review, not yet authoritative.
