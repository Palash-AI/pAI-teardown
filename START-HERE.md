# Start Here — pAI-teardown (Offline Skill)

> **What this is:** A framework for running structured app teardowns. 10 analysis modules, 5 user personas, India-grounded context, expert evaluation frameworks. Produces a current-state report, organised recommendations, and a stakeholder PDF.
> **Who it's for:** Product leaders, PMs, and designers who want a defensible audit of their product (or a competitor's) — not a hot take.
> **How long a run takes:** ~15 min for one module in speed mode · 45-60 min for one module in rigor mode · 2-4 hours for a full 10-module teardown.
> **Author:** Palash Somani (pAI).

---

## What you get from a single run

Every teardown produces three artifacts:

| File | What it is |
|---|---|
| Current-state report (`[app]-current-state-[persona].md`) | Evidence + key issues. Every finding cites a screenshot AND an expert framework. No recommendations yet — pure observation. |
| Recommendations report (`[app]-recommendations-[persona].md`) | Organised by theme (not by module). Quick wins → medium effort → strategic fixes. Expected impact + effort estimate per recommendation. |
| Screenshot manifest (`screenshots/screenshot-manifest.md`) | Every screen captured during the review, systematically named, mapped to module and finding. |

Optionally, you can request a formatted stakeholder PDF on top of these.

**Example output:** see [`samples/duolingo-onboarding/duolingo-onboarding-teardown.pdf`](samples/duolingo-onboarding/duolingo-onboarding-teardown.pdf). That's what a real run produces — Duolingo's onboarding flow, audited against the framework, with screenshots embedded inline at each finding.

---

## Setup (5 minutes)

Full install + first run in the [main README](README.md). The 60-second version:

### 1. Download the folder

Grab pAI-teardown from [github.com/Palash-AI/pAI-teardown](https://github.com/Palash-AI/pAI-teardown) — green **Code** button → **Download ZIP** → unzip somewhere stable.

### 2. Install Claude Desktop

[claude.ai/download](https://claude.ai/download). Sign in.

### 3. Add Mobile MCP (for the automated Android flow)

Claude Desktop → Settings → Developer → Edit Config. Add:

```json
{
  "mcpServers": {
    "mobile": {
      "command": "npx",
      "args": ["-y", "@mobilenext/mobile-mcp@latest"]
    }
  }
}
```

Restart Claude Desktop (Cmd+Q / Alt+F4, not just close the window).

### 4. Tell Claude where the skill is

In a new Claude Desktop chat:

> Load the app-teardown skill from `~/pAI-teardown/skills/app-teardown/SKILL.md` (adjust path to wherever you unzipped). Read it end-to-end. From now on, when I ask for a pAI teardown, follow the STEP 0–8 workflow.

### 5. Boot an Android emulator with the app you want to review

Android Studio → Device Manager → ▶ on your AVD. Install the target app from Play Store (or drag an APK).

---

## Your first teardown — choose one of these three

Type the instruction in plain English to Claude Desktop. The skill recognises the pattern.

### Option A — Audit one module of an app you care about

```
Run a pAI teardown of [app-name] onboarding as new-user
```

Example: *"Run a pAI teardown of Notion onboarding as new-user."*

You'll get the current-state + recommendations + screenshot manifest for the onboarding module, audited from the new-user persona's perspective. Time: ~45 min in rigor mode, ~15 min in speed mode.

### Option B — Quick audit, single module, speed mode

```
Run a pAI teardown of [app-name] homepage as new-user, mode: speed
```

For when you want signal fast — top 3-5 issues, top 3-5 recommendations, ~15 min wall-clock.

### Option C — Full 10-module teardown

```
Run a pAI teardown of [app-name] full as new-user
```

The deep run. All 10 modules. ~2-4 hours of agent work. Best for a product you're seriously evaluating or competing against.

---

## Command grammar

```
/review [app-name] [module] as [persona] (mode: [speed | rigor])
```

| Parameter | Required | Options |
|---|---|---|
| **app-name** | Yes | Any app you can access (Duolingo, Cred, Notion, Stripe, your own product) |
| **module** | Yes | `onboarding`, `homepage`, `discovery`, `personalization`, `content`, `engagement`, `monetization`, `ai`, `cognitive-load`, `persona-alignment`, or `full` |
| **persona** | Yes | `new-user`, `free-user`, `trial-user`, `paid-user`, `lapsed-user` |
| **mode** | Optional | `speed` (15 min, top issues) or `rigor` (45-60 min, comprehensive). Default: rigor. |

---

## The 10 modules (you can audit any one or all)

| Module | What it audits |
|---|---|
| **Onboarding** | First-run experience, time-to-value, signup friction |
| **Homepage & IA** | Information architecture, primary CTA, default navigation |
| **Content consumption** | Reading/viewing/listening experience, completion mechanics |
| **Discovery & search** | Findability, recommendations, search relevance |
| **Engagement & retention** | Habit loops, notifications, streaks, return triggers |
| **Monetization** | Paywall, conversion path, pricing communication |
| **AI integration** | AI surfaces, prompt quality, error handling, transparency |
| **Personalization** | Algorithm transparency, control, relevance signals |
| **Cognitive load** | Mental effort per surface, decision fatigue, clarity |
| **Persona alignment** | How well the product serves each user type |

Run them individually with `/review [app] [module] as [persona]`, or all together with `/review [app] full as [persona]`.

---

## The 5 personas

Each teardown is run from one persona's perspective. Pick the one whose experience you want to understand.

| Persona | Their state |
|---|---|
| `new-user` | First open. No account, no history. Evaluating fit. |
| `free-user` | Has account, uses regularly, hasn't paid. Evaluating value. |
| `trial-user` | In a paid trial. Deciding whether to convert. |
| `paid-user` | Active subscriber. Evaluating retention. |
| `lapsed-user` | Used to be active, hasn't returned. Evaluating winback potential. |

---

## What makes this different from a generic AI audit

| Generic AI critique | pAI-teardown |
|---|---|
| Vibes-based ("looks good", "feels off") | Framework-grounded — every finding cites an expert principle (Nielsen heuristics, Fogg behaviour model, Hooked, etc.) |
| One persona, implicit | Five named personas, explicit. Same product audited from new-user vs lapsed-user produces different findings. |
| Recommendations dumped | Recommendations organised by theme, with effort + impact + dependency |
| Western product defaults | India-grounded context built in (competitor benchmarks, cultural defaults, Tier 2/3 audience considerations) |
| Findings without evidence | Every finding maps to a specific screenshot, named systematically |

---

## Screenshots

For a useful teardown, the agent needs screenshots of the app. The system supports two modes:

1. **You provide screenshots** — drop them into `screenshots/` before running, and the agent references them by filename.
2. **Auto-capture** — if you're on macOS, the screenshot protocol (`screenshot-protocol.md`) walks through capturing screens systematically while you use the app.

The screenshot-protocol.md file in this folder explains both modes.

---

## Sample output

[`samples/duolingo-onboarding/duolingo-onboarding-teardown.pdf`](samples/duolingo-onboarding/duolingo-onboarding-teardown.pdf) is a real sample run. Open it to see:

- How findings are structured (issue + framework citation + screenshot embedded inline)
- How recommendations are themed (not module-by-module dump)
- What a stakeholder-ready PDF actually looks like
- Length: roughly 25-30 pages for a single-module deep teardown

This is what `/review Duolingo onboarding as new-user, mode: rigor` produces. The screenshots in the sample are annotated recreations (clearly banner-marked) — replace with real device captures before redistribution.

---

## Common first-run mistakes (avoid these)

| Mistake | Why it hurts | Fix |
|---|---|---|
| Running `full` mode on your first try | 2-4 hours of agent work, hard to review | Start with one module in speed mode |
| Skipping the persona parameter | Findings get generic | Always specify a persona; rerun from a second persona to see what changes |
| No screenshots | Findings lose evidence | Capture screens before the run, or use the auto-capture protocol |
| Treating recommendations as orders | They're a starting point, not a roadmap | Argue with the recommendations. They're framework-grounded, not your product context. |

---

## File map

```
pAI-teardown/
├── START-HERE.md                    ← you are here
├── Claude.md                        ← agent operating guide
├── README.md                        ← reference / version history
├── appteardown.md                   ← master orchestrator (how a run works)
├── TOKEN-EFFICIENCY-PLAN.md         ← how to run efficiently
├── screenshot-protocol.md           ← screenshot capture guide
├── audit-gap-matrix.md              ← India-groundedness audit findings
├── samples/duolingo-onboarding/     ← sample output (PDF + MD + data.json + screenshots)
├── context/                         ← India consumer context, personas
├── modules/                         ← 10 analysis modules (standard + full)
├── frameworks/                      ← expert evaluation frameworks
├── domains/                         ← domain-specific heuristics
└── output-templates/                ← PDF generation, run logging
```

---

## When to use this vs Manthan

If you came from the Manthan workshop, you have two complementary skills:

| If you're building... | Use |
|---|---|
| A new product from a fuzzy idea | **Manthan** — 7-step sequence, idea → working prototype |
| Auditing an existing product (yours or a competitor's) | **pAI-teardown** — 10-module structured audit with frameworks |

Both share the discipline: structured, evidence-cited, archetype-grounded, India-aware.

---

## Questions

Reply to the email this skill came in, or reach out on LinkedIn.

If you build something interesting with this, I'd love to see it.

— Palash Somani (pAI)

---

*Built with care. Last updated 2026-05-11 for Elevation portfolio distribution.*
