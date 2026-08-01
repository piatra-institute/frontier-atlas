#!/usr/bin/env python3
"""Exhaust all minimal 10-removal neighborhoods around the CF236 cap.

Every outside point is blocked by >=10 disjoint cap-pairs.  A 10-removal
set that makes any outside point addable must therefore choose exactly one
endpoint from each blocker pair of a point with blocker count 10.  There are
24 such points and 2^10 choices per point.  This script enumerates all 24,576
choices and records the individually addable outside points.
"""
from __future__ import annotations
import json
from collections import defaultdict, Counter
from pathlib import Path
from itertools import combinations

ROOT=Path(__file__).resolve().parents[1]
C=[tuple(p) for p in json.loads((ROOT/'cf236.json').read_text())]
S=set(C)
allpts=[]
for n in range(3**7):
    x=n; p=[]
    for _ in range(7): p.append(x%3); x//=3
    allpts.append(tuple(p))

def negsum(a,b): return tuple((-x-y)%3 for x,y in zip(a,b))

blockers=defaultdict(list)
for i,a in enumerate(C):
    for j in range(i+1,len(C)):
        p=negsum(a,C[j])
        if p not in S: blockers[p].append((i,j))

low=sorted(p for p in allpts if p not in S and len(blockers[p])==10)
assert len(low)==24
edge_masks={p:[(1<<i)|(1<<j) for i,j in blockers[p]] for p in low}
for p in low:
    assert len(edge_masks[p])==10
    # blocker edges for a fixed outside point are a matching
    flat=[]
    for i,j in blockers[p]: flat.extend([i,j])
    assert len(flat)==len(set(flat))==20

best=0; best_records=[]; hist=Counter(); unique_R=set()
for seed_idx,p in enumerate(low):
    edges=blockers[p]
    for bits in range(1<<10):
        R=0
        for e,(i,j) in enumerate(edges):
            R |= 1 << (j if (bits>>e)&1 else i)
        assert R.bit_count()==10
        unique_R.add(R)
        addable=[]
        for q in low:
            if all(R & em for em in edge_masks[q]):
                addable.append(q)
        k=len(addable); hist[k]+=1
        if k>best:
            best=k; best_records=[(p,bits,R,addable)]
        elif k==best:
            best_records.append((p,bits,R,addable))

print('low-blocker outside points',len(low))
print('enumerated seed/choice pairs',24*(1<<10))
print('unique removal sets',len(unique_R))
print('individually-addable count histogram')
for k in sorted(hist): print(k,hist[k])
print('maximum individually addable',best)
print('number attaining maximum',len(best_records))
for p,bits,R,A in best_records[:10]:
    removed=[C[i] for i in range(len(C)) if (R>>i)&1]
    print('seed',p,'choice',bits,'addable',A,'removed',removed)

out={
    'max_individually_addable':best,
    'count_best_records':len(best_records),
    'histogram':dict(sorted(hist.items())),
    'best_records':[
        {
            'seed':list(p), 'choice':bits,
            'removed_indices':[i for i in range(len(C)) if (R>>i)&1],
            'addable':[list(q) for q in A],
        }
        for p,bits,R,A in best_records
    ],
}
(ROOT/'certificates'/'exchange10_search.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
