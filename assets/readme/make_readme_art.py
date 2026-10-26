"""Builds the README banner: the agent-environment loop on the left, the Arabic title on the right.

Run from the repo root:  python3 assets/readme/make_readme_art.py
Needs Pillow built with libraqm (Arabic shaping) and the Cairo fonts in assets/fonts (SIL OFL 1.1).
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
FONTS = ROOT / "assets" / "fonts"

W, H = 2400, 840
BG = (8, 12, 20)
BLUE = (57, 135, 229)
ORANGE = (235, 104, 52)
INK = (240, 239, 236)
MUTED = (150, 156, 168)


def font(weight, size):
    return ImageFont.truetype(str(FONTS / f"Cairo_{weight}.ttf"), size)


def ar(d, xy, text, f, fill, anchor="ra"):
    """Arabic (or mixed) text, shaped and laid out right to left."""
    d.text(xy, text, font=f, fill=fill, anchor=anchor, direction="rtl", language="ar")


def arrow(d, p0, p1, col, width=6, head=22):
    d.line([p0, p1], fill=col, width=width)
    a = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    pts = [p1, (p1[0] - head * math.cos(a - 0.45), p1[1] - head * math.sin(a - 0.45)),
           (p1[0] - head * math.cos(a + 0.45), p1[1] - head * math.sin(a + 0.45))]
    d.polygon(pts, fill=col)


def label(d, cx, cy, word, var, sub, f, fs):
    """'word  var_sub' centred at (cx, cy), with a hand-drawn subscript (Cairo has no subscript glyphs)."""
    main = f"{word}  {var}"
    w = d.textlength(main, font=f) + d.textlength(sub, font=fs) + 2
    x0 = cx - w / 2
    d.text((x0, cy), main, font=f, fill=INK, anchor="lm")
    d.text((x0 + d.textlength(main, font=f) + 2, cy + 12), sub, font=fs, fill=INK, anchor="lm")


def banner():
    im = Image.new("RGB", (W, H), BG)

    # faint grid and a rising learning curve behind everything
    grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    g = ImageDraw.Draw(grid)
    for x in range(0, W, 60):
        g.line([(x, 0), (x, H)], fill=(255, 255, 255, 10))
    for y in range(0, H, 60):
        g.line([(0, y), (W, y)], fill=(255, 255, 255, 10))
    pts = []
    for i in range(0, 1101, 6):
        t = i / 1100
        y = 0.95 - 0.17 * (1 - math.exp(-4.2 * t)) + 0.012 * math.sin(37 * t) * (1 - t)
        pts.append((60 + i, int(H * y)))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).line(pts, fill=BLUE + (120,), width=14)
    glow = glow.filter(ImageFilter.GaussianBlur(14))
    g.line(pts, fill=BLUE + (150,), width=4)
    im.paste(glow, (0, 0), glow)
    im.paste(grid, (0, 0), grid)
    ImageDraw.Draw(im).text((1170, pts[-1][1]), "mean reward", font=ImageFont.truetype(str(FONTS / "Cairo_400Regular.ttf"), 24),
                            fill=(110, 150, 205), anchor="lm")

    # agent-environment loop
    d = ImageDraw.Draw(im)
    lat = lambda s: ImageFont.truetype(str(FONTS / "Cairo_600SemiBold.ttf"), s)
    agent = (170, 250, 560, 450)
    env = (720, 250, 1110, 450)
    for box, col, name, sub in [(agent, BLUE, "Agent", "policy  π(a | s)"), (env, ORANGE, "Environment", "Gymnasium · Unity")]:
        d.rounded_rectangle(box, radius=28, fill=(14, 22, 38), outline=col, width=5)
        cx = (box[0] + box[2]) / 2
        d.text((cx, box[1] + 82), name, font=lat(54), fill=INK, anchor="mm")
        d.text((cx, box[1] + 145), sub, font=lat(30), fill=MUTED, anchor="mm")
    arrow(d, (agent[2] + 10, 300), (env[0] - 12, 300), ORANGE)
    label(d, (agent[2] + env[0]) / 2, 268, "action", "a", "t", lat(30), lat(20))
    arrow(d, (env[0] - 12, 400), (agent[2] + 10, 400), BLUE)
    label(d, (agent[2] + env[0]) / 2, 432, "state", "s", "t+1", lat(30), lat(20))
    d.line([(940, env[3] + 8), (940, 560), (365, 560), (365, agent[3] + 22)], fill=(26, 158, 143), width=6)
    arrow(d, (365, 540), (365, agent[3] + 12), (26, 158, 143))
    label(d, 652, 590, "reward", "r", "t+1", lat(30), lat(20))

    # Arabic title block, right aligned
    x = W - 110
    ar(d, (x, 120), "التعلّم المعزّز العميق", font("800ExtraBold", 116), INK)
    ar(d, (x, 300), "كورس Hugging Face بالعربي", font("600SemiBold", 58), (150, 196, 255))
    ar(d, (x, 410), "نوتبوكس كاملة، مشروحة خطوة بخطوة،", font("400Regular", 38), (215, 220, 228))
    ar(d, (x, 466), "ومتشغّلة لحد آخرها بنتايج حقيقية", font("400Regular", 38), (215, 220, 228))
    chips = ["Gymnasium", "Stable-Baselines3", "PyTorch", "Unity ML-Agents"]
    f = lat(28)
    cx = x
    for c in chips:
        w = d.textlength(c, font=f) + 48
        d.rounded_rectangle((cx - w, 572, cx, 626), radius=27, outline=(120, 170, 235), width=2, fill=(16, 28, 48))
        d.text((cx - w / 2, 597), c, font=f, fill=(220, 232, 250), anchor="mm")
        cx -= w + 14
    d.text((x, 708), "Mohamed Ashraf Mostafa  ·  Petroleum & Robotics Engineer", font=lat(28), fill=MUTED, anchor="rm")
    im.save(OUT / "banner.jpg", quality=90, optimize=True, progressive=True)


if __name__ == "__main__":
    banner()
    print("written:", OUT / "banner.jpg")
