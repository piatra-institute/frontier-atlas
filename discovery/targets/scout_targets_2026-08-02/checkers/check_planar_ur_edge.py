#!/usr/bin/env python3
"""Partial checker for uniquely-restricted edge-colouring certificates.
It validates planarity and a supplied colouring. It intentionally does not certify UNSAT
for 2*Delta+4 colours; therefore the target card's checker gate is red.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import networkx as nx
from graph_utils import graph_from_graph6

def unique_perfect_matching(h,m):
    # For small colour classes, enumerate perfect matchings of the induced endpoint graph.
    endpoints=set(x for e in m for x in e); z=h.subgraph(endpoints)
    count=0
    def rec(rem,chosen):
        nonlocal count
        if count>1:return
        if not rem: count+=1; return
        u=min(rem)
        for v in z.neighbors(u):
            if v in rem:
                rec(rem-{u,v},chosen+[(u,v)])
    rec(set(endpoints),[])
    return count==1

def check(payload):
    g=graph_from_graph6(payload['graph6']); coloring={tuple(sorted(map(int,k.split('-')))):int(v) for k,v in payload['coloring'].items()}
    if set(coloring)!=set(tuple(sorted(e)) for e in g.edges()): raise ValueError('colouring must cover every edge exactly')
    proper=True; ur=True
    for c in set(coloring.values()):
        es=[e for e,x in coloring.items() if x==c]
        if len(set(x for e in es for x in e))!=2*len(es): proper=False
        if not unique_perfect_matching(g,es): ur=False
    planar,_=nx.check_planarity(g); D=max(dict(g.degree()).values(),default=0)
    return {"planar":planar,"Delta":D,"colors_used":len(set(coloring.values())),"proper":proper,
            "uniquely_restricted":ur,"valid_upper_certificate":planar and proper and ur,
            "note":"No lower-bound/UNSAT proof is checked by this script."}
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('payload',type=Path); a=ap.parse_args()
    print(json.dumps(check(json.loads(a.payload.read_text())),indent=2,sort_keys=True))
