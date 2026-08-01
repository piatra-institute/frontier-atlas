# A third Wolstenholme prime

**Find.** A prime p >= 5 with the Wolstenholme property C(2p-1, p-1) congruent to 1 modulo p^4 (equivalently p divides the numerator of the Bernoulli number B_{p-3}), beyond the two known: 16843 and 2124679.

**What counts as a win (one-sided).** One further Wolstenholme prime. A single new prime settles the "only two known" state; failure proves nothing.

**Checker (seconds).** For candidate p, test C(2p-1, p-1) mod p^4 via harmonic-sum congruences, or compute the numerator of B_{p-3} mod p. Each candidate is a fast modular computation; confirm with an independent formulation (the Bernoulli-number criterion versus the binomial criterion).

**Search plan.** Sieve primes beyond the last search bound; for each compute the relevant residue (harmonic sums H_{p-1} and related mod p^4, or B_{p-3} mod p) using fast modular arithmetic. The per-prime cost is low, so push the interval as far as compute allows; parallelize over ranges.

**Prior art (verify).** Only two Wolstenholme primes are known (16843, 2124679); searches (McIntosh and others) extended past 10^9 without a third. A third is expected heuristically but unfound, and the search is extendable on a workstation. See the Wolstenholme-prime literature and OEIS A088164. Open, under-tested (verify the current search bound).
