# Batch sweep: refute distance-based graph-index inequalities

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit graph violating a stated distance-index bound, or hardened survivors. Refutation is the clean win.

**Family + panel.** Connected graphs; distance indices: Wiener W=Σ_{u<v}d(u,v), Szeged Sz=Σ_{uv}n_u·n_v, revised Szeged, PI index, Mostar Mo=Σ_{uv}|n_u-n_v|, degree distance, Harary Σ1/d(u,v), eccentric connectivity Σ d(v)·ecc(v), Balaban, and diameter/radius. Here n_u, n_v count vertices closer to each endpoint of edge uv.

**Enumerate.** nauty `geng`, connected graphs to n=9 (A001349: 1,1,2,6,21,112,853,11117,261080); trees, unicyclic, bicyclic families separately, since many conjectures are class-specific.

**Conjecture generation.** Harvest from Wiener 1947; the Szeged-Wiener relation Sz≥W (a theorem, use as a validation check); Mostar-index conjectures (Doslic et al. 2018 and follow-ups on trees/bicyclic/fullerene extremes, several refuted by computer search); and the Aouchiche-Hansen AutoGraphiX "Distance in graphs" conjecture series (Discrete Appl. Math.), which includes several later-refuted bounds. Auto-fit index-vs-(n,diam,W) bounds on n≤7.

**Adversarial families.** Caterpillars, brooms, theta graphs, cycle-with-pendants, long paths, complete-split, and Cartesian products (grids, prisms, hypercubes) pushed large: distance indices grow fast, so extremal shapes surface counterexamples that small enumeration hides.

**Checker (exact).** Recompute all pairwise distances (BFS from every vertex) and the n_u/n_v edge partitions independently; every index is an exact integer or rational sum. Emit violators in graph6.

**Verification discipline.** Generator is not verifier: recompute distances with a second all-pairs routine (BFS vs Floyd-Warshall) and confirm Sz≥W and Wiener=½Σ of the distance matrix as internal consistency checks. Cite each tested bound or mark "could not verify." Report candidates generated / broken / survived, graph6 witnesses.
