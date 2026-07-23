# PROMPT FOR CLASSIFYING AND COUNTING BENT FUNCTIONS IN TEN VARIABLES

## Certified enumeration of bent (and almost-bent) functions within a fixed degree or symmetry class

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 10 of 50
**Area:** Boolean & cryptographic functions
**Modes:** `[enum]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Bent functions are the Boolean functions of maximum nonlinearity in even dimension - flat Walsh spectrum, perfect resistance to linear approximation - and they sit at the crossroads of coding theory, difference sets, and combinatorial design. Their complete enumeration is a benchmark for how far exact classification can be pushed: settled for \(n\le 6\) and, in a landmark computation, *counted* for \(n=8\) by Langevin and Leander; for \(n\ge 10\) the count and classification are **wide open**, with only partial families known. The task is a natural fit for canonical, isomorph-free enumeration and certified search: bent-ness is an exact spectral condition on a length-\(2^n\) vector, equivalence is governed by the affine group and by nauty-style canonical forms, and progress is realistically made inside a fixed algebraic degree or symmetry class where the space is finite-in-practice. The on-machine verifier is a Walsh–Hadamard transform confirming \(|W_f|\equiv 2^{n/2}\); anything short of the Section 2 standard - a partial family with no certified completeness, an equivalence claim without a canonical certificate - is a partial result, never a classification.

## 1. Exact problem statement

Notation as in the Boolean-function conventions: \(f:\mathbb{F}_2^n\to\mathbb{F}_2\) in \(\mathcal{B}_n\), sign function \(\hat f(x)=(-1)^{f(x)}\), Walsh–Hadamard transform
\[
W_f(w)=\sum_{x\in\mathbb{F}_2^n}(-1)^{f(x)+\langle w,x\rangle}.
\]
For **even** \(n\), \(f\) is **bent** iff \(|W_f(w)|=2^{n/2}\) for every \(w\in\mathbb{F}_2^n\); equivalently \(\mathrm{nl}(f)=2^{n-1}-2^{n/2-1}\) is maximal, equivalently the derivative \(D_af(x)=f(x+a)+f(x)\) is balanced for every \(a\neq 0\) (\(f\) is *perfect nonlinear*). Bent functions are never balanced and exist only for even \(n\).

Two structural facts are used repeatedly. First, **Parseval** \(\sum_w W_f(w)^2=2^{2n}\) forces \(\max_w|W_f(w)|\ge 2^{n/2}\), so bent functions are exactly the equality case - the flat-spectrum functions. Second, every bent \(f\) has a **dual** \(\tilde f\) defined by \(W_f(w)=2^{n/2}(-1)^{\tilde f(w)}\), itself bent, with \(\tilde{\tilde f}=f\); duality is an involution on the bent set that the enumeration can exploit and must respect. The **Hamming weight** of a bent function is \(2^{n-1}\pm 2^{n/2-1}\).

Write \(\mathrm{wt}(u)\) for the Hamming weight of \(u\) and \(\langle w,x\rangle=\sum_i w_ix_i\bmod2\). The group acting is the **general affine group** \(\mathrm{AGL}(n,\mathbb{F}_2)=\mathbb{F}_2^n\rtimes\mathrm{GL}(n,\mathbb{F}_2)\), of order \(2^n\prod_{i=0}^{n-1}(2^n-2^i)\), extended by the addition of affine functions; affine equivalence preserves bent-ness, degree, and the flat spectrum, and the enumeration counts orbits under this action.

The **algebraic normal form (ANF)** writes \(f(x)=\bigoplus_{S\subseteq[n]} a_S \prod_{i\in S}x_i\); the **algebraic degree** \(\deg f\) is the largest \(|S|\) with \(a_S=1\). Bent functions satisfy \(\deg f\le n/2\) (for \(n\ge 4\)).

Two functions are **affine-equivalent** if \(g(x)=f(Ax+b)+\langle c,x\rangle+d\) for an invertible \(A\in\mathrm{GL}(n,\mathbb{F}_2)\), \(b,c\in\mathbb{F}_2^n\), \(d\in\mathbb{F}_2\); the group is the general affine group \(\mathrm{AGL}(n,\mathbb{F}_2)\) extended by the addition of affine functions. Classification means listing bent functions up to this equivalence; enumeration means counting them (with or without the equivalence quotient, stated explicitly).

**Companion object (vectorial / almost bent).** A vectorial function \(F:\mathbb{F}_2^n\to\mathbb{F}_2^m\) is **bent (vectorial)** if every nonzero linear combination of its coordinates is bent (needs \(m\le n/2\)); for **odd** \(n\), \(F:\mathbb{F}_2^n\to\mathbb{F}_2^n\) is **almost bent (AB)** iff its Walsh spectrum is \(\{0,\pm2^{(n+1)/2}\}\) - AB functions meet the nonlinearity bound in odd dimension and are always APN (the converse fails). These are the "almost-bent" companions of the bent problem.

**Two standing conventions.** (i) "Count" is ambiguous unless one says whether it counts *functions* or *affine-equivalence classes*; both are reported, labelled, and never interchanged. (ii) The equivalence relation is fixed at the start - affine equivalence for the classification, with any use of the coarser extended-affine/CCZ notion stated explicitly - because the literature's counts are relation-specific and silent mismatches are the commonest error.

**Primary superclasses.** The **Maiorana–McFarland** class \(\mathcal{M}\) consists of \(f(x,y)=\langle x,\pi(y)\rangle+g(y)\) on \(\mathbb{F}_2^{n/2}\times\mathbb{F}_2^{n/2}\) with \(\pi\) a permutation; the **partial-spread** classes \(\mathcal{PS}^+,\mathcal{PS}^-\) (Dillon) are built from \(2^{n/2}\pm1\) pairwise-trivially-intersecting \(n/2\)-subspaces. Not every bent function is (affine-equivalent to one) in \(\mathcal{M}\cup\mathcal{PS}\); measuring the size of this "outside" region is a core motivation of the enumeration.

**Known total counts** (unrestricted, all bent functions, not up to equivalence):
\[
|\mathcal{B}^{\mathrm{bent}}_2|=8,\quad |\mathcal{B}^{\mathrm{bent}}_4|=896,\quad |\mathcal{B}^{\mathrm{bent}}_6|=5{,}425{,}430{,}528,\quad |\mathcal{B}^{\mathrm{bent}}_8|\approx 2^{106.3},
\]
with \(n=8\) the last known exactly (Langevin–Leander) and \(n\ge10\) open.

**The question, adopted scope.** Produce a certified enumeration and/or classification of bent functions in \(n=10\) variables **within a fixed algebraic degree or symmetry class** (e.g. degree \(\le 3\) "cubic" bent, rotation-symmetric bent, homogeneous bent, or a fixed superclass such as \(\mathcal{PS}\) / Maiorana–McFarland), and/or a certified count or bound; secondary scope: almost-bent functions in a fixed odd dimension/class. Cost is measured in exactly-verified bent tests, canonical (nauty-checked) equivalence-class counts, and - for any exhaustiveness claim - orbit-enumeration completeness certificates.

## 2. Resolution standard

Because the *unrestricted* \(n=10\) count is astronomically beyond exhaustive reach, "resolution" here is scoped per target and always carries an exact completeness certificate. A **certified classification/enumeration of class \(C\)** at \(n=10\) consists of:

- an explicit, **isomorph-free** list (or exact count) of the bent functions in \(C\) up to the stated equivalence, and
- a machine-checkable **completeness certificate**: either an exhaustive canonical generation (nauty/orderly generation, with the canonical form independently recomputed) covering all of \(C\), or a DRAT/LRAT-certified argument that no bent function in \(C\) was missed.

Named certified forms:

- **(a) Exhaustive/canonical enumeration** via **nauty** (or bliss/orderly generation) with recomputed canonical labels.
- **(b) SAT-with-DRAT** for existence/nonexistence or exact-count sub-cases.
- **(c) Exact algebraic classification** (e.g. all cubic bent in \(n=10\) via a certified reduction to a finite orbit problem) with a rational/group-theoretic certificate.
- **(d) Burnside/orbit-counting certificate:** an exact count of orbits under \(\mathrm{AGL}(n,\mathbb{F}_2)\) via the Cauchy–Frobenius lemma over certified fixed-point data, cross-checking a canonical-list length.

**Not accepted as resolution.**

- A new infinite family or a set of bent functions in \(n=10\) with **no** certified completeness within a delimited class - that is a construction, not a classification.
- A count reported without stating the acting equivalence group and whether functions or classes are counted.
- A "these are all the bent functions in class \(C\)" claim whose orderly-generation exhaustiveness is asserted but not proved.
- An equivalence-class count from string-comparing ANFs or truth tables without a certified canonical form (missed or duplicated classes void the count).
- A bent-ness claim whose Walsh spectrum is not recomputed by an independent transform.
- A restricted-class count presented as the *total* number of bent functions in \(n=10\).
- Re-deriving the Langevin–Leander \(n=8\) count without an independent completeness certificate and calling the \(n=10\) problem advanced.
- Numerical/heuristic estimates of the \(n=10\) count in place of a certified count or a rigorously proved bound.
- A count that conflates "number of bent functions" with "number of affine-equivalence classes" - state which, always.
- A self-dual / non-self-dual tally that ignores the dual involution's fixed points.
- An almost-bent claim in odd \(n\) whose \(\{0,\pm2^{(n+1)/2}\}\) spectrum is not recomputed, or that silently conflates AB with APN (AB \(\Rightarrow\) APN, not conversely).

## 3. Graded partial-result targets

**P0 - Quadratic base case.** Reproduce the complete classification of quadratic bent functions at \(n=6,8,10\) (a single affine-equivalence class each, tied to non-degenerate symplectic forms) as the smallest end-to-end validation of the bent-test-plus-canonicalization pipeline. *Certificate:* recomputed spectra plus a canonical-form proof of single-orbit-ness.

**P1 - Reproduce the frontier.** Independently enumerate/count bent functions for \(n\le 6\) with a canonical, isomorph-free pipeline (the \(n=6\) affine-equivalence classes are few and known), verifying each is bent by recomputed Walsh spectrum. *Certificate:* canonical-form-checked class list with SHA-256, matching known class counts.

**P2 - Recount \(n=8\) partially.** Reproduce a certified sub-count of the \(n=8\) bent population - e.g. the exact number of cubic (degree-3) bent functions, or the count of self-dual bent functions, or the count within a fixed symmetry class - as an independent validation of the enumeration engine against published figures. *Certificate:* orbit/canonical-generation completeness plus recomputed spectra, matching the published sub-count.

**P3 - A fixed \(n=10\) class, certified.** Choose a class \(C\) in \(n=10\) that is finite-in-practice (rotation-symmetric bent, homogeneous cubic bent, or bent within Maiorana–McFarland / partial-spread parameters) and produce a certified isomorph-free classification or exact count. *Certificate:* canonical-generation completeness for \(C\), recomputed bent tests, nauty-checked class distinctness.

**P4 - Existence/nonexistence within a degree.** Decide, with a certificate, whether homogeneous bent functions of a given degree exist in \(n=10\) (the homogeneous-bent existence question is delicate), or settle a specific parameter of the partial-spread / \(\mathcal{PS}^-\) construction. *Certificate:* explicit witnesses (recomputed spectra) or a DRAT/LRAT / canonical-enumeration nonexistence proof.

**P5 - Certified count or rigorous bound for a broader \(n=10\) class.** Extend P3 to a wider class, or prove an exact rigorous upper/lower bound on the \(n=10\) bent count within a stated degree cap. A certified count of the *non-normal* bent functions in a fixed \(n=10\) family, or of the \(\mathcal{M}\)-outside population, would be especially informative. *Certificate:* completeness certificate or an exact combinatorial bound with rational certificate.

**P6 - Almost-bent companion.** Produce a certified classification/enumeration of almost-bent functions in a fixed odd dimension or class (e.g. AB monomials/quadratics in \(n=9\)) up to CCZ/affine equivalence, cross-referenced to the APN inventory (problem 08). *Certificate:* recomputed Walsh spectra confirming the \(\{0,\pm2^{(n+1)/2}\}\) spectrum, plus certified equivalence classes.

**P7 - Vectorial-bent sub-case.** Classify or count vectorial bent functions \(\mathbb{F}_2^{10}\to\mathbb{F}_2^m\) (every nonzero component bent, \(m\le5\)) within a fixed family, or settle a specific existence question for the maximal \(m\). *Certificate:* recomputed component-wise bent tests plus certified equivalence classes.

## 4. Known results and prior art

- **Counts by dimension:** bent functions number \(8\) (\(n=2\)), \(896\) (\(n=4\)), \(5{,}425{,}430{,}528\) (\(n=6\)), and for \(n=8\) exactly
\[
99{,}270{,}589{,}265{,}934{,}370{,}305{,}785{,}861{,}242{,}880\approx 2^{106.29},
\]
the last computed by **Langevin and Leander** (with Carlet and others; ~2008–2011) via a Möbius/Reed–Muller and orbit-counting attack (verify exact digits and attribution). The \(n=8\) computation counted functions, not affine classes; the affine-class count for \(n=8\) is a distinct, harder figure (verify its status).
- **Classification status:** complete affine classification is known for \(n\le 6\); for \(n=8\) the total is counted and many subclasses (e.g. cubic, self-dual) are classified - self-dual bent in \(n=8\) and cubic-bent enumerations were carried out by Langevin, Leander, Hou, and coauthors (~2010s) (verify) - but a full class list is not tractably enumerable. For \(n\ge 10\) neither the count nor the classification is known; only partial families are (verify).
- **Constructions/superclasses:** Maiorana–McFarland (\(\mathcal{M}\)), partial spreads (\(\mathcal{PS}^+/\mathcal{PS}^-\), Dillon), Rothaus's iterative construction, Dobbertin's construction, and monomial/Niho bent functions; not every bent function lies in the primary classes (the "\(\mathcal{M}\)-vs-\(\mathcal{PS}\)" gap) - Carlet, Mesnager, and others survey these (~2016 Mesnager monograph) (verify).
- **Homogeneous bent:** existence of homogeneous bent functions of degree \(n/2\) is subtle; degree-3 homogeneous bent in low dimensions studied by Qu, Seberry, Pieprzyk and others (~2000s) (verify).
- **Normality:** whether every bent function is normal (constant on some \(n/2\)-flat) fails from \(n=10\) upward; non-normal bent functions in \(n=10,12,14\) were constructed (Canteaut–Daum–Dobbertin–Leander; ~2006) - a structural feature any \(n=10\) enumeration must accommodate (verify).
- **Cayley-graph / strongly-regular-graph view:** bent functions correspond to certain strongly regular graphs and to bent-based difference sets, giving nauty-canonicalizable combinatorial objects (verify).
- **Almost bent (odd \(n\)):** AB functions coincide with functions meeting the odd-dimension nonlinearity bound and are APN; the Gold, Kasami, Welch, and Niho power functions give the classical AB families (verify).
- **Self-dual bent:** the classification of self-dual bent functions in \(n\le8\) (Carlet, Danielsen, Parker, Solé; ~2010) is a tractable, certified sub-population and a good enumeration-engine target (verify).
- **Quadratic bent:** quadratic bent functions are completely understood in every dimension (a single affine-equivalence class, tied to non-degenerate symplectic forms) - the natural first exact class to reproduce at \(n=10\) (verify).
- **Rotation-symmetric bent:** enumerations of rotation-symmetric bent functions in low dimensions (Stănică–Maitra and others; ~2000s) give a finite-in-practice \(n=10\) target class (verify).
- **Vectorial bent:** vectorial bent functions \(\mathbb{F}_2^n\to\mathbb{F}_2^m\) require \(m\le n/2\); their constructions and partial classifications are surveyed in the Mesnager monograph (verify).
- **Counting toolkit:** Langevin's public bent-function project pages tabulate cubic-bent counts, self-dual counts, and orbit data for \(n\le8\) - the natural ground-truth for validating an enumeration engine (verify current contents).
- **Community resources:** the "Boolean functions" wiki collates bent-function families, counts, and equivalence data; use for cross-checks, not as the trusted base (verify).

**Web-verify the headline record tables** - the \(n=8\) bent count, subclass classifications, and any partial \(n=10\) results are actively refined; consult the Boolean-functions community pages, Langevin's bent-function project pages, and recent surveys/journals. **Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

`[enum]` `[search]` first computations on one workstation:

1. **Verified bent test (P1).** Fast Walsh–Hadamard transform in **SageMath** and an independent **C++** implementation; a function is bent iff every \(|W_f(w)|=2^{n/2}\) - an exact integer check. Cross-implement to gate integrity.
2. **Canonical enumeration engine (P1–P3).** Build canonical, isomorph-free generation under \(\mathrm{AGL}(n,\mathbb{F}_2)\) + affine-function addition, using **nauty/Traces** (or **bliss**) for canonical labeling of the associated structure and **orderly generation** to avoid producing isomorphs; validate on \(n\le 6\) against known class counts. Use **GAP** for the affine group, orbit-stabilizer bookkeeping, and orbit counting (Burnside/Cauchy–Frobenius) to certify class totals two ways.
3. **Symmetry / degree restriction (P3–P5).** Restrict to a finite-in-practice class: rotation-symmetric bent (index by cyclic orbits), homogeneous cubic bent (ANF supported on degree-3 monomials only), or bent within \(\mathcal{M}\)/\(\mathcal{PS}\) parameters (index by the defining permutation/spread). Enumerate class representatives, bent-test each, canonicalize survivors.
4. **SAT sub-cases (P4).** Encode "\(\exists\) bent \(f\) in class \(C\) with property \(X\)" as CNF over the ANF/truth-table bits with the balanced-derivative or flat-spectrum constraints; run **CaDiCaL**/**kissat** with proof logging and replay UNSAT with `drat-trim`/`lrat-check`. The balanced-derivative form (\(D_af\) balanced for all \(a\neq0\)) is often a leaner encoding than the flat-spectrum form.
5. **Dual bookkeeping.** For every bent representative compute its dual \(\tilde f\), record whether it is self-dual, and pair non-self-dual classes; the dual is a cheap consistency check (a bent function's dual is bent) and a symmetry to quotient by.
6. **Degree-layer sweep (P2, P5).** Since bent functions have \(\deg\le n/2\), enumerate by increasing degree - quadratic (one class), then cubic - using the ANF-coefficient variables as the search space; the cubic layer at \(n=8\) is a strong engine test against published cubic-bent counts before attempting \(n=10\).
7. **Almost-bent companion (P6).** Reuse the CCZ/affine-equivalence engine from problem 08; enumerate AB candidates in a fixed odd dimension/class, verify the \(\{0,\pm2^{(n+1)/2}\}\) spectrum, and canonicalize.

Candidate \(n=10\) classes to attack first, smallest-space first:

- **Quadratic bent** - a single class; the base-case sanity check.
- **Self-dual bent within a fixed degree** - constrained by the duality involution.
- **Rotation-symmetric bent** - indexed by cyclic orbits, a few hundred RSBF variables.
- **Homogeneous cubic bent** - ANF on degree-3 monomials only; a delicate existence question.
- **Maiorana–McFarland with structured \(\pi\)** - index by the defining permutation family.

**One-workstation scope and failure modes.**

- *Explosion:* the unrestricted \(n=10\) space is far past exhaustion - only a degree/symmetry restriction is finite-in-practice, and any total-count claim must justify completeness of the restriction.
- *Canonicity bugs:* a wrong canonical form under \(\mathrm{AGL}\) merges or splits classes and silently corrupts a count - validate on \(n\le 6\) and cross-check counts by Burnside.
- *Isomorph leakage:* orderly generation must be proved exhaustive; a missed generation rule voids completeness.
- *Memory:* even a restricted \(n=10\) class list can be large - stream, hash, and count rather than materialize.
- *Equivalence subtlety:* affine equivalence vs. the coarser CCZ / "extended-affine" notions must be fixed and stated - mixing them corrupts comparisons with the literature.
- *Duality double-counting:* the dual involution pairs classes; forgetting it either double-counts or wrongly identifies self-dual with non-self-dual classes.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every bent claim is an exact flat-Walsh-spectrum check; every count rests on isomorph-free canonical generation or a Burnside/orbit computation over exact group data; every nonexistence on a DRAT/LRAT proof or a certified exhaustive enumeration. No floating point in a load-bearing step.
2. **Independent verification.** Two independent Walsh transforms agree on every spectrum; every canonical label is recomputed by a separate nauty invocation or a second canonicalizer; every class total is confirmed two ways (canonical-list length and Burnside count); every DRAT/LRAT proof is replayed by a separate checker. The dual of every listed representative is recomputed and checked bent, as a cheap independent consistency test on the whole list.
3. **Reproducibility.** Record the variable ordering, ANF convention, equivalence group used, class definition, all encodings, and tool versions (SageMath, nauty, GAP, solvers), with a SHA-256 manifest over every truth table, ANF, canonical label, CNF, and proof. Cite the baseline count/classification being reproduced or extended (value, authors, source, access date). State explicitly whether every reported number counts functions or affine-equivalence classes.
4. **Preservation.** All enumeration, canonicalization, and search source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).
5. **Honest reporting.** The report states up front the exact class \(C\) for which completeness is certified, whether a *count*, a *classification*, or only a *construction* was produced, and under which equivalence. A restricted-class count is never presented as the total number of \(n=10\) bent functions, and an uncertified family is never presented as a classification.

Calibration for the session lead: the realistic product is P1–P3 - a validated bent-test and canonical-enumeration engine, a reproduced \(n=8\) sub-count, and one certified \(n=10\) class count or classification - plus, with luck, a broader class (P5) or an almost-bent companion result (P6). A full \(n=10\) count is not on the table on one workstation; the value is in exact, certified statements about well-delimited sub-populations, which is exactly what the field lacks for \(n\ge 10\).
