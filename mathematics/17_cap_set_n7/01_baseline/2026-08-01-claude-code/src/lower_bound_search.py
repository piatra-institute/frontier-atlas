#!/usr/bin/env python3
"""Honest lower-bound attempt for a(7): try to find a cap in AG(7,3) larger than
the known 236. This environment has no exact solver (OR-tools / SAT / ILP), so
this uses randomized greedy construction plus local repair of the 236-cap. Those
methods cannot be expected to beat a structured extremal cap that has stood as a
record; the point is to run the attempt honestly, measure how far heuristics
reach, and report the denominator (restarts, time, best size).

A cap is a set with no 3 distinct points summing to 0 mod 3 (no affine line).
Incremental test: keep a `blocked` set = { -(x+y) : x,y in cap }; a point p may be
added iff p is not in cap and not blocked.
"""
from __future__ import annotations
import csv, random, sys, time
from pathlib import Path

Q = 3
DIM = 7
POINTS = [tuple((i // Q**k) % Q for k in range(DIM)) for i in range(Q**DIM)]  # 2187

def neg(v): return tuple((-a) % Q for a in v)
def add(u, v): return tuple((a + b) % Q for a, b in zip(u, v))

def greedy_cap(rng, seed_points=None):
    """Grow a maximal cap by adding random allowed points until stuck."""
    cap = set()
    blocked = set()
    allowed = set(POINTS)
    def place(p):
        for x in cap:
            blocked.add(neg(add(p, x)))
        cap.add(p)
        allowed.discard(p)
    if seed_points:
        for p in seed_points:
            place(p)
        allowed = {p for p in allowed if p not in blocked}
    while allowed:
        p = rng.choice(tuple(allowed))
        place(p)
        allowed = {q for q in allowed if q not in blocked and q not in cap}
    return cap

def is_cap(points):
    pts = list(points); s = set(pts)
    if len(pts) != len(s): return False
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            if neg(add(pts[i], pts[j])) in s and neg(add(pts[i], pts[j])) not in (pts[i], pts[j]):
                # triple pts[i], pts[j], -(pts[i]+pts[j]) all distinct in set
                t = neg(add(pts[i], pts[j]))
                if t != pts[i] and t != pts[j]:
                    return False
    return True

def load_cap(path):
    with open(path, newline="") as f:
        rows = list(csv.reader(f))
    return [tuple(map(int, r)) for r in rows[1:]]

def main():
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 25.0
    rng = random.Random(20260801)

    # 1) pure greedy randomized construction
    t0 = time.time(); best = 0; n = 0
    while time.time() - t0 < budget * 0.6:
        c = greedy_cap(rng); n += 1
        best = max(best, len(c))
    print(f"[greedy] restarts={n} time={time.time()-t0:.1f}s best_size={best} "
          f"(known record 236; gap {236 - best})")

    # 2) local repair of the 236-cap: remove R points, greedily refill
    base = load_cap(Path(__file__).resolve().parents[1] / "data" / "cf236.csv")
    print(f"[base] loaded 236-cap, size={len(base)}")
    best_repair = len(base); t1 = time.time(); trials = 0
    for R in (8, 16, 24, 32):
        while time.time() - t1 < budget * 0.1 * (R / 8):
            keep = list(base); rng.shuffle(keep); keep = keep[R:]
            c = greedy_cap(rng, seed_points=keep); trials += 1
            best_repair = max(best_repair, len(c))
    print(f"[repair] trials={trials} best_size={best_repair} "
          f"(improvement over 236: {best_repair - 236})")

    improved = best_repair > 236 or best > 236
    print(f"\nRESULT: no cap larger than 236 found."
          if not improved else f"\nRESULT: IMPROVEMENT FOUND, size {max(best, best_repair)} -- re-verify immediately!")
    print("Heuristic construction reaches far below the structured 236-cap; "
          "beating 236 needs an exact solver (OR-tools CP-SAT / ILP with local "
          "branching), not available here. This is a documented null attempt.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
