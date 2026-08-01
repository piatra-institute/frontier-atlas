# Batch sweep: refute distance-matrix spectral bounds

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit graph violating a stated distance-spectral bound, or hardened survivors. Refutation is the clean win.

**Family + panel.** Connected graphs; distance matrix D (entries d(u,v)) and distance-Laplacian / distance-signless-Laplacian: distance spectral radius ∂1, smallest distance eigenvalue ∂n, distance spread, distance energy Σ|∂i|, and distance-Laplacian spectral radius. Track n, diameter, Wiener index W (note ∂1 relates to average row sum 2W/n).

**Enumerate.** nauty `geng`, connected graphs to n=9 (A001349: 1,1,2,6,21,112,853,11117,261080); trees and unicyclic graphs separately, since minimiser/maximiser conjectures are class-specific.

**Conjecture generation.** Harvest from Aouchiche-Hansen "Distance spectra of graphs: a survey" (Linear Algebra Appl. 458, 2014) and their distance-Laplacian conjectures (Linear Algebra Appl. 2013), a set with several AutoGraphiX-generated bounds, some later refuted. Auto-fit ∂1-vs-(n,W,diam) and distance-energy bounds on n≤7.

**Adversarial families.** Long paths and caterpillars (large diameter drives ∂1), complete-split, brooms, theta graphs, kneser, and grid/prism products; barbell graphs (two cliques joined by a path) which push distance extremes.

**Checker (exact).** Recompute D by all-pairs BFS independently; compute distance eigenvalues to high precision and certify strict margins with exact charpoly root isolation. Emit violators in graph6.

**Verification discipline.** Generator is not verifier: two distance-matrix builds (BFS vs Floyd-Warshall) and two eigenvalue computations must agree; audit Σ∂i=0 and the row-sum relation to Wiener index. Cite each tested bound or mark "could not verify." Report candidates generated / broken / survived, graph6 witnesses.
