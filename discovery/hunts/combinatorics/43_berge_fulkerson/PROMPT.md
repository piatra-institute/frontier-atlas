# 43. Counterexample to the Berge-Fulkerson Conjecture

**Target.** Find a bridgeless cubic graph whose edges cannot be covered by six perfect matchings such that every edge lies in exactly two of them. The Berge-Fulkerson Conjecture asserts every bridgeless cubic graph admits such a family of six perfect matchings. The candidate counterexamples are snarks. A single certified failure refutes it.

**What counts as a win.** One explicit bridgeless cubic graph with a certified proof that no six perfect matchings double-cover its edges refutes the conjecture (one-sided NO). The certificate is UNSAT of the covering constraint.

**Checker (seconds).** Read G (graph6), cubic bridgeless. Enumerate all perfect matchings of G (fast for tens of vertices). Decide by SAT/ILP whether some multiset of six perfect matchings covers each edge exactly twice (select-with-multiplicity variables over the matchings, edge-coverage = 2 constraints). UNSAT certifies no Berge-Fulkerson cover. Seconds for small snarks.

**Search plan.** Test snarks from the House of Graphs snark catalogue, prioritizing those with high oddness, high resistance, or few perfect matchings (graphs with few perfect matchings are the theoretical danger zone, cf. the Fan-Raspaud subcase); generate new snarks by reductions and batch-test.

**Prior art (verify).** The Berge-Fulkerson Conjecture is open; it implies the weaker Fan-Raspaud and 5-cycle-double-cover statements. Every snark tested has a cover. Re-verify the tested frontier (snarks are enumerated to 36+ vertices via House of Graphs).

**Openness:** documented-open. **Win-type:** counterexample.
