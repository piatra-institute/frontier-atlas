#!/usr/bin/env python3
"""Generate DRUP certificates for one-vertex extension CNFs.

Generator dependencies: networkx and python-sat.  The independent checker in
check_extension_proofs.py uses only the Python standard library and does not
share this generator's graph/CNF implementation.
"""
from pathlib import Path
import argparse, hashlib, json
import networkx as nx
from pysat.solvers import Solver


def adjacency_bits(g):
    a=[0]*g.number_of_nodes()
    for u,v in g.edges:
        a[u]|=1<<v; a[v]|=1<<u
    return a


def complement(a):
    allv=(1<<len(a))-1
    return [allv ^ (1<<v) ^ a[v] for v in range(len(a))]


def k_cliques(a,k):
    result=[]
    def visit(candidates, chosen):
        if len(chosen)==k:
            result.append(tuple(chosen)); return
        need=k-len(chosen)
        while candidates.bit_count()>=need:
            bit=candidates & -candidates
            candidates ^= bit
            v=bit.bit_length()-1
            visit(candidates & a[v], chosen+[v])
    visit((1<<len(a))-1,[])
    return result


def extension_cnf(g):
    a=adjacency_bits(g)
    k4=k_cliques(a,4)
    i4=k_cliques(complement(a),4)
    # x_v=1 means the new vertex is adjacent to v.
    # An independent 4-set needs at least one x_v=1.
    # A clique 4-set needs at least one x_v=0.
    clauses=[[v+1 for v in q] for q in i4]
    clauses += [[-(v+1) for v in q] for q in k4]
    return clauses


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--graphs',type=Path,default=Path('../data/r55_42some.g6'))
    ap.add_argument('--proof-dir',type=Path,default=Path('../proofs'))
    args=ap.parse_args()
    args.proof_dir.mkdir(parents=True,exist_ok=True)
    graphs=list(nx.read_graph6(args.graphs))
    manifest=[]
    for i,g in enumerate(graphs):
        clauses=extension_cnf(g)
        with Solver(name='glucose4',bootstrap_with=clauses,with_proof=True) as solver:
            sat=solver.solve()
            if sat:
                raise RuntimeError(f'graph {i} unexpectedly extends: {solver.get_model()}')
            proof=solver.get_proof()
        path=args.proof_dir/f'ext_{i:03d}.drup'
        path.write_text('\n'.join(proof)+'\n')
        manifest.append({'index':i,'clauses':len(clauses),'proof_lines':len(proof),
                         'proof_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    out=args.proof_dir/'manifest.json'
    out.write_text(json.dumps(manifest,indent=2)+'\n')
    print(f'wrote {len(manifest)} proofs to {args.proof_dir}')

if __name__=='__main__': main()
