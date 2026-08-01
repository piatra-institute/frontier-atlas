# An unextendible maximally entangled basis at an open cell

**Find:** an unextendible maximally entangled basis (UMEB) in C^d tensor C^d, a set of orthonormal maximally entangled states of size less than d^2 whose orthogonal complement contains no maximally entangled state, for a (d, size) cell whose existence is undetermined.

## What counts as a win
An explicit set {|psi_1>,...,|psi_N>} of maximally entangled states, N < d^2, that is unextendible. One-sided: existence closes the cell.

## Checker
Each |psi_j> reshapes to a d x d matrix M_j; maximal entanglement means M_j M_j* = (1/d) I (proportional to unitary), verified exactly. Orthonormality via Tr(M_i* M_j) = delta_ij. Unextendibility: the orthogonal complement subspace V (in matrix space) contains no scalar multiple of a unitary; certify by showing the system M in V, M M* = c I has no solution (exact algebraic elimination for small d). Runtime: seconds.

## Search plan
Build members from mutually orthogonal unitary bases minus a sub-block, following the Bravyi-Smolin and Chen-Fei constructions; then certify complement-unitary-freeness by Groebner/resultant elimination. Vary N to reach an undetermined cell.

## Prior art (verify)
UMEBs were introduced by Bravyi-Smolin (2011) and Chen-Fei (2013); existence and achievable sizes N in C^d tensor C^d are open for many d. Confirm the target (d,N) cell is still undetermined.
