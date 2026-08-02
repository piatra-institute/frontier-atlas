#!/usr/bin/env python3
"""Exact local-complementation and condensation checker for small labeled graphs."""
from __future__ import annotations
import argparse, json
from collections import deque
from pathlib import Path
from graph_utils import graph_from_graph6, graph6


def lc(g,v):
    h=g.copy(); nbr=list(h.neighbors(v))
    for i,u in enumerate(nbr):
        for w in nbr[i+1:]:
            if h.has_edge(u,w): h.remove_edge(u,w)
            else: h.add_edge(u,w)
    return h

def condense(g,C:set[int]):
    outside=sorted(set(g.nodes())-C); c=max(g.nodes(),default=-1)+1
    h=g.subgraph(outside).copy(); h.add_node(c)
    for u in outside:
        if any(g.has_edge(u,s) for s in C): h.add_edge(u,c)
    # canonical relabel preserves outside ordering then c
    mapping={v:i for i,v in enumerate(outside+[c])}
    return __import__('networkx').relabel_nodes(h,mapping,copy=True)
def orbit(g,cap=200000):
    start=graph6(g); seen={start}; q=deque([g])
    while q:
        h=q.popleft()
        for v in h.nodes():
            z=lc(h,v); key=graph6(z)
            if key not in seen:
                seen.add(key); q.append(z)
                if len(seen)>cap: raise RuntimeError("orbit cap exceeded")
    return seen
def condition(g,C:set[int])->bool:
    outside=set(g.nodes())-C
    return all(sum(1 for u in outside if g.has_edge(v,u))<=1 for v in C)
def check(payload):
    g=graph_from_graph6(payload['G_graph6']); gp=graph_from_graph6(payload['Gprime_graph6']); C=set(payload['C'])
    if g.number_of_nodes()!=gp.number_of_nodes(): raise ValueError('order mismatch')
    seq=payload.get('lc_sequence',[]); h=g
    for v in seq: h=lc(h,int(v))
    seq_proof=graph6(h)==graph6(gp)
    og=orbit(g); equivalent=graph6(gp) in og
    cg=condense(g,C); cgp=condense(gp,C); oc=orbit(cg); condensed_equiv=graph6(cgp) in oc
    return {"condition_G":condition(g,C),"condition_Gprime":condition(gp,C),
            "sequence_proves_original_equivalence":seq_proof,"originals_LC_equivalent":equivalent,
            "condensed_LC_equivalent":condensed_equiv,
            "counterexample":bool(condition(g,C) and condition(gp,C) and equivalent and not condensed_equiv),
            "original_orbit_size":len(og),"condensed_orbit_size":len(oc)}
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('payload',type=Path); a=ap.parse_args()
    print(json.dumps(check(json.loads(a.payload.read_text())),indent=2,sort_keys=True))
