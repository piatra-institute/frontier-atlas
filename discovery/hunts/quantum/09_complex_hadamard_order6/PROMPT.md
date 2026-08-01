# A new isolated complex Hadamard matrix of order 6

**Find:** an isolated (defect 0) complex Hadamard matrix of order 6 that is not equivalent to the known isolated point (Tao's spectral matrix S6) and lies outside the known parametric families.

## What counts as a win
An explicit 6 x 6 unimodular H with H H* = 6 I, defect 0, and a computable invariant distinguishing it from S6 and from the catalogued families. One-sided: a genuinely new point advances the still-incomplete order-6 classification.

## Checker
Verify |H_ij| = 1 and H H* = 6 I exactly (algebraic entries). Compute the defect as the dimension of the solution space of the linearised Hadamard conditions at H; defect 0 certifies the matrix is isolated. Distinguish from S6 and known families by the Haagerup fingerprint invariant (the multiset of H_ij H_kl / (H_il H_kj)). Runtime: milliseconds.

## Search plan
Sample candidate points by numerical Hadamard optimisation off the known families, keep those with numerically vanishing defect, then reconstruct exact entries over a number field. Also search Butson BH(6,q) points and self-adjoint order-6 orbits for new isolated members.

## Prior art (verify)
The full classification of 6 x 6 complex Hadamard matrices is open; known objects include the Fourier family, Karlsson's parametric families, and Tao's isolated S6 (Tadej-Zyczkowski catalogue at chaos.if.uj.edu.pl/~karol/hadamard/). Confirm no complete classification or new isolated point has appeared.
