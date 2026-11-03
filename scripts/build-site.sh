#!/usr/bin/env bash
# Build the course site into _site/: VitePress hub, then one Slidev app per deck (slides/*.md).
set -euo pipefail
cd "$(dirname "$0")/.."

export SITE_BASE="${SITE_BASE:-/rdf-training/}"
npx vitepress build site

for deck in slides/*.md; do
  name=$(basename "$deck" .md)
  npx slidev build "$deck" --base "${SITE_BASE}decks/$name/" --out "$PWD/_site/decks/$name"
done
