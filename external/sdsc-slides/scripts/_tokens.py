"""Shared token loader for the SDSC Slides builders.

Loads references/tokens.toml (the single source of truth) and resolves the
type-scale entries — whose `font` and `color` fields are *references* into the
[fonts] and [colors] tables — into concrete values. No third-party deps: uses
the stdlib `tomllib` (Python 3.11+).

The build scripts import this; keep it dependency-free so it works under any of
their PEP 723 environments.
"""

from __future__ import annotations

import tomllib
from pathlib import Path

# tokens.toml lives one directory up from scripts/, in references/.
DEFAULT_TOKENS = Path(__file__).resolve().parent.parent / "references" / "tokens.toml"


def load(path: Path | str | None = None, dark: bool = False) -> dict:
    """Read tokens.toml and return it as a plain dict.

    When ``dark`` is True, the scalar overrides in the ``[dark]`` table are
    merged over ``[colors]`` and ``[dark.gradient]`` replaces ``[gradient]``, so
    callers get a fully-resolved palette for the chosen theme. ``data["_dark"]``
    records which theme was loaded.
    """
    p = Path(path) if path else DEFAULT_TOKENS
    with open(p, "rb") as fh:
        data = tomllib.load(fh)
    if dark and "dark" in data:
        overrides = data["dark"]
        data["colors"].update(
            {k: v for k, v in overrides.items() if not isinstance(v, dict)})
        if "gradient" in overrides:
            data["gradient"] = overrides["gradient"]
    data["_dark"] = dark
    return data


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    """'#RRGGBB' -> (r, g, b) ints in 0..255."""
    h = value.lstrip("#")
    if len(h) != 6:
        raise ValueError(f"expected #RRGGBB, got {value!r}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def resolve_type(tokens: dict, name: str) -> dict:
    """Resolve one [type.<name>] entry into concrete values.

    Returns a dict with: size (pt), weight ("bold"/"regular"), bold (bool),
    font (family name), color (hex string).
    """
    t = tokens["type"][name]
    fonts = tokens["fonts"]
    colors = tokens["colors"]
    return {
        "size": t["size"],
        "weight": t["weight"],
        "bold": t["weight"] == "bold",
        "font": fonts[t["font"]],
        "font_fallback": fonts.get(f"{t['font']}_fallback", ""),
        "color": colors[t["color"]],
    }


def color(tokens: dict, name: str) -> str:
    """Look up a [colors] hex value by key."""
    return tokens["colors"][name]
