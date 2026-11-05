# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "python-pptx>=1.0.0",
# ]
# ///
"""Build an SDSC-branded PowerPoint template (.pptx) from references/tokens.toml.

The token file is the single source of truth (see _tokens.py). This script turns
it into a 16:9 deck whose slide master carries the SDSC fonts + colour scheme and
whose slides demonstrate the SDSC layouts a presenter copies from:

    Title · Section divider · Content (bullets + key-takeaway) · Two-column ·
    Feature grid · Key numbers · Code · Chart palette · Quote / findings ·
    CTA banner · Closing.

It mirrors the Slidev theme one-for-one, so the .pptx and the Markdown deck look
the same. Designers retheme by editing tokens.toml and re-running this — no code
changes. python-pptx cannot embed fonts, so install Space Grotesk + Switzer (and
Fira Code for code) locally for PowerPoint to render them (otherwise the
fallbacks in [fonts] are used).

Usage (from the skill root):
    uv run scripts/build_pptx.py                       # -> SDSC_Slides_Template.pptx
    uv run scripts/build_pptx.py --dark -o Dark.pptx   # dark theme variant
    uv run scripts/build_pptx.py -o my_template.pptx
    uv run scripts/build_pptx.py --tokens path/to/tokens.toml
"""

from __future__ import annotations

import argparse
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

import _tokens

A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
LOGOS = Path(__file__).resolve().parent.parent / "assets" / "logos"


def rgb(hex_value: str) -> RGBColor:
    return RGBColor(*_tokens.hex_to_rgb(hex_value))


# --------------------------------------------------------------------------- #
# Master theme: best-effort write of the SDSC fonts + colour scheme into the
# theme part so NEW slides a user adds also pick up the brand. Wrapped so a
# python-pptx version that parses theme differently never breaks the build.
# --------------------------------------------------------------------------- #
def apply_master_theme(prs: Presentation, tokens: dict) -> None:
    fonts, colors = tokens["fonts"], tokens["colors"]
    ns = {"a": A_NS}

    def edit(root) -> None:
        scheme = root.find(".//a:fontScheme", ns)
        if scheme is not None:
            for tag, family in (("a:majorFont", fonts["heading"]),
                                ("a:minorFont", fonts["body"])):
                latin = scheme.find(f"{tag}/a:latin", ns)
                if latin is not None:
                    latin.set("typeface", family)
        # Map brand colours onto the Office colour-scheme slots.
        clr = {
            "dk2": colors["secondary"], "lt2": colors["background_alt"],
            "accent1": colors["primary"], "accent2": colors["secondary"],
            "accent3": colors["accent_green"], "accent4": colors["text_grey"],
            "hlink": colors["primary"], "folHlink": colors["secondary"],
        }
        scheme = root.find(".//a:clrScheme", ns)
        if scheme is not None:
            for slot, hex_value in clr.items():
                node = scheme.find(f"a:{slot}", ns)
                if node is None:
                    continue
                for child in list(node):
                    node.remove(child)
                srgb = node.makeelement(qn("a:srgbClr"),
                                        {"val": hex_value.lstrip("#").upper()})
                node.append(srgb)

    try:
        theme_part = prs.slide_masters[0].part.part_related_by(RT.THEME)
        if hasattr(theme_part, "_element"):
            edit(theme_part._element)
        else:
            from lxml import etree
            root = etree.fromstring(theme_part.blob)
            edit(root)
            theme_part._blob = etree.tostring(
                root, xml_declaration=True, encoding="UTF-8", standalone=True)
    except Exception as exc:  # pragma: no cover - defensive
        print(f"  ! could not patch master theme ({exc}); per-shape styling "
              "still applies.")


# --------------------------------------------------------------------------- #
# Low-level shape helpers
# --------------------------------------------------------------------------- #
def add_rect(slide, x, y, w, h, fill_hex, line_hex=None, line_pt=0.75):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    if fill_hex is None:
        shape.fill.background()
    else:
        shape.fill.solid()
        shape.fill.fore_color.rgb = rgb(fill_hex)
    if line_hex is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = rgb(line_hex)
        shape.line.width = Pt(line_pt)
    shape.shadow.inherit = False
    return shape


def _style_run(run, style: dict) -> None:
    run.font.name = style["font"]
    run.font.size = Pt(style["size"])
    run.font.bold = style["bold"]
    run.font.color.rgb = rgb(style["color"])


def add_text(slide, x, y, w, h, paragraphs, *, align=PP_ALIGN.LEFT,
             anchor=MSO_ANCHOR.TOP, line_spacing=None):
    """paragraphs: list of (text, resolved-style[, space_after_pt]) tuples."""
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for i, item in enumerate(paragraphs):
        text, style = item[0], item[1]
        space_after = item[2] if len(item) > 2 else 6
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(space_after)
        if line_spacing is not None:
            p.line_spacing = line_spacing
        run = p.add_run()
        run.text = text
        _style_run(run, style)
    return box


def add_bullets(slide, x, y, w, h, items, style, *, gap_pt=10,
                marker="○", marker_hex=None):
    """Bulleted list with a hollow ring marker (U+25CB) in the brand colour."""
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    for i, text in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(gap_pt)
        p.level = 0
        run = p.add_run()
        run.text = text
        _style_run(run, style)
        # Real bullet glyph + hanging indent via DrawingML.
        pPr = p._p.get_or_add_pPr()
        pPr.set("marL", str(Emu(Inches(0.32))))
        pPr.set("indent", str(-Emu(Inches(0.32))))
        if marker_hex is not None:
            bu_clr = pPr.makeelement(qn("a:buClr"), {})
            srgb = bu_clr.makeelement(qn("a:srgbClr"),
                                      {"val": marker_hex.lstrip("#").upper()})
            bu_clr.append(srgb)
            pPr.append(bu_clr)
        bu_font = pPr.makeelement(qn("a:buFont"), {"typeface": "Arial"})
        bu_char = pPr.makeelement(qn("a:buChar"), {"char": marker})
        pPr.append(bu_font)
        pPr.append(bu_char)
    return box


def add_gradient_rect(slide, x, y, w, h, start_hex, end_hex, angle_deg):
    """Full linear-gradient rectangle (used for the title/closing backgrounds)."""
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shape.line.fill.background()
    shape.shadow.inherit = False
    shape.fill.gradient()
    stops = shape.fill.gradient_stops
    stops[0].position = 0.0
    stops[0].color.rgb = rgb(start_hex)
    stops[1].position = 1.0
    stops[1].color.rgb = rgb(end_hex)
    try:
        shape.fill.gradient_angle = float(angle_deg)
    except (AttributeError, NotImplementedError):
        pass  # angle unsupported on this python-pptx — gradient still applies
    return shape


def add_logo(slide, path: Path, x, y, height):
    if path.exists():
        return slide.shapes.add_picture(str(path), x, y, height=height)
    return None


# --------------------------------------------------------------------------- #
# Deck builder — owns geometry + page numbering
# --------------------------------------------------------------------------- #
class Deck:
    def __init__(self, tokens: dict, event: str = ""):
        self.t = tokens
        self.event = event
        self.prs = Presentation()
        self.prs.slide_width = Inches(tokens["meta"]["slide_width_in"])
        self.prs.slide_height = Inches(tokens["meta"]["slide_height_in"])
        apply_master_theme(self.prs, tokens)
        self.W = self.prs.slide_width
        self.H = self.prs.slide_height
        L = tokens["layout"]
        self.mx = Inches(L["margin_x_in"])
        self.mt = Inches(L["margin_top_in"])
        self.footer_h = Inches(L["footer_height_in"])
        self.rule_h = Inches(L["rule_height_in"])
        self.logo_h = Inches(L["logo_height_in"])
        self.title_logo_h = Inches(L["title_logo_height_in"])
        self.content_w = self.W - 2 * self.mx
        self.slide_index = 0          # absolute 1-based slide position
        self._page_runs = []          # (run, idx) to fill in "idx / total"
        self.dark = bool(tokens.get("_dark"))
        # The title/closing slides sit on a deep brand-blue gradient in BOTH
        # themes, so they take a white horizontal lockup. The footer logo
        # follows the slide background (white slide -> colour, dark -> white).
        self.title_logo = LOGOS / "SDSC_logo_horizontal_rgb_white.png"
        self.footer_logo = (LOGOS / "SDSC_Logo_White.png" if self.dark
                            else LOGOS / "SDSC_Logo_RGB.png")
        # White partner silhouettes sit straight on the gradient (no backing).
        self.partners = [LOGOS / "partners" / f for f in (
            "ETH_Zurich_logo_white.png", "EPFL_logo_white.png",
            "PSI_logo_white.png")]

    def ty(self, name):  # resolved type token
        return _tokens.resolve_type(self.t, name)

    def color(self, name):
        return _tokens.color(self.t, name)

    def _blank(self):
        self.slide_index += 1
        return self.prs.slides.add_slide(self.prs.slide_layouts[6])

    # ---- shared chrome ---------------------------------------------------- #
    def _content_bg(self, slide):
        add_rect(slide, 0, 0, self.W, self.H, self.color("background"))

    def _grad_bg(self, slide):
        g = self.t["gradient"]
        add_gradient_rect(slide, 0, 0, self.W, self.H,
                          g["start"], g["end"], g["angle_deg"])

    def _footer(self, slide):
        """SDSC logo (left) · event name (centre) · page n / total (right)."""
        y = self.H - self.footer_h
        add_logo(slide, self.footer_logo, self.mx, y + Inches(0.12), self.logo_h)
        if self.event:
            add_text(slide, self.mx, y + Inches(0.14), self.content_w, Inches(0.3),
                     [(self.event, self.ty("footer"))], align=PP_ALIGN.CENTER)
        box = add_text(slide, self.W - self.mx - Inches(1.6),
                       y + Inches(0.14), Inches(1.6), Inches(0.3),
                       [(f"{self.slide_index} / 0", self.ty("footer"))],
                       align=PP_ALIGN.RIGHT)
        # Remember the run so save() can fill in the real total.
        self._page_runs.append((box.text_frame.paragraphs[0].runs[0],
                                 self.slide_index))

    def _heading(self, slide, title):
        """Content-slide title (no accent rule). Returns y where content starts."""
        add_text(slide, self.mx, self.mt, self.content_w, Inches(0.7),
                 [(title, self.ty("heading"))])
        return self.mt + Inches(0.95)

    def _icon(self, slide, kind, x, y, size):
        shape = {"hexagon": MSO_SHAPE.HEXAGON, "diamond": MSO_SHAPE.DIAMOND,
                 "target": MSO_SHAPE.OVAL}.get(kind, MSO_SHAPE.OVAL)
        sh = slide.shapes.add_shape(shape, x, y, size, size)
        sh.shadow.inherit = False
        if kind == "diamond":
            sh.fill.solid(); sh.fill.fore_color.rgb = rgb(self.color("primary"))
            sh.line.fill.background()
        else:
            sh.fill.background()
            sh.line.color.rgb = rgb(self.color("primary")); sh.line.width = Pt(1.5)
        if kind == "target":  # filled centre dot
            inner = size // 2
            dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, x + inner // 2,
                                         y + inner // 2, inner, inner)
            dot.shadow.inherit = False
            dot.fill.solid(); dot.fill.fore_color.rgb = rgb(self.color("primary"))
            dot.line.fill.background()

    # ---- slide types ------------------------------------------------------ #
    def title(self, title, subtitle, meta):
        slide = self._blank()
        self._grad_bg(slide)
        add_logo(slide, self.title_logo, self.mx, Inches(0.55), self.title_logo_h)
        add_text(slide, self.mx, Inches(3.3), self.content_w, Inches(1.0),
                 [(title, self.ty("title"))])
        add_text(slide, self.mx, Inches(4.35), self.content_w, Inches(0.5),
                 [(subtitle, self.ty("subtitle"))])
        add_text(slide, self.mx, Inches(5.1), self.content_w, Inches(0.4),
                 [(meta, self.ty("meta"))])
        return slide

    def section(self, number, title, desc):
        slide = self._blank()
        add_rect(slide, 0, 0, self.W, self.H, self.color("light_blue_bg"))
        add_text(slide, self.mx, Inches(2.3), self.content_w, Inches(1.3),
                 [(f"{number:02d}", self.ty("section_number"))])
        add_text(slide, self.mx, Inches(3.85), self.content_w, Inches(0.9),
                 [(title, self.ty("section_title"))])
        add_text(slide, self.mx, Inches(4.8), Inches(7.5), Inches(0.9),
                 [(desc, self.ty("section_desc"))], line_spacing=1.3)
        return slide

    def content(self, title, body=None, bullets=None, takeaway=None):
        slide = self._blank()
        self._content_bg(slide)
        y = self._heading(slide, title)
        if body:
            box = add_text(slide, self.mx, y, self.content_w, Inches(0.9),
                           [(body, self.ty("body"))], line_spacing=1.3)
            y += Inches(0.95)
        if bullets:
            add_bullets(slide, self.mx + Inches(0.1), y, self.content_w - Inches(0.1),
                        Inches(2.2), bullets, self.ty("bullet"),
                        marker_hex=self.color("primary"))
            y += Inches(0.5) * len(bullets) + Inches(0.1)
        if takeaway:
            self._takeaway(slide, y, takeaway)
        self._footer(slide)
        return slide

    def _takeaway(self, slide, y, text):
        h = Inches(0.6)
        add_rect(slide, self.mx, y, self.content_w, h, self.color("background_alt"))
        add_rect(slide, self.mx, y, Inches(0.06), h, self.color("accent_green"))
        add_text(slide, self.mx + Inches(0.25), y, self.content_w - Inches(0.4), h,
                 [(text, self.ty("takeaway"))], anchor=MSO_ANCHOR.MIDDLE)

    def two_column(self, title, left, right):
        """left/right: dicts with optional keys head, body, items, code."""
        slide = self._blank()
        self._content_bg(slide)
        top = self._heading(slide, title)
        gap = Inches(0.6)
        col_w = (self.content_w - gap) / 2
        for cx, col in ((self.mx, left), (self.mx + col_w + gap, right)):
            y = top
            if col.get("head"):
                add_text(slide, cx, y, col_w, Inches(0.5),
                         [(col["head"], self.ty("column_head"))])
                y += Inches(0.65)
            if col.get("body"):
                add_text(slide, cx, y, col_w, Inches(0.9),
                         [(col["body"], self.ty("body"))], line_spacing=1.25)
                y += Inches(1.0)
            if col.get("items"):
                add_bullets(slide, cx + Inches(0.1), y, col_w - Inches(0.1),
                            Inches(1.8), col["items"], self.ty("bullet"),
                            marker_hex=self.color("primary"))
            if col.get("code"):
                self._code_box(slide, cx, y, col_w, Inches(2.0), col["code"])
        self._footer(slide)
        return slide

    def feature_grid(self, title, features):
        """features: list of dicts {icon, title, desc} (2-4)."""
        slide = self._blank()
        self._content_bg(slide)
        top = self._heading(slide, title) + Inches(0.2)
        n = len(features)
        gap = Inches(0.35)
        card_w = (self.content_w - gap * (n - 1)) / n
        card_h = Inches(2.5)
        for i, f in enumerate(features):
            cx = self.mx + i * (card_w + gap)
            add_rect(slide, cx, top, card_w, card_h, self.color("background"),
                     line_hex=self.color("border"), line_pt=0.75)
            add_rect(slide, cx, top, card_w, Inches(0.06), self.color("secondary"))
            pad = Inches(0.28)
            self._icon(slide, f.get("icon", "target"), cx + pad,
                       top + Inches(0.32), Inches(0.34))
            add_text(slide, cx + pad, top + Inches(0.85), card_w - 2 * pad,
                     Inches(0.4), [(f["title"], self.ty("feature_title"))])
            add_text(slide, cx + pad, top + Inches(1.3), card_w - 2 * pad,
                     card_h - Inches(1.4), [(f["desc"], self.ty("feature_desc"))],
                     line_spacing=1.25)
        self._footer(slide)
        return slide

    def key_numbers(self, title, stats):
        """stats: list of (number, label) — equal columns, green top rule."""
        slide = self._blank()
        self._content_bg(slide)
        top = self._heading(slide, title) + Inches(0.3)
        n = len(stats)
        gap = Inches(0.5)
        col_w = (self.content_w - gap * (n - 1)) / n
        for i, (num, lab) in enumerate(stats):
            cx = self.mx + i * (col_w + gap)
            add_rect(slide, cx, top, col_w, self.rule_h, self.color("accent_green"))
            add_text(slide, cx, top + Inches(0.2), col_w, Inches(1.1),
                     [(num, self.ty("kpi_number"))])
            add_text(slide, cx, top + Inches(1.35), col_w, Inches(0.6),
                     [(lab, self.ty("kpi_label"))])
        self._footer(slide)
        return slide

    def _code_box(self, slide, x, y, w, h, code):
        add_rect(slide, x, y, w, h, self.color("background_alt"))
        lines = code.split("\n")
        add_text(slide, x + Inches(0.2), y + Inches(0.12), w - Inches(0.3),
                 h - Inches(0.2),
                 [(ln or " ", self.ty("code"), 2) for ln in lines],
                 line_spacing=1.2)

    def code(self, title, body, code):
        slide = self._blank()
        self._content_bg(slide)
        y = self._heading(slide, title)
        if body:
            add_text(slide, self.mx, y, self.content_w, Inches(0.6),
                     [(body, self.ty("body"))])
            y += Inches(0.7)
        self._code_box(slide, self.mx, y, self.content_w,
                       self.H - y - self.footer_h - Inches(0.2), code)
        self._footer(slide)
        return slide

    def findings(self, title, quote, attribution, narrative):
        slide = self._blank()
        self._content_bg(slide)
        y = self._heading(slide, title)
        band_h = Inches(1.7)
        add_rect(slide, self.mx, y, self.content_w, band_h,
                 self.color("background_alt"))
        add_rect(slide, self.mx, y, Inches(0.08), band_h, self.color("secondary"))
        qx = self.mx + Inches(0.4)
        add_text(slide, qx, y + Inches(0.25), self.content_w - Inches(0.7),
                 Inches(0.9), [(f"“{quote}”", self.ty("quote"))],
                 line_spacing=1.25)
        add_text(slide, qx, y + band_h - Inches(0.5), self.content_w - Inches(0.7),
                 Inches(0.4), [(f"— {attribution}", self.ty("quote_attr"))])
        add_text(slide, self.mx, y + band_h + Inches(0.35), self.content_w,
                 Inches(1.0), [(narrative, self.ty("body"))], line_spacing=1.3)
        self._footer(slide)
        return slide

    def banner(self, banner_title, banner_text, body):
        slide = self._blank()
        self._content_bg(slide)
        by = Inches(1.4)
        bh = Inches(1.9)
        add_rect(slide, self.mx, by, self.content_w, bh, self.color("light_blue_bg"))
        add_rect(slide, self.mx, by, Inches(0.08), bh, self.color("secondary"))
        add_text(slide, self.mx, by + Inches(0.35), self.content_w, Inches(0.6),
                 [(banner_title, self.ty("banner_title"))], align=PP_ALIGN.CENTER)
        add_text(slide, self.mx + Inches(1.5), by + Inches(1.0),
                 self.content_w - Inches(3.0), Inches(0.8),
                 [(banner_text, self.ty("banner_text"))],
                 align=PP_ALIGN.CENTER, line_spacing=1.25)
        add_text(slide, self.mx, by + bh + Inches(0.4), self.content_w, Inches(0.6),
                 [(body, self.ty("body"))])
        self._footer(slide)
        return slide

    def palette(self, title, body, swatches, notes):
        """swatches: list of (hex, name, dark_text?); notes: list of (head, text).

        The swatch colours are the sdsc-plotting DATA palette, passed in as
        content — they are not brand tokens. This slide just shows how to
        present that palette on a deck."""
        slide = self._blank()
        self._content_bg(slide)
        y = self._heading(slide, title)
        add_text(slide, self.mx, y, self.content_w, Inches(0.6),
                 [(body, self.ty("body"))], line_spacing=1.3)
        sy = y + Inches(0.9)
        n = len(swatches)
        gap = Inches(0.18)
        sw = (self.content_w - gap * (n - 1)) / n
        sh = Inches(1.0)
        for i, item in enumerate(swatches):
            hex_value, name = item[0], item[1]
            dark_text = item[2] if len(item) > 2 else False
            sx = self.mx + i * (sw + gap)
            add_rect(slide, sx, sy, sw, sh, hex_value)
            txt = "#000000" if dark_text else "#FFFFFF"
            add_text(slide, sx + Inches(0.12), sy + Inches(0.12), sw - Inches(0.2),
                     sh - Inches(0.2),
                     [(hex_value, {**self.ty("caption"), "color": txt, "bold": True}, 1),
                      (name, {**self.ty("caption"), "color": txt})])
        ny = sy + sh + Inches(0.4)
        col_w = (self.content_w - Inches(0.6)) / 2
        for i, (head, text) in enumerate(notes):
            nx = self.mx + i * (col_w + Inches(0.6))
            add_text(slide, nx, ny, col_w, Inches(0.4),
                     [(head, {**self.ty("body"), "bold": True,
                              "color": self.color("content_heading")})])
            add_text(slide, nx, ny + Inches(0.45), col_w, Inches(0.9),
                     [(text, self.ty("caption"))], line_spacing=1.3)
        self._footer(slide)
        return slide

    def closing(self, title, contact_lines):
        slide = self._blank()
        self._grad_bg(slide)
        add_logo(slide, self.title_logo, self.mx, Inches(0.55), self.title_logo_h)
        add_text(slide, self.mx, Inches(2.6), self.content_w, Inches(1.0),
                 [(title, self.ty("title"))])
        paras = []
        for i, line in enumerate(contact_lines):
            style = ({**self.ty("meta"), "color": self.color("text_on_dark"),
                      "weight": "regular", "bold": False} if i == 0
                     else self.ty("meta"))
            paras.append((line, style, 3))
        add_text(slide, self.mx, Inches(3.7), self.content_w, Inches(1.2), paras)
        # White partner silhouettes, bottom-left on the gradient (no band).
        logo_h = Inches(0.36)
        x = self.mx
        y = self.H - Inches(1.0)
        for path in self.partners:
            pic = add_logo(slide, path, x, y, logo_h)
            if pic is not None:
                x = pic.left + pic.width + Inches(0.5)
        return slide

    def _finalize(self):
        total = self.slide_index
        for run, idx in self._page_runs:
            run.text = f"{idx} / {total}"

    def save(self, path: Path):
        self._finalize()
        self.prs.save(str(path))


# --------------------------------------------------------------------------- #
# Example content — public/mock data only (org data-handling rules).
# --------------------------------------------------------------------------- #
def build_example(deck: Deck) -> None:
    deck.title(
        "Presentation Title",
        "Subtitle or tagline goes here",
        "Author Name  ·  2026-06-16  ·  Event or Venue")
    deck.section(
        1, "Introduction & Context",
        "A brief description of what this section covers and why it matters to "
        "the audience.")
    deck.content(
        "Slide Title",
        body="Body text uses Switzer at 18 pt with generous line-height for "
             "readability. Keep slides focused — one key idea per slide works best.",
        bullets=["First bullet point with supporting detail",
                 "Second point — pair colour with labels, never rely on colour alone",
                 "Third point — use metric units and ISO-8601 dates (2026-06-16)"],
        takeaway="Key takeaway or highlighted statement goes here.")
    deck.two_column(
        "Two-Column Layout",
        {"head": "Left Column",
         "body": "Use this column for the main explanation, context, or "
                 "narrative. Keep it concise — 3-4 sentences max per column.",
         "items": ["Point one", "Point two", "Point three"]},
        {"head": "Right Column",
         "body": "Charts, code snippets, diagrams, or a supporting visual go here.",
         "code": '# Example: SDSC chart palette\n'
                 'SDSC_CATEGORICAL = [\n'
                 '    "#26245c",  # Dark Blue\n'
                 '    "#73a235",  # Green\n'
                 '    "#b34a00",  # Orange\n'
                 '    "#56b4e9",  # Sky Blue\n'
                 '    "#cc79a7",  # Pink\n'
                 ']'})
    deck.feature_grid(
        "Three-Column Feature Grid",
        [{"icon": "hexagon", "title": "Feature One",
          "desc": "Short description of this capability or result. Keep it to two "
                  "sentences maximum."},
         {"icon": "diamond", "title": "Feature Two",
          "desc": "Short description of this capability or result. Keep it to two "
                  "sentences maximum."},
         {"icon": "target", "title": "Feature Three",
          "desc": "Short description of this capability or result. Keep it to two "
                  "sentences maximum."}])
    deck.key_numbers(
        "Key Numbers",
        [("250+", "Projects completed"), ("42", "Partner institutions"),
         ("98%", "Reproducibility rate"), ("3.2×", "Speed improvement")])
    deck.section(
        2, "Results & Analysis",
        "Summary of what this section demonstrates, framed around the key "
        "finding or takeaway for the audience.")
    deck.code(
        "Code Example",
        "Apply the SDSC Matplotlib theme once at import time; individual plots "
        "inherit it automatically.",
        'import matplotlib as mpl\n\n'
        'SDSC_CATEGORICAL = ["#26245c", "#73a235", "#b34a00", "#56b4e9", "#cc79a7"]\n\n'
        'mpl.rcParams.update({\n'
        '    "axes.prop_cycle": mpl.cycler(color=SDSC_CATEGORICAL),\n'
        '    "image.cmap":      "viridis",\n'
        '    "axes.spines.top":   False,\n'
        '    "axes.spines.right": False,\n'
        '    "font.family":     "Switzer",\n'
        '    "figure.dpi":      150,\n'
        '})')
    # The swatch colours below are the sdsc-plotting DATA palette (content),
    # NOT brand tokens — a deck colours charts with sdsc-plotting.
    deck.palette(
        "Chart Color Palette",
        "Use in this order — chosen so the first colours are the most "
        "distinguishable. Always pair colour with a redundant encoding.",
        [("#26245C", "Dark Blue · primary"), ("#73A235", "Green"),
         ("#B34A00", "Orange"), ("#56B4E9", "Sky Blue", True),
         ("#CC79A7", "Pink"), ("#B8B8B8", "Muted", True)],
        [("Sequential", "Shades of #26245c — use for ordered categories "
                        "(quintiles, ratings)."),
         ("Continuous", "viridis / batlow / cividis. Never use rainbow/jet — it "
                        "creates false boundaries.")])
    deck.findings(
        "Findings",
        "Model B converges 2× faster on all five benchmark datasets, while "
        "maintaining equivalent out-of-sample accuracy.",
        "Smith et al. (2026), ICML proceedings",
        "Supporting narrative that contextualises the quote. Reference specific "
        "figures, tables, or supplementary material as needed.")
    deck.banner(
        "Call to Action or Key Message",
        "Use this banner component to emphasise a single important takeaway, "
        "next step, or CTA on any standard content slide.",
        "Additional body copy or bullets continue below the banner as normal.")
    deck.closing(
        "Questions?",
        ["Author Name", "author@datascience.ch", "datascience.ch"])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-o", "--output", default="SDSC_Slides_Template.pptx",
                    help="output .pptx path")
    ap.add_argument("--tokens", default=None,
                    help="path to tokens.toml (defaults to ../references)")
    ap.add_argument("--dark", action="store_true",
                    help="build the dark theme (applies the [dark] overrides)")
    ap.add_argument("--event", default="",
                    help="deck/event name shown centred in the footer (empty = none)")
    args = ap.parse_args()

    tokens = _tokens.load(args.tokens, dark=args.dark)
    deck = Deck(tokens, event=args.event)
    build_example(deck)
    out = Path(args.output)
    deck.save(out)
    print(f"  wrote {out}  ({len(deck.prs.slides._sldIdLst)} slides, "
          f"{'dark' if args.dark else 'light'} theme, "
          f"{deck.prs.slide_width.inches:g}x{deck.prs.slide_height.inches:g} in)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
