# PROMPT FOR CERTIFIED MATRIX-RIGIDITY VALUES AND OBSTRUCTIONS

## Exact rigidity of small structured matrices and certified non-rigidity witnesses

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 07 of 50
**Area:** algorithms & bilinear complexity
**Modes:** `[sym]` `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Valiant's matrix rigidity \(R_M(r)\) is the minimum number of entries of a matrix \(M\) that must be changed to reduce its rank below \(r\). A single explicit family that is *Valiant-rigid* - rank stays \(\ge \varepsilon n\) unless \(\ge n^{1+\delta}\) entries change - would imply superlinear circuit lower bounds, but none is known; recent work instead shows several long-hoped-for candidates (Hadamard, Fourier, circulant) are **not** rigid. The asymptotic problem is beyond a single session, so this prompt targets its *certifiable core*: exact rigidity values of specific structured matrices at small size, and machine-checked non-rigidity witnesses or lower-bound obstructions. Both are closed-loop: an upper bound on rigidity is an explicit sparse change-set with an exactly verified rank drop, and a lower bound is a certified statement that no change-set of a given weight lowers the rank - an exact linear-algebra / ILP / SAT infeasibility with a replayable certificate. This matches symbolic and certified-search methods. The on-machine verifier is exact rank computation over the stated field plus a replayable infeasibility certificate. **Honest calibration:** the explicit-rigidity problem is genuinely hard and will not be resolved here; the certified small-case values, witnesses, and obstructions are the product, and are valued as such.

## 1. Exact problem statement

Fix a field \(\mathbb{F}\) (state it; \(\mathbb{Q}\), \(\mathbb{R}\), or \(\mathbb{F}_q\)) and a matrix \(M\in\mathbb{F}^{n\times n}\). For a target rank bound \(r\), the **rigidity** is

\[
R_M(r)\ =\ \min\{\,\lVert C\rVert_0\ :\ \operatorname{rank}_{\mathbb F}(M+C)\ \le\ r\,\},
\]

where \(\lVert C\rVert_0\) is the number of nonzero entries of the change matrix \(C\). Equivalently, \(R_M(r)\) is the fewest entries whose alteration brings the rank to \(\le r\). \(M\) is **Valiant-rigid** if for some constants \(\varepsilon,\delta>0\),

\[
R_M(\varepsilon n)\ \ge\ n^{1+\delta}\quad\text{for all large } n .
\]

**Conventions.**

- Rigidity is field-dependent (change values range over \(\mathbb{F}\)); state the field for every claim.
- A **support-fixed** variant asks only which entries change (values free); the values-and-support variant is the default here - say which is used.
- Generic (random) \(M\) has \(R_M(r)=(n-r)^2\); explicit constructions fall far short of the Valiant regime.
- The special case \(r=n-1\) asks the fewest changes to make \(M\) singular, i.e. \(R_M(n-1)\) equals the minimum number of entries hitting every term of \(\det M\) - already a nontrivial exact-search target.
- Changes may be to arbitrary field values; the sparser but weaker "sign-change" or "Boolean" variants are different problems and must be labelled if used.

Equivalently, writing \(C=\sum_{(i,j)\in S}c_{ij}E_{ij}\) for a support \(S\subseteq[n]\times[n]\), the lower bound to be certified is

\[
\forall S,\ |S|<R_M(r),\ \forall\, (c_{ij})_{(i,j)\in S}\in\mathbb{F}^{S}:\quad \operatorname{rank}_{\mathbb F}\!\Big(M+\textstyle\sum_{(i,j)\in S}c_{ij}E_{ij}\Big)\ >\ r .
\]

**Structured targets (choose per session, state the field and \(r\)).** Hadamard \(H_{2^k}\), Fourier/DFT \(F_n\), circulant and Toeplitz matrices, Vandermonde, Cauchy, Paley/generalized-Hadamard, discrete-geometry incidence matrices, and fixed random matrices as controls. For each, the object of study is the exact function \(r\mapsto R_M(r)\) at small \(n\), and the asymptotic trade-off implied by any provable family bound.

**Known results (to reproduce and re-verify).**

- Hadamard, Fourier, circulant, and Toeplitz matrices are **not** Valiant-rigid (Alman–Williams; Dvir–Edelman; Dvir–Liu).
- Best explicit constructions achieve only \(R_M(r)=\Omega\!\big(\tfrac{n^2}{r}\log\tfrac{n}{r}\big)\), short of \(n^{1+\delta}\) at \(r=\varepsilon n\).
- Exact \(R_M(r)\) for a named matrix at small \(n\) is essentially uncatalogued - this is where certified data can be produced.

**Frontier adopted here.** (i) Exact \(R_M(r)\) for named small matrices over a stated field; (ii) certified non-rigidity witnesses (explicit low-weight change-sets realizing the non-rigidity theorems) or certified rigidity **lower** bounds for structured families at small size. Re-verify all cited results against Section 4.

## 2. Resolution standard

For a stated matrix \(M\), field \(\mathbb F\), and rank bound \(r\), a **resolution** of the exact value \(R_M(r)\) requires **both**:

1. **Upper bound (change-set).** An explicit change matrix \(C\) with \(\lVert C\rVert_0=R_M(r)\) and an **exact rank verification** that \(\operatorname{rank}_{\mathbb F}(M+C)\le r\), computed in exact arithmetic (rational or exact finite-field elimination) by a checker separate from the search.
2. **Lower bound (optimality).** A certificate that no change-set of weight \(R_M(r)-1\) achieves rank \(\le r\). Named forms:
   - (a) a **DRAT/LRAT UNSAT proof** of the SAT/pseudo-Boolean encoding "\(\exists\) support of size \(<R_M(r)\) and values making \(\operatorname{rank}\le r\)" over a finite field;
   - (b) an **ILP infeasibility certificate with an exact rational dual** (SCIP/QSopt_ex) for a linear-algebraic formulation;
   - (c) an **exhaustive support enumeration** over all \(\binom{n^2}{<R_M(r)}\) patterns with exact rank checks (feasible only for very small \(n\)).

For a **non-rigidity theorem instance**, a resolution is an explicit low-weight \(C\) attaining the theorem's claimed change count with the rank drop exactly verified at concrete \(n\), certifying the construction.

The lower-bound certificate must range over *all* weight-\((R_M(r)-1)\) change matrices, not a sampled subset; the encoding therefore quantifies over the support pattern and (for the values-and-support variant) the change values, and the infeasibility artifact is the DRAT/LRAT proof, the exact ILP dual, or the completed enumeration.

**Not accepted as resolution.**

- A change-set (upper bound) with no proof it is minimum-weight.
- A rank computed in floating point (must be exact over the stated field).
- A rigidity claim over one field presented as holding over another.
- An asymptotic non-rigidity statement reported as an exact small-\(n\) value, or conversely.
- A "rigid-looking" experiment (rank stayed high for the change-sets tried) presented as a rigidity lower bound without an infeasibility certificate over *all* change-sets of that weight.
- Any claim of an explicit Valiant-rigid family (this prompt does not expect one; such a claim would require overwhelming, independently checked proof).
- A lower bound proved only for the support-fixed variant reported as a bound on the full (values-and-support) rigidity, or vice versa.

## 3. Graded partial-result targets

- **P1 - Reproduce the negative results.** For explicit small \(n\), construct and exactly verify the low-rank-plus-sparse decompositions underlying the non-rigidity theorems (Hadamard over \(\mathbb{R}\); \(f(x+y)\)-matrices over \(\mathbb{F}_q\); Fourier/circulant over \(\mathbb{C}\)), certifying that the promised change counts really drop the rank.
  - *Certificate:* explicit \(C\) + exact rank check at several \(n\).
- **P2 - Exact small-case rigidity.** Determine \(R_M(r)\) exactly for a named structured matrix at small \(n\) and chosen \(r\), with an upper-bound change-set and a matching infeasibility certificate.
  - *Certificate:* verified \(C\) + certified infeasibility.
- **P3 - Rigidity profile.** The full curve \(r\mapsto R_M(r)\) for a specific small matrix, each point certified, revealing where (if anywhere) it is rigid.
  - *Certificate:* per-\(r\) certificates and a manifest.
- **P4 - Improved obstruction / lower bound.** A certified rigidity lower bound for a structured family at small size stronger than the generic counting bounds, or a certified obstruction to a proposed rigid construction.
  - *Certificate:* the infeasibility certificate + the argument that it beats the counting bound.
- **P5 - New non-rigidity witness.** An explicit low-weight change-set showing a *new* structured family (not yet in the non-rigidity literature) is non-rigid at small \(n\), with exact rank drops and, where possible, a parametric construction.
  - *Certificate:* the family construction + exact checks at several \(n\).
- **P6 - Formalized micro-theorem.** A machine-checked (Lean/Coq) proof of a small exact rigidity statement or of a non-rigidity construction's correctness.
  - *Certificate:* the formal proof + checked kernel.
- **P7 - Cross-field comparison.** For one matrix, certified \(R_M(r)\) over \(\mathbb{Q}\) and over several \(\mathbb{F}_q\), documenting how rigidity shifts with the field.
  - *Certificate:* per-field verified change-sets and infeasibility certificates.

## 4. Known results and prior art

- **Origin.** Valiant (1977) - rigidity and its link to arithmetic circuit / linear-map lower bounds; the target regime \(r=\varepsilon n\), \(R_M(r)\ge n^{1+\delta}\).
- **Generic and counting bounds.** A generic matrix has \(R_M(r)\approx(n-r)^2\); explicit constructions with \(R_M(r)=\Omega\!\big(\tfrac{n^2}{r}\log\tfrac{n}{r}\big)\) are known (Friedman; Shokrollahi–Spielman–Stemann), far short of Valiant's regime.
- **Non-rigidity of candidates.** Alman and Williams (~2017) - the \(2^n\times2^n\) Hadamard matrix is **not** Valiant-rigid. Dvir and Edelman (~2017), via the Croot–Lev–Pach lemma - \(q^n\times q^n\) matrices \(M(x,y)=f(x+y)\) over a fixed \(\mathbb{F}_q\) are not rigid. Dvir and Liu (~2019) - for any abelian group \(G\) and \(f:G\to\mathbb{C}\), the matrix \(M_{xy}=f(x-y)\) is not rigid; hence Fourier, circulant, and Toeplitz are not rigid. Alman (~2021) - further Kronecker-power non-rigidity.
- **Positive / partial rigidity.** Some rigidity is known for special matrices (certain Vandermonde/Cauchy and generalized-Fourier constructions retain nontrivial rigidity in restricted regimes - *verify* the current statements); a 2025 preprint on low-rank matrix rigidity lower bounds and hardness amplification (*verify*).
- **Complexity of computing rigidity.** Exact \(R_M(r)\) is intractable in general (NP-hard flavour); small cases are approachable only by exact linear algebra + ILP/SAT.
- **Rectangular and semi-explicit progress.** Some semi-explicit and higher-rank-regime rigidity lower bounds are known (Kumar–Volk and others), and rigidity in the \(r=o(n)\) or high-\(r\) regimes behaves differently from the Valiant regime; state which regime any small-case result addresses.
- **Surveys and venues.** Workshop notes and surveys (Mrinal Kumar and others) track the state of the art and the barrier results.

**Status as of mid-2026 - re-verify against the current literature and record trackers before starting any session.**

## 5. Attack plan

**`[sym]` - non-rigidity constructions.**

1. For a target matrix, build the explicit low-rank-plus-sparse decomposition from the relevant theorem (polynomial-method / Croot–Lev–Pach for \(f(x\pm y)\) matrices) at concrete small \(n\) in a CAS.
2. Verify the rank drop exactly and count the changed entries.
3. Attempt to extend the construction to a new structured family (P5), checking several \(n\).

**`[search]` - exact small-case rigidity.**

1. For fixed \(M,r\) and a candidate weight \(w\), decide "is there a change-set of weight \(\le w\) making rank \(\le r\)?" by a finite-field SAT/pseudo-Boolean encoding (support indicators + an \(r\)-dimensional column-space witness for rank \(\le r\)), solved with CaDiCaL/kissat/CryptoMiniSat and DRAT/LRAT.
2. Alternatively use an ILP/mixed formulation with exact rational certificates (SCIP exact mode, QSopt_ex/SoPlex).
3. Binary-search \(w\) to pin \(R_M(r)\); for tiny \(n\), exhaustive support enumeration with exact rank checks is the ground-truth cross-check.

**Tools.**

- Algebra: SageMath, Macaulay2 (exact rank, symbolic constructions); FLINT/LinBox for exact rank over \(\mathbb{Q}\) and \(\mathbb{F}_q\).
- SAT: CaDiCaL, kissat, CryptoMiniSat with DRAT/LRAT and drat-trim/cake_lpr.
- Exact optimization: SCIP and QSopt_ex/SoPlex for ILP/LP infeasibility duals.
- Formalization: Lean 4/Coq for P6; custom C++ for support enumeration.

**First concrete session steps.**

1. Reproduce a non-rigidity witness for a small Hadamard \(H_8\) or \(H_{16}\) over \(\mathbb{Q}\) (P1), exact-rank verified.
2. Pick a small structured \(M\) (e.g. \(8\times8\) DFT over a suitable field) and compute \(R_M(r)\) for one \(r\) by exhaustive enumeration as ground truth (P2).
3. Reproduce that value via the SAT and ILP encodings to validate the certified-search pipeline against ground truth.
4. Extend to a rigidity profile (P3) or a new non-rigidity family (P5), staying at \(n\) where exact rank is cheap.
5. Fix the matrix, field, \(r\), and rigidity variant in the report header before any number, and record the exact-rank method used for verification.

**One-workstation scope and failure modes.** Non-rigidity constructions and rigidity profiles for very small \(n\) are feasible; exact \(R_M(r)\) becomes hard fast because the number of weight-\(w\) supports is \(\binom{n^2}{w}\) and each rank check is over a field. The rank-\(\le r\) constraint is nonconvex, so SAT/ILP encodings can be large and slow. Dominant risks:

- Floating-point rank giving a wrong drop - always exact.
- An "experimentally rigid" false lower bound - only an infeasibility certificate over *all* supports counts.
- Field confusion; and over-claiming - a small-case value says nothing about the asymptotic Valiant regime.
- SAT encoding of the rank-\(\le r\) constraint via a column-space witness can be unsound if the witness dimensionality is mis-encoded - validate the SAT model's implied \(C\) with an independent exact-rank check.

Report scope honestly: this program produces certified data points and obstructions, not a resolution of explicit rigidity.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** All ranks are computed in exact arithmetic over the stated field; every rigidity lower bound is a DRAT/LRAT UNSAT proof, an exact ILP infeasibility dual, or an exhaustive exact enumeration. Floating point is exploration only.
2. **Independent verification.** The exact-rank checker is written separately from the search; SAT infeasibility is re-run by a second solver on a sub-instance; ILP duals are re-verified in exact rational arithmetic (QSopt_ex); tiny cases are cross-checked by brute-force support enumeration.
3. **Reproducibility.** The matrix definition, field, rank bound \(r\), rigidity variant (values-free vs fixed-support), encoding, and tool versions are recorded; a SHA-256 manifest covers change-sets, CNFs, proofs, and LP certificates; the specific theorem or value reproduced is cited with source and access date.
4. **Preservation.** Construction and search code, the exact-rank checker, and all certificates are part of the record; large proofs not stored are hashed with regeneration commands.
5. **Honest reporting.** The report states the matrix, field, and \(r\), whether an exact value or only a bound was certified, and explicitly disclaims any asymptotic (Valiant-regime) implication; a construction that merely resisted the change-sets tried is never reported as a rigidity lower bound, and no explicit-rigid-family claim is made without an overwhelming, independently checked proof.
