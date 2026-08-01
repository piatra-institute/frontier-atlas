# A stabilizer decomposition of |T>^n below the rank record

**Find:** an exact stabilizer-rank decomposition of the n-fold magic state |T>^{tensor n} using fewer stabilizer states than the best-known upper bound for that n.

## What counts as a win
An explicit list of chi stabilizer states |s_1>,...,|s_chi> and coefficients c_1,...,c_chi with |T>^{tensor n} = sum_j c_j |s_j> exactly, where chi is smaller than the current best upper bound on the stabilizer rank. One-sided: a smaller exact decomposition is a new upper-bound record.

## Checker
Each |s_j> is given by n stabilizer generators (or as an explicit 2^n vector over the ring Z[1/sqrt2, zeta_8]); verify it is a stabilizer state (its generators commute and are independent Paulis). Verify the exact vector identity sum_j c_j |s_j> = |T>^{tensor n} entrywise over the ring. Runtime: seconds for small n.

## Search plan
Search over structured stabilizer supports (Reed-Muller / self-dual patterns) and solve the exact linear system for the coefficients over the ring; iteratively drop terms and re-solve to shrink chi. Seed from known good small-n decompositions and take tensor/recursive products.

## Prior art (verify)
Upper bounds on the stabilizer rank of |T>^{tensor n} are actively improved (Bravyi-Smith-Smolin; Bravyi-Gosset; Qassim-Pashayan-Gosset 2021; later work). Records are loose. Re-verify the current best chi for the chosen n before claiming an improvement.
