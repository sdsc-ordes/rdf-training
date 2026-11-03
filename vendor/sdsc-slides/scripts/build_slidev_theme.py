# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Generate a Slidev `style.css` from references/tokens.toml.

Same single source of truth as the PowerPoint builder (_tokens.py): the colours
and fonts come straight from the TOML, so a designer retheming the deck edits one
file and re-runs both builders. Slidev auto-loads a `style.css` placed in a
project root, so the output drops in with no further wiring.

No third-party dependencies (stdlib `tomllib`).

Usage (from the skill root):
    uv run scripts/build_slidev_theme.py                 # -> ./style.css
    uv run scripts/build_slidev_theme.py -o examples/.../style.css
"""

from __future__ import annotations

import argparse
from pathlib import Path

import _tokens

# @import rules MUST come before any other CSS rule (the :root vars below), or
# browsers drop them and the fonts never load. So fonts are emitted first.
FONT_IMPORTS = """\
/* Fonts: Space Grotesk (Google Fonts) + Switzer (Fontshare) + Fira Code (mono). */
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');
@import url('https://api.fontshare.com/v2/css?f[]=switzer@400,500,600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&display=swap');
"""

# Static CSS that references the generated variables. Kept stable; only the
# variable values change when tokens.toml changes.
STATIC_CSS = """
:root {
  --slidev-theme-primary: var(--sdsc-primary);
}

/* Body + headings ---------------------------------------------------------- */
.slidev-layout {
  font-family: var(--sdsc-font-body);
  color: var(--sdsc-text);
  background: var(--sdsc-background);
  padding: 2.2rem 2.6rem;
}
.slidev-layout h1,
.slidev-layout h2,
.slidev-layout h3,
.slidev-layout h4 {
  font-family: var(--sdsc-font-heading);
  font-weight: 600;
  color: var(--sdsc-content-heading);
  letter-spacing: -0.01em;
}
.slidev-layout h1 { font-size: 1.9rem; line-height: 1.15; margin-bottom: 0.8rem; }
.slidev-layout h2 { font-size: 1.25rem; line-height: 1.2; }
.slidev-layout p { line-height: 1.55; }
.slidev-layout a { color: var(--sdsc-primary); text-decoration: none; }
.slidev-layout a:hover { color: var(--sdsc-content-heading); }

/* Bullets — a hollow Primary ring marker, never relying on colour alone. */
.slidev-layout ul { list-style: none; padding-left: 0.4rem; margin: 0.6rem 0; }
.slidev-layout ul > li {
  position: relative; padding-left: 1.7rem; margin: 0.45rem 0; line-height: 1.5;
}
.slidev-layout ul > li::before {
  content: ""; position: absolute; left: 0.15rem; top: 0.45em;
  width: 0.62rem; height: 0.62rem; border-radius: 50%;
  border: 2px solid var(--sdsc-primary); box-sizing: border-box;
}

/* Inline code chip + code blocks. Set a light Shiki theme in the deck
   headmatter (e.g. `themes: { light: 'github-light' }`) so tokens read on the
   pale fill; this rule owns the container background, padding, and radius. */
.slidev-layout :not(pre) > code {
  font-family: var(--sdsc-font-mono); font-size: 0.85em;
  background: var(--sdsc-light-blue-bg); color: var(--sdsc-content-heading);
  padding: 0.08em 0.4em; border-radius: 0.25rem;
}
.slidev-layout pre {
  background: var(--sdsc-background-alt) !important;
  border-radius: 0.4rem; padding: 1rem 1.2rem !important;
  font-family: var(--sdsc-font-mono); font-size: 0.78rem; line-height: 1.5;
}
.slidev-layout pre code { font-family: var(--sdsc-font-mono); }

/* Cover + closing logo, pinned top-left (the wordmark — no text eyebrow). */
.sdsc-cover-logo { position: absolute; top: 2rem; left: 2.6rem; height: 0.85rem; }

/* Cover + closing: brand-blue gradient, white type, content centred. */
.slidev-layout.cover,
.slidev-layout.intro {
  background: linear-gradient(var(--sdsc-grad-angle),
              var(--sdsc-grad-start), var(--sdsc-grad-end));
  color: var(--sdsc-text-on-dark);
  display: flex; flex-direction: column; justify-content: center;
  padding: 2.6rem 3rem;
}
.slidev-layout.cover h1,
.slidev-layout.intro h1 {
  color: var(--sdsc-text-on-dark); font-size: 2.9rem; line-height: 1.05;
  margin: 0 0 0.5rem;
}
/* Cover tagline (periwinkle) + meta line (muted) on the gradient. */
.slidev-layout.cover p,
.slidev-layout.intro p { color: var(--sdsc-primary-light); font-size: 1.15rem; margin: 0; }
.sdsc-meta {
  color: var(--sdsc-text-on-dark-muted); font-size: 0.82rem;
  letter-spacing: 0.02em; margin-top: 1.7rem;
}

/* Closing-specific: contact lines + bottom-left partner band (white logos
   straight on the gradient — no backing band). */
.sdsc-contact { margin-top: 1.4rem; }
.sdsc-contact p { margin: 0.12rem 0; font-size: 0.85rem; color: var(--sdsc-text-on-dark-muted); }
.sdsc-contact .sdsc-contact-name { color: var(--sdsc-text-on-dark); font-weight: 500; }
.sdsc-partners {
  position: absolute; bottom: 2rem; left: 3rem;
  display: flex; align-items: center; gap: 1.8rem;
}
.sdsc-partners img { height: 1.25rem; }

/* Section divider — pale lavender panel, big lavender numeral.
   The default theme centres the section slot; left-align it for the SDSC look. */
.slidev-layout.section {
  background: var(--sdsc-light-blue-bg);
  color: var(--sdsc-text);
  display: flex; flex-direction: column; justify-content: center;
  padding: 2.6rem 3rem;
}
.slidev-layout.section > div { width: 100%; text-align: left; }
.slidev-layout.section .sdsc-section-num {
  font-family: var(--sdsc-font-heading); font-weight: 600; font-size: 5rem;
  line-height: 1; color: var(--sdsc-primary-light); margin-bottom: 0.4rem;
}
.slidev-layout.section h1 {
  color: var(--sdsc-content-heading); font-size: 2.5rem; margin: 0 0 0.7rem;
}
.slidev-layout.section p {
  color: var(--sdsc-text-grey); font-size: 1rem; max-width: 38rem; margin: 0;
}

/* Two-column header layout: full-width title, then two columns. */
.slidev-layout.two-cols-header h2,
.slidev-layout.two-cols h2 { margin: 0 0 0.6rem; }

/* Feature grid — equal cards, Secondary top rule, Primary icon. */
.sdsc-features { display: grid; grid-auto-flow: column; grid-auto-columns: 1fr; gap: 1.4rem; margin-top: 1.4rem; }
.sdsc-feature {
  background: var(--sdsc-background);
  border: 1px solid var(--sdsc-border);
  border-top: 0.18rem solid var(--sdsc-secondary);
  padding: 1.1rem 1.2rem 1.3rem;
}
.sdsc-feature .sdsc-feature-icon { color: var(--sdsc-primary); margin-bottom: 0.8rem; }
.sdsc-feature .sdsc-feature-icon svg { width: 1.5rem; height: 1.5rem; }
.sdsc-feature h3 { font-size: 1.02rem; margin: 0 0 0.45rem; color: var(--sdsc-content-heading); }
.sdsc-feature p { font-size: 0.84rem; line-height: 1.5; margin: 0; color: var(--sdsc-text); }

/* Key numbers — equal columns, green top rule, big Secondary numeral. */
.sdsc-kpis { display: flex; gap: 1.6rem; margin-top: 1.4rem; }
.sdsc-kpi {
  flex: 1; border-top: 0.16rem solid var(--sdsc-accent-green); padding-top: 0.9rem;
}
.sdsc-kpi b {
  display: block; font-family: var(--sdsc-font-heading); font-weight: 600;
  font-size: 3rem; color: var(--sdsc-content-heading); line-height: 1;
}
.sdsc-kpi span { display: block; font-size: 0.9rem; color: var(--sdsc-text-grey); margin-top: 0.5rem; }

/* Quote / findings band — alt fill, Secondary left edge, attribution inside. */
.slidev-layout blockquote {
  background: var(--sdsc-background-alt);
  border-left: 0.28rem solid var(--sdsc-secondary);
  padding: 1.1rem 1.4rem; margin: 1.1rem 0; quotes: none;
}
.slidev-layout blockquote p {
  font-family: var(--sdsc-font-heading); color: var(--sdsc-content-heading);
  font-size: 1.25rem; line-height: 1.4; margin: 0;
}
.slidev-layout blockquote p + p { margin-top: 0.6rem; }
.slidev-layout blockquote .sdsc-quote-cite {
  font-family: var(--sdsc-font-body); color: var(--sdsc-text-grey); font-size: 0.85rem;
}

/* Key-takeaway highlight band — alt fill, thin green left edge. */
.sdsc-takeaway {
  background: var(--sdsc-background-alt);
  border-left: 0.22rem solid var(--sdsc-accent-green);
  padding: 0.7rem 1rem; margin: 0.9rem 0; font-size: 0.95rem;
}

/* CTA / key-message banner — lavender fill, Secondary left edge, centred. */
.sdsc-banner {
  background: var(--sdsc-light-blue-bg);
  border-left: 0.32rem solid var(--sdsc-secondary);
  padding: 1.5rem 2rem; margin: 0.4rem 0 1.4rem; text-align: center;
}
.sdsc-banner h2 { color: var(--sdsc-content-heading); font-size: 1.5rem; margin: 0 0 0.5rem; }
.sdsc-banner p { color: var(--sdsc-text); font-size: 0.95rem; margin: 0 auto; max-width: 82%; }

/* Colour-swatch row (e.g. illustrating the sdsc-plotting palette ON a slide). */
.sdsc-swatches { display: flex; gap: 0.7rem; margin: 1.2rem 0; }
.sdsc-swatch {
  flex: 1; border-radius: 0.3rem; padding: 0.7rem 0.8rem; min-height: 3rem;
  font-family: var(--sdsc-font-mono); font-size: 0.72rem; line-height: 1.35;
}
.sdsc-swatch b { display: block; font-weight: 600; }

/* Persistent footer (rendered by global-bottom.vue) — SDSC logo, centred deck
   name, page "n / total", on content slides only. Logo swaps -> white in dark. */
.sdsc-footer {
  position: absolute; bottom: 0; left: 0; right: 0; z-index: 10;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0.5rem 2.6rem;
}
.sdsc-footer img { height: 0.95rem; }
.sdsc-footer .sdsc-logo-dark { display: none; }
html.dark .sdsc-footer .sdsc-logo-light { display: none; }
html.dark .sdsc-footer .sdsc-logo-dark { display: inline; }
.sdsc-footer-event {
  position: absolute; left: 0; right: 0; text-align: center; pointer-events: none;
  font-family: var(--sdsc-font-body); font-size: 0.72rem; color: var(--sdsc-text-grey);
}
.sdsc-footer-page {
  font-family: var(--sdsc-font-body); font-size: 0.72rem; color: var(--sdsc-text-grey);
}

/* Built-in Slidev page number (used on slides without the custom footer). */
.slidev-page-number { color: var(--sdsc-text-grey); font-family: var(--sdsc-font-body); }
"""

# Colour token key -> CSS variable name.
COLOR_VARS = {
    "primary": "--sdsc-primary",
    "primary_light": "--sdsc-primary-light",
    "secondary": "--sdsc-secondary",
    "background": "--sdsc-background",
    "background_alt": "--sdsc-background-alt",
    "background_dark": "--sdsc-background-dark",
    "text": "--sdsc-text",
    "text_grey": "--sdsc-text-grey",
    "text_on_dark": "--sdsc-text-on-dark",
    "text_on_dark_muted": "--sdsc-text-on-dark-muted",
    "border": "--sdsc-border",
    "accent_green": "--sdsc-accent-green",
    "light_blue_bg": "--sdsc-light-blue-bg",
    "content_heading": "--sdsc-content-heading",
}


def _gradient_vars(grad: dict) -> list[str]:
    return [
        f"  --sdsc-grad-start: {grad['start']};",
        f"  --sdsc-grad-end: {grad['end']};",
        f"  --sdsc-grad-angle: {grad['angle_deg']}deg;",
    ]


def render(tokens: dict) -> str:
    # Loaded light (dark=False), so `colors` are the light values and the
    # [dark] table is still available for the html.dark override block.
    colors, fonts = tokens["colors"], tokens["fonts"]
    dark = tokens.get("dark", {})
    dark_scalars = {k: v for k, v in dark.items() if not isinstance(v, dict)}

    lines = [
        "/* SDSC Slides — Slidev theme.",
        f" * Generated from tokens.toml ({tokens['meta']['name']}). DO NOT edit by",
        " * hand — change references/tokens.toml and re-run build_slidev_theme.py.",
        " * Supports light + dark (Slidev toggles html.dark; set `colorSchema:",
        " * dark` in the deck headmatter to force it).",
        " */",
        FONT_IMPORTS,
        ":root {",
        f'  --sdsc-font-heading: "{fonts["heading"]}", "{fonts["heading_fallback"]}", sans-serif;',
        f'  --sdsc-font-body: "{fonts["body"]}", "{fonts["body_fallback"]}", sans-serif;',
        f'  --sdsc-font-mono: "{fonts["mono"]}", "{fonts["mono_fallback"]}", monospace;',
    ]
    for key, var in COLOR_VARS.items():
        lines.append(f"  {var}: {colors[key]};")
    lines += _gradient_vars(tokens["gradient"])
    lines.append("}")

    if dark_scalars or "gradient" in dark:
        lines.append("html.dark {")
        for key, var in COLOR_VARS.items():
            if key in dark_scalars:
                lines.append(f"  {var}: {dark_scalars[key]};")
        if "gradient" in dark:
            lines += _gradient_vars(dark["gradient"])
        lines.append("}")

    return "\n".join(lines) + "\n" + STATIC_CSS


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-o", "--output", default="style.css",
                    help="output CSS path (Slidev auto-loads ./style.css)")
    ap.add_argument("--tokens", default=None,
                    help="path to tokens.toml (defaults to ../references)")
    args = ap.parse_args()

    tokens = _tokens.load(args.tokens)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(tokens))
    print(f"  wrote {out}  ({len(COLOR_VARS)} colour vars + SDSC layout styles)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
