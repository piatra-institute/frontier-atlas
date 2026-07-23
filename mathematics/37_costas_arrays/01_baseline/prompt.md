# PROMPT FOR SETTLING COSTAS-ARRAY EXISTENCE AT THE SMALLEST OPEN ORDER

## Costas arrays: a permutation with all pairwise displacement vectors distinct

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 37 of 50  
**Area:** designs & codes  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A Costas array of order \(n\) is an \(n\times n\) permutation matrix whose \(\binom{n}{2}\) displacement vectors between distinct pairs of ones are all different - a discrete object with an exact, instantly checkable defining condition and immediate use in sonar, radar, and optical-channel design.

Existence is settled for many orders by the Welch and Lempel–Golomb algebraic constructions, and complete enumeration counts are known through roughly \(n=29\); yet for the smallest orders lacking any known array - historically \(32\) and \(33\) - existence has been open since the 1980s. This is a clean finite decision problem with machine-checkable ground truth: exactly the exhaustive-search and construction regime this program targets. The resolution standard in section 2 - settling existence at the smallest open order, by an explicit array or a complete exhaustive nonexistence proof - is the goal; an incomplete search or a construction at a non-minimal order is a partial result, never represented as settling the open case.

## 1. Exact problem statement

Identify a permutation \(f:\{1,\dots,n\}\to\{1,\dots,n\}\) with the array whose ones sit at positions \((i,f(i))\).

The array is a **Costas array** iff all displacement vectors between pairs of ones are distinct; equivalently, the **distinct-differences** (Costas) condition holds:
\[
\forall\,k\in\{1,\dots,n-1\},\ \ \forall\,i\neq i'\in\{1,\dots,n-k\}:\quad f(i+k)-f(i)\ \neq\ f(i'+k)-f(i').
\]

That is, within each fixed row-shift \(k\), the differences \(f(i+k)-f(i)\) are pairwise distinct. Equivalently, the multiset of displacement vectors
\[
\bigl\{(j-i,\,f(j)-f(i)):i<j\bigr\}
\]
has no repeated element.

**Symmetry.** The dihedral group of order 8 (rotations and reflections of the square) acts on Costas arrays; existence and enumeration are studied up to this action, and counts are usually reported both as raw totals and up to symmetry. Any nonexistence search must state the symmetry reduction it uses.

**Constructive landscape (existence handles).** The two families that give most known arrays are:

- **Welch \(W_1(p,g)\):** for a prime \(p\) and primitive root \(g\) modulo \(p\), the array \(f(i)=g^{i}\bmod p\) on \(\{1,\dots,p-1\}\) is Costas of order \(p-1\); variants \(W_2,W_3\) remove one or two fixed points.

- **Lempel–Golomb \(G_2(q,\alpha,\beta)\):** over \(\mathbb{F}_q\) with primitive elements, the condition \(\alpha^{i}+\beta^{f(i)}=1\) defines a Costas array of order \(q-2\); associated constructions give orders \(q-1\).

Arrays not arising from these ("sporadic" or "emergent" arrays) are found only by search and are exactly what an exhaustive enumeration at a new order would newly certify or exclude.

**The open question, made specific.** Determine whether a Costas array of the smallest open order exists - historically \(n=32\) (and then \(n=33\)); **re-verify the current smallest open order** at session start.

- Existence is known for all \(n\le 31\) via the algebraic constructions.

- Complete enumeration counts are known through \(n\approx 29\).

- \(n=32\) and \(n=33\) are the smallest orders with no known array (**verify** current status, since sporadic constructions occasionally close such gaps).

## 2. Resolution standard

A **complete resolution** at a chosen order \(n\) is one of:

- **(A) Existence.** An explicit permutation \(f\) of order \(n\) together with an independent checker verifying, in exact integer arithmetic, that the distinct-differences condition holds for every shift \(k\). This settles existence affirmatively.

- **(B) Nonexistence.** A proof that no Costas array of order \(n\) exists, by a complete exhaustive backtracking (or SAT) search carrying a machine-checkable completeness certificate: an accounting that every branch of the symmetry-reduced search tree was closed, or a DRAT/LRAT proof of `UNSAT` for a faithful encoding.

The headline target is the **smallest** open order; settling a larger order does not settle the open case.

**Named certified forms accepted.**

- Exhaustive backtracking with an explicit, replayable search-tree accounting and a stated symmetry reduction.

- SAT encodings whose `UNSAT` carries DRAT/LRAT.

- Exact integer arithmetic for every displacement-distinctness check.

- Verified algebraic constructions (Welch, Lempel–Golomb) for the existence direction, with the group-theoretic parameters recorded.

**Not accepted as resolution.**

- An incomplete or timed-out search reporting "no array found."

- A "near-Costas" permutation with one or more repeated displacement vectors.

- A construction at a non-minimal order presented as resolving the smallest open case.

- A distinctness check performed only in floating point or only for some shifts.

- A nonexistence claim restricted to arrays with a prescribed symmetry, represented as full nonexistence.

## 3. Graded partial-result targets

- **P1 - Reproduce enumeration counts.** Exhaustively enumerate Costas arrays for \(n\) up to a checkpoint (e.g. \(n\le 20\)) and match published raw and up-to-symmetry counts. *Certificate:* per-order counts + a replay under an independently implemented symmetry reduction.

- **P2 - Verified constructions.** Implement the Welch and Lempel–Golomb constructions, generate arrays for a range of orders including near the open frontier (e.g. \(n=31\)), and verify the Costas property exactly. *Certificate:* generated arrays + exact checker + recorded construction parameters (primitive roots, field, exponents).

- **P3 - Extend the enumeration frontier.** Complete an exhaustive count one order beyond the current published frontier, with a completeness certificate. *Certificate:* count + search-tree accounting + independent replay.

- **P4 - Structural restriction at the open order.** For the smallest open \(n\), rule out Costas arrays within prescribed structural families (e.g. those with a nontrivial dihedral / Golomb symmetry, or a fixed partial pattern) by exhaustive / SAT search. *Certificate:* per-family completeness certificate or DRAT `UNSAT`.

- **P5 - Settle existence (windfall or heroic).** Either exhibit an array at the smallest open order (immediate resolution) or complete the full exhaustive nonexistence with a global completeness certificate. Report honestly that full exhaustion at \(n=32\) is estimated at tens of thousands of core-years and is beyond a single workstation; the likely deliverable is P1–P4 plus a certified partial nonexistence.

## 4. Known results and prior art

- **Costas (c. 1965)** introduced the arrays for sonar frequency-hopping; **Gilbert (1965)** studied the combinatorics.

- The **Welch construction** (via primitive roots mod \(p\)) yields Costas arrays of order \(p-1\); the **Lempel–Golomb constructions** (over \(\mathbb{F}_q\)) yield orders \(q-2\) and \(q-1\). See **Golomb & Taylor (1984)** for the survey of constructions and symmetries.

- Exhaustive enumeration: complete counts are established for all orders up to \(n=29\), with \(n=27,28,29\) completed by **Drakakis, Rickard, Beard, Caballero, Iorio, O'Brien, Gow** and collaborators (c. 2008–2011); **verify** the exact frontier and per-order counts.

- The smallest orders with **no known** Costas array have been \(n=32\) and \(n=33\) since the 1980s; existence there is open (**verify** current status - occasional sporadic constructions have historically closed such gaps at other orders).

- Structural and symmetry results (e.g. constraints on Costas arrays with a given symmetry) appear in **Jedwab–Wodlinger** and the "Open problems in Costas arrays" surveys (**Drakakis** and collaborators, c. 2011; **verify**). Beard maintains databases of known arrays.

- It is a long-standing open question whether Costas arrays exist for all orders \(n\); the density of known arrays thins as \(n\) grows, and no construction is known that covers every order, which is what makes the smallest missing orders sharp test cases.

- Enumeration counts have no known closed form and are believed to decay super-exponentially relative to \(n!\); the search cost at each new order roughly reflects this, so the frontier advances one order at a time.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Confirm the current smallest open order (still \(32\), then \(33\), unless a construction has closed it), the enumeration frontier, and the published per-order counts before committing search effort. Record the exact status with an access date.

## 5. Attack plan

`[search]` - enumeration and construction, both terminating in exact certificates.

- **Exhaustive backtracking.** Custom C++ placing ones column by column, maintaining the set of used displacement vectors with bitsets for \(O(1)\) conflict checks, pruning on the first repeated vector. Symmetry-break with the dihedral group (canonical corner / first-column ordering). This reaches \(n\approx 29\text{–}30\) on one workstation; verify against published counts before trusting it at the frontier.

- **SAT encoding.** Booleans \(x_{i,j}\) for the permutation matrix, with at-most/at-least-one row and column constraints and all-different clauses over displacement vectors; require **DRAT/LRAT** for any `UNSAT`. Solvers: `kissat`, `CaDiCaL`, `CryptoMiniSat`. Useful for structural restrictions and for cross-checking small exhaustive results.

- **Constructions.** `GAP`/`SageMath` for primitive roots and field arithmetic to instantiate Welch and Lempel–Golomb arrays exactly, with the parameters recorded so a third party can regenerate them; verify each with the exact checker.

- **Exact verification core.** A standalone checker takes a permutation and confirms the distinct-differences condition over all shifts in exact integer arithmetic; every artifact passes through it.

- **Difference-triangle representation.** Represent each candidate by its difference triangle (row \(k\) holds \(f(i+k)-f(i)\)); a Costas array is exactly one whose every row has distinct entries, which makes both the incremental pruning and the final certificate a simple per-row distinctness check.

- **One-workstation scope.** P1–P4 are feasible. Full exhaustion at \(n=32\) is not (estimated tens of thousands of core-years); the realistic target is verified constructions, extended enumeration by at most one order, and certified structural nonexistence at the open order.

- **Cross-checking.** Every backtracking count is validated against the published enumeration for small \(n\) before the code is trusted near the frontier; any SAT `UNSAT` for a structural family is cross-checked against a direct backtracking count over the same family.

- **Failure modes.**

  - Off-by-one in Welch / Lempel exponent indexing producing false "constructions."

  - Symmetry-reduction bugs that double-count or miss arrays.

  - An incomplete or timed-out search reported as nonexistence.

  - Floating point creeping into the distinctness check.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every Costas check is exact integer arithmetic; every nonexistence carries a completeness certificate (search-tree accounting or DRAT/LRAT). Heuristic or timed-out searches are never certification.

2. **Independent verification.** A standalone checker (separate from the search) re-verifies every array; a DRAT checker validates every SAT `UNSAT`; enumeration counts are replayed under an independently implemented symmetry reduction and cross-checked against published values.

3. **Reproducibility.** All arrays, construction parameters, encodings, solver versions, seeds, and symmetry conventions recorded; SHA-256 manifest over every artifact; the smallest open order and its status quoted from the current literature with an access date.

4. **Preservation.** Enumeration and construction source is part of the record (the Hadamard-668 lost-source lesson); a `NEXT_STEPS.md` records the frontier order and the exact search-tree checkpoint reached when pausing.

5. **Honest reporting.** The report states up front whether existence at the smallest open order was settled. An extended enumeration, a construction at another order, or a symmetry-restricted nonexistence is labelled as such and never represented as settling the open case.
