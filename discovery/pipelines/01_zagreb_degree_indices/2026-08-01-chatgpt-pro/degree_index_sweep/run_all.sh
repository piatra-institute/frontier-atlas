#!/usr/bin/env bash
set -euo pipefail
python -m pip install -r requirements.txt
python sweep.py --data-dir data --output-dir results
python verify_witnesses.py
