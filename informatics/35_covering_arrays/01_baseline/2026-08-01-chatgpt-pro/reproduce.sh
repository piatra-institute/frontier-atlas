#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

BUILD_DIR="$(mktemp -d)"
trap 'rm -rf "$BUILD_DIR"' EXIT

g++ -std=c++17 -O2 -Wall -Wextra -pedantic \
  src/generate_certificate.cpp \
  -o "$BUILD_DIR/generate_certificate"

"$BUILD_DIR/generate_certificate" "$ROOT"

./verify_all.sh
