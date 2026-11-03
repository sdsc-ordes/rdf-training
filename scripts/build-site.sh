#!/usr/bin/env bash
# Build the course site into _site/: VitePress hub, then one Slidev app per deck (slides/*.md).
set -euo pipefail
cd "$(dirname "$0")/.."

export SITE_BASE="${SITE_BASE:-/rdf-training/}"
npx vitepress build site

files=_site/files
mkdir -p "$files"
cat data/vocab/*.ttl data/concepts/*.ttl data/golden/foods.ttl data/golden/people.ttl > "$files/context.ttl"
cat "$files/context.ttl" data/golden/recipes.ttl > "$files/kg.ttl"
cp data/shapes/*.ttl "$files/"

for deck in slides/*.md; do
  name=$(basename "$deck" .md)
  npx slidev build "$deck" --base "${SITE_BASE}decks/$name/" --out "$PWD/_site/decks/$name"
done
