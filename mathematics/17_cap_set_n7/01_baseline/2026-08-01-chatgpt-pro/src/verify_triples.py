#!/usr/bin/env python3
"""Independent cap verifier scanning every unordered triple."""
from __future__ import annotations
import csv,sys
from itertools import combinations
def main(path:str)->int:
 with open(path,newline='') as f:rows=list(csv.reader(f))
 points=[tuple(map(int,row)) for row in rows[1:]]
 if not points:raise SystemExit('FAIL: empty set')
 n=len(points[0])
 if len(points)!=len(set(points)):raise SystemExit('FAIL: duplicate point')
 if any(len(p)!=n or any(c not in (0,1,2) for c in p) for p in points):raise SystemExit('FAIL: malformed coordinate')
 checked=0
 for a,b,c in combinations(points,3):
  checked+=1
  if all((a[j]+b[j]+c[j])%3==0 for j in range(n)):
   raise SystemExit(f'FAIL: zero-sum triple {a} {b} {c}')
 print(f'PASS triple-scan: n={n} size={len(points)} triples={checked}')
 return 0
if __name__=='__main__':raise SystemExit(main(sys.argv[1]))
