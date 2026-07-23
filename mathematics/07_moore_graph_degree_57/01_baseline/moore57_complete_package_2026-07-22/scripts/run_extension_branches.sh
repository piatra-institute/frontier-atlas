#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BUILD="$ROOT/build"
LOGS="$ROOT/extension_logs"
mkdir -p "$BUILD" "$LOGS"

g++ -O3 -std=c++17 "$ROOT/research_package/dlx_exact_cover.cpp" \
  -o "$BUILD/dlx_exact_cover"

for instance in "$ROOT"/extension_instances/g*_A*.txt; do
  name="$(basename "$instance" .txt)"
  echo "=== $name ===" | tee "$LOGS/$name.log"
  /usr/bin/time -f 'elapsed_seconds=%e max_rss_kb=%M exit=%x' \
    "$BUILD/dlx_exact_cover" "$instance" 2>&1 | tee -a "$LOGS/$name.log"
done
