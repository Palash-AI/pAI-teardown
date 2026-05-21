# Cognitive Load & Visual Clarity Module

## MODULE OVERVIEW

### What This Module Reviews
This module evaluates the visual design, information hierarchy, and cognitive load across all screens. It assesses whether the app is easy to scan and understand at a glance, or whether users are overwhelmed by visual clutter, unclear hierarchy, and information overload. This is critical for user experience quality and directly impacts engagement.

**Scope**: Every major screen reviewed for visual hierarchy, spacing, typography, color usage, CTA density, thumbnail consistency, button clarity, cognitive load, and accessibility.

### AARRR Stage Mapping
**All Stages** — Cognitive load affects every user interaction, from Acquisition through Referral. This module directly impacts:
- First impression clarity (Acquisition/Activation)
- Navigation confidence (Activation/Engagement)
- Feature discovery (Engagement)
- Decision-making speed (all stages)

### Design Skill Integration (Mandatory for Screenshots)

> **`design:critique`** — Run on key screenshots captured during this module. Evaluate: first impression clarity, usability (can user accomplish their goal?), visual hierarchy (clear reading order?), consistency (spacing, colors, typography), and accessibility (contrast ratios, touch target sizes ≥48px, text readability). For India context: test on budget device screenshots (720p, outdoor brightness) and flag elements that fail on low-end screens.

> **`design:ux-copy`** — Run on all UI copy visible in screenshots. Evaluate: CTA clarity (verb-first labels like "Start learning" not "Submit"), error message structure (what happened + why + how to fix), empty state helpfulness, and voice/tone consistency. For India context: assess Hinglish/Hindi label comprehension — are labels self-explanatory for Tier 2-3 users? Would icon-over-text reduce cognitive load for low-literacy users?
- User satisfaction and NPS (Retention)

### Primary Frameworks & Models

| Framework | Application |
|-----------|-------------|
| **Nielsen's 10 Heuristics** | All 10 evaluated; #1, #4, #6, #8 most critical |
| **Norman's 6 Principles** | Affordances, signifiers, mapping, feedback, conceptual model, constraints |
| **HEART (Happiness)** | Visual design impacts user satisfaction |
| **Fogg's Ability** | Clear design reduces cognitive load; clutter increases friction |
| **Cagan's Usability Risk** | Can users figure out the interface without help? |

---

## SCREENS TO NAVIGATE

### 1. Visual Hierarchy & Information Priority
**Purpose**: Assess whether the most important elements stand out.

**What to Observe**:
- Primary focal point: What element draws your eye first?
- Secondary elements: What comes next visually?
- Information weight: Is important information emphasized (size, color, position)?
- Contrast: Do important elements contrast with background?
- Size differentiation: Headings much larger than body text? Or similar size?
- Whitespace: Is there breathing room, or is layout cramped?
- Element positioning: Is important info above fold? Or scrolled out of view?

**India-Specific Observations:**
- Test on a budget device (5.5" 720p, ₹7-12K phone): are touch targets ≥48px? Is font readable at default?
- Do animations perform smoothly on budget chipsets (Helio G35, Snapdragon 4-series, <4GB RAM)?
- Are UI labels in Hindi/Hinglish for Tier 2-3 users? Is icon-over-text used for low-literacy accessibility?
- Is the UI readable in bright outdoor light on a low-brightness budget screen?
- Does the layout work for single-hand operation on a 6.5" phone?

**What to Screenshot**:
- Full screen view to assess overall hierarchy
- Zoomed view of key elements
- Before/after comparison of two different screens (compare hierarchies)
- Heatmap or focus path (what draws attention first, second, third?)

**What to Document**:
- Primary focal point (what element)
- Visual hierarchy clarity (1-5 scale: obvious to unclear)
- Information positioning (above fold / below fold / off-screen)
- Contrast strength (high / medium / weak)
- Whitespace adequacy (cramped / adequate / spacious)

**Framework Checkpoints**:
- **Nielsen #8 (Minimalism)**: Not every element should have equal weight
- **Norman (Conceptual Model)**: Users should understand structure at a glance
- **Fogg Ability**: Clear hierarchy reduces cognitive load

---

### 2. CTA Density & Button Clarity
**Purpose**: Assess how many calls-to-action are present and whether they're clear.

**What to Observe**:
- Number of CTAs on screen: Single clear CTA / 2-3 options / 5+ options / Overwhelming
- CTA prominence: Primary action stands out / All equal weight / Hidden/unclear
- Button design: Look tappable (rounded corners, shadow, color) / Flat, hard to identify / Text links
- CTA labels: Clear action (Play, Subscribe, Save, Delete) / Vague (OK, Submit, Next) / No label
- CTA color: Distinct color draws attention / Blend with background / Color-coded meaning
- Button size: Hit target ≥48px / <48px (too small) / Variable
- Destructive actions: Delete/logout are visually distinct / Look same as other CTAs

**What to Screenshot**:
- Full screen showing all CTAs
- Zoomed view of primary CTA
- Zoomed view of secondary CTAs
- Destructive action button (if present) showing visual treatment
- Comparison of button designs on different screens

**What to Document**:
- Number of CTAs visible without scroll
- CTA clarity (1-5 scale: obvious to confusing)
- Button hit target size (estimated minimum)
- Destructive action clarity (obvious / same as others)
- Visual consistency (all buttons look like buttons / inconsistent styling)

**Framework Checkpoints**:
- **Nielsen #4 (Consistency)**: All CTAs should look like CTAs
- **Norman (Affordances)**: Buttons should look tappable
- **Nielsen #1 (Visibility)**: Primary CTA should be obvious
- **Nielsen #8 (Minimalism)**: Too many CTAs = cognitive overload

---

### 3. Typography & Readability
**Purpose**: Assess text readability and hierarchy.

**What to Observe**:
- Font selection: Professional / Generic / Difficult to read / Accessible
- Font size hierarchy: Distinct levels (heading, subheading, body, small text) / All same size
- Line spacing: Adequate leading for readability / Cramped / Too loose
- Contrast: Dark text on light background (good) / Low contrast (hard to read) / Uneven
- Font weight: Bold used for emphasis / All same weight / Overuse of bold
- Text alignment: Consistent (left, center, right) / Mixed alignment
- Line length: ~50-75 characters per line / Too long (hard to scan) / Too short (choppy)
- Text truncation: Long text is truncated with "..." / No truncation / Wrapping awkwardly

**What to Screenshot**:
- Sample of heading text (size, weight, color)
- Sample of body text (readability, line spacing)
- Zoomed comparison of text hierarchy
- High-contrast area vs. low-contrast area

**What to Document**:
- Typography hierarchy clarity (1-5 scale)
- Readability (1-5 scale: very readable to difficult)
- Font choice appropriateness (1-5 scale)
- Color contrast (high / medium / low) for each text type
- Line spacing adequacy (cramped / adequate / loose)

**Framework Checkpoints**:
- **Nielsen #6 (Recognition)**: Hierarchy should make content scannable
- **Nielsen #8 (Aesthetic/Minimalist)**: Typography should be clean, not ornate
- **WCAG Accessibility**: Contrast ratio ≥4.5:1 for body text; ≥3:1 for large text

---

### 4. Color Usage & Consistency
**Purpose**: Assess color scheme appropriateness and consistency.

**What to Observe**:
- Color palette: Coherent / Random / Too many colors
- Primary color use: Consistent (same color for CTAs, links, focus) / Inconsistent
- Color meaning: Colors have meaning (red = error, green = success) / Colors are decorative only
- Accessibility: Color-blind safe (no red-green only distinction) / Problematic
- Background/text contrast: Good for readability / Poor contrast / Variable
- Theme consistency: Colors match brand / Mismatched / No apparent theme
- Status colors: Success/error/warning clearly distinguished / Hard to tell apart

**What to Screenshot**:
- Color palette overview (show all colors used)
- Comparison of CTA colors across screens (consistent or not)
- Error message in red (if present)
- Success state in green (if present)
- Focus state (highlighted color on interactive element)

**What to Document**:
- Number of distinct colors used (compact palette vs. rainbow)
- Color consistency (1-5 scale: same use everywhere to completely inconsistent)
- Accessibility (color-blind safe / problematic)
- Meaning clarity (colors have purpose / decorative only)
- Status color distinction (error, warning, success clearly different / hard to tell)

**Framework Checkpoints**:
- **Nielsen #4 (Consistency)**: Colors should mean the same thing everywhere
- **WCAG Accessibility**: Color shouldn't be sole information conveyor
- **Norman (Mapping)**: Colors should logically map to meaning (red = stop, green = go)

---

### 5. Spacing, Alignment & Grid
**Purpose**: Assess visual rhythm and layout structure.

**What to Observe**:
- Spacing rhythm: Consistent spacing between elements / Inconsistent gaps
- Grid alignment: Elements aligned to invisible grid / Misaligned / Chaotic
- Padding around text: Text has breathing room / Cramped against edges
- Consistent margins: Section margins are proportional / Vary randomly
- Card/module consistency: All cards similar size/spacing / Variable
- Alignment: Left/center/right consistently applied / Mixed alignment
- Responsive spacing: Spacing adapts to different screen sizes / Fixed spacing breaks layout

**What to Screenshot**:
- Full screen showing overall spacing rhythm
- Zoomed view of element spacing (padding, margins)
- Overlay showing alignment grid (if visible)
- Two different screen sizes showing responsive spacing

**What to Document**:
- Spacing consistency (1-5 scale: perfect rhythm to chaotic)
- Grid alignment quality (1-5 scale: perfectly aligned to chaotic)
- Padding adequacy (1-5 scale: cramped to spacious)
- Visual rhythm quality (1-5 scale: pleasing to jarring)

**Framework Checkpoints**:
- **Nielsen #4 (Consistency)**: Spacing should follow a consistent system
- **Nielsen #8 (Aesthetic/Minimalist)**: Good spacing creates visual calm
- **Fogg Ability**: Good spacing reduces cognitive load

---

### 6. Thumbnail Quality & Image Consistency
**Purpose**: Assess visual quality of content thumbnails and images.

**What to Observe**:
- Thumbnail size consistency: All thumbnails same aspect ratio / Variable sizes
- Image quality: Professional, high-res / Low-res, pixelated / Missing thumbnails
- Image treatment: Consistent (all have border, shadow, etc.) / Inconsistent
- Missing images: Placeholder shown / Broken images / No placeholder
- Image loading: Images load fast / Lazy-loaded, creates blank spaces / Janky load
- Text overlay on images: Readable (good contrast) / Overlapped text / No contrast
- Image optimization: Quick to load / Heavy file sizes / Fast responsive

**What to Screenshot**:
- Grid of thumbnail images showing size consistency
- Close-up of thumbnail quality (professional vs. low-res)
- Text overlay on image (readability check)
- Empty state or placeholder (if image fails to load)
- Slow-loading image during scroll

**What to Document**:
- Thumbnail consistency (1-5 scale: identical to variable)
- Image quality (1-5 scale: professional to poor)
- Readability of text on images (1-5 scale: clear to hard to read)
- Load performance (fast / acceptable / slow)
- Placeholder quality (helpful / missing / poor)

**Framework Checkpoints**:
- **Nielsen #4 (Consistency)**: Thumbnails should have consistent styling
- **Nielsen #1 (Visibility)**: Missing images should have clear placeholders
- **Nielsen #8 (Aesthetic/Minimalist)**: High-quality images improve aesthetic

---

### 7. Accessibility & Inclusive Design
**Purpose**: Assess whether design is accessible to users with disabilities.

**What to Observe**:
- Color contrast: Text/background ratio ≥4.5:1 for body / <4.5:1 (fails WCAG)
- Touch targets: Buttons ≥48px / <48px (too small for motor accessibility)
- Text alternatives: Icons have labels / Text only on hover / No alternative text
- Focus indicators: Keyboard focus visible / Not visible
- Motion: Animations present / Reduced motion option available / Seizure risk
- Audio: Captions for video / Video only / No captions
- Readability: Font size ≥12px / <12px (too small)
- Dark mode: Supported / Light only (problematic for light sensitivity)

**What to Screenshot**:
- Color contrast check (use WebAIM contrast checker in your mind)
- Focus state on buttons/links (keyboard navigation)
- Icon with/without label
- Small touch target (button that's <48px)
- Video with captions (if present)

**What to Document**:
- WCAG compliance level (AAA / AA / A / None)
- Major accessibility gaps (none / minor / major)
- Dark mode availability (yes / no / partial)
- Keyboard navigation (fully supported / partial / not supported)
- Screen reader friendliness (estimated: good / adequate / poor)

**Framework Checkpoints**:
- **WCAG 2.1 Standards**: Contrast, touch targets, alt text, keyboard nav
- **Nielsen #10 (Help & Documentation)**: Accessibility features help diverse users
- **Norman (Constraints)**: Good design prevents errors through structure

---

### 8. Error States & Feedback Clarity
**Purpose**: Assess how errors are presented and whether recovery is obvious.

**What to Observe**:
- Error messages: Specific ("Email is invalid") / Generic ("Error") / Helpful
- Error visibility: Red color + text / Red only / Tooltip / Not visible
- Error recovery: Suggestion provided / User must guess / Not possible
- Success feedback: Confirmation screen / Toast notification / Silent / Not clear
- Loading states: Spinner / Progress bar / Skeleton screen / Nothing (confusing)
- Disable feedback: Disabled button looks disabled / Looks active / Unclear
- Validation timing: Real-time (as user types) / On submit / On blur
- Error prevention: Form validation before submit / No validation

**What to Screenshot**:
- Error state showing message (specific or generic)
- Success confirmation (celebration, modal, toast)
- Loading state (spinner, skeleton, etc.)
- Disabled button (visual treatment)
- Form validation feedback

**What to Document**:
- Error message quality (1-5 scale: specific/helpful to vague)
- Recovery guidance (obvious / requires thought / no guidance)
- Feedback clarity (1-5 scale: obvious to unclear)
- Loading state presence (visible / hidden / confusing)
- Validation feedback (real-time / on submit / none)

**Framework Checkpoints**:
- **Nielsen #1 (Visibility)**: Errors should be obvious
- **Nielsen #9 (Error Recovery)**: Messages should help user recover
- **Norman (Feedback)**: Users should always know what happened

---

## SCORING RUBRIC (1-10)

### 9-10: Best-in-Class (Apple, Google, Figma Level)

**Criteria**:
- **Visual hierarchy is perfect**: Scanning the screen, you immediately see the key information
- **Typography is excellent**: Clear heading/body hierarchy; highly readable; professional fonts
- **Color is purposeful**: Limited palette; consistent meaning; accessible; beautiful
- **Spacing is rhythmic**: Consistent margins/padding; breathing room; grid-aligned
- **CTAs are obvious**: Clear primary action; secondary actions are clear; no ambiguity
- **Thumbnails are consistent**: All same ratio/style; high quality; professional
- **Accessibility is excellent**: WCAG AAA compliance; dark mode; keyboard nav; captions
- **No cognitive overload**: Every element has purpose; minimal clutter; elegant simplicity
- **Feedback is clear**: Errors are specific with recovery guidance; success is celebrated; loading is obvious
- **Polish is evident**: No rough edges; attention to detail; premium feel

**Framework Alignment**:
- **Nielsen #1, #4, #6, #8**: All heuristics exceeded
- **Norman**: All 6 principles implemented beautifully
- **HEART Happiness**: Design increases user satisfaction
- **Fogg Ability**: Clarity reduces friction; easy to use
- **Cagan Usability Risk**: Zero friction; users never get stuck

**Examples**: Apple iOS (design excellence), Google Material Design (clarity), Figma (cognitive clarity)

---

### 7-8: Good / Professional Design

**Criteria**:
- **Visual hierarchy is clear**: Primary, secondary, tertiary elements obviously distinguished
- **Typography is professional**: Hierarchy visible; mostly readable
- **Color is consistent**: Palette is limited; colors have meaning
- **Spacing is adequate**: Breathing room; mostly consistent; minor inconsistencies
- **CTAs are clear**: Primary action obvious; secondary actions are clear
- **Thumbnails are mostly consistent**: Same ratio, professional quality
- **Accessibility is adequate**: WCAG AA compliance; some dark mode / alt text
- **Minimal cognitive overload**: Most elements are necessary; some could be removed
- **Feedback is present**: Errors shown; success acknowledged; loading visible
- **Polish is good**: Professional look; few rough edges

**Framework Alignment**:
- **Nielsen #1, #4, #6, #8**: Most heuristics satisfied
- **Norman**: Most principles implemented
- **HEART Happiness**: Design is pleasant; doesn't detract from experience

**Examples**: Many well-designed apps in top 50

---

### 5-6: Adequate / Decent but Imperfect

**Criteria**:
- **Visual hierarchy is present but unclear**: Can identify main elements; some confusion about priority
- **Typography is serviceable**: Hierarchy exists; some readability issues
- **Color is inconsistent**: Some colors have meaning; others are decorative; palette is large
- **Spacing is uneven**: Some breathing room; some cramped areas; inconsistent system
- **CTAs are present**: Main action is visible; secondary actions are unclear
- **Thumbnails are inconsistent**: Some same ratio; some variable; quality varies
- **Accessibility is basic**: WCAG A compliance; no dark mode; some alt text missing
- **Some cognitive overload**: Some elements could be removed; mild clutter
- **Feedback is partial**: Errors shown but may be vague; success may be silent; loading may not be clear
- **Design feels adequate**: Professional enough; some rough edges

**Framework Alignment**:
- **Nielsen**: Some heuristics violated (consistency, minimalism)
- **HEART Happiness**: Design is neutral; doesn't delight or offend

**Examples**: Many average apps

---

### 3-4: Poor / Cluttered or Confusing Design

**Criteria**:
- **Visual hierarchy is weak**: All elements compete equally; hard to scan; confusing priorities
- **Typography is unclear**: Hierarchy is weak; readability issues; poor font choices
- **Color is chaotic**: Too many colors; colors don't mean anything consistent; inaccessible
- **Spacing is inconsistent**: Cramped areas; large gaps; no system; random
- **CTAs are unclear**: Multiple equal-weight CTAs; main action not obvious; button style varies
- **Thumbnails are inconsistent**: Different aspect ratios; variable quality; unprofessional
- **Accessibility is poor**: WCAG A violations; no dark mode; no alt text
- **Heavy cognitive overload**: Many unnecessary elements; clutter; overwhelming
- **Feedback is missing**: Errors may not be visible; success is silent; loading is unclear
- **Design feels cheap**: Rough, unpolished; looks amateur

**Framework Alignment**:
- **Nielsen #8 (Minimalism)**: Violated heavily; cluttered
- **Fogg Ability**: High friction due to cognitive load
- **HEART Happiness**: Design is unpleasant; may actively reduce satisfaction

**Examples**: Many poorly designed budget apps

---

### 1-2: Severely Flawed / Visual Chaos or Broken Design

**Criteria**:
- **No visual hierarchy**: Everything is equally prominent; completely unscable
- **Typography is unreadable**: Poor contrast; tiny fonts; confusing hierarchy; ornate fonts
- **Color is overwhelming**: 10+ colors; no consistency; inaccessible
- **Spacing is broken**: Cramped everywhere; misaligned; no grid
- **CTAs are invisible or misleading**: Buttons don't look like buttons; hard to find
- **Thumbnails are broken**: Missing images; broken links; wildly inconsistent
- **Accessibility is non-existent**: WCAG violations; no accessibility features
- **Severe cognitive overload**: Ads, pop-ups, clutter everywhere; can barely use app
- **No feedback**: Errors are silent; loading is invisible; confusing state
- **Design is broken**: Looks like an error; unusable

**Framework Alignment**:
- **Nielsen**: Multiple heuristics violated
- **Norman**: Design principles ignored
- **Fogg Ability**: Friction is extreme; users abandon
- **HEART Happiness**: Design actively damages satisfaction

**Examples**: Spammy apps, broken rebuilds, ad-heavy apps

---

## EVIDENCE CHECKLIST

### Visual Hierarchy

- [ ] **Primary focal point**: [Element that draws eye first]
- [ ] **Hierarchy clarity** (1-5 scale): [_____]
- [ ] **Information weight**: [Important elements emphasized / Equal weight / Hidden]
- [ ] **Contrast strength**: [High / Medium / Weak]
- [ ] **Whitespace adequacy**: [Cramped / Adequate / Spacious]

**Framework**: Nielsen #8, Norman (Conceptual Model)

---

### CTA & Button Design

- [ ] **CTAs visible without scroll**: [Number: _____]
- [ ] **Primary CTA prominence**: [Obvious / Clear / Equal with secondary / Hidden]
- [ ] **Button appearance**: [Look tappable / Flat, unclear / Text links]
- [ ] **CTA labels**: [Clear action / Vague / No label]
- [ ] **Color distinctness**: [Distinct color / Blend with background / Variable]
- [ ] **Hit target size**: [≥48px / <48px / Variable]
- [ ] **Destructive actions marked**: [Visually distinct / Same as others / Not applicable]

**Framework**: Nielsen #1, #4, Norman (Affordances)

---

### Typography

- [ ] **Font selection**: [Professional / Generic / Difficult / Accessible]
- [ ] **Hierarchy clarity** (1-5 scale): [_____]
- [ ] **Line spacing**: [Adequate / Cramped / Too loose]
- [ ] **Contrast**: [Dark/light text / Low contrast / Uneven]
- [ ] **Font weight usage**: [Bold for emphasis / All same / Overused]
- [ ] **Text alignment**: [Consistent / Mixed / Random]
- [ ] **Line length**: [~50-75 chars / Too long / Too short]
- [ ] **Readability** (1-5 scale): [_____]

**Framework**: Nielsen #6, #8, WCAG Accessibility

---

### Color Usage

- [ ] **Color palette size**: [Compact / Moderate / Rainbow]
- [ ] **Primary color consistency**: [Same color for CTAs/links / Inconsistent]
- [ ] **Color meaning**: [Has purpose / Decorative / Confusing]
- [ ] **Accessibility**: [Color-blind safe / Problematic]
- [ ] **Text/background contrast**: [WCAG AAA / AA / A / Fails]
- [ ] **Status colors** (error/success/warning): [Distinct / Hard to tell apart / Not colored]

**Framework**: Nielsen #4, #8, Norman (Mapping), WCAG

---

### Spacing & Alignment

- [ ] **Spacing rhythm** (1-5 scale): [_____]
- [ ] **Grid alignment** (1-5 scale): [_____]
- [ ] **Padding adequacy**: [Cramped / Adequate / Spacious]
- [ ] **Margin consistency**: [Proportional / Random / None]
- [ ] **Card/module consistency**: [All similar / Variable / Inconsistent]

**Framework**: Nielsen #4, #8, Norman (Mapping)

---

### Thumbnails & Images

- [ ] **Thumbnail consistency** (1-5 scale): [_____]
- [ ] **Image quality**: [Professional / Low-res / Missing]
- [ ] **Image treatment**: [Consistent / Inconsistent / Variable]
- [ ] **Missing image handling**: [Placeholder shown / Broken / None]
- [ ] **Load performance**: [Fast / Acceptable / Slow]
- [ ] **Text readability on images**: [Clear / Difficult / Overlapped]

**Framework**: Nielsen #1, #4, #8

---

### Accessibility

- [ ] **Color contrast ratio**: [WCAG AAA / AA / A / Fails]
- [ ] **Touch target size**: [≥48px / <48px / Variable]
- [ ] **Text alternatives**: [Present / Missing / Partial]
- [ ] **Focus indicators**: [Visible / Not visible / Partial]
- [ ] **Motion/animation**: [Reduced motion option / Seizure risk / None]
- [ ] **Audio content**: [Captions / No captions / Not applicable]
- [ ] **Font readability**: [≥12px / <12px / Variable]
- [ ] **Dark mode**: [Supported / Light only / Partial]
- [ ] **Keyboard navigation**: [Fully supported / Partial / Not supported]

**Framework**: WCAG 2.1, Nielsen #10

---

### Error States & Feedback

- [ ] **Error messages**: [Specific / Generic / Helpful / None]
- [ ] **Error visibility**: [Obvious / Subtle / Not visible]
- [ ] **Error recovery**: [Guidance provided / User must guess / Not possible]
- [ ] **Success feedback**: [Celebration / Toast / Silent / Not clear]
- [ ] **Loading states**: [Visible / Invisible / Confusing]
- [ ] **Disabled state**: [Looks disabled / Active / Unclear]
- [ ] **Validation timing**: [Real-time / On submit / None]

**Framework**: Nielsen #1, #5, #9, Norman (Feedback)

---

### Overall Cognitive Load

- [ ] **Clutter assessment** (1-5 scale, 5 = very cluttered): [_____]
- [ ] **Essential elements only**: [Yes / Some unnecessary / Many unnecessary]
- [ ] **Visual calm** (1-5 scale): [_____]
- [ ] **Scannability** (1-5 scale): [_____]

**Framework**: Nielsen #8, Fogg (Ability)

---

## KEY ISSUES TEMPLATE

### Issue #1: Visual Hierarchy is Unclear; All Elements Compete Equally
**Problem**: Every element on the screen has similar visual weight. User doesn't know what to focus on.

**Framework Cite**:
- **Nielsen #8 (Minimalism)**: Not every element should be equally prominent
- **Norman (Conceptual Model)**: Users should understand structure at a glance
- **Fogg Ability**: Unclear hierarchy increases cognitive load

**Evidence**: Screenshot showing all elements with similar size/color/weight. No obvious focal point.

**Quantified Impact**: Apps with poor hierarchy see 30-50% lower engagement. Users are confused and leave.

**Hypothesis for Improvement**:
1. Establish clear hierarchy: Primary (largest, top), secondary (medium), tertiary (small)
2. Use color strategically: Primary action in brand color; secondary in neutral
3. Whitespace: Increase padding to separate sections
4. Test: Show to 5 users and ask "What's the most important thing on this screen?" Should be obvious.

Estimated impact: 30-50% improvement in engagement, 20-30% improvement in conversion.

**Comparative Benchmark**: Apple's iOS has crystal-clear hierarchy. Google Material Design clearly differentiates primary/secondary actions.

---

### Issue #2: CTA Overload; Too Many Buttons and Unclear Primary Action
**Problem**: Screen has 5+ buttons, all styled similarly. User doesn't know which to tap first.

**Framework Cite**:
- **Nielsen #8 (Minimalism)**: Each screen should have one primary action
- **Norman (Signifiers)**: Primary CTA should be obviously tappable
- **Fogg Ability**: Multiple equal CTAs create decision paralysis

**Evidence**: Screenshot showing 5+ buttons. Identify which is primary (if unclear, proves the point).

**Quantified Impact**: Apps with clear primary CTA see 50% higher conversion on that action. Apps with multiple equal CTAs see decision paralysis and abandonment.

**Hypothesis for Improvement**:
1. One primary CTA per screen: Make it obvious (largest, brightest color)
2. Secondary CTAs: Smaller or muted color (tap if interested)
3. Destructive actions: Different color or confirmation (delete, logout)
4. Test: A/B test single clear CTA vs. multiple buttons. Measure conversion.

Estimated impact: 50-100% improvement in primary CTA conversion.

**Comparative Benchmark**: Apps like Slack, Duolingo, Spotify have one clear primary action per screen.

---

### Issue #3: Low Contrast or Unreadable Text
**Problem**: Light gray text on white background or other low-contrast combinations. Hard to read.

**Framework Cite**:
- **WCAG Accessibility**: Text contrast should be ≥4.5:1 for body, ≥3:1 for large text
- **Nielsen #6 (Recognition)**: Users should be able to recognize text easily
- **Fogg Ability**: Difficulty reading = friction

**Evidence**: Screenshot showing low-contrast text. Use contrast checker (in your mind: does dark text on light background meet 4.5:1?).

**Quantified Impact**: Low contrast violates accessibility standards and excludes 15-20% of users (color-blind, low vision). Improves engagement across all users.

**Hypothesis for Improvement**:
1. Dark text on light background (or light on dark for dark mode)
2. Contrast ratio ≥4.5:1 for body text (WCAG AA)
3. Contrast ratio ≥3:1 for large text (WCAG AA)
4. Test with contrast checker (WebAIM tool)

Estimated impact: 15-20% improvement in readability, enables accessibility compliance.

**Comparative Benchmark**: Apple's iOS achieves excellent contrast in dark and light modes. Google Material Design sets clear contrast standards.

---

### Issue #4: Cluttered Design with Too Many Elements
**Problem**: Screen is packed with information, ads, buttons, sections. Visually overwhelming.

**Framework Cite**:
- **Nielsen #8 (Minimalism)**: Every element should be necessary. Remove the rest.
- **Fogg Ability**: Clutter is cognitive friction
- **Norman**: Clear, minimal design reduces mental load

**Evidence**: Screenshot showing crowded screen. Count elements. Identify which could be removed.

**Quantified Impact**: Cluttered apps see 40-60% higher bounce rate. Minimal apps see higher engagement and satisfaction.

**Hypothesis for Improvement**:
1. Remove non-essential elements: Ads, secondary features, duplicate sections
2. Progressive disclosure: Hide advanced features; show basics first
3. Whitespace: Increase padding and margins to create breathing room
4. Test: Show cluttered vs. clean version. Users prefer clean.

Estimated impact: 40-60% improvement in engagement, 20-30% improvement in satisfaction.

**Comparative Benchmark**: Apple's focus on minimalism (white space, few elements). Notion balances information density but with clear hierarchy.

---

### Issue #5: Thumbnails are Inconsistent; Variable Size/Aspect Ratio
**Problem**: Content thumbnails are different sizes, aspect ratios, and quality. Layout is jarring.

**Framework Cite**:
- **Nielsen #4 (Consistency)**: Visual elements should be consistent
- **Nielsen #8 (Aesthetic/Minimalist)**: Inconsistency creates visual chaos
- **Norman**: Visual consistency builds trust in system

**Evidence**: Screenshot showing grid of thumbnails. Measure aspect ratios. Show inconsistency.

**Quantified Impact**: Consistent thumbnails look professional and increase engagement. Inconsistent thumbnails feel amateur and reduce trust.

**Hypothesis for Improvement**:
1. Standardize aspect ratio: All thumbnails 16:9, 4:3, or 1:1 (pick one)
2. Consistent styling: Border, shadow, or none—apply to all
3. Placeholder for missing images: Don't show broken images
4. High quality: Optimize images; no pixelation; professional look

Estimated impact: 10-20% improvement in aesthetic perception, higher engagement with content.

**Comparative Benchmark**: YouTube uses consistent 16:9 aspect ratio. Netflix uses consistent card styling. Both feel polished.

---

### Issue #6: No Accessibility; Dark Mode Missing, Poor Contrast, No Captions
**Problem**: App has no accessibility features. Excludes color-blind, low-vision, and deaf users.

**Framework Cite**:
- **WCAG Accessibility**: Should support ≥AA level
- **Nielsen #10 (Help & Documentation)**: Accessibility features are critical support
- **Norman**: Good design includes everyone

**Evidence**: Attempt dark mode (not available), check contrast (WCAG violations), check captions (none), test keyboard nav (broken).

**Quantified Impact**: ~20% of population has some form of disability. Accessibility improves usability for everyone (elderly, low light, etc.).

**Hypothesis for Improvement**:
1. Dark mode: Support system-wide dark mode preference
2. Contrast: Ensure ≥4.5:1 on text; test with contrast checker
3. Alt text: Add descriptions to images for screen readers
4. Captions: Add captions to videos
5. Keyboard navigation: Make all features usable via keyboard
6. Touch targets: Ensure buttons are ≥48px

Estimated impact: 15-20% expansion of addressable user base, 10-15% improvement in overall UX (good accessibility benefits everyone).

**Comparative Benchmark**: Apple's iOS sets high accessibility standards. Google Material Design includes accessibility as core principle.

---

## SPEED MODE vs RIGOR MODE

### SPEED MODE (15 minutes)
1. Visual hierarchy → Obvious or unclear?
2. CTAs → How many? Primary obvious?
3. Color → Consistent / Chaos?
4. Spacing → Cramped / Adequate / Spacious?
5. Thumbnails → Consistent?
6. Accessibility → Dark mode, contrast, captions?
7. Note 2-3 issues
8. Assign score

**Output**: 1 page

---

### RIGOR MODE (45-60 minutes)
1. Visual hierarchy audit (every major screen)
2. CTA density and clarity across all screens
3. Typography hierarchy and readability
4. Color consistency and meaning
5. Spacing and alignment across all screens
6. Thumbnail consistency and quality
7. Accessibility audit (WCAG compliance)
8. Error states and feedback clarity
9. Full Evidence Checklist
10. 5-7 key issues
11. Detailed scoring

**Output**: 5-10 pages

---

## PERSONA-SPECIFIC INSTRUCTIONS

### 1. First-time User
**Test**: Can they understand the interface without help?

**Key Metrics**: Visual clarity, hierarchy obviousness, CTA clarity

**Scoring Focus**: Discoverability, learning curve

### 2. Color-Blind User
**Test**: Can they distinguish status colors (error vs. success)?

**Key Metrics**: Contrast, non-color signals, accessibility

**Scoring Focus**: WCAG compliance, accessibility

### 3. Low-Vision User
**Test**: Is text readable? Are buttons large enough?

**Key Metrics**: Text size, contrast, touch target size

**Scoring Focus**: Contrast, readability, touch targets

---

## DOMAIN-SPECIFIC OVERLAYS

### Education Apps
- **Domain criteria**: Is visual hierarchy supporting learning? Clear progression?
- **Scoring modifier**: +1 if difficulty levels visually distinguished; -1 if all content looks same

### OTT/Streaming
- **Domain criteria**: Are content cards consistent? Is metadata clear?
- **Scoring modifier**: +1 if thumbnails are high quality and consistent; -1 if variable

---

## INDIA-SPECIFIC CHECKS

Every review of an Indian app must include these checks for this module:

### Budget Phone Screen Test
- [ ] Tested on a budget device (5.5-6.5" screen, 720p resolution, ₹5-12K phone)?
- [ ] Are touch targets at least 48px (44px minimum)?
- [ ] Is font readable at default size on a low-brightness screen? (Minimum 14px recommended)
- [ ] Does the layout work for single-hand operation on a 6.5" phone?
- [ ] Are animations smooth on budget chipsets (Helio G35, Snapdragon 4-series, <4GB RAM)?
- [ ] Impact if missing: 60%+ of Indian smartphones are budget devices. An app designed for flagship phones with intricate animations and small touch targets will feel broken for the majority of users.

**Finding template:** "App tested on [budget device]. Animations stutter visibly. Touch targets are <44px. Font at default size requires squinting on 720p screen. Background image loading blocks content. This app is designed for flagships — 60%+ of Indian users on budget devices will have a degraded experience."

**India Benchmark:** Zepto's minimal UI loads in <3 seconds even on budget devices. CRED achieves premium feel with smooth animations that degrade gracefully on lower-end devices — fewer animations, same design quality.

### Hinglish/Hindi Label Comprehension
- [ ] Are UI labels in language the user understands (Hindi/Hinglish for Tier 2-3)?
- [ ] Is icon-over-text prioritized for low-literacy users?
- [ ] Are icons universally understood (not culturally specific to Western users)?
- [ ] Is the navigation self-explanatory without reading text labels?
- [ ] Impact if missing: For Tier 2-3 users with lower English proficiency, English-only labels increase cognitive load significantly. Icon-based navigation reduces this.

**Finding template:** "All UI labels are in English. No Hindi labels. Icons are abstract (not self-explanatory). For Tier 2-3 users, every screen requires mental translation from English — this multiplies cognitive load by 2-3x."

**India Benchmark:** Meesho uses large visual icons with minimal text. Josh/Moj's navigation is entirely icon-based with Hindi labels — near-zero learning curve across tiers.

### Outdoor Readability & Display Constraints
- [ ] Is the UI readable in bright outdoor light (common use context in India)?
- [ ] Is contrast ratio sufficient for low-brightness screens (budget phones often have dim displays)?
- [ ] Does dark mode exist for AMOLED screens (popular on budget Samsung/Realme)?
- [ ] Are colors distinguishable on lower-quality displays?
- [ ] Impact if missing: Indian mobile usage frequently occurs outdoors (commuting, waiting). Low-contrast UIs become invisible in sunlight on budget screens.

**Finding template:** "UI uses light grays on white background. On a budget phone screen in outdoor light, key labels and buttons become invisible. No dark mode option despite AMOLED prevalence on budget Indian phones."

**India Benchmark:** CRED's dark-themed UI is readable across lighting conditions. Zepto's high-contrast design (white on dark backgrounds for key CTAs) works across budget displays.

### Scoring Modifiers (India)
- +1 if tested and optimized for budget devices (≤₹12K phones)
- +1 if icons-over-text navigation for low-literacy accessibility
- +1 if Hindi/Hinglish UI labels available
- -1 if animations lag on budget chipsets (<4GB RAM)
- -1 if touch targets <44px on any screen
- -1 if font size <14px at default setting
- -1 if no dark mode despite AMOLED prevalence

---

## OUTPUT FORMAT

```markdown
# COGNITIVE LOAD & VISUAL CLARITY — [X]/10

## Evidence Summary

### Visual Hierarchy
- **Clarity**: [X]/5
- **Focal point**: [Element that draws eye first]
- **Information weight**: [Obvious / Equal / Confused]

### CTA & Buttons
- **Number visible**: [X] without scroll
- **Primary action**: [Obvious / Clear / Unclear]
- **Button clarity**: [Look tappable / Unclear / Inconsistent]

### Typography
- **Readability**: [X]/5
- **Hierarchy**: [Clear / Adequate / Weak]
- **Professional**: [Yes / Adequate / Poor]

### Color
- **Consistency**: [X]/5
- **Meaning**: [Purposeful / Decorative / Confusing]
- **Contrast**: [Good / Adequate / Poor]

### Spacing
- **Rhythm**: [X]/5
- **Whitespace**: [Spacious / Adequate / Cramped]
- **Alignment**: [Consistent / Mostly / Chaotic]

### Accessibility
- **WCAG level**: [AAA / AA / A / Below A]
- **Dark mode**: [Yes / No]
- **Contrast**: [Good / Adequate / Poor]

### Overall Cognitive Load
- **Clutter**: [X]/5 (5 = very cluttered)
- **Scannability**: [X]/5
- **Visual calm**: [X]/5

---

[Detailed Evidence, Scoring Breakdown, Key Issues sections follow standard format]

**Review Conducted**: [Date] | **Reviewer**: [Name] | **Duration**: [Mode]
```

---

## Summary

This module evaluates the visual and cognitive experience—the foundation of usability. It assesses whether users can quickly understand the interface, find key actions, and execute tasks without mental strain. Grounded in Nielsen's usability heuristics, Norman's design principles, WCAG accessibility standards, and Fogg's behavioral model, this module ensures the app is not just functional but beautiful and clear.

