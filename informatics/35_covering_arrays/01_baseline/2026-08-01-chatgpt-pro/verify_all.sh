#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

sha256sum -c ARTIFACT_MANIFEST.sha256

BUILD_DIR="$(mktemp -d)"
trap 'rm -rf "$BUILD_DIR"' EXIT

g++ -std=c++17 -O2 -Wall -Wextra -pedantic \
  src/verify_coverage_independent.cpp \
  -o "$BUILD_DIR/verify_coverage_independent"

python3 src/verify_coverage.py array_CA_13_2_8_3.csv \
  | tee logs/coverage_python.log

"$BUILD_DIR/verify_coverage_independent" array_CA_13_2_8_3.csv \
  | tee logs/coverage_cpp.log

python3 src/verify_lower_bound_independent.py . \
  | tee logs/independent_lower_bound_verifier.stdout.log

printf '%s\n' 'ALL_CHECKS_PASS'
