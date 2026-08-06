#!/usr/bin/env python3
"""Independent re-derivation of the load-bearing steps of

    Haowei Lin, Shanda Li, "Settling the Optimal Exponent Relating Sumsets and
    Difference Sets", arXiv:2607.27199v1, 29 Jul 2026.

Checks sections 2.1-2.5 and the size formula (14). Does not check the Lean
development, and does not check the paper's historical baseline claims.

Note: pdftotext drops superscripts and renders s = 2^K + 1 as "2K+1", which is
inconsistent with the paper's own "2^K = 1 (mod 3)" and alpha = 2^(K+1-d) steps.
The reading s = 2^K + 1 was confirmed against arxiv.org/html/2607.27199v1 and is
what this script uses.

Run: python3 verify.py     (needs numpy, exits nonzero on any failed check)
"""

import math
import sys

import numpy as np

FAILURES = []


def check(label, ok, detail=""):
    print(f"  [{'ok ' if ok else 'FAIL'}] {label}" + (f"  {detail}" if detail else ""))
    if not ok:
        FAILURES.append(label)


# --- 2.1 base-12 digit gadget -------------------------------------------------

W = [0, 1, 2, 4, 5, 9]
DELTA = {a - b for a in W for b in W}


def Yset(j):
    """Y_j = { sum_{i<j} w_i 12^i : w_i in W }."""
    out = {0}
    for i in range(j):
        out = {y + w * (12 ** i) for y in out for w in W}
    return out


print("2.1  base-12 digit gadget")
check(
    "(3) (W+W) mod 12 = Z/12Z",
    sorted({(a + b) % 12 for a in W for b in W}) == list(range(12)),
)
check(
    "(3) (W-W) mod 12 = Z/12Z minus {6}",
    sorted({(a - b) % 12 for a in W for b in W}) == [x for x in range(12) if x != 6],
)
check(
    "Delta = W-W as printed",
    sorted(DELTA)
    == [-9, -8, -7, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 7, 8, 9],
)

# Lemma 2.1 and (4), by direct enumeration.
for j in range(1, 5):
    Yj, nj = Yset(j), 12 ** j
    check(f"(4) |Y_{j}| = 6^{j}", len(Yj) == 6 ** j)
    check(
        f"Lemma 2.1 (Y_{j}+Y_{j}) mod 12^{j} = Z/12^{j}Z",
        {(a + b) % nj for a in Yj for b in Yj} == set(range(nj)),
    )

# Lemma 2.2: carry automaton, transition matrix (7), recurrence, closed form (5).
print("2.1  Lemma 2.2 (carry automaton)")
E = list(range(-6, 6))  # balanced digits {-6,...,5}
X = {1: frozenset({0}), 2: frozenset({-1, 0}), 3: frozenset({0, 1})}


def Phi(Xs, eps):
    return frozenset(
        {cp for cp in (-1, 0, 1) for c in Xs if eps + c - 12 * cp in DELTA}
    )


M, unlisted = [], 0
for i in (1, 2, 3):
    row = [0, 0, 0]
    for eps in E:
        img = Phi(X[i], eps)
        hit = [j for j in (1, 2, 3) if X[j] == img]
        if hit:
            row[hit[0] - 1] += 1
        elif img:
            unlisted += 1
    M.append(row)
check("(7) transition matrix = [[5,3,3],[4,5,3],[4,4,4]]", M == [[5, 3, 3], [4, 5, 3], [4, 4, 4]], str(M))
check("no reachable carry-set outside {X1,X2,X3}", unlisted == 0)

Mo = np.array(M, dtype=object)
one = np.array([1, 1, 1], dtype=object)
e1 = np.array([1, 0, 0], dtype=object)
brute = [len({(a - b) % 12 ** j for a in Yset(j) for b in Yset(j)}) for j in range(5)]
auto = [int(e1 @ np.linalg.matrix_power(Mo, j) @ one) for j in range(5)]
check("t_j = e1^T M^j 1 matches brute-force |(Y_j - Y_j) mod n_j|", brute == auto, str(brute))

rec = [1, 11]
while len(rec) < 5:
    rec.append(13 * rec[-1] - 16 * rec[-2])
check("recurrence t_{j+2} = 13 t_{j+1} - 16 t_j reproduces t_j", rec == brute)

P = np.linalg.matrix_power(Mo, 2) - 13 * Mo + 16 * np.eye(3, dtype=int).astype(object)
check("(M^2 - 13M + 16 I) 1 = 0", list(P @ one) == [0, 0, 0])

r5 = math.sqrt(105)
lam, mu = (13 + r5) / 2, (13 - r5) / 2
c1, c2 = (r5 + 9) / (2 * r5), (r5 - 9) / (2 * r5)
closed = [c1 * lam ** j + c2 * mu ** j for j in range(5)]
check(
    "(5) closed form matches t_j",
    all(abs(closed[j] - brute[j]) < 1e-6 for j in range(5)),
)
check(
    "(5) both coefficients positive and sum to 1, 0 < mu < lam",
    c1 > 0 and c2 > 0 and abs(c1 + c2 - 1) < 1e-12 and 0 < mu < lam,
)
check("Lemma 2.3  lambda/12 < 31/32", lam / 12 < 31 / 32, f"{lam/12:.9f} < {31/32:.9f}")
check("Lemma 2.3  (31/32)^22 < 1/2", (31 / 32) ** 22 < 0.5, f"{(31/32)**22:.6f}")

# --- 2.2 symmetric additive basis --------------------------------------------

print("2.2  Lemma 2.4 (additive basis in Z/QZ), s = 2^K + 1")


def basis(K):
    s = 2 ** K + 1
    Q, m = s * s, (s - 1) // 2
    H = {x % Q for x in range(-m, m + 1)}
    V = {(k * s) % Q for k in range(s)}
    I = H | V
    return s, Q, H, V, I, I - {0}


for K in (2, 4, 6, 8):
    s, Q, H, V, I, B = basis(K)
    outside = set(range(Q)) - I
    check(f"K={K} s=2^K+1={s} is 2 mod 3 (paper's CRT coprimality step)", s % 3 == 2)
    check(f"K={K} H cap V = {{0}} and (9) |I| = 2s-1 = {2*s-1}", H & V == {0} and len(I) == 2 * s - 1)
    check(f"K={K} I = -I", I == {(-x) % Q for x in I})
    check(f"K={K} I + I = Z/QZ", {(a + b) % Q for a in I for b in I} == set(range(Q)))
    check(f"K={K} every x outside I is in B+B", outside <= {(a + b) % Q for a in B for b in B})
    check(f"K={K} every x outside I is in B-B", outside <= {(a - b) % Q for a in B for b in B})

# --- 2.3-2.5 CRT construction, on scaled-down (K, d) -------------------------
#
# Lemmas 2.5, 2.6, 2.7 and (14) are stated for general K and d, so small d is a
# genuine test of them. The paper's own d = 22(K+2) is far beyond enumeration.

print("2.3-2.5  CRT construction, scaled-down instances")
for K, d in [(2, 2), (2, 3), (4, 2), (4, 3), (6, 2)]:
    s, Q, H, V, I, B = basis(K)
    n, rho = 12 ** d, len(I)
    if math.gcd(Q, n) != 1:
        check(f"K={K} d={d} gcd(Q,n)=1", False)
        continue
    q = Q * n
    Y = Yset(d)
    t = len({(a - b) % n for a in Y for b in Y})
    # (12): least nonnegative representatives of R = ({0} x Z/nZ) u (B x Y)
    R = [x for x in range(q) if x % Q == 0 or (x % Q in B and x % n in Y)]
    A = sorted(set(R) | {x + q for x in R})  # (13)
    RR = len({(a + b) % q for a in R for b in R})
    RmR = len({(a - b) % q for a in R for b in R})
    AA = len({a + b for a in A for b in A})
    AmA = len({a - b for a in A for b in A})
    tag = f"K={K} d={d} (s={s} Q={Q} n={n} rho={rho} t={t})"
    check(f"{tag} (14) |A| = 2(n + (rho-1)6^d)", len(A) == 2 * (n + (rho - 1) * 6 ** d))
    check(f"{tag} Lemma 2.5 |(R+R) mod q| = q", RR == q)
    check(f"{tag} Lemma 2.6 |(R-R) mod q| = rho n + (Q-rho) t", RmR == rho * n + (Q - rho) * t)
    check(f"{tag} Lemma 2.7 |A+A| >= 3|(R+R) mod q|", AA >= 3 * RR)
    check(f"{tag} Lemma 2.7 |A-A| <= 4|(R-R) mod q|", AmA <= 4 * RmR)

# --- scale of the real A_K ----------------------------------------------------
#
# Not a check on the paper: the reason no enumeration search could have found it.

print("scale of the actual A_K, d = 22(K+2)  (prior published best: 1.125944)")
for K in (4, 6, 10, 100):
    d, s = 22 * (K + 2), 2 ** K + 1
    size = 2 * (12 ** d + (2 * s - 2) * 6 ** d)
    print(f"  K={K:4d}  bound 2K/(K+3) = {2*K/(K+3):.6f}   d = {d:5d}   |A_K| ~ 10^{math.log10(size):.0f}")

print()
if FAILURES:
    print(f"FAILED: {len(FAILURES)} check(s): {FAILURES}")
    sys.exit(1)
print("all checks passed")
