# AI Integration Module

## MODULE OVERVIEW

### What This Module Reviews
This module evaluates how well the app integrates AI features—chatbots, AI coaches, smart recommendations, and AI-powered content. It assesses whether AI features are discoverable, trustworthy, contextually relevant, and actually useful to users. This is critical for modern apps where AI can be a differentiator or a gimmick.

**Scope**: From AI chatbot/coach visibility → prompt suggestions → conversation quality → AI recommendations accuracy → AI features integration → user trust and disclaimers.

### AARRR Stage Mapping
**Engagement/Retention** — The stages where AI features keep users engaged and returning. This module directly impacts:
- Whether users discover and use AI features
- Time spent in-app (AI provides value through conversation, recommendations)
- Frequency of return (AI coach/chatbot creates daily habits)
- Retention (personalized AI recommendations keep content fresh)

### Design Skill Integration (Mandatory for Screenshots)

> **`design:critique`** — Run on AI chat interface, AI suggestion cards, AI onboarding/explanation screens, and AI-generated content displays. Evaluate: chat interface usability (input field size, send button clarity), AI response readability, suggestion card design, trust signal placement (disclaimers, "talk to human" option). For India context: is the AI interface approachable for first-time AI users? Does it feel trustworthy on a budget device? Is the "talk to human" fallback visually prominent?

> **`design:ux-copy`** — Run on AI chat prompts, suggested questions, AI response formatting, disclaimer text, and onboarding explanation copy. Evaluate: are suggested prompts specific and helpful? Is AI response formatting scannable? Are disclaimers clear? For India context: are suggested prompts in Hindi/Hinglish? Does the AI explanation use simple language ("Yeh aapka personal teacher hai" > "AI-powered learning assistant")? Is the data privacy disclaimer in Hindi?

### Primary Frameworks & Models

| Framework | Application |
|-----------|-------------|
| **JTBD** | Does AI help user accomplish their job better, or is it a novelty? |
| **HEART (Happiness, Task Success)** | Does AI increase satisfaction and help users complete tasks? |
| **Kano Model (Attractive Feature)** | AI is usually an "attractive" feature—delightful if present, not missed if absent |
| **Norman's Design Principles** | Conceptual model of how AI works; feedback on AI suggestions |
| **Hook Model** | Does AI provide variable, rewarding interactions? |

---

## SCREENS TO NAVIGATE

### 1. AI Feature Discoverability
**Purpose**: Assess whether users can find AI features.

**What to Observe**:
- AI chat/coach visibility: Floating button / Dedicated tab / Hidden in menu / Not present
- Prominence: Always visible / Appears after X interactions / Hidden initially
- Labeling: Clear label (e.g., "AI Coach") / Ambiguous / No label
- Onboarding mention: Is AI feature explained during onboarding? / Discovered by user
- Suggestion to use: Does app proactively suggest using AI? / User must discover
- Icon quality: Does icon signal "AI" or "chat"? (⚡ for AI, 💬 for chat)

**What to Screenshot**:
- Full screen showing AI feature location (if visible)
- Zoomed view of AI button/tab
- Onboarding screen mentioning AI (if present)
- Floating chat button or other entry point

**What to Document**:
- AI feature prominence (1-5 scale: invisible to dominant)
- Discoverability friction (how many taps to access AI?)
- Labeling clarity (obvious it's AI or requires explanation?)
- Onboarding coverage (mentioned during setup / user must discover)

**Framework Checkpoints**:
- **Nielsen #1 (Visibility)**: Is the AI feature visible or hidden?
- **Norman Signifiers**: Does the icon/label signal "AI" or "chat"?
- **Hook Model External Trigger**: Is there a prompt to use the AI feature?

---

### 2. AI Chat / Chatbot Interface & Quality
**Purpose**: Evaluate the chatbot experience if present.

**What to Observe**:
- Chat interface: Message bubbles / List format / Single-line input / Complex UI
- Input method: Text input / Voice input / Suggested prompts / Multiple modes
- Suggested prompts: "Example questions" shown on first open / Not present
- Conversation clarity: Does AI understand user's message? Responds relevantly?
- Response quality: Helpful / Partially helpful / Irrelevant / Confusing
- Response time: Instant / <2 seconds / >2 seconds / No response
- Conversation history: Saved / Not saved / Visible / Hidden

**India-Specific Observations:**
- Does AI chat work in Hindi? Does it handle Hinglish (mixed Hindi-English) input?
- Is voice input to AI available? In Hindi?
- Is there a trust-building explanation in Hindi ("Yeh aapka personal teacher hai")?
- Are suggested prompts available in Hindi/Hinglish?
- Is there a "talk to human" fallback for users who distrust AI?
- Context awareness: Does AI understand the app's content, or generic AI?
- Error handling: If AI doesn't understand, does it ask for clarification?
- Handoff to human: Can user escalate to human support? / No option

**What to Screenshot**:
- Chat interface at start (suggested prompts, if present)
- Sample conversation with user question and AI response
- AI response showing relevant information or suggestions
- Context-specific AI response (e.g., AI recommending content based on user's history)
- Error state (if AI misunderstands)
- Suggested follow-up questions (if present)

**What to Document**:
- Chat intuitiveness (1-5 scale)
- Response quality (1-5 scale: unhelpful to very helpful)
- Response relevance (1-5 scale: off-topic to perfectly relevant)
- Context awareness (generic AI or app-aware?)
- Response time (seconds)
- Suggested prompts quality (helpful / generic / confusing)

**Framework Checkpoints**:
- **JTBD**: Does AI help user accomplish their job?
- **HEART Task Success**: Can user complete their task via AI chat?
- **Norman Conceptual Model**: Does user understand how to use the AI?

---

### 3. AI-Generated Recommendations & Content
**Purpose**: Assess the quality of AI recommendations if present.

**What to Observe**:
- AI recommendations visible: "AI-picked for you" / "AI recommends" / Not labeled as AI
- Recommendation accuracy: Relevant to user / Off-topic / Mix
- Recommendation freshness: Different each time / Same items repeated
- How recommendations are explained: "Based on your history" / No explanation / "AI picked"
- Recommendation confidence: High-confidence picks / Mix of risky / All low-confidence
- User feedback: Can user rate recommendations helpful/unhelpful? / No feedback option
- AI personalization evidence: Generic trending vs. personalized to user
- Recommendation speed: Instant / Delayed / Real-time as user navigates

**What to Screenshot**:
- AI recommendations section (if visible)
- Individual recommendation with explanation
- Zoomed view of how recommendations are labeled
- Feedback option (helpful/unhelpful rating)
- Comparison of AI recs vs. trending (if both visible)

**What to Document**:
- Recommendation relevance (1-5 scale)
- Freshness (variable / same items)
- Explanation quality (clear / opaque)
- User feedback capability (yes / no)
- AI personalization evidence (obvious / invisible)

**Framework Checkpoints**:
- **Hook Variable Reward**: Do recommendations deliver variable surprises?
- **JTBD Locate**: Do AI recommendations help user find relevant content?
- **Kano Attractive**: Are AI recommendations delightful or spam?

---

### 4. AI-Within-Content Features
**Purpose**: Understand AI features embedded within the content consumption experience.

**What to Observe**:
- AI summaries: Available for long-form content / Not present
- AI highlights: Key points extracted by AI / Not available
- AI quiz generation: AI generates questions for learning content / Not available
- AI note-taking suggestions: AI suggests notes during content / Not available
- AI search within content: Can user search a document/transcript via AI? / Not available
- AI transcription: Transcripts generated by AI / Human-made / Not available
- AI content creation: Can user create content via AI? / Not available

**What to Screenshot**:
- AI summary section (if present)
- AI-extracted highlights or key points
- AI quiz or assessments (if present)
- AI search functionality (if available)
- Transcript (human vs. AI generated)

**What to Document**:
- Which AI features are embedded
- Quality of summaries (1-5 scale: accurate to inaccurate)
- Quality of highlights (1-5 scale: insightful to obvious)
- Usefulness of AI quiz (1-5 scale)
- Accessibility of these features (always visible / requires clicking)

**Framework Checkpoints**:
- **JTBD Execute**: Do AI features help user execute their job better?
- **HEART Task Success**: Do AI features improve task completion rates?
- **Norman**: Is it clear what AI features are doing?

---

### 5. AI Trust & Transparency
**Purpose**: Assess whether users trust the AI and understand its limitations.

**What to Observe**:
- AI limitations disclosed: "AI may be inaccurate" warning / Not mentioned / Implicit
- Source attribution: "Based on content X" / No attribution / Sources listed
- Confidence indicator: AI shows confidence level (e.g., "Highly confident") / No indicator
- Disclaimer on AI content: "AI-generated; may have errors" / No disclaimer / Vague
- User understanding: Is it clear this is AI and not human-created? / Ambiguous / Clear
- Feedback for improvement: Can user report AI errors? / No reporting / Hidden
- Privacy assurance: Is user told their chat is private or logged? / No mention
- Data usage: Is user told how their data is used for AI training? / Not disclosed

**What to Screenshot**:
- AI disclaimer or trust indicator (if present)
- Confidence display (if present)
- Privacy notice about AI data usage
- Feedback mechanism for AI errors (if present)
- Source attribution (if shown)

**What to Document**:
- Trust indicator presence and clarity
- Disclaimer quality (clear / vague / not present)
- Confidence display (yes / no)
- Privacy/data usage disclosure (explicit / implicit / not present)
- User understanding likelihood (1-5 scale: clear to confused)

**Framework Checkpoints**:
- **Nielsen #1 (Visibility)**: Is it clear what the AI is and isn't?
- **Fogg Motivation**: Trust in AI increases motivation to use it
- **Cagan Value Risk**: Users need assurance that AI is accurate before trusting it

---

### 6. AI Feature Integration with Core App
**Purpose**: Assess how well AI features are integrated into the main app experience.

**What to Observe**:
- Context awareness: Does AI know what content user is viewing? / Generic AI
- Smart suggestions: Does AI proactively suggest next steps? / User must ask
- Seamless handoff: Can user chat about the content they're viewing? / Separate experience
- Feature discoverability: Are AI features suggested at relevant moments? / Always hidden
- Workflow integration: Is AI chat integrated into the learning/viewing flow? / Separate tab
- Interruption level: Does AI interrupt user's flow? / Seamlessly integrated / Hidden

**What to Screenshot**:
- AI feature in context (e.g., chat while viewing content)
- Smart suggestions based on current context
- Seamless transition from content to AI help
- How AI is suggested at relevant moments

**What to Document**:
- Integration level (seamless / separate feature / isolated)
- Context awareness evidence (obvious / generic)
- Smart suggestion quality (helpful / not present)
- User flow disruption (1-5 scale: seamless to interrupting)

**Framework Checkpoints**:
- **JTBD Execute**: Does AI help user execute their current job without friction?
- **Fogg Ability**: Good integration reduces friction
- **Hook Model**: Seamless integration increases hook strength

---

## SCORING RUBRIC (1-10)

### 9-10: Best-in-Class (ChatGPT Integration, Claude in App Level)

**Criteria**:
- **AI is discoverable and inviting**: Floating button always visible; suggested prompts on first open
- **Chat quality is excellent**: Understands context; responses are relevant, helpful, fast
- **App-aware AI**: Chatbot knows content; recommends based on user's history; context-specific
- **Recommendations are accurate**: AI-picked content is relevant; labeled as AI; user can rate
- **Trust is built-in**: Disclaimers present; confidence indicators shown; privacy explained
- **Integration is seamless**: AI is part of the main flow, not a side feature
- **AI features within content**: Summaries, highlights, quizzes, transcripts all available
- **Feedback mechanism works**: User can report errors; AI learns over time
- **User testing evident**: Feature is polished; no crashes; fast responses

**Framework Alignment**:
- **JTBD**: AI directly helps user accomplish their job
- **HEART Task Success**: AI improves task completion
- **Kano Attractive**: AI is delightful and useful
- **Hook Variable Reward**: Conversations are variable and rewarding

**Examples**: ChatGPT (excellent conversation quality), Claude (context-aware), Duolingo Max (AI coach integrated into learning)

---

### 7-8: Good / Well-Designed AI Feature

**Criteria**:
- **AI is visible but not aggressive**: Easy to find; not interrupting
- **Chat quality is good**: Mostly understands context; responses helpful; minor latency
- **Recommendations are mostly relevant**: Mix of hits; some personalization evident
- **Some disclaimers present**: Trust signals visible though maybe not comprehensive
- **Moderately integrated**: AI is accessible but feels like a separate feature
- **Some AI features within content**: Maybe summaries or highlights; not all features
- **Feedback possible but not prominent**: User can report, but mechanism is hidden
- **Reliable performance**: No major crashes; acceptable latency

**Framework Alignment**:
- **JTBD**: AI is helpful but not essential
- **HEART Task Success**: AI improves some tasks; others not impacted
- **Hook**: Some variable rewards; some repetition

**Examples**: Some modern education apps, integrated AI tutors

---

### 5-6: Adequate / Basic AI Feature or Gimmicky

**Criteria**:
- **AI is present but hard to find**: Hidden in menu or requires discovery
- **Chat quality is basic**: Generic AI; doesn't understand app context; slow responses
- **Recommendations are generic**: Trending mostly; little personalization
- **Minimal trust signals**: No disclaimers or privacy info
- **Isolated feature**: AI chat is separate from main app experience
- **Few AI features within content**: Maybe suggestions; mostly missing
- **Feedback not available**: Users can't report errors
- **Occasional issues**: Some latency or crashes

**Framework Alignment**:
- **JTBD**: AI is nice-to-have, not essential
- **Kano**: AI feels like a gimmick
- **Hook**: Rewards are repetitive; users try once then ignore

**Examples**: Many apps with bolted-on chatbots

---

### 3-4: Poor / AI Feature is Broken or Useless

**Criteria**:
- **AI is hidden or missing**: User doesn't know it exists
- **Chat quality is poor**: Doesn't understand queries; irrelevant responses; very slow
- **Recommendations are terrible**: Completely off-topic; no personalization
- **No trust signals**: No disclaimers; scary privacy implications
- **Completely disconnected**: AI doesn't know app content; generic AI
- **AI features broken**: Features crash or don't work
- **No feedback mechanism**: Users trapped with bad AI

**Framework Alignment**:
- **JTBD Failure**: AI doesn't help user accomplish anything
- **HEART Failure**: AI reduces satisfaction
- **Kano Reverse**: AI feature is actively disliked

**Examples**: Many legacy "AI features" added as afterthought

---

### 1-2: Severely Flawed / AI is Harmful or Non-functional

**Criteria**:
- **AI is broken**: Chatbot crashes or gives nonsensical responses
- **AI is misleading**: Provides false information without disclaimer
- **AI is intrusive**: Aggressive pop-ups trying to push AI
- **Privacy violation**: No disclosure of how user data is used for AI training
- **Dark patterns**: AI chat collects data deceptively; no opt-out

**Framework Alignment**:
- **Fogg Ability Failure**: Bad AI increases friction
- **HEART Failure**: AI damages user satisfaction
- **Cagan Value Risk Failure**: Users can't trust AI; value is zero

**Examples**: Spammy chatbots, misleading AI claims

---

## EVIDENCE CHECKLIST

### AI Feature Discoverability

- [ ] **AI chat/coach present**: [Yes / No]
- [ ] **AI feature location**: [Floating button / Dedicated tab / Menu / Other / Not visible]
- [ ] **Prominence** (1-5 scale): [_____]
- [ ] **Label clarity**: [Clear (says "AI" or "Coach") / Ambiguous / No label]
- [ ] **Onboarding mention**: [Yes / No]
- [ ] **Time to discover**: [Immediately visible / After X interactions / Must dig / Hidden]
- [ ] **Icon quality**: [Signals AI / Generic chat icon / Unclear]

**Framework**: Nielsen #1, Norman (Signifiers)

---

### AI Chat Quality

- [ ] **Chatbot present**: [Yes / No]
- [ ] **Chat interface**: [Message bubbles / List / Other]
- [ ] **Suggested prompts**: [Present / Not present]
- [ ] **Input methods**: [Text / Voice / Both / Limited]
- [ ] **Sample conversation tested**: [Query and response documented]
- [ ] **Response relevance** (1-5 scale): [_____]
- [ ] **Response quality** (1-5 scale): [_____]
- [ ] **Response time**: [<1 sec / 1-3 sec / >3 sec]
- [ ] **Context awareness**: [App-aware / Generic AI / Not tested]
- [ ] **Conversation history**: [Saved / Not saved / Not tested]
- [ ] **Error handling**: [Good recovery / Basic / None]

**Framework**: JTBD, HEART (Task Success), Norman

---

### AI Recommendations

- [ ] **AI recommendations visible**: [Yes, labeled as AI / Yes, not labeled / No]
- [ ] **Recommendation accuracy** (1-5 scale): [_____]
- [ ] **Freshness**: [Variable / Same items / Not tested]
- [ ] **Explanation provided**: [Yes, clear / Yes, vague / No]
- [ ] **User feedback option**: [Yes / No]
- [ ] **Personalization evidence**: [Obvious / Implicit / Generic]
- [ ] **Confidence indicator**: [Yes / No]

**Framework**: Hook (Variable Reward), JTBD (Locate)

---

### AI-Within-Content Features

- [ ] **Summaries available**: [Yes / No]
- [ ] **Highlights available**: [Yes / No]
- [ ] **Quiz generation**: [Yes / No]
- [ ] **Transcript**: [AI-generated / Human / Not available]
- [ ] **AI search**: [Yes / No]
- [ ] **AI note suggestions**: [Yes / No]
- [ ] **Feature quality** (1-5 scale): [_____]

**Framework**: JTBD (Execute), HEART (Task Success)

---

### AI Trust & Transparency

- [ ] **Disclaimer present**: [Explicit / Implicit / Not present]
- [ ] **Disclaimer clarity**: [Clear / Vague / Misleading]
- [ ] **Confidence display**: [Yes, clear / Yes, unclear / No]
- [ ] **Source attribution**: [Yes / Partial / No]
- [ ] **Privacy notice**: [Explicit / Implicit / Not present]
- [ ] **Data usage for AI training**: [Disclosed / Implied / Not mentioned]
- [ ] **User trust confidence** (1-5 scale): [_____]
- [ ] **Error reporting**: [Yes / No]

**Framework**: Nielsen #1 (Visibility), Fogg (Motivation)

---

### AI Integration with App

- [ ] **Feature isolation**: [Seamlessly integrated / Separate feature / Isolated]
- [ ] **Context awareness**: [App-aware / Generic / Not applicable]
- [ ] **Smart suggestions**: [Proactive / User-initiated / Not present]
- [ ] **Workflow disruption** (1-5 scale, 1 = seamless, 5 = very disruptive): [_____]
- [ ] **Feature discoverability at relevant moments**: [Yes / No]

**Framework**: JTBD (Execute), Fogg (Ability)

---

## KEY ISSUES TEMPLATE

### Issue #1: AI Feature is Hidden or Not Discoverable
**Problem**: AI chatbot or AI features exist but user has no idea. Must dig through menu to find.

**Framework Cite**:
- **Nielsen #1 (Visibility)**: AI feature should be visible and accessible
- **Hook Model External Trigger**: Users won't use AI if they don't know it exists

**Evidence**: Show app without AI feature obvious. Document steps to find it.

**Quantified Impact**: Hidden AI features have <10% usage. Visible AI features have 30-50% usage.

**Hypothesis for Improvement**:
1. Add floating chat button (visible on all screens)
2. Suggest AI in onboarding ("Try our AI coach to personalize")
3. Show "Try AI" prompt at relevant moments (stuck on question, want recommendation)

Estimated impact: 300-500% increase in AI feature usage.

**Comparative Benchmark**: ChatGPT shows chat prominently. Duolingo's AI coach is suggested during setup.

---

### Issue #2: Chatbot is Generic; Doesn't Know App Content
**Problem**: Chat works but doesn't understand the app's content. Responds with generic advice, not app-specific help.

**Framework Cite**:
- **JTBD**: AI should help user accomplish their job. Generic AI doesn't help with app-specific job.
- **HEART Task Success**: User can't complete their task because AI doesn't know app context

**Evidence**: Ask chatbot a question specific to the app content. Document if response is context-aware or generic.

**Quantified Impact**: Context-aware AI see 40-60% higher engagement. Generic AI feels useless; users try once then ignore.

**Hypothesis for Improvement**:
1. Build app-specific knowledge base: Feed AI the app's content library
2. Add context to every query: Include user's current content/context with query
3. Train AI on app domain: Use app-specific Q&A to improve responses
4. Test: Compare generic vs. context-aware responses. Users should prefer context-aware.

Estimated impact: 50-100% improvement in AI engagement, 30-50% improvement in AI feature satisfaction.

**Comparative Benchmark**: Duolingo's AI coach knows your learning level and suggests lessons. Claude can reference documents provided. Both are context-aware.

---

### Issue #3: AI Recommendations Are Inaccurate or Spam
**Problem**: AI recommends content that's completely irrelevant or is spam.

**Framework Cite**:
- **Kano Model**: AI recommendations should be attractive/delightful, not reverse (disliked)
- **JTBD Locate**: Inaccurate recommendations fail to help user find relevant content
- **Cagan Value Risk**: Users lose trust in AI when recommendations are bad

**Evidence**: Document 5-10 AI recommendations and their relevance. Are they hitting or missing?

**Quantified Impact**: Accurate AI recommendations see 30-50% click-through. Inaccurate ones see <5% CTR.

**Hypothesis for Improvement**:
1. Improve algorithm: Use user history + collaboration filtering
2. Add feedback loop: Let user rate recommendations helpful/unhelpful
3. Show confidence: Only show recommendations AI is confident about
4. Test relevance: Measure CTR on AI recs. Target >15%.

Estimated impact: 50-100% improvement in AI recommendation engagement.

**Comparative Benchmark**: Netflix and YouTube's recommendations are highly personalized. Amazon product recommendations are accurate due to collaborative filtering.

---

### Issue #4: AI Lacks Trust Signals; User Doesn't Know if It's Reliable
**Problem**: App doesn't explain how AI works, its limitations, or accuracy. User is skeptical.

**Framework Cite**:
- **Nielsen #1 (Visibility)**: User should know what the AI is and its limitations
- **Fogg Motivation**: Trust increases motivation to use AI
- **Cagan Value Risk**: Without trust signals, users assume AI is unreliable

**Evidence**: Look for disclaimers, confidence indicators, privacy notices about AI. What's missing?

**Quantified Impact**: Apps with clear AI trust signals see 2-3x higher AI feature usage. Apps without disclaimers see users avoiding AI.

**Hypothesis for Improvement**:
1. Add disclaimer: "AI-powered; may have errors. Use for reference, not as sole source."
2. Confidence display: Show "Highly confident" vs. "Low confidence" on AI outputs
3. Source attribution: "Based on X and Y sources"
4. Privacy: "Your chat is private and not used for training"
5. Error feedback: "Report error" button if AI gets something wrong

Estimated impact: 50-100% improvement in AI feature trust and usage.

**Comparative Benchmark**: ChatGPT explains that it can make mistakes. Medical AI apps show confidence scores. Both build user trust.

---

## SPEED MODE vs RIGOR MODE

### SPEED MODE (15 minutes)
1. Check if AI exists → Visible/hidden?
2. Test chat → Quality? Context-aware?
3. Check recommendations → Accurate or spam?
4. Check trust signals → Disclaimers/confidence?
5. Note 2 key issues
6. Assign score

**Output**: 1 page

---

### RIGOR MODE (30-45 minutes)
1. Full discoverability audit
2. Extensive chat testing (5+ queries)
3. Recommendation quality testing (10+ recommendations)
4. AI-within-content features testing
5. Trust and transparency review
6. Integration assessment
7. Full Evidence Checklist
8. 3-5 key issues
9. Detailed score

**Output**: 3-5 pages

---

## PERSONA-SPECIFIC INSTRUCTIONS

### 1. New User (First AI Encounter)
**Test**: Is AI feature obvious? Can new user use it without help?

**Key Metrics**: Discoverability, learning curve, first impression

**Scoring Focus**: Accessibility, guided introduction

### 2. Power User
**Test**: Can power user leverage AI for advanced tasks?

**Key Metrics**: Feature depth, customization, advanced capabilities

**Scoring Focus**: Feature richness, context-aware responses

---

## DOMAIN-SPECIFIC OVERLAYS

### Education Apps
- **Domain criteria**: Does AI coach understand user's learning level?
- **Scoring modifier**: +1 if AI adapts to difficulty; -1 if generic

### OTT/Streaming
- **Domain criteria**: Do AI recommendations match viewing history?
- **Scoring modifier**: +1 if AI recs are personalized; -1 if generic trending

---

## INDIA-SPECIFIC CHECKS

Every review of an Indian app must include these checks for this module:

### Hindi/Hinglish AI Chat
- [ ] Does AI chat understand Hindi input (Devanagari script)?
- [ ] Does AI chat understand Hinglish input (Roman script Hindi)?
- [ ] Does AI respond in the user's language preference (Hindi/English/Hinglish)?
- [ ] Is voice input to AI available? In Hindi?
- [ ] Does AI maintain context across language switches (user starts in Hindi, switches to English)?
- [ ] Impact if missing: 45-50% of Indian internet users prefer Hindi. An English-only AI feature excludes half the potential user base from the app's highest-value feature.

**Finding template:** "AI chat is English-only. Hindi input returns English responses or errors. No voice input available. No Hinglish understanding. This AI feature is inaccessible to 45-50% of Indian internet users."

**India Benchmark:** Google Assistant's Hindi adoption in India shows Hindi voice AI achieves 2x engagement of English-only. This is a first-mover opportunity in Indian EdTech — no strong Hindi AI tutor benchmark exists yet.

### AI Trust & Explanation in Hindi
- [ ] Is there a simple explanation of what AI does, in Hindi? ("Yeh aapka personal teacher hai")
- [ ] Is there a data privacy disclaimer in Hindi?
- [ ] Does the app address AI skepticism ("ye bot hai" / "this is just a bot")?
- [ ] Are AI-generated responses clearly labeled?
- [ ] Is there a "talk to human" fallback visible?
- [ ] Impact if missing: Indian users, especially Tier 2-3, have an AI trust deficit. Without explanation in their language, they won't use the feature. "AI" as a term is not universally understood.

**Finding template:** "No explanation of what AI does. No Hindi trust-building copy. No data privacy information in Hindi. No 'talk to human' option. Tier 2-3 users encountering AI without context will either ignore or distrust the feature."

**India Benchmark:** No strong Indian AI trust benchmark yet — this is a design opportunity. However, successful Indian chatbots (banking, customer service) always include "aap hamari team se baat kar sakte hain" (you can talk to our team) as a trust signal.

### AI for Non-Tech-Savvy Users
- [ ] Is the AI interface simple enough for first-time AI users?
- [ ] Is there a guided first interaction (suggested questions, example prompts)?
- [ ] Are suggested prompts in Hindi/Hinglish?
- [ ] Does AI avoid jargon in responses?
- [ ] Can the user interact via voice (not just typing)?
- [ ] Impact if missing: Most Tier 2-3 Indian users have never interacted with an AI chatbot. Without guided first interaction and Hindi prompts, they won't know what to do.

**Finding template:** "AI interface shows empty chat with 'Ask me anything' prompt in English. No suggested questions. No example interactions. No Hindi prompts. First-time AI users in Tier 2-3 India will stare at this screen and close it."

**India Benchmark:** Google Assistant's India launch used Hindi suggested queries and voice-first interaction — achieved 50M+ Hindi users. Voice-first AI reduces the barrier for non-tech-savvy users by 70%.

### Scoring Modifiers (India)
- +1 if AI chat works in Hindi/Hinglish
- +1 if voice input to AI is available
- +1 if AI trust explanation exists in Hindi
- +1 if guided first interaction with Hindi prompts
- -1 if AI is English-only
- -1 if no voice input option
- -2 if no trust explanation and no "talk to human" fallback
- -2 if AI uses technical jargon with no Hindi explanation

---

## OUTPUT FORMAT

```markdown
# AI INTEGRATION — [X]/10

## Evidence Summary

### AI Feature Availability
- **AI chat present**: [Yes / No]
- **Discoverability**: [Visible / Hidden / Requires discovery]
- **Prominence**: [X]/5

### Chat Quality
- **Response relevance**: [X]/5
- **Context awareness**: [App-aware / Generic]
- **Response time**: [X] seconds

### Recommendations
- **Accuracy**: [X]/5
- **Freshness**: [Variable / Same]
- **Personalization**: [Obvious / Generic]

### Trust
- **Disclaimers**: [Present / Absent]
- **Confidence display**: [Yes / No]
- **Privacy notice**: [Clear / Vague / Missing]

### Integration
- **Seamlessness**: [Integrated / Separate / Isolated]
- **Context awareness**: [High / Medium / Low]

---

[Detailed Evidence, Scoring Breakdown, Key Issues sections follow standard format]

**Review Conducted**: [Date] | **Reviewer**: [Name] | **Duration**: [Mode]
```

---

## Summary

This module evaluates AI integration—the modern engagement driver. It assesses whether AI features are discoverable, trustworthy, and actually useful. Grounded in JTBD (job accomplishment), HEART (task success), and Kano (attractive features), this module identifies whether AI is a delightful differentiator or an ignored gimmick.

