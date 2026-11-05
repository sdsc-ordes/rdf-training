# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Verify the SDSC Slides token contrast pairings (WCAG 2.1). No dependencies.

Reads the [[contrast_pairs]] table from references/tokens.toml and checks each
foreground/background combination meets WCAG AA for its role:

    role = "text"  -> >= 4.5:1  (normal body text)
    role = "large" -> >= 3.0:1  (>= 18pt bold or >= 24pt — slide headings/KPIs)

A pair marked `advisory = true` that falls short is reported as [WARN] and does
NOT fail the gate — reserved for brand-mandated colours (the SDSC secondary grey
on white is ~3.7:1), mirroring how sdsc-plotting treats its intentionally
low-contrast palette colour.

Exit code 0 if every non-advisory pair passes, 1 otherwise, so it can gate CI or
a designer's re-theme. Run after editing tokens.toml:

    uv run scripts/verify_tokens.py
"""

from __future__ import annotations

import sys

import _tokens

THRESHOLD = {"text": 4.5, "large": 3.0}


def _linear(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(hex_value: str) -> float:
    r, g, b = (_linear(v / 255.0) for v in _tokens.hex_to_rgb(hex_value))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg: str, bg: str) -> float:
    la, lb = relative_luminance(fg), relative_luminance(bg)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def check_theme(label: str, dark: bool) -> tuple[bool, bool]:
    """Check every contrast pair for one theme. Returns (ok, warned)."""
    tokens = _tokens.load(dark=dark)
    colors = tokens["colors"]
    pairs = tokens.get("contrast_pairs", [])
    if not pairs:
        print(f"[{label}] No [[contrast_pairs]] in tokens.toml — nothing to check.")
        return True, False

    ok, warned = True, False
    print(f"[{label}] WCAG AA contrast (text >= 4.5:1, large >= 3.0:1):")
    for p in pairs:
        role = p.get("role", "text")
        need = THRESHOLD.get(role, 4.5)
        cr = contrast_ratio(colors[p["fg"]], colors[p["bg"]])
        passed = cr >= need
        if passed:
            flag = "OK  "
        elif p.get("advisory"):
            flag = "WARN"
            warned = True
        else:
            flag = "FAIL"
            ok = False
        print(f"  [{flag}] {p['name']:<40} {cr:5.2f}:1  "
              f"(need {need:.1f}, role={role})")
    return ok, warned


def main() -> int:
    ok = True
    warned = False
    for label, dark in (("LIGHT", False), ("DARK", True)):
        theme_ok, theme_warned = check_theme(label, dark)
        ok = ok and theme_ok
        warned = warned or theme_warned
        print()

    if ok:
        msg = ("PASS — all required pairings meet WCAG AA in both themes"
               + (" (advisory warnings above are brand-mandated)." if warned
                  else "."))
    else:
        msg = "FAIL — a required pairing is below threshold (see [FAIL] rows)."
    print(msg)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
