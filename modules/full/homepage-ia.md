# Homepage & Information Architecture Module

## MODULE OVERVIEW

### What This Module Reviews
This module evaluates the homepage, navigation structure, and overall information architecture (IA) of the app. It assesses how clearly the app presents its core content, how intuitive navigation is, and whether users can recognize (vs. recall) key features and sections without friction.

**Scope**: From first content screen → all major navigation patterns, category organization, content hierarchy, and visual signaling.

### AARRR Stage Mapping
**Activation/Engagement** — The stage where users discover the app's breadth and depth. This module directly impacts:
- Feature discoverability and first-time understanding
- Time to accessing core content or features
- Navigation confidence and reduce friction for second/third actions
- Perception of content variety and personalization depth

### Design Skill Integration (Mandatory for Screenshots)

> **`design:critique`** — Run on homepage screenshots. Evaluate: first impression (what draws the eye first — is it the right element?), navigation usability (can user find core content?), visual hierarchy (above-fold priority), consistency (section spacing, card design), and accessibility (touch targets, contrast). For India context: does the homepage work on a 5.5" 720p budget screen? Are visual categories scannable at arm's length?

> **`design:ux-copy`** — Run on all homepage copy. Evaluate: section labels (clear, specific vs vague), CTA labels on homepage cards, empty state messaging if content hasn't loaded. For India context: are labels in Hindi/Hinglish? Is "Trending" translated or culturally adapted? Does social proof copy resonate ("10,000 people in your city" > "1M users globally")?

### Primary Frameworks & Models

| Framework | Application |
|-----------|-------------|
| **Nielsen's 10 Usability Heuristics** | #1 (Visibility), #6 (Recognition vs. Recall), #8 (Aesthetic/Minimalist), #4 (Consistency) |
| **Don Norman's Design Principles** | Signifiers, affordances, mapping, constraints, feedback |
| **HEART (Task Success)** | Can users complete their first navigation-dependent task? |
| **Kano Model** | Clear navigation is "Must-Be"; graceful hierarchy is "One-Dimensional" |
| **JTBD (Locate Step)** | Can users find what they came for without confusion? |
| **Cagan's Value Risk** | Is the value proposition visible on the homepage, or hidden 3 taps deep? |

---

## SCREENS TO NAVIGATE

### 1. App Splash / First Content Load
**Purpose**: Understand the first impression and what content is visible above the fold.

**What to Observe**:
- Load time until content is visible (not skeleton screens, actual content)
- What is visible above the fold (top 380px on typical mobile)
- Are there visual signifiers or labels for sections visible?
- Is there a primary CTA, or is the screen balanced for browsing?
- Color hierarchy and visual balance
- Is personalization evident (personalized content vs. generic default)?

**India-Specific Observations:**
- Does the homepage load fast on 4G with 3-4 bars? Is there a skeleton loader or blank screen?
- Are images lazy-loaded or does the whole page block until images render?
- Is there a Hindi/English language toggle accessible from homepage?
- Is the homepage browse-friendly (visual cards/grids) or search-dependent (empty state)?
- Is there a "Popular in [City]" or "Trending in Hindi" section visible?

**What to Screenshot**:
- Full screen view of homepage load state
- Zoomed view of top-fold area (what users see without scrolling)
- Any loading states or skeleton screens
- Initial recommendation/content if visible

**What to Document**:
- Time from app open to content visible (seconds)
- Number of distinct sections visible above fold
- Clarity of what each section contains (1-5 scale)
- Presence of primary CTA or hero content
- Whether content is personalized or generic

**Framework Checkpoints**:
- **Nielsen #1**: Is the system status visible (what is this app showing me)?
- **Nielsen #8**: Is the screen aesthetic and minimalist, or cluttered?
- **Cagan Value Risk**: Can the user understand the app's value proposition from this screen alone?

---

### 2. Homepage Navigation Structure
**Purpose**: Understand how the app structures its primary navigation and category hierarchy.

**What to Observe**:
- Primary navigation pattern: Bottom tab bar / Side drawer / Top tab bar / None (scrollable list)
- How many tabs/sections are visible in primary nav?
- Are category names self-explanatory or jargon-heavy?
- Is the active tab/section visually highlighted?
- Can user easily switch between sections?
- Is there a home/back button or consistent return point?

**What to Screenshot**:
- Full screen view showing primary navigation bar/drawer
- Zoomed view of navigation labels and icons
- Before/after screenshot when switching between two sections
- Hidden navigation (if in side drawer) shown open and closed

**What to Document**:
- Navigation type and location (bottom, top, side, etc.)
- Number of top-level tabs/sections
- Label clarity for each tab (self-explanatory or confusing?)
- Icon quality and recognizability
- Time to switch between major sections (taps required)

**Framework Checkpoints**:
- **Nielsen #4**: Consistency and standards — do tabs match platform conventions?
- **Nielsen #6**: Recognition — can users recognize which tab they're in without being told?
- **Norman's Signifiers**: Are tab icons + labels sufficient to signal function?

---

### 3. Homepage Category Grid / Content Organization
**Purpose**: Understand how content is organized, categorized, and presented for browsing.

**What to Observe**:
- Content layout: Grid / List / Card stack / Carousel
- How many items visible on first screen?
- Category organization: Alphabetical / By popularity / By relevance / Hierarchical
- Is there visual hierarchy between categories (size, color, prominence)?
- Free vs. locked content visibility (are locked items grayed out or hidden?)
- Content preview: Thumbnail + title / Title only / Thumbnail only
- Scroll depth: How many items before user must scroll?

**What to Screenshot**:
- Full screen view of category/content grid
- Zoomed view of individual content cards (to assess thumbnail quality, text clarity)
- Carousel or grid with multiple items visible
- Any visual indicators of free vs. locked content
- Scroll-down view showing secondary content

**What to Document**:
- Number of content items visible without scroll
- Estimated scroll depth to see all categories (in items or pixels)
- Category naming clarity (1-5 scale)
- Visual distinction between free/locked content (clear / somewhat clear / not clear)
- Thumbnail quality (professional, low-res, missing)
- Information density on each card (1-5 scale: minimal to dense)

**Framework Checkpoints**:
- **Nielsen #8**: Aesthetic and minimalist design — is every item necessary, or is there clutter?
- **Nielsen #6**: Recognition — can users scan and recognize what they want without reading everything?
- **JTBD Locate**: Can users find content matching their job without extensive searching?
- **Kano**: Clear category organization is Must-Be; smart sorting is One-Dimensional.

---

### 4. Header & Top-of-Page Elements
**Purpose**: Assess the app's header, search, and quick-access elements.

**What to Observe**:
- Header style: Fixed / Sticky / Scrolls away / None
- Logo/branding: Size, placement, recognizable
- Search: Always visible / Hidden in header / Floating button / No search
- Search bar design: Full width / Icon only / Text placeholder visible
- Quick actions in header: Filter / Sort / Settings / Notifications / None
- Header clarity: Does it clutter the screen or complement it?
- Back/home navigation: Clear and present or hidden?

**What to Screenshot**:
- Full screen with header visible
- Zoomed view of header and its elements
- Header state when scrolled down (if sticky) vs. top of page
- Search bar focused (if present) showing any hints or suggestions
- Header opened (if menu-based)

**What to Document**:
- Header type and stickiness
- Number of actionable items in header
- Search prominence (1-5 scale: invisible to prominently featured)
- Logo/branding clarity (recognizable / generic)
- Header visual weight (1-5 scale: minimal to dominant)

**Framework Checkpoints**:
- **Nielsen #1**: System visibility — is search visible and accessible?
- **Nielsen #8**: Minimalism — are all header items necessary?
- **Norman's Mapping**: Do header actions map logically to their placement?

---

### 5. Bottom Navigation Bar (if present)
**Purpose**: Assess the primary navigation hub and tab clarity.

**What to Observe**:
- Number of tabs in bottom nav (typically 3-5)
- Tab labels: Text only / Icons only / Icons + text
- Active tab indication: Color change / Background / Underline / Other
- Tab alignment: Evenly spaced / Left-aligned / Centered
- Visibility: Always visible / Hidden on scroll
- Tap targets: Size of hit area for each tab (accessible?)

**What to Screenshot**:
- Full screen showing bottom nav bar clearly
- Zoomed view of all tab icons and labels
- Before/after of switching tabs (to show feedback)
- Bottom nav when active vs. inactive state

**What to Document**:
- Number of tabs and their labels
- Label clarity (self-explanatory, 1-5 scale)
- Icon quality and distinctness
- Spacing and hit target size (estimated minimum 48px recommended)
- Feedback when switching tabs (visual, timing)

**Framework Checkpoints**:
- **Nielsen #4**: Consistency — do tabs follow platform conventions?
- **Nielsen #6**: Recognition — are icons immediately recognizable?
- **Norman's Affordances**: Do tabs look tappable and interactive?

---

### 6. Scroll Behavior & Content Depth
**Purpose**: Understand how content is organized vertically and if scrolling is intuitive.

**What to Observe**:
- Scroll direction: Vertical (standard) / Horizontal / Mixed
- Scroll stickiness: Sections that stick / Smooth scrolling
- Infinite scroll vs. pagination: Does new content load as user scrolls?
- Load time during scroll: Is content pre-loaded or loading mid-scroll?
- Scroll performance: Smooth or janky?
- Back-to-top affordance: Is there a floating button or sticky header to return to top?

**What to Screenshot**:
- Screenshot at top of page
- Screenshot mid-scroll (50% down)
- Screenshot near bottom of page
- Any loading indicators or skeleton screens visible during scroll
- Floating back-to-top button (if present)

**What to Document**:
- Scroll type (vertical, horizontal, mixed)
- Estimated number of scroll positions to see all content
- Performance during scroll (smooth, lag observed?)
- Content loading behavior (preloaded, lazy-loaded, paginated)
- Back-to-top accessibility (easy, hidden, not available)

**Framework Checkpoints**:
- **Nielsen #1**: System visibility — is loading state visible during scroll?
- **Fogg's Ability**: Long scrolls reduce ability (user must invest time). Is this intentional?

---

### 7. Free vs. Locked Content Visibility
**Purpose**: Assess how clearly the app indicates which content is free vs. premium-only.

**What to Observe**:
- Visibility of locked content: Hidden / Shown with lock icon / Shown with "Premium" label
- Lock icon design: Clear, obvious, or subtle?
- Preview of locked content: Full preview / Truncated / No preview
- User's current subscription status: Visible anywhere on screen?
- Can user identify how to unlock content (is the upgrade path clear)?

**What to Screenshot**:
- Content card with lock indicator (if present)
- Zoomed view of lock icon or "Premium" label
- Comparison of free vs. locked content visual treatment
- Screen showing user's subscription status (if visible)

**What to Document**:
- Percentage of visible content that is locked (estimate)
- Lock indicator clarity (1-5 scale: invisible to obvious)
- Whether unlocking path is clear (yes/no)
- User subscription status visibility (visible, hidden, not clear)

**Framework Checkpoints**:
- **Nielsen #1**: Is the app's content offering (free/premium split) clear?
- **Cagan Value Risk**: Can free users see value, or is premium content so hidden they assume there's nothing free?

---

## SCORING RUBRIC (1-10)

Each score should reference specific framework principles and include evidence from the screens above.

### 9-10: Best-in-Class (Apple, YouTube, Notion Level)

**Criteria**:
- Homepage is **optimized for recognition**: Minimal text, clear icons, visual hierarchy instantly communicates structure
- Navigation is **intuitive and consistent**: Users find their way without tooltips or help text
- Content organization is **logical**: Free vs. locked content is obvious; categories are self-explanatory
- **Above-the-fold clarity**: Value proposition and primary CTAs are visible without scrolling
- **No cognitive load**: Every element serves a purpose; visual clutter is minimal
- **Accessibility**: Text hierarchy, color contrast, spacing all meet WCAG standards
- **Mobile-first design**: Bottom navigation is comfortable; hit targets are >48px; no tiny icons
- **Personalization signals**: Even on homepage, users see evidence of personalization (recommendations, "For You" section)

**Framework Alignment**:
- **Nielsen #1, #6, #8**: System visibility is obvious; recognition doesn't require recall; minimal aesthetic
- **Norman**: Signifiers are clear; affordances are obvious; mapping is intuitive
- **JTBD**: Locate step is frictionless
- **Kano**: Must-Be requirements (clarity, navigation) are exceeded; One-Dimensional features (organization, speed) are optimized

**Examples**: YouTube homepage (clear sections, obvious primary action), Apple App Store (stunning visual hierarchy), Notion dashboard (clear structure despite complexity)

---

### 7-8: Good / Well-Designed

**Criteria**:
- Navigation is **clear and learnable**: Users can find their way after 1-2 uses
- Content organization is **mostly logical**: Some category names might need discovery, but overall structure makes sense
- **Free vs. locked content is visible**: Lock indicators are present; not completely hidden
- **Scroll depth is reasonable**: Key categories visible in 1-2 scroll positions (not 10+ scrolls)
- **Visual hierarchy is evident**: Primary section stands out; secondary sections are clearly secondary
- **Bottom nav or clear alternatives**: Navigation is not confusing or hidden
- **Load time is acceptable**: Content visible in <2 seconds; no egregious delays
- **Minimal clutter**: Not magazine-like or overwhelming, but also not sparse

**Framework Alignment**:
- **Nielsen #4**: Consistency is mostly present; minor deviations from standards
- **Norman**: Most signifiers are clear; some elements need learning
- **Fogg Ability**: Navigation requires low cognitive load; clear path to content

**Examples**: Medium (clean card design, recognizable sections), Spotify (clear home sections, some exploration needed), Many top-50 apps

---

### 5-6: Adequate / Decent Structure but Missing Elements

**Criteria**:
- Navigation is **learnable but not intuitive**: Users need 3-4 uses to feel confident
- Content organization is **partially confusing**: Some sections feel out of place or unclear
- **Free vs. locked content is ambiguous**: Not always clear if content is locked; indicators are subtle or missing
- **Scroll depth is deep**: Key categories are 3+ scroll positions down
- **Visual hierarchy is weak**: Multiple elements compete for attention; not clear what's primary
- **Navigation is present but not prominent**: Must hunt for tabs or menu
- **Load time is sluggish**: Content visible in 2-4 seconds; some delays during scroll
- **Moderate clutter**: Some unnecessary elements or redundant sections

**Framework Alignment**:
- **Nielsen #6**: Recognition requires some recall (user must learn the structure)
- **Nielsen #8**: Some visual clutter present
- **JTBD Locate**: Finding content requires some effort; not immediately obvious

**Examples**: Average productivity apps, many finance/investing apps with crowded dashboards

---

### 3-4: Poor / Confusing Structure or Hidden Content

**Criteria**:
- Navigation is **confusing**: Users must actively hunt for sections; tabs are mislabeled or illogical
- Content organization is **illogical**: Categories seem random; no obvious grouping logic
- **Free vs. locked content is hidden**: Locked items are grayed out or removed entirely; user can't see what's locked until tapping
- **Scroll depth is excessive**: Key categories are 5+ scroll positions down
- **Visual hierarchy is absent**: Everything competes equally; no clear focal points
- **Navigation is hard to find**: No visible bottom tabs; menu is hidden; no clear primary nav
- **Load time is slow**: Content takes 4+ seconds to appear; frequent delays during interaction
- **Significant clutter**: Too many sections, cards, and elements competing for attention

**Framework Alignment**:
- **Nielsen #1**: System status is not clear; users are confused about what the app offers
- **Nielsen #6**: User must recall structure instead of recognizing it
- **Nielsen #8**: Visual design is cluttered and overwhelming
- **Cagan Value Risk**: Users can't tell what value the app provides; too much content buried

**Examples**: Poorly designed enterprise apps, some legacy financial apps

---

### 1-2: Severely Flawed / Navigation is Broken or Content is Unreachable

**Criteria**:
- Navigation is **broken or absent**: No clear way to find content; users are stuck on homepage
- Content organization is **random or non-existent**: No discernible structure; browsing is impossible
- **Locked content blocks the app**: Majority of content is behind paywall; free tier appears empty
- **Scroll depth is infinite**: Hundreds of items; no pagination or organization; no clear end
- **Visual hierarchy is non-existent**: Every element screams for attention; visual chaos
- **Homepage is empty or broken**: Loads blank or with errors; no content visible
- **Load time is unacceptable**: Content takes 10+ seconds; frequent timeouts
- **Severe clutter**: Too many ads, sections, and pop-ups; can't see the actual content

**Framework Alignment**:
- **Nielsen #1**: System status is broken; user doesn't know what's happening
- **Nielsen #6**: Recognition is impossible; user must re-learn structure every time
- **JTBD Locate**: Locate step is completely broken; user cannot find content
- **Cagan Value Risk**: Value risk is catastrophic; user can't tell what the app does

**Examples**: Spammy or abandoned apps, broken app rebuilds, ad-heavy free games

---

## SCORING METHODOLOGY

**Award points for**:
- Intuitive navigation: +2 points
- Clear visual hierarchy: +1 point
- Free/locked content visibility: +1 point
- Scroll depth <3 positions: +1 point
- Bottom nav or prominent primary nav: +1 point
- <2 second load time: +1 point
- Personalization signals visible: +1 point

**Deduct points for**:
- Confusing navigation: -2 points
- Weak visual hierarchy: -1 point
- Locked content hidden: -1 point
- Excessive scroll depth (>5): -1 point
- No clear primary nav: -2 points
- Slow load time (>4 sec): -1 point
- Content appears generic/non-personalized: -1 point
- Visual clutter: -1 point

**Final Score**: Start at 5 (baseline) and add/subtract points. Cap at 1-10 scale.

---

## EVIDENCE CHECKLIST

Document these specific data points during your review.

### Navigation Structure

- [ ] **Primary navigation type**: [Bottom tabs / Side drawer / Top tabs / None]
- [ ] **Number of primary navigation items**: [_____]
- [ ] **Navigation labels & clarity** (1-5 scale): [_____]
- [ ] **Time to switch between sections** (in taps): [_____]
- [ ] **Is navigation always visible or does it hide on scroll?**: [Always visible / Hides / Sticky]
- [ ] **Back/home navigation available?**: [Yes / No]

**Framework**: Nielsen #1 (Visibility), #4 (Consistency), Norman (Signifiers)

---

### Homepage Content Organization

- [ ] **Content layout type**: [Grid / List / Cards / Carousel / Other: _____]
- [ ] **Number of content items visible without scrolling**: [_____]
- [ ] **Number of distinct sections/categories visible**: [_____]
- [ ] **Free vs. locked content distinction**: [Clear / Somewhat clear / Not clear]
- [ ] **Content preview type**: [Thumbnail + title / Title only / Thumbnail only / Rich card]
- [ ] **Scroll depth to see all primary categories**: [_____] items or [_____] scrolls

**Framework**: Nielsen #6 (Recognition), #8 (Minimalism), JTBD (Locate)

---

### Header Elements

- [ ] **Header type**: [Fixed / Sticky / Scrolls away / None]
- [ ] **Logo/branding present**: [Yes / No]
- [ ] **Search availability**: [Always visible / In header / Floating button / No search]
- [ ] **Number of actionable header items**: [_____]
- [ ] **Header visual weight** (1-5 scale): [_____]

**Framework**: Nielsen #1 (Visibility), Norman (Affordances)

---

### Free vs. Locked Content Audit

- [ ] **Percentage of visible content that is locked** (estimate): [_____]%
- [ ] **Lock indicator type**: [Icon / Text label / Color change / Grayed out / None]
- [ ] **Lock indicator clarity** (1-5 scale): [_____]
- [ ] **Preview available for locked items?**: [Full / Partial / None]
- [ ] **User subscription status visible?**: [Yes / No / Partially visible]
- [ ] **Is upgrade path clear from locked content?**: [Yes / No]

**Framework**: Cagan Value Risk, Nielsen #1 (System status)

---

### Visual Design & Hierarchy

- [ ] **Primary content focal point** (what draws the eye first): [_____]
- [ ] **Visual hierarchy clarity** (1-5 scale): [_____]
- [ ] **Color usage**: [Consistent / Chaotic / Minimal / Rich]
- [ ] **Typography hierarchy** (heading sizes clearly differentiated?): [Yes / No]
- [ ] **Spacing rhythm** (consistent padding/margins?): [Yes / No / Some areas inconsistent]
- [ ] **Visual clutter assessment** (1-5 scale, 5 = very cluttered): [_____]

**Framework**: Nielsen #8 (Aesthetic, Minimalist), Norman (Conceptual Model)

---

### Loading & Performance

- [ ] **Time from app open to homepage visible**: [_____] seconds
- [ ] **Content fully loaded before interactive**: [Yes / No]
- [ ] **Skeleton screens or loading states used**: [Yes / No]
- [ ] **Scroll performance**: [Smooth / Occasional lag / Frequent stuttering]
- [ ] **Infinite scroll or pagination**: [Infinite / Paginated / Both]

**Framework**: Nielsen #1 (Feedback), Fogg Ability (Friction)

---

### Personalization Signals

- [ ] **Personalized content visible on homepage?**: [Yes / No]
- [ ] **"For You" or personalized section present**: [Yes / No]
- [ ] **Recommendation engine evident**: [Yes / No]
- [ ] **User profile/preference visibility**: [Visible / Hidden / Not applicable]

**Framework**: HEART (Engagement), Reforge (Product Loop)

---

## KEY ISSUES TEMPLATE

### Issue #1: Confusing Navigation or Hidden Key Features
**Problem**: Users cannot easily find major content sections or features. Navigation labels are unclear or structure seems random.

**Framework Cite**:
- **Nielsen #1 (Visibility)**: Users should always know where they are and what they can access. Hidden or unclear navigation violates this.
- **Nielsen #6 (Recognition vs. Recall)**: Navigation should be recognizable (visible, familiar patterns), not require users to remember from previous uses.
- **Norman (Signifiers)**: Navigation labels must clearly signal what each section contains. Icons alone or unclear labels force guessing.

**Evidence**: Screenshots showing navigation structure with unclear labels or sections hard to find.

**Quantified Impact**: Apps with unclear navigation see 20-40% of users abandon after first use. Users spend extra time hunting for content, reducing engagement.

**Hypothesis for Improvement**:
1. Simplify navigation to 4-5 primary sections max
2. Use clear, action-oriented labels ("For You", "Browse", "Downloads", "Settings")
3. Add icons that match user expectations
4. Test navigation labels with 5-10 users and iterate

Estimated impact: 15-25% improvement in feature discoverability, 10-15% increase in engagement.

**Comparative Benchmark**: YouTube keeps navigation to 4 tabs (Home, Shorts, Subscriptions, You) with instantly recognizable icons. Notion shows clear structure (Favorites, All, Templates, Integrations).

---

### Issue #2: Premium Content Blocks the Entire App
**Problem**: Majority of content is locked behind paywall. Free section is so small it appears empty. User can't tell if there's value in the free tier.

**Framework Cite**:
- **Cagan Value Risk**: Cannot assess value when content is hidden. Users need to experience the free tier's value before deciding to upgrade.
- **Fogg MAP**: When ability to access content is blocked, motivation to explore the app drops.
- **AARRR Activation**: Showing premium-only content before free tier value = Activation failure.

**Evidence**: Screenshots showing percentage of locked vs. unlocked content. Estimate: 80% locked, 20% free.

**Quantified Impact**: Apps that hide majority of content see <10% free-to-paid conversion and <30% Activation rate. Apps showing robust free tier see 20-40% conversion.

**Hypothesis for Improvement**:
1. Ensure at least 40-50% of content is accessible in free tier
2. Show "most popular free content" prominently on homepage
3. Clearly label locked items with a small lock icon, not hidden entirely
4. Make free tier genuinely useful (not just trial)

Estimated impact: 30-50% improvement in Activation rate, 15-25% improvement in free-to-paid conversion.

**Comparative Benchmark**: Spotify shows thousands of songs free; premium is about curation/offline, not access. YouTube's free tier is nearly feature-complete; premium is offline + ad-free.

---

### Issue #3: Excessive Scroll Depth to Find Content
**Problem**: Key categories are buried 5+ scroll positions down. User must scroll through 50+ items to find what they want.

**Framework Cite**:
- **Nielsen #8 (Minimalism)**: Every element on screen should be necessary. If scrolling past 50 items, not everything is necessary on homepage.
- **JTBD Locate**: User should find relevant content in <3 scrolls. Excessive scrolling breaks the Locate step.
- **Fogg Ability**: Long scrolls are friction. High friction = lower ability to complete the task.

**Evidence**: Count number of scroll positions needed to see all major categories. Document items visible at each scroll point.

**Quantified Impact**: Each additional scroll depth reduces engagement by 10-15%. Apps with categories visible in <3 scrolls see 30% higher engagement than those requiring 5+ scrolls.

**Hypothesis for Improvement**:
1. **Organize by popularity or relevance**: Show most-used categories first
2. **Use horizontal carousel**: Show multiple categories in single scroll position
3. **Pagination**: "See all categories" link instead of loading them all at once
4. **Smart defaults**: Pre-select a default category so user doesn't have to scroll to start

Estimated impact: 20-30% increase in engagement, reduced bounce on homepage.

**Comparative Benchmark**: Netflix shows 4-6 content categories above fold; you scroll to see more, but key categories (Continue Watching, Top Picks) are immediate. Spotify's home shows Recently Played, Liked Songs, Recommended immediately.

---

### Issue #4: Visual Hierarchy is Unclear; Everything Competes Equally
**Problem**: Homepage shows 10+ sections/items with equal visual weight. No focal point. User doesn't know what the app is about or where to start.

**Framework Cite**:
- **Nielsen #1**: Visibility of system status. User should immediately understand what the app offers. Equal visual weight obscures this.
- **Nielsen #8**: Aesthetic and minimalist design. Not every section should be equally prominent.
- **Norman (Conceptual Model)**: User's mental model of the app's structure is unclear. No hierarchy = no model.

**Evidence**: Screenshot of homepage with visual weight analysis. Identify which elements draw attention equally.

**Quantified Impact**: Apps with unclear visual hierarchy show 2-3x higher drop-off on first screen. Users abandon because they don't understand what the app does.

**Hypothesis for Improvement**:
1. **Establish hierarchy**: Primary section (largest, top), secondary (medium), tertiary (small, at bottom)
2. **Use color strategically**: Highlight primary CTAs; secondary in neutral tones
3. **Contrast and spacing**: Increase whitespace between sections to create breathing room
4. **Test with users**: Ask new users "What is the main thing this app is for?" If they can't answer, hierarchy is broken.

Estimated impact: 25-40% improvement in first-screen understanding, 15-20% higher engagement.

**Comparative Benchmark**: YouTube emphasizes Home feed first (large cards), recommendations second, secondary sections (Shorts, Subscriptions, You) in bottom nav. Clear hierarchy.

---

### Issue #5: Free vs. Locked Content is Completely Unclear
**Problem**: User cannot tell which content is free vs. premium without tapping every item. No visual distinction.

**Framework Cite**:
- **Nielsen #1**: System visibility. User should know content availability before tapping.
- **Nielsen #6**: Recognition. Lock indicators or labels should be visible, not hidden.
- **Cagan Value Risk**: User cannot assess free tier value if they can't see which content is free.

**Evidence**: Screenshots showing content cards with and without lock indicators. Document if lock icons are visible or require tapping to see.

**Quantified Impact**: Apps with clear free/locked distinction see 20-30% higher engagement in free tier. Users explore more because they know what's available.

**Hypothesis for Improvement**:
1. **Add lock icon**: Small, clear lock icon on premium content (bottom-right corner)
2. **Or use label**: Small "Premium" badge on locked items
3. **Or use color**: Slightly different background color for locked items
4. **Test clarity**: Show to 5 users and ask "Which content can you use for free?" Should be >80% accurate.

Estimated impact: 15-25% increase in free-tier engagement, lower abandon rate.

**Comparative Benchmark**: Kindle shows "Sample" clearly; Audible shows lock icon on premium audiobooks; Medium shows "Subscribe to read" overlay on limited articles.

---

## SPEED MODE vs RIGOR MODE INSTRUCTIONS

### SPEED MODE (15-20 minutes)
**Best for**: Quick competitive analysis, rapid IA assessment.

**Flow**:
1. **Screenshot homepage** (above-fold area, full screen)
2. **Navigate each major section** (identify primary nav pattern)
3. **Note free vs. locked** (is it visually clear?)
4. **Count scroll depth** (how many scrolls to see all categories?)
5. **Visual hierarchy assessment** (what draws your eye first?)
6. **Identify 2-3 key issues**
7. **Assign score** (9-10 / 7-8 / 5-6 / 3-4 / 1-2)

**Evidence Output**:
- Navigation type and clarity
- Content organization (obvious or confusing?)
- Free/locked visibility
- 2-3 key issues with framework cite
- Score with 1-sentence justification

**Estimated Output Length**: 1-2 pages

---

### RIGOR MODE (45-60 minutes)
**Best for**: Deep competitive analysis, internal benchmarking, case studies.

**Flow**:
1. **App store listing** → Document positioning and category
2. **Homepage load** → Time load, screenshot top-fold
3. **Complete navigation audit** → All primary sections
4. **Content organization** → Layout type, scroll depth, categorization logic
5. **Header/footer audit** → All actions available
6. **Free vs. locked** → Audit every content type
7. **Visual design analysis** → Hierarchy, color, typography, spacing
8. **Mobile-first assessment** → Touch targets, responsiveness
9. **Scroll performance** → Load during interaction
10. **Personalization audit** → Evidence of personalization on homepage
11. **Detailed evidence** → Fill out entire Evidence Checklist
12. **5-7 key issues** → Comprehensive with benchmarks
13. **Final score** → Detailed justification with point breakdown

**Evidence Output**:
- Evidence Checklist: 90% complete
- 3-5 page detailed analysis
- Persona-specific findings (new user, returning user)
- Comparative benchmarks to category leaders
- Prioritized recommendations

**Estimated Output Length**: 5-10 pages

---

### Hybrid Mode (Recommended)
**Time: 30-40 minutes**

1. Full navigation and content org audit (Rigor)
2. One complete scrollthrough with timing (Rigor)
3. Free vs. locked detailed audit (Rigor)
4. Visual hierarchy assessment (Rigor)
5. Top 3-4 issues (Speed)
6. Score with moderate justification (Hybrid)

---

## PERSONA-SPECIFIC INSTRUCTIONS

### 1. New User (First Open)
**What to Test**:
- Is the app's purpose immediately clear from the homepage?
- Can the user find their desired content in <2 minutes?
- Is the navigation intuitive without prior knowledge?

**Key Metric**: Homepage clarity (can user explain app's purpose after 10 seconds?)

**Scoring Focus**: Visual hierarchy, navigation intuitiveness, content discoverability

---

### 2. Returning User (Day 2+)
**What to Test**:
- Does the app recognize the user and show personalized content?
- Is navigation muscle memory possible (same location every time)?
- Are new/featured content updates visible?

**Key Metric**: Personalization persistence, consistency of layout

**Scoring Focus**: Consistency, personalization, reduced friction for quick access

---

### 3. Content Searcher (Using Browse/Category)
**What to Test**:
- Can user browse categories easily?
- Is category organization logical?
- Can user find content matching their interest?

**Key Metric**: Time to find specific content by category

**Scoring Focus**: Category clarity, organization logic, search functionality

---

## DOMAIN-SPECIFIC OVERLAYS

### Education Apps
**Domain-specific criteria**:
- Are course/curriculum categories clear and well-organized?
- Is difficulty level (beginner/intermediate/advanced) visible?
- Can users see the learning path before committing to a course?

**Scoring Modifiers**:
- +1 if curriculum structure is visible on homepage
- -1 if course difficulty is hidden or unclear

---

### OTT / Streaming Apps
**Domain-specific criteria**:
- Is the content feed immediately populated with recommendations?
- Are genre categories clear and distinct?
- Can user find new/trending content easily?

**Scoring Modifiers**:
- +2 if home feed shows 4+ content recommendations above fold
- -1 if feed appears empty or generic

---

### Social Apps
**Domain-specific criteria**:
- Is the social feed visible immediately (not empty)?
- Are follow/friending suggestions shown?
- Is the "discover" section prominent?

**Scoring Modifiers**:
- +1 if feed is pre-populated with content on first open
- -2 if feed is empty, requiring user to follow someone first

---

### Productivity / Note-Taking Apps
**Domain-specific criteria**:
- Are recent notes/documents visible on homepage?
- Is there a "create new" affordance prominently placed?
- Are different note types/categories organized?

**Scoring Modifiers**:
- +1 if recent items are shown on homepage
- +1 if "create new" is prominently accessible

---

### E-commerce Apps
**Domain-specific criteria**:
- Are product categories clear and browseable?
- Is search prominent and functional?
- Are deal/offer sections visible?

**Scoring Modifiers**:
- +1 if top categories are visible above fold
- +1 if search is prominently featured

---

## INDIA-SPECIFIC CHECKS

Every review of an Indian app must include these checks for this module:

### Data-Light Loading & Performance
- [ ] Does the homepage load in <3 seconds on 4G with 3-4 bars?
- [ ] Are images lazy-loaded or does the whole page block until all images load?
- [ ] Is there a skeleton loader (content placeholder) or does the user see a blank screen?
- [ ] Is above-fold content prioritized for rendering (critical path optimization)?
- [ ] Are thumbnails low-res initially with progressive enhancement?
- [ ] Impact if missing: 60%+ of Indian users are on budget devices with 4G. A 5-second load time causes 40%+ bounce rate. Blank screens during loading are interpreted as "app is broken."

**Finding template:** "Homepage takes 5+ seconds to fully load on 4G. No skeleton loader — user sees blank white screen for 3 seconds. All images load at full resolution simultaneously, blocking content visibility. Budget device users (60%+ of India market) will bounce."

**India Benchmark:** Zepto's homepage loads in <2 seconds with real-time inventory (no heavy hero images). Meesho uses progressive image loading — low-res thumbnails render instantly, full-res loads in background.

### Hindi/English Toggle & Vernacular IA
- [ ] Is there a language toggle (🌐) accessible from the homepage?
- [ ] Are navigation labels available in Hindi/Hinglish?
- [ ] Are category names localized (not just translated — culturally relevant)?
- [ ] Does the homepage adapt content based on language preference?
- [ ] Impact if missing: Tier 2-3 users who prefer Hindi will find English-only navigation confusing. Category labels in English reduce browse-through rates by 20-30%.

**Finding template:** "Homepage navigation is English-only. No language toggle visible. Category labels ('Trending,' 'For You,' 'Continue Learning') are not available in Hindi. This alienates 45-50% of the Indian internet user base."

**India Benchmark:** ShareChat's homepage is entirely in the user's selected language (15 options). Flipkart shows Hindi navigation and deal banners for Hindi-preference users.

### Browse-First Architecture (Tier 2-3 Pattern)
- [ ] Is the homepage browse-friendly (visual cards/grids) or search-dependent?
- [ ] Are categories visible without scrolling?
- [ ] Is there a "Popular in [City]" or "Trending in Hindi" section?
- [ ] Does the homepage show social proof ("10,000 people watched today")?
- [ ] Impact if missing: Tier 2-3 India users browse more than search. A search-first homepage loses these users.

**Finding template:** "Homepage is search-bar-first with minimal browse content above fold. No visual category grid, no trending section, no regional popularity signals. Tier 2-3 users who prefer browsing over searching will find the homepage empty."

**India Benchmark:** Meesho's browse-first homepage: product grid with visual categories, deals above fold, regional trending. 55% of sessions are browse-only. Flipkart's deal-first IA shows personalized offers above fold.

### Scoring Modifiers (India)
- +1 if homepage loads in <3 seconds on 4G
- +1 if Hindi/regional language navigation is available
- +1 if browse-first architecture with visual categories
- -1 if no skeleton loader (blank screen during load)
- -1 if English-only navigation with no language option
- -1 if search-bar-first with no browse content above fold

---

## OUTPUT FORMAT

```markdown
# HOMEPAGE & INFORMATION ARCHITECTURE — [X]/10

## Evidence Summary

### Navigation Structure
- **Primary navigation type**: [Bottom tabs / Side drawer / Other]
- **Number of sections**: [X]
- **Navigation clarity**: [X]/5
- **Time to switch sections**: [X] taps
- **Framework**: Nielsen #1 (Visibility), #4 (Consistency), Norman (Signifiers)

### Content Organization
- **Layout type**: [Grid / List / Cards / Carousel]
- **Items visible without scroll**: [X]
- **Scroll depth to see all categories**: [X] scrolls
- **Free vs. locked visibility**: [Clear / Ambiguous / Hidden]
- **Framework**: Nielsen #6 (Recognition), #8 (Minimalism), JTBD (Locate)

### Visual Hierarchy
- **Primary focal point**: [What draws attention first]
- **Hierarchy clarity**: [X]/5
- **Visual clutter**: [X]/5 (5 = very cluttered)
- **Framework**: Nielsen #8 (Aesthetic/Minimalist), Norman (Conceptual Model)

### Key Metrics
- **Load time to homepage visible**: [X] seconds
- **Personalization signals visible**: [Yes / No]
- **Visual design quality**: [Professional / Adequate / Generic]

### Frameworks Applied
- **Nielsen**: Visibility, recognition, minimalism, consistency assessed
- **Norman**: Signifiers, affordances, mapping, feedback reviewed
- **JTBD**: Locate step evaluated
- **Cagan Value Risk**: Value visibility assessed

---

## Evidence

### [Screen 1: Homepage First Impression]
- **Time to load**: [X] seconds
- **Content visible**: [X] major sections above fold
- **Primary focal point**: [What stands out]
- **Clarity**: [Obvious / Clear / Ambiguous / Confusing]
- **Framework cite**: Nielsen #1, Cagan Value Risk

### [Screen 2: Navigation Structure]
- **Type**: [Bottom tabs / Side / Top / None]
- **Labels**: [Clear / Somewhat clear / Confusing]
- **Number of sections**: [X]
- **Active state indication**: [Obvious / Subtle / None]
- **Framework cite**: Nielsen #4, Norman (Signifiers)

### [Screen 3: Content Organization]
- **Layout**: [Grid / List / Cards / Carousel]
- **Scroll depth**: [X] scrolls to see all
- **Free/locked distinction**: [Clear / Ambiguous / Hidden]
- **Categories**: [Logical / Random / Hierarchical]
- **Framework cite**: Nielsen #6, #8, JTBD

### [Screen 4: Header Elements]
- **Type**: [Fixed / Sticky / Scrolling / None]
- **Search**: [Always visible / Hidden / Not present]
- **Quick actions**: [Filter / Sort / Settings / Notifications / None]
- **Clarity**: [Clean / Cluttered / Minimal]
- **Framework cite**: Nielsen #1

### [Screen 5: Bottom Navigation]
- **Number of tabs**: [X]
- **Labels**: [Text + icons / Icons only / Text only]
- **Clarity**: [Obvious / Clear / Confusing]
- **Hit target size**: [Adequate / Minimal / Unclear]
- **Framework cite**: Nielsen #4, Norman (Affordances)

---

## Scoring Breakdown

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Navigation intuitiveness | [X]/10 | Primary nav is [clear/confusing], takes [X] taps to switch sections |
| Visual hierarchy | [X]/10 | [Primary focal point identified / No clear focal point] |
| Free/locked content clarity | [X]/10 | [Clearly marked / Ambiguous / Hidden] |
| Content organization | [X]/10 | [Logical / Somewhat logical / Confusing structure] |
| Scroll depth | [X]/10 | [X] scrolls to see all categories |
| Load performance | [X]/10 | [X] seconds to homepage visible |
| Personalization | [X]/10 | [Evident / Not visible] on first screen |
| Overall design quality | [X]/10 | [Professional / Adequate / Generic] |

**Total Score: [X.X] → [X]/10**

**Justification**: [2-3 sentence summary grounded in frameworks]

---

## Key Issues

### Issue #1: [Title]
**Problem**: [What was observed]

**Framework Cite**:
- **[Framework name]**: [Principle violated]

**Evidence**: [Specific screenshots/metrics]

**Quantified Impact**: [How many users affected, engagement impact]

**Hypothesis for Improvement**: [Specific, testable hypothesis]

**Comparative Benchmark**: [How do leading apps handle this?]

---

## Persona-Specific Findings

### New User
- **Key metric**: Homepage clarity [1-5 scale]
- **Experience**: [Brief description]
- **Issues**: [Top 1-2 issues]
- **Score**: [X]/10

### Returning User
- **Key metric**: Personalization visibility
- **Experience**: [Brief description]
- **Issues**: [Top 1-2 issues]
- **Score**: [X]/10

---

## Recommendations (Prioritized)

### P0 (Critical)
1. **[Issue affecting navigation or value clarity]**
   - Recommendation: [Specific change]
   - Expected impact: [Estimated lift]

---

**Review Conducted**: [Date] | **Reviewer**: [Name] | **Duration**: [Mode]
```

---

## Summary

This module evaluates the homepage and information architecture—critical for Activation and Engagement. It assesses whether users can understand the app's structure, find content intuitively, and recognize (not recall) key features. Every criterion is grounded in Nielsen's usability heuristics, Norman's design principles, and JTBD's Locate step. Scoring methodology balances professional design standards (Nielsen, Norman) with behavioral psychology (Fogg) to provide actionable insights for product teams.

