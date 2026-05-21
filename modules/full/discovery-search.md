# Content Discovery & Search Module

## MODULE OVERVIEW

### What This Module Reviews
This module evaluates the user's ability to discover, search for, and filter content. It assesses how easy it is for users to find what they're looking for—whether through search, browse/category navigation, trending content, or discovery mechanisms. This is the critical "Locate" step in the Jobs-to-Be-Done framework.

**Scope**: From search bar visibility → search results, filtering, category browse, trending content, personalized discovery, and recommendation surfaces.

### AARRR Stage Mapping
**Engagement** — The stage where active users find content and continue using the app. This module directly impacts:
- Whether users find content matching their intent
- Frequency of app opens (if discovery is easy, users return more)
- Feature adoption (discovery of secondary features)
- Time spent in-app (easy discovery = more browsing)
- Retention signals (users who find value stay)

### Design Skill Integration (Mandatory for Screenshots)

> **`design:critique`** — Run on search UI and browse/discovery screenshots. Evaluate: search bar visibility and prominence, filter/facet usability, results layout clarity, visual hierarchy of search results vs categories, accessibility (touch targets on filter chips, contrast on result cards). For India context: does the search UI accommodate voice input (microphone icon)? Are browse categories visual (image grids) for Tier 2-3 who prefer browsing over search?

> **`design:ux-copy`** — Run on search bar placeholder text, filter labels, empty state ("no results") messaging, and category labels. Evaluate: is placeholder text helpful and specific? Are filter labels clear? Does "no results" copy suggest alternatives? For India context: is search placeholder in Hindi? Are category labels in Hindi/Hinglish? Does the "no results" message suggest browsing as an alternative?

### Primary Frameworks & Models

| Framework | Application |
|-----------|-------------|
| **JTBD (Locate Step)** | Can users find the content they came for without friction? |
| **Nielsen's Heuristics #1, #6** | Visibility of search; recognition vs. recall of content |
| **HEART (Task Success)** | Can users complete their search/discovery task successfully? |
| **Norman's Design Principles** | Signifiers (is search obvious?), affordances (does it look searchable?), mapping (clear filters) |
| **Hook Model (Variable Reward)** | Does discovery deliver variable, satisfying results? Or same content every time? |
| **Reforge (Product Loop)** | Does discovery create a loop (search → find → save → share → return)? |

---

## SCREENS TO NAVIGATE

### 1. Search Bar Visibility & Prominence
**Purpose**: Assess how easy it is for users to find and access the search function.

**What to Observe**:
- Search bar location: Top header (fixed/sticky) / Floating / Hidden in tab / No search
- Search bar prominence: Full-width / Icon button / Tucked in menu
- Search placeholder text: Present and helpful (e.g., "Search lessons") or generic ("Search")
- Search bar state: Always ready (can tap and start typing) or requires extra step
- Search accessibility: On every screen or only on certain screens?
- Tap-to-search latency: Instant or delay?

**What to Screenshot**:
- Full screen showing search bar location and prominence
- Zoomed view of search bar with placeholder text visible
- Search bar in "active/focused" state (if possible)
- Before/after of toggling search visibility (if it hides)

**What to Document**:
- Search bar location and stickiness
- Placeholder text (exact quote)
- Search bar prominence (1-5 scale: invisible to dominating)
- Whether search is always accessible or screen-dependent
- Time from app open to visible search (seconds)

**Framework Checkpoints**:
- **Nielsen #1**: Visibility of system status — is search available/visible?
- **Nielsen #6**: Recognition — can user recognize the search affordance without explanation?
- **Norman's Signifiers**: Does the search bar look like a search bar (text input + magnifying glass)?

---

### 2. Search Flow & Results Quality
**Purpose**: Understand the search experience from query to results.

**What to Observe**:
- Search input: Single text field / Multi-field (category + keyword) / Voice input / Other
- Autocomplete: Suggestions shown while typing / Only after submitting / No autocomplete
- Search latency: How long before results appear after hitting search?
- Results presentation: Grid / List / Cards / Mixed layout
- Results relevance: Do results match the query? Or are they generic/wrong?
- Result information: Title only / Thumbnail + title / Rich preview / Metadata

**India-Specific Observations:**
- Is voice search input available? In Hindi/regional languages? (Microphone icon in search bar)
- Does search handle Hinglish queries (mixed Hindi-English, e.g., "business kaise start kare")?
- Does search autocomplete work in Hindi (Devanagari script)?
- Is search placeholder in Hindi or only English? Does it match the user's language preference?
- Are browse-based discovery paths available as alternatives to search (visual category grids, trending sections)?
- Result ordering: By relevance / By popularity / By recency / Random
- No results state: Helpful message or confusing error?

**What to Screenshot**:
- Search bar with sample query entered
- Autocomplete suggestions (if present) as user types
- Full search results page for a specific query
- Zoomed view of individual result card
- No results state (if applicable)
- Search filters (if present)

**What to Document**:
- Search input type and complexity
- Autocomplete present (yes/no); quality of suggestions (relevant/generic)
- Search latency (seconds from submit to first results)
- Number of results returned
- Results ordering logic (is it smart or random?)
- Result card information density (minimal/moderate/rich)
- Result relevance (1-5 scale: highly relevant to completely off-topic)

**Framework Checkpoints**:
- **JTBD Locate**: Do search results help user find what they came for?
- **Nielsen #1**: Is search latency visible (loading indicator) or confusing?
- **HEART Task Success**: Can user complete their search task successfully?

---

### 3. Search Autocomplete & Suggestions
**Purpose**: Assess the quality and usefulness of search suggestions.

**What to Observe**:
- Autocomplete triggers: Shows on first character / After 2-3 chars / No autocomplete
- Suggestion sources: Popular searches / User history / Trending / Personalized / All
- Suggestion accuracy: Relevant to query / Completely off-topic / Mixed
- Suggestion count: 3 items / 5 items / 10+ items
- Suggestion formatting: Icon + text / Text only / Icons only
- Most popular/trending: Shown in suggestions / Separate section / Not visible

**What to Screenshot**:
- Search bar with 1-2 characters entered, showing suggestions
- Full autocomplete dropdown with all suggestions visible
- Comparison of suggestions for different queries (e.g., "python" vs. "english")

**What to Document**:
- Autocomplete present (yes/no)
- Suggestion accuracy (1-5 scale)
- Number of suggestions shown
- Suggestion sources (what categories appear?)
- Whether trending/popular are highlighted

**Framework Checkpoints**:
- **Hook Model**: Autocomplete provides a quick reward (easy navigation to content). Variable rewards?
- **Nielsen #6**: Recognition — can user recognize relevant suggestions without reading all?

---

### 4. Category / Browse Navigation
**Purpose**: Understand the alternative to search—content discovery through category browsing.

**What to Observe**:
- Category availability: Present / Not visible / Hidden behind menu
- Category breadth: 5 categories / 10 / 20+ / Organized into parent/child
- Category naming: Clear (e.g., "Python Programming") / Vague (e.g., "Tech") / Jargon-heavy
- Category navigation: Tabs / Dropdown / Grid / List / Sidebar
- Subcategories: Flat structure / Multi-level / Collapsible
- Category organization: Alphabetical / By popularity / By relevance / Random
- Content within category: How many items visible without scroll? How organized?

**What to Screenshot**:
- Homepage or dedicated "Browse" screen showing all categories
- One category opened, showing subcategories (if present)
- One category with content items visible
- Category structure visualization

**What to Document**:
- Category breadth and depth (flat vs. hierarchical)
- Category naming clarity (1-5 scale)
- Navigation type (tabs, dropdown, list, etc.)
- Time to browse a category and find specific content
- Logical organization (alphabetical, by usage, etc.)

**Framework Checkpoints**:
- **JTBD Locate**: Can user browse categories and find content by interest?
- **Nielsen #6**: Are category names recognizable (not requiring explanation)?

---

### 5. Filters & Refinement Options
**Purpose**: Assess whether users can narrow search/browse results to match their needs.

**What to Observe**:
- Filter availability: Present on search results / Present on browse / Not visible / Hidden in menu
- Filter types: Difficulty / Duration / Language / Rating / Price / Other
- Filter UI: Checkboxes / Toggles / Sliders / Dropdowns / Multi-select
- Filter persistence: Filters stay applied after navigation / Reset on page change
- Filter feedback: How many results match current filters? (is count visible?)
- Filter reset: Clear all button visible / Must uncheck individually / Not possible
- Smart filtering: Does the app suggest filters based on query? Or manual only?

**What to Screenshot**:
- Search/browse page with filters visible
- Filters opened (if in a drawer or expandable section)
- Filter application in progress (checkboxes selected)
- Results after filters applied (showing before/after count)

**What to Document**:
- Filter types available
- Number of filter options in each category
- Filter UI clarity (1-5 scale: obvious to confusing)
- Whether filter count is visible
- Time to apply multiple filters
- Effectiveness of filters (do results actually narrow relevantly?)

**Framework Checkpoints**:
- **HEART Task Success**: Do filters help users complete their discovery task?
- **Norman Mapping**: Do filter selections logically map to result changes?

---

### 6. Trending / Popular / Recommended Content
**Purpose**: Understand how the app surfaces content without requiring search.

**What to Observe**:
- Trending section: Present / Not visible / Automatic (algorithm-driven)
- Trending source: App-wide trending / Per-category trending / Personalized "trending for you"
- Trending update frequency: Real-time / Daily / Weekly / Unknown
- Popular/bestselling content: Shown / Not shown / Ranked by type
- Recommendation logic: Purely algorithmic / Personalization-based / Editor-curated / Mixed
- Recommendation freshness: Same content every day / Rotates regularly / Personalized variety
- Social proof signals: Ratings, review count, subscriber count shown? (Influences clicks?)

**What to Screenshot**:
- Trending/popular section (if present) as it appears
- Individual trending item with visible signals (ratings, views, etc.)
- "Trending now" vs. "Trending in category" (if both exist)

**What to Document**:
- Trending content types and volume
- Update frequency (is content static or dynamic?)
- Social proof signals visible (ratings, views, reviews?)
- Trending effectiveness (1-5 scale: helpful for discovery or spam?)
- Recommendation personalization (generic or personalized?)

**Framework Checkpoints**:
- **Hook Model Variable Reward**: Are trending recommendations variable (different each visit) or repetitive?
- **HEART Engagement**: Do trending sections increase session engagement?

---

### 7. Search Result Page Design & UX
**Purpose**: Assess the overall quality and clarity of search results pages.

**What to Observe**:
- Result layout: Grid / List / Card stack / Mixed
- Result information: Minimal (title only) / Moderate (title + metadata) / Rich (title + image + description)
- Result visual treatment: Thumbnail images / Icons / Plain text / Video previews
- Result consistency: All results formatted the same / Different layouts
- Metadata shown: Rating / Reviews / Duration / Release date / Price / Author / All
- CTA clarity: "View" button / "Play" button / Tap anywhere / Unclear
- Load more: Pagination ("Next" button) / Infinite scroll / "Load more" button
- Empty state clarity: Message when no results / Blank / Unhelpful error

**What to Screenshot**:
- Full search results page with 5-10 results visible
- Zoomed view of individual result card
- No results state (if applicable)
- Pagination/load more control (if visible)

**What to Document**:
- Result layout and consistency
- Information density per result (1-5 scale: minimal to rich)
- Visual hierarchy (is the clickable area obvious?)
- Result ordering logic (relevant, popular, random?)
- Time to decide which result to tap (1-5 scale: quick to confused)

**Framework Checkpoints**:
- **Nielsen #1**: Is the result page structure clear?
- **Norman Affordances**: Does each result look clickable?
- **HEART Task Success**: Can user easily choose a result and proceed?

---

### 8. Discovery Mechanisms Beyond Search
**Purpose**: Understand alternative content discovery (not requiring explicit search).

**What to Observe**:
- Recommendation engine: Visible ("Recommended for you", "Because you watched...", etc.) / Not visible
- Related content: After viewing one item, are similar items suggested?
- Curated collections: "Best of X", "Staff picks", "Trending now" / Not present
- User-generated discovery: Comments, ratings, reviews visible? Do they drive clicks?
- Social discovery: "Friends are reading X" / Not present
- Personalization signals: Does the app show "based on your history"? (proof of personalization)

**What to Screenshot**:
- Recommendation section (if visible on homepage or after viewing content)
- Curated collection (if present)
- Related content section (if present after viewing content)

**What to Document**:
- Types of discovery mechanisms present
- Effectiveness of each (1-5 scale: helpful or spam?)
- Personalization evidence (is it generic or personal?)
- Social proof influence (do user reviews drive clicks?)

**Framework Checkpoints**:
- **Hook Model**: Discovery surfaces provide Variable Rewards (content is fresh/surprising each visit?)
- **HEART Engagement**: Discovery mechanisms increase time in-app?

---

## SCORING RUBRIC (1-10)

### 9-10: Best-in-Class (YouTube, Spotify, Amazon Level)

**Criteria**:
- **Search is always accessible**: Fixed header or prominent affordance on every screen
- **Search results are highly relevant**: User's query is understood; results match intent
- **Autocomplete is smart**: Suggestions are contextual; trending/popular suggestions visible
- **Multiple discovery paths**: Search + browse + trending + recommendations all work well
- **Filters are powerful and intuitive**: Can narrow results easily; filter counts visible
- **Result pages are clear**: Quick visual scan tells user if result is relevant
- **No friction**: Search latency <1 sec; no confusing empty states
- **Personalization evident**: "For You" recommendations are varied and relevant
- **Variable rewards**: Discover something new each session; content freshness obvious

**Framework Alignment**:
- **JTBD Locate**: User can find what they came for in <30 seconds
- **Nielsen #1, #6**: Search visibility and recognition are excellent
- **Hook Model**: Discovery provides variable, satisfying rewards
- **HEART Task Success**: Users complete search tasks successfully

**Examples**: YouTube (search + trending + recommendations all work), Spotify (browse + recommendations seamless), Amazon (powerful filters + recommendations)

---

### 7-8: Good / Well-Designed

**Criteria**:
- **Search is accessible**: Prominent header or easy-to-find affordance
- **Search results are relevant**: Most results match query; occasional irrelevant item
- **Autocomplete is helpful**: Shows suggestions; mostly contextual
- **Multiple discovery paths exist**: At least 2-3 of (search, browse, trending, recommendations)
- **Filters present but basic**: Can narrow results; counts might not be visible
- **Result page is clear**: User can quickly identify relevant results
- **Minor friction**: Slight latency or confusing UI in some flows
- **Some personalization**: Recommendations are present but may be generic
- **Mostly variable rewards**: Content mostly fresh; some repetition on repeat visits

**Framework Alignment**:
- **JTBD Locate**: User can find content in <60 seconds
- **Nielsen #6**: Navigation is learnable; not all intuitive
- **HEART Task Success**: Most searches succeed; some friction remains

**Examples**: Many streaming apps, some productivity tools

---

### 5-6: Adequate / Basic Search & Discovery

**Criteria**:
- **Search is present but not prominent**: Visible in menu or tab, not always accessible
- **Search results are partially relevant**: Mix of relevant and irrelevant results
- **Autocomplete is absent or basic**: No suggestions or generic ones
- **Limited discovery paths**: Mostly search; browse/trending/recommendations minimal
- **Filters are absent or hard to find**: User must navigate multiple screens to filter
- **Result pages are confusing**: Unclear which result to tap; inconsistent formatting
- **Moderate friction**: Noticeable latency; occasional errors in search
- **Minimal personalization**: Recommendations may not be visible or are generic
- **Repetitive rewards**: Same content every visit; not much discovery

**Framework Alignment**:
- **JTBD Locate**: User can find content but with effort; takes 1-2 minutes
- **Nielsen #6**: Discovery requires learning the structure
- **HEART Task Success**: Search succeeds but with friction

**Examples**: Many average productivity and educational apps

---

### 3-4: Poor / Search is Hard to Use or Ineffective

**Criteria**:
- **Search is hidden or absent**: Must hunt for search button; not on main screen
- **Search results are irrelevant**: Results don't match query; poor relevance algorithm
- **No autocomplete**: User must guess complete query
- **Discovery is limited to browse**: Search/trending/recommendations don't work or missing
- **No filters or filters are broken**: Can't narrow results; filters don't affect results
- **Result pages are confusing**: Unclear how to proceed; inconsistent formatting
- **Significant friction**: Long latency; frequent errors; loading times
- **No personalization**: All users see same recommendations (generic)
- **Poor content freshness**: Same items every visit; no discovery variety

**Framework Alignment**:
- **JTBD Locate**: Locate step is broken; user must resort to other apps to find content
- **Nielsen #1**: Search visibility is poor
- **HEART Task Success**: Most searches fail or require extra effort

**Examples**: Many older apps, some legacy enterprise tools

---

### 1-2: Severely Flawed / Search/Discovery is Broken or Non-existent

**Criteria**:
- **No search function**: App doesn't have search at all
- **Search returns no results or errors**: Broken search algorithm
- **Content is undiscoverable**: No browse categories, no trending, no recommendations
- **Discovery is random**: Browsing shows content in no logical order
- **Extreme friction**: Search takes 10+ seconds; frequent timeouts
- **All content is behind paywall**: User can't see what's available to discover
- **No personalization**: App treats all users identically
- **Heavy ads or spam**: Discovery surface is cluttered with ads instead of content

**Framework Alignment**:
- **JTBD Locate**: Locate step is completely broken
- **HEART Task Success**: Users cannot complete discovery tasks
- **Cagan Value Risk**: User can't even see what value the app offers

**Examples**: Spammy or abandoned apps, broken rebuilds

---

## EVIDENCE CHECKLIST

### Search Bar Accessibility

- [ ] **Search bar location**: [Top header / Floating button / Tab / Hidden / Not present]
- [ ] **Search bar prominence**: [Always visible / Sticky / Appears on scroll / Hidden by default]
- [ ] **Placeholder text**: [_____]
- [ ] **Time from app open to visible search**: [_____] seconds
- [ ] **Is search accessible on all screens or only some?**: [All / Some / Only on specific screens]
- [ ] **Tap-to-search latency**: [Instant / <500ms / <1s / >1s]

**Framework**: Nielsen #1 (Visibility), Norman (Signifiers)

---

### Search Functionality

- [ ] **Autocomplete present**: [Yes / No]
- [ ] **If yes, autocomplete triggers after**: [1 character / 2-3 characters / Full query submission]
- [ ] **Autocomplete suggestion sources**: [Popular / User history / Trending / Personalized / All]
- [ ] **Sample autocomplete suggestions**: [List 3-5 suggestions for a test query]
- [ ] **Autocomplete accuracy**: [Highly relevant / Mostly relevant / Mixed / Off-topic] (1-5 scale: [___])
- [ ] **Number of autocomplete suggestions shown**: [_____]
- [ ] **Search latency** (from submit to results): [<500ms / <1s / 1-3s / >3s]
- [ ] **Search results relevance** (1-5 scale): [_____]
- [ ] **Result ordering**: [By relevance / By popularity / By recency / By engagement / Random]
- [ ] **Number of results returned**: [_____]

**Framework**: JTBD (Locate), HEART (Task Success), Hook (Variable Reward)

---

### Search Results Page

- [ ] **Result layout**: [Grid / List / Cards / Mixed]
- [ ] **Information per result**: [Title only / Title + thumbnail / Title + metadata / Rich card]
- [ ] **Metadata shown**: [Rating / Views / Duration / Price / Author / Release date / Other: _____]
- [ ] **Result consistency**: [All same format / Some variation / Inconsistent]
- [ ] **Result visual clarity**: [Obvious what to tap / Somewhat clear / Unclear] (1-5 scale: [___])
- [ ] **CTA button**: [Clear ("Play", "View", etc.) / Implicit (tap anywhere) / Unclear]
- [ ] **No results state**: [Helpful message / Confusing / Blank / Error message]

**Framework**: Nielsen #1 (Visibility), Norman (Affordances)

---

### Filtering & Refinement

- [ ] **Filters present**: [Yes / No / Only on some result types]
- [ ] **Filter types available**: [Difficulty / Duration / Language / Rating / Price / Category / Date / Other: _____]
- [ ] **Filter UI**: [Checkboxes / Toggles / Sliders / Dropdowns / Multi-select / Other]
- [ ] **Number of filter options in largest category**: [_____]
- [ ] **Filter persistence**: [Filters stay applied / Reset on navigation / Not applicable]
- [ ] **Filter count feedback**: [Shows "X results" when filters applied / No count / Not applicable]
- [ ] **Time to apply 2-3 filters**: [_____] seconds
- [ ] **Effectiveness of filters** (1-5 scale): [_____]

**Framework**: HEART (Task Success), Norman (Mapping)

---

### Category / Browse Navigation

- [ ] **Categories visible**: [Yes / Prominent / Hidden in menu / Not present]
- [ ] **Number of top-level categories**: [_____]
- [ ] **Category breadth**: [Flat structure / Single-level / Multi-level / Hierarchical]
- [ ] **Category naming clarity**: [Obvious / Clear / Ambiguous / Jargon-heavy] (1-5 scale: [___])
- [ ] **Category organization**: [Alphabetical / By popularity / By relevance / Random]
- [ ] **Subcategories present**: [Yes / No]
- [ ] **Time to browse and find specific content**: [_____] seconds

**Framework**: JTBD (Locate), Nielsen #6 (Recognition)

---

### Trending / Popular / Recommendations

- [ ] **Trending section visible**: [Yes, prominent / Yes, but hidden / Not present]
- [ ] **Trending update frequency**: [Real-time / Daily / Weekly / Static]
- [ ] **Trending relevance** (1-5 scale): [_____]
- [ ] **Recommendations visible**: [Yes, personalized / Yes, generic / Not visible]
- [ ] **Recommendation logic**: [Algorithmic / Curated / Editor-picked / Hybrid]
- [ ] **Social proof shown** (ratings, views, reviews): [Yes / Partial / No]
- [ ] **Content freshness** (1-5 scale, 5 = different each visit): [_____]

**Framework**: Hook (Variable Reward), HEART (Engagement)

---

### Discovery Beyond Search

- [ ] **Related content suggestions**: [Present / Not present]
- [ ] **Curated collections** ("Best of", "Staff picks"): [Present / Not present]
- [ ] **User reviews/comments visible**: [Yes / No]
- [ ] **Social discovery** ("Friends are reading"): [Present / Not present]
- [ ] **Personalization signals**: ["Based on your history", "Because you watched", etc. / No signals]

**Framework**: Hook (Variable Reward), HEART (Engagement, Happiness)

---

### Overall Discovery Effectiveness

- [ ] **Number of distinct discovery paths**: [Search only / 2 paths / 3+ paths]
- [ ] **Likelihood user finds content they want**: [Very likely / Likely / Uncertain / Unlikely] (estimation)
- [ ] **Time to find specific content** (estimate for common task): [<30 sec / 30-60 sec / 1-3 min / >3 min]
- [ ] **Serendipitous discovery** (1-5 scale, 5 = high): [_____]

**Framework**: JTBD (Locate), HEART (Engagement)

---

## KEY ISSUES TEMPLATE

### Issue #1: Search is Hidden or Non-Prominent
**Problem**: Search functionality is not visible on the main screen. Users must navigate to a menu or tab to access search.

**Framework Cite**:
- **Nielsen #1 (Visibility)**: Search should always be visible and accessible. Hidden search breaks visibility.
- **JTBD Locate**: If search is hard to find, the Locate step becomes friction-laden.
- **Norman (Signifiers)**: Search affordance must be obviously visible (magnifying glass icon, search bar, etc.).

**Evidence**: Screenshots showing search bar location (or lack thereof). Document time to find search function.

**Quantified Impact**: Apps with non-visible search see 30-50% lower search usage. Users resort to browsing instead, which is slower for finding specific content.

**Hypothesis for Improvement**:
1. Move search to sticky header (always visible)
2. Use recognizable magnifying glass icon if text space is limited
3. Test with 5-10 users: "Find a specific [content type]. Where would you tap first?" Should be search, not "Browse"

Estimated impact: 40-60% increase in search usage, 25% faster content discovery.

**Comparative Benchmark**: YouTube, Google, Amazon all place search in sticky header. Spotify has search as one of bottom tabs (always accessible).

---

### Issue #2: Search Results Are Irrelevant or Inconsistent
**Problem**: Searching for "Python" returns results for "Java", "Ruby", and random courses. Search algorithm doesn't understand user intent.

**Framework Cite**:
- **JTBD Locate**: Search must help users find what they actually want. Irrelevant results fail the Locate step.
- **HEART Task Success**: Users cannot complete their task (find Python course) because search doesn't deliver.
- **Fogg Ability**: Irrelevant results require user to invest more time parsing results. This increases friction.

**Evidence**: Document 3-5 search queries and their results. Highlight irrelevant results. Screenshot before/after.

**Quantified Impact**: Apps with poor search relevance see 20-40% lower search completion rates. Users give up and browse instead (slower). Bounce rate increases.

**Hypothesis for Improvement**:
1. Improve search algorithm: Implement semantic understanding (not just keyword matching)
2. Add filters to narrow results: Category, difficulty, language
3. Test relevance: For top 10 queries, measure % of relevant results. Target >80% relevance.
4. Consider AI-powered search: Use embeddings to understand "Python programming" vs. "Python snake"

Estimated impact: 30-50% improvement in search completion rate, 20% improvement in time to find content.

**Comparative Benchmark**: YouTube ranks by view count + engagement (relevance), not just keyword match. Spotify understands you're looking for music genre, not the reptile.

---

### Issue #3: Autocomplete Missing or Generic
**Problem**: Search bar has no autocomplete. User must type complete query. Or autocomplete shows irrelevant suggestions ("python" shows "java", "coding", "random").

**Framework Cite**:
- **Hook Model**: Autocomplete provides quick rewards (easy navigation). Missing autocomplete = friction that breaks the action→reward cycle.
- **Nielsen #6 (Recognition)**: Autocomplete helps users recognize what they want (they see it in suggestions) rather than recall the exact name.
- **Fogg Ability**: Typing complete queries requires more brain cycles. Autocomplete reduces cognitive load.

**Evidence**: Screenshots of search bar while typing (show autocomplete or lack thereof). Document autocomplete quality.

**Quantified Impact**: Apps with smart autocomplete see 40-60% higher search completion rates and 30% faster search times. Users find content faster with suggestions.

**Hypothesis for Improvement**:
1. Implement contextual autocomplete: Suggest popular searches, trending content, user history
2. Prioritize by relevance: Show "Python Programming" before "Python Cooking"
3. Add trending indicator: Show "🔥 Trending now" in autocomplete
4. Test with users: Type "pyt..." and see what appears. Should be Python-related first, not random.

Estimated impact: 35-50% improvement in search completion, 25% reduction in time to find content.

**Comparative Benchmark**: YouTube shows popular searches and trending. Amazon shows "customers also searched for". Both help users complete searches faster.

---

### Issue #4: Limited Discovery Paths (Only Search, No Browse/Trending)
**Problem**: App only has search. No browse categories, no trending section, no recommendations. Users must know exactly what they want to find it.

**Framework Cite**:
- **JTBD Locate**: Some users come to the app without a specific search query. They want to browse and discover. Search-only breaks Locate for this persona.
- **Hook Model**: Without trending/recommendations, there's no "Variable Reward" discovery. Every visit, user sees same content (if they search same thing).
- **HEART Engagement**: Multiple discovery paths increase engagement. Browse + search + recommendations keep users in app longer.

**Evidence**: Screenshots showing all available discovery mechanisms. Document what's missing.

**Quantified Impact**: Apps with multiple discovery paths see 50-100% higher engagement and 20-30% higher retention. Users spend more time browsing if paths are available.

**Hypothesis for Improvement**:
1. Add a "Browse" or "Categories" tab: Organize content by type, difficulty, language
2. Add a "Trending" section: Show popular content from the past 24-48 hours
3. Add "Recommended for you": Personalized recommendations based on history
4. Test impact: Compare sessions with search-only vs. with multi-path discovery. Measure engagement.

Estimated impact: 40-60% increase in session length, 20-30% improvement in daily engagement.

**Comparative Benchmark**: Spotify has Search + Browse (by mood, genre) + Your Library + New Releases + Recommendations. Multiple paths = high engagement.

---

### Issue #5: Filters Are Missing or Ineffective
**Problem**: Search results show 500 items with no way to filter. Or filters are present but don't actually narrow results. User is stuck.

**Framework Cite**:
- **HEART Task Success**: Users cannot complete their task (find Python for beginners) because they can't filter by difficulty.
- **JTBD Locate**: Filters are critical for Locate when there are many options. Without them, Locate becomes impossible.
- **Fogg Ability**: Without filters, user must scroll through 500 items (high friction). With filters, they see 20 (low friction).

**Evidence**: Screenshots of search results with filter options (or lack thereof). Test a filter and document whether result count changes.

**Quantified Impact**: Apps with powerful filters see 50% reduction in time to find content and 30% higher user satisfaction. Apps without filters see high bounce on search results.

**Hypothesis for Improvement**:
1. Identify top filtering dimensions: Difficulty, Duration, Language, Price, Rating, Recency, Teacher
2. Make filters obviously accessible: Horizontal filter bar above results or side panel
3. Show result count: "Showing 23 results" when filters applied (proof that filtering worked)
4. Add "Popular in X" filter: Show trending content within a category

Estimated impact: 40-60% reduction in time to find content, 25% improvement in search satisfaction.

**Comparative Benchmark**: Amazon shows faceted filters (Brand, Price, Rating, Shipping Speed). E-commerce apps use filters as primary discovery mechanism.

---

### Issue #6: Results Page is Confusing or Inconsistent
**Problem**: Search results show items in different formats (some are cards, some are list items). CTA button location varies. User is confused about which result to click.

**Framework Cite**:
- **Nielsen #4 (Consistency)**: Results should all be formatted consistently. Inconsistency creates confusion.
- **Norman Affordances**: Each result card should look equally clickable. Inconsistent formatting breaks affordances.
- **HEART Task Success**: Users cannot decide which result to click because format is inconsistent.

**Evidence**: Screenshots of 5-10 results showing inconsistent formatting. Highlight variations in layout, CTA placement, metadata shown.

**Quantified Impact**: Apps with inconsistent result formatting see 20-30% lower click-through rates. Users hesitate before clicking because they're unsure.

**Hypothesis for Improvement**:
1. Standardize result card format: All cards show [thumbnail + title + metadata + CTA]
2. Consistent CTA placement: All buttons in same location (bottom-right, or inline)
3. Consistent metadata: All show rating, duration, or relevant metrics
4. Test visual clarity: Show results to 5 users and ask "Click the one you want." Should be >90% success rate.

Estimated impact: 20-30% improvement in click-through rate, faster user decisions.

**Comparative Benchmark**: YouTube result cards are consistent (thumbnail + title + creator + view count). Easy to scan and compare.

---

## SPEED MODE vs RIGOR MODE

### SPEED MODE (15-20 minutes)
1. **Tap search** → Is it visible? How prominent?
2. **Try a search query** → How relevant are results? How fast?
3. **Check autocomplete** → Present or absent? Quality?
4. **Check filters** → Present? Do they work?
5. **Check trending/popular** → Visible? Useful?
6. **Note 2-3 key issues**
7. **Assign score**

**Output**: 1-2 pages with key findings

---

### RIGOR MODE (45-60 minutes)
1. Search bar audit (visibility, prominence, accessibility)
2. Search functionality (query, latency, results relevance)
3. Autocomplete quality (suggestions, accuracy, trending)
4. Category/browse structure (organization, naming, clarity)
5. Filters (types, UI, effectiveness, feedback)
6. Trending/recommendations (freshness, personalization, relevance)
7. Results page design (layout, metadata, CTA clarity)
8. No results state (message, recovery path)
9. Multiple discovery paths (search + browse + trending + recommendations)
10. Full Evidence Checklist completion
11. 5-7 key issues with benchmarks
12. Detailed score justification

**Output**: 5-10 pages with comprehensive analysis

---

## PERSONA-SPECIFIC INSTRUCTIONS

### 1. Intent-Driven User (Knows What They Want)
**Test**: Can they find it via search in <30 seconds?

**Key Metrics**: Search speed, autocomplete quality, result relevance

**Scoring Focus**: Search functionality, result quality

---

### 2. Serendipitous Browser (Browsing to Discover)
**Test**: Can they discover new content via browse/trending/recommendations?

**Key Metrics**: Content variety, freshness, engagement

**Scoring Focus**: Browse structure, trending relevance, recommendation freshness

---

### 3. Filtering Power User (Wants to Narrow Results)
**Test**: Can they apply multiple filters to find exact content?

**Key Metrics**: Filter availability, effectiveness, ease of application

**Scoring Focus**: Filter implementation, result count feedback

---

## DOMAIN-SPECIFIC OVERLAYS

### Education Apps
- **Domain criteria**: Can students find courses by topic, level, instructor?
- **Scoring modifier**: +1 if difficulty filters clearly visible; -1 if hidden

### OTT / Streaming
- **Domain criteria**: Can users find movies/shows by genre, rating, trending?
- **Scoring modifier**: +1 if trending is real-time; -1 if static

### E-commerce
- **Domain criteria**: Powerful search and faceted filters essential
- **Scoring modifier**: +1 if filters show result count; -1 if filters don't work

---

## INDIA-SPECIFIC CHECKS

Every review of an Indian app must include these checks for this module:

### Hindi Voice Search
- [ ] Is voice search input available (microphone icon in search bar)?
- [ ] Does voice search work in Hindi? In regional languages?
- [ ] Does the app handle Hinglish queries (mixed Hindi-English, e.g., "business kaise start kare")?
- [ ] Is there a voice search onboarding tooltip for first-time users?
- [ ] Impact if missing: Google reports 30%+ of Indian searches are voice-based. Flipkart doubled Tier 2 search volume after adding Hindi voice search. Missing voice search means 20-30% of potential search queries from Tier 2-3 are never initiated.

**Finding template:** "Search is text-only. No voice input available. Hindi/Hinglish queries return no results or English-only results. For Tier 2-3 India where voice is often the primary input method, this is a critical discovery gap."

**India Benchmark:** Flipkart added Hindi voice search → 2x search volume from Tier 2, voice search users convert at 1.3x rate of text-only.

### Browse > Search for Tier 2-3
- [ ] Is browse-based discovery available (visual categories, trending sections)?
- [ ] Can users discover content without typing anything?
- [ ] Are there "Trending in Hindi" or "Popular in [Region]" sections?
- [ ] Is WhatsApp deep-link sharing available as a discovery channel?
- [ ] Impact if missing: Tier 2-3 users prefer browsing over search (Meesho: 55% browse-only sessions). Search-dependent discovery alienates the majority of India's mobile users.

**Finding template:** "Discovery relies entirely on search. No browse-friendly content categories, no trending sections, no regional discovery. Tier 2-3 users who browse rather than search (majority of Indian mobile users) have no discovery path."

**India Benchmark:** Meesho's visual category browsing drives 55% browse-only sessions. Pratilipi's genre-based discovery accounts for 45%+ of content starts. Kuku FM's browse-first approach drives 60%+ of new content discovery.

### Regional Trending & Hinglish Query Handling
- [ ] Are trending topics/searches localized by language or region?
- [ ] Does search autocomplete work in Hindi (Hindi script input)?
- [ ] Does search understand transliterated Hindi (Roman script Hindi)?
- [ ] Are search results ranked by regional relevance?
- [ ] Impact if missing: Indian users search in multiple scripts. An app that only indexes English content fails when users type in Hindi or Hinglish.

**Finding template:** "Search autocomplete is English-only. Typing 'बिज़नेस' or 'business kaise kare' returns zero results. Trending section shows global trends, not India/regional trends."

**India Benchmark:** ShareChat has language-specific trending for 15 Indian languages. Josh/Moj regional trending drives 40%+ of video views.

### Scoring Modifiers (India)
- +1 if Hindi voice search is available
- +1 if browse-first discovery with visual categories
- +1 if regional trending/popular sections exist
- -1 if search is text-only with no voice option
- -1 if Hindi/Hinglish queries return zero or irrelevant results
- -2 if discovery is entirely search-dependent with no browse path

---

## OUTPUT FORMAT

```markdown
# CONTENT DISCOVERY & SEARCH — [X]/10

## Evidence Summary

### Search Accessibility
- **Location**: [Top header / Floating / Hidden]
- **Prominence**: [Always visible / Sticky / Hidden by default]
- **Time to find**: [Visible / X seconds to find]

### Search Functionality
- **Autocomplete**: [Yes / No]
- **Autocomplete quality**: [Excellent / Good / Poor]
- **Latency**: [<500ms / <1s / Slow]
- **Result relevance**: [Highly relevant / Mixed / Irrelevant]

### Discovery Paths
- **Search**: [Functional / Broken]
- **Browse categories**: [Present / Missing]
- **Trending**: [Fresh / Static / Missing]
- **Recommendations**: [Personalized / Generic / Missing]

### Filters
- **Available**: [Yes / No / Partial]
- **Types**: [List filter types]
- **Effectiveness**: [Work well / Partially / Broken]

### Key Metrics
- **Likelihood user finds content**: [High / Medium / Low]
- **Estimated time to find content**: [<30 sec / <2 min / >2 min]
- **Discovery variety**: [High / Medium / Low]

### Frameworks Applied
- **JTBD**: Locate step assessed
- **Nielsen**: #1 (Visibility), #6 (Recognition) evaluated
- **Hook Model**: Variable reward quality assessed
- **HEART**: Task Success evaluated

---

## Evidence

### [Screen 1: Search Bar Visibility]
- **Location & prominence**: [Description]
- **Placeholder text**: [Quote]
- **Accessibility**: [Always visible / Contextual / Hidden]
- **Framework cite**: Nielsen #1

### [Screen 2: Search Results]
- **Result relevance**: [Quality of results for test query]
- **Result layout**: [Format, metadata, consistency]
- **CTA clarity**: [Obvious / Subtle / Unclear]
- **Framework cite**: HEART (Task Success)

### [Screen 3: Autocomplete]
- **Present**: [Yes / No]
- **Quality of suggestions**: [Relevant / Generic / Off-topic]
- **Speed**: [Instant / Delayed]
- **Framework cite**: Hook (Variable Reward)

### [Screen 4: Filters]
- **Types available**: [List]
- **Ease of use**: [Obvious / Learnable / Confusing]
- **Result feedback**: [Shows count / No feedback / N/A]
- **Framework cite**: HEART (Task Success)

### [Screen 5: Trending/Recommendations]
- **Visible**: [Prominent / Hidden / Not present]
- **Freshness**: [Variable / Static / N/A]
- **Personalization**: [Evident / Generic / None]
- **Framework cite**: Hook (Variable Reward)

---

## Scoring Breakdown

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Search accessibility | [X]/10 | [Search is always/sometimes/not visible] |
| Search relevance | [X]/10 | [Results match query well/poorly] |
| Autocomplete quality | [X]/10 | [Autocomplete helpful/absent/generic] |
| Filter functionality | [X]/10 | [Filters work well/partially/missing] |
| Browse structure | [X]/10 | [Categories logical/confusing/missing] |
| Trending/recommendations | [X]/10 | [Fresh/variable/stale/missing] |
| Discovery path variety | [X]/10 | [Multiple paths/single path/limited] |
| Overall effectiveness | [X]/10 | [User can find content easily/with effort/with difficulty] |

**Total Score: [X.X] → [X]/10**

**Justification**: [2-3 sentences grounded in frameworks]

---

## Key Issues

### Issue #1: [Title]
**Problem**: [Observation]

**Framework Cite**:
- **[Framework]**: [Principle violated]

**Evidence**: [Specific findings]

**Quantified Impact**: [User impact]

**Hypothesis for Improvement**: [Solution]

**Comparative Benchmark**: [How do leading apps handle this?]

---

## Recommendations (Prioritized)

### P0 (Critical)
1. **[Issue affecting >50% of searches or Locate step]**
   - Recommendation: [Specific change]
   - Expected impact: [Estimated lift in discoverability]

---

**Review Conducted**: [Date] | **Reviewer**: [Name] | **Duration**: [Mode]
```

---

## Summary

This module evaluates content discovery and search—the critical "Locate" step in the JTBD framework. It assesses whether users can find what they want through search, browse, trending, or recommendations. Grounded in JTBD (Locate), Nielsen (Visibility, Recognition), HEART (Task Success), and Hook Model (Variable Rewards), this module identifies friction in discovery and provides actionable recommendations for improving engagement through better content findability.

