# Batch sweep: refute Laplacian and signless-Laplacian eigenvalue bounds

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit graph violating a stated (signless-)Laplacian spectral bound, or hardened survivors. Refutation is the clean win.

**Family + panel.** Connected graphs; Laplacian spectrum μ1≥…≥μn=0, signless-Laplacian spectrum, algebraic connectivity μ_{n−1}, Laplacian energy Σ|μi−2m/n|, Laplacian-spread, and partial sums S_k=Σ_{i≤k}μi.

**Enumerate.** nauty `geng`, connected graphs to n=9 (A001349: 1,1,2,6,21,112,853,11117,261080), n=10 if time.

**Conjecture generation.** Anchor on named open/known statements: Brouwer's conjecture S_k ≤ m + C(k+1,2) (Brouwer-Haemers, "Spectra of Graphs" 2012; verified small, open in general — stress it on under-tested families); the Grone-Merris-Bai statement (a theorem — use as validation baseline); and the signless-Laplacian conjecture list of Cvetkovic-Rowlinson-Simic (several later refuted). Auto-fit algebraic-connectivity and Laplacian-energy bounds on n≤7.

**Adversarial families.** Split graphs, threshold graphs, complete-split, kneser, hypercubes, trees of high/low diameter, and joins G∨H (Laplacian spectra of joins are explicit, giving exact large-n Brouwer test points); random regular graphs.

**Checker (exact).** Recompute the Laplacian/signless-Laplacian spectrum to high precision and certify strict margins via exact charpoly root isolation; verify each partial-sum inequality with certified bounds, not floats. Emit violators in graph6.

**Verification discipline.** Generator is not verifier: two spectrum computations (dense eigensolver vs exact charpoly) must agree; audit Σμi=2m and μn=0. Distinguish testing a theorem (Grone-Merris-Bai, as a self-check) from testing an open conjecture (Brouwer). Cite each statement or mark "could not verify." Report candidates generated / broken / survived, graph6 witnesses.
