# PROMPT FOR CERTIFYING THE NEXT OPTIMAL SORTING NETWORK

## Extending the machine-checked size or depth frontier for comparator sorting networks

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 01 of 50
**Area:** algorithms & bilinear complexity
**Modes:** `[search]` `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A sorting network is an oblivious comparison algorithm: a fixed sequence of compare-exchange operations that sorts every input of length \(n\). Two cost measures matter - the *size* \(s(n)\) (number of comparators) and the *depth* \(d(n)\) (number of parallel layers). Both are known exactly only for small \(n\): size is settled through \(n=12\) and depth through \(n=17\). Each new optimal value is a genuine closed-loop result - an explicit record network (upper bound) together with a machine-checkable proof that no smaller network exists (lower bound). The lower bound is exactly what SAT solvers with proof logging produce: encode "some network of size \(k-1\) sorts \(n\) inputs", break symmetries, and derive a DRAT/LRAT-certified UNSAT proof. The problem is matched to current AI methods because the entire pipeline - encoding, symmetry reduction, solver run, proof replay, and independent sortedness check via the 0/1 principle - is verifiable on one workstation. The on-machine verifier that closes the loop is a DRAT/LRAT checker plus a standalone sortedness checker over all \(2^n\) Boolean inputs. Anything short of a certified matching upper and lower bound at a new \(n\) (Section 2) is a partial result, never a solution.

## 1. Exact problem statement

A **comparator** on channels \(i<j\), written \([i{:}j]\), maps a vector \(x\in\mathbb{R}^n\) to the vector obtained by replacing \((x_i,x_j)\) with \((\min(x_i,x_j),\max(x_i,x_j))\). A **comparator network** on \(n\) channels is a finite sequence \(C=(c_1,\dots,c_k)\) of comparators; it is a **sorting network** if \(C(x)\) is non-decreasing for every \(x\in\mathbb{R}^n\).

**The 0/1 principle.** By Knuth's theorem, \(C\) sorts all real inputs iff it sorts all \(2^n\) Boolean inputs:

\[
C \text{ sorts } \mathbb{R}^n \iff \forall x\in\{0,1\}^n:\ C(x)\ \text{is sorted}.
\]

This reduces correctness to a finite, exactly checkable predicate and underlies every SAT encoding below.

**Cost measures.** The **size** of \(C\) is \(k\). The **depth** is the number of layers in the greedy partition of \(C\) into maximal sets of comparators acting on pairwise-disjoint channels - equivalently, the length of the longest data-dependency chain. Define

\[
s(n)=\min\{\,\mathrm{size}(C): C \text{ sorts } n \text{ channels}\,\},
\qquad
d(n)=\min\{\,\mathrm{depth}(C): C \text{ sorts } n \text{ channels}\,\}.
\]

These are two distinct optimizations: a size-optimal network need not be depth-optimal, and conversely (e.g. minimizing depth often spends extra comparators).

**Normalization and conventions.**

- A network may be assumed to begin with a *canonical first layer* of \(\lfloor n/2\rfloor\) comparators \([2i{-}1{:}2i]\); every sorting network can be transformed to one with this prefix without increasing size or depth (Knuth / Parberry).
- Comparators are non-degenerate (\(i\ne j\)); repeated identical comparators are never useful and are excluded by the encoding.
- "Layer" and "parallel step" are synonymous; depth counts layers.

**Size regime and current frontier.** \(s(n)\) is proved optimal for \(n\le 12\); \(d(n)\) is proved optimal for \(n\le 17\). The two smallest open instances are:

- **Size:** determine \(s(13)\). The best known network has \(45\) comparators; \(45\) is not proved optimal, so the open question is whether \(s(13)\in\{44,45\}\) (the counting lower bound is far below).
- **Depth:** determine \(d(18)\). The best known network has depth \(11\); the trivial bound \(d(18)\ge d(17)=10\) leaves open whether depth \(10\) suffices, i.e. whether \(d(18)\in\{10,11\}\).

**Known optimal values (to reproduce and re-verify).**

- Size: \(s(9)=25\), \(s(10)=29\), \(s(11)=35\), \(s(12)=39\) (all proved optimal); \(s(13)\le 45\) (open).
- Depth: \(d(11)=d(12)=8\), \(d(13)=d(14)=d(15)=d(16)=9\), \(d(17)=10\) (all proved optimal); \(d(18)\le 11\) (open).
- The information-theoretic size floor \(\lceil\log_2 n!\rceil\) and the trivial depth floor \(\lceil\log_2 n\rceil\) are far below these, so both lower bounds are genuinely combinatorial and require the SAT machinery of Section 5.

The task adopts these as the concrete targets. All values above are to be re-verified against Section 4 before a session (records move).

## 2. Resolution standard

Fix a target instance - either \((\text{measure}=\text{size},\,n=13)\) or \((\text{measure}=\text{depth},\,n=18)\), or the next open instance current at session time. A **resolution** consists of a value \(k^\star\) and **both** of the following, independently checked.

1. **Upper bound (construction).** An explicit network \(C\) on \(n\) channels with \(\mathrm{measure}(C)=k^\star\), whose sortedness is verified by a standalone program evaluating all \(2^n\) Boolean inputs (the 0/1 principle), written separately from any search code.
2. **Lower bound (optimality).** A machine-checkable proof that **no** network on \(n\) channels achieves \(\mathrm{measure}=k^\star-1\), delivered as a **DRAT or LRAT UNSAT certificate** for a CNF encoding of

\[
\exists\,C:\ \mathrm{measure}(C)=k^\star-1\ \wedge\ \forall x\in\{0,1\}^n\ C(x)\text{ sorted},
\]

together with (a) the exact encoding source, (b) a written soundness argument for every symmetry-breaking clause (first-layer/first-two-layer normalization, reflection, prefix fixing), and (c) an LRAT check by a formally verified checker.

**Named certified form.** DRAT/LRAT-checked UNSAT for the lower bound; exhaustive 0/1-input sortedness re-evaluation for the upper bound; where symmetry breaking removes solutions, a companion argument (or a second unrestricted-encoding UNSAT run on a reduced sub-instance) that the reduction is sound.

**Not accepted as resolution.**

- A new record network (better upper bound) with no matching lower bound.
- An optimality claim resting on solver output with no replayable DRAT/LRAT proof.
- A lower bound proved only under an unjustified restriction (fixing a full prefix, or assuming the last layers have a specific shape) unless that restriction is proved to lose no optimal network.
- A depth result reported as a size result or vice versa.
- A "generate-and-prune" run whose completeness (that pruning discards only sub-optimal or isomorphic prefixes) is not argued and re-checkable.
- Any pipeline whose symmetry-breaking encoding lacks a soundness argument, or whose proof cannot be re-checked from the recorded CNF and solver version.

## 3. Graded partial-result targets

- **P1 - Reproduce the frontier.** Verify sortedness of published size-optimal networks for \(n\le 12\) and depth-optimal networks for \(n\le 17\), and re-check (or regenerate) the existing UNSAT optimality proofs with a formally verified LRAT checker.
  - *Certificate:* replayed proofs plus a 0/1 sortedness log; SHA-256 manifest over every network and proof file.
- **P2 - Improved upper bound.** A network beating the current best-known size for \(n=13\) (\(<45\) comparators) or achieving depth \(10\) for \(n=18\), sortedness-verified.
  - *Certificate:* the network file and an independent \(2^n\) Boolean check. A depth-\(10\) network for \(n=18\) already settles \(d(18)=10\) via \(d(18)\ge d(17)=10\).
- **P3 - Partial certified lower bound.** A DRAT/LRAT UNSAT proof ruling out \(\mathrm{measure}=k^\star-1\) under an explicitly stated, soundness-argued restriction on early layers, shrinking the open gap.
  - *Certificate:* the restricted-encoding proof plus the restriction's justification and its coverage argument.
- **P4 - One-sided full lower bound.** A complete DRAT/LRAT UNSAT proof that \(s(13)\ge 46\) (resp. \(d(18)\ge 11\)) with full symmetry-breaking soundness.
  - *Certificate:* the certified UNSAT proof, the CNF, and the symmetry-breaking soundness note.
- **P5 - Full resolution of one instance.** Matching P2 and P4 to pin \(s(13)\) or \(d(18)\) exactly, meeting Section 2 in full.
  - *Certificate:* both artifacts plus a combined report stating the exact value and measure.
- **P6 - Second instance or reusable framework.** Having closed one, close the other, or deliver a soundness-audited symmetry-breaking framework that demonstrably scales the SAT lower-bound search one further \(n\).
  - *Certificate:* the second resolution, or the framework with a worked new-instance proof.

## 4. Known results and prior art

- **0/1 principle and foundations.** Knuth, *TAOCP* Vol. 3, §5.3.4 - the 0/1 principle, Batcher's odd-even and bitonic constructions, exact small-\(n\) optima, and the canonical-first-layer normalization.
- **Classical small optima.** Size and depth optima for \(n\le 8\) are classical (Knuth, Floyd–Knuth, Van Voorhis). Batcher (~1968) gives \(O(n\log^2 n)\) size and depth; AKS (Ajtai–Komlós–Szemerédi ~1983) gives asymptotically \(O(n\log n)\) depth but is impractical at small \(n\).
- **Size, SAT era.** Codish, Cruz-Filipe, Frank, Schneider-Kamp (~2014) - "generate-and-prune" established \(s(9)=25\) and \(s(10)=29\). The Bose–Nelson sorting problem for \(11\) and \(12\) channels was answered as \(s(11)=35\), \(s(12)=39\) (Jannis Harder, ~2020, *verify* author and optimality status). \(s(13)\) is open; best known \(45\) (*verify* on the record tracker).
- **Depth, SAT era.** Bundala and Závodný (~2014) proved optimal depths for \(11\le n\le 16\) via SAT over first-two-layer equivalence classes. Ehlers and Müller (~2015) settled \(d(17)=10\) and improved upper bounds for \(17,19,20\). \(d(18)\) is open.
- **Recent upper-bound activity.** A 2025 preprint reports depth-\(13\) networks for \(27\) and \(28\) channels by extending high-quality \(16\)- and \(12\)-channel prefixes and completing with SAT (upper bounds, not optimality).
- **Prefix/normalization theory.** Parberry - the "pairwise" and canonical first-layer arguments; Bundala–Codish–Cruz-Filipe–Schneider-Kamp, "Optimal-depth sorting networks" and "Sorting networks: to the end and back again" - the equivalence-class machinery on the first two layers that makes the depth SAT search tractable.
- **Formally verified checking.** Cruz-Filipe, Marques-Silva, Schneider-Kamp and others produced formally verified checkers for size-optimal sorting-network proofs; the LRAT toolchain (drat-trim, cake_lpr, verified checkers) is standard for solver certificates.
- **Record tracker.** Bert Dobbelaere maintains a public tracker of best-known size and depth networks with optimality status - the reference baseline for any claimed improvement.

**Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

**`[search]` - construction (upper bounds).**

1. Encode "does an \(n\)-channel network of the target measure sort all \(2^n\) inputs?" as CNF over comparator-selection variables and per-layer vector-propagation variables.
2. Seed with hand-crafted or greedily extended prefixes (as in the recent depth-13 constructions): fix a strong prefix, then let CaDiCaL/kissat complete the remaining layers.
3. Validate every candidate with the standalone 0/1 checker before trusting it; record the exact gate list.

**`[cert]` - optimality (lower bounds).**

1. Build the "size \(=k-1\)" (resp "depth \(=k-1\)") satisfiability encoding.
2. Reduce the search space with standard, individually soundness-argued reductions: canonical first layer; first-two-layer equivalence classes (Bundala–Závodný); reflection symmetry; prefix fixing.
3. Run with proof logging (DRAT); trim and convert to LRAT (drat-trim, then cake_lpr or a verified checker).
4. For hard instances use **cube-and-conquer** (march_cu split, kissat/CaDiCaL per cube) with per-cube proofs concatenated.
5. Cross-check with a second solver (CryptoMiniSat) on a sub-instance, and re-run a reduced case *without* symmetry breaking to guard soundness.

**Tools.**

- SAT with proof logging: CaDiCaL, kissat, CryptoMiniSat (DRAT/LRAT).
- Proof checking: drat-trim, cake_lpr, and formally verified LRAT checkers.
- Hard instances: march_cu for cube-and-conquer partitioning.
- Support code: custom C++/Python for the encoder and the independent 0/1 sortedness checker; nauty/Traces if canonicalizing prefix layers.

**First concrete session steps.**

1. Reproduce P1: fetch the current record networks and existing proofs, run the independent 0/1 checker and the LRAT checker end to end.
2. Rebuild the depth encoding for \(n=17\) and re-derive the known \(d(17)=10\) UNSAT to validate the toolchain against a settled instance.
3. Push to the open instance (depth \(n=18\) is the more tractable lower-bound target than size \(n=13\)); attempt the depth-\(10\) construction first (P2), since a hit closes \(d(18)\) immediately.
4. If no depth-\(10\) network exists after strong search, set up the depth-\(10\) UNSAT with first-two-layer classes and begin cube-and-conquer (P4).

**One-workstation scope and failure modes.** A single new record network is usually found in hours. The lower-bound UNSAT for the next open \(n\) is the hard part: the size encoding for \(n=13\) and the depth encoding for \(n=18\) may blow up beyond a workstation without strong symmetry breaking, and cube-and-conquer proofs can reach hundreds of gigabytes. Dominant risks:

- Search blow-up: the size-\(44\) or depth-\(10\) UNSAT may exceed workstation memory/time even with equivalence-class reductions.
- Unsound symmetry breaking: a bad clause silently makes a satisfiable instance UNSAT - guard with an unrestricted re-run on a reduced case.
- Unverified solver output: never trust an UNSAT claim without replaying the LRAT proof through a verified checker.

Report a search that did not close as a certified partial bound (P3/P4), never as a resolution.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every optimality claim carries a DRAT/LRAT UNSAT proof checked by a formally verified checker; every construction is validated by exhaustive \(2^n\) Boolean-input evaluation. Floating point plays no role.
2. **Independent verification.** The sortedness checker and the proof checker are implemented separately from the search/encoder code. At least one lower bound is cross-validated by a second solver on a reduced sub-instance, and symmetry-breaking soundness is argued in writing and spot-checked against an unrestricted encoding.
3. **Reproducibility.** All CNF encodings, solver names and versions, seeds, cube splits, and restriction lemmas are recorded; a SHA-256 manifest covers every CNF, proof, and network file. The specific record being improved is cited with source and access date (the public tracker), so the claimed gain is unambiguous.
4. **Preservation.** Encoder source, symmetry-breaking generators, cube scripts, and the final networks and proofs are part of the record. Anything not preserved (e.g. a multi-hundred-GB proof reduced to a hash) is stated explicitly.
5. **Honest reporting.** The report states up front whether a new optimal value was certified, and in which measure (size vs depth); a record-breaking construction with no matching lower bound is reported as an upper bound only, and an optimality claim without a replayable certified proof is never represented as resolved.
