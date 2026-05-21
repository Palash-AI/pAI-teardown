# Expert Frameworks Reference

> This file is the intellectual foundation for all pAI Review modules. Every scoring dimension, every heuristic, and every recommendation must trace back to one or more frameworks listed here. This ensures reviews are grounded in proven product and design thinking, not opinion.

---

## 1. GOOGLE HEART FRAMEWORK

**Source:** Kerry Rodden, Hilary Hutchinson, Xin Fu (Google Research, 2010)
**Use in teardown:** Structures engagement and retention scoring. Every module should assess against HEART dimensions relevant to that use case.

| Dimension | What It Measures | Signals (Goals → Metrics) |
|-----------|-----------------|---------------------------|
| **Happiness** | User satisfaction, perceived ease of use, NPS | Survey scores, in-app ratings, support ticket sentiment |
| **Engagement** | Depth and frequency of interaction | Sessions per week, watch time per session, features used per session, DAU/MAU ratio |
| **Adoption** | New users successfully onboarded | % completing onboarding, % reaching first value moment, time to first key action |
| **Retention** | Users returning over time | D1/D7/D30 retention, cohort curves, churn rate, reactivation rate |
| **Task Success** | Users completing intended goals | Task completion rate, time on task, error rate, search success rate |

**How to apply:** When scoring any module, ask: "Does this screen/flow help or hurt Happiness, Engagement, Adoption, Retention, and Task Success?" Score each. The weakest HEART dimension is the priority fix.

---

## 2. NIR EYAL'S HOOK MODEL

**Source:** Nir Eyal, "Hooked: How to Build Habit-Forming Products" (2014)
**Use in teardown:** Evaluates whether the app creates sustainable habit loops. Critical for Engagement & Retention module.

### The Hook Cycle

```
TRIGGER → ACTION → VARIABLE REWARD → INVESTMENT
   ↑                                        |
   └────────────────────────────────────────┘
```

| Phase | Definition | What to Look For |
|-------|-----------|-----------------|
| **External Trigger** | Push notification, email, ad, word-of-mouth that brings user to the app | Are notifications well-timed? Do they reference user's context? Are they personalized? |
| **Internal Trigger** | Emotional state that makes user open app without external prompt (boredom, curiosity, FOMO) | Does the app create internal triggers? Does the user think of the app when they feel [emotion]? |
| **Action** | The simplest behavior in anticipation of reward (open app, tap video, search) | Is the action easy? Low friction? Clear path? (BJ Fogg: Motivation + Ability + Trigger = Action) |
| **Variable Reward** | Unpredictable, satisfying outcome (new content, progress, social validation) | Does the app deliver variable rewards? Is content fresh? Are there surprises? Social validation? |
| **Investment** | User puts something back in (data, content, reputation, preferences) | Does the user invest in the app? Watch history? Saved content? Profile completeness? Streaks? |

**How to apply:** Map the app's hook cycle for each persona. If any phase is missing or weak, the habit loop breaks. Most failing apps break at Variable Reward (content feels same every time) or Investment (user has nothing to lose by leaving).

---

## 3. JAKOB NIELSEN'S 10 USABILITY HEURISTICS

**Source:** Jakob Nielsen, Nielsen Norman Group (1994, updated)
**Use in teardown:** Evaluates UI/UX quality across all modules. Every screen should be assessed against these 10 heuristics.

| # | Heuristic | What to Check |
|---|-----------|--------------|
| 1 | **Visibility of system status** | Does the app tell users what's happening? Loading states, progress bars, confirmation feedback, error states |
| 2 | **Match between system and real world** | Does the app use language users understand? Familiar metaphors? Cultural context appropriate for Indian audience? |
| 3 | **User control and freedom** | Can users undo actions? Go back? Exit flows? Skip optional steps? |
| 4 | **Consistency and standards** | Are UI patterns consistent across screens? Do buttons look like buttons? Does the app follow platform conventions (Android/iOS)? |
| 5 | **Error prevention** | Does the app prevent errors before they happen? Form validation, confirmation dialogs, smart defaults? |
| 6 | **Recognition rather than recall** | Is information visible when needed? Can users recognize options (not recall from memory)? Persistent navigation, visible search? |
| 7 | **Flexibility and efficiency of use** | Shortcuts for experienced users? Personalization? Multiple paths to same goal? |
| 8 | **Aesthetic and minimalist design** | Is every element necessary? No clutter? Visual hierarchy clear? Information density appropriate? |
| 9 | **Help users recognize, diagnose, recover from errors** | Clear error messages? Suggested fixes? Recovery paths? |
| 10 | **Help and documentation** | Help accessible when needed? Onboarding tooltips? FAQ? In-context guidance? |

**How to apply:** For each screen reviewed, quickly score against all 10. Flag violations as evidence. Particularly important for Cognitive Load and Onboarding modules.

---

## 4. JOBS-TO-BE-DONE (JTBD)

**Source:** Clayton Christensen, "Competing Against Luck" (2016); Tony Ulwick, "Outcome-Driven Innovation"
**Use in teardown:** Evaluates whether the app serves the actual job the user hired it for. Critical for Persona-Intent Alignment module.

### Core Concept
Users don't buy products — they "hire" them to get a job done. The job has:
- **Functional dimension:** What task am I trying to accomplish? (e.g., "Help me file my Aadhaar card")
- **Emotional dimension:** How do I want to feel? (e.g., "Feel confident I did it right")
- **Social dimension:** How do I want others to see me? (e.g., "Look competent to my family")

### Job Map (8 Steps)
1. **Define** — What is the user trying to achieve?
2. **Locate** — Find the right content/tool for the job
3. **Prepare** — Get ready to do the job (prerequisites, setup)
4. **Confirm** — Verify they have the right thing
5. **Execute** — Do the actual job
6. **Monitor** — Track progress during execution
7. **Modify** — Adjust approach if needed
8. **Conclude** — Finish and verify success

**How to apply:** For each persona, map their JTBD. Then audit whether the app supports all 8 steps. Most apps fail at steps 2 (Locate — poor discovery), 6 (Monitor — no progress tracking), and 8 (Conclude — no completion celebration).

---

## 5. BJ FOGG'S BEHAVIOR MODEL

**Source:** BJ Fogg, Stanford Persuasive Technology Lab, "Tiny Habits" (2019)
**Use in teardown:** Evaluates whether the app makes desired behaviors easy enough to happen. Critical for Onboarding and Engagement modules.

### The Formula
```
B = MAP (Behavior = Motivation × Ability × Prompt)
```

All three must be present simultaneously for a behavior to occur.

| Factor | Definition | What to Audit |
|--------|-----------|--------------|
| **Motivation** | Does the user want to do this? | Is the value proposition clear? Is there emotional payoff? Is the reward visible before the action? |
| **Ability** | Can the user do this easily? | How many steps? How much cognitive load? How much time? How much money? How much physical effort? How socially deviant? |
| **Prompt** | Is there a cue at the right moment? | Is the CTA visible? Well-timed? Contextual? Does it appear when motivation is high and ability is present? |

### Fogg's Simplicity Factors (Ability)
1. Time — does it take too long?
2. Money — does it cost too much?
3. Physical effort — is it physically hard?
4. Brain cycles — does it require too much thinking?
5. Social deviance — does it make me look weird?
6. Non-routine — is it unfamiliar?

**How to apply:** For every key user action (signup, first video, trial start, payment), map MAP. If any factor is below threshold, the behavior won't happen. Most Indian consumer apps fail on "Brain cycles" (too complex) and "Money" (perceived value vs. cost).

---

## 6. REFORGE GROWTH FRAMEWORKS

**Source:** Brian Balfour, Casey Winters, Andrew Chen (Reforge)
**Use in teardown:** Evaluates growth loops, monetization model, and retention architecture. Critical for Monetization and Retention modules.

### Growth Loops (Not Funnels)
Traditional funnels are linear (awareness → acquisition → activation → retention → revenue). Growth loops are circular — output of one cycle feeds the input of the next.

**Types of loops to audit:**
| Loop Type | How It Works | What to Look For |
|-----------|-------------|-----------------|
| **Viral Loop** | User creates content/shares → new users discover → they share | Share buttons, referral programs, social proof, certificate sharing |
| **Content Loop** | Content attracts users → users engage → engagement signals attract more users | SEO, social sharing of content, community contribution |
| **Paid Loop** | Revenue funds acquisition → new users generate revenue → fund more acquisition | LTV:CAC ratio, payback period, retention driving LTV |
| **Product Loop** | Usage creates value → value attracts more usage → more value | Network effects, data flywheel, personalization improving with usage |

### Retention Framework (3 Types)
| Type | Definition | Example |
|------|-----------|---------|
| **New User Retention** | Does the user come back after first session? | D1, D3, D7 retention |
| **Current User Retention** | Do active users stay active? | Weekly/monthly active rates, engagement depth |
| **Resurrected User Retention** | Do churned users come back? | Reactivation rate, win-back campaign effectiveness |

### Monetization-Engagement Alignment
- **Engagement-first:** Build habit → monetize habit (Duolingo, YouTube)
- **Monetization-first:** Gate content → force payment (most failing apps)
- **Balanced:** Freemium with clear upgrade trigger (Spotify, Notion)

**How to apply:** Identify which growth loops exist (or don't). Assess retention type coverage. Evaluate monetization-engagement alignment. Most Indian consumer apps have weak or no loops — they rely entirely on paid acquisition with no organic flywheel.

---

## 7. DON NORMAN'S DESIGN PRINCIPLES

**Source:** Don Norman, "The Design of Everyday Things" (1988, revised 2013)
**Use in teardown:** Evaluates fundamental UX quality. Underpins Cognitive Load and Visual Clarity module.

| Principle | Definition | What to Check |
|-----------|-----------|--------------|
| **Affordance** | Object's properties suggest how it can be used | Do buttons look tappable? Do cards look swipeable? Do inputs look editable? |
| **Signifier** | Perceivable indicator of what action to take | Are CTAs clearly labeled? Do icons communicate function? Are swipe hints visible? |
| **Mapping** | Relationship between controls and their effects | Does tapping a category show that category's content? Does back button go back? Natural spatial layout? |
| **Feedback** | Information about action results | Tap feedback (ripple, highlight)? Loading states? Success/error confirmation? Sound/haptic? |
| **Conceptual Model** | User's understanding of how the system works | Does the user understand the app's structure? Is the mental model correct? |
| **Constraints** | Limiting possible actions to prevent errors | Are impossible actions hidden/disabled? Are destructive actions confirmed? |

**How to apply:** Walk through each screen and note where Norman's principles are violated. These violations are the root cause of usability issues that appear as "confusing UI" or "users don't know what to do."

---

## 8. KANO MODEL

**Source:** Noriaki Kano (1984)
**Use in teardown:** Categorizes features by user expectation. Helps prioritize recommendations.

| Category | Definition | Example in Learning App |
|----------|-----------|----------------------|
| **Must-Be (Basic)** | Expected. Absence causes dissatisfaction. Presence doesn't delight. | Video plays. Search works. Content is findable. App doesn't crash. |
| **One-Dimensional (Performance)** | More is better. Linear satisfaction. | More free content → happier. Faster loading → happier. Better recommendations → happier. |
| **Attractive (Delighter)** | Unexpected positive. Absence doesn't cause dissatisfaction. Presence delights. | Personalized learning path. Completion certificate. AI coach that knows your context. |
| **Indifferent** | Users don't care either way. | Backend architecture. Specific font choice (unless terrible). |
| **Reverse** | Some users actively dislike this. | Aggressive notifications. Forced social features. Auto-playing videos. |

**How to apply:** Categorize every feature found in the teardown. Flag any missing "Must-Be" features as critical issues. Prioritize "One-Dimensional" improvements. Recommend "Attractive" features as differentiators. Kill "Reverse" features.

---

## 9. AARRR (PIRATE METRICS)

**Source:** Dave McClure, 500 Startups (2007)
**Use in teardown:** Maps the full user lifecycle. Ensures teardown covers every stage.

| Stage | Metric | What to Audit |
|-------|--------|--------------|
| **Acquisition** | How do users find the app? | App store optimization, ad-to-install conversion, first screen impression |
| **Activation** | Do users have a great first experience? | Time to first value, onboarding completion, first key action |
| **Retention** | Do users come back? | D1/D7/D30 retention, session frequency, engagement depth |
| **Revenue** | Do users pay? | Trial conversion, subscription rate, LTV, ARPU |
| **Referral** | Do users tell others? | Share rate, invite mechanics, word-of-mouth signals, certificate sharing |

**How to apply:** Every teardown module maps to one or more AARRR stages. The master orchestrator ensures all 5 stages are covered across modules. If a stage has no module coverage, flag it.

---

## 10. MARTY CAGAN'S PRODUCT DISCOVERY

**Source:** Marty Cagan, "Inspired" (2008, 2018) and "Empowered" (2020)
**Use in teardown:** Evaluates whether the product was built with user evidence or assumptions.

### Four Key Risks
| Risk | Question | What to Look For in Teardown |
|------|----------|------------------------------|
| **Value Risk** | Will users want this? | Is the value proposition clear? Does the app solve a real problem? Do users engage with core features? |
| **Usability Risk** | Can users figure out how to use this? | Can users complete key tasks without help? Are error rates low? Is the learning curve acceptable? |
| **Feasibility Risk** | Can we build this? | (Less relevant in teardown; more for new features) |
| **Business Viability Risk** | Does this work for the business? | Is monetization sustainable? Does engagement drive revenue? Is LTV > CAC? |

**How to apply:** For each major feature or flow, assess all four risks. Features that fail on Value Risk (users don't want it) or Usability Risk (users can't use it) should be redesigned before optimizing.

---

## FRAMEWORK-TO-MODULE MAPPING

This table shows which frameworks are primary for each teardown module:

| Module | Primary Frameworks | Secondary Frameworks |
|--------|--------------------|---------------------|
| Onboarding | Fogg (MAP), HEART (Adoption), AARRR (Activation) | Nielsen Heuristics, Norman |
| Homepage & IA | Nielsen Heuristics, Norman, HEART (Task Success) | Kano, JTBD |
| Discovery & Search | JTBD (Locate step), Nielsen (#6 Recognition), HEART (Task Success) | Norman (Signifiers) |
| Personalization | HEART (Engagement, Happiness), Reforge (Product Loop) | JTBD, Kano |
| Content Consumption | JTBD (Execute, Monitor), Hook (Variable Reward), HEART (Engagement) | Nielsen, Norman |
| Engagement & Retention | Hook Model (full cycle), Reforge (Retention), HEART (Retention) | Fogg, AARRR (Retention) |
| Monetization UX | Reforge (Monetization-Engagement), AARRR (Revenue), Fogg (MAP) | Kano, Cagan (Value/Viability) |
| AI Integration | JTBD, HEART (Happiness, Task Success), Kano (Attractive) | Norman, Nielsen |
| Cognitive Load & Visual Clarity | Nielsen Heuristics (all 10), Norman (all 6), HEART (Happiness) | Fogg (Ability) |
| Persona-Intent Alignment | JTBD (full job map), HEART (all 5), Cagan (Value Risk) | Fogg, Hook (Internal Trigger) |

---

## APPLYING FRAMEWORKS IN INDIAN CONSUMER CONTEXT

When using these frameworks for Indian consumer apps, apply these adjustments:

1. **Fogg's Ability factors shift in India:**
   - "Money" sensitivity is 3-5x higher than US/EU. ₹149/month competes with mobile recharge, not Netflix.
   - "Brain cycles" matter more — average Indian mobile user has lower app literacy than US counterpart (especially Tier 2-3).
   - "Non-routine" is critical — many users are first-generation smartphone users. App conventions that feel "obvious" to designers may be novel to users.

2. **Hook Model triggers differ in India:**
   - WhatsApp is the primary external trigger channel (not email, not SMS for engagement).
   - Internal triggers are more community/family-driven ("my friend told me about this") than individual.
   - Variable rewards should be culturally calibrated — progress in English learning has different emotional weight than progress in a game.

3. **AARRR Referral is WhatsApp-first:**
   - Share mechanics must be WhatsApp-native (pre-filled message + deep link).
   - Certificate/badge sharing to Instagram Stories is secondary.
   - "Tell 3 friends" works better than "post to social media" in India.

4. **Kano Model "Must-Be" features differ:**
   - Hindi/regional language support is Must-Be (not Attractive).
   - Low data usage / offline mode is Must-Be in Tier 2-3.
   - UPI/wallet payment options are Must-Be (credit card is not standard).

5. **Pricing psychology:**
   - Annual pricing works better than monthly in India (feels like a "deal").
   - ₹1 trial triggers "too cheap, must be a scam" for some segments.
   - Free-to-paid conversion needs 5-10x more value demonstration than US.

---

*This document is referenced by all teardown modules. When scoring any dimension, cite the specific framework and principle being violated or satisfied.*
