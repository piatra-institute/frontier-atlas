# A minimum-size unextendible product basis on p qubits

**Find:** an unextendible product basis (UPB) on p qubits, with p a multiple of 4 greater than 4 (p = 8, 12, 16, ...), of size at or below the current best-known upper bound, in the range where the minimum cardinality is still open.

## What counts as a win
A set of orthogonal product vectors { tensor_i |v_j^i> } in (C^2)^{tensor p} that no product vector is orthogonal to, of size smaller than the best construction known for that p. One-sided: a smaller UPB tightens the minimum.

## Checker
(1) Orthogonality: every pair of members is orthogonal in at least one qubit factor (the single-qubit vectors there are orthogonal), verified exactly. (2) Unextendibility: the multilinear system "a product vector orthogonal to all members" has no solution, proved by the formally-orthogonal-matrices / graph criterion or by Groebner elimination over the exact field. Runtime: seconds.

## Search plan
Use the method of formally orthogonal matrices and the orthogonality-graph characterisation to build small candidate UPBs, then certify unextendibility exactly. Local search over qubit assignments to shrink size.

## Prior art (verify)
Johnston (2013) and Chen-Johnston (2015) determined the minimum qubit UPB size in all cases except when the number of parties is a multiple of 4 greater than 4, which remains open. Confirm the target p is still in the open range.
