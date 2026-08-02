#!/usr/bin/env python3
"""Dependency preflight for recomputing inverse KL / inverse Z polynomials from a matroid."""
from __future__ import annotations
import argparse,json,shutil
from pathlib import Path
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('payload',type=Path); a=ap.parse_args(); p=json.loads(a.payload.read_text())
    print(json.dumps({"matroid_encoding_present":'bases' in p or 'rank_table' in p,
                      "sage_available":shutil.which('sage') is not None,"full_checker_ready":False,
                      "reason":"matroid-to-Q/Y recurrence not independently vendored"},indent=2,sort_keys=True))
