# Content Consumption Experience

> AARRR: Engagement | Frameworks: JTBD (Execute, Monitor), Hook (Variable Reward), HEART (Engagement), Norman, Nielsen | Speed: 20min | Rigor: 60min

<!-- SPEED MODE -->
## QUICK AUDIT
Navigate: 1. Content Detail Page 2. Player Interface 3. Progress & Resume 4. Series Navigation 5. Accessibility (Captions) 6. Next Content Suggestions 7. Completion & Sharing
Check: Player stability (crashes/lag?), controls available (speed/quality/captions), progress tracking (visible/resume works), series nav (can find next?), autoplay/suggestions present, completion flow
Score anchor: 9-10 = smooth player + comprehensive controls + seamless resume + clear series nav + autoplay + celebration, 7-8 = usable player + good controls + resume usually works + clear series nav + suggestions, 5-6 = basic player + limited controls + resume unreliable + series confusing + generic suggestions, 3-4 = frustrating player + minimal controls + no resume + broken series nav + no suggestions, 1-2 = player crashes/broken + no controls + resume lost + series impossible + no next content
<!-- END SPEED MODE -->

## SCREENS TO NAVIGATE

### 1. Content Detail Page
**Observe:**
- Metadata visible (title, description, duration, author, rating, reviews)
- Series/playlist context (position in sequence shown?)
- Social proof signals (ratings, views, reviews count)
- Preview available or teaser shown?
- CTA clarity (Play/Start/Read button obvious?)

**Screenshot:** Full detail page, metadata section, series indicator, ratings/reviews, CTA button

**Framework check:** Nielsen #1 → Can user identify what this content is about and why they should consume it?

---

### 2. Player Interface
**Observe:**
- Player type (video/audio/text/interactive)
- Control placement (bottom overlay, always visible, hidden on idle)
- Available playback options: Play/pause, seek, speed, quality, captions, fullscreen
- Control intuitiveness (obvious or confusing?)
- Player stability (crashes, lag, buffering?)

**Screenshot:** Player in playing state, controls visible, full-screen view, any error states

**Framework check:** Norman (Affordances) + Nielsen #1 → Do controls signal their function? Can user control playback easily?

---

### 3. Progress Tracking & Resume
**Observe:**
- Progress indicator visible (timeline, percentage, or hidden?)
- Resume functionality (works seamlessly, broken, or missing?)
- Resume UX (automatic suggestion or manual selection?)
- Completion tracked (yes/no)
- Cross-device sync (tested or not applicable?)

**Screenshot:** Content in-progress with progress indicator, resume suggestion on next visit, progress in watch history

**Framework check:** Hook (Investment) + JTBD (Monitor) → Does progress save preserve user investment and enable them to monitor consumption?

---

### 4. Series/Playlist Navigation
**Observe:**
- Series structure visible (all episodes listed, unclear, or not applicable?)
- Episode numbering clarity (Episode 1 of 10 or unclear?)
- Watched indicator (can you see which episodes completed?)
- Next/previous controls obvious or hard to find?
- Autoplay next present, absent, or can be disabled?

**Screenshot:** Series/playlist list with episodes, current position highlighted, next/previous controls, autoplay toggle if present

**Framework check:** Norman (Mapping) → Does "next" button clearly lead to next in sequence? Can user navigate smoothly?

---

### 5. Accessibility & Metadata
**Observe:**
- Subtitle/caption availability (multiple languages, English only, or none?)
- Regional language support (Hindi, Tamil, Marathi, etc. for India context?)
- Transcript available (for podcasts/audio?)
- Duration always visible, must tap, or not shown?
- Download/offline option available?
- Sharing options (WhatsApp, Instagram, email, link copy, or none?)

**Screenshot:** Subtitle toggle/options, transcript view if available, download button, sharing menu

**Framework check:** Nielsen #10 + Fogg (Ability) → Do accessibility features enable users (non-native speakers, low connectivity, accessibility needs)?

---

### 6. Next Content Suggestions
**Observe:**
- Next episode suggestion shown before/after completion or not shown?
- "Up next" queue visible?
- Personalization evidence (personalized vs. generic trending?)
- Autoplay default (on/off)
- Can user customize queue?

**Screenshot:** "Up next" or next episode suggestion, completion screen with recommendations, autoplay countdown if present

**Framework check:** Hook (Variable Reward) + HEART (Engagement) → Does next content suggestion create seamless reward loop?

---

### 7. Completion & Sharing
**Observe:**
- Completion acknowledgment (celebration screen, silent, or not tracked?)
- Achievement recognized and visible?
- Sharing option at completion (easy or hidden?)
- Certificate/badge issued (for education apps)?
- Rating prompt shown (on completion, after X uses, or never?)
- Post-completion suggestion (next content auto-suggested or user must search?)

**Screenshot:** Completion screen with celebration/acknowledgment, sharing options, certificate/badge if issued, rating prompt

**Framework check:** Hook (Investment & Variable Reward) + AARRR (Referral) + HEART (Happiness) → Does completion flow celebrate achievement and enable sharing?

---

## SCORING RUBRIC

| Score | Label | Key Criteria |
|-------|-------|-------------|
| 9-10 | Best-in-class | Smooth player (no crashes), comprehensive controls (speed/quality/captions), seamless resume, clear series nav, autoplay works, celebration on completion, regional language support, offline download available |
| 7-8 | Good | Usable player (occasional lag), good controls (speed, quality, captions), resume usually works, clear series nav, suggestions present, completion acknowledged, some language support |
| 5-6 | Adequate | Basic player (minor friction), limited controls (maybe speed or captions missing), resume unreliable, series navigation requires work, generic suggestions, silent completion, English captions only |
| 3-4 | Poor | Frustrating player (frequent crashes), minimal controls (play/pause only), no resume, series structure confusing, no suggestions, no completion acknowledgment, no captions |
| 1-2 | Critical | Player broken/crashes constantly, no controls, resume impossible, series navigation impossible, no next content, no sharing, heavy buffering |

**Scoring method**: Start at 5. Add: +2 for smooth player, +1 comprehensive controls, +1 seamless resume, +1 clear series nav, +1 autoplay/suggestions, +1 celebration, +1 regional language captions, +1 offline download. Deduct: -2 for crashes, -1 limited controls, -1 resume broken, -1 series confusing, -1 no suggestions. Cap at 1-10.

---

## EVIDENCE CHECKLIST

### Timing & Interaction
- [ ] Time to start playing (seconds) — Framework: Nielsen #1
- [ ] Player response time (immediate, slight delay, slow) — Framework: Norman (Feedback)
- [ ] Seek responsiveness (instant, slight delay, slow) — Framework: Norman (Feedback)
- [ ] Buffering observed (none, occasional, frequent) — Framework: Fogg (Ability)

### Player Controls
- [ ] Playback options available (Play/pause, seek, speed, quality, captions, fullscreen) — Framework: Nielsen #3, Norman
- [ ] Control intuitiveness (1-5 scale) — Framework: Norman (Affordances)
- [ ] Player stability (crashes, lag observed) — Framework: Fogg (Ability)

### Progress Tracking
- [ ] Progress indicator visible (timeline, percentage, circular, hidden) — Framework: JTBD (Monitor)
- [ ] Resume works (seamless, broken, not available) — Framework: Hook (Investment)
- [ ] Resume UX (automatic suggestion, manual, not available) — Framework: JTBD (Monitor)
- [ ] Cross-device sync (tested, not available, not tested) — Framework: Hook (Investment)

### Series Navigation
- [ ] Series structure clarity (clear list, unclear, not applicable) — Framework: Norman (Mapping)
- [ ] Episode numbering (clear: Ep 1/10, unclear) — Framework: Nielsen #1
- [ ] Watched indicator (visible, hidden, not applicable) — Framework: Norman (Feedback)
- [ ] Steps to next episode — Framework: Fogg (Ability)
- [ ] Autoplay present (yes, can disable, no) — Framework: Hook (Variable Reward)

### Accessibility
- [ ] Subtitle/caption availability (multiple languages, English, none) — Framework: Nielsen #10
- [ ] Regional language support (Hindi/Tamil/Marathi, English only, none) — Framework: Fogg (Ability)
- [ ] Transcript available (yes/no/not applicable) — Framework: Nielsen #10
- [ ] Download/offline option (yes, no, limited) — Framework: Fogg (Ability)
- [ ] Sharing options (WhatsApp, Instagram, email, link, none) — Framework: AARRR (Referral)

### Next Content & Engagement
- [ ] Next content suggestion timing (before completion, after, never) — Framework: Hook (Variable Reward)
- [ ] Suggestion relevance (1-5 scale) — Framework: HEART (Engagement)
- [ ] Personalization evidence (personalized, generic, random) — Framework: JTBD (Monitor)
- [ ] User ability to customize queue (yes/no) — Framework: Fogg (Ability)

### Completion Experience
- [ ] Completion acknowledgment (celebration, silent, not tracked) — Framework: Hook (Investment)
- [ ] Achievement tracked and visible (yes, hidden, no) — Framework: HEART (Happiness)
- [ ] Sharing option at completion (prominent, hidden, none) — Framework: AARRR (Referral)
- [ ] Rating prompt timing (on completion, after X uses, never) — Framework: HEART (Happiness)

---

## KEY ISSUE PATTERNS

1. **Player Crashes or High Friction** → Detect: App freezes, crashes, or frequent lag during playback. Framework: Fogg, HEART. Fix: Upgrade player library, test 50+ content items, implement auto-recovery.

2. **Limited Playback Controls** → Detect: No speed adjustment, quality selection, or captions available. Framework: Nielsen #3, Fogg. Fix: Add speed (0.75x-2x), quality tiers (480p-1080p), regional language captions.

3. **Resume Broken or Missing** → Detect: Progress not saved; user must restart from beginning. Framework: Hook (Investment), JTBD. Fix: Save timestamp real-time, offer "Continue watching" on next open, sync cross-device.

4. **Series Navigation Confusing** → Detect: Hard to find next episode; no episode numbering or watched tracking. Framework: Norman (Mapping), JTBD. Fix: Show all episodes with current highlighted, clear numbering (Ep X of Y), watched indicators.

5. **No Captions or Language Gaps** → Detect: No subtitles or English-only; non-native speakers blocked. Framework: Nielsen #10, Fogg. Fix: Auto-generate captions, add Hindi + regional languages, make toggleable.

6. **No Next Content Suggestion** → Detect: After finishing, no autoplay or suggestion; user must manually search. Framework: Hook (Variable Reward), HEART. Fix: Autoplay next episode in series, show "You might also like" queue, one-tap play.

7. **Completion Silent or Not Celebrated** → Detect: Finishing content triggers no feedback or acknowledgment. Framework: Hook (Investment), HEART. Fix: Show celebration screen, track achievement, offer sharing option.

8. **No Offline Support** → Detect: Content requires internet to watch; low-connectivity users blocked. Framework: Fogg (Ability). Fix: Enable download with quality options, reliable offline playback.

---

## OUTPUT FORMAT

```markdown
# CONTENT CONSUMPTION EXPERIENCE — [X]/10

## Evidence Summary
- **Player quality**: [Smooth / Occasional lag / Crashes]
- **Controls available**: [Comprehensive / Good / Limited / Minimal]
- **Resume functionality**: [Works seamlessly / Usually works / Broken / Not available]
- **Series navigation**: [Clear / Requires work / Confusing / Not applicable]
- **Next content suggestion**: [Autoplay + personalized / Generic / Not present]
- **Captions**: [Multiple languages / English / None]
- **Completion experience**: [Celebration + sharing / Acknowledged / Silent]

## Key Metrics
- **Engagement confidence**: [High / Medium / Low]
- **Friction points**: [0-1 minor / 2-3 moderate / 4+ severe]

## Frameworks Applied
- **JTBD**: [Execute and Monitor steps — can user consume and track progress?]
- **Hook**: [Variable Reward cycle — seamless next content → continued consumption?]
- **HEART Engagement**: [Session length, completion rate assessment]
- **Norman**: [Affordances, feedback, mapping in player UI]
- **Fogg**: [Ability friction — controls, resume, navigation]

## Scoring Breakdown

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Player stability | [X]/10 | [Smooth / Occasional lag / Crashes] |
| Playback controls | [X]/10 | [Comprehensive / Good / Limited] |
| Resume functionality | [X]/10 | [Seamless / Works usually / Broken] |
| Series navigation | [X]/10 | [Clear / Requires work / Confusing] |
| Accessibility (captions) | [X]/10 | [Multiple languages / English / None] |
| Next content suggestions | [X]/10 | [Autoplay works / Generic / Missing] |
| Completion experience | [X]/10 | [Celebrated / Acknowledged / Silent] |

**Total Score: [X]/10** | **Justification**: [1-2 sentences on primary friction vs. strengths]

## Key Issues

### Issue #1: [Title]
**Problem**: [What observed] | **Framework**: [Name] | **Impact**: [Conversion/retention %] | **Hypothesis**: [1-line fix]

### Issue #2: [Title]
[Same format]

### Issue #3: [Title]
[Same format]

## Recommendations

### P0 (Critical)
[Issues affecting >50% of users or blocking smooth consumption]

### P1 (High)
[Issues affecting 20-50% of users]

### P2 (Medium)
[Issues affecting <20% of users]

**Review Conducted**: [Date] | **Duration**: [Speed / Rigor / Hybrid]
```
