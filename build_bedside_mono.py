#!/usr/bin/env fontforge -lang=py -script

import os
import sys

import fontforge
import psMat


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "BedsideMono.ttf")

EM_SIZE = 1000
ASCENT = 800
DESCENT = 200
ADVANCE_WIDTH = 600

GLYPH_MAP = {
    "Zero.svg": 0x0030,
    "One.svg": 0x0031,
    "Two.svg": 0x0032,
    "Three.svg": 0x0033,
    "Four.svg": 0x0034,
    "Five.svg": 0x0035,
    "Six.svg": 0x0036,
    "Seven.svg": 0x0037,
    "Eight.svg": 0x0038,
    "Nine.svg": 0x0039,
    "Colon.svg": 0x003A,
}


def build_font():
    font = fontforge.font()
    font.encoding = "UnicodeFull"
    font.em = EM_SIZE
    font.ascent = ASCENT
    font.descent = DESCENT

    font.familyname = "Bedside Mono"
    font.fullname = "Bedside Mono"
    font.fontname = "BedsideMono"
    font.weight = "Regular"
    font.version = "1.0"
    font.copyright = "Copyright 2026"
    font.os2_vendor = "SYRP"
    font.os2_version = 4
    font.os2_weight = 400
    font.os2_width = 5
    font.os2_stylemap = 64
    font.os2_use_typo_metrics = True
    font.os2_typoascent = ASCENT
    font.os2_typodescent = -DESCENT
    font.os2_typolinegap = 0
    font.os2_winascent = ASCENT
    font.os2_windescent = DESCENT
    font.hhea_ascent = ASCENT
    font.hhea_descent = -DESCENT
    font.hhea_linegap = 0
    font.os2_capheight = ASCENT
    font.os2_xheight = int(ASCENT * 0.55)
    font.os2_family_class = 2057
    font.os2_panose = (2, 11, 5, 9, 2, 2, 2, 2, 2, 7)

    add_notdef(font)
    add_space(font)
    import_svg_glyphs(font)

    font.selection.all()
    font.round()
    font.autoHint()
    font.generate(OUTPUT_PATH)


def add_notdef(font):
    glyph = font.createChar(-1, ".notdef")
    outer_left = 80
    outer_bottom = 80
    outer_right = ADVANCE_WIDTH - 80
    outer_top = EM_SIZE - 80
    inner_inset = 90

    pen = glyph.glyphPen()
    pen.moveTo((outer_left, outer_bottom))
    pen.lineTo((outer_right, outer_bottom))
    pen.lineTo((outer_right, outer_top))
    pen.lineTo((outer_left, outer_top))
    pen.closePath()

    pen.moveTo((outer_left + inner_inset, outer_bottom + inner_inset))
    pen.lineTo((outer_left + inner_inset, outer_top - inner_inset))
    pen.lineTo((outer_right - inner_inset, outer_top - inner_inset))
    pen.lineTo((outer_right - inner_inset, outer_bottom + inner_inset))
    pen.closePath()

    glyph.width = ADVANCE_WIDTH


def add_space(font):
    glyph = font.createChar(0x0020, "space")
    glyph.width = ADVANCE_WIDTH


def import_svg_glyphs(font):
    for filename, codepoint in GLYPH_MAP.items():
        path = os.path.join(SCRIPT_DIR, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Missing glyph source: {filename}")

        glyph = font.createChar(codepoint)
        glyph.clear()
        glyph.importOutlines(path)
        align_glyph(glyph, codepoint)
        glyph.width = ADVANCE_WIDTH
        glyph.removeOverlap()
        glyph.correctDirection()


def align_glyph(glyph, codepoint):
    xmin, ymin, xmax, ymax = glyph.boundingBox()

    if codepoint == 0x0031:
        side_bearing = 32
        x_offset = ADVANCE_WIDTH - side_bearing - xmax
    else:
        x_offset = (ADVANCE_WIDTH - (xmax - xmin)) / 2.0 - xmin

    glyph.transform(psMat.translate(x_offset, 0))


if __name__ == "__main__":
    try:
        build_font()
    except Exception as exc:
        print(f"Bedside Mono build failed: {exc}", file=sys.stderr)
        raise
