# PROMPT FOR EXACT STATE COMPLEXITY AND MAGIC-NUMBER RESOLUTION

## Tight state bounds for automaton operations, and which sizes an n-state NFA can determinize to

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 29 of 50  
**Area:** computation models & automated reasoning  
**Modes:** `[search]` `[enum]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The **state complexity** of an operation on regular languages is the exact number of DFA states, in the worst case, needed for the result when the inputs are given by \(n\)-state machines. These are crisp integers with machine-checkable ground truth: an upper bound is a construction, a lower bound is a witness language whose minimal DFA is provably that large, and *tightness* means the two meet. Two families remain partly open. First, the **exact state complexity** of specific operations (reversal, Kleene star, intersection, concatenation, and their compositions) over **fixed small alphabets** - for many operations the general bound needs a large or growing alphabet, and the tight value over a binary or ternary alphabet is unknown. Second, the **magic-number problem**: determinizing an \(n\)-state NFA yields a DFA of some size in \([1,2^n]\); a value \(d\) is **magic** for \(n\) if **no** \(n\)-state NFA has a minimal equivalent DFA of exactly \(d\) states. Over a growing alphabet no value is magic; over the **unary** alphabet magic numbers exist; over **binary/ternary** alphabets the pattern is only partly known. This prompt asks for a certified exact state-complexity value for a specific operation-and-alphabet, or the resolution of magic-number gaps for a specific \((n,\text{alphabet})\), via **exhaustive isomorph-free automata enumeration** with independently-checkable witnesses. A construction without a matching lower bound, or a bound from an unreplayable search, is a partial result.

## 1. Exact problem statement

A **DFA** is \((Q,\Sigma,\delta,q_0,F)\) with total \(\delta:Q\times\Sigma\to Q\); an **NFA** allows \(\delta:Q\times\Sigma\to 2^Q\) (and possibly a set of initial states). The **state complexity** \(\mathrm{sc}(L)\) of a regular language is the number of states of its **minimal** DFA. For a unary operation \(\circ\) (e.g. reversal, star) define
\[
\mathrm{sc}_\circ(n)=\max\{\,\mathrm{sc}(\circ L): \mathrm{sc}(L)\le n\,\},
\]
and analogously \(\mathrm{sc}_\circ(m,n)\) for binary operations (intersection, union, concatenation) with the two arguments' state complexities bounded by \(m,n\). All maxima are over a **fixed alphabet** \(\Sigma\); the alphabet size is part of the problem and can change the answer.

**Known general tight bounds (alphabet-generous).** reversal \(2^n\); Kleene star \(\tfrac34 2^n\); intersection \(mn\); union \(mn\); concatenation \((m-1)2^n + 2^{n-1}\) (up to standard corrections). Witnesses for several of these need alphabet size growing with \(n\); the **fixed-small-alphabet** tight values are the open part.

By the Myhill–Nerode theorem, \(\mathrm{sc}(L)\) equals the number of equivalence classes of the right-congruence \(x\sim_L y\iff(\forall z:\ xz\in L\Leftrightarrow yz\in L)\); a set of \(V\) pairwise-inequivalent words (a **distinguishing family**) certifies \(\mathrm{sc}(L)\ge V\).

**Magic numbers.** For an \(n\)-state NFA \(N\), \(\mathrm{sc}(L(N))\in[1,2^n]\) after subset construction + minimization. Define the attainable set and the magic set for \((n,\Sigma)\):
\[
A(n,\Sigma)=\{\,\mathrm{sc}(L(N)) : N\ \text{an}\ n\text{-state NFA over}\ \Sigma\,\},\qquad \mathrm{Magic}(n,\Sigma)=[n,2^n]\setminus A(n,\Sigma).
\]
Over an alphabet growing with \(n\), \(\mathrm{Magic}=\varnothing\) (the whole range is attainable); over **unary** \(\Sigma\), \(\mathrm{Magic}\neq\varnothing\) (gaps exist); over **binary** \(\Sigma\), a large initial range is non-magic but the full pattern (which \(d\) near \(2^n\), and for which \(n\)) is **open**. The task: for a specific \((n,\Sigma)\), determine \(A(n,\Sigma)\) and \(\mathrm{Magic}(n,\Sigma)\) with certificates.

**Deliverables in scope.**
1. A certified exact \(\mathrm{sc}_\circ\) value for a specific operation over a specific fixed alphabet, at a specific \(n\) (or for all \(n\), if a matching-bound proof is found).
2. A certified resolution of magic-number attainability for a specific \((n,\Sigma)\): the full attainable set with per-value witnesses and a proof of magicness for the rest.
3. A certified new witness family improving a fixed-alphabet lower bound toward the general bound.

## 2. Resolution standard

A result resolves a case only in certified form.

- **Exact operation value.** For fixed \(\circ,\Sigma,n\) (and \(m\)), a value \(V=\mathrm{sc}_\circ(n)\) with **(a)** an upper-bound proof (a construction giving \(\le V\) states for every input in range, with a correctness proof), and **(b)** a matching **witness**: explicit input DFA(s) whose \(\circ\)-image has minimal DFA of exactly \(V\) states - the minimality **certified** (a proved distinguishing set / Myhill–Nerode witness, machine-checkable). For an all-\(n\) claim, a proved witness family plus a matching upper bound.
- **Magic-number resolution.** For fixed \((n,\Sigma)\), the complete attainable set \(A\subseteq[n,2^n]\): each \(d\in A\) has an explicit \(n\)-state NFA witness with certified minimal-DFA size \(d\); each \(d\notin A\) (magic) has a proof of non-attainability - via **exhaustive isomorph-free enumeration** of all \(n\)-state NFAs over \(\Sigma\) (up to state permutation) with the minimal-DFA size computed for each, or via a structural impossibility proof.
A certified lower bound \(\mathrm{sc}(L)\ge V\) is a distinguishing family \(\{w_1,\dots,w_V\}\) with an explicit separator for each pair:
\[
\forall\,i<j\ \exists\,z_{ij}:\quad w_i z_{ij}\in L\ \not\Leftrightarrow\ w_j z_{ij}\in L,
\]
each membership decided by running the (small) recognizer - a trivially replayable certificate.

- **Named certified form.** An **exhaustive machine-enumeration certificate** (canonical, isomorph-free, replayable) over the relevant automaton class, together with, for each headline value, a **certified minimality witness** (a checked Myhill–Nerode distinguishing family). Upper-bound constructions carry a machine-checked correctness proof.

**Not accepted as resolution.**
- A construction (upper bound) with **no matching lower-bound witness** - that is half the answer.
- A witness whose minimal-DFA size is only computed by an unverified minimizer - minimality must be certified (distinguishing set) or cross-checked by an independent minimizer.
- A magicness claim from a search whose completeness (isomorph-freeness, coverage) is asserted but not certified.
- A tight value proved over a **large/growing** alphabet presented as the **fixed-small-alphabet** answer (or vice versa) - the alphabet is part of the statement.
- Silent model drift (partial vs total DFA, single vs multiple initial NFA states, incomplete DFAs) that changes the count.
- A single attainable value offered as "resolving" the magic-number pattern for \((n,\Sigma)\).
- An enumeration whose state-permutation quotient is buggy, so some NFAs are missed and \(A(n,\Sigma)\) is incomplete.
- A tight value proved only up to a floating-point/heuristic minimizer with no distinguishing-family certificate.

## 3. Graded partial-result targets

**P1 - Reproduce known tight bounds with certified witnesses.** For reversal (\(2^n\)), star (\(\tfrac34 2^n\)), intersection (\(mn\)), and concatenation over their standard alphabets:
- reproduce the tight values at small \(n\);
- for each, extract a **certified** minimality witness (a checked distinguishing family), not just a minimizer's state count;
- cross-check the count with a second minimizer.

*Certificate:* per-value witness + independent minimality check. Validates the pipeline.

**P2 - Certified magic-number census for small \((n,\Sigma)\).** For fixed small \(n\) and \(|\Sigma|\in\{1,2\}\):
- exhaustively enumerate \(n\)-state NFAs up to state-permutation (and symbol renaming);
- compute each minimal-DFA size via subset construction + minimization;
- output the complete attainable set \(A(n,\Sigma)\) and the magic set;
- attach a witness NFA and distinguishing family to every attained value.

*Certificate:* canonical-generation code, the attainable/magic partition with per-value witnesses, and a replay harness; SHA-256 manifest over the enumeration.

**P3 - Exact fixed-alphabet operation value at a specific \(n\).** For an operation whose fixed-small-alphabet tight value is open:
- exhaustively (or SAT-guided-then-certified) search input DFAs maximizing the output's minimal-DFA size at a specific \(n\);
- certify the witness's minimal-DFA size with a distinguishing family;
- prove the matching upper bound by a construction-correctness argument.

*Certificate:* certified witness + upper-bound proof at that \(n\).

**P4 - New fixed-alphabet witness family.** Improve a fixed-small-alphabet lower bound for a specific operation toward the general bound, with a proved witness family (all \(n\)):
- define a parametric input family over the fixed alphabet;
- prove its \(\circ\)-image has minimal DFA of the claimed size for all \(n\) (a uniform distinguishing family);
- confirm the small-\(n\) instances against the exhaustive data.

*Certificate:* a family definition with a certified minimality argument and a citation of the improved bound with source and access date.

**P5 - Magic-number gap resolution for a specific alphabet.** For a specific \(\Sigma\) (e.g. binary), settle whether a specific range of \(d\) values near \(2^n\) is magic:
- push the exhaustive census to a new \(n\) (with canonical reduction and pruning), or
- give a structural attainability proof (a parametric NFA family realizing each \(d\) in the range), or
- give a non-attainability (magicness) proof for the range.

*Certificate:* enumeration or structural proof, with an explicit witness NFA for every attainable value in the range.

**P6 - Matching-bound theorem (windfall).** A tight state-complexity theorem for an operation over a fixed small alphabet for all \(n\): a construction (upper bound) and a matching proved witness family (lower bound), formalized where feasible. This closes the operation-over-alphabet question outright rather than at a single \(n\). *Certificate:* both halves; a machine-checked proof of the witness family's minimality and the construction's correctness.

## 4. Known results and prior art

**This area moved a lot recently - web-verify every attribution below before a session.**

- **Classical tight bounds** - reversal \(2^n\), star \(\tfrac34 2^n\), intersection/union \(mn\), concatenation \((m-1)2^n+2^{n-1}\) (Yu, Zhuang, Salomaa ~1994 and successors); many witnesses use growing alphabets, leaving the fixed-alphabet value open. (verify)
- **Fixed-alphabet questions** - for several operations the tight value over a **binary** alphabet is open or was resolved only recently; Kleene closure over binary is attainable up to \(\tfrac34 2^n\) (no magic numbers up to \(n\approx 9\), by exhaustive check). (verify)
- **Magic numbers** - Iwama, Kambayashi, Takaki posed the question; Geffert and others showed magic numbers **exist for unary** automata (the DFA state hierarchy has gaps); over **growing** alphabets **no** magic numbers exist; the **binary** case is only partly settled - a large initial range is non-magic, the top of \([n,2^n]\) is open. (verify)
- **Subset-construction analyses** - recent work re-analyzes the subset construction and reachable-DFA sizes ("A Close Analysis of the Subset Construction", arXiv 2407.09891, ~2024; "Deconstructing Subset Construction", ~2025). (verify)
- **NFA-to-DFA trade-off** - operational complexity of the NFA→DFA blow-up and hardness of computing NFA state complexity (PSPACE-hardness) frame the search cost. (verify)
- **Enumeration tooling** - exact minimal-DFA computation (Hopcroft/Brzozowski), canonical NFA generation up to state permutation, and automata libraries are the standard instruments. (verify)
- **Combined / compositional operations** - the state complexity of compositions (star-of-union, reversal-of-concatenation, …) is a rich open area where fixed-alphabet tight values are frequently unknown; these are good exhaustive-search targets. (verify)
- **Unary case** - for unary languages the tight bounds and the magic-number gaps involve Landau's function and cyclic structure; the unary magic-number existence result (Geffert) is the cleanest confirmed gap. (verify)

Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session. Fixed-alphabet tight values and binary magic-number ranges are exactly the entries most likely to have shifted.

## 5. Attack plan

`[enum]` + `[search]`. One workstation suffices for small \(n\); the NFA count over binary grows fast, so canonical reduction is essential.

1. **Certified minimality core.** Implement two independent DFA minimizers (Hopcroft and Brzozowski) and a **distinguishing-set** extractor that outputs a Myhill–Nerode witness (pairs of strings separating each state pair); minimality is certified when the witness set has the right size and every pair is checkably separated. This underlies every lower bound.
2. **Canonical NFA/DFA generation.** Generate \(n\)-state NFAs (and input DFAs for operation witnesses) up to state permutation and alphabet-symbol renaming:
   - use orderly generation (nauty/Traces for the symmetry quotient) and dedupe by canonical form;
   - restrict to connected, initially-reachable automata to prune trivially-equivalent ones;
   - track exact counts so exhaustiveness is auditable.
3. **Magic-number census (P2/P5).** For each canonical \(n\)-state NFA over \(\Sigma\):
   - run subset construction + minimization and record the minimal-DFA size;
   - accumulate the attainable set \(A(n,\Sigma)\);
   - the complement in \([n,2^n]\) is \(\mathrm{Magic}(n,\Sigma)\), certified by the exhaustiveness of the enumeration;
   - for each attained \(d\), keep one explicit witness NFA plus its distinguishing family.
4. **Operation values (P3/P4).** For a fixed operation and alphabet:
   - search input DFAs (exhaustively at small \(n\), SAT-guided-then-certified at larger \(n\)) maximizing the output's minimal-DFA size;
   - certify each candidate maximum with a distinguishing family;
   - prove the upper bound by a construction-correctness argument (formalize in Coq/Rocq or Lean where feasible).
5. **Scaling.** Push past pure enumeration where the class is too large:
   - use SAT/ILP (CaDiCaL/kissat with DRAT) to *search* for an NFA whose minimal DFA has a target size \(d\);
   - certify the found witness independently (distinguishing family) - the certificate, not the solver run, is the result;
   - for magicness of a specific \(d\), a certified UNSAT (no \(n\)-state NFA yields minimal size \(d\)) is required, with a DRAT proof.

**Failure modes.** (a) Construction-only - reporting an upper bound as the answer. (b) Uncertified minimizer trust - a minimizer bug silently changes a count; always cross-check and extract a distinguishing set. (c) Enumeration blow-up - binary \(n\)-state NFAs explode; canonical reduction and pruning are mandatory, and coverage must be certified, not assumed. (d) Alphabet drift - the single most common error; the tight value depends on \(|\Sigma|\). (e) Model drift - partial vs total DFA, initial-state conventions, \(\varepsilon\)-moves. (f) Unreplayable SAT - always log proofs.

## 6. Verification and auditability requirements

1. **Exact or certified computation:** every lower bound carries a certified minimality witness (a checked distinguishing set) or an isomorph-free exhaustive census; every upper bound carries a construction-correctness proof; every magicness claim rests on certified exhaustiveness; minimizer output alone is exploration.
2. **Independent verification:** every headline number cross-checked:
   - two independent minimizers (Hopcroft and Brzozowski) agree on every reported size;
   - distinguishing families re-validated by a standalone separator checker;
   - the enumeration re-counted by a separate canonical generator;
   - SAT/ILP witnesses re-checked apart from the solver, with DRAT for any unsatisfiability.
3. **Reproducibility:** operation, alphabet, \(n\) (and \(m\)), DFA/NFA conventions (total/partial, initial states, \(\varepsilon\)-moves), canonical-form and minimizer versions recorded; SHA-256 manifest over enumerations, witnesses, and certificates; the exact per-\(n\) automaton counts published; any improved bound cited with source and access date.
4. **Preservation:** generation, minimization, distinguishing-set, and search source are part of the record; anything not preserved is stated explicitly.
5. **Honest reporting:** state up front the alphabet and \(n\), whether **both** a construction and a matching certified witness were obtained (a construction alone is labeled a one-sided bound), and - for magic numbers - whether exhaustiveness was certified for the claimed \((n,\Sigma)\). A tight value over a different alphabet than claimed is flagged, never conflated.
