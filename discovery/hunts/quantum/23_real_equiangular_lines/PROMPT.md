# More equiangular lines in a low real dimension

**Find:** a set of N equiangular lines in R^d with N above the current best-known lower bound, for a dimension d where the maximum a(d) is open (e.g. d = 18, 19, 20, with 57 <= a(18) <= 60, 72 <= a(19) <= 74, 90 <= a(20) <= 94).

## What counts as a win
A Seidel matrix (symmetric, zero diagonal, +/-1 off-diagonal) of size N realising N equiangular lines in R^d with N above the record. One-sided: any larger set raises a(d).

## Checker
Given the Seidel matrix S with common angle arccos(1/alpha), form G = I + (1/alpha) S. Verify G is positive semidefinite with rank(G) <= d, by exact integer/algebraic eigenvalues (S is an integer matrix, so its spectrum is algebraic and computed exactly). PSD-ness and the rank bound certify N equiangular unit vectors in R^d. Runtime: seconds.

## Search plan
Search integer Seidel matrices with smallest eigenvalue -alpha of high multiplicity: seed from strongly regular graphs, regular two-graphs, and known record configurations, then extend by adding a compatible row (a +/-1 vector preserving the eigenvalue structure). Use exact eigenvalue certification, not floating point.

## Prior art (verify)
Maxima of equiangular lines in R^d are tabulated in OEIS A002853; several low dimensions (around 18-23) have a gap between best construction and upper bound (Lemmens-Seidel; Greaves-Koolen-Munemasa-Szollosi). Re-verify the current best lower bound for the chosen d.
