#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import argparse,csv,json,time
import networkx as nx
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType

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

def extension_clauses(G):
 A=bits(G);K=cliques(A);I=cliques(comp(A))
 return [[v+1 for v in q] for q in I]+[[-(v+1) for v in q] for q in K],len(I),len(K)

def solve_bound(G,bound,proof=False):
 clauses,ni,nk=extension_clauses(G);m=len(clauses)
 relax=list(range(43,43+m)); hard=[c+[r] for c,r in zip(clauses,relax)]
 card=CardEnc.atmost(lits=relax,bound=bound,top_id=42+m,encoding=EncType.seqcounter)
 hard.extend(card.clauses)
 with Solver(name='glucose4',bootstrap_with=hard,with_proof=proof) as s:
  sat=s.solve();model=s.get_model() if sat else None;pr=s.get_proof() if proof and not sat else None
 S={x-1 for x in model or [] if 1<=x<=42}
 cost=sum(not any((lit>0 and lit-1 in S) or (lit<0 and -lit-1 not in S) for lit in c) for c in clauses) if sat else None
 return sat,cost,S,len(hard),card.nv,pr,ni,nk

if __name__=='__main__':
 Gs=list(nx.read_graph6('../data/r55_42some.g6'))
 for i in [0,41,255]:
  for b in [0,1,2]:
   t=time.perf_counter();r=solve_bound(Gs[i],b);print(i,b,r[0],r[1],len(r[2]),r[3],r[4],time.perf_counter()-t,flush=True)
