#!/usr/bin/env python3
"""
gen_pwa_icons.py — generates PWA icons for web_reader from the brand loop mark.

Icons are STATIC (brand mark doesn't change), so this only needs re-running if
the brand colours or glyph change — NOT on every build. Run manually:

    python scripts/gen_pwa_icons.py

Output (web_reader/icons/):
    icon-192.png, icon-512.png   — maskable, full-bleed ochre (Android install)
    apple-touch-icon.png (180)   — iOS home-screen
    favicon.png (32)             — browser tab

Design: full-bleed ochre-9 (#8E5F3D) background + the brand "console loop" mark
([ · ]) in paper (#F7F4ED), matching .claude/rules/web-reader-design.md.
"""

from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).parent.parent
OUT_DIR = ROOT / "web_reader" / "icons"

OCHRE = (0x8E, 0x5F, 0x3D)   # --ochre-9
PAPER = (0xF7, 0xF4, 0xED)   # --paper-0 (light bg)

# Brand mark in SVG viewBox space (0..44): two brackets facing a centre dot.
LEFT_BRACKET  = [(14, 18), (14, 26), (18, 26)]
RIGHT_BRACKET = [(30, 18), (30, 26), (26, 26)]
DOT = (22, 22)


def _t(pt, scale, cx, cy):
    """Transform a viewBox coord (centred on 22,22) into icon pixel space."""
    x, y = pt
    return ((x - 22) * scale + cx, (y - 22) * scale + cy)


def _stroke(draw, pts, scale, cx, cy, width):
    """Draw a rounded polyline (round caps + round joins via vertex circles)."""
    tp = [_t(p, scale, cx, cy) for p in pts]
    draw.line(tp, fill=PAPER, width=width, joint="curve")
    r = width / 2
    for (px, py) in tp:
        draw.ellipse([px - r, py - r, px + r, py + r], fill=PAPER)


def render(size: int, maskable: bool) -> Image.Image:
    # Supersample 4x for smooth edges, then downscale.
    ss = 4
    S = size * ss
    img = Image.new("RGBA", (S, S), OCHRE + (255,))
    draw = ImageDraw.Draw(img)

    cx = cy = S / 2
    # Maskable icons must keep content inside the centre ~80% safe zone; the
    # favicon/apple icon can run the glyph a touch larger since they aren't masked.
    fill_ratio = 0.52 if maskable else 0.62
    scale = (S * fill_ratio / 2) / 8.0   # glyph half-extent in viewBox = 8
    width = int(S * 0.055)

    _stroke(draw, LEFT_BRACKET, scale, cx, cy, width)
    _stroke(draw, RIGHT_BRACKET, scale, cx, cy, width)
    # Centre dot
    dr = S * 0.052
    dx, dy = _t(DOT, scale, cx, cy)
    draw.ellipse([dx - dr, dy - dr, dx + dr, dy + dr], fill=PAPER)

    return img.resize((size, size), Image.LANCZOS)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    render(192, maskable=True).save(OUT_DIR / "icon-192.png")
    render(512, maskable=True).save(OUT_DIR / "icon-512.png")
    render(180, maskable=False).save(OUT_DIR / "apple-touch-icon.png")
    render(32,  maskable=False).save(OUT_DIR / "favicon.png")
    print(f"Wrote 4 icons to {OUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
