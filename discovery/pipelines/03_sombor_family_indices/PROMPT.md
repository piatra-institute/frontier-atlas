# Batch sweep: refute Sombor-family index bounds (fresh vein)

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit graph violating a post-2021 Sombor-index bound, or hardened survivors. This is the freshest and most fragile degree-index vein; refutation is the clean win.

**Family + panel.** Connected graphs; Sombor index SO=Σ_{uv}√(d(u)^2+d(v)^2) and its relatives: reduced Sombor Σ√((d(u)-1)^2+(d(v)-1)^2), average Sombor, modified Sombor Σ1/√(d(u)^2+d(v)^2), Sombor spectral radius and Sombor energy (eigenvalues of the SO-weighted adjacency matrix). Track n, m, Δ, δ, and comparisons to Zagreb/Randic.

**Enumerate.** nauty `geng`, connected graphs to n=9 (A001349: 1,1,2,6,21,112,853,11117,261080); trees to n=14 (A000055) for tree-specific claims.

**Conjecture generation.** Harvest bounds from the Sombor literature since Gutman's introduction (MATCH Commun. Math. Comput. Chem. 86, 2021) and the flood of 2021-2025 bound papers relating SO to M1/M2, spectral radius, energy, and chromatic number. Many are stated with equality only at extremal graphs and are untested outside trees. Auto-fit SO-vs-invariant bounds on n≤7.

**Adversarial families.** Complete bipartite, Turan, cocktail-party, kneser, and regular-plus-pendant graphs (SO scales with degree magnitude, so high-degree-spread and dense-regular families are where naive bounds crack); also products of small graphs pushed to hundreds of vertices.

**Checker (exact).** Recompute SO and variants with interval arithmetic on every radical; recompute Sombor spectral radius/energy at high precision and certify the sign of any claimed strict gap.

**Verification discipline.** Generator is not verifier: second independent implementation of each index and of the SO-matrix eigenvalues. No fabricated citations: name each bound's paper or mark "could not verify." Report candidates generated / broken / survived, graph6 witnesses, exact margins.
