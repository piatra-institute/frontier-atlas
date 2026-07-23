# PROMPT FOR ADVANCING SINGMASTER'S MULTIPLICITY CONJECTURE

## Boundedness of \(N(a)\), the number of appearances of \(a\) in Pascal's triangle

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 21 of 50  
**Area:** additive & combinatorial number theory  
**Modes:** `[proof]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Singmaster's conjecture asserts that the number of times an integer \(a>1\) occurs in Pascal's triangle is bounded by an absolute constant, independent of \(a\). The best unconditional bound is

\[
N(a)=O\!\left(\frac{\log a}{\log\log a}\right),
\]

which is *not* a constant, and the strongest recent progress bounds occurrences in the *interior* of the triangle. The largest known multiplicity is \(8\), attained only by \(3003\); infinitely many integers occur at least \(6\) times, from a Pell-equation family; no integer is known to occur more than \(8\) times.

The problem is matched to exact Diophantine search - streaming Pascal's triangle to a large bound and detecting exact collisions - and to symbolic solution of equal-binomial equations reducible to Pell / elliptic curves. **Full resolution is a famous hard problem and is not the expected product**; the graded targets of section 3 - certified censuses and family constructions - are. The resolution standard in section 2 is the target, and any finite-range census or interior bound is reported as a partial result, never as proving the conjecture.

## 1. Exact problem statement

For an integer \(a>1\), define the **multiplicity**

\[
N(a)=\#\bigl\{(n,k)\in\mathbb{Z}^2:\ 0\le k\le n,\ \tbinom{n}{k}=a\bigr\}.
\]

**Counting convention.** Each pair \((n,k)\) is counted, so the two edge occurrences

\[
\binom{a}{1}=\binom{a}{a-1}=a
\]

contribute, while the value \(1\) is excluded (\(1=\binom n0=\binom nn\) occurs infinitely often - which is why \(a>1\)). Every \(a>1\) therefore has \(N(a)\ge2\); the **interior** occurrences are those with \(2\le k\le n-2\).

**Singmaster's conjecture.** There is an absolute constant \(C\) with

\[
N(a)\le C\quad\text{for all }a>1,\qquad\text{equivalently}\qquad \sup_{a>1}N(a)<\infty .
\]

Occurrences beyond the edges come from **collisions** of binomial coefficients: nontrivial solutions of

\[
\binom{n}{k}=\binom{m}{j},\qquad 2\le k\le n/2,\ 2\le j\le m/2,\ (n,k)\ne(m,j),
\]

and of \(\binom{n}{k}=a\) for a fixed target \(a\). By the symmetry \(\binom nk=\binom n{n-k}\), occurrences pair up except on the central column.

**Adopted formulation and admissible advances.** The determination is a proof that \(\sup_a N(a)<\infty\). Admissible partial advances are:
- (a) a certified census of \(N(a)\) for all \(a\le X\), establishing multiplicity records and ruling out \(N(a)\ge m\) in the range;
- (b) certified resolution of specific equal-binomial Diophantine equations;
- (c) certified construction of an infinite family of prescribed multiplicity.

No informal target is accepted.

## 2. Resolution standard

A complete resolution is a proof that \(N(a)\le C\) for an explicit absolute constant \(C\), for **all** \(a>1\), delivered as a **Lean 4 + mathlib** formal proof or an equivalently rigorous, fully checkable argument.

**Named certified form for the search side.** A **multiplicity certificate** to bound \(X\): the exact multiset of all \(a\le X\) with \(N(a)\ge3\), each with its explicit list of witnessing pairs \((n,k)\), **together with a completeness proof** that the search examined every \((n,k)\) with \(\binom nk\le X\). Completeness follows from monotonicity: for fixed \(k\ge1\), \(\binom nk\) is strictly increasing in \(n\), so only \(n\) up to an explicit bound per \(k\) can contribute, and only

\[
k\ \le\ \log_2 X
\]

rows are nonempty; the certificate records these bounds and the row-by-row exhaustion.

**Not accepted as resolution.**
- A finite-range census (e.g. "no \(a\le X\) has \(N(a)\ge9\)") presented as a proof of the conjecture.
- The unconditional bound \(N(a)=O(\log a/\log\log a)\), or any non-constant bound, presented as resolution.
- An interior-only bound (bounded occurrences away from the edges) presented as the full conjecture.
- A single high-multiplicity example, or a family construction, presented as a structural boundedness proof.
- Any floating-point equality of binomial coefficients used as certification (exact bignum comparison is required).

## 3. Graded partial-result targets

- **\(P_1\) - reproduce the census.** A certified search over Pascal's triangle to a modest bound \(X\), recovering the known records: \(3003\) with \(N=8\); the numbers with \(N\ge6\) - e.g. \(120,\ 210,\ 1540,\ 7140,\ 11628,\ 24310\) - and their witnesses.
  - *Certificate:* the multiplicity certificate with a completeness proof to \(X\).

- **\(P_2\) - extend the census.** Push the certified census to a new bound \(X\), confirming no \(a\le X\) has \(N(a)\ge9\) (or reporting a new record), with a replayable certificate.
  - *Certificate:* streamed row-by-row exhaustion + independent recheck of every collision.

- **\(P_3\) - certify the infinite \(\ge6\) family.** Give the exact parametrization of the family with \(N(a)\ge6\) arising from

\[
\binom{n}{k}=\binom{n+1}{k-1}
\]

(equivalently the associated Pell equation / Fibonacci indexing) and prove it yields infinitely many distinct \(a\).
  - *Certificate:* closed-form family + a proof (ideally Lean-formalized) of infinitude and of multiplicity \(\ge6\).

- **\(P_4\) - resolve equal-binomial equations.** For specified shapes - e.g.

\[
\binom n2=\binom m3,\quad \binom n2=\binom m4,\quad \binom n3=\binom m4,\quad \binom{n}{k}=\binom{n+1}{k-1}
\]

- certify **all** integer solutions using the known reductions to Pell / Mordell / elliptic curves, with integral-point computations rechecked.
  - *Certificate:* the curve models + certified integral-point sets.

- **\(P_5\) - quantify interior occurrences.** Reproduce and, over explicit ranges, sharpen the interior bound (bounded number of solutions with \(k\) not too close to the edge), turning the analytic statement into certified finite-range counts.
  - *Certificate:* explicit-range enumeration matching the interior theorem's regime.

- **\(P_6\) - strongest short of resolution.** A Lean-formalized proof of the best known unconditional multiplicity bound, or of \(P_3\)/\(P_4\). The full boundedness proof is a windfall.

## 4. Known results and prior art

- Singmaster (1971) posed the conjecture and observed the infinite family with \(N(a)\ge6\) via \(\binom nk=\binom{n+1}{k-1}\), which reduces to a Pell equation with Fibonacci-indexed solutions (yielding, e.g., the large value \(61218182743304701891431482520\) occurring \(\ge6\) times).
- Abbott–Erdős–Hanson (1974): \(N(a)=O(\log a/\log\log a)\); Kane (~2007, verify) improved the implied factor.
- **Matomäki–Radziwiłł–Shao–Tao–Teräväinen (2022)**, *Singmaster's Conjecture in the Interior of Pascal's Triangle* (Quarterly J. Math.; arXiv 2106.03335, June 2021): via exponential sums over primes, at most a bounded number of solutions (four, or two per half of the triangle) lie in an explicit interior region. (Note: this is Radziwiłł, the analytic number theorist - not Radziszowski of the Ramsey program.)
- de Weger (1997) and others on equal binomial coefficients \(\binom nk=\binom ml\): effective / explicit resolution of several equation shapes via Pell and elliptic curves.
- \(3003\) is the unique known integer with \(N=8\):

\[
\binom{3003}{1}=\binom{78}{2}=\binom{15}{5}=\binom{14}{6},
\]

with symmetric partners; no integer is known with \(N>8\).
- OEIS: **A003015** (numbers occurring \(\ge5\) times in Pascal's triangle) and related sequences for \(\ge6\) and for exactly-\(k\) occurrences (confirm the exact A-numbers).

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Confirm the current census bound \(X\), whether any integer with \(N>8\) has been found, and any refinement of the interior bound.

## 5. Attack plan

`[search]` and `[proof]` on a single workstation.

**Streaming census `[search]`.** Enumerate \(\binom nk\) for \(2\le k\le n/2\) with \(\binom nk\le X\); for fixed \(k\), \(n\) ranges up to the solution of \(\binom nk=X\) (a bounded, computable range), and \(k\le\log_2 X\). Store values in a disk-backed hash / external sort keyed by the exact bignum (GMP/FLINT), then detect equal keys as collisions. The computation is memory-light and embarrassingly streamable, so very large \(X\) - well past \(10^{18}\), into \(10^{30}\)+ with external sorting - is reachable. Every detected equality is re-verified by exact bignum comparison; hash agreement alone is never trusted.

**Equal-binomial equations `[sym]`.** For fixed small \((k,j)\), the equation \(\binom nk=\binom mj\) is a curve in \((n,m)\); reduce to Pell equations (degree-2 cases) or to integral points on genus-1 curves - e.g. \(\binom n2=\binom m3\) - and compute all integral points with Pari/GP or SageMath (elliptic-curve integral-point routines). The family \(\binom nk=\binom{n+1}{k-1}\) gives

\[
k(n+1-k)=(k-1)(n+2-k)\ \Longrightarrow\ \text{a Pell relation},
\]

with an explicit fundamental solution - the source of the infinite \(\ge6\) family.

**Formalization `[proof]`.** Lean 4 + mathlib for the family construction (\(P_3\)) and for any finite equal-binomial resolution (\(P_4\)); these are finite algebraic / inductive facts suited to a proof assistant.

**Scope and failure modes.** The census is the most scalable line: exact, streamable, fully certifiable to large \(X\) on one workstation, with the only real cost being external-sort I/O. Equal-binomial curves of low degree are tractable with standard integral-point machinery. **Honest barrier:** the full conjecture is out of reach - bounding \(N(a)\) uniformly is exactly the open problem, and the interior theorem does not control occurrences near the edges. Expected failure modes:
- hash false positives (mitigated by exact recheck);
- curves of higher genus without effective integral-point algorithms;
- the census confirming boundedness empirically but never proving it.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** All binomial coefficients and equalities are exact bignum computations; collisions are confirmed by exact comparison, never by hash or floating point. Equal-binomial solution sets rest on certified integral-point computations.
2. **Independent verification.** A standalone census checker (recompute each reported witness's \(\binom nk\) and confirm the claimed multiplicity), written separately from the search; for formal targets, the Lean kernel is the independent checker; integral-point sets are re-verified by a second CAS where feasible.
3. **Reproducibility.** The bound \(X\), the per-\(k\) \(n\)-ranges, the external-sort / hashing scheme, seeds, and library versions are recorded; a SHA-256 manifest spans the collision logs, witness lists, curve models, and code.
4. **Preservation.** The census and Diophantine-search source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).
5. **Honest reporting.** The report states up front that the conjecture was not proved (unless it genuinely was), and reports a census bound, an interior-range count, or a family construction as exactly that - never as establishing \(\sup_a N(a)<\infty\).
