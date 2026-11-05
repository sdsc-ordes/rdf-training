# Building the PowerPoint template

`scripts/build_pptx.py` turns `references/tokens.toml` into a 16:9 `.pptx`. Run
it from the skill root with [uv](https://docs.astral.sh/uv/) — the dependency
(`python-pptx`) is declared inline (PEP 723), so no virtualenv setup is needed:

```bash
uv run scripts/build_pptx.py                      # -> SDSC_Slides_Template.pptx
uv run scripts/build_pptx.py --dark -o Dark.pptx  # dark theme ([dark] overrides)
uv run scripts/build_pptx.py -o MyDeck.pptx       # choose the output path
uv run scripts/build_pptx.py --tokens other.toml  # theme from a different TOML
```

## What the script produces

A presentation that is both a **template** (open it, duplicate a slide, replace
the text) and a **worked example** (one slide per layout, see `layouts.md`):

1. The slide size is set to 16:9 from `[meta]` (13.333 × 7.5 in).
2. **The slide master is patched** so new slides inherit the brand:
   - the theme `majorFont`/`minorFont` become Space Grotesk / Switzer;
   - the theme colour scheme slots (`accent1-3`, `dk2`, `hlink`, …) become the
     SDSC Primary / Secondary / green / grey.
   This is best-effort and wrapped in `try/except`: if a future python-pptx
   parses the theme part differently, the build still succeeds and every shape
   is styled explicitly anyway.
3. Each layout is drawn on a **blank** layout (`slide_layouts[6]`) from shapes —
   a full-bleed background (a solid rectangle, the lavender section panel, or a
   gradient on the title and closing slides), text boxes, top rules, ring
   bullets, feature cards, logos, and (on content slides) the footer: SDSC logo
   (left) and the page number `n / total` (right), plus the optional `--event`
   name (centred), with no divider line. The total is filled in at `save()` once
   the slide count is known.
4. The **closing slide** places the **white partner silhouettes** (ETH Zürich,
   EPFL, PSI — the `*_white.png` assets) straight on the gradient, bottom-left,
   with no backing band.

Pass `--dark` to apply the `[dark]` token overrides: content slides go dark with
a light-lavender heading and the white footer logo; the title/closing gradient
darkens; the section/banner panels become deep indigo. Pass `--event "…"` to set
the optional centred footer text (off by default).

The `Deck` methods are: `title`, `section`, `content` (with optional `body`,
`bullets`, `takeaway`), `two_column` (left/right dicts), `feature_grid`,
`key_numbers`, `code`, `findings`, `banner`, `palette`, and `closing`.

## How it maps to the tokens

`_tokens.py` loads the TOML and resolves each `[type.*]` entry — whose `font` and
`color` fields are *references* into `[fonts]` and `[colors]` — into a concrete
`{size, bold, font, color}`. The `Deck` class reads geometry from `[layout]`
(margins, footer height, accent-bar height, logo heights). So:

- change a **colour** → edit `[colors]` → every slide using it updates;
- change a **size or weight** → edit the matching `[type.*]` table;
- change a **margin or the footer height** → edit `[layout]`.

Never hard-code a hex value or font name in the script output — edit the token.

## Fonts (important)

python-pptx **cannot embed fonts**. The .pptx only names "Space Grotesk" and
"Switzer"; PowerPoint substitutes if they are not installed. Install both on any
machine that edits or exports the deck:

- Space Grotesk — Google Fonts.
- Switzer — [Fontshare](https://www.fontshare.com/fonts/switzer).

The `*_fallback` tokens (Arial / Calibri) document the intended substitutes. To
guarantee fidelity on machines without the fonts, embed them from PowerPoint
itself (File → Options → Save → *Embed fonts in the file*) after generating.

## Logos

The builder pulls logos from `assets/logos/`:

- `SDSC_logo_horizontal_rgb_white.png` — wide horizontal lockup on the title and
  closing slides (on the gradient);
- `SDSC_Logo_RGB.png` / `SDSC_Logo_White.png` — content-slide footer (colour in
  the light theme, white in the dark theme);
- `partners/ETH_Zurich_logo_white.png`, `partners/EPFL_logo_white.png`,
  `partners/PSI_logo_white.png` — the white partner silhouettes on the closing
  slide's gradient (no backing band).

Each `add_logo` call no-ops if the file is missing, so the build never breaks on
a logo path. Keep the official files; never recolour or stretch them.

## Extending it

To add a new layout, add a method to `Deck` that calls `self._blank()` and the
shape helpers (`add_rect`, `add_text`, `add_bullets`, `add_logo`), reading colour
and type from `self.color(...)` / `self.ty(...)`. To change the example content,
edit `build_example()` — keep it to **public or mock data** per the SDSC
data-handling rules. Re-run `scripts/verify_tokens.py` after any token edit.

## Limitations

- python-pptx edits existing layouts/masters but does not create brand-new slide
  *layouts* in the layout gallery; this skill draws each layout as slide content
  instead, which is the robust, viewer-independent approach.
- Font embedding and PDF export are done from PowerPoint, not from the script.
