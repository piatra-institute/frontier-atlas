#!/usr/bin/env python3
"""Independent arithmetic validator for a supplied polynomial coefficient sequence.
This does NOT recompute Q_M or Y_M from a matroid, so the corresponding admission gate stays red.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path

def check(payload):
    a=[int(x) for x in payload['coefficients']]
    tests=[{"i":i,"lhs":a[i]*a[i],"rhs":a[i-1]*a[i+1],"pass":a[i]*a[i]>=a[i-1]*a[i+1]} for i in range(1,len(a)-1)]
    return {"coefficients":a,"nonnegative":all(x>=0 for x in a),"tests":tests,"log_concave":all(t['pass'] for t in tests)}
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('payload',type=Path); a=ap.parse_args()
    print(json.dumps(check(json.loads(a.payload.read_text())),indent=2,sort_keys=True))
