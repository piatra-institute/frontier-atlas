# PROMPT FOR SHARP MODULAR-BOOTSTRAP BOUNDS ON THE 2D CFT SPECTRAL GAP

## Linear-programming bounds on the lowest primary dimension at general central charge

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 27 of 50 (Tier 3)
**Source:** top-50 list #48, category G (QFT and mathematical particle theory)
**Modes:** `[bound]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Modular invariance of the torus partition function constrains the spectrum of every unitary 2D CFT. The linear-programming (LP) bound on the lowest primary dimension $\Delta_1$ as a function of central charge $c$ is the cleanest such constraint: Hellerman's $c/6 + O(1)$ bound (2009) began the subject, numerics (Collier–Lin–Yin; Afkhami-Jeddi–Hartman–Tajdini) trace the LP frontier with an apparent asymptote near $c/9.1$, and Hartman–Mazáč–Rastelli (2019) solved the spinless problem exactly at $c = 4$ and $c = 12$ using the Viazovska-type magic functions that solved sphere packing in dimensions 8 and 24. At all other $c$ the exact LP value is unknown, and the asymptotic slope of the LP bound is unknown. This problem is matched to current AI methods because the LP dual is certificate-shaped: an exact functional with proven positivity is a rigorous theorem checkable by machine, and almost all published numbers in this area are floating-point and *not* rigorous - so even the reproduction tier produces publishable certified mathematics. The complete resolution defined in section 2 is the target; anything less is a partial result and must be reported as such.

## 1. Exact problem statement

### 1.1 Setup and normalizations

Consider a unitary 2D CFT with $c_L = c_R = c > 1$, a unique $sl(2)$-invariant vacuum, and a discrete spectrum of Virasoro primaries with total scaling dimensions $0 = \Delta_0 < \Delta_1 \le \Delta_2 \le \cdots$, $\Delta = h + \bar h$. Let $\tau$ be the torus modulus, $q = e^{2\pi i \tau}$, and

\[
Z(\tau,\bar\tau) = \mathrm{Tr}\, q^{L_0 - c/24}\, \bar q^{\bar L_0 - c/24},
\qquad Z(-1/\tau, -1/\bar\tau) = Z(\tau,\bar\tau).
\]

Two character systems are used, and every statement in this program must name which:

- **Variant V (Virasoro):** for $c > 1$, non-degenerate primary characters $\chi_h(\tau) = q^{h - (c-1)/24}/\eta(\tau)$ and vacuum character $\chi_{\mathrm{vac}}(\tau) = q^{-(c-1)/24}(1-q)/\eta(\tau)$.
- **Variant U ($U(1)^c$ / free-boson type):** characters $q^{h - c/24}/\eta(\tau)^{c}$. Variant U at central charge $c$ is exactly the LP sphere-packing problem in dimension $d = 2c$ (Hartman–Mazáč–Rastelli 2019).

Restrict to the spinless (S-invariance only) problem on $\tau = i\beta$, $\beta > 0$, with crossing $\beta \to 1/\beta$ about the self-dual point $\beta = 1$.

### 1.2 The LP bound

For odd-derivative functionals of order $\Lambda$,

\[
\omega \;=\; \sum_{\substack{k \le \Lambda,\ k \text{ odd}}} a_k\, (\beta\partial_\beta)^k \big|_{\beta = 1},
\qquad a_k \in \mathbb{R},
\]

define, for each variant,

\[
\Delta_\Lambda(c) \;=\; \inf\Bigl\{\, \Delta^* : \exists\, \omega\ \text{with}\ \omega[\text{vacuum}] > 0
\ \text{and}\ \omega[\chi_{h}\bar\chi_{\bar h}] \ge 0\ \ \forall\, \Delta = h + \bar h \ge \Delta^* \,\Bigr\},
\]

so that every CFT in the class satisfies $\Delta_1 \le \Delta_\Lambda(c)$. The functional space is finite-dimensional at fixed $\Lambda$, and $\Delta_\Lambda(c)$ decreases in $\Lambda$; define the LP bound

\[
\Delta_{\mathrm{LP}}(c) \;=\; \lim_{\Lambda \to \infty} \Delta_\Lambda(c).
\]

### 1.3 The open questions

1. **Exact values:** determine $\Delta_{\mathrm{LP}}(c)$ exactly at values of $c$ other than the solved points $c = 4$ and $c = 12$ (variant U; verify the exact variant of the HMR solved cases), by constructing extremal "magic" functionals with proven optimality (a matching primal spectrum or dual certificate).
2. **Sharp asymptotics:** determine $\lim_{c\to\infty} \Delta_{\mathrm{LP}}(c)/c$, or failing that, rigorous upper and lower bounds on $\limsup$ and $\liminf$ with explicit constants. The numerical asymptote is reported near $c/9.1$ (verify the current fitted value and its drift at very large $c$).

Informal targets - "improve the bound", "explain the kink" - are not acceptable statements of the problem.

## 2. Complete-resolution standard

Complete resolution is either of:

1. **A new exact point:** a closed-form $\Delta_{\mathrm{LP}}(c_0)$ at some $c_0 \notin \{4, 12\}$, established by an explicit extremal functional (proved positive, with proved sign pattern and vacuum normalization) together with a proof of optimality - either an explicit modular-invariant partition function saturating the bound, or a primal–dual matching argument. All positivity claims proved, not sampled.
2. **The asymptotic law:** a proof that $\Delta_{\mathrm{LP}}(c)/c \to \alpha$ with $\alpha$ exactly determined, for a named variant.

**Not accepted as resolution:**

- SDPB or any floating-point LP/SDP output, at any precision, presented as a bound on $\Delta_{\mathrm{LP}}$ or on CFT spectra (finite-precision duals are not certificates unless rounded to exact data whose positivity is then proved).
- Finite-$\Lambda$ rigorous bounds presented as the LP limit $\Delta_{\mathrm{LP}}(c)$.
- Fitted asymptotic slopes (e.g. "the bound tends to $c/9.1$") presented as theorems.
- "Kink at $c_0$ implies a CFT exists at $c_0$" or any existence claim about theories from LP data alone.
- Sphere-packing translations applied to variant V, where the $d = 2c$ dictionary does not literally hold.
- Bounds that silently drop the spin sum, the vacuum null structure (the $1-q$ factor), or degenerate characters.

## 3. Graded partial-result targets

### P1 - Analytic frontier reproduced

- Re-derive Hellerman's bound $\Delta_1 \le c/6 + O(1)$ with the explicit constant (verify $\approx 0.474$), fully symbolically, checking every inequality step in exact/interval arithmetic.
- Same treatment for the Friedan–Keller improvements (verify their constants).
- *Certificate:* machine-checked derivation notebook re-run from a clean environment.

### P2 - Certified finite-Λ LP bounds (the workhorse)

- For both variants and benchmark values $c \in \{2, 4, 8, 12, 16, 24, 36, 100\}$: rigorous theorems "$\Delta_1 \le B(c)$" via exact rational functional coefficients.
- Positivity on the entire ray $\Delta \ge \Delta^*$ (all spins) must be *proved*: reduced characters give $\omega[\chi] = P(\Delta)\, e^{-2\pi\Delta}$-type expressions with coefficients in $\mathbb{Q}[\pi]$; prove $P \ge 0$ by Sturm sequences / sign-definite decompositions with $\pi$ enclosed in a rational interval, plus an explicit tail bound from the leading coefficient.
- Control: at $c = 4, 12$ the certified bounds must bracket the exact values $1$ and $2$.
- *Certificate:* exact functional data (JSON) plus a standalone checker; this tier alone exceeds standard practice, which is floating-point.

### P3 - Saturation scan

- High-precision extremal functionals and extremal spectra across $c \in (1, 30]$ on a fine grid.
- PSLQ / inverse-symbolic tests of extremal-spectrum data for rational or quadratic-irrational collapse; the known kinks at $c = 4, 12$ must re-emerge as a control.
- Output: dossier of candidate special $c$ values ranked by evidence.
- *Certificate:* data release with precision statements; exploratory tier, labeled as such.

### P4 - Magic-function attempts with certified outcomes

- At the strongest P3 candidates, set up the Viazovska-type ansatz (Laplace transforms of weakly holomorphic/quasimodular forms with prescribed poles) as a finite-dimensional exact linear problem.
- Outcome A: a new exact extremal functional (then feed section 2).
- Outcome B: a certified nonexistence statement for that precisely-defined ansatz space (exact linear algebra, Farkas-style infeasibility certificate) - a real result, reported as scoped to the ansatz.
- *Certificate:* the exact linear system, its solution or infeasibility certificate, and an independent checker.

### P5 - Spinning and charged variants

- Certified finite-$\Lambda$ bounds with spin refinement and with $U(1)$-charge (current) constraints, benchmark grid as in P2 (setups as in Collier–Lin–Yin; Bae–Lee–Song (verify)).
- *Certificate:* as P2.

### P6 - Asymptotic theorems

- Rigorous bounds $\alpha_- \le \liminf_c \Delta_{\mathrm{LP}}(c)/c \le \limsup_c \Delta_{\mathrm{LP}}(c)/c \le \alpha_+$ for variant U, by translating sphere-packing LP asymptotics (Kabatiansky–Levenshtein upper side; Cohn–Elkies/Cohn–Zhao; dual-LP lower bounds à la Cohn–de Courcy-Ireland (verify)), with the dictionary proved rather than cited.
- Whatever transfers to variant V proved separately, or the failure of transfer documented.
- *Certificate:* theorem with explicit constants.

### P7 - Strongest short of resolution

- A new exact $\Delta_{\mathrm{LP}}(c_0)$ with optimality proof, or the exact asymptotic slope - i.e., the section-2 standard at one point.

## 4. Known results and prior art

- Cardy 1986: asymptotic spectral density from modular invariance (background).
- Hellerman 2009: $\Delta_1 \le c/6 + O(1)$ with explicit constant (verify value $\approx 0.4737$).
- Friedan–Keller 2013: higher-derivative LP improvements at large $c$.
- Qualls–Shapere ~2013: related bounds (verify scope).
- Collier–Lin–Yin ~2016–2018: systematic numerics, spin-refined bounds, kinks at $c = 4, 12$.
- Afkhami-Jeddi–Hartman–Tajdini 2019: large-$c$ LP numerics; reported slope near $c/9.08$ (verify).
- Hartman–Mazáč–Rastelli 2019: exact spinless solutions at $c = 4$ and $c = 12$ via magic functions; identification of the $U(1)^c$ problem with LP sphere packing in $d = 2c$; builds on Viazovska 2016 ($d=8$) and Cohn–Kumar–Miller–Radchenko–Viazovska 2016 ($d=24$).
- Mazáč 2016; Mazáč–Paulos ~2018: analytic extremal functionals, the functional-basis technology.
- Afkhami-Jeddi–Cohn–Hartman–de Laat–Tajdini ~2020: high-dimensional sphere packing vs modular bootstrap numerics (verify their large-$c$ slope data).
- Sphere-packing LP rigor: Cohn–Elkies 2003; Kabatiansky–Levenshtein 1978; Cohn–Zhao 2014; dual/impossibility bounds for LP (Cohn–de Courcy-Ireland, ~2019 (verify)).
- SDPB: Simmons-Duffin 2015 (v2: Landry–Simmons-Duffin ~2019) - arbitrary-precision SDP solver, non-certified output.

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

Mode `[bound]`: every deliverable is an inequality with a certificate.

1. **Exact character layer.**
   - Implement reduced characters at $\tau = i$: strip $\eta$ factors so functional entries become $P_k(\Delta)\, e^{-2\pi(\Delta - \xi_c)}$ with $P_k \in \mathbb{Q}[\pi][\Delta]$.
   - The only transcendentals are then powers of $\pi$ (and $\Gamma(1/4)$ via $\eta(i) = \Gamma(1/4)/(2\pi^{3/4})$ if kept explicit - prefer formulations where it cancels).
   - SageMath/SymPy for the symbolic layer; Arb (python-flint) for ball enclosures of $\pi$-polynomials.
2. **Exploration.** SDPB, or an mpmath simplex at 200–600 digits, to locate near-extremal functionals and the bisection window in $\Delta^*$; derivative order $\Lambda \lesssim 101$ is workstation-feasible.
3. **Certification (P2).**
   - Round the floating dual to nearby rationals (LLL-assisted denominators).
   - Prove $\omega[\text{vac}] > 0$ by ball arithmetic; prove $P(\Delta) \ge 0$ on $[\Delta^*, \infty)$ by Sturm sequences over $\mathbb{Q}$ after interval-enclosing the $\pi$-dependent coefficients, subdividing the $\pi$ interval until every sign decision closes; tail from the leading coefficient.
   - Independent checker in C++ with a different interval library (MPFI or kv) re-verifies every certificate.
4. **Exact LP (alternative path).** QSopt_ex / SoPlex-exact, or a fractions-based simplex, on a discretized constraint set - the discretization is exploration; only the whole-ray positivity proof certifies.
5. **Magic-function ansatz (P4).** Pari/GP and SageMath modular-forms machinery for the ansatz spaces; exact linear algebra in FLINT/IML; the ansatz-space definition ships inside the artifact.

Expected failure modes: ill-conditioning of the derivative basis at large $\Lambda$ (use orthogonalized functional bases); forgetting that positivity must hold for *all* $(h,\bar h)$ with $h + \bar h = \Delta$, not just spin zero (in variant V the spinless reduction must be justified or the spin dependence bounded); rational rounding destroying feasibility (re-solve locally with margin); claiming the $\Lambda \to \infty$ limit from finite-$\Lambda$ data; sign errors in the $(1-q)$ vacuum-null factor, which silently invalidate every downstream number.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All certified bounds rest on exact rational functional data plus interval enclosures with directed rounding (Arb); SDPB/floating output is exploration only and labeled so in every table.
2. **Independent verification.** Each positivity certificate is re-checked by a standalone C++ checker (different interval library, no shared code); Sturm-sequence computations re-run in two CAS (SageMath, Pari/GP).
3. **Reproducibility.** Pinned versions of SDPB, FLINT/Arb, SageMath, Pari/GP; all functional data, bisection logs, and precision parameters archived; SHA-256 manifest over certificates and spectra data.
4. **Preservation.** Failed rounding attempts, infeasible ansatz spaces, and abandoned $c$-scan regions preserved and indexed; nothing silently dropped.
5. **Honest reporting.** Every reported number carries one of three labels - (finite-$\Lambda$, certified), (numerical, extrapolated), (exact, proved) - and the final report states up front whether the section-2 standard was met, with the strongest achieved tier named explicitly.
