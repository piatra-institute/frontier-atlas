# An AME state at an open cell of the AME table

**Find:** an absolutely maximally entangled (AME) pure state of n qudits of local dimension d for an (n,d) cell listed as undetermined in the table of AME states.

## What counts as a win
An explicit state vector |psi> in (C^d)^{tensor n}, ideally with algebraic amplitudes, whose every bipartition of floor(n/2) parties is maximally mixed. One-sided: existence resolves the cell affirmatively.

## Checker
For every subset S of parties with |S| = floor(n/2), compute the reduced density matrix rho_S by tracing out the complement and verify rho_S = I / d^{|S|} exactly. By purity it suffices to check all floor(n/2)-subsets. With amplitudes in a cyclotomic field the trace-outs are exact; number of subsets is polynomial and each RDM is small. Runtime: seconds.

## Search plan
Classical route: build from an MDS / Reed-Solomon code (works when d >= n-1). For hard cells with small d, imitate the golden AME(4,6): search 2-unitary / perfect-tensor structure by nonlinear optimisation over unitaries, then reconstruct exact entries. Also search minimal-support states over orthogonal arrays IrOA(strength floor(n/2)).

## Prior art (verify)
Qubit AME exist only for n = 2,3,5,6 (settled). For d >= 3 many (n,d) cells remain open; see the table of AME states maintained by Huber and Wyderka (tp.nt.uni-siegen.de). Re-verify the chosen cell has not been closed since.
