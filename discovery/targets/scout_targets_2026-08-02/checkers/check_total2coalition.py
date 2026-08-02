#!/usr/bin/env python3
"""Certificate checker for a total-2-coalition partition beating Conjecture 1."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
from graph_utils import graph_from_graph6, validate_partition


def total2dom(g,S:set[int])->bool:
    return all(sum(v in S for v in g.neighbors(u))>=2 for u in g.nodes())

def check(payload:dict)->dict:
    g=graph_from_graph6(payload["graph6"]); blocks=[set(x) for x in payload["partition"]]
    validate_partition(g.nodes(),blocks)
    individual=[total2dom(g,b) for b in blocks]
    partners=[]
    for i,b in enumerate(blocks):
        ps=[j for j,c in enumerate(blocks) if i!=j and (not individual[i]) and (not individual[j]) and total2dom(g,b|c)]
        partners.append(ps)
    valid=all((not individual[i]) and partners[i] for i in range(len(blocks)))
    deg=[d for _,d in g.degree()]; delta=min(deg); Delta=max(deg); f=delta//2
    bound=f*(Delta-2*f+1)+math.ceil(delta/2)
    return {"n":g.number_of_nodes(),"m":g.number_of_edges(),"delta":delta,"Delta":Delta,
            "partition_size":len(blocks),"bound":bound,"individual_total2dom":individual,
            "partners":partners,"valid_total2_coalition_partition":valid,
            "counterexample_certificate":bool(valid and len(blocks)>bound)}
if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("payload",type=Path); a=ap.parse_args()
    print(json.dumps(check(json.loads(a.payload.read_text())),indent=2,sort_keys=True))
