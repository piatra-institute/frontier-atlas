# PROMPT FOR BOUNDING THE SCHUR NUMBER S(6)

## Certified bounds on the sixth Schur number, the direct SAT-search sibling of R(5,5)

**PIATRA INSTITUTE**  
**Prompt revision:** 23 July 2026  
**Rank:** 12 of 50  
**Area:** Ramsey/extremal  
**Modes:** `[search]` `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The Schur number $S(n)$ is the largest $N$ for which $\{1,\dots,N\}$ admits a partition into $n$ sum-free sets. The sequence

\[
S(1)=1,\quad S(2)=4,\quad S(3)=13,\quad S(4)=44,\quad S(5)=160
\]

is exactly known; the last value was settled by Heule's *Schur Number Five* (2017), a SAT computation whose unsatisfiability certificate - a DRAT proof of roughly two petabytes - is the largest formal proof produced to date. $S(6)$ is open. This is the single most direct sibling of our $R(5,5)$ work: the object is a colouring of an interval, the lower bound is a witness that is trivially checkable, and the upper bound is a propositional unsatisfiability claim over a clean CNF. The task is to produce **certified bounds on $S(6)$** - an independently verified explicit $6$-colouring giving a record lower bound, and whatever SAT-based or analytic progress on the upper side is reachable on one workstation. The resolution standard in section 2 (the exact value of $S(6)$ with a machine-checkable proof both ways) is the target; every lesser result - a record colouring, a partial UNSAT lemma, a tightened analytic bound - is reported honestly as a partial result and never represented as determining $S(6)$.

## 1. Exact problem statement

Fix the integer interval $[1,N]=\{1,2,\dots,N\}$. A set $A\subseteq\mathbb{Z}_{>0}$ is **sum-free** (in the Schur, or *strong*, sense) if there is no solution to

\[
x+y=z,\qquad x,y,z\in A,
\]

where $x=y$ is permitted. Equivalently $A$ contains no $a,b$ (possibly equal) with $a+b\in A$; in particular no $a$ with $2a\in A$ can share a class with $a$. An $n$-colouring $c:[1,N]\to\{1,\dots,n\}$ is **sum-free** (a *Schur colouring*) if every colour class $c^{-1}(k)$ is sum-free. The triple $\{x,y,x+y\}$ (with $x=y$ allowed, giving $\{x,2x\}$) is a **Schur triple**; a colouring is sum-free iff no Schur triple is monochromatic.

**Definition.** $S(n)$ is the largest $N$ such that a sum-free $n$-colouring of $[1,N]$ exists. Equivalently, $S(n)+1$ is the least $N$ for which every $n$-colouring of $[1,N]$ contains a monochromatic Schur triple.

*Micro-example.* $S(2)=4$: the colouring $\{1,4\},\{2,3\}$ of $[1,4]$ is sum-free (no class contains $x,y,x+y$), while every $2$-colouring of $[1,5]$ has a monochromatic Schur triple.

We adopt the **strong** Schur condition (allowing $x=y$), which is the convention under which $S(5)=160$. This must not be confused with:

- the **weak Schur number** $\mathrm{WS}(n)$, which forbids only $x+y=z$ with $x,y,z$ *pairwise distinct* (so $\mathrm{WS}(n)\ge S(n)$; e.g. $\mathrm{WS}(5)=196$). $\mathrm{WS}$ is a different sequence and is **not** the target here;
- the **modular** Schur numbers, which partition the cyclic group $\mathbb{Z}/m\mathbb{Z}$ rather than an interval.

The open question addressed by this prompt: **determine $S(6)$, or the sharpest certified two-sided bracket**

\[
L\le S(6)\le U .
\]

A lower bound $S(6)\ge L$ is witnessed by an explicit sum-free $6$-colouring of $[1,L]$. An upper bound $S(6)\le U$ is the statement that no sum-free $6$-colouring of $[1,U+1]$ exists - a propositional unsatisfiability claim (section 5).

## 2. Resolution standard

A **complete resolution** determines $S(6)=V$ for an explicit integer $V$ and supplies both:

1. **Lower certificate.** An explicit sum-free $6$-colouring $c:[1,V]\to\{1,\dots,6\}$, given as a machine-readable vector, together with a soundness argument that its colour classes are sum-free.
2. **Upper certificate.** A machine-checkable proof that the CNF $\Phi_{6,V+1}$ (section 5) is unsatisfiable, in **DRAT or LRAT** form, checked by an independent proof checker (`drat-trim`, `dpr-trim`, or an LRAT checker), together with a proof that $\Phi_{6,V+1}$ faithfully encodes "no sum-free $6$-colouring of $[1,V+1]$". The fidelity argument must cover:
   - the at-least-one / at-most-one colour clauses (each integer receives exactly one colour);
   - the Schur-triple exclusion clauses (every monochromatic triple is forbidden, including the $x=y$ case);
   - every symmetry-breaking predicate, shown satisfiability-preserving.

Symmetry-breaking predicates added to $\Phi$ are permitted only if accompanied by a proof (or an independently reproduced argument) that they preserve satisfiability, exactly as in the $S(5)$ work.

**Not accepted as resolution.**

- A record lower-bound colouring alone (it bounds $S(6)$ from below only).
- An UNSAT result whose proof is not emitted in a certified format, or whose DRAT/LRAT trace is not independently checked, or whose encoding fidelity is not argued.
- A "SAT solver returned UNSAT" claim without a preserved, replayable proof object (the trace, or a documented reason it is too large to store, with a segment-checking protocol).
- A colouring found by a heuristic and reported without an exact sum-free verification.
- A bound proved only for the weak Schur number $\mathrm{WS}(6)$, or only modularly, presented as a statement about $S(6)$.
- Any numerical or probabilistic estimate of $S(6)$.
- Matching the value to an OEIS entry or a survey figure without reproducing a certificate.

Honest calibration: full resolution is **not** expected. The two-petabyte proof already required for $S(5)$ at $N=161$ makes an UNSAT proof near the true value of $S(6)$ (which exceeds $536$) far beyond a single workstation. The realistic product is a certified record lower bound plus partial upper-side lemmas.

## 3. Graded partial-result targets

Ordered milestones, each independently valuable and separately certifiable.

**P1 - Reproduce the frontier with our toolchain.** Re-derive $S(5)=160$ end to end:

- (a) emit a sum-free $5$-colouring of $[1,160]$ with an exact class-wise verifier;
- (b) build $\Phi_{5,161}$ with the same symmetry breaking as *Schur Number Five*, run a modern solver, and obtain UNSAT with a DRAT proof;
- (c) independently check as much of that proof as storage allows, documenting a segment-checking protocol for the part that cannot be stored.

*Certificate:* the $[1,160]$ colouring + verifier, and a checked (possibly partial) DRAT trace for $N=161$, with a SHA-256 manifest. This validates the pipeline against a known answer before any new claim.

**P2 - Certify the current record lower bound.** Reproduce and independently verify an explicit sum-free $6$-colouring of $[1,536]$ (or the current record $L_0$; see section 4), yielding $S(6)\ge L_0$. *Certificate:* the colouring as a length-$L_0$ vector over $\{1,\dots,6\}$; a standalone checker that scans every triple $\{a,b,a+b\}$ with $a+b\le L_0$ and confirms no monochromatic Schur triple; a canonical serialization and hash.

**P3 - Improve the lower bound.** Find a sum-free $6$-colouring of $[1,L_0+1]$ or longer, giving $S(6)\ge L_0+1$. The growth ratios $S(5)/S(4)=160/44\approx3.6$ against $536/160\approx3.35$ suggest headroom, so this target is genuinely open. Methods:

- SAT with the interval fixed to $N=L_0+1$ and heavy symmetry breaking;
- tabu / simulated-annealing search over colour vectors, minimizing the count of monochromatic Schur triples;
- extending the record colouring's block structure by hand-guided repair.

*Certificate:* the new colouring, exact-verified as in P2, with the search source preserved.

**P4 - Structure mining and a parametric construction.** Extract the algebraic structure of the best colourings - arithmetic-progression blocks, multiplicative/affine templates, and the reflection symmetry $x\mapsto N+1-x$ - and turn it into a parametric family $c_n$ giving a lower bound $S(n)\ge f(n)$ that beats the recursive $S(n)\ge 3S(n-1)+1$ (which only gives $S(6)\ge481$) and is certified at $n=6$. *Certificate:* the construction with a proof its classes are sum-free for the stated parameters, plus the concrete $n=6$ instance verified as in P2.

**P5 - Partial upper-side SAT lemmas.** For values $N$ within reach, produce certified UNSAT results for *restricted* problems: $\Phi_{6,N}$ augmented with structural assumptions (fixed colours of small elements, forced block boundaries, or an assumed automorphism), each restriction proved satisfiability-preserving or clearly labelled conditional. Emit DRAT/LRAT and check independently. *Certificate:* per-instance CNF, solver log, checked proof trace, and a precise statement of what was proved (unconditional or conditional-on-stated-structure).

**P6 - Strongest result short of resolution.** Any of:

- (a) a certified two-sided bracket $L\le S(6)\le U$ narrower than the published $536\le S(6)\le 1836$, with both sides machine-checked;
- (b) an improved *unconditional* upper bound via the Ramsey/analytic route (section 5) with a machine-verified numerical core;
- (c) a full determination of $S(6)$ meeting section 2 (windfall).

*Certificate:* both directional certificates to the section-2 standard for whatever bracket is claimed.

## 4. Known results and prior art

- **Exact values.** $S(1)=1,\ S(2)=4,\ S(3)=13,\ S(4)=44$ (classical, Baumert/Golomb-era computations, mid-20th century) and $S(5)=160$, proved by **Marijn Heule**, *Schur Number Five* (2017; AAAI 2018). The UNSAT proof at $N=161$ is a DRAT certificate of roughly two petabytes, generated by a cube-and-conquer split and checked with a verified checker.
- **Lower bounds for $S(6)$.** $S(6)\ge 536$, from a symmetric sum-free partition - **Fredricksen and Sweet**, "Symmetric sum-free partitions and lower bounds for Schur numbers" (Electron. J. Combin., 2000) (verify the exact record; later work may have improved it). More recent constructions of Schur and weak-Schur lower bounds for larger $n$ appear in work of **Ageron, Eliahou, and coauthors** (c. 2021) - check whether their methods raise the $n=6$ record above $536$ (verify).
- **Upper bound for $S(6)$.** $S(6)\le 1836$ is the commonly cited figure (verify), descending from the relation $S(n)\le R_n(3)-2$ to the multicolour triangle Ramsey number $R_n(3)$ and its factorial-type upper bound. Any tightening of $R_6(3)$ tightens this.
- **The Ramsey link.** A sum-free $n$-colouring of $[1,N]$ yields a triangle-free $n$-edge-colouring of $K_{N+1}$ (the Schur/Cayley construction), so

  \[
  R_n(3)\ge S(n)+2 .
  \]

  This ties problem 12 to problem 15 ($R(3,3,3,3)$) and to the diagonal multicolour ladder.
- **Recursive lower bound.** $S(n)\ge 3\,S(n-1)+1$, giving $S(6)\ge481$ from $S(5)=160$ - weaker than the construction record, but a sanity floor.
- **Method lineage.** SAT encodings with lexicographic / colour-class symmetry breaking, cube-and-conquer partitioning, and DRAT proof logging are the state of the art here, exactly the toolchain of the $R(5,5)$ program.

**Status as of mid-2026 - re-verify against the current literature before starting any session.** In particular re-check whether the $S(6)\ge536$ lower bound has been improved, whether the $\le1836$ upper bound still stands, and whether any new SAT result narrows the interval.

## 5. Attack plan

**CNF encoding (`[search]`/`[cert]`).** Variables $x_{i,k}$ for $i\in[1,N]$, $k\in\{1,\dots,6\}$, meaning "$i$ has colour $k$". The CNF $\Phi_{6,N}$ has clauses:

- *At-least-one colour:* $\displaystyle\bigvee_{k=1}^{6} x_{i,k}$ for each $i\in[1,N]$ (add *at-most-one* for a cleaner model; for existence, at-least-one suffices and is smaller);
- *Schur-triple exclusion:* for each colour $k$ and each pair $a\le b$ with $a+b\le N$,

  \[
  \lnot x_{a,k}\ \lor\ \lnot x_{b,k}\ \lor\ \lnot x_{a+b,k},
  \]

  where the case $a=b$ degenerates to $\lnot x_{a,k}\lor\lnot x_{2a,k}$.

The exclusion clauses number $\Theta(6\,N^2)$. Symmetry breaking: fix the colour of $1$; break colour-permutation symmetry with a standard lex predicate; optionally fix small elements as in the $S(5)$ model. Every added predicate is logged with a satisfiability-preservation note.

**Solvers and proofs.** Lower-bound / feasibility searches at fixed $N$: **CaDiCaL** and **kissat**; for record-chasing at $N\approx L_0$, run parallel seeds and a local-search phase (**CryptoMiniSat**, or a bespoke tabu search over colour vectors). Upper-bound / UNSAT attempts on restricted instances: **CaDiCaL** or **kissat** with **DRAT** logging; convert to **LRAT** and check with `drat-trim` / `dpr-trim` or an LRAT checker. Cube-and-conquer (`march_cu`-style splitting) for any instance that does not close directly.

**Custom C++ / SageMath.** A standalone verifier (a few dozen lines) reads a colour vector and rejects on the first monochromatic Schur triple - this is the load-bearing lower-bound checker and must be independent of the search code. SageMath / Python for structure mining of good colourings (block boundaries, the $x\mapsto N+1-x$ symmetry, residue patterns) feeding P4.

**One-workstation scope.** Feasible: exact verification of any candidate $6$-colouring up to $N\sim10^4$ (milliseconds); local / SAT search for record colourings at $N\approx536$–$600$; restricted UNSAT lemmas (P5) for modest $N$; full reproduction of the $[1,160]$ colouring. **Out of scope on one machine:** an UNSAT proof anywhere near the true $S(6)$ - the $S(5)$ proof was already ~2 PB at $N=161$, so honest reporting must not promise the upper side. **Failure modes:** at-most-one clause blow-up (use commander / ladder encodings if needed); solver timeouts on unrestricted UNSAT (expected - pivot to restricted lemmas); DRAT traces too large to store (document a segmented re-derivation protocol rather than claim an unchecked UNSAT); local search plateaus (diversify seeds, seed from the record colouring).

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every lower bound is a colour vector checked by exact integer arithmetic over all Schur triples; every upper bound is a DRAT/LRAT proof checked by a formal proof checker. Floating point and solver "UNSAT" prints are exploration only - never certification. Encoding-fidelity arguments accompany every CNF.
2. **Independent verification.** The lower-bound checker is written independently of the search / encoder (ideally a second implementation and a second language). UNSAT traces are checked by a proof checker not derived from the solver; where a trace is too large to store in full, a documented segment-recheck protocol stands in and is stated as such.
3. **Reproducibility.** All CNF generators, symmetry-breaking predicates, solver versions and flags, random seeds, and the environment are recorded; a SHA-256 manifest covers every colouring, CNF, proof trace, and log.
4. **Preservation.** All search and construction source - encoders, local-search code, cube generators, verifiers - is part of the record (the Hadamard-668 lost-source lesson). Anything not preserved (e.g. a multi-petabyte trace) is named explicitly with the protocol to regenerate and spot-check it, never silently dropped.
5. **Honest reporting.** The report states up front whether $S(6)$ was determined (almost certainly not) and reports each result at its true strength - "certified $S(6)\ge L$", "conditional UNSAT lemma", "reproduced $S(5)=160$" - and never presents a record lower bound or a restricted lemma as the value of $S(6)$.
