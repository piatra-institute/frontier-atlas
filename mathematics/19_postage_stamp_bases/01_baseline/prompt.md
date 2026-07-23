# PROMPT FOR NEW EXTREMAL VALUES OF THE POSTAGE-STAMP FUNCTION \(n(h,k)\)

## Extremal additive bases and the \(h\)-range

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 19 of 50  
**Area:** additive & combinatorial number theory  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The postage-stamp problem asks, for a \(k\)-element set of denominations and a bound \(h\) on the number of stamps, how long an initial run of integers \(\{1,\dots,N\}\) can all be paid exactly; the extremal length is the postage-stamp function \(n(h,k)\). Exact values are known for small \(h,k\) from decades of branch-and-bound computation (Stöhr, Selmer, Mrose, Mossige, Challis), and many pairs \((h,k)\) remain open. The problem has exact, machine-checkable ground truth: the \(h\)-range of a fixed basis is verified by a cheap reachability computation, and optimality over all \(k\)-bases is an exhaustive search with an infeasibility / completeness certificate - a clean fit for certified branch-and-bound on one workstation.

Full "resolution" is per-\((h,k)\): the deliverable is the exact value \(n(h,k)\) for an open pair, with an extremal basis and a completeness proof. The resolution standard in section 2 is the target for the chosen pair; a good basis without a matching optimality certificate is reported as a lower bound only, never as the value.

## 1. Exact problem statement

An **additive basis** of \(k\) denominations is a set

\[
A=\{a_1,\dots,a_k\}\subseteq\mathbb{Z}_{>0},\qquad a_1=1<a_2<\dots<a_k,
\]

where \(a_1=1\) is forced, since \(1\) must be payable. For an order \(h\ge1\), the set of values payable with **at most \(h\) stamps** (denominations reusable) is

\[
S_h(A)=\Bigl\{\textstyle\sum_{i=1}^k c_i a_i \ :\ c_i\in\mathbb{Z}_{\ge0},\ \textstyle\sum_i c_i\le h\Bigr\}.
\]

The **\(h\)-range** of \(A\) is the largest initial run it covers,

\[
n(h,A)=\max\{N\ge0:\ \{1,2,\dots,N\}\subseteq S_h(A)\},
\]

and the **postage-stamp function** (global / extremal form) is

\[
n(h,k)=\max\{\,n(h,A):\ |A|=k,\ 1\in A\,\}.
\]

A basis attaining the maximum is an **extremal \((h,k)\)-basis**.

**Normalizations fixed here.**
- Denominations are strictly increasing with \(a_1=1\).
- "At most \(h\) stamps" means \(0\le\sum_i c_i\le h\).
- This is the *global* postage-stamp problem; the *local* variant, which fixes the largest denomination, is not the object here.

The known small-case tables use exactly this convention.

**Elementary bounds.** Two facts frame the search. A crude upper bound counts representations:

\[
n(h,k)\ \le\ \binom{h+k}{k}-1,
\]

since at most \(\binom{h+k}{k}\) multisets of \(\le h\) stamps from \(k\) denominations exist (including the empty sum for \(0\)). A crude lower bound comes from the greedy / powers basis: with \(a_i=(h+1)^{\,i-1}\), every value below \((h+1)^k\) that is base-\((h+1)\) representable with digit sum \(\le h\) is reachable, so \(n(h,k)\) grows at least polynomially in \(h\) for fixed \(k\). Extremal bases beat both; closing the gap is the computational content.

**The open determination.** For a specified currently-open pair \((h,k)\), compute the exact integer \(n(h,k)\), together with an extremal basis and a proof that no \(k\)-basis does better. No informal target ("a strong basis") is accepted.

## 2. Resolution standard

Because \(n(h,k)\) is a family, the resolution standard is stated per target pair \((h,k)\). A complete resolution of one open pair is the exact value \(n(h,k)=N\), delivered as an **extremal-basis certificate**, namely both of the following.

1. **Lower witness.** An explicit basis \(A^\star\) with \(n(h,A^\star)=N\), certified by a **reachability proof**: a dynamic-programming computation of the minimum stamp count

\[
w(m)=\min\Bigl\{\textstyle\sum_i c_i \ :\ \textstyle\sum_i c_i a_i=m,\ c_i\in\mathbb{Z}_{\ge0}\Bigr\}
\]

for \(m=0,1,\dots,N+1\), showing \(w(m)\le h\) for all \(m\le N\) and \(w(N+1)>h\).

2. **Upper witness.** A proof that no \(k\)-basis exceeds \(N\), by an **exhaustive branch-and-bound** over admissible bases (canonical increasing order, standard admissibility pruning), whose completeness is argued and whose search is replayable - or an integer-program infeasibility certificate that "some \(k\)-basis has \(h\)-range \(\ge N+1\)" is infeasible.

**Not accepted as resolution.**
- A basis with a large \(h\)-range but no matching optimality proof (a lower bound only).
- A value from an incomplete heuristic or randomized search, or a truncated branch-and-bound whose pruning is not justified.
- An ILP objective value without an independently checkable infeasibility / completeness certificate.
- An asymptotic formula \(n(h,k)\sim(\cdot)\) presented as an exact value.

## 3. Graded partial-result targets

- **\(P_1\) - reproduce a known frontier.** Recompute a published row or column of the table (e.g. the closed forms for \(k=2,3\), or a full block of Challis / Mossige values) with our own verified reachability + branch-and-bound.
  - *Certificate:* extremal bases + reachability logs + completeness argument, matching the literature.

- **\(P_2\) - certify one new open value.** For the smallest currently-open \((h,k)\), produce \(n(h,k)\) with an extremal-basis certificate.
  - *Certificate:* the full section-2 artifact.

- **\(P_3\) - extend a row or column.** Add one new certified value along fixed \(k\) (increasing \(h\)) or fixed \(h\) (increasing \(k\)).
  - *Certificate:* as \(P_2\), plus the boundary case that was previously the frontier.

- **\(P_4\) - improve a lower bound where optimality is out of reach.** For a large \((h,k)\) beyond exhaustive search, a certified \(h\)-range value for an explicit good basis (reachability-verified), reported as a lower bound on \(n(h,k)\).
  - *Certificate:* basis + reachability proof; optimality explicitly not claimed.

- **\(P_5\) - mine structure and certify a construction.** From extremal bases, extract a parametric construction (e.g. regular / arithmetic-progression bases) and certify an improved asymptotic lower bound on \(n(h,k)/k\) or \(n(h,k)/h\).
  - *Certificate:* the construction + a proof of its \(h\)-range for all parameters.

- **\(P_6\) - settle a long-standing open pair.** Both bounds for a specific pair singled out in the literature.
  - *Certificate:* the section-2 artifact with a completeness proof at scale.

## 4. Known results and prior art

- Rohrbach (1937) posed the additive-basis extremal question; Stöhr (1955) gave the general framework and closed forms for small \(k\).
- Selmer's work (*The local postage stamp problem*, ~1980s) and Mrose (~1979) supplied lower-bound constructions.
- Extensive exact computation: **Challis (1993)** tabulated \(n(h,k)\) for many \((h,k)\); **Mossige** (1981, 1987, 1998) computed further rows / columns by branch-and-bound; Kløve, Kirfel, and others extended the tables.
- Closed forms are known for \(k=2\) and \(k=3\) (Stöhr, Hofmeister); for larger \(k\), most values are computational, and the frontier is bounded by the feasibility of the exhaustive search.
- Related: Graham–Sloane (1980) on additive bases; the Erdős–Turán additive-basis question (a distinct problem - boundedness of the representation function for asymptotic bases).
- OEIS records the extremal values by row and column (the sequences for fixed small \(h\) and for fixed small \(k\); confirm the exact A-numbers before citing).

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Identify precisely which \((h,k)\) are open and what the current record bases and bounds are; the exhaustive frontier advances with hardware.

## 5. Attack plan

`[search]` on a single workstation.

**Reachability - the easy, always-certified half.** For a fixed basis \(A\), compute \(w(m)\) by a coin-problem DP:

\[
w(0)=0,\qquad w(m)=1+\min_{a\in A,\ a\le m} w(m-a),
\]

scanning \(m\) upward until \(w(m)>h\); the last \(m\) with \(w(m)\le h\) is \(n(h,A)\). Cost is \(O(N\cdot k)\) in exact integers.

**Exhaustive branch-and-bound - the hard half.** Generate candidate bases in strictly increasing order with **admissibility pruning**: given a partial basis \(\{a_1,\dots,a_j\}\) with current \(h\)-range \(r_j\), the next denomination must satisfy

\[
a_{j+1}\le r_j+1
\]

(else a gap at \(r_j+1\) is unavoidable), and upper bounds on \(n(h,k)\) - e.g.

\[
n(h,k)\ \le\ \binom{h+k}{k}-1,
\]

together with sharper counting / regular-basis bounds - prune branches that cannot beat the incumbent. Run depth-first with the incumbent best value, and record the completed search tree (or a summary sufficient to replay it). An ILP alternative maximizes \(N\) with variables encoding both the basis and per-value representations; extract an infeasibility certificate for the upper bound.

**Symmetry and canonicity.** Bases are ordered sets, so the only symmetry is the ordering itself; canonical (increasing) generation avoids duplicates without `nauty`. Care is needed only to prune equivalent partial extensions.

**Scope and failure modes.** The reachability half is trivial and always certifiable. Exhaustive optimality is feasible for small \(k\) (say \(k\le 7\)–\(8\)) and moderate \(h\), but the admissible-basis tree grows super-polynomially - be explicit about which \((h,k)\) are within reach on one workstation. Expected failure modes:
- branch-and-bound blow-up at the chosen \((h,k)\);
- weak pruning bounds leaving too many branches;
- an incumbent found quickly but the optimality proof (the completeness sweep) intractable - in which case fall back to \(P_4\) (a certified lower bound).

## 6. Verification and auditability requirements

1. **Exact or certified computation.** All arithmetic is exact integer; \(h\)-ranges are computed by the DP above and rechecked; upper bounds rest on a replayable exhaustive search or an exact ILP infeasibility certificate. Floating point is exploration only.
2. **Independent verification.** A standalone reachability checker (independent of the search code) re-verifies each extremal basis's \(h\)-range and the failure at \(N+1\); the exhaustive completeness is re-argued and, where feasible, replayed by a second implementation. Dual DP formulations (forward coin-DP vs. bounded-summand enumeration) cross-check \(n(h,A)\).
3. **Reproducibility.** Search order, pruning bounds, admissibility rules, incumbent updates, and any parallel partitioning are recorded; a SHA-256 manifest spans basis files, search logs, and code.
4. **Preservation.** The branch-and-bound and reachability source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).
5. **Honest reporting.** The report states up front, per target pair, whether \(n(h,k)\) was determined (both bounds) or only a lower bound established, and never presents a good basis or an incomplete search as the exact value.
