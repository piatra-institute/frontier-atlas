# Batch sweep: resolve small combinatorial-design existence "?" cells

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit design settling an open small-parameter existence cell, or a certified nonexistence by exhaustive small search. Both are clean, exactly-checkable witnesses.

**Family + panel.** Combinatorial designs: t-designs t-(v,k,λ), resolvable and super-simple designs, balanced incomplete block designs, group-divisible designs, and difference families. The target quantity is existence (yes with a construction, or no with an exhaustive/parity obstruction).

**Enumerate / source.** The Handbook of Combinatorial Designs, 2nd ed. (Colbourn-Dinitz, 2007) existence tables, which mark small admissible parameter sets as unknown ("?"); and the La Jolla Covering Repository (Gordon) for covering-design records. Pick admissible parameters (passing the divisibility/Fisher necessary conditions) that are still open at small v.

**Conjecture generation.** For each open cell, attempt construction by prescribing a small automorphism group (Kramer-Mesner: reduce to a 0/1 system over group orbits, solve by SAT/ILP), and by direct difference-family search over small groups. Where construction fails, attempt exhaustive nonexistence for tiny v.

**Adversarial / structured search.** Cyclic and 1-rotational constructions, prescribed automorphisms (Z_v, dihedral, Frobenius), starter-adder methods, and resolvability via parallel classes — the standard routes that realize sporadic small designs.

**Checker (exact).** Verify a constructed design combinatorially: every t-subset lies in exactly λ blocks (exhaustive count), block sizes correct, resolvability partitions verified. A nonexistence claim must come with an exhaustive-search or exact-obstruction certificate, not a heuristic.

**Verification discipline.** Generator is not verifier: re-verify the t-subset coverage with a second independent counter; confirm the parameter set was genuinely open by citing the Handbook cell (edition, page) or mark "could not verify." Report the denominator: cells attempted / constructed / proven-nonexistent / left open, with explicit block lists.
