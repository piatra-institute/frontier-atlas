# Batch sweep: refute graph-energy bounds and find equienergetic witnesses

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit graph violating a stated energy bound, or an equienergetic non-cospectral pair, or hardened survivors. Both a refutation and a witness pair are clean wins.

**Family + panel.** Connected graphs; energy-type invariants: graph energy E(G)=Σ|λi|, Estrada index Σe^{λi}, Laplacian-energy-like LEL, incidence energy, Laplacian energy, and the derived notions hyperenergetic (E>2n−2), hypoenergetic, and equienergetic (equal E, non-cospectral).

**Enumerate.** nauty `geng`, connected graphs to n=9 (A001349: 1,1,2,6,21,112,853,11117,261080), n=10 if time; regular graphs as a stress class (energy interacts cleanly with regularity).

**Conjecture generation.** Harvest bounds from the "Graph Energy" literature (Li-Shi-Gutman, 2012, and Gutman's MATCH open-problem lists): the Koolen-Moulton upper bound and its tightness cases, Estrada-index bounds (de la Pena-Gutman-Rada, Linear Algebra Appl. 427, 2007), and LEL/incidence-energy comparisons — several stated bounds are tight only at special graphs and untested broadly. Also hunt equienergetic non-cospectral pairs (a witness search): bucket graphs by exact energy.

**Adversarial families.** Complete bipartite and cocktail-party graphs, line graphs of regular graphs (classical equienergetic source), circulants, and Cartesian/tensor products (energy is sub/super-additive across products, giving large-n test points).

**Checker (exact).** Compute eigenvalues to high precision and certify strict bound margins by exact characteristic-polynomial root isolation; energy equality for a pair is confirmed only if the multiset of |λi| sums agree under certified bounds AND the graphs are non-cospectral (distinct charpolys). Emit graph6.

**Verification discipline.** Generator is not verifier: two spectrum computations (dense eigensolver vs exact charpoly) must agree; audit Σλi=0, Σλi^2=2m. No strict inequality decided on float. Cite each bound or mark "could not verify." Report candidates generated / broken / survived, with graph6 witnesses and equienergetic pairs.
