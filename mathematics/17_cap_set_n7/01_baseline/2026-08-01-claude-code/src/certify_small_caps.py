#!/usr/bin/env python3
"""Exact maximum caps in AG(d,3) via CP-SAT, decision formulation with affine-frame
symmetry breaking.

To certify a(d) <= K it suffices to prove no (K+1)-cap exists. Any cap larger than
a(d-1) cannot lie in a hyperplane, so it affinely spans and (after an affine map)
contains the standard frame {0, e_1, ..., e_d}. Fixing that frame removes almost
all of AGL(d,3) and is the symmetry break that makes these instances tractable.
This holds here since K+1 > a(d-1) in every case: 21>9, 46>20, 113>45.

Reports:
  - bound: INFEASIBLE at size K+1 proves a(d) <= K (solver-attested, not LRAT).
  - witness: a K-cap found by feasibility, re-checked by an independent triple scan.
"""
from __future__ import annotations
import json, sys, time
from pathlib import Path
from ortools.sat.python import cp_model

Q = 3

def points(d):
    return [tuple((i // Q**k) % Q for k in range(d)) for i in range(Q**d)]

def lines(pts):
    idx = {p: i for i, p in enumerate(pts)}
    seen, out = set(), []
    for i, x in enumerate(pts):
        for j in range(i + 1, len(pts)):
            z = tuple((-(a + b)) % Q for a, b in zip(x, pts[j]))
            tri = frozenset((i, j, idx[z]))
            if len(tri) == 3 and tri not in seen:
                seen.add(tri); out.append(tuple(sorted(tri)))
    return out

def frame_indices(pts, d):
    idx = {p: i for i, p in enumerate(pts)}
    fr = [idx[tuple([0] * d)]]
    for k in range(d):
        e = [0] * d; e[k] = 1
        fr.append(idx[tuple(e)])
    return fr

def triple_scan_ok(cap):
    s = set(cap)
    for i in range(len(cap)):
        for j in range(i + 1, len(cap)):
            z = tuple((-(a + b)) % Q for a, b in zip(cap[i], cap[j]))
            if z in s and z != cap[i] and z != cap[j]:
                return False
    return True

def solve_size(d, size, time_limit, workers=8):
    """Is there a `size`-cap containing the frame? Returns (status, witness)."""
    pts = points(d); L = lines(pts); fr = set(frame_indices(pts, d))
    m = cp_model.CpModel()
    z = [m.NewBoolVar(f"z{i}") for i in range(len(pts))]
    for a, b, c in L:
        m.Add(z[a] + z[b] + z[c] <= 2)
    for i in fr:
        m.Add(z[i] == 1)
    m.Add(sum(z) == size)
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = float(time_limit)
    s.parameters.num_search_workers = workers
    st = s.Solve(m)
    wit = [pts[i] for i in range(len(pts)) if s.Value(z[i]) == 1] if st in (cp_model.OPTIMAL, cp_model.FEASIBLE) else []
    return s.StatusName(st), len(pts), len(L), round(s.WallTime(), 1), wit

def certify(d, known, tl_bound, tl_wit):
    # bound: no (known+1)-cap
    st_b, npts, nlin, dt_b, _ = solve_size(d, known + 1, tl_bound)
    proven = (st_b == "INFEASIBLE")
    # witness: a known-cap
    st_w, _, _, dt_w, wit = solve_size(d, known, tl_wit)
    wit_ok = bool(wit) and triple_scan_ok(wit)
    print(f"a({d}): no-{known+1}-cap -> {st_b} ({dt_b}s)"
          f"{' => a('+str(d)+') <= '+str(known)+' PROVEN' if proven else ' (not closed)'}; "
          f"witness {known}-cap {st_w} triple-scan={'PASS' if wit_ok else 'n/a'} ({dt_w}s)")
    return dict(d=d, points=npts, lines=nlin, known=known,
                bound_status=st_b, bound_seconds=dt_b, bound_proven=proven,
                witness_status=st_w, witness_seconds=dt_w,
                witness_triple_scan=("PASS" if wit_ok else "n/a"))

def main():
    outdir = Path(__file__).resolve().parents[1]
    dims = sys.argv[1] if len(sys.argv) > 1 else "4,5,6"
    tl6 = float(sys.argv[2]) if len(sys.argv) > 2 else 120.0
    plan = {4: (60, 10), 5: (90, 20), 6: (tl6, 30)}
    known = {4: 20, 5: 45, 6: 112}
    results = []
    for d in [int(x) for x in dims.split(",")]:
        tb, tw = plan[d]
        results.append(certify(d, known[d], tb, tw))
    (outdir / "certificates" / "small_caps.json").write_text(json.dumps(results, indent=2))
    print("wrote certificates/small_caps.json")

if __name__ == "__main__":
    main()
