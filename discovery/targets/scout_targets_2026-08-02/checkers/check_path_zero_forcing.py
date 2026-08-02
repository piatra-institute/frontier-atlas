#!/usr/bin/env python3
"""Exact coefficient checker for z(G;k) <= z(P_n;k)."""
from __future__ import annotations
import argparse,json
from pathlib import Path
import networkx as nx
from graph_utils import graph_from_graph6, zero_forcing_set_count

def check(payload):
    g=graph_from_graph6(payload['graph6']); k=int(payload['k']); p=nx.path_graph(g.number_of_nodes())
    zg=zero_forcing_set_count(g,k); zp=zero_forcing_set_count(p,k)
    return {"n":g.number_of_nodes(),"k":k,"z_G_k":zg,"z_Pn_k":zp,"difference":zg-zp,"counterexample":zg>zp}
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('payload',type=Path); a=ap.parse_args()
    print(json.dumps(check(json.loads(a.payload.read_text())),indent=2,sort_keys=True))
