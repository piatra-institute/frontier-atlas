#!/usr/bin/env python3
"""Nonlocal search for a 237-cap in AG(7,3) (a new lower-bound record if found).

The known 236-cap is complete, so no point extends it; a 237-cap needs
rearrangement. This fixes the set size at 237 and minimizes the number of fully
selected affine lines E(A) by point swaps. E=0 means a 237-cap, which would beat
the 236 record. Honest odds are low; this runs the correct search and reports the
minimum violation count reached (the denominator).

A line is a triple {p,x,y} with p+x+y=0 mod 3. E(A) = number of such triples in A.
"""
from __future__ import annotations
import csv, random, sys, time
from pathlib import Path

Q, DIM, NP = 3, 7, 3**7
pts = [tuple((i // Q**k) % Q for k in range(DIM)) for i in range(NP)]
idof = {p: i for i, p in enumerate(pts)}

def third(i, j):
    a, b = pts[i], pts[j]
    return idof[tuple((-(a[k] + b[k])) % Q for k in range(DIM))]

def lines_through(p, A):
    """Number of lines {p,x,y} with x,y in A\\{p}, counted once (x<y)."""
    c = 0
    for x in A:
        if x == p:
            continue
        y = third(p, x)
        if x < y and y in A:
            c += 1
    return c

def energy(A):
    return sum(lines_through(p, A) for p in A) // 3

def descent(A, budget, rng):
    A = set(A); E = energy(A); best = E
    t0 = time.time()
    while time.time() - t0 < budget and E > 0:
        p = rng.choice(tuple(A))
        q = rng.randrange(NP)
        if q in A:
            continue
        lp = lines_through(p, A)
        A.discard(p)
        lq = lines_through(q, A)
        newE = E - lp + lq
        if newE <= E:                       # accept improving or equal
            A.add(q); E = newE; best = min(best, E)
        else:
            A.add(p)                         # revert
    return A, E, best

def load_cap(path):
    with open(path, newline="") as f:
        rows = list(csv.reader(f))
    return [idof[tuple(map(int, r))] for r in rows[1:]]

def main():
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 240.0
    rng = random.Random(20260801)
    base = load_cap(Path(__file__).resolve().parents[1] / "data" / "cf236.csv")
    print(f"loaded 236-cap (E={energy(set(base))}, expect 0)")
    overall_best = 999; found = None; restarts = 0
    per = 30.0
    t0 = time.time()
    while time.time() - t0 < budget and overall_best > 0:
        restarts += 1
        if restarts % 2 == 1:               # seed A: 236-cap + 1 random outside
            outside = [i for i in range(NP) if i not in set(base)]
            A0 = base + [rng.choice(outside)]
        else:                               # seed A: random 237-set
            A0 = rng.sample(range(NP), 237)
        A, E, best = descent(A0, per, rng)
        overall_best = min(overall_best, best)
        if E == 0:
            found = sorted(A)
            break
        print(f"  restart {restarts}: min E={best} (overall best {overall_best})")
    if found:
        print(f"\n*** 237-CAP FOUND (E=0) -- NEW RECORD, verify immediately ***")
        Path("found237.txt").write_text("\n".join(",".join(map(str, pts[i])) for i in found))
    else:
        print(f"\nRESULT: no 237-cap found. best min-violations={overall_best} over "
              f"{restarts} restarts in {time.time()-t0:.0f}s. Lower bound remains 236.")

if __name__ == "__main__":
    main()
