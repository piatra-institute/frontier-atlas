# Counterexample to the antimagic labeling conjecture

**Refute.** The Hartsfield-Ringel antimagic conjecture: find a connected graph G with more than two vertices that has no antimagic edge labeling (a bijection from the edges to {1, ..., m} such that the vertex sums, each vertex summed over its incident edge labels, are all distinct).

**What counts as a win (one-sided).** One connected graph on at least 3 vertices for which no antimagic labeling exists. A single such graph refutes the conjecture; failure proves nothing.

**Checker (seconds).** Given a candidate G, prove no antimagic labeling exists: encode "assign a permutation of {1..m} to edges with all vertex sums distinct" as a SAT/CP instance and certify unsatisfiability (DRAT proof), or exhaust the m! labelings with strong pruning for small m. Independently confirm the UNSAT certificate. For a claimed labeling of any subcase, verify vertex sums are distinct directly.

**Search plan.** Target structured candidates where vertex-sum collisions are forced: highly symmetric regular graphs, certain trees and disconnected-looking dense graphs, and graphs with many degree-equal vertices. For each candidate run the SAT non-existence check; batch over a catalogue of small graphs (nauty geng). The conjecture is proven for many classes, so search outside them.

**Prior art (verify).** Hartsfield and Ringel conjectured every connected graph except K_2 is antimagic; it is proven for many families (dense graphs, regular graphs, trees with at most one degree-2 vertex, and others) but open in general. See Hartsfield-Ringel and the antimagic-labeling survey literature (Gallian's dynamic survey on graph labeling). Open (verify).
