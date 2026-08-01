#!/usr/bin/env python3
"""Deterministic simulated-annealing provenance for the CA(13;2,8,3) witness.

The witness is independently certified by the coverage checkers; this heuristic
is provenance only and is not part of the proof of optimality.
"""
from __future__ import annotations

import csv
import math
import random
import sys
import time
from pathlib import Path

N, K, V = 13, 8, 3


def score_array(a: list[list[int]]) -> tuple[int, dict[tuple[int, int], list[int]]]:
    counts: dict[tuple[int, int], list[int]] = {}
    missing = 0
    for i in range(K):
        for j in range(i + 1, K):
            c = [0] * 9
            for row in a:
                c[3 * row[i] + row[j]] += 1
            counts[(i, j)] = c
            missing += sum(x == 0 for x in c)
    return missing, counts


def search(seed: int = 123, restarts: int = 50, steps: int = 300_000) -> tuple[list[list[int]], int, int]:
    rng = random.Random(seed)
    for restart in range(restarts):
        a = [[rng.randrange(V) for _ in range(K)] for _ in range(N)]
        score, counts = score_array(a)
        for step in range(steps):
            if score == 0:
                return a, restart, step
            r = rng.randrange(N)
            c = rng.randrange(K)
            old = a[r][c]
            new = rng.randrange(V - 1)
            if new >= old:
                new += 1

            delta = 0
            changes: list[tuple[tuple[int, int], int, int]] = []
            for d in range(K):
                if d == c:
                    continue
                i, j = (c, d) if c < d else (d, c)
                if c < d:
                    old_index = 3 * old + a[r][d]
                    new_index = 3 * new + a[r][d]
                else:
                    old_index = 3 * a[r][d] + old
                    new_index = 3 * a[r][d] + new
                pair_counts = counts[(i, j)]
                delta += int(pair_counts[old_index] == 1) - int(pair_counts[new_index] == 0)
                changes.append(((i, j), old_index, new_index))

            phase = (step % 20_000) / 20_000
            temperature = 0.05 + 0.8 * (1.0 - phase)
            accept = (
                delta < 0
                or (delta == 0 and rng.random() < 0.5)
                or (delta > 0 and rng.random() < math.exp(-delta / temperature))
            )
            if accept:
                a[r][c] = new
                for key, old_index, new_index in changes:
                    counts[key][old_index] -= 1
                    counts[key][new_index] += 1
                score += delta
    raise RuntimeError("search budget exhausted without a covering array")


def main() -> int:
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("upper_search_reproduction.csv")
    started = time.perf_counter()
    array, restart, step = search()
    elapsed = time.perf_counter() - started
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow([f"c{i}" for i in range(K)])
        writer.writerows(array)
    print(f"seed=123")
    print(f"restart={restart}")
    print(f"step={step}")
    print(f"elapsed_seconds={elapsed:.6f}")
    print(f"output={output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
