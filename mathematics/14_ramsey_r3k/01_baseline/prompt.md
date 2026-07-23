# PROMPT FOR DETERMINING R(3,10) IN THE R(3,k) LADDER

## The smallest open triangle-versus-independent-set Ramsey number

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 14 of 50  
**Area:** Ramsey/extremal  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Ramsey numbers $R(3,k)$ measure how large a triangle-free graph can be while keeping its independence number below $k$. The ladder is known through $R(3,9)=36$ (Grinstead–Roberts, 1982); the first open rung is $R(3,10)$, now pinned to the two-element interval

\[
R(3,10)\in\{40,41\}
\]

- lower bound $40$ (Exoo), upper bound $41$ (Angeltveit, 2024, improving the earlier $\le42$ of Goedgebeur–Radziszowski). These are among the crispest finite Ramsey targets in existence: because the interval has width one, a single decisive certificate settles it. A triangle-free graph on $40$ vertices with independence number $\le9$ would give $R(3,10)\ge41$ and hence $R(3,10)=41$; a certified proof that no such graph exists gives $R(3,10)=40$. The task is to **resolve $R(3,10)$, or produce certified progress on the $R(3,k)$ ladder.** The resolution standard in section 2 is the target; every lesser result is reported as a partial result and never represented as determining $R(3,10)$.

## 1. Exact problem statement

For $k\ge2$, $R(3,k)$ is the least $N$ such that every graph on $N$ vertices contains a triangle $K_3$ or an independent set of size $k$. Equivalently, since the forbidden clique has size $3$:

**Definition.** A **$(3,k;N)$-graph** is a **triangle-free** graph $G$ (no $K_3$) on $N$ vertices with

\[
\alpha(G)\le k-1 .
\]

Its existence certifies $R(3,k)>N$, i.e. $R(3,k)\ge N+1$. Thus $R(3,k)$ is the least $N$ for which no triangle-free graph on $N$ vertices has $\alpha\le k-1$.

For the focus case $k=10$: a **$(3,10;N)$-graph** is a triangle-free graph on $N$ vertices with $\alpha(G)\le9$. Write $e(3,k;N)$ for the number of $(3,k;N)$-graphs up to isomorphism.

*Micro-example.* The $5$-cycle $C_5$ is a $(3,3;5)$-graph - triangle-free with independence number $2$ - certifying $R(3,3)>5$; with $R(3,3)\le6$ this gives $R(3,3)=6$. At larger $k$ the extremal $(3,k)$-graphs are typically vertex-transitive (cyclic or Cayley), a regularity the constructions of section 5 exploit.

Two opposing structural pressures pin the order $39$–$41$ regime. Triangle-freeness forces every neighbourhood $N(v)$ to be independent, so

\[
\Delta(G)\le\alpha(G)\le 9,\qquad |E(G)|\le \tfrac{9N}{2};
\]

simultaneously $\alpha(G)\le9$ forces the graph to be dense enough to admit no independent $10$-set. A $(3,10;N)$-graph must satisfy both at once.

The open question: **determine $R(3,10)$** (known to be $40$ or $41$), and more broadly improve any rung of the $R(3,k)$ ladder or its data. Convention: simple undirected graphs; triangle-free means no three mutually adjacent vertices; $\alpha$ is the size of the largest independent (pairwise non-adjacent) set.

## 2. Resolution standard

A **complete resolution of $R(3,10)$** fixes the value $V\in\{40,41\}$ and supplies:

1. **Lower certificate.** An explicit $(3,10;V-1)$-graph as a canonical adjacency object (graph6 / adjacency matrix), with a verified check that
   - $G$ is triangle-free (no $K_3$ over all triples), and
   - $\alpha(G)\le9$ (no independent $10$-set - a certified independence-number computation).
2. **Upper certificate.** A certified proof that no $(3,10;V)$-graph exists, in one of two forms:
   - (a) an **exhaustive isomorph-free enumeration** of triangle-free graphs on $V$ vertices with maximum independence $\le9$, shown empty, via a canonical-augmentation generator with a replayable record and an independent recount; or
   - (b) a **SAT unsatisfiability proof** (DRAT/LRAT) for "$\exists$ a $(3,10;V)$-graph", checked by an independent proof checker with an encoding-fidelity argument.

Concretely, exactly one of these resolves it:

\[
\text{a verified }(3,10;40)\text{-graph}\ \Rightarrow\ R(3,10)=41;\qquad
\text{certified nonexistence of }(3,10;40)\text{-graphs}\ \Rightarrow\ R(3,10)=40 .
\]

**Not accepted as resolution.**

- A $(3,10;39)$-graph alone (it only re-certifies the known lower bound $R(3,10)\ge40$).
- A nonexistence claim from a solver's UNSAT print with no preserved, independently checked DRAT/LRAT trace.
- An enumeration whose triangle-free / independence completeness is not argued and independently reconstructed.
- The upper bound $41$ cited from Angeltveit (2024) without reproducing a certificate at our standard - that is context, not a resolution artifact.
- Any asymptotic bound (Kim / Shearer-type) presented as pinning the finite value.
- A restricted-family negative (e.g. no *cyclic* $(3,10;40)$-graph) presented as the full nonexistence - it is a valuable partial (P3), not a resolution.
- Matching an OEIS / survey figure without an on-machine certificate.

Honest calibration: the *lower* resolution route - searching for a $(3,10;40)$-graph - is a pure, fully checkable search and is the tractable path to a decisive result. The *upper* route - certifying no $(3,10;40)$-graph exists - is the harder enumeration and may exceed one workstation. Report accordingly.

## 3. Graded partial-result targets

**P1 - Reproduce the frontier.** Re-derive $R(3,9)=36$ with our toolchain:

- verify a $(3,9;35)$-graph (triangle-free, $\alpha\le8$);
- reproduce the nonexistence of $(3,9;36)$-graphs (or a documented partial re-enumeration), matching published counts $e(3,9;N)$ where available.

*Certificate:* verified $(3,9;35)$-graph; enumeration / recount record with SHA-256 manifest. Validates the pipeline against a known answer.

**P2 - Certify the record lower bound.** Reproduce and independently verify an explicit $(3,10;39)$-graph, giving $R(3,10)\ge40$ (Exoo; see section 4). *Certificate:* the graph in graph6, a standalone checker confirming triangle-freeness and $\alpha\le9$, and its isomorphism-class hash.

**P3 - Decide the interval from below.** Search exhaustively-enough for a $(3,10;40)$-graph. If one is found, $R(3,10)=41$ is *resolved*. Prioritize structured families:

- cyclic / circulant and Cayley triangle-free graphs on $\mathbb{Z}_{40}$ and small groups;
- graphs from the triangle-free process (as heuristic seeds, then verified exactly);
- local-search extensions of $(3,10;39)$-graphs by one vertex.

*Certificate:* a verified $(3,10;40)$-graph (as in P2) with search source preserved; a certified *negative* over a restricted family (e.g. "no vertex-transitive $(3,10;40)$-graph") is itself a recorded partial.

**P4 - Decide the interval from above.** Attempt a certified nonexistence of $(3,10;40)$-graphs (⇒ $R(3,10)=40$), by canonical-augmentation enumeration of triangle-free graphs with $\alpha\le9$, or SAT with a checked DRAT/LRAT proof. This is the hard research target. *Certificate:* the enumeration nonexistence record with independent recount, or the checked proof trace with encoding-fidelity argument.

**P5 - Ladder data and other rungs.** Produce certified constructions or enumeration counts for neighbouring open cases ($R(3,11)$, $R(3,12)$, …) and mine the extremal $(3,k)$-graphs for structure (girth, spectrum, vertex-transitivity) toward a construction template. Optionally sharpen the finite data underlying the $R(3,k)=\Theta(k^2/\log k)$ constants. *Certificate:* verified graphs / complete counts with independent recount.

**P6 - Strongest result short of resolution.** A certified improvement to any $R(3,k)$ bracket for $k\ge10$ - a better lower-bound graph or a certified nonexistence - or the full determination of $R(3,10)$ meeting section 2 (the crisp target). *Certificate:* both directional certificates at the section-2 standard for the claimed bracket.

## 4. Known results and prior art

- **Known ladder.** $R(3,3)=6,\ R(3,4)=9,\ R(3,5)=14,\ R(3,6)=18,\ R(3,7)=23,\ R(3,8)=28,\ R(3,9)=36$. The last is **Grinstead and Roberts** (1982). (Verify each against the current survey.)
- **Lower-bound constructions.** The record $(3,10;39)$-graph and its predecessors are typically cyclic / circulant graphs found by targeted search over connection sets (Exoo and others supplied such Ramsey graphs across the ladder). Published isomorph counts $e(3,k;N)$ for small $N$ - in the survey and McKay's data pages - are the cross-check for any re-enumeration.
- **Sibling context.** $R(3,10)$ is the off-diagonal two-colour analogue of the multicolour triangle numbers (problem 15) and the Schur numbers (problem 12); all three yield to the same certified-search-plus-nonexistence discipline and share the nauty / SAT toolchain.
- **$R(3,10)$ interval.** Lower bound $R(3,10)\ge40$ from a $(3,10;39)$-graph - **Geoffrey Exoo** (verify exact record / year). Upper bound $R(3,10)\le41$ - **Vigleik Angeltveit** (2024; the preprint "$R(3,10)\le41$", arXiv:2401.00392, verify), improving the $R(3,10)\le42$ of **Goedgebeur and Radziszowski**, "New computational upper bounds for Ramsey numbers $R(3,k)$" (c. 2012–2013).
- **Asymptotics (context).** $R(3,k)=\Theta(k^2/\log k)$: upper bound $R(3,k)\le(1+o(1))\,k^2/\ln k$ - **Shearer** (1983); matching lower bound $R(3,k)\ge(\tfrac14-o(1))\,k^2/\ln k$ - **Kim** (1995); refined constants via the triangle-free process - **Bohman–Keevash** and **Fiz Pontiveros–Griffiths–Morris** (c. 2013–2020). These fix the growth but not the small finite values.
- **Smallest open cases.** $R(3,10)$ and $R(4,6)$ are the two smallest undetermined two-colour Ramsey numbers (survey statement).
- **Data cross-checks.** McKay's and Goedgebeur's public data pages list triangle-free Ramsey-graph representatives and counts $e(3,k;N)$ for many classes; these are the external ground truth for the P1/P2 reproductions and for validating any new enumeration.
- **Survey and methods.** **Radziszowski**, *Small Ramsey Numbers* (Electron. J. Combin. DS1; 2024 revision, verify). Core methods: canonical-augmentation isomorph-free generation of triangle-free graphs (McKay's lineage, **nauty/Traces**); the Goedgebeur–Radziszowski neighbourhood / gluing algorithm for triangle-free Ramsey graphs; SAT for nonexistence.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Re-check whether $R(3,10)$ has been fully resolved to $40$ or $41$ since the 2024 upper bound, and whether the lower-bound record or any higher rung has moved.

## 5. Attack plan

**Triangle-free isomorph-free generation (`[search]`).** Use **nauty/Traces** and the specialized triangle-free extension algorithm (Goedgebeur–Radziszowski lineage): grow triangle-free graphs vertex by vertex under canonical augmentation, pruning any partial graph whose independence already forces $\alpha\ge10$. Track $e(3,10;N)$ and cross-check with a second canonical labeler. This is the P1 / P4 workhorse.

**SAT nonexistence (`[search]`).** Encode "$\exists$ a $(3,10;N)$-graph" as CNF: edge variables $x_{ij}$; for every triple $\{i,j,k\}$ a clause forbidding a triangle, and for every $10$-subset $S$ a clause forbidding an independent set:

\[
\lnot x_{ij}\lor\lnot x_{ik}\lor\lnot x_{jk}\quad(\text{no }K_3),\qquad
\bigvee_{\{i,j\}\subseteq S} x_{ij}\quad(\text{no independent }10\text{-set}).
\]

Lex / canonical symmetry breaking (proved satisfiability-preserving). Solve with **CaDiCaL** / **kissat**, log **DRAT**, convert to **LRAT**, check with `drat-trim` / `dpr-trim`. The $10$-subset clauses are numerous - use lazy / incremental independence constraints or a hybrid CP model if the direct CNF is too large.

A cheap but powerful pruning rule follows from the neighbourhood structure: in any triangle-free graph $N(v)$ is independent, so

\[
\Delta(G)\le\alpha(G)\le 9 .
\]

Any partial graph violating $\Delta\le9$, or whose complement already contains a $K_{10}$, is discarded immediately in the canonical-augmentation search - this is what makes enumeration at orders $39$–$41$ conceivable. The flat SAT model at $N=40$ has $780$ edge variables and $\binom{40}{3}=9{,}880$ triangle clauses, but

\[
\binom{40}{10}=847{,}660{,}528
\]

independent-$10$-set clauses - so lazy constraints (post a $10$-set clause only when the solver proposes an independent $10$-set) are essential, not optional.

**Constructions for lower bounds (`[search]`).** Circulant / Cayley triangle-free graphs on $\mathbb{Z}_{40}$ and small groups; graphs from the triangle-free random process (heuristic seeds, verified exactly); local search (simulated annealing / tabu) on adjacency matrices minimizing (triangle, independent-$10$-set) violations; extend $(3,10;39)$-graphs by one vertex.

**CAS support.** **SageMath** for exact independence-number computation (a certified $\alpha$ via ILP or a clique solver on the complement), automorphism groups, and structure mining; a standalone C++ / Python checker (triangle scan + certified independence) is the load-bearing verifier, independent of the search code.

**One-workstation scope.** Feasible: exact verification of any candidate graph on $\le41$ vertices (fast); vertex-transitive / circulant searches for a $(3,10;40)$-graph; SAT nonexistence for restricted subclasses; reproduction of $R(3,9)=36$ data. **Possibly in reach, possibly not:** a full unconditional nonexistence of $(3,10;40)$-graphs - attempt it, but report conditionally if incomplete. **Failure modes:** the $10$-independent-set constraint dominates the CNF (use lazy constraints); enumeration blow-up (prune by independence early, checkpoint); local-search plateaus (diversify, seed from Exoo's graph); a subtle isomorph / independence bug (dual canonical forms, certified $\alpha$, recount).

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Triangle-freeness by exhaustive triple scan; independence number by a certified solver (ILP with a checked optimal, or exhaustive subset scan for small $N$); upper bounds by isomorph-free enumeration with a completeness argument or DRAT/LRAT proofs. Floating point is exploration only; solver "UNSAT" prints are never certification alone.
2. **Independent verification.** The graph checker is independent of the search / encoder; enumeration completeness is re-established by an independent recount and a second canonical labeler (nauty vs. Traces); SAT traces are checked by a checker not derived from the solver; encoding-fidelity arguments accompany every CNF.
3. **Reproducibility.** All generators, gluing scripts, CNF encoders, tool versions and flags, seeds, and environment are recorded; a SHA-256 manifest covers every graph, catalogue, CNF, proof trace, and log.
4. **Preservation.** All search and enumeration source is part of the record (the Hadamard-668 lost-source lesson). Any artifact too large to store is named with a protocol to regenerate and spot-check it, never silently dropped.
5. **Honest reporting.** The report states up front whether $R(3,10)$ was resolved, and reports each result at its true strength - "certified $R(3,10)\ge40$", "found a $(3,10;40)$-graph ⇒ $R(3,10)=41$", "certified no vertex-transitive $(3,10;40)$-graph" - never presenting a re-certification of a known bound or a restricted result as the full determination.
