# pAI Teardown Skill — India-Groundedness Audit

> **Date:** 2026-03-01
> **Auditor role:** Senior India Consumer Product Strategist + Growth & Monetization Expert
> **Method:** Full end-to-end audit of all 10 full/ module files — Observations, Benchmarks, Key Issues, Recommendations, Roadmap, KPIs.
> **Scoring:** A (India-native), B (Has some India context), C (Generic international), D (Almost entirely Western), F (Completely Western-centric)

---

## Gap Matrix

| Module | Lines | Observations | Benchmarks | Key Issues | Recs/Roadmap/KPIs | Intl Apps Cited | India Apps Cited | Grade | Notes |
|--------|-------|-------------|-----------|------------|-------------------|-----------------|-----------------|-------|-------|
| **Monetization** | 991 | A | B+ | B+ | B | 8 (Duolingo, Reforge) | Unacademy ×2 only | **B+** | Best module. Has India section (UPI, ₹ pricing, family plans, ₹1 trial, regional pricing, Hindi copy). Benchmarks still lean Duolingo/Reforge — no CRED pricing, Meesho referral, Zepto trial, Flipkart annual plan. Observations are India-aware. |
| **Content Consumption** | 857 | B- | C+ | C | C | 8 (Netflix, YouTube, Apple TV, Spotify) | 0 | **C** | Has "Tier 2-3 Low-Connectivity" persona but observations don't specifically ask about download quality options (360/480/720p), data usage warnings, WiFi vs mobile data prompts, or data-saver mode. Benchmarks: Netflix, YouTube, Spotify only. |
| **Onboarding** | 1368 | B- | D+ | C | C | 32 (Duolingo ×12, Slack ×5, Notion ×4, Calm ×3, etc.) | 0 | **C-** | Observations miss India auth (Truecaller auto-fill, WhatsApp login, Google One-Tap, OTP auto-read). 32 intl benchmarks, 0 India. No Meesho 3-screen onboarding, CRED rewards-first, PhysicsWallah class-first. |
| **Engagement-Retention** | 952 | B- | D | C | C | 17 (Duolingo ×8, Headspace ×2, Strava ×2, Peloton ×2) | 0 | **C-** | Observations miss WhatsApp re-engagement, 8-11 PM peak timing, cricket season strategy, Hindi notification copy. Benchmarks: only Duolingo, Headspace, Strava, Peloton. Missing: CRED coins, Dream11, Meesho referrals, Josh/Moj. |
| **Homepage IA** | 917 | B- | D | C | C | 7 (YouTube ×3, Apple, Spotify ×2, Notion, Netflix, etc.) | 0 | **C-** | Observations miss data-light loading, skeleton loaders, lazy-loading for slow 4G. Benchmarks: YouTube, Apple, Spotify, Notion. Missing: Flipkart deal-first IA, Swiggy location-first, Meesho browse-first. |
| **Discovery-Search** | 861 | C+ | D | C | C | 8 (YouTube ×5, Spotify ×3, Amazon ×3, Google) | 0 | **D+** | **Voice search completely absent from observations** — critical for Tier 2-3 India. Hindi search, Hinglish queries not mentioned. Benchmarks: YouTube, Spotify, Amazon. Missing: Flipkart Hindi voice search, Meesho visual search, Pratilipi genre browsing. |
| **Personalization** | 821 | C+ | D | C | C | 7 (Spotify ×3, Netflix ×3, YouTube, Amazon, Duolingo, Calm) | 0 | **D+** | Observations miss language-as-personalization, tier-based content, regional trending, festival-based personalization. Benchmarks: Netflix, Spotify, Duolingo, Amazon only. No India personalization patterns. |
| **Cognitive Load** | 809 | C+ | D | C | C | 8 (Apple iOS ×3, Google Material ×2, Notion, Slack, etc.) | 0 | **D** | **Observations assume flagship devices.** Missing: budget phone screen sizes (5.5" 720p), outdoor readability, Hinglish label comprehension, low-literacy icon-over-text, animation performance on budget chipsets. Benchmarks: Apple, Google Material only. |
| **AI Integration** | 622 | C | D | C | C | 4 (generic) | 0 | **D** | **Observations are entirely English-centric.** Missing: Hindi/Hinglish AI chat, voice-first AI, AI trust deficit in India, Hindi disclaimers, AI explanation for non-tech-savvy users. No app benchmarks at all. |
| **Persona Alignment** | 792 | C | D | C | C | 8 (Duolingo ×6, Skillshare ×4, Notion ×2, Slack) | 0 | **D** | **No India persona framework in observations.** Doesn't detect Task Finisher/Explorer/Structured Learner. No tier-based persona differences. Every benchmark: Duolingo, Skillshare, Notion, Slack. |

### Benchmark Audit Summary

**Total International App Citations Across All Modules: 107**
Top cited: Duolingo (30+), YouTube (15+), Spotify (12+), Netflix (10+), Notion (8+), Slack (6+), Apple (6+), Amazon (5+)

**Total Indian App Citations Across All Modules: 2**
Both are "Unacademy" in the Monetization module.

**Ratio: 107:2 (53:1 international to India)**

This is the core problem. When a reviewer follows these modules, their Comparative Benchmarks will automatically default to Duolingo, Netflix, Spotify because that's what the templates model. A Tier 2 Indian PM reading "Benchmark: Slack lets power users skip setup" would find this irrelevant — they'd want "Benchmark: Meesho's 3-tap onboarding gets Tier 2 users to first product browse in under 10 seconds."

---

## Summary Diagnosis

### What's Strong
- **Monetization** is the only module with dedicated India sections — UPI, ₹ pricing, regional pricing, Hindi copy, ₹1 trial psychology. This should be the template for how India context gets embedded in every module.
- **india-consumer.md** (236 lines) is a solid foundation — tier segmentation, behavioral patterns, trust signals, competitive context. But it's only *referenced* during review, not *applied* during output generation.
- **india-ref.md** (38 lines) is a crisp delta table. Good for quick loading.
- **Framework coverage in Observations** is genuinely strong — Nielsen, Norman, Fogg, JTBD, Hook, HEART, Kano, Cagan, Reforge are all correctly applied. Evidence checklists are thorough and well-structured.

### Observations Audit — India Gaps Found

The Observations sections are the strongest part of the skill, but they're not clean. After reading all 10 modules' "Screens to Navigate" and "What to Observe" sections end to end, here are the specific India gaps:

**1. Discovery-Search: Voice search completely absent.**
The module covers search bar visibility, autocomplete, filters, trending — but never mentions voice search. For Tier 2-3 India, voice search is often the *primary* discovery method (Hindi voice input). Flipkart added Hindi voice search and saw 2x search volume from Tier 2. Google Search in India is 30%+ voice. The module doesn't ask: "Is voice input available? In what languages? Does it work with Hindi/Hinglish?"

**2. Cognitive Load: Budget device context missing.**
The "What to Observe" checklist evaluates visual hierarchy, typography, spacing — all on an abstract quality scale. It doesn't ask: "Does this work on a 5.5" 720p budget Android? Are touch targets big enough for single-hand operation on a 6.5" phone? Is font readable at default size on a low-brightness outdoor screen? Are animations janky on budget chipsets (Helio G35, Snapdragon 4-series)?"

**3. AI Integration: Language and trust gap.**
The module evaluates AI discoverability, chat quality, recommendations — but entirely in English. No observation prompt for: "Does AI chat work in Hindi? Does it handle Hinglish (mixed Hindi-English) input? Is voice input to AI available? Is there a trust/disclaimer in Hindi? Do Indian users understand what 'AI' means or does the app need to explain it?"

**4. Engagement-Retention: India engagement patterns absent.**
Observations cover Hook Model, streaks, badges, re-engagement — all universal. Missing India-specific observation prompts: "Does the app use WhatsApp for re-engagement? Are notifications timed for 8-11 PM India peak? Is there a cricket/IPL season disruption strategy? Are streaks visible on the WhatsApp share card? Does re-engagement messaging use Hindi/regional language?"

**5. Personalization: Language-as-personalization missing.**
Observations ask about "For You" sections, recommendation quality, JTBD probes — but never ask: "Does the app personalize by language preference? Does it detect Tier 1 vs Tier 2 users and show different content? Does it personalize based on regional context (festivals, local events, state-specific content)?"

**6. Persona Alignment: No India persona framework loaded.**
The module's observation section asks about persona detection and adaptive UX generically. It doesn't reference: "Does the app detect Task Finisher vs Explorer vs Structured Learner? Does it account for tier-based persona differences (Tier 1 Explorer vs Tier 2 Explorer behave differently)? Does it adjust for age-based Indian behavior patterns (Gen Z social-first, Young Millennial career-focused)?"

**7. Homepage IA: Data-light loading not observed.**
Observations evaluate navigation, visual hierarchy, content organization — but don't ask: "Does the homepage load fast on 4G with 3-4 bars? Are images lazy-loaded or does the whole page block? Is there a skeleton loader or does the user see a blank screen? Is above-fold content prioritized for slow connections?"

**8. Onboarding: India-specific auth patterns missing.**
The module's Login/Signup observation is thorough (screens, time, error handling) but doesn't specifically ask: "Is Truecaller auto-fill supported? Does OTP auto-read work? Is WhatsApp login available? Does the app handle Indian phone numbers (+91, 10-digit) correctly? Is Google One-Tap sign-in available (dominant in India Android)?"

**9. Content Consumption: Offline and data-saving observations weak.**
The module mentions "Low-Connectivity User (Tier 2-3)" as a persona but the observation checklist doesn't specifically ask: "Can content be downloaded for offline viewing? What quality options exist (360p, 480p, 720p)? Does the app show data usage per video? Is there a 'data saver' mode? Does it warn before streaming on mobile data vs WiFi?"

**Overall Observations Grade: B — Strong framework coverage but missing ~15-20 India-specific observation prompts across 9 of 10 modules.**

These gaps mean that even when a reviewer follows the observation checklists perfectly, they'll miss India-critical evidence. The fix: add 2-5 India-specific observation prompts to each module's "What to Observe" sections, inside a clearly marked `**India-Specific Observations:**` sub-section.

### What's Broken

1. **Benchmarks are overwhelmingly Western (107:2 ratio).** Across all 10 modules, 107 benchmark citations reference international apps (Duolingo 30+, YouTube 15+, Spotify 12+, Netflix 10+, Notion 8+) vs only 2 Indian app citations (both "Unacademy" in Monetization). This means every Comparative Benchmark in every module defaults to Western products. A reviewer following these templates will produce output that compares an Indian EdTech app to Slack's onboarding rather than Meesho's 3-tap flow.

2. **Key Issues templates are entirely Western-centric.** Example issues cite Duolingo, Notion, Slack, Apple, Netflix. Zero issues cite Meesho, CRED, Zepto, ShareChat, Unacademy, PhysicsWallah, Josh/Moj. An Indian PM reading these would immediately recognize them as "American product review translated."

3. **Recommendations don't account for India constraints.** "Improve recommendation algorithm" doesn't address that 60% of target users prefer Hindi, browse (not search), and compare to YouTube (free). "Add push notifications" doesn't account for WhatsApp as primary re-engagement, 8-11 PM peak times, or cricket season disruption.

4. **Roadmap/KPI sections are absent or generic.** Most modules have a `P0/P1/P2` template but no India-specific prioritization logic. A recommendation might be P0 globally but P2 in India (e.g., "add Apple Pay" is P0 in US but irrelevant in India). Conversely, "add UPI" is P0 in India but wouldn't appear in a Western framework.

5. **Persona Alignment module doesn't load any India personas.** The module talks about personas abstractly but doesn't reference the five actual personas (new-user, free-user, trial-user, paid-user, lapsed-user) or the three behavioral personas (Task Finisher, Explorer, Structured Learner). It's a framework without India-specific content.

6. **Eight modules have zero Indian app benchmarks.** Only Monetization cites an Indian app (Unacademy ×2). The other 9 modules cite exclusively Western apps. Discovery-Search, Cognitive Load, AI Integration, Persona Alignment are the worst — they benchmark against Apple, Google Material, Slack, Skillshare with zero India alternatives.

---

## What Needs to Happen

### Layer 1: New `india-product-strategy.md` Context File
A new file (loaded by orchestrator alongside india-consumer.md) that provides:
- **India-specific Issue Templates** — example issues written with India context (UPI missing, Hindi copy absent, WhatsApp re-engagement missing, budget device performance)
- **India Competitor Benchmark Library** — Meesho, CRED, Zepto, ShareChat, Unacademy, PhysicsWallah, Josh/Moj, Pratilipi with what each does well per module dimension
- **India KPI Benchmarks** — D1/D7/D30 retention norms for India consumer apps, trial→paid conversion by tier, acceptable price points by segment
- **India Roadmap Prioritization Rules** — P0/P1/P2 modifiers (e.g., "if target includes Tier 2-3, language support is P0 not P1")
- **India Recommendation Patterns** — templates for India-native recs (WhatsApp deep links, UPI integration, Hindi onboarding, ₹1 trial with value frontloading, family plans, festival timing, cricket season planning)

### Layer 2: India Sections Added to Each Module
For the 6 India-blind modules (Discovery-Search, Cognitive Load, AI Integration, Persona Alignment, Homepage IA, Personalization), add a dedicated `## INDIA-SPECIFIC CHECKS` section (like Monetization already has). Each section should have:
- India-specific audit checklist items
- India competitor benchmarks for that module dimension
- Finding templates with India context
- Scoring modifiers for India apps

### Layer 3: Design Plugin Integration
Use `design:critique` to strengthen Cognitive Load and Homepage IA modules with structured design feedback methodology. Use `design:ux-writing` to add India-specific copy review criteria (Hinglish, Hindi, regional language assessment) to Onboarding and Monetization.

### Layer 4: Orchestrator Update
Update `appteardown.md` to:
- Explicitly load `india-product-strategy.md` during Step 2 (Context Loading)
- Instruct each module to apply India context during Issues/Recs generation, not just Observations
- Add a "India Fit Check" step after scoring — every recommendation is validated against india-consumer.md

---

## Execution Priority

| Priority | Task | Impact | Effort | Model |
|----------|------|--------|--------|-------|
| **1** | Create `india-product-strategy.md` — India Competitor Benchmark Library + India Issue Templates + India KPI Benchmarks + India Roadmap Rules + India Recommendation Patterns | Highest — single file upgrades all 10 modules' benchmarks, issues, recs, roadmap, KPIs | Medium-High (~400-500 lines, new file) | **Opus** |
| **2** | Add `## INDIA-SPECIFIC CHECKS` sections to 9 modules (all except Monetization which already has one) — India audit checklists, India competitor benchmarks, finding templates, scoring modifiers | High — directly fixes the worst gaps in each module | High (9 modules × ~60-100 lines each) | Sonnet with Opus-written spec |
| **3** | Add `**India-Specific Observations:**` prompts to 9 modules' "What to Observe" sections — voice search, budget devices, Hindi/regional language, WhatsApp, data-saving, India auth patterns | High — fixes observation blindspots that cause evidence to be missed | Medium (9 modules × ~10-20 lines each) | Sonnet with Opus-written spec |
| **4** | Update Monetization India section — expand from Unacademy-only to 5+ India competitor benchmarks (CRED, Meesho, Zepto, Flipkart, PhysicsWallah) | Medium — already good, needs broader benchmark set | Low (~30-50 lines) | Sonnet |
| **5** | Update orchestrator (`appteardown.md`) — load `india-product-strategy.md` in Step 2, add "India Fit Check" after scoring, require India Benchmark in every Comparative Benchmark | Medium — ensures India context is always applied, not optional | Low (~20-30 lines) | Sonnet |
| **6** | Read Anthropic Design plugin skills (`design:critique`, `design:ux-writing`) and integrate references into Cognitive Load, Homepage IA, and Onboarding modules | Low-Medium — sharpens 2-3 modules with structured design feedback and India copy review | Low-Medium | Sonnet |
| **7** | Update Claude.md indexes (skill folder + project folder) to reference new files | Low — navigation only | Very Low | Sonnet |
| **8** | Verification — run a mental test teardown of one module (Onboarding) with the updated files and check: would a Meesho PM find this actionable? | Critical — catches remaining gaps before considering the skill "done" | Low | **Opus** |

---

---

## Detailed Execution Spec (For Sonnet or Opus to Follow)

### Task 1: Create `india-product-strategy.md` (OPUS REQUIRED)

**Location:** `Skills/pAI-teardown/context/india-product-strategy.md`

**Structure:**
```
# India Product Strategy Context — pAI Teardown
## 1. India Competitor Benchmark Library (organized by module dimension)
## 2. India-Specific Issue Templates (5-8 example issues with India framing)
## 3. India KPI Benchmarks (D1/D7/D30 norms, trial→paid by tier, pricing)
## 4. India Roadmap Prioritization Rules (P0/P1/P2 modifiers)
## 5. India Recommendation Patterns (reusable India-native rec templates)
```

**Section 1 — India Competitor Benchmark Library:**
For each of these 15 Indian apps, document what they do well for each relevant module dimension:

| App | Category | Relevant Module Dimensions |
|-----|----------|---------------------------|
| Meesho | Social commerce | Onboarding (3-tap), Homepage IA (browse-first), Personalization (regional), Discovery (visual search), Engagement (referral loops) |
| CRED | Fintech/rewards | Onboarding (rewards-first), Engagement (coins/streaks), Monetization (premium positioning), Cognitive Load (minimal design) |
| Zepto | Quick commerce | Onboarding (address-first), Homepage IA (deal-first), Content Consumption (speed), Cognitive Load (clean) |
| Flipkart | E-commerce | Discovery (Hindi voice search), Homepage IA (personalized deals), Monetization (annual plans, Flipkart Plus), Personalization (tier-based) |
| Swiggy | Food delivery | Homepage IA (location-first), Discovery (category-first), Personalization (time-of-day), Engagement (Swiggy One loyalty) |
| Zomato | Food delivery | Engagement (Gold/Pro loyalty), Monetization (subscription tiers), Content Consumption (restaurant browsing), Cognitive Load (playful UI) |
| Unacademy | EdTech | Onboarding (class-first), Content Consumption (live class + VOD), Monetization (cohort pricing), Engagement (educator-led), Persona (exam-specific) |
| PhysicsWallah | EdTech | Onboarding (exam selection), Monetization (affordable), Content Consumption (long-form lectures), Engagement (community/Telegram), Persona (exam-specific) |
| Josh/Moj | Short video | Engagement (infinite scroll), Content Consumption (autoplay), Discovery (trending by region), Personalization (vernacular algo), Homepage IA (feed-first) |
| ShareChat | Social/regional | Personalization (language-first), Discovery (regional trending), Engagement (creator rewards), Content Consumption (multi-format) |
| Kuku FM | Audio content | Content Consumption (audio-first, offline), Monetization (₹99/month sweet spot), Personalization (language + genre), Discovery (browse-first) |
| Dream11 | Fantasy sports | Engagement (daily contests), Monetization (micro-transactions), Personalization (sport-specific), Onboarding (contest-first) |
| Pratilipi | Vernacular reading | Personalization (language-first), Discovery (genre browsing), Content Consumption (reading UX), Engagement (serialized content) |
| Naukri | Job search | Onboarding (resume-first), Personalization (job-match), Discovery (filter-heavy), Monetization (recruiter-side) |
| BYJU'S | EdTech (cautionary) | What went wrong: aggressive monetization, trust erosion, complex onboarding. Use as negative benchmark. |

For each app, provide 2-3 sentences on what they do well + what metric it impacts. Use web search to verify current state if needed.

**Section 2 — India-Specific Issue Templates:**
Write 5-8 example Key Issues in full format (Problem → Framework Cite → Evidence → Quantified Impact → Hypothesis → Comparative Benchmark) but with India context. Examples:
- "UPI Payment Method Missing" (Monetization)
- "No Hindi/Regional Language Support in Onboarding" (Onboarding)
- "WhatsApp Re-engagement Absent" (Engagement-Retention)
- "Voice Search Not Available for Hindi Users" (Discovery-Search)
- "AI Chat English-Only, No Hindi Support" (AI Integration)
- "Budget Device Performance Not Optimized" (Cognitive Load)
- "No Tier 2-3 Pricing Tier" (Monetization)
- "Content Not Downloadable for Offline Viewing" (Content Consumption)

**Section 3 — India KPI Benchmarks:**
| Metric | India EdTech Norm | India Consumer App Norm | Source/Basis |
|--------|------------------|------------------------|-------------|
| D1 retention | 30-40% | 25-35% | India App Annie data |
| D7 retention | 15-25% | 12-20% | |
| D30 retention | 8-15% | 5-12% | |
| Trial→Paid (Tier 1) | 8-15% | — | |
| Trial→Paid (Tier 2) | 3-8% | — | |
| Acceptable monthly price (Tier 1) | ₹149-249 | ₹99-199 | |
| Acceptable monthly price (Tier 2) | ₹49-99 | ₹29-79 | |
| Free content ratio expected | 40-60% | 60-80% | |
| WhatsApp share rate | 5-10% of active users | 3-8% | |
| Hindi language adoption | 45-55% of users switch if available | — | |

**Section 4 — India Roadmap Prioritization Rules:**
Table of P0/P1/P2 modifiers. Example:
- "If app targets Tier 2-3: Hindi/regional language → P0 (not P1)"
- "If app has subscriptions: UPI payment → P0 (not optional)"
- "If app has content: Offline download → P0 for Tier 2-3"
- "WhatsApp share integration → P1 for any social/content app"
- "Voice search in Hindi → P1 for discovery-heavy apps"
- "Family plan → P2 unless targeting students (then P1)"

**Section 5 — India Recommendation Patterns:**
Reusable templates. Example:
- "Add WhatsApp deep-link sharing with pre-filled Hindi message"
- "Implement ₹1 trial with value-first day (core feature unlocked immediately)"
- "Add Hindi/Hinglish language toggle accessible from every screen"
- "Show data usage per video; add 360p/480p quality options for Tier 2-3"
- "Time push notifications for 7-8 PM IST (pre-peak trigger)"
- "Add Truecaller auto-fill + OTP auto-read for frictionless auth"

---

### Task 2: Add `## INDIA-SPECIFIC CHECKS` to 9 Module Files (SONNET OK)

**For each of these 9 files in `modules/full/`:**
onboarding.md, homepage-ia.md, discovery-search.md, content-consumption.md, engagement-retention.md, cognitive-load.md, personalization.md, persona-alignment.md, ai-integration.md

**Add a section BEFORE the OUTPUT FORMAT section** in each file:

```markdown
## INDIA-SPECIFIC CHECKS

Every review of an Indian app must include these checks for this module:

### [Check 1 Title]
- [ ] [Checklist item]
- [ ] [Checklist item]
- [ ] Impact if missing: [What happens]

**Finding template:** "[Example finding text with India context]"

**India Benchmark:** "[Indian app] does [what] which results in [metric]."

### [Check 2 Title]
[Same structure]

### Scoring Modifiers (India)
- +1 if [India-specific positive]
- -1 if [India-specific negative]
```

**Specific checks per module (Sonnet should add these):**

| Module | India Checks to Add |
|--------|-------------------|
| Onboarding | Truecaller auto-fill, OTP auto-read, WhatsApp login, Google One-Tap, Hindi onboarding option, ₹1 trial India perception |
| Homepage IA | Data-light loading, skeleton loaders, Hindi/English toggle, content-first for low-bandwidth, Tier 2 browse-first patterns |
| Discovery-Search | Hindi voice search, Hinglish query handling, browse > search for Tier 2-3, regional trending, WhatsApp deep link as discovery |
| Content Consumption | Download for offline, quality options (360/480/720p), data usage display, data-saver mode, WiFi vs mobile data warning |
| Engagement-Retention | WhatsApp re-engagement, 8-11 PM notification timing, cricket/IPL season strategy, Hindi notification copy, CRED-style coin mechanics |
| Cognitive Load | Budget phone screen test (5.5" 720p), Hinglish label comprehension, icon-over-text for low literacy, animation perf on budget chipsets, outdoor readability |
| Personalization | Language-as-personalization, tier-based content, regional trending, festival personalization, family profile sharing |
| Persona Alignment | Task Finisher/Explorer/Structured Learner detection, tier-based persona differences, age-based India behavioral patterns |
| AI Integration | Hindi/Hinglish AI chat, voice-first AI, AI trust explanation in Hindi, data privacy in Hindi, AI skepticism handling ("ye bot hai") |

---

### Task 3: Add India-Specific Observation Prompts (SONNET OK)

**For each module's "What to Observe" sections**, add a `**India-Specific Observations:**` block with 2-5 bullet points. These go inside the existing screen navigation sections, not as separate sections.

Example for Discovery-Search, Screen 1 (Search Bar):
```markdown
**India-Specific Observations:**
- Is voice search input available? In Hindi/regional languages?
- Does search handle Hinglish queries (mixed Hindi-English)?
- Is search placeholder in Hindi or English? Does it match the user's language preference?
```

---

### Task 4: Expand Monetization India Benchmarks (SONNET OK)

In `modules/full/monetization.md`, find the `## INDIA-SPECIFIC MONETIZATION CHECKS` section and add Comparative Benchmarks for: CRED (premium subscription positioning), Meesho (referral-first monetization), Zepto (trial-first with instant delivery value), Flipkart Plus (loyalty points), PhysicsWallah (affordable EdTech pricing at ₹2-5K/year).

---

### Task 5: Update Orchestrator (SONNET OK)

In `appteardown.md`:

**Step 2 (Context Loading):** Add `india-product-strategy.md` to the explicit load list:
```
3. Load India context: `context/india-consumer.md` + `context/india-product-strategy.md`
```

**After Step 5 (Scoring):** Add a new step:
```
## STEP 5.5: INDIA FIT CHECK
For every Key Issue and Recommendation generated:
1. Validate against india-consumer.md — would this work for a Tier 2 Hindi-speaking user?
2. Ensure at least one India app is cited in Comparative Benchmarks (from india-product-strategy.md)
3. Check that Roadmap priorities account for India constraints (from india-product-strategy.md Section 4)
4. Verify KPI targets use India benchmarks, not global defaults (from india-product-strategy.md Section 3)
```

---

### Task 6: Design Plugin Integration (SONNET OK)

Read `design:critique` and `design:ux-writing` skill files. In Cognitive Load and Homepage IA modules, add a note:
```
> **Optional Enhancement:** Run the `design:critique` skill on key screenshots for structured design feedback (usability, hierarchy, consistency scoring).
```

In Onboarding and Monetization modules, add:
```
> **Optional Enhancement:** Run the `design:ux-writing` skill to evaluate Hinglish/Hindi copy quality on paywall, CTA labels, and onboarding messages.
```

---

### Task 7: Update Claude.md Indexes (SONNET OK)

Update `Skills/pAI-teardown/Claude.md` to add:
- `context/india-product-strategy.md` in the context files listing
- `screenshot-protocol.md` in the root files listing
- `audit-gap-matrix.md` in the root files listing (mark as reference/audit artifact)

Update the main workspace `Claude.md` if the pAI-teardown skill description needs updating.

---

### Task 8: Verification (OPUS REQUIRED)

Run a mental test: take the updated Onboarding module and mentally walk through a teardown of an Indian EdTech app. At each stage ask:
- Do observations prompt India-specific evidence collection?
- Do benchmarks cite at least one Indian app alongside the international one?
- Do Key Issues use India-native reasoning (not translated Western logic)?
- Do Recommendations account for India constraints?
- Would a PM at Meesho/CRED say "yes, this is actionable for my market"?

Document any remaining gaps found during verification.

---

## Opus vs Sonnet Decision for Execution

| Task | Recommended Model | Rationale |
|------|------------------|-----------|
| **Task 1** (india-product-strategy.md) | **Opus** | This is the highest-leverage file. Requires synthesizing India market knowledge across 10 module dimensions, writing India-native issue templates, calibrating KPI benchmarks for India segments. Sonnet would produce something that looks right but the competitor analysis depth and KPI calibration would be shallow. |
| **Tasks 2-7** (module edits, orchestrator, indexes) | **Sonnet** | These are execution tasks with clear specs above. The decisions are already made in this audit — Sonnet just needs to follow the spec and write the content. Quality should be fine because the spec is detailed enough. |
| **Task 8** (verification) | **Opus** | Critical thinking to catch gaps Sonnet might miss. Opus can hold the full India product context while stress-testing each section. |

**Recommended workflow:**
1. Opus creates Task 1 (`india-product-strategy.md`) — the foundation everything else builds on
2. Switch to Sonnet for Tasks 2-7 — mechanical execution following the specs above
3. Switch back to Opus for Task 8 — verification and gap-catching

**Risk if Sonnet does Task 1:** The India Competitor Benchmark Library would likely cite surface-level app features rather than the strategic "why" behind each design choice. KPI benchmarks would be generic ranges rather than calibrated to India EdTech vs India consumer app vs India commerce. Issue templates would read like "add Hindi support" rather than grounding why Hindi is P0 for Tier 2-3 with specific revenue impact. The file would be adequate but not award-winning.

---

*This audit was conducted by reading all 9,012 lines across 10 full/ module files + 274 lines of India context files. Observations audit: read all "Screens to Navigate" and "What to Observe" sections, identified 9 India-specific gaps. Benchmark audit: grep-counted every app citation (107 international, 2 Indian). Scoring based on: "Would a senior PM at Meesho/CRED/Zepto read this recommendation and say it's actionable for their India market?"*
