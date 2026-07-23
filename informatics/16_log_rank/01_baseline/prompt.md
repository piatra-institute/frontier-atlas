# PROMPT FOR CERTIFIED SMALL-CASE DETERMINISTIC COMMUNICATION COMPLEXITY VERSUS MATRIX RANK

## Exact \(D(f)\) and improved log-rank separations for explicit small Boolean matrices

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 16 of 50
**Area:** complexity & communication
**Modes:** `[search]` `[opt]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The log-rank conjecture asserts that the deterministic two-party communication complexity of a Boolean function is polylogarithmic in the rank of its communication matrix: \(D(f)=(\log \operatorname{rank} M_f)^{O(1)}\). Despite four decades of work the gap between the best upper bound, \(D(f)=O(\sqrt{\operatorname{rank}}\,)\), and the best separation, \(D(f)\ge(\log\operatorname{rank})^{\log_3 6}\), remains enormous; the conjecture is one of the central open problems of communication complexity, with direct bearing on circuit lower bounds, the communication analogues of the polynomial hierarchy, and matrix-analytic questions (chromatic number of low-rank graphs, matrix discrepancy). This prompt does not ask for the conjecture. It asks for the *certifiable* by-product that current machine methods can actually deliver: the **exact** deterministic communication complexity of explicit small communication matrices, computed by exhaustive protocol-partition search with an independently checked matching lower bound, together with any small-case *separation* whose \(D\) value and rank are both certified exactly. The on-machine verifier that closes the loop is a protocol-tree replayer paired with an exact rational rectangle-cover / rank lower-bound certificate. Anything short of the section-2 standard - a numerical rank, a protocol with no matching lower bound, an asymptotic gesture - is a partial result, never a solution.

## 1. Exact problem statement

Fix finite sets \(X,Y\) and a function \(f:X\times Y\to\{0,1\}\). Its **communication matrix** is

\[
M_f\in\{0,1\}^{X\times Y},\qquad (M_f)_{x,y}=f(x,y).
\]

**Deterministic protocol.** A deterministic protocol \(\Pi\) is a finite binary tree; each internal node is owned by Alice (who knows \(x\)) or Bob (who knows \(y\)) and is labelled by a function of that party's input choosing the child; each leaf is labelled \(0\) or \(1\). The protocol computes \(f\) if for every \((x,y)\) the leaf reached outputs \(f(x,y)\). The **cost** of \(\Pi\) is the depth of the tree (worst-case number of bits exchanged). The **deterministic communication complexity** is

\[
D(f)=\min_{\Pi\ \text{computes}\ f}\operatorname{depth}(\Pi).
\]

Equivalently, a protocol of cost \(c\) induces a partition of \(X\times Y\) into at most \(2^c\) **monochromatic combinatorial rectangles** \(R=A\times B\) (\(A\subseteq X,\ B\subseteq Y\)) obtained by a sequence of row- or column-splits. \(D(f)\) is the minimum depth of such a **split-tree** (partition) refinement - strictly stronger than the unrestricted monochromatic partition number \(\chi(f)\), for which

\[
\log_2\chi(f)\ \le\ D(f)\ \le\ O\!\big((\log\chi(f))^2\big).
\]

**Rank.** \(\operatorname{rank}(M_f)\) is taken **over \(\mathbb{Q}\)** (the real rank) as the primary measure; the field-\(\mathbb{F}_2\) rank and the nonnegative rank are recorded separately, since the conjecture is customarily stated for the real rank and the log-rank statement is field-sensitive. The universal lower bound

\[
D(f)\ \ge\ \log_2\operatorname{rank}(M_f)
\]

holds over any field.

**The open question (as adopted here).** Determine whether there is an absolute constant \(c\) with \(D(f)\le C\,(\log_2\operatorname{rank} M_f)^c\) for all \(f\), and pin down the least admissible exponent. The two live numerical anchors are the **separation exponent**

\[
\alpha^\*=\sup_f \frac{\log D(f)}{\log\log\operatorname{rank} M_f}\ \ge\ \log_3 6\approx 1.631,
\]

and the **upper-bound exponent** \(\beta\) in \(D(f)=O(\operatorname{rank}^{\beta})\), known to satisfy \(\beta\le 1/2\).

**Starting from the prompt alone.** A reader with this document reconstructs \(M_f\) from a truth table, computes \(D(f)\) by the split-tree definition, computes \(\operatorname{rank}\) over \(\mathbb{Q}\) and \(\mathbb{F}_2\), and checks \(D\ge\log_2\operatorname{rank}\). No external state is presumed.

## 2. Resolution standard

Full resolution is either (i) a proof that some absolute constant \(c\) works for all \(f\) (the conjecture), or (ii) a construction of an explicit family with \(D(f)\ge (\log\operatorname{rank})^{\omega(1)}\), i.e. super-polylogarithmic, refuting it. Neither is expected in a session; both, if approached, must arrive in **certified form**.

**Named certified form.** For any load-bearing exact value of \(D(f)\):

- an **upper bound** given as an explicit protocol split-tree, serialized node-by-node, replayed by an independent checker over all \(|X|\cdot|Y|\) inputs to confirm correctness and depth; and

- a **matching lower bound** given as an **exact rational linear-programming certificate** for the fractional rectangle-cover / partition bound, or a fooling-set / rank certificate, such that no split-tree of depth \(D-1\) exists.

The rank is certified by exact integer/rational Gaussian elimination, never by floating point. A claimed *separation* is certified only when both the \(D\)-value (both directions) and \(\operatorname{rank}\) are exact.

**Not accepted as resolution.**

- A numerically estimated rank or singular-value threshold in place of exact rank over a stated field.

- A protocol (upper bound) with no matching lower bound, or a lower bound with no protocol - one side of the equality is not the exact value.

- The unrestricted partition number \(\log\chi(f)\) reported as \(D(f)\); they differ and the split-tree constraint is mandatory.

- An unreplayable solver run, or a protocol tree that the independent checker cannot re-evaluate to the claimed depth on every input.

- Asymptotic hand-waving (\(\tilde O,\ \Omega\)) where an exact small-case value is requested.

- A single hand-built matrix whose "separation" is not certified in both directions.

## 3. Graded partial-result targets

Each target names its certificate. P1–P3 rebuild the frontier with our own verified toolchain; P4–P6 are the realistic strong products.

- **P1 - Exhaustive exact \(D\) versus rank for tiny domains.** Compute exact \(D(f)\) for **all** \(f:\{0,1\}^2\times\{0,1\}^2\to\{0,1\}\) (the \(2^{16}\) Boolean \(4\times4\) matrices, reduced by row/column permutation and complement symmetry) and tabulate \((D,\operatorname{rank}_\mathbb{Q},\operatorname{rank}_{\mathbb{F}_2})\).
  *Certificate:* per-class protocol tree + LP lower bound + exact ranks; a manifest listing every symmetry class and its exact triple.

- **P2 - Canonical hard families at small \(n\).** Certify exact \(D\) and rank for `EQ`\(_n\) (equality), `GT`\(_n\) (greater-than), `DISJ`\(_n\) (set-disjointness), and inner-product `IP`\(_n\) for \(n\) up to the reach of exhaustive search (target \(n\le 5\), i.e. \(32\times32\)).
  *Certificate:* matching protocol/LP pair per instance; comparison of \(D\) against \(\log_2\operatorname{rank}\).

- **P3 - Reproduce the Nisan–Wigderson/Kushilevitz separation at explicit sizes.** Build the recursive gadget construction at levels \(k=1,2,3,\dots\), compute exact \(\operatorname{rank}\) and a certified lower bound on \(D\), and confirm the ratio \(\log D/\log\log\operatorname{rank}\) approaching \(\log_3 6\) at finite size.
  *Certificate:* exact rank per level, certified \(D\) lower bound per level, tabulated ratios.

- **P4 - Improved small-case separation ratio.** Exhibit an explicit matrix (any construction, any reachable size) with a strictly larger certified value of \(D(f)/(\log_2\operatorname{rank})^{\log_3 6}\) than the best small instance in P3.
  *Certificate:* exact rank + two-sided certified \(D\); a diff against the P3 record with source and size.

- **P5 - Certified low-rank upper-bound witnesses.** For a family of communication matrices of exact rank \(r\), exhibit and replay a protocol of cost \(O(\sqrt r)\) (matching Lovett / Sudakov–Tomon at the constant level for small \(r\)), and certify optimality where the search closes.
  *Certificate:* protocol tree + LP lower bound establishing the exact \(D\) for each \(r\) in range.

- **P6 - Push exact \(D\) to \(8\times8\) and \(16\times16\).** Extend the exhaustive/branch-and-bound protocol search to selected \(64\)- and \(256\)-input matrices with certified two-sided \(D\), reporting the largest matrices for which \(D\) is now known exactly.
  *Certificate:* protocol tree + LP/rank lower bound + resource log; explicit statement of which classes closed and which timed out.

## 4. Known results and prior art

- Lower bound \(D(f)\ge\log_2\operatorname{rank}(M_f)\) and the log-rank conjecture: Lovász–Saks (1988, verify) posed the polylog form; the conjecture is standardly attributed to this line.

- Best deterministic **upper bound** in terms of rank: Lovett (\(\approx\)2014–2016, verify) proved \(D(f)=O(\sqrt{\operatorname{rank}}\,\log\operatorname{rank})\); the log factor was subsequently removed to \(O(\sqrt{\operatorname{rank}}\,)\) by Sudakov–Tomon ("Matrix discrepancy and the log-rank conjecture," arXiv 2311.18524, \(\approx\)2023, verify). A direct proof of Lovett's bound is due to Rothvoss (\(\approx\)2014, verify).

- Best **separation** (lower bound on \(D\) in terms of log-rank): Nisan–Wigderson (\(\approx\)1995, verify) constructed \(f\) with \(D(f)\ge(\log\operatorname{rank})^{\log_3 6}\), \(\log_3 6\approx1.631\); the base gadget/constant refinement is often credited to Kushilevitz (verify). Göös–Pitassi–Watson (\(\approx\)2015–2018, verify) established related deterministic-vs-partition and rank separations in the query/communication lifting framework.

- Equivalent formulations and the corruption/discrepancy route: Gavinsky–Lovett and others on equivalent forms of log-rank (verify); a 2024–2025 line "The Log-Rank Conjecture: New Equivalent Formulations" (arXiv 2510.02583, verify) restates it via matrix parameters. Treat all such reformulations as inputs, not settled facts.

- Related but distinct: the **approximate**-rank / log-approximate-rank conjecture was **refuted** by Chattopadhyay–Mande–Sherstov (\(\approx\)2019, verify). This is a different (randomized/approximate) statement; do not conflate it with the deterministic log-rank conjecture, which remains open.

- Exact small-case \(D\): scattered in textbooks (Kushilevitz–Nisan) as worked examples; no systematic certified census of exact \(D\) versus rank for all small matrices is standard - that census is the P1 product.

**Status as of mid-2026 - re-verify against the current literature before starting any session.**

## 5. Attack plan

**`[search]` - exact \(D\) by protocol-partition search.** Implement, in custom C++, a memoized recursion over subrectangles: a state is a pair (row subset \(A\), column subset \(B\));

\[
\mathrm{cost}(A,B)=
\begin{cases}
0 & f\ \text{constant on}\ A\times B,\\[2pt]
1+\min\big(\text{Alice-split},\ \text{Bob-split}\big) & \text{otherwise,}
\end{cases}
\]

where an Alice-split minimizes \(\max(\mathrm{cost}(A_0,B),\mathrm{cost}(A_1,B))\) over partitions \(A=A_0\sqcup A_1\), and a Bob-split symmetrically over \(B=B_0\sqcup B_1\). Prune with the \(\log_2\operatorname{rank}\) and fooling-set lower bounds and with branch-and-bound against the incumbent. For \(4\times4\) and \(8\times8\) this closes; for \(16\times16\) use canonical-form dedup (row/column permutation, complement) and best-first search. Emit the optimal split-tree.

**Lower-bound certificates.** For each closed instance produce an exact rational LP certificate for the fractional rectangle-cover bound (`QSopt_ex`/`SoPlex`/`SCIP` exact mode), and/or an explicit fooling set, so the lower bound is independent of the search that found the protocol.

**Exact rank.** `SageMath`/`FLINT` for rank over \(\mathbb{Q}\), \(\mathbb{F}_2\), and small \(\mathbb{F}_p\); record all three.

**`[opt]` - bound optimization on the separation.** Use SDP relaxations (\(\gamma_2\) norm, approximate rank) via `SDPA-GMP` for exploratory ranking of candidate hard matrices, but convert any load-bearing quantity to an exact certificate before it enters a claim. Search the NW/Kushilevitz gadget space and small random low-rank matrices for improved finite separation ratios (P4).

**One-workstation scope.** \(4\times4\) exhaustive census: minutes. \(8\times8\): hours with dedup. \(16\times16\): selected instances only, days, not a full census.

**Failure modes.** The subrectangle state space is \(2^{|X|}\cdot2^{|Y|}\) - exhaustive \(D\) is intractable past \(\sim\)\(16\times16\); floating-point rank silently miscounts near-degenerate matrices (use exact arithmetic only); LP duals from a non-exact solver are not certificates; canonical-form bugs cause double counting or missed classes (cross-check counts against `nauty`-style orbit sizes).

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every \(D\)-value is two-sided: an explicit protocol tree (upper) and an exact rational LP / fooling-set / rank certificate (lower). Every rank is exact over a named field. Floating point and SDP output are exploratory only and never load-bearing.

2. **Independent verification.** A standalone protocol-replayer, written separately from the search, re-evaluates each emitted tree on all inputs and confirms its depth; a separate LP-dual checker validates each lower-bound certificate; ranks are recomputed by a second CAS. Dual implementations for any headline separation.

3. **Reproducibility.** All truth tables, canonical-form conventions, solver versions and exact-arithmetic flags, and search seeds are recorded; a SHA-256 manifest covers every matrix, protocol tree, and certificate; the specific prior small-case value or separation ratio being improved is cited with source and access date.

4. **Preservation.** Search and enumeration source, canonicalization code, and all certificates are part of the record. Anything not preserved is stated explicitly.

5. **Honest reporting.** The report states up front whether any exact \(D\) census was completed, for which matrix sizes \(D\) is now certified, whether a finite separation ratio was strictly improved, and over which field the ranks are taken. The log-rank conjecture itself is not claimed touched unless the section-2 certified standard is met; a good protocol or a suggestive numerical trend is reported as such and never dressed as a resolution.
