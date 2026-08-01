#!/usr/bin/env python3
"""Independent cap verifier: for every distinct pair x,y, check -x-y is absent."""
from __future__ import annotations
import json,sys
from itertools import combinations
from pathlib import Path
def main(path:str)->int:
 raw=json.loads(Path(path).read_text())
 points=[tuple(map(int,p)) for p in raw]
 if not points:raise SystemExit('FAIL: empty set')
 n=len(points[0])
 if len(points)!=len(set(points)):raise SystemExit('FAIL: duplicate point')
 if any(len(p)!=n or any(c not in (0,1,2) for c in p) for p in points):raise SystemExit('FAIL: malformed coordinate')
 S=set(points);checked=0
 for x,y in combinations(points,2):
  z=tuple((-a-b)%3 for a,b in zip(x,y));checked+=1
  if z in S:raise SystemExit(f'FAIL: line witness {x} {y} {z}')
 print(f'PASS pair-midpoint: n={n} size={len(points)} pairs={checked}')
 return 0
if __name__=='__main__':raise SystemExit(main(sys.argv[1]))
