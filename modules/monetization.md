# Monetization UX Module (Revenue Stage)

> AARRR: Revenue | Frameworks: Reforge Monetization-Engagement Alignment, Fogg MAP, Kano, Nielsen | Speed: 20min | Rigor: 45min

<!-- SPEED MODE -->
## QUICK AUDIT
Navigate: 1. First paywall moment 2. Pricing page 3. Payment methods 4. Cancellation path 5. Trial entry (if exists) 6. Freemium content library
Check: Paywall timing (before/after value), UPI availability, annual pricing, free content ratio, cancellation ease
Score anchor: 9-10 = Paywall after 5+ free value moments, 40%+ free content, UPI default, annual 30%+ off, easy cancel. 7-8 = Paywall after 3 free moments, 50/50 free/paid, all payment methods, cancellation 2-3 clicks. 5-6 = Paywall after 2 moments, some free content, payment friction, cancel hard. 3-4 = Paywall day 0-1, <20% free, no UPI, cancel via email. 1-2 = Aggressive monetization-first, no freemium, zero trust signals.
<!-- END SPEED MODE -->

---

## SCREENS TO NAVIGATE

### 1. PAYWALL / TRIAL PROMPT (Every Instance)
**Observe:**
- Timing (seconds from app open? which screen? triggered by user action or broadcast?)
- Copy quality (is value prop clear in <2 sentences? answers "what am I paying for?")
- Visual hierarchy (dominant element: CTA, price, feature list?)
- Fogg MAP assessment (Motivation clear? Payment methods visible? CTA contextual?)
- Urgency/scarcity (countdown? limited offer? expiring trial?)
- Social proof (ratings, user count, testimonials, trust badges?)

**Screenshot:** First paywall full screen, CTA button state, pricing display

**Framework check:** Fogg MAP → Motivation (benefits visible?), Ability (payment methods present?), Prompt (contextual or broadcast?)

---

### 2. PRICING PAGE / SUBSCRIPTION OPTIONS
**Observe:**
- Plan tiers (free, single plan, multiple options?)
- Price formatting (₹/year or ₹/month? annual discount visible?)
- Feature differentiation (what's free vs. paid? visible before purchase?)
- Annual discount (% off monthly? matches India expectation of 25-30%?)
- Trial offer (₹1? 7-day free? terms clear?)
- Value messaging (tier taglines or benefit statements present?)
- Kano categorization intent (must-be, one-dimensional, attractive features?)

**Screenshot:** Full pricing page, plan comparison, annual plan positioning

**Framework check:** Reforge → Is freemium ratio 30-50% free? Are Must-Be features free? Is annual pricing prominently featured?

---

### 3. PAYMENT FLOW (UPI, Card, Wallet Options)
**Observe:**
- Payment methods available (UPI, credit/debit card, wallet, Google Pay, PhonePe?)
- UPI prominence (default or hidden? Tier 1-3 parity?)
- Payment provider (Razorpay, PhonePe, Google Play Billing?)
- Form friction (how many steps? pre-filled fields? validation feedback?)
- Security trust signals (SSL badge, encryption message, provider logos?)
- Failure handling (retry option? help text visible? Nielsen #9)
- Confirmation screen (receipt option? return to app automatic?)

**Screenshot:** Payment method selection, UPI flow entry, confirmation screen

**Framework check:** Fogg MAP Ability → Is payment method selection low-friction? Is India's primary method (UPI) accessible?

---

### 4. PREMIUM UPSELL SURFACES
**Observe:**
- Contextuality (triggered by user action vs. random broadcast?)
- Copy quality (explains benefit at that moment?)
- Hard vs. soft (blocks progress or suggests?)
- Frequency (count per free user session; >3 = annoying)
- Dismissability (can user dismiss and continue free version? Nielsen #3)

**Screenshot:** Representative upsell, dismiss state, free content continuation

**Framework check:** Reforge → Are upsells contextual (high conversion) vs. broadcast (high friction)?

---

### 5. FREE VS. PAID CONTENT DIFFERENTIATION
**Observe:**
- Visual indicators (lock icons, "Premium" badges, color differentiation?)
- Metadata visibility (can free users see what they're missing? teaser metadata?)
- Freemium ratio (% of total content accessible free? count sample set)
- Feature differentiation (premium = different feature or just more content?)
- Progression path (does free content naturally lead to premium? product loop evident?)

**Screenshot:** Content library with free/locked items, premium badge example, teaser content

**Framework check:** Reforge Engagement-First → Free tier should be useful on its own (not just teasers). Minimum 30-40% free.

---

### 6. TRIAL ONBOARDING (If Trial Exists)
**Observe:**
- Trial entry friction (how easy to start? low friction = Fogg Ability)
- Guidance for trial users (tooltips, tutorials, feature highlights shown?)
- Premium feature discovery (does app guide user to what's premium? or left to discover?)
- Trial clarity (does user know they're in trial? how long? when ends?)
- Conversion readiness (by day 3, has value been experienced?)

**Screenshot:** Trial entry point, trial welcome message (if any), premium feature highlight, trial-ending state

**Framework check:** Reforge Trial Quality → Best trials onboard user to premium features. Weak trials leave user thinking "premium = same as free."

---

### 7. RENEWAL / CANCELLATION FLOW
**Observe:**
- Cancellation discoverability (where is cancel button? Settings path clear?)
- Steps to cancel (count: 1-click ideal, <3 acceptable, 5+ = friction violation)
- Confirmation dialog (shown before cancellation? manipulative copy present? Nielsen #3)
- Win-back offer (discount shown during cancellation attempt?)
- Refund policy visibility (shown pre-purchase and post-cancellation?)
- Renewal clarity (next billing date shown before charge?)
- Auto-renewal transparency (clear subscription will renew? legal requirement)

**Screenshot:** Full cancellation path (each step), confirmation dialog, win-back offer if present

**Framework check:** Nielsen Heuristic #3 → User Control and Freedom. Cancellation ease is trust signal. Difficult cancellation = perceived scam.

---

## SCORING RUBRIC

| Score | Label | Key Criteria |
|-------|-------|-------------|
| 9-10 | Best-in-class | Paywall after 20+ free uses, 40%+ free content, social proof strong, UPI default, annual 30%+ off, easy 1-click cancel, trial onboards to premium |
| 7-8 | Good | Paywall after 5+ free uses, 50/50 free/paid, clear value prop, UPI + card available, annual discount present, <3 click cancel, trial guidance shown |
| 5-6 | Adequate | Paywall after 2-3 free uses, 50/50 free/paid, payment friction present, UPI available but secondary, annual available, cancel possible but hard, weak trial guidance |
| 3-4 | Poor | Paywall day 1, <20% free content, weak value prop, payment methods incomplete, UPI missing, cancel requires email, trial exists but no guidance |
| 1-2 | Critical | Paywall on app open, <5% free, monetization-first model, payment options missing, no annual, cancel impossible, aggressive dark patterns |

**Scoring method**: Start at 5. Add: +2 for paywall after value demo, +1 for 40%+ free content, +1 UPI prominent, +1 annual 30%+ off, +1 easy cancellation, +1 strong social proof, +1 trial onboards. Deduct: -2 paywall day 0, -2 <20% free, -1 no UPI, -1 no annual, -2 cancel via email, -1 weak value prop. Cap 1-10.

---

## EVIDENCE CHECKLIST

### Paywall Timing & Frequency [Reforge]
- [ ] First paywall appears on screen #X after Y seconds (D0, after login, after 5 screens, after first value moment)
- [ ] Paywall appears contextual (user tried premium feature) vs. broadcast (random prompt)
- [ ] Total paywalls per free user session: [count] (Reforge: >3 = too frequent)
- [ ] Soft paywalls (suggest) vs. hard paywalls (block): [ratio]
- [ ] Users can dismiss and continue free version [Nielsen #3]

**Template:** "First paywall appears screen #03 (2 min after open, after completing 1 free lesson). Subsequent 4 paywalls during session, all contextual. Screenshot: #03-paywall-first-appearance.png"

---

### Free Content Ratio [Reforge]
- [ ] Free tier includes: [specific features/content types]
- [ ] Premium-only features: [specific features/content types]
- [ ] Estimated % of total content free: [X]% (Reforge target: 30-50% free)
- [ ] Free content useful on its own, not just teasers [Kano Must-Be check]
- [ ] Freemium ratio assessment: Generous/Balanced/Restrictive

**Template:** "Free tier: 5 courses out of 50, 1 daily practice, profile creation ≈ 8% free. Remaining 92% locked. Below Reforge engagement-first model (target 30-50%). Screenshot: #04-content-library.png"

---

### Payment Methods Available [Fogg MAP Ability]
- [ ] UPI available? Yes/No. If yes: default or secondary?
- [ ] Credit/Debit card available? Yes/No.
- [ ] Wallet options (Google Pay, PhonePe, Paytm): [list]
- [ ] Payment provider: [Razorpay, PhonePe, Google Play Billing]
- [ ] Payment form friction: [step count, pre-filled fields]

**Template:** "UPI default, Credit Card, Google Pay available. PhonePe missing. Razorpay processor. 3-step form (Phone → Amount → Confirm). Screenshot: #07-payment-methods.png"

---

### Social Proof on Paywall [Fogg MAP Motivation]
- [ ] App rating visible? (e.g., ⭐4.8/5 from 45K reviews)
- [ ] User count visible? (e.g., "1.2M+ subscribers")
- [ ] Testimonials shown? How many?
- [ ] Trust badges (verified, media mentions)?
- [ ] Social proof assessment: Strong / Moderate / Weak

**Template:** "⭐4.7/5, 1.2M+ subscribers, 3 testimonials, Google Play verified. Assessment: Strong. Screenshot: #05-paywall-social-proof.png"

---

### Value Proposition Clarity [Fogg MAP Motivation]
- [ ] Paywall copy states what you get for paying (specific features, not generic "Unlock Premium")
- [ ] Copy <50 words, emotional benefit clear
- [ ] Feature list provided? Benefit statement present?
- [ ] Value clarity assessment: Clear / Moderate / Vague

**Template:** "Copy: 'Unlock all 500+ courses, unlimited downloads, offline access, ₹199/month.' Emotional benefit clear: 'Learn without limits.' Assessment: Clear. Screenshot: #05-paywall-value-prop.png"

---

### Trial Terms & Auto-Renewal Transparency [Nielsen #3, India Legal]
- [ ] Trial offer type: [₹1 7-day, free 3-day, etc.]
- [ ] Auto-renewal notice shown before purchase? [Yes/No with screenshot reference]
- [ ] Cancellation path mentioned pre-purchase? [Yes/No]
- [ ] One-click unsubscribe available? [Yes/No]
- [ ] Trial-to-paid conversion messaging present? [Yes/No]

**Template:** "₹1 7-day trial. Auto-renewal: 'Your subscription will renew at ₹199/month on [date]' shown on checkout. Cancellation path mentioned. One-click cancel in Settings. Screenshot: #06-trial-terms.png"

---

### Urgency & Scarcity Tactics [Ethical Assessment]
- [ ] Countdown timer? [Yes/No with hours remaining]
- [ ] Limited offer language? ["Only ₹49 today", "Offer expires", "Limited spots"]
- [ ] Dark patterns detected? [Unclear dismiss, pre-checked boxes, misleading copy]
- [ ] Ethical assessment: Informative scarcity / Manipulative dark patterns / None

**Template:** "'Offer expires in 4 hours' countdown. Copy: 'Get ₹149/month for ₹99 today only.' Assessment: Mild urgency (informs without coercing). No dark patterns. Screenshot: #05-paywall-urgency.png"

---

### Cancellation Ease [Nielsen #3 User Control]
- [ ] Cancellation discoverable in Settings? [Yes/No]
- [ ] Steps to cancel: [count] (1-click ideal, <3 acceptable, 5+ problematic)
- [ ] Confirmation dialog manipulative? [Yes/No with copy note]
- [ ] Win-back offer shown? [Yes/No]
- [ ] Refund policy visible pre-purchase? [Yes/No]
- [ ] Cancellation difficulty assessment: Easy / Moderate / Hard

**Template:** "Settings → Subscriptions → Cancel (3 steps). Dialog: 'Are you sure? You'll lose access to all features.' No win-back offer. Refund policy not pre-purchase. Assessment: Moderate difficulty. Screenshot: #12-cancellation-flow.png"

---

### Price Positioning [India-Specific Context]
- [ ] Price in ₹ (not USD)? [Yes/No]
- [ ] Annual plan available? [Yes/No]. If yes: [X]% discount vs. monthly
- [ ] Price point: ₹[X]/month or ₹[X]/year
- [ ] Positioning vs. competitors in domain: [higher/lower/similar]
- [ ] Tier 2-3 fit assessment: Tier 1 (₹99-199/mo) / Tier 2 (₹49-99/mo) / Tier 3 (₹29-49/mo)
- [ ] Annual discount vs. India expectation (25-30% minimum)

**Template:** "Annual: ₹1,799/year (25% savings vs. ₹199/month monthly, below India expectation). No highlight of annual as 'Best Value.' Tier 2 users may find ₹199/mo high. Competitor comparison: Duolingo ₹1,499/year. Screenshot: #04-pricing-page.png"

---

## KEY ISSUE PATTERNS

1. **Paywall Before Value** → Detect: Subscription screen on app open before any core feature use. Framework: Reforge Monetization-Engagement, Fogg MAP. Fix: Defer until after 5+ free value moments (lessons, videos, content consumed).

2. **Inverted Freemium Ratio** → Detect: <20% free content; premium dominates. Framework: Reforge. Fix: Expand free tier to 30-50% of content; unlock key features (search, downloads).

3. **No Social Proof on Paywall** → Detect: Only price shown, no ratings/testimonials/trust badges. Framework: Fogg MAP Motivation. Fix: Add rating, user count, 1-2 testimonials, trust badge.

4. **Missing UPI Payment** → Detect: Only card/wallet available; UPI absent. Framework: Fogg MAP Ability. Fix: Add UPI as default (Razorpay, PhonePe, Google Play Billing integration).

5. **Cancellation Requires Email/Support** → Detect: No in-app cancel button; must email support. Framework: Nielsen #3. Fix: Add one-click Settings → Subscriptions → Cancel.

6. **Trial Without Premium Feature Guidance** → Detect: Trial starts but app shows same content as free; no highlight of premium features. Framework: Reforge Trial Quality. Fix: Add welcome message, tooltips on premium features, conversion messaging day 3.

7. **No Annual Pricing or Poor Annual Discount** → Detect: Monthly only, or annual <25% discount. Framework: India Context. Fix: Offer annual at 30-35% savings; highlight as "Best Value."

8. **Unclear Auto-Renewal Terms** → Detect: No renewal date shown before charge; billing date vague. Framework: Nielsen #3, India Legal. Fix: Show "Next charge: ₹X on [date]" and "Subscription auto-renews. Cancel anytime."

---

## OUTPUT FORMAT

```markdown
# MONETIZATION UX — [X]/10

## Evidence Summary
- **Paywall timing**: [Before/After/During] first value (Framework: Reforge)
- **Free content ratio**: [X]% (Target: 30-50%)
- **Payment methods**: [UPI present? Default? Card? Wallet?] (Framework: Fogg MAP Ability)
- **Annual plan**: [Available? Discount %?]
- **Cancellation friction**: [Steps to cancel? In-app or email?] (Framework: Nielsen #3)
- **Social proof on paywall**: [Strong/Moderate/Weak]

## Scoring Breakdown

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Paywall timing | [X]/10 | [When paywall appears relative to value] |
| Free content ratio | [X]/10 | [% free, assessed vs. Reforge target] |
| Payment options | [X]/10 | [UPI availability, method count] |
| Cancellation ease | [X]/10 | [Steps, in-app or email] |
| Social proof | [X]/10 | [Ratings, testimonials, badges present] |
| Trial quality | [X]/10 | [Guidance to premium features present?] |
| India fit | [X]/10 | [₹ pricing, annual discount, UPI] |

**Total Score: [X]/10** | **Justification**: [1-2 sentences citing Reforge/Fogg/Nielsen]

## Key Issues

### Issue #1: [Title]
**Problem**: [What observed] | **Framework**: [Reforge/Fogg/Nielsen] | **Impact**: [User %, conversion impact] | **Hypothesis**: [1-line fix]

### Issue #2: [Title]
[Same structure]

### Issue #3: [Title]
[Same structure]

## Competitive Benchmarking
- **vs. [Competitor A]**: [Pricing, freemium ratio, trial quality, payment methods]
- **vs. [Competitor B]**: [Same structure]

**Review Conducted**: [Date] | **Duration**: [Speed / Rigor]
```
