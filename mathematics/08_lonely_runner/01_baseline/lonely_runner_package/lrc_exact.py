#!/usr/bin/env python3
"""Exact arithmetic utilities for the Lonely Runner Conjecture.

The module contains no floating-point arithmetic.  It can:
  * evaluate ||x|| for rational x;
  * test witnesses on a prescribed 1/d grid;
  * compute the exact maximum loneliness of a concrete integer tuple by
    enumerating the complete set of critical times;
  * construct and verify the two universal-grid obstructions described in
    the accompanying research report.

This is a checker for finite claims and certificates.  It is not claimed to
resolve the Lonely Runner Conjecture for arbitrary k.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from pathlib import Path
from typing import Iterable, Iterator, Sequence


def distance_to_nearest_integer(x: Fraction) -> Fraction:
    """Return ||x|| exactly for a rational x."""
    r = x.numerator % x.denominator
    return Fraction(min(r, x.denominator - r), x.denominator)


def minimum_loneliness(speeds: Sequence[int], t: Fraction) -> Fraction:
    """Return min_i ||t*u_i|| exactly."""
    if not speeds:
        raise ValueError("speeds must be nonempty")
    if any(u == 0 for u in speeds):
        raise ValueError("all speeds must be nonzero")
    return min(distance_to_nearest_integer(t * abs(u)) for u in speeds)


def threshold(speeds: Sequence[int]) -> Fraction:
    """Return the stationary-runner LRC threshold 1/(k+1)."""
    if not speeds:
        raise ValueError("speeds must be nonempty")
    return Fraction(1, len(speeds) + 1)


def critical_times(speeds: Sequence[int]) -> Iterator[Fraction]:
    """Enumerate a complete finite set containing a global maximizer.

    Let F(t)=min_i ||u_i t||.  F is a continuous piecewise-linear function
    on R/Z.  A maximizer can be chosen either at a breakpoint of one active
    triangular wave, which has denominator 2|u_i|, or at an intersection of
    active branches of opposite slope, which has denominator |u_i|+|u_j|.
    Allowing i=j covers the breakpoint denominator.  Therefore it is enough
    to enumerate t=a/(|u_i|+|u_j|), 0<=a<|u_i|+|u_j|.
    """
    values = sorted(set(abs(u) for u in speeds))
    if not values or any(v == 0 for v in values):
        raise ValueError("all speeds must be nonzero")
    seen: set[Fraction] = set()
    for i, a in enumerate(values):
        for b in values[i:]:
            den = a + b
            for num in range(den):
                t = Fraction(num, den)
                if t not in seen:
                    seen.add(t)
                    yield t


@dataclass(frozen=True)
class MaximumLoneliness:
    value: Fraction
    witnesses: tuple[Fraction, ...]


def exact_maximum_loneliness(speeds: Sequence[int]) -> MaximumLoneliness:
    """Compute max_t min_i ||u_i t|| exactly for a concrete tuple."""
    best = Fraction(-1, 1)
    witnesses: list[Fraction] = []
    for t in critical_times(speeds):
        value = minimum_loneliness(speeds, t)
        if value > best:
            best = value
            witnesses = [t]
        elif value == best:
            witnesses.append(t)
    return MaximumLoneliness(best, tuple(sorted(set(witnesses))))


def grid_witnesses(speeds: Sequence[int], denominator: int) -> tuple[Fraction, ...]:
    """Return every witness in (1/denominator)Z/Z, using exact arithmetic."""
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    alpha = threshold(speeds)
    result = []
    for a in range(denominator):
        t = Fraction(a, denominator)
        if minimum_loneliness(speeds, t) >= alpha:
            result.append(t)
    return tuple(result)


def nearest_half_grid_point(target: Fraction, frequency: int) -> Fraction:
    """Return (2m+1)/(2*frequency) nearest to target in [0,1)."""
    if frequency <= 0:
        raise ValueError("frequency must be positive")
    x = target * frequency - Fraction(1, 2)
    floor_x = x.numerator // x.denominator
    candidates = set()
    for m in range(floor_x - 2, floor_x + 4):
        m_mod = m % frequency
        candidates.add(Fraction(2 * m_mod + 1, 2 * frequency))

    def circle_distance(a: Fraction, b: Fraction) -> Fraction:
        delta = abs(a - b)
        return min(delta, 1 - delta)

    return min(candidates, key=lambda t: (circle_distance(t, target), t))


def diagonal_obstruction(k: int, d: int) -> tuple[int, ...]:
    """Return (1,2,...,k-1,d)."""
    if k < 2:
        raise ValueError("k must be at least 2")
    if d <= k - 1:
        raise ValueError("d must exceed k-1 so that speeds are distinct")
    return tuple(range(1, k)) + (d,)


def congruence_obstruction(k: int, d: int) -> tuple[int, ...]:
    """Return (1,2,...,k-1,d+k), congruent to (1,...,k) mod d."""
    if k < 2:
        raise ValueError("k must be at least 2")
    if d <= 0:
        raise ValueError("d must be positive")
    return tuple(range(1, k)) + (d + k,)


def strict_witness_for_accelerated_prefix(k: int, last_speed: int) -> Fraction:
    """Construct a strict witness near 1/k for (1,...,k-1,last_speed)."""
    if k < 2:
        raise ValueError("k must be at least 2")
    if last_speed <= k - 1:
        raise ValueError("last_speed must exceed k-1")
    return nearest_half_grid_point(Fraction(1, k), last_speed)


def theorem_bound(k: int) -> Fraction:
    """Return k(k+1)(k-1)/2, the sufficient last-speed bound."""
    if k < 2:
        raise ValueError("k must be at least 2")
    return Fraction(k * (k + 1) * (k - 1), 2)


def fraction_text(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def certificate_record(kind: str, k: int, d: int) -> dict:
    """Build one exact obstruction certificate record."""
    if kind == "diagonal":
        speeds = diagonal_obstruction(k, d)
        symbolic_reason = (
            "At every grid time t=a/d, the last coordinate is d*t=a, "
            "so its distance to the nearest integer is 0."
        )
    elif kind == "congruence":
        speeds = congruence_obstruction(k, d)
        symbolic_reason = (
            "Modulo d the tuple equals (1,2,...,k).  A witness for "
            "(1,2,...,k) occurs only at t=s/(k+1) with gcd(s,k+1)=1; "
            "when gcd(d,k+1)=1 no such nonzero time lies on the 1/d grid."
        )
    else:
        raise ValueError("kind must be 'diagonal' or 'congruence'")

    last = speeds[-1]
    t = strict_witness_for_accelerated_prefix(k, last)
    distances = [distance_to_nearest_integer(t * u) for u in speeds]
    alpha = Fraction(1, k + 1)
    grid = grid_witnesses(speeds, d)
    maximum = exact_maximum_loneliness(speeds)
    return {
        "kind": kind,
        "k_relative_speeds": k,
        "total_runners": k + 1,
        "grid_denominator": d,
        "speeds": list(speeds),
        "gcd_of_speeds": gcd(*speeds),
        "all_speeds_distinct": len(set(speeds)) == len(speeds),
        "all_speeds_coprime_to_grid_denominator": all(gcd(u, d) == 1 for u in speeds),
        "threshold": fraction_text(alpha),
        "sufficient_last_speed_bound": fraction_text(theorem_bound(k)),
        "last_speed": last,
        "bound_condition_holds": Fraction(last, 1) > theorem_bound(k),
        "strict_witness": fraction_text(t),
        "distances_at_strict_witness": [fraction_text(x) for x in distances],
        "minimum_distance_at_strict_witness": fraction_text(min(distances)),
        "strict_witness_verified": min(distances) > alpha,
        "exact_maximum_loneliness": fraction_text(maximum.value),
        "exact_maximizing_times": [fraction_text(x) for x in maximum.witnesses],
        "grid_witness_count": len(grid),
        "grid_witnesses": [fraction_text(x) for x in grid],
        "no_grid_witness_verified": len(grid) == 0,
        "symbolic_no_grid_witness_reason": symbolic_reason,
    }


def verify_certificate(data: dict) -> list[str]:
    """Verify every finite claim in a generated certificate.

    Returns a list of human-readable checks.  Raises AssertionError on failure.
    """
    checks: list[str] = []
    for record in data.get("examples", []):
        kind = record["kind"]
        k = int(record["k_relative_speeds"])
        d = int(record["grid_denominator"])
        expected = certificate_record(kind, k, d)
        assert record == expected, f"certificate mismatch for {kind} k={k}, d={d}"
        checks.append(f"verified {kind} obstruction for k={k}, d={d}")
    assert checks, "certificate contains no examples"
    return checks


def build_default_certificate() -> dict:
    """Return the two k=13 exact examples used in the report."""
    return {
        "schema": "piatra-institute/lrc-grid-obstruction-certificate/v1",
        "arithmetic": "exact rational arithmetic; no floating point",
        "examples": [
            certificate_record("diagonal", 13, 2000),
            certificate_record("congruence", 13, 2003),
        ],
    }


def run_self_tests() -> None:
    # Canonical tight tuples for small k.
    for k in range(1, 8):
        speeds = tuple(range(1, k + 1))
        result = exact_maximum_loneliness(speeds)
        assert result.value == Fraction(1, k + 1), (k, result)

    # The two report examples.
    data = build_default_certificate()
    verify_certificate(data)

    # Robust example uses a prime d>k, hence every speed is a unit modulo d.
    robust = data["examples"][1]
    d = robust["grid_denominator"]
    assert all(gcd(u, d) == 1 for u in robust["speeds"])


def parse_speeds(values: Iterable[str]) -> tuple[int, ...]:
    speeds = tuple(int(v) for v in values)
    if not speeds:
        raise ValueError("at least one speed is required")
    if any(v == 0 for v in speeds):
        raise ValueError("all speeds must be nonzero")
    return speeds


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="run exact regression tests")
    parser.add_argument("--speeds", nargs="+", help="integer speeds to analyse")
    parser.add_argument("--grid", type=int, help="test every time on the 1/d grid")
    parser.add_argument("--maximum", action="store_true", help="compute exact maximum loneliness")
    parser.add_argument(
        "--write-default-certificate",
        type=Path,
        help="write the two exact k=13 obstruction records as JSON",
    )
    parser.add_argument("--verify-certificate", type=Path, help="verify a certificate JSON file")
    args = parser.parse_args()

    did_work = False
    if args.self_test:
        run_self_tests()
        print("self-tests: PASS")
        did_work = True

    if args.write_default_certificate:
        data = build_default_certificate()
        args.write_default_certificate.write_text(
            json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        print(f"wrote {args.write_default_certificate}")
        did_work = True

    if args.verify_certificate:
        data = json.loads(args.verify_certificate.read_text(encoding="utf-8"))
        for message in verify_certificate(data):
            print(message)
        print("certificate: PASS")
        did_work = True

    if args.speeds:
        speeds = parse_speeds(args.speeds)
        print(f"speeds={speeds}")
        print(f"threshold={fraction_text(threshold(speeds))}")
        if args.grid is not None:
            witnesses = grid_witnesses(speeds, args.grid)
            print(f"grid denominator={args.grid}")
            print(f"grid witness count={len(witnesses)}")
            if witnesses:
                print("grid witnesses=" + ", ".join(fraction_text(t) for t in witnesses))
        if args.maximum:
            result = exact_maximum_loneliness(speeds)
            print(f"maximum loneliness={fraction_text(result.value)}")
            print("maximizing times=" + ", ".join(fraction_text(t) for t in result.witnesses))
        did_work = True

    if not did_work:
        parser.print_help()


if __name__ == "__main__":
    main()
