#!/usr/bin/env python3
"""Render the slide PNGs for one lesson from video/lesson_NN/slides.json.

Usage: python3 scripts/make_slides.py 2

Slide types in slides.json:
  title     {"title", "subtitle", "line3"}
  content   {"heading", "bullets": [...], "code": [...], "note"}
  subscribe {"steps": [...]}
  image     {"file": "source/some.png"}   (use a finished PNG as-is)

Output: video/lesson_NN/slides/slide1.png, slide2.png, ... (1920x1080)
"""
import json
import shutil
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
W, H = 1920, 1080
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
BOLD, REG, MONO = "DejaVuSans-Bold.ttf", "DejaVuSans.ttf", "DejaVuSansMono.ttf"
BG, FG, ACC, SUB, CODEBG = (8, 58, 50), (255, 255, 255), (245, 184, 65), (127, 227, 201), (4, 30, 26)
BOTTOM_LIMIT = H - 140  # nothing may be drawn below this line


def font(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


def base(title, footer):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 14], fill=ACC)
    d.text((110, 90), title, font=font(BOLD, 74), fill=FG)
    d.text((W - 110, H - 60), footer, font=font(REG, 32), fill=SUB, anchor="rs")
    return im, d


def bullets(d, items, y, size=46, gap=95):
    for it in items:
        d.ellipse([120, y + 18, 146, y + 44], fill=ACC)
        d.text((180, y), it, font=font(REG, size), fill=FG)
        y += gap
    return y


def code(d, lines, y, size=40):
    x = 120
    w = W - 2 * x
    h = 70 * len(lines) + 40
    d.rounded_rectangle([x, y, x + w, y + h], radius=18, fill=CODEBG)
    for i, ln in enumerate(lines):
        d.text((x + 36, y + 30 + i * 70), ln, font=font(MONO, size), fill=(220, 240, 235))
    return y + h


def render_title(s, footer):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 14], fill=ACC)
    d.text((W // 2, 300), s["title"], font=font(BOLD, 96), fill=FG, anchor="mm")
    d.text((W // 2, 440), s["subtitle"], font=font(REG, 66), fill=ACC, anchor="mm")
    d.text((W // 2, 580), s.get("line3", ""), font=font(REG, 50), fill=SUB, anchor="mm")
    d.text((W // 2, 900), footer, font=font(REG, 42), fill=SUB, anchor="mm")
    return im


def render_content(s, footer, slide_no):
    im, d = base(s["heading"], footer)
    y = 230
    if s.get("bullets"):
        y = bullets(d, s["bullets"], y, gap=s.get("gap", 95)) + 30
    if s.get("code"):
        y = code(d, s["code"], y, size=s.get("code_size", 40)) + 30
    if s.get("note"):
        d.text((120, H - 160), s["note"], font=font(REG, 38), fill=SUB)
    if y > BOTTOM_LIMIT:
        raise ValueError(f"slide {slide_no}: content runs to y={y}, past {BOTTOM_LIMIT}. Shorten it or split the slide.")
    return im


def render_subscribe(s, footer):
    im, d = base(s.get("heading", "Before you go"), footer)
    y = 260
    for i, step in enumerate(s["steps"], 1):
        d.ellipse([120, y, 220, y + 100], fill=ACC)
        d.text((170, y + 50), str(i), font=font(BOLD, 56), fill=BG, anchor="mm")
        d.text((260, y + 22), step, font=font(REG, 52), fill=FG)
        y += 170
    return im


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: make_slides.py <lesson number>")
    lesson = int(sys.argv[1])
    folder = ROOT / "video" / f"lesson_{lesson:02d}"
    spec = json.loads((folder / "slides.json").read_text(encoding="utf-8"))
    out = folder / "slides"
    out.mkdir(exist_ok=True)
    footer = spec.get("footer", f"Vortex Java · Lesson {lesson} of 150")

    for i, s in enumerate(spec["slides"], 1):
        t = s["type"]
        target = out / f"slide{i}.png"
        if t == "image":
            shutil.copy(folder / s["file"], target)
        elif t == "title":
            render_title(s, footer).save(target)
        elif t == "content":
            render_content(s, footer, i).save(target)
        elif t == "subscribe":
            render_subscribe(s, s.get("footer", footer)).save(target)
        else:
            sys.exit(f"slide {i}: unknown type '{t}'")
        print(f"slide {i} ({t}) -> {target.relative_to(ROOT)}")
    print(f"done: {len(spec['slides'])} slides for lesson {lesson}")


if __name__ == "__main__":
    main()
