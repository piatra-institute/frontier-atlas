# PROMPT FOR CERTIFIED ADDITION-CHAIN LENGTHS AND SCHOLZ–BRAUER

## Exact \(\ell(n)\) values and machine-checked verification of \(\ell(2^n-1)\le n-1+\ell(n)\)

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 04 of 50
**Area:** algorithms & bilinear complexity
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

An addition chain for a positive integer \(n\) is the shortest straight-line program that reaches \(n\) from \(1\) using only additions of earlier results; \(\ell(n)\) is its length. It is the exact-complexity measure for single-exponentiation \(x\mapsto x^n\) and a classical testbed for optimal-search methods. The **Scholz–Brauer conjecture**, \(\ell(2^n-1)\le n-1+\ell(n)\), is open in general though verified over large ranges and proved for structured cases. The problem is closed-loop on both fronts: an upper bound on \(\ell(n)\) is an explicit chain (trivially checkable), and the exact value \(\ell(n)\) demands an optimality proof - a complete branch-and-bound over the finite tree of chains with a replayable pruning log. This matches current AI methods: exact search with strong number-theoretic pruning, plus formal or independently re-run certificates. The on-machine verifier is a chain validator (upper bound) together with a replayable exhaustive-search log or a machine-checked inequality over a range (Scholz–Brauer). Anything short of an exact certified \(\ell(n)\) at a new \(n\), a certified extension of the Scholz–Brauer verified range, or a proved structural theorem is a partial result.

## 1. Exact problem statement

An **addition chain** for \(n\in\mathbb{Z}_{>0}\) is a sequence

\[
1=a_0,a_1,\dots,a_r=n,\qquad \forall k\ge 1\ \exists\, i,j<k:\ a_k=a_i+a_j
\]

(repetition of indices allowed). Its **length** is \(r\) (the number of additions), and

\[
\ell(n)=\min\{\,r:\ \text{an addition chain of length } r \text{ reaches } n\,\}.
\]

**Elementary bounds.** With \(\nu(n)\) the number of \(1\)-bits and \(\lambda(n)=\lfloor\log_2 n\rfloor\),

\[
\lambda(n)\le \ell(n)\le \lambda(n)+\nu(n)-1\quad(\text{binary method}),
\qquad
\ell(n)\ge \log_2 n+\log_2\nu(n)-2.13\quad(\text{Schönhage}).
\]

A chain is a **star chain** (Brauer chain) if each \(a_k\) uses the immediately preceding element \(a_{k-1}\); \(\ell^\ast(n)\) is the shortest star-chain length, \(\ell(n)\le\ell^\ast(n)\), with the first strict inequality at \(n=12509\) (Hansen).

**Scholz–Brauer.** The conjecture is

\[
\ell(2^n-1)\ \le\ n-1+\ell(n)\qquad(\forall n\ge 1),
\]

known to hold over a large verified range and proved for many structured families; the analogous **Brauer** statement \(\ell^\ast(2^n-1)\le n-1+\ell^\ast(n)\) is a theorem (Brauer).

**Conventions.**

- The cost measure is *number of additions* (chain length); every claim states whether it concerns \(\ell\) or the star variant \(\ell^\ast\).
- "Exact \(\ell(n)\)" always means a certified optimum, never a best-found upper bound.
- Big integers \(2^n-1\) are handled in exact arithmetic (GMP/FLINT); no floating-point length estimates enter a load-bearing step.

**Frontier adopted here.** Two targets: (i) exact \(\ell(n)\) for numbers beyond the current exhaustive tables, each with a certified optimality proof; (ii) machine-checked verification (or a proved structural theorem) for Scholz–Brauer over an extended range of \(n\). Re-verify current ranges against Section 4.

## 2. Resolution standard

**For an exact \(\ell(n)\) value.** Produce the integer \(\ell(n)\) with **both**:

1. an explicit chain of that length, validated by a standalone checker confirming each step is a sum of two earlier terms and the last term is \(n\); and
2. a certificate that no chain of length \(\ell(n)-1\) reaches \(n\) - the named form is a **complete branch-and-bound search with a replayable log** whose pruning rules (bounding functions, the Bleichenbacher–Flammenkamp reduced-graph reduction, small-step/big-step limits) are each stated with a soundness argument and whose exhaustiveness an independent re-runner can confirm.

**For Scholz–Brauer over a range.** For every \(n\) in an explicit interval \([n_0,n_1]\) extending the current verified frontier, a machine-checked demonstration of \(\ell(2^n-1)\le n-1+\ell(n)\): either

- (a) an explicit chain for \(2^n-1\) of length \(\le n-1+\ell(n)\) with \(\ell(n)\) itself certified (reducing to the exact-value standard); or
- (b) a formal proof (Lean/Coq) of a structural lemma covering the range.

The certificate must be independently re-checkable.

**Not accepted as resolution.**

- An upper bound on \(\ell(n)\) (a good chain) reported as the exact value without an optimality proof.
- An exact-value claim from a search whose pruning is unsound or whose exhaustiveness is not replayable.
- A heuristic "no shorter chain found" without a complete search over the bounded tree.
- A Scholz–Brauer verification that silently assumes an uncertified \(\ell(n)\).
- Conflating \(\ell\) with \(\ell^\ast\); a proof of the Brauer (star) inequality presented as a proof of Scholz–Brauer for \(\ell\).
- A single strict-inequality instance reported as a disproof of the (still open) conjecture.
- A Scholz–Brauer range certified using \(\ell(n)\) values taken from a published table without re-deriving or re-checking their optimality in this package.

## 3. Graded partial-result targets

- **P1 - Reproduce the tables.** Independently recompute \(\ell(n)\) for a substantial range with our own branch-and-bound and validator; reproduce landmark values and the census up to a stated bound, matching the published tables.
  - *Certificate:* validated chains plus replayable optimality logs; SHA-256 manifest.
- **P2 - Certified Scholz–Brauer range.** A machine-checked verification of \(\ell(2^n-1)\le n-1+\ell(n)\) for every \(n\) in an interval, each \(\ell(n)\) certified.
  - *Certificate:* per-\(n\) chains and optimality proofs, re-checkable.
- **P3 - New exact \(\ell(n)\) values.** Determine \(\ell(n)\) for specific numbers beyond current exhaustive coverage (e.g. selected high-\(\nu(n)\) numbers, or a new census level), each with an optimality certificate.
  - *Certificate:* the branch-and-bound log and the chain.
- **P4 - Structural theorem.** A proved lemma extending the known Scholz–Brauer families (new residue classes or special forms of \(n\)) or a proved bound on \(\ell(2^n-1)-\ell(n)\).
  - *Certificate:* a formal proof, or a fully written argument with any computational lemma independently checked.
- **P5 - Extend the census.** Push the complete table of \(\ell(n)\) (all \(n\) with \(\ell(n)\le L\)) one level of \(L\) further with certified optimality, reproducing the reduced-graph method.
  - *Certificate:* the census with per-value certificates and a manifest.
- **P6 - Strict-inequality / equality phenomena.** Independently confirm and certify reported strict-inequality instances of Scholz–Brauer (\(\ell(2^n-1)=n-2+\ell(n)\)) or map the \(n\) with \(\ell(2n)=\ell(n)\).
  - *Certificate:* certified \(\ell\) values on both sides of each reported instance.
- **P7 - Formalized validator.** A machine-checked (Lean/Coq) definition of the addition-chain predicate and a verified checker for externally produced chains, shrinking the trusted base for all upper-bound claims.
  - *Certificate:* the formal predicate and the checked checker.

## 4. Known results and prior art

- **Foundations.** Knuth, *TAOCP* Vol. 2, §4.6.3 - addition chains, the binary and factor methods, \(\ell(n)\), and the Scholz–Brauer history; Brauer (1939) - \(\ell^\ast(2^n-1)\le n-1+\ell^\ast(n)\); Hansen - non-star chains, first strict \(\ell<\ell^\ast\) at \(n=12509\).
- **Exact-value computation.** Bleichenbacher and Flammenkamp - the reduced-graph search that makes exhaustive \(\ell(n)\) computation tractable; Achim Flammenkamp's public tables of shortest chains; Neill Clift, "Calculating optimal addition chains" (~2011) - extended the exact census to all \(n\) with \(\ell(n)\le 29\) (a dataset of tens of millions of numbers, later enlarged) and improved the search algorithm.
- **Scholz–Brauer status.** Proved for many structured families and verified computationally over large ranges (Clift). Recent progress: notes (~2021–2023) proving the conjecture for infinitely many integers and for classes with \(\ell(2n)=\ell(n)\); Clift (July 2024) reported the **first instances of strict inequality** \(\ell(2^n-1)=n-2+\ell(n)\) - these **refine** but do **not** refute the conjecture, which remains open in general (*verify* the exact numbers and ranges).
- **Related conjectures.** \(\ell(2n)\ge\ell(n)\) (open in general); growth of \(\ell(2^a-1)\); the "star-chain" (Knuth/Hansen) questions.
- **Formalization tracking.** The DeepMind "formal-conjectures" project lists Scholz among open formalization targets, providing a Lean statement to build P4/P7 against.
- **Small values.** \(\ell(n)\) for the first several dozen \(n\) is tabulated in Knuth and OEIS (A003313); these are the correctness gate for any re-implementation.
- **Thurber and others.** Thurber and later authors proved Scholz–Brauer for further structured classes and small ranges; these arguments are the templates for the P4 structural theorems.

**Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

**`[search]` - exact values.**

1. Implement the Bleichenbacher–Flammenkamp reduced-graph branch-and-bound: build chains under a canonical ordering.
2. Prune with lower-bound functions (\(\log_2 n+\log_2\nu(n)-c\), plus the "vertical"/one-step bounds) and the reduced-graph normal form to avoid isomorphic re-exploration.
3. For a target \(n\), prove \(\ell(n)=r\) by exhibiting a length-\(r\) chain and completing the exhaustive search at length \(r-1\) returning empty; log all pruning decisions.

**`[search]` - Scholz–Brauer.**

1. For each \(n\) in the target interval, certify \(\ell(n)\) as above.
2. Construct an explicit chain for \(2^n-1\) via the standard Brauer construction (length \(\le n-1+\ell(n)\)), validate it, and record the inequality.
3. Where a family argument applies, formalize the lemma (P4) rather than re-searching every \(n\).

**Tools.**

- Search: custom C++ branch-and-bound (reduced-graph representation, bitset chains), with Neill Clift's published method as the reference.
- Arithmetic: GMP/FLINT for big integers on \(2^n-1\).
- Orchestration and validation: SageMath/Python; OEIS A003313 tables as the gate.
- Formalization: Lean 4 or Coq for structural lemmas and the chain-validity predicate.

**First concrete session steps.**

1. Reproduce \(\ell(n)\) for all \(n\le 1000\) and cross-check against the tables (correctness gate).
2. Re-verify Scholz–Brauer for a modest already-covered range, exercising both the exact-value and Brauer-construction paths.
3. Extend the Scholz–Brauer verification (P2) to a fresh \(n\)-interval, certifying each \(\ell(n)\).
4. Attempt a targeted new exact value (P3) at a high-\(\nu(n)\) number where the bound is loose.

**One-workstation scope and failure modes.** Reproducing tables up to moderate \(\ell(n)\) and verifying Scholz–Brauer over a fresh range are feasible on one workstation. Extending the full census one level of \(\ell\) is expensive (tens of millions to billions of numbers) and may exceed a single machine - scope P5 realistically. Dominant risks:

- An unsound pruning rule dropping an optimal chain - guard by re-running flagged \(n\) without the rule and with dual bounding functions.
- Big-integer or validator bugs on \(2^n-1\) - cross-check GMP against Python.
- Reporting a good chain as the exact value - never without the completed length-\((r-1)\) search.

Report unfinished searches as certified upper bounds, not exact values.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Chains are validated in exact integer arithmetic; every exact \(\ell(n)\) carries a complete branch-and-bound optimality log; Scholz–Brauer claims reduce to certified \(\ell\) values or formal lemmas. No floating point in a load-bearing step.
2. **Independent verification.** The chain validator is written separately from the search; a second, independently coded branch-and-bound re-confirms a sample of exact values without the primary pruning; big-integer arithmetic is cross-checked (GMP vs Python).
3. **Reproducibility.** The reduced-graph encoding, pruning and bounding rules, search order, and tool versions are recorded; a SHA-256 manifest covers chains, logs, and census files; the standing verified ranges and tables (Clift/Flammenkamp, OEIS A003313) being extended are cited with source and access date.
4. **Preservation.** The branch-and-bound source, the validator, and the certificates/logs are part of the record; census files too large to store are reduced to hashes with regeneration commands preserved.
5. **Honest reporting.** The report states whether a value is an exact certified \(\ell(n)\) or an upper bound, whether the measure is \(\ell\) or \(\ell^\ast\), and the exact \(n\)-range for any Scholz–Brauer verification; a strict-inequality instance is reported as a refinement, never as a disproof of the (still open) conjecture.
