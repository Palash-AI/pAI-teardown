# Cognitive Load & Visual Clarity

> AARRR: All Stages | Frameworks: Nielsen, Norman, HEART, Fogg, WCAG | Speed: 15min | Rigor: 60min

<!-- SPEED MODE -->
## QUICK AUDIT
Navigate: 1. Home / main screen 2. Content list / browse screen 3. Content detail / player screen 4. Settings / profile 5. Any form or error state
Check: Visual hierarchy obvious on first glance, primary CTA is clear, typography readable, color consistent, no clutter, thumbnails consistent size/quality
Score anchor: 9-10 = Apple/Material-level polish (hierarchy instant, minimal CTAs, accessible), 7-8 = professional (clear hierarchy, consistent), 5-6 = functional but inconsistent (some clutter), 3-4 = cluttered or confusing (no hierarchy), 1-2 = broken or unreadable
<!-- END SPEED MODE -->

## SCREENS TO NAVIGATE

### 1. Visual Hierarchy & Information Priority
**Observe:**
- Primary focal point: what draws the eye first?
- Information weight: important info emphasized by size, color, position?
- Contrast: key elements stand out from background?
- Whitespace: breathing room or cramped?
- Element positioning: important info above fold?

**Screenshot:** Full screen for overall hierarchy assessment; zoomed view of key elements

**Framework check:** Nielsen #8 + Norman (Conceptual Model) → Does the user understand structure at a glance? Not every element should have equal weight.

---

### 2. CTA Density & Button Clarity
**Observe:**
- Number of CTAs visible without scroll (target: 1 primary, ≤2 secondary)
- Primary CTA prominence: distinct color/size or equal weight with others?
- Button design: look tappable (rounded, color, shadow) or flat/text-link?
- CTA labels: clear action ("Play", "Subscribe") or vague ("OK", "Next")?
- Hit target size: estimated ≥48px or too small?
- Destructive actions (delete, logout): visually distinct or same as others?

**Screenshot:** Full screen showing all CTAs; zoomed primary CTA; destructive action if present

**Framework check:** Nielsen #8 + Norman (Affordances) → One primary CTA per screen. Buttons must look tappable.

---

### 3. Typography & Readability
**Observe:**
- Font size hierarchy: distinct heading / body / small text levels or all similar?
- Line spacing: readable leading or cramped?
- Contrast: dark text on light (good) / low contrast (failing WCAG)?
- Text alignment: consistent left/center/right or mixed?
- Truncation: long text handled with "..." or wraps awkwardly?

**Screenshot:** Heading + body text sample; high vs. low contrast area if present

**Framework check:** Nielsen #6 + WCAG → Contrast ≥4.5:1 body, ≥3:1 large text. Hierarchy should make content scannable.

---

### 4. Color Usage & Consistency
**Observe:**
- Palette size: compact (3-5 colors) or rainbow (10+)?
- Primary color consistency: same hue for all CTAs/links/focus states?
- Color meaning: red = error, green = success — consistent?
- Color-blind safety: no red/green-only distinctions?
- Status colors (error/success/warning): clearly distinguishable?

**Screenshot:** CTA color comparison across screens; error and success states

**Framework check:** Nielsen #4 + Norman (Mapping) → Colors must mean the same thing everywhere. Color alone must not convey status.

---

### 5. Spacing, Alignment & Grid
**Observe:**
- Spacing rhythm: consistent margins/padding between elements or random gaps?
- Grid alignment: elements on invisible grid or misaligned/chaotic?
- Card/module consistency: all cards similar size and spacing?
- Text padding: breathing room against edges or cramped?

**Screenshot:** Full screen showing spacing rhythm; zoomed element spacing

**Framework check:** Nielsen #4 + #8 → Consistent spacing system; good whitespace creates visual calm and reduces load.

---

### 6. Thumbnail Quality & Image Consistency
**Observe:**
- Aspect ratio: all thumbnails same ratio or variable?
- Image quality: high-res professional or pixelated/low-quality?
- Missing images: placeholder shown or broken?
- Text on images: readable contrast or text washed out?
- Load performance: fast / lazy-loaded with blank gaps / janky?

**Screenshot:** Grid of thumbnails for consistency check; close-up of quality; broken image placeholder if present

**Framework check:** Nielsen #4 + #8 → Consistent thumbnail treatment is a trust signal. Inconsistency feels amateur.

---

### 7. Accessibility
**Observe:**
- Color contrast (estimate): WCAG AA (4.5:1 body) passing or failing?
- Touch targets: buttons estimated ≥48px or too small?
- Icons: have labels or icon-only?
- Dark mode: supported or light-only?
- Captions: on video content?
- Font size: ≥12px or too small?

**Screenshot:** Icon without label (if present); estimated small touch target; dark mode toggle or absence

**Framework check:** WCAG 2.1 + Nielsen #10 → AA compliance minimum; accessibility improvements benefit all users.

---

### 8. Error States & Feedback Clarity
**Observe:**
- Error messages: specific ("Email is invalid") / generic ("Error occurred") / absent?
- Error visibility: red + text / red only / not visible?
- Recovery guidance: suggests fix or user must guess?
- Success feedback: celebration / toast / silent?
- Loading states: spinner / skeleton / nothing?
- Validation timing: real-time / on submit / absent?

**Screenshot:** Error state with message; success confirmation; loading state

**Framework check:** Nielsen #1 + #9 + Norman (Feedback) → Users must always know what happened and how to recover.

---

## SCORING RUBRIC

| Score | Label | Key Criteria |
|-------|-------|-------------|
| 9-10 | Best-in-class | Instant hierarchy, 1 primary CTA, purposeful color, rhythmic spacing, consistent thumbnails, WCAG AA+, specific errors with recovery, no clutter |
| 7-8 | Good | Clear hierarchy, primary CTA obvious, mostly consistent color/spacing, adequate thumbnails, WCAG AA, errors shown |
| 5-6 | Adequate | Hierarchy present but unclear, 2-3 equal CTAs, some inconsistency, thumbnails variable, WCAG A, basic errors |
| 3-4 | Poor | Weak hierarchy (all elements equal), 5+ CTAs, chaotic color, cramped spacing, inconsistent thumbnails, accessibility gaps, vague/missing errors |
| 1-2 | Critical | No hierarchy, buttons invisible/misleading, 10+ colors, broken layout, missing images everywhere, WCAG failures, no feedback |

**Scoring method:** Start at 5. Add: +1 hierarchy obvious at a glance, +1 single clear primary CTA, +1 typography readable with clear levels, +1 color palette consistent with meaning, +1 rhythmic spacing, +1 thumbnails uniform quality/ratio, +1 WCAG AA on contrast, +1 specific errors with recovery. Deduct: -2 no visual hierarchy, -2 CTA overload, -1 low contrast text, -1 thumbnail chaos, -1 no error feedback. Cap at 1-10.

---

## EVIDENCE CHECKLIST

### Visual Hierarchy
- [ ] Primary focal point: [Element that draws eye first]
- [ ] Hierarchy clarity (1-5): [_____]
- [ ] Information weight: [Emphasized / Equal / Hidden]
- [ ] Contrast strength: [High / Medium / Weak]
- [ ] Whitespace: [Spacious / Adequate / Cramped]

**Framework:** Nielsen #8, Norman (Conceptual Model)

### CTA & Buttons
- [ ] CTAs visible without scroll: [Count: _____]
- [ ] Primary CTA prominence: [Obvious / Clear / Equal / Hidden]
- [ ] Buttons look tappable: [Yes / Flat/unclear / Text links]
- [ ] CTA labels: [Clear action / Vague / No label]
- [ ] Hit target size: [≥48px / <48px / Variable]
- [ ] Destructive actions marked: [Distinct / Same as others / N/A]

**Framework:** Nielsen #1, #4, #8, Norman (Affordances)

### Typography
- [ ] Font hierarchy (1-5): [_____]
- [ ] Readability (1-5): [_____]
- [ ] Line spacing: [Adequate / Cramped / Too loose]
- [ ] Text alignment: [Consistent / Mixed]
- [ ] Contrast: [WCAG pass / Fail / Variable]

**Framework:** Nielsen #6, #8, WCAG

### Color Usage
- [ ] Palette size: [Compact ≤5 / Moderate / Rainbow 10+]
- [ ] CTA color consistency: [Same everywhere / Inconsistent]
- [ ] Color meaning: [Purposeful / Decorative / Confusing]
- [ ] Status colors distinct: [Yes / Hard to tell / Not colored]
- [ ] Accessibility: [Color-blind safe / Problematic]

**Framework:** Nielsen #4, Norman (Mapping), WCAG

### Spacing & Alignment
- [ ] Spacing rhythm (1-5): [_____]
- [ ] Grid alignment (1-5): [_____]
- [ ] Padding adequacy: [Spacious / Adequate / Cramped]
- [ ] Card/module consistency: [Uniform / Variable]

**Framework:** Nielsen #4, #8

### Thumbnails & Images
- [ ] Aspect ratio consistency: [Same / Variable]
- [ ] Image quality: [Professional / Mixed / Low-res]
- [ ] Missing image handling: [Placeholder / Broken / N/A]
- [ ] Text on images readable: [Yes / Difficult / N/A]
- [ ] Load performance: [Fast / Acceptable / Slow/blank gaps]

**Framework:** Nielsen #1, #4, #8

### Accessibility
- [ ] Color contrast: [WCAG AAA / AA / A / Fails]
- [ ] Touch targets: [≥48px / <48px / Variable]
- [ ] Icons have labels: [Yes / Some / No]
- [ ] Dark mode: [Supported / Partial / Light only]
- [ ] Video captions: [Yes / No / N/A]
- [ ] Min font size: [≥12px / <12px]

**Framework:** WCAG 2.1, Nielsen #10

### Error States & Feedback
- [ ] Error messages: [Specific / Generic / Absent]
- [ ] Error visibility: [Obvious / Subtle / Not visible]
- [ ] Recovery guidance: [Provided / User must guess / None]
- [ ] Success feedback: [Celebration / Toast / Silent]
- [ ] Loading states: [Visible / Absent / Confusing]
- [ ] Validation timing: [Real-time / On submit / None]

**Framework:** Nielsen #1, #5, #9, Norman (Feedback)

### Overall Cognitive Load
- [ ] Clutter (1-5, 5 = very cluttered): [_____]
- [ ] Scannability (1-5): [_____]
- [ ] Visual calm (1-5): [_____]

**Framework:** Nielsen #8, Fogg (Ability)

---

## KEY ISSUE PATTERNS

1. **No Visual Hierarchy — All Elements Compete** → Detect: User can't identify the most important thing on the screen; equal-weight layout. Framework: Nielsen #8, Norman, Fogg Ability. Fix: Establish 3-tier hierarchy (primary/secondary/tertiary by size + color + position); increase whitespace between sections.

2. **CTA Overload — No Clear Primary Action** → Detect: 5+ buttons on one screen with similar visual weight; unclear what to tap. Framework: Nielsen #8, Norman (Signifiers). Fix: One primary CTA in brand color; secondary actions smaller or muted; destructive actions in red with confirmation.

3. **Low Contrast / Unreadable Text** → Detect: Light gray on white, or text on busy image background; WCAG AA failing. Framework: WCAG, Nielsen #6, Fogg Ability. Fix: Body text ≥4.5:1 contrast ratio; large text ≥3:1; add semi-transparent overlay on image text.

4. **Thumbnail Inconsistency** → Detect: Grid with mixed aspect ratios, variable quality, some broken images. Framework: Nielsen #4, #8. Fix: Standardize to one aspect ratio (16:9 recommended); consistent border/shadow treatment; placeholder for missing images.

5. **No Accessibility Features** → Detect: Dark mode absent, icons without labels, buttons <48px, no captions. Framework: WCAG 2.1. Fix: Support system dark mode; label all icons; ensure 48px minimum tap targets; add video captions.

6. **Vague Error Messages** → Detect: "Something went wrong" or no error at all; user doesn't know how to recover. Framework: Nielsen #9, Norman (Feedback). Fix: Specific messages ("Email already in use — try logging in"); always include a recovery action.

---

## OUTPUT FORMAT

```markdown
# COGNITIVE LOAD & VISUAL CLARITY — [X]/10

## Evidence Summary

### Visual Hierarchy
- **Focal point**: [What draws eye first]
- **Clarity**: [X]/5 | **Whitespace**: [Spacious / Adequate / Cramped]

### CTA & Buttons
- **CTAs without scroll**: [Count] | **Primary obvious**: [Yes / No]
- **Look tappable**: [Yes / Flat / Inconsistent]

### Typography
- **Readability**: [X]/5 | **Hierarchy**: [Clear / Adequate / Weak]
- **Contrast**: [WCAG pass / fail]

### Color
- **Consistency**: [X]/5 | **Meaning**: [Purposeful / Decorative]

### Spacing
- **Rhythm**: [X]/5 | **Thumbnails**: [Consistent / Variable / Broken]

### Accessibility
- **WCAG level**: [AAA / AA / A / Below A] | **Dark mode**: [Yes / No]

### Overall Cognitive Load
- **Clutter**: [X]/5 | **Scannability**: [X]/5

## Scoring Breakdown

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Visual hierarchy | [X]/10 | [Obvious / Unclear / Absent] |
| CTA clarity | [X]/10 | [Count and primary prominence] |
| Typography | [X]/10 | [Readability and hierarchy] |
| Color consistency | [X]/10 | [Palette size and meaning] |
| Spacing & alignment | [X]/10 | [Rhythm quality] |
| Thumbnails | [X]/10 | [Consistency and quality] |
| Accessibility | [X]/10 | [WCAG level] |
| Error feedback | [X]/10 | [Specificity and recovery] |

**Total Score: [X]/10** | **Justification**: [1-2 sentences]

## Key Issues

### Issue #1: [Title]
**Problem**: [Observed] | **Framework**: [Name] | **Impact**: [User %] | **Hypothesis**: [1-line fix]

## Recommendations

### P0 (Critical)
[Hierarchy, contrast, or accessibility blockers]

### P1 (High)
[CTA clarity, thumbnail consistency, error states]

**Review Conducted**: [Date] | **Duration**: [Speed / Rigor]
```
