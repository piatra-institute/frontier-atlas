# 42. A de Bruijn sequence with an extra structural property

**Find.** A de Bruijn sequence B(k, n) carrying an additional constraint whose existence at the target parameters is open. Candidates: a *single-track* de Bruijn sequence (all k^n windows distinct AND the sequence's cyclic shifts by fixed amounts recover the coordinates) at an open (k, n); a de Bruijn sequence that is simultaneously a valid "perfect necklace"; or one whose window values form a specified permutation pattern. Several such constrained-de-Bruijn existence questions at small parameters are unresolved (verify the target).

**What counts as a win.** One explicit cyclic sequence over {0..k-1} of length k^n whose length-n windows are all k^n distinct strings (de Bruijn) AND that satisfies the stated extra property. One-sided: a single witness settles existence for those parameters.

**Checker (seconds).** Slide the length-n window cyclically; collect all k^n windows into a set and assert every length-n string appears exactly once (de Bruijn condition). Then verify the extra property directly (e.g. for single-track: check the fixed-shift coordinate reconstruction). O(k^n * n), fast for the small parameters at issue.

**Search plan.** Structured: Hamiltonian/Eulerian search on the de Bruijn graph restricted by the extra constraint; SAT/CP encoding both the coverage and the structural property; adapt known constructions (prefer-one, Lempel's D-morphism, Gorski/Etzion single-track constructions) and repair to hit the open case.

**Prior art (verify).** de Bruijn (1946); Etzion & Lempel on single-track / constrained de Bruijn sequences; the constrained-de-Bruijn existence tables (verify which (k, n) with the chosen property are open).
