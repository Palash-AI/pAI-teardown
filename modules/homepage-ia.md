# Homepage & Information Architecture

> AARRR: Activation/Engagement | Frameworks: Nielsen, Norman, JTBD, Cagan Value Risk, Kano | Speed: 15min | Rigor: 45min

<!-- SPEED MODE -->
## QUICK AUDIT
Navigate: 1. Splash/Load 2. Primary Navigation 3. Content Grid 4. Header 5. Bottom Nav 6. Scroll Depth 7. Free/Locked Content. Check: Navigation clarity (recognition vs recall), scroll depth to key content, free vs locked visibility, visual hierarchy focal point. Score anchor: 9-10 = obvious hierarchy + intuitive nav + clear free/locked + <3 scroll, 7-8 = clear nav + logical org + visible free/locked + reasonable scroll, 5-6 = learnable nav + some confusion + ambiguous free/locked + deep scroll, 3-4 = confusing nav + illogical org + hidden free/locked + excessive scroll, 1-2 = broken nav + random org + blocked content + impossible scroll.
<!-- END SPEED MODE -->

## SCREENS TO NAVIGATE

### 1. App Splash / First Content Load
**Observe:**
- Load time until content visible (seconds)
- What visible above fold (top 380px mobile)
- Visual signifiers/section labels present
- Primary CTA or balanced browsing
- Color hierarchy and balance
- Personalization evident (personalized vs. generic)

**Screenshot:** Full homepage load state, zoomed top-fold area, loading states if present, initial recommendation/content

**Framework check:** Nielsen #1 (Visibility) → Is system status/app value clear? Nielsen #8 (Minimalism) → Aesthetic or cluttered? Cagan Value Risk → Value proposition visible without scroll?

---

### 2. Homepage Navigation Structure
**Observe:**
- Primary nav pattern: Bottom tabs / Side drawer / Top tabs / None
- Number of visible tabs/sections
- Category name clarity (self-explanatory or jargon)
- Active tab visually highlighted
- Easy section switching
- Home/back button present

**Screenshot:** Primary nav bar/drawer, zoomed nav labels and icons, before/after section switch, nav shown open/closed

**Framework check:** Nielsen #4 (Consistency) → Platform conventions? Nielsen #6 (Recognition) → Icon recognizability? Norman (Signifiers) → Do tabs signal function?

---

### 3. Homepage Category Grid / Content Organization
**Observe:**
- Content layout: Grid / List / Card stack / Carousel
- Items visible on first screen
- Category organization: Alphabetical / Popularity / Relevance / Hierarchical
- Visual hierarchy between categories
- Free vs. locked visibility
- Content preview: Thumbnail + title / Title only / Thumbnail only
- Scroll depth needed

**Screenshot:** Full content grid, zoomed content cards, carousel/grid with items, free vs. locked indicators, scroll-down view

**Framework check:** Nielsen #8 (Minimalism) → Every item necessary? Nielsen #6 (Recognition) → Scan and recognize without reading? JTBD (Locate) → Find content matching job? Kano → Clear org is Must-Be.

---

### 4. Header & Top-of-Page Elements
**Observe:**
- Header: Fixed / Sticky / Scrolls away / None
- Logo/branding size and recognizable
- Search: Always visible / Hidden / Floating / None
- Search bar: Full width / Icon / Placeholder visible
- Quick actions: Filter / Sort / Settings / Notifications
- Header clarity and clutter
- Back/home navigation visibility

**Screenshot:** Full screen with header, zoomed header elements, header scrolled vs. top, search focused, menu opened

**Framework check:** Nielsen #1 (Visibility) → Search accessible? Nielsen #8 (Minimalism) → All items necessary? Norman (Mapping) → Actions map logically?

---

### 5. Bottom Navigation Bar (if present)
**Observe:**
- Number of tabs (typically 3-5)
- Tab labels: Text only / Icons only / Icons + text
- Active tab indication: Color / Background / Underline / Other
- Tab alignment: Evenly spaced / Left-aligned / Centered
- Visibility: Always visible / Hidden on scroll
- Tap target size (accessible?)

**Screenshot:** Bottom nav clearly visible, zoomed all tab icons/labels, before/after tab switch, active vs. inactive state

**Framework check:** Nielsen #4 (Consistency) → Platform conventions? Nielsen #6 (Recognition) → Icons immediately recognizable? Norman (Affordances) → Buttons look tappable?

---

### 6. Scroll Behavior & Content Depth
**Observe:**
- Scroll direction: Vertical / Horizontal / Mixed
- Scroll stickiness (sections stick?)
- Infinite scroll vs. pagination
- Load time during scroll
- Scroll performance: Smooth or janky
- Back-to-top affordance present

**Screenshot:** Top of page, mid-scroll (50%), near bottom, loading indicators, back-to-top button if present

**Framework check:** Nielsen #1 (Visibility) → Loading state visible? Fogg Ability → Long scrolls reduce ability. Intentional?

---

### 7. Free vs. Locked Content Visibility
**Observe:**
- Locked content: Hidden / Shown with lock icon / Shown with "Premium" label
- Lock icon design clarity
- Preview of locked content: Full / Truncated / None
- User subscription status visible
- Upgrade path clear

**Screenshot:** Content card with lock, zoomed lock indicator, free vs. locked comparison, subscription status if visible

**Framework check:** Nielsen #1 (Visibility) → Free/premium split clear? Cagan Value Risk → Can free users see value or is premium so hidden it looks empty?

---

## SCORING RUBRIC

| Score | Label | Key Criteria |
|-------|-------|-------------|
| 9-10 | Best-in-class | Optimized for recognition, intuitive/consistent nav, logical content org, value visible above fold, no cognitive load, accessible, mobile-first, personalization signals visible |
| 7-8 | Good | Clear learnable nav, mostly logical org, free/locked visible, reasonable scroll depth <3, evident hierarchy, prominent nav, <2 sec load, minimal clutter |
| 5-6 | Adequate | Learnable nav (3-4 uses), partially confusing org, ambiguous free/locked, deep scroll (3+), weak hierarchy, nav present but not prominent, 2-4 sec load, moderate clutter |
| 3-4 | Poor | Confusing nav (hunting required), illogical org, hidden free/locked, excessive scroll (5+), no hierarchy, hard to find nav, 4+ sec load, significant clutter |
| 1-2 | Critical | Broken/absent nav, random org, blocked content, infinite scroll, no hierarchy, empty/broken homepage, 10+ sec load, severe clutter |

**Scoring method**: Start at 5 (baseline). Add: +2 intuitive nav, +1 clear hierarchy, +1 free/locked visible, +1 <3 scroll depth, +1 prominent nav, +1 <2 sec load, +1 personalization. Deduct: -2 confusing nav, -1 weak hierarchy, -1 hidden content, -1 >5 scroll, -2 no nav, -1 slow load, -1 generic content, -1 clutter. Cap at 1-10.

---

## EVIDENCE CHECKLIST

### Navigation Structure
- [ ] Primary nav type: [Bottom tabs / Side drawer / Top / None] — Nielsen #1, #4
- [ ] Number of primary nav items: [_____]
- [ ] Label clarity (1-5): [_____]
- [ ] Time to switch sections (taps): [_____]
- [ ] Navigation visibility: [Always / Hides / Sticky]
- [ ] Back/home navigation: [Yes / No]

### Homepage Content Organization
- [ ] Content layout type: [Grid / List / Cards / Carousel / Other]
- [ ] Items visible without scrolling: [_____]
- [ ] Distinct sections visible: [_____]
- [ ] Free vs. locked distinction: [Clear / Somewhat / Not clear]
- [ ] Content preview type: [Thumbnail + title / Title only / Thumbnail / Rich card]
- [ ] Scroll depth to see all categories: [_____] items or scrolls — Nielsen #6, #8, JTBD

### Header Elements
- [ ] Header type: [Fixed / Sticky / Scrolls / None]
- [ ] Logo/branding: [Yes / No]
- [ ] Search availability: [Always / In header / Floating / None]
- [ ] Number of actionable header items: [_____]
- [ ] Header visual weight (1-5): [_____] — Nielsen #1, Norman

### Free vs. Locked Content
- [ ] Percentage of visible locked content: [_____]%
- [ ] Lock indicator type: [Icon / Text label / Color / Grayed out / None]
- [ ] Lock indicator clarity (1-5): [_____]
- [ ] Preview for locked items: [Full / Partial / None]
- [ ] User subscription status visible: [Yes / No / Partial]
- [ ] Upgrade path clear: [Yes / No] — Cagan Value Risk, Nielsen #1

### Visual Design & Hierarchy
- [ ] Primary focal point: [_____]
- [ ] Hierarchy clarity (1-5): [_____]
- [ ] Color usage: [Consistent / Chaotic / Minimal / Rich]
- [ ] Typography hierarchy: [Yes / No]
- [ ] Spacing rhythm: [Yes / No / Inconsistent]
- [ ] Visual clutter (1-5, 5=cluttered): [_____] — Nielsen #8, Norman

### Loading & Performance
- [ ] Time to homepage visible: [_____] seconds
- [ ] Content fully loaded before interactive: [Yes / No]
- [ ] Skeleton screens/loading states: [Yes / No]
- [ ] Scroll performance: [Smooth / Occasional lag / Stuttering]
- [ ] Infinite scroll or pagination: [Infinite / Paginated / Both] — Nielsen #1, Fogg Ability

### Personalization Signals
- [ ] Personalized content visible: [Yes / No]
- [ ] "For You" section present: [Yes / No]
- [ ] Recommendation engine evident: [Yes / No]
- [ ] User profile visibility: [Visible / Hidden / N/A] — HEART, Reforge

---

## KEY ISSUE PATTERNS

1. **Confusing Navigation** → Detect: Users cannot find major sections; unclear/random labels. Nielsen #1, #6, Norman. Fix: Simplify to 4-5 primary sections, use action-oriented labels, matching icons, test with 5-10 users.

2. **Premium Content Blocks Free Tier** → Detect: 80%+ locked, free tier appears empty. Cagan Value Risk, Fogg MAP, AARRR. Fix: 40-50% free content, show popular free first, small lock icon (not hidden), make free genuinely useful.

3. **Excessive Scroll Depth** → Detect: Key categories 5+ scrolls down, 50+ items. Nielsen #8, JTBD, Fogg Ability. Fix: Organize by popularity/relevance, use horizontal carousel, pagination with "See all", smart defaults.

4. **Unclear Visual Hierarchy** → Detect: 10+ sections with equal weight, no focal point. Nielsen #1, #8, Norman. Fix: Primary (large, top), secondary (medium), tertiary (small, bottom); strategic color; test user mental model.

5. **Free vs. Locked Completely Unclear** → Detect: Cannot tell which content is free without tapping each; no visual distinction. Nielsen #1, #6, Cagan Value Risk. Fix: Small clear lock icon, "Premium" badge, or color distinction; test clarity with 5 users.

---

## OUTPUT FORMAT

```markdown
# HOMEPAGE & INFORMATION ARCHITECTURE — [X]/10

## Evidence Summary
- **Primary navigation type**: [Bottom tabs / Side / Other]
- **Sections visible**: [X]
- **Navigation clarity**: [X]/5
- **Scroll depth to all categories**: [X] scrolls
- **Free vs. locked visibility**: [Clear / Ambiguous / Hidden]

## Key Metrics
- **Load time to homepage visible**: [X] seconds
- **Personalization signals**: [Yes / No]
- **Visual hierarchy clarity**: [X]/5

## Frameworks Applied
- **Nielsen**: Visibility, recognition, minimalism, consistency
- **Norman**: Signifiers, affordances, mapping, feedback
- **JTBD**: Locate step evaluated
- **Cagan Value Risk**: Value visibility assessed

## Scoring Breakdown

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Navigation intuitiveness | [X]/10 | [Primary nav is clear/confusing], [X] taps to switch |
| Visual hierarchy | [X]/10 | [Focal point identified / No clear focal point] |
| Free/locked clarity | [X]/10 | [Clearly marked / Ambiguous / Hidden] |
| Content organization | [X]/10 | [Logical / Somewhat / Confusing] |
| Scroll depth | [X]/10 | [X] scrolls to see all categories |
| Load performance | [X]/10 | [X] seconds to visible |
| Personalization | [X]/10 | [Evident / Not visible] |
| Design quality | [X]/10 | [Professional / Adequate / Generic] |

**Total Score: [X]/10** | **Justification**: [1-2 sentences grounded in frameworks]

## Key Issues

### Issue #1: [Title]
**Problem**: [Observed] | **Framework**: [Nielsen/Norman/JTBD/Cagan] | **Impact**: [User % affected, engagement impact] | **Fix**: [Specific hypothesis]

### Issue #2: [Title]
[Same structure]

### Issue #3: [Title]
[Same structure]

## Recommendations

### P0 (Critical)
[Issues affecting navigation or value clarity]

### P1 (High)
[Issues affecting content discovery or engagement]

**Review Conducted**: [Date] | **Duration**: [Speed / Rigor / Hybrid]
```
