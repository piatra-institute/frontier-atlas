# 41. Counterexample to the Cycle Double Cover Conjecture

**Target.** Find a bridgeless graph with no cycle double cover: a bridgeless graph for which there is no collection of cycles covering every edge exactly twice. The Cycle Double Cover Conjecture (Szekeres, Seymour) asserts every bridgeless graph has one; the minimal counterexamples, if any, are snarks (cyclically-4-edge-connected cubic graphs of girth >= 5, chromatic index 4).

**What counts as a win.** One explicit bridgeless graph together with a certified proof that no cycle double cover exists refutes the conjecture (one-sided NO). The certificate is UNSAT of the cover constraint.

**Checker (seconds).** Read G (graph6), bridgeless cubic. Decide existence of a cycle double cover by SAT: choose a set of cycles (or, equivalently, an even-subgraph decomposition) such that each edge is in exactly two; encode candidate cycles / a suitable flow model and require every edge covered exactly twice. UNSAT (with DRAT proof) certifies no CDC. For small snarks this runs in seconds.

**Search plan.** Draw candidate snarks from the complete snark catalogue (Brinkmann, Goedgebeur, House of Graphs) and batch-test CDC existence; prioritize snarks with high oddness / resistance and non-cyclically-5-edge-connected structure, the theoretical danger zone; generate new snarks by known reductions and test.

**Prior art (verify).** The Cycle Double Cover Conjecture is open; every snark tested so far (all snarks up to 36+ vertices, via the House of Graphs snark lists) has a CDC. Re-verify the current tested frontier; a counterexample must be a snark that has escaped enumeration.

**Openness:** documented-open. **Win-type:** counterexample.
