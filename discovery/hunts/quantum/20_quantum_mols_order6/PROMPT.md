# Mutually orthogonal quantum Latin squares of order 6 beyond the known count

**Find:** a set of k mutually orthogonal quantum Latin squares (QLS) of order 6 with k larger than the largest known set (classically N(6)=1; a quantum orthogonal pair is known via the AME(4,6) golden state).

## What counts as a win
k QLS of order 6, i.e. k arrays L^(1),...,L^(k) of unit vectors in C^6 with orthonormal rows and columns, that are mutually orthogonal, for k >= 3. One-sided: any set larger than the known maximum is a new record.

## Checker
For each L: every row is an orthonormal basis of C^6 and every column is an orthonormal basis (exact Gram = I). For each pair (L,M): the 36 vectors |L_ij> tensor |M_ij> form an orthonormal basis of C^6 tensor C^6 (their Gram matrix equals I, exact). Algebraic entries make this exact. Runtime: seconds.

## Search plan
Build from 2-unitary / perfect-tensor structure and from quantum-orthogonal decompositions of C^6 (Hadamard pairs on coordinate planes), extending the AME(4,6) construction; optimise a third square's entries for orthogonality against a fixed pair, then reconstruct exact vectors.

## Prior art (verify)
Musto-Vicary (2016) defined quantum Latin squares; Rather et al. (2022) gave an orthogonal QLS pair of order 6 (AME(4,6)); recent works build further order-6 QLS. Whether 3 or more mutually orthogonal QLS of order 6 exist is, to confirm, open.
