#!/usr/bin/env bash
# Export every deck (src/slides/*.md) to _site/pdf/. Run inside the nix devshell for $SLIDEV_CHROMIUM.
set -euo pipefail
cd "$(dirname "$0")/../.."

mkdir -p _site/pdf
for deck in src/slides/*.md; do
  name=$(basename "$deck" .md)
  npx slidev export "$deck" --per-slide --output "$PWD/_site/pdf/kg-$name.pdf" \
    ${SLIDEV_CHROMIUM:+--executable-path "$SLIDEV_CHROMIUM"} --timeout 120000 --wait 1000
done
