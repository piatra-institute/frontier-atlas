#!/usr/bin/env python3
from pathlib import Path
from itertools import combinations
import json,time,networkx as nx
from pysat.solvers import Solver
from pysat.card import CardEnc,EncType
from bounded_bad_extension import extension_clauses

def make_formula(G,bound=2):
 clauses,ni,nk=extension_clauses(G);m=len(clauses)
 relax=list(range(43,43+m));hard=[c+[r] for c,r in zip(clauses,relax)]
 card=CardEnc.atmost(lits=relax,bound=bound,top_id=42+m,encoding=EncType.seqcounter)
 hard.extend(card.clauses)
 return clauses,hard,card.nv

def cost(clauses,S):
 bad=[]
 for i,c in enumerate(clauses):
  if not any((lit>0 and lit-1 in S) or (lit<0 and -lit-1 not in S) for lit in c):bad.append(i)
 return bad

def extend(G,S):
 H=G.copy();H.add_node(42);H.add_edges_from((42,v) for v in S);return H

def bad5(H):
 A=[0]*43
 for u,v in H.edges():A[u]|=1<<v;A[v]|=1<<u
 out=[]
 for S in combinations(range(43),5):
  mask=sum(1<<v for v in S)
  twice=sum((A[v]&mask).bit_count() for v in S)
  if twice==0:out.append((S,'I'))
  elif twice==20:out.append((S,'K'))
 return out

def classify(graphs):
 classes=[]
 for rec,H in graphs:
  placed=False
  for c in classes:
   if H.number_of_edges()==c['graph'].number_of_edges() and sorted(dict(H.degree()).values())==sorted(dict(c['graph'].degree()).values()) and nx.is_isomorphic(H,c['graph']):
    c['members'].append(rec);placed=True;break
  if not placed:classes.append({'graph':H,'members':[rec]})
 return classes

Gs=list(nx.read_graph6('../data/r55_42some.g6'));allgraphs=[];summary={};t0=time.perf_counter()
for idx in [41,255]:
 clauses,hard,nv=make_formula(Gs[idx]);models=[]
 with Solver(name='glucose4',bootstrap_with=hard) as s:
  while s.solve():
   model=s.get_model();S={v for v in range(42) if v+1 in model};bad=cost(clauses,S)
   assert len(bad)<=2
   H=extend(Gs[idx],S);b=bad5(H);assert len(b)==len(bad)
   rec={'base_index':idx,'neighbor_set':sorted(S),'new_degree':len(S),'bad5':[[list(x),col] for x,col in b]}
   models.append(rec);allgraphs.append((rec,H))
   s.add_clause([-(v+1) if v in S else v+1 for v in range(42)])
 summary[str(idx)]={'labeled_projected_models':len(models),'models':models}
 print(idx,len(models),flush=True)
classes=classify(allgraphs)
outclasses=[]
for i,c in enumerate(classes):
 H=c['graph'];outclasses.append({'class':i,'edges':H.number_of_edges(),
  'degree_sequence':sorted(dict(H.degree()).values()),'members':c['members'],
  'graph6':nx.to_graph6_bytes(H,header=False).decode().strip()})
res={'elapsed_seconds':time.perf_counter()-t0,'per_base':summary,'isomorphism_classes':outclasses}
Path('../results/two_bad_extension_enumeration.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({'elapsed_seconds':res['elapsed_seconds'],'counts':{k:v['labeled_projected_models'] for k,v in summary.items()},'classes':len(classes),'class_sizes':[len(c['members']) for c in outclasses]},indent=2))
