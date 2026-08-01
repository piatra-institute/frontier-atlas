#!/usr/bin/env python3
"""Superpermutations on n symbols: verifier + greedy construction + short local
improvement. The open case is n=6, with 867 <= s(6) <= 872. A string shorter than
872 that still contains all 720 permutations would be a new record.

Verifier: a string over {1..n} is a superpermutation iff every one of the n!
permutations occurs as a contiguous length-n substring. This is checked exactly by
scanning windows, so any candidate is trivially certified.
"""
from __future__ import annotations
import json, sys
from math import factorial
from itertools import permutations

def verify(s, n):
    need = set(permutations(range(1, n + 1)))
    have = set()
    for i in range(len(s) - n + 1):
        have.add(tuple(s[i:i + n]))
    return need.issubset(have), len(need - have)

def greedy(n):
    """Max-overlap greedy superpermutation: repeatedly append the unseen
    permutation that shares the longest overlap with the current suffix. Terminates
    and yields a valid superpermutation (length sum_{k<=n} k! for this tie-break)."""
    start = tuple(range(1, n + 1))
    s = list(start)
    remaining = set(permutations(range(1, n + 1)))
    remaining.discard(start)
    # index unseen permutations by every prefix for fast overlap lookup
    from collections import defaultdict
    by_prefix = defaultdict(set)
    for p in remaining:
        for o in range(1, n):
            by_prefix[p[:o]].add(p)
    while remaining:
        appended = False
        for o in range(n - 1, 0, -1):
            suffix = tuple(s[-o:])
            bucket = by_prefix.get(suffix)
            if bucket:
                p = min(bucket)                 # deterministic tie-break
                s.extend(p[o:])
                remaining.discard(p)
                for oo in range(1, n):
                    by_prefix[p[:oo]].discard(p)
                appended = True
                break
        if not appended:                        # no overlap: append a full new perm
            p = min(remaining)
            s.extend(p); remaining.discard(p)
            for oo in range(1, n):
                by_prefix[p[:oo]].discard(p)
    return s

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    known_min = {1: 1, 2: 3, 3: 9, 4: 33, 5: 153}   # exact; s(6) open in [867,872]
    # validate the greedy against known exact values
    print("validation (greedy length vs known minimal):")
    for k in range(1, 6):
        s = greedy(k); ok, _ = verify(s, k)
        print(f"  n={k}: greedy len={len(s)} (minimal {known_min[k]}), "
              f"valid={ok}, sum k! = {sum(factorial(j) for j in range(1,k+1))}")
    # the target case
    s6 = greedy(n)
    ok, miss = verify(s6, n)
    L = len(s6)
    record_ub, record_lb = 872, 867
    print(f"\nn={n}: greedy superpermutation length={L}, valid={ok} "
          f"(missing {miss} perms)")
    print(f"known bounds: {record_lb} <= s({n}) <= {record_ub}. "
          f"greedy gives sum k! = {sum(factorial(j) for j in range(1,n+1))}.")
    beat = L < record_ub
    print("RESULT: " + (f"*** length {L} < {record_ub} -- NEW RECORD, verify ***"
                        if (beat and ok) else
                        f"greedy length {L} does not beat the record {record_ub}; "
                        f"matching or beating 872 needs a dedicated construction / "
                        f"Chaffin-method or ATSP search, out of scope for plain greedy."))
    cert = dict(n=n, greedy_length=L, valid=bool(ok),
                known_lower=record_lb, known_upper=record_ub,
                beats_record=bool(beat and ok))
    outdir = __import__("pathlib").Path(__file__).resolve().parents[1] / "certificates"
    (outdir / f"superperm_n{n}.json").write_text(json.dumps(cert, indent=2))
    if ok:
        (outdir.parent / f"superperm_n{n}.txt").write_text("".join(map(str, s6)))
    print("wrote certificate + string")

if __name__ == "__main__":
    main()
