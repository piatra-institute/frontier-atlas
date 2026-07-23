#!/usr/bin/env python3
"""Generate radius-r DRUP proofs using an explicit sequential counter encoding."""
from pathlib import Path
from itertools import combinations
import argparse,json,time,hashlib
from pysat.solvers import Solver

N=43; PAIRS=list(combinations(range(N),2)); PID={p:i+1 for i,p in enumerate(PAIRS)}

def rows():return [x.strip() for x in Path('../data/near43_graph1.matrix').read_text().splitlines() if x.strip()]

def atmost_seq(xs,k,top):
 n=len(xs)
 if k>=n:return [],top
 if k==0:return [[-x] for x in xs],top
 def s(i,j):return top+(i-1)*k+j # 1<=i<=n-1,1<=j<=k
 cs=[]
 for i in range(1,n):cs.append([-xs[i-1],s(i,1)])
 for i in range(2,n):
  cs.append([-s(i-1,1),s(i,1)])
  for j in range(2,k+1):
   cs.append([-xs[i-1],-s(i-1,j-1),s(i,j)])
   cs.append([-s(i-1,j),s(i,j)])
 for i in range(2,n+1):cs.append([-xs[i-1],-s(i-1,k)])
 return cs,s(n-1,k)

def formula(r):
 R=rows();cs=[];hist=[0]*11
 for S in combinations(range(N),5):
  ps=list(combinations(S,2));bits=[R[a][b]=='1' for a,b in ps];e=sum(bits);hist[e]+=1
  if e<=r:cs.append([(-PID[p] if bit else PID[p]) for p,bit in zip(ps,bits)])
  if 10-e<=r:cs.append([(PID[p] if bit else -PID[p]) for p,bit in zip(ps,bits)])
 card,nv=atmost_seq(list(range(1,len(PAIRS)+1)),r,len(PAIRS));cs+=card
 return cs,nv,hist

def main():
 ap=argparse.ArgumentParser();ap.add_argument('radii',type=int,nargs='+');args=ap.parse_args();outdir=Path('../proofs/near_radius_seq');outdir.mkdir(parents=True,exist_ok=True)
 manifest=[]
 for r in args.radii:
  t=time.perf_counter();cs,nv,hist=formula(r);build=time.perf_counter()-t
  with Solver(name='glucose4',bootstrap_with=cs,with_proof=True) as s:
   ts=time.perf_counter();sat=s.solve();solve=time.perf_counter()-ts
   if sat:raise RuntimeError(f'radius {r} SAT')
   proof=s.get_proof()
  p=outdir/f'radius_{r}.drup';p.write_text('\n'.join(proof)+'\n')
  rec={'radius':r,'variables':nv,'clauses':len(cs),'proof_lines':len(proof),'build_seconds':build,'solve_seconds':solve,'histogram':hist,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
  manifest.append(rec);print(json.dumps(rec),flush=True)
 Path(outdir/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
if __name__=='__main__':main()
