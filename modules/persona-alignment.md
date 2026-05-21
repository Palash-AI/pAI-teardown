# Persona-Intent Alignment

> AARRR: All Stages | Frameworks: JTBD, HEART, Cagan, Fogg MAP, Hook | Speed: 20min | Rigor: 60min

<!-- SPEED MODE -->
## QUICK AUDIT
Navigate: 1. Onboarding questions (what does the app ask?) 2. First content screen after onboarding 3. Browse/content screens as beginner 4. Same screens as advanced user (if segmentable) 5. Monetization/paywall 6. Settings/preferences
Check: Does the app ask JTBD questions (not just demographics)? Does content change based on answers? Can an expert skip? Does communication feel "made for me"?
Score anchor: 9-10 = distinct paths per persona, content adapts, onboarding varies by persona, 7-8 = some adaptation visible, 5-6 = quiz exists but content same for all, 3-4 = no segmentation, 1-2 = actively wrong persona assumptions
<!-- END SPEED MODE -->

## SCREENS TO NAVIGATE

### 1. Persona Detection & Onboarding Segmentation
**Observe:**
- Does the app ask questions? JTBD ("What's your goal?") or demographic (age/gender)?
- Do answers visibly change the onboarding path or first content screen?
- Are personas labeled ("You're a Beginner") or implicit?
- Onboarding length: same for all personas or varies by expertise?
- Segment-specific value prop: does app explain why it's for THIS persona?

**Screenshot:** Full onboarding question sequence; first content screen after answering (before/after comparison if testable)

**Framework check:** JTBD + Fogg MAP → Questions must probe the job, not demographics. Different personas need different prompts and ability scaffolding.

---

### 2. Adaptive Content & Feature Visibility
**Observe:**
- Same content for all or filtered by persona / difficulty levels?
- Advanced features hidden from beginners or always shown?
- Progressive disclosure: features revealed as user advances?
- Content recommendations: persona-specific or generic trending?
- Community/social: segmented by persona (beginner forum vs. expert forum)?

**Screenshot:** Content list for beginner path vs. expert path (if testable); difficulty labels on content; any feature-hiding in action

**Framework check:** JTBD + Fogg Ability → Beginners need simpler content; experts need advanced. Showing advanced features to beginners increases friction.

---

### 3. Adaptive UX & Persona-Specific Flows
**Observe:**
- Navigation, CTAs: same for all or vary by persona?
- Skip/fast-path for experts: can they reach core features without the guided flow?
- Tutorials: persona-specific (new users get guided tour; experts skip) or forced on all?
- Help/support: different depth by persona or one-size?
- Settings: beginner-simple vs. expert-full or same for all?

**Screenshot:** Navigation/CTA comparison for different personas if visible; skip option presence; tutorial first screen

**Framework check:** Fogg MAP + Norman (Affordances) → Experts want shortcuts (high ability); beginners want guidance. Advanced features should be discoverable by experts, invisible to beginners.

---

### 4. Success Metrics & Personas
**Observe:**
- Progress tracking: same milestones for all or persona-specific (beginner: finish first lesson; expert: 100% complete)?
- Gamification: streaks/points for casual / in-depth metrics for serious — or same for all?
- Achievement badges: generic ("Started!") or persona-aware ("Expert Certified")?
- Stretch goals: are advanced users challenged with harder content or everything capped?

**Screenshot:** Progress/achievements screen; milestone celebration; performance dashboard

**Framework check:** HEART + Cagan Value Risk → Different personas have different success metrics. A beginner completing their first lesson is as meaningful as an expert finishing an advanced track.

---

### 5. Monetization & Persona
**Observe:**
- Free tier: same for all or different by persona?
- Paywall messaging: same copy for casual and serious users?
- Student/teacher or special pricing: present or flat pricing for all?
- Paywall timing: same moment for all or triggered by persona context?

**Screenshot:** Free tier features; paywall screen with messaging; any special pricing tiers

**Framework check:** Cagan Value Risk + Fogg MAP → Different personas perceive value differently. Expert willing-to-pay ≠ beginner's. Flat pricing serves neither well.

---

### 6. Communication & Persona
**Observe:**
- In-app tone: friendly/celebratory for beginners, efficient/technical for experts — or same?
- Language complexity: jargon avoided for beginners? Technical terms used for experts?
- Push notifications: different guidance for new users vs. power users?
- Help/error text: different complexity by persona?

**Screenshot:** Sample notification or help text; in-app messaging tone; error message

**Framework check:** Fogg Motivation + Norman (Conceptual Model) → Language should match persona's mental model. Beginners: encouraging. Experts: efficient.

---

### 7. Persona-Specific Onboarding Depth
**Observe:**
- Expert skip option: "I know this app" / detect expertise and offer skip / forced for all?
- Beginner path: more extensive with scaffolding and practice?
- Guided tour: present for new users, skippable for returning?
- Time to first value: measurably different between beginner and expert?

**Screenshot:** Skip/fast-path button if present; beginner vs. expert first interaction timing

**Framework check:** Fogg Ability + JTBD + HEART Adoption → Different personas activate differently. Forcing experts through beginner onboarding is friction that drives churn.

---

## SCORING RUBRIC

| Score | Label | Key Criteria |
|-------|-------|-------------|
| 9-10 | Best-in-class | JTBD questions in onboarding, 3+ distinct persona paths, content/UX/onboarding/comms all adapt, expert skip available, monetization persona-aware, user can update persona |
| 7-8 | Good | Personas identified, some content adaptation, beginner/expert flows noticeably different, some UX variation, partially adapted tone |
| 5-6 | Adequate | Quiz exists but content mostly same, maybe skip option, some difficulty levels, same pricing/comms for all |
| 3-4 | Poor | No questions asked, one-size-fits-all flow and content, no skip, generic pricing and comms |
| 1-2 | Critical | Wrong persona assumption forced on all (e.g., assumes beginner, alienates experts); some users cannot accomplish their job at all |

**Scoring method:** Start at 5. Add: +1 JTBD questions in onboarding, +1 content adapts to persona, +1 expert skip or fast-path available, +1 difficulty levels clearly differentiated, +1 success metrics vary by persona, +1 monetization persona-aware, +1 user can change persona later. Deduct: -2 no questions/segmentation, -1 quiz asked but ignored (content same), -1 no skip for experts, -1 completely generic comms. Cap at 1-10.

---

## EVIDENCE CHECKLIST

### Persona Detection
- [ ] Personas app targets: [Estimated count: _____]
- [ ] Detection method: [JTBD questions / Behavioral / Explicit / None]
- [ ] Questions ask about: [Goal / Experience / Use case / Demographics / Nothing]
- [ ] Persona labels: [Explicit ("Beginner") / Implicit / None]
- [ ] User can change persona later: [Yes / No]

**Framework:** JTBD, Fogg (MAP)

### Content Adaptation
- [ ] Content varies by persona: [Significantly / Somewhat / Not at all]
- [ ] Difficulty levels visible: [Clear / Implicit / Absent]
- [ ] Features hidden for beginners: [Yes / No]
- [ ] Recommendations personalized: [By persona / Generic trending]
- [ ] Community segmented: [Yes / No / N/A]

**Framework:** JTBD, Fogg (Ability)

### UX Adaptation
- [ ] Navigation varies by persona: [Yes / No]
- [ ] CTAs vary: [Yes / No]
- [ ] Expert skip/fast-path: [Yes / No]
- [ ] Tutorial persona-specific: [Yes / Forced on all / Absent]
- [ ] Settings complexity varies: [Yes / Same for all]

**Framework:** Fogg (MAP), Norman (Affordances)

### Success Metrics
- [ ] Progress tracking adapted: [Yes / No]
- [ ] Milestones persona-specific: [Yes / No]
- [ ] Gamification adapted: [Yes / No]
- [ ] Achievements persona-aware: [Yes / Generic / None]

**Framework:** HEART (all 5), Cagan (Value Risk)

### Monetization
- [ ] Free tier varies by persona: [Yes / No]
- [ ] Paywall messaging varies: [Yes / No]
- [ ] Special pricing available (student, teacher): [Yes / No]
- [ ] Paywall timing varies: [Yes / Same moment for all]

**Framework:** Fogg (MAP), Cagan (Value Risk), AARRR (Revenue)

### Communication
- [ ] Messaging tone varies: [Yes / No]
- [ ] Language complexity adapts: [Yes / No]
- [ ] Notifications segmented: [Yes / No]
- [ ] Learning resources vary: [By complexity / Same for all]

**Framework:** Fogg (Motivation), JTBD

### Onboarding Depth
- [ ] Expert skip available: [Yes / No]
- [ ] Beginner path extended: [Yes / Same length]
- [ ] Guided tour: [Persona-specific / Forced on all / Absent]
- [ ] Time to first value varies: [Beginner: ___s / Expert: ___s]

**Framework:** Fogg (Ability), JTBD (Activation)

### Overall Alignment
- [ ] Multiple distinct persona paths: [Clearly / Somewhat / No]
- [ ] Evidence throughout app: [Clear / Only onboarding / Not evident]
- [ ] User feels "made for me": [Likely / Neutral / Unlikely]

---

## KEY ISSUE PATTERNS

1. **One-Size-Fits-All — No Segmentation** → Detect: No onboarding questions; all users see identical content and flows. Framework: JTBD, Cagan Value Risk, Fogg MAP. Fix: Add 3-5 JTBD questions in onboarding; use answers to filter content and adapt first-value path per persona.

2. **Quiz Asked — Content Ignored** → Detect: App asks personalization questions but shows same content regardless of answers. Framework: JTBD, Fogg Motivation. Fix: Make adaptation visible and immediate ("Now showing Intermediate content"); A/B test adapted vs. generic to prove engagement lift.

3. **Expert Forced Through Beginner Onboarding** → Detect: No skip option; expert user spends 10+ minutes on beginner flow before reaching core value. Framework: Nielsen #3, Fogg Ability. Fix: Add "I know this app" skip; detect expertise from quiz answers and offer fast-path.

4. **Content is One Difficulty Level** → Detect: Beginner feels overwhelmed; expert feels bored; no beginner/intermediate/advanced labeling. Framework: Fogg Ability, JTBD, Hook. Fix: Create 2-3 difficulty tiers; label clearly; suggest next level on completion.

5. **Generic Monetization** → Detect: Same free tier, same paywall copy, same timing for beginner and expert. Framework: Cagan Value Risk, Fogg MAP, AARRR. Fix: Experts convert faster — shorten trial; beginners need proof of value first — show value before paywall.

---

## OUTPUT FORMAT

```markdown
# PERSONA-INTENT ALIGNMENT — [X]/10

## Evidence Summary

### Persona Detection
- **Detection method**: [JTBD questions / Behavioral / None]
- **Questions ask about**: [Goal / Experience / Demographics]
- **Persona labels**: [Explicit / Implicit / None]

### Content Adaptation
- **Varies by persona**: [Significantly / Somewhat / Not at all]
- **Difficulty levels**: [Clear / Implicit / Absent]
- **Features adapted**: [Yes / No]

### UX Adaptation
- **Expert skip/fast-path**: [Yes / No]
- **Tutorial**: [Persona-specific / Forced / Absent]

### Success Metrics
- **Vary by persona**: [Yes / No]
- **Milestones differ**: [Yes / No]

### Overall Alignment
- **Multiple distinct paths**: [Yes / Somewhat / No]
- **User feels "made for me"**: [Likely / Neutral / Unlikely]

## Persona Walkthroughs

### Beginner
- **Time to first value**: [X]s | **Experience**: [Welcoming / Neutral / Overwhelming]
- **Score**: [X]/10

### Expert
- **Skip available**: [Yes / No] | **Shortcuts present**: [Yes / No]
- **Score**: [X]/10

## Scoring Breakdown

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Persona detection | [X]/10 | [Questions asked; JTBD or demographic] |
| Content adaptation | [X]/10 | [Same or different; difficulty levels] |
| UX adaptation | [X]/10 | [Skip; tutorial; shortcuts] |
| Success metrics | [X]/10 | [Same or persona-specific] |
| Monetization | [X]/10 | [Persona-aware or flat] |
| Communication | [X]/10 | [Tone/language varies or not] |
| Onboarding depth | [X]/10 | [Varies or same length] |

**Total Score: [X]/10** | **Justification**: [1-2 sentences]

## Key Issues

### Issue #1: [Title]
**Problem**: [Observed] | **Framework**: [Name] | **Impact**: [User %] | **Hypothesis**: [1-line fix]

## Recommendations

### P0 (Critical)
[Segmentation or content adaptation blockers]

### P1 (High)
[Expert fast-path; difficulty levels; monetization]

**Review Conducted**: [Date] | **Duration**: [Speed / Rigor]
```
