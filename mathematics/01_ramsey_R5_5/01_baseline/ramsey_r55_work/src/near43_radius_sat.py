#!/usr/bin/env python3
from pathlib import Path
from itertools import combinations
from pysat.solvers import Solver
from pysat.card import CardEnc, EncType
import argparse,time,json

def read(path):
 rows=[x.strip() for x in Path(path).read_text().splitlines() if x.strip()]
 return rows,len(rows)

def build(rows,n,r):
 pairs=list(combinations(range(n),2)); idx={p:i+1 for i,p in enumerate(pairs)}
 clauses=[]; hist=[0]*11
 for S in combinations(range(n),5):
  ps=list(combinations(S,2)); base=[rows[a][b]=='1' for a,b in ps]; e=sum(base);hist[e]+=1
  if e<=r:
   # final graph cannot have all edges 0: OR(final edge is 1)
   clauses.append([(-idx[p] if bit else idx[p]) for p,bit in zip(ps,base)])
  if 10-e<=r:
   # final graph cannot have all edges 1: OR(final edge is 0)
   clauses.append([(idx[p] if bit else -idx[p]) for p,bit in zip(ps,base)])
 card=CardEnc.atmost(lits=list(range(1,len(pairs)+1)),bound=r,top_id=len(pairs),encoding=EncType.seqcounter)
 clauses.extend(card.clauses)
 return pairs,clauses,card.nv,hist

def main():
 ap=argparse.ArgumentParser();ap.add_argument('graph',type=int);ap.add_argument('radius',type=int)
 ap.add_argument('--proof',action='store_true');args=ap.parse_args()
 rows,n=read(f'../data/near43_graph{args.graph}.matrix')
 t=time.perf_counter();pairs,clauses,nv,hist=build(rows,n,args.radius);tb=time.perf_counter()-t
 with Solver(name='glucose4',bootstrap_with=clauses,with_proof=args.proof) as s:
  ts=time.perf_counter();sat=s.solve();solve_sec=time.perf_counter()-ts
  model=s.get_model() if sat else None;proof=s.get_proof() if args.proof and not sat else None
 flips=[]
 if sat:
  positive=set(x for x in model if x>0 and x<=len(pairs));flips=[pairs[i-1] for i in sorted(positive)]
 out={'graph':args.graph,'radius':args.radius,'variables':nv,'clauses':len(clauses),
      'build_seconds':tb,'solve_seconds':solve_sec,'satisfiable':sat,'flips':flips,
      'histogram':hist,'proof_lines':len(proof) if proof else None}
 print(json.dumps(out,indent=2))
 Path(f'../results/near43_g{args.graph}_radius{args.radius}_sat.json').write_text(json.dumps(out,indent=2)+'\n')
 if proof:
  Path(f'../proofs/near43_g{args.graph}_radius{args.radius}.drup').write_text('\n'.join(proof)+'\n')

if __name__=='__main__':main()
