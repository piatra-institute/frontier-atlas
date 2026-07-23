#!/usr/bin/env python3
from pathlib import Path
from itertools import combinations
from collections import Counter
import json

def read(path):
 rows=[x.strip() for x in Path(path).read_text().splitlines() if x.strip()]
 n=len(rows); return rows,n

def landscape(rows,n):
 delta={(i,j):0 for i in range(n) for j in range(i+1,n)}
 base_bad=0; hist=Counter()
 for S in combinations(range(n),5):
  pairs=list(combinations(S,2))
  ones=[p for p in pairs if rows[p[0]][p[1]]=='1']
  e=len(ones);hist[e]+=1
  if e==0:
   base_bad+=1
   for p in pairs:delta[p]-=1
  elif e==10:
   base_bad+=1
   for p in pairs:delta[p]-=1
  elif e==1:
   delta[ones[0]]+=1
  elif e==9:
   only0=next(p for p in pairs if rows[p[0]][p[1]]=='0')
   delta[only0]+=1
 vals={p:base_bad+d for p,d in delta.items()}
 dist=Counter(vals.values());m=min(vals.values())
 best=[list(p) for p,x in vals.items() if x==m]
 return {'base_bad':base_bad,'five_set_edge_histogram':dict(sorted(hist.items())),
         'one_flip_bad_count_distribution':dict(sorted(dist.items())),
         'minimum_after_one_flip':m,'best_one_flips':best}

out={}
for gi in (1,2):
 rows,n=read(f'../data/near43_graph{gi}.matrix');out[f'graph{gi}']=landscape(rows,n)
print(json.dumps(out,indent=2))
Path('../results/near43_flip_landscape.json').write_text(json.dumps(out,indent=2)+'\n')
