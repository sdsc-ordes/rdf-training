# Building the Slidev deck

[Slidev](https://sli.dev) renders a deck from a single `slides.md`. The SDSC look
comes from a `style.css` generated out of `references/tokens.toml`, so the
Markdown deck and the PowerPoint template share one source of truth.

## Scaffold a project

```bash
# 1. Create the project (or use an existing folder with a slides.md).
npm create slidev@latest my-sdsc-deck
cd my-sdsc-deck

# 2. Generate the SDSC theme into the project root. Slidev auto-loads ./style.css.
uv run /path/to/skill/scripts/build_slidev_theme.py -o style.css
#    (or copy the pre-generated assets/slidev/style.css)

# 3. Add the footer component + logos (see "Footer" and "Logos" below):
cp /path/to/skill/assets/slidev/global-bottom.vue .
mkdir -p public/partners
cp /path/to/skill/assets/logos/SDSC_Logo_RGB.png public/
cp /path/to/skill/assets/logos/SDSC_Logo_White.png public/
cp /path/to/skill/assets/logos/SDSC_logo_horizontal_rgb_white.png public/
cp /path/to/skill/assets/logos/partners/*.png public/partners/

# 4. Author slides.md, then preview / build / export:
npx slidev                     # live preview — press `d` to toggle dark mode
npx slidev build --base /x/    # static site -> dist/
npx slidev export --per-slide  # PDF/PNG (needs playwright-chromium; --dark for dark)
```

`build_slidev_theme.py` has **no third-party dependencies** (stdlib `tomllib`),
so `uv run` it from anywhere; pass `--tokens` to theme from a different TOML.

## How the theme works

The generated `style.css` has three parts:

1. a `:root` block of `--sdsc-*` CSS variables — the colours, font stacks, and
   gradient, written straight from `tokens.toml`;
2. an `html.dark { … }` block overriding the variables that change in dark mode
   (from the `[dark]` table) — Slidev toggles `html.dark`, so set
   `colorSchema: dark` in the headmatter to force it; and
3. a stable block of layout CSS that *references* those variables: body/heading
   fonts, ring bullets, inline-code chips and code blocks, the `.cover` and
   `.section` layouts, and the helper classes `.sdsc-meta`, `.sdsc-section-num`,
   `.sdsc-takeaway`, `.sdsc-features`/`.sdsc-feature`, `.sdsc-kpis`/`.sdsc-kpi`,
   `.sdsc-banner`, `.sdsc-swatches`, blockquote bands, `.sdsc-cover-logo`,
   `.sdsc-contact`, `.sdsc-footer`, and `.sdsc-partners`.

Re-theme by editing `tokens.toml` and re-running the builder — never hand-edit
`style.css` (it is regenerated and carries a "do not edit" header).

## Footer

`global-bottom.vue` (copy it to the project root) draws the SDSC logo (left) and
the page number `n / total` (right) at the bottom of **content** slides, and
hides itself on the cover, section, quote, and closing layouts. An optional
centred deck/event name comes from a `footer:` field in the deck headmatter (the
first slide's frontmatter); leave it unset (as the example does) to hide it. It reads the live
navigation state (`useNav()`), so the page number is correct when presenting and
in the SPA. The all-in-one `slidev export` shares one nav state across pages —
use `slidev export --per-slide` for correct per-slide page numbers in a PDF. The
footer logo swaps colour → white in dark mode via the `.sdsc-footer` CSS. There
is no divider line above the footer.

## Logos

Put these in `public/` (referenced with root-absolute paths):

- `SDSC_logo_horizontal_rgb_white.png` — the cover + closing logo
  (`<img class="sdsc-cover-logo" src="/SDSC_logo_horizontal_rgb_white.png" />`);
- `SDSC_Logo_RGB.png` + `SDSC_Logo_White.png` — the footer logo (light / dark);
- `partners/ETH_Zurich_logo_white.png`, `partners/EPFL_logo_white.png`,
  `partners/PSI_logo_white.png` — the white partner silhouettes for the
  closing-slide `.sdsc-partners` band (they sit straight on the gradient).

## Fonts

The CSS `@import`s Space Grotesk (Google Fonts) and Switzer (Fontshare), so they
load in the browser with no extra config. You can also declare them in the deck
headmatter for Slidev's font optimisation:

```yaml
fonts:
  sans: Switzer
  serif: Switzer
  mono: 'Fira Code'
# Space Grotesk is applied to headings via style.css.
```

## SDSC layouts in `slides.md`

Map each slide to an SDSC layout (full details + copy-paste blocks in
`layouts.md`):

| Slide | Headmatter / markup |
|-------|---------------------|
| Title | `layout: cover` + `.sdsc-cover-logo` + `#` + tagline + `.sdsc-meta` (optional `footer:`) |
| Section divider | `layout: section` + `.sdsc-section-num` + `#` + description |
| Content | `layout: default`, `#` heading, bullets, optional `.sdsc-takeaway` |
| Two-column | `layout: two-cols-header`, `#` + `::left::` / `::right::` |
| Feature grid | `.sdsc-features` of `.sdsc-feature` cards |
| Key numbers | a `.sdsc-kpis` row of `.sdsc-kpi` blocks |
| Code | `#` heading + a fenced ```` ```python ```` block |
| Quote / findings | `#` heading + a `>` blockquote band + narrative |
| CTA banner | a `.sdsc-banner` block |
| Closing | `layout: cover` + `.sdsc-cover-logo` + `.sdsc-contact` + `.sdsc-partners` |

Example title slide (no text eyebrow — the logo carries the wordmark):

```md
---
theme: default
layout: cover
# footer: My Event   # optional — sets the centred footer text on content slides
---
<img class="sdsc-cover-logo" src="/SDSC_logo_horizontal_rgb_white.png" alt="Swiss Data Science Center" />

# Presentation Title

Subtitle or tagline goes here

<div class="sdsc-meta">Author Name · 2026-06-16 · Event or Venue</div>
```

## Charts on a slide

Slidev renders Mermaid, code, and embedded images. When a slide carries a chart,
colour that chart with the **sdsc-plotting** palette (its colours encode data);
keep the surrounding slide chrome — headings, footer, KPI rule — in the SDSC
brand colours from this skill. Do not mix the two roles. The **Chart Color
Palette** slide in the example deck shows how to *present* the sdsc-plotting
palette on a slide (the swatch colours are that data palette, not brand tokens).

## Tips

- The footer is the `global-bottom.vue` component, not a theme slot; the
  cover/section/quote/closing layouts suppress it automatically.
- Keep one idea per slide and ≤ ~5 bullets, exactly as in PowerPoint.
- Commit `slides.md`, `style.css`, `global-bottom.vue`, and `public/`; `dist/`
  and `node_modules/` are build artefacts.
