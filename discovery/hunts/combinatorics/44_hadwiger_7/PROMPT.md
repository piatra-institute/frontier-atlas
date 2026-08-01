# 44. Counterexample to Hadwiger's Conjecture for t = 7

**Target.** Find a graph G that is 7-chromatic but has no K7 minor. Hadwiger's Conjecture asserts every graph with no K_t minor is (t-1)-colorable; equivalently every t-chromatic graph has a K_t minor. The cases t <= 6 are theorems (t = 6 via the Four Color Theorem, Robertson-Seymour-Thomas); t = 7 is open. A 7-chromatic K7-minor-free graph refutes it for t = 7.

**What counts as a win.** One explicit graph with chromatic number exactly 7 and no K7 minor refutes Hadwiger for t = 7 (one-sided NO). Both properties are exactly certifiable.

**Checker (seconds).** Read G (graph6). Verify chi(G) = 7: not 6-colorable (SAT UNSAT with DRAT) and 7-colorable (an explicit coloring). Verify no K7 minor: exact minor test (branch-and-bound over the 7 branch sets / rooted-minor model). Keep G to a few dozen vertices so both checks finish in seconds.

**Search plan.** Start from dense 7-chromatic graphs with bounded structure (e.g. specific graph products, line graphs, or graphs from the known tightness of t <= 6 extremal families) and delete/contract to destroy all K7 minors while holding chromatic number at 7; local search alternating "increase chromatic number" and "reduce connectivity toward minor-free"; test candidate families with a fast minor filter first, exact SAT second.

**Prior art (verify).** Hadwiger's Conjecture for t = 7 is open (surveys by Seymour, "Hadwiger's conjecture"). No counterexample is known for any t. Re-verify status; this is a hard target and any near-miss (7-chromatic with only sparse K7 minors) is worth documenting honestly.

**Openness:** documented-open. **Win-type:** counterexample.
