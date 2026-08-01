# Batch sweep: refute chromatic-number inequalities

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit graph violating a stated chromatic bound, or hardened survivors. Refutation is the clean win.

**Family + panel.** Connected graphs; χ (chromatic number), ω (clique number), Δ (max degree), fractional χ_f, and derived quantities. Anchor conjectures: Reed's conjecture χ ≤ ⌈(Δ+1+ω)/2⌉ (Reed, J. Graph Theory 27, 1998; verified for small n, open in general) and the Borodin-Kostochka conjecture (if Δ≥9 and χ≥Δ then ω≥Δ; open).

**Enumerate.** nauty `geng`, connected graphs to n=9 (A001349: 1,1,2,6,21,112,853,11117,261080). Reed and Borodin-Kostochka are proven for all small n, so treat small enumeration as a self-consistency check and put the real search into structured families at larger n.

**Conjecture generation.** Test the named conjectures plus auto-fit χ-vs-(Δ,ω,χ_f) bounds. Include fractional and circular-chromatic relaxations where integer versions are safe.

**Adversarial families.** Kneser and Schrijver graphs (χ far above ω), Mycielskians (triangle-free, χ→∞), shift/Cayley graphs, line graphs of high-Δ graphs, random Δ-regular graphs, and Δ=9…14 constructions targeting Borodin-Kostochka; complements of sparse graphs.

**Checker (exact).** Compute χ exactly by SAT/ILP with a proof of both a valid k-colouring and non-(k−1)-colourability (UNSAT certificate); compute ω exactly by max-clique. Never trust a heuristic colouring. Emit violators in graph6 with the certificate.

**Verification discipline.** Generator is not verifier: recompute χ with a second exact solver and independently verify the colouring is proper and the lower bound holds. Cite each conjecture's source or mark "could not verify." Report candidates generated / broken / survived, graph6 witnesses.
