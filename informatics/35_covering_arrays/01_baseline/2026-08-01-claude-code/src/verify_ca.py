#!/usr/bin/env python3
"""Independent covering-array verifier. A CSV is a CA(N;t,k,v) iff every t of the k
columns shows all v^t symbol combinations. Self-certifying and cheap.

Usage: verify_ca.py <csv> t k v
"""
from __future__ import annotations
import csv, itertools, json, sys
from pathlib import Path

def load(p):
    rows = []
    for r in csv.reader(open(p)):
        r = [x for x in r if x.strip() != '']
        if not r:
            continue
        try:
            rows.append([int(x) for x in r])
        except ValueError:
            continue
    return rows

def check(A, t, k, v):
    assert all(len(r) == k for r in A), "row width mismatch"
    assert all(0 <= x < v for r in A for x in r), "symbol out of range"
    missing = 0; nsub = 0
    for cols in itertools.combinations(range(k), t):
        seen = {tuple(row[c] for c in cols) for row in A}
        nsub += 1
        missing += v ** t - len(seen)
    return len(A), nsub, missing

def main():
    path = Path(sys.argv[1]); t, k, v = map(int, sys.argv[2:5])
    A = load(path)
    N, nsub, missing = check(A, t, k, v)
    ok = (missing == 0)
    print(f"{path.name}: N={N}, {k} cols, strength {t}, {nsub} column-{t}-subsets, "
          f"missing={missing} -> {'VALID CA (CAN(%d,%d,%d) <= %d)' % (t,k,v,N) if ok else 'INVALID'}")
    outdir = Path(__file__).resolve().parents[1] / "certificates"
    outdir.mkdir(exist_ok=True)
    (outdir / f"verify_{path.stem}.json").write_text(json.dumps(
        dict(file=path.name, N=N, t=t, k=k, v=v, subsets=nsub,
             missing_interactions=missing, valid=ok,
             upper_bound=f"CAN({t},{k},{v}) <= {N}" if ok else None), indent=2))
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())
