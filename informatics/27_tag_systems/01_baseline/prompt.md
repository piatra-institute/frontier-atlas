# PROMPT FOR CERTIFIED ANALYSIS OF A SMALL TAG SYSTEM WITH OPEN HALTING BEHAVIOR

## Post's tag system and the Collatz-flavored halting frontier of tiny tag / cyclic-tag systems

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 27 of 50  
**Area:** computation models & automated reasoning  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A **tag system** is one of the simplest computational models: read the first symbol of a word, append a short production word for it, delete the first \(v\) symbols, repeat. Despite this triviality, tag systems sit right on the decidability frontier - 2-tag systems are Turing-universal, and the halting behavior of specific tiny ones is a famous open problem. **Post's tag system** (deletion number \(v=2\), productions \(0\to 00\), \(1\to 1101\)) has had **unknown behavior since ~1921**: it is not known whether every initial word eventually halts (empties or reaches an unread state) or cycles, or whether some word grows forever - a Collatz-like open question that Post, Minsky, and later Wolfram all probed empirically without resolution. This prompt asks for a *certified* advance on a specific small tag system: a proof of eventual periodicity/halting for a structured class of inputs, a certified extended computation (a record trajectory with a machine-checkable trace and an exact non-cycling/non-halting-so-far certificate), or - the windfall - a proved divergent (infinitely growing) trajectory. The verifier is a certified simulator over exact big-integer/word representations plus, where a claim is general, a machine-checked invariant. This is a Collatz-flavored problem: honest calibration is mandatory - full settlement of Post's system is a landmark, and most of the value is in certified partial structure.

## 1. Exact problem statement

A **tag system** \(\mathcal T=(A,v,P)\) has a finite alphabet \(A\), a **deletion number** \(v\ge 1\), and a production function \(P:A\to A^*\). A configuration is a word \(w\in A^*\). One **step** on \(w=a_1a_2\cdots a_\ell\) (with \(\ell\ge v\)) is: read the leading symbol \(a_1\), append \(P(a_1)\), then delete the first \(v\) symbols, giving \(a_{v+1}\cdots a_\ell\,P(a_1)\). The system **halts** on \(w\) if it reaches a word of length \(<v\) (or, in the "reaches a fixed unread symbol" convention, a designated halting symbol); it **cycles** if it revisits a configuration; it **diverges** if the length grows without bound and it never cycles. A **cyclic tag system** is the restricted, deterministic variant used in universality proofs (a fixed cyclic list of append-words, appending or not according to the leading bit, always deleting one symbol).

Formally, the one-step map on \(w=a_1\cdots a_\ell\) (\(\ell\ge v\)) is
\[
\mathsf{step}(w)=a_{v+1}a_{v+2}\cdots a_\ell\,P(a_1),
\]
and the orbit is \(w,\ \mathsf{step}(w),\ \mathsf{step}^2(w),\dots\). Three mutually exclusive fates: **halt** (\(\ell<v\) reached), **cycle** (\(\mathsf{step}^i(w)=\mathsf{step}^j(w)\), \(i<j\)), **diverge** (\(|\mathsf{step}^t(w)|\to\infty\), no repeat).

**Post's tag system.** \(A=\{0,1\}\), \(v=2\), \(P(0)=00\), \(P(1)=1101\). **Open question:** does every initial word halt or cycle, or does some word diverge? Equivalently, is the reachability/halting problem of this fixed system decidable, and what is the answer on all inputs? Post reported all tested words halted or cycled; this remains unproven in general. Because reading \(a_1\) and appending \(P(a_1)\) lengthens by \(|P(a_1)|-v\) per step (\(0\) for a leading \(0\), \(+2\) for a leading \(1\)), the length obeys a data-dependent recurrence that behaves like a Collatz iteration on the block structure.

**In-scope systems.**
1. Post's \((v=2;\ 00,1101)\) system - the flagship.
2. Other small tag systems with \(v=2\) and \(|A|\le 3\) whose halting behavior is unknown or borderline.
3. Small **cyclic** tag systems with open cycle/halt structure.

Size is measured by \((|A|,\,v,\ \sum_a|P(a)|)\).

**Deliverables in scope.**
1. **Certified behavior on an input class.** A proof that every word in a precisely defined, infinite class of initial words halts or cycles (with an explicit bound or invariant), for a fixed small system.
2. **Certified extended computation.** For a specific hard input, a record-length trajectory with a machine-checkable trace and an exact certificate that it has not cycled (a bloom-filter/hash-set replay proof) up to the record - a lower bound on any halting/cycling time.
3. **Certified structural result.** A proved eventual-periodicity theorem, a proved growth/shrink invariant, or a certified reduction of the system's behavior to a stated Collatz-like conjecture.
4. **Divergence (windfall).** A proved infinitely-growing trajectory for a specific input of a small tag system.

## 2. Resolution standard

A result is a resolution only in certified form.

- **Class behavior theorem.** For a fixed small system, a machine-checked theorem "every initial word in class \(C\) halts (resp. cycles) within \(f(|w|)\) steps," where \(C\) is precisely defined and infinite, \(f\) explicit, and the proof is formalized (Coq/Rocq or Lean) or reduced to a checked invariant. Certificate: the formal proof.
- **Extended-computation certificate.** For a specific input, an exact trajectory to step \(N\) with a **certified no-cycle proof** up to \(N\) (a replayable configuration-hash set with a soundness argument) and, if halting, an exact halting time with an independent re-run. Certificate: the trace + a standalone replay + a hash manifest. This certifies a *lower bound* on halting/cycling time, never non-halting.
- **Divergence proof.** A machine-checked proof that a specific input's length grows without bound (a proved self-similar/expanding invariant), settling divergence for that input. Certificate: the formal invariant proof.
A class certificate, formally, is a machine-checked statement
\[
\forall w\in C:\ \exists\,t\le f(|w|)\ \bigl(\mathsf{step}^t(w)\ \text{halts}\ \vee\ \exists\,i<j\le t:\ \mathsf{step}^i(w)=\mathsf{step}^j(w)\bigr),
\]
with \(C\) an explicit infinite class and \(f\) an explicit bound; a divergence certificate is a machine-checked \(\forall t:\ |\mathsf{step}^{t+1}(w)|\ge|\mathsf{step}^{t}(w)|\) with strict growth infinitely often.

- **Named certified form.** One of: a **formally verified halting / non-halting (eventual-periodicity / divergence) proof** for a specified input or class; or an **exhaustive machine-enumeration certificate** classifying all inputs up to a length bound (each halting or cycling, with an explicit witness). A hardness result may take the form of a **certified reduction** to a named Collatz-like conjecture.

**Not accepted as resolution.**
- "Simulated to \(10^{12}\) steps without halting" presented as evidence the input diverges - a long non-halting run is undecided, not a divergence proof.
- A no-cycle claim without a certified configuration-set replay (hash collisions or memory truncation silently miss a cycle).
- A class theorem argued from examples rather than a proved invariant.
- Settling a *different* system (a modified deletion number, altered productions) and presenting it as Post's system.
- A reduction to Collatz offered as *deciding* the system - a reduction is a hardness statement, not a settlement.
- Floating-point or lossy word representations; words must be exact.
- A census claimed complete over length \(\le L\) that silently dropped words exceeding a memory or step budget without flagging them as residual.
- A "record transient" reported without the exact seed and a reproducible run.

## 3. Graded partial-result targets

**P1 - Reproduce the flagship behavior empirically, certified as far as it goes.** Build an exact simulator for Post's system and:
- reproduce the known empirical picture (short words halt or become periodic);
- for a batch of inputs up to length \(L\), produce certified halt/cycle verdicts with explicit witnesses (a cycle is a repeated configuration; a halt is length \(<v\));
- reproduce any published long-transient input to its known length.

*Certificate:* per-input trace + no-cycle/until-cycle replay + hashes. Validates the pipeline.

**P2 - Certified length-bounded census.** Prove that **every** initial word of length \(\le L\) (largest \(L\) you can complete) halts or cycles:
- enumerate all \(2^L\) (or symmetry-reduced) initial words;
- simulate each with certified cycle detection to a verdict;
- record the maximum halting/cycling time and maximum transient length;
- flag any word still unresolved at the step budget as residual.

*Certificate:* exhaustive enumeration with per-word verdict and a replay harness; SHA-256 manifest.

**P3 - Structural invariant on a subclass.** Prove a halting or eventual-periodicity theorem for a precisely defined infinite subclass of inputs, with an explicit bound. Candidate subclasses:
- all-\(0\) words \(0^n\) (the productions keep them in a controlled regime);
- words of a fixed short period repeated;
- words whose \(1\)-density stays below a threshold under iteration.

*Certificate:* a machine-checked invariant proof establishing halting/cycling within an explicit \(f(|w|)\).

**P4 - Record extended computation.** For the hardest small input(s) found in P1–P2, push the certified trajectory to a new record:
- run the run-length-encoded simulator far beyond the previous record;
- maintain the exact visited-configuration store so the no-cycle property stays certified;
- report the maximum transient length reached and the step count, a lower bound on any halting/cycling time.

*Certificate:* the trace, a standalone replay of the no-cycle property, and a citation of the prior record with source and access date.

**P5 - Certified hardness reduction.** Reduce the halting behavior of a fixed small tag system (or a natural subclass of Post's) to a precisely stated Collatz-like conjecture:
- encode the block dynamics as an integer map \(g\) and identify halting with an orbit condition of \(g\);
- machine-check the equivalence of the two halting conditions;
- name the resulting number-theoretic conjecture explicitly so direct-decision attempts can be retired.

*Certificate:* the formal reduction and the named target conjecture.

**P6 - Divergence or full settlement (windfall).** A proved divergent trajectory for a specific input, or a proof that every input of a fixed small system halts/cycles. *Certificate:* the formal proof; explicit statement of which was established.

## 4. Known results and prior art

**This area moved a lot recently - web-verify every attribution below before a session.**

- **Post (~1921)** - introduced tag systems; posed the halting behavior of the \(v=2\), \(00\,/\,1101\) system; reported empirically that tested words halt or become periodic. Behavior remains **open**. (verify)
- **Minsky, Cocke–Minsky (~1960s)** - 2-tag systems are Turing-universal (used in the universality of small Turing machines); tested Post's system further without settling it. (verify)
- **Wolfram (2021 essay, "After 100 Years, Can We Finally Crack Post's Problem of Tag?")** - extensive computational study; frames it as a case of computational irreducibility; reports very long transients for some inputs and unresolved status. (verify)
- **De Mol** - work on the boundaries of solvability/unsolvability in small tag systems and their relation to Collatz-like functions (arXiv 0906.3329 and related, ~2009); "Tag systems and Collatz-like functions." (verify)
- **Infinitely-growing configurations** - recent constructive work on inputs to Post's tag system that (conjecturally or provably in restricted senses) grow (arXiv 2105.07529, ~2021). (verify exact claim)
- **Universality boundaries** - 2-symbol tag systems / cyclic tag systems shown universal via cyclic-tag simulation; note the delicate line between the *universal* general family and *specific fixed* systems whose behavior is a Collatz-like open problem. (verify)
- **Deletion number vs universality** - 2-tag systems (\(v=2\)) are already universal (Cocke–Minsky), which is *why* the halting of a *specific* \(v=2\) system can be as hard as a Collatz problem; the general decision problem for \(v=2\) tag systems is undecidable. (verify)
- **Empirical record** - long transients for specific Post-system inputs are catalogued (Wolfram's study, De Mol); re-confirm the current record transient length and the largest \(L\) for which a full length-\(\le L\) census exists. (verify)

Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session. Confirm the current record transient/length for Post's system and the status of any claimed divergent input.

## 5. Attack plan

`[search]`, proof-heavy on the invariant side. One workstation suffices; the constraint is memory for cycle detection at scale.

1. **Exact simulator.** Implement Post's system (and small variants) over exact word representations with efficient leading-symbol read and tail append (deque / rope / run-length encoding of long \(0\)-blocks, since \(0\to00\) breeds runs). Big-integer counters for step counts.
2. **Certified cycle detection.** Combine Floyd/Brent cycle detection with an exact configuration store:
   - a claimed no-cycle must be backed by a **replayable** set of visited canonical configurations, not a lossy Bloom filter;
   - a cycle verdict emits the exact repeated configuration and the two step indices;
   - a halt verdict emits the terminal short word;
   - for very long orbits, use a disk-backed exact store and prove the store lossless.
3. **Census (P2).** Enumerate all words up to length \(L\); simulate each with cycle detection; record verdicts, halting/cycling times, and max transient length; hash everything.
4. **Structure mining (P3).** Look for conserved quantities and periodic "skeletons":
   - track the run-length dynamics of \(0\)-blocks under \(0\to00\) versus the \(1\to1101\) injections;
   - measure \(1\)-density, block-count, and other functionals along orbits;
   - convert any robust pattern into a candidate invariant and formalize it (Coq/Rocq or Lean);
   - immediately assign a counterexample search to any conjectured invariant before investing in a proof.
5. **Record runs (P4) and reductions (P5).** Push hard inputs with the run-length simulator; encode the block dynamics as a Collatz-like map and, if it matches a named conjecture, machine-check the reduction.

**Failure modes.** (a) Long-run-as-proof - the cardinal error; a non-halting run of any length is undecided. (b) Lossy cycle detection - a hash filter without exact backing can miss a cycle and falsely suggest divergence. (c) Memory blow-up - configurations can grow large; run-length encoding and disk-backed hash sets are needed, with the no-cycle replay kept sound. (d) Wrong system - a transcription error in the productions studies a different system. (e) Reduction-as-decision - a Collatz reduction is hardness, not settlement. (f) Cherry-picked class - a "class theorem" must have a proved invariant, not selected examples.

## 6. Verification and auditability requirements

1. **Exact or certified computation:** words and step counts are exact (no floating point, no lossy encoding); every halt/cycle verdict carries an explicit witness; every no-cycle claim carries a replayable exact configuration set; every general theorem is a machine-checked invariant with the axiom set printed.
2. **Independent verification:** every artifact re-checked apart from the search that produced it:
   - trajectories re-run by a separate simulator (ideally a different word representation);
   - cycle/no-cycle certificates re-checked by a standalone replay over the visited-configuration store;
   - class-theorem and divergence proofs checked by a proof-assistant kernel with the axiom set printed;
   - record lengths reproduced from the stored seed.
3. **Reproducibility:** system definition (productions, deletion number, halting convention), encodings, length bounds, and versions recorded; SHA-256 manifest over census, traces, and certificates; any record transient/length cited with source and access date.
4. **Preservation:** simulator, cycle-detection/replay code, census generator, and any formal proofs are part of the record; anything not preserved is stated explicitly.
5. **Honest reporting:** state up front whether a *certified structural result* (a proved class theorem, eventual periodicity, or divergence) was obtained or only a *certified extended computation / census* (which bounds halting/cycling time but proves nothing about the general open question). A long non-halting run is never reported as divergence, and a Collatz reduction is reported as hardness, not a solution. This is a Collatz-flavored open problem - certified partial structure is the expected product.
