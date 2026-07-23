#!/usr/bin/env python3
"""Exact and independent numerical checks for the flat A15/Laguerre honeycomb.

This verifies a polyhedral competitor, not the curved relaxed Weaire-Phelan foam
and not global Kelvin optimality.

Laguerre convention
-------------------
Cell i consists of points x satisfying
    |x-p_i|^2 - w_i <= |x-(p_j+lambda)|^2 - w_j
for every site j and period lambda in 2 Z^3.

Dependencies
------------
Required: sympy
Optional independent half-space reconstruction: numpy, scipy
"""
from __future__ import annotations

from itertools import product
from math import acos, degrees

from sympy import N, Rational, cbrt, simplify, sqrt

r = cbrt(2)
delta = Rational(5, 4) - r

# Cubic torus [0,2)^3, volume 8. Two type-A sites and six type-B sites.
sites = [
    (Rational(0), Rational(0), Rational(0)),
    (Rational(1), Rational(1), Rational(1)),
    (Rational(1, 2), Rational(0), Rational(1)),
    (Rational(3, 2), Rational(0), Rational(1)),
    (Rational(0), Rational(1), Rational(1, 2)),
    (Rational(0), Rational(1), Rational(3, 2)),
    (Rational(1), Rational(1, 2), Rational(0)),
    (Rational(1), Rational(3, 2), Rational(0)),
]
weights = [Rational(0), Rational(0)] + [delta] * 6

# In the topology interval containing delta, exact polyhedral integration gives:
V_A = (
    Rational(125, 128)
    - Rational(75, 32) * delta
    + Rational(15, 8) * delta**2
    - Rational(1, 2) * delta**3
)
V_B = (
    Rational(129, 128)
    + Rational(25, 32) * delta
    - Rational(5, 8) * delta**2
    + Rational(1, 6) * delta**3
)

# The equal-volume equation collapses to a translated cube.
weight_polynomial = 64 * delta**3 - 240 * delta**2 + 300 * delta + 3
translated_cube = 64 * (delta - Rational(5, 4)) ** 3 + 128

assert simplify(weight_polynomial) == 0
assert simplify(weight_polynomial - translated_cube) == 0
assert simplify(V_A - 1) == 0
assert simplify(V_B - 1) == 0
assert simplify(2 * V_A + 6 * V_B - 8) == 0

# Three face-area orbits at equal volume:
# a: A-B pentagon; b: axial B-B hexagon; c: non-axial B-B pentagon.
a = sqrt(5) * r**2 / 8
b = 1 - r**2 / 4
c = sqrt(6) * (3 - r**2) / 12

S_A = 12 * a
S_B = 4 * a + 2 * b + 8 * c
mean_full_boundary_area = simplify((2 * S_A + 6 * S_B) / 8)
physical_film_area_in_torus = simplify(8 * mean_full_boundary_area / 2)

# Equivalent normalization of Kusner-Sullivan: their cells have volume 8 and
# their A counts half of a cell boundary.
A_KS = 3 + 3 * sqrt(6) + (6 * sqrt(5) - 4 * sqrt(6) - 3) / cbrt(16)
mean_from_KS = simplify(2 * A_KS / (8 ** Rational(2, 3)))
assert simplify(mean_full_boundary_area - mean_from_KS) == 0

# Two exact non-Plateau sector angles occurring at triple edges.
theta_1 = degrees(acos(-Rational(2, 5)))
theta_2 = degrees(acos(-Rational(3, 5)))
assert abs(theta_1 - 120.0) > 1.0
assert abs(theta_2 - 120.0) > 1.0

print("EXACT SYMBOLIC CERTIFICATE")
print("r = cube_root(2) =", N(r, 30))
print("type-B minus type-A weight delta = 5/4-r =", N(delta, 30))
print("V_A =", simplify(V_A), " V_B =", simplify(V_B))
print("A-B pentagon area a =", N(a, 30))
print("B-B axial hexagon area b =", N(b, 30))
print("B-B nonaxial pentagon area c =", N(c, 30))
print("type-A cell boundary area =", N(S_A, 30))
print("type-B cell boundary area =", N(S_B, 30))
print("mean full cell-boundary area =", mean_full_boundary_area)
print("mean full cell-boundary area (decimal) =", N(mean_full_boundary_area, 40))
print("physical film area in the 8-cell torus =", N(physical_film_area_in_torus, 40))
print("non-Plateau sector angles =", theta_1, theta_2)


def independent_halfspace_check() -> None:
    """Reconstruct one cell of each orbit directly from periodic inequalities.

    This part is floating-point and independent of the closed-form volume/area
    expressions above. It serves as a geometric cross-check, not as the exact
    certificate itself.
    """
    try:
        import numpy as np
        from scipy.spatial import ConvexHull, HalfspaceIntersection
    except ImportError:
        print("\nNUMERICAL HALF-SPACE CROSS-CHECK SKIPPED (install numpy and scipy)")
        return

    points = np.asarray([[float(x) for x in p] for p in sites], dtype=float)
    ws = np.asarray([float(N(w, 30)) for w in weights], dtype=float)

    def reconstruct(i: int) -> tuple[float, float, int]:
        p = points[i]
        halfspaces = []
        # Images in this range are more than sufficient for these bounded cells.
        for j, q0 in enumerate(points):
            for k in product(range(-2, 3), repeat=3):
                if j == i and k == (0, 0, 0):
                    continue
                q = q0 + 2.0 * np.asarray(k, dtype=float)
                normal = 2.0 * (q - p)
                rhs = float(np.dot(q, q) - np.dot(p, p) + ws[i] - ws[j])
                # scipy uses normal.x + offset <= 0.
                halfspaces.append(np.r_[normal, -rhs])

        hs = np.asarray(halfspaces, dtype=float)
        if float(np.max(hs[:, :3] @ p + hs[:, 3])) >= -1e-10:
            raise RuntimeError("chosen interior point is not strictly interior")
        vertices = HalfspaceIntersection(hs, p).intersections
        hull = ConvexHull(vertices)
        return float(hull.volume), float(hull.area), int(len(vertices))

    va, sa, nva = reconstruct(0)
    vb, sb, nvb = reconstruct(2)
    assert abs(va - 1.0) < 1e-10
    assert abs(vb - 1.0) < 1e-10
    assert abs(sa - float(N(S_A, 20))) < 1e-10
    assert abs(sb - float(N(S_B, 20))) < 1e-10

    print("\nINDEPENDENT PERIODIC HALF-SPACE CROSS-CHECK")
    print(f"type A: vertices={nva}, volume={va:.15f}, boundary area={sa:.15f}")
    print(f"type B: vertices={nvb}, volume={vb:.15f}, boundary area={sb:.15f}")


independent_halfspace_check()
