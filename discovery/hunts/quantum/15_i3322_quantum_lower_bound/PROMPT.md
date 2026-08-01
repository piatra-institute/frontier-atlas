# A new lower bound on the I3322 quantum value

**Find:** an explicit finite-dimensional state and measurements giving an I3322 Bell value above the best published lower bound on its (unknown) quantum maximum.

## What counts as a win
A dimension d, a bipartite state rho on C^d tensor C^d, and dichotomic projective measurements {A1,A2,A3}, {B1,B2,B3} with I3322 value strictly greater than the current record. One-sided: any larger value is a valid new lower bound.

## Checker
Build the I3322 Bell operator M = sum of the Collins-Gisin coefficients times A_x tensor B_y (with the marginal terms). Verify each A_x, B_y is a valid dichotomic observable (Hermitian, eigenvalues in {+1,-1}, i.e. A_x^2 = I). Evaluate Tr(rho M). Report the largest eigenvalue of M as a state-optimal bound. Exact for algebraic entries, else interval arithmetic with certified two-sided bounds. Runtime: seconds.

## Search plan
Seesaw optimisation over rho and measurements at increasing d (the maximum is believed to need d -> infinity); track the value versus d. Rationalise or algebraically certify any record-beating point, then confirm with the exact eigenvalue check.

## Prior art (verify)
The quantum maximum of I3322 is unknown; Pal and Vertesi (2010) gave the best numerical lower bound and conjectured infinite dimension is required (Open Quantum Problems, oqp.iqoqi.oeaw.ac.at, "All the Bell inequalities"). Re-verify the current record before claiming an improvement.
