# 39. Counterexample to the Total Coloring Conjecture

**Target.** Find a graph G with total chromatic number chi''(G) >= Delta(G) + 3. The Total Coloring Conjecture (Behzad, Vizing) asserts every graph satisfies chi'' <= Delta + 2. A single graph needing Delta + 3 total colors refutes it. The conjecture is proven for many classes (Delta <= 5, planar with large Delta, etc.), so a counterexample would be sparse and structurally special.

**What counts as a win.** One explicit graph G together with a certified value chi''(G) >= Delta + 3 refutes the conjecture (one-sided NO). The certificate is a proof that no total coloring with Delta + 2 colors exists.

**Checker (seconds).** Read G (graph6). Compute Delta. Decide total-(Delta+2)-colorability exactly by SAT: variables assign a color in {1..Delta+2} to each vertex and edge; clauses forbid equal colors on adjacent vertices, on incident edges, and on a vertex and its incident edge. UNSAT (with a DRAT proof) certifies chi'' >= Delta + 3. Feasible for graphs with a few dozen vertices/edges.

**Search plan.** Focus on hard classes: graphs where the "Type 2" gap is tight (Delta + 2 forced), then perturb toward Delta + 3; small dense graphs, cliques minus matchings, and Cayley graphs; enumerate small graphs with nauty and batch-test total-(Delta+2)-colorability, flagging any UNSAT.

**Prior art (verify).** The Total Coloring Conjecture is open in general (surveys by Yap, "Total Colourings of Graphs," and later). All small graphs tested so far are Type 1 or Type 2 (chi'' in {Delta+1, Delta+2}); no Delta+3 graph is known. Re-verify no counterexample has appeared.

**Openness:** documented-open. **Win-type:** counterexample.
