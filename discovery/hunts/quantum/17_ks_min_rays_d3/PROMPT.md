# A Kochen-Specker set in dimension 3 below 31 rays

**Find:** a set of fewer than 31 rays in R^3 that is Kochen-Specker uncolorable, beating the standing Conway-Kochen record.

## What counts as a win
An explicit list of unit vectors in R^3 (rational/algebraic coordinates) whose orthogonality structure admits no valid {0,1} coloring, with fewer than 31 rays. One-sided: any smaller uncolorable set lowers the record.

## Checker
From the vectors compute the orthogonality graph exactly (<u,v> = 0 tests over the exact field). A valid coloring assigns 0/1 to each ray so that no two orthogonal rays are both 1 and every complete orthogonal triad (basis) has exactly one 1. Encode as a SAT/CSP instance and prove UNSAT (a resolution/DRAT certificate), certifying uncolorability. Runtime: seconds to minutes.

## Search plan
Grow candidate ray sets from dense orthogonality graphs (rational unit vectors, orthad-rich configurations) and use SAT with symmetry breaking (nauty orbits) to test colorability; minimise ray count by MUS extraction. Certify every UNSAT with an independent checker.

## Prior art (verify)
The smallest known KS set in dimension 3 has 31 rays (Conway-Kochen); computer search gives a lower bound near 24, so the minimum is open after about 60 years (recent SAT + nauty studies re-certify 31 within specific search spaces). Overlaps the atlas problem physics/01_kochen_specker_minimal.
