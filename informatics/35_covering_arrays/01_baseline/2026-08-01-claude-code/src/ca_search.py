#!/usr/bin/env python3
"""Search for a CA(N; t, k, v) with fewer rows than the best known, i.e. a new
covering-array record. Target: CA(38; 3, 7, 3) (best known upper bound 39).

Min-conflicts + simulated annealing on a fixed N-row array, minimizing the number
of uncovered strength-t interactions. Warm-started from the CA(39) with one row
dropped (few uncovered), plus random restarts. Any array reaching 0 uncovered is a
valid covering array; a found CA(38;3,7,3) is a new record, checkable in seconds.
"""
from __future__ import annotations
import csv, itertools, json, math, random, sys, time
from pathlib import Path

K, V, T = 7, 3, 3
TRIPLES = list(itertools.combinations(range(K), T))
NT = len(TRIPLES)
TW = [[] for _ in range(K)]
for ti, tr in enumerate(TRIPLES):
    for c in tr:
        TW[c].append(ti)

def cidx(vals):
    x = 0
    for a in vals:
        x = x * V + a
    return x

def decode(ci):
    return [(ci // 9) % 3, (ci // 3) % 3, ci % 3]

class State:
    def __init__(self, A):
        self.A = [row[:] for row in A]; self.N = len(A)
        self.cov = [[0] * (V ** T) for _ in range(NT)]
        for r in range(self.N):
            for ti, tr in enumerate(TRIPLES):
                self.cov[ti][cidx([self.A[r][c] for c in tr])] += 1
        self.cost = sum(1 for ti in range(NT) for ci in range(V ** T)
                        if self.cov[ti][ci] == 0)

    def apply(self, r, c, new):
        old = self.A[r][c]
        if old == new:
            return
        for ti in TW[c]:
            tr = TRIPLES[ti]
            oc = cidx([self.A[r][cc] for cc in tr])
            self.cov[ti][oc] -= 1
            if self.cov[ti][oc] == 0:
                self.cost += 1
        self.A[r][c] = new
        for ti in TW[c]:
            tr = TRIPLES[ti]
            nc = cidx([self.A[r][cc] for cc in tr])
            if self.cov[ti][nc] == 0:
                self.cost -= 1
            self.cov[ti][nc] += 1

    def uncovered(self):
        return [(ti, ci) for ti in range(NT) for ci in range(V ** T)
                if self.cov[ti][ci] == 0]

def move(s, r, cols, vals, temp, rng):
    olds = [s.A[r][c] for c in cols]
    before = s.cost
    for c, nv in zip(cols, vals):
        s.apply(r, c, nv)
    if s.cost - before <= 0 or rng.random() < math.exp(-(s.cost - before) / temp):
        return True
    for c, ov in zip(cols, olds):
        s.apply(r, c, ov)
    return False

def repair(A0, deadline, rng):
    s = State(A0); temp = 1.5; best = s.cost
    while s.cost > 0 and time.time() < deadline:
        if rng.random() < 0.8:
            unc = s.uncovered()
            if not unc:
                break
            ti, ci = rng.choice(unc)
            move(s, rng.randrange(s.N), list(TRIPLES[ti]), decode(ci), temp, rng)
        else:
            move(s, rng.randrange(s.N), [rng.randrange(K)], [rng.randrange(V)], temp, rng)
        best = min(best, s.cost)
        temp = max(0.05, temp * 0.999985)
    return s, best

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

def main():
    budget = float(sys.argv[1]) if len(sys.argv) > 1 else 500.0
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 38
    rng = random.Random(20260801)
    outdir = Path(__file__).resolve().parents[1]
    ca39 = load(outdir / "data" / "CA_39_3_7_3.csv")
    t0 = time.time(); best_overall = 10 ** 9; found = None; starts = 0
    seeds = [[ca39[i] for i in range(len(ca39)) if i != drop][:N] for drop in range(len(ca39))]
    while time.time() - t0 < budget and best_overall > 0:
        starts += 1
        if starts <= len(seeds):
            A0 = seeds[starts - 1]
        else:
            A0 = [[rng.randrange(V) for _ in range(K)] for _ in range(N)]
        dl = min(t0 + budget, time.time() + 12.0)   # per-start slice
        s, best = repair(A0, dl, rng)
        best_overall = min(best_overall, best)
        if s.cost == 0:
            found = s.A; break
        print(f"start {starts}: best uncovered this start={best} (overall best={best_overall})",
              flush=True)
    if found:
        print(f"\n*** FOUND CA({N};3,7,3) -- NEW RECORD (best known was 39). Verify. ***", flush=True)
        (outdir / f"CA_{N}_3_7_3.csv").write_text("\n".join(",".join(map(str, row)) for row in found))
        cert = dict(map="CA(N;3,7,3)", N=N, found=True, record=(N < 39))
    else:
        print(f"\nRESULT: no CA({N};3,7,3) found. best min-uncovered={best_overall} over "
              f"{starts} starts in {time.time()-t0:.0f}s. Best known upper bound remains 39.", flush=True)
        cert = dict(map="CA(N;3,7,3)", N=N, found=False, best_uncovered=best_overall, starts=starts)
    (outdir / "certificates" / f"ca_search_N{N}.json").write_text(json.dumps(cert, indent=2))

if __name__ == "__main__":
    main()
