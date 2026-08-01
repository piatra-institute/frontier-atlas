# Counterexample to the lonely runner conjecture

**Refute.** The lonely runner conjecture, in the standard normalization with n runners: one runner fixed at the origin (speed 0) and n-1 runners with distinct nonzero integer speeds v_1, ..., v_{n-1} on a unit-circumference track. The conjecture asserts some time t makes every moving runner at distance at least 1/n from the origin, i.e. {v_i t} in [1/n, 1 - 1/n] for all i simultaneously. Find a speed set for which no such t exists, at the smallest open number of runners (currently n = 8, i.e. 7 nonzero speeds).

**What counts as a win (one-sided).** One speed set for which the gap 1/n is never simultaneously attained. A single such set refutes the conjecture; failure proves nothing.

**Checker (seconds).** For integer speeds the "good" times form a union of intervals with rational endpoints (multiples of 1/(n v_i)); the covering condition "no t works" is decided exactly over the finite set of critical rationals within one period. Verify with exact rational arithmetic that the required simultaneous window is empty.

**Search plan.** Enumerate distinct-speed tuples up to a bound (normalize by gcd and by the standard reductions), and for each test the covering condition exactly; prune using necessary conditions from the proven small cases. Focus near known tight (extremal-gap) configurations.

**Prior art (verify).** The lonely runner conjecture is proven through the 7-runner case (Barajas and Serra, ca. 2008, and earlier work for fewer runners) and is open for 8 runners and beyond. See the lonely-runner survey literature (Bienia et al.; Barajas-Serra). Confirm the current proven range before fixing the target n (verify).
