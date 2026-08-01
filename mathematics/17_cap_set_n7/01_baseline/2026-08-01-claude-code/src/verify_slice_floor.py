#!/usr/bin/env python3
"""Certified slice floor for a hypothetical 237-cap in AG(7,3).

Claim: every 237-cap has some hyperplane slice of size >= 89, and the
first-three-moment method cannot force >= 90. This pins the moment method's reach
at 89, while the known rigidity classifications only start near 110 (the 89..110
gap is exactly where the a(7) upper bound is stuck).

Proof of the floor is an exact integer Farkas certificate. The moment identities
over the 1093 hyperplane directions are
    sum_t n_t = 1093,  sum_t n_t P(t) = 364*C(237,2),  sum_t n_t Q(t) = 121*C(237,3),
with P(t)=sum C(x,2), Q(t)=sum C(x,3). If integers (y0,y1,y2) satisfy
    y0 + y1 P(t) + y2 Q(t) >= 0   for every profile t with all parts <= 88,
    y0*1093 + y1*TP + y2*TQ < 0,
then no nonnegative combination of such profiles can meet the moment totals, so no
237-cap has all slices <= 88. The complement (all slices <= 89 is feasible) shows
the floor is exactly 89. LP is used only to *find* the certificate; it is then
checked in exact integer arithmetic.
"""
from __future__ import annotations
import json, sys
from math import comb
from pathlib import Path

D = 1093            # (3^7-1)/2 hyperplane directions
PAIR = 364          # (3^6-1)/2
TRIP = 121          # (3^5-1)/2

def profiles(M, maxpart):
    out = []
    for a in range(min(maxpart, M), -1, -1):
        for b in range(min(a, M - a), -1, -1):
            c = M - a - b
            if 0 <= c <= b:
                out.append((a, b, c))
    return out

def P(t): return sum(comb(x, 2) for x in t)
def Q(t): return sum(comb(x, 3) for x in t)

def moment_totals(M): return D, PAIR * comb(M, 2), TRIP * comb(M, 3)

def lp_feasible(M, maxpart):
    from scipy.optimize import linprog
    ts = profiles(M, maxpart)
    sn, sP, sQ = moment_totals(M)
    A_eq = [[1] * len(ts), [P(t) for t in ts], [Q(t) for t in ts]]
    r = linprog(c=[0] * len(ts), A_eq=A_eq, b_eq=[sn, sP, sQ],
                bounds=[(0, None)] * len(ts), method="highs")
    return r.success

def find_farkas(M, maxpart):
    """Integer (y0,y1,y2): y0 + y1 P + y2 Q >= 0 on all <=maxpart profiles,
    aggregate < 0. Found by LP, snapped to integers, verified exactly."""
    from scipy.optimize import linprog
    ts = profiles(M, maxpart)
    sn, sP, sQ = moment_totals(M)
    A_ub = [[-1, -P(t), -Q(t)] for t in ts]          # -(y0+y1P+y2Q) <= 0
    A_ub.append([sn, sP, sQ]); b_ub = [0] * len(ts) + [-1]  # aggregate <= -1
    res = linprog(c=[sn, sP, sQ], A_ub=A_ub, b_ub=b_ub,
                  bounds=[(-1e7, 1e7)] * 3, method="highs")
    if not res.success:
        return None
    y1f, y2f = res.x[1], res.x[2]
    # For any integer (y1,y2), the exact minimal integer y0 keeping every profile
    # nonnegative is -min_t(y1 P + y2 Q). Then only the aggregate sign is in question.
    for k in (1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 5000, 10000, 100000):
        y1, y2 = round(y1f * k), round(y2f * k)
        if (y1, y2) == (0, 0):
            continue
        y0 = -min(y1 * P(t) + y2 * Q(t) for t in ts)
        if y0 * sn + y1 * sP + y2 * sQ < 0:
            return (y0, y1, y2)
    return None

def main():
    M = 237
    outdir = Path(__file__).resolve().parents[1] / "certificates"
    outdir.mkdir(exist_ok=True)
    sn, sP, sQ = moment_totals(M)
    # floor: <=88 infeasible via Farkas, <=89 feasible
    y = find_farkas(M, 88)
    assert y is not None, "no Farkas certificate found for <=88"
    assert not lp_feasible(M, 88), "expected <=88 infeasible"
    assert lp_feasible(M, 89), "expected <=89 feasible"
    ts88 = profiles(M, 88)
    agg = y[0] * sn + y[1] * sP + y[2] * sQ
    ok = all(y[0] + y[1] * P(t) + y[2] * Q(t) >= 0 for t in ts88) and agg < 0
    cert = dict(
        claim="Every 237-cap in AG(7,3) has a hyperplane slice of size >= 89; "
              "the first-three-moment method cannot force >= 90.",
        premise="a(6) = 112 (max slice); moment identities over 1093 directions.",
        moment_totals=dict(sum_n=sn, sum_nP=sP, sum_nQ=sQ),
        farkas_certificate=dict(
            y=list(y),
            statement="y0 + y1*P(t) + y2*Q(t) >= 0 for all profiles with parts <= 88, "
                      "but y0*1093 + y1*sum_nP + y2*sum_nQ < 0",
            aggregate=agg, verified_exact_integer=ok),
        floor=89,
        feasible_at_89=True,
        gap_note="moment method reaches 89; rigidity classifications start near 110; "
                 "the 89..110 interval is unbridged.")
    (outdir / "slice_floor_237.json").write_text(json.dumps(cert, indent=2))
    print(f"237-cap slice floor: <=88 INFEASIBLE (Farkas y={y}, aggregate={agg}), "
          f"<=89 FEASIBLE -> every 237-cap has a slice >= 89 (exact-integer verified: {ok}).")
    print("wrote certificates/slice_floor_237.json")

if __name__ == "__main__":
    sys.exit(main())
