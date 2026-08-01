# Real MUBs beyond the known count

**Find:** a set of real mutually unbiased bases in R^d exceeding the largest known set, for an open d where the maximum r(d) is undetermined.

## What counts as a win
Real orthonormal bases B0,...,Bm (entries real) with more members than the best known construction for that d. One-sided: any larger valid set improves the record on r(d).

## Checker
Verify each Bk is a real orthogonal matrix (Bk^T Bk = I). For every pair a<b verify that all entries of Ba^T Bb have squared value 1/d (real unbiasedness). All entries rational or algebraic, so the check is exact rational linear algebra in milliseconds.

## Search plan
Real MUBs correspond to specific association schemes and to collections of {+1,-1}/sqrt(d) matrices; enumerate via difference sets, Hadamard-matrix pairs, and quaternary-code constructions. Numerically optimise real orthogonal frames for the unbiasedness constraint, then round to exact rationals. SAT/ILP over sign patterns for small d.

## Prior art (verify)
The maximum number of real MUBs r(d) is bounded by d/2 + 1 for d = 0 mod 4 and is exactly determined only in special dimensions; many cells are open (Boykin-Sitharam-Tarifi-Wocjan; LeCompte-Martin-Owens; Cameron-Seidel connection to association schemes). Confirm the specific target cell is still undetermined.
