#!/usr/bin/env python3
"""Exact enumeration checker for the full-bunkbed arboreal-gas inequality on small graphs."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import networkx as nx
from graph_utils import graph_from_graph6


def bunkbed(g):
    h=nx.Graph(); h.add_nodes_from((v,l) for v in g.nodes() for l in (0,1))
    for u,v in g.edges():
        h.add_edge((u,0),(v,0)); h.add_edge((u,1),(v,1))
    for v in g.nodes(): h.add_edge((v,0),(v,1))
    return h

def check(payload):
    g=graph_from_graph6(payload['graph6']); u=int(payload['u']); v=int(payload['v'])
    lam=Fraction(str(payload['lambda']))
    if lam <= 0:
        raise ValueError('lambda must be positive')
    if u not in g or v not in g:
        raise ValueError('u and v must be vertices of the base graph')
    h=bunkbed(g); edges=list(h.edges())
    if len(edges)>24: raise ValueError('checker guard: at most 24 bunkbed edges')
    den=Fraction(0); same=Fraction(0); cross=Fraction(0); forests=0
    for mask in range(1<<len(edges)):
        f=nx.Graph(); f.add_nodes_from(h.nodes()); chosen=[]
        for i,e in enumerate(edges):
            if mask>>i&1: chosen.append(e)
        f.add_edges_from(chosen)
        if not nx.is_forest(f): continue
        forests+=1; w=lam**len(chosen); den+=w
        if nx.has_path(f,(u,0),(v,0)): same+=w
        if nx.has_path(f,(u,0),(v,1)): cross+=w
    return {"base_n":g.number_of_nodes(),"bunkbed_edges":len(edges),"forests":forests,
            "lambda":str(lam),"same_weight":str(same),"cross_weight":str(cross),"normalizer":str(den),
            "difference_weight":str(same-cross),"counterexample":same<cross}
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('payload',type=Path); a=ap.parse_args()
    print(json.dumps(check(json.loads(a.payload.read_text())),indent=2,sort_keys=True))
