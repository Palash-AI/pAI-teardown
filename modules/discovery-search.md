# Content Discovery & Search

> AARRR: Engagement | Frameworks: JTBD (Locate), Nielsen #1/#6, HEART (Task Success), Hook Model, Norman | Speed: 15-20min | Rigor: 45-60min

<!-- SPEED MODE -->
## QUICK AUDIT
Navigate: 1. Search bar prominence 2. Try one search query 3. Check autocomplete 4. Scan filters 5. Check trending/popular 6. Browse categories
Check: Search visibility (always accessible?), result relevance (1-5), autocomplete quality (present/absent), discovery paths (search + browse + trending?), time to find content
Score anchor: 9-10 = Always-visible search + highly relevant results + smart autocomplete + multiple discovery paths, 7-8 = Accessible search + mostly relevant + some autocomplete + 2-3 paths, 5-6 = Search present but not prominent + mixed relevance + basic discovery, 3-4 = Search hidden or slow + poor relevance + limited paths, 1-2 = Search broken or missing + no discovery
<!-- END SPEED MODE -->

## SCREENS TO NAVIGATE

### 1. Search Bar Visibility & Prominence
**Observe:**
- Location (top header, floating, hidden in tab, not present)
- Prominence (full-width, icon button, tucked in menu)
- Placeholder text (helpful or generic)
- Accessibility (always available, contextual, screen-dependent)
- Tap-to-search latency

**Screenshot:** Full screen with search bar, zoomed view of placeholder text, focused state

**Framework check:** Nielsen #1 → Is search always visible and easy to find?

---

### 2. Search Flow & Results Quality
**Observe:**
- Search input type (single field, multi-field, voice)
- Autocomplete (present while typing, after submit, none)
- Search latency (seconds to first results)
- Results presentation (grid, list, cards)
- Results relevance (match query or generic/wrong)
- Result information density (title only, thumbnail + title, rich preview)
- Result ordering (relevance, popularity, recency, random)
- No results state messaging

**Screenshot:** Query entered, autocomplete suggestions, full results page, zoomed result card, no results state, filters visible

**Framework check:** JTBD Locate → Do results help user find what they came for?

---

### 3. Search Autocomplete & Suggestions
**Observe:**
- Autocomplete triggers (1 char, 2-3 chars, none)
- Suggestion sources (popular searches, user history, trending, personalized)
- Suggestion accuracy (relevant, off-topic, mixed)
- Suggestion count and formatting
- Trending/popular highlighting

**Screenshot:** 1-2 chars entered with suggestions, full dropdown, comparison of different queries

**Framework check:** Hook Model → Does autocomplete provide quick, variable rewards?

---

### 4. Category / Browse Navigation
**Observe:**
- Category visibility (present, hidden, missing)
- Category breadth and depth (flat, single-level, hierarchical)
- Category naming clarity (obvious, clear, ambiguous, jargon)
- Category navigation type (tabs, dropdown, grid, list, sidebar)
- Category organization (alphabetical, popularity, relevance)
- Content within category organization

**Screenshot:** Homepage/Browse screen with all categories, one category expanded, content items visible

**Framework check:** JTBD Locate → Can user browse categories and find content by interest?

---

### 5. Filters & Refinement Options
**Observe:**
- Filter availability (search results, browse, hidden, menu)
- Filter types (difficulty, duration, language, rating, price, etc.)
- Filter UI (checkboxes, toggles, sliders, dropdowns)
- Filter persistence (stay applied, reset on navigation)
- Result count feedback (visible or not)
- Filter reset option (clear all, must uncheck individually, not possible)
- Smart filtering (suggested by app or manual)

**Screenshot:** Search/browse with filters visible, filters expanded, filters applied, before/after result count

**Framework check:** HEART Task Success → Do filters help users narrow results effectively?

---

### 6. Trending / Popular / Recommended Content
**Observe:**
- Trending section (present, missing, automatic)
- Trending source (app-wide, per-category, personalized)
- Trending update frequency (real-time, daily, weekly, unknown)
- Recommendation logic (algorithmic, personalization, editor-curated, mixed)
- Content freshness (same every day, rotates, personalized)
- Social proof signals (ratings, reviews, view count)

**Screenshot:** Trending/popular section, individual items with signals, "Trending now" vs. "Trending in category"

**Framework check:** Hook Model Variable Reward → Is content fresh/variable or repetitive?

---

### 7. Search Result Page Design
**Observe:**
- Result layout (grid, list, card stack, mixed)
- Result information (minimal, moderate, rich)
- Visual treatment (thumbnails, icons, plain text, video previews)
- Result consistency (same format or variation)
- Metadata shown (rating, reviews, duration, price, author, date)
- CTA clarity ("View", "Play", tap anywhere, unclear)
- Load more mechanism (pagination, infinite scroll, load button)
- Empty state messaging

**Screenshot:** Full results page with 5-10 items, zoomed result card, no results state, pagination control

**Framework check:** Nielsen #1 → Is the result page structure clear? Norman Affordances → Does each result look clickable?

---

### 8. Discovery Mechanisms Beyond Search
**Observe:**
- Recommendation engine visibility (visible or hidden)
- Related content (shown after viewing item)
- Curated collections ("Best of X", "Staff picks")
- User-generated discovery (comments, ratings, reviews visible)
- Social discovery ("Friends are reading X")
- Personalization signals (proof of personalization or generic)

**Screenshot:** Recommendation section, curated collection, related content after viewing

**Framework check:** Hook Model → Do discovery surfaces provide variable rewards?

---

## SCORING RUBRIC

| Score | Label | Key Criteria |
|-------|-------|-------------|
| 9-10 | Best-in-class | Always-accessible search, highly relevant results, smart autocomplete with trending visible, multiple discovery paths (search + browse + trending + recommendations), powerful filters with visible counts, clear result pages, <1 sec latency, evident personalization, variable content freshness |
| 7-8 | Good | Accessible search header, mostly relevant results, helpful autocomplete, 2-3 discovery paths, basic filters, clear results, minor latency, some personalization, mostly variable content |
| 5-6 | Adequate | Search in menu/tab (not always visible), mixed relevance, absent/basic autocomplete, limited discovery paths, filters hard to find, confusing results, moderate latency, minimal/generic personalization, repetitive content |
| 3-4 | Poor | Search hidden/hard to find, irrelevant results, no autocomplete, limited to browse only, no/broken filters, confusing result pages, significant latency, no personalization, static content |
| 1-2 | Critical | No search, broken results, no discovery mechanisms, extreme friction, all content behind paywall, heavy ads/spam in discovery surface |

**Scoring method**: Start at 5. Add: +2 for always-visible search, +1 for high relevance, +1 for smart autocomplete, +1 for 3+ discovery paths, +1 for effective filters, +1 for clear results, +1 for <1 sec latency, +1 for evident personalization. Deduct: -2 for hidden/slow search, -2 for poor relevance, -1 for no autocomplete, -1 for single discovery path, -1 for broken filters, -1 for confusing results, -1 for ads/spam.

---

## EVIDENCE CHECKLIST

### Search Bar Accessibility
- [ ] Search bar location: [Top header / Floating / Tab / Hidden / Not present]
- [ ] Placeholder text: [_____]
- [ ] Always visible or contextual: [All screens / Some / Only specific screens]
- [ ] Tap-to-search latency: [Instant / <500ms / <1s / >1s]
**Framework**: Nielsen #1

---

### Search Functionality
- [ ] Autocomplete present: [Yes / No]
- [ ] Autocomplete triggers after: [1 char / 2-3 chars / Full query / Never]
- [ ] Suggestion sources: [Popular / User history / Trending / Personalized]
- [ ] Autocomplete accuracy (1-5): [_____]
- [ ] Search latency (submit to results): [<500ms / <1s / 1-3s / >3s]
- [ ] Results relevance (1-5): [_____]
- [ ] Result ordering: [Relevance / Popularity / Recency / Random]
- [ ] Number of results returned: [_____]
**Framework**: JTBD, HEART, Hook

---

### Search Results Page
- [ ] Result layout: [Grid / List / Cards / Mixed]
- [ ] Information per result: [Title only / Title + thumbnail / Rich card]
- [ ] Metadata shown: [Rating / Views / Duration / Price / Author / Date]
- [ ] Result consistency: [All same / Variation / Inconsistent]
- [ ] Visual clarity (1-5): [_____]
- [ ] CTA button: [Clear / Implicit / Unclear]
- [ ] No results state: [Helpful message / Confusing / Blank]
**Framework**: Nielsen #1, Norman

---

### Filters & Refinement
- [ ] Filters present: [Yes / No / Only on some]
- [ ] Filter types: [Difficulty / Duration / Language / Rating / Price / Other]
- [ ] Filter UI: [Checkboxes / Toggles / Sliders / Dropdowns / Multi-select]
- [ ] Filter persistence: [Stay applied / Reset / Not applicable]
- [ ] Result count feedback: [Shows count / No feedback / Not applicable]
- [ ] Effectiveness (1-5): [_____]
**Framework**: HEART, Norman

---

### Category / Browse Navigation
- [ ] Categories visible: [Yes / Prominent / Hidden / Not present]
- [ ] Number of top-level categories: [_____]
- [ ] Category breadth: [Flat / Single-level / Multi-level / Hierarchical]
- [ ] Category naming clarity (1-5): [_____]
- [ ] Category organization: [Alphabetical / Popularity / Relevance / Random]
**Framework**: JTBD, Nielsen #6

---

### Trending / Popular / Recommendations
- [ ] Trending visible: [Yes, prominent / Yes, hidden / Not present]
- [ ] Trending update frequency: [Real-time / Daily / Weekly / Static]
- [ ] Trending relevance (1-5): [_____]
- [ ] Recommendations: [Personalized / Generic / Not visible]
- [ ] Content freshness (1-5, 5 = different each visit): [_____]
- [ ] Social proof shown: [Yes / Partial / No]
**Framework**: Hook, HEART

---

### Discovery Beyond Search
- [ ] Related content: [Present / Not present]
- [ ] Curated collections: [Present / Not present]
- [ ] User reviews/comments visible: [Yes / No]
- [ ] Social discovery: [Present / Not present]
- [ ] Personalization signals: [Visible / None]
**Framework**: Hook, HEART

---

### Overall Effectiveness
- [ ] Number of distinct discovery paths: [Search only / 2 paths / 3+ paths]
- [ ] Likelihood user finds content: [Very likely / Likely / Uncertain / Unlikely]
- [ ] Time to find specific content: [<30 sec / 30-60 sec / 1-3 min / >3 min]
- [ ] Serendipitous discovery (1-5): [_____]
**Framework**: JTBD, HEART

---

## KEY ISSUE PATTERNS

1. **Search Hidden or Non-Prominent** → Detect: Search in menu or tab, not sticky header. Framework: Nielsen #1. Fix: Move to sticky top header; use magnifying glass icon if space limited.

2. **Search Results Irrelevant or Inconsistent** → Detect: Searching "Python" returns unrelated results; poor algorithm. Framework: JTBD Locate. Fix: Improve relevance algorithm; add filters; implement semantic understanding.

3. **Autocomplete Missing or Generic** → Detect: No autocomplete or suggestions unrelated to query. Framework: Hook Model. Fix: Add contextual autocomplete; prioritize by relevance; show trending.

4. **Limited Discovery Paths (Search Only)** → Detect: Only search available; no browse/trending/recommendations. Framework: Hook Model. Fix: Add browse categories, trending section, personalized recommendations.

5. **Filters Missing or Ineffective** → Detect: 500+ results with no filter option or filters don't work. Framework: HEART Task Success. Fix: Add key filter dimensions; show result count; make filters accessible.

6. **Result Page Confusing or Inconsistent** → Detect: Results in different formats, unclear CTA location. Framework: Nielsen #4. Fix: Standardize card format; consistent CTA placement; consistent metadata.

7. **No Personalization or Variable Rewards** → Detect: All users see same generic content; same items every visit. Framework: Hook Model. Fix: Implement personalization based on history; rotate content freshness.

8. **Poor Empty State or No Results Messaging** → Detect: Blank page or confusing error when no results. Framework: Nielsen #10. Fix: Suggest related searches; show example content; provide refine path.

---

## OUTPUT FORMAT

```markdown
# CONTENT DISCOVERY & SEARCH — [X]/10

## Evidence Summary
- **Search accessibility**: [Location, always visible?, latency]
- **Search quality**: [Relevance 1-5, latency, result ordering]
- **Autocomplete**: [Present/absent, quality 1-5]
- **Discovery paths**: [Search, Browse, Trending, Recommendations present/missing]
- **Filters**: [Available, types, effectiveness 1-5]
- **Personalization**: [Evident, generic, none]

## Key Metrics
- **Time to find content**: [<30 sec / 30-60 sec / 1-3 min / >3 min]
- **Discovery variety**: [High / Medium / Low]
- **Friction level**: [Low / Moderate / High]

## Frameworks Applied
- **JTBD Locate**: User can find content they came for
- **Nielsen #1, #6**: Search visibility and recognition
- **HEART Task Success**: Users complete search tasks
- **Hook Model**: Discovery provides variable rewards

## Scoring Breakdown

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Search accessibility | [X]/10 | [Always/sometimes/not visible] |
| Search relevance | [X]/10 | [Results match query well/poorly] |
| Autocomplete quality | [X]/10 | [Helpful/absent/generic] |
| Discovery paths | [X]/10 | [Multiple/limited/single] |
| Filters | [X]/10 | [Effective/partial/missing] |
| Result clarity | [X]/10 | [Clear/confusing/inconsistent] |

**Total Score: [X]/10** | **Justification**: [1-2 sentences grounded in frameworks]

## Key Issues

### Issue #1: [Title]
**Problem**: [What observed] | **Framework**: [Name] | **Impact**: [User impact] | **Fix**: [1-line solution]

### Issue #2: [Title]
[Same structure]

### Issue #3: [Title]
[Same structure]

## Recommendations

### P0 (Critical)
[Issues affecting >50% of searches or Locate step]

### P1 (High)
[Issues affecting 20-50% of searches]

**Review Conducted**: [Date] | **Duration**: [Speed / Rigor]
```
