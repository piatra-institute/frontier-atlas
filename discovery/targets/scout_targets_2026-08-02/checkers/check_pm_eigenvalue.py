#!/usr/bin/env python3
"""Schema/dependency preflight for the perfect-matching-scheme eigenvalue target.
A full checker requires the paper's exact zonal-spherical-function recurrence or Sage code.
"""
from __future__ import annotations
import argparse,json,shutil
from pathlib import Path
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('payload',type=Path); a=ap.parse_args(); p=json.loads(a.payload.read_text())
    print(json.dumps({"schema_ok":all(k in p for k in ('n','mu','lambda','eigenvalue')),
                      "sage_available":shutil.which('sage') is not None,
                      "full_checker_ready":False,
                      "reason":"exact eigenvalue recomputation not vendored"},indent=2,sort_keys=True))
