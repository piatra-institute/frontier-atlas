# PROMPT FOR CERTIFIED MINIMUM-GATE CLIFFORD AND CNOT CIRCUITS

## Optimal CNOT-count of a linear reversible function and optimal-gate synthesis of a specific Clifford operator

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 37 of 50
**Area:** quantum computation & codes
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Below the non-Clifford layer, the second cost that dominates fault-tolerant and NISQ circuits is the number of two-qubit gates - CNOTs. Two clean sub-problems live here. First, the **linear reversible** (GF(2)) synthesis problem: an invertible \(n\times n\) matrix over \(\mathbb{F}_2\) describes a CNOT-only circuit, and one asks for the fewest CNOTs realizing it. Second, the **Clifford** synthesis problem: given a stabilizer/Clifford operator (a symplectic action on the Pauli group), find the minimum-gate circuit over a fixed elementary set \(\{H, S, \mathrm{CNOT}\}\). Both are finite, exactly checkable, and open in the specific: Patel–Markov–Hayes give an asymptotically optimal \(\Theta(n^2/\log n)\) CNOT bound and Bravyi–Maslov give canonical forms bounding Clifford cost, yet the exact minimum for a specific matrix or a specific Clifford operator is generally unknown. The verifier is exact: a candidate circuit multiplies out (over \(\mathbb{F}_2\) for CNOT-only, over the symplectic representation for Clifford) and is compared to the target, while optimality is settled by SAT/ILP infeasibility of every cheaper circuit with a checked proof. Anything short of the section-2 standard - a good circuit with no matching lower bound, a heuristic count, an unreplayable solver run - is a partial result, never a solution.

## 1. Exact problem statement

**Linear reversible functions.** A CNOT gate with control \(c\) and target \(t\) acts on a basis state \(x \in \mathbb{F}_2^n\) by \(x_t \mapsto x_t \oplus x_c\); as a matrix over \(\mathbb{F}_2\) it is the transvection

\[
E_{tc} \;=\; I + e_t e_c^{\top},
\qquad t \ne c .
\]

A CNOT-only circuit computes an invertible linear map \(A \in \mathrm{GL}(n,\mathbb{F}_2)\), and every such \(A\) is a product of transvections. Define the **CNOT-count**

\[
\mathrm{cnot}(A) \;=\; \min\{\,k \;:\; A = E_{t_k c_k}\cdots E_{t_1 c_1}\,\},
\]

the minimum number of CNOTs under all-to-all connectivity. A connectivity graph \(G\) may be imposed, restricting the allowed \((t,c)\) pairs to its edges and giving \(\mathrm{cnot}_G(A)\).

**Clifford operators.** Modulo phases the \(n\)-qubit Pauli group is \(\mathbb{F}_2^{2n}\); a Clifford operator acts by an affine symplectic map \((M, v)\) with

\[
M \in \mathrm{Sp}(2n,\mathbb{F}_2),
\qquad
M^{\top} \Omega\, M = \Omega,
\qquad
\Omega = \begin{pmatrix}0 & I_n \\ I_n & 0\end{pmatrix},
\]

together with a phase (sign) vector on the images of the generators. Fix the elementary gate set

\[
\mathcal{G} \;=\; \{\,H_i,\; S_i,\; \mathrm{CNOT}_{ij}\,\}.
\]

For a Clifford \(U\) given by its stabilizer tableau (its action on \(X_i, Z_i\) with signs) define the **gate-count**

\[
\mathrm{gc}_{\mathcal{G}}(U) \;=\; \min\{\,k \;:\; U = g_k \cdots g_1,\ g_j \in \mathcal{G}\,\},
\]

and, separately, the **CNOT-count of a Clifford** (weighting only two-qubit gates). Global phase is quotiented out; the single-qubit weighting must be declared (unit weight vs. free single-qubit gates).

The search spaces are finite but grow fast, which fixes the workstation-scope boundary:

\[
\big|\mathrm{GL}(n,\mathbb{F}_2)\big| = \prod_{i=0}^{n-1}\!\big(2^n - 2^i\big),
\qquad
\big|\mathcal{C}_n / \text{phase}\big| = 2^{n^2 + 2n}\prod_{i=1}^{n}\!\big(4^i - 1\big).
\]

So exhaustive Cayley-graph search is feasible only for small \(n\) (roughly \(n \le 4\)), and larger targets need SAT/ILP with a bounded circuit length.

The cost measure, the target (an explicit \(A\), or an explicit Clifford tableau / named operator such as a stabilizer-state preparation, a CZ-layer, or a permutation-plus-phase), the connectivity, and the weighting are all fixed in every claim. The open question, per target: **produce a circuit of size \(k\) and a proof that no circuit over the declared set realizes the target with fewer than \(k\) gates.** Start from this prompt alone - transvections, the symplectic representation, and both cost measures are defined above.

## 2. Resolution standard

For a **named** target - an explicit \(A \in \mathrm{GL}(n,\mathbb{F}_2)\) or an explicit Clifford tableau - in a declared cost measure, connectivity, and weighting, resolution is a pair:

1. an explicit circuit of size \(k\) whose product (over \(\mathbb{F}_2\), or as a symplectic-plus-sign tableau) equals the target exactly; and

2. a machine-checkable proof that no valid circuit of size \(< k\) realizes the target.

**Named certified form.** The lower bound must take one of the following forms.

- **SAT optimality with a proof.** Encode "there exists a valid circuit of size \(\le k-1\) computing the target" (bounded gate sequence; state = the \(\mathbb{F}_2\) matrix or the symplectic tableau) as CNF; obtain UNSAT with a DRAT/LRAT proof checked by an independent checker; the \(k\)-gate witness is separately reconstructed.

- **ILP optimality with a proof.** An integer program whose optimum equals the minimum count, solved to proven optimality with an exact rational (Farkas / branch-and-bound) certificate in an exact solver.

- **Exhaustive-BFS optimality.** For small \(n\), a breadth-first shortest-path search in the Cayley graph of \(\mathrm{GL}(n,\mathbb{F}_2)\) or the Clifford group over \(\mathcal{G}\), with the frontier at distance \(k-1\) shown not to contain the target - replayed by an independent enumerator.

**Not accepted as resolution.**

- A circuit from Patel–Markov–Hayes, Gaussian elimination, Steiner-tree, or PermRowCol heuristics reported as optimal **without a matching lower bound**.

- A count from Bravyi–Maslov canonical-form layer bounds treated as the exact minimum (canonical forms bound cost; they do not certify per-instance optimality).

- A **numerically** checked Clifford equality; equality must be exact over \(\mathbb{F}_2\) / the tableau.

- An **unreplayable** solver run (bare UNSAT, no proof trace), or a proof the checker rejects.

- Mixing connectivity assumptions or single-qubit weightings between the witness and the lower bound.

## 3. Graded partial-result targets

- **P1 - Reproduce the frontier.** Re-derive known exact CNOT-counts for small named linear functions (the reverse permutation, small full-rank circulants) and the canonical-form gate bounds for small Cliffords with our own exact toolchain. Certificate: exact reconstruction + shortest-path replay.

- **P2 - Exact CNOT-count, small \(n\).** Certify \(\mathrm{cnot}(A)\) for all/most \(A \in \mathrm{GL}(n,\mathbb{F}_2)\) at \(n = 3,4\) (all-to-all) by full BFS in the Cayley graph, and tabulate the diameter. Certificate: complete BFS replay + independent distance check.

- **P3 - Connectivity-restricted optima.** For a fixed sparse connectivity \(G\) (line, ring, grid) and a named \(A\), certify \(\mathrm{cnot}_G(A)\) via SAT/ILP with a checked infeasibility proof. Certificate: DRAT/LRAT UNSAT + witness.

- **P4 - Exact Clifford gate-count.** For a named small Clifford (a specific 3–4 qubit tableau, e.g. a stabilizer-state encoder), certify \(\mathrm{gc}_{\mathcal G}(U)\) and the CNOT-count. Certificate: SAT UNSAT at \(k-1\) + exact tableau witness.

- **P5 - A new exact value.** Establish a previously-untabulated exact CNOT- or Clifford-count for a named operator at the edge of feasibility (\(n=5\), or a specific structured family), or certify optimality of a construction believed optimal but never proved. Certificate: full manifest, both directions checked.

- **P6 - Reusable optimality harness.** An audited SAT/ILP encoder for both problems with a standalone lower-bound checker, validated against the BFS ground truth of P2. Certificate: source + cross-solver agreement on shared instances.

## 4. Known results and prior art

- **Linear reversible synthesis.** Patel, Markov, Hayes, *Optimal synthesis of linear reversible circuits*, QIC **8** (2008) - asymptotically optimal \(\Theta(n^2/\log n)\) CNOTs, optimal up to a constant, not per-instance exact. Connectivity-aware refinements: Steiner-tree synthesis (Nash–Gheorghiu–Mosca, ~2020, verify), PermRowCol (de Griend–Duncan, ~2020, verify), A*/beam-search variants.

- **Clifford canonical forms.** Bravyi, Maslov, *Hadamard-free circuits expose the structure of the Clifford group*, IEEE Trans. Inf. Theory **67**(7), 4546–4563 (2021) - canonical form \(F_1\,H\,S\,F_2\) (Hadamard-free layers, a Hadamard layer, a qubit permutation); layered depth and gate bounds; near-optimal random-Clifford sampling.

- **Stabilizer-circuit canonical form.** Aaronson, Gottesman, *Improved simulation of stabilizer circuits*, PRA (2004) - an 11-round canonical form; source of tableau bookkeeping.

- **Clifford optimization (heuristic upper bounds).** Bravyi, Shaydulin, Hu, Maslov, *Clifford circuit optimization with templates and symbolic Pauli gates*, Quantum (2021); Maslov–Roetteler shorter stabilizer circuits (~2018, verify).

- **Generators and relations.** Selinger and others on presentations of the \(n\)-qubit Clifford group (~2015, verify) - structural, not per-instance optimality.

- **CNOT minimum-cost.** Recent exact/ILP treatments of CNOT synthesis cost (Springer QIP, *Minimum synthesis cost of CNOT circuits*, ~2025, verify).

Status as of mid-2026 - re-verify against the current literature (and record trackers) before starting any session.

## 5. Attack plan

`[search]`. One workstation.

1. **Exact state representations.** Linear reversible: the \(\mathbb{F}_2\) matrix (bit-packed). Clifford: the stabilizer tableau (symplectic matrix + sign bits), with a tested update rule per gate. Verify the representation against a second implementation (Stim's tableau simulator) on random circuits before trusting it.

2. **BFS ground truth (small \(n\)).** Full breadth-first search in the Cayley graph over the elementary set for \(n = 3,4\): gives exact optima and the diameter, and becomes the oracle validating the SAT/ILP encoders. Store distances.

3. **SAT encoding.** Bounded circuit of length \(k\): variables for gate choice per slot and for the induced state; constraint that the final state equals the target; ask for length \(k-1\). Drive kissat/CaDiCaL/CryptoMiniSat with DRAT/LRAT logging; check with `drat-trim`/`lrat-check`.

4. **ILP encoding.** An exact-rational integer program for the same optimum; solve to proven optimality in SCIP/SoPlex/QSopt_ex with a Farkas / optimality certificate. Use as a second, independent optimality route.

5. **Connectivity constraints.** Restrict the allowed CNOT pairs to the edges of \(G\); re-run P3–P4 to expose the connectivity overhead exactly.

6. **Failure modes.** The Cayley graph explodes past \(n=4\)–\(5\) (the Clifford group order grows super-exponentially); CNF/ILP size grows with the length bound \(k\); tableau update bugs silently corrupt the target (guard with Stim cross-checks); connectivity/weighting mismatches between witness and lower bound; trusting a bare UNSAT. Keep every claim in one declared cost measure, connectivity, and weighting.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** All products and equalities are exact over \(\mathbb{F}_2\) / the symplectic-plus-sign tableau; every optimality claim carries a DRAT/LRAT UNSAT proof, an exact ILP-infeasibility certificate, or a completed BFS with a replayable frontier. Floating point plays no role.

2. **Independent verification.** A standalone checker, separate from the search, that (a) reconstructs the witness circuit's action and compares to the target, and (b) replays the lower-bound proof (a DRAT/LRAT checker, a second solver, or a re-run BFS). Cross-check tableau updates against Stim.

3. **Reproducibility.** Every encoding, solver name+version, seed, connectivity graph, and weighting convention recorded; SHA-256 manifest over circuits, tableaux/matrices, CNF/LP files, and proof traces; any baseline value matched or improved cited with source and access date.

4. **Preservation.** All search, encoding, and reconstruction source is part of the record; anything not preserved is stated explicitly (the Hadamard-668 lost-source lesson).

5. **Honest reporting.** The report states up front, per target and cost measure, whether a witness and a matching lower bound were both certified, whether the result is exact or only an upper bound, and whether any published value was strictly improved - with connectivity and weighting fixed. A canonical-form bound or a heuristic count is never presented as the exact minimum.
