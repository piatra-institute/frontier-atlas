#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import argparse,csv,json,time
import networkx as nx
from pysat.formula import WCNF
from pysat.examples.rc2 import RC2

def bits(G):
 A=[0]*len(G)
 for u,v in G.edges():A[u]|=1<<v;A[v]|=1<<u
 return A

def comp(A):
 m=(1<<len(A))-1;return [m^(1<<v)^A[v] for v in range(len(A))]

def cliques(A,k=4):
 out=[]
 def rec(cand,p):
  if len(p)==k:out.append(tuple(p));return
  need=k-len(p)
  while cand.bit_count()>=need:
   b=cand&-cand;cand^=b;v=b.bit_length()-1
   rec(cand&A[v],p+[v])
 rec((1<<len(A))-1,[]);return out

def solve(G):
 A=bits(G);K=cliques(A);I=cliques(comp(A))
 f=WCNF()
 for q in I:f.append([v+1 for v in q],weight=1)
 for q in K:f.append([-(v+1) for v in q],weight=1)
 with RC2(f,solver='g4',adapt=True,exhaust=True,incr=False,minz=True,trim=5) as rc2:
  model=rc2.compute();cost=rc2.cost
 S={x-1 for x in model if 1<=x<=len(A)}
 # Direct objective audit
 badI=sum(all(v not in S for v in q) for q in I)
 badK=sum(all(v in S for v in q) for q in K)
 assert badI+badK==cost
 return cost,len(K),len(I),S,badK,badI

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--start',type=int,default=0);ap.add_argument('--end',type=int,default=None)
 args=ap.parse_args();Gs=list(nx.read_graph6('../data/r55_42some.g6'));end=len(Gs) if args.end is None else min(args.end,len(Gs))
 rows=[];t=time.perf_counter()
 for i in range(args.start,end):
  cost,nk,ni,S,bk,bi=solve(Gs[i]);rows.append({'index':i,'min_bad':cost,'k4':nk,'i4':ni,
   'new_degree':len(S),'bad_clique5':bk,'bad_independent5':bi,'neighbor_mask_hex':hex(sum(1<<v for v in S))})
  print(i,cost,len(S),flush=True)
 out=Path(f'../results/min_bad_ext_{args.start}_{end}.csv')
 with out.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 print(json.dumps({'start':args.start,'end':end,'seconds':time.perf_counter()-t,'distribution':dict(Counter(r['min_bad'] for r in rows))},indent=2))
if __name__=='__main__':main()
