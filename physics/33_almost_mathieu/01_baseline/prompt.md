# PROMPT FOR DETERMINING THE FRACTAL DIMENSION OF THE CRITICAL ALMOST-MATHIEU SPECTRUM

## The Hofstadter butterfly at $\lambda = 1$: is the dimension $1/2$ at golden-mean frequencies?

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 33 of 50 (Tier 3)
**Source:** top-50 list #14, category B (rigorous many-body and condensed matter)
**Modes:** `[proof]` `[sym]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The critical almost-Mathieu operator - the Harper model at coupling $\lambda = 1$, whose spectra over rational frequencies draw the Hofstadter butterfly - has a spectrum of zero Lebesgue measure for every irrational frequency, and the physics tradition (Thouless scaling; Wilkinson–Austin numerics) predicts that at golden-mean-type frequencies its box and Hausdorff dimensions equal $1/2$. Rigorously: the upper bound $\dim_H \le 1/2$ is known (Jitomirskaya–Krasovsky - verify exact statement and frequency scope), the dimension collapses to $0$ for exceptional Liouville-type frequencies (Last–Shamis), and matching lower bounds are the open front. The problem is unusually machine-adjacent: for every rational approximant $p/q$ the spectrum is a union of $q$ bands determined through an exact integer-coefficient discriminant polynomial (Chambers' formula), and Hausdorff continuity of spectra in the frequency (Avron–van Mouche–Simon) converts certified band data into rigorous covers of the irrational spectrum - certified covers give certified dimension bounds. Adjacent payoff: moiré materials and magnetic Bloch bands. The complete resolution defined in section 2 is the target, and anything less must be reported as a partial result, never represented as a solution. The lower bound is genuinely hard; the graded targets are the realistic product.

## 1. Exact problem statement

On $\ell^2(\mathbb{Z})$ define the almost-Mathieu operator (AMO)

\[
(H_{\lambda,\alpha,\theta}\,\psi)(n) \;=\; \psi(n+1) + \psi(n-1) + 2\lambda\cos\!\big(2\pi(\theta + n\alpha)\big)\,\psi(n),
\]

with coupling $\lambda \in \mathbb{R}$, frequency $\alpha \in \mathbb{R}\setminus\mathbb{Q}$, phase $\theta \in \mathbb{T}$. For irrational $\alpha$ the spectrum $\Sigma_{\lambda,\alpha} = \sigma(H_{\lambda,\alpha,\theta})$ is a compact, $\theta$-independent subset of $\mathbb{R}$. This prompt fixes the critical coupling $\lambda = 1$ and writes $\Sigma_\alpha = \Sigma_{1,\alpha}$.

Frequencies: the golden mean $\alpha_g = (\sqrt5 - 1)/2$, continued-fraction convergents $p_n/q_n = F_{n-1}/F_n$ (Fibonacci numbers); more generally, bounded-type $\alpha$ (bounded partial quotients).

Dimensions, fixed explicitly. For compact $K \subset \mathbb{R}$ and $\epsilon > 0$ let $N(K, \epsilon)$ be the minimal number of $\epsilon$-intervals covering $K$; then

\[
\overline{\dim}_B(K) = \limsup_{\epsilon \to 0} \frac{\log N(K,\epsilon)}{\log(1/\epsilon)},
\qquad
\underline{\dim}_B(K) = \liminf_{\epsilon \to 0} \frac{\log N(K,\epsilon)}{\log(1/\epsilon)},
\]

and $\dim_H$ is Hausdorff dimension, with $\dim_H \le \underline{\dim}_B \le \overline{\dim}_B$ always.

**Target theorem (critical dimension).** For $\alpha = \alpha_g$ (strong form: all bounded-type $\alpha$):

\[
\dim_H(\Sigma_{\alpha}) \;=\; \overline{\dim}_B(\Sigma_{\alpha}) \;=\; \tfrac12 .
\]

Given the known upper bound $\dim_H \le 1/2$ (verify scope; whether a matching *box*-dimension upper bound is published must also be verified), the live content is the lower bound $\dim_H(\Sigma_{\alpha_g}) \ge 1/2$. A proof of $\underline{\dim}_B \ge 1/2$ is a distinct and weaker-but-major statement - box dimension dominates Hausdorff dimension, so box lower bounds do not imply the Hausdorff statement; the two must never be conflated in any artifact.

Machinery to be used exactly, hence stated exactly.

- **Rational spectra.** For $\alpha = p/q$, $\gcd(p, q) = 1$, the union over $\theta$ of the spectra, $\Sigma_{p/q} = \bigcup_\theta \sigma(H_{1,p/q,\theta})$, is determined by the discriminant of the $q$-step transfer cocycle: there is a monic-normalizable polynomial $\Delta_{p/q}(E)$ of degree $q$ with integer coefficients at $\lambda = 1$, and Chambers' formula isolates the $\theta$-dependence as an additive $2\cos(2\pi q\theta)$ term (derive and fix the exact normalization in-session before any computation), so that

\[
\Sigma_{p/q} \;=\; \big\{ E \in \mathbb{R} \;:\; \Delta_{p/q}(E) \in [-4,\, 4] \big\}
\quad\text{(window to be fixed with the normalization)},
\]

a union of $q$ closed bands, disjoint except possibly for a central touching at even $q$.

- **Continuity bridge.** Hausdorff continuity in frequency (Avron–van Mouche–Simon 1990): for all $\alpha, \alpha'$,

\[
d_H\big(\Sigma_{\lambda,\alpha},\, \Sigma_{\lambda,\alpha'}\big) \;\le\; C_\lambda\, |\alpha - \alpha'|^{1/2},
\qquad C_\lambda \le 6\,(2\lambda)^{1/2} \ \text{(verify constant and hypotheses)}.
\]

Consequently the $q_n$-band systems at convergents, inflated by $C\,|\alpha_g - p_n/q_n|^{1/2} = O(q_n^{-1})$ at bounded type, are explicit covers of $\Sigma_{\alpha_g}$, and every band of the approximant contains points within the inflation distance of $\Sigma_{\alpha_g}$: the two-way bridge from certified polynomial root isolation to rigorous dimension bounds.

## 2. Complete-resolution standard

A complete resolution is a proof of the Target theorem for $\alpha_g$ at minimum - both Hausdorff and box dimensions equal to $1/2$ - with full proofs of every analytic ingredient; every computational ingredient (band widths, cover cardinalities, mass distributions) certified in exact integer/rational or interval arithmetic with independent checkers. A proof for all bounded-type frequencies is the strong form. A certified disproof - $\dim_H(\Sigma_{\alpha_g}) \ne 1/2$ - equally counts as resolution.

**Not accepted as resolution:**

- Numerical box-counting or multifractal estimates of the butterfly at any depth (these exist since the 1980s and prove nothing).
- Finite-scale certified covers presented as dimension statements without a proved all-scales mechanism: a certified cover at scale $q_{40}$ bounds nothing about the dimension by itself; only an inductive scheme uniform in $n$ does.
- Results for $\lambda \ne 1$ (the subcritical and supercritical AMO dimension theory is a different, largely settled world) passed off as critical results.
- Almost-every-$\alpha$ statements presented as covering $\alpha_g$: a.e. results say nothing about a specific bounded-type frequency, and bounded type is itself a measure-zero class.
- The known upper bound $\le 1/2$, restated in any packaging, as progress on the lower bound.
- Heuristic Thouless-scaling or renormalization pictures without rigorous error control.
- Results about the Fibonacci Hamiltonian (the discontinuous-potential cousin, where dimension theory IS well developed) passed off as AMO results - the models are spectrally very different; the Fibonacci literature is method inspiration only.

## 3. Graded partial-result targets

Ordered from most accessible to strongest short of resolution; each is independently valuable and certifiable, and none depends on a later one succeeding.

**P1 - Exact discriminants and certified band data at Fibonacci convergents.**
- Task: compute $\Delta_{p_n/q_n}(E)$ exactly (integer coefficients; symbolic transfer products or the Chambers route) for $q_n$ up to at least $F_{20} = 6765$; isolate all band edges as certified real algebraic numbers (Arb/FLINT root isolation on integer polynomials); tabulate certified total bandwidth $|\Sigma_{p_n/q_n}|$, individual band widths, and gaps.
- Certificate: integer polynomial files, interval root enclosures, and an independent checker re-verifying sign changes in pure integer arithmetic.
- Value: reproduces and extends the known frontier with a verified toolchain; the scaling table $q_n\,|\Sigma_{p_n/q_n}|$ tests the Thouless constant (limit $\approx 32\,C_{\mathrm{Cat}}/\pi$, $C_{\mathrm{Cat}}$ Catalan's constant - verify before citing) with certified numbers for the first time.

**P2 - Certified upper bounds on box dimension via AvMS covers.**
- Task: prove the cover lemma (bands of $\Sigma_{p_n/q_n}$ inflated by $C|\alpha_g - p_n/q_n|^{1/2}$ cover $\Sigma_{\alpha_g}$); combine with P1 data into certified cover cardinalities $N(\epsilon_n)$; then upgrade to a genuine dimension bound via an inductive band-splitting estimate - how the $q_{n+1}$-bands sit inside inflated $q_n$-bands, machine-verified per level, proved uniform if the pattern is certified symbolically - yielding an unconditional $\overline{\dim}_B(\Sigma_{\alpha_g}) \le d^*$ with explicit $d^*$.
- Certificate: the cover lemma and induction proved; interval manifest for all counts.
- Value: any certified $d^* < 1$ validates the method; $d^*$ near $1/2$ benchmarks it against the Jitomirskaya–Krasovsky bound and may give the first *box*-dimension upper bound if none is published (verify).

**P3 - Certified packing data and a lower box-dimension bound.**
- Task: use the lower direction of AvMS - every point of $\Sigma_{p_n/q_n}$ lies within the inflation distance of $\Sigma_{\alpha_g}$ - so bands separated by more than twice the inflation force distinct points of $\Sigma_{\alpha_g}$; certified gap data give certified packing numbers $P(\epsilon_n)$. Upgrade to all scales via the inductive structure (exact renormalization of the discriminant/trace recursion at Fibonacci convergents, `[sym]`), yielding an unconditional $\underline{\dim}_B(\Sigma_{\alpha_g}) \ge d_* > 0$.
- Certificate: proofs plus interval manifest; the induction step certified symbolically or proved by hand.
- Value: to our knowledge no positive rigorous lower bound on the critical dimension at $\alpha_g$ is published (verify carefully - this is the novelty check gating the whole prompt); even $d_* = 0.1$ would be publishable.

**P4 - Mass-distribution upgrade: Hausdorff lower bound.**
- Task: upgrade P3 to $\dim_H$ via the mass distribution principle: construct a probability measure on a certified nested-band Cantor scheme with certified branching numbers and diameter ratios at every level; the Frostman exponent is then computable from certified combinatorics.
- Certificate: the nested-scheme theorem with all ratios certified; the measure construction proved.
- Value: the strongest realistic target short of resolution; $d_* \to 1/2$ here closes the problem.

**P5 - Frequency families and symbolic renormalization.**
- Task: extend P1–P4 to metallic means $\alpha = [\,0; \overline{m}\,]$ and quantify how certified bounds depend on the partial-quotient bound; derive the exact evolution of the discriminant under $q_n \to q_{n+1}$ at $\lambda = 1$ (the AMO trace evolution must be derived, not borrowed from the Fibonacci-Hamiltonian trace map $x_{n+1} = x_n x_{n-1} - x_{n-2}$, which belongs to a different model - verify and keep the two rigorously separated); hunt for certifiable invariant structures.
- Certificate: CAS derivations exported as proofs; any uniform-in-$n$ certified statement.
- Value: turns the finite-scale patterns of P2/P3 into candidate induction hypotheses; the family view separates golden-mean accidents from bounded-type mechanisms.

**P6 - Conditional closure of the $1/2$ lower bound.**
- Task: strongest short of resolution - a proved theorem "if the certified renormalization quantity $R_n$ satisfies inequality $I$ for all $n \ge n_0$, then $\dim_H(\Sigma_{\alpha_g}) \ge 1/2$", with $I$ machine-checked for all $n \le N$ and the remaining induction step stated precisely as the open analytic input.
- Certificate: the conditional theorem plus the finite verification manifest.
- Value: reduces the conjecture to one named inequality; the sharpest possible handoff to analysts.

## 4. Known results and prior art

- Hofstadter (1976): the butterfly. Aubry–André (1980): duality at $\lambda = 1$; total-bandwidth conjecture.
- Bellissard–Simon (1982); Bellissard's gap-labelling program (1980s–90s): K-theory labels for the butterfly's gaps - the structural backbone behind the band combinatorics P2/P3 exploit.
- Thouless (1983, 1990): total-bandwidth scaling $\sim c/q$ at criticality and the Catalan-constant limit (verify the exact constant); scaling arguments for dimension $1/2$.
- Wilkinson–Austin (c. 1990s): renormalization analysis and numerics giving dimension $\approx 0.5$ at golden mean (verify claimed values).
- Avron–van Mouche–Simon (1990): $\tfrac12$-Hölder continuity of spectra in $\alpha$ - the load-bearing bridge (verify constant $6(2\lambda)^{1/2}$ and hypotheses); total bandwidth continuity.
- Last (1993–94): zero-measure critical spectrum for a.e. $\alpha$; quantitative bandwidth bounds at rational approximants.
- Avila–Krikorian (2006): zero measure for the remaining frequencies - combined with Last: $|\Sigma_\alpha| = 0$ for all irrational $\alpha$ at $\lambda = 1$ (verify that the union of scopes is truly all irrationals).
- Last–Shamis (c. 2016): frequencies with $\dim_H(\Sigma_\alpha) = 0$ exist - dimension is not universal in $\alpha$; all theorems must be frequency-specific.
- Jitomirskaya–Krasovsky (c. 2019–2022): $\dim_H(\Sigma_\alpha) \le 1/2$ (verify the exact published statement, its frequency scope, and whether any box-dimension statement is included).
- Helffer–Sjöstrand (late 1980s): semiclassical renormalization of the Harper butterfly for a class of frequencies - the deepest structural analysis available; mine it for P5.
- Avila–Jitomirskaya (2009), Ten Martini theorem; Avila's global theory (c. 2015): context for why $\lambda = 1$ is the critical boundary case.
- Becker and collaborators (c. 2022+): magic-angle and moiré spectral theory using butterfly technology (adjacent payoff; verify).
- Methodological analogue: Damanik–Embree–Gorodetski–Tcheremchantsev (c. 2008) and successors proved two-sided fractal-dimension bounds for the *Fibonacci Hamiltonian* via trace-map dynamics - the proof architecture (hyperbolicity of a renormalization map controlling band combinatorics) is the template P5 should try to transplant, with the caveat of the "Not accepted" list.
- Lower bounds at criticality: as of last review we know of no published positive lower bound for $\dim(\Sigma_{\alpha_g})$ - verify carefully; the novelty of P3/P4 hinges on it.

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

Modes `[proof]` `[sym]`. Single-workstation first computations.

1. **Exact discriminant pipeline (Julia/FLINT or C++/FLINT).** Build $\Delta_{p/q}(E)$ by exact polynomial transfer products over $\mathbb{Z}[E]$ (FLINT `fmpz_poly`; cost near-linear in $q$ with FFT multiplication, memory the binding constraint; $q \sim 10^4$ feasible). Verify the Chambers structure symbolically for small $q$ (SymPy) before trusting the general derivation; a normalization error here poisons everything downstream.
2. **Certified root isolation (Arb).** Band edges are real roots of the integer polynomials $\Delta_{p/q}(E) \mp 4$: isolate all with certified intervals; band widths and gaps as certified differences. Independent checker: exact sign evaluation of the integer polynomial at rational points bracketing each root - pure integer arithmetic, the strongest possible check, no intervals involved.
3. **Cover/packing ledger.** A small verified program consuming certified band data plus the AvMS constant (carried as an exact rational upper bound), emitting $N(\epsilon)$ and $P(\epsilon)$ tables with directed comparisons: covers rounded up, packings rounded down.
4. **Symbolic renormalization (`[sym]`).** Derive the exact recursion of $\Delta_{p_n/q_n}$ along Fibonacci convergents at $\lambda = 1$; compute exactly, per level, which $q_{n+1}$-bands lie inside which inflated $q_n$-bands; search for an eventually-periodic inclusion pattern certifiable by symbolic induction. Expected failure mode: the pattern is only approximately periodic and the induction needs an analytic input - in that case identify the input precisely and record it as the P6 hypothesis rather than papering over it.
5. **Expected failure modes, global.** Integer-coefficient blowup beyond $q \sim 10^4$ (mitigate: certified interval-Chebyshev representations, at the price of losing the pure-integer checker - document the trade); the AvMS inflation swamping band scales if convergent denominators grow too slowly (not an issue at golden mean - quantify the margin); box/Hausdorff conflation in write-ups (terminology check mandated in the report template).
6. **What runs where.** Everything above is single-workstation. The deep regime $q \gtrsim 10^5$ matters only if the P1 scaling table shows drifting constants; do not go there first.
7. **Order of battle.** Normalization derivation (SymPy, small $q$, cross-checked against direct matrix spectra of $H_{1,p/q,\theta}$ on $\theta$-grids in interval arithmetic) before any large-$q$ run; P1 complete before the cover/packing ledger consumes it; the P5 recursion work starts only after P2/P3 finite-scale patterns indicate what to look for.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Discriminants over $\mathbb{Z}[E]$; all band edges as certified enclosures rooted in integer polynomials; all dimension-relevant comparisons in directed interval arithmetic; the AvMS constant as an exact rational bound with its proof cited and re-checked.
2. **Independent verification.** Dual checkers for every band edge - interval (Arb) and pure-integer sign bracketing; independent reimplementation of the cover/packing counters (Python) against the primary (Julia/C++); the symbolic recursion re-derived in a second CAS.
3. **Reproducibility.** All $p/q$, polynomial files, precision settings, and library versions recorded; SHA-256 manifest over polynomials, root enclosures, cover/packing tables, and CAS notebooks.
4. **Preservation.** The symbolic derivation notebooks (Chambers normalization, recursion derivations) carry the correctness of everything downstream and are first-class artifacts; failed renormalization ansätze are preserved as negative results; anything unpreserved is declared.
5. **Honest reporting.** The report opens by stating whether the Target theorem was proved (expected: no), then lists which of P1–P6 reached certificate standard, every unconditional dimension bound obtained with box vs. Hausdorff labeled scrupulously, and the precise analytic statement still missing for the $1/2$ lower bound. Finite-scale data are never described as dimension results.
