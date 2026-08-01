#!/usr/bin/env python3
"""Independent reproduction of the hyperplane-profile (standard-diagram) staircase
for caps in AG(7,3).

This is a second, from-scratch implementation. It does two things for each
hypothetical cap size M in {291, 290, 289, 288}:

  (A) VERIFY the published separating functional: enumerate every sorted
      hyperplane profile, recompute the pair moment P and triple moment Q, and
      confirm which profiles have negative slack, the exact aggregate slack (from
      the moment identities), and the forced minimum number of exceptional
      directions.

  (B) INDEPENDENTLY REDERIVE a separator: without using the published
      coefficients, solve an LP for a functional that is >= 0 off the claimed
      exceptional set and yields a negative aggregate. If feasible, the reduction
      does not depend on anyone's specific magic numbers.

Background arithmetic (all exact integers):
  A hyperplane direction splits F_3^7 into three parallel 6-flats with a sorted
  profile t = (a, b, c), a + b + c = M, 112 >= a >= b >= c >= 0 (112 = a(6)).
  There are D = (3^7 - 1)/2 = 1093 directions. Each pair of cap points shares a
  direction in (3^6 - 1)/2 = 364 of them; each noncollinear triple in
  (3^5 - 1)/2 = 121. With P(t) = sum C(x,2), Q(t) = sum C(x,3), the moment
  identities are
        sum_t n_t          = 1093
        sum_t n_t P(t)     = 364 * C(M,2)
        sum_t n_t Q(t)     = 121 * C(M,3).
  For an affine slack S(t) = A*Q(t) + B*P(t) + C, the aggregate sum_t n_t S(t)
  is therefore fixed by the moment totals alone, independent of the (unknown)
  distribution n_t. If S >= 0 on every non-exceptional profile yet the aggregate
  is negative, some exceptional (negative-slack) profile must occur, with total
  multiplicity >= ceil(|aggregate| / max|negative slack|).
"""
from __future__ import annotations
import json, math, sys
from pathlib import Path

N = 7
CAP6 = 112                       # a(6), the max slice size (Potechin); external premise
D = (3**N - 1) // 2              # 1093 hyperplane directions
PAIR_MULT = (3**(N-1) - 1) // 2  # 364
TRIPLE_MULT = (3**(N-2) - 1) // 2  # 121

def c2(x: int) -> int: return x * (x - 1) // 2
def c3(x: int) -> int: return x * (x - 1) * (x - 2) // 6
def P(t): return c2(t[0]) + c2(t[1]) + c2(t[2])
def Q(t): return c3(t[0]) + c3(t[1]) + c3(t[2])

def profiles(M: int):
    """All sorted profiles (a,b,c), a+b+c=M, CAP6>=a>=b>=c>=0."""
    out = []
    for a in range(min(CAP6, M), -1, -1):
        for b in range(min(a, M - a), -1, -1):
            c = M - a - b
            if 0 <= c <= b:
                out.append((a, b, c))
    return out

def moment_totals(M: int):
    return D, PAIR_MULT * c2(M), TRIPLE_MULT * c3(M)  # sum n, sum nP, sum nQ

# Published separating functionals, written as S(t) = A*Q(t) + B*P(t) + C0.
# 291 and 289 come from the committed generators; 290 and 288 were proposed in
# review and are reproduced here from scratch.
def centered(A, B, base):
    """A*(Q - Q(base)) + B*(P - P(base)) as (A, B, C0)."""
    return A, B, -(A * Q(base) + B * P(base))

PUBLISHED = {
    291: dict(coeffs=centered(631, -57531, (97, 97, 97)),
              exceptional={(112, 112, 67)}),
    290: dict(coeffs=centered(44, -3999, (97, 97, 96)),
              exceptional={(112, 112, 66), (112, 111, 67)}),
    289: dict(coeffs=(86, -7793, 70_101_168),
              exceptional={(112, 112, 65), (112, 111, 66),
                           (112, 110, 67), (111, 111, 67)}),
    288: dict(coeffs=centered(3, -271, (96, 96, 96)),
              exceptional={(112, 112, 64), (112, 111, 65), (112, 110, 66),
                           (112, 109, 67), (111, 111, 66), (111, 110, 67)}),
}

def slack(t, coeffs):
    A, B, C0 = coeffs
    return A * Q(t) + B * P(t) + C0

def aggregate(M, coeffs):
    A, B, C0 = coeffs
    sn, sP, sQ = moment_totals(M)
    return A * sQ + B * sP + C0 * sn

def verify_published(M):
    coeffs = PUBLISHED[M]["coeffs"]
    exp = PUBLISHED[M]["exceptional"]
    ts = profiles(M)
    neg = {t: slack(t, coeffs) for t in ts if slack(t, coeffs) < 0}
    zero = [t for t in ts if slack(t, coeffs) == 0]
    agg = aggregate(M, coeffs)
    assert set(neg) == exp, f"M={M}: neg set {set(neg)} != expected {exp}"
    assert all(slack(t, coeffs) >= 0 for t in ts if t not in exp)
    worst = max(-s for s in neg.values())
    min_dirs = (-agg + worst - 1) // worst  # ceil(|agg| / worst), agg < 0
    assert agg < 0
    return dict(size=M, admissible_profiles=len(ts),
                aggregate_slack=agg,
                negative_profiles=sorted(([list(t), neg[t]] for t in neg),
                                         key=lambda r: r[1]),
                zero_profiles=[list(t) for t in zero],
                max_negative_magnitude=worst,
                min_exceptional_directions=min_dirs,
                reduces_to=f"a(7) <= {M-1}",
                coeffs=list(coeffs))

def independent_separator(M):
    """LP: find our OWN (A,B,C0) forcing exactly the claimed exceptional set,
    without the published coefficients. Returns the found functional or None."""
    try:
        from scipy.optimize import linprog
    except Exception:
        return None
    exp = PUBLISHED[M]["exceptional"]
    ts = profiles(M)
    sn, sP, sQ = moment_totals(M)
    # variables x = [A, B, C0]; A >= 1 (positive Q weight), B <= 0 (negative P weight)
    A_ub, b_ub = [], []
    for t in ts:
        row = [Q(t), P(t), 1]
        if t in exp:
            A_ub.append(row); b_ub.append(-1)          # slack <= -1 on exceptional
        else:
            A_ub.append([-v for v in row]); b_ub.append(0)  # slack >= 0 elsewhere
    A_ub.append([sQ, sP, sn]); b_ub.append(-1)         # aggregate <= -1
    # minimize the aggregate (push it well below 0) inside a bounded box, so the
    # optimum sits at a vertex with wide margins that snap cleanly to integers.
    res = linprog(c=[sQ, sP, sn], A_ub=A_ub, b_ub=b_ub,
                  bounds=[(1, 1_000_000), (-10_000_000, 0), (-1e13, 1e13)],
                  method="highs")
    if not res.success:
        return None
    Af, Bf, C0f = res.x
    # scale the rational solution by increasing factors and snap to integers;
    # a strict separator spans an open cone, so some integer point reproduces it.
    for k in (1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000):
        coeffs = (max(1, round(Af * k)), round(Bf * k), round(C0f * k))
        neg = {t for t in ts if slack(t, coeffs) < 0}
        if neg == exp and aggregate(M, coeffs) < 0:
            return dict(feasible=True, integer_check="exact", scale=k,
                        coeffs=[int(v) for v in coeffs],
                        aggregate_slack=aggregate(M, coeffs),
                        note="separator found by LP, independent of published coeffs")
    return dict(feasible=True, integer_check="rational_only",
                lp_coeffs=[float(v) for v in res.x])

def main():
    outdir = Path(__file__).resolve().parents[1] / "certificates"
    outdir.mkdir(exist_ok=True)
    print(f"identities: D={D} pair_mult={PAIR_MULT} triple_mult={TRIPLE_MULT} "
          f"(expect 1093/364/121)")
    assert (D, PAIR_MULT, TRIPLE_MULT) == (1093, 364, 121)
    summary = []
    for M in (291, 290, 289, 288):
        rep = verify_published(M)
        indep = independent_separator(M)
        rep["independent_separator"] = indep
        (outdir / f"staircase_{M}.json").write_text(json.dumps(rep, indent=2))
        summary.append(rep)
        tag = "exact" if indep and indep.get("integer_check") == "exact" else \
              ("weak" if indep else "no-scipy")
        print(f"M={M}: {len(rep['negative_profiles'])} exceptional profile(s) "
              f"{[tuple(r[0]) for r in rep['negative_profiles']]}, "
              f"aggregate={rep['aggregate_slack']}, "
              f">= {rep['min_exceptional_directions']} forced dirs -> {rep['reduces_to']}; "
              f"independent LP separator: {tag}")
    print("\nStaircase (each step needs the listed profiles proved impossible by SAT):")
    print("  291 -> 290 -> 289 -> 288 -> 287")
    print("  known literature upper bound: a(7) <= 288 (arXiv:2206.09804)")
    print("  only a(7) <= 287 would beat it; all arithmetic here is a REDUCTION, "
          "not a bound: it forces which profiles a SAT search must still eliminate.")

if __name__ == "__main__":
    sys.exit(main())
