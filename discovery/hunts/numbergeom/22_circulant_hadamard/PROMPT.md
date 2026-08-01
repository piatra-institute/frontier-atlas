# Circulant Hadamard matrix of order greater than 4

**Refute.** The circulant Hadamard matrix conjecture: find a circulant +/-1 matrix H of order n > 4 with H H^T = n I, at an order not excluded by the known number-theoretic constraints.

**What counts as a win (one-sided).** One +/-1 sequence of length n > 4 whose circulant has orthogonal rows (equivalently, all nonzero periodic autocorrelations vanish). A single witness refutes the conjecture; failure proves nothing.

**Checker (seconds).** From the first row v in {+1,-1}^n, assert every nonzero cyclic shift has zero dot product with v (periodic autocorrelation zero at all nonzero lags). O(n^2), exact integers.

**Search plan.** n must equal 4u^2; only orders passing the field-descent and self-conjugacy tests are candidates. Search sign vectors with the periodic-autocorrelation constraint via SAT/CP; exploit the required symmetry (perfect difference set structure) to fix many signs; meet-in-the-middle on autocorrelation contributions. Evolutionary search scored by autocorrelation defect.

**Prior art (verify).** Ryser conjectured no circulant Hadamard matrix exists for order n > 4. It is equivalent to the nonexistence of certain perfect binary arrays / difference sets, and is proven for many orders via field descent (Leung, Schmidt), but remains open in general. See Ryser's conjecture and the Leung-Schmidt field-descent papers. Target an order not yet excluded (verify).
