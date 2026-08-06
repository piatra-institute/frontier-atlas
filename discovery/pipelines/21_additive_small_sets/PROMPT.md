# Batch sweep: refute additive-combinatorics small-set conjectures

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit small set (or finite abelian group element) witnessing that a claimed additive bound is beatable, or hardened survivors. Refutation is the clean win.

**Family + panel.** Finite integer sets A ⊂ [0,N] and subsets of finite abelian groups; quantities: |A+A|, |A−A| and the sum-vs-difference balance (MSTD: |A+A|>|A−A|), Sidon/B_h property (all h-fold sums distinct), sum-free density, the Davenport constant D(G) (longest zero-sum-free sequence +1), and the doubling constant |A+A|/|A|.

**Enumerate.** Exhaustive small sets: all A ⊆ {0,…,N} up to translation/reflection for N≤ ~24 (prune by symmetry); all subsets/sequences over small abelian groups Z_n and Z_a×Z_b. Sanity-check: the smallest MSTD set is {0,2,3,4,7,11,12,14} (verify by direct computation before any sweep).

**Conjecture generation.** Anchor on real open questions: the exact Davenport constant of higher-rank groups (open for rank ≥ 4; Gao-Geroldinger survey 2006), extremal MSTD density (Martin-O'Bryant 2007; Hegarty), and maximal Sidon-set sizes in intervals/groups. Auto-fit conjectural bounds (e.g. min |A+A|/|A| at fixed structure) on small cases, then push.

**Adversarial families.** Arithmetic progressions and generalized APs, Sidon-set-based constructions, symmetric vs skewed sets (for MSTD), B_h greedy sets, and structured group sequences (long runs of a single generator) for Davenport.

**Checker (exact).** Compute A+A, A−A, and all h-fold sums exactly as integer/group sets; verify zero-sum-free sequences by exhaustive subset-sum. A refutation is a concrete set beating a stated bound, re-verified. Emit the explicit set.

**Verification discipline.** Generator is not verifier: recompute every sumset and the Davenport witness with a second routine; confirm the {0,2,3,4,7,11,12,14} baseline. Cite each bound's source or mark "could not verify." Report candidates generated / broken / survived, with explicit sets.

**Scope limit (added 2026-08-06).** Do not spend this pipeline on the sum-vs-difference *exponent* question, i.e. how large `log(|A+A|/|A|) / log(|A-A|/|A|)` can be. It is settled: Lin-Li, arXiv:2607.27199, 29 Jul 2026, prove the supremum is 2 by an explicit family whose smallest record-beating member has about `10^143` elements. Eight agent systems, AlphaEvolve included, plateaued at 1.079-1.145 by enumerating exactly the way this pipeline does. See `../../../FRONTIER_LOG.md`. The targets that remain genuinely small-set are minimal and extremal-density MSTD sets, Sidon/B_h sizes, and Davenport constants; keep the sweep on those.
