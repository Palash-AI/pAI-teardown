# pAI Teardown Plugin — Setup & Usage Guide

**Version:** 1.1.0
**Built by:** [Palash Somani](https://www.linkedin.com/in/palash-somani-artificial-intelligence/)

---

## What Is This?

**pAI Teardown** is a structured UX audit system you run inside Claude Desktop. It lets any PM, designer, or researcher run a rigorous, framework-backed review of any mobile app — in minutes, not days.

Every review produces:
- A **Current State file** — scored evidence, issues, screenshot-referenced findings (no recommendations — just facts)
- A **Recommendations file** — high-level AI-generated feature recommendations
- A **Screenshot Manifest** — every screen captured, named, and mapped to findings
- An optional **Stakeholder PDF** — consulting-grade report with embedded screenshots

It covers **10 UX modules** (onboarding, homepage, discovery, personalization, content, engagement, monetization, AI, cognitive load, persona alignment) and is grounded in **10 expert frameworks** (HEART, Hook Model, Nielsen, JTBD, Fogg, Reforge, Norman, Kano, AARRR, Cagan) — with built-in India consumer benchmarks.

---

## Prerequisites

Before installing, make sure you have the following:

### 1. Claude Desktop App
- Download from: https://claude.ai/download
- Sign in with your work or personal Claude account
- Make sure you're on the latest version (Settings → check for updates)

### 2. Node.js (for Mobile MCP — required for automated screenshots)
- Download from: https://nodejs.org (v18+ recommended)
- Verify: `node --version` in your terminal — you should see a version like `v20.10.0`

### 3. Android Studio + Emulator (for automated app navigation)
- Download from: https://developer.android.com/studio
- After installing, create an **Android Virtual Device (AVD)**:
  1. Open Android Studio → **Device Manager** (right sidebar or Tools menu)
  2. Click **Create Device**
  3. Choose a phone (e.g., Pixel 6) and a system image (API 33+ recommended)
  4. Click **Finish** → then click the ▶ Play button to start the emulator
- Install the app you want to review on the emulator:
  - **Apps with a Play Store listing:** open the Play Store inside the emulator, sign in, install the app like on a real phone
  - **Apps shared as APKs:** drag the `.apk` file onto the running emulator window — it installs automatically
- **Verify the emulator is reachable via ADB (Android Debug Bridge):**
  ADB is the command-line tool that talks to Android devices and emulators. Mobile MCP uses it under the hood. ADB ships with Android Studio's "Platform Tools" SDK component.

  With your emulator running, open a terminal and run:

  ```bash
  adb devices
  ```

  You should see output like:

  ```
  List of devices attached
  emulator-5554   device
  ```

  If you instead get `command not found: adb`, ADB isn't on your PATH yet. Add it:

  - **macOS / Linux** — add this line to `~/.zshrc` (zsh) or `~/.bashrc` (bash):
    ```bash
    export PATH="$PATH:$HOME/Library/Android/sdk/platform-tools"
    ```
    On Linux, the path is typically `$HOME/Android/Sdk/platform-tools`. Run `source ~/.zshrc` (or `~/.bashrc`) to reload.
  - **Windows** — Settings → System → About → Advanced system settings → Environment Variables → edit `Path` → add `%LOCALAPPDATA%\Android\Sdk\platform-tools`. Restart your terminal.

  Re-run `adb devices` after fixing PATH. You must see your emulator listed before moving on — if ADB can't see it, Mobile MCP won't either.

> **Note:** You do NOT need Android Studio if you're doing manual reviews (providing screenshots yourself). Mobile MCP is only required for automated navigation.

---

## Installation: Step-by-Step

### Step 1 — Download pAI-teardown from GitHub

The plugin is open and free.

1. Open https://github.com/Palash-AI/pAI-teardown in your browser
2. Click the green **Code** button → **Download ZIP**
3. Unzip the archive somewhere stable on your machine. Example: `~/pAI-teardown/` on macOS / Linux, or `C:\Users\<you>\pAI-teardown\` on Windows
4. Don't leave it in `Downloads/` — pick a folder you won't accidentally clean up

> **Alternative (for the technically-inclined):** clone the repo with git so you can pull future updates later:
> ```bash
> git clone https://github.com/Palash-AI/pAI-teardown.git ~/pAI-teardown
> ```

### Step 2 — Open Claude Desktop

Open the Claude Desktop app and start a new conversation.

### Step 3 — Load the Skill into Claude Desktop

Claude Desktop reads the skill straight from the folder you just downloaded — there's no plugin install step.

In your new conversation, send this message (replace the path with wherever you unzipped to):

```
Load the app-teardown skill from ~/pAI-teardown/skills/app-teardown/SKILL.md
end-to-end, plus ~/pAI-teardown/appteardown.md for the deep spec.
From now on, when I ask for a pAI teardown, follow the STEP 0–8 workflow
defined in that skill.
```

Claude will read the skill files and confirm it's ready.

> **Tip:** If you use Claude Desktop's project / workspace feature, drop the `pAI-teardown/` folder into a project once. Future conversations in that project will already have the skill loaded — you won't need to re-do Step 3 every time.

### Step 4 — Set Up Mobile MCP (for Automated Screenshots)

Add Mobile MCP to your Claude Desktop configuration:

1. Open Claude Desktop → **Settings** → **Developer** → **Edit Config**
2. This opens the `claude_desktop_config.json` file in your text editor
3. Add the following inside the `"mcpServers"` block (or create the block if it doesn't exist):

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

4. Save the file and **fully quit and restart Claude Desktop** (Cmd+Q on macOS / Alt+F4 on Windows — not just close the window)
5. Open your Android emulator (from Android Studio Device Manager) and install the app you want to review

**Verify the install in two layers:**

> **Layer 1 — ADB sees the emulator (OS level):** in a terminal, run `adb devices`. You should see your emulator listed (e.g. `emulator-5554   device`). If you don't, the emulator isn't running or ADB isn't on your PATH — fix that first (see Prerequisites §3). Mobile MCP can't work if ADB can't see the device.
>
> **Layer 2 — Mobile MCP sees the emulator (Claude level):** After restarting Claude Desktop, start a new conversation and type: `list available mobile devices`. Claude should return a list including your running emulator. If Layer 1 passes but Layer 2 fails, the issue is Mobile MCP / Claude Desktop config — not your emulator.

### Step 5 — Verify Installation

In a new Claude Desktop conversation (with the skill loaded — see Step 3), type:

```
Run a pAI teardown of Duolingo onboarding as new-user, mode: speed
```

Claude should:
- Confirm the parameters with you
- List your emulator as the connected device
- Launch Duolingo automatically
- Navigate the onboarding flow, capturing ~3–5 screenshots
- Produce a current-state file + recommendations file + screenshot manifest in the `pAI-teardown/` folder

If you see all three output files, the install is working end-to-end. You can now run any other app, module, or persona.

---

## Using the Plugin

### Basic Command

Type this to Claude Desktop in plain English. The skill recognises the pattern.

```
Run a pAI teardown of [app-name] [module] as [persona], mode: [speed | rigor]
```

### Examples

```
Run a pAI teardown of Duolingo onboarding as new-user
Run a pAI teardown of Notion monetization as trial-user, mode: speed
Run a pAI teardown of Cred full as free-user, mode: rigor
Run a pAI teardown of Netflix engagement as paid-user
```

### Parameters

| Parameter | Required | Options |
|-----------|----------|---------|
| **App name** | Yes | Any app you can install on the emulator (Duolingo, Notion, Cred, your own product, a competitor) |
| **Module** | Yes | `onboarding`, `homepage`, `discovery`, `personalization`, `content`, `engagement`, `monetization`, `ai`, `cognitive-load`, `persona-alignment`, or `full` |
| **Persona** | Yes | `new-user`, `free-user`, `trial-user`, `paid-user`, `lapsed-user` |
| **Mode** | Optional | `speed` (≈15 min, top issues) or `rigor` (≈45-60 min, comprehensive). Default: `rigor` |

---

## The 10 Review Modules

| # | Module | What It Covers | Key Frameworks |
|---|--------|----------------|---------------|
| 1 | `onboarding` | First-run flow, time-to-value, friction | Fogg MAP, HEART Adoption |
| 2 | `homepage` | IA, navigation, visual hierarchy | Nielsen, Norman, Kano |
| 3 | `discovery` | Search, browse, content surfacing | JTBD, Nielsen Recognition |
| 4 | `personalization` | Recommendation quality, relevance | Hook Model, Reforge |
| 5 | `content` | Consumption UX, player, reader | JTBD, Norman Feedback |
| 6 | `engagement` | Retention loops, habit formation | Hook Model, Reforge Retention |
| 7 | `monetization` | Paywall UX, upgrade flows, pricing | Reforge, Fogg MAP, AARRR |
| 8 | `ai` | AI feature integration, discoverability | JTBD, HEART, Kano |
| 9 | `cognitive-load` | Visual clarity, decision fatigue | Nielsen, Norman, Fogg Ability |
| 10 | `persona-alignment` | Whether the app serves the user's job | JTBD, Cagan, Fogg MAP |

---

## Scoring Scale

| Score | Label | What It Means |
|-------|-------|---------------|
| 1–2 | Critical | Fundamentally broken. Fix immediately. |
| 3–4 | Poor | Significant issues. High-priority. |
| 5–6 | Below Average | Functional but behind competitors. |
| 7–8 | Good | Solid, with minor optimization opportunities. |
| 9–10 | Excellent | Best-in-class. Benchmark-worthy. |

Each score is backed by a specific framework citation and a competitive benchmark (e.g., "Duolingo reaches first lesson in 60 sec; this app takes 4 minutes").

---

## Adding Context for Your App (Recommended)

For the most relevant reviews of an app you own, add a `[your-app]-context.md` file to the `context/` folder inside `pAI-teardown/`. This context file teaches Claude about:
- Your product goals and north star metrics
- User personas (your actual ones, with names)
- Past review history
- Squad structure and ownership

If the file already exists, the skill will auto-load it at the start of every review of that app. After each review, Claude auto-appends findings to this file, so it learns over time.

**Template structure** for a context file:
```markdown
# [App Name] Context

## Product Overview
...

## Key Metrics (North Star, L28, etc.)
...

## Personas
...

## Review History
(auto-appended by the skill after each review)
```

---

## Adding a New Domain

The plugin ships with an **education domain** reference (`domains/education.md`) containing benchmarks from Duolingo, Coursera, Khan Academy, Unacademy, etc.

To add a new domain (e.g., OTT, Finance, E-commerce):
1. Create a file: `domains/[domain].md`
2. Include: domain-specific heuristics, best-in-class benchmarks with real metrics, common failure modes, key metrics
3. The orchestrator will auto-detect and load it based on the app type

---

## Running Without an Emulator (Manual Mode)

If you don't have Android Studio set up, you can still run full reviews by providing screenshots manually:

1. Take screenshots of the app on your phone or any device
2. Drop them into `pAI-teardown/screenshots/[run-id]/img/` using the naming convention from `screenshot-protocol.md` — e.g. `01-splash-new-user.png`, `02-home-new-user.png`
3. Tell Claude: `Run a pAI teardown of [app] [module] as [persona] — screenshots are already in screenshots/[run-id]/img/`

Claude will use the provided screenshots as evidence and still produce the full structured output.

---

## Output Files

All review outputs are saved to your `pAI-teardown/` folder:

| File | Description |
|------|-------------|
| `[app]-current-state-[persona].md` | Evidence + scored issues (no recs) |
| `[app]-recommendations-[persona].md` | High-level AI-generated feature recommendations |
| `screenshots/[run-id]/screenshot-manifest.md` | All screenshots mapped to findings |
| `[app]-teardown-[date].pdf` | (On request) Full consulting-grade PDF with embedded screenshots |
| `context/[app]-context.md` | Auto-updated after each review |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Claude doesn't seem to know about pAI teardown | Re-do Step 3: send the "Load the app-teardown skill from..." message at the start of the conversation. Claude Desktop loads context per-conversation. |
| Mobile MCP not connecting | First, isolate the layer: run `adb devices` in a terminal. If it doesn't list the emulator, the problem is OS-level (see the two `adb` rows below). If it does list the emulator but Claude still can't see it, ensure the emulator was running BEFORE you started the Claude conversation, and **fully quit and restart Claude Desktop** (Cmd+Q / Alt+F4) after editing the MCP config — closing the window isn't enough. Verify `npx --version` works in a terminal. |
| `adb devices` shows no devices | The emulator isn't actually running — go back to Android Studio → Device Manager → ▶. If it's already running but ADB still shows nothing, restart the ADB server: `adb kill-server && adb start-server`, then run `adb devices` again. |
| `command not found: adb` | ADB isn't on your PATH. Either call it by its full path (macOS default: `~/Library/Android/sdk/platform-tools/adb devices`) or add platform-tools to PATH — see Prerequisites §3. |
| App not found on emulator | Install via Play Store (signed in) or drag the `.apk` onto the running emulator window |
| Screenshots failing to save | Claude will fall back to `/tmp/` and copy to the project folder automatically. If issues persist, run a handshake test (see `screenshot-protocol.md`). |
| `ModuleNotFoundError: reportlab` when generating PDF | Run `pip install reportlab Pillow` (or `pip3`) — needed only for PDF output |
| PDF fonts look like Times / Courier | Install Poppins + Lato from https://fonts.google.com — double-click each `.ttf` to install |
| Unknown domain | Claude will use general frameworks only; add a domain file (see "Adding a New Domain") to improve results |
| Review feels generic | Add a `[app]-context.md` file to `context/` with app-specific metrics and personas |
| Newer release on GitHub | `cd` into your folder and `git pull` (if you cloned), or re-download the ZIP and replace. Re-do Step 3 so Claude reloads the skill. |

---

## Privacy & Data

- All reviews run **locally within your Claude session** — no data is sent to third-party services
- Screenshots are saved to your local workspace folder only
- The `[app]-context.md` file is stored in your local folder and is only accessible to you

---

## Feedback & Improvements

This plugin was built by [Palash Somani](https://www.linkedin.com/in/palash-somani-artificial-intelligence/) and is actively evolving. If you:
- Find a bug or unexpected behaviour → DM Palash on LinkedIn
- Want to add a new module or domain → see "Adding a New Domain" above
- Want to add a new competitor benchmark → edit the relevant `modules/[module].md` file directly

---

*Built with 10 expert frameworks, 10 review modules, India consumer context, and education domain benchmarks. v1.1.0*
