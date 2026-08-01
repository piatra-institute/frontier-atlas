#!/usr/bin/env python3
"""Certified upper bound a(d) <= K for caps in AG(d,3), with an independently
checked DRAT proof.

Encode "a cap of size >= K+1 containing the affine frame {0,e_1,...,e_d} exists"
as CNF and show UNSAT with CaDiCaL, then check the DRAT proof with drat-trim.
Frame-fixing is WLOG because any cap larger than a(d-1) affinely spans, so
K+1 > a(d-1) is required and asserted. A "VERIFIED" from drat-trim makes the bound
proof-checked, not merely solver-attested. The frame-WLOG lemma is the only
non-SAT premise.

Usage:  sat_cap_bound.py <cadical> <drat-trim> <outdir> <dims> <time_limit_s>
        e.g. sat_cap_bound.py cadical tools/drat-trim proofs 2,3,4 300
"""
from __future__ import annotations
import json, subprocess, sys, time
from pathlib import Path
from pysat.card import CardEnc, EncType

Q = 3
KNOWN = {1: 2, 2: 4, 3: 9, 4: 20, 5: 45, 6: 112}

def points(d):
    return [tuple((i // Q**k) % Q for k in range(d)) for i in range(Q**d)]

def lines(pts):
    idx = {p: i for i, p in enumerate(pts)}
    seen, out = set(), []
    for i, x in enumerate(pts):
        for j in range(i + 1, len(pts)):
            z = tuple((-(a + b)) % Q for a, b in zip(x, pts[j]))
            t = frozenset((i, j, idx[z]))
            if len(t) == 3 and t not in seen:
                seen.add(t); out.append(tuple(sorted(t)))
    return out

def frame(pts, d):
    idx = {p: i for i, p in enumerate(pts)}
    fr = [idx[tuple([0]*d)]]
    for k in range(d):
        e = [0]*d; e[k] = 1; fr.append(idx[tuple(e)])
    return fr

def build_cnf(d, K):
    pts = points(d); npt = len(pts); L = lines(pts); fr = frame(pts, d)
    var = lambda i: i + 1
    clauses = [[-var(a), -var(b), -var(c)] for a, b, c in L]   # no affine line fully chosen
    clauses += [[var(i)] for i in fr]                          # frame chosen (WLOG)
    card = CardEnc.atleast(lits=[var(i) for i in range(npt)], bound=K + 1,
                           top_id=npt, encoding=EncType.seqcounter)
    clauses += [list(c) for c in card.clauses]
    return clauses, max(npt, card.nv), npt, len(L)

def write_dimacs(path, clauses, nv):
    with open(path, "w") as f:
        f.write(f"p cnf {nv} {len(clauses)}\n")
        for c in clauses:
            f.write(" ".join(map(str, c)) + " 0\n")

def certify(d, cadical, drat_trim, outdir, time_limit):
    K = KNOWN[d]
    assert K + 1 > KNOWN[d - 1], "frame-fixing not WLOG unless K+1 > a(d-1)"
    clauses, nv, npt, nlin = build_cnf(d, K)
    cnf = outdir / f"ag{d}_no{K+1}cap.cnf"; drat = outdir / f"ag{d}_no{K+1}cap.drat"
    write_dimacs(cnf, clauses, nv)
    t0 = time.time()
    try:
        p = subprocess.run([str(cadical), str(cnf), str(drat)],
                           capture_output=True, text=True, timeout=time_limit)
        out = p.stdout
    except subprocess.TimeoutExpired:
        out = ""
    dt = time.time() - t0
    res = ("UNSAT" if "s UNSATISFIABLE" in out else
           "SAT" if "s SATISFIABLE" in out else "timeout")
    rec = dict(d=d, K=K, points=npt, lines=nlin, clauses=len(clauses),
               solve_seconds=round(dt, 1), result=res)
    if res != "UNSAT":
        print(f"a({d}) <= {K}: {res} ({dt:.1f}s) -- not certified")
        return rec
    c = subprocess.run([str(drat_trim), str(cnf), str(drat)],
                       capture_output=True, text=True, timeout=time_limit)
    rec["drat_trim"] = "VERIFIED" if "s VERIFIED" in c.stdout else "FAILED"
    rec["proof_bytes"] = drat.stat().st_size
    print(f"a({d}) <= {K}: UNSAT ({dt:.1f}s, {npt} vars, {nlin} lines, "
          f"{len(clauses)} clauses) -> drat-trim: {rec['drat_trim']} "
          f"(proof {rec['proof_bytes']//1024} KB)")
    return rec

def main():
    cadical, drat_trim = sys.argv[1], Path(sys.argv[2])
    outdir = Path(sys.argv[3]); outdir.mkdir(parents=True, exist_ok=True)
    dims = [int(x) for x in sys.argv[4].split(",")] if len(sys.argv) > 4 else [2, 3, 4]
    tl = float(sys.argv[5]) if len(sys.argv) > 5 else 300.0
    recs = [certify(d, cadical, drat_trim, outdir, tl) for d in dims]
    (outdir.parent / "certificates" / "sat_bounds.json").write_text(json.dumps(recs, indent=2))
    print("wrote certificates/sat_bounds.json")

if __name__ == "__main__":
    main()
