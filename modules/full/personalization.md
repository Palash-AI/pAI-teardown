# Personalization & Relevance Module

## MODULE OVERVIEW

### What This Module Reviews
This module evaluates how well the app personalizes its experience to individual users. It assesses whether the app learns from user behavior, proactively shows relevant content, and adapts over time. This is critical for sustained engagement—users feel the app is "made for them," not generic.

**Scope**: From onboarding personalization probes → recommendation engine quality → preference settings → watch/read history → progressive profiling → adaptive difficulty/content scaffolding.

### AARRR Stage Mapping
**Engagement/Retention** — The stages where personalized experiences keep users coming back. This module directly impacts:
- Whether users find content relevant to their goals
- Session frequency (personalized content = more reasons to return)
- Time spent in-app (relevant content = longer engagement)
- Feature adoption (personalization unlocks secondary features)
- Churn prevention (generic = feel like the app isn't for me)

### Design Skill Integration (Mandatory for Screenshots)

> **`design:critique`** — Run on "For You" sections, recommendation cards, preference settings screens, and personalized homepage states. Evaluate: recommendation card design clarity, visual distinction between personalized vs generic content, settings usability, consistency of personalized elements. For India context: is the personalized feed visually different when Hindi is selected vs English? Do regional recommendation cards show location signals ("Popular in Pune")?

> **`design:ux-copy`** — Run on recommendation labels, "For You" section headers, preference question copy, and acknowledgment messages ("Based on your interests..."). Evaluate: are section labels specific ("For You" > "Recommendations")? Do questions feel relevant? For India context: are recommendation labels in Hindi? Does "Popular in your city" copy feel personal? Are preference questions culturally appropriate (exam type, language, job goal)?

### Primary Frameworks & Models

| Framework | Application |
|-----------|-------------|
| **HEART (Engagement, Happiness)** | Does personalization increase user satisfaction and engagement? |
| **Reforge (Product Loop)** | Does personalization create a flywheel (usage → data → better recs → more usage)? |
| **Hook Model (Variable Reward)** | Does personalization deliver variable, surprising content or repetitive/same every time? |
| **JTBD** | Does the app understand the user's actual job and serve it, or generic job? |
| **Fogg Behavioral Model** | Does personalization increase motivation (relevance) and reduce ability friction? |
| **Kano Model** | Personalization is a "satisfier"—its absence is felt as a miss. |

---

## SCREENS TO NAVIGATE

### 1. Onboarding Personalization Probes
**Purpose**: Understand what user data is collected during signup to enable personalization.

**What to Observe**:
- Quiz/questions present: Yes / No / Optional
- If present, are questions JTBD-based or demographic?
- Number of questions asked
- How responses are acknowledged ("Great! We found X for you")
- Whether responses visibly change the first content screen (before/after comparison)
- Timing: Questions before or after showing first content?
- Skip option: Can user skip personalization questions?
- Progressive profiling: Questions asked upfront vs. revealed over time

**What to Screenshot**:
- Personalization question screen (if present)
- All questions (paraphrase or transcribe)
- Screen acknowledgment of answers ("Based on your selection...")
- First content screen after personalization (to see impact)
- Comparison: What does a new user with different answers see (same or different content)?

**What to Document**:
- Question type: JTBD / Demographic / Preference-based
- Number of questions
- Skip option available (yes/no)
- Visibility of impact (is personalization acknowledged to user?)
- Estimated impact: Can you identify that content changed based on answers?

**Framework Checkpoints**:
- **JTBD**: Questions should probe functional/emotional/social jobs, not just demographics
- **Fogg MAP**: Good questions increase motivation (relevance shown early)
- **Kano**: Proactive personalization is a satisfier; absence is noticed negatively

---

### 2. "For You" / Personalized Homepage Section
**Purpose**: Assess the quality and visibility of personalized recommendations on the homepage.

**What to Observe**:
- "For You" or "Recommended" section present
- Section placement: Above fold / Below fold / Hidden until scroll
- Content in section: Relevant to assumed user goals / Generic / Irrelevant

**India-Specific Observations:**
- Does the app personalize by language preference (Hindi user sees Hindi content first, not English)?
- Is there tier-based content personalization (Tier 1 vs Tier 2-3 different recommendations)?
- Does the app show "Popular in [City]" or regional trending signals?
- Is festival/seasonal personalization present (Diwali offers, exam season content, IPL-themed)?
- Does the app support family profiles for shared devices (common in Tier 2-3)?
- Section refresh: Does it show different content on each visit or same items?
- Personalization evidence: Can you tell it's personalized vs. generic?
- How personalization is explained: "Based on your history", "Trending in your interests", or no label?
- Section size: How many items visible? Is there more with scroll?
- Variety: Are recommendations diverse or repetitive?

**What to Screenshot**:
- Full homepage showing "For You" section location
- Zoomed view of "For You" section with 3-5 items
- One recommendation item with visible signals (why was it recommended?)
- Second visit screenshot showing whether recommendations changed
- Comparison with a different user profile (if possible)

**What to Document**:
- "For You" prominence (1-5 scale: invisible to dominant)
- Relevance of recommendations (1-5 scale: highly relevant to random)
- Freshness (same items every visit or variable?)
- Personalization evidence (obvious or invisible?)
- Number of recommendations visible
- Estimated impact: Would user engage with these recommendations?

**Framework Checkpoints**:
- **HEART Engagement**: Does "For You" increase engagement time?
- **Hook Model Variable Reward**: Are recommendations variable (fresh, surprising) each visit?
- **Reforge Product Loop**: Do recommendations create a loop (view → data → better recs)?

---

### 3. Recommendation Quality & Relevance
**Purpose**: Evaluate the accuracy and usefulness of recommendations throughout the app.

**What to Observe**:
- Recommendations visible after consuming content: "Related to this", "Because you watched", etc.
- Recommendation accuracy: Do recommendations match the content you just viewed or the user's profile?
- Recommendation diversity: Are recommendations varied or showing the same items repeatedly?
- Recommendation freshness: Are they recent/trending or old content?
- Recommendation timing: When do recommendations appear (immediately, after delay)?
- Explanation: Are recommendations labeled "Based on your history" or unlabeled?
- Social signals: Do recommendations include user ratings/reviews that influence clicks?

**What to Screenshot**:
- Recommendations shown after viewing one piece of content
- Zoomed view of individual recommendation card
- Compare recommendations for two different content items (are they relevant or generic?)
- Recommendations on second visit (same recommendations or fresh?)

**What to Document**:
- Recommendation accuracy (1-5 scale for each context)
- Recommendation diversity (1-5 scale: repetitive to varied)
- Freshness of recommended content (recently added or old backlog?)
- Explanation label present (yes/no)
- Click potential (would you want to click these recommendations?)

**Framework Checkpoints**:
- **HEART Engagement**: Do recommendations increase time in-app?
- **JTBD**: Are recommendations relevant to the user's actual jobs, or generic?
- **Hook Variable Reward**: Do recommendations provide surprise/discovery, or same items?

---

### 4. Preference Settings & Customization
**Purpose**: Understand whether users can control their personalization.

**What to Observe**:
- Settings page: Present / Hidden / Requires multiple taps
- Preference options available: Language / Content type / Difficulty / Interests / Notification frequency / Other
- Preference clarity: Are options self-explanatory or confusing?
- Impact visibility: When preferences are changed, do results immediately change?
- Reset option: Can user reset personalization to start over?
- Edit ease: How easy is it to change preferences (1 tap vs. 5 taps)?
- Onboarding questions revisit: Can user go back and re-answer personalization quiz?

**What to Screenshot**:
- Settings page showing all preference options
- One preference setting changed (before/after comparison of content)
- Notification frequency setting (if present)
- Any confirmation after changing preferences
- Reset/clear personalization button (if present)

**What to Document**:
- Number of preference options available
- Preference categories (language, content type, difficulty, interests, etc.)
- Ease of changing preferences (1-5 scale: 1 = many taps, 5 = obvious button)
- Feedback when preferences change (immediate / delayed / no feedback)
- Reset capability present (yes/no)

**Framework Checkpoints**:
- **Nielsen #3 (User Control)**: Users should be able to control personalization
- **Fogg MAP**: Easy preference changes = high ability
- **JTBD**: User should be able to update their job if priorities change

---

### 5. Watch/Read History & Content Tracking
**Purpose**: Assess whether the app tracks user consumption and uses it for personalization.

**What to Observe**:
- History visible: Users can see their watch/read history
- History usage: Is history used to recommend similar content? To resume content?
- History organization: By recency / By category / Searchable / Random
- Continue watching/reading: Does app suggest resuming half-finished content?
- History clearing: Can user delete history? Delete individual items?
- Privacy: Is user informed that history is tracked?
- Forget option: Can user ask the app to "forget this" to not recommend similar content?

**What to Screenshot**:
- History page showing user's watch/read history
- Individual history item with metadata (date watched, progress, etc.)
- Continue watching section on homepage (if present)
- How app suggests "Pick up where you left off"
- Delete/clear history options (if present)

**What to Document**:
- History visible and accessible (yes/no)
- History organization clarity (chronological, by type, etc.)
- Integration with recommendations (history drives recommendations?)
- Continue feature presence (yes/no, how helpful?)
- Privacy notice present (yes/no)
- Ability to delete history (full or selective?)

**Framework Checkpoints**:
- **Reforge Product Loop**: History is the data that drives personalization
- **HEART Engagement**: Easy resume (continue watching) increases engagement
- **Hook Investment**: History represents user investment (time spent, streaks, etc.)

---

### 6. Difficulty/Content Scaffolding & Progressive Personalization
**Purpose**: Understand whether the app adapts content difficulty or depth based on user progress.

**What to Observe**:
- Difficulty levels: Present (Beginner / Intermediate / Advanced) or all same level
- Dynamic scaffolding: Does the app suggest next level when user completes current?
- Difficulty recommendation logic: Is it based on test scores, completion rate, or user preference?
- Content prerequisite: Does the app prevent you from accessing advanced content without prerequisites?
- Learning path: Can user see their progression and upcoming content?
- Remediation: If user struggles, does the app suggest easier content or provide more help?

**What to Screenshot**:
- Difficulty selection screen (if present)
- Content detail page showing difficulty level
- Learning path or progression visual (if visible)
- Recommendation for next level (after completing content)
- Struggle signal (if user fails assessment, how does app respond?)

**What to Document**:
- Difficulty scaffolding present (yes/no)
- How difficulty is communicated (labels, badges, visual indicators)
- Dynamic difficulty adjustment (automatic or manual?)
- Learning path visibility (can user see what's next?)
- Remediation features (help for struggling users?)

**Framework Checkpoints**:
- **Fogg MAP**: Difficulty scaffolding reduces ability friction (content is appropriately challenging)
- **JTBD**: Understanding user skill level is part of understanding their job
- **Hook Variable Reward**: Appropriately difficult content is more rewarding

---

### 7. Cold Start Problem & New User Experience
**Purpose**: Assess how the app personalizes for brand-new users with no history.

**What to Observe**:
- Generic homepage: What does a new user with no history see?
- Default recommendations: How are recommendations generated for new users?
- Personalization onboarding: Does the app ask upfront questions to seed personalization?
- Time to personalization: How long before recommendations feel personalized vs. generic?
- Fallback strategy: When there's no data, does the app show trending, popular, or random?

**What to Screenshot**:
- New user homepage (what a fresh install sees)
- Recommendation algorithm for new user (generic or smart?)
- Onboarding flow that seeds personalization
- Comparison: New user experience vs. established user with history

**What to Document**:
- Time to meaningful personalization (how long does user need to use app before recs are personal?)
- Seed personalization present (upfront questions, interest selection, etc.)
- Fallback strategy when no history (trending, popular, random?)
- New user satisfaction (1-5 scale: do new users feel the app is for them?)

**Framework Checkpoints**:
- **JTBD**: New user may not have clear job yet; app should help them discover it
- **Fogg Motivation**: Even new users need value shown early; generic recs reduce motivation
- **Hook Model**: Cold start is the biggest challenge—break into the loop

---

### 8. Personalization Transparency & Explainability
**Purpose**: Understand whether the app explains why recommendations are shown.

**What to Observe**:
- Explanation labels: "Because you watched", "Trending in your interests", "Recommended for you", etc.
- Data collection transparency: Is user told what data is tracked and used for personalization?
- Control transparency: Can user understand what preferences drive personalization?
- Privacy notice: GDPR/privacy disclosure about personalization
- Opt-out: Can user disable personalization and get generic content instead?
- Dark patterns: Is data collection opaque or explicitly clear?

**What to Screenshot**:
- Recommendations with explanation labels (or lack thereof)
- Privacy/settings page showing data collection notice
- Any transparency UI about personalization algorithm
- Opt-out option (if present)

**What to Document**:
- Recommendation explanations present (yes/no, how often?)
- Data collection transparency (explicitly stated or opaque?)
- Privacy notice quality (clear or vague?)
- Opt-out capability (yes/no, how easy?)
- User control over personalization (high / medium / low)

**Framework Checkpoints**:
- **Nielsen #1 (Visibility)**: Users should know what data is collected and how it's used
- **JTBD**: Transparent personalization builds trust
- **Kano**: Transparency is a "Must-Be" for users in regulated markets (India: RBI, TRAI)

---

## SCORING RUBRIC (1-10)

### 9-10: Best-in-Class (Spotify, Netflix, YouTube Level)

**Criteria**:
- **Onboarding personalization**: JTBD-based questions asked upfront; impact is immediately visible
- **"For You" section is excellent**: Relevant, fresh recommendations above fold; user can tell it's personal
- **Recommendations are accurate**: Throughout the app, recommendations match the user's actual interests and history
- **Preference controls are intuitive**: User can easily adjust what the app knows about them
- **History is integrated**: Easy to resume, search history, and "forget" recommendations
- **Difficulty scaffolding works**: App suggests next level or content based on user progress
- **Cold start is handled gracefully**: New users get useful recommendations quickly (upfront questions + smart defaults)
- **Transparency is excellent**: User knows what data is collected and why

**Framework Alignment**:
- **HEART Engagement**: Personalization increases session length, frequency, and feature adoption
- **Reforge Loop**: Usage → data → better recs → more usage. Loop is established.
- **Hook Variable Reward**: Recommendations are fresh and surprising each visit
- **JTBD**: App clearly understands user's job and serves it proactively

**Examples**: Spotify (personalized discovery weekly), Netflix (resume + recommendations + difficulty from start), YouTube (For You feed)

---

### 7-8: Good / Well-Designed

**Criteria**:
- **Onboarding personalization**: Present and questions are mostly JTBD-based
- **"For You" section is good**: Visible, mostly relevant, some freshness
- **Recommendations are mostly relevant**: Mix of on-target and occasional miss
- **Preference controls exist**: Not always obvious but functional
- **History is present**: Can resume content, view history, but might require digging
- **Some difficulty scaffolding**: Beginner vs. advanced visible; not all content is same level
- **New user experience is decent**: Upfront questions or smart defaults help seed personalization
- **Some transparency**: Privacy notice present, though might not be prominent

**Framework Alignment**:
- **HEART Engagement**: Personalization has positive impact; could be stronger
- **Hook Model**: Rewards are mostly variable; some repetition
- **JTBD**: App serves the job reasonably well; not all edge cases handled

**Examples**: Many streaming apps, good productivity tools

---

### 5-6: Adequate / Basic Personalization

**Criteria**:
- **Onboarding personalization is minimal**: Few or generic questions; impact not immediately visible
- **"For You" section exists but is weak**: Present but hard to find; recommendations are generic
- **Recommendations are hit-or-miss**: Maybe relevant, maybe random
- **Preference controls are hard to find**: Settings are buried or unclear
- **History is present but limited**: Can see what you watched but can't easily resume
- **No difficulty scaffolding**: All content appears same level
- **Cold start problem exists**: New users see generic content initially
- **Transparency is minimal**: Privacy notice present but vague

**Framework Alignment**:
- **HEART Engagement**: Personalization has minimal impact on engagement
- **Reforge Loop**: Loop is broken or incomplete (data collected but not used well)
- **JTBD**: App serves job but in generic way, not personalized to this user

**Examples**: Many average productivity and educational apps

---

### 3-4: Poor / Personalization is Weak or Absent

**Criteria**:
- **No onboarding personalization**: App doesn't ask about user preferences
- **No "For You" section**: Recommendations are absent or completely generic
- **Recommendations are irrelevant**: Don't match user's history or interests
- **No preference controls**: User can't customize what they see
- **History is invisible**: User can't see watch/read history or resume content
- **Cold start is broken**: New users see random or irrelevant content
- **No transparency**: No privacy notice or data collection explanation

**Framework Alignment**:
- **HEART Engagement**: Lack of personalization reduces engagement
- **JTBD**: App doesn't understand or serve individual user jobs
- **Kano**: Absence of personalization is a dissatisfier

**Examples**: Many older or legacy apps, some simple tools

---

### 1-2: Severely Flawed / Personalization is Absent or Harmful

**Criteria**:
- **App treats all users identically**: No distinction between users
- **All content is generic or irrelevant**: Recommendations are spam or off-topic
- **Data is collected but not used**: App asks for preferences but ignores them
- **Dark patterns in personalization**: User data is sold or used in ways that feel invasive
- **Cold start blocks engagement**: New users see nothing useful; no onboarding

**Framework Alignment**:
- **JTBD Failure**: App doesn't serve individual user jobs at all
- **Kano Dissatisfier**: Lack of personalization actively reduces satisfaction
- **Hook Model Broken**: No variable rewards; content is same every visit

**Examples**: Spammy apps, legacy enterprise tools, abandoned apps

---

## EVIDENCE CHECKLIST

### Onboarding Personalization

- [ ] **Personalization questions asked during onboarding**: [Yes / No]
- [ ] **If yes, number of questions**: [_____]
- [ ] **Question types**: [JTBD / Demographic / Preference / Mixed]
- [ ] **Sample questions** (paraphrase 2-3): [_____]
- [ ] **Impact on first content screen**: [Obvious (different content vs. generic) / Subtle / Not visible]
- [ ] **User acknowledgment**: ["Based on your selection..." shown / Silent change / No indication]
- [ ] **Skip option**: [Yes / No / Required to complete]

**Framework**: JTBD, Fogg (MAP)

---

### "For You" / Personalized Section

- [ ] **"For You" or "Recommended" section visible**: [Yes, prominent / Yes, hidden / Not present]
- [ ] **Section placement**: [Above fold / Below fold / In secondary screen]
- [ ] **Number of items in section**: [_____]
- [ ] **Recommendation relevance** (1-5 scale): [_____]
- [ ] **Freshness on second visit**: [Same items / Different items / Partially refreshed]
- [ ] **Personalization evidence**: [Obvious (user understands why) / Hidden / Generic]
- [ ] **Explanation label**: ["Based on your history" / "Trending in your interests" / None / Other: _____]

**Framework**: HEART (Engagement), Hook (Variable Reward)

---

### Recommendation Quality

- [ ] **Recommendations throughout app** (after consuming content, in sidebars, etc.): [Yes / No]
- [ ] **Recommendation accuracy** (1-5 scale): [_____]
- [ ] **Recommendation diversity** (1-5 scale: repetitive to varied): [_____]
- [ ] **Freshness of recommended content**: [Recently added / Trending / Old backlog / Mix]
- [ ] **Explanation provided**: [Yes, always / Sometimes / Not present]
- [ ] **Social signals included** (ratings, reviews, view count): [Yes / Partial / No]
- [ ] **Serendipitous discovery** (1-5 scale: same items vs. delightful surprises): [_____]

**Framework**: Hook (Variable Reward), HEART (Engagement)

---

### Preference Settings

- [ ] **Settings/preferences page location**: [Easy to find / Requires digging / Hidden]
- [ ] **Preference options available**: [List types: Language, Content type, Difficulty, Interests, Notifications, Other: _____]
- [ ] **Clarity of preferences**: [Self-explanatory / Learnable / Confusing]
- [ ] **Impact on content**: [Immediate change visible / Delayed / No change]
- [ ] **Reset/clear personalization**: [Option present / Not present]
- [ ] **Onboarding quiz revisit**: [Can re-answer / One-time only]
- [ ] **Ease of changing preferences** (1-5 scale): [_____]

**Framework**: Nielsen #3 (User Control), Fogg (Ability)

---

### History & Content Tracking

- [ ] **Watch/read history visible**: [Yes / No]
- [ ] **History accessible**: [Easy (< 2 taps) / Moderate (3-4 taps) / Hard (5+ taps)]
- [ ] **History organization**: [Chronological / By category / Searchable / Random]
- [ ] **Continue watching/reading feature**: [Present / Missing]
- [ ] **Effectiveness of resume** (1-5 scale): [_____]
- [ ] **History deletion**: [Can delete all / Can delete individual items / Not possible]
- [ ] **Privacy notice about tracking**: [Explicit / Vague / Not present]
- [ ] **Forget/don't recommend option**: [Yes / No]

**Framework**: Reforge (Product Loop), Hook (Investment)

---

### Difficulty/Content Scaffolding

- [ ] **Difficulty levels indicated**: [Yes, explicit (Beginner/Intermediate/Advanced) / Implicit / Not visible]
- [ ] **Dynamic scaffolding**: [App suggests next level / Manual selection / Not present]
- [ ] **Learning path visible**: [Clear pathway / Unclear / Not visible]
- [ ] **Remediation for struggling users**: [Help offered / No support / Not tested]
- [ ] **Progression tracking**: [User can see progress / Progress is hidden / No tracking]

**Framework**: Fogg (Ability), JTBD (Skill level understanding)

---

### Cold Start Problem

- [ ] **New user personalization**: [Seed questions / Smart defaults / Generic for all / Random]
- [ ] **Time to first personalized recommendation**: [Immediately / After 1-2 interactions / After many sessions / Never]
- [ ] **Fallback for new users**: [Trending / Popular / Random / Blank]
- [ ] **New user satisfaction** (1-5 scale): [_____]

**Framework**: JTBD, Fogg (Motivation)

---

### Personalization Transparency

- [ ] **Recommendation explanations**: [Always shown / Sometimes / Never]
- [ ] **Data collection notice**: [Explicit / Vague / Not present]
- [ ] **User understands why they see content**: [Obviously / Implicitly / No idea]
- [ ] **Opt-out capability**: [Easy / Possible but hidden / Not possible]
- [ ] **Privacy/GDPR notice**: [Clear / Present but vague / Not present]
- [ ] **Dark patterns detected**: [None / Subtle / Obvious data harvesting]

**Framework**: Nielsen #1 (Visibility), JTBD (Trust)

---

## KEY ISSUES TEMPLATE

### Issue #1: No Personalization Upfront; App is Generic for All Users
**Problem**: App doesn't ask about user preferences during onboarding. All users see identical homepage and recommendations.

**Framework Cite**:
- **JTBD**: Without understanding the user's job, the app cannot personalize. All users are treated as having identical needs.
- **Kano Model**: Personalization is a satisfier; its absence is felt as "this app doesn't understand me."
- **Fogg MAP**: Generic content reduces motivation (user doesn't see relevance immediately).

**Evidence**: Screenshots showing identical homepage across different user types (new user, returning user, different interests).

**Quantified Impact**: Apps without upfront personalization see 30-50% lower engagement and 20-30% higher churn. Users don't feel the app is "for them."

**Hypothesis for Improvement**:
1. Add 5-7 JTBD questions during onboarding: "What's your goal?", "How much time can you dedicate?", "What's your experience level?"
2. Show impact immediately: First content screen changes based on answers
3. Test: A/B test generic vs. personalized onboarding. Measure engagement, D7 retention.

Estimated impact: 40-60% improvement in engagement, 20-30% improvement in retention.

**Comparative Benchmark**: Duolingo asks "Why are you learning?". Calm asks "Why meditate?". Both see high engagement because personalization is upfront.

---

### Issue #2: "For You" Section is Missing or Generic
**Problem**: No personalized recommendations visible. Or recommendations exist but are same for all users (trending only, not personalized).

**Framework Cite**:
- **HEART Engagement**: Personalization increases engagement. Absence of it means missed engagement opportunity.
- **Hook Model Variable Reward**: Generic trending doesn't deliver variable rewards; user sees same content every visit.
- **Reforge Loop**: Without recommendations, the loop (usage → data → better recs) is broken.

**Evidence**: Screenshots of homepage showing lack of personalization. Compare with a different user profile (same content shown, not personalized).

**Quantified Impact**: Apps with "For You" recommendations see 50-100% higher engagement. Apps without see constant bounce because content isn't relevant.

**Hypothesis for Improvement**:
1. Build recommendation engine: Collaborative filtering (users like you watched X) or content-based (you watched A, so here's B)
2. Show "For You" prominently: Above fold, refreshed daily
3. Explain recommendations: "Based on your history", "Because you watched", etc.
4. Test: Measure engagement with/without "For You". Target 30-50% increase in click-through.

Estimated impact: 50-100% increase in engagement, 30-50% increase in feature adoption.

**Comparative Benchmark**: Netflix shows "Recommended For You" prominently. Spotify shows "Discovery Weekly" recommendations. Both are core engagement drivers.

---

### Issue #3: Recommendations Are Irrelevant or Not Based on History
**Problem**: App shows recommendations, but they don't match user's interests or history. Or recommendations are completely generic (trending only).

**Framework Cite**:
- **JTBD**: Irrelevant recommendations suggest the app doesn't understand the user's job.
- **HEART Task Success**: User's task is to find relevant content. Irrelevant recommendations fail this task.
- **Hook Variable Reward**: Irrelevant recommendations are not rewarding; user learns not to trust the app.

**Evidence**: Screenshots of recommendations for a specific user and context. Document mismatch (e.g., user watched Python course, recommendations show Java unrelated courses).

**Quantified Impact**: Apps with poor recommendation relevance see 20-40% lower engagement and recommendations are rarely clicked (CTR <5%). Apps with relevant recommendations see CTR >20%.

**Hypothesis for Improvement**:
1. Improve algorithm: Use user's watch history, category preferences, difficulty level
2. Diversify recommendations: Mix of "Similar to what you watched" + "Trending in your interests" + "New in your category"
3. Test relevance: For top 100 users, measure recommendation CTR. Target >15% CTR.
4. Collect feedback: "Is this helpful?" button on recommendations to train algorithm

Estimated impact: 50-100% improvement in recommendation CTR, 30-50% improvement in engagement.

**Comparative Benchmark**: YouTube's "Up next" is usually highly relevant (based on watch history). Amazon's product recommendations are accurate (collaborative + content-based).

---

### Issue #4: No Preference Controls; User Can't Customize Personalization
**Problem**: App personalizes but user has no control. Can't change language, difficulty level, or turn off recommendations.

**Framework Cite**:
- **Nielsen #3 (User Control)**: Users should always have control over their experience. Forced personalization violates this.
- **JTBD**: User's job may change. App should allow them to update their preferences.
- **Kano**: Ability to customize is a satisfier; its absence is a dissatisfier.

**Evidence**: Attempt to access preferences. Screenshot settings page showing lack of options or controls.

**Quantified Impact**: Apps with preference controls see 20-30% higher satisfaction (NPS). Users feel agency. Apps without see higher churn (user feels controlled).

**Hypothesis for Improvement**:
1. Add preferences page: Language, content type, difficulty, notification frequency, "Forget my history"
2. Make preferences easy to access: Settings icon always visible or bottom-nav tab
3. Real-time feedback: When user changes preference, show immediate impact ("Now showing Intermediate content")
4. Revisit onboarding quiz: Let user re-answer personalization questions anytime

Estimated impact: 20-30% improvement in satisfaction (NPS), 10-15% reduction in churn.

**Comparative Benchmark**: Spotify lets users adjust recommendation settings per playlist. Netflix lets users hide titles to improve recommendations.

---

### Issue #5: Cold Start Problem; New Users See Generic Content
**Problem**: New users without history see irrelevant or blank recommendations. Takes many sessions before app personalizes.

**Framework Cite**:
- **JTBD**: New user's job is to find out if the app is for them. Generic content fails this test.
- **Fogg Motivation**: Generic content has low motivation. User needs to see value immediately.
- **Hook Model**: Cold start is the hardest—app needs to break into the loop quickly.

**Evidence**: Fresh install experience. Screenshot first-time homepage and recommendations.

**Quantified Impact**: Apps that solve cold start with upfront questions see 30-50% higher Activation. Apps that don't see users abandon before seeing personalized content.

**Hypothesis for Improvement**:
1. Seed personalization upfront: Ask 5-7 JTBD questions during onboarding
2. Smart defaults: If user doesn't answer, use app's most popular content seeded by category
3. Quick personalization: Show "For You" recommendations within 3-5 interactions (not after 100 interactions)
4. Test: Measure time to first personalized recommendation. Target: <5 minutes for new users.

Estimated impact: 40-60% improvement in Activation rate, 20-30% improvement in D7 retention.

**Comparative Benchmark**: Netflix asks profile preferences upfront (content type, kids/mature). Duolingo asks "Why are you learning?". Both solve cold start in onboarding.

---

## SPEED MODE vs RIGOR MODE

### SPEED MODE (15-20 minutes)
1. **Check onboarding** → Are personalization questions asked?
2. **Check "For You"** → Visible? Relevant?
3. **Check recommendations** → Throughout the app, are they relevant?
4. **Check settings** → Can user control personalization?
5. **Check history** → Can user resume and see watch history?
6. **Note 2-3 key issues**
7. **Assign score**

**Output**: 1-2 pages

---

### RIGOR MODE (45-60 minutes)
1. Full onboarding audit (personalization questions, impact)
2. "For You" section (placement, relevance, freshness)
3. Recommendation quality throughout app
4. Preference controls (accessibility, options, impact)
5. History feature (organization, resume, deletion)
6. Difficulty scaffolding (if applicable)
7. Cold start experience (new user)
8. Personalization transparency (explanations, privacy)
9. Complete Evidence Checklist
10. 5-7 key issues
11. Detailed score justification

**Output**: 5-10 pages

---

## PERSONA-SPECIFIC INSTRUCTIONS

### 1. New User (First Install)
**Test**: Is onboarding personalization present? Can new user see personalized content quickly?

**Key Metrics**: Seed questions, cold start time, first "For You" recommendation

**Scoring Focus**: Onboarding personalization, cold start handling

---

### 2. Returning User with History
**Test**: Are recommendations personalized? Do they reflect watch history? Are they fresh?

**Key Metrics**: Recommendation relevance, freshness, engagement

**Scoring Focus**: Recommendation quality, history integration

---

### 3. Power User Customizing Preferences
**Test**: Can user adjust their personalization? Are preference changes reflected immediately?

**Key Metrics**: Preference control accessibility, impact visibility

**Scoring Focus**: Preference controls, user agency

---

## DOMAIN-SPECIFIC OVERLAYS

### Education Apps
- **Domain criteria**: Does app track learning progress and adapt difficulty?
- **Scoring modifier**: +1 if difficulty scaffolding is automatic; -1 if all content is same level

### OTT / Streaming
- **Domain criteria**: Are recommendations fresh weekly? Do they match viewing history?
- **Scoring modifier**: +1 if "Continue Watching" is prominent; -1 if recommendations are generic

### Productivity
- **Domain criteria**: Does app learn your workflow and suggest relevant features?
- **Scoring modifier**: +1 if app shows relevant features proactively; -1 if all features are always shown equally

---

## INDIA-SPECIFIC CHECKS

Every review of an Indian app must include these checks for this module:

### Language-as-Personalization
- [ ] Does the app personalize by language preference (not just translate UI)?
- [ ] Is the content feed/library filtered by selected language?
- [ ] Are recommendations language-aware (Hindi user gets Hindi content first)?
- [ ] Can users switch language without losing personalization data?
- [ ] Impact if missing: In India, language IS the primary personalization axis. A Hindi user seeing English-first content feels the app "isn't for me" — this is a deeper personalization failure than wrong recommendations.

**Finding template:** "Language toggle exists but doesn't affect content recommendations. Switching to Hindi only changes UI labels — content feed remains English-first. Language-as-personalization is not implemented."

**India Benchmark:** ShareChat: language selection → entire feed, trending, and recommendations filtered to that language. Kuku FM: language + genre as primary personalization axes. Pratilipi: 12 languages, each with independent recommendation algorithms.

### Tier-Based Content Personalization
- [ ] Does the app detect Tier 1 vs Tier 2-3 user patterns and show different content?
- [ ] Are price points personalized by tier/region?
- [ ] Does the app adjust content complexity by user sophistication level?
- [ ] Are "Popular in [City]" or regional trending signals used?
- [ ] Impact if missing: Tier 1 and Tier 2-3 users have fundamentally different content preferences, price sensitivity, and engagement patterns. One-size-fits-all personalization underperforms by 30-40%.

**Finding template:** "All users see identical content feed regardless of location or tier. No regional popularity signals. No price personalization by tier. Tier 2-3 users see Tier 1 content that feels aspirational rather than relatable."

**India Benchmark:** Flipkart shows premium products and faster delivery to Tier 1, value deals and EMI options to Tier 2-3. Regional language campaigns show 20%+ higher CTR than English-only in Tier 2.

### Festival & Regional Personalization
- [ ] Does the app personalize for festivals (Diwali, Holi, Eid, Pongal, etc.)?
- [ ] Are regional events reflected in content/recommendations?
- [ ] Is there cricket/IPL season content personalization?
- [ ] Are seasonal patterns (exam season, festival season, cricket season) used in recommendation timing?
- [ ] Impact if missing: Indian consumers respond strongly to cultural context. Festival-themed content and recommendations see 2-5x engagement spikes.

**Finding template:** "No festival personalization. No regional event awareness. During IPL season, app shows generic content while competitors run cricket-themed engagement. Missing India's strongest cultural engagement triggers."

**India Benchmark:** Flipkart Big Billion Days: festival-specific homepage takeover drives 50%+ of annual GMV. Josh/Moj: festival-specific hashtag challenges see 5-10x normal engagement.

### Family Profile Sharing
- [ ] Does the app support multiple profiles under one account (phone sharing is common)?
- [ ] Can personalization be separated between family members?
- [ ] Is content appropriate for shared viewing context?
- [ ] Impact if missing: In Tier 2-3 India, phone sharing within families is common. One user's viewing history corrupting another's recommendations degrades the experience for everyone.

**Finding template:** "Single profile per account. No family profiles. In Tier 2-3 India where phone sharing is common, one family member's activity corrupts personalization for others."

**India Benchmark:** Netflix India: multiple profiles with separate recommendation engines. YouTube: profile switching for family devices.

### Scoring Modifiers (India)
- +1 if language-based personalization affects content feed (not just UI)
- +1 if tier-based or regional personalization is implemented
- +1 if festival/cultural event personalization exists
- -1 if language selection only changes UI labels, not content recommendations
- -1 if all users see identical content regardless of location/tier
- -1 if no family profile support for shared devices

---

## OUTPUT FORMAT

```markdown
# PERSONALIZATION & RELEVANCE — [X]/10

## Evidence Summary

### Onboarding Personalization
- **Questions asked**: [Yes / No]
- **Question quality**: [JTBD / Demographic / Mixed]
- **Impact on experience**: [Obvious / Subtle / Not visible]

### Recommendation Quality
- **"For You" visible**: [Yes, prominent / Yes, hidden / No]
- **Relevance**: [Highly relevant / Mixed / Irrelevant]
- **Freshness**: [Variable each visit / Same items / Stale]

### User Control
- **Preference controls**: [Easy to access / Hidden / None]
- **Options available**: [Language, Difficulty, Interests, Notifications, Other]
- **Customization impact**: [Visible / Hidden / Not working]

### History Integration
- **Watch/read history**: [Visible / Hidden / Missing]
- **Resume feature**: [Working / Broken / Missing]
- **History used for recommendations**: [Yes / Partially / No]

### Key Metrics
- **Personalization evidence**: [Obvious (user feels it) / Implicit / Not visible]
- **User agency**: [High (can control) / Medium / Low (forced)]
- **Recommendation CTR** (estimate): [High / Medium / Low]

### Frameworks Applied
- **HEART**: Engagement, Happiness assessed
- **Hook**: Variable Rewards evaluated
- **Reforge**: Product Loop assessed
- **JTBD**: Job understanding evaluated

---

## Evidence

### [Screen 1: Onboarding Personalization]
- **Questions present**: [Yes / No]
- **Question quality**: [Type and relevance]
- **Impact visible**: [Before/after comparison of content]
- **Framework cite**: JTBD, Fogg

### [Screen 2: "For You" Section]
- **Visible**: [Location, prominence]
- **Relevance**: [Examples of recommendations shown]
- **Freshness**: [Same or different on second visit]
- **Framework cite**: HEART (Engagement), Hook (Variable Reward)

### [Screen 3: Recommendations Throughout App]
- **Location**: [After content, sidebars, etc.]
- **Accuracy**: [Match user's history / Generic]
- **Explanation**: [Label showing why recommended]
- **Framework cite**: JTBD, Hook

### [Screen 4: Preference Controls]
- **Accessibility**: [Easy / Buried]
- **Options**: [Available settings]
- **Impact**: [Changes are reflected]
- **Framework cite**: Nielsen #3 (Control)

### [Screen 5: History & Resume]
- **History visible**: [Yes / No]
- **Resume feature**: [Working / Missing]
- **Organization**: [Chronological / By type]
- **Framework cite**: Reforge (Loop), Hook (Investment)

---

## Scoring Breakdown

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Onboarding personalization | [X]/10 | [Questions present/absent, JTBD-based/demographic] |
| "For You" quality | [X]/10 | [Visible, relevant, fresh/generic, static] |
| Recommendation accuracy | [X]/10 | [Match history / Irrelevant] |
| Preference controls | [X]/10 | [Easy to find / Buried / Missing] |
| History integration | [X]/10 | [Used for recs / Visible but not used / Hidden] |
| Difficulty scaffolding | [X]/10 | [Dynamic / Manual / Missing] |
| Cold start handling | [X]/10 | [Upfront questions / Smart defaults / Generic] |
| Personalization transparency | [X]/10 | [Clear explanations / Opaque / Dark patterns] |

**Total Score: [X.X] → [X]/10**

**Justification**: [2-3 sentences grounded in frameworks]

---

## Key Issues

### Issue #1: [Title]
[Standard format]

---

## Recommendations

### P0 (Critical)
1. **[Issue affecting >50% of users or blocking engagement]**
   - Recommendation: [Specific change]
   - Expected impact: [Estimated lift]

---

**Review Conducted**: [Date] | **Reviewer**: [Name] | **Duration**: [Mode]
```

---

## Summary

This module evaluates personalization—the engine of engagement and retention. It assesses whether the app understands individual user jobs and serves them proactively. Grounded in HEART (Engagement), Hook (Variable Rewards), Reforge (Product Loops), and JTBD, this module identifies gaps in personalization and provides recommendations for building loops that keep users returning.

