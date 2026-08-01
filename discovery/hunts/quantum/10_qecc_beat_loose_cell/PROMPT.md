# A stabilizer code beating a loose codetables cell

**Find:** a binary stabilizer code [[n,k,d]] whose distance d exceeds the current best-known lower bound for that (n,k), at a cell where the tabulated lower and upper bounds still differ.

## What counts as a win
Explicit stabilizer generators achieving [[n,k,d']] with d' > previous best-known d. One-sided: it raises the record for that cell.

## Checker
Write the n-k generators as symplectic vectors in GF(2)^{2n}. Verify pairwise commutation (symplectic inner product 0) and independence. Compute the exact minimum distance: the least weight of a Pauli operator in the normalizer but not the stabilizer (for k>0), by coset-leader / exact minimum-weight search over GF(2), feasible for n up to roughly 30. Runtime: seconds to minutes at small n.

## Search plan
Start from CSS codes built on good classical binary codes, and from graph/quasi-cyclic stabilizer constructions; local search (add/swap generators) maximising distance under the commutation constraint. Confirm each candidate distance with an independent minimum-weight solver (ILP and a coset search).

## Prior art (verify)
codetables.de (Grassl, "Bounds on the parameters of quantum codes") lists best-known [[n,k,d]] with open gaps between lower and upper bounds. Pick a loose cell and re-verify the current record before claiming an improvement.
