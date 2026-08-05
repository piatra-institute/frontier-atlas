#!/usr/bin/env python3
"""Probe Conjecture 4.1 of arXiv:2606.26509v2 (Xu, Das, Bera).

Conjecture: for any k-partite graph G of order n, ASO(G) <= ASO(T_n(k)),
equality iff G = T_n(k) (balanced complete k-partite).

ASO(G) = sum_{uv in E} sqrt( (d_u^2 + d_v^2) / (d_u + d_v - 2) ).

Complete k-partite graphs are k-partite, so it suffices to compare ASO over all
partitions of n into k parts. For parts (n_1..n_k), a vertex in part i has degree
n - n_i, and there are n_i*n_j edges between parts i and j.
"""
import math
from itertools import count


def aso_complete_multipartite(parts, n):
    tot = 0.0
    k = len(parts)
    for i in range(k):
        di = n - parts[i]
        for j in range(i + 1, k):
            dj = n - parts[j]
            den = di + dj - 2
            if den <= 0:
                return None
            tot += parts[i] * parts[j] * math.sqrt((di * di + dj * dj) / den)
    return tot


def partitions_into_k(n, k, minpart=1):
    """All (sorted desc) partitions of n into exactly k parts >= minpart."""
    if k == 1:
        if n >= minpart:
            yield (n,)
        return
    for first in range(minpart, n - minpart * (k - 1) + 1):
        for rest in partitions_into_k(n - first, k - 1, first):
            yield (first,) + rest


def balanced(n, k):
    q, r = divmod(n, k)
    return tuple(sorted([q + 1] * r + [q] * (k - r)))


def main():
    print(f"{'n':>4} {'k':>3} {'balanced ASO':>16} {'best ASO':>16} {'best partition':>22} {'VIOLATION':>10}")
    violations = []
    for k in range(2, 7):
        for n in range(k, 61):
            bal = balanced(n, k)
            bal_v = aso_complete_multipartite(bal, n)
            if bal_v is None:
                continue
            best_v, best_p = bal_v, bal
            for p in partitions_into_k(n, k):
                v = aso_complete_multipartite(p, n)
                if v is None:
                    continue
                if v > best_v + 1e-12:
                    best_v, best_p = v, p
            viol = best_p != bal and best_v > bal_v + 1e-9
            if viol:
                violations.append((n, k, bal, bal_v, best_p, best_v))
                print(f"{n:>4} {k:>3} {bal_v:>16.9f} {best_v:>16.9f} {str(best_p):>22} {'YES':>10}")
    print()
    if violations:
        print(f"COUNTEREXAMPLES FOUND: {len(violations)}")
        n, k, bal, bv, bp, bpv = violations[0]
        print(f"smallest: n={n} k={k}  balanced {bal} ASO={bv:.12f}  vs  {bp} ASO={bpv:.12f}"
              f"  gap={bpv-bv:.12f}")
    else:
        print("no violation among complete k-partite graphs, n<=60, k<=6")


if __name__ == "__main__":
    main()
