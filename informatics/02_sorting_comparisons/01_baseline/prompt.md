# PROMPT FOR DETERMINING THE MINIMUM NUMBER OF COMPARISONS TO SORT

## The worst-case comparison complexity \(S(n)\) at the smallest open \(n\)

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 02 of 50
**Area:** algorithms & bilinear complexity
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

\(S(n)\) is the minimum number of pairwise comparisons that suffices, in the worst case, to sort \(n\) distinct elements by any adaptive comparison algorithm - equivalently, the minimum height of a binary comparison decision tree with \(n!\) leaves that is *realizable* by a valid comparison strategy. It is the oldest exact-complexity question in algorithmics and the reference point for adaptive sorting. The information-theoretic bound \(S(n)\ge\lceil\log_2 n!\rceil\) is not always tight; the Ford–Johnson (merge-insertion) algorithm gives the best known upper bound for small \(n\) but is not always optimal, and closing the gap requires exact search. The problem is matched to current AI methods because both sides are finite and certifiable: an upper bound is an explicit strategy (a comparison tree of the claimed height), and a lower bound is an adversary/exhaustive argument over a finite, prunable game tree, replayable by an independent checker. \(S(n)\) is settled for all \(n\le 18\) and for \(n=22\); the smallest open case is \(n=19\). The on-machine verifier that closes the loop is a decision-tree validator (upper bound) plus a replayable exhaustive/adversary search log (lower bound). Anything short of pinning \(S(n)\) at a new \(n\), or a certified improvement of the standing bracket, is a partial result.

## 1. Exact problem statement

Elements come from a totally ordered set; the only allowed primitive is a comparison "is \(a<b\)?" returning one bit. A **sorting algorithm** is an adaptive strategy: a binary tree in which each internal node queries an ordered pair of the \(n\) elements and each leaf outputs a total order. The tree **sorts** if every one of the \(n!\) permutations reaches a leaf consistent with it, and the query at each node is answerable given the comparisons already made on the path (**realizability**). The **cost** is the tree height (worst-case number of comparisons):

\[
S(n)=\min_{\text{realizable sorting trees }T}\ \mathrm{height}(T).
\]

**Information-theoretic lower bound.** A height-\(h\) binary tree has at most \(2^h\) leaves, and a sorting tree needs \(n!\) distinguishable outcomes, so

\[
S(n)\ \ge\ \lceil\log_2 n!\rceil .
\]

This bound is exact for many \(n\) but provably not all - the first failure is \(n=12\), where \(\lceil\log_2 12!\rceil = 29\) but \(S(12)=30\).

**Ford–Johnson upper bound.** Merge-insertion sort gives an explicit strategy of cost

\[
F(n)=\sum_{k=1}^{n}\left\lceil \log_2 \tfrac{3k}{4}\right\rceil ,
\]

which matches \(S(n)\) at every \(n\) where \(S(n)\) is known; but \(F\) is known **not** to be optimal for some larger \(n\) (the first known suboptimality is around \(n=47\)).

**Known values (to reproduce and re-verify).**

- \(S(n)=F(n)\) is proved for all \(n\le 18\) and for \(n=22\), with \(F(12)=30,\ F(13)=34,\ F(14)=38,\ F(15)=42,\ F(16)=46,\ F(17)=50,\ F(18)=54,\ F(22)=71\).
- \(S(12)=30>29=\lceil\log_2 12!\rceil\) is the first case exceeding the information-theoretic bound.
- The smallest open \(n\) is \(19\), where \(F(19)=58\) is conjectured but unproved optimal (*verify* the tabulated \(F\)-values before use).

**Conventions.**

- Only two-outcome comparisons are counted; the model is deterministic and adaptive (the next query may depend on all prior answers).
- "Realizable" excludes trees that branch on a comparison already implied by the transitive closure of earlier answers - such a branch has an empty child and is disallowed.
- \(S(n)\) is a worst-case (not average-case) measure; the average-comparison problem is distinct and out of scope here.

**Frontier adopted here.** Primary target: determine \(S(19)\), or certify a strictly improved bracket \(\lceil\log_2 19!\rceil\le S(19)\le F(19)\). Secondary: \(S(20),S(21)\), and \(n=23\). Re-verify the frontier against Section 4.

## 2. Resolution standard

Fix the smallest open \(n\) (currently \(19\)). A **resolution** produces the exact integer \(S(n)\) together with **both**, independently checked.

1. **Upper bound (strategy).** An explicit comparison decision tree of height \(S(n)\) sorting all \(n!\) permutations, validated by an independent program that (a) confirms every leaf's consistent permutation set, (b) confirms realizability at each node, and (c) confirms the induced partition of all \(n!\) permutations is complete and disjoint. A compact generator (Ford–Johnson when it attains the bound) is acceptable provided the validator expands and checks it.
2. **Lower bound (impossibility).** A certified proof of

\[
\nexists\ \text{realizable sorting tree } T \text{ on } n \text{ elements with } \mathrm{height}(T)\le S(n)-1 .
\]

   The named certified form is an **exhaustive minimax / adversary search with a replayable log**: a poset-based decision procedure (state = the partial order of comparisons made so far) proving that from the empty antichain no strategy forces all \(n!\) outcomes within \(S(n)-1\) comparisons, with (a) the state representation and pruning rules stated exactly, (b) memoized states hashed canonically up to isomorphism, and (c) an independent re-runner that replays the pruning decisions.

**Not accepted as resolution.**

- The information-theoretic value \(\lceil\log_2 n!\rceil\) reported as \(S(n)\) without a matching strategy at that height.
- A Ford–Johnson upper bound with no proof it is optimal at that \(n\).
- A lower bound from a search whose pruning (isomorphism reduction, dominance) is not soundness-argued or not replayable.
- A claim about "split-and-merge" or any restricted algorithm class presented as a bound on all comparison algorithms.
- A single lucky adversary line rather than a complete minimax over the strategy tree.
- A bound conditioned on an unproven structural assumption (e.g. that an optimal tree uses a particular first comparison pattern) without a coverage argument.

## 3. Graded partial-result targets

- **P1 - Reproduce the frontier.** Independently re-derive \(S(n)\) for a band up to \(n=18\) (and \(n=22\)) with our own realizability validator and minimax engine; confirm \(S(12)=30\).
  - *Certificate:* validated trees plus replayable lower-bound logs; SHA-256 manifest.
- **P2 - Sharpened lower bound at \(n=19\).** A certified proof that \(S(19)\ge \lceil\log_2 19!\rceil + c\) for the largest \(c\ge 0\) achievable, narrowing the bracket toward \(F(19)\).
  - *Certificate:* replayable exhaustive/adversary log with stated pruning and canonicalization.
- **P3 - Confirmed upper bound at \(n=19\).** Validation that \(F(19)\) is achievable, i.e. an explicit height-\(F(19)\) strategy passing the independent validator (rigorous reproduction of the standing upper bound).
  - *Certificate:* the validated decision tree with exact linear-extension accounting.
- **P4 - Improved upper bound at \(n=19\).** A realizable strategy of height \(F(19)-1\) if one exists - this would show Ford–Johnson is *not* optimal at \(19\) - fully validated.
  - *Certificate:* the validated tree and the leaf-partition check.
- **P5 - Full resolution of \(n=19\).** Matching P2 with P3 (or P2 with P4) to pin \(S(19)\) exactly per Section 2.
  - *Certificate:* both artifacts and a combined report stating the exact value.
- **P6 - Next instances.** Determine \(S(20)\) and/or \(S(21)\), or a certified bracket for \(n=23\), reusing the engine.
  - *Certificate:* per-\(n\) validated trees and lower-bound logs.
- **P7 - Formalized micro-result.** A machine-checked (Lean/Coq) proof of the decision-tree lower-bound framework, or of a single settled small value \(S(n)\), keeping generated search certificates outside the trusted base.
  - *Certificate:* the formal proof plus a small checker for the external search artifacts.

## 4. Known results and prior art

- **Foundations.** Ford and Johnson (~1959) - merge-insertion sort and \(F(n)\). Knuth, *TAOCP* Vol. 3, §5.3.1 - decision-tree formulation, the \(\lceil\log_2 n!\rceil\) bound, tables of \(S(n)\); Hadian–Sobel and Manacher on the asymptotic suboptimality of merge-insertion.
- **Exact values by \(n\).** \(S(n)=F(n)\) proved for \(n=12\) (Wells, ~1965), \(n=13\) (Kasai et al., ~1994), \(n=14,15,22\) (Peczarski, ~2004), and \(n=16,17,18\) (Stober and Weiss, ~2023, *verify*). \(S(16)=46\) settled a long-standing open case.
- **Suboptimality of Ford–Johnson.** Peczarski, "The Ford–Johnson algorithm still unbeaten for less than 47 elements" (~2007) - no split-and-merge algorithm beats \(F(n)\) for \(n<47\), and any improvement must use a genuinely different strategy. The first \(n\) with \(S(n)<F(n)\) is not pinned down.
- **Open cases.** Whether \(S(19)=F(19)\) is the classic smallest open instance; \(n=20,21\) and \(n\ge 23\) (except \(22\)) are open.
- **Search technique.** Peczarski and Stober–Weiss use poset-based minimax with isomorphism reduction and dominance pruning; exact linear-extension counting bounds the branching. OEIS A036604 tracks \(S(n)\).
- **Related measures.** The *average*-case comparison problem and the *insertion*/*merging* subproblems have their own literature (Knuth §5.3.1–5.3.2); they inform pruning but are not the worst-case \(S(n)\) targeted here.
- **Lower-bound theory.** The "information-theoretic + one" and Bender-style adversary arguments explain why \(S(12)>\lceil\log_2 12!\rceil\); the exact frontier beyond \(n=18\) rests entirely on exhaustive minimax rather than closed-form bounds.

**Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

**`[search]` - lower bound (the hard side).** Model the sorting game as a two-player minimax over *posets*.

1. A state is a partial order on the \(n\) elements (the comparisons made so far and their transitive closure).
2. A move picks an incomparable pair \((a,b)\); the adversary answers to keep the harder branch.
3. The algorithm wins within \(h\) if it can force every reachable state to a total order in \(\le h\) moves.
4. To prove \(S(n)\ge h+1\), show the root cannot be forced within \(h\). Solve by depth-limited minimax with canonical poset hashing (nauty on the Hasse diagram), memoization of solved states, and dominance pruning; log every pruning and memo decision for replay.

**`[search]` - upper bound.**

1. Take Ford–Johnson as the incumbent and reproduce its height-\(F(n)\) tree explicitly.
2. Identify the merge steps that dominate the comparison count (the binary-insertion of the "leftover" elements).
3. Search for height-\((F(n)-1)\) strategies by local modification and by exact SAT/ILP encodings of "a height-\(h\) realizable tree exists".
4. Validate every candidate structurally over the poset/decision-tree, counting linear extensions, rather than by brute-force enumeration of \(19!\approx1.2\times10^{17}\) permutations.

**Lower-bound certificate structure.** The replayable log records, for each visited state: its canonical key, the branching pair chosen, the adversary's forced child, and either a memo hit or the proof that no move forces a win within the remaining budget. The independent re-runner recomputes canonical keys and re-checks that every claimed "unwinnable within \(h\)" state indeed has no forcing move.

**Tools.**

- Search: custom C++ minimax with a canonical poset key.
- Canonicalization: nauty/Traces for Hasse-diagram canonical forms.
- Counting: exact linear-extension counting (DP over antichains) for small \(n\).
- Orchestration and cross-checks: Python/SageMath; optionally a SAT/ILP encoding of "a height-\(h\) realizable tree exists" for the upper-bound side.

**First concrete session steps.**

1. Build and validate the poset minimax on \(n\le 11\) against known \(S(n)\), confirming the engine and canonicalization.
2. Reproduce \(S(12)=30\) (the first super-information-theoretic case) as a correctness gate.
3. Reproduce \(S(16)=46\) and \(S(18)=54\) to confirm the engine scales to the published frontier.
4. Attack \(n=19\): first push the lower bound (P2), then reconcile with the \(F(19)\) upper bound (P3).
5. In parallel, probe for a height-\(57\) strategy (P4); a hit would be a historic disproof of Ford–Johnson optimality at \(19\) and must survive the full independent validator before any announcement.

**One-workstation scope and failure modes.** \(n\le 18\) is reproducible in reasonable time; \(n=19\) is at the edge and may not close on one machine. Dominant risks:

- State-space blow-up defeating memoization at \(n=19\).
- An unsound dominance rule making a hard state look easy - re-check flagged states without the rule.
- Canonicalization bugs collapsing non-isomorphic posets - dual-implement the poset key and cross-check.
- Linear-extension counting overflow or off-by-one at \(n=19\) - use exact big-integer arithmetic and validate counts against \(\sum_{\text{leaves}}1 = n!\).

Report an unclosed \(n=19\) honestly as a certified bracket (P2/P3), not as a resolution.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Upper bounds are exact decision trees validated by exhaustive structural checking and exact linear-extension counting; lower bounds are complete minimax searches with recorded pruning. No floating point enters a load-bearing claim.
2. **Independent verification.** The decision-tree validator and the linear-extension counter are implemented separately from the search engine; the poset canonicalization is dual-implemented (nauty vs a hand-rolled refinement) and cross-checked on all reached states up to a size cutoff; a sample of pruned states is re-solved without the pruning rule.
3. **Reproducibility.** State encoding, pruning/dominance rules, canonicalization method, memo hashing, and tool versions are recorded; a SHA-256 manifest covers the search logs and validated trees; the standing values \(S(n)\) reproduced or extended are cited with source and access date (OEIS A036604 and the primary papers).
4. **Preservation.** The minimax engine, the validator, the canonicalization code, and the full replay logs are part of the record; any log too large to store is reduced to a hash with the generating command preserved.
5. **Honest reporting.** The report states whether \(S(n)\) was pinned exactly at a new \(n\) or only bracketed; a Ford–Johnson upper bound is never reported as \(S(n)\) without a matching certified lower bound, and an unreplayable search is never represented as an optimality proof.
