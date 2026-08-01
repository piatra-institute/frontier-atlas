# An exact SIC fiducial in a dimension with no exact solution

**Find:** an exact (algebraic) Weyl-Heisenberg covariant SIC-POVM fiducial vector in a dimension d where no exact solution is on record (smallest gaps: d = 22, 23, 25, 26, 27, 29, ...).

## What counts as a win
Exact coordinates of a fiducial |f> in C^d (entries in an explicit number field) generating a SIC. One-sided: an exact solution in a gap dimension is a new entry on the exact-SIC frontier.

## Checker
Let D_{a,b} = X^a Z^b be the d^2 Weyl-Heisenberg displacement operators. Verify |<f | D_{a,b} | f>|^2 = 1/(d+1) for all (a,b) != (0,0), and <f|f> = 1. With algebraic entries this is exact arithmetic over the field; d^2 - 1 overlaps of length-d vectors. Runtime: seconds.

## Search plan
Compute a high-precision numerical fiducial by the standard variational search over the WH orbit. Then reconstruct the minimal polynomial / number field of the fiducial coordinates via integer-relation (PSLQ/LLL) and Galois-structure heuristics (Appleby-Grassl-Scott-Yard style), and certify the reconstructed exact vector with the checker above.

## Prior art (verify)
Exact WH-SIC fiducials are published for d = 1..21, 24, 28, 30, 31, 35, 37, 39, 43, 48, 53, 124, 323 and a few more; other dimensions have only numerical solutions (Scott-Grassl 2010; Grassl-Scott 2017; Fuchs-Hoang-Stacey catalogue). Confirm the target dimension still lacks an exact solution.
