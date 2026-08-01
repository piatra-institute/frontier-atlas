# 32. The period of Treblecross (octal game 0.007)

**Find.** A period (and pre-period) for the Sprague-Grundy nim-sequence of the octal game 0.007, i.e. one-dimensional Treblecross. Flammenkamp has computed its nim-values past 2^25 (over 11 million values, largest G = 1401) with no period found; whether the sequence is ultimately periodic is a famous open octal-games question. Guy conjectures all finite-octal games are ultimately periodic.

**What counts as a win.** A stated pre-period p0, period P, and saltus, together with the finite certificate below. One-sided: the arithmetic-periodicity theorem turns a sufficiently long verified periodic stretch into a proof of eventual periodicity forever. (Almost everyone expects no small period exists; this is an honest long shot, but the win, if any, is finitely checkable.)

**Checker (seconds-to-minutes).** Recompute the nim-sequence G(n) = mex over the game's moves up to the Guy-Smith bound 2*(p0 + P) + (largest heap referenced in the octal code); assert G(n + P) = G(n) throughout that range (with the saltus for the "0.007" move set). If it holds to the bound, ultimate periodicity is proved. Exact integer mex computation.

**Search plan.** Structured: extend the nim-value computation with Flammenkamp's sparse-space / bit-parallel mex techniques; scan every prefix for a candidate (p0, P) and test the periodicity condition. Realistically a negative or inconclusive result; report the frontier reached.

**Prior art (verify).** Flammenkamp, "Sprague-Grundy values of octal games" (uni-bielefeld.de/~achim/octal.html; unsettled.txt); Guy & Smith arithmetic-periodicity theorem; Guy, "Unsolved Problems in Combinatorial Games." Open.
