# Screenshot Protocol — pAI Teardown Skill

> **Purpose:** Ensure every screenshot taken during a teardown is (a) captured, (b) saved into the right folder with the right filename, and (c) embedded inline in the generated PDF at the right finding.
> **Read this once before any teardown.** It's short.

---

## TL;DR

1. Screenshots live in `screenshots/[run-id]/img/` inside this skill's folder. Example: `screenshots/duolingo-onboarding-2026-05/img/01-language-pick-new-user.png`.
2. Naming convention: `[##]-[screen-name]-[persona].png` (e.g. `03-paywall-d0-new-user.png`).
3. Maintain a `screenshot-manifest.md` alongside the images.
4. The PDF generator picks up images by exact filename from your data file and embeds them inline in the corresponding evidence card. If a file is missing it renders a visible "MISSING SCREENSHOT" placeholder so you can fill the gap.

---

## How screenshots get captured (three modes)

### Mode A — You drop them in yourself (zero setup, works everywhere)

Just put PNGs into `screenshots/[run-id]/img/` before or during the run, using the naming convention. The agent references them by filename.

Capture sources:
- macOS: `Cmd+Shift+4` (region) or `Cmd+Shift+5` (window/recording)
- Windows: Win+Shift+S
- Linux: `gnome-screenshot -a` or Flameshot
- Mobile: phone's native screenshot, then AirDrop / Google Photos / cable transfer

### Mode B — Agent uses macOS `screencapture` for browser/web apps

If the app being audited is a web app, the agent can capture browser tabs via the Claude in Chrome MCP (`mcp__Claude_in_Chrome__computer` with `action: "screenshot"`, `save_to_disk: true`). Files land in the temp folder; the agent then `mv`s them into `screenshots/[run-id]/img/` with the right filename.

### Mode C — Agent drives a real device / emulator via Mobile MCP

For mobile apps. Requires Mobile MCP installed (see README "Path 3 — With live device automation").

```
mobile_save_screenshot(
  "[your-workspace]/screenshots/[run-id]/img/[##]-[screen-name]-[persona].png"
)
```

If your filesystem layout puts the workspace on a shared mount (Cowork or Docker), make sure the mobile MCP and the PDF generator see the *same* path — easiest way is to use absolute paths everywhere.

> **Tip — handshake test:** before capturing in earnest, save one screenshot, then confirm the file exists from the side that will later read it (the PDF generator). If it does, you're good. If not, fall back to Mode A and copy files manually.

---

## Naming convention

```
[##]-[screen-name]-[persona].png
```

| Part | Format | Example |
|------|--------|---------|
| Sequence | 2-digit number | `01`, `02`, `03` |
| Screen name | Lowercase hyphenated | `language-pick`, `home-feed`, `paywall-d0` |
| Persona | Short label | `new-user`, `free-user`, `trial-user`, `paid-user`, `lapsed-user` |

**Examples:**
- `01-language-pick-new-user.png`
- `02-motivation-quiz-new-user.png`
- `03-first-lesson-new-user.png`
- `04-streak-celebration-new-user.png`
- `05-paywall-d3-free-user.png`

---

## Manifest

Maintain `screenshots/[run-id]/screenshot-manifest.md` as you capture. Template:

```markdown
| # | Filename | Screen | Module(s) | Key Observations |
|---|----------|--------|-----------|-----------------|
| 01 | 01-language-pick-new-user.png | Language picker | Onboarding | No signup wall — value-first |
| 02 | 02-motivation-quiz-new-user.png | "Why are you learning?" | Onboarding | 4-tap commitment |
```

This file is one of the three required outputs of every teardown run (alongside the current-state and recommendations markdown files).

---

## Screenshot rules

1. **Every screen navigated = one saved screenshot.** No exceptions.
2. **Save immediately** — never defer saving to end of session. If you do, you'll lose state and have to rerun.
3. **One screenshot can serve multiple modules.** Homepage may be evidence for Onboarding AND Homepage IA — embed in both PDF sections, reference once in the manifest.
4. **Volume is driven by evidence, not a preset count.** Speed mode: 3–5 per module. Rigor mode: 8–15 per module.
5. **Phone-portrait orientation** for mobile apps. For web/desktop, capture the visible-area screen (don't full-page scroll-stitch — it makes PDF embedding awkward).

---

## How screenshots end up inline in the PDF

The PDF generator (`output-templates/generate_pdf.py`) reads your data JSON, finds each `evidence_card`'s `screenshot` filename, looks it up in `screenshots/[run-id]/img/`, and embeds it inline next to the analysis text (left column: image, right column: observations + framework citation).

**If the file is missing**, the generator draws a clearly-marked red "MISSING SCREENSHOT" placeholder box with the expected filename written inside it, plus a `⚠️ MISSING SCREENSHOT` line to stdout. You know exactly which file to add and re-run.

**Path resolution** — paths are relative to `output-templates/generate_pdf.py`. The default screenshot directory is `<this-skill-folder>/screenshots/img/`. To override (e.g. for a per-run subfolder), either:

```bash
# via env var
SCREENSHOT_DIR=/abs/path/to/screenshots/img python output-templates/generate_pdf.py --data my-run.json

# OR via data JSON
{ ..., "screenshot_dir": "/abs/path/to/screenshots/img", ... }
```

Never hardcode session-specific or username-specific paths inside `generate_pdf.py` itself — those will break the moment someone else uses the skill.

---

## Quick reference

| Situation | Action |
|-----------|--------|
| Solo run, manual screenshots | Mode A. Drop PNGs into `screenshots/[run-id]/img/`. |
| Web app | Mode B. Browser MCP → temp → `mv` into `screenshots/[run-id]/img/`. |
| Mobile app, live automation | Mode C. `mobile_save_screenshot` direct to `screenshots/[run-id]/img/`. |
| Shared filesystem mount | Use absolute paths; run a handshake test before the real capture. |
| PDF shows MISSING placeholders | Filename mismatch between data JSON and disk. Fix and re-run. |
