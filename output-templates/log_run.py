"""
pAI Teardown — Run Token Logger
================================
Records token usage, cost, and run metadata for every teardown run.

Usage (called by Claude at the end of each run):
  python log_run.py \\
      --app "Duolingo" \\
      --persona "new-user" \\
      --flow "onboarding" \\
      --mode "rigor" \\
      --input-tokens 46000 \\
      --output-tokens 4200 \\
      --pdf "duolingo-onboarding-teardown.pdf" \\
      [--model "claude-sonnet-4-6"] \\
      [--notes "First run"]

How to estimate tokens (Claude's job before calling this script):
  Input tokens  ≈ sum of all file characters read during the run ÷ 4
                  (use: wc -c file.txt → divide by 4)
                  + screenshot count × 1500 (mobile screenshots via vision)
                  + conversation history ÷ 4
  Output tokens ≈ total characters in all outputs generated ÷ 4

The script appends one row to run-log.csv and prints a formatted cost report.

Pricing defaults (override with --input-cpm and --output-cpm):
  claude-sonnet-4-6: $3.00/MTok input  · $15.00/MTok output
  claude-opus-4-5:   $15.00/MTok input · $75.00/MTok output
  claude-haiku-4-5:  $0.80/MTok input  · $4.00/MTok output
"""

import argparse
import csv
import os
import sys
from datetime import date, datetime

# ── Pricing table ($ per million tokens) ─────────────────────────────────────
PRICING = {
    "claude-sonnet-4-6":      (3.00,  15.00),
    "claude-sonnet-4-5":      (3.00,  15.00),
    "claude-sonnet-4-5-20250929": (3.00, 15.00),
    "claude-opus-4-5":        (15.00, 75.00),
    "claude-opus-4-5-20251101": (15.00, 75.00),
    "claude-haiku-4-5":       (0.80,   4.00),
    "claude-haiku-4-5-20251001": (0.80,  4.00),
}
DEFAULT_MODEL = "claude-sonnet-4-6"

# ── File paths ────────────────────────────────────────────────────────────────
_SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.dirname(_SCRIPT_DIR)
LOG_FILE     = os.path.join(_PROJECT_DIR, "run-log.csv")

FIELDNAMES = [
    "run_number", "date", "app", "persona", "flow", "mode",
    "model", "input_tokens", "output_tokens", "total_tokens",
    "cost_usd", "pdf_file", "notes",
]


# ── Helpers ──────────────────────────────────────────────────────────────────

def _next_run_number(log_path: str) -> int:
    """Return the next sequential run number."""
    if not os.path.exists(log_path):
        return 1
    with open(log_path, newline="") as f:
        rows = [r for r in csv.DictReader(f) if r.get("run_number", "").strip()]
    if not rows:
        return 1
    return max(int(r["run_number"]) for r in rows) + 1


def _compute_cost(input_tokens: int, output_tokens: int,
                  input_cpm: float, output_cpm: float) -> float:
    return (input_tokens * input_cpm + output_tokens * output_cpm) / 1_000_000


def _bar(value: float, max_value: float, width: int = 30, char: str = "█") -> str:
    filled = int(round(value / max_value * width)) if max_value > 0 else 0
    return char * filled + "░" * (width - filled)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Log a pAI teardown run.")
    parser.add_argument("--app",            required=True, help="App name (e.g. Duolingo)")
    parser.add_argument("--persona",        required=True, help="Persona (e.g. new-user)")
    parser.add_argument("--flow",           required=True,
                        help="Flow reviewed (e.g. onboarding, monetization, full)")
    parser.add_argument("--mode",           default="rigor",
                        choices=["speed", "rigor", "hybrid"],
                        help="Review mode")
    parser.add_argument("--input-tokens",   required=True, type=int,
                        help="Estimated input token count")
    parser.add_argument("--output-tokens",  required=True, type=int,
                        help="Estimated output token count")
    parser.add_argument("--model",          default=DEFAULT_MODEL,
                        help="Model used (default: claude-sonnet-4-6)")
    parser.add_argument("--pdf",            default="",
                        help="PDF filename generated (optional)")
    parser.add_argument("--notes",          default="",
                        help="Optional notes for this run")
    parser.add_argument("--input-cpm",      type=float, default=None,
                        help="Override input price ($ per million tokens)")
    parser.add_argument("--output-cpm",     type=float, default=None,
                        help="Override output price ($ per million tokens)")

    args = parser.parse_args()

    # Resolve pricing
    model_key = args.model.lower()
    if model_key in PRICING:
        default_in, default_out = PRICING[model_key]
    else:
        # Unknown model — fall back to Sonnet pricing with a warning
        default_in, default_out = PRICING[DEFAULT_MODEL]
        print(f"  ⚠  Unknown model '{args.model}'. Using Sonnet pricing as fallback.")

    input_cpm  = args.input_cpm  if args.input_cpm  is not None else default_in
    output_cpm = args.output_cpm if args.output_cpm is not None else default_out

    total_tokens = args.input_tokens + args.output_tokens
    cost_usd     = _compute_cost(args.input_tokens, args.output_tokens, input_cpm, output_cpm)
    run_number   = _next_run_number(LOG_FILE)
    today        = date.today().isoformat()

    # ── Write to CSV ──────────────────────────────────────────────────────────
    file_exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "run_number":    run_number,
            "date":          today,
            "app":           args.app,
            "persona":       args.persona,
            "flow":          args.flow,
            "mode":          args.mode,
            "model":         args.model,
            "input_tokens":  args.input_tokens,
            "output_tokens": args.output_tokens,
            "total_tokens":  total_tokens,
            "cost_usd":      f"{cost_usd:.4f}",
            "pdf_file":      args.pdf,
            "notes":         args.notes,
        })

    # ── Print cost report ────────────────────────────────────────────────────
    bar_width = 28
    max_tok   = max(args.input_tokens, args.output_tokens, 1)

    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║           pAI TEARDOWN — RUN COST REPORT             ║")
    print("╠══════════════════════════════════════════════════════╣")
    print(f"║  Run #{run_number:<4}  {today}                              ║")
    print("╠══════════════════════════════════════════════════════╣")
    print(f"║  App      : {args.app:<41}║")
    print(f"║  Persona  : {args.persona:<41}║")
    print(f"║  Flow     : {args.flow:<41}║")
    print(f"║  Mode     : {args.mode:<41}║")
    print(f"║  Model    : {args.model:<41}║")
    print("╠══════════════════════════════════════════════════════╣")
    in_bar  = _bar(args.input_tokens,  max_tok, bar_width)
    out_bar = _bar(args.output_tokens, max_tok, bar_width)
    print(f"║  Input    : {args.input_tokens:>9,} tok  {in_bar} ║")
    print(f"║  Output   : {args.output_tokens:>9,} tok  {out_bar} ║")
    print(f"║  Total    : {total_tokens:>9,} tok                             ║")
    print("╠══════════════════════════════════════════════════════╣")
    in_cost  = args.input_tokens  * input_cpm  / 1_000_000
    out_cost = args.output_tokens * output_cpm / 1_000_000
    print(f"║  Input cost  : ${in_cost:.4f}  ({args.input_tokens:,} × ${input_cpm}/MTok)     ║")
    print(f"║  Output cost : ${out_cost:.4f}  ({args.output_tokens:,} × ${output_cpm}/MTok)    ║")
    print(f"║  ─────────────────────────────────────────────────  ║")
    print(f"║  TOTAL COST  : ${cost_usd:.4f}                              ║")
    print("╠══════════════════════════════════════════════════════╣")
    if args.pdf:
        print(f"║  PDF  : {args.pdf:<45}║")
    if args.notes:
        # word-wrap notes at 45 chars
        words = args.notes.split()
        line, lines = "", []
        for w in words:
            if len(line) + len(w) + 1 > 45:
                lines.append(line)
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            lines.append(line)
        for i, l in enumerate(lines):
            prefix = "Notes" if i == 0 else "     "
            print(f"║  {prefix}: {l:<44}║")
    print("╠══════════════════════════════════════════════════════╣")
    print(f"║  Logged to: run-log.csv (row {run_number})                    ║")
    print("╚══════════════════════════════════════════════════════╝")
    print()

    # ── Running totals ────────────────────────────────────────────────────────
    with open(LOG_FILE, newline="") as f:
        all_rows = [r for r in csv.DictReader(f) if r.get("run_number", "").strip()]

    if len(all_rows) > 1:
        total_cost_all = sum(float(r["cost_usd"]) for r in all_rows)
        total_tok_all  = sum(int(r["total_tokens"]) for r in all_rows)
        print(f"  📊 Cumulative ({len(all_rows)} runs): "
              f"{total_tok_all:,} tokens · ${total_cost_all:.4f} total")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
