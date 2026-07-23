# PROMPT FOR SETTLING A SPECIFIC OPEN STEINER SYSTEM OR \(t\)-DESIGN

## Existence of a small combinatorial design whose existence is open

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 39 of 50  
**Area:** designs & codes  
**Modes:** `[search]` `[enum]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A Steiner system \(S(t,k,v)\) places blocks (\(k\)-subsets) on a \(v\)-point set so that every \(t\)-subset lies in exactly one block; more generally a \(t\)-\((v,k,\lambda)\) design asks for every \(t\)-subset in exactly \(\lambda\) blocks. Keevash (2014) and Glock–Kühn–Lo–Osthus proved existence for all sufficiently large \(v\) meeting the divisibility conditions, but this leaves many specific small parameter sets genuinely undecided.

Each open case is a finite, exactly-checkable target: existence is witnessed by an explicit block set (every \(t\)-subset covered exactly \(\lambda\) times, checkable in exact arithmetic), and nonexistence by an exhaustive isomorph-free search with a completeness certificate. This is the `[search]`+`[enum]` regime of the program, adjacent to projective planes (04) and MOLS (34). The resolution standard in section 2 - settling a specific open design by construction or certified nonexistence - is the goal; a prescribed-symmetry-only result or an incomplete search is a partial result, never reported as the full settlement.

## 1. Exact problem statement

Let \(V\) be a \(v\)-set.

A \(t\)-\((v,k,\lambda)\) **design** is a collection \(\mathcal B\) of \(k\)-subsets (**blocks**) of \(V\) such that every \(t\)-subset of \(V\) lies in exactly \(\lambda\) blocks. A **Steiner system** \(S(t,k,v)\) is the case \(\lambda=1\).

Counting incidences gives the **divisibility (necessary) conditions**: for every \(0\le i\le t\),
\[
\binom{k-i}{\,t-i\,}\ \Big|\ \lambda\binom{v-i}{\,t-i\,},
\]
and the block count is
\[
b=\lambda\binom{v}{t}\Big/\binom{k}{t}.
\]

Parameters satisfying these are **admissible**; admissibility is necessary, not sufficient.

*Worked instance.* For \(S(2,6,v)\) (\(t=2,k=6,\lambda=1\)) the two conditions read \(5\mid v-1\) and \(30\mid v(v-1)\), i.e. \(v\equiv1\) or \(6\pmod{15}\); the block count is \(b=v(v-1)/30\) and the replication number is \(r=(v-1)/5\). The value \(v=51\) satisfies both (\(r=10\), \(b=85\)) and is admissible yet historically undecided - the kind of gap this prompt targets.

**\(q\)-analogues (optional generalisation).** A subspace design \(S_q(t,k,v)\) replaces subsets by subspaces of \(\mathbb{F}_q^v\); the first nontrivial \(q\)-Steiner system \(S_2(2,3,13)\) was constructed in 2016 (Braun–Etzion–Östergård–Vardy–Wassermann; **verify**), and small \(q\)-analogue existence questions are an adjacent, equally machine-checkable target.

**Isomorphism and prescribed symmetry.** Designs are considered up to isomorphism (relabelling of \(V\)); the automorphism group \(\mathrm{Aut}(\mathcal B)\le\mathrm{Sym}(V)\) acts on blocks. Prescribing a group \(G\le\mathrm{Sym}(V)\) as a subgroup of automorphisms (the **Kramer–Mesner** setting) reduces existence to a covering / exact-cover system over the \(G\)-orbits of \(t\)- and \(k\)-subsets - the practical route to both constructions and small nonexistence proofs.

**The open question, made specific.** Fix one admissible parameter set whose existence is currently open, and decide it.

Concrete candidate families, to be **re-verified** at session start:

- Steiner systems \(S(2,6,v)\) - the smallest historically open value being \(v=51\), with the frontier actively moving (several \(S(2,6,v)\) cases were settled in 2025–2026; **verify**).

- Other block-size-\(\ge6\) systems from the Handbook's undecided lists (\(S(2,7,v)\), \(S(2,8,v)\), \(S(2,9,v)\), and higher-\(t\) systems).

The chosen parameters and their status must be quoted from the current literature, not from this prompt.

## 2. Resolution standard

A **complete resolution** for a chosen admissible open case is one of:

- **(A) Existence.** An explicit block set \(\mathcal B\) together with an independent checker verifying, in exact arithmetic, that every \(t\)-subset of \(V\) lies in exactly \(\lambda\) blocks (and each block has size \(k\)). This settles existence affirmatively.

- **(B) Nonexistence.** A proof that no such design exists, by a complete isomorph-free exhaustive search carrying a machine-checkable completeness certificate, or an algebraic obstruction reducible to independently verifiable finite computations.

The headline target is a genuinely open case, decided outright - not merely under a prescribed symmetry (unless the symmetry-restricted result is itself the honestly-stated deliverable).

**Named certified forms accepted.**

- Exhaustive isomorph-free enumeration via `nauty`/`Traces` canonical forms or orderly generation, with a replay checker.

- Kramer–Mesner reduction solved by exact-cover / ILP / SAT / LLL, with the constructed design verified exactly and any `UNSAT` carrying DRAT/LRAT.

- Exact verification of the design property (every \(t\)-subset covered exactly \(\lambda\) times).

**Not accepted as resolution.**

- A block set whose covering was checked only on a sample of \(t\)-subsets.

- A "near-design" with a few over- or under-covered \(t\)-subsets.

- A nonexistence result valid only for designs with a prescribed automorphism group, represented as full nonexistence.

- A heuristic or timed-out search reporting "none found," absent a completeness certificate over a delimited class.

- Reproducing a Handbook value without independent regeneration and verification.

## 3. Graded partial-result targets

- **P1 - Reproduce and verify a known design.** Regenerate a classical design (e.g. the Witt systems \(S(5,6,12)\), \(S(5,8,24)\), or an \(S(2,4,v)\)) and verify the exact-covering property with an independently written checker. *Certificate:* block list + checker output + SHA-256.

- **P2 - Kramer–Mesner machinery.** Reproduce a known design via the prescribed-automorphism-group method: build the orbit incidence matrix and solve the exact-cover system (ILP / LLL / SAT), verifying the result exactly. *Certificate:* the \(G\)-orbit data + solver output + exact verification.

- **P3 - Construct an open design.** Settle an open admissible case affirmatively by a Kramer–Mesner search over a well-chosen group \(G\), then verify exactly. *Certificate:* the design + \(G\) + exact-covering check.

- **P4 - Prescribed-symmetry nonexistence.** For an open case, prove no design with a prescribed nontrivial \(G\) exists (SAT / ILP `UNSAT` with DRAT, or exhaustive orbit search). *Certificate:* proof trace + explicit \(G\) and orbit model.

- **P5 - Exhaustive decision for a small case.** Complete an isomorph-free existence / nonexistence for a genuinely open case within reach, with a global completeness certificate. *Certificate:* enumeration log + independent replay.

- **P6 - Settle a case outright (windfall).** Construct, or prove nonexistent, a specific open Steiner system / \(t\)-design.

- **P7 - Family or large set.** Extend a settled construction to a family or to a large-set / resolvable version, with the same certificate standard.

## 4. Known results and prior art

- **Kirkman (1847)** and **Steiner (1853)** originated triple systems; **Hanani** settled the existence spectra of \(S(2,3,v)\), \(S(2,4,v)\), \(S(2,5,v)\), and the Steiner quadruple systems \(S(3,4,v)\) (existence iff \(v\equiv2,4\pmod6\)). So for \(k\le5\), \(S(2,k,v)\) exists for all admissible \(v\), and \(S(3,4,v)\) is fully decided.

- **Witt designs** \(S(4,5,11)\), \(S(5,6,12)\), \(S(4,7,23)\), \(S(5,8,24)\) arise from the Mathieu groups.

- **Teirlinck (1987)** proved nontrivial \(t\)-designs exist for every \(t\); **Keevash (2014)** proved Steiner systems and designs exist for all large \(v\) meeting divisibility, reproved combinatorially by **Glock, Kühn, Lo, Osthus (2016)**. These are asymptotic and do not decide specific small \(v\).

- **Kramer & Mesner (1976)** introduced prescribing an automorphism group; the method (with LLL and ILP / SAT solvers) underlies most modern small-design constructions - **Braun, Kerber, Kohnert, Laue, Wassermann** and collaborators.

- The **Handbook of Combinatorial Designs** (Colbourn & Dinitz, 2nd ed., 2007) tabulates undecided cases; for block size \(\ge6\) many \(S(2,k,v)\) remain open. **Reid–Rowley** survey \(S(2,4,v)\) refinements (anti-Pasch, etc.).

- The frontier is moving: recent 2025–2026 work reports \(S(2,6,226)\), \(S(2,6,441)\), \(S(2,7,505)\), \(S(2,8,225)\), \(S(2,9,289)\), and \(S(2,9,369)\) among others (**verify** each - attributions and exact parameters must be checked against the current arXiv / journals).

- Classification tooling: **Kaski & Östergård**, *Classification Algorithms for Codes and Designs* (2006); **Östergård–Pottonen** (Steiner triple systems of order 19).

**Status as of mid-2026 - re-verify against the current literature before starting any session.** The undecided lists shrink as constructions appear; confirm that the chosen parameter set is still open, check the Handbook's successor / errata and recent arXiv, and record the status with an access date before committing search effort.

## 5. Attack plan

`[search]` for constructions, `[enum]` for isomorph-free decision; both terminate in exact certificates.

- **Prescribed-automorphism construction (workhorse).** Choose a group \(G\le\mathrm{Sym}(V)\), build the Kramer–Mesner orbit-incidence matrix over the \(G\)-orbits of \(t\)- and \(k\)-subsets, and solve the exact-cover / \(\{0,1\}\) system with **LLL** (`fplll`), ILP (`Gurobi`/`SCIP` for exploration, exact re-check), or SAT (`kissat`/`CaDiCaL`, with DRAT for `UNSAT`). `GAP` supplies candidate groups and orbits.

- **Isomorph-free enumeration.** `nauty`/`Traces` for canonical block-design forms; orderly or canonical-augmentation generation for exhaustive small-case decisions; replay under an independently implemented canonicaliser.

- **Tactical decomposition and resolvability.** When the target is a resolvable or large-set design, exploit parallel-class structure to split the search; verify resolvability exactly (a partition of all points by each class) rather than assuming it from the construction.

- **Exact verification core.** A standalone checker enumerates all \(\binom{v}{t}\) \(t\)-subsets and confirms each is covered exactly \(\lambda\) times, in exact integer arithmetic; `SageMath` (`designs`) and `GAP` (`DESIGN` package) cross-check block sizes, replication numbers, and automorphisms.

- **One-workstation scope.** Kramer–Mesner with a well-chosen \(G\) turns a huge search into a tractable exact-cover instance - the realistic route to a construction. Unrestricted exhaustive enumeration is feasible only for small \(v\); larger cases without a prescribed group are out of reach. Choose \(G\) to make both the construction and any nonexistence claim tractable.

- **Failure modes.**

  - A poorly chosen group giving an infeasible or intractable orbit system.

  - ILP / SAT blowup on the exact-cover instance.

  - Incomplete isomorph rejection (over- or under-counting).

  - Verifying the covering on a sample rather than all \(t\)-subsets.

  - Representing a prescribed-\(G\) nonexistence as full nonexistence.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every design is verified by exact enumeration of all \(t\)-subsets; every nonexistence carries a completeness certificate (isomorph-free replay or DRAT/LRAT). Heuristic or timed-out searches are never certification.

2. **Independent verification.** A standalone covering checker (separate from the search) re-verifies every constructed design; a DRAT checker validates SAT `UNSAT`; a second system (`SageMath` vs `GAP`) recomputes design parameters and automorphism groups.

3. **Reproducibility.** All block sets, groups \(G\), orbit matrices, encodings, solver versions, and seeds recorded; SHA-256 manifest over every artifact; the chosen parameters and their open status quoted from the current literature with an access date.

4. **Preservation.** Construction and enumeration source is part of the record (the Hadamard-668 lost-source lesson); a `NEXT_STEPS.md` records the parameters attacked, the groups tried, and the state of the search when pausing.

5. **Honest reporting.** The report states up front whether the chosen open case was settled outright. A prescribed-symmetry nonexistence, a reproduced classical design, or an incomplete search is labelled as such and never represented as deciding the design's existence in general.
