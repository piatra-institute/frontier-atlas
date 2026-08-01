#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

sha256sum -c MANIFEST.sha256
mkdir -p .build

g++ -O3 -std=c++17 -Wall -Wextra -pedantic two_slice_rank9.cpp -o .build/two_slice_rank9
python3 tests/test_two_slice_formula.py
python3 verify_upper.py decomposition.json
python3 verify_lower.py \
  --orbits orbits.json \
  --orbit7-cert certificates/backtracking_orbit7.json \
  --full-cert certificates/backtracking_full.json \
  --two-slice-exe .build/two_slice_rank9

echo "ALL CHECKS PASSED: R_F2(<2,2,3>) = 11"
