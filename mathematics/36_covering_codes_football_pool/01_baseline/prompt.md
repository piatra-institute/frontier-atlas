# PROMPT FOR CLOSING A SPECIFIC OPEN COVERING NUMBER \(K_q(n,R)\)

## Covering codes and the football-pool problem: the minimum size of a covering code

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 36 of 50  
**Area:** designs & codes  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

\(K_q(n,R)\) is the minimum number of codewords in a \(q\)-ary code of length \(n\) whose Hamming balls of radius \(R\) cover the whole space. The ternary radius-one case is the classical **football-pool problem** (predict \(n\) match outcomes from \(\{1,\mathrm{X},2\}\), guarantee at most one wrong), and several small instances - notably \(K_3(6,1)\) - have exact values that have resisted determination for decades, with a stubborn gap between the smallest known covering and the best lower bound.

Every open \((q,n,R)\) is a finite, machine-checkable optimisation: an upper bound is a covering code verified by exact ball enumeration, and a lower bound becomes a proof only via an exact combinatorial/LP argument. This is the certified-search regime of the program, adjacent to optimal codes (35) and Hadamard matrices (02). The resolution standard in section 2 - determining a specific open \(K_q(n,R)\) exactly - is the goal; a one-sided improvement is a genuine partial result, never reported as the exact value.

## 1. Exact problem statement

Fix an alphabet \(\mathbb{Z}_q\) and the Hamming metric on \(\mathbb{Z}_q^n\).

For \(x\in\mathbb{Z}_q^n\), the ball \(B_R(x)=\{y:d_H(x,y)\le R\}\) has size
\[
|B_R(x)|=\sum_{i=0}^{R}\binom{n}{i}(q-1)^i .
\]

A code \(C\subseteq\mathbb{Z}_q^n\) has **covering radius** \(\le R\) iff \(\bigcup_{c\in C}B_R(c)=\mathbb{Z}_q^n\); that is, every word is within distance \(R\) of some codeword. Define
\[
K_q(n,R)=\min\{\,|C|:\ C\subseteq\mathbb{Z}_q^n,\ \textstyle\bigcup_{c\in C}B_R(c)=\mathbb{Z}_q^n\,\}.
\]

The **sphere-covering bound** gives the immediate lower estimate
\[
K_q(n,R)\ \ge\ \left\lceil \frac{q^n}{\sum_{i=0}^R\binom{n}{i}(q-1)^i} \right\rceil,
\]
which for \(q=3,R=1\) reads \(K_3(n,1)\ge\lceil 3^n/(1+2n)\rceil\) and is exact only at the perfect lengths \(n=(3^m-1)/2\).

Codes need not be linear; linear covering codes and coset-leader arguments are used as construction tools, not as a restriction.

**Excess and density (the lower-bound handles).** For a code \(C\) of covering radius \(\le R\), the total ball volume overshoots the space by the **excess**
\[
E(C)=\sum_{c\in C}|B_R(c)|-q^n\ \ge\ 0,
\]
and refined counting of how excess concentrates on words covered multiple times (van Wee-type arguments) yields lower bounds strictly above the sphere-covering estimate. The **covering density** \(\mu=|C|\cdot|B_R|/q^n\ge 1\) measures efficiency; the football-pool difficulty is that near-optimal ternary radius-one coverings sit only slightly above \(\mu=1\), so both directions require exact, not asymptotic, arguments.

**Amalgamation and direct sums.** Coverings of \((q,n_1,R_1)\) and \((q,n_2,R_2)\) combine to cover \((q,n_1+n_2,R_1+R_2)\); such product and amalgamated-direct-sum constructions supply many upper-bound records and are used freely, provided the resulting covering is re-verified exactly.

**The football-pool problem** is the case \(q=3,\ R=1\): \(K_3(n,1)\). Perfect ternary codes give exact values at \(n=(3^m-1)/2\) (\(n=1,4,13,\dots\)); off these lengths the exact values are hard, and \(K_3(6,1)\) is the classic stubborn instance.

**The open question, made specific.** Fix one currently open \((q,n,R)\) and determine \(K_q(n,R)\) exactly.

A concrete flagship, to be **re-verified** at session start: \(K_3(6,1)\), for which the best known covering has size \(73\) (Wille, 1987) and the best published lower bound is \(65\) (both values **verify**). The chosen instance and its current bracket must be quoted from a live covering-code table, not from this prompt.

## 2. Resolution standard

A **complete resolution** for a chosen open \((q,n,R)\) is a matched pair.

- **Upper side.** An explicit code \(C\) with \(|C|=M\) and a proof, by exhaustive enumeration of all \(q^n\) words, that each lies in some \(B_R(c)\) - i.e. a certified covering of size \(M\).

- **Lower side.** A proof that \(K_q(n,R)\ge M\), given as an **exact** argument: an exact-rational LP dual over the covering polytope, an excess / van Wee-type counting inequality carried out in exact integer arithmetic, or a DRAT-backed SAT `UNSAT` for "does a covering of size \(M{-}1\) exist?" over a fully symmetry-reduced model.

Together these give \(K_q(n,R)=M\).

**Named certified forms accepted.**

- Exhaustive / ILP search for the optimum with an exact optimality certificate.

- Exact-rational LP lower bounds with directed rounding (dual feasibility checked in exact arithmetic).

- DRAT/LRAT proofs for SAT-encoded nonexistence of a smaller covering.

**Not accepted as resolution.**

- A smaller covering code (better upper bound) reported as the exact value.

- A covering claim verified only on a sample of words rather than all \(q^n\).

- A floating-point LP lower bound with no exact rational dual.

- A lower bound that assumes linearity or a prescribed symmetry, reported as the unrestricted \(K_q(n,R)\).

- Heuristic search output ("best found = \(M\)") presented as optimality without a completeness certificate.

## 3. Graded partial-result targets

- **P1 - Reproduce the frontier upper bound.** Regenerate a best-known covering code for the target instance (e.g. a size-73 covering for \(K_3(6,1)\)) and verify the covering by exact enumeration of all \(q^n\) words. *Certificate:* code file + exhaustive-ball checker output.

- **P2 - Reproduce the frontier lower bound.** Reproduce the best published lower bound for the target via an exact LP or excess-counting argument recomputed in exact arithmetic. *Certificate:* the inequality chain / LP dual + independent recomputation.

- **P3 - Exact LP lower-bound engine.** Build the covering LP (or its excess / van Wee refinement) in exact rational arithmetic and reproduce published lower bounds across a range of \((q,n,R)\). *Certificate:* dual vectors + exact verifier.

- **P4 - Upper-bound improvement.** Find a smaller covering for a specific open instance via metaheuristic search (tabu / simulated annealing), followed by exact verification. *Certificate:* the smaller code + exhaustive-ball check + search provenance.

- **P5 - Lower-bound improvement.** Raise the lower bound for a specific open instance via a stronger exact combinatorial / LP argument or a DRAT-backed small-case `UNSAT`. *Certificate:* exact argument or proof trace + independent check.

- **P6 - Close an instance (windfall).** Determine \(K_q(n,R)\) exactly for a genuinely open instance - upper and lower certified and equal.

## 4. Known results and prior art

- **Kamps & van Lint (1967)** formalised the football-pool problem and early \(K_3(n,1)\) bounds; the problem traces to European football betting pools of the 1960s.

- Perfect ternary Hamming codes give \(K_3(n,1)\) exactly at \(n=(3^m-1)/2\) (e.g. \(K_3(4,1)=9\), \(K_3(13,1)=3^{10}\)).

- **Wille (1987)** found a covering of size \(73\) for \(n=6\) (\(K_3(6,1)\le 73\)); later metaheuristic work (simulated annealing, tabu search) reproduced or approached this. The best published lower bound for \(K_3(6,1)\) is \(65\) (**verify** both endpoints and any recent movement).

- **van Wee (1988)** gave improved sphere-covering (excess) lower bounds; **Habsieger**, **Blass–Litsyn**, and others sharpened combinatorial lower bounds.

- **Östergård** and collaborators (**Hämäläinen, Honkala, Kaikkonen, Litsyn**) produced many covering-code records via computer search; **Linderoth, Margot, Thain** improved football-pool bounds via ILP / parallel branch-and-bound.

- **Cohen, Honkala, Litsyn, Lobstein**, *Covering Codes* (North-Holland, 1997) is the standard monograph. **Kéri's** online tables of \(K_q(n,R)\) are the living reference for current bounds.

- Known exact ternary radius-one values run out early: \(K_3(n,1)\) is settled for small \(n\) and at the perfect lengths, but \(K_3(6,1)\) and several nearby instances remain open, which is why the football-pool problem is quoted as a benchmark for exact combinatorial optimisation (**verify** the exact list of settled vs. open small \(n\)).

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Covering-code records move; confirm the current best upper and lower bounds for the chosen \((q,n,R)\) from Kéri's tables (or the current successor) and record the exact bracket with an access date. Do not trust the \(65\le K_3(6,1)\le 73\) bracket above without checking.

## 5. Attack plan

`[search]` - small coverings first for the upper side, exact combinatorics for the lower side.

- **Upper side (construction).** Metaheuristics (simulated annealing, tabu search, large-neighbourhood local search) to find small coverings, then **exact verification**: enumerate all \(q^n\) words and confirm each is covered. Exploit linear/coset structure and prescribed automorphism groups (`GAP`, `SageMath`) to compress the search and the certificate.

- **Lower side (exact bounds).** Formulate the covering LP (minimise \(\mathbf 1^\top z\) subject to the ball-incidence covering constraints) and solve its dual in exact rational arithmetic (`QSopt_ex`, exact `SoPlex`); strengthen with van Wee / excess counting done in exact integers.

- **Small-case exactness.** For narrow ranges, encode "covering of size \(M{-}1\) exists?" as SAT and require **DRAT** for `UNSAT`; or solve the set-cover ILP (`Gurobi`/`SCIP`) with symmetry breaking for exploration and re-certify optimality exactly (exact LP dual at the root, or exhaustive / SAT completeness).

- **Group-invariant search.** Restrict to codes invariant under a chosen group (e.g. cyclic or affine actions on \(\mathbb{Z}_q^n\)) to shrink both the construction search and the covering certificate; report any such restriction explicitly, since it can only prove upper bounds, never a lower bound on the unrestricted \(K_q(n,R)\).

- **One-workstation scope.** Verifying a covering of \(3^6=729\) words is instant; \(q^n\) up to a few million is feasible. Metaheuristic upper-bound search is cheap. Exact LP lower bounds are feasible for modest \(n\); exact ILP optimality for the full football-pool instance is hard and may only yield certified bounds, not the exact optimum - report honestly.

- **Warm starts.** Seed the metaheuristics from known record coverings and from product / amalgamated-direct-sum constructions of smaller solved instances, so search effort concentrates on improving rather than rediscovering the frontier.

- **Failure modes.**

  - Verifying a covering on a sample instead of all \(q^n\) words.

  - A floating LP dual that turns out infeasible in exact arithmetic.

  - Symmetry-breaking that accidentally excludes optimal codes.

  - A metaheuristic "best found" mistaken for a proven optimum.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every covering is verified by exhaustive exact enumeration of all \(q^n\) words; every lower bound rests on an exact rational LP dual, an exact counting inequality, or a DRAT-backed `UNSAT`. Floating point and metaheuristics are exploratory only.

2. **Independent verification.** A standalone ball-covering checker (written separately from the search) re-verifies every code; a separate exact-arithmetic routine recomputes every LP dual; a DRAT checker validates SAT `UNSAT`.

3. **Reproducibility.** All codes, dual vectors, LP/ILP models, solver versions, seeds, and metaheuristic parameters recorded; SHA-256 manifest over every artifact; the chosen \((q,n,R)\) and its bracket quoted from a live table with an access date.

4. **Preservation.** Search and bound source is part of the record (the Hadamard-668 lost-source lesson); a `NEXT_STEPS.md` records the instance attacked and the remaining gap when pausing.

5. **Honest reporting.** The report states up front whether a full determination (upper and lower certified and equal) was achieved. A better covering or a better lower bound alone is labelled a one-sided improvement and never represented as the exact \(K_q(n,R)\).
