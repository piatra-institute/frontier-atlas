# PROMPT FOR A CERTIFIED OPTIMAL SELECTION OR MERGING NETWORK

## The minimum number of comparators to select the \(t\)-th largest of \(n\), or to merge two sorted sequences

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 46 of 50  
**Area:** search, sequences & games  
**Modes:** `[search]` `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A comparator network is an oblivious data-flow circuit of compare-and-exchange gates: fixed wiring, no branching, cost measured in comparators. Sorting networks (rank 01) are the fully-ordered case; this problem is the *selection* and *merging* cousin, with a different objective. A **\(t\)-selection network** must place the \(t\)-th largest of its \(n\) inputs on a designated output wire for every input; the **median** is \(t=\lceil n/2\rceil\); a **merging network** \(M(m,n)\) must sort the concatenation of an already-sorted \(m\)-sequence and \(n\)-sequence. The minimum comparator counts are known only for small sizes and are open beyond. The problem is an exact fit for certified search because of the **zero-one principle**: a comparator network computes a monotone selection correctly on all inputs iff it does so on all \(2^n\) binary inputs - so a candidate network is verified cheaply and completely, and optimality is a finite SAT question. The verifier that closes the loop is a zero-one checker (the network selects correctly on every binary vector) plus a DRAT/LRAT optimality proof that no smaller network exists, checked by drat-trim / cake\_lpr. Anything short of a matched construction and lower bound for a specified \((t,n)\) or \((m,n)\) - a good network with no optimality proof, or an asymptotic bound where an exact integer is asked - is a partial result, never a solution.

## 1. Exact problem statement

A **comparator** \([i\!:\!j]\) on wires \(i<j\) replaces \((x_i,x_j)\) by \((\min,\max)=(x_i\wedge x_j,\ x_i\vee x_j)\) in the Boolean case. A **comparator network** on \(n\) wires is a finite sequence \(C=(c_1,\dots,c_C)\) of comparators; its size is \(C\).

**Zero-one principle.** A comparator network realizes a prescribed monotone selection on all real inputs iff it does so on all \(2^n\) inputs in \(\{0,1\}^n\). Every correctness claim below is therefore a statement about binary inputs.

**\(t\)-selection network.** \(C\) is a \(t\)-selection network on \(n\) wires if there is a fixed output wire \(o\) such that, after running \(C\), wire \(o\) holds the \(t\)-th largest of the \(n\) inputs, for every input. Define

\[
U_t(n)=\min\{\,C : \text{a size-}C\ t\text{-selection network on } n \text{ wires exists}\,\}.
\]

The **median network** minimum is \(W(n)=U_{\lceil n/2\rceil}(n)\).

**Classification (top-\(t\)) network.** A stronger object routes the \(t\) largest inputs to \(t\) designated wires (order among them free); its minimum is denoted \(V_t(n)\ge U_t(n)\).

**Merging network.** \(C\) is an \((m,n)\)-merging network if, whenever wires \(1..m\) carry a sorted sequence and wires \(m{+}1..m{+}n\) carry a sorted sequence, \(C\) outputs the sorted concatenation. Define

\[
\widehat M(m,n)=\min\{\,C : \text{a size-}C\ (m,n)\text{-merging network exists}\,\}.
\]

**Base cases (start-from-prompt).** Selecting the maximum is a tournament, so

\[
U_1(n)=U_n(n)=n-1,
\]

and selecting the maximum and minimum simultaneously (a classification into extremes) costs the classical

\[
\left\lceil \tfrac{3n}{2}\right\rceil-2
\]

comparators. Merging a single element into a sorted \(n\)-list satisfies \(\widehat M(1,n)=n\) (verify). These anchor the small end; the open content is the interior \(t\) (especially the median) and general \((m,n)\).

**Target.** Fix one concrete instance - a specific \((t,n)\) for selection/median, or a specific \((m,n)\) for merging - and certify the exact minimum comparator count, or a certified improved bound.

The cost measure is comparator count (size); a depth variant may be pursued separately but must be labelled as such. This is the comparator-network model; comparison-tree selection lower bounds (Blum et al.) live in a different model and do not transfer.

**Decision form used by the search.** The optimum is located by the monotone family

\[
\mathrm{NET}(t,n,C):\quad \text{does a size-}C\ t\text{-selection network on } n \text{ wires exist?}
\]

(satisfiable for \(C\ge U_t(n)\), unsatisfiable below); certifying \(U_t(n)=C\) means a witness network for \(\mathrm{NET}(t,n,C)\) and a checked refutation of \(\mathrm{NET}(t,n,C-1)\). The merging optimum is bracketed identically.

A reader starting from this prompt alone has comparators, networks, the zero-one principle, the selection/median/merging objectives, the decision form, and the optima \(U_t(n)\), \(W(n)\), \(\widehat M(m,n)\).

## 2. Resolution standard

**Named certified form: SAT with a DRAT optimality proof.** A resolution of "\(U_t(n)=C\)" (or \(\widehat M(m,n)=C\)) consists of two independently checkable artifacts.

1. **Upper bound (a network).** An explicit network of \(C\) comparators, given as a comparator list, together with a zero-one checker that evaluates it on all \(2^n\) binary inputs and confirms the designated wire (or output block) is correct on every one. The list plus the checker's accept is the certificate.
2. **Lower bound.** A DRAT/LRAT UNSAT proof of the SAT encoding "there exists a \((C-1)\)-comparator \(t\)-selection network on \(n\) wires", checked by drat-trim and re-checked by cake\_lpr. The encoding's soundness (that a satisfying assignment would decode to a valid network) is itself argued and, ideally, independently re-decoded.

Both parts are mandatory: the exact value is proven only when construction and lower bound meet. For a merely *improved* bound, one certified side suffices, reported as an inequality.

The encoding must be sound in the decode direction: a satisfying assignment is mechanically decoded to a comparator list and re-checked by the zero-one verifier, so that a SAT result is never accepted on the solver's word alone. The UNSAT proof carries the lower bound; the re-decoded witness carries the upper bound; the two are kept logically separate.

**Not accepted as resolution.**

- A network with no optimality proof, or one verified only on sampled inputs rather than the full \(2^n\) binary set.
- A DRAT-free "the solver returned UNSAT" claim; every lower bound needs an emitted, re-checked proof.
- An asymptotic bound (Batcher upper bound, Miltersen–Paterson–Tarui lower bound) presented as an exact small-instance value.
- A depth-optimal network offered as size-optimal, or a classification network passed off as a bare \(t\)-selection network without noting \(V_t\ge U_t\).
- Any correctness argument relying on floating-point or on a non-exhaustive input sample.

## 3. Graded partial-result targets

Ordered from reproducing the known frontier to the strongest result short of a full new family of optima. Each target names the artifact that proves it and how it is independently checked.

**P1 - Reproduce a known selection optimum.** For a small \((t,n)\) with \(U_t(n)\) settled (e.g. small median networks), recompute it end-to-end: explicit network plus DRAT UNSAT at \(C-1\).
*Certificate:* zero-one checker accept; drat-trim/cake\_lpr exit on the lower bound.

**P2 - Reproduce the sorting-network SAT pipeline (cross-ref 01).** Re-derive one settled sorting-network size optimum with the same toolchain to validate the encoding and proof checking against a published record.
*Certificate:* zero-one accept and checked UNSAT matching the cited value.

**P3 - Exact value for an open selection/median instance.** Certify \(U_t(n)\) (or \(W(n)\)) for one instance beyond the known frontier by matched construction and DRAT lower bound.
*Certificate:* both artifacts of §2 under a SHA-256 manifest.

**P4 - Exact merging optimum.** Certify \(\widehat M(m,n)\) for a specific open \((m,n)\): explicit merging network plus checked UNSAT at \(C-1\), using the merging zero-one principle (only sorted binary inputs need be checked).
*Certificate:* restricted zero-one checker accept; checked lower-bound proof.

**P5 - Improved one-sided bound.** Where the exact value is out of reach, certify a strictly better construction (new upper bound) or a strictly better DRAT lower bound than the published record, reported as an inequality with the baseline cited.
*Certificate:* the certified side plus the exact prior record and access date.

**P6 - Classification vs selection gap.** For a fixed \(n\), certify \(V_t(n)\) and \(U_t(n)\) for a range of \(t\) and report the exact gap \(V_t-U_t\).
*Certificate:* matched certificates on both objectives.

**P7 - Structure mining ([sym]-adjacent).** From certified optimal networks, extract a reusable sub-network pattern or a lower-bound lemma and state it as a precise conjecture with supporting certified data.
*Certificate:* the data table plus the conjecture, each datum individually certified; no pattern is claimed beyond the certified range.

## 4. Known results and prior art

- The zero-one principle is due to Bouricius and is standard in Knuth, *TAOCP* Vol. 3, §5.3.4 (verify), which also tabulates small selection- and median-network sizes and states the selection problem.
- Note the objective genuinely differs from sorting: a selection network need not sort, so \(U_t(n)\) can be strictly below the sorting-network size \(S(n)\); reusing a sorting network is only an upper bound, never evidence of the selection optimum.
- Selection-network constructions: V. E. Alekseev (~1969) and A. C. Yao / F. F. Yao gave \(O(n\log t)\)-comparator \(t\)-selection networks (verify authorship and bounds); exact minimum sizes are established only for small \(n\).
- Merging: K. Batcher's odd-even merge (~1968) gives \(M(m,n)\le \tfrac{m+n}{2}\log_2(m+1)+O(n)\); Miltersen, Paterson, and Tarui, "The asymptotic complexity of merging networks," *J. ACM* 43(1), 1996, proved a matching asymptotic lower bound \(\widehat M(m,n)\ge \tfrac{m+n}{2}\log_2(m+1)-O(m)\). Batcher's merge is **not** known to be size-optimal for general \((m,n)\); small cases are settled by search.
- SAT-certified optimality for comparator networks (the toolchain to import, cross-ref rank 01): Codish, Cruz-Filipe, Frank, and Schneider-Kamp showed 25 comparators optimal for sorting nine inputs and 29 for ten (~2014); Ehlers and Müller ("The Final Countdown", ~2015) and Bundala–Závodný (depth optimality) extended the method (verify each).
- Small exact selection/median-network sizes appear in OEIS and in Knuth's tables; re-verify each entry and its provenance before use.
- Lower-bound techniques beyond brute SAT include partial-order (poset) reachability arguments and adversary/cut methods; these can prune the search or supply a checkable inequality, but a bare exact value in the network model is settled only by exhaustive/SAT search for the sizes of interest.
- Depth-optimality (minimizing layers rather than comparators) is a separate objective with its own record (Bundala–Závodný, ~2014, verify); a depth result never certifies a size result.

**Status as of mid-2026 - re-verify against the current literature (and OEIS/record trackers) before starting any session.**

## 5. Attack plan

`[search]` `[cert]` - first computations on one workstation.

- **Zero-one verifier first.** Implement the exhaustive \(2^n\)-input checker (bitset simulation of the comparator list, one machine word per binary input processed in parallel). This is the foundation for every upper bound; validate it on textbook networks.
- **Reuse the sorting-network baseline.** A known optimal sorting network gives an immediate upper bound on \(U_t(n)\) and a sanity target; run the imported pipeline (rank 01) on it first to confirm the encoding and proof-checking stack end-to-end before attacking the selection objective.
- **SAT encoding (P1–P4).** Adopt the established comparator-network encoding: for each layer/position a comparator choice \([i\!:\!j]\), propagate each of the \(2^n\) binary inputs symbolically, and constrain the designated output wire to equal the \(t\)-th largest bit. Use the standard optimizations from the sorting-network SAT literature - subsumption of equivalent prefixes, the "last comparator" and first-layer normalizations, and value-symmetry breaking - every reduction kept inside the proof or separately justified.
- **Solve and prove.** Run CaDiCaL / kissat at size \(C-1\), emit DRAT, check with drat-trim, convert to LRAT and re-check with cake\_lpr. A satisfying assignment at size \(C\) is decoded back into a comparator list and re-verified by the zero-one checker (never trust the decode).
- **Correctness constraint.** With \(v^{(k)}_i\) the value on wire \(i\) after comparator \(k\) on binary input \(b\in\{0,1\}^n\), each comparator enforces

  \[
  v^{(k)}_i=v^{(k-1)}_i\wedge v^{(k-1)}_j,\qquad
  v^{(k)}_j=v^{(k-1)}_i\vee v^{(k-1)}_j,
  \]

  and the final clause fixes the designated wire to the \(t\)-th largest bit of \(b\); one such block per binary input, sharing the comparator-choice variables.
- **Partial-order pruning.** Track, per prefix, the poset of forced order relations among wires; prune candidate comparators that cannot advance the selection, and use the poset to certify quick lower bounds before invoking the full SAT refutation.
- **Merging specialization (P4).** For merging, restrict the checked input set to sorted binary pairs (there are \((m+1)(n+1)\) of them), shrinking both the verifier and the encoding dramatically relative to full selection.
- **Prefix/orderly search for constructions.** A custom C++ generator builds candidate networks comparator-by-comparator with canonical-prefix pruning (à la the sorting-network "generate and prune"), feeding upper bounds to the SAT lower-bound step.
- **Sanity bracket.** For merging, cross-check every certified value against the Batcher upper bound and the Miltersen–Paterson–Tarui asymptotic lower bound; a certified value outside that corridor signals a bug in the encoding or verifier.
- **One-workstation scope and failure modes.** The \(2^n\) input blow-up caps \(n\) (around the high teens for full selection; larger for merging thanks to the sorted-pair restriction), and the SAT lower bound is the expensive half. Expect (i) UNSAT instances that exceed the time budget one comparator short of optimal - report the certified inequality honestly; (ii) encoding bugs where a symmetry break excludes the optimum (guard by decoding and re-verifying every SAT witness); (iii) confusing selection, classification, and merging objectives; (iv) trusting an unproven UNSAT. Record the largest instance actually closed.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every upper bound is verified on the complete binary input set (all \(2^n\), or all sorted pairs for merging); every lower bound is a drat-trim/cake\_lpr-checked UNSAT. No sampling, no floating point.
2. **Independent verification.** The zero-one checker, the SAT encoder, and the network decoder are separate programs. Each SAT witness is decoded and re-verified independently of the solver; each UNSAT is checked by two proof checkers (one formally verified).
3. **Reproducibility.** Encodings, symmetry-breaking rules, solver names/versions, seeds, and generator parameters are recorded; a SHA-256 manifest covers every network, proof, and log. The prior record for the instance is cited with source and access date.
4. **Preservation.** Encoder, generator, checker, and decoder source are part of the record. Any discarded search or lost proof is stated explicitly.
5. **Honest reporting.** The report states up front, per instance, whether both bounds were certified (hence the exact optimum), or only one side (an inequality), in which objective (selection / classification / merging) and cost measure (size / depth). A construction without a matching lower bound is never presented as the optimum.
