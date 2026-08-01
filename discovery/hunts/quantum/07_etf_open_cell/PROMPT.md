# An equiangular tight frame at an open table cell

**Find:** an equiangular tight frame (ETF) of N vectors in C^d (or R^d) for a pair (d,N) marked "unknown" in the ETF existence tables.

## What counts as a win
An explicit N x d frame (or its N x N Gram matrix) meeting the ETF conditions. One-sided: existence closes the cell.

## Checker
Form the Gram matrix G (G_ii = 1). Verify equiangularity |G_ij| = sqrt((N-d)/(d(N-1))) for all i != j, tightness G^2 = (N/d) G, and rank(G) = d. Equivalently G is a rank-d projection (times N/d) with constant off-diagonal modulus. Exact over algebraic entries or certified interval; N x N eigendecomposition. Runtime: seconds for tabulated small (d,N).

## Search plan
Try combinatorial constructions first: Steiner ETFs from 2-(v,k,1) designs, ETFs from difference sets / Paley / hyperovals, and Tremain/GDD constructions. For cells outside known families, alternating-projection numerical search on the Gram cone, then exact reconstruction of the sign/phase pattern (a Seidel or Butson matrix) over roots of unity.

## Prior art (verify)
Fickus and Mixon, "Tables of the existence of equiangular tight frames," maintain a survey table of (d,N) existence with explicit open cells. Re-check the chosen cell against the latest version of that table.
