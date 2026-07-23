# PROMPT FOR OPTIMAL LOW-DIFFERENTIAL-UNIFORMITY PERMUTATIONS

## Differentially-\(k\)-uniform S-boxes of \(\mathbb{F}_2^n\) with high nonlinearity, minimal \(k\)

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 11 of 50
**Area:** Boolean & cryptographic functions
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Differential uniformity is the exact number that bounds a block cipher's exposure to differential cryptanalysis, and the S-box is where it is fought. APN (differential uniformity \(2\)) permutations are the ideal, but in even dimension they may not exist at all (the big APN problem, our problem 08) - so real ciphers use **differentially-4-uniform** permutations with the highest achievable nonlinearity, and the frontier questions are: for a given even \(n\), what is the *minimum* differential uniformity of a permutation, and what is the *maximum* nonlinearity attainable at differential uniformity \(4\)? Several of these are open with a live record table. The task fits certified search exactly: differential uniformity and nonlinearity are exact counts over \(2^n\) field elements, equivalence is governed by CCZ/EA transformations and nauty canonical forms, and the productive constructions (butterflies, inverse-function modifications, binomials) are structured enough to search and to bound. The on-machine verifier is a recomputed DDT plus a Walsh spectrum plus a bijectivity check; anything short of the Section 2 standard - a construction with no matching optimality certificate, a heuristic S-box without a recomputed DDT - is a partial result, never a resolution.

## 1. Exact problem statement

For \(F:\mathbb{F}_2^n\to\mathbb{F}_2^n\) (identify \(\mathbb{F}_2^n\cong\mathbb{F}_{2^n}\) as needed) and \(a,b\in\mathbb{F}_2^n\), the difference distribution table entry and differential uniformity are
\[
\delta_F(a,b)=\bigl|\{x:F(x+a)+F(x)=b\}\bigr|,\qquad
\delta(F)=\max_{a\neq0,\ b}\delta_F(a,b).
\]
\(\delta(F)\ge 2\) always; \(F\) is **APN** iff \(\delta(F)=2\) and **differentially \(k\)-uniform** iff \(\delta(F)=k\) (so \(k\) is even). The **nonlinearity** of a vectorial \(F\) is
\[
\mathrm{nl}(F)=2^{n-1}-\tfrac12\max_{v\neq0,\ w}\Bigl|\sum_{x}(-1)^{\langle v,F(x)\rangle+\langle w,x\rangle}\Bigr|,
\]
the minimum nonlinearity over nonzero linear combinations \(\langle v,F\rangle\) of coordinates. Here \(\mathrm{wt}(u)\) is the Hamming weight and \(\langle v,x\rangle=\sum_i v_ix_i\bmod2\). Every nonzero-\(a\) DDT row satisfies \(\sum_b\delta_F(a,b)=2^n\) with all entries even; the **differential spectrum** is the multiset \(\{\delta_F(a,b):a\neq0\}\), a CCZ-invariant finer than \(\delta(F)\) alone. **CCZ-equivalence** and **EA-equivalence** are as in problem 08 (affine action on the graph \(\mathcal{G}_F\subseteq\mathbb{F}_2^{2n}\)); both preserve \(\delta(F)\) and the extended Walsh spectrum, and CCZ preserves nonlinearity. \(F\) is a **permutation** iff its image multiset is all of \(\mathbb{F}_2^n\).

The relevant upper bound on vectorial nonlinearity is the **Sidelnikov–Chabaud–Vaudenay (SCV)** bound
\[
\mathrm{nl}(F)\le 2^{n-1}-\tfrac12\sqrt{3\cdot2^{n}-2-2\cdot\tfrac{(2^n-1)(2^{n-1}-1)}{2^n-1}}\ \le\ 2^{n-1}-2^{(n-1)/2},
\]
with the simpler right-hand form for permutations; for even \(n\) it cannot be met (that is the AB/odd-\(n\) case), so the operative even-\(n\) question is how close to \(2^{n-1}-2^{n/2}\) a differentially-4-uniform permutation can get. A refined invariant is the **boomerang uniformity** \(\beta(F)\) (Cid–Huang–Peyrin–Sasaki–Song), the maximum of the boomerang connectivity table, which further separates 4-uniform permutations of equal \(\delta\) and \(\mathrm{nl}\).

**Reference values.** For the inverse function \(F(x)=x^{2^n-2}\) on \(\mathbb{F}_{2^n}\) (the AES S-box for \(n=8\)): \(\delta(F)=4\) for even \(n\), \(\delta(F)=2\) (APN) for odd \(n\); its nonlinearity is \(2^{n-1}-2^{n/2}\) for even \(n\). The maximum possible nonlinearity of any permutation of \(\mathbb{F}_2^n\) (even \(n\)) is at most the "Sidelnikov–Chabaud–Vaudenay"-type bound; whether \(2^{n-1}-2^{n/2}\) is optimal for differentially-4-uniform permutations in a given even \(n\) is part of the open landscape.

For orientation, the operative even-\(n\) targets at \(\delta=4\) are the nonlinearities
\[
n=6:\ \mathrm{nl}\le 24,\qquad n=8:\ \mathrm{nl}\le 112,\qquad n=10:\ \mathrm{nl}\le 480,
\]
where \(2^{n-1}-2^{n/2}\) is the inverse-function value and the best-known 4-uniform permutations meet or approach it; whether it can be exceeded (or is optimal) at \(\delta=4\) is the crux.

**The questions, adopted scope.** For specified even \(n\) (primary \(n=8\); secondary \(n=6,10\)):
(i) the **minimum differential uniformity** \(\delta_{\min}(n)=\min\{\delta(F):F\text{ a permutation of }\mathbb{F}_2^n\}\) - is it \(2\) or \(4\)? (this is the big APN problem when the answer would be \(2\); cross-reference problem 08);
(ii) among differentially-\(4\)-uniform permutations, the **maximum nonlinearity**, and constructions/classifications attaining it;
(iii) certified existence/nonexistence of permutations with prescribed \((\delta,\mathrm{nl})\) in structured families. Cost: verified DDTs, Walsh spectra, bijectivity checks; DRAT/LRAT for nonexistence.

## 2. Resolution standard

A **full resolution** of a scoped instance is one of:

- **(Optimal value)** a proof that \(\delta_{\min}(n)=k\) or that the maximum nonlinearity of differentially-\(4\)-uniform permutations of \(\mathbb{F}_2^n\) equals \(N\): a construction attaining \((k\text{ or }N)\) with recomputed DDT, Walsh spectrum and bijectivity check, **plus** a matching machine-checkable bound (a DRAT/LRAT UNSAT proof, or an isomorph-free exhaustion within a certified-complete class, that nothing does better);
- **(Existence/classification)** a certified isomorph-free classification of the differentially-\(4\)-uniform permutations of \(\mathbb{F}_2^n\) attaining a stated nonlinearity within a delimited family, with a completeness certificate.

Named certified forms:

- **(a) Explicit construction** with a recomputed DDT, Walsh spectrum, and bijectivity check.
- **(b) CCZ/EA-equivalence-complete search** within a family, with certified equivalence tests and canonical forms (nauty on the attached structure).
- **(c) SAT-with-DRAT** for existence/nonexistence of a permutation with prescribed \((\delta,\mathrm{nl})\) constraints.
- **(d) Canonical enumeration via nauty** guaranteeing a case split is complete.

**Not accepted as resolution.**

- A differentially-4-uniform permutation with high nonlinearity but **no** matching optimality/bound certificate - a good S-box, a genuine partial result (P-level), not a determined optimum.
- Any claim about \(\delta_{\min}(n)=2\) (an APN permutation) - that is problem 08 and must meet *its* Section 2 standard; here \(\delta=4\) results are the object.
- A construction whose DDT, Walsh spectrum, or bijectivity is not independently recomputed.
- A CCZ/EA-equivalence assertion without an explicit affine transformation matrix a checker can multiply out.
- A within-family maximum presented as the global optimum without a certified losslessness/completeness argument.
- A construction inheriting a family's \(\delta\le4\) guarantee but never actually recomputing \(\delta\) on the concrete instance.
- An unreplayable UNSAT, or an "up to equivalence" enumeration whose canonicity/completeness is uncertified.
- A nonlinearity value reported without stating the field representation (the value is representation-independent, but bugs often are not).
- A boomerang-uniformity or differential-spectrum claim not recomputed from the DDT/BCT directly.
- A comparison against a "best known" record without citing the specific paper and value being compared to.
- A "no 4-uniform permutation beats \(N\)" claim whose family scope is broader than the enumeration/SAT actually covered.
- An S-box whose algebraic degree (a fourth design axis) is not reported alongside \((\delta,\mathrm{nl},\beta)\).
- A permutation presented as "new" without a certified CCZ/EA-inequivalence to the reference families.
- A heuristic-search optimum quoted without the full S-box table archived and its DDT re-derived.

## 3. Graded partial-result targets

**P0 - AES base case.** Recompute the DDT, Walsh spectrum, boomerang table, and bijectivity of the AES inverse S-box on \(\mathbb{F}_{2^8}\), confirming \(\delta=4\), \(\mathrm{nl}=112\); this is the ground-truth anchor for the whole toolchain and every implementation must reproduce it exactly. *Certificate:* recomputed tables with SHA-256 matching the standard AES S-box.

**P1 - Reproduce the frontier.** Recompute the DDT, Walsh spectrum, and bijectivity of reference S-boxes: the inverse function on \(\mathbb{F}_{2^8}\) (AES; expect \(\delta=4\), \(\mathrm{nl}=112\)), Gold/Bracken–Leander differentially-4-uniform permutations, and a butterfly-construction permutation. *Certificate:* recomputed DDTs/spectra with SHA-256, matching published values.

**P2 - Equivalence & invariant infrastructure.** Stand up the CCZ/EA-equivalence engine (shared with problem 08): certified equivalence tests, the ortho-derivative/Walsh invariant for the \(\delta=4\) setting, and nauty canonicalization of the attached structure; validate against known equivalences among 4-uniform families. *Certificate:* transformation matrices / invariant tables replayed by a separate checker.

**P3 - Best-known nonlinearity, reproduced and searched.** For \(n=8\), reproduce the best-known nonlinearity among differentially-4-uniform permutations and run a certified search (structured family or symmetry-restricted) for any improvement or a certified "no improvement in this family". *Certificate:* recomputed spectra of the optimum, plus a family-restricted DRAT UNSAT or canonical exhaustion.

**P4 - Small-\(n\) exact optimum.** For \(n=6\), determine the maximum nonlinearity of differentially-4-uniform permutations exactly (small enough for a certified exhaustion within CCZ-classes), and settle \(\delta_{\min}(6)\) landscape questions that do not reduce to the known \(n=6\) APN permutation. A certified statement of the form "the maximum nonlinearity of a 4-uniform permutation of \(\mathbb{F}_2^6\) is exactly \(m\)" would be a clean, publishable exact value. *Certificate:* isomorph-free class exhaustion with completeness certificate.

**P5 - Structured-family classification (\(n=8/10\)).** Classify, up to CCZ/EA equivalence with a completeness certificate, the differentially-4-uniform permutations attaining the top nonlinearity within a delimited family (butterflies, inverse-function modifications, binomials \(x^{2^i+1}+ \cdots\)). Report the number of inequivalent optima and their four-axis profiles. *Certificate:* per-family exhaustiveness + nauty-checked distinctness.

**P6 - Certified optimality or bound.** Produce a machine-checkable bound: a DRAT/LRAT proof that no permutation of \(\mathbb{F}_2^8\) in a stated (broad) family beats nonlinearity \(N\) at \(\delta=4\), or an exact spectral/LP bound. *Certificate:* CNF + replayed proof, or exact rational certificate.

**P7 - Low-boomerang optimum.** Within the 4-uniform, high-nonlinearity population at \(n=8\), find or certify the minimum boomerang uniformity \(\beta(F)\), the modern tertiary S-box criterion. *Certificate:* recomputed boomerang connectivity tables plus a family-restricted optimality argument.

## 4. Known results and prior art

- **Differential uniformity basics:** \(\delta(F)\ge2\) for all \(F\); APN (\(\delta=2\)) is optimal but may be unattainable by permutations in even \(n\), so \(\delta=4\) is the practical target (Nyberg's foundational work on differentially uniform mappings, ~1993) (verify).
- **Inverse function:** \(x^{-1}=x^{2^n-2}\) is differentially 4-uniform for even \(n\) with nonlinearity \(2^{n-1}-2^{n/2}\); it is the AES S-box at \(n=8\) (\(\delta=4\), \(\mathrm{nl}=112\)) (Nyberg, ~1993–1994) (verify).
- **Butterflies:** Perrin, Udovenko and Biryukov (Crypto 2016) introduced the butterfly structure, giving differentially-4-uniform permutations of \(\mathbb{F}_2^{2k}\) with very high nonlinearity and high degree for odd \(k\); follow-up work (Canteaut–Duval–Perrin; Li–Tian–Yu–Wang; ~2016–2018) resolved a nonlinearity open problem and expanded the list (verify).
- **Modifications of the inverse and binomial/multinomial families:** differentially-4-uniform permutations from modifying the inverse function on subfields/cosets, and binomial constructions with high nonlinearity (Bracken–Leander; Qu–Tan–Tan–Li; Zha–Hu–Sun; ~2011–2015) (verify).
- **Even-dimension difficulty:** constructing differentially-4-uniform permutations *with high nonlinearity* is markedly harder in even dimension; the minimum differential uniformity of permutations in even \(n\) (is it 2 or 4?) is exactly the big APN problem for the \(\delta=2\) side (cross-reference problem 08).
- **Bounds:** the Sidelnikov–Chabaud–Vaudenay bound governs vectorial nonlinearity; whether \(2^{n-1}-2^{n/2}\) is the best achievable at \(\delta=4\) for given even \(n\) is not settled in general (verify).
- **Boomerang uniformity:** introduced by Cid, Huang, Peyrin, Sasaki and Song (~2018) as a fourth S-box criterion; the boomerang spectra of the inverse and of the known 4-uniform families are actively catalogued (Boura–Canteaut; Li–Qu–Sun–Li; ~2019) (verify).
- **Small-\(n\) classification:** optimal 4-bit S-boxes (\(n=4\)) are fully classified (Leander–Poschmann, ~2007); for \(n=6\) the 4-uniform landscape is small enough for certified exhaustion within CCZ-classes (verify).
- **Locally-APN and raising-degree constructions:** further 4-uniform families come from concatenation, interpolation, and degree-raising of APN functions (Zha–Hu–Sun–Shan; Tang–Carlet–Tang; ~2015–2020) (verify).
- **Surveys/resources:** Carlet's monograph (~2021) and the "Boolean functions" wiki collate the differential-uniformity and boomerang tables (verify).
- **Surveys:** Carlet's monograph on Boolean functions for cryptography (~2021) collates the differential-uniformity landscape (verify).

- **Cross-reference:** the \(\delta=2\) boundary of this problem *is* problem 08 (APN permutation); results there settle \(\delta_{\min}(n)\) from below, and this problem inherits its equivalence engine and inventory.

**Web-verify the headline record tables** - the best-known nonlinearity at \(\delta=4\) for \(n=8\) and the butterfly/inverse-modification records move; consult the Boolean-functions community pages and recent ePrint/ToSC papers. **Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

`[search]` first computations on one workstation:

1. **Ground truth (P0–P1).** In **SageMath**, evaluate DDTs, Walsh spectra, boomerang tables, and bijectivity for the reference S-boxes; cross-implement the DDT and Walsh spectrum in **custom C++ for Boolean-function search** - both cheap for \(n\le 10\). Agreement gates integrity.
   The AES S-box is the immovable anchor: if either implementation fails to reproduce \(\delta=4,\ \mathrm{nl}=112\) on it, stop and fix the field representation before proceeding.
2. **Equivalence engine (P2).** Reuse the CCZ/EA machinery from problem 08: certified equivalence tests, ortho-derivative invariant, and **nauty/Traces** canonicalization of the attached structure; **GAP** for the affine/matrix group orbits.
3. **Family search (P3, P5).** Parameterize the productive families (butterfly coefficients; inverse-function modifications on cosets; binomials \(x^{2^i+1}+cx^{2^j+1}\)) and sweep, exactly computing \((\delta,\mathrm{nl},\deg,\beta)\) for each and canonicalizing survivors. Restrict by symmetry (subgroup-invariant permutations) to make sweeps finite-in-practice. Record the full four-axis profile per survivor, not just \(\delta\) and \(\mathrm{nl}\).
4. **Small-\(n\) exhaustion (P4).** For \(n=6\), exhaust CCZ/affine classes of permutations with a certified canonical generation and read off the maximum nonlinearity at each \(\delta\); the class count here is small enough that a complete, isomorph-free sweep is feasible on one workstation.
5. **SAT bounds (P6).** Encode "permutation of \(\mathbb{F}_2^n\) with \(\delta\le 4\) and \(\mathrm{nl}\ge N+2\) (+ structural constraints)" as CNF; run **CaDiCaL**/**kissat**/**CryptoMiniSat** with proof logging; replay UNSAT with `drat-trim`/`lrat-check`. Use exact ILP/LP (SCIP, QSopt_ex) for spectral bounds.
6. **Boomerang tabulation (P5).** For each surviving 4-uniform permutation compute the boomerang uniformity \(\beta(F)\) as a secondary optimization target, since low \(\beta\) is now a design criterion alongside low \(\delta\) and high \(\mathrm{nl}\).

Productive even-\(n\) families to sweep, in rough order of yield:

- **Inverse function** \(x^{-1}\) - the reference (AES) point, \(\delta=4\), \(\mathrm{nl}=2^{n-1}-2^{n/2}\).
- **Butterflies** (Perrin–Udovenko–Biryukov) - high nonlinearity, best-known at several \(n\).
- **Inverse-function modifications** on subfields/cosets - many 4-uniform permutations with strong \(\mathrm{nl}\).
- **Gold/Bracken–Leander and binomial** \(x^{2^i+1}+cx^{2^j+1}\) forms - algebraically parameterized sweeps.

**One-workstation scope and failure modes.**

- *DDT/Walsh cheap, search space vast:* the space of permutations of \(\mathbb{F}_2^8\) is \((2^8)!\) - only family/symmetry restriction or SAT makes it finite-in-practice, and any *global*-optimum claim must justify completeness.
- *Canonicity/equivalence bugs* silently merge or split classes - dual-implement invariants, validate on \(n=6\).
- *Unverified solver output:* UNSAT is unproven until a separate DRAT/LRAT checker replays it.
- *Bound rigor:* a floating-point spectral bound is exploratory until made exact-rational.
- *Scope creep into problem 08:* any \(\delta=2\) permutation belongs there and must meet that standard; here the object is \(\delta=4\) optimality.
- *Profile tunnel vision:* optimizing \(\mathrm{nl}\) alone can wreck degree or boomerang uniformity - track all four axes so a "record" is not a regression on an unreported axis.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every \(\delta\) is from a recomputed DDT, every nonlinearity from a recomputed Walsh spectrum, every permutation from an exact bijectivity check; every equivalence from an explicit affine matrix; every bound from a DRAT/LRAT proof or exact rational certificate. No floating point in a load-bearing step.
2. **Independent verification.** Two independently written DDT/Walsh implementations agree on every load-bearing value; every CCZ/EA transformation is replayed by a checker; every DRAT/LRAT proof is replayed; every "up-to-equivalence" class list is recanonicalized by a separate nauty run; every boomerang connectivity table is recomputed independently of the DDT code.
3. **Reproducibility.** Record the field representation, family parameterization, symmetry restriction, all encodings, and tool versions (SageMath, nauty, GAP, solvers), with a SHA-256 manifest over every S-box table, DDT, spectrum, CNF, and proof. Cite the best-known baseline \((\delta,\mathrm{nl})\) being matched or beaten (value, authors, source, access date).
4. **Preservation.** All search, family-sweep, and enumeration source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson). The full S-box table of every record-level permutation is archived, not just its profile numbers.
5. **Honest reporting.** The report states up front whether an *optimal value* was determined (with a matching bound), a *best-known record* improved, or only a *good S-box* constructed, and in which family the claim's completeness holds. A within-family maximum is never presented as the global optimum, and no \(\delta=4\) result is dressed as bearing on the \(\delta=2\) big APN problem beyond an explicit cross-reference.

Calibration for the session lead: the realistic product is P1–P3 - a validated DDT/Walsh/equivalence toolchain, reproduced reference records, and a certified within-family maximum or classification at \(n=8\) - plus, with luck, a small-\(n\) exact optimum (P4) or a family-restricted upper bound (P6). A *global* even-\(n\) minimum-uniformity or maximum-nonlinearity theorem is a major result and out of scope for a single workstation session; the value lies in exact, certified statements about well-delimited S-box families that block ciphers actually use.
