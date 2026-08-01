# A small-dimensional superactivation witness

**Find:** two quantum channels, each with zero quantum capacity, whose joint use has positive quantum capacity, in total dimension smaller than the best-known explicit superactivation example.

## What counts as a win
Choi matrices J1, J2 of channels N1, N2, each certified zero-capacity, plus a single input showing the joint channel has positive coherent information, at smaller input/output dimension than prior explicit constructions. One-sided: only the positive joint bound plus the two zero-capacity certificates count.

## Checker
Zero capacity of each channel via an exact structural certificate: PPT (partial transpose of the Choi matrix is PSD, so quantum capacity is 0) or antidegradability (an exact linear-algebra witness). Positivity of joint capacity: exhibit an input sigma with coherent information I_c(sigma, N1 tensor N2) > 0, certified by a two-sided interval bound on the entropies (rational spectra plus certified logarithms). Runtime: seconds.

## Search plan
Pair a PPT (Horodecki-type) channel with an erasure/symmetric channel; optimise the joint coherent information over inputs at small dimensions, shrinking the block sizes while keeping each factor PPT/antidegradable. Certify the final witness exactly.

## Prior art (verify)
Superactivation was discovered by Smith and Yard (2008) with sizeable dimensions; the minimal dimensions for explicit superactivation are not sharply established and remain an active target (recent "onset of superactivation" studies, 2026). Confirm the smallest current explicit example before claiming smaller.
