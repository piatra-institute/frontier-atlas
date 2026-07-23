# PROMPT FOR A CERTIFIED OPTIMAL SMALL MAGIC-STATE DISTILLATION PROTOCOL

## Minimum-overhead distillation of \(|T\rangle\) or \(|\mathrm{CCZ}\rangle\) - yield vs error-suppression vs qubit cost

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 40 of 50
**Area:** quantum computation & codes
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

A fault-tolerant quantum computer implements Clifford gates cheaply but needs a supply of **magic states** - \(|T\rangle\), \(|\mathrm{CCZ}\rangle\), \(|\mathrm{CS}\rangle\) - distilled from noisy copies through Clifford circuits and measurement. Distillation is the single largest qubit- and time-cost in most resource estimates, so the optimization of small distillation routines - how many noisy inputs, how many rounds, what error-suppression exponent, at what qubit footprint - is of direct hardware consequence. The problem is concrete: for a fixed input/output count \((n \to k)\), determine the best achievable error-suppression order and yield, and produce a protocol that attains it together with a checked figure of merit. The theory is combinatorial and exact: distillation protocols come from **triorthogonal** and more general codes (Bravyi–Haah), whose defining conditions are \(\mathbb{F}_2\) parity constraints checkable exactly, and whose output error polynomial is a finite polynomial in the input error rate computable symbolically. So the trade-off is machine-certifiable - the output infidelity polynomial, the acceptance probability, and the overhead exponent \(\gamma\) are exact rational/symbolic quantities - and the optimum over small codes is a finite (if large) search amenable to SAT/ILP and exhaustive \(\mathbb{F}_2\) enumeration. The verifier is exact: recompute the triorthogonality conditions and the output error polynomial symbolically, and confirm the claimed figure of merit. Anything short of the section-2 standard - a Monte-Carlo-estimated infidelity, a protocol with no matching optimality argument, an asymptotic overhead claim - is a partial result, never a solution.

## 1. Exact problem statement

A **magic state** is a single- (or multi-) qubit non-stabilizer state, e.g.

\[
|T\rangle \;=\; T|+\rangle \;=\; \tfrac{1}{\sqrt2}\big(|0\rangle + e^{i\pi/4}|1\rangle\big),
\qquad
|\mathrm{CCZ}\rangle \;=\; \mathrm{CCZ}\,|{+}{+}{+}\rangle .
\]

A **distillation protocol** takes \(n\) noisy copies (each afflicted, in the standard model, by a stochastic Pauli error of rate \(p\) after twirling to the relevant channel) and, via a Clifford circuit plus stabilizer measurements with post-selection on the trivial syndrome, outputs \(k\) copies of higher fidelity. Two figures characterize it.

- **Error suppression.** The output error rate is

  \[
  p_{\mathrm{out}} \;=\; c\, p^{\,d} + O(p^{\,d+1}),
  \]

  where \(d\) is the **distance** of the underlying code (the leading exponent) and \(c\) is an exact combinatorial coefficient (a count of low-weight logical-error configurations).

- **Overhead.** With acceptance probability \(P_{\mathrm{acc}}\), the cost per output scales with \(n/k\) and the rounds needed to reach a target error; the standard scale-invariant figure is

  \[
  \gamma \;=\; \frac{\log(n/k)}{\log d},
  \]

  the number of raw states consumed per output scaling as \(1/\varepsilon^{\gamma}\) to reach output error \(\varepsilon\).

**Triorthogonal construction (Bravyi–Haah).** A binary \(m \times n\) matrix \(G\) is **triorthogonal** if

\[
\sum_{i} G_{ai} G_{bi} \equiv 0
\quad\text{and}\quad
\sum_{i} G_{ai} G_{bi} G_{ci} \equiv 0
\pmod 2
\qquad\text{for all distinct } a,b,c .
\]

Splitting the rows into "logical" and "stabilizer" classes yields a \([[n,k,d]]\) CSS code that distills \(|T\rangle\) with the error-suppression order above. The canonical example is the \([[15,1,3]]\) Reed–Muller routine, whose exact output error rate under the twirled model is

\[
p_{\mathrm{out}} \;=\; 35\, p^{3} + O(p^{4}),
\qquad
n = 15,\ k = 1,\ d = 3,
\qquad
\gamma = \frac{\log 15}{\log 3} \approx 2.46 ,
\]

a value every implementation of the section-5 core must reproduce symbolically before any new protocol is trusted.

The cost measures are the pair \((n,k)\), the suppression exponent \(d\), the leading coefficient \(c\), the acceptance probability \(P_{\mathrm{acc}}(p)\), and \(\gamma\). The target state (\(|T\rangle\), \(|\mathrm{CCZ}\rangle\), \(|\mathrm{CS}\rangle\)) and the noise model (twirled Pauli / stochastic) are declared per claim. The open problem, per regime: **for fixed \((n,k)\) or fixed \(d\), find the protocol optimizing the declared figure of merit and prove no small protocol in the class does better.** Start from this prompt alone - the state, the suppression/overhead definitions, and triorthogonality are all fixed above.

## 2. Resolution standard

Fix a class (e.g. triorthogonal \([[n,k,d]]\) \(|T\rangle\)-distillation, twirled model) and a figure of merit (minimize \(\gamma\); or maximize \(d\) at fixed \((n,k)\); or minimize \(n\) at fixed \((k,d)\)). Resolution is a pair:

1. an explicit protocol - the triorthogonal matrix \(G\) (or the code + Clifford circuit + measurement / post-selection) - with its output error polynomial and \((n,k,d,c,P_{\mathrm{acc}},\gamma)\) computed exactly; and

2. a proof that no protocol in the declared class beats it on the declared figure of merit.

**Named certified form.** One of:

- **Exhaustive \(\mathbb{F}_2\) optimality.** A complete enumeration (up to the relevant equivalence, with a stated canonicity rule) of triorthogonal matrices of the given shape, showing none achieves a better figure of merit; the winning protocol's triorthogonality and error polynomial recomputed by an independent checker.

- **SAT/ILP optimality with a proof.** Encode "a triorthogonal \([[n,k,d]]\) code with figure of merit better than \(M\) exists" as CNF/ILP over the \(\mathbb{F}_2\) parity constraints; obtain UNSAT with a DRAT/LRAT proof (or ILP infeasibility with an exact certificate), independently checked; the witness protocol verified separately.

- **Exact figure-of-merit improvement.** An explicit protocol whose exactly-computed \(\gamma\) (or \(d\) at fixed \((n,k)\), or footprint) strictly beats the cited best-known, with the output error polynomial and acceptance probability derived symbolically.

**Not accepted as resolution.**

- An output infidelity from **Monte-Carlo** sampling rather than the exact error polynomial.

- A protocol with a good figure of merit but **no optimality argument** within a declared class (an upper bound on quality, not a proof of optimality).

- A **numerically** verified triorthogonality (it must be exact \(\mathbb{F}_2\) parity checks).

- An **unreplayable** solver run, or an **incomplete** enumeration reported as optimality.

- An asymptotic overhead claim (e.g. "\(\gamma \to \log_2 3\)") presented as a specific small-protocol optimum.

- Comparing across different noise models or state types without declaring them.

## 3. Graded partial-result targets

- **P1 - Reproduce the classic routines.** Rebuild the \([[15,1,3]]\) Reed–Muller \(|T\rangle\)-distillation and the \([[5,1,3]]\)-based \(H\)-type routine; recompute their exact output polynomials \(p_{\mathrm{out}}(p)\), leading coefficients, and \(P_{\mathrm{acc}}\). Certificate: symbolic error polynomial + triorthogonality check.

- **P2 - The triorthogonal frontier, small \(n\).** Exhaustively enumerate triorthogonal matrices for small \((n,k)\) and tabulate the achievable \((d,c,\gamma)\); reproduce the known small-code trade-offs. Certificate: complete enumeration with a canonicity rule + replay.

- **P3 - Exact figure of merit for a family.** For a named family (e.g. the \([[3k+8,k,2]]\)-type Bravyi–Haah codes, verify), compute \(\gamma\) exactly and confirm the reported trade-off. Certificate: symbolic derivation + independent recomputation.

- **P4 - A certified small optimum.** For a fixed \((n,k)\) (or fixed \(d\)) at the edge of exhaustive feasibility, certify the optimal \(d\) / minimal \(n\) via complete \(\mathbb{F}_2\) enumeration or SAT/ILP infeasibility. Certificate: DRAT/LRAT UNSAT or complete search + exact witness.

- **P5 - An improved trade-off.** Produce a small \(|T\rangle\) or \(|\mathrm{CCZ}\rangle\) protocol strictly beating a cited best-known figure of merit at its \((n,k)\), fully certified in both the protocol and the exact figure. Certificate: complete manifest; both the error polynomial and the optimality/comparison independently checked.

- **P6 - Reusable analysis harness.** An audited tool that, given a triorthogonal \(G\) (or a code), emits the exact output error polynomial, \(P_{\mathrm{acc}}\), and \(\gamma\), validated against P1. Certificate: source + agreement with a second implementation on shared protocols.

## 4. Known results and prior art

- **Foundations.** Bravyi, Kitaev, *Universal quantum computation with ideal Clifford gates and noisy ancillas*, PRA (2005) - the \([[15,1,3]]\) Reed–Muller \(T\)-distillation and the \([[5,1,3]]\) \(H\)-type routine; the noisy-ancilla model.

- **Triorthogonality & low overhead.** Bravyi, Haah, *Magic-state distillation with low overhead*, PRA **86**, 052329 (2012) - triorthogonal codes; overhead \(\gamma = \log(n/k)/\log d\) approaching \(\log_2 3 \approx 1.585\).

- **Improved / generalized routines.** Reichardt (~2005, verify) improved distillation; Meier, Eastin, Knill small distillation codes (~2013, verify); Jones and Campbell–Howard *synthillation* / multilevel protocols (~2016, verify); Haah, Hastings, and collaborators, *Codes and protocols for distilling \(T\), controlled-\(S\), and Toffoli/CCZ* (~2018, verify) - generalized triorthogonality for CS and CCZ.

- **Footprint optimization.** Litinski, *Magic State Distillation: Not as Costly as You Think*, Quantum (2019) - space-time footprints of factories; Gidney–Fowler CCZ / \(T\) factory constructions (~2019, verify).

- **Constant overhead (asymptotic, adjacent).** Recent constant-overhead magic-state-distillation constructions (arXiv 2408.07764, 2024, verify) - asymptotic \(\gamma \to 0\), not small-protocol optima.

- **Reference.** The Error Correction Zoo lists magic-distillation codes and their yield parameters - a cross-check for figures of merit.

Status as of mid-2026 - re-verify against the current literature before starting any session.

## 5. Attack plan

`[search]`. One workstation.

1. **Symbolic error-polynomial core.** Given a triorthogonal \(G\) (or a CSS distillation code + circuit), compute \(p_{\mathrm{out}}(p)\) exactly as a polynomial in the input error rate (enumerate logical-error configurations weighted by input-error parity classes) and \(P_{\mathrm{acc}}(p)\); implement in SageMath with exact rational / polynomial arithmetic. Validate on \([[15,1,3]]\).

2. **Triorthogonality enumeration.** Encode the pairwise and triple parity conditions and sweep binary matrices of the target shape, reduced by a stated equivalence (row/column operations preserving triorthogonality); certify completeness for P2/P4.

3. **SAT/ILP optimality.** For "does a triorthogonal \([[n,k,d]]\) with figure of merit \(> M\) exist?", build CNF over the \(\mathbb{F}_2\) parity constraints; drive kissat/CaDiCaL/CryptoMiniSat with DRAT/LRAT logging; check with `drat-trim`/`lrat-check`. Mirror with an exact ILP for a second route.

4. **CCZ / CS generalization.** Extend the triorthogonality conditions to the generalized (weak-triorthogonal / CCZ) forms and recompute figures for those targets.

5. **Cross-check with tooling.** Verify the underlying CSS code parameters and distances with Stim / the quantum-code toolchain (problem 38), and cross-check factory footprints against Litinski's tabulated values where relevant.

6. **Failure modes.** Combinatorial blow-up of triorthogonal enumeration past modest \(n\); the error-polynomial derivation is subtle (twirling assumptions, post-selection conditioning) and a wrong model gives a wrong exponent; the Monte-Carlo temptation (never report a sampled infidelity as the certified polynomial); equivalence-reduction bugs breaking completeness; mixing state types or noise models. Declare the model in every claim.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Triorthogonality is checked by exact \(\mathbb{F}_2\) parity; output error polynomials and acceptance probabilities are exact symbolic / rational objects; optimality carries a DRAT/LRAT proof, an exact ILP certificate, or a complete canonical enumeration. Monte-Carlo is exploration only.

2. **Independent verification.** A standalone checker, separate from the search, that (a) re-verifies triorthogonality and recomputes \(p_{\mathrm{out}}(p)\), \(P_{\mathrm{acc}}\), and \(\gamma\) for the winning protocol, and (b) replays the optimality proof (a proof checker, a second solver, or a re-run enumeration). A second error-polynomial implementation.

3. **Reproducibility.** Every matrix \(G\), circuit, noise model, figure-of-merit definition, solver/CAS name+version, and equivalence rule recorded; SHA-256 manifest over protocols, polynomials, CNF/LP files, and proof traces; the cited best-known figure being matched or beaten given with source and access date.

4. **Preservation.** All enumeration, analysis, and search source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).

5. **Honest reporting.** The report states up front, per \((n,k)\) and model, whether the figure of merit is exact, whether optimality within a declared class was proved, and whether a best-known trade-off was strictly improved - never presenting a sampled infidelity, an asymptotic overhead, or a class-restricted optimum as more than it is.
