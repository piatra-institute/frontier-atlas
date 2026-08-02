#!/usr/bin/env python3
"""Exact small-graph checker for chi(G) <= Z(G)/2 + 2 on triangle-free graphs."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import networkx as nx
from graph_utils import graph_from_graph6, chromatic_number, zero_forcing_number


def check(payload: dict) -> dict:
    g = graph_from_graph6(payload["graph6"])
    tf = sum(nx.triangles(g).values()) == 0
    chi = chromatic_number(g)
    z = zero_forcing_number(g)
    return {
        "n": g.number_of_nodes(), "m": g.number_of_edges(), "triangle_free": tf,
        "chi": chi, "Z": z, "lhs_2chi": 2*chi, "rhs_Z_plus_4": z+4,
        "counterexample": bool(tf and 2*chi > z+4),
    }

if __name__ == "__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("payload", type=Path); a=ap.parse_args()
    print(json.dumps(check(json.loads(a.payload.read_text())), indent=2, sort_keys=True))
