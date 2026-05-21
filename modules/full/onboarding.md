# Onboarding & First Value Experience Module

## MODULE OVERVIEW

### What This Module Reviews
This module evaluates the first-run experience (FRX) and onboarding journey of a mobile application. It assesses how quickly and intuitively users can reach their first meaningful value moment—the moment where the app demonstrates its core promise and delivers on the "why" the user installed it.

**Scope**: From app icon tap → first core interaction with the app's primary feature.

### AARRR Stage Mapping
**Activation** — The stage where users convert from interested downloaders to engaged users. This module directly impacts:
- Feature discovery and understanding
- Motivation to return
- Initial habit formation
- Paywall effectiveness (if applicable)

### Design Skill Integration (Mandatory for Screenshots)

> **`design:critique`** — Run on every onboarding screen screenshot. Evaluate: first impression (does the app look trustworthy at first glance?), usability (can user complete onboarding without confusion?), visual hierarchy (is the primary CTA obvious?), consistency (do screens feel like one flow?), accessibility (touch targets on OTP input, button sizes, contrast). For India context: does onboarding look and feel professional on a budget Android? Is the flow completable in ≤3 screens?

> **`design:ux-copy`** — Run on all onboarding copy. Evaluate: CTA labels ("Abhi shuru karo" vs "Submit"), value proposition clarity (specific outcome > vague promise), error messages (OTP failed? Tell user what to do next), social proof ("Ravi from Jaipur learned English in 30 days" > "1M users worldwide"). For India context: is copy in Hindi/Hinglish for Tier 2-3? Is "cancel anytime" visible and trustworthy? Does ₹1 trial copy explain what happens after trial ends?

### Primary Frameworks & Models

| Framework | Application |
|-----------|-------------|
| **Fogg Behavioral Model (B=MAP)** | Analyzing Motivation, Ability, and Prompt timing in each onboarding step |
| **HEART Adoption Metric** | Measuring happiness/engagement and retention signals during FRX |
| **AARRR Activation** | Defining what constitutes "activation" for this product category |
| **Duolingo Benchmark** | <60 seconds to first value moment (education apps especially) |
| **Jobs to Be Done (JTBD)** | Understanding the functional/emotional/social jobs the user hired the app to do |
| **Hook Model (Nir Eyal)** | Trigger → Action → Variable Reward → Investment cycle during onboarding |
| **Nielsen's 10 Usability Heuristics** | System visibility, user control, error prevention, and help |
| **Don Norman's Design of Everyday Things** | Signifiers, affordances, feedback, and constraints in UI/UX |
| **Kano Model** | Basic needs vs. satisfiers vs. delighters in onboarding |

---

## SCREENS TO NAVIGATE

### 1. App Store Listing / First Impression
**Purpose**: Understand pre-download expectations and positioning.

**What to Observe**:
- App icon design and memorability
- Headline/tagline clarity (does it immediately answer "what is this for?")
- Key screenshots and their order (do they show the core feature first?)
- Ratings and review sentiment (signal of successful or failed activation downstream)
- Call-to-action button ("Get", "Open", "Install")
- Category classification and competition

**What to Screenshot**:
- Full app listing (icon, name, tagline, key visual)
- First 2-3 key screenshots from listing
- Overall rating and number of reviews
- Top positive and negative review quotes (especially related to onboarding)

**What to Document**:
- App positioning in one sentence
- User jobs implied by marketing copy
- Any onboarding-related promises ("Learn in 5 minutes", "Set up in 30 seconds", etc.)
- Competitive context (what do competitors show for same job?)

---

### 2. Splash Screen / Loading
**Purpose**: Assess first visual experience and brand impression.

**What to Observe**:
- Load time (how long until interactive?)
- Branding consistency (does logo/color scheme match app store listing?)
- Loading state clarity (is progress indicated? Any skeleton screens?)
- Whether any copy appears ("Loading...", brand tagline, motivational message)
- Animation quality (does it feel premium or generic?)

**India-Specific Observations:**
- Test splash/load time on a budget device (Redmi 10A, Realme C55, Samsung Galaxy M04 — ₹7-12K phones). Does it load in <3 seconds on 4G?
- Do animations stutter on budget chipsets (<4GB RAM, Helio G35/Snapdragon 4-series)?
- Is there a skeleton loader or does the user see a blank/frozen screen on slow connections?

**What to Screenshot**:
- Splash screen as it appears
- Any animated loading states
- Timeline of load sequence

**What to Document**:
- Total time from app tap to splash screen appearance
- Total time from splash to first interactive screen
- Brand impression (0-5 scale: does it feel professional?)
- User confidence at this stage (do they understand they've opened the right app?)

---

### 3. Login / Signup Flow
**Purpose**: Understand authentication friction and data collection strategy.

**What to Observe** (for each step):
- **Welcome Screen**: Does it explain why login is required? Any guest/skip option?
- **Email/Phone Entry**: Single field or multi-step? Error handling clarity?
- **Password Entry**: Requirements shown upfront? Password strength indicator?
- **OTP/Verification**: Does it explain timing? Can user easily request resend?
- **Password Reset**: Recovery path clear if user forgets credentials?
- **Profile Completion**: How many fields mandatory vs. optional? Field by field or all at once?
- **Account Verification Email**: Does user need to check email before proceeding? Timeline?

**India-Specific Observations:**
- Is Truecaller auto-fill supported for phone number entry (one-tap verification)?
- Does OTP auto-read work on Android (SMS permission → auto-fill without switching apps)?
- Is WhatsApp login available as an auth option?
- Is Google One-Tap sign-in available (dominant on Indian Android devices)?
- Does the app handle Indian phone numbers (+91, 10-digit) correctly?
- Is there a language selection step during onboarding (Hindi/Hinglish/English)?

**What to Screenshot**:
- First auth screen (with messaging visible)
- Each step of the flow
- Any error states (wrong password, email not found, etc.)
- Success confirmation screen

**What to Document**:
- Total number of screens in auth flow
- Total time to complete authentication
- Whether user sees any value BEFORE or ONLY AFTER authentication
- Data requested at each step (and explained why?)
- Fallback options (guest mode, skip, social auth, biometric?)
- Clarity of instructions (Nielsen #5: Error recovery clarity)

**Framework Checkpoints**:
- **Fogg MAP**: Is ability to complete auth high (clear instructions, simple form)? Is motivation explained (why login required)?
- **JTBD**: Does the app explain why it needs this data before asking?

---

### 4. Permission Requests
**Purpose**: Assess permission friction and contextual timing.

**What to Observe** (for each permission):
- **Trigger**: When does the permission request appear? (On app open? On feature access?)
- **Messaging**: Does it explain WHY the app needs this permission and WHAT VALUE the user gets?
- **Denial Handling**: What happens if user taps "Don't Allow"? Can they continue? Can they re-request?
- **Number & Sequence**: How many permissions total? In what order? (Camera before contacts? Notifications before location?)

**Typical Permissions to Check**:
- Notifications (most intrusive, usually comes last)
- Location (sensitive, needs context)
- Camera/Photos (feature-gated, should come when feature accessed)
- Contacts (very sensitive, rarely needed)
- Microphone (feature-gated)
- Calendar (feature-gated)
- Health data (very sensitive, needs strong value prop)

**What to Screenshot**:
- Each permission request dialog as presented
- Any pre-permission education screens (e.g., "We use location to find nearby stores")
- Error or "blocked" states if user denies

**What to Document**:
- Sequence of permission requests (which comes first/last?)
- Time elapsed before FIRST permission request (in seconds from app open)
- User choice on each (Allow/Don't Allow/Maybe Later)
- How app responds to denials (graceful degradation or blocking?)
- Total "permission tax" (cumulative friction of all requests)

**Framework Checkpoints**:
- **Fogg MAP**: Permission requests reduce Ability (friction) and Motivation (interruption). Are they contextualized?
- **Nielsen #3**: User control and freedom — can user dismiss, deny, or defer permissions?
- **Hook Model**: Permissions are interrupts that disrupt the reward cycle.

---

### 5. Onboarding Quiz / Interest Selection
**Purpose**: Assess personalization and contextual value demonstration.

**What to Observe** (if present):
- **Timing**: Before or after showing core feature?
- **Length**: How many questions? (Industry sweet spot: 3-7 questions)
- **Relevance**: Do questions probe JTBD and use cases? Or generic demographic data?
- **Visualization**: Are options presented as buttons, dropdowns, card selects?
- **Progress Indicator**: Does user see how many questions remain?
- **Personalization Impact**: Are results shown immediately? Does the app change based on answers?

**Sample Strong Questions** (JTBD-grounded):
- "What's your primary goal with [feature]?" (Functional job)
- "How much time can you dedicate daily?" (Job constraint)
- "What's your experience level?" (Ability segmentation)
- "What matters most: Speed, depth, or simplicity?" (Value preference)

**Sample Weak Questions** (generic demographic):
- "What's your age?"
- "What's your gender?"
- "Where do you live?"
(Unless directly tied to personalized content — e.g., location-based services)

**What to Screenshot**:
- Quiz intro screen (if any)
- 2-3 representative question screens
- Results screen / confirmation of selections
- First content screen after quiz (to see personalization effect)

**What to Document**:
- Number and type of questions asked
- Whether questions are onboarding-specific or preference-based
- How directly answers map to user segmentation (can you see the personalization?)
- Time spent in quiz flow
- Whether quiz result is acknowledged ("Great! We found X for you")

**Framework Checkpoints**:
- **JTBD**: Questions should probe the job, not demographics. Is the quiz actually discovering intent?
- **Fogg MAP**: Good questions increase perceived value (motivation) and personalization (relevant ability).
- **Kano Model**: Personalization is a satisfier/delighter — absence is noticed negatively.

---

### 6. Paywall / Trial Prompt
**Purpose**: Assess monetization strategy timing and narrative framing.

**What to Observe** (if paywall present):
- **Timing**: Before, during, or after first value moment?
- **Framing**: Positive (what you GET) vs. negative (what you LOSE)?
- **Pricing Clarity**: Single tier or multiple options? Price in local currency? Annual vs. monthly framing?
- **Trial Option**: Free trial offered? Duration clear (7 days, 14 days)?
- **Escape Hatch**: Can user skip/dismiss and use free tier? How prominent is "Continue Free"?
- **Social Proof**: Ratings, subscriber count, money-back guarantee?
- **Value Articulation**: Does paywall message explain what the paid tier unlocks? Or is it assumed?

**Red Flags** (paywall before value):
- Paywall appears before user has interacted with any core feature
- No trial period offered
- No free tier option (except if paid-only business model)
- Dismissal button is hidden or uses dark patterns

**Green Flags** (paywall after value):
- Paywall appears only when accessing premium features
- Free tier shows core value first
- Trial is generous (7+ days for productivity, 30+ for lifestyle)
- Copy emphasizes user's progress ("You've learned X. Unlock premium to continue")

**What to Screenshot**:
- First paywall screen as shown
- Full pricing table (if expandable)
- Trial terms and fine print
- Dismiss/skip button state
- Confirmation screen after choosing tier

**What to Document**:
- Exact moment paywall appears (e.g., "After 2 onboarding questions" or "On app open before login")
- Number of steps before paywall appears
- Whether user can use app meaningfully before paywall
- Price point(s) and billing frequency options
- Trial duration offered
- Free tier capabilities (what can free user do?)

**Framework Checkpoints**:
- **Fogg MAP**: Paywall before value = low motivation + blocked ability = activation failure.
- **AARRR Activation**: Paywall timing is a primary Activation driver. Ideal: show value before asking for money.
- **Kano Model**: Paywall can be a "dissatisfier" if presented too early or without strong value messaging.

---

### 7. First Content Screen
**Purpose**: Assess clarity of core feature and ease of first interaction.

**What to Observe**:
- **Clarity**: Can user immediately identify the core feature? Does the screen have a clear focal point?
- **Signifiers** (Norman): Are CTAs visually distinct? Do buttons look clickable?
- **Empty State vs. Populated**: Does the screen show sample content or is it blank? (Blank = higher friction)
- **Guidance**: Is there instructional copy, tooltips, or walkthroughs?
- **Navigation**: Can user easily understand how to navigate the app? Is the bottom tab bar or side menu clear?
- **Progressive Disclosure**: Is the screen simple (single action) or crowded (many options)?

**What to Screenshot**:
- Full screen view
- Any tooltips or in-app guidance as revealed
- Navigation options (if bottom tab bar or side menu visible)
- Any empty state or placeholder content

**What to Document**:
- Cognitive load (1-5 scale: how many options are available?)
- Clarity of primary CTA (can user identify the next action?)
- Whether content is pre-populated (sample/default) or requires user input
- On-screen guidance or help available
- Time from app open to reaching this screen

**Framework Checkpoints**:
- **Nielsen #1**: System visibility — does this screen make the system status (what the app does) immediately clear?
- **Norman's Affordances**: Do interactive elements signal their function?
- **Fogg MAP**: Is this screen high-ability (simple, guided) and high-motivation (shows clear value)?

---

### 8. First Interaction with Core Feature
**Purpose**: Assess the "moment of truth" — does the app deliver on its promise immediately?

**What to Observe**:
- **Interaction Ease**: How many taps/inputs required to perform a meaningful action?
- **Feedback**: Does the app respond instantly and clearly to the user's action?
- **Outcome**: Is the result what the user expected? Does it deliver the promised job-to-be-done?
- **Delight**: Is there any delightful surprise? Animation, progress visualization, celebration?
- **Friction Points**: Does the app request additional data, permissions, or sign-ups before showing the result?

**Scoring the First Interaction** (Duolingo benchmark for education):
- **Best-in-Class**: User completes meaningful first action in <30 seconds from app open, gets immediate feedback, sees clear value.
- **Good**: Action completes in 1-2 minutes, feedback is clear, value is evident.
- **Okay**: Action completes in 2-5 minutes, feedback is present but might be unclear.
- **Poor**: Action takes >5 minutes, requires excessive data entry, or value is not immediately clear.

**What to Screenshot**:
- Screen state BEFORE user taps primary CTA
- Screen state IMMEDIATELY AFTER user completes first action (before any navigation)
- Any celebration/success screen (if present)
- First result or outcome of the action

**What to Document**:
- **Time to value** (in seconds): From app open to first meaningful result
- **Steps to value** (in action count): How many taps/inputs did user perform?
- **Feedback quality** (1-5 scale): Was feedback immediate and clear?
- **Value clarity** (1-5 scale): Does user understand they've experienced the core promise?
- **Subsequent prompts**: After the first action, does the app ask for payment, rate on app store, or enable next feature?

**Framework Checkpoints**:
- **Fogg MAP**: This is the critical moment where Ability meets Motivation. High scores on both = activation.
- **Hook Model**: Action → Variable Reward. Is the reward clear? Is it variable (not always the same)?
- **HEART Adoption**: Engagement during this moment is a key adoption signal.
- **Duolingo Benchmark**: Education apps should hit value in <60 seconds.

---

## SCORING RUBRIC (1-10)

Each score should reference specific framework principles and include evidence from the screens above.

### 9-10: Best-in-Class (Duolingo/Slack Level)

**Criteria**:
- Time to first value: **<60 seconds** (Duolingo benchmark)
- Paywall: **After demonstrating core value**, not before
- Personalization: **Proactive** (questions asked) **and visible** (results immediately change the experience)
- Permissions: **Contextualized** (requested when feature is accessed, with clear explanation)
- First interaction: **Immediate feedback**, clear success state, celebratory tone
- Onboarding steps: **Minimal** (<5 screens) but comprehensive (covers what user needs to know)
- Error handling: **Graceful** (users can recover from mistakes without frustration)
- Friction signals: **None evident** (no dark patterns, no forced interrupts, no data theft)

**Framework Alignment**:
- **Fogg MAP**: Ability is maximized (simple, guided path) and Motivation is sustained (value shown early and often)
- **HEART Adoption**: Users show strong engagement signals (they complete first meaningful action)
- **Nielsen #1 & #5**: System status is always clear; users understand what happened after each action
- **JTBD**: App has clearly identified the user's job and designed onboarding to serve it
- **Kano Model**: Basic needs are met (clarity, simplicity) and satisfiers present (personalization, polish)

**Examples**: Duolingo, Slack, Superhuman, Telegram, Tik Tok (for scroll engagement)

---

### 7-8: Good / Well-Designed

**Criteria**:
- Time to first value: **60-120 seconds**
- Paywall: **After first value is shown**, or free tier is genuinely useful
- Personalization: **Present** (at least interest or experience level probing)
- Permissions: **Mostly contextualized**, max 2 requests before first value
- First interaction: **Clear feedback**, success state evident
- Onboarding steps: **5-8 screens**, well-organized
- Error handling: **Present** (users can correct mistakes)
- Friction signals: **Minimal** (maybe 1 minor dark pattern or unnecessary permission)

**Framework Alignment**:
- **Fogg MAP**: Strong Ability and Motivation through most of journey; one possible dip
- **Hook Model**: Clear trigger→action→reward cycle established during first interaction
- **Nielsen #1**: System status visible; users can always answer "what do I do next?"

**Examples**: Notion, Calm, Stripe, Many lifestyle apps in top 50

---

### 5-6: Adequate / Decent Flow but Missing Key Elements

**Criteria**:
- Time to first value: **120-300 seconds** (3-5 minutes)
- Paywall: **Present but not blocking everything**; free tier has some value
- Personalization: **Minimal or generic** (demographics, not JTBD)
- Permissions: **Multiple requests early on**, but mostly deferrable
- First interaction: **Feedback present but might be unclear**
- Onboarding steps: **8-12 screens**, some feel redundant
- Error handling: **Basic** (error messages present, but may not suggest recovery)
- Friction signals: **2-3 present** (e.g., one permission before value, rating prompt too early, generic onboarding questions)

**Framework Alignment**:
- **Fogg MAP**: Ability is okay (some friction); Motivation is unclear (value not strongly articulated)
- **Nielsen #10**: Help & documentation may be needed but not provided
- **JTBD**: Job is identified but onboarding doesn't clearly show how app serves it

**Examples**: Average productivity apps, many finance/investing apps, some education apps

---

### 3-4: Poor / Some Value Shown but Slow or Generic

**Criteria**:
- Time to first value: **5-15 minutes**
- Paywall: **Appears early** or blocks free functionality that should be free
- Personalization: **Absent or completely generic** (no questions asked, or only demographic)
- Permissions: **Aggressive request sequence** (all permissions asked upfront)
- First interaction: **Feedback unclear or delayed**, user unsure if they succeeded
- Onboarding steps: **12-20+ screens**, feels like busy work
- Error handling: **Weak** (error messages are unhelpful or blame user)
- Friction signals: **4+ present** (paywall, rating prompt, multiple permissions, unclear navigation, generic onboarding)

**Framework Alignment**:
- **Fogg MAP**: Ability is low (complex onboarding, multiple steps) and Motivation is decreasing (value delayed too long)
- **Hook Model**: Reward cycle is not established; users may abandon before completing onboarding
- **Nielsen #3**: User control is limited (many required steps, hard to skip)
- **AARRR Activation**: Activation rate likely <30% (high abandonment during onboarding)

**Examples**: Legacy banking apps, some healthcare apps, older enterprise tools

---

### 1-2: Severely Flawed / Paywall Before Value, No Personalization, Multiple Interrupts

**Criteria**:
- Time to first value: **>15 minutes or unreachable without payment**
- Paywall: **Appears immediately or before any feature demonstration**
- Personalization: **None**; app treats all users identically
- Permissions: **All requested upfront**, some suspicious (why does a note app need location?)
- First interaction: **Feedback absent**, user unsure what happened
- Onboarding steps: **20+ screens** or users can't skip any
- Error handling: **Absent** (app crashes or shows generic errors)
- Friction signals: **6+ present** (paywall, aggressive permissions, rating prompts, confusing navigation, broken flows, forced tutorial, pop-up ads during onboarding)

**Framework Alignment**:
- **Fogg MAP**: Ability is very low (friction everywhere) and Motivation is zero (no value shown before asking for money/data)
- **AARRR Activation**: Activation rate likely <5%; this onboarding drives users away
- **Nielsen #3**: User control is almost nonexistent
- **Kano Model**: This onboarding is a strong dissatisfier

**Examples**: Ad-heavy free games, some spammy productivity apps, very old apps that haven't been updated

---

### Scoring Methodology

**Award points for**:
- Time to value <60 sec: +2 points
- Personalization present and visible: +1 point
- Paywall after, not before: +1 point
- <2 permission requests before value: +1 point
- Clear success feedback on first action: +1 point
- <5 onboarding screens: +1 point
- Zero dark patterns: +1 point
- Graceful error handling: +1 point

**Deduct points for**:
- Time to value >5 min: -2 points
- Paywall before value: -3 points
- No personalization: -1 point
- All permissions requested upfront: -1 point
- Unclear or delayed feedback: -1 point
- Rating prompt before meaningful interaction: -1 point
- Suspicious permission requests: -2 points

**Final Score**: Start at 5 (baseline) and add/subtract points. Cap at 1-10 scale.

---

## EVIDENCE CHECKLIST

Document these specific data points during your review. Each piece of evidence should be tied to a framework principle and supported by screenshot/screen recording.

### Timing Metrics

- [ ] **Time from app tap to splash screen visibility** (seconds)
- [ ] **Time from splash to first interactive screen** (seconds)
- [ ] **Time from app open to authentication prompt** (if applicable)
- [ ] **Time from auth completion to first content screen** (seconds)
- [ ] **Time from first content screen to first core interaction** (seconds)
- [ ] **TOTAL time from app open to first value moment** (seconds) — **KEY METRIC**
- [ ] **Time spent in onboarding quiz** (if present)
- [ ] **Time between permission requests** (if multiple)

### Interaction Counts

- [ ] **Number of screens seen before first core interaction**
- [ ] **Number of taps/inputs required to reach first value moment**
- [ ] **Number of permission request dialogs shown**
- [ ] **Number of interrupts before first value** (rating prompts, subscription pushes, etc.)

### Permission Audit

- [ ] **List of all permissions requested, in order**: [Notifications, Location, Camera, ...] Frameworks: Fogg MAP, Nielsen #3
- [ ] **Time elapsed before first permission request** (seconds after app open)
- [ ] **For each permission: user choice** (Allow / Don't Allow / Maybe Later)
- [ ] **For each permission: context provided?** (Yes / No / Minimal)
- [ ] **Cumulative permission friction score** (1-5 scale)

**Evidence**: Screenshot of each permission request dialog with timestamp

---

### Personalization Audit

- [ ] **Personalization type**: None / Demographic / JTBD-based / Behavioral
- [ ] **If personalization present: number of questions asked**
- [ ] **Sample questions** (directly paraphrase questions shown): Framework: JTBD
- [ ] **Personalization visible on first content screen?** (Does the content change based on answers?) (Yes / No / Partially)
- [ ] **How explicitly is personalization acknowledged?** (e.g., "We found X for you" or hidden change?)
- [ ] **Personalization impact score** (1-5: how much does the app actually change?): Framework: Kano Model

**Evidence**: Screenshots of quiz (if present) and before/after first content screen

---

### Paywall Audit (if applicable)

- [ ] **Paywall present?** Yes / No
- [ ] **Timing of first paywall**: At app open / After login / After onboarding / On first premium feature access / After X minutes of free use
- [ ] **Paywall positioning relative to first value moment**: Before / During / After / Never
- [ ] **Free tier available?** Yes / No
- [ ] **If free tier: is it actually usable?** (Can free user accomplish meaningful action?) Yes / No / Partially
- [ ] **Trial offered?** Yes / No. If yes, duration: _____ days
- [ ] **Pricing tiers shown**: Number of options: _____ / Clarity (1-5): _____ / Price in local currency: Yes / No
- [ ] **Paywall messaging tone**: Value-focused (emphasis on benefits) / Loss-averse (emphasis on what you'll lose) / Neutral
- [ ] **Escape hatch visible?** (Can user dismiss/skip?) Yes / Easily / Obscurely / No

**Evidence**: Full screenshot of paywall, pricing detail, and dismiss option if present. Framework: Fogg MAP, AARRR Activation, Kano Model

---

### Authentication Audit (if login/signup required)

- [ ] **Authentication method(s) offered**: Email / Phone / Social (which?) / Biometric / Guest
- [ ] **Number of steps to complete auth**: _____
- [ ] **Time to complete auth**: _____ seconds
- [ ] **Data requested at each step** (e.g., email, password, full name, DOB, etc.): Framework: JTBD, Nielsen #1
- [ ] **Is the reason for each data request explained?** Yes / No / Some fields
- [ ] **Can user see any value before completing auth?** Yes / No / Limited preview
- [ ] **Account recovery (forgot password) path clear?** Yes / No / Not tested
- [ ] **Errors encountered & recovery**: None / (describe)

**Evidence**: Sequence of auth screens, each with timestamp. Framework: Fogg MAP (Ability: form complexity), JTBD (why each data field?)

---

### First Interaction / Value Moment

- [ ] **What is the core feature interaction?** (e.g., "Create first note", "Swipe through first card", "Input first search", "Take first photo")
- [ ] **Steps to initiate core feature interaction**:
  - [ ] Step 1: _____
  - [ ] Step 2: _____
  - [ ] Step 3: _____
- [ ] **Feedback on interaction completion**: None / Delayed / Immediate + clear / Immediate + celebratory
- [ ] **Success state** (does user see they succeeded?): Obvious / Somewhat clear / Unclear / App crashed or errored
- [ ] **Subsequent interrupts after first interaction**: None / Rating prompt / Share prompt / Payment push / Help prompt
- [ ] **Feeling after first interaction** (subjective): Excited / Satisfied / Neutral / Confused / Frustrated

**Evidence**: Screenshot before and after first core interaction. Best-in-class: celebratory feedback or progress indicator. Frameworks: Fogg MAP (Ability/Motivation), Hook Model (Reward), HEART (Adoption signals)

---

### Navigation & Wayfinding

- [ ] **Primary navigation pattern**: Bottom tab bar / Side drawer / Top tab bar / Segmented control / Other: _____
- [ ] **Is primary navigation visible from first content screen?** Yes / No / Hidden until scroll
- [ ] **Can user easily identify how to access**: Core feature / Settings / Help / Profile
- [ ] **Clarity of labels** (are buttons/tabs self-explanatory?): 1-5 scale: _____
- [ ] **Number of navigation options visible at once** (cognitive load): _____

**Evidence**: Screenshot of full first content screen with navigation visible. Frameworks: Nielsen #1 (Visibility of system status), Norman (Affordances and signifiers)

---

### Interrupts & Dark Patterns

- [ ] **Rating/review prompt appears**: Before first interaction / After first interaction / After X interactions / Never
- [ ] **If rating prompt: timing appropriateness** (1-5 scale, 5=perfect timing): _____
- [ ] **Share/referral prompt appears when**: Never / Before value / After first interaction / After X interactions
- [ ] **Push notification consent timing**: Never / Upfront / After value / (when?)
- [ ] **Dark patterns detected**: None / Unclear dismiss buttons / Pre-checked boxes / Misleading language / Other: _____
- [ ] **Ads appear during onboarding**: Yes / No. If yes, when and frequency: _____
- [ ] **Forced tutorials**: None / Skippable / Not skippable

**Evidence**: Screenshots of any interrupts, with focus on timing and UX treatment. Frameworks: Nielsen #3 (User control), Kano Model (Dissatisfiers)

---

### Overall Activation Signals

- [ ] **Likelihood user completes onboarding**: <20% / 20-50% / 50-80% / >80% (estimation based on friction)
- [ ] **Likelihood user returns after first session**: <20% / 20-50% / 50-80% / >80% (estimation)
- [ ] **Blockers to activation identified**: [List 1-3 key friction points]
- [ ] **Delighters present**: None / Minor / Notable (provide examples)
- [ ] **Overall impression**: Likely abandon / Might use again / Will definitely return

**Evidence**: Synthesis of all evidence above. Frameworks: AARRR Activation, HEART Adoption

---

## KEY ISSUES TEMPLATE

Document the most critical issues found during your review. Each issue should:
1. **State the problem** (what did you observe?)
2. **Cite the framework principle** (why is this a problem?)
3. **Quantify the impact** (how many users does this affect?)
4. **Suggest a hypothesis for improvement**

### Example Issues

#### Issue #1: Paywall Before Value
**Problem**: A subscription screen requesting payment appears on app open, before the user has interacted with any core feature.

**Framework Cite**:
- Fogg Behavioral Model: When Ability (can I access the feature?) is blocked, and Motivation (why should I trust this?) is uncertain, users don't activate. Paywall before value breaks both.
- AARRR Activation: Showing pricing before demonstrating value is a backwards funnel. Users should experience value first, then be willing to pay to unlock more.

**Evidence**: Screenshot showing paywall at [TIME], which is before [TIME to first interaction].

**Quantified Impact**: If industry standard for "free tier trial before paywall" is 60+ seconds, and this app shows paywall at 5 seconds, we estimate 40-60% of users abandon before seeing value.

**Hypothesis for Improvement**: Move paywall to appear after user completes first meaningful interaction (e.g., after creating first note, taking first photo, etc.). Estimated impact: 20-30% increase in activation rate.

**Comparative Benchmark**: Notion shows paywall only when user tries to add a third database. Slack shows value for 30 days before free tier limits appear.

---

#### Issue #2: No Interest Probing (Generic Onboarding)
**Problem**: App shows a 3-question survey asking age, gender, and location—data unrelated to why the user installed the app.

**Framework Cite**:
- Jobs to Be Done (JTBD): Without understanding the functional, emotional, or social job the user hired this app for, the app cannot personalize its experience. Generic demographic data doesn't help.
- Fogg Behavioral Model: Motivation is not sustained because the app doesn't acknowledge the specific job the user came to do. Result: app feels generic.
- Kano Model: Personalization to the user's actual need is a "satisfier." Absence of it is felt as a missed opportunity.

**Evidence**: Screenshots of onboarding questions showing: [Q1: Age, Q2: Gender, Q3: Location]. User data then not used to change the first content screen (before/after comparison shows identical screens).

**Quantified Impact**: Users who skip this survey report lower perceived relevance. Apps that ask use-case-focused questions (Duolingo: "Why are you learning?") see 25-40% higher engagement.

**Hypothesis for Improvement**: Replace demographic questions with JTBD probes:
- "What's your primary goal with [core feature]?"
- "How much time can you dedicate daily?"
- "What's your experience level?"

Test whether users who answer these questions see higher completion rates. Estimated impact: 15-25% improvement in relevant engagement.

**Comparative Benchmark**: Duolingo asks "Why are you learning?", Calm asks "Why do you want to meditate?", Notion asks "What are you planning?" All see high engagement because the app then delivers experiences matched to the answer.

---

#### Issue #3: Too Many Permission Requests, Too Early
**Problem**: App requests 5 permissions on app open (Notifications, Location, Camera, Contacts, Health data) before user has accessed any feature that uses them.

**Framework Cite**:
- Fogg Behavioral Model: Permission requests are interrupts that reduce Ability (user must decide, not act) and Motivation (interruption breaks momentum). Timing them before value is experienced violates the MAP model.
- Nielsen's 10 Usability Heuristics (#3: User control and freedom): Users should always have the ability to deny, defer, or re-request permissions. Asking all at once with unclear explanations violates user control.
- Hook Model: Permission requests are friction that breaks the Trigger→Action→Reward cycle.

**Evidence**: Screenshots of 5 sequential permission dialogs appearing at [TIMES]. None of the dialogs explain why the app needs the permission or when it will be used.

**Quantified Impact**: Apps that request all permissions upfront see 30-50% of users deny at least one permission, often bluntly (no nuance in which are truly needed). Staggered, contextual permission requests see >80% allow rates.

**Hypothesis for Improvement**:
1. **Defer permissions**: Only request permissions when the feature that uses them is accessed.
2. **Add context**: Before requesting, show a screen explaining "We use location to show nearby [stores/events/people]."
3. **Sequence by sensitivity**: Request less sensitive ones first (notifications), more sensitive ones last (contacts, health data).

Estimated impact: 40-50% reduction in permission denials, higher feature adoption.

**Comparative Benchmark**: iOS Health app requests health permissions only when user accesses a specific data type. Uber requests location only when user books a ride (not on app open). Both see high permission grant rates.

---

#### Issue #4: No Contextual Guidance (Missing Signifiers)
**Problem**: First content screen is blank except for a large "+" button. No label, no help text, no indication of what tapping it does.

**Framework Cite**:
- Donald Norman's "Design of Everyday Things": A signifier is a perceptible indicator of how to use something. This "+" button has no signifier—the user must guess its function.
- Nielsen's 10 Usability Heuristics (#1: Visibility of system status): Users should always know what the system is doing and what's expected next. This blank screen communicates neither.
- Fogg MAP: Lack of clarity (what is the action?) reduces Ability. Users with low ability don't take action.

**Evidence**: Screenshot of first content screen. Text overlay or zoomed-in view of "+" button showing no associated label or help text.

**Quantified Impact**: Apps with unlabeled primary actions see 20-40% lower interaction rates on that action. Apps with tooltips or labels see >80% completion.

**Hypothesis for Improvement**: Add a label below or beside the "+" button ("Create note", "Add photo", etc.). Add a tooltip on first load ("Tap + to create your first note"). If screen is truly blank, add in-app onboarding text ("You have no notes yet. Ready to create your first?").

Estimated impact: 30-50% increase in first-time interaction rate.

**Comparative Benchmark**: Notion shows "Add a page" next to the "+" icon. Slack shows "No messages yet. Send your first message!" Evernote has a labeled note creation button.

---

#### Issue #5: Rating Prompt Too Early / at Wrong Moment
**Problem**: After user creates their first note (completes first meaningful action), the app immediately shows "Love this app? Rate us on the App Store!"

**Framework Cite**:
- Kano Model: Requesting a rating before the user has experienced sufficient value is a "Dissatisfier." The user hasn't yet determined if the app is worth the effort of giving feedback. Asking prematurely feels extractive.
- Hook Model: The Reward moment (user sees their created note) is interrupted by a request to leave the app and go to the App Store. This breaks the variable reward cycle and prevents the user from enjoying their success.
- HEART Adoption: Users who are interrupted before their reward is fully processed show lower retention. Let the moment land before asking for anything.

**Evidence**: Screenshot timeline: [Action] "Create note" → [Reward] "Note appears on screen" → [Interrupt] "Rating prompt" within 3 seconds.

**Quantified Impact**: Apps that ask for ratings within the first 2-5 uses see <5% rating completion and are often rate-bombed. Apps that ask after 20-30 uses or after the user has completed a meaningful workflow see 20-40% rating completion and higher-quality reviews.

**Hypothesis for Improvement**:
1. **Delay the prompt**: Only show after user has completed 3-5 meaningful interactions over multiple sessions.
2. **Trigger on positive signals**: Show after user unlocks a milestone, completes a goal, or rates their satisfaction in-app.
3. **Use elegant timing**: If you must show it early, use a non-blocking in-app banner (not a modal). Let user dismiss it easily.

Estimated impact: Increase rating requests completion rate from <5% to 20-40%. Improve app store rating quality.

**Comparative Benchmark**: Slack shows no rating prompt until 30+ messages sent. Duolingo shows a satisfication check-in ("How was today's lesson?") before considering an app store rating request. Both report high-quality reviews.

---

### Common Issue Patterns by Category

#### Paywall Timing Issues
- Paywall appears before value is shown
- Free tier is so limited it's unusable (missing "basic functionality")
- Trial duration is too short for user to experience value (e.g., 3 days for a social app)
- Pricing is not transparent (hidden fees, unclear billing cycle)

#### Permission Issues
- All permissions requested on app open (before any feature access)
- Permissions lack context (no explanation of why the app needs them)
- Permission denials break the app entirely (no graceful degradation)
- Suspicious permissions for the app category (e.g., file access for a weather app)

#### Personalization Issues
- No onboarding questions asked; app treats all users the same
- Questions asked are demographic, not JTBD-based
- User answers don't visibly change the experience
- Personalization is mentioned but not evident to the user

#### Navigation Issues
- Primary CTA is not obvious (too many equal-weight buttons)
- Help/settings/profile are hard to find
- Labels are jargon-heavy or unclear
- Navigation is hidden until user discovers it

#### Interrupts & Timing Issues
- Rating prompt shows up too early
- Share/referral prompts appear before user has value to share
- Tutorial is forced and not skippable
- Pop-ups appear during critical onboarding moments

#### Clarity & Signifiers
- Primary action button has no label or icon (just ">" or "+")
- Empty state is blank (no guidance on what to do)
- Success of first action is unclear (does the app respond?)
- Error messages are vague ("Something went wrong") with no recovery path

---

## SPEED MODE vs RIGOR MODE INSTRUCTIONS

Choose the right mode based on your time constraints and depth requirements.

### SPEED MODE (15-20 minutes)
**Best for**: Quick competitive analysis, rapid testing, initial viability screening.

**Flow**:
1. **Skip app store listing** (go straight to download)
2. **Navigate login** → Note user/pass options, time to complete
3. **Skip any onboarding quiz** (if present, just scan questions, don't focus on answers)
4. **Navigate first screen** → Identify the core feature
5. **Perform first core interaction** → Time it, screenshot result
6. **Check for paywall** → Is it before or after first value?
7. **Note 3 key issues** → Framework-grounded, with evidence
8. **Assign score** → Use simplified rubric (9-10 / 7-8 / 5-6 / 3-4 / 1-2)

**Evidence Output**:
- Time from app open to first value: [X seconds]
- Paywall timing: [Before/After value] at [X seconds]
- 3 key issues with framework cite
- Score with 1-sentence justification

**Estimated Output Length**: 1-2 pages

---

### RIGOR MODE (45-90 minutes)
**Best for**: Deep product analysis, internal benchmarking, writing case studies, competitive teardowns.

**Flow**:
1. **App store listing** → Document positioning, screenshots, reviews mentioning onboarding
2. **Splash screen** → Time load, capture brand impression
3. **Full auth flow** → Navigate each step, time each, document data requested
4. **Every permission request** → Screenshot each, document response, evaluate context
5. **Onboarding quiz** (if present) → Transcribe all questions, evaluate JTBD vs. demographic
6. **Every screen before value** → Screenshot and timestamp each
7. **Paywall** (if present) → Full analysis, pricing tiers, trial terms, copy tone
8. **First content screen** → Navigation audit, signifier check, clarity assessment
9. **First interaction** → Complete flow with before/after, timing, feedback, subsequent prompts
10. **Detailed evidence** → Fill out entire Evidence Checklist
11. **5-7 key issues** → Comprehensive analysis with comparative benchmarks
12. **Persona-specific review** (if applicable) → Test as new user, returning user, trial user, paid user
13. **Final score** → Detailed justification with point breakdown

**Evidence Output**:
- Evidence Checklist: 90% complete
- 3-5 page detailed analysis
- Multiple persona findings (if reviewed)
- Comparative benchmarks to category leaders
- Prioritized recommendations for improvement

**Estimated Output Length**: 5-10 pages

---

### Hybrid Mode (Recommended)
**Time: 30-45 minutes**

1. Full auth and permission audit (like Rigor)
2. One complete playthrough to first value (like Rigor)
3. Paywall evaluation (like Rigor)
4. Top 3-4 issues (like Speed)
5. Score with moderate justification (hybrid)

**Best for**: Balancing speed with depth. Useful for regular competitive analysis or quarterly product audits.

---

## PERSONA-SPECIFIC INSTRUCTIONS

Test the app as different user personas to understand how onboarding changes across different use cases. Not all personas apply to all apps; choose the ones relevant to your product category.

### 1. New User (First Install, First Launch)
**Persona**: User installs app for the first time, opens it immediately, has no context.

**What to Test**:
- Full onboarding flow (all screens, all questions, all permissions)
- First impression clarity (does app explain what it does?)
- Speed to first value (how long before user sees core feature?)
- Personalization (is it offered? Is it used?)

**Evidence**:
- Time from app open to first value
- Number of steps before value
- Clarity rating of core feature on first screen
- Whether personalization questions are asked and how they change the experience

**Key Metric**: Activation rate (% of users who complete onboarding)

**Scoring Focus**: Time to value, clarity, personalization presence

---

### 2. Free Returning User (Second Open, No Subscription)
**Persona**: User completed onboarding yesterday, opens app today as a free user.

**What to Test**:
- Is onboarding repeated or skipped?
- Are there soft paywalls or limitations shown?
- Is there encouragement to upgrade?
- Does the app remember personalization from first session?

**Evidence**:
- Screenshots of second open screen
- Whether paywall/upgrade prompts appear
- Whether personalization is applied (does content reflect their previous choices?)
- How the app welcomes returning users (is it different from first session?)

**Key Metric**: Day 1 retention, paywall effectiveness

**Scoring Focus**: Paywall placement, personalization retention, friction on second visit

---

### 3. Trial User (After Trial Starts, Before Trial Ends)
**Persona**: User completed signup, trial is active, they're in the middle of using paid features.

**What to Test**:
- Are there indicators of remaining trial time?
- Does the app show content/features that will disappear after trial?
- Is there messaging about converting to paid?
- Are trial limitations enforced or can user ignore them?

**Evidence**:
- Screenshots showing trial status indicator
- Warning messages about trial expiry
- Messaging about conversion to paid
- Timing of first "upgrade to continue" prompt

**Key Metric**: Trial-to-paid conversion rate

**Scoring Focus**: Paywall messaging clarity, trial status visibility, conversion timing

---

### 4. Paid User (After Subscription Purchased)
**Persona**: User has paid for subscription. Do they see different onboarding? Are paid features automatically unlocked?

**What to Test**:
- Is there onboarding for paid features?
- Does the app acknowledge the purchase (celebration screen)?
- Are premium features clearly marked?
- Is there guidance on using newly unlocked features?

**Evidence**:
- Screenshots of post-purchase experience
- Whether premium features are explained or left to discovery
- Any celebration or confirmation of payment success
- First interaction with a premium feature

**Key Metric**: Feature adoption within paid tier

**Scoring Focus**: Premium feature clarity, onboarding for paid (if applicable)

---

### 5. Lapsed User (Returning After 30+ Days of Non-Use)
**Persona**: User who downloaded 30+ days ago, didn't engage, is coming back.

**What to Test**:
- Does app show a re-engagement onboarding?
- Is the original onboarding repeated or skipped?
- Are there "what's new" messages?
- Does the app use prior data to re-engage (e.g., "You created 3 notes. Ready to add more?")

**Evidence**:
- Screenshots of re-engagement flow
- Whether app recognizes returning user status
- Any messaging that leverages prior usage
- How app tries to win them back

**Key Metric**: Lapsed user reactivation rate

**Scoring Focus**: Re-engagement strategy, personalization to prior usage

---

### Persona Scorecard Template

| Persona | Time to Value | Paywall Timing | Clarity | Personalization | Overall Score | Key Issue |
|---------|---------------|----------------|---------|-----------------|---------------|-----------|
| New User | 45 sec | After | Excellent | Yes, visible | 8/10 | N/A |
| Returning (Day 2) | N/A | On-screen | Good | Yes, remembered | 7/10 | Upgrade prompt timing |
| Trial User | 2 min | In-app banner | Good | Partial | 6/10 | No trial timer visible |
| Paid User | 1 min | N/A | Excellent | Yes | 8/10 | N/A |
| Lapsed (30d) | 90 sec | After | Okay | Weak | 5/10 | No re-engagement messaging |

---

## DOMAIN-SPECIFIC OVERLAYS

Apply these additional criteria and benchmarks based on the app's category.

### Education Apps (Duolingo, Coursera, Khan Academy)

**Primary Metric**: Time to first learning moment (benchmark: <60 seconds, ideally <30 seconds)

**Domain-Specific Criteria**:
- Does the first interaction teach something? (Not just a setup screen.)
- Is gamification present in the onboarding? (Progress indicator, point reward, streak start?)
- Can the user immediately understand the learning path? (Is the curriculum visible?)
- Is there a "learning hook" in the first 2 minutes? (A reason to come back?)

**Scoring Modifiers**:
- +1 if time to first learning moment is <30 sec
- +1 if onboarding is skippable for returning users
- -2 if time to first learning moment is >5 min
- -1 if curriculum/learning path is not visible on first screen

**Benchmark Apps**:
- **Duolingo** (9/10): 30-second first lesson, streak begins on day 1, next lesson is suggested
- **Babbel** (7/10): 2-minute first lesson, personalization based on goal, clear curriculum
- **Khan Academy** (6/10): 5-minute setup, paywall after first video (minor friction), good curriculum visibility

**Key Questions**:
- What is the user learning in their first 60 seconds?
- Is there a visible win (points, completion, streak) in the first interaction?
- Does the app immediately show the learning path / curriculum?

---

### OTT / Streaming Apps (Netflix, Spotify, YouTube)

**Primary Metric**: Time to first content play (benchmark: <30 seconds)

**Domain-Specific Criteria**:
- Can user find and start playing content in <30 seconds?
- Is the home feed immediately filled with recommendations?
- Is search always accessible?
- Does personalization affect content recommendations on first screen?

**Scoring Modifiers**:
- +2 if time to first play is <30 sec
- +1 if home feed is pre-loaded with recommendations
- +1 if search is prominent and functional
- -2 if app shows setup screens before showing content
- -2 if onboarding recommends content but doesn't let user play it immediately

**Benchmark Apps**:
- **YouTube** (9/10): 10-second first video play, home feed immediately shows recommendations
- **Netflix** (8/10): 20-second first play, home screen shows personalized recommendations, profile selection adds 5-10 seconds
- **Spotify** (7/10): 30-second first play, but onboarding quiz adds 2-3 minutes for new users (trade-off for better personalization)

**Key Questions**:
- How many taps to play first content?
- Is the home feed showing recommendations immediately, or is it loading?
- Can the user search for specific content on their first visit?

---

### Social Apps (Instagram, TikTok, Slack)

**Primary Metric**: Time to first engagement moment (viewing user-generated content or experiencing the social feed)

**Domain-Specific Criteria**:
- Can user see others' content/posts immediately?
- Is the feed already populated or blank?
- Are follow/friending suggestions shown?
- Is the social graph built during onboarding or discovered?

**Scoring Modifiers**:
- +2 if user sees rich content feed within 30 seconds
- +1 if follow/friending suggestions are shown
- +1 if user can interact (like, comment, message) without completing profile
- -2 if feed is empty on first screen (no content to engage with)
- -2 if user must complete profile before seeing content

**Benchmark Apps**:
- **TikTok** (9/10): Feed visible in 10 seconds, content immediately swipeable, no profile required for viewing
- **Instagram** (7/10): Feed visible in 30 seconds, but profile completion/photo upload is encouraged early (optional but prominent)
- **Slack** (8/10): Team is shown immediately (if user was invited), messages visible without setup, very minimal onboarding

**Key Questions**:
- Is the content feed populated or empty on first screen?
- How many profile fields are required vs. optional?
- Can user interact (like, reply, message) before profile is complete?

---

### Finance / Investing Apps (Robinhood, Coinbase, Wise)

**Primary Metric**: Time to first meaningful action (viewing portfolio, executing first trade, checking balance)

**Domain-Specific Criteria**:
- Are trust signals visible early? (Regulatory badges, security info, insurance claims?)
- Is the onboarding overly strict due to KYC/AML requirements? (Accepted friction, but how minimized?)
- Can user view content before account verification?
- Is the paywall/premium tier features clear?

**Scoring Modifiers**:
- +1 if trust signals are visible on first screen
- +1 if user can view content/prices before account verification
- +1 if KYC/AML flow is broken into digestible steps (not all at once)
- -2 if KYC/AML onboarding is excessively long (>10 minutes)
- -1 if trust signals are absent or buried
- -2 if account verification blocks all content viewing

**Benchmark Apps**:
- **Coinbase** (6/10): Trust signals present, but KYC is mandatory and lengthy (8-12 minutes). Can't view prices without starting verification.
- **Wise** (7/10): Faster KYC (3-5 minutes), trust signals visible, some content viewable before verification
- **Robinhood** (5/10): KYC is lengthy, some prompts for tutorials before seeing portfolio, paywall for premium features is early

**Key Questions**:
- Are regulatory/security badges visible?
- How much content/data can user view before identity verification?
- Is KYC broken into steps or presented as one giant form?
- Is there a paywall for basic functionality vs. premium analytics?

---

### Productivity / Note-Taking Apps (Notion, Evernote, Microsoft OneNote)

**Primary Metric**: Time to create first note/document (benchmark: <2 minutes)

**Domain-Specific Criteria**:
- Can user create a note immediately or is there setup?
- Are templates shown to jump-start creation?
- Is the rich text editor intimidating or intuitive?
- Are collaboration features shown too early or at right time?

**Scoring Modifiers**:
- +1 if user can create first note in <60 seconds
- +1 if templates are available and suggested
- +1 if rich text editor is simple but powerful
- -1 if first screen is empty with no guidance ("Create note" button with no label)
- -2 if collaboration/sharing setup is required before creating first note

**Benchmark Apps**:
- **Apple Notes** (9/10): Blank note ready to edit immediately, minimalist interface, first note created in 5-10 seconds
- **Notion** (7/10): Impressive templates, but initial database/page creation can be confusing, first note takes 1-2 minutes for new users
- **Evernote** (6/10): Onboarding is lengthy, first note can be created quickly but navigation is not intuitive

**Key Questions**:
- How many steps to create the first note?
- Are templates offered?
- Is collaboration mentioned before the user has created anything to collaborate on?

---

### Health & Fitness Apps (MyFitnessPal, Fitbit, Strava)

**Primary Metric**: Time to first workout/health log entry (benchmark: <3 minutes)

**Domain-Specific Criteria**:
- Is there permission pollution (asking for health, location, camera all at once)?
- Is the personalization based on fitness level/goals?
- Can user start logging data before premium paywall?
- Is wearable integration setup required or optional?

**Scoring Modifiers**:
- +1 if fitness level/goals are probed with JTBD questions
- +1 if user can log first workout without integrating wearables
- +1 if time to first log entry is <3 minutes
- -2 if all health/location/camera permissions are requested upfront
- -2 if paywall blocks free logging functionality

**Benchmark Apps**:
- **Strava** (8/10): Asks "What do you do?" and "Fitness level", fast first workout log, optional wearable integration
- **MyFitnessPal** (6/10): Lengthy personalization quiz, paywall for recipes/meal plans, permissions requested early
- **Fitbit** (5/10): Wearable setup is front-and-center, may not work without device, long onboarding

**Key Questions**:
- Are health/location permissions bundled together or contextualized?
- Can user log data without integrating wearables?
- Are fitness goals/level probed in the onboarding quiz?

---

### Messaging / Communication Apps (WhatsApp, Telegram, Signal)

**Primary Metric**: Time to send first message (benchmark: <2 minutes)

**Domain-Specific Criteria**:
- Are contacts imported automatically or manually?
- Is the contact import experience clear?
- Can user see their contact list before importing?
- Is there messaging history shown on first open?

**Scoring Modifiers**:
- +1 if contacts are imported in <30 seconds
- +1 if user can see recent chats immediately
- +1 if first message can be sent in <60 seconds
- -1 if contact import requires multiple steps
- -2 if no contacts are shown on first screen

**Benchmark Apps**:
- **Telegram** (8/10): Fast contact sync, recent chats visible, can start messaging immediately
- **WhatsApp** (7/10): Contact sync is automatic, some setup required, clear chat history
- **Signal** (6/10): Contact sync requires permission and sync step, takes slightly longer than competitors

**Key Questions**:
- How automatic is contact discovery?
- Are recent chats/conversations visible on first screen?
- How many steps to send the first message?

---

### How to Apply Domain-Specific Overlays

1. **Identify the app's category** (Education, OTT, Social, Finance, Productivity, Health, Messaging)
2. **Find the "Primary Metric"** for that category
3. **Measure that metric** during your review (e.g., for Education: time to first learning moment)
4. **Apply the Scoring Modifiers** to your final score
5. **Compare to Benchmark Apps** in the same category
6. **Highlight the key questions** in your findings

**Example**:
- App: Duolingo (Education)
- Base Score: 8/10 (good auth, quick paywall timing, clear navigation)
- Domain Metric: Time to first learning moment = 45 seconds
- Scoring Modifier: 45 sec is between 30-60 sec target, no modifier applied (neutral)
- Compare to Benchmarks: Duolingo should be 9/10 (it's a gold standard)
- Key Questions: ✓ First interaction teaches, ✓ Gamification visible, ✓ Learning path clear, ✓ Hook present
- **Final Score Adjustment**: Upgrade to 9/10 because this app is a benchmark for the category

---

## INDIA-SPECIFIC CHECKS

Every review of an Indian app must include these checks for this module:

### India Auth & Login Patterns
- [ ] Is Truecaller auto-fill supported for phone number entry?
- [ ] Does OTP auto-read work on Android (no need to switch to SMS app)?
- [ ] Is WhatsApp login available as an auth option?
- [ ] Is Google One-Tap sign-in available (dominant on Indian Android)?
- [ ] Does the app handle Indian phone numbers correctly (+91, 10-digit)?
- [ ] Impact if missing: 40-60% higher onboarding friction vs apps with auto-fill. Indian users expect OTP auto-read — manually copying OTP feels broken.

**Finding template:** "Onboarding requires manual phone number entry and OTP copy-paste. No Truecaller auto-fill, no SMS auto-read, no Google One-Tap. This adds 30-45 seconds of friction that Indian users don't experience on Meesho, Zepto, or Swiggy."

**India Benchmark:** Meesho's onboarding: phone + OTP with auto-read → language selection → browse products in under 3 taps. Onboarding completion >85%. Zepto: GPS auto-detect → confirm location → see products in <5 seconds.

### Hindi/Regional Language Onboarding
- [ ] Is a language selection step available during onboarding?
- [ ] Are value proposition screens available in Hindi/Hinglish?
- [ ] Are CTA buttons translated ("Abhi shuru karo" / "Start now")?
- [ ] Are error messages localized?
- [ ] Is social proof in Hindi ("Jaipur se Ravi ne 30 din mein English seekhi")?
- [ ] Impact if missing: 40-60% higher drop-off for Tier 2-3 Hindi-speaking users encountering English-only onboarding.

**Finding template:** "Onboarding is English-only. No language selection, no Hindi CTAs, no localized value propositions. 45-50% of Indian internet users prefer Hindi — this onboarding excludes the majority of the addressable market."

**India Benchmark:** ShareChat's first screen is language selection (15 languages). Kuku FM onboards in 10 Indian languages. Meesho auto-detects region and defaults to appropriate language.

### India Pricing Perception in Onboarding
- [ ] If pricing is shown during onboarding, is it in ₹ with India-appropriate price points?
- [ ] Is there a ₹1 trial or free trial without card requirement?
- [ ] Is "cancel anytime" visible and in Hindi/English?
- [ ] Are UPI payment logos shown early (trust signal)?
- [ ] Impact if missing: Unknown pricing or USD pricing triggers "scam" or "too expensive" perception. No trial = no Tier 2-3 conversion.

**Finding template:** "Onboarding shows pricing in USD / doesn't show pricing at all / shows ₹299 as only option with no trial. For Tier 2-3 India, ₹99 is the ceiling and free trial is expected."

**India Benchmark:** PhysicsWallah shows transparent ₹2-5K/year pricing during onboarding with no sales pressure. Kuku FM shows ₹99/month clearly. Both have trust scores significantly higher than competitors who hide pricing.

### Scoring Modifiers (India)
- +1 if Truecaller auto-fill or OTP auto-read is implemented
- +1 if Hindi/regional language onboarding is available
- +1 if onboarding completes in ≤3 screens
- -1 if onboarding is English-only with no language option
- -1 if phone number entry is manual with no auto-fill
- -1 if pricing is hidden or only shown in USD
- -2 if onboarding requires email (not standard in India) or credit card before value

---

## OUTPUT FORMAT

Structure your findings using this template to ensure consistency and clarity.

```markdown
# ONBOARDING & FIRST VALUE EXPERIENCE — [X]/10

## Evidence Summary

### Timing Metrics
- **Time from app open to first value moment**: [X] seconds
- **Number of steps before first interaction**: [Y] steps
- **Number of permission requests**: [Z] (timing: [before/after value])
- **Time in auth flow**: [A] seconds
- **Paywall timing**: [Before/After/During] first value

### Personalization Audit
- **Personalization type**: [None / Demographic / JTBD-based / Behavioral]
- **Questions asked** (if any): [Paraphrase 2-3 questions]
- **Personalization visible on first content screen**: [Yes / No / Partially]

### Key Metrics
- **Activation confidence**: [Low / Medium / High] (estimation of % who complete onboarding)
- **Paywall effectiveness**: [Blocks / Warns / Non-blocking]
- **Friction points identified**: [Number: 1-2 minor / 3-5 moderate / 6+ severe]

### Frameworks Applied
- **Fogg MAP**: [Brief assessment of Motivation, Ability, Prompt timing]
- **HEART Adoption**: [Brief assessment of engagement signals]
- **JTBD**: [Brief assessment of job understanding]
- **Hook Model**: [Brief assessment of trigger→action→reward cycle]

---

## Evidence

### Screenshot-Supported Findings

**[Screen 1: App Store Listing]**
- App positioning: [1-sentence summary]
- Key visual promise: [What screenshots show about onboarding]
- Review sentiment re: onboarding: [Any positive/negative mentions]
- Framework cite: JTBD (does positioning match actual user job?)

**[Screen 2: Splash / Loading]**
- Load time: [X] seconds
- Brand impression: [Professional / Adequate / Generic] (1-5 scale: [X])
- Framework cite: Nielsen #1 (system visibility)

**[Screen 3: Auth Flow]**
- Total steps: [X]
- Data requested: [Email, Password, Full Name, DOB, ...]
- Time to complete: [X] seconds
- Value shown before auth: [Yes / No / Limited preview]
- Framework cite: Fogg MAP (Ability: form complexity, Motivation: value promise)

**[Screen 4: Permissions]**
- Sequence: [Notifications → Location → Camera → ...]
- Timing of first request: [X] seconds after app open
- Context provided: [Yes for all / Some / None]
- User choice recorded: [Allow / Don't Allow / Maybe Later]
- Framework cite: Nielsen #3 (user control), Fogg MAP (interrupts reduce ability)

**[Screen 5: Onboarding Quiz (if applicable)]**
- Number of questions: [X]
- Type: [JTBD / Demographic / Preference]
- Sample questions: [Q1, Q2, Q3]
- Personalization visible after: [Yes / No]
- Framework cite: JTBD (does quiz discover the job?), Kano (is personalization a satisfier?)

**[Screen 6: Paywall (if applicable)]**
- Timing: [X] seconds after app open / After [action]
- Position relative to first value: [Before / During / After]
- Free tier available: [Yes / No]
- Trial offered: [Yes, X days / No]
- Copy tone: [Value-focused / Loss-averse / Neutral]
- Framework cite: Fogg MAP (paywall timing affects motivation), AARRR (value before monetization)

**[Screen 7: First Content Screen]**
- Primary navigation pattern: [Bottom tabs / Side drawer / Other]
- Clarity of core feature: [Obvious / Clear / Ambiguous / Hidden] (1-5 scale: [X])
- Signifiers present: [Yes: buttons labeled / No: "+ button unlabeled]
- Empty state: [Populated with sample / Blank with guidance / Blank, no guidance]
- Framework cite: Norman (affordances and signifiers), Nielsen #1 (system visibility)

**[Screen 8: First Interaction]**
- Core feature interaction: [Create first note / Send first message / etc.]
- Steps to initiate: [Tap → Enter text → Tap Save = 3 steps]
- Feedback on completion: [Immediate celebration / Clear success / Delayed / None]
- Subsequent prompts: [Rating, Share, Upgrade, None]
- Framework cite: Fogg MAP (ability and motivation at the reward moment), Hook Model (action→reward cycle), HEART (adoption signals)

---

## Scoring Breakdown

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Time to value (<60 sec) | 8/10 | Measured at [X] seconds |
| Paywall timing (after value) | 9/10 | Paywall at [after first interaction] |
| Personalization | 7/10 | Quiz asked 5 JTBD questions, visible on first content screen |
| Permissions (contextualized) | 6/10 | Location requested upfront without context; others deferred |
| First interaction clarity | 8/10 | CTA labeled, feedback immediate, success obvious |
| Navigation intuitiveness | 7/10 | Bottom tabs are clear; help/settings slightly hidden |
| Error handling | 8/10 | Invalid email shows helpful error message |
| Dark patterns | 9/10 | No dark patterns detected |

**Total Score: 7.75 → 8/10** (rounded to nearest integer)

**Justification**: Strong time-to-value and paywall timing put this app in the "Good / Well-Designed" band (7-8). Personalization is present but generic. Permissions have minor friction. Overall, this app demonstrates solid Fogg MAP balance: Ability is high (clear navigation, simple first interaction) and Motivation is sustained (value shown early). A minor deduction for permission context would push this to 8/10 consistently.

---

## Key Issues

### Issue #1: [Title]
**Problem**: [What was observed] — cite evidence with screenshot ref

**Framework Cite**:
- [Framework name]: [Specific principle violated]

**Quantified Impact**: [How many users affected, what's the conversion impact?]

**Hypothesis for Improvement**: [Specific, testable hypothesis]

**Comparative Benchmark**: [What do leading apps do differently?]

---

### Issue #2: [Title]
[Same structure]

---

### Issue #3: [Title]
[Same structure]

---

## Persona-Specific Findings

### New User (First Install)
- **Key metric**: Time to first value = [X] sec
- **Experience**: [Brief description of first 2 minutes]
- **Issues**: [Top 1-2 issues for new users]
- **Score**: [X]/10

### Returning User (Day 2+, Free)
- **Key metric**: Paywall friction on second visit
- **Experience**: [Brief description of second open]
- **Issues**: [Top 1-2 issues for returners]
- **Score**: [X]/10

### Trial User
- **Key metric**: Trial status visibility
- **Experience**: [Brief description of trial period]
- **Issues**: [Top 1-2 issues for trial users]
- **Score**: [X]/10

---

## Recommendations (Prioritized)

### P0 (Critical)
1. **[Issue affecting >50% of users or activation blocker]**
   - Recommendation: [Specific change]
   - Expected impact: [Estimated lift in engagement/activation]

### P1 (High)
2. **[Issue affecting 20-50% of users or retention driver]**
   - Recommendation: [Specific change]
   - Expected impact: [Estimated lift]

### P2 (Medium)
3. **[Issue affecting <20% of users or minor friction]**
   - Recommendation: [Specific change]
   - Expected impact: [Estimated lift]

---

## Appendix: Detailed Evidence Checklist

- [ ] App store listing screenshot
- [ ] Splash screen timing logged
- [ ] Auth flow screens documented
- [ ] Each permission request captured
- [ ] Onboarding quiz (if applicable) transcribed
- [ ] Paywall (if applicable) fully documented
- [ ] First content screen clarity assessed
- [ ] First interaction before/after screenshots
- [ ] Timing measurements validated
- [ ] Persona-specific flows tested (if applicable)

---

**Review Conducted**: [Date] | **Reviewer**: [Name] | **Duration**: [Mode: Speed / Rigor / Hybrid]
```

---

## Summary

This module skill file is now complete and ready for use. It provides:

1. **Comprehensive framework grounding** — Every criterion and issue type is tied to specific expert frameworks (Fogg, HEART, AARRR, JTBD, Hook, Nielsen, Norman, Kano)

2. **Actionable structure** — From screens to navigate, to scoring rubric, to evidence checklist, to key issues template

3. **Flexibility** — Speed Mode vs. Rigor Mode allows testing at different depths

4. **Domain specificity** — Overlays for Education, OTT, Social, Finance, Productivity, Health, and Messaging apps with category-specific metrics and benchmarks

5. **Persona depth** — Instructions for testing across new users, returning users, trial users, paid users, and lapsed users

6. **Professional output format** — Clear template for delivering findings with evidence, scoring breakdown, key issues, and recommendations

The module is thoroughly grounded in expert product thinking and designed for both quick competitive reviews and deep product audits. Every scoring criterion has a framework rationale, and every issue template includes evidence structure, quantified impact, and comparative benchmarks.