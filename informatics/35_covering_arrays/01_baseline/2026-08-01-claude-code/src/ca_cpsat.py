#!/usr/bin/env python3
"""Exact CP-SAT search for a CA(N; t, k, v). For N < best-known, SAT is a new
record; UNSAT proves CAN(t,k,v) >= N+1 (optimality). Target CA(38;3,7,3).

Model: x[r][c] in {0..v-1}. For every t-column set and every symbol combo, at
least one row realizes it. Symmetry break: first row all zeros (WLOG by per-column
symbol permutation). A found array is re-verified exactly before being reported.
"""
from __future__ import annotations
import itertools, json, sys, time
from pathlib import Path
from ortools.sat.python import cp_model

def verify(A, t, k, v):
    for cols in itertools.combinations(range(k), t):
        seen = {tuple(row[c] for c in cols) for row in A}
        if len(seen) != v ** t:
            return False
    return True

def search(N, t, k, v, tl, workers=8):
    m = cp_model.CpModel()
    x = [[m.NewIntVar(0, v - 1, f"x{r}_{c}") for c in range(k)] for r in range(N)]
    for c in range(k):
        m.Add(x[0][c] == 0)                              # WLOG first row all zeros
    # equality booleans eq[r][c][val] = (x[r][c]==val)
    eq = [[[m.NewBoolVar(f"e{r}_{c}_{val}") for val in range(v)]
           for c in range(k)] for r in range(N)]
    for r in range(N):
        for c in range(k):
            for val in range(v):
                m.Add(x[r][c] == val).OnlyEnforceIf(eq[r][c][val])
                m.Add(x[r][c] != val).OnlyEnforceIf(eq[r][c][val].Not())
    for cols in itertools.combinations(range(k), t):
        for combo in itertools.product(range(v), repeat=t):
            row_hits = []
            for r in range(N):
                hit = m.NewBoolVar("")
                for i, c in enumerate(cols):
                    m.AddImplication(hit, eq[r][c][combo[i]])
                row_hits.append(hit)
            m.AddBoolOr(row_hits)
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = float(tl)
    s.parameters.num_search_workers = workers
    t0 = time.time()
    st = s.Solve(m)
    dt = time.time() - t0
    name = s.StatusName(st)
    A = ([[s.Value(x[r][c]) for c in range(k)] for r in range(N)]
         if st in (cp_model.OPTIMAL, cp_model.FEASIBLE) else None)
    return name, A, round(dt, 1)

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 38
    tl = float(sys.argv[2]) if len(sys.argv) > 2 else 600.0
    t, k, v = 3, 7, 3
    outdir = Path(__file__).resolve().parents[1]
    name, A, dt = search(N, t, k, v, tl)
    rec = dict(map=f"CA({N};{t},{k},{v})", status=name, seconds=dt)
    if A is not None and verify(A, t, k, v):
        rec["found"] = True; rec["record"] = (N < 39)
        (outdir / f"CA_{N}_3_7_3_cpsat.csv").write_text(
            "\n".join(",".join(map(str, row)) for row in A))
        print(f"*** CP-SAT FOUND CA({N};3,7,3) ({name}, {dt}s) -- NEW RECORD (best known 39) ***")
    elif name == "INFEASIBLE":
        rec["found"] = False; rec["proves"] = f"CAN(3,7,3) >= {N+1}"
        print(f"CP-SAT: CA({N};3,7,3) INFEASIBLE ({dt}s) -> CAN(3,7,3) >= {N+1} "
              f"(would make 39 optimal if N+1=39)")
    else:
        rec["found"] = False
        print(f"CP-SAT: {name} ({dt}s) -- no CA({N};3,7,3) found, not proven impossible")
    (outdir / "certificates" / f"ca_cpsat_N{N}.json").write_text(json.dumps(rec, indent=2))

if __name__ == "__main__":
    main()
