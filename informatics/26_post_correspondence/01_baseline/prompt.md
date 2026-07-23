# PROMPT FOR SETTLING THE DECIDABILITY OF SMALL POST CORRESPONDENCE PROBLEMS

## Where does PCP(n) cross from decidable to undecidable? The n = 3, 4 frontier

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 26 of 50  
**Area:** computation models & automated reasoning  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Post Correspondence Problem asks, given a finite list of \(n\) pairs of strings, whether some nonempty sequence of indices makes the two concatenations equal. The general problem is undecidable, and the sharp question is **how few pairs suffice** for undecidability. The frontier is now narrow: **PCP(2) is decidable** (Ehrenfeucht–Karhumäki–Rozenberg, 1982); **PCP(5) is undecidable** (Neary, 2015, improving the PCP(7) bound of Matiyasevich–Sénizergues, 2005). The decidability of **PCP(3) and PCP(4) is open** - a genuine, crisp decidability frontier. This is matched to certified search in two directions at once: for a *decidability* result, one seeks a proved-total decision procedure for all \(n\)-pair instances (or a structural classification of the \(n=3\) instance space); for the *undecidability* side, one seeks a smaller undecidable construction (e.g. pushing below 5) via a certified reduction from a known-undecidable system (binary tag systems, small Turing machines). Even short of settling \(n=3\), the boundary can be mapped: exhaustively analyze small instances (bounded alphabet, bounded string length) and certify each as solvable, unsolvable, or reduced to a canonical hard core. This is a decidability-frontier problem: honest calibration is mandatory - settling PCP(3) is a landmark, not a routine session.

## 1. Exact problem statement

An **instance** of PCP is a finite list of pairs \((u_1,v_1),\dots,(u_n,v_n)\) with \(u_i,v_i\in\Sigma^*\) over a finite alphabet \(\Sigma\). A **solution** is a finite sequence \(i_1,\dots,i_k\) with \(k\ge 1\) and \(1\le i_j\le n\) such that
\[
u_{i_1}u_{i_2}\cdots u_{i_k}\ =\ v_{i_1}v_{i_2}\cdots v_{i_k}.
\]
The instance is **solvable** if a solution exists. **PCP(n)** is the decision problem restricted to instances with exactly \(n\) pairs (any alphabet size; the interesting reductions use \(|\Sigma|=2\)). We measure the frontier by \(n\) (number of pairs); a secondary measure is the **width** \(\max_i(|u_i|+|v_i|)\), used to bound exhaustive instance families.

**Configuration search.** A partial match reads left to right; after using indices \(i_1\dots i_j\) one side is a prefix of the other, and the outstanding **difference** \(\Delta_j\) (the unmatched suffix, tagged by which side is ahead) is the only state that matters. A solution is a path from the empty difference back to the empty difference through a nonempty index sequence:
\[
\varepsilon \xrightarrow{\,i_1\,}\Delta_1\xrightarrow{\,i_2\,}\cdots\xrightarrow{\,i_k\,}\varepsilon,\qquad
\Delta_{j}\in(\{L,R\}\times\Sigma^*)\cup\{\varepsilon\}.
\]
The difference set may be infinite; decidability of PCP(n) is exactly the question of whether reachability of \(\varepsilon\) in this (possibly infinite) transition system is decidable for all \(n\)-pair instances.

**Known frontier.** PCP(1) trivially decidable; **PCP(2) decidable** (EKR 1982, via a structural analysis of 2-rule instances); **PCP(5), PCP(6), PCP(7), \(\dots\) undecidable** (Neary 2015 for 5; earlier Matiyasevich–Sénizergues for 7). **PCP(3) and PCP(4): open.**

**The questions.**
1. **Decidability of PCP(3)** (and PCP(4)): is there a total algorithm deciding solvability of every 3-pair (resp. 4-pair) instance? A positive answer is a decision procedure with a correctness proof; a negative answer is a certified undecidability reduction into \(n=3\) (resp. 4).
2. **Boundary mapping.** For bounded families (fixed alphabet, bounded width), classify every instance as solvable (exhibit a solution), unsolvable (certify no solution), or reduced to a canonical residual core; produce a certified census.
3. **Sharpening the undecidable side.** Any certified undecidable construction with \(n<5\) settles PCP(4) (and, if \(n=3\), PCP(3)) negatively.

Note the distinction from the **bounded PCP** (does a solution of length \(\le \ell\) exist?), which is NP-complete and is a *tool* here, not the target: the target is the *unbounded* solvability of fixed-\(n\) instances.

## 2. Resolution standard

A result resolves the frontier only in certified form.

- **Decidability of PCP(n).** A total decision procedure \(A_n\) taking any \(n\)-pair instance to solvable/unsolvable, with a **proof of totality and correctness** (formalized in Coq/Rocq or Lean, or a rigorously checked structural classification of the \(n\)-pair instance space). For \(n=3\) this is a headline result; the certificate is the formal proof, plus agreement with an independent solver on a large instance census.
- **Undecidability of PCP(n) for n < 5.** A **certified reduction** from a known-undecidable problem (binary tag systems à la Neary; small Turing-machine halting; a semi-Thue word problem) producing, for each source instance, an \(n\)-pair PCP instance that is solvable iff the source halts/accepts - with a machine-checked proof of the reduction's correctness. The certificate is the formal reduction proof.
A certified reduction, formally, exhibits a computable \(R\) from instances \(x\) of an undecidable source problem \(\mathcal P\) to \(n\)-pair PCP instances with a machine-checked equivalence
\[
\forall x:\quad x\in \mathcal P\ \Longleftrightarrow\ R(x)\ \text{is solvable},
\]
which transports undecidability of \(\mathcal P\) to PCP(n).

- **Named certified form.** Either a **formally verified decision procedure** (total, correct) for all \(n\)-pair instances, or a **certified undecidability construction** (a machine-checked reduction) lowering the undecidable frontier. A boundary-map deliverable is an **exhaustive machine-enumeration certificate** classifying a bounded instance family, each verdict independently checkable.

**Not accepted as resolution.**
- A solver that decides "most" 3-pair instances but is not proved total (it may loop forever on some instance - precisely the open case).
- An empirical claim ("all tested 3-pair instances were decided") presented as decidability of PCP(3).
- An undecidability reduction whose correctness (the solvable-iff-halts equivalence) is only argued informally.
- Using **bounded** PCP (NP-complete) results as if they settled unbounded solvability.
- A single hard instance offered as evidence of undecidability without a reduction covering an undecidable source class.
- Convention drift on what "PCP(n)" counts (marked PCP, one-sided variants, \(\omega\)-PCP) without stating it.
- A census claimed exhaustive whose symmetry quotient is buggy, so some instances are silently omitted.
- A transducer-emptiness verdict with no replayable invariant behind it.

## 3. Graded partial-result targets

**P1 - Reproduce both anchors.** Independently verify both ends of the frontier:
- implement and certify the EKR structural decision procedure and run it on a census of 2-pair instances;
- reproduce Neary's PCP(5) reduction on sample binary-tag-system inputs and check the solvable-iff-halts correspondence on finite prefixes.

*Certificate:* a checked EKR procedure with a census; a re-derived 5-pair instance from a sample undecidable source with a verified correspondence. Validates the pipeline and both directions.

**P2 - Certified bounded-width census of PCP(3).** For 3-pair instances over \(|\Sigma|=2\) up to a width bound \(W\), classify every instance as solvable (exhibit a solution), unsolvable (certify), or *residual* (undecided by current methods):
- enumerate instances up to the symmetry group - swap of the two morphisms, index permutation, alphabet renaming, and reversal;
- run the semi-decider and the unsolvability battery on each;
- collect the residual undecided core and hash it.

*Certificate:* canonical enumeration, per-instance verdict with an independent checker, and a residual list with hashes.

**P3 - Shrink the residual core.** Develop and certify new unsolvability criteria that dispose of residual 3-pair instances, driving the undecided core toward a structured family:
- length/Parikh-vector linear invariants over exact rationals;
- automaton-based reachability obstructions with replayable certificates;
- periodicity / pumping arguments on the difference dynamics.

*Certificate:* each criterion proved sound; each newly-decided instance carries its certificate; the shrunken residual core is re-hashed.

**P4 - Structural classification of a PCP(3) subfamily.** Prove decidability for a natural, exhaustively-defined subclass of 3-pair instances by a total decision procedure with a correctness proof. Candidate subclasses:
- all instances where one pair is length-balanced (\(|u_i|=|v_i|\));
- a fixed length profile \((|u_i|,|v_i|)_i\);
- instances whose difference dynamics are eventually periodic.

*Certificate:* the formal proof plus agreement with the P2 census on the subclass.

**P5 - Sharpen the undecidable side.** Attempt a certified undecidable construction at \(n=4\) (settling PCP(4) negatively), or an improved reduction that lowers width/alphabet at \(n=5\):
- start from Neary's binary-tag-system encoding and compress the pair count;
- machine-check the solvable-iff-halts equivalence on the compressed reduction;
- confirm no pair was silently merged in a way that changes solvability.

*Certificate:* a machine-checked reduction with the solvable-iff-halts equivalence; cite the record improved with source and access date.

**P6 - Full settlement of PCP(3) (windfall).** A proved decision procedure for all 3-pair instances, or a certified undecidability reduction into 3 pairs. Either direction is a landmark: a decision procedure ends the residual core entirely, while a reduction into 3 pairs would collapse the open frontier to \(\{2\ \text{decidable},\ 3\ \text{undecidable}\}\). *Certificate:* the formal proof; independent replay on a large census; explicit statement of which direction was established.

## 4. Known results and prior art

**This area moved a lot recently - web-verify every attribution below before a session.**

- **PCP(2) decidable** - Ehrenfeucht, Karhumäki, Rozenberg (~1982), via a structural analysis of 2-rule instances. (verify)
- **PCP(7) undecidable** - Matiyasevich, Sénizergues (~2005), through 3-rule semi-Thue systems. (verify)
- **PCP(5) undecidable** - Neary (STACS 2015), "Undecidability in binary tag systems and the Post correspondence problem for five pairs of words"; the current smallest **proved-undecidable** value. (verify)
- **PCP(4) reduction line** - Neary's earlier "…for four pairs of words" (arXiv 1312.6700, ~2013/2015) tightens the *binary tag system* undecidability and is the natural launch point for attacking PCP(4). (verify exact claim: confirm whether 4 pairs is proved undecidable or remains the open target - sources conflict; re-check.)
- **PCP(3), PCP(4) open** - the decidability of 3-pair (and, pending the above verification, 4-pair) instances is unresolved; this is the frontier. (verify current status)
- **Infinite / two-sided variants** - the \(\omega\)-PCP and marked-PCP variants have their own smaller undecidable bounds (e.g. undecidability of the infinite PCP for small domain sizes); keep these distinct from the finite one-sided PCP(n). (verify)
- **Formalization** - recent certified-programs work formalizes PCP reductions (Coq Library of Undecidability Proofs entries; CPP-venue proof-generation for PCP, ~2025). (verify)
- **Bounded PCP** - deciding whether a solution of length \(\le\ell\) exists is NP-complete; it is a *tool* for the solvable side and for width-bounded exhaustion, not a statement about the fixed-\(n\) frontier. (verify)
- **Semi-Thue lineage** - the undecidable-source chain is halting/Turing machines \(\to\) semi-Thue systems with few rules \(\to\) binary tag systems \(\to\) PCP; each hop costs a few pairs, which is why lowering the pair count is a reduction-engineering problem. (verify)

Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session. **In particular, re-confirm the exact status of PCP(4): whether Neary's four-pair result establishes undecidability at 4 or only tightens the tag-system side, since this determines whether the open frontier is \{3\} or \{3,4\}.**

## 5. Attack plan

`[search]`, but the decidability direction is proof-heavy. One workstation suffices for census and solver work.

1. **Solver core.** Build the two engines:
   - a sound PCP **semi-decider** - BFS/DFS over the configuration difference with dominance pruning, length-difference bounds, and prefix-compatibility filtering; termination only on found solution or provable dead-end;
   - a **bounded**-PCP SAT/ILP encoding (CaDiCaL/kissat with DRAT logging) to find solutions up to a length bound and to certify their absence up to that bound.

   A found solution is a definitive *solvable* certificate; a DRAT bounded-absence proof is *not* an unsolvability proof (longer solutions may exist).
2. **Unsolvability certificates.** Implement proved-sound methods, each emitting a replayable certificate:
   - **transducer emptiness** - represent reachable differences as a finite automaton (when the difference set is regular) and certify the equal-state is unreachable;
   - **linear invariants** - a letter-count or length functional \(\lambda\) with \(\lambda(u_i)=\lambda(v_i)\) impossible to balance (exact rational arithmetic);
   - **prefix/suffix incompatibility** - no pair can start (or end) a match;
   - **DRAT-checked bounded exhaustion** - for width-bounded instances, SAT-certify no solution up to the relevant length.
3. **Canonical census (P2).** Enumerate 3-pair instances up to the symmetry group and width bound; classify each with the tools above; collect the residual undecided core. The quotient must account for:
   - swapping the two morphisms (\(u\leftrightarrow v\)) and reversing all words;
   - permuting the three indices and renaming alphabet symbols;
   - removing dominated or trivially-unsolvable instances early.
4. **Structural theory (P3/P4).** Mine the residual core for structure; prove decidability lemmas for subfamilies and formalize them (Coq/Rocq or Lean, reusing the Coq Library of Undecidability Proofs where possible). This is the road to P6.
5. **Undecidable side (P5).** Re-implement Neary's tag-system→PCP reduction, then attempt to compress it to 4 pairs (or tighten width/alphabet), formalizing the solvable-iff-halts equivalence.

**Failure modes.** (a) Semi-decider mistaken for decider - a search that finds solutions cannot prove *un*solvability; the open case is exactly non-termination. (b) Bounded-PCP confusion - NP-completeness of bounded PCP says nothing about the unbounded fixed-\(n\) frontier. (c) Uncertified transducer emptiness - always emit a replayable invariant. (d) Symmetry-quotient bugs - a census with a canonicity error is not exhaustive. (e) Undecidable wall - PCP(3) may itself be undecidable *and* hard to reduce into; recognize when a subfamily result is the realistic product. (f) Status drift - the 4-pair literature is easy to misread; verify before claiming the frontier.

## 6. Verification and auditability requirements

1. **Exact or certified computation:** every *solvable* verdict carries an explicit solution (a checkable index sequence); every *unsolvable* verdict carries a proved-sound certificate (transducer-emptiness invariant, exact linear invariant, or DRAT-checked bounded-exhaustion where applicable); every decidability claim is a proved-total procedure. Empirical timeouts are exploration only.
2. **Independent verification:** every artifact re-checked apart from the search that produced it:
   - solutions re-checked by a trivial standalone concatenation-equality checker;
   - transducer-emptiness and linear invariants re-validated by a separate replay;
   - DRAT bounded-exhaustion certificates run through an independent DRAT checker;
   - decision-procedure proofs checked by a proof-assistant kernel with the axiom set printed.
3. **Reproducibility:** alphabet, width bounds, symmetry-quotient conventions, solver and enumerator versions recorded; SHA-256 manifest over the instance census, verdicts, and certificates; the PCP(2)/PCP(5) anchors and any improved bound cited with source and access date.
4. **Preservation:** semi-decider, invariant checkers, census generator, and any formal proofs are part of the record; anything not preserved is stated explicitly.
5. **Honest reporting:** state up front whether a *decision procedure* (total, proved) or only a *semi-decider census* was produced, whether the undecidable frontier was lowered and in which model, and the exact size of any residual undecided core. This is a decidability frontier - a partial census with a shrinking hard core is the expected, respectable product; a semi-decider is never reported as settling PCP(3).
