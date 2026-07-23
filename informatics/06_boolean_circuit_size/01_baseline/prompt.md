# PROMPT FOR CERTIFIED MINIMUM CIRCUIT SIZE OF EXPLICIT SMALL FUNCTIONS

## Exact circuit and formula size via SAT-based exact synthesis with optimality proofs

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 06 of 50
**Area:** algorithms & bilinear complexity
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The minimum circuit size of a Boolean function - the fewest gates over a fixed basis needed to compute it - is the most concrete instance of the central question of complexity theory, and for small functions it is exactly computable. Knuth determined the exact circuit size of all \(4\)- and \(5\)-input functions; the frontier now lies at specific structured \(6\)-input functions and at completeness for restricted families, reachable by SAT-based **exact synthesis**: "is there a circuit of size \(s\) computing \(f\)?" is a satisfiable/unsatisfiable question whose UNSAT side gives a certified lower bound. This is the archetypal AI-native task - the field's own tool (SAT with proof logging) settles it, and every result is machine-checkable: an upper bound is an explicit circuit (a truth-table re-evaluation), a lower bound is a DRAT/LRAT UNSAT proof. The on-machine verifier that closes the loop is a circuit evaluator over all \(2^n\) inputs plus a DRAT/LRAT checker on the size-\((s-1)\) infeasibility proof. Any circuit without a matching optimality proof, or a heuristic "smallest found", is a partial result.

## 1. Exact problem statement

Fix an input count \(n\) and a **gate basis** \(\mathcal{B}\) (state it explicitly). Two standard choices:

- \(\mathcal{B}_2\) = all \(16\) two-input Boolean gates; **circuit size** \(C(f)\) = number of gates (the Knuth measure).
- \(\{\wedge,\vee,\neg\}\) with fan-in \(2\) and \(\neg\) free; **formula size** \(L(f)\) = number of leaves when the circuit is a tree.

A **circuit** is a directed acyclic graph whose sources are the \(n\) inputs (and constants) and whose internal nodes are gates from \(\mathcal{B}\), with one designated output; it **computes** \(f:\{0,1\}^n\to\{0,1\}\) if the output column equals \(f\)'s truth table. Define

\[
C_{\mathcal B}(f)=\min\{\,\#\text{gates in a circuit over }\mathcal B\text{ computing }f\,\},\qquad
L(f)=\min\{\,\#\text{leaves in a formula computing }f\,\}.
\]

**NPN equivalence.** Functions are considered up to negation of inputs, permutation of inputs, and negation of output; this preserves \(C_{\mathcal B_2}\). The class counts are

\[
\#\text{NPN}(4)=222,\qquad \#\text{NPN}(5)=616\,126,\qquad \#\text{NPN}(6)\approx 2.0\times10^{14}.
\]

**Conventions.**

- The basis and the size measure (circuit vs formula vs multiplicative complexity vs depth) are declared up front; a value over one basis never transfers to another.
- Constants \(0,1\) and input negations are free in \(\mathcal{B}_2\); the encoding fixes this precisely.
- A "specific function" is given by its full \(2^n\)-bit truth table or an exact algebraic description.
- Multi-output functions (e.g. a full multiplier) are handled as a shared circuit with several designated outputs; the size is the total gate count, and the encoding must be stated as multi-output.

**Known values (to reproduce and re-verify).**

- Over \(\mathcal B_2\), the hardest \(4\)-input function needs \(7\) gates and the hardest \(5\)-input function needs \(12\) gates (Knuth); most functions sit well below the counting bound \(C(f)\le (1+o(1))2^n/n\) (Lupanov).
- Every \(n\le 5\) NPN class has a known exact \(C(f)\) and \(L(f)\); these tables are the correctness gate for any re-implementation.
- No \(6\)-input function has a fully certified exact \(C_{\mathcal B_2}\) in general; specific named functions are the live targets.

**Frontier adopted here.** \(C_{\mathcal B_2}(f)\) and \(L(f)\) are fully tabulated for all \(f\) with \(n\le 5\). The open frontier is: (i) specific named \(6\)-input functions (symmetric functions, small arithmetic like \(3\)-bit multiplier outputs, threshold/majority, S-box coordinates, ECC encoders); (ii) completeness for structured \(6\)-input subfamilies - a full census of \(2^{64}\) functions is infeasible. State the exact function(s) or family and the basis. Re-verify Knuth's tables against Section 4.

## 2. Resolution standard

For a stated function \(f\) (or family) and basis \(\mathcal B\), a **resolution** is the exact integer \(C_{\mathcal B}(f)\) (or \(L(f)\)) with **both**:

1. **Upper bound (circuit).** An explicit gate list computing \(f\), verified by a standalone evaluator over all \(2^n\) inputs (truth-table match), written separately from the synthesis code.
2. **Lower bound (optimality).** A **DRAT/LRAT UNSAT certificate** for the exact-synthesis CNF

\[
\exists\ \text{circuit of size } C_{\mathcal B}(f)-1 \text{ over } \mathcal B \text{ computing } f,
\]

   with (a) the encoding source, (b) a soundness argument for every symmetry-breaking / structural constraint (topological ordering, no-redundant-gate, colexicographic canonicalization), and (c) an LRAT check by a formally verified checker.

For a **family/classification** result, the same must hold for every member, with the enumeration of members proved complete (isomorph-free), or the family defined so a single parametric certificate covers it.

**Not accepted as resolution.**

- A circuit reported as minimal without a size-\((s-1)\) UNSAT proof.
- An optimality claim from solver output with no replayable DRAT/LRAT proof.
- A lower bound under an unjustified structural restriction (fixing the top gate) unless proved to lose no optimal circuit.
- A result over one basis reported as holding for another (a \(\{\wedge,\vee,\neg\}\) formula-size claim reported as \(\mathcal B_2\) circuit size).
- A "smallest circuit found by heuristic" without exhaustive/UNSAT optimality; an incomplete family census presented as complete.
- A circuit-size value quoted for a function up to NPN equivalence but applied to a non-representative member without accounting for the (free) input/output negations that map between them.

## 3. Graded partial-result targets

- **P1 - Reproduce the tables.** Independently regenerate the full \(n=4\) circuit-size table (\(222\) NPN classes) and a verified slice of the \(n=5\) table (\(616\,126\) classes) with our own exact-synthesis engine and evaluator; match Knuth's values.
  - *Certificate:* per-class circuits, matching UNSAT proofs at size \(-1\), and a manifest.
- **P2 - Certified minimum for a named \(6\)-input function.** Determine \(C_{\mathcal B_2}(f)\) (and/or \(L(f)\)) for a specific \(6\)-input function of interest, with both an explicit circuit and a size-\((s-1)\) UNSAT proof.
  - *Certificate:* verified circuit + certified UNSAT.
- **P3 - Improved upper bound.** A smaller circuit than the best published for a specific function (a new record), truth-table verified.
  - *Certificate:* the evaluated circuit and the cited baseline.
- **P4 - Certified lower-bound gap-closing.** A DRAT/LRAT UNSAT proof establishing \(C_{\mathcal B}(f)\ge s\) for a function where only an upper bound was known, narrowing or closing the bracket.
  - *Certificate:* the certified UNSAT proof and encoding.
- **P5 - Complete a small \(6\)-input subfamily.** An isomorph-free complete classification of a structured family (all symmetric \(6\)-input functions, or all functions of a bounded circuit size) with certified minima throughout.
  - *Certificate:* the complete enumeration + per-member certificates.
- **P6 - Multiplicative-complexity or depth variant.** The exact multiplicative complexity (AND-gate count over \(\{\oplus,\wedge\}\)) or minimum depth of a named function, with matching UNSAT proofs - a measure of direct cryptographic relevance.
  - *Certificate:* verified circuit + certified optimality in the stated measure.
- **P7 - Formalized checker.** A machine-checked (Lean/Coq) circuit-evaluation predicate and a verified checker for synthesized circuits, reducing the trusted base of all upper-bound claims.
  - *Certificate:* the formal predicate and the checked checker.

## 4. Known results and prior art

- **Knuth's tables.** Knuth, *TAOCP* Vol. 4A (2011) and Vol. 4 Fascicle 6, *Satisfiability* (2015) - exact circuit size \(C(f)\) and formula size for all \(n\le 4\) and all \(n=5\) functions, via a specialized exact-synthesis/BDD method; also depth and formula-size tables. The number of \(5\)-input NPN classes is \(616\,126\).
- **SAT-based exact synthesis.** Kojevnikov, Kulikov, Yaroslavtsev, "Finding efficient circuits using SAT-solvers" (SAT 2009) - the CNF encoding of "a size-\(s\) circuit computes \(f\)", giving upper bounds from SAT models and lower bounds from UNSAT.
- **Synthesis toolchains.** Haaswijk, Soeken, Testa, Mishchenko, De Micheli - "Classifying functions with exact synthesis" (~2017) and "SAT-based exact synthesis: encodings, topology families, and parallelism" (~2019); Soeken et al. on practical exact synthesis in the EPFL logic-synthesis toolchain.
- **Multiplicative complexity.** Determining multiplicative complexity of Boolean functions via SAT (~2020, e.g. reducing \(\wedge\)-count for S-boxes); relevant to masking and MPC-friendly ciphers.
- **QBF and local improvement.** Circuit minimization with QBF-based exact synthesis (~2023) and SAT-based circuit local improvement (Kulikov et al., ~2021) - heuristic/optimal hybrids.
- **Tooling.** ABC (Berkeley), the EPFL `mockturtle`/`percy` exact-synthesis libraries, and Knuth's own programs from the TAOCP software page.
- **Counting context.** Shannon's counting lower bound and Lupanov's \((1+o(1))2^n/n\) upper bound frame the range; they are asymptotic and do not give exact small-\(n\) values, which is precisely why exhaustive/SAT synthesis is needed.
- **Cryptographic instances.** Exact circuit and multiplicative-complexity results for concrete S-boxes (AES, small ciphers) and multipliers are scattered across the applied-crypto literature and are natural P2/P6 targets with real utility.
- **Depth and delay.** Exact minimum-depth synthesis and joint size/depth optimization have their own SAT encodings (Knuth's depth tables; the size/depth Pareto frontier); they are the reference for the P6 depth variant.

**Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

**`[search]` - exact synthesis.**

1. Use the standard "does a size-\(s\) circuit compute \(f\)?" CNF: variables for each of \(s\) gates (its two fan-in sources and its \(4\)-bit truth-table selector); constraints propagate the correct output column for all \(2^n\) rows.
2. Binary-search on \(s\): the smallest satisfiable \(s\) gives the circuit; UNSAT at \(s-1\) gives the certified lower bound (log DRAT, convert to LRAT, check with a verified checker).
3. Add soundness-argued symmetry breaking: topological normal form, no two gates with identical inputs, colexicographic ordering, output-gate canonicalization.

**`[search]` - classification.**

1. Generate NPN-class representatives isomorph-free (NPN canonical form / nauty on the function's structure).
2. Run exact synthesis per representative, memoizing by canonical truth table.
3. Prove the representative set complete before reporting a family census.

**Tools.**

- SAT: CaDiCaL, kissat, CryptoMiniSat (DRAT/LRAT).
- Checking: drat-trim, cake_lpr / verified LRAT checkers.
- Synthesis libraries: EPFL `percy`/`mockturtle` and ABC as cross-checks.
- Support code: custom C++/Python for the encoder, NPN canonicalization, and the independent truth-table evaluator.

**UNSAT certificate structure.** The lower-bound artifact is the size-\((s-1)\) CNF, the solver's DRAT trace, its LRAT conversion, and the verified checker's acceptance log; the symmetry-breaking soundness note argues that each added constraint removes only circuits equivalent to (or dominated by) a retained one, so UNSAT of the restricted formula implies UNSAT of the full one.

**First concrete session steps.**

1. Reproduce the \(n=4\) table end to end (SAT circuit + UNSAT at size \(-1\)) as a correctness gate (P1).
2. Cross-check a sample of \(n=5\) values against Knuth's published table.
3. Pick a named \(6\)-input target (e.g. \(3\times3\)-bit multiplier output bit, or MAJ\(_6\)); find a good circuit, then push the size-\((s-1)\) UNSAT (P2).
4. If UNSAT is hard, apply cube-and-conquer and record a certified partial lower bound (P4).
5. Fix the basis and measure in the report header before quoting any size, and attach the truth table of the target function verbatim.

**One-workstation scope and failure modes.** \(n=4\) is trivial; a full \(n=5\) reproduction is a large but feasible batch; individual \(6\)-input functions are tractable when \(C(f)\) is modest. Full \(6\)-input classification (\(2^{64}\)) is infeasible - restrict to named functions or structured families. Dominant risks:

- UNSAT blow-up for functions near the maximum \(6\)-input complexity (\(\approx 2^6/6\) gates).
- An unsound symmetry-breaking clause making a synthesizable size look infeasible - guard with an unrestricted re-run.
- Trusting solver output without LRAT replay.
- Encoding errors in the gate-semantics constraints that silently accept a wrong circuit - cross-check every SAT model with the independent truth-table evaluator.
- NPN-canonicalization bugs breaking a classification's completeness - dual-implement the canonical form.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every minimality claim carries a DRAT/LRAT UNSAT proof checked by a formally verified checker; every circuit is validated by exhaustive \(2^n\)-input truth-table evaluation. No floating point.
2. **Independent verification.** The circuit evaluator and the proof checker are implemented separately from the synthesis engine; results are cross-checked against ABC/`percy` on a sample; NPN canonicalization is dual-implemented for any classification claim.
3. **Reproducibility.** The basis, size measure, CNF encoding, symmetry-breaking constraints, and tool versions are recorded; a SHA-256 manifest covers CNFs, proofs, and circuit files; Knuth's tables (or the published value) reproduced or extended are cited with source and access date.
4. **Preservation.** The encoder, canonicalization code, evaluator, and all circuits and proofs are part of the record; large UNSAT proofs not stored are hashed with regeneration commands.
5. **Honest reporting.** The report states the exact function/family, the basis, and the measure, and whether the minimum was certified or only an upper bound obtained; a heuristically found circuit is never reported as minimal without a matching certified UNSAT proof, and an incomplete family census is never reported as complete.
