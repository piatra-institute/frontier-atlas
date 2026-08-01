# A genuinely quantum unitary error basis in dimension 6

**Find:** a unitary error basis (UEB) in C^6 built from a genuinely quantum Latin square of order 6, hence not equivalent to any Weyl-Heisenberg (nice) UEB or any shift-and-multiply UEB coming from a classical Latin square.

## What counts as a win
A set {U_1,...,U_36} of 6 x 6 unitaries with Tr(U_j* U_k) = 6 delta_{jk}, whose underlying quantum Latin square is provably non-classical (its cells are not a permutation of a fixed basis). One-sided: such a UEB is a new object beyond the classically-derived and group-type constructions.

## Checker
Verify each U_j is unitary (U_j* U_j = I) and Tr(U_j* U_k) = 6 delta_{jk} for all pairs (exact over algebraic entries). Extract the associated quantum Latin square and certify it non-classical: some cell vector is not proportional to a standard basis vector, and the square is not monomially equivalent to a classical one (finite invariant check). Runtime: seconds.

## Search plan
Use the Musto-Vicary correspondence: an order-6 quantum Latin square plus complex Hadamard matrices yields a shift-and-multiply UEB. Feed in a genuinely quantum order-6 QLS (from the AME(4,6) circle of constructions), then verify the resulting UEB is inequivalent to nice/classical ones.

## Prior art (verify)
UEBs and their equivalence classes are studied by Werner (2001) and Musto-Vicary (2016); whether small dimensions admit UEBs outside the nice / classical shift-and-multiply families is open, with order 6 the natural test case. Confirm no classification rules this out.
