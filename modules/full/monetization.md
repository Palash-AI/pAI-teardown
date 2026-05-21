# Monetization UX Module (Revenue Stage)

> **Module Purpose:** Audit the "Value Before Friction" principle in monetization design. Evaluates whether the app creates habit and demonstrates value BEFORE introducing payment friction.
>
> **AARRR Stage:** Revenue
>
> **Primary Frameworks:** Reforge Monetization-Engagement Alignment, Fogg MAP for conversion, HEART (Happiness), Kano for feature categorization
>
> **Persona-Specific:** New user (first paywall moment), Free user (frequency of paywalls), Trial user (trial experience quality), Paid user (value reinforcement), Lapsed user (win-back offers)
>
> **Time Estimate:** Speed mode 20 min | Rigor mode 45-60 min

---

## MODULE OVERVIEW

### The Core Principle

Most Indian consumer apps fail at monetization not because of pricing, but because they ask for money **before demonstrating value**. This violates Reforge's foundational principle: **Monetization-Engagement Alignment**.

### Design Skill Integration (Mandatory for Screenshots)

> **`design:critique`** — Run on paywall and pricing screenshots. Evaluate: first impression (does the paywall feel premium or desperate?), usability (can user understand pricing options quickly?), visual hierarchy (is the recommended plan visually dominant?), consistency (does paywall match app's design language?), accessibility (is pricing text readable, contrast sufficient?). For India context: does the paywall design signal trust or trigger "scam" perception? Is ₹ pricing prominent? Are UPI logos visible?

> **`design:ux-copy`** — Run on all paywall and pricing copy. Evaluate: CTA labels ("Start free trial" > "Subscribe now"), price anchoring copy (₹X/month vs annual savings clearly shown), cancellation messaging ("Cancel anytime" visible and clear), feature comparison copy (free vs paid). For India context: is paywall copy in Hindi/Hinglish for Tier 2-3? Does value prop cite specific outcomes? Is ₹1 trial framed as risk-free? Does annual plan show monthly equivalent ("₹79/month, billed ₹949/year")?

**Reforge Monetization Models (from expert-frameworks.md):**
- **Engagement-first:** Build habit → then monetize (Duolingo, YouTube, Spotify). Users see 20-40 free uses before paywall. They understand the value. They convert at 2-5%.
- **Monetization-first:** Gate content → force payment (most failing apps). Users see paywall on Day 0. They've experienced nothing. They convert at 0.1-0.3%.
- **Balanced freemium:** Free content that's useful → Premium adds premium layer (not essential version). Notion, Canva. Convert at 1-3%.

**This module audits:**
1. **Paywall timing** — When does the user first see a paywall? (Measure: after how many seconds, how many screens, which action triggers it)
2. **Freemium ratio** — What % of core features/content are free vs. paid?
3. **Value proposition clarity** — Can the user articulate what they get for paying?
4. **Conversion mechanism** — Fogg MAP: Is Motivation clear? Is Ability present (payment methods)? Is the Prompt well-timed?
5. **Payment friction** — Are payment methods available? (UPI, credit card, wallet for Indian users)
6. **Trial quality** — If trial exists, does it onboard the user to premium features?
7. **Cancellation ease** — Can users cancel without punishment? (Nielsen heuristic #3: User control)
8. **Social proof** — Are there ratings, user counts, testimonials on paywall? (Fogg: Low motivation needs credibility)
9. **Price positioning** — Is pricing in ₹? Is annual pricing available? Does it match Indian consumer mental models?
10. **Urgency tactics** — Are there artificial scarcity mechanics? (Ethical consideration: Do they coerce or inform?)

---

## SCREENS TO NAVIGATE & OBSERVE

### 1. PAYWALL/TRIAL PROMPT (Every Instance)

**What to find:**
- First paywall appearance (usually on Day 0 or when user tries to access premium feature)
- Every subsequent paywall in the app (free users might see 5-10 paywalls per session)
- Trial prompts (if freemium model exists)

**What to observe & document:**

| Aspect | Observation | Evidence |
|--------|-------------|----------|
| **Timing** | How many seconds after app open? How many screens navigated? Which action triggered paywall? | Screenshot + timestamp |
| **Screen context** | Is the paywall blocking progress (hard paywall) or suggesting an upgrade (soft upsell)? | Screenshot + description |
| **Copy quality** | Is the value prop clear in <2 sentences? Does it answer "What am I paying for?" | Screenshot + transcription |
| **Visual hierarchy** | What's the dominant element? CTA button? Price? Feature list? | Screenshot + annotation |
| **Fogg MAP assessment** | Is Motivation visible? (benefits of paid) Are payment methods (Ability) present? Is the CTA prompt clear? | Checklist |
| **Urgency/scarcity** | Is there a countdown timer? Limited offer? Expiring trial? | Screenshot + note |
| **Social proof** | Ratings? User count ("2.3M+ users")? Testimonials? Reviews? | Screenshot + count |

**Actions to take:**

1. Take a screenshot of the first paywall
2. Read the copy out loud (note if it's confusing)
3. Tap the CTA — what happens? Does it go to pricing page or trial flow?
4. Go back and continue using the app to find all paywalls
5. For each paywall, note whether it's contextual (user tried to access premium) or broadcast (random prompt)
6. Try to close paywalls — can you dismiss them easily? Is there a "Not now" or "Skip" option?

---

### 2. PRICING PAGE / SUBSCRIPTION OPTIONS

**What to find:**
- Dedicated pricing page (if navigable from paywalls or settings)
- Plan options (free tier, single plan, multiple tiers)
- Price display (in ₹? in USD? clear per-month or annual?)

**What to observe & document:**

| Aspect | Observation | Evidence |
|--------|-------------|----------|
| **Plan tiers** | How many options? (Free, Premium, Premium+) | Screenshot of full pricing page |
| **Price formatting** | ₹1,999/year or ₹199/month? Annual discount available? | Screenshot + transcription |
| **Feature differentiation** | What features are free vs. paid? Can user see the diff before paying? | Screenshot + comparison table |
| **Annual vs. monthly** | Is annual pricing available and highlighted? (Indians prefer annual deals) | Screenshot |
| **Trial offer** | ₹1 trial? 7-day free trial? Clear what happens after trial? | Screenshot + terms |
| **Value messaging** | Does each tier have a tagline or benefit statement? ("Best for students", "For professionals") | Screenshot + transcription |
| **Kano categorization** | Which features are Must-Be (basic)? One-Dimensional (more is better)? Attractive (delighters)? | Analysis |

**Actions to take:**

1. Navigate to the pricing page (usually from paywall or settings)
2. Screenshot the full page (if it's long, scroll and take multiple screenshots)
3. Check: Is annual pricing available? How much cheaper than monthly?
4. Tap on a plan — what information is shown? (Kano: Can user see what they get?)
5. Look for trial terms — are they clear? (Reforge: Trial quality indicates commitment to onboarding)
6. Compare to domain benchmarks from `domains/[domain].md`

---

### 3. PAYMENT FLOW (UPI, Card, Wallet Options)

**Critical for India:** This is where 90% of payment abandonment happens. UPI is non-negotiable for Tier 2-3.

**What to find:**
- Payment method options available (UPI, credit/debit card, wallet)
- Which payment provider (Razorpay, PhonePe, Google Pay, etc.)
- Error handling in payment flow
- Confirmation screen after payment

**What to observe & document:**

| Aspect | Observation | Evidence |
|--------|-------------|----------|
| **Payment methods** | UPI? Credit card? Debit card? Wallet (PhonePe, Paytm, Google Pay)? | Screenshot showing options |
| **UPI prominence** | Is UPI the default option or hidden in a dropdown? (Tier 1 vs. Tier 2-3 parity) | Screenshot |
| **Payment provider** | Who processes payments? Razorpay? PhonePe? Google Play Billing? | Note from UPI flow |
| **Form friction** | How many steps? Are fields pre-filled (Fogg: Ability)? Is there validation feedback? | Walk-through + screenshot |
| **Security trust signals** | SSL badge? Encryption message? Razorpay/PhonePe logos? | Screenshot |
| **Failure handling** | What happens if payment fails? Can user retry? Is there help text? (Nielsen #9: Error recovery) | Note |
| **Confirmation** | After payment, what's shown? Order confirmation? Receipt option? Return to app automatic? | Screenshot + note |

**Actions to take:**

1. Tap to purchase (don't complete; stop at confirmation)
2. Take screenshot of payment method selection
3. Check if UPI is available and where (default or secondary)
4. Note all payment methods visible
5. If possible (and approved by user), complete payment for test account
6. Document the confirmation screen

---

### 4. "PLUS" / PREMIUM UPSELL SURFACES

**What to find:**
- In-app badges ("+ Upgrade", "Go Premium", "Unlock this")
- Feature locks / paywalls triggered by user action (not broadcast)
- Contextual upsells (feature you just tried to use is locked)

**What to observe & document:**

| Aspect | Observation | Evidence |
|--------|-------------|----------|
| **Contextuality** | Is the upsell contextual to what the user tried? (Good: "You've used 10 downloads. Upgrade for unlimited." Bad: Random "Get Plus" banner) | Screenshot + context |
| **Copy quality** | Does the upsell explain the benefit at that moment? | Transcription |
| **Hard vs. soft** | Is the upsell blocking progress (hard) or suggesting (soft)? | Note |
| **Frequency** | How many upsells per session for a free user? (Reforge: > 3 = annoying) | Count + note |
| **Dismissability** | Can the user dismiss and continue using free version? (Nielsen #3) | Test + note |

**Actions to take:**

1. Trigger premium features to see upsells
2. Count total upsells seen in one session
3. Note whether they're contextual or broadcast
4. Try to dismiss each — what happens?

---

### 5. FREE VS. PAID CONTENT DIFFERENTIATION

**What to find:**
- Visual indicators (lock icons, "Premium" badges)
- Content accessibility (can free users see premium content metadata?)
- Freemium ratio (what % of total content is free?)

**What to observe & document:**

| Aspect | Observation | Evidence |
|--------|-------------|----------|
| **Visual indicators** | Are premium items clearly marked? (Lock icon? "Premium" badge? Different color?) | Screenshot |
| **Metadata visibility** | Can free users see what they're missing? (E.g., premium video title/thumbnail, but can't play) | Screenshot |
| **Freemium ratio** | Of 100 items visible, how many are free vs. locked? Calculate % | Count + calculation |
| **Feature differentiation** | Is premium a different feature (storage limit) or better content (better lessons)? | Analysis |
| **Progression path** | As user engages with free content, does it naturally lead to premium? (Reforge: Product loop) | Test + note |

**Actions to take:**

1. Browse content library (homepage, search, category)
2. Count free vs. locked items
3. Screenshot examples of free and locked content
4. Check: Can you see what you're missing? (Important for motivation)

---

### 6. TRIAL ONBOARDING (If Trial Exists)

**What to find:**
- Trial start flow
- Guidance for trial users (tooltips, tutorials)
- Feature highlights (what should trial user explore?)
- Conversion messaging (when trial ends, what happens?)

**What to observe & document:**

| Aspect | Observation | Evidence |
|--------|-------------|----------|
| **Trial entry** | How easy is it to start a trial? (Fogg: Is it low friction?) | Screenshot + step count |
| **Onboarding** | When user starts trial, are they guided to premium features? Or left to discover? (Critical: Many fail here) | Screenshot + note |
| **Clarity** | Does the user know they're in a trial? How long? When does it end? | Screenshot + transcription |
| **Premium feature discovery** | Does the app highlight what's new/premium during trial? (Fogg: Motivation + Ability) | Screenshot |
| **Conversion readiness** | By day 3 of trial, has user experienced enough value to justify paying? (Data from analytics if available) | Analysis + note |

**Actions to take:**

1. Start a trial (if possible)
2. Take screenshot of trial entry point
3. Note: Is there a welcome message explaining what's premium?
4. Check: Are there tooltips highlighting premium features?
5. Continue using app for 2-3 days of trial (simulated) to see conversion messaging

---

### 7. RENEWAL / CANCELLATION FLOW

**Critical Nielsen Heuristic #3: User control and freedom.** This is where trust is won or lost.

**What to find:**
- How to cancel subscription
- Number of steps to cancel
- Cancellation confirmation
- Win-back offers (do they appear during cancellation?)
- Refund policy visibility

**What to observe & document:**

| Aspect | Observation | Evidence |
|--------|-------------|----------|
| **Cancellation discoverability** | Where is the cancel button? (Settings → Subscriptions? Or hidden in terms?) | Screenshot + path |
| **Steps to cancel** | Count the steps. (1-click = ideal. 3-4 clicks = acceptable. 5+ = friction violation) | Step count |
| **Confirmation** | Is there a confirmation dialog? What does it say? (Ethical: Is it manipulative? "Are you sure you want to lose access to all your courses?"?) | Screenshot + assessment |
| **Win-back offer** | Does the app offer a discount to keep the user? ("₹99 instead of ₹199 for 1 month?") | Screenshot |
| **Refund policy** | Is it visible before purchase? After cancellation? | Screenshot |
| **Renewal clarity** | Before charging, does the app confirm next billing date? | Screenshot |
| **Auto-renewal transparency** | Is it clear that the subscription will renew? (Legal requirement in many markets) | Screenshot |

**Actions to take:**

1. Go to Settings / Account / Subscriptions
2. Find the cancel button (take screenshot if it's hard to find)
3. Click cancel and document every step
4. Assess: Is this easy for the user? Would a user struggle?
5. Note: Did a win-back offer appear? Was it ethical or manipulative?

---

### 8. UPGRADE PROMPTS WITHIN CONTENT

**What to find:**
- Paywalls triggered by user action within a lesson/content piece
- Hard paywalls (blocking progress) vs. soft upsells (suggesting)
- Content teasers (can user see next lesson is locked?)

**What to observe & document:**

| Aspect | Observation | Evidence |
|--------|-------------|----------|
| **Timing** | After how much free content is the paywall triggered? (E.g., after 3 free lessons) | Count |
| **Contextuality** | Is the paywall contextual? ("You've finished the free section. Next section is premium.") Or random broadcast? | Assessment |
| **Hard vs. soft** | Does it block progress or suggest? (Hard = Nielsen violation. Soft = acceptable) | Note |
| **Value clarity** | Does the paywall explain what comes next? Can you see the locked content metadata? | Screenshot |

**Actions to take:**

1. Consume free content (lesson, article, video)
2. When paywall appears, screenshot it
3. Note the context (where are you in the app?)
4. Try to proceed without paying — what happens?

---

## SCORING RUBRIC (1-10)

Use this rubric to score the Monetization module. Score reflects how well the app aligns with Reforge's monetization-engagement framework and India consumer expectations.

### Score Mapping

| Score | Label | Definition | Reforge Alignment | Fogg MAP | India Fit |
|-------|-------|-----------|-------------------|----------|-----------|
| **1-2** | Critical Failure | Paywall on D0 before value. No freemium. Aggressive dark patterns. UPI not available. Auto-renewal unclear. Cancellation impossible. | Monetization-first model. Will fail. | All MAP factors absent. | Incompatible with Tier 2-3 expectations. |
| **3-4** | Poor | Paywall early (screen 2-3). Some free content but locked too early. Weak value prop. Basic payment methods. Cancellation hard. | Monetization-first. Slight concession to engagement. | Motivation unclear. Ability low (missing payment method). | Missing UPI. Pricing too high. |
| **5-6** | Below Average | Reasonable freemium ratio (50/50 free/paid) but paywall design is weak. No social proof. Payment friction. Trial exists but not guided. | Balanced but execution flawed. | Motivation present but weak. Ability present but friction. | Payment methods adequate. Pricing reasonable. Trial exists. Cancellation possible but hard. |
| **7-8** | Good | Solid freemium model (40% free, 60% premium premium-only). Paywall after value demo. Social proof on paywall. Clear pricing. UPI + cards available. Easy cancellation. Some trial guidance. | Engagement-first mindset, decent execution. | All MAP factors strong. Motivation clear. Ability high. Prompt contextual. | UPI prominent. Annual pricing available. Trial well-guided. Hindi/Hinglish support. |
| **9-10** | Excellent | Best-in-class (Duolingo/Spotify model). Users don't feel paywalled until 20+ uses. Clear value prop. Social proof. Multiple pricing tiers. All payment methods. Trial onboards to premium feature discovery. Win-back offers. Easy cancellation. Renewal clarity. | Engagement-first perfectly executed. | All MAP factors optimized. Frictionless conversion. | Tier 1-3 parity in experience. Annual pricing highlighted. ₹49-199 range. Transparent terms. |

### Scoring Considerations for Indian Context

**Adjust score down if:**
- Paywall appears before Day 0 value (critical for Tier 2-3)
- UPI is not available (instant -2 points for India)
- Pricing in USD not ₹ (confusing for Indian users)
- Annual pricing not available (Indians prefer annual deals)
- Cancellation requires email/support contact (-2 points)
- Auto-renewal not transparent (-1 point)
- Hindi support missing and app targets Tier 2-3 (-1 point)

**Adjust score up if:**
- Freemium ratio is 40:60 (free:paid) or better
- ₹1 trial or 7-day free trial with onboarding guidance
- Annual pricing 30%+ cheaper than monthly (Indians expect this)
- Trial experience guides user to premium features
- Win-back offers appear (shows understanding of churn recovery)
- Multiple payment methods prominent (UPI, cards, wallet)

---

## EVIDENCE CHECKLIST

Document these specific findings in the "Current State" file. Every bullet should reference a screenshot.

### Paywall Timing & Frequency

- [ ] First paywall appears on screen #X (timeline: D0, D1, after 5 screens, after 10 min of usage)
- [ ] Paywall appears after user completes first free value moment (lesson, video, quiz)
- [ ] Total paywalls per session for free user: [X] (count all instances)
- [ ] Paywalls are contextual (triggered by user action trying to access premium) vs. broadcast (random prompts)
- [ ] Soft paywalls (suggest upgrade) vs. hard paywalls (block progress): [ratio]
- [ ] Users can dismiss paywalls and continue with free version (Nielsen #3: User control)

**Template:** "Paywall first appears on screen #03 (login → home → free content → paywall prompt). Screenshot: #03-paywall-first-appearance-new-user.png. Timing: 2 minutes after app open."

---

### Free Content Ratio

- [ ] Free tier includes: [specific features/content types]
- [ ] Premium-only features: [specific features/content types]
- [ ] Estimated % of total content accessible to free users: [X]% (e.g., 40% free, 60% locked)
- [ ] Free content is useful on its own (not just a teaser) — assess via Kano "Must-Be" check
- [ ] User can get value without paying (measure in "value moments" e.g., lessons completed, videos watched, problems solved)

**Template:** "Free tier includes 5 courses (out of 50), 1 daily practice session, and profile creation. ≈ 8% of content is free. Remaining 92% locked behind paywall. Screenshot: #04-content-library-free-user.png"

---

### Trial Terms & Auto-Renewal Transparency

- [ ] Trial offer: [type] (e.g., ₹1 7-day trial, free 3-day trial)
- [ ] Auto-renewal terms clearly stated before purchase (screenshot shows: "Your subscription will renew on [date]")
- [ ] Cancellation option discoverable before payment ("You can cancel anytime in Settings")
- [ ] Trial conversion rate signal (if accessible): [X]% (or "not available")

**Template:** "₹1 7-day trial offered. Auto-renewal notice shown on checkout screen: 'Your subscription will auto-renew at ₹199/month on [date].' Cancellation path shown: Settings → Subscriptions → Cancel. Screenshot: #06-trial-terms-new-user.png"

---

### Payment Methods Available (Critical for India)

- [ ] UPI available? Yes/No. If yes, is it default or secondary option?
- [ ] Credit/Debit card available? Yes/No.
- [ ] Wallet options (Google Pay, PhonePe, Paytm, etc.)? List: [X, Y, Z]
- [ ] Which payment provider handles transactions? (Razorpay, PhonePe, Google Play Billing, etc.)
- [ ] Payment form friction level (number of steps, pre-filled fields): [description]

**Template:** "Payment methods available: UPI (default option), Credit Card, Debit Card, Google Pay. PhonePe wallet not available. Processed through Razorpay. Payment form requires: Phone, Amount, Confirmation — 3 steps. Screenshot: #07-payment-methods-new-user.png"

---

### Social Proof on Paywall (Fogg: Motivation Factor)

- [ ] User rating visible on paywall? (e.g., ⭐ 4.8/5)
- [ ] User count visible? (e.g., "2.3M+ subscribers")
- [ ] Testimonials shown? Yes/No. How many? Content sample:
- [ ] Trust badges (verified badge, media mentions, etc.)? List: [X, Y, Z]
- [ ] Social proof assessment: Strong/Moderate/Weak

**Template:** "Paywall shows: ⭐ 4.7/5 (from 45K reviews), '1.2M+ paid subscribers,' and 3 user testimonials (sample: 'Best investment for my learning'). Trust badge: Verified by Google Play. Assessment: Strong social proof. Screenshot: #05-paywall-social-proof-new-user.png"

---

### Value Proposition Clarity (Fogg: Motivation Factor)

- [ ] Paywall copy clearly states: "What you get for paying"
- [ ] Copy is concise (<50 words describing benefit)
- [ ] Specific features listed (not generic "Unlock Premium")
- [ ] Emotional benefit clear (e.g., "Unlock all courses and never worry about content limits again")
- [ ] Value clarity assessment: Clear/Moderate/Vague

**Template:** "Paywall copy: 'Unlock all 500+ courses, unlimited downloads, offline access, and ad-free learning for ₹199/month.' Feature list provided. Emotional benefit clear: 'Learn at your pace without limits.' Value clarity: Clear. Screenshot: #05-paywall-value-prop-new-user.png"

---

### Urgency & Scarcity Tactics (Ethical Assessment)

- [ ] Countdown timer? Yes/No. If yes: [X hours remaining]
- [ ] Limited offer language? ("Only ₹49 today", "Offer expires", "Limited spots")
- [ ] Subscription bundling? ("2 months free when you buy annual")
- [ ] Dark patterns detected? (e.g., "Unsubscribe" button hidden, misleading copy)
- [ ] Ethical assessment: Informative scarcity / Manipulative dark patterns / None

**Template:** "Countdown timer: 'Offer expires in 4 hours' with red background. Copy: 'Get ₹149/month plan for ₹99 today only.' Assessment: Mild urgency (informs without coercing). No detected dark patterns. Screenshot: #05-paywall-urgency-new-user.png"

---

### Cancellation Ease (Nielsen Heuristic #3: User Control)

- [ ] Cancellation discoverable in Settings or Account section? Yes/No.
- [ ] Steps to cancel: [count] (1-click ideal, <3 acceptable, 5+ problematic)
- [ ] Confirmation dialog shown before cancellation? Yes/No. Copy: [note if manipulative]
- [ ] Win-back offer on cancellation? Yes/No. Content: [e.g., "₹99/month for 3 months?"]
- [ ] Refund policy mentioned before purchase? Yes/No.
- [ ] Cancellation difficulty assessment: Easy/Moderate/Hard

**Template:** "Cancellation path: Settings → Subscriptions → [App Name] → Cancel (3 steps). Confirmation dialog: 'Are you sure? You'll lose access to all premium features.' No win-back offer. Refund policy not shown pre-purchase. Assessment: Moderate difficulty. Nielsen #3 not violated but could be smoother. Screenshot: #12-cancellation-flow-paid-user.png"

---

### Price Positioning (India-Specific)

- [ ] Price shown in ₹ (not USD, not confusing)
- [ ] Annual plan available? Yes/No. If yes, discount: [X]% off monthly
- [ ] Price point: ₹[X]/month or ₹[X]/year
- [ ] Positioning vs. competitors in domain (e.g., vs. Duolingo, Unacademy, etc.): [higher/lower/similar]
- [ ] Price psychology check: Does it match Indian consumer expectations?
  - Tier 1: ₹99-199/month is sweet spot
  - Tier 2: ₹49-99/month is sweet spot
  - Tier 3: ₹29-49/month is maximum
- [ ] Price clarity assessment: Clear / Confusing

**Template:** "Annual plan: ₹1,799/year (vs ₹199/month = 25% savings, which is below Indian expectation of 30%+). Monthly-only plan not highlighted. Price positioning: Similar to Unacademy (₹2,400/year), higher than Duolingo (₹1,499/year). Tier 2 users may find ₹199/month high. Assessment: Price positioning could better match Tier 2-3 expectations. Screenshot: #04-pricing-page-new-user.png"

---

### Auto-Renewal Transparency (India Legal Requirement)

- [ ] Billing date clearly shown before purchase? Yes/No.
- [ ] Auto-renewal confirmation required before charging? Yes/No.
- [ ] Cancellation reminder email sent before renewal? (best practice)
- [ ] One-click unsubscribe available? Yes/No.
- [ ] Legal compliance assessment: Full transparency / Partially transparent / Non-transparent

**Template:** "Checkout page shows: 'Your subscription will auto-renew on February 28, 2026 at ₹199.' One-click cancel in Settings. No cancellation reminder email pre-renewal (gap). Assessment: Mostly transparent but could improve with renewal reminder. Screenshot: #06-checkout-confirmation-new-user.png"

---

## KEY ISSUES TEMPLATE

For each issue found, use this structure in the "Current State" file:

### Issue Title & Framework Citation

**[Issue #X]: [Specific, actionable title]**

**Framework violated:** [Primary framework] — [specific principle]

**Evidence (with screenshot reference):**
- Bullet 1 with screenshot #X
- Bullet 2 with screenshot #X

**Impact:**
- Reforge: [How does this violate monetization-engagement alignment?]
- Fogg MAP: [Which factor breaks? Motivation? Ability? Prompt?]
- India fit: [Does this violate India consumer expectations?]
- User control: [Does this violate Nielsen #3?]

**Severity:** Critical / High / Medium / Low

---

## COMMON KEY ISSUES

Use these as starting points when auditing. Adapt to app-specific findings.

### 1. Monetization Precedes Value

**Issue:** Paywall appears on D0 before user experiences core value.

**Framework violated:** Reforge Monetization-Engagement Alignment — "Monetization-first models fail. Value must come before friction."

**Example Evidence:**
- Paywall appears on screen #2 (after login)
- User hasn't completed a single free lesson
- Messaging: "Upgrade to Premium to unlock content"
- Fogg MAP broken: Motivation low (no value experienced yet), Ability requires payment

**Impact:**
- Tier 2-3 users insta-uninstall (5-10 second decision window)
- Conversion rate likely 0.2% or below
- Violates Reforge principle

**Recommendation anchor:** Defer paywall until user completes 3-5 free value moments (lessons, quizzes, content pieces)

---

### 2. Inverted Freemium Ratio

**Issue:** Premium content dominates; free content is insufficient to build habit.

**Framework violated:** Reforge "Engagement-first" model requires 30-50% free content. This app offers <20%.

**Example Evidence:**
- Free tier: 2 courses (out of 50)
- Locked features: Search, downloads, offline mode
- Free content experience doesn't demonstrate full product capability
- Fogg MAP broken: Ability to understand product value is low

**Impact:**
- Users can't experience the product fully
- Trial conversion will be low (user hasn't learned to use premium features)
- Competitors offering 50%+ free content will dominate

**Recommendation anchor:** Expand free tier to 40%+ of content. Unlock key features (search, basic downloads) for free users.

---

### 3. No Social Proof on Paywall

**Issue:** Paywall shows price only, no credibility signals.

**Framework violated:** Fogg MAP — Motivation broken when evidence is absent. "If I don't see other users validating this, why should I pay?"

**Example Evidence:**
- Paywall shows: "₹199/month — Unlock All"
- No rating, user count, testimonials
- No trust badges (Google Play Verified, media mentions)
- Fogg: Motivation is low; credibility is zero

**Impact:**
- Conversion rate likely 0.5% or below
- Users don't know if they're paying for a legitimate product
- Especially damaging in India where "unknown = scam" is common perception

**Recommendation anchor:** Add: (1) App rating (if >4.5), (2) user count (if >100K), (3) one 2-sentence testimonial, (4) trust badge

---

### 4. Pricing Doesn't Match India Consumer Mental Models

**Issue:** Price is too high for target user or not positioned for annual savings.

**Framework violated:** Reforge framework adjusted for India — Tier 2-3 users expect ₹29-99/month, not ₹199/month.

**Example Evidence:**
- Monthly pricing: ₹199/month (Tier 1 sweet spot, not Tier 2)
- No annual plan offered (users prefer annual deals for ₹999-1,200/year)
- Competitors offer ₹99-149/month
- Tier 2 user sees this as "expensive relative to other subscriptions I'm paying for"

**Impact:**
- Free-to-paid conversion will be low in Tier 2-3
- Users will compare to other ₹100-200 subscriptions (mobile recharge, streaming service)
- Will lose Tier 2 addressable market

**Recommendation anchor:** (1) Introduce annual plan at ₹1,299/year (36% savings, matches India expectations). (2) Offer ₹99/month tier for Tier 2 users or ₹149/month with value positioning for professionals.

---

### 5. Missing UPI Payment Option

**Issue:** Only credit/debit card available; UPI not supported.

**Framework violated:** Fogg MAP — Ability broken. 90% of Tier 2-3 users can't pay (UPI-only).

**Example Evidence:**
- Payment methods shown: Credit Card, Debit Card, Google Pay
- UPI missing (most common payment method in India)
- Fogg: 60% of potential users have Ability = 0 (they don't have a credit card)

**Impact:**
- ~60% of Tier 2-3 market lost at payment stage
- Conversion abandonment likely 50%+ at payment flow
- Critical blocker for revenue from India's largest user base

**Recommendation anchor:** Add UPI as default payment option (partner with Razorpay, PhonePe, or Google Play Billing with UPI support)

---

### 6. Cancellation Requires Email or Support Contact

**Issue:** User can't cancel in-app; must email support or call.

**Framework violated:** Nielsen Heuristic #3: User Control and Freedom. Also violates India's consumer expectations (seen as hidden friction, trust-breaking).

**Example Evidence:**
- Settings → Subscriptions section doesn't show cancel option
- Only option: "Contact Support" email link
- Screenshots show no in-app cancellation path

**Impact:**
- User trust is broken (perceived as manipulative/scammy)
- Abandonment/refund requests to payment processors (chargebacks)
- Legal risk in regulated markets

**Recommendation anchor:** Add one-click "Cancel Subscription" in Settings → Subscriptions, with confirmation dialog. Offer win-back discount, but allow easy cancellation.

---

### 7. Trial Without Onboarding to Premium Features

**Issue:** User gets trial access but app doesn't guide them to premium features; they finish trial without understanding what they're missing.

**Framework violated:** Reforge — Trial should be a "premium feature discovery" experience. Fogg MAP — Motivation (what am I paying for?) is never built.

**Example Evidence:**
- Trial starts with generic "You're in trial until [date]" notification
- App shows same home screen as free user
- No tooltips or highlights on premium features
- Screenshots #X show trial experience is identical to free experience
- User doesn't know what premium unlocks

**Impact:**
- Trial-to-paid conversion will be very low (user hasn't experienced value)
- Wasted marketing spend on trial acquisition
- Users think premium is "same as free" → no motivation to convert

**Recommendation anchor:** (1) Show welcome message: "Explore these 3 premium features during your trial." (2) Add tooltips highlighting premium features. (3) Track: Did user try the premium features? If yes, show retention incentive ("You loved [feature] — keep it with paid plan")

---

### 8. Premium Tab Is Just a Paywall, Not a Feature

**Issue:** If the app has a "Premium" or "Plus" tab, it's just a re-display of the paywall, not showcasing premium features or content.

**Framework violated:** Kano Model — "Attractive" features should be discoverable and exciting. If premium is just "Click here to pay," it's not attractive.

**Example Evidence:**
- "Premium" or "Go Plus" tab exists in navigation
- Tap it → shows paywall with pricing
- Doesn't showcase what premium gives you (courses, features, benefits)
- Wasted screen real estate

**Impact:**
- Missed opportunity to demonstrate premium value
- User doesn't know what's premium before deciding to convert
- Low motivation (Fogg: Motivation broken)

**Recommendation anchor:** Redesign Premium tab to showcase: (1) Premium content preview (with teasers), (2) Premium features highlighted, (3) Social proof (user testimonials about premium), (4) Then the paywall at the bottom

---

### 9. No Annual Pricing or Poor Annual Discount

**Issue:** App offers monthly pricing only, or annual pricing exists but isn't discounted enough to match India expectations.

**Framework violated:** India Consumer Context — "Indians prefer annual deals. A 10% discount is not enough. Minimum 25-30% discount expected."

**Example Evidence:**
- Monthly: ₹199/month × 12 = ₹2,388/year
- Annual: ₹2,099/year (only 12% discount, users expect 25-30%)
- Or: No annual option at all
- Competitor (e.g., Duolingo) offers ₹1,499/year (37% savings)

**Impact:**
- Users perceive annual plan as not a good deal
- Will stick with monthly (or not subscribe)
- Competitive disadvantage vs. apps with 30% annual discounts

**Recommendation anchor:** Introduce annual plan at ₹1,399-1,599/year (30-35% savings vs. monthly). Highlight annual as "Best value" with badge.

---

### 10. Unclear Auto-Renewal Terms

**Issue:** User doesn't see when subscription renews or how much they'll be charged until checkout.

**Framework violated:** India Legal Requirements + Nielsen Heuristic #3: User control requires transparency.

**Example Evidence:**
- Checkout page doesn't show renewal date
- Auto-renewal not mentioned until confirmation email
- Renewal amount shown as vague ("₹199" without clarifying "per month")
- Screenshots #X show no clarity on next billing date

**Impact:**
- Users surprised by renewal charge (feels like hidden charge)
- Refunds/chargebacks to payment processor
- Legal compliance risk
- Trust destruction

**Recommendation anchor:** Before purchase, clearly state: (1) First charge: ₹X on [date], (2) Next charge: ₹X on [date], (3) "Subscription auto-renews. Cancel anytime in Settings."

---

## SPEED vs. RIGOR MODE

### Speed Mode (20 minutes)

1. **Paywall observation:**
   - When does first paywall appear? (screenshot + timestamp)
   - What's the messaging?
   - One key observation about Fogg MAP

2. **Pricing page:**
   - Navigate to pricing (screenshot)
   - Note pricing, annual plan available? Payment methods?
   - One Fogg assessment

3. **Payment flow:**
   - Is UPI available? (screenshot of payment methods)
   - Count steps to pay

4. **Cancellation:**
   - Find cancel button (screenshot + path or note "not found")

5. **Quick score:**
   - 1-10 based on first paywall timing + UPI availability + annual pricing
   - One sentence rationale
   - Top 3 issues

**Output:** Scorecard (1-10), 3 issues, 1 paragraph per issue. No comprehensive evidence bullets.

### Rigor Mode (45-60 minutes)

1. **Map all monetization touchpoints:**
   - Every paywall in the app (not just first)
   - Count paywalls per session
   - Categorize: contextual vs. broadcast, hard vs. soft

2. **Comprehensive evidence:**
   - 8-10+ screenshots covering all screens
   - Detailed observations per evidence checklist above
   - Kano categorization of free vs. premium features

3. **Full payment flow audit:**
   - Complete checkout flow (UPI, card, wallet)
   - Error handling
   - Confirmation screen
   - Payment provider and security signals

4. **Trial quality assessment:**
   - Trial entry experience
   - Onboarding to premium features (yes/no)
   - Trial-to-paid messaging

5. **Cancellation deep dive:**
   - Full cancellation path (screenshot each step)
   - Manipulation tactics (if any)
   - Win-back offer assessment

6. **Price benchmarking:**
   - Compare to domain benchmarks (from `domains/[domain].md`)
   - Compare to direct competitors
   - Tier 1-2-3 price psychology assessment

7. **Comprehensive scoring:**
   - Full rubric applied
   - 5-7 key issues with detailed evidence + frameworks
   - Competitive benchmarking

**Output:** Full Current State file with scorecard, comprehensive evidence, all key issues, competitive benchmarking, detailed scoring rationale.

---

## PERSONA-SPECIFIC GUIDANCE

### New User (First Session, No Paywall Decision Yet)

**What to audit:**
- When does first paywall appear in user journey?
- Is there value before paywall? (Reforge: Monetization-first apps fail)
- What's the perceived value of the app at paywall moment?
- Copy of first paywall (is motivation clear?)
- Fogg MAP assessment at this moment

**Example flow:** Splash → Login → Home → Content → First Paywall (or first trigger)

**Screenshot checklist:** Paywall appearance, copy, pricing, payment methods visible

**Key finding:** "New user sees paywall on screen #5 (home page, trying to access second course). Paywalls before demonstrating value = monetization-first model. Reforge predicts <1% conversion."

---

### Free User (Recurring, Multiple Paywalls)

**What to audit:**
- How many paywalls per session?
- Are they annoying/disruptive?
- Can user continue using free version after dismissing?
- Soft vs. hard paywall ratio

**Example flow:** Open app → Home (soft upsell: "Upgrade" banner) → Browse content (no paywall) → Try to download (hard paywall) → Try to search (soft upsell)

**Screenshot checklist:** Every upsell/paywall seen in session

**Key finding:** "Free user sees 5 upsells per 15-minute session (too frequent = Nielsen #3 violation). Can dismiss all and continue free. Paywall fatigue likely."

---

### Trial User (Experiencing Premium)

**What to audit:**
- Did app onboard user to premium features? (Critical)
- Did user understand what's premium vs. free?
- Did app build motivation to convert?
- Trial-to-paid conversion messaging

**Example flow:** Start trial → Welcome message (or no message?) → Explore features → Near end of trial: "Your trial ends in 3 days"

**Screenshot checklist:** Trial entry, any guidance, trial-ending messaging, win-back offer

**Key finding:** "Trial starts with no guidance. App looks identical to free version. User doesn't know what's premium. No conversion messaging until day 6 (too late). Trial experience failed to build motivation for paid."

---

### Paid User (Experiencing Renewal)

**What to audit:**
- Is renewal transparent? (Renewal date clear before charging)
- Value reinforcement? (Does app remind you what you're paying for?)
- Renewal messaging (receipt, confirmation)
- Willingness to renew (satisfaction signal)

**Example flow:** Day 28 of paid subscription → App shows "Your subscription renews tomorrow" (or no message?) → Day 29: Charged → Does app celebrate or send confirmation?

**Screenshot checklist:** Renewal reminder, billing confirmation, post-charge messaging

**Key finding:** "Paid user sees renewal charge but no clarity on renewal date before it happens. No renewal confirmation email. No value reinforcement. High risk of churn (user may not even notice they paid, then regret)."

---

### Lapsed User (Considering Re-Subscription)

**What to audit:**
- Do win-back offers exist? (Reforge: Resurrected User Retention)
- Messaging (what discount? for how long?)
- Is re-subscription easy?
- Do they see the paywall as a win-back opportunity?

**Example flow:** User had paid subscription, cancelled 3 months ago → Opens app → Sees "Welcome back" offer or regular paywall?

**Screenshot checklist:** If available, lapsed user experience, win-back offer, ease of re-subscription

**Key finding:** "Lapsed users see regular paywall (no win-back offer). Missed revenue recovery. Reforge: Resurrected User Retention unaddressed."

---

## INDIA-SPECIFIC MONETIZATION CHECKS

Every monetization review for an Indian app must include these checks:

### UPI / Google Pay / PhonePe Availability

- [ ] **UPI available?** Yes/No. If yes, is it the default option?
- [ ] **PhonePe integration?** Yes/No
- [ ] **Google Pay (UPI)?** Yes/No
- [ ] **Paytm Wallet?** Yes/No
- [ ] **Impact:** If UPI missing, estimate revenue loss (50-60% of Tier 2-3 market can't pay)

**Finding template:** "UPI missing. Only Credit/Debit card and Google Pay available. PhonePe not integrated. Estimated 55% of Tier 2-3 market unable to pay. Critical gap."

---

### Pricing in ₹ (Not USD)

- [ ] Prices displayed in ₹?
- [ ] Any prices shown in USD or other currency?
- [ ] Currency symbol clear?

**Finding template:** "Pricing shown in ₹ (₹199/month). Clear and appropriate for India market. No USD pricing visible. ✓"

---

### Annual Plan Available & Appropriately Discounted

- [ ] Annual plan offered?
- [ ] Discount vs. monthly: [X]%
- [ ] Does it meet India expectations (25-30% minimum)?
- [ ] Annual plan prominently featured?

**Finding template:** "Annual plan available: ₹1,799/year (25% savings vs. ₹199/month). Below India expectation of 30%+ savings. Annual plan not highlighted as 'Best Value.' Competitor Duolingo: ₹1,499/year (37% savings). Opportunity to improve annual positioning."

---

### ₹1 Trial Perception & Delivery

**India-specific insight:** In some segments, ₹1 pricing triggers "this is a scam" perception. In others, it's irresistible. Depends on:
- Brand trust (Duolingo ₹1 = trusted. Unknown app ₹1 = suspicious)
- Trial quality (must deliver value in first 3 days)

- [ ] If ₹1 trial offered: Does it actually deliver value in first use?
- [ ] Is ₹1 framed as "try for free" or "recurring ₹1/week"?
- [ ] Do users understand what happens after trial?

**Finding template:** "₹1 7-day trial offered. First day experience is weak (just onboarding, no core features). High trial-to-churn likely. Recommend: (1) Clarify trial is non-recurring ₹1, (2) Show core feature on day 1."

---

### Family Plan or Sharing Option

- [ ] Family plan available? (e.g., 5 members for ₹299/month)
- [ ] Account sharing detection?
- [ ] Regional pricing variation? (Higher price in Tier 1, lower in Tier 2)

**Finding template:** "No family plan. Single-user subscriptions only. Missed revenue opportunity (Indians appreciate family sharing). Competitor offering family plan at ₹349/month (for 5 people) undercuts at price-per-user."

---

### Regional Pricing Variation

- [ ] Same pricing for Tier 1 and Tier 2 users?
- [ ] Should Tier 2 see ₹99/month vs Tier 1 ₹199/month?
- [ ] Regional language support (Hindi) available?

**Finding template:** "Uniform pricing (₹199/month) across all geographies. Tier 2 users find this high. Opportunity: Offer ₹99/month tier or show annual plan as better value for budget users."

---

### Language Support (Hindi/Regional)

- [ ] Hindi support in paywall copy?
- [ ] Regional language options?
- [ ] If targeting Tier 2-3, is English-only paywall a problem?

**Finding template:** "Paywall available in English only. App targets Hindi-speaking Tier 2 audience (content is Hindi). Monetization copy in English creates friction (user reads English app benefits, but understands Hindi). Opportunity: Translate paywall to Hindi."

---

### India Competitor Monetization Benchmarks

Use these as Comparative Benchmarks alongside international references. Every monetization review of an Indian app must cite at least one Indian competitor.

**CRED — Premium Subscription Positioning:**
CRED proves Indian consumers engage with premium-positioned fintech products. Free app earns through merchant partnerships. Gamified rewards (CRED Coins) create engagement without subscription friction. Coin Rush events (3-day limited windows) drive 3x engagement spikes. Key lesson: Indian users respond to earned rewards over purchased subscriptions. Revenue per user from merchant commissions, not subscription fees.

**Meesho — Referral-First Monetization:**
Meesho monetizes through seller commissions, not user subscriptions. The buyer experience is entirely free. Referral loop: share product → earn credit when friend buys. Word-of-mouth drives 60%+ of growth. Key lesson: for mass-market India (Tier 2-3), consider monetizing the supply side (sellers, advertisers) rather than the user. Referral users have 1.4x higher LTV than organic.

**Zepto — Trial-First with Instant Value:**
Zepto's monetization is through delivery margins, not subscriptions. But their UX principle applies: users see value (products near them, delivery time) before any transaction. Zero friction to first order. Key lesson: show value before asking for money. Cashback offers (₹40-75) reduce perceived cost of first transaction. Repeat users order 3-4x/week — frequency beats high margin per transaction.

**Flipkart Plus / Black — Tiered Loyalty:**
Free tier (Flipkart Plus): earned after 4+ transactions/year, provides free delivery and member offers. No upfront cost — users earn their way in. Paid tier (Flipkart Black): ₹1,499/year for premium perks. SuperCoins earned on every purchase, redeemable across ecosystem. Key lesson: free loyalty tier → paid premium creates natural upgrade path. Plus members transact 2.5x more frequently. SuperCoin redemption drives 15%+ repeat purchase rate.

**PhysicsWallah — Affordable EdTech Pricing:**
₹2,199-4,800/year for flagship JEE/NEET courses — dramatically undercuts BYJU'S (₹20-50K/year) and Unacademy (₹18-29K/year). No EMI pressure tactics. Transparent pricing visible before signup. 4.46M paid users (up 153% from FY23). Profitable (₹69.7 Cr PAT in Q2FY26). Key lesson: cost leadership at scale is more profitable than premium pricing with aggressive sales in Indian EdTech. 60%+ of conversions cite "affordability" as primary reason.

**Scoring Modifiers (India Monetization Benchmarks):**
- +1 if pricing is competitive with PhysicsWallah/Kuku FM benchmarks for the category
- +1 if referral/loyalty mechanics exist (CRED/Flipkart model)
- +1 if value is demonstrated before payment is requested (Zepto/PhysicsWallah model)
- -1 if pricing exceeds category norms (e.g., EdTech above ₹5K/year without premium justification)
- -1 if monetization is aggressive (BYJU'S anti-pattern: sales pressure, hidden charges)
- -2 if no UPI payment AND pricing above ₹149/month (excludes Tier 2-3 entirely)

---

## OUTPUT FORMAT

This module produces evidence and key issues that will be compiled into the "Current State" file. Follow this format:

### In the Current State File, include:

```markdown
## MONETIZATION UX — X/10

### Score Breakdown
[If Rigor Mode: Detailed scoring across sub-dimensions]

### Evidence

**Paywall Timing & Frequency**
- [Bullet with screenshot reference]
- [Bullet with screenshot reference]

**Free Content Ratio**
- [Bullet with screenshot reference]

**Payment Methods**
- [Bullet with screenshot reference]

**Social Proof & Value Proposition**
- [Bullet with screenshot reference]

**Trial & Onboarding**
- [Bullet with screenshot reference]

**Cancellation Flow**
- [Bullet with screenshot reference]

**India-Specific Checks**
- [UPI availability bullet]
- [Pricing in ₹ bullet]
- [Annual plan bullet]

### Key Issues

**Issue #1: [Title]**
- Framework violated: [Framework] — [principle]
- Evidence (screenshots): [#X, #Y, #Z]
- Impact: [Reforge, Fogg, India fit]
- Severity: [Critical/High/Medium/Low]

[Repeat for each issue found]

### Competitive Benchmarking

**Vs. [Competitor A]:**
- Pricing comparison: [note]
- Freemium ratio: [note]
- Trial experience: [note]

**Vs. [Competitor B]:**
- [Same structure]

### Scoring Rationale

[1-2 paragraph explanation of score, citing frameworks, domain benchmarks, India fit]
```

---

## QUICK REFERENCE: FRAMEWORK VIOLATIONS & FIXES

| Framework | Principle | What to Audit | Red Flag | Quick Fix |
|-----------|-----------|--------------|----------|-----------|
| **Reforge** | Monetization-Engagement Alignment | Is paywall after value? | Paywall on D0 | Defer paywall to after 5 free value moments |
| **Reforge** | Freemium ratio | % of content free? | <30% free | Expand free tier to 40%+ |
| **Fogg MAP** | Motivation | Is value clear? | "Upgrade to Premium" vague copy | Show specific benefits (e.g., "500+ courses") |
| **Fogg MAP** | Ability | Can user pay? | UPI missing | Add UPI payment method |
| **Fogg MAP** | Prompt | Is CTA contextual? | Random paywalls | Show paywall when user tries to access premium |
| **Kano** | Must-Be features | Are basic features free? | Key features locked | Unlock search, basic downloads for free users |
| **Nielsen #3** | User Control | Can user cancel? | Cancel requires email | Add one-click cancel in Settings |
| **Cagan** | Value Risk | Does user want to pay? | Trial exists but no guidance | Onboard trial users to premium features |
| **AARRR** | Referral | Do users share? | No sharing on paywall | Add referral mechanics (win-back offers, share teasers) |
| **AARRR** | Retention | Do paid users renew? | No renewal clarity | Show renewal date/amount before charging |

---

*This module is designed to be executed in 20-60 minutes depending on mode. Every finding must cite frameworks and include screenshot evidence. Output feeds into the "Current State" and "Recommendations" files.*
