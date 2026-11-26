#!/usr/bin/env bash
# Build the course site into _site/: VitePress hub, then one Slidev app per deck (src/slides/*.md).
set -euo pipefail
cd "$(dirname "$0")/../.."

export SITE_BASE="${SITE_BASE:-/rdf-training/}"
npx vitepress build src/site

files=_site/files
mkdir -p "$files"
cat src/data/ontology/ontology.ttl src/data/ontology/enumerations.ttl src/data/instances.ttl > "$files/kg.ttl"
cp src/data/ontology/*.ttl src/data/instances.ttl src/data/shacl-advanced.ttl "$files/"

for deck in src/slides/*.md; do
  name=$(basename "$deck" .md)
  npx slidev build "$deck" --base "${SITE_BASE}decks/$name/" --out "$PWD/_site/decks/$name"
done
