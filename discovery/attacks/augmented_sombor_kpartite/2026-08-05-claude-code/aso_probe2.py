#!/usr/bin/env python3
"""Probe 2 of Conjecture 4.1 (arXiv:2606.26509v2): non-complete k-partite graphs.

The ASO edge term f(du,dv) = sqrt((du^2+dv^2)/(du+dv-2)) is NOT monotone in du:
d/dx (x^2+c^2)/(x+c-2) < 0 when x < 2-c+sqrt(2c^2-4c+4). So deleting edges can in
principle raise ASO. Tests:
  (a) delete one edge from T_n(k);
  (b) hill-climb on edge toggles inside a fixed k-partition, starting from T_n(k)
      and from random k-partite graphs.
"""
import math
import random


def aso_from_adj(adj, n):
    deg = [len(adj[i]) for i in range(n)]
    tot = 0.0
    for u in range(n):
        for v in adj[u]:
            if v > u:
                den = deg[u] + deg[v] - 2
                if den <= 0:
                    return None
                tot += math.sqrt((deg[u] ** 2 + deg[v] ** 2) / den)
    return tot


def turan(n, k):
    part = [i % k for i in range(n)]
    adj = [set() for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            if part[u] != part[v]:
                adj[u].add(v)
                adj[v].add(u)
    return adj, part


def delete_one_edge_test(nmax=40):
    print("=== (a) delete one edge from T_n(k) ===")
    found = False
    for k in range(2, 6):
        for n in range(k + 1, nmax + 1):
            adj, part = turan(n, k)
            base = aso_from_adj(adj, n)
            if base is None:
                continue
            edges = [(u, v) for u in range(n) for v in adj[u] if v > u]
            for (u, v) in edges:
                adj[u].discard(v); adj[v].discard(u)
                val = aso_from_adj(adj, n)
                adj[u].add(v); adj[v].add(u)
                if val is not None and val > base + 1e-9:
                    print(f"  VIOLATION n={n} k={k}: T_n(k) ASO={base:.9f} -> delete edge "
                          f"({u},{v}) ASO={val:.9f}")
                    found = True
                    break
            if found:
                break
        if found:
            break
    if not found:
        print(f"  no single-edge deletion beats T_n(k) for k<=5, n<={nmax}")


def hill_climb(n, k, part, adj, iters=20000, rng=None):
    """Toggle edges (respecting the k-partition) greedily to maximize ASO."""
    rng = rng or random.Random(0)
    cur = aso_from_adj(adj, n)
    if cur is None:
        cur = -1.0
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n) if part[u] != part[v]]
    improved = True
    while improved:
        improved = False
        rng.shuffle(pairs)
        for (u, v) in pairs:
            if v in adj[u]:
                adj[u].discard(v); adj[v].discard(u)
            else:
                adj[u].add(v); adj[v].add(u)
            val = aso_from_adj(adj, n)
            if val is not None and val > cur + 1e-12:
                cur = val
                improved = True
            else:
                if v in adj[u]:
                    adj[u].discard(v); adj[v].discard(u)
                else:
                    adj[u].add(v); adj[v].add(u)
    return cur


def hill_climb_test(nmax=24, trials=3):
    print("\n=== (b) hill-climb over k-partite graphs (fixed partition) ===")
    found = False
    for k in range(2, 5):
        for n in range(k + 2, nmax + 1):
            adj0, part = turan(n, k)
            base = aso_from_adj(adj0, n)
            if base is None:
                continue
            # start from Turan
            adj, _ = turan(n, k)
            best = hill_climb(n, k, part, adj, rng=random.Random(1))
            # random restarts
            for t in range(trials):
                rng = random.Random(100 + t)
                adjr = [set() for _ in range(n)]
                for u in range(n):
                    for v in range(u + 1, n):
                        if part[u] != part[v] and rng.random() < 0.7:
                            adjr[u].add(v); adjr[v].add(u)
                best = max(best, hill_climb(n, k, part, adjr, rng=rng))
            if best > base + 1e-7:
                print(f"  VIOLATION n={n} k={k}: T_n(k) ASO={base:.9f} < hill-climb best {best:.9f}")
                found = True
            else:
                print(f"  n={n:>3} k={k}: max = T_n(k) = {base:.6f}  (climb {best:.6f})")
    if not found:
        print("  no k-partite graph found beating T_n(k) in range")


if __name__ == "__main__":
    delete_one_edge_test()
    hill_climb_test()
