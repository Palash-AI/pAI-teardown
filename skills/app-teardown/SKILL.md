---
name: app-teardown
description: >
  This skill should be used when the user wants to "review an app", "run a teardown",
  "audit a mobile app", "review onboarding", "review monetization", "review engagement",
  or uses the /review command. It runs a structured, framework-grounded UX teardown on
  any mobile or web app — producing scored screenshot-cited evidence, key issues, themed
  recommendations, an auto-updated app-context file, and a stakeholder-ready PDF. India
  consumer context is baked in. Trigger phrases: "review [app]", "teardown [app]",
  "audit [app]", "/review", "run a product review".
version: 1.1.0
author: Palash Somani (https://www.linkedin.com/in/palash-somani-artificial-intelligence/)
---

# pAI App Teardown — Master Orchestrator

> **Command:** `/review [app-name] [module] as [persona] (mode: speed|rigor)`
> **Examples:**
> - `/review Duolingo onboarding as new-user`
> - `/review Cred monetization as trial-user`
> - `/review Notion full as free-user, mode: rigor`

This file is the **orchestrator**. For deep-dive specifications (typography, framework-explanation standard, competitor-comparison standard, PDF schema), see `appteardown.md` at the plugin root.

---

## STEP 0 — Parse the command

| Parameter | Required | Options | Default |
|---|---|---|---|
| **App name** | Yes | Any app (e.g. "Duolingo", "Notion", "Cred") | — |
| **Module** | Yes | `onboarding`, `homepage`, `discovery`, `personalization`, `content`, `engagement`, `monetization`, `ai`, `cognitive-load`, `persona-alignment`, or `full` | `full` |
| **Persona** | Yes | `new-user`, `free-user`, `trial-user`, `paid-user`, `lapsed-user` | `new-user` |
| **Mode** | Optional | `speed` (≈15 min) or `rigor` (≈45–60 min) | `rigor` |
| **Domain** | Auto-detect | `education`, `ott`, `finance`, `ecommerce`, `social` | Auto-detect from app |

If anything required is missing, ask the user once.

---

## STEP 1 — Load context (lean by default)

Paths resolve from `${CLAUDE_PLUGIN_ROOT}` (set automatically when this skill loads).

**Always load:**
1. `${CLAUDE_PLUGIN_ROOT}/frameworks/expert-frameworks-ref.md` — compact framework lookup (full encyclopedia in `expert-frameworks.md` if needed).
2. `${CLAUDE_PLUGIN_ROOT}/context/india-ref.md` — compact India delta table (full version in `india-consumer.md`).
3. `${CLAUDE_PLUGIN_ROOT}/context/india-product-strategy.md` — India competitor library, KPI benchmarks, prioritization rules.

**Load based on domain:**
4. `${CLAUDE_PLUGIN_ROOT}/domains/[domain].md` (e.g. `education.md`). If a domain file doesn't exist, proceed with general frameworks and note the gap.

**Load active persona only:**
5. `${CLAUDE_PLUGIN_ROOT}/context/personas/[persona].md`. Do NOT load all 5.

**Load app-specific context if it exists:**
6. `${CLAUDE_PLUGIN_ROOT}/context/[app-name]-context.md`. If absent, skip; create it during STEP 8 (auto-learn).

**Load the module file ONLY when executing that module:**
7. `${CLAUDE_PLUGIN_ROOT}/modules/[module].md` (standard) — or `${CLAUDE_PLUGIN_ROOT}/modules/full/[module].md` if rigor mode and the standard module's anchor description isn't enough.

> **Token discipline:** never pre-load all 10 modules for a single-module run. See `TOKEN-EFFICIENCY-PLAN.md` for the 7-tactic playbook.

---

## STEP 2 — Connect to the app

**If Mobile MCP is available** (live mobile device or emulator):
1. `mobile_list_available_devices` → confirm a device is connected.
2. `mobile_list_apps` → find the target app's package name.
3. `mobile_launch_app` → confirm with an initial screenshot.

**If no Mobile MCP**, or if the target is a web app:
- Use Claude Code's browser tools (e.g. `Claude in Chrome` MCP) for web apps.
- Or: ask the user to drop screenshots into `screenshots/[run-id]/img/` and reference them by filename.
- Note in the output: "Review based on [auto-capture / browser / manual screenshots]".

---

## STEP 3 — Screenshot protocol

Read `${CLAUDE_PLUGIN_ROOT}/screenshot-protocol.md` once before capturing anything.

Summary:
1. Capture every screen you navigate — no exceptions.
2. Save with the convention `[##]-[screen-name]-[persona].png` into `screenshots/[run-id]/img/`.
3. Log each capture in `screenshots/[run-id]/screenshot-manifest.md` immediately (never batch at the end).
4. Every evidence bullet must cite its screenshot number.

---

## STEP 3.5 — Mandatory design + UX-copy review (where available)

If the user's Claude install has the Anthropic Design plugin loaded, run two passes per module's screenshots:

1. `design:critique` — usability, hierarchy, consistency, accessibility. For India context: judge on budget-device (720p, outdoor brightness) parity.
2. `design:ux-copy` — CTAs, labels, errors, empty states, notifications. For India context: Hindi/Hinglish quality, Tier 2-3 clarity, ₹ pricing presentation.

Both outputs feed back into evidence bullets, key issues, scoring modifiers, and recommendations. If these plugins aren't installed, skip and note the gap.

---

## STEP 4 — Execute the module(s)

### Single module
Read `${CLAUDE_PLUGIN_ROOT}/modules/[module].md` and follow its rubric: screens to navigate, what to observe, framework checks, scoring anchors.

### Full review (10 modules in order)

| # | Module | File | AARRR |
|---|---|---|---|
| 1 | Onboarding & First Value | `modules/onboarding.md` | Activation |
| 2 | Homepage & IA | `modules/homepage-ia.md` | Activation / Engagement |
| 3 | Content Discovery & Search | `modules/discovery-search.md` | Engagement |
| 4 | Personalization | `modules/personalization.md` | Engagement / Retention |
| 5 | Content Consumption | `modules/content-consumption.md` | Engagement |
| 6 | Engagement & Retention | `modules/engagement-retention.md` | Retention |
| 7 | Monetization UX | `modules/monetization.md` | Revenue |
| 8 | AI Integration | `modules/ai-integration.md` | Engagement / Retention |
| 9 | Cognitive Load | `modules/cognitive-load.md` | All |
| 10 | Persona-Intent Alignment | `modules/persona-alignment.md` | All |

### Speed vs Rigor

**Speed (~15 min total for full, ~5 min per module):** 3–5 screenshots per module, 1-sentence scoring rationale, top 3 issues only, no detailed evidence bullets.

**Rigor (~45–60 min single module, ~3–4 hours for full):** 8–15 screenshots per module, comprehensive evidence bullets with framework citations, all key issues documented, all framework violations called out.

---

## STEP 5 — Scoring methodology

### Per-module scale (1–10)

| Score | Label | Definition |
|---|---|---|
| 1–2 | Critical | Fundamentally broken. Immediate fix required. |
| 3–4 | Poor | Significant issues. High-priority. |
| 5–6 | Below Average | Functional but subpar vs competitors. |
| 7–8 | Good | Solid. Minor optimization opportunities. |
| 9–10 | Excellent | Best-in-class. Benchmark for others. |

### Every score must reference

1. At least one **expert framework** ("Violates Fogg's Ability principle because…").
2. At least one **domain benchmark** ("Duolingo reaches first lesson in 60 seconds; this app takes 4 minutes").
3. At least one **India consumer consideration** ("Tier 2 users on budget devices would…").

### Weighted average for full review

- Onboarding × 1.5, Monetization × 1.5, Engagement & Retention × 1.5, all others × 1.0.

---

## STEP 5.5 — India Fit Check (mandatory after every recommendation)

Run each Key Issue + Recommendation through:

1. **India consumer reality check** (`context/india-consumer.md`): would this work for a Tier 2 Hindi-speaking user on a budget Android device? If not, reframe.
2. **At least one Indian competitor benchmark** must appear in each Comparative Benchmark — pulled from `context/india-product-strategy.md` Section 1. International apps OK *alongside*, not instead of.
3. **India roadmap prioritization** (`india-product-strategy.md` Section 4): P0 in the global market may be P2 in India and vice versa.
4. **India KPI benchmarks** (`india-product-strategy.md` Section 3): don't use global D1/D7/D30 — they overstate India norms by 30–50%.
5. **BYJU's anti-pattern**: aggressive-monetization risk check before any pricing recommendation.

---

## STEP 6 — Produce outputs

Every run produces 3 markdown artifacts, plus an optional PDF.

### 1. Current state file — `[app]-current-state-[persona].md`

Sections: Header (app + version + persona + date + overall score) → Scorecard table → Per-module evidence (screenshot-cited bullets) → Per-module key issues (framework-cited, numbered) → Top 5 critical issues → Competitive benchmarking → Scoring rationale.

**Rule:** zero recommendations in this file — pure observation.

### 2. Recommendations file — `[app]-recommendations-[persona].md`

Organized by **theme**, NOT by module. Per theme: Quick Wins (1–2 weeks) / Medium Effort (2–4 weeks) / Strategic Fixes (4–8 weeks) → Expected impact. Plus an implementation roadmap (4 phases × 12 weeks) and a success-metrics section (current → 4w → 8w → 12w targets).

### 3. Screenshot manifest — `screenshots/[run-id]/screenshot-manifest.md`

Every captured screen, named systematically, mapped to module and finding.

### 4. Stakeholder PDF (on request) — `[app]-teardown-[date].pdf`

Generated via `${CLAUDE_PLUGIN_ROOT}/output-templates/generate_pdf.py --data [app]-data.json`. The data-file schema is documented inside that script (`--help`) and at the bottom of `appteardown.md`.

**Reference `appteardown.md` §6 for**: typography spec (Poppins + Lato), color palette, evidence-card layout, framework-explanation standard, competitor-comparison standard, para+bullet writing pattern.

---

## STEP 7 — Log token usage

At the end of every run, estimate input/output tokens and run:

```bash
python ${CLAUDE_PLUGIN_ROOT}/output-templates/log_run.py \
  --app "[App]" --persona "[persona]" --flow "[module|full]" \
  --mode "[speed|rigor]" \
  --input-tokens [n] --output-tokens [n] \
  --pdf "[pdf-filename-or-empty]" \
  --notes "[brief note]"
```

Targets:
- Speed, single module: < 15K input
- Rigor, single module: < 40K input
- Rigor, full (10 modules): < 80K input

---

## STEP 8 — Auto-learn: update app context

After every run, append to `${CLAUDE_PLUGIN_ROOT}/context/[app-name]-context.md` (create if absent):

```markdown
## Review: [Date] — [Module] as [Persona] ([Mode])

### Scores
| Module | Score | Delta from Last |

### Key Findings
- [NEW] / [CHANGED] / [RESOLVED] markers

### Cumulative Review History
| # | Date | Module | Persona | Score |
```

Rules: read before appending (no duplicates); compare against previous findings; track version changes; accumulate persona coverage.

---

## Module routing

| Command | Routes to |
|---|---|
| `/review [app] onboarding as [persona]` | `modules/onboarding.md` |
| `/review [app] homepage as [persona]` | `modules/homepage-ia.md` |
| `/review [app] discovery as [persona]` | `modules/discovery-search.md` |
| `/review [app] personalization as [persona]` | `modules/personalization.md` |
| `/review [app] content as [persona]` | `modules/content-consumption.md` |
| `/review [app] engagement as [persona]` | `modules/engagement-retention.md` |
| `/review [app] monetization as [persona]` | `modules/monetization.md` |
| `/review [app] ai as [persona]` | `modules/ai-integration.md` |
| `/review [app] cognitive-load as [persona]` | `modules/cognitive-load.md` |
| `/review [app] persona-alignment as [persona]` | `modules/persona-alignment.md` |
| `/review [app] full as [persona]` | All 10 in sequence |

---

## Error handling

| Situation | Action |
|---|---|
| Mobile MCP not connected | Ask user to provide screenshots manually |
| App not installed | Ask user to install; document as a finding |
| App crashes during review | Document as a finding; restart and continue |
| Screenshots not reaching the workspace | Save to `/tmp/`, immediately `cp` into `screenshots/[run-id]/img/` (don't batch) |
| Unknown domain | Use general frameworks; skip domain file; note the gap |
| No previous app context | Create new file; note "first review" |
| Anthropic Design plugin not installed | Skip STEP 3.5; note that design + ux-copy passes were not run |

---

## Built by

**Palash Somani** — [LinkedIn](https://www.linkedin.com/in/palash-somani-artificial-intelligence/).
Skill is provided as-is; feedback welcome.
