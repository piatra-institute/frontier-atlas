# PROMPT FOR THE 2D ISING MODEL IN A MAGNETIC FIELD

## Exact structure and integrability obstructions off the Onsager line

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 38 of 50 (Tier 4)
**Source:** top-50 list #22, category C (exactly solvable models and lattice statistics)
**Modes:** `[sym]` `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The square-lattice Ising model has an exact free energy only on the zero-field line (Onsager 1944); for $H\neq0$ no exact solution exists, and none is expected. The known exact islands are the scaling theory at $T=T_c$ with small $H$ - Zamolodchikov's $E_8$ field theory (1989), confirmed experimentally - the Lee–Yang circle theorem and edge scaling, and analyticity theorems (Isakov's essential singularity at $H=0$ below $T_c$). This is a **Tier 4 problem: background and opportunistic only**. No frontal assault on the free energy is to be attempted or budgeted; any session on this prompt runs at low priority relative to Tier 1–2 problems and should reuse their tooling. The product is the graded targets: certified field-series at fixed temperature with structure analysis, exact finite-lattice data with certified Lee–Yang structure, certified lattice extraction of $E_8$ signatures, and - the one place where a genuine theorem is plausibly within reach of machine-assisted work - non-integrability statements in the precise sense of nonexistence of local conserved charges (Shiraishi–Chiba-style; verify current formulations first). The complete resolution defined in section 2 is the target in name only; it is explicitly not the expected outcome, and anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

### 1.1 Model

Square-lattice boxes $\Lambda_{L,M}\subset\mathbb{Z}^2$, spins $\sigma_i\in\{\pm1\}$, periodic boundary conditions unless flagged:

\[
Z_{L,M}(K,h)=\sum_{\sigma}\exp\Big(K\sum_{\langle ij\rangle}\sigma_i\sigma_j+h\sum_i\sigma_i\Big),
\qquad K=J/k_BT,\quad h=H/k_BT .
\]

Free energy $f(K,h)=\lim_{L,M\to\infty}\tfrac{1}{LM}\log Z_{L,M}$; magnetization $M(K,h)=\partial f/\partial h$. In the algebraic variables

\[
u=e^{-4K},\qquad \mu=e^{-2h},
\]

$Z_{L,M}$ is, up to an explicit prefactor, a polynomial in $(u,\mu)$ with nonnegative integer coefficients; the exact prefactor convention is fixed and recorded in-session.

### 1.2 Transfer matrix and quantum chain

Row-to-row transfer matrix $V(K,h)$ on $(\mathbb{C}^2)^{\otimes L}$ in the symmetric form $V=V_h^{1/2}V_2V_1V_h^{1/2}$ (horizontal-bond, vertical-bond, and field factors), with $Z_{L,M}=\mathrm{tr}\,V^M$. Its extreme anisotropic limit is the mixed-field Ising quantum chain

\[
H_{\mathrm{MFI}}=-\sum_{j}\big(Z_jZ_{j+1}+g\,X_j+\lambda\,Z_j\big),
\qquad g,\lambda>0,
\]

with $X,Z$ Pauli matrices. Every claim must declare which object it concerns - 2D classical model, row transfer matrix, or chain - and the dictionary between them is part of the record.

### 1.3 Known exact boundary (not the target)

$h=0$ (Onsager; Yang); $K\to\infty$ ground states; fixed-width strips (everything algebraic); the scaling limit $T=T_c$, $h\to0^+$ described by the $E_8$ integrable field theory with mass ratios such as $m_2/m_1=2\cos(\pi/5)$; the imaginary field $h=i\pi/2$, where exact lattice results exist (verify literature) and which is excluded from any "resolution" claim as previously known.

### 1.4 The open problem (adopted formulation)

Off the line $h=0$ and off the trivial limits, determine the exact-solvability structure of $f(K,h)$. The session-relevant precise questions:

1. **(Exactness)** Does any nontrivial exact island exist on the lattice at real $h\neq0$ - a point or curve $(K,h)$ where $f$, $M$, or the correlation length is in closed form?
2. **(Integrability obstruction)** For which $(g,\lambda)$ with $\lambda\neq0$ does $H_{\mathrm{MFI}}$ possess local conserved charges? Precisely: a *local conserved charge of support $k$* is an operator

\[
Q=\sum_{j}\tau_j(q),\qquad q\in\mathrm{End}\big((\mathbb{C}^2)^{\otimes k}\big),
\]

with $\tau_j$ the translation embedding $q$ at sites $j,\dots,j+k-1$, such that $[H_{\mathrm{MFI}},Q]=0$ and $Q$ is not a linear combination of $H_{\mathrm{MFI}}$, the identity, and charges of smaller support. Conjecture: none exists for any $k$ when $\lambda\neq0$. Proofs exist for closely related chains and possibly for this one (verify Chiba-type results before any work).
3. **(Analytic structure)** The nature of the fixed-$T$ field series of $f$ and $M$: radius, singularities (Lee–Yang edge), D-finiteness or its failure.

## 2. Complete-resolution standard

A complete resolution - stated for discipline; not expected - is one of:

- **(A)** An exact closed form for $f(K,h)$ on an open region with real $h\neq0$, with proof and certified numerical verification against transfer-matrix enclosures.
- **(B)** A new exact island: closed form for $f$, $M$, or the correlation length on an explicit curve or point with real $h\neq0$, with proof (imaginary-field and other previously published islands excluded).
- **(C)** A complete integrability classification of $H_{\mathrm{MFI}}$: for all $(g,\lambda)$ with $\lambda\neq0$ and all support sizes $k$, a proof that no nontrivial local conserved charge exists (or the discovery of one), with every computational step certified.

**Not accepted as resolution:**

- Restatements or numerical confirmations of the $E_8$ spectrum, Fonseca–Zamolodchikov analytic structure, or Lee–Yang/Cardy edge scaling - field-theory results about the scaling limit, not the lattice free energy.
- Truncated series in $h$, to any order, or Padé/differential-approximant analytics presented as exact solution.
- Non-integrability for a bounded support cutoff $k\le k_0$ presented as the full classification (that is P5 - valuable, but partial).
- Numerical transfer-matrix spectra, TCSA, or DMRG data of any precision presented as exact structure.
- Complexity-theoretic remarks (hardness of Ising with fields on general graphs) offered as resolving the analytic question on $\mathbb{Z}^2$.
- Re-derivations of the Lee–Yang or Isakov theorems presented as new.

## 3. Graded partial-result targets

Tier 4 discipline, stated as binding session rules:

- attempt these targets only as background capacity permits, and never at the expense of a Tier 1–2 session;
- every target is sized to reuse tooling from the Tier 1–2 category C problems (transfer matrices, series engines, interval Perron certificates), and the session must record what it borrows;
- the expected best outcome of a session on this prompt is P1–P3 plus the P5 literature gate; P5/P6 as theorems are opportunistic upside, not the plan of record.

- **P1 - Exact finite-lattice data with certified Lee–Yang structure.**
  - *Task:* compute $Z_{L,M}(K,h)$ as exact bivariate polynomials in $(u,\mu)$ for sizes up to a measured frontier (target $16\times16$ with symmetry reduction), dual implementations; certify on this data that all zeros in $\mu$ lie on $|\mu|=1$ at physical $u$ (the Lee–Yang circle theorem - known, and serving here as pipeline validation) with certified root localization.
  - *Certificate:* polynomial files + dual-code agreement + Arb interval root certificates.
- **P2 - Long certified field series at fixed temperature.**
  - *Task:* finite-lattice-method series for $f$ and $M$ in powers of $h$, and mixed low-temperature/field expansions, with exact rational coefficients, at general $u$ and at $u=u_c$; extend the classical tables (Sykes-era high-field polynomials; Baxter–Enting methodology) with our own verified code.
  - *Certificate:* exact coefficients, two independent derivations agreeing, hashes.
- **P3 - Structure analysis of the field series.**
  - *Task:* D-finiteness exclusion certificates for the fixed-$T$ field series ("no ODE of order $\le r$, degree $\le d$ annihilates the series to depth $N$"); certified singularity analysis in $\mu$ - Lee–Yang edge location and exponent enclosures at $T>T_c$, with the field-theory prediction $\sigma=-1/6$ used as a labeled comparison point, never as an assumption.
  - *Certificate:* linear-algebra transcripts; Arb enclosures with stated error logic.
- **P4 - Certified lattice $E_8$ signatures.**
  - *Task:* at $u=u_c$ with small $h>0$: interval-certified leading and subleading transfer-matrix eigenvalues on strips at feasible widths; extraction of mass-gap ratios with rigorous finite-size treatment where provable and honest labeling where not; comparison against $m_2/m_1=2\cos(\pi/5)=1.6180\ldots$ and higher ratios.
  - *Certificate:* interval eigenvalue enclosures + extraction scripts; a certified table "ratio $\in$ [interval] at width $L$" - a reproducibility anchor for the experimental literature.
  - *Value:* the $E_8$ ratios are usually exhibited by field-theory or DMRG numerics; a fully certified lattice table at declared widths is a new kind of artifact.
- **P5 - Bounded non-integrability theorem for the mixed-field Ising chain.**
  - *Task:* for explicit support cutoffs $k\le k_0$ (target $k_0\ge10$; push as far as exact linear algebra allows), prove that $H_{\mathrm{MFI}}$ - ideally symbolically in $(g,\lambda)$, else on declared parameter families - has no nontrivial conserved charge of support $\le k_0$: exact nullspace computation on the commutant constraint, independently re-deriving the Shiraishi–Chiba proof architecture. **Literature gate:** if the full theorem for exactly this chain is already published (verify), the target becomes an independent certified verification plus a precisely scoped extension (parameter families, boundary variants, quasi-local or higher-spin charge classes they exclude).
  - *Certificate:* the constraint matrices, exact ranks, an independent checker, and a mathematical write-up of exactly what the finite computation proves.
- **P6 - Strongest realistic proof target.**
  - *Task:* promote P5 to all $k$ - a full non-integrability theorem in the sense of (C) for at least one explicit $(g,\lambda)$ - by an induction on support size whose base cases are the certified P5 computations; only if the literature check shows this exact statement unpublished.
  - *Certificate:* complete proof with certified computational base cases.

## 4. Known results and prior art

- L. Onsager (1944), C. N. Yang (1952): the $h=0$ exact line. B. McCoy, T. T. Wu (1973 book and onward): the analyticity tradition for the 2D Ising model, including field and boundary-field questions.
- T. D. Lee, C. N. Yang (1952): circle theorem. M. E. Fisher (1978): Lee–Yang edge as a critical point. J. Cardy (1985): the 2D edge as the $\mathcal{M}(2,5)$ minimal model, $\sigma=-1/6$.
- S. N. Isakov (1984): essential singularity of the free energy at $h=0$ for $T<T_c$; no analytic continuation in $h$ through the transition.
- A. B. Zamolodchikov (1989): $E_8$ integrable structure of the $T=T_c$, $h\neq0$ scaling theory; eight masses with algebraic ratios. P. Fonseca, A. B. Zamolodchikov (2003): analytic properties of the Ising field-theory free energy in field. R. Coldea and collaborators (2010): experimental confirmation of the lowest $E_8$ ratios in CoNb$_2$O$_6$.
- Series tradition: M. F. Sykes and collaborators (1960s–70s): high-field polynomials. R. J. Baxter, I. Enting (1979): the finite-lattice method. A. J. Guttmann school: series-analysis practice.
- Numerical exact-structure work at criticality in field: variational corner-transfer-matrix computations of the scaling function (V. Mangazeev, M. Batchelor and collaborators, ~2008–2010) (verify).
- Imaginary field $h=i\pi/2$: exact solvability results (Lin–Wu tradition, ~1988) (verify precise statements).
- Lattice non-integrability proofs: N. Shiraishi (2019): absence of local conserved quantities in the XYZ chain with field; Y. Chiba (~2024): proof for the mixed-field Ising chain (verify exact scope - this determines the status of P5/P6); subsequent classification programs for spin-1/2 chains (Shiraishi school, ~2024 onward) (verify).
- No exact lattice free energy at real $h\neq0$ exists; no credible path to one is known.

**Status as of mid-2026 - re-verify against current literature before starting the session.** In particular: the exact scope of the Chiba/Shiraishi non-integrability theorems (this decides whether P5/P6 are new theorems, extensions, or certified verifications), any new exact islands in field, and the current state of the field-series tables.

## 5. Attack plan

Single workstation; everything below deliberately shares infrastructure with prompts 06, 12, 13, 14.

1. **Finite-lattice engine (P1, P2).**
   - C++ transfer matrix over $\mathbb{Z}[u,\mu]$ with FLINT polynomial arithmetic; symmetry reduction (translation; spin-flip combined with $\mu\to\mu^{-1}$); SymPy reference implementation for small sizes.
   - Failure mode: bivariate coefficient swell - switch to evaluation at many rational points with CRT interpolation, recording the degree-bound argument that makes reconstruction rigorous.
   - Failure mode: prefactor-convention drift between the polynomial and exponential forms of $Z_{L,M}$ - the frozen convention of section 1.1 is checked by an automated identity test at $h=0$ against Onsager finite-lattice data.
2. **Series structure (P3).**
   - Sage ore_algebra exclusion runs on the exact series; Arb (python-flint) for certified zero localization and edge enclosures via interval Newton on partial factorizations.
   - Failure mode: too few terms for informative exclusion envelopes - report the exact $(r,d,N)$ reached; never extrapolate the envelope.
3. **Strip spectra (P4).**
   - Sparse implicit application of $V$; power/Lanczos exploration; certification: Collatz–Wielandt-type certificates for the dominant eigenvalue, gap-based certified bounds for subdominant ones where achievable.
   - Failure mode: rigorous subdominant enclosures are genuinely hard - the honest fallback is a rigorous dominant eigenvalue plus clearly-labeled non-rigorous subdominant data; the ratio table then carries mixed labels, stated per entry.
4. **Conserved-charge linear algebra (P5, P6).**
   - The commutant constraint $[H_{\mathrm{MFI}},\sum_j\tau_j(Q)]=0$ for support-$k$ densities $Q$ is a finite exact linear system in the Pauli-basis coefficients (dimension growing like $4^k$); build it symbolically (SymPy/Sage), compute ranks exactly (FLINT modulo several primes with reconstruction; symbolic minors for parameter families); re-verify any claimed nullspace by direct commutator substitution in a second CAS.
   - Failure mode: memory ceiling in $k$ (expect $k_0$ in the low teens) - state the reached $k_0$ exactly; a bounded theorem with exact scope beats an unbounded claim with a gap.
5. **Literature gate (mandatory first step for P5/P6).**
   - Execute the section 4 verification pass before any conserved-charge work; if the full non-integrability theorem for $H_{\mathrm{MFI}}$ is published, re-scope to certified verification plus extension the same day, and record the re-scoping in the report.

## 6. Verification and auditability requirements

Instantiating the five template requirements for this problem:

1. **Exact arithmetic.** All partition-function polynomials and series coefficients exact; all zero-localization and eigenvalue claims in Arb ball arithmetic with directed rounding; all conserved-charge rank computations exact (multi-prime with reconstruction, or symbolic); floating point only in quarantined exploration.
2. **Independent verification.** Dual implementations of the finite-lattice engine; an independent checker re-verifying (i) Lee–Yang certificates by evaluating the polynomials on certified arcs, and (ii) every claimed conserved-charge nullspace by direct commutator substitution in a different CAS from the one that built the constraint matrix.
3. **Reproducibility.** A conventions file fixing the $(u,\mu)$ normalizations, boundary conditions, and the chain dictionary; all sizes, primes, and precisions recorded; SHA-256 manifest over polynomials, series, constraint matrices, certificates, and logs.
4. **Preservation.** All code preserved, including failed certification attempts; imported field-theory numbers ($E_8$ masses) and any published series used for cross-checks archived with provenance, separate from our recomputations.
5. **Honest reporting.** The report opens by restating that this is a Tier 4 background problem and whether the section 2 standard was met (expected: not); every non-integrability claim carries its exact finite scope ($k\le k_0$, parameter set) inside the claim itself; scaling-theory comparisons (P4) are labeled comparisons, never lattice theorems; and any literature-gate re-scoping of P5/P6 is stated explicitly.
