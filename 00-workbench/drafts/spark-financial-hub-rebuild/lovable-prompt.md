# Lovable Prompt: Duplicate of Spark Financial HUB

Use this prompt as a starting point in Lovable to generate a similar app. Draft for review, not yet authoritative.

## Prompt

Build an internal broker onboarding, training, and reference hub called "[Your Product Name]" for a mortgage brokerage. Use React with TanStack Router, shadcn/ui components, Tailwind CSS v4, and Supabase for auth and data (Postgres + RLS). Use a dark, minimal, professional theme with OKLCH color tokens (light and dark mode) and one custom brand accent color.

Auth: Supabase email and password auth, gate all internal routes behind an authenticated layout. Add a user_roles table (broker, manager, admin).

Pages:
1. Dashboard: welcome banner, onboarding progress card, new-this-week training count, required-modules counter, upcoming team training, quick links, latest announcements feed.
2. Onboarding: a 4-week, about 18-task checklist grouped by week, some tasks auto-completed by a database function when the user visits related pages, others manually checkable. Include a manager-facing Team Onboarding page listing every user's completion percent.
3. Training: a library of sections (each with a title and description), each containing lessons (rich text or video, required or elective) and an end-of-section quiz. Show aggregate stats (total lessons, required count, section count) and filter tabs (All, Required, Elective). Each lesson opens its own detail page with mark complete or incomplete.
4. Mortgage and Lender Guides: tabbed reference area: a filterable lender comparison table, product guides, qualifying and rate tools, and worked deal scenarios.
5. Prospecting and Scripts: tabbed playbooks (lead-gen strategies) and a scripts library (call and email scripts).
6. SOPs: standard operating procedures, filterable by category.
7. Forms and Checklists: a library of downloadable reference documents.
8. Compliance and Licensing: non-negotiable compliance rules plus a per-province or region regulator and license-level reference table.
9. Activity Targets: a weekly KPI tracker with editable actuals per week and auto-totals, grouped by category.
10. Team Directory, Announcements, and a manager-facing Team Progress dashboard showing training, onboarding, and quiz completion per user.

Data should be fully database-driven (sections, lessons, quizzes, and tasks as rows, not hardcoded), so an admin can add new training content without code changes. Include row-level security so brokers can only edit their own progress and KPI data, while managers and admins can view everyone's.

## Source
Drafted by Claude based on live inspection of https://sparkfinancialhub.com on 2026-07-24.
