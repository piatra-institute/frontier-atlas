# Four mutually unbiased bases in C^6

**Find:** four orthonormal bases of C^6 that are pairwise mutually unbiased. Equivalently, three complex 6x6 Hadamard matrices H1, H2, H3 (all entries unimodular, Hk Hk* = 6 I) such that H1, H2, H3 and every ratio Hi* Hj / sqrt(6) are again complex Hadamard.

## What counts as a win
An explicit set {B0=I, B1, B2, B3} of four bases (or the three Hadamards). Existence is one-sided: producing the object settles it and refutes the standing numerical consensus that the maximum in d=6 is 3.

## Checker
For every pair a<b form M = Ba* Bb. Verify each column of each Bk is orthonormal (Bk* Bk = I) and that every entry of M satisfies |M_ij|^2 = 1/6 exactly. Over algebraic amplitudes this is exact; otherwise use interval arithmetic with certified error < 1e-30. Runtime: microseconds (four 6x6 matrices).

## Search plan
Numerical: parametrise B1..B3 as products of a 6x6 complex Hadamard family (Fourier F6(a,b), Karlsson, spectral S6) times phases, maximise the MUB defect by gradient/seesaw, then attempt exact reconstruction of any near-solution over a cyclotomic field. Algebraic: search Hadamard triples inside the known order-6 families; SAT/CAS over roots of unity for structured (Butson) subcases.

## Prior art (verify)
Maximum number of MUBs in C^6 is a long-standing open problem; only 3 are known, none proven maximal (Zauner; Grassl; Brierley-Weigert; Raynal-Lu-Englert). Heavy numerical evidence against a 4th, no proof.
