#!/usr/bin/env python3
"""Preflight benchmark for dihedral quotienting of signed C_n(1,2) switching classes.

This does not search for a counterexample. It measures only the representation reduction
claimed in the Stage-0 search edge. Switching classes use the same gauge as
check_signed_circulant.py: n-1 step-1 path edges positive, then one wrap bit and n
step-2 bits.
"""
from __future__ import annotations

import argparse
import json
import random
import time
from typing import Callable

import numpy as np

from check_signed_circulant import matrix_from_bits, spectral_radius


def edge_key(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def edge_bits_from_int(n: int, x: int) -> dict[tuple[int, int], int]:
    """Return edge sign bits (0 positive, 1 negative) in the fixed gauge."""
    e: dict[tuple[int, int], int] = {}
    for i in range(n - 1):
        e[(i, i + 1)] = 0
    e[(0, n - 1)] = (x >> 0) & 1
    for i in range(n):
        e[edge_key(i, (i + 2) % n)] = (x >> (i + 1)) & 1
    expected = 2 * n
    if len(e) != expected:
        raise RuntimeError(f"support collision: expected {expected} edges, got {len(e)}")
    return e


def transform_class(n: int, x: int, sign: int, shift: int) -> int:
    """Apply v -> sign*v+shift mod n, then restore the fixed switching gauge."""
    original = edge_bits_from_int(n, x)
    transformed: dict[tuple[int, int], int] = {}
    for (u, v), bit in original.items():
        pu = (sign * u + shift) % n
        pv = (sign * v + shift) % n
        transformed[edge_key(pu, pv)] = bit

    # Switching bits s_v force each path edge (i,i+1), i<n-1, positive.
    switch = [0] * n
    for i in range(n - 1):
        edge_bit = transformed[(i, i + 1)]
        switch[i + 1] = switch[i] ^ edge_bit

    def normalized(u: int, v: int) -> int:
        return transformed[edge_key(u, v)] ^ switch[u] ^ switch[v]

    y = normalized(0, n - 1) << 0
    for i in range(n):
        y |= normalized(i, (i + 2) % n) << (i + 1)
    return y


def basis_images(n: int, sign: int, shift: int) -> list[int]:
    width = n + 1
    zero = transform_class(n, 0, sign, shift)
    if zero != 0:
        raise RuntimeError("dihedral action unexpectedly affine rather than linear")
    return [transform_class(n, 1 << j, sign, shift) for j in range(width)]


def make_lut(images: list[int], start: int, length: int) -> list[int]:
    table = [0] * (1 << length)
    for value in range(1, 1 << length):
        low = value & -value
        j = low.bit_length() - 1
        table[value] = table[value ^ low] ^ images[start + j]
    return table



def gf2_rank(rows: list[int]) -> int:
    rows = [r for r in rows if r]
    rank = 0
    while rows:
        pivot = max(rows, key=int.bit_length)
        rows.remove(pivot)
        bit = 1 << (pivot.bit_length() - 1)
        rows = [q for r in rows if (q := (r ^ pivot if r & bit else r))]
        rank += 1
    return rank


def burnside_orbit_count(n: int) -> int:
    width = n + 1
    actions: set[tuple[int, ...]] = set()
    for sign in (1, -1):
        for shift in range(n):
            actions.add(tuple(basis_images(n, sign, shift)))
    fixed_total = 0
    for images in actions:
        rows = []
        for out_bit in range(width):
            row = 0
            for in_bit, image in enumerate(images):
                if (image >> out_bit) & 1:
                    row |= 1 << in_bit
            row ^= 1 << out_bit  # (T-I)x=0; minus equals plus over GF(2).
            rows.append(row)
        nullity = width - gf2_rank(rows)
        fixed_total += 1 << nullity
    if fixed_total % len(actions):
        raise RuntimeError("Burnside average is not integral")
    return fixed_total // len(actions)

def action_tables(n: int) -> list[tuple[list[int], list[int]]]:
    width = n + 1
    split = min(10, width)
    out = []
    seen = set()
    for sign in (1, -1):
        for shift in range(n):
            images = basis_images(n, sign, shift)
            key = tuple(images)
            if key in seen:
                continue
            seen.add(key)
            out.append((make_lut(images, 0, split), make_lut(images, split, width - split)))
    return out


def canonical(x: int, tables: list[tuple[list[int], list[int]]], split: int) -> int:
    lo = x & ((1 << split) - 1)
    hi = x >> split
    return min(a[lo] ^ b[hi] for a, b in tables)


def bits_string(n: int, x: int) -> str:
    # Translate internal field bits to the checker's left-to-right bit string.
    return ''.join('1' if (x >> j) & 1 else '0' for j in range(n + 1))


def validate_action(n: int, tables: list[tuple[list[int], list[int]]], samples: int = 12) -> None:
    width = n + 1
    split = min(10, width)
    rng = random.Random(260718334 + n)
    identity = canonical(0, tables, split)
    if identity != 0:
        raise RuntimeError("zero class not fixed")
    for _ in range(samples):
        x = rng.randrange(1 << width)
        rho = spectral_radius(matrix_from_bits(n, bits_string(n, x)))
        lo = x & ((1 << split) - 1)
        hi = x >> split
        for a, b in rng.sample(tables, min(4, len(tables))):
            y = a[lo] ^ b[hi]
            rho_y = spectral_radius(matrix_from_bits(n, bits_string(n, y)))
            if not np.isclose(rho, rho_y, rtol=0.0, atol=1e-10):
                raise RuntimeError(f"spectral radius changed under action: {rho} vs {rho_y}")


def benchmark(n: int) -> dict:
    if n < 8 or n % 2:
        raise ValueError("n must be even and at least 8")
    start = time.perf_counter()
    tables = action_tables(n)
    validate_action(n, tables)
    setup_seconds = time.perf_counter() - start
    width = n + 1
    split = min(10, width)
    total = 1 << width
    t0 = time.perf_counter()
    orbit_count = sum(canonical(x, tables, split) == x for x in range(total))
    enumeration_seconds = time.perf_counter() - t0
    burnside_count = burnside_orbit_count(n)
    if burnside_count != orbit_count:
        raise RuntimeError(f"canonical count {orbit_count} disagrees with Burnside count {burnside_count}")
    return {
        "n": n,
        "switching_classes": total,
        "distinct_dihedral_actions_on_classes": len(tables),
        "dihedral_orbits": orbit_count,
        "burnside_orbits": burnside_count,
        "orbit_count_matches_burnside": True,
        "reduction_factor": total / orbit_count,
        "setup_seconds": setup_seconds,
        "enumeration_seconds": enumeration_seconds,
        "spectral_invariance_samples_passed": True,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("n", nargs="+", type=int)
    args = ap.parse_args()
    rows = [benchmark(n) for n in args.n]
    print(json.dumps({"rows": rows}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
