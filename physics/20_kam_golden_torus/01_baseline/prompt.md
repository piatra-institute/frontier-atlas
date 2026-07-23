# PROMPT FOR THE EXACT BREAKUP THRESHOLD OF THE GOLDEN INVARIANT CIRCLE OF THE STANDARD MAP

## Greene's constant $K_c \approx 0.971635406$, the MacKay renormalization fixed point, and certified two-sided windows

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 20 of 50 (Tier 2)
**Source:** top-50 list #38, category E (dynamical systems and classical mechanics)
**Modes:** `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The golden-mean invariant circle of the Chirikov standard map is the most robust KAM torus of the best-studied area-preserving map, and its breakup parameter $K_c = 0.971635406\ldots$ (Greene 1979) is the canonical critical constant of the Hamiltonian transition to chaos. No closed form is known, no exact characterization is proven, and even the rigorous two-sided window - computer-assisted KAM existence below, converse-KAM nonexistence above - does not pinch to the observed value. The problem is matched to current AI methods because every ingredient is a certified-computation or symbolic-mining task: a-posteriori KAM validation in ball arithmetic, converse-KAM box coverings, Lanford-style functional-analytic enclosures of the MacKay renormalization fixed point, and disciplined PSLQ mining of high-precision digits. The complete resolution defined in section 2 - an exact determination of $K_c$ - is the target; it is frankly unlikely at present, and the graded targets of section 3 are the intended session product. Anything less than section 2 must be reported as a partial result, never as a solution.

## 1. Exact problem statement

### 1.1 The map and the golden circle

On the cylinder $\mathbb{A} = \mathbb{T} \times \mathbb{R}$, $\mathbb{T} = \mathbb{R}/\mathbb{Z}$, define the standard family

\[
f_K(x, y) = \big(x + y',\; y'\big), \qquad y' = y - \tfrac{K}{2\pi}\,\sin(2\pi x),
\]

an exact symplectic twist map. Sign and scaling conventions differ across the literature by conjugation; this normalization, with $K_c \approx 0.9716354$, is the one adopted, and any session using another convention must exhibit the conjugacy explicitly before comparing numbers. Fix the golden rotation number

\[
\gamma = \frac{\sqrt{5} - 1}{2} .
\]

A **rotational invariant circle (RIC)** with rotation number $\gamma$ is a homotopically nontrivial $f_K$-invariant set that is the graph of a continuous function $y = \varphi(x)$ (Birkhoff: any RIC of a twist map is a Lipschitz graph), on which the induced circle dynamics has rotation number $\gamma$.

### 1.2 The threshold and the question

Define

\[
\mathcal{K}(\gamma) = \{ K \ge 0 : f_K \text{ has a RIC of rotation number } \gamma \}, \qquad
K_c = \sup \mathcal{K}(\gamma).
\]

Note that $\mathcal{K}(\gamma)$ being an interval (monotone destruction) is itself unproven for the standard family; all statements must distinguish $\sup$ from interval endpoints.

**Adopted question.** *Determine $K_c$ exactly: produce either a closed-form expression, or a proved exact characterization - for example, as the unique parameter where the standard family meets the stable manifold of a rigorously constructed renormalization fixed point - together with a certified enclosure consistent with $K_c = 0.9716354063\ldots$*

### 1.3 The renormalization frame

Greene's residue criterion computes $K_c$ from the stability of the periodic orbits with rotation numbers $p_k/q_k$ the Fibonacci convergents of $\gamma$. For a period-$q$ orbit, the residue is

\[
R \;=\; \tfrac14\,\big(2 - \operatorname{tr} Df_K^{\,q}\big),
\]

and the (non-rigorous) criterion reads: subcritically the convergent-orbit residues $R_k \to 0$, supercritically $|R_k| \to \infty$, and at $K = K_c$ they tend to a universal value $R^* \approx 0.25$. MacKay (1982–83) explained this via a renormalization operator $\mathcal{R}$ on commuting pairs of area-preserving maps:

- the simple (integrable) fixed point governs subcritical behavior;
- a **critical fixed point**, with a single unstable eigenvalue $\delta \approx 1.6280$, is conjectured to govern breakup, $K_c$ being the parameter where the standard family crosses its codimension-one stable manifold.

A computer-assisted existence proof of a critical commuting-pair fixed point is due to Arioli–Koch (~2010) - verify the exact statement, function space, and what portion of hyperbolicity is established. The full global picture (stable manifold, transversal family crossing, and identification of the crossing parameter with $K_c$ as defined in 1.2) is not proven. That gap is part of the problem, not background.

## 2. Complete-resolution standard

A complete resolution is one of:

1. **Closed form.** An exact expression for $K_c$ over an explicitly declared class of constants and functions, with complete proof, plus a certified interval enclosure of the expression agreeing with a certified enclosure of $K_c$.
2. **Exact renormalization characterization.** All of:
   - (i) existence of the critical fixed point of an explicitly defined $\mathcal{R}$ in an explicit Banach space, with certified enclosure;
   - (ii) hyperbolicity: one simple unstable eigenvalue (certified enclosure of $\delta$) and a certified spectral bound $< 1$ on the complement, modulo trivial/coboundary directions;
   - (iii) a codimension-one local stable manifold;
   - (iv) proof that the standard family crosses it transversally at a unique parameter $K^*$, with certified enclosure;
   - (v) proof that $K^* = K_c$ in the sense of 1.2 - RIC existence on the relevant side and nonexistence on the other, at map level, not merely at renormalization level. Item (v) is the historically missing global step and must not be elided.

**Not accepted as resolution**

- Greene-residue or any other numerics, at any precision, including "hundreds of digits".
- A certified two-sided window $[K_{\mathrm{exist}}, K_{\mathrm{nonexist}}]$, however tight - that is P1/P2, not a resolution.
- Formal renormalization expansions or non-rigorous fixed-point computations.
- A PSLQ-candidate closed form without proof (report it, clearly labeled conjectural).
- Assuming without proof that $\mathcal{K}(\gamma)$ is an interval, or that Greene's criterion is exact (partial justifications exist - Falcolini–de la Llave, MacKay - but the criterion is not a theorem for this family).
- Results for other rotation numbers, other maps, or averaged noble thresholds represented as statements about this $K_c$.

## 3. Graded partial-result targets

- **P1 - Reproduce a certified two-sided window with our own pipeline.**
  - *Task (existence):* implement the parameterization method with an a-posteriori KAM theorem (Figueras–Haro–Luque style) in ball arithmetic; certify the golden RIC at $K = 0.97$ or better.
  - *Task (nonexistence):* implement a converse-KAM criterion (MacKay–Percival cone-crossing / Jungreis style) over an interval box covering; certify absence of the golden RIC at an explicit $K < 1$.
  - *Certificate:* stored Fourier enclosures plus the verified constants of the KAM theorem; box covering plus cone data - each re-checkable by a standalone verifier.
  - *Value:* toolchain gate; no downstream claim is valid without it.
- **P2 - Tighten the window beyond the published state of the art.**
  - *Task:* push certified existence toward $0.9716{+}$ (Fourier sizes and precision grow steeply) and golden-specific nonexistence below the classical $63/64 = 0.984375$, toward $0.98$ and below.
  - *Certificate:* as P1, at the new parameter values.
  - *Value:* any certified improvement on either side over the literature (as re-verified at session start) is publishable on its own.
- **P3 - High-precision $K_c$ with honest error tiers, plus disciplined relation mining.**
  - *Task:* compute $K_c$ via extended-precision residue sequences accelerated by renormalization extrapolation (MPFR/Arb). Report three tiers: certified interval (from P2); digits stable under method variation; extrapolated digits with a stated non-rigorous error model. Then run PSLQ/LLL against a pre-registered constant basis - declared before mining ($\pi$, $\log 2$, $\gamma = (\sqrt5-1)/2$, $\zeta$ values, $\Gamma$ values at rationals, the MacKay eigenvalue $\delta$, area-preserving scaling constants) - with declared degree/height budgets and multiple-testing accounting.
  - *Certificate:* the tiered value table; mining logs; exclusion certificates (lower bounds on integer-relation norms) for all negatives.
  - *Value:* the community's reference value with, for the first time, an explicit rigor stratification. Honest calibration: hundreds of *certified* digits are likely unreachable because $K_c$ is defined through the family, not through a fixed point; say so in the report.
- **P4 - Certified critical renormalization fixed point (Lanford-style enclosure).**
  - *Task:* independent reproduction, and where possible strengthening, of the Arioli–Koch-type result: existence of the critical fixed point of an explicit commuting-pair operator via Newton–Kantorovich/Krawczyk contraction in an explicit Banach algebra of analytic functions (interval Taylor coefficients on stated polydisks, geometric tail bounds); certified enclosures of the unstable eigenvalue $\delta$ and a spectral bound on the stable complement.
  - *Certificate:* coefficient enclosures, contraction constants, eigenpair residual bounds; independent contraction-inequality checker.
  - *Value:* re-establishes the deepest rigorous fact in the area on an auditable modern stack; prerequisite for P5.
- **P5 - Stable manifold and family crossing.**
  - *Task:* certified codimension-one local stable manifold of the P4 fixed point, and a certified proof that the (renormalized) standard family crosses it transversally at a unique parameter with enclosure $[a,b] \ni 0.9716\ldots$; any rigorous bridge toward section 2 item (v), even one-sided ($K^* \ge K_c$ or $K^* \le K_c$).
  - *Certificate:* manifold enclosure data and the transversality inequality, independently checked.
  - *Value:* the strongest realistic result short of resolution; would reduce the exact-determination problem to the single global step (v).

## 4. Known results and prior art

- Greene (1979): residue criterion, $K_c \approx 0.971635$. MacKay (1982 thesis; 1983 Physica D): renormalization for invariant circles, the critical fixed point, $\delta \approx 1.628$, refined $K_c \approx 0.9716354063$ (verify digit count).
- Rigorous existence (lower bounds): early KAM gave small $K$; de la Llave–Rana (~1990): computer-assisted existence of the golden RIC to $K \approx 0.91$; Figueras–Haro–Luque (2017, Found. Comput. Math.): modern a-posteriori validation reaching $K = 0.9716$ (verify the exact value claimed).
- Rigorous nonexistence (upper bounds): Mather (1984): no RICs at all for $|K| > 4/3$; MacKay–Percival (1985): converse KAM, no RICs for $|K| \ge 63/64 \approx 0.9844$; Jungreis (1991): further improvements (verify the exact threshold and whether it is golden-specific). Check for post-2017 certified converse-KAM work - the current certified window is the key fact to re-verify.
- Greene-criterion justification: Falcolini–de la Llave (~1992) and MacKay (~1992): partial rigorous justifications; the criterion is not a theorem for this family.
- Renormalization rigor: Arioli–Koch (~2010): computer-assisted existence of the critical commuting-pair fixed point (verify scope); Koch (1999–2008) and Gaidashev–Koch: rigorous renormalization for related Hamiltonian settings; Stirnemann (1990s): related golden-circle operators (verify). The full hyperbolicity + stable manifold + family-crossing chain: open.
- Completed analogy: critical circle-map renormalization (de Faria–de Melo ~1999–2000; Yampolsky ~2002–03), where the conceptual program was finished - the model for what section 2 item 2 demands here.
- Non-rigorous high-precision breakup studies: Sobolev blow-up and Padé methods (Calleja–Celletti–de la Llave school, 2010s) - exploratory guidance only.

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

All under `[sym]`, with certified numerics as the substrate.

1. **Existence side (P1a/P2).** Parameterization method: solve the invariance equation $F \circ R_\gamma = f_K \circ F$ for the circle embedding $F$ as a Fourier series. Quasi-Newton iteration in double/extended precision for the approximate solution ($N \sim 2^{12}$–$2^{16}$ modes near-critical); validation via an a-posteriori KAM theorem in Arb ball arithmetic (rigorous composition, rigorous tail bounds); kv or CAPD as the second implementation. Diophantine constants of $\gamma$ are exact.
2. **Nonexistence side (P1b/P2).** Converse KAM: reduce to a fundamental annulus, cover by interval boxes, propagate cone/Lipschitz conditions (MacKay–Percival cone-crossing) with directed rounding; adaptive refinement where the criterion is marginal. Embarrassingly parallel over boxes.
3. **High-precision $K_c$ (P3).** Residues of Fibonacci periodic orbits by Newton on the periodicity equations in MPFR (periods $q_k \sim 10^5$ feasible); Richardson/renormalization extrapolation of the residue crossing; cross-validate against the unstable-eigenvalue expansion at the P4 fixed point. PSLQ via PARI/GP or mpmath at $\ge 2\times$ digit margin, only against the pre-registered basis.
4. **Renormalization enclosure (P4/P5).** Represent the commuting pair by generating functions or direct Taylor maps in two variables on stated polydisks; truncate with explicit geometric tail bounds in a weighted $\ell^1$ Banach algebra; Krawczyk/Newton–Kantorovich contraction with interval coefficients (Arb primary, independent C++/MPFR check); verified dominant eigenpair for $\delta$ (interval power iteration plus Gershgorin control of the compact remainder).

**First computations (session day one).**

1. Non-rigorous Fourier solve of the invariance equation at $K = 0.5$ and $K = 0.9$; confirm the expected exponential decay of Fourier modes (pipeline sanity).
2. Fibonacci periodic orbits to period $q = 987$ in double precision; reproduce Greene's $K_c$ to six digits via the residue crossing.
3. One complete Arb validation run at $K = 0.5$ with loose tolerances - the full certify-and-check loop end-to-end before pushing $K$ upward.
4. Cone-crossing nonexistence with a coarse box cover at $K = 1.2$, then $K = 1.0$; run the independent checker on both artifacts.

**Workstation feasibility.**

- P1: hours-to-days (the 2017-era validations ran on modest hardware).
- P2 near $0.9716{+}$ / $0.98$: days-to-weeks, memory-bound in Fourier size and box count.
- P3: tens of digits cheap; each further band exponentially harder.
- P4: workstation-months of function-space engineering; budget across sessions.

**Expected failure modes.**

- The analyticity strip of the circle shrinks to zero as $K \uparrow K_c$: Fourier tail bounds saturate and the existence method stalls strictly below $K_c$ - inherent, not a bug; report the stall point.
- Converse-KAM box counts blow up as $K \downarrow K_c$ from above; each increment of the upper bound costs multiplicatively.
- A wrong function-space choice in P4 makes Newton diverge despite an excellent numerical fixed point; expect several space redesigns before contraction closes.
- PSLQ false positives at thin precision margins; the pre-registration and margin rules of P3 exist precisely for this.
- Convention mismatches ($K$ vs $K/2\pi$, sign of the kick) silently corrupt literature cross-checks; pin the 1.1 normalization in code and in the checker.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All existence and nonexistence claims via interval/ball arithmetic with directed rounding (Arb primary); Diophantine constants of $\gamma$ exact; extrapolated $K_c$ digits carry no certification and must be labeled non-rigorous wherever they appear, including tables and abstracts.
2. **Independent verification.** Standalone checkers, code-independent of the solvers: (a) a KAM certificate checker re-verifying the invariance-defect and condition inequalities from stored Fourier enclosures; (b) a converse-KAM checker re-propagating cones over the stored box cover; (c) a contraction-inequality checker for P4. Dual implementations (Arb-based and kv/C++-based) for (a) and (c).
3. **Reproducibility.** Fourier sizes, precisions, box-refinement schedules, extrapolation orders, PSLQ bases and budgets (pre-registered and timestamped before mining), tool versions, and a SHA-256 manifest over all certificates and logs.
4. **Preservation.** Solver and checker source; failed validation attempts (the $K$ values where the KAM step failed to close are scientifically informative and must be recorded); the complete PSLQ log including negatives.
5. **Honest reporting.** The report opens by stating that $K_c$ remains exactly undetermined (unless section 2 is met); the certified window is stated separately from extrapolated digits; no conjectural closed-form candidate appears anywhere without the word "conjectural" attached to it.
