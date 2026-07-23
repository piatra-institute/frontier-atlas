# PROMPT FOR EXACT SEPARATIONS AMONG SENSITIVITY, BLOCK SENSITIVITY, AND DEGREE

## The still-open \(s\)–\(bs\) gap and small-\(n\) extremal Boolean functions, post-Huang

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 17 of 50
**Area:** complexity & communication
**Modes:** `[search]` `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Sensitivity \(s(f)\), block sensitivity \(bs(f)\), and real polynomial degree \(\deg(f)\) are among the most-studied combinatorial complexity measures of a Boolean function, and their mutual polynomial equivalence underlies decision-tree, quantum-query, and circuit theory. **The sensitivity conjecture - that \(\deg(f)\) is polynomially bounded by \(s(f)\) - was proved by Huang in 2019** (\(\deg(f)\le s(f)^2\), whence \(bs(f)\le s(f)^4\)); that headline is closed and is not a target here. What remains stubbornly open are the **exact** relationships: the true maximal gap between \(s\) and \(bs\) (best known quadratic, \(bs\approx\tfrac23 s^2\), against an upper bound \(bs\le 2s^4\)), the tight constants and exponents, and the extremal functions that realize the extremes at each small arity \(n\). These are precisely the questions where exhaustive small-\(n\) computation produces a durable, certifiable object: the exact \((s,bs,\deg,C)\) profile of every Boolean function up to some \(n\), together with the extremal witnesses. The on-machine verifier is a direct evaluator of \(s,bs,\deg\) from the truth table plus an isomorph-free enumerator that certifies extremality. Anything short of section 2 - a suggestive family with no matching bound, a non-exhaustive sample presented as an extremum - is a partial result.

## 1. Exact problem statement

Let \(f:\{0,1\}^n\to\{0,1\}\). For \(x\in\{0,1\}^n\) and \(B\subseteq[n]\), let \(x^{B}\) be \(x\) with the coordinates in \(B\) flipped. Define, at a point \(x\),

\[
s(f,x)=\big|\{i\in[n]:f(x^{\{i\}})\ne f(x)\}\big|,\qquad s(f)=\max_x s(f,x).
\]

The **block sensitivity** at \(x\) is the maximum number \(k\) of pairwise-disjoint blocks \(B_1,\dots,B_k\subseteq[n]\) with \(f(x^{B_j})\ne f(x)\) for all \(j\), and

\[
bs(f)=\max_x bs(f,x).
\]

The companions are **certificate complexity** \(C(f)\), the real **degree**

\[
\deg(f)=\deg\Big(\text{unique multilinear }p\text{ with }p(x)=f(x)\ \forall x\in\{0,1\}^n\Big),
\]

the **approximate degree** \(\widetilde{\deg}(f)\), and the **decision-tree depth** \(D(f)\). The basic order is

\[
s(f)\ \le\ bs(f)\ \le\ C(f)\ \le\ D(f)\ \le\ \deg(f)^{\,O(1)}.
\]

**Gated fact (do not target).** Huang (2019): \(\deg(f)\le s(f)^2\) for all \(f\); consequently

\[
bs(f)\ \le\ \deg(f)^2\ \le\ s(f)^4 .
\]

Every workstream must state this bound explicitly and treat "is the sensitivity conjecture true?" as answered **YES**. Record the exact constant of any sharper consequence used (verify).

**Open questions (adopted here).**

1. **Exact \(s\)–\(bs\) gap.** Determine the exponent

\[
\sigma^\*=\sup_f \frac{\log bs(f)}{\log s(f)}.
\]

The best lower witness gives \(bs\ge\tfrac23 s^2-\tfrac13 s\) (a quadratic gap realized only with constant \(\tfrac23\)); the upper bound is \(bs\le 2s^4\). Pin the exponent and the tight constant.

2. **Small-\(n\) extremal profiles.** For each \(n\), compute \(\max_f bs(f)/s(f)^2\), \(\max_f \deg(f)/s(f)^2\), \(\max_f \deg(f)/bs(f)\), and \(\max_f C(f)/bs(f)\), and exhibit the extremal \(f\).

3. **Tight companion constants.** Which of \(C\le bs^2\), \(\deg\le bs\cdot?\), etc. are tight, and where.

**Starting from the prompt alone.** A reader reconstructs \(f\) from a \(2^n\)-bit truth table and computes \(s,bs,C,\deg\) directly - \(s\) by neighbour flips, \(bs\) by a max-disjoint-blocks search or small ILP per point, \(\deg\) by the Möbius/Fourier transform - so every measure in section 2 is machine-checkable from the object alone.

## 2. Resolution standard

Full resolution of an open question above is a **proof** (for an exponent/constant, valid for all \(f\)) or a **certified extremal census** (for the small-\(n\) values). Named certified forms:

- **Exact measure census.** For a stated \(n\), the exact tuple \((s,bs,C,\deg,\widetilde{\deg},D)\) for a canonical representative of **every** NPN-equivalence class of \(n\)-bit functions (negation of inputs, permutation of inputs, negation of output), with the extremal ratios and their witnesses. The census is certified by (a) a complete, isomorph-free class enumerator whose class count matches the known NPN count for that \(n\), and (b) a measure evaluator run on every representative.

- **Proof artifact** (for an exponent/constant claim): a formal Lean 4 / Coq proof, or a finite reduction to a machine-checked base case (a tight-example family plus a proved recursion), independently replayed.

**Not accepted as resolution.**

- Reporting Huang's theorem, or any consequence of it, as new - it is the gate, not the target.

- A separating **family** offered without a matching upper bound as the "maximal gap"; a construction bounds \(\sigma^\*\) from below only.

- A **sampled** or heuristic search over \(n\)-bit functions presented as an extremum, when the class enumeration is not exhaustive/isomorph-free for that \(n\).

- Floating-point degree computation (round-off can drop or invent a monomial); \(\deg\) must be computed in exact integer/rational Fourier arithmetic.

- \(bs\) computed by a greedy block choice rather than a certified maximum disjoint-block packing.

- Asymptotic \(O/\Omega\) statements where an exact small-\(n\) value or a tight constant is requested.

## 3. Graded partial-result targets

- **P1 - Verified measure evaluator + tiny census.** Implement exact \(s,bs,C,\deg\) and enumerate all NPN classes for \(n\le 4\); reproduce the known small extremal ratios.
  *Certificate:* class count equals the known NPN count for each \(n\le4\); full \((s,bs,\deg,C)\) table; a second, independent evaluator agrees on every representative.

- **P2 - Extend the census to \(n=5,6\).** Complete the isomorph-free census and extremal-ratio extraction for \(n=5\) and, as far as compute allows, \(n=6\) (via NPN canonical forms).
  *Certificate:* matching NPN class counts; extremal witnesses with their exact tuples; resource log stating where the enumeration closed.

- **P3 - Certified \(s\)–\(bs\) extremal witnesses.** For each \(n\) in range report the exact \(\max_f bs(f)/s(f)^2\) and the function(s) achieving it; compare against the \(\tfrac23\)-constant Ambainis–Sun family restricted to that \(n\).
  *Certificate:* exhaustive extremality within the census; explicit witness truth tables.

- **P4 - Push the finite \(s\)–\(bs\) construction.** Search (SAT/ILP-guided, not exhaustive) for a function on \(n\) beyond the census with a certified ratio \(bs(f)/s(f)^2\) strictly exceeding the best census value or the \(\tfrac23\) asymptotic constant at finite \(n\).
  *Certificate:* exact \(s\) and a certified maximum disjoint-block packing for \(bs\); a diff against the best known finite ratio with source.

- **P5 - Tight-constant sub-lemmas, machine-checked.** Formalize (Lean 4/Coq) one exact inequality with its tightness at small \(n\) - e.g. \(C(f)\le bs(f)^2\) with the extremal small witness, or a clean case of \(bs\le \deg^2\).
  *Certificate:* a checked proof term plus the extremal instance the census produced.

- **P6 - Degree-vs-block-sensitivity small extrema.** Tabulate \(\max_f \deg(f)/bs(f)\) over the census and identify the extremal functions, contributing exact data to the still-open exact \(\deg\)-vs-\(bs\) separation.
  *Certificate:* exhaustive extremality within the census; witnesses.

## 4. Known results and prior art

- **Sensitivity conjecture - PROVED.** Huang, "Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture," Annals of Mathematics 190 (2019), 949–955: \(\deg(f)\le s(f)^2\). This is the gate. (verify)

- **Best \(s\)–\(bs\) separation.** Ambainis–Sun (\(\approx\)2011, "New separation between \(s(f)\) and \(bs(f)\)," arXiv 1108.3494, verify): \(bs(f)\ge \tfrac23 s(f)^2-\tfrac13 s(f)\), improving the constant from Rubinstein's \(\tfrac12\) (\(\approx\)1995, verify); the quadratic remains the largest known gap. Foundational relations: Nisan–Szegedy (\(\approx\)1994, verify).

- **Upper bounds on \(bs\) via \(s\).** Following Huang, \(bs(f)\le \deg^2\le s^4\); refinements of the constant/exponent appear in follow-ups (record the exact statement and constant actually used, verify).

- **Certificate vs block sensitivity.** Exact relations \(bs\le C\le bs^2\); tightness questions and small extremal functions (Kenyon–Kutin, and later works on \(C\) vs \(bs\), verify).

- **Degree vs block sensitivity - still open exactly.** "On Separation between the Degree of a Boolean Function and the Block Sensitivity" (arXiv 2101.08600, verify) and related; the exact \(\deg\)-vs-\(bs\) exponent is not settled.

- **Small-\(n\) data.** Partial tables of \((s,bs,\deg)\) for small \(n\) circulate in lecture notes and the complexity-measure literature; a fully certified isomorph-free census with extremal witnesses is the P1–P2 product.

**Status as of mid-2026 - re-verify against the current literature before starting any session.**

## 5. Attack plan

**`[search]` - census by NPN canonical enumeration.** For \(n\le6\), generate one canonical representative per NPN-equivalence class (input permutations, input negations, output negation) using an orderly/canonical-augmentation scheme; cross-check the class count against the published NPN counts (a hard correctness gate). For each representative compute:

- \(s\) by direct neighbour flips;

- \(bs(f,x)\) as a **maximum disjoint-block packing**, solved exactly per point by ILP (`SCIP` exact) or a small exact set-packing search, then \(bs=\max_x\);

- \(C(f)\) via minimal certificates (exact set cover);

- \(\deg\) via the exact integer Möbius/Fourier transform.

Extract all extremal ratios.

**`[search]` beyond the census.** For P4, use SAT/SMT or ILP to *construct* candidate high-\(bs/s^2\) functions on larger \(n\) (encode "\(s(f)\le a\) and \(bs(f)\ge b\)"), with proof logging where the encoding admits DRAT.

**`[proof]` - tight-constant lemmas.** Formalize the base inequalities and their small extremal witnesses in Lean 4 (Mathlib has finite Boolean-function scaffolding) or Coq; keep each lemma small and independently replayable.

**Tools.** Custom C++ for enumeration and measure evaluation; `SageMath`/`FLINT` for exact Fourier/Möbius and NPN canonicalization cross-checks; `SCIP`/`SoPlex` exact for the \(bs\) and \(C\) packings/covers; `kissat`/`CaDiCaL` with DRAT for the construction searches; Lean 4 for P5.

**One-workstation scope.** \(n\le4\): trivial. \(n=5\): the census is comfortable. \(n=6\): the NPN class count is large; expect the full census to be the boundary of a single workstation - report exactly how far it closed.

**Failure modes.** Greedy \(bs\) undercounts (must be exact max packing); floating-point \(\deg\) is unsafe; an off-by-one in NPN canonicalization corrupts the whole census (gate on the known class count); construction SAT instances blow up quickly past the census range.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** \(s,bs,C,\deg\) are computed in exact arithmetic; \(bs\) and \(C\) use certified optimal packings/covers, not greedy heuristics; \(\deg\) uses exact Fourier/Möbius. No floating point in any load-bearing measure.

2. **Independent verification.** A second, independently written measure evaluator recomputes every reported tuple; the enumeration's class count is checked against the known NPN count for each \(n\); each formal lemma (P5) is replayed by the proof kernel from source.

3. **Reproducibility.** Truth-table format, NPN canonicalization convention, solver versions and exact flags, and enumeration order are recorded; a SHA-256 manifest covers every representative, tuple, witness, and proof term; the prior small-\(n\) table or finite ratio being improved is cited with source and access date.

4. **Preservation.** Enumerator, evaluator, packing/cover solvers, and formal proofs are part of the record; anything not preserved is stated explicitly.

5. **Honest reporting.** The report opens by restating that the sensitivity conjecture is Huang's theorem and is not a target, then states which \(n\) the census closed for, which extremal ratios and witnesses are now certified, and whether any finite \(s\)–\(bs\) ratio strictly beats the best known. A construction is never reported as pinning an exponent supremum without a matching upper bound.
