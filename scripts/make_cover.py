"""Render assets/cover.svg to assets/cover.jpg (1600 x 2560, RGB) for KDP and the editions.

Needs cairosvg, Pillow and the Inter and Inter Display fonts installed. Run by hand when the
cover changes; the built JPEG is committed so CI does not need the fonts.
"""

import io
import math
from pathlib import Path

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
W, H = 1600, 2560
INK, PAPER, MUTED, ACCENT = "#0d1117", "#f4f1ea", "#3a4250", "#ff6b2c"


def arc(cx, cy, r, start, end):
    """SVG path for a circular arc from start to end degrees, clockwise from 12 o'clock."""
    a0, a1 = math.radians(start - 90), math.radians(end - 90)
    x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
    large = 1 if (end - start) % 360 > 180 else 0
    return f"M{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{y1:.1f}"


def rings():
    """Concentric rings with offset gaps: layered defences, each with its own opening."""
    cx, cy = W / 2, 980
    parts = []
    for i, r in enumerate(range(140, 760, 62)):
        gap = 26 + i * 3
        offset = (i * 47) % 360
        colour = ACCENT if i == 2 else MUTED
        width = 16 if i == 2 else 10
        parts.append(
            f'<path d="{arc(cx, cy, r, offset + gap, offset + 360)}" fill="none" '
            f'stroke="{colour}" stroke-width="{width}" stroke-linecap="round"/>'
        )
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="58" fill="{PAPER}"/>')
    return "\n".join(parts)


SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="{W}" height="{H}" fill="{INK}"/>
  {rings()}
  <text x="120" y="1960" fill="{PAPER}" font-family="Inter Display" font-weight="900"
        font-size="250" letter-spacing="-6">HARD</text>
  <text x="120" y="2190" fill="{PAPER}" font-family="Inter Display" font-weight="900"
        font-size="250" letter-spacing="-6">TARGET</text>
  <rect x="124" y="1700" width="180" height="14" fill="{ACCENT}"/>
  <text x="124" y="1650" fill="{PAPER}" font-family="Inter" font-weight="500"
        font-size="54">The 2026 field manual for digital privacy</text>
  <text x="124" y="2420" fill="{PAPER}" font-family="Inter" font-weight="600"
        font-size="58" letter-spacing="10">MORGAN HOLLAND</text>
  <text x="1476" y="2420" fill="{MUTED}" font-family="Inter" font-weight="500"
        font-size="40" text-anchor="end">with AI agent prompts</text>
</svg>
"""


def main():
    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets/cover.svg").write_text(SVG, encoding="utf-8")
    png = cairosvg.svg2png(bytestring=SVG.encode(), output_width=W, output_height=H)
    Image.open(io.BytesIO(png)).convert("RGB").save(
        ROOT / "assets/cover.jpg", "JPEG", quality=90, dpi=(300, 300), optimize=True
    )


if __name__ == "__main__":
    main()
