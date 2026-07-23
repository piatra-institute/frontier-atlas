# PROMPT FOR THE STABILIZER RANK OF \(|T\rangle^{\otimes n}\)

## Minimum number of stabilizer states summing to \(n\) copies of the magic state

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 41 of 50
**Area:** quantum computation & codes
**Modes:** `[search]` `[opt]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The **stabilizer rank** \(\chi(|\psi\rangle)\) is the fewest stabilizer states whose linear combination equals \(|\psi\rangle\). For the magic state \(|T\rangle\), the rank of the tensor power \(\chi(|T\rangle^{\otimes n})\) directly governs the runtime of the best classical simulators of Clifford+\(T\) circuits: a circuit with \(n\) \(T\)-gates is simulable in time scaling with this rank, so every improvement to the exact value or its bounds is a statement about the classical hardness of quantum computation. The quantity is exact and finite for each \(n\) - a minimum over decompositions into stabilizer states, of which there are finitely many in each dimension - yet exact values are known only for tiny \(n\), with a super-polynomial gap between the best upper bounds (clever nested decompositions) and the best lower bounds (\(\Omega(n)\), Peleg–Shpilka–Volk). This is a sharp AI-for-mathematics target: an upper bound is an explicit finite decomposition whose correctness is an exact linear-algebra identity, and a lower bound (or an exact value) reduces to infeasibility of "fewer than \(r\) stabilizer states span \(|T\rangle^{\otimes n}\)", checkable by exact rank/linear-system arguments and, for small \(n\), by exhaustive search over the finite stabilizer set with a machine-checked proof. The verifier that closes the loop is exact: reconstruct the decomposition over the appropriate ring, and certify non-representability by an exact-rational linear-algebra or SAT/ILP infeasibility proof. Anything short of the section-2 standard - a numerically fitted decomposition, an upper bound with no matching lower bound, an asymptotic exponent presented as an exact value - is a partial result, never a solution.

## 1. Exact problem statement

A **stabilizer state** on \(n\) qubits is a state stabilized by a maximal abelian subgroup of the Pauli group (equivalently, produced from \(|0\rangle^{\otimes n}\) by a Clifford circuit); there are finitely many, and their amplitudes lie in \(\mathbb{Z}[\tfrac{1}{\sqrt2}, i]\) up to normalization. For a state \(|\psi\rangle\), the **stabilizer rank** is

\[
\chi(|\psi\rangle) \;=\; \min\Big\{\, r \;:\; |\psi\rangle = \sum_{j=1}^{r} c_j\,|\phi_j\rangle,\ c_j \in \mathbb{C},\ |\phi_j\rangle \text{ stabilizer states} \,\Big\}.
\]

Take the magic state \(|T\rangle = \tfrac{1}{\sqrt2}(|0\rangle + e^{i\pi/4}|1\rangle)\) (equivalently \(|H\rangle\), Clifford-equivalent), and study

\[
\chi_n \;:=\; \chi\big(|T\rangle^{\otimes n}\big).
\]

Basic facts: \(\chi_0 = 1\), \(\chi_1 = 2\); \(\chi_n\) is nondecreasing and submultiplicative,

\[
\chi_{n+m} \;\le\; \chi_n \chi_m,
\]

so the exponent

\[
\alpha \;=\; \lim_{n\to\infty} \tfrac{1}{n}\log_2 \chi_n
\]

exists. The simulation link is quantitative: a Clifford+\(T\) circuit with \(n\) \(T\)-gates, acting on a stabilizer input and terminating in a Pauli measurement, can be classically evaluated in time

\[
\mathrm{poly}(n)\cdot \chi_n^{\,O(1)} ,
\]

so any exact value or improved bound on \(\chi_n\) transfers directly to the runtime of the best known simulators (Bravyi–Gosset).

The **lower-bound condition** is a purely linear-algebraic statement. Fix an ordering \(|\phi_1\rangle,\dots,|\phi_N\rangle\) of the finitely many \(n\)-qubit stabilizer states. Then \(\chi_n \ge r\) iff, for every size-\((r-1)\) subset \(J\),

\[
|T\rangle^{\otimes n} \;\notin\; \mathrm{span}\{\,|\phi_j\rangle : j \in J\,\} ,
\]

a membership test decidable by exact rank over \(\mathbb{Z}[\tfrac{1}{\sqrt2}, i]\). This is what makes small-\(n\) exact values certifiable.

Two related quantities may be declared explicitly when used.

- **Exact stabilizer rank** \(\chi_n\), as above.

- **Approximate stabilizer rank** \(\chi_\delta(|\psi\rangle) = \min\{\chi(|\phi\rangle) : \big\||\phi\rangle - |\psi\rangle\big\| \le \delta\}\), which controls approximate simulation.

The current knowledge frames the whole target as a gap to close:

\[
\Omega(n) \;\le\; \chi_n \;\le\; O\!\big(2^{\alpha n}\big),
\qquad
\alpha \le 0.3963 ,
\]

a linear lower bound against an exponential upper bound, with the true growth rate unknown.

The cost measure is the integer \(\chi_n\) (or its exponent \(\alpha\), or the approximate rank at a stated \(\delta\)). The open problem: **for a specific \(n\), certify \(\chi_n\) exactly, or improve the best upper or lower bound on \(\chi_n\) (or on \(\alpha\)) with a checked certificate.** Start from this prompt alone - stabilizer states, the rank, and the tensor-power target are all fixed above.

## 2. Resolution standard

Fix a specific \(n\) (and the exact vs. approximate variant, with \(\delta\) if approximate). Resolution is **one** of:

1. **Exact value.** An explicit decomposition of \(|T\rangle^{\otimes n}\) into \(r\) stabilizer states (upper bound) **and** a proof that no decomposition into \(r-1\) stabilizer states exists (lower bound), giving \(\chi_n = r\); or

2. **Improved bound.** A decomposition beating the best-known upper bound, or an infeasibility proof beating the best-known lower bound (or improving \(\alpha\)).

**Named certified form.** One of:

- **Exact decomposition (upper bound).** The \(r\) stabilizer states given explicitly (as Clifford-circuit specs or stabilizer tableaux) with coefficients \(c_j \in \mathbb{Z}[\tfrac{1}{\sqrt2}, i]\); the sum recomputed exactly over that ring and shown equal to \(|T\rangle^{\otimes n}\) up to normalization.

- **Exhaustive / SAT lower bound (exact value at small \(n\)).** Over the finite set of \(n\)-qubit stabilizer states, a proof that no \(r-1\) of them linearly span \(|T\rangle^{\otimes n}\) - an exact-rational rank / linear-system infeasibility over all \(\binom{N}{r-1}\) subsets (made feasible by symmetry reduction), or a SAT/ILP encoding whose UNSAT is DRAT/LRAT-checked; replayed by an independent checker.

- **Structural lower bound with a checked inequality.** An exact algebraic lower-bound argument (in the Peleg–Shpilka–Volk / Lovitz style) instantiated for the specific \(n\), with all arithmetic exact and independently re-derived.

**Not accepted as resolution.**

- A decomposition found by **numerical** least-squares and reported without exact reconstruction over \(\mathbb{Z}[\tfrac{1}{\sqrt2}, i]\).

- An **upper bound with no matching lower bound** presented as the exact rank.

- An **asymptotic** exponent \(\alpha\) presented as a specific \(\chi_n\).

- An **unreplayable** search (a bare UNSAT, or an enumeration with no completeness argument) reported as a lower bound.

- Conflating exact and approximate rank, or dropping the \(\delta\) in the approximate case.

- Improving a bound already superseded in the current literature (the baseline must be cited with an access date).

## 3. Graded partial-result targets

- **P1 - Reproduce the small-\(n\) frontier.** Independently certify the known exact small values (e.g. \(\chi_1 = 2\), and the smallest \(n\) with \(\chi_n < 2^n\)) and reproduce the best-known small decompositions exactly. Certificate: exact ring reconstruction + a lower-bound proof for the reproduced values.

- **P2 - Exact linear-algebra core.** Build exact representations of \(n\)-qubit stabilizer states and an exact rank / linear-system solver over \(\mathbb{Z}[\tfrac{1}{\sqrt2}, i]\); reproduce a published decomposition and verify it exactly. Certificate: exact identity check.

- **P3 - A certified small exact value.** For the largest \(n\) reachable by symmetry-reduced exhaustion, certify \(\chi_n\) exactly (both directions). Certificate: exact decomposition + DRAT/LRAT or complete-enumeration lower bound.

- **P4 - An improved upper bound.** Find a decomposition of \(|T\rangle^{\otimes n}\) beating the best cited upper bound for a specific \(n\) (via nested / recursive constructions), reconstructed exactly. Certificate: exact ring identity + cited superseded baseline.

- **P5 - An improved lower bound.** Raise the best cited lower bound on \(\chi_n\) for a specific \(n\), or improve a bound on \(\alpha\), with a checked exact certificate (infeasibility or a structural inequality). Certificate: complete manifest; independently re-derived.

- **P6 - Reusable rank harness.** An audited exact-arithmetic tool that verifies a claimed decomposition and runs the small-\(n\) infeasibility search, validated against P1–P2. Certificate: source + a second implementation's agreement on shared instances.

## 4. Known results and prior art

- **Simulation link.** Bravyi, Gosset, *Improved classical simulation of quantum circuits dominated by Clifford gates*, PRL (2016) - runtime governed by stabilizer rank; Bravyi, Browne, Calpin, Campbell, Gosset, Howard, *Simulation of quantum circuits by low-rank stabilizer decompositions*, Quantum (2019) - approximate rank.

- **Lower bounds.** Bravyi, Smith, Smolin, *Trading classical and quantum computational resources*, PRX (~2016, verify) - \(\Omega(\sqrt n)\); Peleg, Shpilka, Volk, *Lower Bounds on Stabilizer Rank*, Quantum **6**, 652 (2022) - \(\Omega(n)\) exact, and \(\Omega(\sqrt n/\log n)\) for approximate rank (the first nontrivial approximate lower bound); a probabilistic quadratic lower bound on approximate rank (arXiv 2305.10277, 2023, verify).

- **Upper bounds.** Bravyi–Smith–Smolin small nested decompositions; Qassim, Pashayan, Gosset, *Improved upper bounds on the stabilizer rank of magic states*, Quantum (2021) - \(\chi(|T\rangle^{\otimes m}) = O(2^{\alpha m})\) with \(\alpha \le 0.3963\), improving \(\approx 0.463\); Lovitz, Steffan, *New techniques for bounding stabilizer rank*, Quantum (2022).

- **Small exact values.** \(\chi_1 = 2\); the small \(\chi_n\) values and the smallest \(n\) with \(\chi_n < 2^n\) discussed in the above (exact values beyond small \(n\) are open) - reproduce and cite precisely (verify).

Status as of mid-2026 - re-verify against the current literature before starting any session.

## 5. Attack plan

`[search]` `[opt]`. One workstation.

1. **Exact arithmetic core.** Represent stabilizer states exactly (tableau + amplitude in \(\mathbb{Z}[\tfrac{1}{\sqrt2}, i]\), via SageMath \(\mathbb{Q}(\zeta_8)\)); implement exact linear solves / rank over that ring. Validate on published decompositions.

2. **Upper bounds first.** Reconstruct known nested / recursive decompositions and search for better ones (recursive 6-copy-style blocks, Clifford-orbit tricks); each candidate certified by an exact identity.

3. **Small-\(n\) exact values.** Enumerate \(n\)-qubit stabilizer states - there are \(2^n \prod_{i=1}^{n}(2^i + 1)\) of them - reduce by the Clifford symmetry of \(|T\rangle^{\otimes n}\), and test whether any \(r-1\) span the target via exact linear algebra - the lower-bound engine for tiny \(n\).

4. **SAT/ILP lower bounds.** Encode "some \(r-1\) stabilizer states span \(|T\rangle^{\otimes n}\)" (over the finite state set) into CNF/ILP; a DRAT/LRAT-checked UNSAT gives \(\chi_n \ge r\). Use as an independent route to the exhaustion.

5. **Structural bounds.** Instantiate the Peleg–Shpilka–Volk / Lovitz inequalities for the specific \(n\) with exact arithmetic; cross-check against the search where both apply. Track the induced bound on the exponent \(\alpha\), since a small-\(n\) exact value combined with submultiplicativity \(\chi_{n+m} \le \chi_n \chi_m\) upper-bounds \(\alpha\) directly.

6. **Failure modes.** The number of stabilizer states explodes super-exponentially, so exhaustion is confined to very small \(n\) even with symmetry reduction; exact linear algebra over \(\mathbb{Z}[\zeta_8]\) is slow (guard the ring implementation); numerical decompositions that don't reconstruct exactly; conflating exact vs approximate rank; trusting a bare UNSAT. Declare exact-vs-approximate and \(\delta\) in every claim.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Decompositions are reconstructed exactly over \(\mathbb{Z}[\tfrac{1}{\sqrt2}, i]\); lower bounds carry a DRAT/LRAT UNSAT proof, an exact-rational infeasibility certificate, or a complete symmetry-reduced enumeration with a stated completeness argument. Floating point is screening only.

2. **Independent verification.** A standalone checker, separate from the search, that (a) recomputes the decomposition sum and compares it to \(|T\rangle^{\otimes n}\), and (b) replays the lower-bound proof (a proof checker, a second solver, or a re-run enumeration). A second exact-ring implementation.

3. **Reproducibility.** Every stabilizer-state list, decomposition, encoding, solver/CAS name+version, symmetry-reduction rule, and (if approximate) the \(\delta\) recorded; SHA-256 manifest over all artifacts and proof traces; the best-known bound being matched or improved cited with source and access date.

4. **Preservation.** All search, decomposition, and reconstruction source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).

5. **Honest reporting.** The report states up front, per \(n\) and variant, whether an exact value was certified (both directions), whether only a one-sided bound was obtained, whether the result is exact or approximate rank, and whether a published bound was strictly improved - never presenting a numerical decomposition, an upper bound alone, or an asymptotic exponent as the exact \(\chi_n\).
