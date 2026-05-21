---
description: Run a structured, framework-grounded UX teardown on any app
allowed-tools: Read, Write, Bash, WebFetch, WebSearch, mcp__mobile__mobile_list_available_devices, mcp__mobile__mobile_list_apps, mcp__mobile__mobile_launch_app, mcp__mobile__mobile_take_screenshot, mcp__mobile__mobile_save_screenshot, mcp__mobile__mobile_click_on_screen_at_coordinates, mcp__mobile__mobile_swipe_on_screen, mcp__mobile__mobile_list_elements_on_screen
argument-hint: [app-name] [module] as [persona] (mode: speed|rigor)
---

Run a pAI app teardown using the `app-teardown` skill.

The user's input: $ARGUMENTS

Parse these from the input:
- **App name** — any app (e.g. "Duolingo", "Notion", "Cred", "MyApp")
- **Module** — one of: `onboarding`, `homepage`, `discovery`, `personalization`, `content`, `engagement`, `monetization`, `ai`, `cognitive-load`, `persona-alignment`, or `full`
- **Persona** — one of: `new-user`, `free-user`, `trial-user`, `paid-user`, `lapsed-user`
- **Mode** (optional) — `speed` (≈15 min, top issues) or `rigor` (≈45–60 min, comprehensive). Default: `rigor`.

If any required parameter is missing, ask the user before proceeding.

Then load `skills/app-teardown/SKILL.md` and execute the full teardown workflow from STEP 0 through STEP 8 described in that skill. For the deeper reference (PDF typography spec, framework explanation standard, competitor comparison standard), `appteardown.md` at the plugin root has the long-form version.
