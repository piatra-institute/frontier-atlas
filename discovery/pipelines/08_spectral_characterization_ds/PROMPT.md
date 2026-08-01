# Batch sweep: cospectral mates and determined-by-spectrum witnesses

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** explicit small cospectral non-isomorphic pairs (witnesses that a graph is NOT determined by its spectrum) under a matrix where none is catalogued, or a certified determined-by-spectrum verdict for a small graph. Both are clean, checkable objects.

**Family + panel.** Connected graphs; spectra under four matrices: adjacency A, Laplacian L, signless-Laplacian Q, and distance D. For each matrix, the question is whether a graph is uniquely determined by that spectrum (DS) or has a cospectral mate.

**Enumerate.** nauty `geng`, connected graphs to n=9 (A001349: 1,1,2,6,21,112,853,11117,261080). Sanity-check the fraction of adjacency-cospectral graphs against the Haemers-Spence tabulation (fraction non-DS by n; van Dam-Haemers, Linear Algebra Appl. 373, 2003, and Discrete Math. 309, 2009).

**Conjecture generation.** The open backdrop is the van Dam-Haemers conjecture that almost all graphs are DS. Target under-catalogued cells: Q-spectra and D-spectra cospectral mates are far less tabulated than A/L. Generate candidate mates by Godsil-McKay switching and by hashing every graph's spectrum (rounded via exact charpoly) into buckets; any bucket with two non-isomorphic graphs sharing an exact spectrum is a witness.

**Adversarial families.** Trees (many are non-DS for A), Godsil-McKay switching sets, regular graphs and SRG parameter twins, and product families.

**Checker (exact).** Match spectra by exact integer characteristic polynomials (not floats); confirm non-isomorphism with nauty canonical form. A pair passes only if charpolys are identical and canonical labels differ.

**Verification discipline.** Generator is not verifier: recompute charpolys with a second exact routine and re-run the isomorphism test in a second library. Cite the Haemers-Spence counts or mark "could not verify." Report the denominator: graphs bucketed / mate-pairs found / DS-verdicts, with graph6 pairs.
