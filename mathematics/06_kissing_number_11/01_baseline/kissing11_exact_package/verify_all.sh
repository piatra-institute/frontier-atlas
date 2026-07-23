#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 generate_604.py
python3 verify_604.py
python3 verify_saturation_604.py
( cd supplementary && python3 verify_p_slice_certificate.py )
if [[ -f MANIFEST.sha256 ]]; then
  sha256sum -c MANIFEST.sha256
fi
