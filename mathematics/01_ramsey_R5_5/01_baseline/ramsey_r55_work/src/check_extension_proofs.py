#!/usr/bin/env python3
"""Independent, standard-library checker for the archived extension proofs.

It decodes graph6 without NetworkX, reconstructs each extension CNF via direct
4-subset enumeration (not the generator's clique routine), verifies each input
has neither K5 nor an independent 5-set, then replays every proof as DRUP using
reverse unit propagation.  Clause deletions, if present, are conservatively
ignored; retaining clauses cannot make an invalid RUP step valid.
"""
from __future__ import annotations
from itertools import combinations
from pathlib import Path
import argparse, hashlib, json, sys, time


def decode_graph6(line: bytes) -> list[int]:
    s=line.strip()
    if not s: raise ValueError('empty graph6 line')
    vals=[b-63 for b in s]
    if any(v<0 or v>63 for v in vals): raise ValueError('invalid graph6 byte')
    if vals[0] <= 62:
        n=vals[0]; payload=vals[1:]
    elif len(vals)>=4 and vals[1] != 63:
        n=(vals[1]<<12)|(vals[2]<<6)|vals[3]; payload=vals[4:]
    else:
        raise ValueError('large graph6 orders are not needed by this checker')
    needed=n*(n-1)//2
    bits=[]
    for v in payload:
        bits.extend((v>>shift)&1 for shift in (5,4,3,2,1,0))
    if len(bits)<needed: raise ValueError('truncated graph6 payload')
    adj=[0]*n; p=0
    for j in range(1,n):
        for i in range(j):
            if bits[p]:
                adj[i]|=1<<j; adj[j]|=1<<i
            p+=1
    return adj


def complement(adj: list[int]) -> list[int]:
    allv=(1<<len(adj))-1
    return [allv ^ (1<<v) ^ adj[v] for v in range(len(adj))]


def contains_clique(adj: list[int], k: int) -> bool:
    n=len(adj)
    def search(candidates: int, depth: int) -> bool:
        if depth==k: return True
        need=k-depth
        while candidates.bit_count()>=need:
            b=candidates & -candidates
            candidates ^= b
            v=b.bit_length()-1
            if search(candidates & adj[v],depth+1): return True
        return False
    return search((1<<n)-1,0)


def extension_cnf_direct(adj: list[int]) -> list[tuple[int,int]]:
    """Return clauses as (positive-mask, negative-mask)."""
    clauses=[]
    for a,b,c,d in combinations(range(len(adj)),4):
        ab=(adj[a]>>b)&1; ac=(adj[a]>>c)&1; ad=(adj[a]>>d)&1
        bc=(adj[b]>>c)&1; bd=(adj[b]>>d)&1; cd=(adj[c]>>d)&1
        total=ab+ac+ad+bc+bd+cd
        mask=(1<<a)|(1<<b)|(1<<c)|(1<<d)
        if total==0: clauses.append((mask,0))      # x_a or x_b or x_c or x_d
        elif total==6: clauses.append((0,mask))    # not x_a or ... or not x_d
    return clauses


def parse_proof(path: Path):
    for lineno,line in enumerate(path.read_text().splitlines(),1):
        line=line.strip()
        if not line: continue
        deletion=line.startswith('d ')
        if deletion: line=line[2:]
        pos=neg=0; terminated=False
        for token in line.split():
            lit=int(token)
            if lit==0: terminated=True; break
            if not 1<=abs(lit)<=42:
                raise ValueError(f'{path}:{lineno}: literal out of range')
            if lit>0: pos|=1<<(lit-1)
            else: neg|=1<<(-lit-1)
        if not terminated: raise ValueError(f'{path}:{lineno}: missing 0')
        yield deletion,(pos,neg),lineno


def is_rup(formula: list[tuple[int,int]], candidate: tuple[int,int]) -> bool:
    pos,neg=candidate
    # Assume the negation of the candidate clause.
    ones=neg; zeros=pos
    if ones & zeros: return True
    assigned=ones|zeros
    while True:
        changed=False
        for cp,cn in formula:
            if (cp&ones) or (cn&zeros): continue
            remaining=(cp|cn)&~assigned
            if remaining==0: return True
            if remaining & (remaining-1)==0:
                if cp & remaining:
                    if zeros & remaining: return True
                    if not (ones & remaining):
                        ones|=remaining; assigned|=remaining; changed=True
                else:
                    if ones & remaining: return True
                    if not (zeros & remaining):
                        zeros|=remaining; assigned|=remaining; changed=True
        if not changed: return False


def check_one(index: int, adj: list[int], proof_path: Path) -> dict:
    if len(adj)!=42: raise ValueError(f'graph {index}: expected 42 vertices')
    if contains_clique(adj,5): raise ValueError(f'graph {index}: contains K5')
    if contains_clique(complement(adj),5): raise ValueError(f'graph {index}: contains independent 5-set')
    formula=extension_cnf_direct(adj)
    additions=deletions=0
    empty_seen=False
    for deletion,clause,lineno in parse_proof(proof_path):
        if deletion:
            deletions+=1
            continue  # conservative: keep the clause in formula
        if not is_rup(formula,clause):
            raise ValueError(f'{proof_path}:{lineno}: non-RUP addition')
        formula.append(clause); additions+=1
        if clause==(0,0): empty_seen=True
    if not empty_seen: raise ValueError(f'{proof_path}: proof has no empty clause')
    return {'index':index,'base_clauses':len(extension_cnf_direct(adj)),
            'proof_additions':additions,'proof_deletions_ignored':deletions}


def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--graphs',type=Path,default=Path('../data/r55_42some.g6'))
    ap.add_argument('--proof-dir',type=Path,default=Path('../proofs'))
    ap.add_argument('--start',type=int,default=0)
    ap.add_argument('--end',type=int,default=None)
    args=ap.parse_args()
    lines=[x for x in args.graphs.read_bytes().splitlines() if x.strip()]
    end=len(lines) if args.end is None else min(args.end,len(lines))
    t=time.perf_counter(); results=[]
    for i in range(args.start,end):
        adj=decode_graph6(lines[i])
        results.append(check_one(i,adj,args.proof_dir/f'ext_{i:03d}.drup'))
    elapsed=time.perf_counter()-t
    print(json.dumps({'status':'VERIFIED','start':args.start,'end':end,
                      'graphs_checked':len(results),'seconds':elapsed,
                      'proof_additions':sum(x['proof_additions'] for x in results)},indent=2))
    return 0

if __name__=='__main__': raise SystemExit(main())
