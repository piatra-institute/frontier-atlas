# PROMPT FOR SETTLING COLOR-KINEMATICS DUALITY AT LOOP LEVEL

## BCJ duality and the double copy: existence and obstruction theorems for loop integrands

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 35 of 50 (Tier 3)
**Source:** top-50 list #47, category G (QFT and mathematical particle theory)
**Modes:** `[sym]` `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Color-kinematics (CK) duality - the statement that gauge-theory amplitudes admit cubic-graph representations whose kinematic numerators satisfy the same Jacobi identities as their color factors - is proven at tree level (Bern–Carrasco–Johansson 2008, with several independent proofs) and conjectural at loop level, where the double copy would deliver gravity integrands, including those powering gravitational-wave calculations. The loop-level status is nuanced: explicit CK-satisfying representations exist through specific loop orders in specific theories, while at other points (five loops in N=4; two-loop all-plus Yang–Mills in natural ansätze) no representation has been found and workarounds ("generalized double copy") were invented. The problem is matched to current AI methods because at fixed loop order and multiplicity, CK existence inside a declared ansatz space is a finite exact-linear-algebra question: an explicit numerator set is a machine-checkable existence certificate, and a Farkas-type infeasibility certificate is a machine-checkable obstruction theorem. The complete resolution defined in section 2 is the target; the graded targets of section 3 - certified existence and nonexistence theorems at fixed order - are the realistic product, and must never be represented as the all-order statement.

## 1. Exact problem statement

### 1.1 Cubic-graph representations

Work in pure Yang–Mills or N=4 super-Yang–Mills with gauge group $SU(N_c)$, dimensional regularization around $D = 4 - 2\epsilon$ (numerator polynomiality in $D$ tracked explicitly). An $m$-point $L$-loop amplitude is written over the finite set $\Gamma(L,m)$ of cubic graphs:

\[
\mathcal{A}^{(L)}_m \;=\; i^L\, g^{\,m-2+2L} \sum_{\Gamma \in \Gamma(L,m)} \int \prod_{j=1}^{L} \frac{d^D \ell_j}{(2\pi)^D}\; \frac{1}{S_\Gamma}\, \frac{c_\Gamma\, n_\Gamma(\ell, p)}{\prod_{e \in \Gamma} d_e},
\]

where $c_\Gamma$ is the color factor (product of structure constants $f^{abc}$), $d_e$ the inverse propagators, $S_\Gamma$ the symmetry factor, and $n_\Gamma$ a numerator polynomial in external and loop momenta (and polarizations/superspace data). Color factors satisfy antisymmetry and Jacobi relations: for every triple $(\Gamma_s, \Gamma_t, \Gamma_u)$ of graphs differing in one propagator,

\[
c_{\Gamma_s} \;=\; c_{\Gamma_t} + c_{\Gamma_u},
\]

with sign conventions fixed once and recorded in machine-readable form.

**Definition (CK-satisfying representation).** A choice $\{n_\Gamma\}$ such that:

1. $n_\Gamma$ flips sign with $c_\Gamma$ under vertex flips (antisymmetry);
2. $n_{\Gamma_s} = n_{\Gamma_t} + n_{\Gamma_u}$ for every Jacobi triple, with loop-momentum labelings matched;
3. all generalized-unitarity cuts of the right-hand side equal the cuts of the amplitude of the declared theory.

When such $\{n_\Gamma\}$ exists, the double copy replaces $c_\Gamma \to \tilde n_\Gamma$ (a second, possibly identical, CK-satisfying numerator set) to produce the integrand of the corresponding gravitational theory (BCJ 2010):

\[
\mathcal{M}^{(L)}_m \;=\; i^{L+1} \Bigl(\frac{\kappa}{2}\Bigr)^{m-2+2L} \sum_{\Gamma \in \Gamma(L,m)} \int \prod_{j=1}^{L} \frac{d^D \ell_j}{(2\pi)^D}\; \frac{1}{S_\Gamma}\, \frac{n_\Gamma\, \tilde n_\Gamma}{\prod_{e \in \Gamma} d_e}.
\]

The claim that $\mathcal{M}^{(L)}_m$ is the gravity amplitude is itself part of the conjecture at loop level and is verified only through the orders where CK representations are known.

### 1.2 The open questions

- **Q1 (all-order existence).** Does N=4 SYM admit CK-satisfying integrand representations for all $(L, m)$? No proof exists for any $L \ge 1$ as an all-$m$ statement, and at $(L,m) = (5,4)$ no representation was found despite a dedicated campaign.
- **Q2 (obstruction structure).** For which (theory, $L$, $m$, ansatz class) does no CK representation exist? Known negative evidence is ansatz-relative; no ansatz-free obstruction theorem is known.
- **Q3 (double-copy consistency).** Is the generalized double copy (cut-level construction, Bern et al. 2017) a complete substitute - i.e., a proven all-order gravity-integrand construction?

Ansatz-relativity is central and must be kept explicit: "no CK representation exists" is only meaningful relative to a declared numerator space (power counting, locality, crossing/relabeling symmetry, four- versus $D$-dimensional cuts). Every statement in this program names its ansatz space $\mathcal{A}$ or proves ansatz-freeness. No informal phrasing ("the double copy works at loops") is an acceptable target.

## 2. Complete-resolution standard

Complete resolution is one of:

1. **Proof of Q1:** an all-order construction (all $L$, all $m$) of CK-satisfying integrands for N=4 SYM (or a precisely named theory), with properties 1–3 of section 1.1 proved and the locality/power-counting class of the numerators stated exactly.
2. **Ansatz-free refutation:** a theorem that for some $(L, m)$ no CK-satisfying representation exists in the *full* space of local numerators of arbitrary finite power counting - an obstruction invariant under all representation freedom, with the invariance proved - plus a precise statement of what the double copy can still produce there.
3. **Proof of Q3:** a proven, theory-level generalized-double-copy construction valid at all orders, with the gravity integrand's cuts proved correct.

**Not accepted as resolution:**

- Existence inside a declared finite ansatz space presented as ansatz-free existence, or nonexistence in a finite ansatz presented as an absolute obstruction.
- Order-by-order constructions through any finite $(L, m)$ presented as the all-order statement.
- Floating-point cut checks; only exact arithmetic counts.
- Tree-level results (KLT, BCJ relations) restated or re-proved as loop-level progress.
- "CK duality up to total derivatives / up to anomalies / off-shell in a BV framework" without a precise theorem stating exactly which of properties 1–3 survives - homotopy-algebraic manifestations that silently relax locality or introduce non-local field redefinitions do not meet the standard (they may be reported as partial structure, cf. P6).
- Double-copy outputs asserted to be gravity amplitudes without cut verification.

## 3. Graded partial-result targets

### P1 - Tree-level ground truth with our own toolchain

- Independent implementation of YM tree amplitudes (Berends–Giele recursion) over exact rationals and finite fields $\mathbb{F}_p$ with CRT lift and rational reconstruction.
- Verify color decomposition, Kleiss–Kuijf, and BCJ amplitude relations exactly for $m \le 8$.
- Construct explicit tree-level CK numerators (e.g. from the Del Duca–Dixon–Maltoni basis plus KLT-derived transformations).
- *Certificate:* exact identities over $\mathbb{Q}$; standalone checker re-evaluating amplitudes at independent random rational kinematics.

### P2 - Certified replication of a known loop-level CK representation

- Take the published N=4 SYM 3-loop 4-point CK numerators (BCJ 2010) and verify in exact arithmetic: all Jacobi triples, all symmetry-factor conventions, and a spanning set of unitarity cuts against independently computed tree input from P1.
- This end-to-end independent verification is rarely done and calibrates every convention in the pipeline.
- *Certificate:* cut-match residuals identically zero over $\mathbb{Q}$; machine-readable graph and Jacobi-triple tables.

### P3 - Certified existence/nonexistence at fixed $(L, m, \text{theory}, \mathcal{A})$

- Encode CK constraints plus cut matching as an exact linear system over $\mathbb{Q}$ (finite-field sampling, CRT lift, rational reconstruction).
- Outcome A: explicit numerators - an existence certificate, independently re-verified.
- Outcome B: an exact infeasibility certificate (Farkas vector / inconsistent subsystem) yielding the theorem "no CK representation exists within $\mathcal{A}$".
- Primary targets: two-loop four-point pure YM; two-loop five-point all-plus pure YM (reproduce the Mogull–O'Connell obstruction as a certified theorem with $\mathcal{A}$ in the statement); two-loop five-point N=4 (existence, replicating Carrasco–Johansson).
- A certified nonexistence with explicit $\mathcal{A}$ is publishable.

### P4 - Obstruction structure

- From P3 infeasibility data, extract minimal infeasible subsystems (IIS): which cut equations conflict with which Jacobi orbits.
- Prove minimality; chart the stability of the obstruction under a declared enlargement ladder (higher power counting, relabeling asymmetry, $D$-dimensional terms) - the feasibility boundary is the scientific product.
- *Certificate:* IIS data plus machine-verified minimality and the enlargement-ladder log.

### P5 - Generalized double copy, certified

- Implement the cut-level generalized-double-copy construction on a controlled example (one- or two-loop, low multiplicity).
- Certify that the constructed gravity integrand's spanning cuts equal the double-copied cuts exactly.
- *Certificate:* exact cut equalities over $\mathbb{Q}$.

### P6 - Sector proofs (strongest short of resolution)

- All-order theorems in restricted sectors: the self-dual sector's kinematic algebra (Monteiro–O'Connell 2011) made into a proof of CK duality for self-dual YM at tree level, extended to one-loop all-plus if sustainable.
- Formalize the algebraic core - Lean 4 formalization of the Jacobi-closure statement and the DDM basis dimension $(m-2)!$ is a suitable artifact.
- Any all-$m$ statement at fixed $L \ge 1$, or any ansatz-free obstruction, proved, exceeds this tier and approaches section 2.

## 4. Known results and prior art

- Kawai–Lewellen–Tye 1986: tree-level closed/open string relations (gravity = YM$^2$ at tree level).
- Bern–Carrasco–Johansson 2008: CK duality and BCJ amplitude relations at tree level; proofs via string monodromy (Bjerrum-Bohr–Damgaard–Vanhove 2009; Stieberger 2009) and on-shell recursion (Feng–Huang–Jia ~2010).
- Bern–Carrasco–Johansson 2010: loop-level conjecture and double copy; N=4 SYM 4-point CK representations at 1–3 loops; 4-loop 4-point (Bern–Carrasco–Dixon–Johansson–Roiban ~2012).
- Carrasco–Johansson 2011: two-loop five-point N=4 CK representation (verify scope).
- Bern–Carrasco–Chen–Johansson–Roiban–Zeng 2017: five-loop four-point N=4 - standard CK representation not found; generalized double copy introduced and used for the five-loop UV computation.
- Mogull–O'Connell 2015: obstructions to natural CK ansätze at two-loop five-gluon all-plus, and relaxations that work (verify exact ansatz statements).
- Monteiro–O'Connell 2011: kinematic algebra of the self-dual sector.
- CHY/ambitwistor formulations: Cachazo–He–Yuan 2013; loop-level scattering equations (Geyer–Mason–Monteiro–Tourkine ~2015) (verify what they prove about CK at loops).
- Homotopy-algebraic program: Reiterer ~2019; Borsten–Jurčo–Kim–Macrelli–Sämann–Wolf ~2020–2023 - claims that CK duality can be made manifest at loop level via BV-type completions, with important caveats about locality/renormalization (verify exact theorems; this is the most likely place where the frontier moved by 2026).
- Reviews: Bern–Carrasco–Chiodaroli–Johansson–Roiban, the double-copy review ~2019 with later updates (verify latest edition).
- Payoff line: post-Minkowskian gravitational-wave computations via double copy (Bern–Cheung–Roiban–Shen–Solon–Zeng 2019, 3PM; 4PM extensions ~2021–2022).

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

1. **Kinematics substrate.**
   - Exact rational spinor-helicity and $D$-dimensional momenta over $\mathbb{Q}$ and $\mathbb{F}_p$ (own Python/FLINT code).
   - Berends–Giele recursion for trees; identities checked at many independent rational points with certified degree bounds (Schwartz–Zippel), then exact reconstruction where feasible.
2. **Graph layer.** Generate $\Gamma(L,m)$ with symmetry factors and Jacobi triples combinatorially (own code plus nauty for isomorphism); publish the machine-readable tables - published conventions are a chronic source of sign errors.
3. **Linear systems (P3).**
   - Ansatz spaces: local polynomial numerators of declared mass dimension and power counting, symmetrized over graph automorphisms.
   - Sizes: two-loop five-point ansätze reach $10^4$–$10^6$ unknowns - workstation-feasible with $\mathbb{F}_p$ sampling (FLINT sparse solvers), then CRT and rational reconstruction.
   - Store the exact system, not just the solution.
4. **Cuts.** Spanning sets of generalized-unitarity cuts built from P1 trees; $D$-dimensional cuts via six-dimensional embedding for pure YM (the all-plus sector needs the $\mu^2$ terms - a known trap); FORM for heavy symbolic manipulation where Python is too slow.
5. **Certification.**
   - Existence: an independent checker re-verifies Jacobi triples and cut equalities from stored numerators.
   - Nonexistence: the Farkas certificate re-checked by exact matrix-vector arithmetic in a standalone C++/GMP tool.
6. **Formal layer (P6).** Lean 4: color Jacobi closure, DDM basis dimension, tree-level BCJ relations at low multiplicity over exact kinematics.

Expected failure modes: incomplete cut spanning sets producing false "existence" (mitigate: prove or inherit - with citation and check - the spanning property for the declared theory and order); too-small ansatz producing vacuous "nonexistence" (mitigate: always publish $\mathcal{A}$ and run the P4 enlargement ladder); sign and labeling drift between graph tables and cut code (mitigate: end-to-end tree-level closure tests); rational-reconstruction failures from unlucky primes; conflating four-dimensional and $D$-dimensional statements.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All amplitude identities, cut matches, and feasibility results over $\mathbb{Q}$ or $\mathbb{F}_p$ with CRT-certified lifts; no floating-point number enters any certificate.
2. **Independent verification.** Every existence certificate re-checked by a standalone checker (C++/GMP) sharing no code with the solver; every infeasibility certificate re-verified by direct exact arithmetic; tree-level inputs cross-checked against an independent recursion implementation.
3. **Reproducibility.** All kinematic seeds, primes, ansatz definitions, graph tables, and solver parameters recorded; SHA-256 manifest over systems, certificates, and numerator tables; pinned FLINT/FORM/nauty versions.
4. **Preservation.** The exact linear systems (not only their solutions), failed ansätze, and the enlargement-ladder logs are part of the record; discarded material is listed.
5. **Honest reporting.** Every statement carries its scope - (tree), (fixed $(L,m)$, ansatz $\mathcal{A}$), (sector) - and the final report states up front that the all-order questions Q1–Q3 remain open unless section 2 was met; ansatz-relative nonexistence is never reported as an absolute obstruction.
