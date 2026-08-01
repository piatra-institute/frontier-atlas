# A fourth Wilson prime

**Find.** A prime p with p^2 dividing (p-1)! + 1 (a Wilson prime) beyond the three known: 5, 13, 563.

**What counts as a win (one-sided).** One prime p for which the Wilson quotient ((p-1)! + 1)/p is divisible by p. A single new prime settles the "only three known" state; failure proves nothing.

**Checker (seconds).** For a candidate p, compute (p-1)! + 1 mod p^2 by a fast modular product (or use the Wilson quotient recurrence) and assert it is 0 mod p^2. Each candidate is a fast modular computation; verify with an independent routine (e.g. a Wilson-quotient identity).

**Search plan.** Sieve primes in a range beyond the last exhaustive search bound; for each, compute the Wilson quotient modulo p^2 using an optimized modular factorial (product tree, or the known congruences that speed the residue). Distribute across ranges; the check is cheap per prime, so extend the searched interval as far as compute allows.

**Prior art (verify).** Only three Wilson primes are known (5, 13, 563), and searches have extended past 2 x 10^13 (Costa, Gerbicz, Harvey and earlier work) without finding a fourth. A fourth is expected on heuristic grounds but not found; the search is extendable on a workstation. See the Wilson-prime search literature and OEIS A007540. Open, under-tested (verify the current search bound).
