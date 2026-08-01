# Batch sweep: refute adjacency-spectrum inequalities

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit graph violating a stated adjacency-eigenvalue bound, or hardened survivors. Refutation is the clean win.

**Family + panel.** Connected graphs; adjacency spectrum λ1≥…≥λn and derived invariants: spectral radius λ1, second eigenvalue λ2, spread λ1−λn, spectral gap λ1−λ2, nullity (multiplicity of 0), number of distinct eigenvalues, and their relations to n, m, Δ, ω, χ, α, girth.

**Enumerate.** nauty `geng`, connected graphs to n=9 (A001349: 1,1,2,6,21,112,853,11117,261080), n=10 if time. Add regular graphs and strongly regular parameter sets as a stress class.

**Conjecture generation.** Harvest from Aouchiche-Hansen "A survey of automated conjectures in spectral graph theory" (Linear Algebra Appl. 432, 2010), which lists many AutoGraphiX spectral conjectures, several later refuted; plus Nikiforov-style spectral-extremal bounds and spectral-radius-vs-chromatic conjectures. Auto-fit λ1-vs-invariant and spread-vs-(n,m) bounds on n≤7.

**Adversarial families.** Turan graphs, complete bipartite, kneser and Johnson graphs, cocktail-party graphs, friendship graphs, random regular graphs, and Cartesian/tensor products (spectra compose, so products give exact large-n test points that cheaply break spread and gap bounds).

**Checker (exact).** Recompute eigenvalues to high precision AND, where a claim is strict, certify the sign of the margin with interval arithmetic or an exact characteristic-polynomial computation (integer coefficients); never decide a strict inequality on raw float. Emit violators in graph6.

**Verification discipline.** Generator is not verifier: compute the spectrum two ways (dense eigensolver vs exact charpoly root isolation) and require agreement; check Σλi=0 and Σλi^2=2m as internal audits. Cite each tested bound or mark "could not verify." Report candidates generated / broken / survived, graph6 witnesses.
