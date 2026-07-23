# PROMPT FOR BOUNDING THE VAN DER WAERDEN NUMBER W(2,7)

## Certified bounds on the two-colour, seven-term arithmetic-progression number

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 16 of 50  
**Area:** Ramsey/extremal  
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

$W(2,7)$ is the least $N$ such that every $2$-colouring of $\{1,\dots,N\}$ contains a monochromatic $7$-term arithmetic progression. Van der Waerden's theorem guarantees it is finite; the exact values are known only through

\[
W(2,3)=9,\quad W(2,4)=35,\quad W(2,5)=178,\quad W(2,6)=1132,
\]

the last settled by Kouřil and Paul (2008) with a SAT computation. $W(2,7)$ is open, with a documented lower bound $W(2,7)\ge3703$. This is a direct SAT-search sibling of the Schur programme: a lower bound is a $2$-colouring of an interval avoiding a monochromatic long progression - a trivially checkable witness - and an upper bound is a propositional unsatisfiability claim over a clean CNF. Unlike the Ramsey cases, van der Waerden numbers have **no useful analytic upper bound** (the best general bounds are tower-type), so the upper side is reachable only by SAT at values far below the truth; the scientific content here is the lower-bound construction and the certified reproduction of small cases. The task is to **improve and certify bounds on $W(2,7)$.** The resolution standard in section 2 (the exact value with machine-checkable proofs both ways) is the target; every lesser result is reported as a partial result and never represented as determining $W(2,7)$.

## 1. Exact problem statement

A **$k$-term arithmetic progression** ($k$-AP) in $\mathbb{Z}_{>0}$ is a set

\[
\{a,\,a+d,\,a+2d,\,\dots,\,a+(k-1)d\},\qquad a\ge1,\ d\ge1 .
\]

For $r,k\ge1$, an $r$-colouring $c:[1,N]\to\{1,\dots,r\}$ is **$k$-AP-free** if no $k$-AP is monochromatic under $c$.

**Definition.** The van der Waerden number $W(r,k)$ is the least $N$ such that **no** $k$-AP-free $r$-colouring of $[1,N]$ exists; equivalently $W(r,k)-1$ is the largest $N$ admitting a $k$-AP-free $r$-colouring. Van der Waerden's theorem (1927) guarantees $W(r,k)<\infty$.

Here $r=2$, $k=7$. A **witness** for $W(2,7)>N$ is a $2$-colouring $c:[1,N]\to\{0,1\}$ with no monochromatic $7$-AP; its existence gives $W(2,7)\ge N+1$. An **upper bound** $W(2,7)\le U$ is the statement that every $2$-colouring of $[1,U]$ has a monochromatic $7$-AP - a propositional unsatisfiability claim (section 5).

*Micro-example.* $W(2,3)=9$: the colouring $\texttt{00110011}$ of $[1,8]$ (i.e. $c(i)=0,0,1,1,0,0,1,1$) has no monochromatic $3$-AP, so $W(2,3)>8$; every $2$-colouring of $[1,9]$ contains one, so $W(2,3)=9$. The good colourings that realize the record lengths are, at larger $k$, typically periodic or palindromic - the structure the zipper constructions of section 5 chase.

The open question: **determine $W(2,7)$**, or the sharpest certified bracket

\[
L+1\le W(2,7)\le U ,
\]

where a $7$-AP-free $2$-colouring of $[1,L]$ exists and none exists for $[1,U]$. Convention: the two colours are unordered (colour-swap is a symmetry); progressions have integer $a,d\ge1$ and stay within $[1,N]$; the increasing and decreasing enumerations denote the same AP.

## 2. Resolution standard

A **complete resolution** determines $W(2,7)=V$ and supplies:

1. **Lower certificate.** An explicit $7$-AP-free $2$-colouring $c:[1,V-1]\to\{0,1\}$, given as a bit-vector of length $V-1$, with a soundness argument (an exhaustive scan over all $7$-APs in $[1,V-1]$ finds none monochromatic).
2. **Upper certificate.** A machine-checkable proof that the CNF $\Psi_{V}$ (section 5) encoding "$\exists$ a $7$-AP-free $2$-colouring of $[1,V]$" is unsatisfiable, in **DRAT or LRAT** form, checked by an independent proof checker, together with an encoding-fidelity argument that:
   - $\Psi_V$'s clauses are exactly the monochromatic-$7$-AP exclusions (both colour polarities of every $7$-AP), and
   - any symmetry-breaking predicate preserves satisfiability.

**Not accepted as resolution.**

- A record lower-bound colouring alone (bounds only the lower side).
- An UNSAT result whose proof is not emitted in a certified format, not independently checked, or whose encoding fidelity is not argued.
- A "SAT solver returned UNSAT" claim without a preserved, replayable proof object (or a documented protocol for a trace too large to store).
- A colouring produced by local search and reported without an exact $7$-AP-free verification.
- An asymptotic or tower-type bound (van der Waerden / Gowers-style) presented as pinning the finite value.
- A bound for a different parameter ($W(2,6)$, $W(3,k)$, or a mixed number) reported as a statement about $W(2,7)$.
- A colouring avoiding only $7$-APs of a restricted common difference (e.g. $d\le d_0$) presented as fully $7$-AP-free.
- Matching an OEIS / survey figure without an on-machine certificate.

Honest calibration: full resolution is **not** expected. The exact value of $W(2,7)$ is unknown even in order of magnitude beyond the lower bound; with no analytic upper bound in reach and each new exact van der Waerden number ($W(2,6)=1132$) already a major SAT effort, an UNSAT proof near the truth is far beyond one workstation. The realistic product is a certified record lower bound and small-case reproduction.

## 3. Graded partial-result targets

**P1 - Reproduce the frontier with our toolchain.** Re-derive $W(2,6)=1132$:

- (a) verify a $6$-AP-free $2$-colouring of $[1,1131]$ with an exact scanner;
- (b) build $\Psi_{1132}$ for $k=6$, run a modern solver, and obtain UNSAT with a **DRAT** proof;
- (c) check that proof with an independent checker.

This is a large but plausibly workstation-scale SAT run and directly validates the pipeline against a known answer. *Certificate:* the $[1,1131]$ colouring + verifier; a checked DRAT trace for $N=1132$; SHA-256 manifest.

**P2 - Certify the record lower bound.** Reproduce and independently verify an explicit $7$-AP-free $2$-colouring of $[1,3702]$ (or the current record $L_0$; see section 4), giving $W(2,7)\ge3703$. *Certificate:* the colouring as a length-$L_0$ bit-vector; a standalone checker that scans every $7$-AP $\{a,a+d,\dots,a+6d\}\subseteq[1,L_0]$ and confirms none is monochromatic; a canonical serialization and hash.

**P3 - Improve the lower bound.** Find a $7$-AP-free $2$-colouring of $[1,L_0+1]$ or longer, giving $W(2,7)\ge L_0+1$. Methods:

- cyclic / palindromic "zipper" constructions (Rabung / Herwig-style);
- SAT-based local search (the Herwig–Heule–van Lambalgen–van Maaren approach);
- pattern blow-ups and periodic templates, plus modern guided search.

*Certificate:* the new colouring, exact-verified as in P2, with search source preserved.

**P4 - Structure mining and a parametric construction.** Extract the structure of the best colourings (period, palindromic symmetry, zipper seams, block templates) and turn it into a parametric family giving lower bounds $W(2,k)\ge g(k)$ or explicit improved colourings, certified at $k=7$. *Certificate:* the construction with a proof of $7$-AP-freeness for the stated parameters, plus the concrete instance verified as in P2.

**P5 - Partial upper-side SAT lemmas.** For values $N$ within reach, produce certified UNSAT results for *restricted* problems: $\Psi_N$ (for $k=7$) augmented with structural assumptions (fixed prefix, forced period, assumed symmetry), each restriction labelled unconditional-if-proved-preserving or clearly conditional. Emit DRAT/LRAT and check independently. *Certificate:* per-instance CNF, solver log, checked proof trace, and a precise statement of what was proved.

**P6 - Strongest result short of resolution.** Any of:

- an improved certified lower-bound record with a preserved witness;
- (aspirationally) a certified two-sided bracket - noting honestly that any reachable SAT upper bound will lie far above the true value and so will not meaningfully narrow the interval;
- full resolution meeting section 2 (windfall).

*Certificate:* directional certificates at the section-2 standard for whatever is claimed.

## 4. Known results and prior art

- **Exact values.** $W(2,3)=9$, $W(2,4)=35$, $W(2,5)=178$, and $W(2,6)=1132$ - the last by **Michal Kouřil and Jerome Paul**, "The van der Waerden number $W(2,6)$ is 1132" (Experimental Mathematics, 2008), via SAT; Kouřil later extended parallel-SAT methods to related numbers (e.g. $W(3,4)$). (Verify the smaller-value attributions against the survey.)
- **Lower bound for $W(2,7)$.** $W(2,7)\ge3703$ (attributed to Rabung / Lotts-type cyclic constructions; verify exact record and author). Methods for van der Waerden lower bounds:
  - cyclic constructions - **Rabung** (1979);
  - "a new method to construct lower bounds" - **Herwig, Heule, van Lambalgen, and van Maaren** (Electron. J. Combin., 2007);
  - cyclic-zipper improvements and further records - **Rabung–Lotts**, **Monroe**, and **Ahmed, Kullmann, and Snevily**, "On the van der Waerden numbers" (c. 2014);
  - more recent improved lower bounds appear in preprints around 2021 (e.g. arXiv 2111.01099, verify) and in neural-network-guided constructions (c. 2022).

  Re-check whether the $W(2,7)$ record now exceeds $3703$.
- **No usable upper bound.** General upper bounds on $W(2,k)$ are tower-type - **Gowers** (2001) gave the first primitive-recursive bound; for large $k$, **Green** (2022) improved *lower* bounds - but none is near the finite $W(2,7)$. The only sharp upper bounds are SAT-computed and feasible so far only up to $k=6$.
- **Method lineage.** SAT with symmetry breaking, cube-and-conquer, and DRAT proof logging is the state of the art for the exact values - the same toolchain as Schur $S(5)$ and the $R(5,5)$ programme.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** Re-check the current $W(2,7)$ lower-bound record and its author / year, and whether any new SAT result has produced *any* certified upper bound for $W(2,7)$.

## 5. Attack plan

**CNF encoding (`[search]`).** One Boolean variable $x_i$ per element $i\in[1,N]$ ($x_i=1$ means colour $1$, else colour $0$). For each $7$-AP $P=\{a,a+d,\dots,a+6d\}\subseteq[1,N]$, two clauses forbid monochromaticity:

\[
\bigvee_{p\in P} x_p\quad(\text{not all colour }0),\qquad
\bigvee_{p\in P} \lnot x_p\quad(\text{not all colour }1).
\]

Colour-swap symmetry is broken by fixing $x_1=1$; further symmetry-breaking predicates are logged with a satisfiability-preservation note. This CNF is $\Psi_N$; the number of $7$-APs in $[1,N]$ is

\[
\#\{(a,d): a\ge1,\ d\ge1,\ a+6d\le N\}=\sum_{d\ge1}\max(0,\,N-6d)=\Theta\!\left(\tfrac{N^2}{12}\right),
\]

giving two clauses each. For P1 use the $k=6$ analogue ($a+5d\le N$).

**Solvers and proofs.** Lower-bound / feasibility searches at fixed $N$: **CaDiCaL**, **kissat**, and **CryptoMiniSat**, plus a dedicated SAT-based local search for long $7$-AP-free colourings. Upper-bound / UNSAT (P1 and P5): **CaDiCaL** / **kissat** with **DRAT** logging, converted to **LRAT** and checked with `drat-trim` / `dpr-trim`; cube-and-conquer (`march_cu`-style splitting) for hard instances such as $N=1132$, $k=6$.

**Cyclic and zipper constructions (`[search]`).** Fix a period $m$ and a $2$-colouring $\sigma$ of $\mathbb{Z}/m\mathbb{Z}$; extend it periodically to $[1,N]$ by $c(i)=\sigma(i\bmod m)$ and measure the largest prefix that stays $7$-AP-free - that prefix length is a lower bound. A **zipper** concatenates two shifted cyclic blocks across a seam,

\[
c=\underbrace{\sigma\sigma\cdots\sigma}_{\text{block A}}\ \big|\ \underbrace{\tau\tau\cdots\tau}_{\text{block B}},
\]

tuning the seam to push the free prefix further than either block alone (the Rabung / Herwig lineage). Periodicity and palindromy are search heuristics only - every candidate is re-checked by the exact scanner.

**Custom C++ and CAS.** A standalone verifier (a few dozen lines) reads a bit-vector and rejects on the first monochromatic $7$-AP by scanning all $(a,d)$ with $a+6d\le N$ - this is the load-bearing lower-bound checker and is independent of the search code. Custom C++ for the cyclic / zipper search; **SageMath** / Python for structure mining of good colourings (period, palindromic symmetry, seam analysis) feeding P4.

**One-workstation scope.** Feasible: exact verification of any candidate colouring up to $N\sim10^5$ (fast); reproducing $W(2,6)=1132$ UNSAT with DRAT (large but plausible with modern solvers + cube-and-conquer); zipper / local-search lower-bound chasing for $k=7$ around $N\approx3700$–$4500$; restricted UNSAT lemmas. **Out of scope:** an UNSAT proof anywhere near the true $W(2,7)$ - do not promise the upper side. **Failure modes:** clause count grows with the number of $7$-APs - manageable, but symmetry breaking matters; solver timeouts on unrestricted UNSAT beyond $k=6$ (expected - pivot to restricted lemmas); DRAT traces too large to store (document a segmented re-derivation protocol rather than claim an unchecked UNSAT); local-search plateaus (diversify seeds, exploit periodicity, seed from the record colouring).

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every lower bound is a bit-vector checked by an exact scan over all $7$-APs; every upper bound is a DRAT/LRAT proof checked by a formal proof checker. Floating point and solver "UNSAT" prints are exploration only - never certification. Encoding-fidelity arguments accompany every CNF.
2. **Independent verification.** The $7$-AP-free checker is written independently of the search / encoder (ideally a second implementation and a second language). UNSAT traces are checked by a proof checker not derived from the solver; where a trace is too large to store, a documented segment-recheck protocol stands in and is stated as such.
3. **Reproducibility.** All CNF generators, symmetry-breaking predicates, construction code, solver versions and flags, seeds, and environment are recorded; a SHA-256 manifest covers every colouring, CNF, proof trace, and log.
4. **Preservation.** All search and construction source - encoders, zipper / local-search code, cube generators, verifiers - is part of the record (the Hadamard-668 lost-source lesson). Any artifact not preserved (e.g. a very large trace) is named explicitly with the protocol to regenerate and spot-check it, never silently dropped.
5. **Honest reporting.** The report states up front whether $W(2,7)$ was determined (it will not be) and reports each result at its true strength - "certified $W(2,7)\ge L$", "reproduced $W(2,6)=1132$", "conditional UNSAT lemma" - and never presents a record lower bound or a restricted lemma as the value of $W(2,7)$.
