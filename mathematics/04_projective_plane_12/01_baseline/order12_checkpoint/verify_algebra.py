#!/usr/bin/env python3
"""Exact arithmetic checks for the universal order-12 incidence-matrix consequences."""
from __future__ import annotations

from math import prod

q = 12
v = q * q + q + 1
k = q + 1
m = q * k  # 156

assert v == 157 and k == 13 and m == 156

# det(q I + J) = q^(v-1) (q+v) and q+v = (q+1)^2.
gram_det = q ** (v - 1) * (q + v)
det_abs = k * q ** ((v - 1) // 2)
assert det_abs * det_abs == gram_det
assert det_abs == 13 * 12**78

# From N(13 N^T - J) = 156 I, every Smith invariant divides 156.
# The determinant's prime valuations then force the following exact counts.
assert det_abs == 2**156 * 3**78 * 13
rank_mod_3 = v - 78
rank_mod_13 = v - 1
assert rank_mod_3 == 79
assert rank_mod_13 == 156

# If r is the binary rank, the 2-adic Smith multiplicities are forced as below.
for r in range(1, 80):
    c0, c1, c2 = r, 158 - 2 * r, r - 1
    assert c0 + c1 + c2 == 157
    assert c1 + 2 * c2 == 156
    assert min(c0, c1, c2) >= 0

print("PASS")
print(f"v={v}, k={k}")
print(f"|det N|={det_abs}")
print("N^{-1}=(13 N^T-J)/156 (formal consequence of NN^T=12I+J and regularity)")
print("Smith exponent divides 156")
print(f"rank_F3(N)={rank_mod_3}")
print(f"rank_F13(N)={rank_mod_13}")
print("binary Smith profile: (v2=0,v2=1,v2=2)=(r,158-2r,r-1), 1<=r<=79")
