#!/usr/bin/env python3
from pathlib import Path
from itertools import combinations
from collections import Counter
import json, networkx as nx

def read_matrix(path):
 rows=[x.strip() for x in Path(path).read_text().splitlines() if x.strip()]
 n=len(rows); assert all(len(r)==n for r in rows)
 assert all(rows[i][i]=='0' for i in range(n))
 assert all(rows[i][j]==rows[j][i] for i in range(n) for j in range(n))
 A=[0]*n
 for i in range(n):
  for j in range(i+1,n):
   if rows[i][j]=='1':A[i]|=1<<j;A[j]|=1<<i
 return rows,A

def to_nx(A,exclude=None):
 verts=[v for v in range(len(A)) if v!=exclude]
 G=nx.Graph();G.add_nodes_from(verts)
 G.add_edges_from((i,j) for i in verts for j in verts if i<j and (A[i]>>j)&1)
 return nx.convert_node_labels_to_integers(G)

def bad5(A):
 out=[]
 for S in combinations(range(len(A)),5):
  mask=sum(1<<v for v in S)
  twice=sum((A[v]&mask).bit_count() for v in S)
  if twice==0:out.append({'vertices':list(S),'color':'independent'})
  elif twice==20:out.append({'vertices':list(S),'color':'clique'})
 return out

def key(G):
 return (G.number_of_edges(),tuple(sorted(dict(G.degree()).values())),nx.weisfeiler_lehman_graph_hash(G))

known=list(nx.read_graph6('../data/r55_42some.g6'))
buckets={}
for i,G in enumerate(known):
 buckets.setdefault(key(G),[]).append((i,False,G))
 H=nx.complement(G);buckets.setdefault(key(H),[]).append((i,True,H))
allres=[]; mats=[]
for gi in (1,2):
 rows,A=read_matrix(f'../data/near43_graph{gi}.matrix');mats.append(rows)
 bad=bad5(A); inter=set(range(43))
 for b in bad:inter&=set(b['vertices'])
 matches=[]
 for v in sorted(inter):
  H=to_nx(A,v); found=[]
  for idx,isc,K in buckets.get(key(H),[]):
   if nx.is_isomorphic(H,K):found.append({'known_index':idx,'complement':isc})
  matches.append({'deleted_vertex':v,'edges':H.number_of_edges(),'matches':found})
 deg=[x.bit_count() for x in A]
 allres.append({'graph':gi,'vertices':43,'edges':sum(deg)//2,
   'degree_counts':dict(sorted(Counter(deg).items())),
   'bad5':bad,'bad5_intersection':sorted(inter),
   'good_deletions':sorted(inter),'good_deletion_matches':matches})
# exact matrix Hamming distance
diffs=[]
for i in range(43):
 for j in range(i+1,43):
  if mats[0][i][j]!=mats[1][i][j]:diffs.append([i,j])
result={'graphs':allres,'edge_flips_between_graphs':diffs}
print(json.dumps(result,indent=2))
Path('../results/near43_analysis.json').write_text(json.dumps(result,indent=2)+'\n')
