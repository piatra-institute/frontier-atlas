# PROMPT FOR THE BILINEAR RANK OF A SPECIFIC SMALL BILINEAR MAP

## Certified exact rank of rectangular products, polynomial and algebra multiplication

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 05 of 50
**Area:** algorithms & bilinear complexity
**Modes:** `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The bilinear complexity (rank) of a bilinear map \(\phi:U\times V\to W\) is the minimum number of essential multiplications in any bilinear algorithm computing \(\phi\) - equivalently the tensor rank of its structure tensor. It is the exact-complexity measure for the elementary algebraic operations underneath fast arithmetic: rectangular matrix products \(\langle 2,2,3\rangle,\langle 2,3,3\rangle\), polynomial multiplication modulo \(x^n\), and multiplication in \(\mathbb{C}\), \(\mathbb{H}\), and other small algebras. Many exact ranks remain open. The task is inherently certifiable: an upper bound is an explicit bilinear algorithm whose correctness is an exact polynomial identity, and a lower bound is an algebraic obstruction (the substitution method, Gröbner-basis infeasibility, or flattening/border-rank bounds) with a machine-checkable core. This is matched to current symbolic-computation methods - exact CAS verification, flip-graph and SAT search, and Gröbner reasoning. The on-machine verifier is exact identity checking of a claimed algorithm plus a replayable lower-bound certificate, over an explicitly fixed field. Any single algorithm without a matching lower bound, or a numerical-only decomposition, is a partial result. This prompt targets a **specific chosen small map** each session, pinned exactly.

## 1. Exact problem statement

Fix a field \(\mathbb{F}\) (state it; default \(\mathbb{Q}\)). A **bilinear map** \(\phi:\mathbb{F}^a\times\mathbb{F}^b\to\mathbb{F}^c\) is given by its structure tensor \(T_\phi\in\mathbb{F}^a\otimes\mathbb{F}^b\otimes\mathbb{F}^c\),

\[
\phi(x,y)_k=\sum_{i,j}(T_\phi)_{ijk}\,x_i y_j .
\]

A **bilinear algorithm of length \(r\)** computes \(r\) products \(p_\ell=L_\ell(x)\,M_\ell(y)\) with \(L_\ell,M_\ell\) linear forms and recovers each output as a linear combination of the \(p_\ell\); this exists iff

\[
T_\phi=\sum_{\ell=1}^{r} u_\ell\otimes v_\ell\otimes w_\ell .
\]

The **bilinear complexity / rank** is \(R(\phi)=\min\{r:\text{such a decomposition exists over }\mathbb{F}\}\); **border rank** \(\underline{R}(\phi)\) permits \(\mathbb{F}(\varepsilon)\)-coefficients with the identity holding modulo \(O(\varepsilon)\).

**Conventions.**

- Rank is field-dependent and invariant under the \(\mathrm{GL}\times\mathrm{GL}\times\mathrm{GL}\) action; state the field and the exact tensor convention for every claim.
- "Essential multiplications" excludes scalar multiplications by field constants; only the bilinear products \(p_\ell\) are counted.
- Each session fixes one target map and one field; mixing maps or fields within a single rank claim is disallowed.

**Target maps (choose one per session, state the field).**

- **Rectangular matrix products:** \(\langle 2,2,3\rangle\) (\(R=11\), Hopcroft–Kerr - reproduce and certify), \(\langle 2,3,3\rangle\) (bracket \([14,15]\), open), \(\langle 3,3,3\rangle\) (bracket \([19,23]\); see also problem 03).
- **Polynomial multiplication:** product of two degree-\(<n\) polynomials, or multiplication modulo \(x^n\) (the \(n\)-point convolution tensor); exact ranks known for small \(n\), open for larger.
- **Algebra multiplication:** \(\mathbb{C}\) over \(\mathbb{R}\) (\(R=3\), Winograd - optimal), quaternions \(\mathbb{H}\) over \(\mathbb{R}\) (open bracket), and other small associative algebras.

**Known values (to reproduce and re-verify).**

- \(R(\langle 2,2,2\rangle)=7\); \(R(\langle 2,2,3\rangle)=11\); \(R(\mathbb{C}/\mathbb{R})=3\) (optimal).
- \(R(\langle 2,3,3\rangle)\in[14,15]\) (open); polynomial multiplication of degree-\(<n\) over an infinite field has rank \(2n-1\) (optimal, Winograd), with finite-field corrections when too few evaluation points exist.

Re-verify all cited values against Section 4.

## 2. Resolution standard

For the chosen map \(\phi\) over the stated field, a **resolution** is the exact integer \(R(\phi)\) (or \(\underline{R}(\phi)\)) with **both**:

1. **Upper bound (algorithm).** An explicit rank-\(r\) decomposition (rational or fixed-field entries) with an **exact polynomial-identity verification** that it reproduces \(T_\phi\), performed by a checker written separately from the search.
   - *Preferred form:* the decomposition plus a Macaulay2/SageMath script confirming the entrywise identity.
2. **Lower bound (optimality).** A certificate that

\[
\nexists\ \{(u_\ell,v_\ell,w_\ell)\}_{\ell=1}^{R-1}\ \text{over } \mathbb{F}\ \text{with}\ T_\phi=\sum_{\ell} u_\ell\otimes v_\ell\otimes w_\ell .
\]

   Accepted named forms:
   - (a) a **substitution-method** argument (Alexeev–Bläser–Smirnov style) reduced to a finite checkable case analysis;
   - (b) a **Gröbner-basis infeasibility certificate** (recorded ideal + monomial order showing the rank-\((R-1)\) variety is empty);
   - (c) over a finite field, a **DRAT/LRAT UNSAT proof** for the SAT encoding of decomposition existence.

**Not accepted as resolution.**

- An algorithm (upper bound) with no matching lower bound.
- A decomposition checked only numerically (must be exact).
- A lower bound over one field claimed for another, or a border-rank bound reported as a rank bound.
- A flattening/dimension lower bound presented as tight when it does not match the upper bound.
- A rank claim for a map different from (or a special case of) the one stated.
- A rank inherited from an unproven symmetry ansatz without a proof that it preserves the optimum.
- A commutative-algorithm count (which may use fewer products by exploiting \(x_iy_j=y_jx_i\)) reported as the standard non-commutative bilinear rank; the two measures differ and must be labelled.

## 3. Graded partial-result targets

- **P1 - Reproduce known ranks.** Exactly certify a slate of settled small ranks (\(\langle 2,2,2\rangle=7\), \(\langle 2,2,3\rangle=11\), \(\mathbb{C}/\mathbb{R}=3\), small polynomial products), each with an explicit algorithm and the matching lower-bound argument.
  - *Certificate:* exact identity checks and replayable lower-bound logs; SHA-256 manifest.
- **P2 - New certified algorithm.** A rank-\(r\) bilinear algorithm for the chosen open map matching or improving the best known upper bound, exactly verified (e.g. a rank-\(15\) scheme for \(\langle 2,3,3\rangle\), or a new finite-field record).
  - *Certificate:* the decomposition and its exact check.
- **P3 - Improved lower bound (finite field).** A DRAT/LRAT UNSAT proof raising the certified \(\mathbb{F}_2/\mathbb{F}_p\) lower bound for the chosen map.
  - *Certificate:* the certified UNSAT proof and the CNF encoding.
- **P4 - Improved lower bound (\(\mathbb{Q}\)/\(\mathbb{R}\)).** A substitution-method or Gröbner certificate raising the field-\(\mathbb{Q}\) (or \(\mathbb{R}\)) lower bound (e.g. \(\langle 2,3,3\rangle\ge 15\), closing that bracket).
  - *Certificate:* the recorded computation, independently re-run.
- **P5 - Close a bracket.** Pin \(R(\phi)\) (or \(\underline{R}(\phi)\)) exactly for one open small map per Section 2 - e.g. resolve \(\langle 2,3,3\rangle\), a quaternion-multiplication rank, or a specific \(\bmod\ x^n\) product.
  - *Certificate:* matching upper and lower certificates for that map.
- **P6 - Family or classification.** Extend a resolved case to a small family (a range of polynomial degrees or rectangular formats) with certified ranks throughout.
  - *Certificate:* per-instance certificates and a manifest.
- **P7 - Formalized micro-result.** A machine-checked proof (Lean/Coq) of a specific small rank (upper and lower) or of the bilinear-decomposition identity for a named algorithm.
  - *Certificate:* the formal proof with any search artifact checked by a small external verifier.

## 4. Known results and prior art

- **Foundations.** Strassen (1969), Winograd (1970s) - the bilinear complexity framework; \(R(\mathbb{C}/\mathbb{R})=3\) (Winograd, optimal). Bürgisser, Clausen, Shokrollahi, *Algebraic Complexity Theory* (1997) - the standard reference for exact small ranks, the substitution method, and polynomial-multiplication complexity.
- **Rectangular products.** Hopcroft and Kerr (1971) - \(R(\langle 2,2,3\rangle)=11\), \(R(\langle 2,3,3\rangle)\le 15\), and general \(\langle 2,n\rangle\) results. Alekseev, Smirnov - exact/approximate ranks for \(4\times2\), \(2\times2\) and related formats; Smirnov (~2013) - new bilinear algorithms and estimates for rectangular formats.
- **Recent finite-field bounds.** \(R(\langle 2,3,3\rangle)\ge 14\) (*verify*), and a 2026 preprint on automated small-format lower bounds over finite fields.
- **Polynomial and algebra multiplication.** Optimal ranks for multiplication of low-degree polynomials over infinite fields (\(2n-1\) by interpolation, optimal - Winograd) and finite-field corrections (fewer evaluation points); quaternion and small-algebra multiplication ranks studied by de Groote, Bshouty, and others, with several brackets still open.
- **Lower-bound methods.** The substitution method (Bläser, Alexeev–Smirnov), flattening/border-rank bounds (Landsberg–Ottaviani), and SAT/Gröbner infeasibility for finite fields.
- **Search tooling.** Flip-graph search (Kauers–Moosbauer, ~2022–) for upper bounds; exact CAS verification (Macaulay2/Singular) for identities.
- **Complex/quaternion multiplication.** \(R(\mathbb{C}/\mathbb{R})=3\) is optimal (Winograd); quaternion multiplication over \(\mathbb{R}\) has a known upper bound of \(8\) with the exact rank/border-rank still debated in the literature (*verify*), making it a clean target for P5.
- **Convolution tensors.** Cyclic convolution of length \(n\) relates to multiplication in \(\mathbb{F}[x]/(x^n-1)\); its rank depends on the factorization of \(x^n-1\) over \(\mathbb{F}\) (Winograd's CRT bounds), a good source of exactly certifiable small cases.

**Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

**`[sym]` - upper bounds and certification.**

1. Fix the target map's structure tensor exactly over the chosen field.
2. Seed with the best known algorithm (Hopcroft–Kerr, Smirnov, or interpolation for polynomial products).
3. Run **flip-graph search** over \(\mathbb{Q}\) and \(\mathbb{F}_p\) for improvements or new structure.
4. Export every candidate to an independent exact identity checker (Macaulay2/SageMath) before trusting it.

**`[sym]` - lower bounds.**

1. Apply the **substitution method** symbolically: eliminate variables to reduce \(R(\phi)\ge R(\phi')+1\) chains down to a checkable base case.
2. In parallel, set up the rank-\(r\) decomposition variety as a polynomial system and test emptiness with Gröbner bases (Macaulay2/Singular).
3. Over finite fields, encode decomposition existence as CNF (parity constraints), run CaDiCaL/kissat with DRAT/LRAT, and symmetry-break with a soundness argument.

**Tools.**

- Algebra: SageMath, Macaulay2, Singular (exact identity checks, Gröbner bases).
- Linear algebra: FLINT for exact \(\mathbb{F}_q\) computations.
- Search: flip-graph code (custom C++).
- SAT: CaDiCaL, kissat, CryptoMiniSat with DRAT/LRAT and drat-trim/cake_lpr.

**Substitution-method certificate structure.** The lower-bound log records the sequence of variable substitutions (each setting a linear form to a constant), the resulting reduced tensor at each step, and the base-case rank bound; the independent re-runner recomputes each reduced tensor and confirms the rank drop of exactly one per substitution and the base case by exhaustive check.

**First concrete session steps.**

1. Choose the target map and field; load and verify a known algorithm (e.g. Hopcroft–Kerr for \(\langle 2,2,3\rangle\)) with the independent checker (P1).
2. Run a short flip-graph search over \(\mathbb{F}_2\) to confirm the toolchain rediscovers low-rank schemes.
3. Stand up the finite-field SAT lower bound at a rank just below the known upper bound and confirm the expected SAT/UNSAT behaviour.
4. Scope the \(\mathbb{Q}\) Gröbner lower bound on the smallest tractable instance before committing to the open bracket.
5. Commit the target map, field, and measure in the report header before producing any rank number, so upper- and lower-bound claims are unambiguously comparable.

**One-workstation scope and failure modes.** Reproducing known ranks and searching for new upper bounds on a chosen small map are feasible on one workstation. Dominant risks:

- Exact \(\mathbb{Q}\) lower bounds via Gröbner bases are the bottleneck - the rank-\(r\) variety for a \(15\)-triple decomposition may exceed memory; scope to the smallest open map or a finite field.
- Numerical "algorithms" failing exact checking; conflating field, rank vs border rank, or map format.
- Unsound symmetry breaking in the SAT encoding.

State the field and measure with every number, and report a narrowed bracket honestly when a value does not close.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every algorithm is verified by exact polynomial-identity checking over the stated field; every lower bound is a substitution-method case analysis, a Gröbner infeasibility certificate, or a DRAT/LRAT UNSAT proof. Floating point is exploration only.
2. **Independent verification.** The identity checker is separate from the search; SAT lower bounds are re-run on a sub-instance by a second solver; Gröbner results are re-run with a different order or CAS; the substitution case analysis is spot-checked by hand or a second script.
3. **Reproducibility.** The field, tensor convention, symmetry-breaking action, and tool versions are recorded; a SHA-256 manifest covers decompositions, CNFs, proofs, and ideals; the specific known value reproduced or improved is cited with source and access date.
4. **Preservation.** Search code, encoders, CAS scripts, and all certificates are part of the record; large UNSAT proofs not stored are hashed with regeneration commands.
5. **Honest reporting.** The report states the map, the field, whether rank or border rank, and whether a value was pinned or only bracketed; an upper-bound algorithm is never reported as the exact rank without a matching certified lower bound.
