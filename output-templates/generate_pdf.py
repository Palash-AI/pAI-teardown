"""
Consulting-Grade pAI Review PDF Generator — Data-Driven Template
================================================================
Built by Palash Somani (https://www.linkedin.com/in/palash-somani-artificial-intelligence/).

This is the canonical PDF template for pAI Review reports. It is fully
data-driven: pass a JSON file with --data and the script renders that
content using the consulting-grade template defined below.

Run:
    python output-templates/generate_pdf.py --data my-review-data.json

The data file's schema is documented at the bottom of this script (see
the argparse epilog for the full example).

Design principles:
- Professional typography: Poppins headings + Lato body (with safe fallbacks)
- Consulting report style, NOT research report
- Para + bullet writing: opening sentence → 2-4 supporting bullets → closing so-what
- Evidence cards: screenshot (left) + analysis (right) in 2-column layout
- Real app screenshots embedded inline (missing files render as clear placeholders)

Visual language:
- Navy (#0F1B2D) + Blue accent (#2563EB) primary palette
- Section headings: Poppins Bold 18pt with blue accent bar underneath
- Body: Lato Regular 9.5pt, justified
- Callout boxes: light blue bg (#DBEAFE) with 3pt blue left border
- Severity tags: red (critical), amber (high), blue (medium), green (good)
- Alternating table row backgrounds (white + #F8FAFC)
- Headers: blue accent line + app name + CONFIDENTIAL
- Footers: author attribution + page number + thin blue bar
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor, white, Color
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Image,
    Table, TableStyle, PageBreak, Flowable, NextPageTemplate
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import sys
import json
import argparse

# ============================================================
# CONFIGURATION — all paths resolved relative to THIS file
# ============================================================

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_DIR = os.path.dirname(_SCRIPT_DIR)   # one level up from output-templates/

# Default screenshot dir / output path; overridable by data JSON or env var.
SCREENSHOT_DIR = os.environ.get(
    "SCREENSHOT_DIR",
    os.path.join(_PROJECT_DIR, "screenshots", "img")
)
OUTPUT_PATH = os.environ.get(
    "PDF_OUTPUT_PATH",
    os.path.join(_PROJECT_DIR, "teardown-output.pdf")
)


# ============================================================
# FONT REGISTRATION (with safe fallbacks)
# ============================================================
#
# Tries to register Poppins + Lato from common system paths and from an
# optional PAI_FONT_DIR env var. If a font isn't found, it falls back to
# the matching ReportLab built-in (Helvetica), so the PDF still renders.

_FONT_SEARCH_PATHS = [
    os.environ.get("PAI_FONT_DIR", ""),
    "/usr/share/fonts/truetype/google-fonts",
    "/usr/share/fonts/truetype/lato",
    "/usr/share/fonts/truetype/poppins",
    "/usr/share/fonts/google-fonts",
    "/usr/local/share/fonts",
    os.path.expanduser("~/.fonts"),
    os.path.expanduser("~/Library/Fonts"),
    "/Library/Fonts",
    "C:\\Windows\\Fonts",
]


def _find_font(filenames):
    """Return the first existing path matching any candidate filename."""
    for folder in _FONT_SEARCH_PATHS:
        if not folder or not os.path.isdir(folder):
            continue
        for fn in filenames:
            full = os.path.join(folder, fn)
            if os.path.isfile(full):
                return full
    return None


_REGISTRATIONS = [
    # (logical font name, [candidate filenames], built-in fallback)
    ("Poppins",          ["Poppins-Regular.ttf"],  "Helvetica"),
    ("Poppins-Medium",   ["Poppins-Medium.ttf"],   "Helvetica-Bold"),
    ("Poppins-Bold",     ["Poppins-Bold.ttf"],     "Helvetica-Bold"),
    ("Poppins-Light",    ["Poppins-Light.ttf", "Poppins-Regular.ttf"], "Helvetica"),
    ("Poppins-Italic",   ["Poppins-Italic.ttf"],   "Helvetica-Oblique"),
    ("Lato",             ["Lato-Regular.ttf"],     "Helvetica"),
    ("Lato-Bold",        ["Lato-Bold.ttf"],        "Helvetica-Bold"),
    ("Lato-Italic",      ["Lato-Italic.ttf"],      "Helvetica-Oblique"),
    ("Lato-Light",       ["Lato-Light.ttf", "Lato-Regular.ttf"], "Helvetica"),
    ("Lato-Semibold",    ["Lato-Semibold.ttf", "Lato-Bold.ttf"], "Helvetica-Bold"),
]

# Map logical font name → actual registered name (either the .ttf or the fallback)
FONT = {}
_missing = []
for logical, candidates, fallback in _REGISTRATIONS:
    path = _find_font(candidates)
    if path:
        try:
            pdfmetrics.registerFont(TTFont(logical, path))
            FONT[logical] = logical
            continue
        except Exception:
            pass
    FONT[logical] = fallback
    _missing.append(logical)

if _missing:
    print("⚠️  Some fonts could not be loaded; using Helvetica fallbacks for: "
          + ", ".join(_missing))
    print("   To get the full design, install Poppins + Lato (free from Google Fonts).")
    print("   See README → Installation → Path 2.\n")

# Register family aliases so <b>/<i> work inside Paragraph markup
try:
    pdfmetrics.registerFontFamily(
        FONT["Poppins"],
        normal=FONT["Poppins"],
        bold=FONT["Poppins-Bold"],
        italic=FONT["Poppins-Italic"],
    )
    pdfmetrics.registerFontFamily(
        FONT["Lato"],
        normal=FONT["Lato"],
        bold=FONT["Lato-Bold"],
        italic=FONT["Lato-Italic"],
    )
except Exception:
    pass


# ============================================================
# PAGE GEOMETRY
# ============================================================

PAGE_W, PAGE_H = A4
MARGIN_LEFT = 22 * mm
MARGIN_RIGHT = 22 * mm
MARGIN_TOP = 22 * mm
MARGIN_BOTTOM = 22 * mm
USABLE_W = PAGE_W - MARGIN_LEFT - MARGIN_RIGHT


# ============================================================
# COLOR PALETTE
# ============================================================

NAVY = HexColor("#0F1B2D")
CHARCOAL = HexColor("#1E293B")
SLATE = HexColor("#334155")
STEEL = HexColor("#64748B")
SILVER = HexColor("#94A3B8")
ACCENT = HexColor("#2563EB")
ACCENT_LIGHT = HexColor("#DBEAFE")
ACCENT_DARK = HexColor("#1E40AF")
CRITICAL = HexColor("#DC2626")
WARNING = HexColor("#D97706")
GOOD = HexColor("#059669")
BG_LIGHT = HexColor("#F8FAFC")
BG_CARD = HexColor("#F1F5F9")
BG_TABLE_ALT = HexColor("#F8FAFC")
BORDER = HexColor("#E2E8F0")
WHITE_BG = white


# ============================================================
# CUSTOM FLOWABLES
# ============================================================

class AccentBar(Flowable):
    def __init__(self, width, height=3, color=ACCENT):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.width, self.height, fill=1, stroke=0)

    def wrap(self, availWidth, availHeight):
        return (self.width, self.height + 2)


class ThinDivider(Flowable):
    def __init__(self, width, color=BORDER):
        Flowable.__init__(self)
        self.width = width
        self.color = color

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(0.5)
        self.canv.line(0, 0, self.width, 0)

    def wrap(self, availWidth, availHeight):
        return (self.width, 4)


class ScoreIndicator(Flowable):
    """Visual score circle with color coding."""
    def __init__(self, score, max_score=10, size=70):
        Flowable.__init__(self)
        try:
            self.score = float(score)
        except (TypeError, ValueError):
            self.score = 0
        self.max_score = max_score
        self.size = size

    def _color(self):
        r = self.score / self.max_score
        if r <= 0.3:
            return CRITICAL
        if r <= 0.6:
            return WARNING
        return GOOD

    def draw(self):
        c = self.canv
        cx = cy = self.size / 2
        r = self.size / 2 - 2
        col = self._color()
        c.setStrokeColor(col); c.setLineWidth(3.5); c.setFillColor(white)
        c.circle(cx, cy, r, fill=1, stroke=1)
        c.setStrokeColor(Color(col.red, col.green, col.blue, 0.15)); c.setLineWidth(1)
        c.circle(cx, cy, r - 6, fill=0, stroke=1)
        c.setFillColor(col); c.setFont(FONT["Poppins-Bold"], 28)
        score_text = str(int(self.score)) if self.score == int(self.score) else f"{self.score:.1f}"
        c.drawCentredString(cx, cy - 10, score_text)

    def wrap(self, availWidth, availHeight):
        return (self.size, self.size)


class MissingScreenshotBox(Flowable):
    """Placeholder when a referenced screenshot file isn't on disk."""
    def __init__(self, width=1.45 * inch, height=3.0 * inch, filename="", num=0):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.filename = filename
        self.num = num

    def draw(self):
        c = self.canv
        c.setStrokeColor(CRITICAL); c.setFillColor(HexColor("#FEF2F2"))
        c.setLineWidth(0.8); c.setDash([4, 3])
        c.rect(0, 0, self.width, self.height, fill=1, stroke=1)
        c.setDash([])
        # Icon
        cx, cy = self.width / 2, self.height / 2 + 12
        c.setStrokeColor(CRITICAL); c.setFillColor(CRITICAL)
        c.roundRect(cx - 14, cy - 10, 28, 22, 4, fill=0, stroke=1)
        c.circle(cx, cy - 1, 6, fill=0, stroke=1)
        # Label
        c.setFillColor(CRITICAL); c.setFont(FONT["Lato-Bold"], 6.5)
        c.drawCentredString(self.width / 2, self.height / 2 - 8, "SCREENSHOT MISSING")
        # Filename (wrap if long)
        c.setFont(FONT["Lato"], 5.5); c.setFillColor(STEEL)
        name = self.filename or "(unknown)"
        max_chars = 22
        if len(name) > max_chars:
            mid = len(name) // 2
            c.drawCentredString(self.width / 2, self.height / 2 - 20, name[:mid])
            c.drawCentredString(self.width / 2, self.height / 2 - 29, name[mid:])
        else:
            c.drawCentredString(self.width / 2, self.height / 2 - 20, name)
        # Instruction
        c.setFont(FONT["Lato-Italic"], 5.5); c.setFillColor(SILVER)
        c.drawCentredString(self.width / 2, 14, "Add to screenshots/img/")

    def wrap(self, availWidth, availHeight):
        return (self.width, self.height)


# ============================================================
# PARAGRAPH STYLES
# ============================================================

styles = getSampleStyleSheet()

cover_title = ParagraphStyle('CoverTitle', fontName=FONT['Poppins-Bold'], fontSize=36, leading=42, textColor=NAVY, alignment=TA_LEFT)
cover_subtitle = ParagraphStyle('CoverSubtitle', fontName=FONT['Poppins-Light'], fontSize=20, leading=26, textColor=CHARCOAL, alignment=TA_LEFT)
cover_meta_label = ParagraphStyle('CoverMetaLabel', fontName=FONT['Lato'], fontSize=9, leading=13, textColor=STEEL, alignment=TA_LEFT)
cover_meta_value = ParagraphStyle('CoverMetaValue', fontName=FONT['Lato-Semibold'], fontSize=10, leading=14, textColor=CHARCOAL, alignment=TA_LEFT)

h1 = ParagraphStyle('H1', fontName=FONT['Poppins-Bold'], fontSize=18, leading=24, textColor=NAVY, alignment=TA_LEFT)
h2 = ParagraphStyle('H2', fontName=FONT['Poppins-Medium'], fontSize=13, leading=18, textColor=CHARCOAL, spaceBefore=18, spaceAfter=6, alignment=TA_LEFT)
h3 = ParagraphStyle('H3', fontName=FONT['Poppins-Medium'], fontSize=11, leading=15, textColor=SLATE, spaceBefore=12, spaceAfter=4, alignment=TA_LEFT)

body = ParagraphStyle('Body', fontName=FONT['Lato'], fontSize=9.5, leading=14.5, textColor=SLATE, spaceAfter=8, alignment=TA_JUSTIFY)
body_bold = ParagraphStyle('BodyBold', fontName=FONT['Lato-Bold'], fontSize=9.5, leading=14.5, textColor=CHARCOAL, spaceAfter=8, alignment=TA_JUSTIFY)

evidence = ParagraphStyle('Evidence', fontName=FONT['Lato'], fontSize=9, leading=14, textColor=SLATE, spaceAfter=6, alignment=TA_JUSTIFY)
framework_cite = ParagraphStyle('FrameworkCite', fontName=FONT['Lato-Italic'], fontSize=8.5, leading=12, textColor=ACCENT_DARK, spaceAfter=4, leftIndent=8)

issue_title = ParagraphStyle('IssueTitle', fontName=FONT['Poppins-Medium'], fontSize=10.5, leading=15, textColor=NAVY, spaceAfter=3)
issue_desc = ParagraphStyle('IssueDesc', fontName=FONT['Lato'], fontSize=9, leading=13.5, textColor=SLATE, spaceAfter=10, alignment=TA_JUSTIFY)

rec_num = ParagraphStyle('RecNum', fontName=FONT['Poppins-Bold'], fontSize=10, leading=14, textColor=ACCENT)
rec_title_style = ParagraphStyle('RecTitle', fontName=FONT['Poppins-Medium'], fontSize=10.5, leading=15, textColor=NAVY, spaceAfter=3)
rec_body = ParagraphStyle('RecBody', fontName=FONT['Lato'], fontSize=9, leading=13.5, textColor=SLATE, spaceAfter=12, alignment=TA_JUSTIFY)

caption = ParagraphStyle('Caption', fontName=FONT['Lato-Italic'], fontSize=8, leading=11, textColor=SILVER, alignment=TA_CENTER)
callout = ParagraphStyle('Callout', fontName=FONT['Lato-Italic'], fontSize=9, leading=13, textColor=STEEL, leftIndent=12, rightIndent=12)
finding_label = ParagraphStyle('FindingLabel', fontName=FONT['Lato-Bold'], fontSize=8, leading=11, textColor=ACCENT, spaceAfter=2)


# ============================================================
# RUNTIME GLOBALS (set per build)
# ============================================================

_HEADER_STRIP = ""
_FOOTER_BRAND = "Powered by pAI Review — built by Palash Somani"


# ============================================================
# PAGE TEMPLATES
# ============================================================

def cover_page_template(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(ACCENT)
    canvas.rect(0, 0, PAGE_W, 6, fill=1, stroke=0)
    canvas.rect(0, PAGE_H - 3, PAGE_W, 3, fill=1, stroke=0)
    canvas.restoreState()


def body_page_template(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(ACCENT); canvas.setLineWidth(1.5)
    canvas.line(MARGIN_LEFT, PAGE_H - 16 * mm, PAGE_W - MARGIN_RIGHT, PAGE_H - 16 * mm)
    canvas.setFillColor(STEEL); canvas.setFont(FONT['Lato'], 7.5)
    canvas.drawString(MARGIN_LEFT, PAGE_H - 14.5 * mm, _HEADER_STRIP)
    canvas.drawRightString(PAGE_W - MARGIN_RIGHT, PAGE_H - 14.5 * mm, "CONFIDENTIAL")
    canvas.setStrokeColor(BORDER); canvas.setLineWidth(0.5)
    canvas.line(MARGIN_LEFT, MARGIN_BOTTOM - 6 * mm, PAGE_W - MARGIN_RIGHT, MARGIN_BOTTOM - 6 * mm)
    canvas.setFillColor(STEEL); canvas.setFont(FONT['Lato'], 8)
    canvas.drawRightString(PAGE_W - MARGIN_RIGHT, MARGIN_BOTTOM - 11 * mm, f"{doc.page}")
    canvas.setFont(FONT['Lato-Light'], 7)
    canvas.drawString(MARGIN_LEFT, MARGIN_BOTTOM - 11 * mm, _FOOTER_BRAND)
    canvas.setFillColor(ACCENT)
    canvas.rect(0, 0, PAGE_W, 2.5, fill=1, stroke=0)
    canvas.restoreState()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def section_heading(text):
    return [Paragraph(text, h1), AccentBar(60, height=2.5, color=ACCENT), Spacer(1, 10)]


def sub_heading(text):
    return [Paragraph(text, h2)]


def thin_divider():
    return [Spacer(1, 8), ThinDivider(USABLE_W), Spacer(1, 8)]


def _resolve_screenshot(path_or_name):
    """Resolve a screenshot reference to an absolute path.

    Rules:
    - If `path_or_name` is absolute → use as-is.
    - Otherwise → look up in SCREENSHOT_DIR.
    """
    if not path_or_name:
        return None
    if os.path.isabs(path_or_name):
        return path_or_name
    return os.path.join(SCREENSHOT_DIR, path_or_name)


def _audit_screenshots(card_specs):
    """Print which referenced screenshots exist and which don't."""
    if not card_specs:
        return
    print(f"\n📸  Auditing {len(card_specs)} screenshot reference(s)...")
    missing = 0
    for c in card_specs:
        name = c.get("screenshot", "")
        full = _resolve_screenshot(name)
        if full and os.path.isfile(full):
            size_kb = os.path.getsize(full) / 1024
            print(f"   ✅ {name}  ({size_kb:.0f} KB)")
        else:
            print(f"   ⚠️  MISSING: {name}")
            missing += 1
    if missing:
        print(f"\n   {missing} screenshot(s) missing — placeholder boxes will render in their place.\n")
    else:
        print(f"   All screenshots present.\n")


def evidence_card(screenshot_path, screenshot_num, screen_name,
                  caption_text, observations, framework_text):
    """Two-column evidence card: image left, analysis right."""
    img_elements = []
    if screenshot_path and os.path.exists(screenshot_path):
        img = Image(screenshot_path, width=1.45 * inch, height=3.0 * inch)
        img.hAlign = 'CENTER'
        img_elements.append(img)
        img_elements.append(Spacer(1, 4))
        img_elements.append(Paragraph(f"Screenshot #{int(screenshot_num):02d}", caption))
    else:
        missing_name = os.path.basename(screenshot_path) if screenshot_path else "(no file)"
        print(f"   ⚠️  MISSING SCREENSHOT #{int(screenshot_num):02d}: {screenshot_path}")
        img_elements.append(MissingScreenshotBox(filename=missing_name, num=screenshot_num))
        img_elements.append(Spacer(1, 4))
        img_elements.append(Paragraph(
            f"<font color='#DC2626'>⚠ Screenshot #{int(screenshot_num):02d} missing</font>",
            caption))

    analysis = [
        Paragraph(f"FINDING {int(screenshot_num)}", finding_label),
        Paragraph(screen_name, issue_title),
        Spacer(1, 2),
        Paragraph(f"<i>{caption_text}</i>", caption) if caption_text else Spacer(1, 0),
        Spacer(1, 4),
    ]
    if isinstance(observations, list):
        for obs in observations:
            analysis.append(Paragraph(obs, evidence))
    elif observations:
        analysis.append(Paragraph(observations, evidence))
    analysis.append(Spacer(1, 6))
    if framework_text:
        analysis.append(Paragraph(f"<i>{framework_text}</i>", framework_cite))

    card_table = Table(
        [[img_elements, analysis]],
        colWidths=[1.75 * inch, USABLE_W - 1.85 * inch],
        style=TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (0, 0), 0),
            ('RIGHTPADDING', (0, 0), (0, 0), 10),
            ('LEFTPADDING', (1, 0), (1, 0), 10),
            ('RIGHTPADDING', (1, 0), (1, 0), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('LINEAFTER', (0, 0), (0, 0), 0.5, BORDER),
        ])
    )
    wrapper = Table(
        [[card_table]],
        colWidths=[USABLE_W],
        style=TableStyle([
            ('BOX', (0, 0), (-1, -1), 0.5, BORDER),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
            ('BACKGROUND', (0, 0), (-1, -1), BG_LIGHT),
        ])
    )
    return [wrapper, Spacer(1, 14)]


def make_issue_row(num, title, severity, description):
    sev_colors = {"CRITICAL": CRITICAL, "HIGH": WARNING, "MEDIUM": ACCENT, "LOW": GOOD}
    sev_color = sev_colors.get(str(severity).upper(), STEEL)
    return [
        Spacer(1, 4),
        Table(
            [[
                Paragraph(f"{num}", ParagraphStyle('IssueNum', fontName=FONT['Poppins-Bold'], fontSize=11, textColor=sev_color, alignment=TA_CENTER)),
                [
                    Paragraph(f"{title}  <font name='{FONT['Lato-Bold']}' size='7.5' color='{sev_color.hexval()}'>[{str(severity).upper()}]</font>", issue_title),
                    Paragraph(description, issue_desc),
                ]
            ]],
            colWidths=[28, USABLE_W - 32],
            style=TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 6),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                ('LEFTPADDING', (0, 0), (0, 0), 0),
                ('RIGHTPADDING', (0, 0), (0, 0), 8),
                ('LEFTPADDING', (1, 0), (1, 0), 0),
                ('LINEBELOW', (0, 0), (-1, -1), 0.3, BORDER),
            ])
        ),
    ]


# ============================================================
# DATA-DRIVEN BUILD
# ============================================================

def _label_for(score):
    try:
        s = float(score)
    except (TypeError, ValueError):
        return ""
    if s <= 2: return "Critical"
    if s <= 4: return "Poor"
    if s <= 6: return "Below Average"
    if s <= 8: return "Good"
    return "Excellent"


def _color_for(score):
    try:
        s = float(score)
    except (TypeError, ValueError):
        return STEEL
    if s <= 3: return CRITICAL
    if s <= 5: return WARNING
    if s <= 7: return ACCENT
    return GOOD


def build_pdf(data):
    """Build the PDF report fully from `data` (dict)."""
    global _HEADER_STRIP, _FOOTER_BRAND, OUTPUT_PATH, SCREENSHOT_DIR

    if data.get("screenshot_dir"):
        SCREENSHOT_DIR = os.path.abspath(data["screenshot_dir"])
    if data.get("output_path"):
        OUTPUT_PATH = os.path.abspath(data["output_path"])

    app = data.get("app", "Unknown App")
    subtitle = data.get("subtitle", "Product Teardown")
    module_label = data.get("module_label", data.get("module", "").title())
    date_str = data.get("date", "")
    version = data.get("version", "")
    persona_label = data.get("persona_label", data.get("persona", ""))
    mode = data.get("mode", "Rigor")
    device = data.get("device", "")
    frameworks = data.get("frameworks", [])
    overall_score = data.get("overall_score", "")
    overall_label = data.get("overall_label") or _label_for(overall_score)
    overall_description = data.get("overall_description", "")
    overall_color = _color_for(overall_score)

    prepared_by = data.get("prepared_by", "Palash Somani")
    prepared_by_role = data.get("prepared_by_role", "Skill author — pAI Review")
    prepared_by_url = data.get("prepared_by_url", "https://www.linkedin.com/in/palash-somani-artificial-intelligence/")
    prepared_for = data.get("prepared_for", "")
    prepared_for_role = data.get("prepared_for_role", "")

    _HEADER_STRIP = data.get("header_strip",
                             f"{app.upper()}  |  {module_label.upper()}  |  {date_str.upper()}")
    _FOOTER_BRAND = data.get("footer_brand",
                             f"Built by {prepared_by} — Powered by pAI Review")

    cards = data.get("evidence_cards", [])
    _audit_screenshots(cards)

    doc = BaseDocTemplate(
        OUTPUT_PATH, pagesize=A4,
        leftMargin=MARGIN_LEFT, rightMargin=MARGIN_RIGHT,
        topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM,
        title=f"{app} {module_label} Teardown",
        author=prepared_by,
        subject=f"pAI Review — {module_label}",
    )
    cover_frame = Frame(30 * mm, MARGIN_BOTTOM, PAGE_W - 60 * mm,
                        PAGE_H - MARGIN_TOP - MARGIN_BOTTOM, id='cover')
    body_frame = Frame(MARGIN_LEFT, MARGIN_BOTTOM, USABLE_W,
                       PAGE_H - MARGIN_TOP - MARGIN_BOTTOM - 6 * mm, id='body')
    doc.addPageTemplates([
        PageTemplate(id='cover', frames=cover_frame, onPage=cover_page_template),
        PageTemplate(id='body', frames=body_frame, onPage=body_page_template),
    ])

    story = []

    # -------------------------------------------------------- COVER
    story.append(Spacer(1, 50))
    story.append(Paragraph("pAI REVIEW", ParagraphStyle(
        'BrandMark', fontName=FONT['Lato'], fontSize=9, leading=12,
        textColor=ACCENT, spaceAfter=24)))
    story.append(Paragraph(app, cover_title))
    story.append(Paragraph(subtitle, cover_subtitle))
    story.append(Spacer(1, 8))
    story.append(AccentBar(50, height=3))
    story.append(Spacer(1, 28))

    # Score block
    score_label = ParagraphStyle('SL', fontName=FONT['Lato'], fontSize=8, leading=10, textColor=STEEL, spaceAfter=4)
    score_val = ParagraphStyle('SV', fontName=FONT['Poppins-Bold'], fontSize=18, leading=22, textColor=overall_color, spaceAfter=6)
    score_stat = ParagraphStyle('SS', fontName=FONT['Lato-Italic'], fontSize=9, leading=12, textColor=overall_color)
    score_table = Table(
        [[
            ScoreIndicator(overall_score, 10, size=72),
            [
                Paragraph("OVERALL SCORE", score_label),
                Paragraph(f"{overall_score} out of 10", score_val),
                Paragraph(f"{overall_label} — {overall_description}" if overall_description
                          else overall_label, score_stat),
            ]
        ]],
        colWidths=[90, USABLE_W - 120],
        style=TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (1, 0), (1, 0), 16),
        ])
    )
    story.append(score_table)
    story.append(Spacer(1, 36))

    # Meta
    meta_items = [
        ("APP VERSION", version),
        ("PERSONA", persona_label),
        ("MODULE", module_label),
        ("MODE", mode),
        ("DATE", date_str),
        ("DEVICE", device),
    ]
    meta_rows = [[Paragraph(label, cover_meta_label),
                  Paragraph(val or "—", cover_meta_value)]
                 for label, val in meta_items]
    meta_table = Table(meta_rows, colWidths=[USABLE_W * 0.3, USABLE_W * 0.7])
    meta_table.setStyle(TableStyle([
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('LINEBELOW', (0, 0), (-1, -2), 0.3, BORDER),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 30))

    if frameworks:
        story.append(Paragraph("FRAMEWORKS APPLIED", ParagraphStyle(
            'FL', fontName=FONT['Lato'], fontSize=8, textColor=STEEL, spaceAfter=6)))
        story.append(Paragraph(
            "  ·  ".join(frameworks),
            ParagraphStyle('FList', fontName=FONT['Lato-Light'], fontSize=9, leading=13, textColor=CHARCOAL)))
        story.append(Spacer(1, 24))

    # Built-by block
    story.append(ThinDivider(USABLE_W * 0.4))
    story.append(Spacer(1, 10))
    if prepared_for:
        story.append(Paragraph("Prepared for", ParagraphStyle(
            'PL', fontName=FONT['Lato'], fontSize=8, textColor=SILVER, spaceAfter=2)))
        story.append(Paragraph(prepared_for, ParagraphStyle(
            'PN', fontName=FONT['Poppins-Medium'], fontSize=12, textColor=NAVY, spaceAfter=2)))
        if prepared_for_role:
            story.append(Paragraph(prepared_for_role, ParagraphStyle(
                'PR', fontName=FONT['Lato'], fontSize=9, textColor=STEEL, spaceAfter=10)))
    story.append(Paragraph("Built by", ParagraphStyle(
        'BBy', fontName=FONT['Lato'], fontSize=8, textColor=SILVER, spaceAfter=2)))
    if prepared_by_url:
        story.append(Paragraph(
            f"<link href='{prepared_by_url}' color='#0F1B2D'>{prepared_by}</link>",
            ParagraphStyle('BByName', fontName=FONT['Poppins-Medium'], fontSize=12, textColor=NAVY, spaceAfter=2)))
    else:
        story.append(Paragraph(prepared_by, ParagraphStyle(
            'BByName', fontName=FONT['Poppins-Medium'], fontSize=12, textColor=NAVY, spaceAfter=2)))
    story.append(Paragraph(prepared_by_role, ParagraphStyle(
        'BByRole', fontName=FONT['Lato'], fontSize=9, textColor=STEEL)))

    story.append(NextPageTemplate('body'))
    story.append(PageBreak())

    # -------------------------------------------------------- EXEC SUMMARY
    exec_summary = data.get("executive_summary", {})
    if exec_summary:
        story.extend(section_heading("Executive Summary"))
        for para in exec_summary.get("paragraphs", []):
            story.append(Paragraph(para, body))
        co = exec_summary.get("callout")
        if co:
            callout_table = Table(
                [[[
                    Paragraph(co.get("label", "CALLOUT"), ParagraphStyle(
                        'CalloutLabel', fontName=FONT['Lato-Bold'], fontSize=7.5,
                        textColor=ACCENT, spaceAfter=4)),
                    Paragraph(co.get("text", ""), ParagraphStyle(
                        'CalloutText', fontName=FONT['Lato-Semibold'], fontSize=9.5,
                        leading=14, textColor=CHARCOAL)),
                ]]],
                colWidths=[USABLE_W],
                style=TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), ACCENT_LIGHT),
                    ('TOPPADDING', (0, 0), (-1, -1), 12),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
                    ('LEFTPADDING', (0, 0), (-1, -1), 16),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 16),
                    ('LINEBEFORE', (0, 0), (0, -1), 3, ACCENT),
                ])
            )
            story.append(Spacer(1, 8))
            story.append(callout_table)
            story.append(Spacer(1, 16))

    # -------------------------------------------------------- SCORECARD
    scorecard = data.get("scorecard", [])
    if scorecard:
        story.extend(sub_heading("Scorecard"))
        sc_data = [[
            Paragraph("Dimension", ParagraphStyle('THText', fontName=FONT['Lato-Bold'], fontSize=8.5, textColor=white)),
            Paragraph("Score", ParagraphStyle('THText', fontName=FONT['Lato-Bold'], fontSize=8.5, textColor=white, alignment=TA_CENTER)),
            Paragraph("Status", ParagraphStyle('THText', fontName=FONT['Lato-Bold'], fontSize=8.5, textColor=white, alignment=TA_CENTER)),
        ]]
        for row in scorecard:
            sc = row.get("score", "")
            sc_color = _color_for(sc)
            sc_data.append([
                Paragraph(row.get("dimension", ""), ParagraphStyle('TD1', fontName=FONT['Lato'], fontSize=9, textColor=CHARCOAL)),
                Paragraph(f"{sc} / 10", ParagraphStyle('TD2', fontName=FONT['Lato-Bold'], fontSize=9, textColor=sc_color, alignment=TA_CENTER)),
                Paragraph(row.get("status", "").upper(), ParagraphStyle('TD3', fontName=FONT['Lato-Bold'], fontSize=8, textColor=white, alignment=TA_CENTER)),
            ])
        sc_table = Table(sc_data, colWidths=[USABLE_W * 0.55, USABLE_W * 0.2, USABLE_W * 0.25])
        ts = [
            ('BACKGROUND', (0, 0), (-1, 0), NAVY),
            ('TOPPADDING', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]
        for i, row in enumerate(scorecard, start=1):
            ts.append(('BACKGROUND', (2, i), (2, i), _color_for(row.get("score", ""))))
        sc_table.setStyle(TableStyle(ts))
        story.append(sc_table)
        story.append(Spacer(1, 16))

    note = data.get("note_after_scorecard")
    if note:
        story.append(Paragraph(note, callout))
        story.append(Spacer(1, 8))

    story.append(PageBreak())

    # -------------------------------------------------------- EVIDENCE
    if cards:
        story.extend(section_heading("Evidence & Analysis"))
        story.append(Paragraph(
            "Each finding below is grounded in established product and design frameworks, "
            "with reference screenshots captured during the audit.", body))
        story.append(Spacer(1, 10))
        per_page = 0
        for c in cards:
            story.extend(evidence_card(
                _resolve_screenshot(c.get("screenshot", "")),
                c.get("num", 0),
                c.get("title", ""),
                c.get("caption", ""),
                c.get("observations", []),
                c.get("framework", ""),
            ))
            per_page += 1
            if per_page >= 2:
                story.append(PageBreak())
                per_page = 0
        if per_page > 0:
            story.append(PageBreak())

    # -------------------------------------------------------- KEY ISSUES
    issues = data.get("key_issues", [])
    if issues:
        story.extend(section_heading("Key Issues"))
        story.append(Paragraph(
            "Issues ranked by severity and impact on the persona's experience.", body))
        story.append(Spacer(1, 6))
        for i, iss in enumerate(issues, start=1):
            story.extend(make_issue_row(
                iss.get("num", i),
                iss.get("title", ""),
                iss.get("severity", "MEDIUM"),
                iss.get("description", ""),
            ))
        story.append(PageBreak())

    # -------------------------------------------------------- RECOMMENDATIONS
    rec_table_rows = data.get("recommendations_table", [])
    rec_details = data.get("recommendations_detail", [])
    if rec_table_rows or rec_details:
        story.extend(section_heading("Recommendations"))

        if rec_table_rows:
            header = [
                Paragraph("#", ParagraphStyle('TH', fontName=FONT['Lato-Bold'], fontSize=8, textColor=white, alignment=TA_CENTER)),
                Paragraph("Recommendation", ParagraphStyle('TH', fontName=FONT['Lato-Bold'], fontSize=8, textColor=white)),
                Paragraph("Effort", ParagraphStyle('TH', fontName=FONT['Lato-Bold'], fontSize=8, textColor=white, alignment=TA_CENTER)),
                Paragraph("Impact", ParagraphStyle('TH', fontName=FONT['Lato-Bold'], fontSize=8, textColor=white, alignment=TA_CENTER)),
                Paragraph("Timeline", ParagraphStyle('TH', fontName=FONT['Lato-Bold'], fontSize=8, textColor=white, alignment=TA_CENTER)),
            ]
            td = lambda t, bold=False: Paragraph(t, ParagraphStyle('TD', fontName=FONT['Lato-Bold'] if bold else FONT['Lato'], fontSize=8.5, leading=12, textColor=CHARCOAL))
            td_c = lambda t, color=CHARCOAL: Paragraph(t, ParagraphStyle('TDC', fontName=FONT['Lato'], fontSize=8.5, leading=12, textColor=color, alignment=TA_CENTER))
            rows = [header]
            for r in rec_table_rows:
                impact = r.get("impact", "")
                imp_color = CRITICAL if impact.lower().startswith("very") else (WARNING if impact.lower() == "high" else ACCENT)
                rows.append([
                    td_c(str(r.get("num", ""))),
                    td(r.get("title", ""), bold=True),
                    td_c(r.get("effort", "")),
                    td_c(impact, imp_color),
                    td_c(r.get("timeline", "")),
                ])
            rt = Table(rows, colWidths=[USABLE_W * 0.06, USABLE_W * 0.40, USABLE_W * 0.16, USABLE_W * 0.18, USABLE_W * 0.20])
            rt.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), NAVY),
                ('TOPPADDING', (0, 0), (-1, -1), 8),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('LEFTPADDING', (0, 0), (-1, -1), 8),
                ('RIGHTPADDING', (0, 0), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 0.5, BORDER),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE_BG, BG_TABLE_ALT]),
            ]))
            story.append(rt)
            story.append(Spacer(1, 20))

        if rec_details:
            story.extend(sub_heading("Detail"))
            for i, r in enumerate(rec_details, start=1):
                story.append(Paragraph(f"{i:02d}", rec_num))
                story.append(Paragraph(r.get("title", ""), rec_title_style))
                story.append(Paragraph(r.get("description", ""), rec_body))
                if i < len(rec_details):
                    story.extend(thin_divider())
        story.append(PageBreak())

    # -------------------------------------------------------- SCORING RATIONALE
    sr = data.get("scoring_rationale", {})
    if sr:
        story.extend(section_heading("Scoring Rationale"))
        story.append(Table(
            [[
                ScoreIndicator(overall_score, 10, size=56),
                Paragraph(
                    f"<b>{overall_score} / 10 — {overall_label}</b><br/>"
                    f"{sr.get('summary', '')}",
                    ParagraphStyle('SE', fontName=FONT['Lato'], fontSize=9.5, leading=14.5, textColor=CHARCOAL)
                )
            ]],
            colWidths=[72, USABLE_W - 80],
            style=TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('LEFTPADDING', (1, 0), (1, 0), 12),
            ])
        ))
        story.append(Spacer(1, 14))

        if sr.get("intro"):
            story.append(Paragraph(sr["intro"], body))

        violations = sr.get("framework_table", [])
        if violations:
            vh = [[
                Paragraph("Framework", ParagraphStyle('VTH', fontName=FONT['Lato-Bold'], fontSize=8, textColor=white)),
                Paragraph("Assessment", ParagraphStyle('VTH', fontName=FONT['Lato-Bold'], fontSize=8, textColor=white)),
            ]]
            for v in violations:
                vh.append([
                    Paragraph(v.get("framework", ""), ParagraphStyle('VTD1', fontName=FONT['Lato-Semibold'], fontSize=8.5, textColor=CHARCOAL)),
                    Paragraph(v.get("assessment", ""), ParagraphStyle('VTD2', fontName=FONT['Lato'], fontSize=8.5, textColor=SLATE)),
                ])
            v_table = Table(vh, colWidths=[USABLE_W * 0.32, USABLE_W * 0.68])
            v_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), CHARCOAL),
                ('TOPPADDING', (0, 0), (-1, -1), 7),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
                ('LEFTPADDING', (0, 0), (-1, -1), 8),
                ('RIGHTPADDING', (0, 0), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 0.3, BORDER),
                ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE_BG, BG_TABLE_ALT]),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ]))
            story.append(v_table)
            story.append(Spacer(1, 16))

        if sr.get("closing"):
            story.append(Paragraph(sr["closing"], body))

    closing_note = data.get("closing_note")
    if closing_note:
        story.append(Spacer(1, 20))
        note_table = Table(
            [[Paragraph(closing_note, callout)]],
            colWidths=[USABLE_W],
            style=TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), BG_CARD),
                ('TOPPADDING', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
                ('LEFTPADDING', (0, 0), (-1, -1), 12),
                ('RIGHTPADDING', (0, 0), (-1, -1), 12),
                ('BOX', (0, 0), (-1, -1), 0.3, BORDER),
            ])
        )
        story.append(note_table)

    story.append(Spacer(1, 30))
    story.extend(thin_divider())
    story.append(Spacer(1, 8))
    story.append(Paragraph("Built by", ParagraphStyle(
        'CB', fontName=FONT['Lato'], fontSize=8, textColor=SILVER, spaceAfter=2)))
    if prepared_by_url:
        story.append(Paragraph(
            f"<link href='{prepared_by_url}' color='#0F1B2D'>{prepared_by}</link>",
            ParagraphStyle('CN', fontName=FONT['Poppins-Medium'], fontSize=11, textColor=NAVY, spaceAfter=2)))
    else:
        story.append(Paragraph(prepared_by, ParagraphStyle(
            'CN', fontName=FONT['Poppins-Medium'], fontSize=11, textColor=NAVY, spaceAfter=2)))
    story.append(Paragraph(prepared_by_role, ParagraphStyle(
        'CR', fontName=FONT['Lato'], fontSize=9, textColor=STEEL, spaceAfter=8)))

    doc.build(story)
    file_size = os.path.getsize(OUTPUT_PATH)
    print(f"\n✅  PDF generated: {OUTPUT_PATH}")
    print(f"    Size : {file_size / 1024:.1f} KB\n")


# ============================================================
# CLI
# ============================================================

EXAMPLE_SCHEMA = """\
Expected JSON schema (minimal example):

{
  "app": "Duolingo",
  "subtitle": "Onboarding Experience Review",
  "module": "onboarding",
  "module_label": "Onboarding & First Value Experience",
  "version": "v7.x",
  "persona": "new-user",
  "persona_label": "New User (first open)",
  "mode": "Rigor (45–60 min)",
  "date": "May 19, 2026",
  "device": "iOS 18 / iPhone 15",
  "frameworks": ["Fogg Behavior Model", "Nielsen Heuristics", "Hook Model"],
  "overall_score": 9,
  "overall_label": "Excellent",
  "overall_description": "Best-in-class. Benchmark for others.",

  "prepared_by": "Palash Somani",
  "prepared_by_role": "Skill author — pAI Review",
  "prepared_by_url": "https://www.linkedin.com/in/palash-somani-artificial-intelligence/",
  "prepared_for": "Elevation Capital portfolio",
  "prepared_for_role": "Sample teardown / calibration reference",

  "output_path": "duolingo-onboarding-teardown.pdf",
  "screenshot_dir": "screenshots/duolingo-onboarding/img",

  "header_strip": "DUOLINGO  |  ONBOARDING TEARDOWN  |  MAY 2026",

  "executive_summary": {
    "paragraphs": ["...", "..."],
    "callout": {"label": "BENCHMARK", "text": "..."}
  },

  "scorecard": [
    {"dimension": "Onboarding & First Value Experience",
     "score": 9, "status": "Excellent"}
  ],

  "evidence_cards": [
    {"num": 1, "screenshot": "01-language-pick-new-user.png",
     "title": "Language picker before signup wall",
     "caption": "First screen, no auth required",
     "observations": ["...", "..."],
     "framework": "Fogg MAP: low friction = high Ability …"}
  ],

  "key_issues": [
    {"num": 1, "title": "...", "severity": "MEDIUM",
     "description": "..."}
  ],

  "recommendations_table": [
    {"num": 1, "title": "...", "effort": "1 week",
     "impact": "Medium", "timeline": "Next sprint"}
  ],

  "recommendations_detail": [
    {"num": 1, "title": "...", "description": "..."}
  ],

  "scoring_rationale": {
    "summary": "...",
    "intro": "...",
    "framework_table": [{"framework": "Fogg MAP", "assessment": "..."}],
    "closing": "..."
  },

  "closing_note": "Optional disclaimer."
}
"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="pAI Review PDF Generator (data-driven).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=EXAMPLE_SCHEMA,
    )
    parser.add_argument("--data", required=True,
                        metavar="FILE",
                        help="Path to a JSON data file (see schema below).")
    args = parser.parse_args()

    data_path = os.path.abspath(args.data)
    if not os.path.isfile(data_path):
        print(f"\n❌  Data file not found: {data_path}")
        sys.exit(1)
    with open(data_path, "r", encoding="utf-8") as fh:
        review_data = json.load(fh)

    print(f"\n📄  Loaded review data: {data_path}")
    print(f"    App      : {review_data.get('app', '?')}")
    print(f"    Persona  : {review_data.get('persona', '?')}")
    print(f"    Module   : {review_data.get('module', '?')}")
    print(f"    Score    : {review_data.get('overall_score', '?')}/10")

    # Resolve data-relative paths (output_path, screenshot_dir) against the
    # data file's directory so users can write portable JSON.
    data_dir = os.path.dirname(data_path)
    if review_data.get("output_path") and not os.path.isabs(review_data["output_path"]):
        review_data["output_path"] = os.path.join(data_dir, review_data["output_path"])
    if review_data.get("screenshot_dir") and not os.path.isabs(review_data["screenshot_dir"]):
        review_data["screenshot_dir"] = os.path.join(data_dir, review_data["screenshot_dir"])

    build_pdf(review_data)
