# A fourth Brown number (Brocard's problem)

**Find.** Integers n > 7 and m with n! + 1 = m^2, a solution to Brocard's problem beyond the three known pairs (n, m) = (4, 5), (5, 11), (7, 71).

**What counts as a win (one-sided).** One pair (n, m) with n! + 1 a perfect square and n > 7. A single new solution settles the "only three known" state; failure proves nothing.

**Checker (seconds).** For candidate n, test whether n! + 1 is a perfect square via an exact integer square root (isqrt). To search fast without giant factorials, test n! + 1 for squareness modulo many primes first (a square must be a quadratic residue everywhere), rejecting almost all n cheaply. Certify a hit with exact big-integer isqrt.

**Search plan.** Sieve n over a large range using the modular-quadratic-residue filter (compute n! mod q incrementally for a panel of primes q, discard n where n! + 1 is a non-residue mod any q); only survivors get the exact isqrt test. Extend past the last published search bound.

**Prior art (verify).** Brocard's problem asks whether n! + 1 = m^2 has solutions besides n = 4, 5, 7; it is conjectured (Erdos) there are no others, and searches (Berndt-Galway and later) extended into the 10^9-10^12 range without a fourth. Open, under-tested relative to the flagship conjectures. See OEIS A146968 / A085692 and the Brocard-problem literature (verify the search bound).
