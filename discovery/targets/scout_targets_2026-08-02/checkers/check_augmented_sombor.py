#!/usr/bin/env python3
"""Checker for a k-partite graph exceeding/equalling the Turan ASO value."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
from graph_utils import graph_from_graph6, turan_graph, validate_partition


def aso(g) -> float:
    d=dict(g.degree())
    total=0.0
    for u,v in g.edges():
        den=d[u]+d[v]-2
        if den <= 0:
            raise ValueError("ASO undefined on an isolated P2 component/edge with degree pair (1,1)")
        total += math.sqrt((d[u]**2+d[v]**2)/den)
    return total

def check(payload: dict) -> dict:
    g=graph_from_graph6(payload["graph6"]); k=int(payload["k"]); parts=payload["partition"]
    validate_partition(g.nodes(),parts)
    independent=all(not g.has_edge(u,v) for b in parts for i,u in enumerate(b) for v in b[i+1:])
    tg,_=turan_graph(g.number_of_nodes(),k)
    a=aso(g); t=aso(tg); tol=1e-10
    return {"n":g.number_of_nodes(),"m":g.number_of_edges(),"k":k,"valid_k_partition":independent,
            "ASO_graph":a,"ASO_Turan":t,"difference":a-t,
            "strict_counterexample":bool(independent and a>t+tol),
            "equality_case":bool(independent and abs(a-t)<=tol)}
if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("payload",type=Path); a=ap.parse_args()
    print(json.dumps(check(json.loads(a.payload.read_text())),indent=2,sort_keys=True))
