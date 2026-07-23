# PROMPT FOR CERTIFIED GATE-COUNT LOWER BOUNDS ON A SPECIFIC UNITARY

## Minimum number of two-qubit gates to exactly implement a named \(n\)-qubit operator

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 43 of 50
**Area:** quantum computation & codes
**Modes:** `[search]` `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

How many two-qubit gates does it take to build a given \(n\)-qubit unitary exactly? A parameter-counting argument gives a worst-case floor of order \(4^n/n^2\), and for the generic operator the count is essentially forced; but for a **specific** structured operator the exact minimum is usually unknown, and proving a lower bound - "this unitary needs at least \(g\) two-qubit gates" - is the hard direction, because it must rule out every cheaper circuit. This is exactly the kind of finite, adversarial statement current AI methods can close: for a fixed gate library, "there is a circuit with \(\le g-1\) two-qubit gates equal to \(U\)" is a bounded search whose infeasibility can be certified by exhaustive shortest-path enumeration (for small \(n\)) or by a SAT/ILP encoding with a machine-checked UNSAT proof, and reconstruction of any witness circuit is exact. The value of a certified lower bound is that it converts a folklore "believed optimal" circuit into a theorem. The verifier that closes the loop is exact: a witness circuit multiplies out to \(U\) over the exact entry ring, and the lower bound is a checked infeasibility proof for all cheaper circuits. This is the lower-bound-focused companion to the synthesis prompts (36, 37): here the deliverable is the **certified minimum gate count** of a named operator, not merely a good circuit. Anything short of the section-2 standard - a counting-bound estimate, a heuristic "optimal" circuit, an unreplayable solver run - is a partial result, never a solution.

## 1. Exact problem statement

Fix a **gate library** \(\mathcal{L}\): the two-qubit gates counted (\(\mathrm{CNOT}\), or \(\mathrm{CZ}\), or arbitrary two-qubit unitaries), together with the single-qubit gates allowed for free or at unit weight (this must be declared). For an exactly-implementable \(n\)-qubit unitary \(U\) - either exactly synthesizable over a discrete set (Clifford+\(T\), entries in \(\mathbb{Z}[\tfrac{1}{\sqrt2}, i]\)) or a fixed algebraic operator - define the **two-qubit gate count**

\[
g_{\mathcal{L}}(U) \;=\; \min\{\,\#\{\text{two-qubit gates in } C\} \;:\; C \text{ a circuit over } \mathcal{L},\ C = U\,\},
\]

with single-qubit gates counted or free per the declaration.

The **counting (dimension) lower bound**: an \(n\)-qubit circuit with \(m\) generic two-qubit gates and free single-qubit gates has at most \(O(m + n)\) continuous parameters, while \(U(2^n)\) has \(4^n - 1\); hence any universal set needs \(\Omega(4^n/n^2)\) two-qubit gates in the worst case, and for the \(\mathrm{CZ}\)-count specifically

\[
g_{\mathrm{CZ}}(U) \;\ge\; \tfrac{1}{4}\big(4^n - 3n - 1\big)
\]

for a generic \(U\) (Shende–Bullock–Markov). The argument is a dimension count: a circuit with \(g\) two-qubit gates from a fixed set and free single-qubit rotations is parameterized by

\[
\dim \;\le\; 3(g+1)n + (\text{discrete choices}),
\]

while the target manifold \(SU(2^n)\) has real dimension \(4^n - 1\); matching forces \(g = \Omega(4^n/n)\), and the sharper CZ bookkeeping gives the displayed \(\tfrac14(4^n - 3n - 1)\). This bounds the **generic** case; a specific \(U\) may need far fewer, and pinning its exact minimum is the target here.

For a **discrete** library (Clifford+\(T\), or CNOT+single-qubit-Clifford) the set of circuits with \(\le g\) two-qubit gates is finite: with \(L\) elementary gate types on \(n\) qubits the number of length-\(\ell\) words is at most \(L^{\ell}\), so the reachable set at bounded gate count is finite and "no cheaper circuit equals \(U\)" is a decidable statement. This is the regime in which machine-checkable lower bounds are attainable; for continuous libraries the same question is a real-algebraic-geometry problem and only the dimension bound and a few small classifications are known exactly.

The one fully settled regime anchors the rest. For \(n = 2\), the KAK / magic-basis invariants of \(U \in SU(4)\) partition operators into exactly-known CNOT classes: a generic two-qubit unitary needs exactly \(3\) CNOTs, and the classes needing \(0\), \(1\), or \(2\) are characterized by explicit polynomial conditions on the local invariants,

\[
g_{\mathrm{CNOT}}(U) \in \{0,1,2,3\}
\qquad (n=2),
\]

decidable exactly. Reproducing this classification with an exact toolchain (P1) is the calibration point; the open work is the analogous exact minima at \(n \ge 3\).

The cost measure is the integer \(g_{\mathcal{L}}(U)\) (two-qubit-gate / CNOT / CZ count); the library, the single-qubit weighting, the connectivity (all-to-all unless a graph is declared), the exact-vs-approximate mode (exact only here), and the target \(U\) are all fixed per claim. The smallest genuinely multi-qubit anchor is the Toffoli gate, for which the exact CNOT-minimum is known:

\[
g_{\mathrm{CNOT}}(\mathrm{Toffoli}) \;=\; 6
\]

(Shende–Markov), a result that must rule out every 5-CNOT circuit - the model instance of a certified lower bound. Most named 3- and 4-qubit operators have no such matching pair on record.

The open problem, per target: **for a named \(U\), prove a lower bound \(g_{\mathcal L}(U) \ge g\) - ideally matching a known \(g\)-gate circuit, certifying the exact minimum.** Start from this prompt alone - the library, the cost measure, and the counting bound are defined above.

## 2. Resolution standard

Fix a named operator \(U\), a library \(\mathcal{L}\), a single-qubit weighting, and a connectivity. Resolution is:

1. a certified **lower bound** \(g_{\mathcal L}(U) \ge g\) - a machine-checkable proof that no circuit over \(\mathcal{L}\) with \(\le g-1\) two-qubit gates equals \(U\); and, when the exact minimum is claimed,

2. a matching **witness** circuit with exactly \(g\) two-qubit gates whose product recomputes to \(U\) exactly.

**Named certified form.** The lower bound must take one of the following forms.

- **Exhaustive shortest-path lower bound (small \(n\)).** A breadth-first / iterative-deepening search over circuits with \(\le g-1\) two-qubit gates (single-qubit freedom handled by a canonical or discretized normal form, or by working in a discrete group) proving \(U\) is unreachable; the frontier and unreachability are replayed by an independent enumerator.

- **SAT/ILP infeasibility with a proof.** Encode "a circuit over \(\mathcal{L}\) with \(\le g-1\) two-qubit gates equals \(U\)" (for a discrete library, e.g. Clifford+\(T\) or a stabilizer / permutation target) as CNF/ILP; obtain UNSAT with a DRAT/LRAT proof (or ILP infeasibility with an exact certificate), independently checked; the \(g\)-gate witness verified separately.

- **Exact structural lower bound.** An algebraic invariant argument (entangling-power / tensor-structure, or a counting bound sharpened for the specific \(U\)) with all arithmetic exact and independently re-derived, matching a construction.

**Not accepted as resolution.**

- The **counting bound** \(\Omega(4^n/n^2)\) quoted as the exact minimum for a specific operator (it is a generic / worst-case statement).

- A **heuristic** "optimal" circuit (from a transpiler or a numerical decomposition) with no infeasibility proof for cheaper circuits.

- A **numerically** verified witness (floating-point equality) without exact reconstruction.

- An **unreplayable** solver run (bare UNSAT), or an **incomplete** search reported as a lower bound.

- Mixing libraries, single-qubit weightings, or connectivities between the lower bound and the witness.

- An asymptotic bound where a specific integer is asked.

## 3. Graded partial-result targets

- **P1 - Reproduce settled minima.** Re-derive known exact two-qubit-gate minima with our toolchain: 3 CNOTs for a generic two-qubit unitary (and the 2-CNOT / 1-CNOT classes), 6 CNOTs for the Toffoli (Shende–Markov). Certificate: exact witness + independent lower-bound proof.

- **P2 - Exhaustive small-\(n\) frontier.** For a discrete library at \(n = 2, 3\), compute exact minimum two-qubit-gate counts for a family of named targets by full shortest-path search. Certificate: complete BFS replay + exact distance.

- **P3 - Connectivity-restricted lower bounds.** For a fixed sparse connectivity and a named operator, certify the two-qubit-gate minimum via SAT/ILP with a checked infeasibility proof. Certificate: DRAT/LRAT UNSAT + witness.

- **P4 - A named 3–4 qubit operator.** Certify the exact two-qubit-gate minimum (or a new lower bound) for a specific operator outside the settled list (a specific reversible function, a specific Clifford, a small entangling gate). Certificate: checked infeasibility at \(g-1\) + exact witness.

- **P5 - A new certified lower bound.** Establish a previously-unproved lower bound for a named operator at the edge of feasibility, ideally matching a folklore-optimal circuit to pin the exact minimum. Certificate: full manifest, both directions independently checked.

- **P6 - Reusable lower-bound harness.** An audited exhaustive / SAT lower-bound engine with a standalone infeasibility checker, validated against the P1–P2 ground truth. Certificate: source + cross-solver / cross-enumerator agreement on shared instances.

## 4. Known results and prior art

- **Counting / dimension bounds.** Shende, Bullock, Markov, *Synthesis of quantum-logic circuits*, IEEE TCAD (2006); *Minimal universal two-qubit CNOT-based circuits*, PRA **69**, 062321 (2004) - generic CZ-count \(\ge \tfrac{1}{4}(4^n - 3n - 1)\); three CNOTs necessary and sufficient for a generic two-qubit unitary.

- **Two-qubit optima.** Vatan, Williams (~2004, verify) and Vidal, Dawson - 3-CNOT optimal two-qubit circuits; the 17→18 elementary-gate lower/upper-bound refinements for arbitrary two-qubit operators (verify).

- **Local invariants.** Makhlin, and Zhang–Vala–Sastry–Whaley (~2003, verify) - the local (KAK) invariants of two-qubit unitaries that make the \(n=2\) CNOT classification an exact, decidable test; the calibration ground truth for P1.

- **Toffoli / small operators.** Shende, Markov, *On the CNOT-cost of TOFFOLI gates* (~2009, verify) - the Toffoli needs 6 CNOTs; small multiply-controlled gate costs.

- **Upper-bound synthesis.** Bullock–Markov; the quantum Shannon decomposition (Shende–Bullock–Markov) - best generic CNOT upper bounds (\(\approx \tfrac{23}{48}4^n\)); these are constructions, not per-operator lower bounds.

- **Discrete-set lower bounds.** The exact-synthesis and \(T\)-count machinery (problem 36) and the Clifford/CNOT synthesis machinery (problem 37) supply the discrete-library infeasibility encodings reused here.

- **CNOT-cost of Cliffords.** The CNOT-cost of stabilizer operators connects to the linear-reversible optima of problem 37; the exact two-qubit-gate minimum of a named Clifford is generally open beyond small \(n\).

- **General difficulty.** No super-linear circuit lower bound is known for an explicit operator beyond the dimension/counting bound; the frontier is small named operators certified exactly, which is precisely why the finite discrete-library search is the right instrument.

Status as of mid-2026 - re-verify against the current literature before starting any session.

## 5. Attack plan

`[search]` `[cert]`. One workstation.

1. **Exact representation.** Discrete targets (Clifford+\(T\), stabilizer, permutation): exact matrices over \(\mathbb{Z}[\omega]\) or tableaux / \(\mathbb{F}_2\) (reuse the problem 36–37 cores). Fixed algebraic targets: exact algebraic entries. Every witness product and equality is exact.

2. **Exhaustive shortest-path (small \(n\)).** BFS / iterative deepening over circuits with a bounded two-qubit-gate count, single-qubit freedom handled by a canonical normal form or by working inside a discrete group; this gives exact minima and the oracle validating the encoders.

3. **SAT/ILP infeasibility.** Encode "some circuit with \(\le g-1\) two-qubit gates equals \(U\)" (discrete library) into CNF/ILP; drive kissat/CaDiCaL/CryptoMiniSat with DRAT/LRAT logging; check with `drat-trim`/`lrat-check`. Mirror with an exact ILP (SCIP) and a Farkas certificate.

4. **Structural invariants.** Sharpen the counting bound or apply entangling-structure invariants for the specific \(U\) to prune or to give an independent lower bound; keep the arithmetic exact.

5. **Match to constructions.** Pull the best-known circuit (Qiskit/PyZX transpile, hand construction) as the upper bound; the goal is to make lower and upper meet.

6. **Failure modes.** Circuit-space explosion past \(n = 3\)–\(4\); the continuous single-qubit freedom makes exact lower bounds hard for arbitrary-two-qubit-gate libraries - restrict to discrete libraries where infeasibility is finite and certifiable; CNF size growth with the gate budget; trusting a bare UNSAT; library / weighting / connectivity mismatches between the two directions. Declare the full library and conventions in every claim.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Witness circuits reconstruct \(U\) exactly (over \(\mathbb{Z}[\omega]\) / the tableau / algebraic entries); every lower bound carries a DRAT/LRAT UNSAT proof, an exact ILP-infeasibility certificate, or a complete replayable shortest-path search. Floating point is screening only.

2. **Independent verification.** A standalone checker, separate from the search, that (a) reconstructs the witness and compares it to \(U\), and (b) replays the infeasibility proof (a DRAT/LRAT checker, a second solver, or a re-run BFS). Dual encodings (SAT and ILP) where both apply.

3. **Reproducibility.** Every library definition, weighting, connectivity, encoding, solver name+version, seed, and normal-form convention recorded; SHA-256 manifest over circuits, matrices/tableaux, CNF/LP files, and proof traces; any baseline lower bound matched or improved cited with source and access date.

4. **Preservation.** All search, encoding, and reconstruction source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).

5. **Honest reporting.** The report states up front, per operator and library, whether a lower bound was certified, whether it matches a construction (pinning the exact minimum), whether the result is exact, and whether any published bound was strictly improved - never presenting the counting bound, a transpiler output, or a numerical witness as a certified per-operator minimum.
