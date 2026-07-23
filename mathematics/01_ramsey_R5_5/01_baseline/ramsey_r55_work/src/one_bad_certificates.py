#!/usr/bin/env python3
"""Generate DRUP proofs that each known 42-vertex graph has no extension with <=1 bad K5."""
from pathlib import Path
import argparse,hashlib,json
import networkx as nx
from pysat.solvers import Solver
from bounded_bad_extension import extension_clauses

def amo1(variables,top):
 n=len(variables)
 if n<=1:return [],top
 s=list(range(top+1,top+n)) # n-1 sequential variables
 cs=[[-variables[0],s[0]]]
 for i in range(1,n-1):
  cs += [[-variables[i],s[i]],[-s[i-1],s[i]],[-variables[i],-s[i-1]]]
 cs += [[-variables[-1],-s[-1]]]
 return cs,s[-1]

def formula(G):
 base,ni,nk=extension_clauses(G);m=len(base)
 r=list(range(43,43+m))
 cs=[c+[rv] for c,rv in zip(base,r)]
 amo,top=amo1(r,42+m);cs+=amo
 return cs,top,ni,nk

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--start',type=int,default=0);ap.add_argument('--end',type=int,default=None)
 ap.add_argument('--out',type=Path,default=Path('../proofs/one_bad'));args=ap.parse_args()
 args.out.mkdir(parents=True,exist_ok=True);Gs=list(nx.read_graph6('../data/r55_42some.g6'));end=len(Gs) if args.end is None else min(args.end,len(Gs));manifest=[]
 for i in range(args.start,end):
  cs,nv,ni,nk=formula(Gs[i])
  with Solver(name='glucose4',bootstrap_with=cs,with_proof=True) as s:
   if s.solve():raise RuntimeError(f'index {i} has <=1 bad extension')
   proof=s.get_proof()
  p=args.out/f'onebad_{i:03d}.drup';p.write_text('\n'.join(proof)+'\n')
  manifest.append({'index':i,'variables':nv,'clauses':len(cs),'proof_lines':len(proof),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
  if i%50==0:print(i,flush=True)
 Path(args.out/f'manifest_{args.start}_{end}.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print(json.dumps({'start':args.start,'end':end,'proofs':len(manifest),'lines':sum(x['proof_lines'] for x in manifest)},indent=2))
if __name__=='__main__':main()
