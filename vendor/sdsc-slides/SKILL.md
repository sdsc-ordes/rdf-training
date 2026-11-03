---
name: sdsc-slides
description: >-
  Use this skill when creating slide decks or presentation templates for the
  Swiss Data Science Center (SDSC / datascience.ch) — building a branded
  PowerPoint (.pptx) template with python-pptx, or a Markdown-based deck with
  Slidev, using the SDSC brand colours, the Space Grotesk + Switzer type pairing,
  and the standard slide layouts (title, section, content, two-column, feature
  grid, key numbers, code, quote, CTA banner, closing). Use when the user asks to make an SDSC presentation,
  slide template, pptx, or Slidev deck. All design values come from one
  references/tokens.toml so designers retheme by editing a single file. Do not
  use for web UI (use sdsc-ui-kit) or for the colours inside a chart (use
  sdsc-plotting).
---

# SDSC Slides

Build SDSC-branded presentations two ways from **one source of truth**:

- a **PowerPoint `.pptx` template** generated with `python-pptx`, and
- a **Markdown deck** rendered with [Slidev](https://sli.dev).

Both are themed from `references/tokens.toml`. A designer edits that one TOML
file and re-runs the builders — no code changes — so the deck stays on-brand as
the design system evolves. A deck is **interface chrome**, so its colours and
type follow the `sdsc-ui-kit` brand system (not the `sdsc-plotting` data
palette). When you place a chart *on* a slide, colour that chart with
`sdsc-plotting`.

## When to use this skill

Apply whenever generating, theming, or reviewing a presentation for SDSC — a
kick-off deck, a talk, a report-out, or a reusable template — in either
PowerPoint or Slidev. For web pages and components use **sdsc-ui-kit**; for the
colours encoding data inside a figure use **sdsc-plotting**.

## Core rules (always apply)

1. **One source of truth.** Every colour, font, type size, and margin lives in
   `references/tokens.toml`. Never hard-code a hex value or font name in a deck
   or in the builder output — change the token and rebuild.
2. **Fonts:** Space Grotesk for titles, headings, and numbers; Switzer for body,
   bullets, captions, and footers; Fira Code for code. python-pptx cannot embed
   fonts — install them locally so PowerPoint renders them; Slidev loads them
   from Google Fonts / Fontshare.
3. **Brand colours:** the title and closing slides use a brand-blue gradient with
   white type and the horizontal logo; section dividers use a pale lavender panel
   (`#DDDEEC`) with a periwinkle number and a Secondary title;
   content slides follow the theme background with Secondary headings (light
   lavender in dark mode); Primary `#5561A6` is for links, feature icons, and
   bullet rings; Secondary `#26235C` for KPI numbers; Green `#90CA42` is only the
   KPI top rule and the key-takeaway edge — never a body or background colour.
4. **Two themes from one file.** Light is the default; `--dark` (pptx) /
   `html.dark` (Slidev) applies the `[dark]` token overrides. Both are built
   from the same `tokens.toml`.
5. **16:9** widescreen (13.333 × 7.5 in) is the default aspect ratio. No
   labels/eyebrows above headings and no accent rule under them; the footer
   carries the SDSC logo and the page number `n / total` (plus an optional
   centred deck/event name), with no divider line; the closing slide shows the
   white partner silhouettes on the gradient.
6. **Accessibility:** keep WCAG AA (4.5:1 body text, 3:1 large text). The brand
   grey `#848484` is ~3.7:1 on white — use it only for short, large-enough
   captions and footers, never for body copy. Never use colour as the only
   signal.
7. **Verify after every token change:** run `uv run scripts/verify_tokens.py`.
   It checks both themes' contrast (advisory-only for the brand grey).

## Procedure

1. **Pick the format.** PowerPoint (`.pptx`) when the audience edits in
   PowerPoint/Keynote; Slidev when the deck is Markdown, version-controlled, or
   needs live code/diagrams. The design is identical either way.
2. **Theme from the tokens.** Run the matching builder from the skill root with
   [uv](https://docs.astral.sh/uv/) (scripts declare their deps inline, PEP 723);
   add `--dark` / `html.dark` for the dark theme:
   - PowerPoint: `uv run scripts/build_pptx.py -o MyDeck.pptx` (`--dark` for dark)
   - Slidev: `uv run scripts/build_slidev_theme.py -o <project>/style.css`, then
     copy `assets/slidev/global-bottom.vue` and the logos into `<project>/public/`
     (see `references/slidev.md`).
3. **Author the content** using the layouts in `references/layouts.md`. In
   PowerPoint, duplicate a generated slide and replace its text; in Slidev, write
   `slides.md` and pick the SDSC layout per slide.
4. **Retheme by editing tokens, not output.** To change a brand value, edit
   `references/tokens.toml`, re-run both builders, and re-run the verifier.
5. **Mind the data rule:** charts dropped onto a slide are coloured by
   `sdsc-plotting`, not by these brand tokens.

## References — read the one that matches the task

- **`references/tokens.toml`** — the single source of truth: colours, the
  Space Grotesk + Switzer fonts, the slide type scale (in points), layout
  margins, and the contrast-gate pairings. Edit this to retheme everything.
- **`references/layouts.md`** — the SDSC slide layouts (title, section, content,
  two-column, feature grid, key numbers, code, quote/findings, CTA banner,
  closing): what each is for, its colours, and how to build it in both PowerPoint
  and Slidev. Read when composing slides.
- **`references/pptx.md`** — how `build_pptx.py` turns the tokens into a
  PowerPoint template (master theme, layouts, footer, logos) and how to extend
  it. Read when building or customising the .pptx.
- **`references/slidev.md`** — how to scaffold an SDSC Slidev project, wire in
  the generated `style.css`, and use the SDSC layout classes. Read when building
  the Markdown deck.

## Scripts (run with `uv` — inline PEP 723 dependencies)

- **`scripts/build_pptx.py`** — reads `tokens.toml`, writes a 16:9 `.pptx` whose
  master carries the SDSC fonts + colour scheme and whose slides demonstrate
  every layout. (`python-pptx`)
- **`scripts/build_slidev_theme.py`** — reads `tokens.toml`, writes a Slidev
  `style.css` with the SDSC variables and layout styles. (no dependencies)
- **`scripts/verify_tokens.py`** — dependency-free WCAG-AA contrast checker for
  the token pairings; exit code gates CI. Run after any token edit.

## Assets

- **`assets/logos/`** — official SDSC logos used by the builders (horizontal
  colour + white, the SDSC colour + white lockups) and `partners/` (ETH Zürich,
  EPFL, PSI — both the colour originals and the `*_white.png` silhouettes used on
  the closing slide's gradient).
- **`assets/slidev/style.css`** — the generated SDSC Slidev theme (light + dark),
  ready to copy into a Slidev project root (regenerate with `build_slidev_theme.py`).
- **`assets/slidev/global-bottom.vue`** — the Slidev footer component (SDSC logo
  + page number, hidden on cover/section/quote/closing). Copy it to the project
  root alongside `style.css`.
