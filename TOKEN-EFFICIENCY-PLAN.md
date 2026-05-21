# pAI Teardown — Token Efficiency Plan

> **Role:** Principal AI Systems Architect
> **Date:** February 2026
> **Model analysed:** claude-sonnet-4-6 ($3/MTok input · $15/MTok output)

---

## The Diagnosis

A full 10-module rigor review currently consumes **~182,000 input tokens** and costs **~$0.77/run**.
A single-module rigor review costs **~$0.24/run**.

That sounds cheap. It isn't — because **only 8% of what you're loading is information Claude doesn't already know**.

```
Full review — where input tokens go today
─────────────────────────────────────────
All 10 module files          100K tok  (55%)
  ↳ Example issues/templates  55K tok  (30%) ← pure waste
  ↳ Irrelevant domain overlays 15K tok  (8%) ← waste
  ↳ Unused persona sections    16K tok  (9%) ← waste
  ↳ Genuinely needed           14K tok  (8%) ← keep

PDF template re-read each run  12K tok   (7%) ← avoidable
Framework/domain/india context 20K tok  (11%) ← can compress 75%
Screenshots (30 × 1.5K)        45K tok  (25%) ← irreducible
```

The frameworks — Fogg MAP, HEART, Nielsen, JTBD, Hook Model — are deeply embedded in Claude's
training. Writing out full explanations of them adds tokens without adding knowledge. Same for
example issue writeups, domain overlays for the wrong domain, and persona flows for untested personas.

---

## The 7 Efficiency Tactics

### Tactic 1 — Strip framework boilerplate from module files
**Savings: ~55K tokens per full review | 30% of current input**

Each module currently re-explains every framework in 20-40 lines. Claude knows these.

**Current pattern (16K tokens — onboarding.md alone):**
```
### Fogg Behavioral Model
B = MAP (Behavior = Motivation × Ability × Prompt)
All three must be present simultaneously...
| Factor | Definition | What to Audit |
...30 more lines...
```

**Lean pattern (2 tokens):**
```
Primary frameworks: Fogg MAP · HEART Adoption · Nielsen #3 · JTBD · Kano
Audit focus: [3 specific things to check for this module]
```

Claude already knows the model. It only needs to know which framework applies and what to look for.
Remove all framework re-explanations from module files. Replace with a 3-column mapping table
(framework → key principle → what to look for in this specific app category).

---

### Tactic 2 — Extract domain overlays to separate files, load only the relevant one
**Savings: ~15K tokens per run | 8% of current input**

The onboarding module alone has domain-specific overlays for Education, OTT, Social, Finance,
Productivity, Health, and Messaging. For an education-app review you load 6 irrelevant domains.

**Current:** Overlays embedded in every module file → always loaded.

**Fix:** Each domain file (`domains/education.md`) contains the overlays. Module files reference
`→ Apply [domain] overlay from domains/[domain].md`. The orchestrator already loads the right
domain file; modules just inherit it. Since the domain file is already loaded, the modules need
zero additional text for domain specifics.

---

### Tactic 3 — Load only the active persona's instructions
**Savings: ~16K tokens per full review | 9% of current input**

Each module documents all 5 personas (new-user, free-user, trial-user, paid-user, lapsed-user).
When running as `new-user`, the other 4 personas' instructions load and are ignored.

**Fix:** Persona instructions move to `context/personas/[persona].md`. Modules reference
`→ Persona: see context/personas/[persona].md`. The orchestrator loads only the right one.
The active persona file should be <100 lines covering all 10 modules' persona-specific angles.

---

### Tactic 4 — Remove verbose example issues from module files
**Savings: ~10-15K tokens per module in rigor mode**

Each module has 8-10 example issue writeups (150-200 words each). These exist as "scaffolding
for a weaker model." Claude claude-sonnet-4-6 doesn't need scaffolding — it needs the
**framework mapping + evidence checklist**, not a pre-written example it must NOT copy verbatim.

**Keep:** Issue categories and a 1-line "anchor" per issue (the pattern to detect).
**Remove:** Full 200-word example writeups.

This is the single highest-leverage change — it's 30% of all input tokens.

---

### Tactic 5 — Never re-read generate_pdf.py at runtime
**Savings: ~12K tokens per PDF generation run | 7% of current input**

The 1,200-line PDF script is read in full before every PDF generation, even though the template
is fixed. What changes run-to-run is only the **content data** (scores, findings, screenshots).

**Fix:** Separate the template (read once, never again) from the content data.
The skill should produce a compact JSON data file (~50-100 lines) containing:
```json
{
  "app": "Duolingo", "version": "v7.x", "date": "2026-05-19",
  "overall_score": 2, "persona": "new-user", "modules": [...],
  "evidence_cards": [...], "issues": [...], "recommendations": [...]
}
```
Then run: `python output-templates/generate_pdf.py --data [app]-data.json`
The script reads the data file (tiny) and applies the fixed template. No template re-read needed.

---

### Tactic 6 — Compress context files to lean summaries
**Savings: ~15K tokens per run (context files from 20K → 5K)**

`expert-frameworks.md` (4.5K tokens) is the full encyclopedia of 10 frameworks. Replace it
with a 30-line lookup table — just the framework name, key question, and what to audit.
Claude fills in the details from training.

Same for `india-consumer.md` (3.2K tokens): compress to a 40-line table of India-specific
deltas from global norms. Remove all explanatory prose.

Both files can still exist in full for human reference — but the skill should load the
**compressed version** (`frameworks/expert-frameworks-ref.md`, `context/india-ref.md`) at runtime.

---

### Tactic 7 — Speed mode: load section headers only, not full files
**Savings: 70% of module content in speed mode**

Current speed mode still loads the full module file. True speed mode should:

1. Each module file gets a `## SPEED MODE` block at the top (30 lines): screens, 3 checks, score.
2. The orchestrator in speed mode loads **only the SPEED MODE block** of each module using
   a targeted file read (lines 1-35), not the full file.
3. Rigor mode loads the full file as today.

This requires adding a clear `<!-- END SPEED MODE -->` marker to each module file.

---

## Projected Savings

| Scenario | Current Cost | Optimised Cost | Savings |
|----------|-------------|---------------|---------|
| Full review, rigor (10 modules) | $0.77 | $0.46 | **40%** |
| Single module, rigor | $0.24 | $0.11 | **53%** |
| Single module, speed | ~$0.12 | ~$0.03 | **75%** |

*At 2 full reviews/week: saves ~$33/year. At 10/week: saves ~$163/year.*
*The bigger gain is context window headroom — leaner prompts = more room for screenshots.*

---

## Implementation Priority

Execute in this order for maximum impact with minimum refactoring:

| Priority | Tactic | Effort | Input Token Savings |
|----------|--------|--------|---------------------|
| **P0** | Remove example issue writeups from module files | Medium | ~55K / full run |
| **P0** | Never re-read PDF template at runtime (data file pattern) | Low | ~12K / run |
| **P1** | Compress context files to lean references | Low | ~15K / run |
| **P1** | Domain overlays → use domain file, don't embed in modules | Medium | ~15K / run |
| **P2** | Persona instructions → separate persona file | Medium | ~16K / run |
| **P2** | Speed mode header blocks in each module file | Medium | 70% of module tokens in speed runs |
| **P3** | Full module file rewrite to lean format | High | entire Tactic 1-4 savings |

**Recommended starting point:** P0 items only — they require no refactoring of the run protocol,
just editing the module files and changing how the PDF generation works.

---

## Quality Preservation Guarantee

None of these changes reduce output quality because:

1. **Framework knowledge is in Claude's weights**, not in the files. Removing the re-explanations
   doesn't remove the knowledge — it removes redundancy.

2. **Example issues train bad habits** — Claude tends to pattern-match on examples and produce
   outputs that echo the examples' structure/wording rather than the actual findings. Removing
   them produces *better* analysis, not worse.

3. **Output tokens are unchanged** — All analysis depth, framework citations, and PDF structure
   stay the same. Only the input scaffolding is reduced.

4. **Screenshots remain** — The real evidence quality comes from live screenshots, not from
   checklist text. Screenshots are irreducible and that's correct.

---

## Execution Habit: Token-Aware Running

Every run should follow this discipline:

```
Before running:
  □ Am I running rigor or speed mode?
  □ Which single module (or 'full')?
  □ Load ONLY: orchestrator + app context + relevant domain + active persona
  □ Do NOT load all modules upfront for a single-module run

During run:
  □ Load each module file only when executing that module
  □ Generate screenshots to workspace mount IMMEDIATELY after capture
  □ Write findings to disk incrementally (not in one giant output)

After run:
  □ Run log_run.py to record token usage and cost
  □ Generate PDF from data file (not by re-reading template)
```

---

*See `output-templates/log_run.py` for the token accounting system.*
*Token log: `run-log.csv` in this folder.*
