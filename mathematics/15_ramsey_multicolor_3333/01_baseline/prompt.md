# PROMPT FOR BOUNDING THE MULTICOLOUR RAMSEY NUMBER R(3,3,3,3)

## Certified bounds on the four-colour triangle Ramsey number

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 15 of 50  
**Area:** Ramsey/extremal  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

$R(3,3,3,3)$ is the least $N$ such that every colouring of the edges of $K_N$ with four colours contains a monochromatic triangle. The two- and three-colour cases are exactly known - $R(3,3)=6$ and $R(3,3,3)=17$ (Greenwood–Gleason, 1955) - but the four-colour number is open, with the wide interval

\[
51\le R(3,3,3,3)\le62
\]

(upper bound: Fettes–Kramer–Radziszowski). A lower bound is a construction problem: exhibit a four-colouring of $K_N$ with no monochromatic triangle, equivalently a decomposition of $K_N$ into four triangle-free graphs - a fully checkable object. The upper bound is a nonexistence / counting problem settled only by a certified enumeration, SAT proof, or verified combinatorial argument. This case is a natural companion to Schur $S(6)$ (problem 12): a sum-free $4$-colouring of $[1,n]$ yields a triangle-free four-edge-colouring of $K_{n+1}$, so $R(3,3,3,3)\ge S(4)+2=46$, and the true lower bound improves on this. The task is to **narrow the $R(3,3,3,3)$ interval with certified constructions (lower) and certified nonexistence / counting (upper).** The resolution standard in section 2 is the target; every lesser result is reported as a partial result and never represented as determining $R(3,3,3,3)$.

## 1. Exact problem statement

For $r\ge1$, the multicolour (diagonal, triangle) Ramsey number $R_r(3)=R(\underbrace{3,\dots,3}_{r})$ is the least $N$ such that every $r$-colouring $\chi:E(K_N)\to\{1,\dots,r\}$ has a monochromatic triangle. Equivalently, $R_r(3)-1$ is the largest $N$ for which $E(K_N)$ can be partitioned into $r$ triangle-free graphs.

**Definition (the $r=4$ case).** A **good $4$-colouring** of $K_N$ is a map

\[
\chi:E(K_N)\to\{1,2,3,4\}
\]

such that each colour class $\chi^{-1}(c)$ is a triangle-free graph on $N$ vertices. Its existence certifies $R(3,3,3,3)>N$, i.e. $R(3,3,3,3)\ge N+1$. Thus $R(3,3,3,3)$ is the least $N$ admitting no good $4$-colouring.

The open question: **determine $R(3,3,3,3)$**, or the sharpest certified bracket

\[
L+1\le R(3,3,3,3)\le U ,
\]

where a good $4$-colouring of $K_L$ exists and none exists for $K_U$. Convention: $K_N$ is the complete simple graph; a triangle is a monochromatic $K_3$; colours are unordered labels (colour-permutation is a symmetry of the problem, generating a group of order $4!=24$ on top of the vertex symmetry).

*Counting context.* A good $4$-colouring decomposes the $\binom{N}{2}$ edges of $K_N$ into four triangle-free graphs. Since a triangle-free graph on $N$ vertices has at most $\lfloor N^2/4\rfloor$ edges (Mantel's theorem), four classes carry at most $4\lfloor N^2/4\rfloor\approx N^2$ edges - comfortably above $\binom{N}{2}$, so the edge budget is not the obstruction; the obstruction is the simultaneous triangle-freeness of all four classes on shared vertices, which is what forces $R(3,3,3,3)$ to be finite and makes the search delicate.

*Local constraint.* Fix a vertex $v$ and let $A_c$ be the set of vertices joined to $v$ in colour $c$. No edge inside $A_c$ may take colour $c$ (it would close a monochromatic triangle with $v$), so $A_c$ carries a good $3$-colouring in the remaining colours; hence $|A_c|\le R(3,3,3)-1=16$. As the $A_c$ partition the other $N-1$ vertices,

\[
N-1=\sum_{c=1}^{4}|A_c|\ \le\ 4\,(R(3,3,3)-1)=64,
\]

which is the recursive bound $R(3,3,3,3)\le66$; the certified $\le62$ improves it by global counting.

## 2. Resolution standard

A **complete resolution** fixes $R(3,3,3,3)=V$ and supplies:

1. **Lower certificate.** An explicit good $4$-colouring of $K_{V-1}$, given as a symmetric $(V-1)\times(V-1)$ matrix over $\{1,2,3,4\}$ (or four adjacency matrices summing to $K_{V-1}$), with a verified check that each colour class is triangle-free (no monochromatic triple).
2. **Upper certificate.** A certified proof that no good $4$-colouring of $K_V$ exists, in one of two forms:
   - (a) an **exhaustive isomorph-free enumeration** (over colourings up to graph-isomorphism and colour-permutation) shown empty, with a replayable generation record and independent recount; or
   - (b) a **SAT unsatisfiability proof** (DRAT/LRAT) for the CNF encoding "$\exists$ a good $4$-colouring of $K_V$", checked by an independent proof checker, with an encoding-fidelity argument (including how colour-symmetry breaking preserves satisfiability).

**Not accepted as resolution.**

- A record good $4$-colouring alone (bounds only the lower side).
- A nonexistence claim from a solver's UNSAT print without a preserved, independently checked DRAT/LRAT trace.
- An enumeration whose triangle-free / colour-symmetry completeness is not argued and independently reconstructed.
- The upper bound $62$ cited from Fettes–Kramer–Radziszowski without reproducing a certificate at our standard - that is context, not a resolution artifact.
- A bound proved only for the Schur / additive proxy ($S(4)$) presented as a statement about $R(3,3,3,3)$.
- Any numerical / probabilistic estimate or asymptotic bound reported as the exact value.
- A nonexistence proved only for cyclic / Cayley colourings presented as the unrestricted result - it is a partial (P4/P5), not a resolution.
- Matching an OEIS / survey figure without an on-machine certificate.

Honest calibration: with an interval of width $11$, full resolution is **very unlikely** on one workstation. The realistic product is a certified reproduction / improvement of the lower bound and certified enumeration data or SAT lemmas nibbling at the upper side.

## 3. Graded partial-result targets

**P1 - Reproduce the frontier.** Re-derive $R(3,3,3)=17$ with our toolchain:

- verify a good $3$-colouring of $K_{16}$ (the classical construction whose colour classes are Clebsch graphs);
- reproduce the nonexistence of a good $3$-colouring of $K_{17}$ (or a documented partial re-enumeration; recall exactly two good $3$-colourings of $K_{16}$ exist up to isomorphism - Kalbfleisch–Stanton).

*Certificate:* the $K_{16}$ colouring + triangle-free verifier; nonexistence / recount record with SHA-256 manifest. Validates the pipeline against a known answer.

**P2 - Certify the record lower bound.** Reproduce and independently verify an explicit good $4$-colouring of $K_{50}$, giving $R(3,3,3,3)\ge51$ (see section 4). *Certificate:* the $50\times50$ colour matrix, a standalone checker confirming each of the four classes is triangle-free, and the canonical hash of the colouring.

**P3 - Improve the lower bound.** Search for a good $4$-colouring of $K_{51}$ (would give $R(3,3,3,3)\ge52$). Prioritize algebraic constructions:

- Cayley colourings over $\mathbb{Z}_{51}$ / small groups (four symmetric connection sets, each a triangle-free Cayley graph);
- affine and projective-plane templates over $\mathbb{F}_q$;
- colourings lifted from sum-free $4$-partitions of intervals (the Schur link), then improved.

Then SAT with the order fixed and colour-symmetry broken, and local search. *Certificate:* a verified good $4$-colouring of $K_{51}$ (as in P2), search source preserved; a certified negative over a restricted family (e.g. "no cyclic good $4$-colouring of $K_{51}$") is itself a recorded partial.

**P4 - Certified enumeration / lemmas toward the upper bound.** Produce certified counts or structural constraints on good $4$-colourings at accessible orders (small $N$ complete catalogues; forced local structure; degree / neighbourhood constraints implied by triangle-freeness of four classes). *Certificate:* complete catalogues with independent recount, or checked SAT lemmas with encoding-fidelity arguments.

**P5 - Upper-bound progress.** Either

- (a) a certified nonexistence of good $4$-colourings at some $N<62$ (⇒ $R(3,3,3,3)\le N$) via enumeration or SAT with a checked proof - the hard research target; or
- (b) an improved analytic / counting upper bound with a machine-verified numerical core, reported as a bound.

*Certificate:* enumeration nonexistence record or checked DRAT/LRAT trace for (a); verified counting / SDP certificate for (b).

**P6 - Strongest result short of resolution.** A certified bracket narrower than $51\le R(3,3,3,3)\le62$ - an improved lower bound with a verified colouring, or an improved upper bound with a certified nonexistence - or full resolution meeting section 2 (windfall). *Certificate:* both directional certificates at the section-2 standard for the claimed bracket.

## 4. Known results and prior art

- **Known small cases.** $R(3,3)=6$; $R(3,3,3)=17$ - **Greenwood and Gleason** (1955), with the extremal $K_{16}$ colouring built from the Clebsch graph. Exactly two good $3$-colourings of $K_{16}$ exist up to isomorphism - **Kalbfleisch and Stanton** (verify).
- **$R(3,3,3,3)$ interval.** Lower bound $R(3,3,3,3)\ge51$ (explicit good $4$-colouring of $K_{50}$; attribution to a cyclic / algebraic construction - possibly **Chung** (1973) improved to $51$ by later work - verify the exact record and author). Upper bound $R(3,3,3,3)\le62$ - **Fettes, Kramer, and Radziszowski**, "An upper bound of 62 on the classical Ramsey number $R(3,3,3,3)$" (c. 2004), via computer-assisted counting (a companion "global arguments" paper accompanies it). Verify both endpoints.
- **Recursive upper bound (context).** $R_r(3)\le r\,(R_{r-1}(3)-1)+2$ gives $R_4(3)\le 4\cdot16+2=66$; the $62$ bound improves this by dedicated arguments.
- **The Schur link.** A sum-free $4$-colouring of $[1,n]$ gives a good $4$-colouring of $K_{n+1}$, so

  \[
  R(3,3,3,3)\ge S(4)+2=46
  \]

  (problem 12). The true lower bound $\ge51$ beats the Schur floor - good colourings need not come from intervals.
- **Recent multicolour work.** A 2025 preprint, "New bounds for some small multicolour Ramsey numbers" (arXiv, verify), may have updated the $R(3,3,3,3)$ interval or nearby $R_4(3)$-type values - check before starting.
- **Survey and methods.** **Radziszowski**, *Small Ramsey Numbers* (Electron. J. Combin. DS1; 2024 revision, verify), tabulates multicolour bounds. Methods: algebraic (Cayley / affine) constructions, isomorph-free enumeration (**nauty/Traces**), and SAT.
- **Sibling context.** $R(3,3,3,3)$ is the four-colour rung above $R(3,3,3)=17$ and the multicolour analogue of $R(4,6)$ (problem 13) and $R(3,10)$ (problem 14); its lower bounds connect directly to Schur $S(4)$ (problem 12) through the Cayley / sum-free construction, so the three problems share both toolchain and constructions.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Re-check both endpoints of the interval and the exact author / year of the lower-bound construction, and whether any 2024–2026 preprint has narrowed $51\le R(3,3,3,3)\le62$.

## 5. Attack plan

**SAT existence / nonexistence (`[search]`).** Variables $y_{ij,c}$ for each edge $\{i,j\}$ and colour $c\in\{1,2,3,4\}$, meaning "$\{i,j\}$ has colour $c$". The CNF has clauses:

- *exactly one colour per edge:* $\displaystyle\bigvee_{c=1}^{4} y_{ij,c}$ plus at-most-one clauses;
- *no monochromatic triangle:* for every triangle $\{i,j,k\}$ and every colour $c$,

  \[
  \lnot y_{ij,c}\ \lor\ \lnot y_{ik,c}\ \lor\ \lnot y_{jk,c}.
  \]

Break colour-permutation and vertex symmetry with lex predicates (proved satisfiability-preserving). Existence at $N$: **CaDiCaL** / **kissat** returning SAT yields a colouring (lower bound). Nonexistence at $N$: DRAT logging, convert to LRAT, check with `drat-trim` / `dpr-trim`. At $N=51$ the model has $4\binom{51}{2}=5{,}100$ colour variables and, over the $\binom{51}{3}=20{,}825$ triangles,

\[
4\binom{51}{3}=83{,}300\ \text{no-monochromatic-triangle clauses};
\]

quotienting the order-$24$ colour-permutation group by symmetry breaking is what keeps this search feasible.

**Algebraic constructions (`[search]`).** Cayley colourings: partition the nonzero elements of $\mathbb{Z}_N$ (or a small group) into four symmetric connection sets $S_1,\dots,S_4$ with $S_c=-S_c$ and $\bigsqcup_c S_c=\mathbb{Z}_N\setminus\{0\}$, colouring edge $\{i,j\}$ by the class of $i-j$; each class is triangle-free iff no $S_c$ contains $a,b,a+b$ - precisely a sum-free condition, the Schur link made concrete. Affine / projective templates over $\mathbb{F}_q$. Lift sum-free $4$-partitions of $[1,n]$ to colourings of $K_{n+1}$ as a baseline, then improve. Verify every candidate exactly.

**Enumeration and CAS.** **nauty/Traces** for isomorph-free enumeration of good $4$-colourings at small orders and for canonical forms / colour-symmetry handling. **SageMath** for triangle-free checking of each class, automorphism / colour-symmetry groups, and structure mining. A standalone C++ / Python checker (scan every triangle in every colour class) is the load-bearing verifier, independent of the search code.

**One-workstation scope.** Feasible: exact verification of any candidate colouring up to $N\approx62$ (fast); Cayley / affine and SAT searches for good $4$-colourings at $N=51$–$55$; small-order enumeration; reproduction of the $K_{16}$ case. **Out of scope:** an unconditional nonexistence near $N=62$ (interval width $11$; do not promise the upper side). **Failure modes:** exactly-one / triangle clause counts grow as $\binom{N}{2}$ and $\binom{N}{3}$ - use efficient encodings and symmetry breaking; SAT timeouts (restrict to structured colourings, report conditionally); local-search plateaus (diversify, seed from the record colouring); isomorph / colour-symmetry bugs (dual canonical forms, recount).

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every lower bound is a colour matrix checked by scanning all triangles in all four classes; every upper bound is an isomorph-free enumeration with a completeness argument or a DRAT/LRAT proof checked by an independent checker. Floating point (any SDP route) enters only through a rational / interval certificate; solver "UNSAT" prints are never certification alone.
2. **Independent verification.** The triangle-free checker is written independently of the search / encoder; enumeration completeness is re-established by an independent recount and a second canonical labeler (nauty vs. Traces); SAT traces are checked by a checker not derived from the solver; encoding-fidelity arguments (including colour-symmetry breaking) accompany every CNF.
3. **Reproducibility.** All construction generators, CNF encoders, tool versions and flags, seeds, and environment are recorded; a SHA-256 manifest covers every colouring, catalogue, CNF, proof trace, and log.
4. **Preservation.** All search and enumeration source is part of the record (the Hadamard-668 lost-source lesson). Any artifact too large to store is named with a protocol to regenerate and spot-check it, never silently dropped.
5. **Honest reporting.** The report states up front whether $R(3,3,3,3)$ was determined (very likely not) and reports each result at its true strength - "certified $R(3,3,3,3)\ge51$", "found a good $4$-colouring of $K_{51}$", "certified no cyclic good $4$-colouring of $K_{51}$" - never presenting a record colouring or a restricted lemma as the value of $R(3,3,3,3)$.
