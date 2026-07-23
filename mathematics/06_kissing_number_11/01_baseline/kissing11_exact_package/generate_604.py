#!/usr/bin/env python3
"""Generate an exact 604-point spherical code in R^11 over Q(sqrt(2)).

Storage convention: each coordinate is [a,b], meaning (a+b*sqrt(2))/3.
Thus every code vector has squared norm 4, equivalently scaled squared norm 36.
"""
from __future__ import annotations
import hashlib, json
from itertools import combinations, product
from pathlib import Path

PAIRS = [(0, 6), (1, 4), (2, 5), (3, 7)]
TRIPLE_FAMILIES = [
    [(1,2,3),(4,5,7),(0,2,7),(3,5,6),(0,3,4),(1,6,7),(0,1,5),(2,4,6)],
    [(1,2,7),(3,4,5),(0,5,7),(2,3,6),(0,1,3),(4,6,7),(0,2,4),(1,5,6)],
    [(1,3,5),(2,4,7),(0,2,3),(5,6,7),(0,1,7),(3,4,6),(0,4,5),(1,2,6)],
]
U_NUM = [(2,1,2),(2,-2,-1),(1,2,-2)]  # u_j = U_NUM[j]/3


def make_code():
    vectors, labels = [], []

    # Six 4-subsets formed by unions of two PAIRS.
    supports = []
    for i,j in combinations(range(4),2):
        supports.append(tuple(sorted(PAIRS[i] + PAIRS[j])))
    # Twenty-four supports T union {8+k}: one 8-triple family per layer.
    for k,fam in enumerate(TRIPLE_FAMILIES):
        supports.extend(tuple(sorted(T + (8+k,))) for T in fam)

    # B: 16 signed coordinate axes on the first 8 coordinates.
    for i in range(8):
        for s in (-1,1):
            v = [[0,0] for _ in range(11)]
            v[i] = [6*s,0]
            vectors.append(v); labels.append(f"B_axis_{i}_{s:+d}")

    # B: all 16 signings of each 4-support, 30*16=480 vectors.
    for si,S in enumerate(supports):
        for signs in product((-1,1), repeat=4):
            v = [[0,0] for _ in range(11)]
            for idx,s in zip(S,signs):
                v[idx] = [3*s,0]
            vectors.append(v)
            labels.append(f"B_support_{si:02d}_{''.join('+' if s>0 else '-' for s in signs)}")

    # E1: +/-e_a +/-e_b +/-sqrt(2)u_j, 4*4*6=96 vectors.
    for pi,(a,b) in enumerate(PAIRS):
        for sa,sb in product((-1,1), repeat=2):
            for j,num in enumerate(U_NUM):
                for su in (-1,1):
                    v = [[0,0] for _ in range(11)]
                    v[a] = [3*sa,0]; v[b] = [3*sb,0]
                    for t,n in enumerate(num):
                        v[8+t] = [0,su*n]
                    vectors.append(v)
                    labels.append(f"E1_pair{pi}_{sa:+d}{sb:+d}_u{j}_{su:+d}")

    # E2: sqrt(2)(+/-u_i +/-u_j), 3*4=12 vectors.
    for i,j in combinations(range(3),2):
        for si,sj in product((-1,1), repeat=2):
            v = [[0,0] for _ in range(11)]
            for t in range(3):
                v[8+t] = [0,si*U_NUM[i][t] + sj*U_NUM[j][t]]
            vectors.append(v)
            labels.append(f"E2_u{i}_{si:+d}_u{j}_{sj:+d}")

    assert len(vectors) == 604
    return vectors, labels, supports


def main():
    outdir = Path(__file__).resolve().parent
    vectors, labels, supports = make_code()
    payload = {
        "field": "Q(sqrt(2))",
        "coordinate_encoding": "[a,b] denotes (a+b*sqrt(2))/3",
        "dimension": 11,
        "cardinality": 604,
        "target_squared_norm": 4,
        "vectors": vectors,
        "labels": labels,
        "pair_partition": PAIRS,
        "triple_families": TRIPLE_FAMILIES,
        "supports": supports,
        "u_numerators": U_NUM,
    }
    data = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    path = outdir / "construction_604.json"
    path.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    (outdir / "construction_604.sha256").write_text(f"{digest}  construction_604.json\n")
    print(path)
    print(digest)

if __name__ == "__main__":
    main()
