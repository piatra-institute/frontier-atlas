#!/usr/bin/env python3
"""Coefficient-level spectrum comparison; construction of E_n is intentionally absent."""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('payload',type=Path); a=ap.parse_args(); p=json.loads(a.payload.read_text())
    n=int(p['n']); vals=sorted(map(float,p['singular_values']),reverse=True); target=sorted([1.0]+[2**(-k/2) for k in range(1,n)],reverse=True)
    err=max((abs(x-y) for x,y in zip(vals,target)),default=math.inf) if len(vals)==len(target) else math.inf
    print(json.dumps({"n":n,"length_ok":len(vals)==n,"max_abs_error":err,"matches_1e-10":err<=1e-10,
                      "full_checker_ready":False,"reason":"E_n is not independently constructed from Hermite roots"},indent=2,sort_keys=True))
