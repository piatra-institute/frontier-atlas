#!/usr/bin/env python3
"""Certify which known 42-vertex representatives admit <=2 bad-K5 extensions."""
from pathlib import Path
import argparse,hashlib,json
import networkx as nx
from pysat.solvers import Solver
from bounded_bad_extension import extension_clauses
from near_radius_certificates import atmost_seq

def formula(G):
 base,ni,nk=extension_clauses(G);m=len(base);relax=list(range(43,43+m))
 cs=[c+[r] for c,r in zip(base,relax)]
 card,nv=atmost_seq(relax,2,42+m);cs+=card
 return base,cs,nv,ni,nk

def exact_cost(base,model):
 S={x-1 for x in model if 1<=x<=42}
 bad=sum(not any((lit>0 and lit-1 in S) or (lit<0 and -lit-1 not in S) for lit in c) for c in base)
 return bad,sorted(S)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('start',type=int);ap.add_argument('end',type=int);args=ap.parse_args()
 out=Path('../proofs/two_bad');out.mkdir(parents=True,exist_ok=True)
 Gs=list(nx.read_graph6('../data/r55_42some.g6'));manifest=[]
 for i in range(args.start,min(args.end,len(Gs))):
  base,cs,nv,ni,nk=formula(Gs[i])
  with Solver(name='glucose4',bootstrap_with=cs,with_proof=True) as s:
   sat=s.solve()
   if sat:
    bad,S=exact_cost(base,s.get_model());assert bad<=2
    rec={'index':i,'status':'SAT','bad':bad,'neighbor_set':S,'variables':nv,'clauses':len(cs)}
   else:
    proof=s.get_proof();p=out/f'twobad_{i:03d}.drup';p.write_text('\n'.join(proof)+'\n')
    rec={'index':i,'status':'UNSAT','variables':nv,'clauses':len(cs),'proof_lines':len(proof),
         'proof_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
  manifest.append(rec)
  if i%25==0:print(i,rec['status'],flush=True)
 (out/f'manifest_{args.start}_{args.end}.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print(json.dumps({'start':args.start,'end':args.end,'sat':[x['index'] for x in manifest if x['status']=='SAT'],
                   'unsat':sum(x['status']=='UNSAT' for x in manifest),
                   'proof_lines':sum(x.get('proof_lines',0) for x in manifest)},indent=2))
if __name__=='__main__':main()
