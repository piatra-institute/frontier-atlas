#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p .build/reproduced
python3 generate_backtracking_certificate.py \
  --orbits orbits.json --orbit-index 7 --target 9 \
  --output .build/reproduced/backtracking_orbit7.json
python3 generate_backtracking_certificate.py \
  --orbits orbits.json --orbit-index 10 --target 11 \
  --output .build/reproduced/backtracking_full.json
cmp certificates/backtracking_orbit7.json .build/reproduced/backtracking_orbit7.json
cmp certificates/backtracking_full.json .build/reproduced/backtracking_full.json
echo "CERTIFICATE REPRODUCTION OK"
