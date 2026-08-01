# Batch sweep: refute poset and lattice inequalities

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit poset/lattice violating a stated inequality, or hardened survivors. Refutation is the clean win.

**Family + panel.** Finite posets and lattices; invariants: number of linear extensions e(P), the balance constant δ(P)=max over incomparable pairs of the fraction of extensions with x<y, order dimension, height, width, Mobius function values, and the order polynomial. Anchor: the 1/3-2/3 conjecture (every finite non-total poset has an incomparable pair balanced within [1/3,2/3]; Kislitsyn 1968, open, best known constant below 1/3).

**Enumerate.** All unlabeled posets to n=8 (count-check A000112: 1,1,2,5,16,63,318,2045,16999 for n=0..8) and all lattices to n=9 (A006966: 1,1,1,1,2,5,15,53,222,1078). Compute e(P) exactly by counting linear extensions.

**Conjecture generation.** Test the 1/3-2/3 balance constant on every poset; auto-fit inequalities among (linear extensions, dimension, height, width, antichain counts) and log-concavity/unimodality claims for the order polynomial and Whitney numbers. Flag any lattice violating a proposed correlation or log-concavity bound.

**Adversarial families.** Posets minimizing the balance constant (the known near-1/3 posets, small "N" and fence posets), Boolean lattices, partition lattices, divisor lattices, and random bipartite-height-2 posets (extremal for many linear-extension bounds).

**Checker (exact).** Count linear extensions exactly (dynamic programming over down-sets); compute the balance constant exactly as rationals; verify lattice axioms (unique meets/joins). Emit violators as cover relations.

**Verification discipline.** Generator is not verifier: recompute e(P) with a second method (topological-sort DP vs recursion) and confirm rationals exactly; re-check isomorphism in a second canonicalizer. Cite each inequality, noting 1/3-2/3 remains open. Report candidates generated / broken / survived, with poset witnesses.
