# AI Integration

> AARRR: Engagement/Retention | Frameworks: JTBD, HEART, Kano, Norman, Hook Model, Nielsen | Speed: 15min | Rigor: 45min

<!-- SPEED MODE -->
## QUICK AUDIT
Navigate: 1. AI chat/coach entry point 2. Chat interface (test a query) 3. AI recommendations section 4. AI-within-content features 5. Trust/disclaimer signals 6. App integration context
Check: AI discoverable without digging, chat response is context-aware (not generic), recommendations relevant/fresh, disclaimers/confidence signals present
Score anchor: 9-10 = visible + context-aware + fresh recs + trust signals + seamless integration, 7-8 = findable + mostly relevant + some trust, 5-6 = exists but generic AI + weak integration, 3-4 = hidden or broken, 1-2 = misleading/harmful/non-functional
<!-- END SPEED MODE -->

## SCREENS TO NAVIGATE

### 1. AI Feature Discoverability
**Observe:**
- AI chat/coach location: floating button / dedicated tab / hidden in menu / absent
- Prominence: always visible / revealed after X interactions / hidden initially
- Label clarity: "AI Coach" / "Chat" / ambiguous icon only
- Onboarding mention: explained during setup or user must discover?
- Icon quality: signals AI (⚡) or just chat (💬)?

**Screenshot:** Full screen showing AI entry point location; zoomed view of button/tab

**Framework check:** Nielsen #1 + Hook External Trigger → Is AI visible? Does the app prompt users to try it?

---

### 2. AI Chat Interface & Quality
**Observe:**
- Input: text only / voice / suggested prompts on open
- Response relevance (1-5): does AI know the app's content or respond generically?
- Response time: <1s / 1-3s / >3s
- Context awareness: gives app-specific help vs. generic advice
- Conversation history saved or lost on close
- Error handling: clarification request or dead-end?

**Screenshot:** Chat on first open (suggested prompts if present); sample query + response; error state if AI misunderstands

**Framework check:** JTBD + HEART Task Success → Does AI help accomplish the user's job? Does it know the app context?

---

### 3. AI Recommendations
**Observe:**
- Visible and labeled as AI? ("AI picked for you" / unlabeled / absent)
- Accuracy (1-5): relevant to user history and interests?
- Freshness: different each visit or same items repeated?
- User feedback option: can rate helpful/unhelpful?
- Explanation: "Based on your history" / "Trending" / no label

**Screenshot:** AI recommendations section; individual rec with explanation label; feedback option if present

**Framework check:** Hook Variable Reward + JTBD Locate → Do recs deliver fresh discovery? Do they help find relevant content?

---

### 4. AI-Within-Content Features
**Observe:**
- AI summaries or key highlights available?
- AI-generated quizzes or assessments?
- Transcript (AI or human-made)?
- AI-powered search within content?
- Accessibility: features always visible or require tapping?

**Screenshot:** AI summary section; AI highlights or quiz if present; transcript source label

**Framework check:** JTBD Execute + HEART Task Success → Do embedded AI features help the user do the job better?

---

### 5. AI Trust & Transparency
**Observe:**
- Disclaimer: "AI may be inaccurate" / vague / absent
- Confidence indicator shown?
- Source attribution: "Based on content X" / none
- Privacy notice: user told if chat is logged or used for training?
- Error reporting: can user flag bad AI output?

**Screenshot:** Any disclaimer/trust indicator; privacy notice; confidence display; feedback/report mechanism

**Framework check:** Nielsen #1 + Fogg Motivation → Does transparency build trust and motivation to use AI?

---

### 6. AI Integration with Core App
**Observe:**
- Context-awareness: does AI know what content user is currently viewing?
- Smart suggestions: does AI proactively surface next steps?
- Workflow disruption (1-5, 5 = very disruptive): seamless or isolated feature?
- AI surfaced at relevant moments or always hidden?

**Screenshot:** AI in context (e.g., chat while viewing content); smart suggestion based on current screen

**Framework check:** JTBD Execute + Fogg Ability + Hook → Does integration reduce friction? Does seamlessness strengthen the hook?

---

## SCORING RUBRIC

| Score | Label | Key Criteria |
|-------|-------|-------------|
| 9-10 | Best-in-class | Visible + context-aware chat + accurate labeled recs + trust signals + seamless integration + content features (summaries/quizzes) + user feedback loop |
| 7-8 | Good | Findable + mostly context-aware + recs mostly relevant + some trust signals + moderately integrated + some content features |
| 5-6 | Adequate | Present but generic AI + recs are trending-only + minimal trust signals + isolated feature + few content features |
| 3-4 | Poor | Hidden or hard to find + generic/slow chat + irrelevant recs + no trust signals + disconnected from app content |
| 1-2 | Critical | Broken/crashing + misleading outputs + no privacy disclosure + dark pattern data collection |

**Scoring method:** Start at 5. Add: +1 AI prominently discoverable, +1 chat is context-aware, +1 recs relevant and fresh, +1 trust signals/disclaimer present, +1 seamlessly integrated, +1 AI-within-content features present, +1 user feedback mechanism. Deduct: -2 AI completely hidden, -2 chat is generic/broken, -1 recs are irrelevant spam, -1 no disclaimers, -1 privacy violation. Cap at 1-10.

---

## EVIDENCE CHECKLIST

### Discoverability
- [ ] AI feature present: [Yes / No]
- [ ] Location: [Floating button / Tab / Menu / Hidden]
- [ ] Prominence (1-5): [_____]
- [ ] Label clarity: [Clear "AI" / Ambiguous / No label]
- [ ] Onboarding mention: [Yes / No]

**Framework:** Nielsen #1, Norman (Signifiers)

### Chat Quality
- [ ] Chatbot present: [Yes / No]
- [ ] Suggested prompts on open: [Yes / No]
- [ ] Sample query tested + response documented
- [ ] Response relevance (1-5): [_____]
- [ ] Context awareness: [App-aware / Generic AI]
- [ ] Response time: [<1s / 1-3s / >3s]
- [ ] Conversation history: [Saved / Lost on close]
- [ ] Error handling: [Clarifies / Dead-end]

**Framework:** JTBD, HEART (Task Success), Norman

### AI Recommendations
- [ ] Present and AI-labeled: [Yes / Unlabeled / Absent]
- [ ] Accuracy (1-5): [_____]
- [ ] Freshness: [Variable / Same items]
- [ ] Explanation label: [Yes / No]
- [ ] User feedback option: [Yes / No]

**Framework:** Hook (Variable Reward), JTBD (Locate)

### AI-Within-Content
- [ ] Summaries: [Yes / No]
- [ ] Highlights: [Yes / No]
- [ ] Quiz generation: [Yes / No]
- [ ] Transcript: [AI / Human / Absent]
- [ ] AI search: [Yes / No]
- [ ] Feature quality (1-5): [_____]

**Framework:** JTBD (Execute), HEART (Task Success)

### Trust & Transparency
- [ ] Disclaimer: [Explicit / Implicit / Absent]
- [ ] Confidence display: [Yes / No]
- [ ] Source attribution: [Yes / Partial / No]
- [ ] Privacy notice: [Explicit / Vague / Absent]
- [ ] Error reporting: [Yes / No]

**Framework:** Nielsen #1 (Visibility), Fogg (Motivation)

### Integration
- [ ] Integration level: [Seamless / Separate feature / Isolated]
- [ ] Context awareness: [App-aware / Generic]
- [ ] Smart suggestions: [Proactive / User-initiated / Absent]
- [ ] Workflow disruption (1-5): [_____]

**Framework:** JTBD (Execute), Fogg (Ability)

---

## KEY ISSUE PATTERNS

1. **Hidden AI Feature** → Detect: AI chatbot exists but buried in menu; usage typically <10%. Framework: Nielsen #1, Hook (Trigger). Fix: Add floating chat button; mention AI in onboarding; surface contextual "Try AI" prompt at relevant moments.

2. **Generic Chat (App-Unaware)** → Detect: Ask AI a question specific to current content; it responds with generic internet advice. Framework: JTBD, HEART Task Success. Fix: Feed AI the app content library; pass user's current screen context with every query.

3. **Inaccurate or Spam Recommendations** → Detect: AI-labeled recs have no relationship to user history; CTR <5%. Framework: Kano (Reverse), JTBD Locate. Fix: Collaborative filtering + content-based signals; add "helpful?" feedback to train algorithm; show confidence threshold.

4. **No Trust Signals** → Detect: No disclaimer, no confidence indicator, no privacy notice anywhere in AI flows. Framework: Nielsen #1, Fogg Motivation. Fix: Add "AI-powered; may have errors" note; show confidence level; disclose whether chat is private or used for training.

---

## OUTPUT FORMAT

```markdown
# AI INTEGRATION — [X]/10

## Evidence Summary
- **AI feature present**: [Yes / No] | **Location**: [Visible / Hidden]
- **Chat context-awareness**: [App-aware / Generic] | **Response time**: [X]s
- **Recommendation accuracy**: [X]/5 | **Freshness**: [Variable / Same]
- **Trust signals**: [Disclaimer / Confidence / Privacy: present or absent]
- **Integration level**: [Seamless / Separate / Isolated]

## Frameworks Applied
- **JTBD**: [Does AI serve user's job?]
- **HEART Task Success**: [Does AI help complete tasks?]
- **Hook Variable Reward**: [Are recs fresh and surprising?]
- **Kano**: [Delightful differentiator or ignored gimmick?]

## Scoring Breakdown

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Discoverability | [X]/10 | [Location and prominence] |
| Chat quality | [X]/10 | [Context-aware / Generic; relevance score] |
| Recommendations | [X]/10 | [Accuracy, freshness, labeling] |
| In-content features | [X]/10 | [What's present] |
| Trust & transparency | [X]/10 | [Disclaimer, privacy, confidence] |
| App integration | [X]/10 | [Seamless / Isolated] |

**Total Score: [X]/10** | **Justification**: [1-2 sentences]

## Key Issues

### Issue #1: [Title]
**Problem**: [Observed] | **Framework**: [Name] | **Impact**: [User %] | **Hypothesis**: [1-line fix]

## Recommendations

### P0 (Critical)
[Activation blockers or affecting >50% of users]

### P1 (High)
[20-50% of users; retention drivers]

**Review Conducted**: [Date] | **Duration**: [Speed / Rigor]
```
