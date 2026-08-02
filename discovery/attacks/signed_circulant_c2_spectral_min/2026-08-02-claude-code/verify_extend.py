#!/usr/bin/env python3
"""Independent extension of Conjecture 3, arXiv:2607.18334 (Suvagiya).

Conjecture 3: for the 4-regular circulant C_n(1,2) on Z/nZ (edges of step 1 and 2),
the minimum over all edge-signings (equivalently switching classes) of the spectral
radius of the signed adjacency matrix equals
    rho_minus(n) = 2*sqrt(cos(pi/n)^2 + cos(2*pi/n)^2)   for every even n >= 8.
The source reports exhaustive verification through n=18. This script re-derives it
independently and pushes to n>18.

This is a SEPARATE implementation from the scout checker (checkers/check_signed_circulant.py):
different bit indexing, batched eigvalsh, its own matrix build. Agreement on the
n=8..18 overlap is the cross-check; n=20,22,24 is the new range.

Encoding (spanning-tree gauge): the step-1 path edges (i,i+1), i=0..n-2, are fixed +1
(they form a spanning tree, so switching gauges them positive). The n+1 free edges are
the wrap edge (n-1,0) and the n step-2 edges (i,i+2 mod n). Bit b of the integer index
selects the sign of free edge b (bit=1 -> -1). Enumerating index 0..2^(n+1)-1 covers
every switching class exactly once.
"""
from __future__ import annotations

import argparse
import math
import time

import numpy as np


def target(n: int) -> float:
    return 2.0 * math.sqrt(math.cos(math.pi / n) ** 2 + math.cos(2.0 * math.pi / n) ** 2)


def free_edges(n: int):
    """Ordered list of the n+1 free edges: wrap edge, then the n step-2 edges."""
    edges = [(n - 1, 0)]
    edges += [(i, (i + 2) % n) for i in range(n)]
    return edges


def scan(n: int, batch_bits: int = 15, tol: float = 1e-9):
    if n < 8 or n % 2:
        raise ValueError("n must be even and >= 8")
    t = target(n)
    nbits = n + 1
    total = 1 << nbits
    batch = 1 << batch_bits
    fe = free_edges(n)
    path = [(i, i + 1) for i in range(n - 1)]

    best = math.inf
    best_idx = -1
    counter = None  # (rho, index) if any class strictly below target

    for start in range(0, total, batch):
        end = min(start + batch, total)
        idx = np.arange(start, end, dtype=np.int64)
        b = end - start
        A = np.zeros((b, n, n), dtype=np.float64)
        for (u, v) in path:  # spanning-tree edges, always +1
            A[:, u, v] = 1.0
            A[:, v, u] = 1.0
        for bit, (u, v) in enumerate(fe):
            s = 1.0 - 2.0 * ((idx >> bit) & 1).astype(np.float64)  # bit=1 -> -1
            A[:, u, v] = s
            A[:, v, u] = s
        ev = np.linalg.eigvalsh(A)                     # ascending, shape (b, n)
        rho = np.maximum(ev[:, -1], -ev[:, 0])         # spectral radius per class
        j = int(np.argmin(rho))
        if rho[j] < best:
            best = float(rho[j])
            best_idx = int(idx[j])
        below = np.nonzero(rho < t - tol)[0]
        if below.size:
            jj = int(below[0])
            counter = (float(rho[jj]), int(idx[jj]))
            break
    return {
        "n": n,
        "classes": total,
        "target": t,
        "min_spectral_radius": best,
        "min_index_bits": format(best_idx, f"0{nbits}b") if best_idx >= 0 else None,
        "abs_error_vs_target": abs(best - t),
        "holds": counter is None and abs(best - t) <= 1e-6,
        "counterexample": None if counter is None
        else {"spectral_radius": counter[0], "index_bits": format(counter[1], f"0{nbits}b"),
              "gap_below_target": t - counter[0]},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ns", nargs="+", type=int, help="even orders n to scan")
    ap.add_argument("--batch-bits", type=int, default=15)
    ap.add_argument("--tol", type=float, default=1e-9)
    args = ap.parse_args()
    for n in args.ns:
        t0 = time.time()
        r = scan(n, batch_bits=args.batch_bits, tol=args.tol)
        r["seconds"] = round(time.time() - t0, 2)
        verdict = "COUNTEREXAMPLE" if r["counterexample"] else ("holds" if r["holds"] else "CHECK")
        print(f"n={r['n']:3d}  classes={r['classes']:>12,d}  "
              f"min_rho={r['min_spectral_radius']:.15f}  target={r['target']:.15f}  "
              f"abs_err={r['abs_error_vs_target']:.2e}  {verdict}  ({r['seconds']}s)")
        if r["counterexample"]:
            print("   COUNTEREXAMPLE:", r["counterexample"])


if __name__ == "__main__":
    main()
