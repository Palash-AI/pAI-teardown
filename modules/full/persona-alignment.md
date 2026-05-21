# Persona-Intent Alignment Module

## MODULE OVERVIEW

### What This Module Reviews
This module evaluates whether the app serves different user personas differently—or if it's a one-size-fits-all experience. It assesses the app's ability to detect and adapt to different user types, contexts, intents, and skill levels. This is critical for apps that serve diverse audiences (educators and learners, beginners and experts, casual and power users).

**Scope**: Testing the app across multiple personas (new user, intermediate, expert; casual, power; different goals), checking for adaptive UI, personalized CTAs, persona-specific success metrics, and whether the app feels "made for me" or generic.

### AARRR Stage Mapping
**All Stages** — Persona alignment directly impacts every stage:
- **Acquisition**: Does marketing target right personas? Do personas feel the app is for them?
- **Activation**: Does onboarding adapt to persona? Does first value differ by type?
- **Engagement**: Does the app feel relevant to this persona's goals?
- **Retention**: Do personas see continued value or does the app feel stale?
- **Revenue**: Does monetization align with persona's willingness to pay?
- **Referral**: Do personas recommend to others like them?

### Design Skill Integration (Mandatory for Screenshots)

> **`design:critique`** — Run on screenshots from different persona paths (if testable: new user vs returning, beginner vs expert, different exam types). Evaluate: does the UI adapt visually for different personas? Are CTAs and content hierarchy persona-appropriate? Is the design flexible enough to serve multiple personas without feeling generic? For India context: does the app look different for Tier 1 vs Tier 2 users? Is the design approachable for first-time app users (Tier 3)?

> **`design:ux-copy`** — Run on persona-specific copy: onboarding questions, welcome messages, feature labels, and CTAs shown to different user types. Evaluate: are questions JTBD-focused ("What do you want to achieve?" > "How old are you?")? Do CTAs match persona intent? For India context: are persona questions in Hindi for Tier 2-3 onboarding? Does the app use exam-specific language for EdTech personas ("JEE 2026 preparation" > "Science courses")?

### Primary Frameworks & Models

| Framework | Application |
|-----------|-------------|
| **JTBD (Full Job Map)** | What job does each persona hire the app to do? |
| **HEART (All 5 Dimensions)** | Different personas may have different success metrics |
| **Cagan's Value Risk** | Does the app demonstrate value differently to different personas? |
| **Fogg's Behavior Model (MAP)** | Different personas have different motivation, ability, and prompt needs |
| **Hook Model (Internal Triggers)** | Does the app create different internal triggers for different personas? |

---

## SCREENS TO NAVIGATE

### 1. Persona Detection & Onboarding Segmentation
**Purpose**: Understand how the app identifies and segments users.

**What to Observe**:
- Persona identification: App asks JTBD questions / Assumes all same / Detects via behavior
- Questions ask about: Job/goal / Experience level / Use case / All of above / Generic
- Segmentation visible: Does onboarding change based on persona? Or same for all?
- Persona labels: Does app label personas (e.g., "You're a Beginner")? / Hidden / Not segmented
- Segment-specific value prop: Does app explain why it's good for THIS persona?
- Onboarding time varies: Does onboarding length vary by persona (expert = shorter)? / Same for all

**India-Specific Observations:**
- Does the app detect Task Finisher vs Explorer vs Structured Learner behavioral personas?
- Does the app differentiate Tier 1 vs Tier 2-3 versions of the same persona (different content, pricing)?
- Are age-based Indian behavioral patterns reflected (Gen Z social-first vs Young Millennial career-focused)?
- Is the persona framework India-aware (exam-specific for EdTech, tier-specific for consumer apps)?

**What to Screenshot**:
- Onboarding questions (full sequence)
- Different onboarding paths (if available)
- Persona acknowledgment (if any)
- First screen for different personas (if testable)
- Personalized value prop (if shown)

**What to Document**:
- Number of personas app is designed for (estimated)
- Persona detection method (questions / behavioral / none)
- Onboarding segmentation (yes / no)
- Whether different personas see different first value
- Persona acknowledgment (explicit label / implicit / none)

**Framework Checkpoints**:
- **JTBD**: Questions should probe the job; answers segment personas
- **Fogg MAP**: Different personas need different prompts and ability scaffolding
- **Cagan Value Risk**: Each persona has different value perception; onboarding should show their specific value

---

### 2. Adaptive Content & Feature Visibility
**Purpose**: Assess whether content and features adapt to persona.

**What to Observe**:
- Content adaptation: Same content for all / Filtered by persona / Difficulty levels / All visible
- Feature hiding: Advanced features hidden from beginners / Shown to all / Always visible
- Difficulty/level options: Beginner/Intermediate/Advanced clearly differentiated / Not differentiated
- Progressive disclosure: Features revealed as user progresses / All at once
- Smart defaults: Does app set defaults based on persona (e.g., beginner mode default)? / Same for all
- Content recommendations vary: Different personas see different recommendations / Generic trending
- Community/social: Does app segment by persona (forums, study groups)? / All mixed

**What to Screenshot**:
- Content for beginner vs. intermediate persona (if testable)
- Advanced features hidden (if applicable)
- Difficulty selection or auto-detection
- Progressive feature disclosure
- Personalized content recommendations by persona
- Community/social features (if persona-segmented)

**What to Document**:
- Adaptive content presence (yes / no / partial)
- Difficulty levels visible and distinct (yes / no / unclear)
- Feature hiding for complexity (yes / no)
- Progressive disclosure (yes / no)
- Content recommendation variation by persona (obvious / generic)
- Community segmentation (yes / no / not applicable)

**Framework Checkpoints**:
- **JTBD**: Content should serve the job for this specific persona
- **Fogg Ability**: Beginners need simpler content; experts need advanced
- **Hook Model**: Different personas may need different variable rewards

---

### 3. Adaptive UX & Persona-Specific Flows
**Purpose**: Understand whether the UI adapts to persona needs.

**What to Observe**:
- Navigation changes: Do navigating options change by persona? / Same for all
- CTA variations: Does app show different CTAs for different personas? / Same for all
- Shortcut visibility: Do expert personas get direct shortcuts? / Same navigation for all
- Tutorial presence: New users get guided tour / Experts skip / No tutorial
- Help/support: Different help for beginners / Same for all / Not available
- Notifications: Different notification preferences by persona / Same for all
- Onboarding quiz revisit: Can user change persona later? / One-time assignment / Not possible
- Settings complexity: Beginner-simple vs. expert-full settings? / Same settings for all

**What to Screenshot**:
- Navigation menu for different personas (if visibly different)
- CTA variations by persona (if present)
- Tutorial or guided flow (if persona-specific)
- Help/support offering (different or same)
- Settings page (simple vs. complex options)
- Notification preferences (if persona-specific)

**What to Document**:
- Navigation adaptation (yes / no)
- CTA adaptation (yes / no)
- Shortcut/speed paths for experts (yes / no)
- Tutorial adaptation (yes / no / always present)
- Help system segmentation (yes / no)
- Settings complexity variation (yes / no)

**Framework Checkpoints**:
- **Fogg MAP**: Experts want shortcuts (high ability); beginners want guidance (lower ability)
- **Norman (Affordances)**: Advanced features should be discoverable by experts, hidden from beginners
- **JTBD Execute**: Different personas may need different execution paths

---

### 4. Success Metrics & Personas
**Purpose**: Assess whether success is defined differently for different personas.

**What to Observe**:
- Success definition varies: Different personas have different goals / All same goal
- Progress tracking adapted: Beginner sees milestones; expert tracks depth / Same tracking for all
- Milestone celebrations: Different milestones by persona (finish first course vs. 100% complete) / Same for all
- Stretch goals: Are advanced users challenged with harder content? / No progression
- Gamification adapted: Points/streaks for casual / In-depth metrics for serious / Same for all
- Achievement badges: Different badges by persona (e.g., "Certified" vs. "Just Started") / Generic badges
- Performance metrics: Does app show different stats by persona? (e.g., percentile vs. absolute) / Same metrics for all

**What to Screenshot**:
- Progress tracking for different personas
- Milestone celebrations (different or same)
- Achievement/badge system
- Performance dashboard (if persona-specific)
- Stretch goals or challenge tiers
- Success acknowledgment

**What to Document**:
- Success metric variation (yes / no)
- Progress tracking adaptation (yes / no)
- Milestone variation by persona (yes / no)
- Gamification adaptation (yes / no)
- Achievement system persona-awareness (yes / no)
- Challenge/stretch goals present (yes / no)

**Framework Checkpoints**:
- **HEART**: Different personas may have different engagement, adoption, or retention drivers
- **Cagan Value Risk**: Success looks different for different personas
- **Hook Model**: Different personas need different rewards

---

### 5. Monetization & Persona
**Purpose**: Understand whether pricing and paywall adapt to persona.

**What to Observe**:
- Free tier by persona: Different free tiers / Same free tier for all
- Trial length varies: Experts get shorter trial (they decide faster) / Same for all
- Pricing transparency by persona: Is cost justified differently? / Same justification for all
- Upsell timing: When is paywall shown? Different by persona or same? / Not applicable
- Payment options: All personas see same payment methods / Different options
- Perceived value by persona: Does app emphasize different value to different personas?
- Student/teacher discount: Tier-appropriate pricing / Not available

**What to Screenshot**:
- Free tier offering (all same or varied)
- Trial terms (if varied by persona)
- Pricing presentation (different or same)
- Paywall messaging (persona-specific or generic)
- Payment options (all same or varied)
- Special pricing (student, teacher, etc.)

**What to Document**:
- Free tier variation (yes / no)
- Trial adaptation (yes / no)
- Pricing messaging variation (yes / no)
- Paywall persona-awareness (yes / no)
- Payment option variation (yes / no)
- Special pricing for personas (yes / no)

**Framework Checkpoints**:
- **Cagan Value Risk**: Different personas perceive value differently; paywall messaging should reflect
- **Fogg MAP**: Expert users may convert faster; beginners may need more persuasion
- **AARRR Revenue**: Persona-aligned pricing increases conversion

---

### 6. Communication & Persona
**Purpose**: Assess whether the app communicates differently to different personas.

**What to Observe**:
- Messaging tone varies: Beginner (friendly, simple) vs. expert (technical, efficient) / Same tone for all
- Language complexity: Jargon avoided for beginners / Technical terms for experts / Same language for all
- Notifications differ: Beginners get more guidance / Experts get brief updates / Same for all
- Email/in-app messaging: Different by persona / Same copy for all
- Community language: Beginner discussions vs. expert discussions / All mixed / No community
- Learning resources: Different resource complexity by persona / Same resources for all

**What to Screenshot**:
- In-app messaging/notifications (sample for different personas)
- Help text or guidance (if varied)
- Community discussions (if persona-segmented)
- Email or push notifications (if persona-specific)
- Help documentation (different complexity or same)

**What to Document**:
- Messaging tone variation (yes / no)
- Language complexity adaptation (yes / no)
- Notification segmentation (yes / no)
- Community segmentation (yes / no / not applicable)
- Learning resource variation (yes / no)

**Framework Checkpoints**:
- **Fogg Motivation**: Messaging should motivate this specific persona
- **Norman (Conceptual Model)**: Language should match persona's mental model
- **JTBD**: Communication should help persona accomplish their specific job

---

### 7. Persona-Specific Onboarding Depth
**Purpose**: Evaluate whether onboarding length/depth varies by persona.

**What to Observe**:
- Expert users: Can they skip onboarding or is it forced? / Can skip / Always required
- Beginner users: Is onboarding more extensive? / Same length for all / No onboarding
- Time to value varies: Beginners take longer to reach first value / Same for all
- Content scaffolding: Are prerequisites shown for beginners? / All content available immediately
- Guided tours: First-time users get guided steps / Power users skip / No tour
- Practice/exercises: Included for beginners / Optional for experts / Not available

**What to Screenshot**:
- Onboarding flow for different personas (if testable)
- Skip option (if available)
- Guided tour (if persona-specific)
- Time to first value for beginner vs. expert

**What to Document**:
- Onboarding skip option (yes / no)
- Onboarding length variation (yes / no / same length)
- Guided tour availability (yes / no / optional)
- Content scaffolding (yes / no)
- Practice exercises (yes / no / optional)
- Time to value variation (measurable difference / same for all)

**Framework Checkpoints**:
- **Fogg Ability**: Beginners need simpler, shorter paths; experts need quick access
- **JTBD**: Onboarding should prepare persona for their specific job
- **HEART Adoption**: Different personas activate differently; adapt onboarding

---

## SCORING RUBRIC (1-10)

### 9-10: Best-in-Class Persona Alignment (Duolingo, Skillshare, Notion Level)

**Criteria**:
- **Personas clearly identified**: App asks JTBD questions; identifies 3+ persona types
- **Content adapts to persona**: Different content, features, difficulty levels visible for each
- **UX is persona-specific**: Navigation, CTAs, shortcuts, help all vary by persona
- **Success metrics differ**: Progress tracking, milestones, achievements vary by persona
- **Onboarding varies significantly**: Expert = 30 sec to first value; Beginner = 3 min with guidance
- **Monetization aligned**: Free tiers, pricing, paywall timing vary by persona
- **Communication matches persona**: Tone, language, notifications adapted
- **User can change persona**: If goals change, user can update persona anytime
- **Persona-specific challenges/goals**: Different personas see different success metrics
- **Evidence throughout**: Walking through app as different persona feels like "made for me"

**Framework Alignment**:
- **JTBD**: Each persona's job is specifically served
- **HEART**: All 5 dimensions (happiness, engagement, adoption, retention, task success) are persona-aware
- **Cagan Value Risk**: Value proposition clearly differs by persona
- **Fogg MAP**: Each persona gets optimized motivation, ability, and prompts
- **Hook Model**: Different personas experience different internal triggers and rewards

**Examples**: Duolingo (casual vs. serious learners), Skillshare (hobbyists vs. professionals), Notion (personal vs. team)

---

### 7-8: Good / Well-Designed Persona Support

**Criteria**:
- **Personas identified**: App asks questions; identifies 2-3 persona types
- **Content partially adapts**: Some content varies by persona; some is one-size-fits-all
- **UX mostly persona-specific**: Some navigation/CTA variation; not comprehensive
- **Success metrics partially adapted**: Some persona-specific tracking; some generic
- **Onboarding somewhat varies**: Beginner and expert flows are noticeably different
- **Monetization somewhat aligned**: Free tier may vary; pricing is mostly same
- **Communication mostly matches**: Tone is slightly adapted; language is mostly consistent
- **User can see persona**: Persona is mentioned or settings can be changed
- **Some persona-specific features**: Not all features, but some are persona-aware

**Framework Alignment**:
- **JTBD**: Some persona-specific job support; some generic
- **HEART**: Partially adapted to persona
- **Fogg**: Some persona-specific motivation or ability support

**Examples**: Many good educational and productivity apps

---

### 5-6: Adequate / Minimal Persona Awareness

**Criteria**:
- **Personas somewhat identified**: Maybe a quiz, but results not strongly used
- **Content mostly generic**: One-size-fits-all for most content; maybe difficulty levels
- **UX is mostly generic**: Navigation is same for all; no persona-specific CTAs
- **Success metrics are generic**: Same progress tracking for all personas
- **Onboarding is same**: All users see similar flow; maybe an option to skip
- **Monetization is not persona-aligned**: Same free tier, pricing, trial for all
- **Communication is generic**: Tone and language same for all
- **Persona not mentioned**: User may not realize app thinks of them as a persona
- **Some awareness but minimal adaptation**: App knows persona exists but doesn't serve it well

**Framework Alignment**:
- **JTBD**: Generic job understanding; some personas served, others not
- **HEART**: Limited persona-specific adaptation
- **Fogg**: Minimal persona-specific optimization

**Examples**: Many average apps with basic onboarding questions that aren't used

---

### 3-4: Poor / One-Size-Fits-All Design

**Criteria**:
- **No persona identification**: No questions asked; no segmentation
- **Content is completely generic**: All users see same content; no difficulty levels
- **UX is identical for all**: Same navigation, CTAs, features for everyone
- **Success metrics are one-size**: All users tracked same way; no persona variation
- **Onboarding is same**: All users see same flow; no skip option
- **Monetization ignores personas**: Expert willing to pay ≠ beginner, but pricing same
- **Communication is generic**: Same tone, language, notifications for all
- **App feels generic**: Doesn't feel "made for me"; could serve anyone

**Framework Alignment**:
- **JTBD Failure**: App doesn't adapt to different jobs
- **Cagan Value Risk**: Fails to demonstrate value to diverse personas
- **Fogg**: No persona-specific optimization; some personas frustrated

**Examples**: Many simple or legacy apps

---

### 1-2: Severely Flawed / Actively Alienates Some Personas

**Criteria**:
- **Wrong persona assumption**: App assumes beginner or expert; penalizes the other
- **Forced path**: User can't adapt to their needs; one path forced on all
- **Opposite of persona needs**: App recommends wrong content; suggests wrong features
- **Monetization misaligned**: Pricing is wrong for many personas
- **Communication mismatched**: Tone alienates some personas
- **Personas are actively harmed**: Some personas feel the app isn't for them at all

**Framework Alignment**:
- **JTBD Failure**: App actively prevents some personas from accomplishing their job
- **Cagan Value Risk**: Value proposition is wrong for many personas
- **Fogg**: Some personas have zero motivation or high friction

**Examples**: Apps that assume one persona only; legacy enterprise tools

---

## EVIDENCE CHECKLIST

### Persona Detection

- [ ] **Personas app targets**: [Estimated number: _____]
- [ ] **Persona identification method**: [JTBD questions / Behavioral / Explicit / None]
- [ ] **Questions ask about**: [Job/goal / Experience / Use case / Demographics / None]
- [ ] **Persona labels**: [Explicit label (e.g., "Beginner") / Implicit / None]
- [ ] **User can change persona**: [Yes / No / Not applicable]

**Framework**: JTBD, Fogg (MAP)

---

### Content Adaptation

- [ ] **Content varies by persona**: [Significantly / Somewhat / Not at all]
- [ ] **Difficulty levels visible**: [Clear / Implicit / Not available]
- [ ] **Features hidden for complexity**: [Yes / No]
- [ ] **Recommendations personalized**: [By persona / Generic trending]
- [ ] **Community segmented**: [Yes / No / Not applicable]
- [ ] **Examples of adaptation**: [List specific differences for different personas]

**Framework**: JTBD, Fogg (Ability)

---

### UX Adaptation

- [ ] **Navigation varies**: [Yes / No]
- [ ] **CTAs vary**: [Yes / No]
- [ ] **Shortcuts for experts**: [Yes / No]
- [ ] **Tutorial adaptation**: [Yes, persona-specific / Yes, everyone / No]
- [ ] **Help segmentation**: [Yes / No]
- [ ] **Settings complexity**: [Simple vs. Full / All same level]

**Framework**: Fogg (MAP), Norman

---

### Success Metrics

- [ ] **Success definition varies**: [Yes, by persona / No, same for all]
- [ ] **Progress tracking adapted**: [Yes / No]
- [ ] **Milestones persona-specific**: [Yes / No]
- [ ] **Achievements vary**: [Yes / No]
- [ ] **Challenges adapt**: [Yes / No]
- [ ] **Performance metrics vary**: [Yes, percentile vs. absolute / No, same metric]

**Framework**: HEART (all 5), Cagan (Value Risk)

---

### Monetization

- [ ] **Free tier varies**: [Yes / No]
- [ ] **Trial length varies**: [Yes / No]
- [ ] **Pricing messaging varies**: [Yes / No]
- [ ] **Paywall timing varies**: [Yes / No]
- [ ] **Payment options vary**: [Yes / No]
- [ ] **Special pricing available**: [Yes, e.g., student / No]

**Framework**: Fogg (MAP), Cagan (Value Risk), AARRR (Revenue)

---

### Communication

- [ ] **Messaging tone varies**: [Yes, beginner vs. expert / No, same tone]
- [ ] **Language complexity varies**: [Yes / No]
- [ ] **Notifications segmented**: [Yes / No]
- [ ] **Email/in-app messaging varies**: [Yes / No]
- [ ] **Community segmented**: [Yes / No]
- [ ] **Learning resources vary**: [Yes, by complexity / No, same resources]

**Framework**: Fogg (Motivation), JTBD

---

### Onboarding

- [ ] **Skip option for experts**: [Yes / No]
- [ ] **Extended for beginners**: [Yes / No / Same length]
- [ ] **Guided tour**: [Yes, persona-specific / Yes, everyone / No]
- [ ] **Practice/exercises**: [Yes, for beginners / Yes, optional / No]
- [ ] **Time to first value by persona**: [Beginner: _____ sec / Expert: _____ sec]
- [ ] **Scaffolding/prerequisites**: [Yes / No]

**Framework**: Fogg, JTBD (Activation)

---

### Overall Persona Alignment

- [ ] **Personas clearly served**: [Yes, multiple distinct paths / Somewhat, minimal variation / No, one-size-fits-all]
- [ ] **Evidence of persona thinking**: [Throughout app / Only onboarding / Not evident]
- [ ] **User feels "made for me"**: [Likely yes / Neutral / Unlikely]

**Framework**: JTBD (full), HEART (all 5), Cagan

---

## KEY ISSUES TEMPLATE

### Issue #1: One-Size-Fits-All Design; App Doesn't Adapt to Different Personas
**Problem**: App treats all users identically. No onboarding questions or segmentation. Beginners and experts see same content and features.

**Framework Cite**:
- **JTBD**: Beginners' job is different (learn, build confidence) from experts' (deepen, master). App serves neither well.
- **Cagan Value Risk**: App doesn't demonstrate value to different personas. Beginners see complexity; experts see shallow content.
- **Fogg MAP**: Beginners need guided, simple paths; experts need shortcuts. Same path frustrates both.
- **HEART**: Different personas have different engagement, adoption, and retention drivers. Ignoring this kills engagement.

**Evidence**: Walkthrough as beginner vs. expert shows identical experience. Same content, CTAs, features for all.

**Quantified Impact**: Apps with strong persona alignment see 50-100% higher engagement across different user types. One-size-fits-all apps see high churn (wrong for most personas).

**Hypothesis for Improvement**:
1. **Identify 2-3 target personas**: Beginner/intermediate/expert, or casual/serious, or different use cases
2. **Ask JTBD questions in onboarding**: "What's your goal?", "How much experience do you have?", "How will you use this?"
3. **Adapt content by persona**: Different difficulty levels, features, recommendations
4. **Adapt UX by persona**: Shortcuts for experts, guidance for beginners
5. **Test with different personas**: Each persona should feel "made for me"

Estimated impact: 50-100% improvement in engagement, 30-50% improvement in retention, 25-40% improvement in conversion by persona.

**Comparative Benchmark**: Duolingo asks "Why are you learning?" and adapts content. Skillshare targets beginner creators vs. professional educators. Notion serves personal users vs. team use. All strongly persona-aligned.

---

### Issue #2: Onboarding Personas But Content Isn't Segmented
**Problem**: App asks JTBD questions during onboarding, identifies persona, but then shows same content/features for all.

**Framework Cite**:
- **JTBD**: Questions identify persona's job, but content doesn't serve it. Persona identification without adaptation is useless.
- **Fogg Motivation**: User answers questions expecting the app to personalize. Lack of adaptation = broken promise = motivation drops.
- **HEART**: Adoption is hurt (user doesn't see value); engagement is hurt (content isn't relevant).

**Evidence**: Answer onboarding questions; document persona assignment. Then navigate content—is it different? Screenshot comparison.

**Quantified Impact**: Apps that ask but don't adapt see minimal engagement improvement. Apps that ask AND adapt see 40-60% engagement improvement. Asking without adapting feels worse than not asking.

**Hypothesis for Improvement**:
1. **Ensure questions drive adaptation**: If you ask "beginner vs. expert", use that to filter content
2. **Make adaptation visible**: User should see "This content is for beginners" or difficulty markers
3. **Test adaptation**: Create beginner account and expert account. Content should be noticeably different.
4. **Progressive disclosure**: Show simple first, expert features hidden until needed

Estimated impact: 40-60% improvement in perceived personalization, 20-30% improvement in engagement.

**Comparative Benchmark**: Duolingo asks goal; content adapts. Skillshare asks experience level; course difficulty filters by level. Both make adaptation obvious.

---

### Issue #3: Expert Users Can't Skip Onboarding; Forced into Beginner Path
**Problem**: Expert users are forced through the same slow onboarding as beginners. No skip option. Frustrating for power users.

**Framework Cite**:
- **Nielsen #3 (User Control)**: Users should have freedom to skip optional steps
- **Fogg Ability**: Forced onboarding is friction that reduces ability
- **Fogg Motivation**: Expert users are demotivated by treating them as beginners

**Evidence**: Try to skip onboarding as an expert. Is skip button available? Time to first value as expert (vs. beginner).

**Quantified Impact**: Apps that let experts skip onboarding see 50-100% improvement in expert activation. Expert users abandon if onboarding is too long.

**Hypothesis for Improvement**:
1. **Offer skip option**: "I know this app" button that skips onboarding
2. **Detect expertise**: If user answers "advanced" to multiple questions, offer skip
3. **Fast path for experts**: If not skipped, at least reduce time to first value
4. **Optional guidance**: Provide tooltips for features but don't force tutorial

Estimated impact: 50-100% improvement in expert activation, 40% improvement in expert retention.

**Comparative Benchmark**: Slack lets power users skip setup. Notion has "Templates" that let experienced users jump in quickly. Both respect user expertise.

---

### Issue #4: Content is One Difficulty Level; No Beginner vs. Advanced Path
**Problem**: All content is same difficulty. Beginners are overwhelmed; experts are bored.

**Framework Cite**:
- **Fogg Ability**: Too-hard content = low ability = abandonment. Too-easy content = low motivation = abandonment.
- **JTBD**: Beginners' job is to learn basics; experts' job is to deepen. Same content serves neither.
- **Hook Model**: Content should match skill level for optimal reward.

**Evidence**: Try content as beginner (confusing?). Try as expert (bored?). Screenshot both paths.

**Quantified Impact**: Apps with difficulty levels see 50-100% better completion rates. Apps with one level see 30-40% abandonment (users choose wrong level or leave).

**Hypothesis for Improvement**:
1. **Create 2-3 difficulty levels**: Beginner, intermediate, advanced (or equivalent)
2. **Make difficulty obvious**: Label each course/lesson with difficulty
3. **Adaptive progression**: Suggest next level when current is completed
4. **Option to adjust**: Let users change difficulty mid-course

Estimated impact: 50-100% improvement in completion rate, 40% improvement in engagement depth.

**Comparative Benchmark**: Duolingo has difficulty levels (Stories, Lessons, Podcasts for different levels). Skillshare sorts by beginner/intermediate/advanced. Both see high completion.

---

### Issue #5: Monetization Ignores Personas; Same Price for All
**Problem**: Same pricing for casual users and serious users. Beginners see same price as experts.

**Framework Cite**:
- **Cagan Value Risk**: Different personas perceive value differently. Casual users see less value than serious users.
- **Fogg Motivation**: Experts are willing to pay more; beginners are price-sensitive. Flat pricing leaves money on table and alienates beginners.
- **AARRR Revenue**: Persona-aligned pricing increases LTV and conversion.

**Evidence**: Compare free tier and pricing for different personas (if segmented at all).

**Quantified Impact**: Apps with tiered pricing (free for casual, paid for serious) see 30-50% better free-to-paid conversion. Apps with flat pricing see lower conversion.

**Hypothesis for Improvement**:
1. **Segment free tier**: Casual users get free tier; serious users see upgrade value
2. **Tier-appropriate pricing**: Explore whether different personas have different willingness to pay
3. **Trial variation**: Experts may convert faster; shorten trial; beginners may need longer trial
4. **Special pricing**: Student/teacher discounts if applicable

Estimated impact: 30-50% improvement in free-to-paid conversion, 20-30% improvement in LTV.

**Comparative Benchmark**: Skillshare offers annual plans (serious learners) vs. monthly (casual). Duolingo offers different tiers (free, Plus, Super). Both align pricing to personas.

---

### Issue #6: Communication Tone Doesn't Match Persona
**Problem**: App uses same tone for all users. Technical jargon for beginners; oversimplified for experts. Communication misses the mark.

**Framework Cite**:
- **Fogg Motivation**: Communication that matches persona's mental model increases motivation
- **JTBD**: Beginners and experts understand different terminology; communication should match
- **Norman (Conceptual Model)**: App's mental model should match persona's understanding

**Evidence**: Compare in-app messaging (notifications, help text, error messages) for different personas. Does tone match?

**Quantified Impact**: Apps with persona-matched communication see 20-30% higher satisfaction. Apps with mismatched communication feel generic.

**Hypothesis for Improvement**:
1. **Tone for beginners**: Friendly, encouraging, simple language, celebrate small wins
2. **Tone for experts**: Efficient, technical, less hand-holding, respect their expertise
3. **Test with personas**: Beginners should feel welcomed; experts should feel respected
4. **Segment messaging**: Different notifications, help text, error messages by persona

Estimated impact: 20-30% improvement in satisfaction, 15-25% improvement in perceived personalization.

**Comparative Benchmark**: Duolingo's tone is fun and celebratory (beginner-friendly). Professional learning apps have technical tone (expert-friendly). Both match their audience.

---

## SPEED MODE vs RIGOR MODE

### SPEED MODE (15-20 minutes)
1. Check onboarding → Questions asked? Persona identified?
2. Check content → Same for all or varies by persona?
3. Check features → All visible or hidden for beginners?
4. Check onboarding variation → Same length for all or varies?
5. Check monetization → Same pricing for all or varies?
6. Note 2-3 key issues
7. Assign score

**Output**: 1-2 pages

---

### RIGOR MODE (45-60 minutes)
1. Full onboarding audit as multiple personas
2. Content audit for 2-3 different personas
3. Feature visibility comparison
4. UX audit (navigation, CTAs, help)
5. Success metrics audit
6. Monetization audit
7. Communication tone audit
8. Onboarding depth variation
9. Test app as beginner → expert → power user (3+ walkthroughs)
10. Full Evidence Checklist
11. 5-7 key issues
12. Detailed scoring

**Output**: 5-10 pages

---

## PERSONA WALKTHROUGHS

### Persona 1: New Beginner User
**Description**: Installing app for the first time, zero experience, unsure if app is for them.

**Test**:
1. Does app ask JTBD questions?
2. Is beginner-friendly onboarding offered?
3. How long to first value?
4. Does content match beginner level?
5. Are advanced features hidden?
6. Does communication feel welcoming?

**Document**: Time to first value, clarity of first interaction, beginner-specific adaptations

---

### Persona 2: Intermediate / Returning User
**Test**:
1. Does app remember persona?
2. Are recommendations appropriate?
3. Can user access more advanced content?
4. Is next level suggested naturally?

**Document**: Personalization persistence, progression clarity

---

### Persona 3: Expert / Power User
**Test**:
1. Can they skip onboarding?
2. Are shortcuts available?
3. Can they access advanced features directly?
4. Is communication efficient or oversimplified?

**Document**: Expert efficiency, expert respect

---

## DOMAIN-SPECIFIC OVERLAYS

### Education Apps
- **Domain criteria**: Are difficulty levels clearly differentiated? Does app track progress by level?
- **Scoring modifier**: +1 if difficulty adaptation is dynamic; -1 if all content is same level

### OTT / Streaming
- **Domain criteria**: Are recommendations varied by viewing history or persona?
- **Scoring modifier**: +1 if beginner gets easy content; expert gets niche/advanced

### Productivity / Note-Taking
- **Domain criteria**: Do personal users get simpler UX than team users?
- **Scoring modifier**: +1 if interface adapts by use case

---

## INDIA-SPECIFIC CHECKS

Every review of an Indian app must include these checks for this module:

### India Behavioral Persona Detection
- [ ] Does the app detect Task Finisher behavior (goal-oriented, wants to complete specific task)?
- [ ] Does the app detect Explorer behavior (browsing, discovering, no specific goal)?
- [ ] Does the app detect Structured Learner behavior (wants curriculum, sequence, progression)?
- [ ] Does the app adapt UX based on detected persona (different homepage, different content order)?
- [ ] Impact if missing: India's three dominant behavioral personas (Task Finisher, Explorer, Structured Learner) have fundamentally different needs. A one-size-fits-all UX underserves all three.

**Finding template:** "App presents identical experience to all users regardless of behavioral intent. No detection of whether user wants to complete a specific task, browse content, or follow a structured path. All three persona types get the same homepage and navigation."

**India Benchmark:** Unacademy detects exam-specific personas (UPSC = long-term prep, JEE = intensive 6-month, Banking = 3-month cycles) and adapts content cadence, pricing, and engagement. PhysicsWallah's Prep Meter adapts recommendations based on individual learning persona.

### Tier-Based Persona Differences
- [ ] Does the app account for Tier 1 vs Tier 2-3 versions of the same persona?
- [ ] Is content complexity adjusted by tier? (Tier 1 Explorer ≠ Tier 2 Explorer)
- [ ] Are engagement mechanics tier-appropriate? (Gamification works stronger in Tier 2-3)
- [ ] Is pricing persona-aware by tier?
- [ ] Impact if missing: A Tier 1 Explorer and Tier 2 Explorer have different content preferences, language needs, and price sensitivity. Treating them as one persona misses both.

**Finding template:** "App treats all Explorers identically regardless of tier. Tier 2-3 Explorers see the same English-first, premium-priced content as Tier 1 Explorers. No tier-based persona differentiation."

**India Benchmark:** Flipkart personalizes by tier: Tier 1 sees premium products, Tier 2-3 sees value deals and EMI options. Meesho's entire product is designed for the Tier 2-3 Explorer persona — browse-first, visual-first, Hindi-first.

### Age-Based India Behavioral Patterns
- [ ] Does the app detect Gen Z (15-24) social-first, FOMO-driven behavior?
- [ ] Does the app serve Young Millennial (25-32) career-focused, upskilling needs?
- [ ] Does the app accommodate Gen X (41-55) trust-dependent, simple-UI preferences?
- [ ] Is the UX appropriate for the primary age demographic?
- [ ] Impact if missing: Indian age segments have distinct digital behavior patterns. Gen Z expects Reels-style UX; Gen X expects simple, trust-signaling interfaces. Wrong-age UX feels alienating.

**Finding template:** "App targets 18-35 demographic but presents identical UX to all ages. No Gen Z-specific social features, no career-focused framing for Young Millennials, no simplified mode for older users."

**India Benchmark:** Dream11 targets Gen Z with social leagues, contest-first onboarding, and social proof CTAs. PhysicsWallah targets students (15-22) with exam-specific, community-driven features. Naukri serves Young Millennials with career-ROI framing.

### Scoring Modifiers (India)
- +1 if Task Finisher/Explorer/Structured Learner detection is implemented
- +1 if tier-based persona differentiation exists
- +1 if age-appropriate UX variation is available
- -1 if identical experience regardless of behavioral intent
- -1 if no tier awareness in persona targeting
- -1 if age-inappropriate UX for primary demographic

---

## OUTPUT FORMAT

```markdown
# PERSONA-INTENT ALIGNMENT — [X]/10

## Evidence Summary

### Persona Identification
- **Personas app targets**: [Number estimated]
- **Detection method**: [Questions / Behavioral / Explicit / None]
- **Questions ask about**: [JTBD / Experience / Use case / Other]
- **Persona labels**: [Explicit / Implicit / None]

### Content Adaptation
- **Varies by persona**: [Significantly / Somewhat / Not at all]
- **Difficulty levels**: [Clear / Implicit / Not available]
- **Features adapted**: [Yes / No]

### UX Adaptation
- **Navigation varies**: [Yes / No]
- **CTAs vary**: [Yes / No]
- **Help segmented**: [Yes / No]

### Success Metrics
- **Vary by persona**: [Yes / No]
- **Progress tracking adapted**: [Yes / No]
- **Milestones vary**: [Yes / No]

### Monetization
- **Varies by persona**: [Yes / No]
- **Free tier segmented**: [Yes / No]

### Communication
- **Tone adapted**: [Yes / No]
- **Language complexity varies**: [Yes / No]

### Overall Alignment
- **Multiple personas clearly served**: [Yes, distinct paths / Somewhat / No, one-size-fits-all]
- **Evidence throughout app**: [Clear / Minimal / Not evident]
- **User feels "made for me"**: [Yes / Neutral / No]

---

## Persona Walkthroughs

### Beginner User
- **Time to first value**: [X] seconds
- **Experience**: [Welcoming and guided / Neutral / Overwhelming]
- **Clarity**: [High / Medium / Low]
- **Score**: [X]/10

### Intermediate User
- **Personalization**: [Remembered preferences / Fresh start]
- **Progression**: [Clear next level / No direction]
- **Score**: [X]/10

### Expert User
- **Efficiency**: [Shortcuts available / Same path as beginner / Forced slow]
- **Respect**: [Advanced features available / All basic / Condescending]
- **Score**: [X]/10

---

[Detailed Evidence, Scoring Breakdown, Key Issues sections follow standard format]

**Review Conducted**: [Date] | **Reviewer**: [Name] | **Duration**: [Mode]
```

---

## Summary

This module evaluates persona-intent alignment—the critical driver of product-market fit. It assesses whether the app serves diverse user types effectively or treats everyone the same. Grounded in JTBD (different jobs for different personas), HEART (persona-specific success metrics), Cagan (value perception varies by persona), and Fogg (MAP differs by persona), this module ensures the app is truly "made for me" rather than "made for someone like me—but not quite."

