#!/usr/bin/env python3
from __future__ import annotations
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
C=[tuple(p) for p in json.loads((ROOT/'cf236.json').read_text())]
S=set(C)
allpts=[]
for n in range(3**7):
    x=n
    p=[]
    for _ in range(7):
        p.append(x%3); x//=3
    allpts.append(tuple(p))

def negsum(a,b):
    return tuple((-x-y)%3 for x,y in zip(a,b))

blockers=defaultdict(list)
for i,a in enumerate(C):
    for j in range(i+1,len(C)):
        b=C[j]
        p=negsum(a,b)
        if p not in S:
            blockers[p].append((i,j))

hist=Counter(len(blockers[p]) for p in allpts if p not in S)
print('outside',len(allpts)-len(C))
print('blocker histogram')
for k in sorted(hist): print(k,hist[k])
print('min',min(hist),'max',max(hist))
for k in sorted(hist)[:5]:
    pts=[p for p in allpts if p not in S and len(blockers[p])==k]
    print('k',k,'count',len(pts),'first',pts[:10])

# Sum checks: each cap pair blocks exactly one outside point.
print('total blocker pairs',sum(k*v for k,v in hist.items()),'expected',len(C)*(len(C)-1)//2)

# Layer histogram of outside points by blocker number.
layer=Counter()
for p in allpts:
    if p not in S:
        layer[(p[0],len(blockers[p]))]+=1
print('by first coordinate')
for key in sorted(layer): print(key,layer[key])
