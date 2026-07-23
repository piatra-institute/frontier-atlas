# PROMPT FOR A CERTIFIED SHORTEST PERMUTATION-SUPERSEQUENCE VALUE

## The minimum length of a string over \([n]\) containing every permutation of \([n]\) as a subsequence

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 44 of 50  
**Area:** search, sequences & games  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Fix the alphabet \([n]=\{1,\dots,n\}\). A string \(w\) over \([n]\) is an *\(n\)-supersequence* if every one of the \(n!\) permutations of \([n]\) occurs in \(w\) as a (not necessarily contiguous) subsequence. Let \(\sigma(n)\) be the shortest length of such a \(w\). A classical construction gives \(\sigma(n)\le n^2-2n+4\) for \(n\ge 3\), and this is conjectured to be exact; equality is proven only for a handful of small \(n\). The problem matters as the subsequence-analogue of the superpermutation problem (rank 34, which uses contiguous *substrings*) and as a clean testbed for certified combinatorial search: a claimed value of \(\sigma(n)\) decomposes into an explicit short word (an upper bound whose length any checker can re-count) and a machine-checkable proof that no shorter word works (a lower bound, delivered as an exhaustive branch-and-bound completeness log or a DRAT/LRAT-checked UNSAT proof). The verifier that closes the loop is a two-part checker: a linear-time subsequence-cover verifier for the witness word, and a proof checker (drat-trim / cake\_lpr for the CNF route, or an independent search replay for the enumeration route). Anything short of a matched upper and lower bound for a specific \(n\) - in particular a construction with no lower bound, or a formula asserted without proof - is a partial result, never a solution.

## 1. Exact problem statement

Let \(w=w_1w_2\cdots w_L\) be a string over \([n]\), and let \(\pi=\pi_1\cdots\pi_n\) be a permutation of \([n]\).

**Subsequence.** \(\pi\) is a *subsequence* of \(w\) if there exist indices

\[
1\le i_1<i_2<\cdots<i_n\le L
\qquad\text{with}\qquad
w_{i_j}=\pi_j\ \ (1\le j\le n).
\]

**Supersequence.** \(w\) is an *\(n\)-supersequence* (a universal string for permutations under the subsequence order) if every one of the \(n!\) permutations of \([n]\) is a subsequence of \(w\).

**The optimum.** Define

\[
\sigma(n)=\min\{\,L : \text{some } w\in[n]^L \text{ is an } n\text{-supersequence}\,\}.
\]

**The conjecture.** The standing conjecture is

\[
\sigma(n)=n^2-2n+4\qquad(n\ge 3),
\]

where the right-hand side is furnished by an explicit construction (an upper bound) and is conjectured tight; the matching lower bound is the open content.

The cost measure is string length; there is no other normalization.

**Elementary bounds (start-from-prompt).** Concatenating \(n\) copies of the identity block \(12\cdots n\) yields a word of length \(n^2\) in which every permutation \(\pi\) embeds by taking \(\pi_i\) from the \(i\)-th block; hence

\[
\sigma(n)\le n^2.
\]

The refined construction of §4 saves \(2n-4\) symbols, giving \(\sigma(n)\le n^2-2n+4\). On the other side, an elementary counting argument forces

\[
\sigma(n)=(1-o(1))\,n^2,
\]

so the entire open content lives in the second-order term \(-2n+4\): proving the lower bound \(\sigma(n)\ge n^2-2n+4\) for a specific \(n\) is exactly what is missing.

This is **distinct from** the superpermutation problem (rank 34), which asks for the shortest string containing every permutation as a *contiguous substring*. Here the containment relation is the subsequence order, and the two optima differ.

**Adjacent secondary formulations** (permitted as auxiliary targets, never as substitutes for \(\sigma(n)\)):

- **Shortest common superstring.** For a fixed finite set \(S\) of strings, \(\mathrm{SCS}(S)\) is the shortest \(w\) containing every \(s\in S\) as a contiguous substring - an NP-hard optimization whose small-instance optima are certifiable.
- **De Bruijn / universal cycles.** A de Bruijn sequence \(B(k,n)\) has exact length \(k^n\); the open content is in optimized *linear* (acyclic) universal strings and in universal cycles for restricted combinatorial structures.

**Decision form used by the search.** The optimum is located by a sequence of decision instances

\[
\mathrm{SUP}(n,L):\quad \exists\, w\in[n]^L \text{ that is an } n\text{-supersequence?}
\]

which is monotone in \(L\) (satisfiable for \(L\ge\sigma(n)\), unsatisfiable below). Certifying \(\sigma(n)=L\) means exhibiting a witness for \(\mathrm{SUP}(n,L)\) and a checked refutation of \(\mathrm{SUP}(n,L-1)\).

A reader starting from this prompt alone has every definition needed: alphabet, subsequence, supersequence, the optimum \(\sigma(n)\), the conjectured value, and the decision form driving the search.

## 2. Resolution standard

**Named certified form: exhaustive search with a checked optimality certificate.** A resolution of "\(\sigma(n)=L\)" for a specific \(n\) consists of two independently checkable artifacts.

1. **Upper bound.** An explicit word \(w\in[n]^{L}\) with a linear-time verifier confirming that all \(n!\) permutations are subsequences (a greedy leftmost-embedding pass per permutation, or one automaton sweep). The witness plus the verifier's accept is the certificate.
2. **Lower bound.** A machine-checked proof that no word in \([n]^{L-1}\) is an \(n\)-supersequence, delivered as either
   - (a) a DRAT/LRAT UNSAT proof of a CNF encoding "some length-\((L-1)\) word covers all permutations", checked by drat-trim or cake\_lpr; or
   - (b) a complete branch-and-bound / IDA\* enumeration whose pruning is sound and whose completeness log an independent driver can replay.

Both parts are mandatory: \(\sigma(n)=L\) is proven only when the upper and lower bounds meet. The two artifacts must be checkable by code written independently of the search that produced them - the checker never trusts the solver, only its emitted proof or replay log.

**Not accepted as resolution.**

- An upper-bound construction - including a proof that \(\sigma(n)\le n^2-2n+4\) - with no matching certified lower bound.
- The formula \(n^2-2n+4\) asserted for the target \(n\) by analogy or pattern, without a proof specific to that \(n\).
- A word found by heuristic or randomized search presented as optimal without a lower-bound certificate.
- A solver run that reports UNSAT without an emitted, re-checkable proof, or a search whose pruning cannot be independently replayed.
- A single satisfying instance offered as evidence about the optimum, or an asymptotic statement where an exact value is asked.

## 3. Graded partial-result targets

**P1 - Reproduce the small-\(n\) frontier.** Recompute \(\sigma(n)\) for every \(n\) already settled (small \(n\); see §4) with our own toolchain: an explicit shortest word plus a DRAT/LRAT UNSAT proof (or a replayable exhaustive log) at length \(\sigma(n)-1\).
*Certificate:* subsequence-cover verifier accept on the witness; proof-checker exit on the lower bound.

**P2 - Re-verify the construction.** For the smallest open \(n\), independently build the \(n^2-2n+4\) construction and re-count its length and coverage.
*Certificate:* verifier accept, giving a certified upper bound \(\sigma(n)\le n^2-2n+4\).

**P3 - Certified lower bound for an open \(n\).** For the smallest open \(n\), push the certified lower bound as high as the budget allows: a checked UNSAT (or exhaustive completeness) proof that no word of length \(\ell\) is an \(n\)-supersequence, for the largest \(\ell<n^2-2n+4\) reachable.
*Certificate:* checked UNSAT proof at length \(\ell\); the gap to the construction reported exactly.

**P4 - A new exact value (headline).** Close the gap for one open \(n\): matched construction and lower-bound certificate establishing \(\sigma(n)=n^2-2n+4\).
*Certificate:* both artifacts of §2, under a SHA-256 manifest.

**P5 - Exact SCS optimum.** For a specific fixed instance \(S\) (documented, non-trivial), certify \(\mathrm{SCS}(S)=L\) via an explicit superstring and an LRAT/ILP-exact lower bound.
*Certificate:* witness plus checked optimality proof.

**P6 - Structure of minimal supersequences.** For an \(n\) where \(\sigma(n)\) is known, certify the exact count (up to the natural symmetries) of length-\(\sigma(n)\) supersequences, documenting the non-uniqueness.
*Certificate:* isomorph-free enumeration with a replay log.

**P7 - De Bruijn / universal-cycle variant.** For a fixed restricted structure (a language or subset of \(k\)-ary strings), certify the exact shortest linear universal string, or confirm the \(k^n\) cyclic optimum with an explicit witness and a matching lower-bound certificate.
*Certificate:* witness plus checked optimality proof.

## 4. Known results and prior art

- The upper bound \(\sigma(n)\le n^2-2n+4\) via an explicit construction, and the conjecture that it is exact, trace to M. Newey (~1973); the sequence is recorded in OEIS **A062714** (verify id and offset).
- Equality is reported proven for small \(n\); the literature commonly cites tightness up to around \(n\le 7\) - verify the exact largest settled \(n\) and the responsible computation before relying on it.
- Small witnesses realizing \(n^2-2n+4\): \(n=3\) admits the length-7 word `1213212`; \(n=4\) admits the length-12 word `123412314321` (verify).
- Deciding whether a *given* word contains all permutations as subsequences is coNP-complete in the general (parameter-in-input) setting - see "All Permutations Supersequence is coNP-complete" (~2015, verify authorship and venue). For fixed length the per-permutation check is linear, so certifying a concrete candidate is cheap.
- The problem appears as Problem 15 ("Short Supersequence of Permutations") in the "125 problems in text algorithms" collection (verify).
- Shortest-common-superstring is NP-hard (Gallant–Maier–Storer, ~1980, verify) with a long approximation-ratio literature; de Bruijn sequences \(B(k,n)\) have exact length \(k^n\) and count \((k!)^{k^{n-1}}/k^n\) (classical).
- Lower-bound techniques for \(\sigma(n)\) (counting/entropy and adversary arguments) exist but have not closed the gap for general \(n\); mark any specific attribution "(verify)".
- Refined lower bounds on the second-order term (of the form \(\sigma(n)\ge n^2-c\,n^{\,7/4+\varepsilon}\)) are attributed to Kleitman–Kwiatkowski (verify authorship, exponent, and year); they narrow but do not close the \(-2n+4\) gap.
- Note the direction: \(\sigma(n)\) equals the SCS of the *set of all \(n!\) permutations* under the subsequence (not substring) order, so generic SCS heuristics do not transfer - the subsequence structure is essential.

**Status as of mid-2026 - re-verify against the current literature (and OEIS/record trackers) before starting any session.**

## 5. Attack plan

`[search]` - first computations on one workstation.

- **Reproduce (P1).** Encode "a word of length \(L\) over \([n]\) is an \(n\)-supersequence" as CNF: position-letter variables \(x_{p,a}\) (one-hot per position); for each permutation \(\pi\) an embedding gadget asserting an increasing index sequence realizing \(\pi\) (a layered "reached prefix \(j\) of \(\pi\) by position \(p\)" encoding). Run CaDiCaL / kissat at \(L=\sigma(n)-1\), emit DRAT, check with drat-trim, convert to LRAT and re-check with cake\_lpr (a formally verified checker). This validates the pipeline against known values.
- **Symmetry breaking.** The first occurrence of each letter and the relabelling symmetry of \([n]\) admit lex-leader constraints; add them as clauses kept inside the proof. Any symmetry break must be provably satisfiability-preserving - guard against silently dropping the optimum.
- **Lower bounds for open \(n\) (P3).** Two independent engines: (a) the SAT route above at increasing \(\ell\); (b) a custom C++ IDA\*/branch-and-bound over words with state = the set of permutation-embedding frontiers still open (a bitmask over the \(n!\) permutations), and an admissible remaining-length bound. The two engines cross-check every UNSAT / infeasibility claim.
- **Upper bounds (P2, P4).** Emit the \(n^2-2n+4\) construction and run the linear verifier; also try MaxSAT / ILP (SCIP with exact rational bounds) to hunt for any shorter word before committing budget to the matching lower bound.
- **SCS and enumeration (P5, P6).** ILP overlap-graph formulation for SCS with exact LP duals; nauty only if a symmetry group needs canonical forms in the minimal-word enumeration.
- **Proof-logging discipline.** Every UNSAT claim is emitted as DRAT at solve time and checked before the value is recorded; no "the solver said UNSAT" is trusted. For the IDA\* route, the completeness log records the frontier bitmask at each backtrack so an independent replayer can confirm no branch was skipped.
- **One-workstation scope and failure modes.** The \(n!\) permutation constraints dominate - \(n=6\) means 720 gadgets, \(n=7\) means 5040 - so the open frontier is small. Expect (i) search blow-up at the lower-bound step well below the construction length; (ii) weak admissible bounds stalling IDA\*; (iii) unverified solver output (never trust an UNSAT without a re-checked proof); (iv) symmetry-breaking bugs that silently drop the optimum. Record the exact reachable \(\ell\) rather than overclaiming.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every load-bearing claim rests on a re-checkable artifact: a subsequence-cover verifier accept for each upper bound; a drat-trim/cake\_lpr-checked UNSAT (or a replayable exhaustive log) for each lower bound. Floating point plays no role; all arithmetic is integer.
2. **Independent verification.** The witness verifier and the search/encoding code are written separately. Each SAT UNSAT is checked by two proof checkers (one formally verified); each exhaustive lower bound is replayed by an independent driver; the SAT and IDA\* engines cross-validate infeasibility.
3. **Reproducibility.** All CNF encodings, symmetry-breaking clauses, solver names and versions, seeds, and IDA\* bound functions are recorded; a SHA-256 manifest covers every witness, proof, and log. The prior value of \(\sigma(n)\) reproduced or extended is cited with source and access date.
4. **Preservation.** Encoder, search, and verifier source are part of the record. Anything not preserved (a discarded solver run, a lost intermediate proof) is stated explicitly.
5. **Honest reporting.** The report states up front, per target \(n\), whether both bounds were certified (hence \(\sigma(n)\) settled), or only one side and by how large a gap. A construction without a matching lower bound is reported as an upper bound only, never as the value of \(\sigma(n)\).
