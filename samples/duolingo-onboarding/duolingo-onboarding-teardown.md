# Duolingo — Current State Teardown (Smoke Test)

> **Source of truth for:** Duolingo onboarding (first 5 screens), audited as a **new-user** persona on 2026-05-21
> **Device:** Android emulator — sdk_gphone64_arm64, Android 16, 1080×2400, emulator-5554
> **Mode:** Speed (smoke-test scope — 5 screens, no full module audit)
> **Module covered:** Onboarding & First Value Experience
> **Module score:** 8 / 10 (initial impression; full rigor audit would refine)
> **Frameworks applied:** Fogg MAP · HEART Adoption · Nielsen Heuristics · JTBD · Hook Model
> **India-context lens:** Tier 1-3 budget device users, Hindi-first defaults, ₹ pricing psychology

---

## Scorecard Summary

| Dimension | Score | Status | Anchor |
|---|---|---|---|
| Time to first interaction | 9/10 | Excellent | ~3 seconds from launch to interactive CTA |
| Permission overreach (D0) | 10/10 | Excellent | Zero permission prompts before value (vs many Indian apps asking notification + location on launch) |
| India localisation in default UI | 9/10 | Excellent | Hindi listed first in native-language picker, ahead of English |
| Onboarding expectation-setting | 8/10 | Good | "10 quick questions before your first lesson" — Fogg Motivation-priming done well |
| Branding consistency | 9/10 | Excellent | Duo mascot anchors every screen post-launch; tagline visible on screen 1 |
| Visual hierarchy | 8/10 | Good | Single primary CTA per screen, plenty of whitespace, clear progress bar appears on screen 4 |

**Module score:** 8/10 — Solid. Minor optimization opportunities exist but no critical issues observed in the captured flow.

---

## Module 1 — Onboarding & First Value Experience

### Evidence

**Finding 1 — First-screen value clarity** *(see Screenshot #01)*

- Landing screen shows the Duo mascot, "duolingo" wordmark, and a single-line value prop: "Learn for free. Forever."
- Two CTAs, both clearly labelled and styled distinctly: `GET STARTED` (primary, filled green) and `I ALREADY HAVE AN ACCOUNT` (secondary, outlined).
- No permission requests, no paywall, no language selection forced before the user sees what the app is about.

*Framework — Fogg Behavior Model:* All three pillars are present at the moment the user opens the app. **Motivation** is primed by the explicit free-forever promise (which addresses the single biggest Indian-consumer objection to ed-tech). **Ability** is high — one tap to proceed. **Prompt** is unambiguous — the green CTA. The behaviour (tap GET STARTED) will occur.

*Benchmark:* Many Indian ed-tech apps fire a notification permission within the first 3 seconds, before any value has been demonstrated. Duolingo defers all permission prompts. This is the correct pattern; the Indian audience is highly permission-sensitive after years of aggressive ed-tech apps.

---

**Finding 2 — Character-led emotional anchor** *(see Screenshot #02)*

- After GET STARTED, the user lands on a full-screen Duo mascot with a speech bubble: "Hi there! I'm Duo!". Single `CONTINUE` button.
- This screen does no functional work — it's an emotional setup. It establishes that the onboarding will be guided by a character, not a form.

*Framework — Hook Model (Trigger + Variable Reward):* The mascot is the internal trigger Duolingo cultivates over time. By foregrounding it on the second screen, every subsequent question feels like an interaction with a character rather than a data-collection form. This is a known habit-formation pattern that pays off over weeks of use.

*Benchmark:* Indian apps that lead with a mascot or guide character (PhysicsWallah's teacher-first format, BYJU'S animated explainers) see higher emotional stickiness. Duolingo's approach is consistent with this pattern but more whimsical.

---

**Finding 3 — Explicit length + value commitment** *(see Screenshot #03)*

- Duo speech bubble: "Just 10 quick questions before we start your first lesson!". Single `CONTINUE` button.
- Sets a precise expectation: exactly 10 questions, and the reward is named (first lesson). Zero ambiguity.

*Framework — Nielsen #1 (Visibility of system status):* The user knows up-front how long the flow will take and what they get at the end. This is the right pattern for any flow longer than 2 screens.

*Benchmark:* Most apps don't tell the user the flow length — users abandon at screen 3 because they don't know if there are 5 or 50 more. By pre-committing, Duolingo trades one extra screen for dramatically lower mid-flow abandonment.

---

**Finding 4 — India-aware native-language picker** *(see Screenshot #04)*

- Screen prompts: "What language do you speak?". Six options in this order:
  1. **मैं हिन्दी बोलता/बोलती हूँ** (Hindi, Devanagari script)
  2. **I speak English**
  3. **আমি বাংলা বলি** (Bengali)
  4. **నేను తెలుగు మాట్లాడతాను** (Telugu)
  5. **நான் தமிழ் பேசுவேன்** (Tamil)
  6. **I speak another language**
- A top-bar progress indicator becomes visible (~3% filled).

*Framework — JTBD (Job-To-Be-Done):* The user's job is "learn a language I care about." Asking which language they already speak is the first signal needed to personalise the second-screen course list. Critically, **the question is framed in each respondent's own native script** — a Hindi speaker sees Devanagari, not transliterated Roman text.

*India context — strong signal:* Hindi is the first option in the list, ahead of English. This is unusual for a global product — most international apps default English to the top, then offer regional languages as alternatives. Duolingo's choice signals genuine market commitment to India. Plus the four southern Indian languages (Bengali, Telugu, Tamil, all in native scripts) before the catch-all "another language" option.

*Benchmark:* Compare to Spotify or Netflix on first install in India — both default to English and require the user to dig into Settings to find Hindi. Duolingo's first-screen Hindi prioritisation is closer to Meesho's Hindi-first onboarding, which drove its Tier 2-3 dominance.

---

**Finding 5 — Course picker with India in the top 3** *(see Screenshot #05)*

- After selecting "I speak English", the user lands on "What would you like to learn?" under section header "For English speakers".
- Course list ordering (top to bottom):
  1. Intermediate English
  2. **Chess** *(non-language course — notable)*
  3. **Hindi** *(India context)*
  4. German
  5. Japanese
  6. French
  7. Spanish

*Framework — JTBD + Reforge growth-loop:* The course list is recommended based on the previous answer (native-language = English). This is server-side personalisation done at the right moment — after the user has self-identified, before they've felt any friction.

*India context:* Hindi appears 3rd in the learnable-course list for English speakers, ahead of the historically-default European languages (German, French, Spanish) and Japanese. This is editorial product judgment — Duolingo's growth team has decided Hindi is a high-conversion course for English speakers (likely targeting both India-resident Hindi-learners and the Indian diaspora). Worth tracking for any Indian ed-tech competitor evaluating Duolingo's market positioning.

*Notable non-language signal:* Chess as the 2nd course — Duolingo has begun expanding beyond language learning. Any competitor benchmarking against Duolingo should know this isn't a language-only product anymore.

---

### Key Issues (none critical from this 5-screen sample)

| # | Issue | Severity | Framework |
|---|---|---|---|
| 1 | Two consecutive Duo-mascot screens (#02 + #03) could be consolidated into one if testing shows the welcome screen doesn't add measurable engagement. Borderline — likely an A/B test outcome at scale. | LOW | Nielsen #8 (Aesthetic and minimalist design) |
| 2 | No language-detection from device locale — every user must tap their language manually. On budget Android devices in Tier 2-3 India, the device locale is often Hindi already; pre-selecting based on locale would shave one screen. | LOW | Fogg Ability (reduce friction) |
| 3 | Light onboarding-progress visibility — the top bar appears on screen 4 but isn't shown on screens 2-3. Adding it from screen 2 would tell the user "this flow has a defined end." | LOW | Nielsen #1 (Visibility of system status) |

**No critical or high-severity issues observed in the captured 5-screen sample.** A full rigor audit covering all 10+ onboarding screens (motivation quiz, daily-goal, first-lesson, notification-permission, paywall) would be needed to score the full module conclusively.

---

## Scope note

This is a **speed-mode smoke test** — 5 screens covering the first ~30 seconds of the new-user flow. It validates the pipeline mechanics (capture, naming, manifest, report generation, inline screenshot embedding) end-to-end on a fresh machine running Mobile MCP for the first time. A full rigor audit would cover ~15 onboarding screens and score every dimension defined in `modules/full/onboarding.md`.

---

## Sources

- Captures: `screenshots/duolingo-smoketest/img/01–05`
- Manifest: `screenshots/duolingo-smoketest/screenshot-manifest.md`
- Frameworks referenced: `frameworks/expert-frameworks.md` (Fogg MAP, Hook Model, Nielsen Heuristics, JTBD)
- India context applied: `context/india-consumer.md`, `context/india-product-strategy.md`
- Reviewer: Claude (Sonnet 4.6) driving Mobile MCP from Claude Code on macOS
