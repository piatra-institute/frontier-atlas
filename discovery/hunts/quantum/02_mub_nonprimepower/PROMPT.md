# A fourth MUB in a non-prime-power dimension

**Find:** four mutually unbiased bases in C^d for a non-prime-power d where only three are known, primarily d=10 (also d=14, d=22, all of the form 2p).

## What counts as a win
An explicit fourth basis unbiased to a known MUB triple in C^10 (or C^14, C^22). One-sided: any valid quadruple beats the current record of 3 and constrains the general non-prime-power MUB question.

## Checker
Given B0,B1,B2,B3 (d x d), verify Bk* Bk = I for each, and for every pair a<b that all entries of Ba* Bb have squared modulus 1/d. Exact over algebraic entries, else certified interval arithmetic. Runtime: milliseconds.

## Search plan
Seed with the standard triple (product construction from the prime-power factor, or a Fourier-based triple). Numerically optimise a candidate 4th basis to minimise total unbiasedness defect (seesaw / Riemannian gradient over the unitary group), then reconstruct exactly over a small number field. Also try Butson/cyclotomic ansatze and MUB-from-Latin-square constructions over Z_d.

## Prior art (verify)
For d = 2p the number-theoretic lower bound gives only 3 MUBs, and whether a 4th exists is open for all such d (d=6,10,14,22,...). The maximum number of MUBs is unknown for every non-prime-power dimension (Boykin et al.; Bengtsson; Durt-Englert-Bengtsson-Zyczkowski review).
