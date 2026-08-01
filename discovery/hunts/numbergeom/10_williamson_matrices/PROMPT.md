# Williamson matrices at an open order

**Find.** Four symmetric circulant (or type-1) +/-1 matrices A, B, C, D of order n with A^2 + B^2 + C^2 + D^2 = 4n I, at an order n where none is known.

**What counts as a win (one-sided).** One quadruple of first rows generating symmetric circulants that satisfy the Williamson equation. A single witness settles existence at that order (and yields a Hadamard matrix of order 4n); failure proves nothing.

**Checker (seconds).** Build the four circulants from their first rows, assert each is symmetric and +/-1, and assert A^2 + B^2 + C^2 + D^2 = 4n I exactly (integer matrix multiply). Equivalent fast check: the sum of the four periodic autocorrelation functions is zero at every nonzero shift. O(n^2).

**Search plan.** Reduce by symmetry: symmetric circulants are determined by floor(n/2) sign choices each; enforce the autocorrelation condition via meet-in-the-middle over pairs; SAT/CP on the sign variables; evolutionary search scored by autocorrelation defect. Use the power-spectral-density filter to prune early.

**Prior art (verify).** Williamson matrices were enumerated exhaustively up to order 59 (Holzmann, Kharaghani, Tayfeh-Rezaie, ca. 2008), showing none exist for some orders (e.g., 35) and leaving others open. Existence at various odd orders is undetermined. Confirm the target order is open before starting (verify).
