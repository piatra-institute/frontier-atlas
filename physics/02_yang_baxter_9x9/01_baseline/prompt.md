# PROMPT FOR THE CLASSIFICATION OF INVERTIBLE CONSTANT YANG–BAXTER SOLUTIONS IN THREE STATES

## The constant Yang–Baxter equation for 9×9 matrices on $\mathbb{C}^3\otimes\mathbb{C}^3$

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 02 of 50 (Tier 1)
**Source:** top-50 list #30, category C (exactly solvable models and lattice statistics)
**Modes:** `[search]` `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The constant Yang–Baxter equation in braid form asks for $R\in\mathrm{End}(V\otimes V)$, $V=\mathbb{C}^3$, satisfying $(R\otimes I)(I\otimes R)(R\otimes I)=(I\otimes R)(R\otimes I)(I\otimes R)$. Hietarinta classified the two-state ($4\times4$) case in the early 1990s; the three-state ($9\times9$) case is open. It is a finite object - $729$ cubic polynomial equations in $81$ unknowns, modulo an explicit symmetry group - and therefore in principle a Gröbner-basis problem, but one far beyond naive elimination. Every genuinely new equivalence class is a candidate integrable vertex model and a candidate braiding gate, so partial classifications of structured subfamilies carry direct payoff. The problem is matched to current AI methods because the work is symmetry-guided stratification of a giant polynomial system, with cheap independent certification of every claimed solution family. The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

### 1.1 Spaces and notation

Let $V=\mathbb{C}^3$ with fixed ordered basis $e_1,e_2,e_3$, and give $V\otimes V$ the lexicographic basis

\[
e_1\otimes e_1,\ e_1\otimes e_2,\ e_1\otimes e_3,\ e_2\otimes e_1,\ \dots,\ e_3\otimes e_3 .
\]

Write $R\in\mathrm{End}(V\otimes V)$ as a $9\times9$ complex matrix with entries $R^{ab}_{ij}$ defined by

\[
R\,(e_i\otimes e_j)=\sum_{a,b=1}^{3}R^{ab}_{ij}\;e_a\otimes e_b .
\]

Let $P\in\mathrm{End}(V\otimes V)$ be the flip, $P(u\otimes v)=v\otimes u$, and $I$ the identity on $V$.

### 1.2 The equation

On $V^{\otimes 3}$, with $R_{12}=R\otimes I$ and $R_{23}=I\otimes R$, the braid-form constant Yang–Baxter equation is

\[
R_{12}\,R_{23}\,R_{12}\;=\;R_{23}\,R_{12}\,R_{23}.
\tag{YBE}
\]

Componentwise, for all $a,b,c,i,j,k\in\{1,2,3\}$:

\[
\sum_{p,q,r}R^{ab}_{pq}\,R^{qc}_{rk}\,R^{pr}_{ij}
\;=\;
\sum_{p,q,r}R^{bc}_{qr}\,R^{aq}_{ip}\,R^{pr}_{jk},
\]

i.e. $3^6=729$ polynomial equations, each homogeneous cubic in the $81$ entries of $R$. The alternative "quantum" form $\check R_{12}\check R_{13}\check R_{23}=\check R_{23}\check R_{13}\check R_{12}$ is related by $\check R=PR$; every statement in this prompt is in the braid convention, and any imported result must be converted explicitly, with the conversion recorded.

### 1.3 Solution variety and symmetry group

Let $\mathcal{Y}\subset\mathbb{C}^{81}$ be the affine variety cut out by (YBE), and

\[
\mathcal{Y}^{\times}=\{R\in\mathcal{Y}:\det R\neq 0\}
\]

the invertible locus (handled algebraically by saturating the ideal at $\det R$). The following operations map $\mathcal{Y}^{\times}$ to itself; let $G$ be the group they generate:

1. **Gauge:** $R\mapsto (Q\otimes Q)\,R\,(Q\otimes Q)^{-1}$, $Q\in GL(3,\mathbb{C})$ (only $Q$ mod scalars acts, so this is a $PGL(3)$ action, dimension 8).
2. **Scaling:** $R\mapsto \lambda R$, $\lambda\in\mathbb{C}^{\times}$.
3. **Transposition:** $R\mapsto R^{T}$ (both sides of (YBE) are palindromic words; transposition reverses products and preserves the equation).
4. **Flip conjugation:** $R\mapsto PRP$ (conjugate (YBE) on $V^{\otimes3}$ by the order reversal $v_1\otimes v_2\otimes v_3\mapsto v_3\otimes v_2\otimes v_1$; this exchanges $R_{12}$ with the corresponding operator for $PRP$ - prove this lemma in-session as part of P1).
5. **Inversion:** $R\mapsto R^{-1}$ on the invertible locus.

Two solutions are *equivalent* iff they lie in the same $G$-orbit.

### 1.4 The open problem

Produce a complete classification of $\mathcal{Y}^{\times}/G$: an explicit finite list of parametric families of invertible $9\times9$ solutions such that every invertible solution is $G$-equivalent to a member of at least one listed family, with overlaps explicitly described.

### 1.5 Named subfamilies (fixed for sections 2–5)

- *Permutation-type:* $R(e_i\otimes e_j)=e_{\sigma(i,j)}\otimes e_{\tau(i,j)}$ for maps $\sigma,\tau:\{1,2,3\}^2\to\{1,2,3\}$; equivalently $R$ is a $9\times9$ permutation matrix. Invertible set-theoretic solutions on a 3-element set correspond to these via the braid/flip dictionary, which must be stated explicitly when reporting.
- *Monomial:* $R=D\Pi$ with $\Pi$ permutation-type and $D$ invertible diagonal.
- *Upper-triangular:* $R^{ab}_{ij}=0$ unless $(a,b)\preceq(i,j)$ lexicographically. Triangularity is preserved by the products in (YBE); this is a closed subfamily.
- *Charge-conserving ("19-vertex-type"):* $R^{ab}_{ij}=0$ unless $a+b=i+j$. The nonzero pattern has $1+4+9+4+1=19$ free entries in blocks of sizes $1,2,3,2,1$.

**Calibration example.** The three-state Drinfeld–Jimbo solution: with $E_{ij}$ the $3\times3$ matrix units and $q\in\mathbb{C}^\times$,

\[
R_{DJ}=q\sum_{i}E_{ii}\otimes E_{ii}+\sum_{i\neq j}E_{ii}\otimes E_{jj}+(q-q^{-1})\sum_{i<j}E_{ij}\otimes E_{ji},
\]

and $\check R_{DJ}=P\,R_{DJ}$ satisfies (YBE) together with the Hecke relation $(\check R_{DJ}-q)(\check R_{DJ}+q^{-1})=0$. Verifying this symbolically in $q$ is a mandatory smoke test of every pipeline component.

No informal phrasing ("essentially all solutions", "the interesting solutions") is an acceptable target.

## 2. Complete-resolution standard

A complete resolution consists of all of the following, in machine-verifiable form.

1. **Explicit list.** Finitely many families $R_{\alpha}(t_1,\dots,t_{k_\alpha})$ with entries explicit rational (or explicitly presented algebraic) functions of the parameters over $\overline{\mathbb{Q}}$, with exact parameter domains (inequations such as $\det R_\alpha\neq0$, parameter identifications).
2. **Membership certificates.** For each family, symbolic verification that (YBE) holds identically in the parameters, in exact arithmetic, reproduced by an independent checker.
3. **Completeness proof.** A certified decomposition of the ideal of $\mathcal{Y}$ saturated at $\det R$ - primary/prime decomposition, or a fully documented case tree of Gröbner computations with per-node certificates - proving that every point of $\mathcal{Y}^{\times}$ lies in the $G$-orbit of some listed family. Every branch of every case split must be closed by an ideal-theoretic certificate (radical-membership cofactors or an explicit parametrization), never by an exhaustion claim.
4. **Non-redundancy.** For each pair of families, either a proof of $G$-inequivalence via computed $G$-invariants (unordered spectra of $R$ and $PR$, ranks of partial transposes and partial traces, trace words), or an explicit description of the overlap.
5. **Reproducibility package** per section 6.

**Not accepted as resolution:**

- Numerical solution clouds, homotopy-continuation point lists, or floating-point families without exact certificates.
- Classification restricted to unitary, real, symmetric, involutive ($R^2=I$), or Hermitian $R$, represented as the general answer.
- Classification of the "generic stratum" only, with degenerate strata (non-diagonalizable $R$, coinciding eigenvalues, vanishing invariants) left unexamined or waved off.
- Ansatz families (triangular, charge-conserving, tensor-product or Clifford constructions) without a proof that the ansatz exhausts its stated stratum.
- Results computed only modulo primes, without reconstruction and exact verification in characteristic 0.
- Any classification "up to equivalence" for an equivalence group differing from the $G$ of section 1.3 without an explicit conversion.
- Classification of the non-invertible locus presented as this problem (it is a separate problem).

## 3. Graded partial-result targets

Full resolution is genuinely uncertain at current Gröbner technology; the graded targets below are the realistic product of a session, and each is independently valuable.

- **P1 - Certified reproduction of the two-state classification.**
  - *Task:* re-derive Hietarinta's $4\times4$ classification with our own pipeline - full case tree, per-branch Gröbner certificates, exact verification of every family, cross-check against the published list, all discrepancies documented. Machine-verify the symmetry lemmas of section 1.3 (items 3–5) and the calibration example of section 1.5.
  - *Certificate:* machine-readable case ledger; independent-checker runs on every family; discrepancy log.
  - *Value:* the pipeline-validation gate for everything else; also the first fully certificate-grade version of a 30-year-old computation.
- **P2 - Symmetry and invariant infrastructure for three states.**
  - *Task:* a certified set of gauge normal forms (stratification of $R$ by the Jordan/spectral data of a distinguished gauge-covariant object, e.g. the partial trace $\mathrm{tr}_2 R$) and a certified library of $G$-invariants with proofs of invariance, sufficient to separate all known inequivalent examples.
  - *Certificate:* symbolic invariance proofs; normal-form theorem with exact case analysis.
- **P3 - Complete classification of permutation-type and monomial invertible solutions.**
  - *Task:* exhaust the permutation case (finite: $9!$ candidates with pruning), then the monomial case (small polynomial system per surviving permutation); cross-link to the set-theoretic Yang–Baxter literature for $|X|=3$ (Etingof–Schedler–Soloviev tradition).
  - *Certificate:* exhaustive enumeration by two independent implementations agreeing on canonical forms; per-solution symbolic verification.
- **P4 - Complete classification of charge-conserving (19-vertex-type) invertible solutions.**
  - *Task:* the 19-variable cubic system with block structure; expected within reach of msolve/Singular after stratification by the invertible diagonal blocks.
  - *Certificate:* full ideal decomposition with membership certificates and case ledger.
- **P5 - Complete classification of upper-triangular invertible solutions.**
  - *Task:* 45 variables; the diagonal of (YBE) closes on the diagonal entries of $R$, giving a recursive stratification (solve the diagonal system first, then ascend the triangle).
  - *Certificate:* case tree with per-node Gröbner certificates.
- **P6 - Classification on the low-degree-minimal-polynomial stratum.**
  - *Task:* all invertible solutions whose minimal polynomial has degree $\le2$ (Hecke-type; connect to the Gurevich and Ewen–Ogievetsky traditions), then degree 3 if feasible.
  - *Certificate:* ideal-theoretic completeness proof on the stratum; explicit comparison with the known $GL(3)$ quantum-group classification.
- **P7 - Certified new families.**
  - *Task:* any invertible solution family proved (via P2 invariants) inequivalent to all previously published families; document Baxterization attempts (existence or obstruction of a spectral-parameter extension) for each.
  - *Certificate:* symbolic (YBE) verification plus inequivalence proofs.

Each of P3–P6, completed to the section 2 standard *restricted to its stratum*, is a publishable classification and must be reported as exactly that - a stratum result.

## 4. Known results and prior art

- J. Hietarinta (1992–1993): complete classification of constant Yang–Baxter solutions in two dimensions ($4\times4$), by computer-algebra elimination with symmetry reduction; related work on upper-triangular solutions in higher dimensions (verify scope).
- V. Drinfeld (1992): posed the set-theoretic Yang–Baxter problem.
- P. Etingof, T. Schedler, A. Soloviev (1999): structure and enumeration of non-degenerate involutive set-theoretic solutions on small sets; J.-H. Lu, M. Yan, Y. Zhu (2000): non-involutive structure theory.
- W. Rump (2007): braces; L. Guarnieri, L. Vendramin (2017): skew braces - the algebraic backbone of set-theoretic classification. Ö. Akgün, M. Mereb, L. Vendramin (~2022): constraint-programming enumeration of set-theoretic solutions up to size ~10 (verify).
- D. Gurevich (~1991): Hecke symmetries. H. Ewen, O. Ogievetsky (~1994): classification of $GL(3)$ quantum-matrix-group $R$-matrices - the closest completed three-state relative of this problem (verify exact scope).
- H. Dye (2003): classification of unitary $4\times4$ braid-form solutions. L. Kauffman, S. Lomonaco (2004): braiding gates and universality - the quantum-computing payoff channel.
- N. Crampé, L. Frappat, E. Ragoucy, M. Vanicat and collaborators (~2013–2019): classifications of low-dimensional $R$-matrices *with spectral parameter* under ansätze (verify which cases are complete).
- P. Padmanabhan, F. Sugino, D. Trancanelli (~2020–2021): constant YBE families from Clifford and partition algebras (verify).
- R. Vieira (~2018–2019): differential approach to solving/classifying the YBE for two-state systems, with claims toward higher states (verify).
- To our knowledge, no complete $9\times9$ classification of $\mathcal{Y}^{\times}/G$ exists; the literature contains families and strata only.

**Status as of mid-2026 - re-verify against current literature before starting the session.** In particular search for: any claimed 9×9 classification (full or for the triangular/charge-conserving strata), new set-theoretic enumerations, and recent msolve-scale Gröbner records.

## 5. Attack plan

All of this runs on a single workstation (≤ 64 GB RAM) except where flagged.

1. **Pipeline validation (P1).**
   - SageMath driving Singular and msolve; encode (YBE) for $n=2$ (16 variables), impose gauge normal forms for $Q\in GL(2)$, saturate at $\det R$, decompose.
   - Independent checker: a ~100-line SymPy script (and separately Pari/GP) that substitutes each family into (YBE) and verifies the zero matrix symbolically.
   - Expected wall time: hours. Failure mode: convention mismatches against Hietarinta's published tables (quantum vs braid form) - resolve via the recorded $\check R=PR$ dictionary before reporting discrepancies.
2. **Symmetry reduction before elimination (P2).**
   - Never feed the raw 81-variable system to a Gröbner engine; it will not terminate in feasible memory (if attempted anyway, record the failure explicitly).
   - Fix gauge by Jordan-reducing a distinguished gauge-covariant object (e.g. $\mathrm{tr}_2 R$ or a corner block), stratify by its Jordan type, and use only the residual gauge group within each stratum.
3. **Finite subproblems first (P3).**
   - Permutation-type: depth-first search over $\sigma,\tau$ tables with (YBE) checked on partial assignments; dual implementations (Python and C++); results compared as canonical forms under the monomial-gauge subgroup of $G$.
4. **Structured strata (P4, P5, P6).**
   - msolve/FGb, degrevlex; modular runs at several 31-bit primes to map component structure cheaply; rational reconstruction; characteristic-0 certification via ideal-membership cofactors - discovery may be expensive, verification is cheap and is the deliverable.
   - Singular `primdec`/`minAssGTZ` for decompositions; Macaulay2 as a second opinion on component counts.
5. **Invariants and non-redundancy.**
   - Exact computation (Pari/GP or SymPy over $\overline{\mathbb{Q}}$) of spectra of $R$ and $PR$, ranks of partial transposes/traces, and trace words to length ~6; stored as certified canonical data per family.
6. **Expected failure modes.**
   - Gröbner memory blow-up on strata with large residual symmetry - mitigate by further case splits and by using the scaling action to dehomogenize.
   - Components silently lost when saturating at $\det R$ - mitigate with saturation certificates and a component census modulo several primes.
   - Case-ledger drift - the ledger is a machine-readable file, and a dedicated script re-verifies that the case tree covers its stratum.

## 6. Verification and auditability requirements

Instantiating the five template requirements for this problem:

1. **Exact arithmetic.** All classification claims over $\mathbb{Q}$, $\overline{\mathbb{Q}}$, or $\mathbb{Q}(t_1,\dots,t_k)$; modular Gröbner runs are exploration only and labeled as such; no floating point anywhere in a certificate.
2. **Independent verification.** Every claimed family re-verified by a standalone SymPy checker written independently of the discovery code, and by a second checker in a different system (Pari/GP or Macaulay2); every completeness certificate (ideal-membership cofactors) re-verified by naive polynomial arithmetic in the checker, not by the Gröbner engine that produced it.
3. **Reproducibility.** CAS versions (Singular, msolve, Sage, Macaulay2), prime choices, term orders, and seeds recorded; SHA-256 manifest over the case ledger, all ideals (as text), all certificates, and all checker outputs.
4. **Preservation.** The full case tree - including dead branches and failed eliminations - is part of the record; any stratum abandoned for resource reasons is listed as OPEN in the ledger, never silently dropped.
5. **Honest reporting.** The final report states first whether $\mathcal{Y}^{\times}/G$ was completely classified (expected answer: no), then exactly which strata (P3–P6) were completed to the section 2 standard, and which new families (P7) were certified. A stratum classification must never be phrased as "the classification of the 9×9 Yang–Baxter equation".
