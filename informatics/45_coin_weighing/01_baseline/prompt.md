# PROMPT FOR A CERTIFIED EXACT QUERY NUMBER IN SEARCHING WITH ERRORS

## The minimum number of queries in a Rényi–Ulam / coin-weighing problem, with a checked optimality certificate

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 45 of 50  
**Area:** search, sequences & games  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Combinatorial search with errors asks: how many queries must a Questioner ask to identify an unknown element of a finite set, when the Responder may lie (or answers are otherwise corrupted) up to \(e\) times? The two canonical families are the **Rényi–Ulam game** (an unknown \(x\in\{1,\dots,m\}\), yes/no or comparison questions, at most \(e\) mendacious answers) and **coin-weighing / counterfeit-coin** problems (identify defective coins using a balance or a subset-sum query). For many concrete \((m,e,\text{query-type})\) settings the exact minimum query number is unknown - the information-theoretic volume (sphere-packing) bound is not always tight, and the true optimum is settled only by search. This is a sharp fit for certified game-tree search: an optimal adaptive strategy is a finite decision tree that a checker can replay against every adversary response, and a lower bound is a checked adversary (weight-function) argument or an exhausted minimax. The verifier that closes the loop is a strategy-tree replayer (confirming the claimed query count identifies the secret against every legal error pattern) together with a lower-bound checker (a re-evaluated Berlekamp weight bound, or a replayable minimax completeness log). Anything short of a matched upper and lower bound for a specified instance - a strategy with no optimality proof, or a volume bound that does not meet a construction - is a partial result, never a solution.

## 1. Exact problem statement

Fix a finite **search space** \(S\) with \(|S|=m\); the Responder secretly fixes \(x^\star\in S\). A **query type** \(\mathcal Q\) is a family of admissible questions:

- **subset (membership) queries:** "Is \(x^\star\in A\)?" for \(A\subseteq S\);
- **comparison (threshold) queries:** "Is \(x^\star\le t\)?" (\(S\) linearly ordered);
- **balance weighings:** partition a chosen set of coins onto two pans; the answer is left-heavy / right-heavy / balanced;
- **subset-sum (counting) queries:** report the number of defectives in a chosen subset.

An **error model** bounds corruption: in the Rényi–Ulam game the Responder may return at most \(e\) false answers over the whole game (adaptive lies, \(e\) fixed in advance).

A **strategy** is adaptive: the \(k\)-th question may depend on all prior answers. It is a **winning** \(q\)-query strategy if, after at most \(q\) questions, the Questioner names \(x^\star\) correctly against every response sequence consistent with the error bound. Define

\[
N(\mathcal Q, m, e)=\min\{\,q : \text{a winning } q\text{-query strategy exists}\,\}.
\]

**Coin-weighing instances** are cast the same way: \(S\) is the set of possible defective-configurations (e.g. "exactly one heavy coin among \(n\)", or "an unknown subset of counterfeit coins"), \(\mathcal Q\) is the weighing family, \(e=0\) unless weighings themselves may err. Two reference cases anchor the family. The **counterfeit-coin** classic asks for the largest \(n\) identifiable (one defective of unknown heavier/lighter direction) in \(k\) balance weighings; the classical capacity is

\[
n \le \frac{3^k-3}{2},
\]

each weighing yielding one of three outcomes. The **Erdős–Rényi detecting-set** problem asks for the fewest subset-sum queries to identify a hidden subset \(T\subseteq[n]\), where the information bound gives \(q\ge n/\log_2 n\,(1+o(1))\) and exact small-\(n\) optima are open.

**Target.** Fix one concrete instance \((\mathcal Q, m, e)\) - the specific numbers are part of the session's declaration - and certify the exact value \(N(\mathcal Q,m,e)\). The cost measure is the number of queries; adaptivity, query type, and error model are fixed and stated. Adaptive and non-adaptive optima differ and must never be conflated.

**Decision form used by the search.** The optimum is bracketed by a monotone family of decision instances

\[
\mathrm{WIN}(\mathcal Q,m,e,q):\quad \text{does a winning } q\text{-query adaptive strategy exist?}
\]

satisfiable for \(q\ge N\) and unsatisfiable below; certifying \(N=q\) means a witness strategy for \(\mathrm{WIN}(\cdot,q)\) and a checked refutation of \(\mathrm{WIN}(\cdot,q-1)\).

A reader starting from this prompt alone has the search space, the query families, the error model, the notion of a winning strategy, the decision form, and the optimum \(N(\mathcal Q,m,e)\).

## 2. Resolution standard

**Named certified form: exhaustive game-tree (minimax) search with a checked optimality certificate.** A resolution of "\(N(\mathcal Q,m,e)=q\)" for a fixed instance consists of two independently checkable artifacts.

1. **Upper bound (a strategy).** An explicit adaptive decision tree of depth \(q\), given as data, together with a replayer that, for every leaf, confirms the surviving candidate set (the "state" - for Rényi–Ulam a Berlekamp state vector counting candidates by lies-used-so-far) is a singleton, against every legal answer sequence. The tree plus the replayer's accept is the certificate.
2. **Lower bound.** A machine-checked proof that no depth-\((q-1)\) strategy wins, delivered as either
   - (a) a checked **weight-function / volume argument** - the sphere-packing bound

     \[
     2^{q}\ \ge\ \sum_{x\in S}\sum_{i=0}^{e}\binom{q}{i},
     \]

     re-evaluated in exact integers, when it forces depth \(\ge q\); or
   - (b) an **exhausted minimax**: a complete game-tree search whose completeness log an independent driver replays, confirming every first-move-and-response branch forces depth \(\ge q\).

Both parts are mandatory: \(N=q\) is proven only when the strategy and the lower bound meet, and the checkers are written independently of the search.

**Not accepted as resolution.**

- The Berlekamp / volume bound presented as the answer when no matching strategy is exhibited (the bound is frequently *not* tight).
- A strategy that identifies the secret in \(q\) queries but with no proof that \(q-1\) is impossible.
- A non-adaptive (predetermined-question) result reported as the adaptive optimum, or vice versa.
- A heuristic or randomized strategy, an asymptotic query rate where an exact integer is asked, or a minimax run whose completeness cannot be independently replayed.
- Any claim resting on floating-point weight computations rather than exact integer arithmetic.

## 3. Graded partial-result targets

**P1 - Reproduce a settled value.** For a known instance (e.g. Rényi–Ulam with \(e=1\) or \(e=2\), a specific \(m\); or the classic 12-coin counterfeit problem), recompute \(N\) with our own toolchain: an explicit optimal strategy tree plus a checked lower bound.
*Certificate:* strategy replayer accept at depth \(q\); lower-bound checker (weight bound or exhausted minimax) at depth \(q-1\).

**P2 - Berlekamp-state harness.** Implement and validate the Berlekamp state / character-count machinery for the chosen error model, reproducing the volume bound exactly for a range of \((m,e)\).
*Certificate:* exact integer volume-bound table cross-checked against the literature.

**P3 - Exact value for an open instance.** For a specific \((\mathcal Q,m,e)\) whose optimum is not settled, certify \(N\) by matched construction and lower bound.
*Certificate:* both artifacts of §2 under a SHA-256 manifest; the gap-closing step documented.

**P4 - Tightness / non-tightness of the volume bound.** For a family of instances, certify exactly which \(m\) attain the Berlekamp bound and which force one extra query, with a strategy or an exhausted minimax at each boundary.
*Certificate:* per-\(m\) matched certificates; the character (borderline) set identified exactly.

**P5 - Coin-weighing optimum.** For a specific counterfeit or detecting-set instance, certify the exact number of weighings, with an explicit weighing schedule and a checked lower bound.
*Certificate:* schedule replayer accept plus lower-bound proof.

**P6 - Non-adaptive companion.** For the same instance, certify the non-adaptive (predetermined-batch) optimum and report the adaptive/non-adaptive gap exactly.
*Certificate:* an explicit query matrix with a separating (uniquely-decodable) proof, and a matching lower bound.

**P7 - Perfect/imperfect boundary.** For a fixed \(e\), certify exactly the set of \(m\) for which the game is perfect (sphere-packing bound attained) versus imperfect (one extra query forced), over a documented range.
*Certificate:* per-\(m\) matched strategy/lower-bound pair, with the boundary tabulated and hashed.

## 4. Known results and prior art

- The problem was posed by A. Rényi (~1961, search with a fixed fraction of lies) and popularized by S. Ulam (1976): find an integer in \([1,10^6]\) with one lie - the answer is 25, with 24 provably insufficient (verify both halves).
- Feedback / adaptive error-correction framing: E. Berlekamp (~1968); the state-vector "volume" bound and the weight (Berlekamp) function are the standard lower-bound tool.
- The comprehensive reference is A. Pelc, "Searching games with errors - fifty years of coping with liars," *Theoretical Computer Science* (~2002) - a taxonomy by query type, interactivity, and error model (verified title and venue).
- Exact solutions: \(e=1\) by A. Pelc (~1987), where for search space \(m\) the optimum is the least \(q\) with

  \[
  2^{q}\ \ge\ m\,(q+1),
  \]

  except for a small explicitly characterized set of \(m\) needing one more (verify the exceptional set); \(e=2\) completed by Czyzowicz–Mundici–Pelc (~1988–1990); larger fixed \(e\) treated by Cicalese, Deppe, Mundici and others; the "pathological liar game" values \(F^\ast_1, F^\ast_2\) by Spencer–Winkler / Ellis–Yan (verify each attribution and year).
- Coin weighing: the counterfeit-coin classic (Dyson, Grossman, ~1945); the Erdős–Rényi (~1963) and Lindström / Cantor–Mills detecting-matrix results for identifying a hidden subset by subset-sum queries; Bshouty and others on optimal non-adaptive schemes (verify).
- Query-type sensitivity: comparison-only (threshold) questions generally force more queries than arbitrary subset questions, and the two settings have separate exact-value literatures; a value proven for one type says nothing about the other.
- The half-lie and constrained-lie variants (the Responder may only err in one direction, or lies are weighted) have their own exact-value frontiers and distinct volume bounds (verify per variant).
- The information-theoretic sphere-packing lower bound (stated in §2) is classical but not always tight; the residual gap is exactly where exhaustive search earns its keep. Instances where equality holds are called *perfect*; the interesting instances are the imperfect ones forcing one extra query.

**Status as of mid-2026 - re-verify against the current literature (and record trackers) before starting any session.**

## 5. Attack plan

`[search]` - first computations on one workstation.

- **State model (P2).** Represent a Rényi–Ulam position by its Berlekamp state \((a_0,\dots,a_e)\), where \(a_i\) counts candidates that have already survived \(i\) lies. A subset query splits the state; the residual game is losable within \(q\) further questions only if the Berlekamp weight satisfies

  \[
  w_q(a_0,\dots,a_e)\ =\ \sum_{i=0}^{e} a_i \sum_{j=0}^{e-i}\binom{q}{j}\ \le\ 2^{q}.
  \]

  Implement \(w_q\) in exact integers; it is both the pruning heuristic and the lower-bound witness.
- **Reproduce (P1).** Build the known optimal strategy for \(e\le 2\) and for the 12-coin problem; replay every tree exhaustively; confirm the matching lower bound. This validates the state model and the replayer.
- **Exhaustive minimax (P3).** A custom C++ negamax over states with memoization (transposition table keyed by canonicalized state), iterative deepening on \(q\), and alpha-beta-style pruning that is *sound for exact optima*. Emit a completeness log recording, per explored state, the minimizing query and the maximizing response, so an independent replayer can confirm no branch was skipped.
- **Lower bounds.** Two independent routes: the exact weight/volume bound, and the exhausted minimax; require them to agree on every borderline instance. A SAT/ILP encoding of "a depth-\((q-1)\) strategy exists" (tree variables + covering constraints) gives a third, DRAT-checkable route for small instances.
- **Coin weighing (P5, P6).** Model weighings as ternary-outcome queries. For non-adaptive schemes, a query matrix \(M\in\{0,1\}^{q\times n}\) identifies every hidden subset iff the sums \(M\mathbf 1_T\) are distinct over all \(T\subseteq[n]\); i.e.

  \[
  M x = M y \ \Longrightarrow\ x=y \qquad (x,y\in\{0,1\}^n).
  \]

  Search for minimal such \(M\) (detecting matrices) with nauty-canonical deduplication and an exact distinctness check; use ILP for optimal weighing counts with exact duals.
- **Cross-checking bounds.** For each closed instance, require the volume bound, the exhausted minimax, and (where feasible) the SAT UNSAT route to agree; a disagreement is a bug, not a discovery, and halts the claim.
- **Symmetry and canonicalization.** Distinct positions frequently share a canonical Berlekamp state; keying the transposition table on the sorted/canonicalized state collapses the search dramatically. Any canonicalization must be proven to preserve game value, or it corrupts the optimum.
- **One-workstation scope and failure modes.** State-space growth is the wall: the number of reachable Berlekamp states explodes with \(m\) and \(e\), and minimax depth compounds it. Expect (i) memoization tables exceeding RAM (mitigate with canonical state keys and symmetry reduction); (ii) unsound pruning silently returning a non-optimal depth - every pruning rule must be proven exact-preserving; (iii) volume-bound over-trust when it is not tight; (iv) confusing adaptive with non-adaptive optima. Record the largest instance actually closed, not the largest attempted.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** All weight/volume arithmetic is in exact integers; every optimum rests on a replayable strategy tree and a checked lower bound (weight argument, exhausted minimax, or DRAT UNSAT). Floating point is for exploration only.
2. **Independent verification.** The strategy replayer, the minimax search, and the volume-bound evaluator are separate programs; each lower bound is confirmed by at least two of {weight bound, exhausted minimax, SAT UNSAT}; the strategy tree is replayed by code that shares no state with the search.
3. **Reproducibility.** The instance \((\mathcal Q,m,e)\), query encoding, state canonicalization, pruning rules, solver/search versions, and seeds are recorded; a SHA-256 manifest covers every tree, log, and proof. Any reproduced or extended prior value is cited with source and access date.
4. **Preservation.** Search, replayer, and bound-checker source are part of the record. Any discarded run or lost log is stated explicitly.
5. **Honest reporting.** The report states up front, per instance, whether both bounds were certified (hence \(N\) settled), the query type and error model, and whether the volume bound was tight. A strategy without a matching lower bound is reported as an upper bound only; an adaptive result is never presented as a non-adaptive one.
