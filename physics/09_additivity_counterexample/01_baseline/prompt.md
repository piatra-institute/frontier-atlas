# PROMPT FOR AN EXPLICIT CERTIFIED COUNTEREXAMPLE TO ADDITIVITY OF MINIMUM OUTPUT ENTROPY

## Constructing a verifiable low-dimensional quantum channel pair violating $S_{\min}$ additivity

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 09 of 50 (Tier 1)
**Source:** top-50 list #4, category A (quantum information and foundations)
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Hastings proved in 2009 that the minimum output von Neumann entropy of quantum channels is not additive - and hence that the Holevo capacity is not additive - but the proof is probabilistic, lives in enormous dimensions, and to this day *no explicit channel pair violating additivity is known*. Producing one, with the violation certified by exact or interval arithmetic including a certified *global lower bound* on the single-copy minimum output entropy, would convert a cornerstone of quantum Shannon theory from an existence statement into an inspectable object and calibrate how small additivity violations can be made. The problem is search-shaped: explicitly parametrized channel families, a hard but finite-dimensional certification task per candidate, and a ladder of Rényi-$p$ warm-ups where explicit counterexamples already exist. The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

A quantum channel is a completely positive trace-preserving map $\Phi : \mathcal{B}(\mathbb{C}^{n}) \to \mathcal{B}(\mathbb{C}^{m})$, presented by Kraus operators $\{A_k\}$,

\[
\Phi(\rho) = \sum_k A_k \rho A_k^\dagger, \qquad \sum_k A_k^\dagger A_k = \mathbb{1},
\]

or by a Stinespring isometry $V : \mathbb{C}^n \to \mathbb{C}^m \otimes \mathbb{C}^e$ (environment dimension $e$). The von Neumann entropy is $S(\rho) = -\operatorname{Tr}\rho\log_2\rho$; base 2 throughout, and every artifact states its base. The **minimum output entropy** is

\[
S_{\min}(\Phi) \;=\; \min_{|\psi\rangle \in \mathbb{C}^n,\ \||\psi\rangle\|=1} S\big(\Phi(|\psi\rangle\langle\psi|)\big),
\]

the restriction to pure inputs being sufficient by concavity of $S$. For $p \ge 0$, $p \ne 1$, the Rényi variant uses

\[
S_p(\rho) = \frac{1}{1-p}\log_2 \operatorname{Tr}\rho^p ,
\]

giving $S_{p,\min}(\Phi)$; $p \to 1$ recovers $S_{\min}$. Additivity always holds as an inequality, $S_{\min}(\Phi \otimes \Psi) \le S_{\min}(\Phi) + S_{\min}(\Psi)$, by product inputs; the (disproved) additivity conjecture asserted equality.

**The problem: exhibit explicit channels $\Phi, \Psi$ - given by exact Kraus/Stinespring data over a stated number field, in dimensions small enough for certification (working target: input dimension at most a few hundred) - together with a certified proof that**

\[
S_{\min}(\Phi \otimes \Psi) \;<\; S_{\min}(\Phi) + S_{\min}(\Psi).
\]

Terms are fixed as follows:

- **Explicit** means deterministically specified: no random ensemble with positive-probability success, no machine-precision unitaries, no truncated decimals.
- **Certified** means: an upper bound on the left side via an explicit input state with interval-certified output entropy, and rigorous *global* lower bounds on $S_{\min}(\Phi)$ and $S_{\min}(\Psi)$ - the global-optimization certificate is the crux (section 5).
- The template $\Psi = \bar\Phi$ (entrywise conjugate channel) probed with a maximally entangled input is the recommended, not mandated, shape.
- The Rényi relatives ($p > 1$, and $p$ near 0) are in-scope warm-ups stated identically with $S_{p,\min}$; they are graded targets, not the resolution.

## 2. Complete-resolution standard

An explicit pair $(\Phi, \Psi)$ with exact defining data, plus a certificate package proving the strict inequality above for the von Neumann case $p = 1$, consisting of:

1. **Upper bound (left side).** An explicit input $|\Omega\rangle$ on the product input space, with $S\big((\Phi\otimes\Psi)(|\Omega\rangle\langle\Omega|)\big)$ enclosed by interval arithmetic with directed rounding - or evaluated exactly when the output spectrum is algebraic - giving $S_{\min}(\Phi\otimes\Psi) \le U$.
2. **Lower bounds (right side).** Certified global bounds $S_{\min}(\Phi) \ge L_\Phi$ and $S_{\min}(\Psi) \ge L_\Psi$ from a complete, replayable branch-and-bound (or SOS/SDP) certificate covering the entire pure-state input manifold, all bounds computed in interval arithmetic.
3. **Strictness with margin.** $U < L_\Phi + L_\Psi$ with an explicit certified gap $\delta > 0$; the whole chain checkable by an independent verifier from stored artifacts alone.

**Not accepted as resolution:**

- Random-ensemble arguments (Hastings-style), however sharpened - existence is already known; the problem is explicitness.
- A violation for Rényi $p \ne 1$, including new explicit $p > 1$ examples, presented as the resolution; these are graded targets P1, P4, P5.
- Floating-point estimates of $S_{\min}$ on either side; local optimization ("no lower output entropy was found") standing in for a global lower-bound certificate.
- A certified violation of Holevo-capacity additivity or another Shor-equivalent form is acceptable **only** if the equivalence is instantiated explicitly and certified end-to-end at the stated dimensions; hand-waved transfer through the equivalences is not.
- Channels specified by a random seed or by data that cannot be reproduced symbol-for-symbol.
- Asymptotic or infinite-dimensional constructions without a certified finite instance.

## 3. Graded partial-result targets

**P1 - Re-certify the explicit Werner–Holevo violation ($p > 4.79$).**
*Task:* the $d = 3$ Werner–Holevo channel $\Phi_{WH}(\rho) = \tfrac{1}{2}\left(\operatorname{Tr}(\rho)\,\mathbb{1} - \rho^{T}\right)$ violates multiplicativity of the maximal output $p$-norm for $\Phi_{WH}\otimes\Phi_{WH}$ when $p > 4.7823\ldots$ Reproduce with exact arithmetic: the product-channel output spectrum on the antisymmetric maximally entangled input is exactly computable, and the single-copy maximum is provable by the channel's covariance (re-derive the closed form).
*Certificate:* exact spectra, exact/interval inequality chain, independent checker.
*Effort:* days; validates the entire reporting pipeline on the one fully explicit landmark.

**P2 - Certified global $S_{\min}$ lower bounds for benchmark channels.**
*Task:* build the global-optimization certifier (section 5) and validate it where the answer is provable by hand: unital qubit channels, depolarizing channels, entanglement-breaking channels (additivity known - King, Shor). Target: certified two-sided enclosures of $S_{\min}$ for input dimensions up to ~20–50 with useful gap.
*Certificate:* branch-and-bound trees with per-leaf interval bounds, independently replayed.
*Value:* this tool is the load-bearing deliverable; without it, no resolution claim is even possible.
*Effort:* weeks; the certifier is the session's main engineering investment.

**P3 - Certified additivity-verification sweeps in low dimension.**
*Task:* for structured families (random-unitary channels with few Kraus terms, covariant channels), certify either a violation or $S_{\min}(\Phi\otimes\bar\Phi) \ge L$ with $L$ close to $2\,S_{\min}(\Phi)$, over a documented grid of channels.
*Certificate:* per-channel enclosure dossiers.
*Value:* certified *non*-violation windows convert folklore ("small dimensions look additive") into intervals and delimit where an explicit counterexample can live.
*Effort:* continuous background compute once P2 exists; report coverage honestly.

**P4 - Explicit Rényi violations at smaller $p$.**
*Task:* push the explicit-violation frontier from $p \approx 4.79$ toward $p = 1$: structured ansätze (group-covariant channels, antisymmetric projections, conjugate pairs) where representation theory collapses the single-copy maximization to a provable closed form while an entangled input beats the product bound. Also re-verify the known explicit counterexamples for $p$ near 0 (Cubitt–Harrow–Leung–Montanaro–Winter) (verify their degree of explicitness) as a second anchor.
*Certificate:* exact/interval inequality chains as in P1.
*Value:* any certified explicit violation at a new smaller $p$ - especially $p \le 2$ - is publishable.
*Effort:* the representation-theoretic case analysis is the bottleneck, not compute.

**P5 - Explicit violation for $p = 1 + \epsilon$.**
*Task:* an explicit pair and a certified violation of Rényi additivity for some fixed $p$ strictly between 1 and 2, with the full certificate structure of section 2 (integer-$p$ trace polynomials make certification friendlier; fractional $p$ via monotonicity sandwiches).
*Value:* the strongest realistic pre-resolution result and the direct template for $p = 1$.
*Effort:* attempt only after P4 has produced at least one certified violation below $p = 3$.

**P6 - Full resolution at $p = 1$** per section 2.

Honest calibration: the quantitative anatomy of Hastings' proof (Fukuda–King–Moser; Belinschi–Collins–Nechita) indicates that known-technique violations are tiny and live in very large dimensions; an explicit $p=1$ example may require genuinely new structure, not search alone. Expect P2–P4 as the session's real products.

## 4. Known results and prior art

- Additivity conjecture equivalences (Holevo capacity, entanglement of formation, strong superadditivity): Shor (2004).
- Additivity holds for special classes: unital qubit channels (King, 2002); depolarizing channels (King, 2003); entanglement-breaking channels (Shor, 2002).
- Explicit Rényi violation: Werner–Holevo channel, $d = 3$, multiplicativity of the maximal output $p$-norm fails for $p > 4.7823\ldots$ (Werner–Holevo, 2002).
- Random Rényi violations for all $p > 1$: Hayden–Winter (2008).
- Counterexamples for $p$ close to 0: Cubitt–Harrow–Leung–Montanaro–Winter (~2008) (verify explicitness).
- $p = 1$ disproof: Hastings (2009), random unitary channels $\Phi, \bar\Phi$ with maximally entangled input; violation size extremely small.
- Quantitative anatomy and dimension requirements of the random proof: Fukuda–King–Moser (~2010); Brandão–Horodecki (~2010); Aubrun–Szarek–Werner via Dvoretzky's theorem (~2010–2011); Belinschi–Collins–Nechita, free-probability sharpening with violations approaching one bit asymptotically (~2013–2016). No explicit instance has been extracted from any of these (verify - search specifically for post-2020 derandomization claims before starting).
- Certification context: interval branch-and-bound global optimization; Lasserre/SOS hierarchies for polynomial objectives - noting $S$ is not polynomial, while integer-$p$ Rényi surrogates are.

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

**The certifier (core tool).**

- Certified global lower bound for $S_{\min}(\Phi)$: branch-and-bound over the pure-input manifold $\mathbb{CP}^{n-1}$ (real chart decomposition), per-box interval enclosure of the output density matrix and its spectrum (Gershgorin and interval eigenvalue bounds), entropy bounds from spectral enclosures, plus certified derivative/Lipschitz pruning.
- Implementation: C++ with Arb/FLINT ball arithmetic; SymPy/SageMath for exact spectra of algebraic inputs.
- Feasible single-workstation scale: input dimension in the tens for full global certification; the product-channel side needs only an *upper* bound (one explicit input), cheap whenever the output spectrum (dimension $m^2$ or $me$-scale) can be enclosed.

**Rényi surrogates.**

- For integer $p \ge 2$, $\operatorname{Tr}\,\Phi(\psi)^p$ is a polynomial in the input coordinates: SOS/Lasserre moment relaxations (SDPA-GMP, rational rounding, exact $LDL^T$ verification) give certified global bounds without branch-and-bound.
- Use standard monotonicity/sandwich inequalities between Rényi entropies to transfer bounds toward $p = 1$ where they are strong enough.

**Ansatz search.**

- Covariant channels: irrep multiplicities collapse $S_{\min}$ to small explicit problems with provable symmetry lemmas (certify the symmetry reduction itself).
- Conjugate pairs $\Phi \otimes \bar\Phi$ with maximally entangled probe: the output has an exactly computable large eigenvalue contribution - exploit it for the upper bound.
- Few-Kraus random-unitary channels built from exact algebraic unitaries (finite-group representations), so every candidate is explicit by construction.
- Floating-point pre-screen at scale (millions of candidates); only survivors enter certification.

**Expected failure modes.**

- Curse of dimensionality in branch-and-bound above input dimension ~30: mitigate via covariance (certify on a fundamental domain with a proved symmetry lemma).
- Interval blowup near degenerate output spectra: higher-precision balls, cluster-robust eigenvalue enclosures.
- The substantive risk: violations at $p = 1$ may simply not exist at certifiable dimensions; P3 converts that outcome into certified non-violation windows rather than a null session.

**Anti-goal hygiene.**

- No claim ever rests on "the optimizer converged"; every reported number is an interval with stated radius, or exact.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Channel data exact (rational or algebraic entries, isometry conditions verified exactly); every certified inequality via ball arithmetic with directed rounding or exact algebraic computation, including rigorous enclosure of logarithms; floating point only in pre-screening.
2. **Independent verification.** A standalone verifier replays: (a) trace preservation/isometry of the channel data; (b) the upper-bound input's output-spectrum enclosure; (c) the complete branch-and-bound tree, every leaf's bound re-derived from the stored box description; implemented independently of the search code (Python/Arb bindings versus the C++ core). SOS certificates re-checked by exact rational PSD verification.
3. **Reproducibility.** Candidate-generation logs (including pre-screening seeds and ansatz parameters), certifier version and precision policies, and complete branch trees stored; SHA-256 manifest over channel data, trees, certificates, and code.
4. **Preservation.** The searcher, the certifier, all near-miss candidates with enclosures, and all certified non-violation windows preserved; anything not preserved is declared.
5. **Honest reporting.** The report opens with whether an explicit certified $p = 1$ violation was obtained (expected: no); states the smallest $p$ with an explicit certified violation and every certified enclosure with its radius; and never presents Rényi results, random-ensemble reasoning, or uncertified numerics as the resolution.
