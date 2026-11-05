# Validation and build recipes. CI runs the same recipes.

python := "src tests tools/scripts"

# List recipes.
default:
    @just --list

# Enter the dev shell (direnv does this on cd).
shell:
    nix develop ./tools/nix

# Install Python and Node dependencies from the lockfiles.
setup:
    uv sync --locked
    npm ci

# Format Python code.
format:
    uv run ruff format {{python}}
    uv run ruff check --fix {{python}}

# Lint Python code and check the slide theme against the SDSC tokens.
lint:
    uv run ruff check {{python}}
    uv run ruff format --check {{python}}
    uv run external/sdsc-slides/scripts/verify_tokens.py
    just theme

# Check src/slides/style.css is the theme generated from the SDSC tokens.
theme:
    #!/usr/bin/env bash
    set -euo pipefail
    out="$(mktemp)"
    trap 'rm -f "$out"' EXIT
    uv run external/sdsc-slides/scripts/build_slidev_theme.py -o "$out"
    diff "$out" src/slides/style.css || { echo "src/slides/style.css is out of date: run tools/scripts/update-sdsc-kit.py"; exit 1; }

# Run the Python tests (data, shapes, queries, slide code and bibliographies).
test:
    uv run pytest -q

# Run the SHACL and SPARQL examples through the JavaScript engines too.
cross-check:
    npm run cross-check

# Rebuild the deck bibliographies after editing src/slides/references.toml or a Sources line.
refs:
    uv run python -m kgcourse.refs

# Serve a deck with live reload.
dev deck="src/slides/workshop-2h.md":
    npx slidev {{deck}}

# Build the site and decks into _site/.
build:
    npm run build

# Export every deck to PDF in _site/pdf/.
export:
    npm run export

# Flag slides that overflow; needs `just build` first.
check-slides:
    npm run check:slides

# Run every check CI runs.
check: lint test cross-check build check-slides
