"""
Generate annotated mockup screenshots for the Duolingo onboarding teardown sample.

These are not real Duolingo screen captures — they are annotated recreations that
visually represent each step of Duolingo's onboarding flow as documented in public
sources (Built for Mars, Growth.Design, App Store listings). Each mockup carries a
visible "ANNOTATED RECREATION" banner so a reader cannot mistake it for a real
screen capture. Before final external distribution, swap these for actual screenshots.

Run:  python make_mockups.py
"""
from PIL import Image, ImageDraw, ImageFont
import os
import sys

OUT = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(OUT, "img")
os.makedirs(IMG_DIR, exist_ok=True)

# Phone-portrait size (iPhone-ish proportions)
W, H = 414, 896

# Duolingo-ish colors
DUO_GREEN = (88, 204, 2)
DUO_GREEN_DARK = (70, 163, 0)
DUO_BLUE = (28, 176, 246)
DUO_YELLOW = (255, 200, 0)
DUO_RED = (255, 75, 75)
BG = (255, 255, 255)
TEXT_DARK = (61, 61, 61)
TEXT_MED = (119, 119, 119)
LIGHT_GREY = (229, 229, 229)
BANNER_BG = (220, 38, 38)


def _font(size, bold=False):
    """Best-effort font loader; falls back to default if not found."""
    candidates_bold = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf",
    ]
    candidates_reg = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
    ]
    pool = candidates_bold if bold else candidates_reg
    for p in pool:
        if os.path.isfile(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


def _new_canvas():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # Status bar
    d.rectangle([(0, 0), (W, 30)], fill=(245, 245, 245))
    d.text((20, 8), "9:41", font=_font(13, bold=True), fill=TEXT_DARK)
    d.text((W - 50, 8), "100%", font=_font(11), fill=TEXT_MED)
    # Annotated-recreation banner
    d.rectangle([(0, 30), (W, 56)], fill=BANNER_BG)
    d.text((W // 2 - 100, 36), "ANNOTATED RECREATION", font=_font(11, bold=True), fill=(255, 255, 255))
    return img, d


def _centered(d, y, text, font, fill=TEXT_DARK):
    bbox = d.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    d.text(((W - w) // 2, y), text, font=font, fill=fill)


def _rounded_rect(d, xy, radius, fill, outline=None, width=0):
    """ImageDraw rounded rectangle (Pillow ≥8.2)."""
    try:
        d.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)
    except AttributeError:
        d.rectangle(xy, fill=fill, outline=outline)


def _btn(d, y, label, fill=DUO_GREEN, text_color=(255, 255, 255), width_ratio=0.85, height=56):
    pad = int(W * (1 - width_ratio) / 2)
    _rounded_rect(d, [(pad, y), (W - pad, y + height)], 14, fill=fill)
    bbox = d.textbbox((0, 0), label, font=_font(17, bold=True))
    w = bbox[2] - bbox[0]
    d.text(((W - w) // 2, y + height // 2 - 11), label, font=_font(17, bold=True), fill=text_color)


def _draw_owl(d, cx, cy, size=70, color=DUO_GREEN):
    # Stylized owl: oval body + 2 eyes + beak
    d.ellipse([(cx - size, cy - size), (cx + size, cy + size)], fill=color)
    eye_r = size // 4
    d.ellipse([(cx - size // 2 - eye_r, cy - 10 - eye_r), (cx - size // 2 + eye_r, cy - 10 + eye_r)], fill=(255, 255, 255))
    d.ellipse([(cx + size // 2 - eye_r, cy - 10 - eye_r), (cx + size // 2 + eye_r, cy - 10 + eye_r)], fill=(255, 255, 255))
    d.ellipse([(cx - size // 2 - 6, cy - 16), (cx - size // 2 + 6, cy - 4)], fill=(0, 0, 0))
    d.ellipse([(cx + size // 2 - 6, cy - 16), (cx + size // 2 + 6, cy - 4)], fill=(0, 0, 0))
    # Beak
    d.polygon([(cx - 8, cy + 10), (cx + 8, cy + 10), (cx, cy + 22)], fill=DUO_YELLOW)


def screen_01_landing():
    """Launch screen: Duo mascot + 'Learn a language for free' + Get started."""
    img, d = _new_canvas()
    _draw_owl(d, W // 2, 250, size=80)
    _centered(d, 360, "Learn a language for free.", _font(22, bold=True))
    _centered(d, 392, "Forever.", _font(22, bold=True))
    _btn(d, 540, "GET STARTED", fill=DUO_GREEN)
    _btn(d, 614, "I ALREADY HAVE AN ACCOUNT", fill=(255, 255, 255), text_color=DUO_BLUE)
    # Outline for second button (we used white fill)
    pad = int(W * 0.075)
    _rounded_rect(d, [(pad, 614), (W - pad, 670)], 14, fill=(255, 255, 255), outline=DUO_BLUE, width=2)
    _centered(d, 614 + 20, "I ALREADY HAVE AN ACCOUNT", _font(15, bold=True), fill=DUO_BLUE)
    _centered(d, 820, "Note: no signup wall — value-first", _font(11), fill=TEXT_MED)
    img.save(os.path.join(IMG_DIR, "01-landing-new-user.png"))


def screen_02_language():
    """Language picker: list of languages with flags + checkmarks."""
    img, d = _new_canvas()
    d.text((20, 70), "I want to learn...", font=_font(20, bold=True), fill=TEXT_DARK)
    langs = [
        ("Spanish", "🇪🇸", True),
        ("French", "🇫🇷", False),
        ("Japanese", "🇯🇵", False),
        ("German", "🇩🇪", False),
        ("Italian", "🇮🇹", False),
        ("Korean", "🇰🇷", False),
        ("Chinese", "🇨🇳", False),
        ("Hindi", "🇮🇳", False),
    ]
    y = 120
    for name, flag, selected in langs:
        bg = DUO_GREEN if selected else (250, 250, 250)
        fg = (255, 255, 255) if selected else TEXT_DARK
        _rounded_rect(d, [(20, y), (W - 20, y + 60)], 12, fill=bg, outline=LIGHT_GREY, width=1)
        d.text((40, y + 20), flag, font=_font(20))
        d.text((90, y + 20), name, font=_font(16, bold=True), fill=fg)
        if selected:
            d.text((W - 50, y + 20), "✓", font=_font(20, bold=True), fill=(255, 255, 255))
        y += 70
    _btn(d, 760, "CONTINUE", fill=DUO_GREEN)
    img.save(os.path.join(IMG_DIR, "02-language-pick-new-user.png"))


def screen_03_motivation():
    """Why are you learning Spanish? — multi-choice."""
    img, d = _new_canvas()
    _draw_owl(d, 80, 110, size=40)
    _rounded_rect(d, [(140, 90), (W - 30, 160)], 12, fill=(245, 245, 245))
    d.text((155, 105), "Why are you learning", font=_font(14, bold=True), fill=TEXT_DARK)
    d.text((155, 125), "Spanish?", font=_font(14, bold=True), fill=TEXT_DARK)
    options = [
        ("🌎  For travel", False),
        ("👨‍👩‍👧  For family / friends", True),
        ("🧠  Brain training", False),
        ("🎓  School", False),
        ("💼  My career", False),
        ("🎬  TV / Music", False),
    ]
    y = 200
    for label, selected in options:
        bg = DUO_GREEN if selected else (250, 250, 250)
        fg = (255, 255, 255) if selected else TEXT_DARK
        _rounded_rect(d, [(20, y), (W - 20, y + 64)], 12, fill=bg, outline=LIGHT_GREY, width=1)
        d.text((35, y + 22), label, font=_font(16, bold=True), fill=fg)
        y += 74
    _btn(d, 720, "CONTINUE", fill=DUO_GREEN)
    _centered(d, 820, "Note: 4-tap commitment, no signup yet", _font(11), fill=TEXT_MED)
    img.save(os.path.join(IMG_DIR, "03-motivation-quiz-new-user.png"))


def screen_04_daily_goal():
    """Daily goal: 5 / 10 / 15 / 20 minutes."""
    img, d = _new_canvas()
    _draw_owl(d, 80, 110, size=40)
    _rounded_rect(d, [(140, 90), (W - 30, 160)], 12, fill=(245, 245, 245))
    d.text((155, 105), "Great. Now pick a", font=_font(14, bold=True), fill=TEXT_DARK)
    d.text((155, 125), "daily learning goal:", font=_font(14, bold=True), fill=TEXT_DARK)
    goals = [
        ("Casual", "5 min / day", False),
        ("Regular", "10 min / day", True),
        ("Serious", "15 min / day", False),
        ("Intense", "20 min / day", False),
    ]
    y = 200
    for label, sub, selected in goals:
        bg = DUO_GREEN if selected else (250, 250, 250)
        fg = (255, 255, 255) if selected else TEXT_DARK
        sub_fg = (220, 245, 200) if selected else TEXT_MED
        _rounded_rect(d, [(20, y), (W - 20, y + 80)], 12, fill=bg, outline=LIGHT_GREY, width=1)
        d.text((35, y + 16), label, font=_font(17, bold=True), fill=fg)
        d.text((35, y + 46), sub, font=_font(13), fill=sub_fg)
        y += 90
    _btn(d, 720, "CONTINUE", fill=DUO_GREEN)
    img.save(os.path.join(IMG_DIR, "04-daily-goal-new-user.png"))


def screen_05_first_lesson():
    """First lesson — translate a sentence by tapping word bubbles."""
    img, d = _new_canvas()
    # Top bar with X + progress + heart
    d.text((20, 75), "✕", font=_font(20, bold=True), fill=TEXT_MED)
    _rounded_rect(d, [(50, 80), (W - 70, 95)], 7, fill=LIGHT_GREY)
    _rounded_rect(d, [(50, 80), (180, 95)], 7, fill=DUO_GREEN)
    d.text((W - 60, 75), "❤ 5", font=_font(14, bold=True), fill=DUO_RED)
    # Prompt
    d.text((20, 140), "Translate this sentence", font=_font(16, bold=True), fill=TEXT_DARK)
    _draw_owl(d, 60, 220, size=30)
    _rounded_rect(d, [(100, 200), (W - 30, 250)], 12, fill=(245, 245, 245))
    d.text((115, 218), '"The boy drinks milk"', font=_font(16, bold=True), fill=TEXT_DARK)
    # Picked words area
    d.line([(20, 320), (W - 20, 320)], fill=LIGHT_GREY, width=1)
    d.line([(20, 380), (W - 20, 380)], fill=LIGHT_GREY, width=1)
    _rounded_rect(d, [(30, 330), (110, 370)], 10, fill=(255, 255, 255), outline=DUO_BLUE, width=2)
    d.text((50, 340), "El", font=_font(16, bold=True), fill=DUO_BLUE)
    _rounded_rect(d, [(120, 330), (200, 370)], 10, fill=(255, 255, 255), outline=DUO_BLUE, width=2)
    d.text((135, 340), "niño", font=_font(16, bold=True), fill=DUO_BLUE)
    # Word bank
    words = [("bebe", 30, 430), ("agua", 130, 430), ("leche", 230, 430),
             ("come", 30, 490), ("pan", 130, 490), ("toma", 230, 490)]
    for w, x, y in words:
        _rounded_rect(d, [(x, y), (x + 90, y + 40)], 10, fill=(255, 255, 255), outline=LIGHT_GREY, width=2)
        d.text((x + 20, y + 10), w, font=_font(15, bold=True), fill=TEXT_DARK)
    _btn(d, 660, "CHECK", fill=LIGHT_GREY, text_color=TEXT_MED)
    _centered(d, 820, "Note: first lesson in <60 sec, no signup", _font(11), fill=TEXT_MED)
    img.save(os.path.join(IMG_DIR, "05-first-lesson-new-user.png"))


def screen_06_streak():
    """End of lesson 1 — streak celebration + notification ask."""
    img, d = _new_canvas()
    d.rectangle([(0, 56), (W, H)], fill=(255, 251, 230))
    _centered(d, 100, "Great first lesson!", _font(24, bold=True))
    # Big flame
    d.ellipse([(W // 2 - 60, 150), (W // 2 + 60, 270)], fill=DUO_RED)
    d.polygon([(W // 2 - 40, 150), (W // 2 + 40, 150), (W // 2, 80)], fill=DUO_RED)
    _centered(d, 200, "1", _font(60, bold=True), fill=(255, 255, 255))
    _centered(d, 300, "You're on a 1-day streak", _font(18, bold=True))
    _centered(d, 332, "Keep it going tomorrow.", _font(14), fill=TEXT_MED)
    # Notification reminder card
    _rounded_rect(d, [(30, 400), (W - 30, 540)], 14, fill=(255, 255, 255), outline=LIGHT_GREY, width=2)
    d.text((50, 420), "🔔  Daily reminders", font=_font(14, bold=True), fill=TEXT_DARK)
    d.text((50, 445), "Set a reminder at:", font=_font(13), fill=TEXT_MED)
    _rounded_rect(d, [(50, 472), (130, 508)], 8, fill=DUO_GREEN)
    d.text((68, 480), "7 PM", font=_font(13, bold=True), fill=(255, 255, 255))
    _rounded_rect(d, [(140, 472), (220, 508)], 8, fill=(255, 255, 255), outline=LIGHT_GREY, width=2)
    d.text((160, 480), "8 PM", font=_font(13, bold=True), fill=TEXT_DARK)
    _rounded_rect(d, [(230, 472), (310, 508)], 8, fill=(255, 255, 255), outline=LIGHT_GREY, width=2)
    d.text((250, 480), "9 PM", font=_font(13, bold=True), fill=TEXT_DARK)
    _btn(d, 600, "TURN ON REMINDERS", fill=DUO_GREEN)
    _btn(d, 670, "NO THANKS", fill=(255, 255, 255), text_color=TEXT_MED)
    pad = int(W * 0.075)
    _rounded_rect(d, [(pad, 670), (W - pad, 726)], 14, fill=(255, 255, 255), outline=LIGHT_GREY, width=2)
    _centered(d, 670 + 20, "NO THANKS", _font(15, bold=True), fill=TEXT_MED)
    _centered(d, 820, "Note: notification ask AFTER value delivered", _font(11), fill=TEXT_MED)
    img.save(os.path.join(IMG_DIR, "06-streak-celebration-new-user.png"))


def screen_07_save_progress():
    """Account creation — framed as 'Save your progress' AFTER lesson 1."""
    img, d = _new_canvas()
    _draw_owl(d, W // 2, 150, size=60)
    _centered(d, 240, "Save your progress!", _font(22, bold=True))
    _centered(d, 280, "Make sure you don't lose your", _font(14), fill=TEXT_MED)
    _centered(d, 302, "1-day streak.", _font(14), fill=TEXT_MED)
    # Inputs
    _rounded_rect(d, [(30, 360), (W - 30, 410)], 10, fill=(250, 250, 250), outline=LIGHT_GREY, width=1)
    d.text((45, 378), "Age", font=_font(14), fill=TEXT_MED)
    _rounded_rect(d, [(30, 425), (W - 30, 475)], 10, fill=(250, 250, 250), outline=LIGHT_GREY, width=1)
    d.text((45, 443), "Name (optional)", font=_font(14), fill=TEXT_MED)
    _rounded_rect(d, [(30, 490), (W - 30, 540)], 10, fill=(250, 250, 250), outline=LIGHT_GREY, width=1)
    d.text((45, 508), "Email or username", font=_font(14), fill=TEXT_MED)
    _rounded_rect(d, [(30, 555), (W - 30, 605)], 10, fill=(250, 250, 250), outline=LIGHT_GREY, width=1)
    d.text((45, 573), "Password", font=_font(14), fill=TEXT_MED)
    _btn(d, 640, "CREATE ACCOUNT", fill=DUO_GREEN)
    _centered(d, 710, "or", _font(13), fill=TEXT_MED)
    _btn(d, 730, "CONTINUE WITH GOOGLE", fill=(255, 255, 255), text_color=TEXT_DARK)
    pad = int(W * 0.075)
    _rounded_rect(d, [(pad, 730), (W - pad, 786)], 14, fill=(255, 255, 255), outline=LIGHT_GREY, width=2)
    _centered(d, 730 + 20, "CONTINUE WITH GOOGLE", _font(15, bold=True), fill=TEXT_DARK)
    _centered(d, 830, "Note: account gated AFTER value, framed as loss-aversion", _font(10), fill=TEXT_MED)
    img.save(os.path.join(IMG_DIR, "07-save-progress-new-user.png"))


def screen_08_no_paywall():
    """Home / lesson tree on Day 0 — no paywall shown, Super offered as upsell only."""
    img, d = _new_canvas()
    # Top bar with streak, gems, hearts
    d.text((25, 70), "🔥 1", font=_font(15, bold=True), fill=DUO_RED)
    d.text((110, 70), "💎 5", font=_font(15, bold=True), fill=DUO_BLUE)
    d.text((195, 70), "❤ 5", font=_font(15, bold=True), fill=DUO_RED)
    d.text((290, 70), "🇪🇸", font=_font(20))
    # Unit header
    _rounded_rect(d, [(20, 110), (W - 20, 180)], 14, fill=DUO_GREEN)
    d.text((40, 125), "SECTION 1, UNIT 1", font=_font(11, bold=True), fill=(220, 245, 200))
    d.text((40, 145), "Order food and drinks", font=_font(16, bold=True), fill=(255, 255, 255))
    # Lesson tree nodes
    nodes_y = [220, 290, 360, 430, 500]
    for i, y in enumerate(nodes_y):
        is_done = i == 0
        is_current = i == 1
        is_locked = i > 1
        offset = ((i % 2) * 80) - 40
        cx = W // 2 + offset
        if is_done:
            d.ellipse([(cx - 35, y - 35), (cx + 35, y + 35)], fill=DUO_GREEN)
            d.text((cx - 8, y - 10), "★", font=_font(22, bold=True), fill=(255, 255, 255))
        elif is_current:
            d.ellipse([(cx - 40, y - 40), (cx + 40, y + 40)], fill=DUO_GREEN_DARK)
            d.text((cx - 8, y - 10), "▶", font=_font(20, bold=True), fill=(255, 255, 255))
        else:
            d.ellipse([(cx - 35, y - 35), (cx + 35, y + 35)], fill=LIGHT_GREY)
            d.text((cx - 6, y - 10), "🔒", font=_font(18))
    # Super card (NOT a paywall — discoverable upsell)
    _rounded_rect(d, [(20, 600), (W - 20, 720)], 14, fill=(245, 245, 255), outline=DUO_BLUE, width=2)
    d.text((40, 615), "✨ Try Super Duolingo", font=_font(15, bold=True), fill=DUO_BLUE)
    d.text((40, 640), "No ads, unlimited hearts, personalized", font=_font(11), fill=TEXT_MED)
    d.text((40, 658), "review. Try free for 14 days.", font=_font(11), fill=TEXT_MED)
    _rounded_rect(d, [(40, 680), (200, 710)], 8, fill=DUO_BLUE)
    d.text((75, 687), "TRY 14 DAYS FREE", font=_font(11, bold=True), fill=(255, 255, 255))
    # Bottom nav
    d.line([(0, 760), (W, 760)], fill=LIGHT_GREY, width=1)
    icons = ["🏠", "🏆", "💎", "🛡", "👤"]
    for i, ic in enumerate(icons):
        d.text((30 + i * 75, 800), ic, font=_font(22))
    _centered(d, 870, "Note: no paywall block — value continues uninterrupted", _font(10), fill=TEXT_MED)
    img.save(os.path.join(IMG_DIR, "08-home-no-paywall-new-user.png"))


def main():
    print(f"Writing mockups to: {IMG_DIR}")
    screen_01_landing()
    screen_02_language()
    screen_03_motivation()
    screen_04_daily_goal()
    screen_05_first_lesson()
    screen_06_streak()
    screen_07_save_progress()
    screen_08_no_paywall()
    files = sorted(os.listdir(IMG_DIR))
    print(f"Generated {len(files)} mockups:")
    for f in files:
        print(f"  {f}")


if __name__ == "__main__":
    main()
