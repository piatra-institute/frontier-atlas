# PROMPT FOR A CERTIFIED EXACT RESET THRESHOLD C(n)

## The Černý conjecture: the longest shortest reset word over all synchronizing \(n\)-state automata

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 49 of 50  
**Area:** search, sequences & games  
**Modes:** `[search]` `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A deterministic finite automaton is *synchronizing* if some input word - a *reset word* - drives every state to one common state, regardless of the start state. The **Černý conjecture** asserts that every synchronizing \(n\)-state automaton has a reset word of length at most \((n-1)^2\); the Černý automata attain exactly \((n-1)^2\), so the conjectured maximum \(C(n)\) equals \((n-1)^2\). Despite sixty years of work only a cubic upper bound is known in general, while \(C(n)\) is settled exactly only for small \(n\) by exhaustive computation. This is one of the sharpest exact-search targets in the field: the shortest reset word of a given automaton is computed exactly by breadth-first search in the subset automaton, so a candidate maximizer is verified cheaply, and "no \(n\)-state automaton resets slower" is a finite claim provable by isomorph-free enumeration or a DRAT-checked SAT refutation. The verifier that closes the loop is an exact subset-automaton BFS (the reset length of each automaton) plus a completeness certificate (a replayable enumeration or a checked UNSAT). Anything short of a matched maximizer and an exhaustiveness proof for a specific \(n\) - an automaton meeting \((n-1)^2\) offered as if it settled \(C(n)\), or the cubic bound quoted as exact - is a partial result, never a solution.

## 1. Exact problem statement

A **deterministic finite automaton (DFA)** is \(\mathcal A=(Q,\Sigma,\delta)\) with \(|Q|=n\) states, input alphabet \(\Sigma\), and a **complete** deterministic transition function \(\delta:Q\times\Sigma\to Q\), extended to words by \(\delta(q,wa)=\delta(\delta(q,w),a)\). No initial/final states are needed.

**Reset word.** A word \(w\in\Sigma^\ast\) is a **reset (synchronizing) word** if it maps all states to one:

\[
\bigl|\{\delta(q,w):q\in Q\}\bigr|=1.
\]

\(\mathcal A\) is **synchronizing** if a reset word exists. Its **reset threshold** is

\[
\operatorname{rt}(\mathcal A)=\min\{\,|w| : w \text{ is a reset word of } \mathcal A\,\}.
\]

**The extremal function.** Over all synchronizing \(n\)-state DFAs (with any alphabet), define

\[
C(n)=\max\{\,\operatorname{rt}(\mathcal A) : \mathcal A \text{ synchronizing},\ |Q|=n\,\}.
\]

**The conjecture.** Černý's conjecture is

\[
C(n)=(n-1)^2 .
\]

The **Černý automata** \(\mathcal C_n\) (two letters) satisfy \(\operatorname{rt}(\mathcal C_n)=(n-1)^2\), giving the lower bound \(C(n)\ge (n-1)^2\); the conjecture is the matching upper bound.

**Target.** Fix a specific \(n\) and certify the exact value \(C(n)\) - i.e. \(C(n)=(n-1)^2\) for that \(n\) - or certify an improved general or partial bound. The cost measure is reset-word length. The maximum is over *all* alphabet sizes; a value proven only for binary automata must be labelled as such, since larger alphabets could in principle reset more slowly (they do not, conjecturally, but that requires proof).

**Subset (power) automaton.** The reset threshold is realized as a shortest path in the deterministic automaton on subsets of \(Q\): states are nonempty \(S\subseteq Q\), the letter \(a\) sends \(S\) to \(\delta(S,a)=\{\delta(q,a):q\in S\}\), and

\[
\operatorname{rt}(\mathcal A)=\min\{\,|w| : \delta(Q,w) \text{ is a singleton}\,\},
\]

a shortest path from \(Q\) to any singleton, computed exactly by breadth-first search over the \(2^n-1\) nonempty subsets.

**Decision form used by the search.** Exhaustiveness is the refutation of

\[
\mathrm{SLOW}(n,\ell):\quad \exists\ \text{synchronizing } n\text{-state DFA with } \operatorname{rt}>\ell,
\]

so certifying \(C(n)=(n-1)^2\) means a witness for \(\mathrm{SLOW}(n,(n-1)^2-1)\) is *false* (checked UNSAT / exhausted enumeration) while \(\mathcal C_n\) witnesses \(\operatorname{rt}=(n-1)^2\).

A reader starting from this prompt alone has DFAs, reset words, the reset threshold, the subset automaton, the extremal \(C(n)\), the Černý automata, the decision form, and the conjecture.

## 2. Resolution standard

**Named certified form: exhaustive automata enumeration (or SAT with DRAT) with a checked optimality certificate.** A resolution of "\(C(n)=(n-1)^2\)" for a specific \(n\) consists of two independently checkable artifacts.

1. **Maximizer (lower bound).** An explicit synchronizing \(n\)-state DFA - the Černý automaton \(\mathcal C_n\) suffices - with an exact subset-automaton BFS confirming \(\operatorname{rt}=(n-1)^2\). The automaton plus the BFS output is the certificate.
2. **Exhaustiveness (upper bound).** A machine-checked proof that no synchronizing \(n\)-state DFA has reset threshold \(>(n-1)^2\), delivered as either
   - (a) an **isomorph-free enumeration** of all \(n\)-state DFAs (up to state-relabelling and letter symmetry) over each relevant alphabet size, each checked by exact subset-automaton BFS, with a replayable completeness log; or
   - (b) a **DRAT/LRAT UNSAT** proof that "there exists a synchronizing \(n\)-state DFA with a state-pair not merged within \((n-1)^2\) steps", checked by drat-trim / cake\_lpr.

Both parts are mandatory: \(C(n)\) is settled only when maximizer and exhaustiveness meet, i.e.

\[
(n-1)^2 \ \le\ C(n)\ \le\ (n-1)^2 .
\]

For a merely improved general bound, a single certified side (a new upper-bound proof, or a slower automaton family) suffices, reported as an inequality against the cited record.

**Not accepted as resolution.**

- An automaton attaining \((n-1)^2\) presented as proof that \(C(n)=(n-1)^2\); that is only the lower bound.
- The cubic upper bound (Frankl–Pin, Szykuła, Shitov) quoted as if it were the exact value.
- A reset word found heuristically, without a subset-automaton BFS proving it is *shortest*.
- An enumeration whose completeness or isomorph-rejection cannot be independently replayed, or a SAT UNSAT with no checked proof.
- A result for one alphabet size reported as the all-alphabet \(C(n)\); an asymptotic bound where an exact value is asked.

## 3. Graded partial-result targets

Ordered from reproducing the known frontier to the strongest result short of a proof for a new \(n\). Each names its certificate.

**P1 - Reproduce the reset-threshold pipeline.** Recompute \(\operatorname{rt}(\mathcal C_n)=(n-1)^2\) for a range of \(n\) by exact subset-automaton BFS, in two independent implementations.
*Certificate:* matching BFS reset lengths from two codebases.

**P2 - Reproduce a settled \(C(n)\).** For an \(n\) where \(C(n)\) is already established by exhaustive search, re-derive it end-to-end: maximizer plus a replayable exhaustiveness certificate, matched against the published value and access date.
*Certificate:* isomorph-free enumeration replay (or checked UNSAT) reproducing the record.

**P3 - Exact \(C(n)\) for a new \(n\).** Certify \(C(n)=(n-1)^2\) for one \(n\) beyond the current exhaustively-settled frontier, over all relevant alphabet sizes.
*Certificate:* both artifacts of §2 under a SHA-256 manifest; the alphabet-size coverage documented.

**P4 - Binary-alphabet extension.** Push the binary-alphabet verification (where the search is far cheaper) to a larger \(n\) than currently certified, honestly labelled as the two-letter case.
*Certificate:* replayable binary enumeration or checked UNSAT at \((n-1)^2+1\).

**P5 - Improved general or restricted bound.** Certify a strictly better upper bound than the published record for a structured class (one-cluster, Eulerian, or circular automata), or a new slowly-synchronizing family with certified reset thresholds.
*Certificate:* the certified side plus the exact prior record and access date.

**P6 - Slowly-synchronizing census.** For a fixed small \(n\), certify the complete list of \(n\)-state DFAs whose reset threshold is within a chosen margin of \((n-1)^2\), with exact BFS on each.
*Certificate:* the isomorph-free census with per-automaton BFS certificates.

## 4. Known results and prior art

- J. Černý (~1964) posed the conjecture and exhibited the automata \(\mathcal C_n\) with \(\operatorname{rt}=(n-1)^2\); it is among the oldest and most-tested open problems in automata theory.
- Cubic upper bounds: the Frankl–Pin bound \((n^3-n)/6\) (~1982–1983) stood for decades; M. Szykuła ("Improving the upper bound…", ~2018) first broke it; Y. Shitov (~2019) lowered the constant further to about \(0.1654\,n^3\) (verify the exact constant and paper).
- The conjecture is proven for many structured classes (one-cluster automata with prime-length cycle - Steinberg; Eulerian; circular - Dubuc; aperiodic - Trahtman) and verified exhaustively for small \(n\): true for all automata with \(n\le 5\) states regardless of alphabet, and for binary automata up to larger \(n\) (around \(n\le 11\)) - verify the exact settled ranges.
- Exhaustive/experimental computations of reset thresholds: Ananichev–Gusev–Volkov and the Kisielewicz–Kowalski–Szykuła experimental report (~2013) tabulate small-automaton reset thresholds; the "slowly synchronizing automata" series (Ananichev, Volkov, Gusev, Szykuła) maps the extremal families.
- Surveys: M. Volkov, "Synchronizing automata and the Černý conjecture" (~2008); the maintained "List of results on the Černý conjecture and reset thresholds" arXiv resource (verify current version).
- The shortest reset word of a given DFA is computed exactly by BFS in the \(2^n\)-state subset automaton; deciding synchronizability is polynomial (the pair automaton - two states can always be merged iff the automaton is synchronizing), but computing the shortest-reset-word *length* is NP-hard in general - exact only for the small \(n\) of interest here.
- Černý's original automata remain, sixty years on, the slowest known synchronizers; extensive search has found no family beating \((n-1)^2\), which is the empirical backbone of the conjecture (verify against the current slowly-synchronizing census).

**Status as of mid-2026 - re-verify against the current literature (and the reset-threshold tracker) before starting any session.**

## 5. Attack plan

`[search]` `[cert]` - first computations on one workstation. Everything hinges on a trusted exact reset-threshold engine and a trusted enumeration/refutation; the maximizer side is easy (the Černý automaton), the exhaustiveness side is the work.

- **Exact reset-threshold engine first.** Implement subset-automaton BFS: from the full set \(Q\), apply each letter, BFS over subsets until a singleton is reached; the depth is \(\operatorname{rt}\). Bitset-encode subsets (one machine word for \(n\le 64\)) for speed. Implement it twice and require agreement on \(\mathcal C_n\) and textbook automata before trusting either.
- **Isomorph-free DFA generation (P2, P3).** Generate all \(n\)-state DFAs up to state-relabelling (and letter permutation) with canonical-form rejection (nauty-style orderly generation or an explicit canonical labelling); feed each synchronizing automaton to the BFS engine; record the maximum and a replayable completeness log.
- **Prune aggressively but soundly.** Restrict to strongly connected, synchronizing automata (a necessary structure), and use the pair-automaton test - two states \(\{p,q\}\) are mergeable iff the automaton is synchronizing - to skip non-synchronizing candidates:

  \[
  \mathcal A \text{ synchronizing}\iff \forall p,q\in Q\ \exists w:\ \delta(p,w)=\delta(q,w).
  \]

  Every pruning rule must be proven not to drop a potential maximizer.
- **SAT route (P3, P4).** Encode "an \(n\)-state DFA exists whose shortest reset word exceeds \((n-1)^2\)": transition variables \(\delta(q,a)\), plus a layered subset-reachability constraint asserting that from \(Q\) no singleton is reached within \((n-1)^2\) steps. Refute it with CaDiCaL / kissat → DRAT (drat-trim, then cake\_lpr).
- **Counterexample handling.** A satisfying assignment is a candidate counterexample to Černý itself; it is re-decoded to a DFA and re-checked by exact BFS before any alarm - and preserved and reported, never suppressed, if it survives.
- **Structured classes (P5).** For one-cluster / Eulerian / circular families, specialize both the generation and the bound to push further than the unrestricted census, since these classes carry proven partial results to build on.
- **Generator validation.** Before any exhaustiveness claim, confirm the DFA generator reproduces known counts of \(n\)-state automata up to isomorphism (and of synchronizing ones) for small \(n\); a miscount is an immediate disqualifier.
- **One-workstation scope.** The \(2^n\) subset automaton and the super-exponential DFA count cap \(n\) sharply: unrestricted all-alphabet enumeration is feasible only for very small \(n\), while binary and structured classes reach further. Choose the target \(n\) accordingly and state the alphabet coverage.
- **Failure modes.** Expect (i) enumeration blow-up - report the largest \(n\) actually closed; (ii) canonical-labelling bugs that double-count or, worse, silently skip automata (validate the generator's count against known DFA totals); (iii) trusting an unproven UNSAT on the solver's word; (iv) conflating binary with all-alphabet results. A satisfying SAT instance is a candidate counterexample and is verified exhaustively, never suppressed.

## 6. Verification and auditability requirements

1. **Exact computation.** Every reset threshold is an exact subset-automaton BFS depth; every exhaustiveness claim is a replayable enumeration or a drat-trim/cake\_lpr-checked UNSAT. No sampling, no floating point.
2. **Independent verification.** The BFS engine, the DFA generator, and the SAT encoder are separate programs; the generator's automaton count is validated against known enumeration totals; each maximizer's reset length is re-confirmed by a second BFS; each UNSAT is checked by two proof checkers.
3. **Reproducibility.** The alphabet sizes covered, canonical-form scheme, pruning rules, solver/tool names and versions, and seeds are recorded; a SHA-256 manifest covers the census files, proofs, and logs. Any reproduced or extended value is cited with source and access date.
4. **Preservation.** Generator, BFS engine, encoder, and checker source are part of the record. Any discarded run or lost log is stated explicitly.
5. **Honest reporting.** The report states up front, per \(n\), whether both maximizer and exhaustiveness were certified (hence \(C(n)\) settled), over which alphabet sizes, or only one side (an inequality). An automaton meeting \((n-1)^2\) is reported as a lower-bound witness, never as a proof of \(C(n)\); a binary-only result is never presented as the all-alphabet value.
