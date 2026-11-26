#!/usr/bin/env bash
# Build docs/data/recipes.rete from the course data, then the self-contained lab page docs/lab.html.
#
#   bash src/rete/build-rete.sh            # .rete file and lab page
#   bash src/rete/build-rete.sh --no-lab   # .rete file only
#
# Uses the rete CLI at the pinned version: $RETE_BIN if set, else `rete` on PATH when its version
# matches, else the release binary, downloaded once into .cache/rete/ and checked against SHA256SUMS.
set -euo pipefail
cd "$(dirname "$0")/../.."

RETE_VERSION="${RETE_VERSION:-0.7.8}" # keep in step with rete-graph in package.json
out=docs/data/recipes.rete

rete_bin() {
  if [[ -n "${RETE_BIN:-}" ]]; then
    echo "$RETE_BIN"
    return
  fi
  if command -v rete >/dev/null && [[ "$(rete --version 2>/dev/null)" == "rete $RETE_VERSION" ]]; then
    command -v rete
    return
  fi

  local cache=".cache/rete/$RETE_VERSION"
  if [[ ! -x "$cache/rete" ]]; then
    local os arch target asset url
    case "$(uname -s)" in
      Darwin) os=apple-darwin ;;
      Linux) os=unknown-linux-gnu ;;
      *) echo "unsupported system $(uname -s): set RETE_BIN to a rete $RETE_VERSION binary" >&2; exit 1 ;;
    esac
    case "$(uname -m)" in
      arm64 | aarch64) arch=aarch64 ;;
      x86_64 | amd64) arch=x86_64 ;;
      *) echo "unsupported machine $(uname -m): set RETE_BIN to a rete $RETE_VERSION binary" >&2; exit 1 ;;
    esac
    target="$arch-$os"
    asset="rete-$RETE_VERSION-$target.tar.gz"
    url="https://github.com/caviri/rete/releases/download/v$RETE_VERSION"

    mkdir -p "$cache/dl"
    echo "downloading $asset" >&2
    curl -fsSL "$url/$asset" -o "$cache/dl/$asset"
    curl -fsSL "$url/SHA256SUMS" -o "$cache/dl/SHA256SUMS"
    (
      cd "$cache/dl"
      grep " [*]\{0,1\}$asset\$" SHA256SUMS >sum
      if command -v sha256sum >/dev/null; then sha256sum -c sum >&2; else shasum -a 256 -c sum >&2; fi
    )
    tar -xzf "$cache/dl/$asset" -C "$cache/dl"
    cp "$(find "$cache/dl" -type f -name rete | head -n 1)" "$cache/rete"
    chmod +x "$cache/rete"
    rm -rf "$cache/dl"
  fi
  echo "$cache/rete"
}

rete="$(rete_bin)"
echo "using $("$rete" --version) ($rete)"

# One Turtle file: ontology, value lists and instance data, the same sources as the course's kg.ttl.
src="$(mktemp -d)"
trap 'rm -rf "$src"' EXIT
cat src/data/ontology/ontology.ttl src/data/ontology/enumerations.ttl \
  src/data/golden/{countries,units,foods,people,recipes}.ttl >"$src/recipes.ttl"

# Date of the last change to the data, so that the same sources give the same file.
epoch="$(git log -1 --format=%ct -- src/data 2>/dev/null || true)"
export SOURCE_DATE_EPOCH="${epoch:-$(date +%s)}" RETE_BUILD_RECORD=reproducible
created="$(date -u -r "$SOURCE_DATE_EPOCH" +%F 2>/dev/null || date -u -d "@$SOURCE_DATE_EPOCH" +%F)"

mkdir -p "$(dirname "$out")"
"$rete" build "$src/recipes.ttl" -o "$out" \
  --card --label-index \
  --title "Recipe knowledge graph" \
  --description "Course data of the SDSC knowledge graphs training: ontology, SKOS value lists, foods and recipes." \
  --license "https://www.apache.org/licenses/LICENSE-2.0" \
  --source "https://github.com/sdsc-ordes/rdf-training" \
  --created "$created"
"$rete" verify "$out"
"$rete" info "$out"

if [[ "${1:-}" != "--no-lab" ]]; then
  node src/rete/build-lab.mjs
fi
