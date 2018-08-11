#!/bin/sh

set -e

find "$(dirname "${0}")/../" \
  \( \
  -name '*.js' \
  -o -name '*.json' \
  -o -name '*.md' \
  -o -name '*.gyp' \
  \) \
  -not -path '*/node_modules/*' \
  -not -path '*/build/*' \
  -not -path '*/woff2/*' \
  -print0 | \
  xargs --null "$(npm bin)/prettier" --write
