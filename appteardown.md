# pAI Review — Master Orchestrator Skill

> **Command:** `/review [app-name] [module] as [persona]`
> **Examples:**
> - `/review Duolingo onboarding as new-user`
> - `/review Notion monetization as trial-user`
> - `/review Cred full as free-user`
> - `/review Stripe payments as new-user`

---

## WHAT THIS SKILL DOES

This is the master orchestrator for the pAI Review system. It:
1. Parses the user's command to extract: **app name**, **module** (or "full"), and **persona**
2. Loads the right context files (domain, frameworks, consumer context, app-specific context)
3. Routes to the correct module skill (or runs all modules for "full" review)
4. Manages screenshot capture and naming
5. Produces two output files: **Current State** (evidence + issues) and **Recommendations**
6. Generates a formatted **PDF** for stakeholder sharing

---

## STEP 0: PARSE THE COMMAND

Extract these from the user's input:

| Parameter | Required | Options | Default |
|-----------|----------|---------|---------|
| **App Name** | Yes | Any app name (e.g., "Duolingo", "Cred", "Notion") | — |
| **Module** | Yes | `onboarding`, `homepage`, `discovery`, `personalization`, `content`, `engagement`, `monetization`, `ai`, `cognitive-load`, `persona-alignment`, or `full` | `full` |
| **Persona** | Yes | `new-user`, `free-user`, `trial-user`, `paid-user`, `lapsed-user`, or custom description | `new-user` |
| **Mode** | Optional | `speed` or `rigor` | `rigor` |
| **Domain** | Auto-detect or specify | `education`, `ott`, `finance`, `ecommerce`, `social`, or custom | Auto-detect from app |

If any required parameter is missing, ask the user. Example prompt:
> "I'll run the teardown. Just need to confirm:
> - **App:** [detected or ask]
> - **Module:** Which area to review? (onboarding / monetization / engagement / full / etc.)
> - **Persona:** Review as which user type? (new-user / free-user / trial-user / paid-user / lapsed-user)
> - **Mode:** Speed (top issues, 15 min) or Rigor (comprehensive, 45-60 min)?"

---

## STEP 1: LOAD CONTEXT FILES

Based on parsed parameters, read these files in order:

### Always Load:
1. `frameworks/expert-frameworks.md` — Intellectual foundation (HEART, Hook, Nielsen, JTBD, Fogg, Reforge, Norman, Kano, AARRR, Cagan)
2. `context/india-consumer.md` — India consumer demographics, behavior, and trust signals
3. `context/india-product-strategy.md` — India competitor benchmarks, issue templates, KPI norms, roadmap rules, recommendation patterns

### Load Based on Domain:
4. `domains/[domain].md` — Domain-specific benchmarks and heuristics
   - Education app → `domains/education.md`
   - OTT app → `domains/ott.md`
   - Finance app → `domains/finance.md`
   - E-commerce → `domains/ecommerce.md`

### Load If App-Specific Context Exists:
5. `context/[app-name]-context.md` — App-specific context (metrics, personas, past teardowns)
   - For a new app → skip (or create during first review using the structure documented in this file)
   - After 2+ reviews of the same app, the auto-learn step builds this file up automatically

### Load Based on Module:
6. `modules/[module].md` — The specific module skill to execute
   - For `full` → load all modules sequentially

---

## STEP 2: CONNECT TO DEVICE & LAUNCH APP

### If Mobile MCP Is Available:
1. List available devices: `mobile_list_available_devices`
2. Connect to the target device
3. List apps: `mobile_list_apps` → find the target app's package name
4. Launch the app: `mobile_launch_app`
5. Confirm app is running by taking initial screenshot

### If No Mobile MCP:
- Ask user to provide screenshots manually
- Or use browser-based version if available
- Note in output: "Review based on [manual screenshots / browser version / emulator]"

---

## STEP 3: SCREENSHOT PROTOCOL

> **📖 READ `screenshot-protocol.md` NOW** before taking any screenshots.
> Full path: `Skills/pAI-teardown/screenshot-protocol.md`
> It contains: confirmed working method, handshake test, naming convention, fallbacks, manifest template, and PDF embedding instructions.

### Summary (full details in screenshot-protocol.md)
1. **Run the handshake test first** — save one test screenshot to the Mac path and confirm the VM can see it
2. **Use the workspace path** for every `mobile_save_screenshot` call: `[your-workspace-path]/[project-folder]/screenshots/img/[##]-[screen-name]-[persona].png`
3. **Log each screenshot in a manifest** as you go — save to `[project-folder]/screenshots/screenshot-manifest.md`
4. **Reference screenshots in evidence** — every evidence bullet cites its screenshot number ("See screenshot #03")
5. **Save immediately** — never defer or batch screenshot saves to the end of a session

---

## STEP 3.5: MANDATORY DESIGN SKILL REVIEW ON SCREENSHOTS

Every module's screenshots must be reviewed using both design skills. This is not optional — screenshots without design review produce incomplete evidence.

**For every set of module screenshots, run:**

1. **`design:critique`** — Evaluate usability, visual hierarchy, consistency, and accessibility. Each module's "Design Skill Integration" section specifies what to focus on for that module. For India context: always assess on budget device screenshots (720p, outdoor brightness) and flag elements that fail on ₹7-12K phones.

2. **`design:ux-copy`** — Evaluate all visible UI copy: CTAs, labels, error messages, empty states, social proof, and notifications. Each module's "Design Skill Integration" section specifies the India-specific copy checks. For India context: always assess Hindi/Hinglish copy quality, CTA clarity for Tier 2-3 users, and whether copy resonates culturally (exam-specific language for EdTech, regional social proof, ₹ pricing presentation).

**Output from design skills feeds directly into:**
- Evidence bullets (cite design:critique findings as evidence)
- Key Issues (design:ux-copy gaps become copy/language Key Issues)
- Scoring modifiers (accessibility failures from design:critique affect scores)
- Recommendations (design:ux-copy suggestions become copy improvement recs)

---

## STEP 4: EXECUTE THE MODULE(S)

### For Single Module:
Read `modules/[module].md` and follow its instructions. The module file contains:
- What screens to navigate
- What to observe and document
- Scoring rubric with framework references
- Evidence template
- Key issues template

### For Full Review:
Execute modules in this order (each module is a separate file in `modules/`):

| Order | Module | File | AARRR Stage |
|-------|--------|------|-------------|
| 1 | Onboarding & First Value | `modules/onboarding.md` | Activation |
| 2 | Homepage & Information Architecture | `modules/homepage-ia.md` | Activation / Engagement |
| 3 | Content Discovery & Search | `modules/discovery-search.md` | Engagement |
| 4 | Personalization & Relevance | `modules/personalization.md` | Engagement / Retention |
| 5 | Content Consumption Experience | `modules/content-consumption.md` | Engagement |
| 6 | Engagement & Retention Mechanics | `modules/engagement-retention.md` | Retention |
| 7 | Monetization UX | `modules/monetization.md` | Revenue |
| 8 | AI Integration | `modules/ai-integration.md` | Engagement / Retention |
| 9 | Cognitive Load & Visual Clarity | `modules/cognitive-load.md` | All stages |
| 10 | Persona-Intent Alignment | `modules/persona-alignment.md` | All stages |

### Speed Mode vs. Rigor Mode

**Speed Mode (per module):**
- Navigate key screens only (3-5 screenshots per module)
- Score the dimension (1-10) with 1-sentence rationale
- List top 3 issues only
- No detailed evidence bullets — just the critical finding
- Total time: ~15 minutes for full review

**Rigor Mode (per module):**
- Navigate ALL relevant screens (8-15 screenshots per module)
- Score with full rationale citing frameworks
- Comprehensive evidence bullets with screenshot references
- All key issues documented
- Framework violations explicitly called out
- Total time: ~45-60 minutes for full review

---

## STEP 5: SCORING METHODOLOGY

### Per-Module Scoring (1-10 scale)

| Score | Label | Definition |
|-------|-------|-----------|
| 1-2 | Critical | Fundamentally broken. Core functionality missing or counterproductive. Immediate fix required. |
| 3-4 | Poor | Significant issues. Feature exists but poorly implemented. High-priority fix. |
| 5-6 | Below Average | Functional but subpar. Missing key elements that competitors do well. Medium-priority. |
| 7-8 | Good | Solid implementation. Minor issues. Some optimization opportunities. |
| 9-10 | Excellent | Best-in-class. Could be used as benchmark for others. Minor polish only. |

### Scoring Must Reference:
1. **At least one expert framework** (e.g., "Scores 2/10 on Onboarding because it violates Fogg's Ability principle — paywall adds 3 extra steps before value")
2. **At least one domain benchmark** (e.g., "Duolingo reaches first lesson in 60 seconds; this app takes 90+ seconds to reach a paywall")
3. **At least one India consumer consideration** (e.g., "Tier 2 users on budget devices would experience this as...")

### Overall Score Calculation
- Simple average of all module scores (for full review)
- Weighted average available if specific modules are more critical:
  - Onboarding: 1.5x weight (first impression drives everything)
  - Monetization: 1.5x weight (directly impacts revenue)
  - Engagement & Retention: 1.5x weight (drives LTV)
  - Others: 1.0x weight

---

## STEP 5.5: INDIA FIT CHECK

For every Key Issue and Recommendation generated in any module:

1. **Validate against india-consumer.md** — Would this recommendation work for a Tier 2 Hindi-speaking user on a budget Android device? If not, flag it and provide an India-appropriate alternative.
2. **Ensure at least one India app is cited in Comparative Benchmarks** — Use `india-product-strategy.md` Section 1 (India Competitor Benchmark Library). Every Comparative Benchmark must include at least one Indian app alongside any international reference.
3. **Check Roadmap priorities against India constraints** — Use `india-product-strategy.md` Section 4 (India Roadmap Prioritization Rules). Validate that P0/P1/P2 classifications account for India-specific escalations (e.g., Hindi support is P0, not P1, for Tier 2-3 apps).
4. **Verify KPI targets use India benchmarks** — Use `india-product-strategy.md` Section 3 (India KPI Benchmarks). Do NOT use global D1/D7/D30 or conversion benchmarks — they overestimate India norms by 30-50%.
5. **BYJU'S anti-pattern check** — For every monetization recommendation, ask: "Could this be perceived as aggressive or trust-eroding?" If yes, reframe using PhysicsWallah/Kuku FM/Meesho models.

---

## STEP 6: PRODUCE OUTPUTS

### Output 1: Current State File
**Filename:** `[app-name]-current-state-[version]-[persona].md`
**Location:** `[project-folder]/`

Structure:
```markdown
# [APP NAME] — CURRENT STATE TEARDOWN

> Source of Truth for [version], audited as [persona] on [date]
> Device: [device info]
> Overall Score: X.X / 10

## SCORECARD SUMMARY
[Table: dimension, score, status]

## [MODULE NAME] — X/10
### Evidence
[Bullet points with screenshot references]
### Key Issues
[Numbered list of issues with framework citations]

[Repeat for each module]

## TOP 5 CRITICAL ISSUES
## COMPETITIVE BENCHMARKING
## SCORING RATIONALE
## CHANGE LOG
```

**Rules:**
- NO recommendations in this file
- Every evidence point references a screenshot
- Every key issue cites an expert framework
- Every score includes domain benchmark comparison

### Output 2: Recommendations File
**Filename:** `[app-name]-recommendations-[version]-[persona].md`
**Location:** `[project-folder]/`

Structure:
```markdown
# [APP NAME] — RECOMMENDATIONS

> Companion to: [current-state-filename]
> Organized by: Thematic sections for actionability

## [THEMATIC SECTION] (e.g., Personalization & Onboarding)
### Quick Wins (1-2 weeks)
### Medium Effort (2-4 weeks)
### Strategic Fixes (4-8 weeks)
### Expected Impact

[Repeat for each thematic section]

## IMPLEMENTATION ROADMAP (12 Weeks)
## SUCCESS METRICS & KPIs
## CHANGE LOG
```

**Rules:**
- Organized by THEME (not by module) — group related fixes together
- Each recommendation has effort estimate and expected impact
- Recommendations must pass the India consumer reality check
- Include implementation roadmap with phases

### Output 3: Screenshot Manifest
**Filename:** `screenshot-manifest.md`
**Location:** `[project-folder]/screenshots/`

### Output 4: Stakeholder PDF (Optional — triggered by user)
**Filename:** `[app-name]-teardown-[date].pdf`
**Location:** `[project-folder]/`

Generated using reportlab. This is a consulting-grade deliverable — NOT a summary. The audience may not know product frameworks or competitor details. Every claim must be supported with a screenshot and explained in plain language.

**Expected page count:** 30-45 pages for a full 10-module review. Driven by evidence density, not a target.

#### PDF Structure:

**Pages 1-2: Cover + Table of Contents**
- Cover: app name, version, date, overall weighted score (large), key business metrics (3-4), reviewer, device, persona, business goal
- Table of contents with section names

**Pages 3-4: Executive Summary**
- 1.5 pages. What was reviewed, why, and the headline findings.
- Include a colored callout box with the 3 most critical numbers (e.g., "48% trial-to-paid, 18% P0 cancellation, 28% P0-P1 retention")
- Written so a CXO can read this page alone and understand the situation

**Page 5: Scorecard Summary**
- Table: all modules, scores (color-coded: red 1-3, orange 4-5, blue 6-7, green 8-10), weights, AARRR stage
- Simple average + weighted average
- 1-2 sentence methodology note

**Pages 6+: Per-Module Deep Dives (2-4 pages per module)**

This is the core of the report. For EACH module:

**Evidence Cards (1-2 pages):**
Each evidence finding is a 2-column card:
- LEFT column: embedded screenshot (~1.5" x 3" phone portrait) with caption (screen name + what to look for)
- RIGHT column:
  1. **OBSERVATIONS** (2-4 bullet points describing what is seen on screen and what is missing)
  2. **WHAT THIS MEANS** (2-3 sentences explaining the framework violation in plain language — see Framework Explanation Standard below)
  3. **BENCHMARK** (2-3 sentences: what a specific competitor does, why it works, and the gap — see Competitor Comparison Standard below)

Each module should have 2-4 evidence cards, driven by the findings. A single screenshot may appear in multiple modules if it serves as evidence for both (e.g., homepage screenshot for both Onboarding and Homepage IA).

**Key Issues (1 page):**
Each issue is 150-200 words with this structure:
1. Issue title + severity tag [CRITICAL / HIGH / MEDIUM]
2. Description: what's happening and why it's a problem (3-4 sentences)
3. FRAMEWORK: name the framework, explain the principle in plain language, explain how this screen violates it (3-4 sentences)
4. BENCHMARK: what a specific competitor does differently and why it works (2-3 sentences)
5. BUSINESS IMPACT: what metric this affects and by how much (1-2 sentences with estimates)

**Module Recommendations (optional, 0.5-1 page):**
Top 2-3 recommendations specific to this module, with effort estimate and expected impact.

**After All Modules:**

**Top 5 Critical Issues (1 page):**
- Table: issue, module, score, description, expected impact of fixing
- These are the highest-leverage problems across all modules

**Competitive Benchmarking (1-2 pages):**
- Table with "Why It Matters" column — don't just list what competitors do, explain the behavioral insight behind why their approach works
- Cover 3-4 competitors relevant to the app's domain

**Recommendations Summary (2-3 pages):**
- Organized by theme (not by module) — group related fixes
- Table per theme: recommendation name, effort level, timeline, description
- Color-coded effort tags (green = quick win, orange = medium, blue = strategic)

**Implementation Roadmap (1 page):**
- Phased table: phase name, timeline, key items, expected outcome
- 4 phases across 12 weeks

**Success Metrics (1-2 pages):**
- Primary metrics: current → 4-week → 8-week → 12-week targets
- Secondary/leading indicators: current → target
- Guardrail metrics: floor values (don't regress)

#### Framework Explanation Standard

**RULE: Never name-drop a framework.** Every framework citation must include:

1. **Framework name** (e.g., "Fogg's Behavior Model")
2. **The principle in plain language** (e.g., "This model says behavior only happens when three things align at the same moment: the person has enough Motivation to act, the Ability to do it easily, and a Prompt that triggers the action.")
3. **How this specific screen violates it** (e.g., "On this screen, the app asks for notification permission — a strong Prompt — but the user hasn't seen any content yet, so their Motivation is near zero. The equation fails: without Motivation, no amount of Prompting will get the user to say yes.")
4. **Why it matters for the business** (e.g., "This means notification opt-in rates will be low, reducing the app's ability to re-engage users on Day 2+, directly feeding the retention cliff.")

**Bad example:** "Violates Fogg's Ability principle."
**Good example:** "Fogg's Behavior Model says behavior requires Motivation, Ability, and Prompt together. Here, the app asks for notifications before showing any content — high Prompt but zero Motivation. Users have no reason to say yes because they don't yet know what they'd be notified about. This drives low opt-in rates and weakens the Day 2+ re-engagement loop."

#### Competitor Comparison Standard

**RULE: Never make a bare comparison.** Every competitor reference must include:

1. **What the competitor does specifically** (e.g., "Duolingo asks 4 onboarding questions — language choice, daily goal, current skill level, and why they're learning — in under 20 seconds")
2. **Why that approach works** — the behavioral insight (e.g., "This works because it creates a psychological commitment (consistency principle) and gives the app enough signal to personalise the first lesson. Users feel the app 'understands' them.")
3. **The gap vs the app being reviewed** — quantified if possible (e.g., "[App] asks zero questions. The gap: Duolingo's onboarding drives 40%+ D7 retention vs industry average of 15-20%. [App]'s D7 retention is 18%.")

**Bad example:** "Duolingo waits until Day 7 to ask for ratings."
**Good example:** "Duolingo delays its rating prompt until Day 7+, and only shows it to users who have maintained an active streak. By that point, users have invested 7+ days of effort and feel positively about the product. This is based on the Peak-End Rule — people judge experiences by their peak moment and their most recent moment, not the average. Asking for ratings during a streak celebration (peak) produces 4.5+ star reviews. The reviewed app asks on Day 0, before any value delivery, when the user's experience is neutral at best."

#### Screenshot Embedding Rules

1. **Save ALL screens reviewed** during the teardown to disk using `mobile_save_screenshot` — not just inline captures. Every screen navigated = a saved PNG file.
2. **The screenshot count is driven by evidence, not pre-set.** Don't target a specific number. If a module needs 4 screenshots to make its case, use 4. If 2 suffice, use 2.
3. **Each evidence point that cites a screen must embed that screenshot inline in the PDF.** No "See screenshot #03" without the actual image on the same page.
4. **A single screenshot may serve multiple modules.** The homepage screenshot is evidence for both Onboarding (no welcome screen) and Homepage IA (category organisation). Embed it in both sections.
5. **Screenshots are phone-portrait orientation** (~1.5" x 3" in PDF) with a caption below: screen name + "Look for: [what the reader should notice]"
6. **Save screenshots to:** `[project-folder]/screenshots/img/[##]-[screen-name].png`
7. **Path discipline — critical:** The PDF generator (`output-templates/generate_pdf.py`) resolves `SCREENSHOT_DIR` relative to its own file location. It will look for screenshots at `[project-folder]/screenshots/img/`. Always save screenshots there — never to `/tmp/` without immediately copying, and never to a hardcoded `/sessions/[id]/...` path. The script will print a clear `⚠️ MISSING SCREENSHOT` warning for every file it cannot find, so you'll know exactly which files to add before re-running.

#### Writing Style: Para + Bullet (Consulting Style)

**RULE: Every analysis section uses para + bullet structure** — NOT long unbroken paragraphs, NOT bullet-only lists. This is the standard consulting report format optimised for scannability.

The pattern for every analysis block:

1. **Opening sentence** (1 line) — states the finding or claim plainly
2. **Supporting bullets** (2-4 bullets, 1-2 lines each) — evidence, observations, or sub-points
3. **Closing sentence** (1 line, optional) — so-what or business implication

**Bad example (wall of text):**
> Fogg's Behavior Model says behavior requires Motivation, Ability, and Prompt together. Here, the app asks for notifications before showing any content — high Prompt but zero Motivation. Users have no reason to say yes because they don't yet know what they'd be notified about. This drives low opt-in rates and weakens the Day 2+ re-engagement loop which is the primary mechanism for retention in mobile apps and especially education products where daily habit formation is the core growth loop.

**Good example (para + bullet):**
> Fogg's Behavior Model says behavior only happens when three elements converge: Motivation, Ability, and Prompt.
>
> - **Motivation:** Near-zero — the user hasn't seen any content yet and has no reason to want notifications
> - **Prompt:** Fired too early — notification ask appears before any value demonstration
> - **Result:** The equation fails; opt-in rates will be low, weakening the Day 2+ re-engagement loop
>
> This directly feeds the P0→P1 retention cliff (28%).

Apply this pattern to: OBSERVATIONS, WHAT THIS MEANS, BENCHMARK, Issue descriptions, and Recommendation details.

#### Typography Spec

**RULE: Use Poppins for headings + Lato for body.** These fonts are pre-installed on the VM. Never use Helvetica or other system fonts.

The PDF generator template at `output-templates/generate_pdf.py` already has these fonts registered. Always use that template as the base.

| Element | Font | Weight | Size (pt) | Leading (pt) | Use |
|---------|------|--------|-----------|---------------|-----|
| Cover Title | Poppins | Bold | 36 | 42 | App name on cover page |
| Cover Subtitle | Poppins | Light | 20 | 26 | Module/review type on cover |
| Section Heading (H1) | Poppins | Bold | 18 | 24 | "Executive Summary", "Module 1: Onboarding" |
| Sub-heading (H2) | Poppins | Medium | 13 | 18 | "Evidence & Analysis", "Key Issues" |
| Sub-sub-heading (H3) | Poppins | Medium | 11 | 15 | "Finding 1", evidence card titles |
| Body Text | Lato | Regular | 9.5 | 14.5 | Main analysis paragraphs |
| Body Bold | Lato | Bold | 9.5 | 14.5 | Emphasis within body |
| Evidence Text | Lato | Regular | 9 | 14 | Observations, analysis in evidence cards |
| Framework Citation | Lato | Italic | 8.5 | 12 | Indented framework explanation |
| Issue Title | Poppins | Medium | 10.5 | 15 | Issue name in key issues section |
| Issue Description | Lato | Regular | 9 | 13.5 | Issue detail text |
| Table Header | Lato | Bold | 8.5 | — | Column headers in data tables |
| Table Body | Lato | Regular | 8.5-9 | 12 | Table cell content |
| Caption | Lato | Italic | 8 | 11 | Screenshot captions |
| Footer | Lato | Regular | 7.5 | 10 | Page footer text |
| Rec Number | Poppins | Bold | 10 | 14 | "01", "02" in recommendations |

**Font Registration (Python):**
```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Poppins (headings)
pdfmetrics.registerFont(TTFont('Poppins', '/usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Poppins-Medium', '/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf'))
pdfmetrics.registerFont(TTFont('Poppins-Bold', '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Poppins-Light', '/usr/share/fonts/truetype/google-fonts/Poppins-Light.ttf'))
pdfmetrics.registerFont(TTFont('Poppins-Italic', '/usr/share/fonts/truetype/google-fonts/Poppins-Italic.ttf'))

# Lato (body)
pdfmetrics.registerFont(TTFont('Lato', '/usr/share/fonts/truetype/lato/Lato-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Lato-Bold', '/usr/share/fonts/truetype/lato/Lato-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Lato-Italic', '/usr/share/fonts/truetype/lato/Lato-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Lato-Light', '/usr/share/fonts/truetype/lato/Lato-Light.ttf'))
pdfmetrics.registerFont(TTFont('Lato-Semibold', '/usr/share/fonts/truetype/lato/Lato-Semibold.ttf'))
```

#### Color Palette

| Name | Hex | Use |
|------|-----|-----|
| Navy | #0F1B2D | Primary text, headers |
| Charcoal | #1E293B | Secondary headers |
| Slate | #334155 | Body text |
| Steel | #64748B | Muted text, labels |
| Silver | #94A3B8 | Captions, meta |
| Accent Blue | #2563EB | Accent bars, links, highlights |
| Accent Light | #DBEAFE | Accent backgrounds |
| Critical Red | #DC2626 | Critical issues, scores 1-3 |
| Warning Amber | #D97706 | High issues, scores 4-5 |
| Good Green | #059669 | Positive scores 8-10 |
| BG Light | #F8FAFC | Section backgrounds |
| BG Card | #F1F5F9 | Card backgrounds |
| Border | #E2E8F0 | Borders, dividers |

#### Professional Formatting

- Consistent header on every page: blue accent line + "APP NAME | MODULE | DATE" (left) + "CONFIDENTIAL" (right)
- Consistent footer: "Prepared by [Author] | Powered by pAI Review" (left) + page number (right) + thin blue accent bar at page bottom
- Color-coded severity tags: red = critical (1-3), amber = high (4-5), blue = medium (6-7), green = good (8-10)
- Alternating row backgrounds in tables (white + #F8FAFC light gray)
- Section headings: Poppins Bold 18pt with 2.5pt blue accent bar underneath
- Evidence cards: bordered card with light background (#F8FAFC), thin vertical divider between screenshot and analysis columns
- Callout boxes: light blue background (#DBEAFE) with 3pt blue left border for key stats/benchmarks

---

## STEP 7: LOG TOKEN USAGE & COST — MANDATORY AFTER EVERY RUN

Token accounting is required at the end of every run. This feeds `run-log.csv` and prints
a cost report alongside the PDF.

### How to estimate tokens before calling the script

**Input token estimate (characters ÷ 4):**

| What was loaded | How to measure |
|-----------------|---------------|
| Each file read via Read tool | `wc -c [file]` ÷ 4 |
| Screenshots (mobile, via vision) | Count × 1,500 tokens each |
| Conversation overhead (system prompt + prior turns) | Estimate 5,000 tokens flat |

**Output token estimate:** Total characters Claude generated this run ÷ 4.
Single module rigor: ~3,000–6,000 tok. Full 10-module run: ~12,000–18,000 tok.

### Call the logger at the end of every review

```bash
python [project-folder]/output-templates/log_run.py \
  --app "[App Name]" \
  --persona "[persona]" \
  --flow "[module or 'full']" \
  --mode "[speed|rigor|hybrid]" \
  --input-tokens [estimated] \
  --output-tokens [estimated] \
  --pdf "[pdf-filename-or-empty]" \
  --notes "[brief note about this run]"
```

The script auto-assigns a run number, computes cost, appends to `run-log.csv`, and shows
running totals across all historical runs.

### Token efficiency targets — check before every run

| Mode | Scope | Target Input Tokens | Target Cost |
|------|-------|--------------------|-------------|
| Speed | Single module | < 15,000 | < $0.05 |
| Rigor | Single module | < 40,000 | < $0.15 |
| Rigor | Full (10 modules) | < 80,000 | < $0.46 |

If your estimate exceeds these targets, check what extra files were loaded unnecessarily.
Read `TOKEN-EFFICIENCY-PLAN.md` for the full 7-tactic savings playbook.

**Token-aware loading discipline:**
- Load each module file **only when executing that module** — do not pre-load all 10 upfront
- In speed mode, read only the first 35 lines of each module file (screens + 3 checks + score)
- Never re-read `generate_pdf.py` to generate the PDF — pass a data file to the script instead
- Load only the active persona's context, not all 5 persona sections

---

## STEP 8: AUTO-LEARN — UPDATE CONTEXT AFTER EVERY REVIEW

After every review run, the orchestrator MUST automatically update the app's context file. This is how the system gets smarter over time.

### What to Append to `context/[app-name]-context.md`:

```markdown
## Review: [Date] — [Module] as [Persona] ([Mode])

### Scores
| Module | Score | Delta from Last |
|--------|-------|-----------------|
| [module] | X/10 | +/-Y |

### Key Findings (New or Changed)
- [Finding 1 — if this is new since last review, mark as NEW]
- [Finding 2 — if this changed since last review, mark as CHANGED and note what changed]
- [Finding 3 — if this was previously flagged and is now fixed, mark as RESOLVED]

### Screenshots Taken
[Count] screenshots saved to [path]

### Cumulative Review History
| # | Date | Module | Persona | Score | Reviewer |
|---|------|--------|---------|-------|----------|
| 1 | [date] | [module] | [persona] | X/10 | [name] |
```

### Auto-Learn Rules:
1. **Always read the existing context file first** before appending. Don't duplicate.
2. **Compare current findings with previous findings** — call out what improved, what regressed, what's new.
3. **Update the "Last Reviewed" timestamp** at the top of the context file.
4. **If a previously flagged issue is now resolved**, move it from "Current Issues" to "Resolved Issues" with the date.
5. **If the app version changed**, note it prominently — version changes may explain score deltas.
6. **Accumulate persona coverage** — track which personas have been reviewed and which haven't. Flag gaps.

### Context File Grows Into a Knowledge Base:
After 5+ reviews, the context file becomes a powerful reference:
- Score trends over time (is the app improving?)
- Issue lifecycle (when flagged → when fixed → impact of fix)
- Persona coverage map (which user types are well-reviewed, which are blind spots)
- Version-to-version delta (what changed between app updates)
- Seasonal patterns (if engagement/monetization scores shift by season)

---

## MODULE ROUTING TABLE

| Command | Routes To |
|---------|-----------|
| `/review [app] onboarding as [persona]` | `modules/onboarding.md` |
| `/review [app] homepage as [persona]` | `modules/homepage-ia.md` |
| `/review [app] discovery as [persona]` | `modules/discovery-search.md` |
| `/review [app] personalization as [persona]` | `modules/personalization.md` |
| `/review [app] content as [persona]` | `modules/content-consumption.md` |
| `/review [app] engagement as [persona]` | `modules/engagement-retention.md` |
| `/review [app] monetization as [persona]` | `modules/monetization.md` |
| `/review [app] ai as [persona]` | `modules/ai-integration.md` |
| `/review [app] cognitive-load as [persona]` | `modules/cognitive-load.md` |
| `/review [app] persona-alignment as [persona]` | `modules/persona-alignment.md` |
| `/review [app] full as [persona]` | All modules in sequence |

---

## ERROR HANDLING

| Situation | What to Do |
|-----------|-----------|
| Mobile MCP not connected | Ask user to connect device or provide screenshots manually |
| App not installed | Ask user to install, or offer to search for package name |
| App crashes during review | Document the crash as a finding; restart and continue |
| Screenshots can't be saved to workspace | Save to `/tmp/` via mobile_save_screenshot, then **immediately** `cp` each file to `[project-folder]/screenshots/img/`. Do NOT batch this at the end. If filesystems are isolated, use PIL to create annotated reference images from inline captures. Note in manifest which are direct vs recreated. Never hardcode session paths. |
| Unknown domain | Default to general frameworks; skip domain-specific context; note gap |
| No previous context | Create new context file during review; note "first review" |

---

---

## OPEN ITEMS / FUTURE WORK

> These are descoped for now but should be revisited. Remind the user periodically.

- [ ] **Domain files needed:** OTT (`domains/ott.md`), Finance (`domains/finance.md`), E-commerce (`domains/ecommerce.md`), Social (`domains/social.md`). Currently only `education.md` exists. Build these when the skill is used for a non-education app.
- [ ] **Output templates:** Formalized `.md` templates for current-state and recommendations files (currently inline in orchestrator).
- [ ] **Plugin packaging:** Bundle the entire skill system as an installable Claude Desktop plugin with proper manifest.
- [ ] **Competitive review mode:** A variant that reviews 2-3 competing apps side-by-side using the same module.
- [ ] **Team calibration:** A calibration exercise where 2+ reviewers score the same app and compare results to align scoring standards.

---

*This skill is the entry point for all app teardowns. It orchestrates module skills, manages screenshots, auto-learns from every run, and assembles the final deliverables.*

---

## OPEN ITEMS — TOKEN EFFICIENCY (next implementation round)

> From `TOKEN-EFFICIENCY-PLAN.md` — implement in priority order:

- [ ] **P0 — Remove example issue writeups from module files** (~55K tokens saved per full run). Replace 200-word examples with 1-line "anchor" descriptions.
- [ ] **P0 — PDF data file pattern**: skill produces `[app]-data.json`, script reads it. Never re-read 1,200-line template per run (~12K tokens saved).
- [ ] **P1 — Compress context files**: `expert-frameworks-ref.md` (30-line lookup table) and `india-ref.md` (40-line delta table). Load these instead of full files at runtime (~15K tokens saved).
- [ ] **P1 — Domain overlays**: remove from module files; inherit from loaded domain file (~15K tokens saved).
- [ ] **P2 — Persona files**: extract to `context/personas/[persona].md`; load only the active one (~16K tokens saved).
- [ ] **P2 — Speed mode headers**: add `<!-- END SPEED MODE -->` block (top 35 lines) to each module; orchestrator reads partial file in speed mode (70% module savings in speed runs).
