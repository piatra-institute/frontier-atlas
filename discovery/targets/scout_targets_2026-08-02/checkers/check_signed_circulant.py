#!/usr/bin/env python3
"""Checker and B0 replay for Conjecture 3 of arXiv:2607.18334.

A switching class is represented by fixing the step-1 path edges
(0,1),...,(n-2,n-1) positive. The free bits encode the wrap edge
(n-1,0), followed by the n step-2 edges (i,i+2 mod n).
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Iterable

import numpy as np
import sympy as sp


def target(n: int) -> float:
    return 2.0 * math.sqrt(math.cos(math.pi / n) ** 2 + math.cos(2 * math.pi / n) ** 2)


def matrix_from_bits(n: int, bits: str) -> np.ndarray:
    if n < 8 or n % 2:
        raise ValueError("n must be even and at least 8")
    if len(bits) != n + 1 or set(bits) - {"0", "1"}:
        raise ValueError(f"bits must be a binary string of length {n+1}")
    a = np.zeros((n, n), dtype=np.int64)
    for i in range(n - 1):
        a[i, i + 1] = a[i + 1, i] = 1
    sign = -1 if bits[0] == "1" else 1
    a[n - 1, 0] = a[0, n - 1] = sign
    for i in range(n):
        j = (i + 2) % n
        sign = -1 if bits[i + 1] == "1" else 1
        a[i, j] = a[j, i] = sign
    return a


def spectral_radius(a: np.ndarray) -> float:
    vals = np.linalg.eigvalsh(a.astype(float))
    return float(np.max(np.abs(vals)))


def exact_root_interval(a: np.ndarray, digits: int = 40) -> tuple[sp.Rational, sp.Rational]:
    """Rational interval enclosing the spectral radius of an integer symmetric matrix."""
    x = sp.Symbol("x")
    p = sp.Poly(sp.Matrix(a.tolist()).charpoly(x).as_expr(), x, domain=sp.ZZ)
    eps = sp.Rational(1, 10**digits)
    intervals = p.intervals(eps=eps)
    real_intervals: list[tuple[sp.Rational, sp.Rational]] = []
    for (lo, hi), multiplicity in intervals:
        for _ in range(multiplicity):
            real_intervals.append((sp.Rational(lo), sp.Rational(hi)))
    if len(real_intervals) != a.shape[0]:
        raise RuntimeError("not all roots isolated as real")
    lower = max(min(abs(lo), abs(hi)) if lo * hi > 0 else sp.Rational(0) for lo, hi in real_intervals)
    upper = max(max(abs(lo), abs(hi)) for lo, hi in real_intervals)
    return lower, upper


def all_bits(width: int) -> Iterable[str]:
    for x in range(1 << width):
        yield format(x, f"0{width}b")


def baseline(ns: list[int]) -> dict:
    rows = []
    for n in ns:
        best = math.inf
        best_bits = None
        for bits in all_bits(n + 1):
            rho = spectral_radius(matrix_from_bits(n, bits))
            if rho < best:
                best, best_bits = rho, bits
        rows.append({
            "n": n,
            "classes": 1 << (n + 1),
            "minimum": best,
            "target": target(n),
            "absolute_error": abs(best - target(n)),
            "optimizer_bits": best_bits,
            "pass_1e-9": abs(best - target(n)) <= 1e-9,
        })
    return {"baseline": rows, "all_pass": all(r["pass_1e-9"] for r in rows)}


def check_payload(payload: dict, certify: bool) -> dict:
    n = int(payload["n"])
    bits = str(payload["bits"])
    a = matrix_from_bits(n, bits)
    rho = spectral_radius(a)
    t = target(n)
    out = {
        "n": n,
        "bits": bits,
        "spectral_radius_float": rho,
        "conjectured_minimum_float": t,
        "gap_rho_minus_target": rho - t,
        "counterexample_at_1e-10": rho < t - 1e-10,
        "support_ok": True,
    }
    if certify:
        lo, hi = exact_root_interval(a)
        out["spectral_radius_exact_interval"] = [str(lo), str(hi)]
        out["interval_width_float"] = float(hi - lo)
        # High-precision target evaluation is supplementary; a claimed witness must have a gap
        # much larger than both this numerical uncertainty and the rational root interval width.
        out["certification_rule"] = "accept only if exact spectral-radius upper bound < 100-digit target lower estimate"
        out["target_100_digits"] = str(sp.N(2 * sp.sqrt(sp.cos(sp.pi/n)**2 + sp.cos(2*sp.pi/n)**2), 100))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("payload", nargs="?", type=Path)
    ap.add_argument("--baseline", nargs="+", type=int)
    ap.add_argument("--certify", action="store_true")
    args = ap.parse_args()
    if args.baseline:
        print(json.dumps(baseline(args.baseline), indent=2, sort_keys=True))
        return
    if args.payload is None:
        ap.error("payload JSON is required unless --baseline is used")
    payload = json.loads(args.payload.read_text())
    print(json.dumps(check_payload(payload, args.certify), indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
