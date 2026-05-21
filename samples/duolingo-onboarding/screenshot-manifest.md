# Screenshot Manifest — Duolingo Onboarding (Smoke Test)

> **App:** Duolingo (com.duolingo)
> **Persona:** new-user
> **Module:** onboarding
> **Mode:** speed (smoke test — 5 screens, ~3 minutes of capture)
> **Device:** Android emulator (sdk_gphone64_arm64, Android 16, 1080×2400, emulator-5554)
> **Date:** 2026-05-21
> **Capture tool:** Mobile MCP (`@mobilenext/mobile-mcp` via npx) driven from Claude Code

| # | Filename | Screen | Module(s) | Key Observations |
|---|----------|--------|-----------|-----------------|
| 01 | `01-launch-new-user.png` | Landing / first open | Onboarding | Duo mascot animation; tagline "Learn for free. Forever."; two CTAs (`GET STARTED` for new users, `I ALREADY HAVE AN ACCOUNT` for returning). No permission prompts. No paywall. Brand-clear in <3 seconds. |
| 02 | `02-welcome-duo-new-user.png` | Mascot welcome | Onboarding | Full-screen Duo character with speech bubble "Hi there! I'm Duo!". Single `CONTINUE` button. Establishes the character that anchors the rest of the onboarding. |
| 03 | `03-quiz-intro-new-user.png` | Quiz intent-set | Onboarding | Duo speech bubble: "Just 10 quick questions before we start your first lesson!". Sets expectation for length and explicitly commits to value (first lesson) at the end. Single `CONTINUE`. |
| 04 | `04-language-picker-new-user.png` | Native-language picker | Onboarding · Personalization | "What language do you speak?" — options ordered: Hindi (Devanagari), I speak English, Bengali, Telugu, Tamil, I speak another language. **Hindi listed first**, ahead of English — strong India localisation signal. Top progress bar appears (~3% filled). |
| 05 | `05-course-picker-new-user.png` | Learn-course picker | Onboarding · Personalization | "What would you like to learn?" — section header "For English speakers". Courses listed in order: Intermediate English, Chess, Hindi, German, Japanese, French, Spanish. **Hindi listed 3rd**, ahead of European/Asian language defaults. Chess is a notable non-language course offering. |

---

## Capture summary

- Total screens captured: **5** (target was 3-5 for smoke test)
- Total wall-clock time: **~3 minutes** (target was <15 minutes for speed mode)
- All screens saved to: `screenshots/duolingo-smoketest/img/`
- Naming convention: `[##]-[screen-name]-[persona].png` ✅
- Every screen mapped to ≥1 module and has ≥1 key observation ✅

## Pipeline verification

| Check | Status |
|---|---|
| ADB sees emulator (`adb devices`) | ✅ `emulator-5554` online |
| Mobile MCP can launch app | ✅ launched via `mobile_launch_app` |
| Mobile MCP can capture + save screenshots | ✅ 5/5 PNGs saved to correct path |
| Mobile MCP can list on-screen elements | ✅ used to navigate via coordinates |
| Mobile MCP can tap at coordinates | ✅ 5 taps executed successfully |
| File naming convention applied | ✅ all 5 files match `[##]-[screen-name]-[persona].png` |
| Screen content matches expected onboarding flow | ✅ landing → welcome → quiz-intent → language → course |
