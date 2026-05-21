# Onboarding & First Value Experience

> AARRR: Activation | Frameworks: Fogg MAP, HEART, AARRR, JTBD, Hook Model, Nielsen, Norman, Kano | Speed: 20min | Rigor: 90min

<!-- SPEED MODE -->
## QUICK AUDIT
Navigate: 1. App Store Listing 2. Splash/Load 3. Auth Flow 4. Permission Requests 5. Onboarding Quiz 6. Paywall 7. First Content Screen 8. First Core Interaction
Check: Time from app open to first value (target <60 sec), Paywall timing (before or after value), Personalization visibility (present and used)
Score anchor: 9-10 = <60 sec to value + personalization visible + paywall after, 7-8 = 60-120 sec to value + good feedback, 5-6 = 120-300 sec to value + some friction, 3-4 = 5-15 min to value + paywall early, 1-2 = >15 min or unreachable without payment
<!-- END SPEED MODE -->

## SCREENS TO NAVIGATE

### 1. App Store Listing
**Observe:**
- Icon design and memorability — does it stand out?
- Headline clarity — does it answer "what is this for?"
- Key screenshots order — does core feature appear first?
- Ratings and review sentiment — signal of onboarding success/failure?
- CTA button and category classification

**Screenshot:** Full listing (icon, name, tagline), first 2-3 key screenshots, rating/review summary

**Framework check:** JTBD → Do marketing copy and initial screenshots clearly promise the job the user hired this app for?

---

### 2. Splash Screen / Loading
**Observe:**
- Load time — seconds until interactive
- Branding consistency — logo/color match app store listing?
- Loading state clarity — progress indicated or skeleton screens shown?
- Animation quality — premium or generic?

**Screenshot:** Splash screen as it appears, timeline of load sequence

**Framework check:** Nielsen #1 → Is brand impression professional and does user feel confident they opened the right app?

---

### 3. Login / Signup Flow
**Observe:**
- Welcome screen — explains why login required? Guest/skip option?
- Email/phone entry — single field or multi-step? Error handling clarity?
- Password entry — requirements shown upfront? Strength indicator?
- OTP/verification — timing explained? Easy resend?
- Profile completion — mandatory vs. optional fields? All at once or field-by-field?
- Can user see any value before completing auth?

**Screenshot:** First auth screen, each step, error states, success confirmation

**Framework check:** Fogg MAP → Is Ability high (clear instructions, simple form) and Motivation explained (why login required)?

---

### 4. Permission Requests
**Observe:**
- Trigger — when does request appear? (On app open or on feature access?)
- Messaging — explains WHY the app needs this and WHAT VALUE user gets?
- Denial handling — what happens if user denies? Can they continue? Re-request?
- Sequence — which permissions first/last? (Camera before contacts? Notifications last?)
- Typical to check: Notifications, Location, Camera, Contacts, Microphone, Calendar, Health data

**Screenshot:** Each permission dialog, pre-permission education screens, denial states

**Framework check:** Nielsen #3 + Fogg MAP → Permissions reduce Ability (friction) and Motivation (interruption). Are they contextualized?

---

### 5. Onboarding Quiz / Interest Selection
**Observe:**
- Timing — before or after showing core feature?
- Length — how many questions? (Sweet spot: 3-7)
- Relevance — do questions probe JTBD or just collect demographics?
- Personalization impact — results shown immediately? Does app change based on answers?
- Progress indicator — user sees how many questions remain?

**Screenshot:** Quiz intro, 2-3 representative questions, results screen, first content screen after quiz

**Framework check:** JTBD → Questions should probe the job, not demographics. Are answers directly tied to content personalization?

---

### 6. Paywall / Trial Prompt
**Observe:**
- Timing — before, during, or after first value moment?
- Framing — positive (what you GET) or negative (what you LOSE)?
- Pricing clarity — single tier or multiple? Price in local currency? Annual vs. monthly?
- Trial option — offered? Duration clear?
- Escape hatch — can user skip/dismiss easily?
- Social proof — ratings, subscriber count, guarantee?

**Screenshot:** First paywall screen, pricing table, trial terms, dismiss button

**Framework check:** Fogg MAP + AARRR → Paywall before value = low motivation + blocked ability = activation failure. Ideal: show value before asking for money.

---

### 7. First Content Screen
**Observe:**
- Clarity — can user identify core feature immediately? Clear focal point?
- Signifiers (Norman) — are CTAs visually distinct? Do buttons look clickable?
- Empty state — sample content or blank? (Blank = higher friction)
- Guidance — instructional copy, tooltips, walkthroughs?
- Navigation — can user understand how to navigate the app?
- Cognitive load — is screen simple or crowded?

**Screenshot:** Full screen view, tooltips as revealed, navigation options, empty state or placeholder content

**Framework check:** Nielsen #1 + Norman → Does this screen make what the app does immediately clear? Do interactive elements signal their function?

---

### 8. First Interaction with Core Feature
**Observe:**
- Interaction ease — how many taps/inputs to perform meaningful action?
- Feedback — does app respond instantly and clearly?
- Outcome — is result what user expected? Does it deliver the promised job?
- Delight — any delightful surprise? Animation, progress, celebration?
- Friction points — does app request additional data, permissions, or sign-ups before showing result?

**Screenshot:** Screen state BEFORE user taps primary CTA, immediately AFTER completion, celebration screen if present, first result

**Framework check:** Fogg MAP + Hook Model → This is the critical Ability × Motivation moment. Does Action → Variable Reward cycle work? Is reward clear and variable?

---

## SCORING RUBRIC

| Score | Label | Key Criteria |
|-------|-------|-------------|
| 9-10 | Best-in-class | Time to value <60 sec, paywall after demonstrating core value, proactive + visible personalization, contextualized permissions, immediate feedback, <5 screens, graceful error handling, zero dark patterns |
| 7-8 | Good | Time to value 60-120 sec, paywall after first value, some personalization present, <2 permission requests before value, clear feedback, 5-8 screens, minimal friction |
| 5-6 | Adequate | Time to value 120-300 sec, paywall present but not blocking, minimal/generic personalization, multiple early permission requests (deferrable), basic error handling, 8-12 screens, 2-3 friction points |
| 3-4 | Poor | Time to value 5-15 min, paywall blocks free functionality, no personalization, aggressive permission sequence, unclear feedback, 12-20+ screens, 4+ friction points |
| 1-2 | Critical | Time to value >15 min or unreachable without payment, paywall at app open, no personalization, all permissions upfront, no feedback, 20+ screens, 6+ friction points, broken flows |

**Scoring method**: Start at 5 (baseline). Add: +2 for <60 sec time-to-value, +1 personalization visible, +1 paywall after, +1 <2 permissions before, +1 clear success feedback, +1 <5 screens, +1 zero dark patterns, +1 graceful errors. Deduct: -2 for >5 min time-to-value, -3 paywall before value, -1 no personalization, -1 all permissions upfront, -1 unclear feedback, -1 rating prompt too early, -2 suspicious permissions. Cap at 1-10.

---

## EVIDENCE CHECKLIST

### Timing Metrics
- [ ] Time from app tap to splash screen visibility (seconds) — Framework: Nielsen #1
- [ ] Time from splash to first interactive screen (seconds) — Framework: Nielsen #1
- [ ] Time from app open to first content screen (seconds) — Framework: Fogg MAP
- [ ] Time from first content screen to first core interaction (seconds) — Framework: Hook Model
- [ ] TOTAL time from app open to first value moment (seconds) — KEY METRIC — Framework: Fogg MAP + AARRR
- [ ] Time spent in onboarding quiz if present (seconds) — Framework: JTBD
- [ ] Time between permission requests if multiple (seconds) — Framework: Nielsen #3

### Interaction Counts
- [ ] Number of screens before first core interaction — Framework: Fogg MAP (complexity)
- [ ] Number of taps/inputs to reach first value moment — Framework: Fogg MAP (ability)
- [ ] Number of permission request dialogs shown — Framework: Nielsen #3
- [ ] Number of interrupts before first value (ratings, subscriptions, etc.) — Framework: Kano

### Permission Audit
- [ ] List of all permissions requested in order (Notifications, Location, Camera, ...) — Framework: Fogg MAP, Nielsen #3
- [ ] Time elapsed before first permission request (seconds after app open) — Framework: Fogg MAP
- [ ] For each permission: user choice (Allow / Don't Allow / Maybe Later) — Framework: Nielsen #3
- [ ] Context provided for each permission? (Yes / No / Minimal) — Framework: Norman (signifiers)
- [ ] Cumulative permission friction score (1-5 scale) — Framework: Fogg MAP

### Personalization Audit
- [ ] Personalization type: None / Demographic / JTBD-based / Behavioral — Framework: JTBD
- [ ] Number of questions asked if applicable — Framework: JTBD
- [ ] Sample questions paraphrased (capture exact wording if possible) — Framework: JTBD
- [ ] Personalization visible on first content screen? (Yes / No / Partially) — Framework: Kano
- [ ] How explicitly personalization acknowledged? (e.g., "We found X for you") — Framework: Norman

### Paywall Audit
- [ ] Paywall present? Yes / No — Framework: AARRR
- [ ] Timing of first paywall (at app open / after login / after onboarding / on premium feature access / after X min) — Framework: AARRR
- [ ] Paywall position relative to first value (Before / During / After / Never) — Framework: Fogg MAP
- [ ] Free tier available? Yes / No / Is it usable? — Framework: AARRR
- [ ] Trial offered? Yes / No. Duration: _____ days — Framework: AARRR
- [ ] Pricing tiers shown: count _____ / Clarity (1-5): _____ / Local currency: Yes / No — Framework: AARRR
- [ ] Paywall messaging tone (Value-focused / Loss-averse / Neutral) — Framework: Norman
- [ ] Escape hatch visible? (Yes / Easily / Obscurely / No) — Framework: Nielsen #3

### Authentication Audit
- [ ] Authentication methods offered (Email / Phone / Social / Biometric / Guest) — Framework: Fogg MAP
- [ ] Number of steps to complete auth: _____ — Framework: Fogg MAP
- [ ] Time to complete auth: _____ seconds — Framework: Fogg MAP
- [ ] Data requested at each step (email, password, full name, DOB, etc.) — Framework: JTBD
- [ ] Reason for each data request explained? (Yes / No / Some) — Framework: JTBD
- [ ] User can see value before completing auth? (Yes / No / Limited preview) — Framework: Fogg MAP
- [ ] Account recovery (forgot password) path clear? — Framework: Nielsen #5

### First Interaction / Value Moment
- [ ] What is the core feature interaction? (e.g., "Create first note", "Send first message") — Framework: JTBD
- [ ] Steps to initiate: Step 1 _____ Step 2 _____ Step 3 _____ — Framework: Fogg MAP
- [ ] Feedback on completion (None / Delayed / Immediate + clear / Immediate + celebratory) — Framework: Hook Model
- [ ] Success state obvious/clear/unclear/crashed? — Framework: Norman
- [ ] Subsequent interrupts after first interaction (None / Rating / Share / Payment / Help) — Framework: Kano
- [ ] Feeling after first interaction (Excited / Satisfied / Neutral / Confused / Frustrated) — Framework: HEART

### Navigation & Wayfinding
- [ ] Primary navigation pattern (Bottom tabs / Side drawer / Top tabs / Segmented control / Other) — Framework: Nielsen #1
- [ ] Navigation visible from first content screen? (Yes / No / Hidden until scroll) — Framework: Nielsen #1
- [ ] Easy to identify: Core feature / Settings / Help / Profile access — Framework: Norman
- [ ] Label clarity (buttons self-explanatory?) (1-5 scale): _____ — Framework: Norman
- [ ] Number of navigation options visible at once (cognitive load): _____ — Framework: Nielsen #1

### Interrupts & Dark Patterns
- [ ] Rating/review prompt timing (Never / Before / After first / After X interactions) — Framework: Kano
- [ ] Share/referral prompt timing (Never / Before value / After first / After X) — Framework: Hook Model
- [ ] Push notification consent timing (Never / Upfront / After value / When?) — Framework: Nielsen #3
- [ ] Dark patterns detected? (None / Unclear dismiss buttons / Pre-checked boxes / Misleading copy / Ads / Forced tutorials) — Framework: Nielsen #3, Kano
- [ ] Ads during onboarding? (Yes / No / When and frequency?) — Framework: Kano

### Overall Activation Signals
- [ ] Likelihood user completes onboarding (<20% / 20-50% / 50-80% / >80%) — Framework: AARRR
- [ ] Likelihood user returns after first session (<20% / 20-50% / 50-80% / >80%) — Framework: HEART
- [ ] Blockers to activation identified (list 1-3 key friction points) — Framework: Fogg MAP
- [ ] Delighters present? (None / Minor / Notable — examples?) — Framework: Kano

---

## KEY ISSUE PATTERNS

1. **Paywall Before Value** → Detect: Subscription screen on app open before any core feature interaction. Framework: Fogg MAP, AARRR. Fix: Move paywall to appear after user completes first meaningful interaction (e.g., after creating first note, taking first photo).

2. **No Interest Probing / Generic Onboarding** → Detect: 3-question survey asking age/gender/location unrelated to why user installed. Framework: JTBD, Kano. Fix: Replace demographic questions with JTBD probes ("What's your primary goal?", "How much time can you dedicate?", "What's your experience level?").

3. **Too Many Permissions Too Early** → Detect: 5+ permission requests on app open before feature access. Framework: Fogg MAP, Nielsen #3. Fix: Defer permissions to feature access; add context before requesting ("We use location to show nearby stores"); sequence by sensitivity.

4. **No Contextual Guidance / Missing Signifiers** → Detect: Blank first content screen or unlabeled "+" button with no hint of function. Framework: Norman, Nielsen #1. Fix: Add label/tooltip ("Create note"), add in-app text ("You have no notes. Ready to create your first?"), use affordances.

5. **Rating Prompt Too Early** → Detect: Rating request immediately after first core interaction or within first 2-5 uses. Framework: Kano, Hook Model. Fix: Show rating prompt only after 20-30 uses or after completing meaningful workflow; trigger on positive signals (milestone, goal completion).

6. **Unclear First Interaction Feedback** → Detect: User completes action but no response or delayed response. Framework: Hook Model, Norman. Fix: Provide immediate, celebratory feedback (animation, progress indicator, success message).

7. **Aggressive Permission Denials** → Detect: Denying one permission breaks entire app or feature; no graceful degradation. Framework: Nielsen #3. Fix: Allow partial permission grant; degrade gracefully when permissions denied; re-request later with stronger context.

8. **Empty Free Tier** → Detect: Free tier exists but is completely unusable (can't create anything, can't see examples). Framework: AARRR. Fix: Free tier should allow meaningful first action and demonstrate core value before paywall.

---

## OUTPUT FORMAT

```markdown
# ONBOARDING & FIRST VALUE EXPERIENCE — [X]/10

## Evidence Summary
- **Time from app open to first value moment**: [X] seconds
- **Number of steps before first interaction**: [Y] steps
- **Number of permission requests**: [Z] (timing: before/after value)
- **Paywall timing**: [Before/After/During] first value
- **Personalization type**: [None / Demographic / JTBD-based]

## Key Metrics
- **Activation confidence**: [Low / Medium / High]
- **Friction points identified**: [1-2 minor / 3-5 moderate / 6+ severe]

## Frameworks Applied
- **Fogg MAP**: [Motivation, Ability, Prompt assessment]
- **HEART Adoption**: [Engagement signal assessment]
- **JTBD**: [Job understanding assessment]
- **Hook Model**: [Trigger→Action→Reward assessment]

## Scoring Breakdown

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Time to value | [X]/10 | Measured at [X] seconds |
| Paywall timing | [X]/10 | Paywall at [timing] |
| Personalization | [X]/10 | [Description] |
| Permissions | [X]/10 | [Description] |
| First interaction clarity | [X]/10 | [Description] |
| Navigation | [X]/10 | [Description] |
| Dark patterns | [X]/10 | [Description] |

**Total Score: [X]/10** | **Justification**: [1-2 sentences]

## Key Issues

### Issue #1: [Title]
**Problem**: [What observed] | **Framework**: [Name] | **Impact**: [User %, conversion impact] | **Hypothesis**: [1-line fix]

### Issue #2: [Title]
[Same structure]

### Issue #3: [Title]
[Same structure]

## Recommendations

### P0 (Critical)
[Issues affecting >50% of users or activation blockers]

### P1 (High)
[Issues affecting 20-50% of users or retention drivers]

### P2 (Medium)
[Issues affecting <20% of users or minor friction]

**Review Conducted**: [Date] | **Duration**: [Speed / Rigor / Hybrid]
```
