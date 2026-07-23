from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
import networkx as nx, numpy as np, random, itertools
G=nx.Graph()
for line in (ROOT / 'data' / '510.edge').read_text().splitlines():
 p=line.split()
 if not p:continue
 if p[0]=='p':n=int(p[2]);G.add_nodes_from(range(n))
 elif p[0]=='e':G.add_edge(int(p[1])-1,int(p[2])-1)
adj=[list(G.neighbors(v)) for v in range(n)]
d=nx.coloring.greedy_color(G,strategy='DSATUR')
col=np.array([d[i] for i in range(n)],dtype=np.uint8)
assert col.max()<5
rng=random.Random(20260722)
rows=[col.copy()]
for it in range(30000):
 if rng.random()<0.15:
  v=rng.randrange(n)
  used=0
  for w in adj[v]:used|=1<<int(col[w])
  choices=[c for c in range(5) if c!=col[v] and not ((used>>c)&1)]
  if choices:col[v]=rng.choice(choices)
 else:
  a,b=rng.sample(range(5),2)
  candidates=np.flatnonzero((col==a)|(col==b))
  s=int(candidates[rng.randrange(len(candidates))])
  seen={s};stack=[s]
  while stack:
   v=stack.pop()
   for w in adj[v]:
    if w not in seen and (col[w]==a or col[w]==b):seen.add(w);stack.append(w)
  idx=np.fromiter(seen,dtype=np.int32)
  m=(col[idx]==a);col[idx[m]]=b;col[idx[~m]]=a
 if it%10==9:rows.append(col.copy())
rows=np.array(rows,dtype=np.uint8)
np.save(ROOT / 'data' / '510_kempe_samples_3001.npy', rows)
rows.tofile(ROOT / 'data' / '510_kempe_samples_3001.u8')
print('rows',rows.shape)
# patterns on six special vertices (0-based)
S=[211,217,223,488,489,490]
def patt(vals):
 mp={};out=[]
 for x in vals:
  if int(x) not in mp:mp[int(x)]=len(mp)
  out.append(mp[int(x)])
 return tuple(out)
from collections import Counter
for tri in itertools.combinations(S,3):
 C=Counter(patt(r[list(tri)]) for r in rows)
 allpat={(0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,2)}
 miss=allpat-set(C)
 if miss:
  print('tri',tuple(x+1 for x in tri),'missing',miss,'counts',C)
