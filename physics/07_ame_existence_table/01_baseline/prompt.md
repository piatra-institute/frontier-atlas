# PROMPT FOR COMPLETING THE ABSOLUTELY-MAXIMALLY-ENTANGLED STATES EXISTENCE TABLE

## Deciding the undecided $(n,d)$ entries for AME states of $n$ qudits

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 07 of 50 (Tier 1)
**Source:** top-50 list #5, category A (quantum information and foundations)
**Modes:** `[search]` `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

An absolutely maximally entangled state AME$(n,d)$ is a pure state of $n$ qudits of local dimension $d$ whose every $\lfloor n/2 \rfloor$-body marginal is maximally mixed - the extremal objects of multipartite entanglement, equivalent to pure quantum MDS-type codes and to the perfect tensors used in holographic codes. Existence is decided for most $(n,d)$, but a finite list of cells remains open. The 2021 positive resolution of AME$(4,6)$ via a quantum solution of Euler's 36-officers problem showed that open cells can fall to structured search; the 2017 negative resolution of AME$(7,2)$ showed they can fall to semidefinite and weight-enumerator certificates. Each undecided cell is a *finite, certifiable* existence question: a construction verified in exact arithmetic, or a nonexistence certificate from the enumerator cone. That per-cell decidability profile - search on one side, rational SDP certificates on the other - is precisely what our toolchain is built for. The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

Fix integers $n \ge 2$ and $d \ge 2$. A pure state $|\psi\rangle \in (\mathbb{C}^d)^{\otimes n}$ with $\||\psi\rangle\| = 1$ is **absolutely maximally entangled**, written AME$(n,d)$, if for every subset $S \subseteq \{1,\dots,n\}$ with $|S| = \lfloor n/2 \rfloor$,

\[
\rho_S \;=\; \operatorname{Tr}_{S^c} |\psi\rangle\langle\psi| \;=\; \frac{\mathbb{1}_{d^{|S|}}}{d^{|S|}} .
\]

Equivalently: every balanced bipartition ($\lfloor n/2\rfloor$ vs. $\lceil n/2\rceil$ parties) carries maximal entanglement entropy. Imposing the condition at $|S| = \lfloor n/2\rfloor$ implies it for all smaller $S$ (re-derive in-session).

Equivalent formulations, all used below and to be kept exactly synchronized:

- AME$(n,d)$ states are exactly the $\lfloor n/2\rfloor$-uniform states of $n$ qudits;
- they are exactly the pure quantum codes $((n, 1, \lfloor n/2\rfloor + 1))_d$;
- for even $n$, they are perfect tensors: the coefficient tensor is proportional to an isometry across every balanced bipartition;
- minimal-support AME states are equivalent to classical MDS codes $[n, \lceil n/2\rceil, \lfloor n/2\rfloor + 1]_d$ - which can fail to exist even when AME states exist (AME$(4,6)$ is the canonical warning).

By purity, the marginal condition on $S$ and on its complement are equivalent, so the number of independent balanced-marginal constraints is

\[
\tfrac{1}{2}\binom{n}{\lfloor n/2\rfloor} \ \text{(even } n\text{)}, \qquad \binom{n}{\lfloor n/2\rfloor} \ \text{(odd } n\text{)};
\]

checkers must nonetheless verify all subsets and use the redundancy as an internal consistency test.

Define the existence predicate $\mathrm{AME}(n,d) \in \{\text{yes}, \text{no}\}$.

**The problem: decide $\mathrm{AME}(n,d)$ for the currently undecided cells, targeting the smallest first.**

The scope of "the table" adopted here is the Huber–Wyderka open-table tradition (the maintained online table of AME existence). The session must begin by reconstructing that table with per-cell provenance (target P1) and freezing a verified list $U$ of undecided cells; the target set is $U$. We deliberately refuse to hard-code $U$ in this prompt: the table moves, and a stale list is worse than none. The anchors in section 4 are fixed points; the frozen $U$ becomes part of the session record.

Note that for fixed $n$, all but finitely many $d$ are decided - constructions exist for all sufficiently large $d$ (Reed–Solomon-type for prime powers $d \ge n-1$, and products/combinations beyond) - so $U$ is finite and concentrated at small $d$, non-prime-power $d$, and moderate $n$.

## 2. Complete-resolution standard

For each targeted cell $(n,d) \in U$, exactly one of:

1. **Existence.** An explicit state:
   - exact amplitudes over a stated field (rational, cyclotomic, or algebraic with minimal polynomials), or an exact combinatorial construction (orthogonal array, graph state over a stated ring, 2-unitary/multiunitary matrix) from which amplitudes are derived exactly;
   - together with exact verification that *every* $\binom{n}{\lfloor n/2\rfloor}$-choice marginal is exactly maximally mixed, executed by an independent checker.
2. **Nonexistence.** A proof. If computer-assisted:
   - a rational (exactly feasible) dual certificate for an LP/SDP over the Shor–Laflamme/shadow enumerator cone, or an exhaustive argument with per-branch certificates;
   - checked end-to-end in exact arithmetic by an independent checker;
   - plus a human-readable soundness argument for the relaxation used (why feasibility of a state implies feasibility of the relaxed system).

Complete resolution of this prompt = every cell of the frozen $U$ decided to this standard. Partial resolution = a nonempty subset of $U$ decided; report cell-by-cell.

**Not accepted as resolution:**

- Numerical states with marginals maximally mixed to machine precision (seesaw or gradient outputs) without an exact or validated-numerics lift.
- Nonexistence claimed from failed numerical searches, or from floating-point SDP infeasibility without a rational dual certificate.
- Existence claimed from a classical OA/MDS object without exact verification of the induced quantum state's marginals; conversely, nonexistence of classical MDS/OA objects presented as nonexistence of AME - the AME$(4,6)$ history is exactly this trap.
- Deciding a cell already decided in the literature and presenting it as new (re-verification is P1: valuable, and labeled as such).
- Statements about $k$-uniform states with $k < \lfloor n/2\rfloor$ presented as AME results.
- "Approximate AME" or $\varepsilon$-AME results presented as existence.

## 3. Graded partial-result targets

**P1 - Verified table reconstruction.**
*Task:* rebuild the AME existence table for at least $2 \le n \le 10$, $2 \le d \le 10$: for every decided cell, a citation *plus independent re-verification* - exact marginal checks for constructive cells; re-derivation or replay of nonexistence certificates for negative cells (including AME$(4,2)$, AME$(7,2)$, and the $n \ge 8$ qubit exclusions). Output the frozen undecided list $U$ with provenance.
*Certificate:* per-cell dossier, hashed; checker code.
*Value:* a serviceable community artifact on its own.

**P2 - Exact re-certification of the two modern landmarks.**
*Task:* (a) AME$(4,6)$ - verify the published 2-unitary/quantum-Latin-square solution in exact arithmetic (the published amplitudes lie in a small explicit field; verify all balanced marginals exactly). (b) AME$(7,2)$ - reproduce nonexistence via the weight-enumerator/shadow LP-SDP with a rational dual certificate of our own.
*Certificate:* exact checker transcripts; rational dual vector with exact feasibility verification.
*Effort:* days to a week each.

**P3 - Certified nonexistence for the smallest tractable open cell.**
*Task:* select from $U$ the cell with the smallest enumerator-cone relaxation; run the symmetry-reduced LP/SDP hierarchy (Shor–Laflamme enumerators, quantum MacWilliams transform, shadow inequalities; higher levels as needed) at high precision; round to a rational certificate.
*Certificate:* rational dual certificate, independently checked.
*Calibration:* the known hierarchy may well be feasible for the truly open cells - that is why they are open. Certified feasibility of the relaxation is then reported as a structured negative result delimiting the method, not buried.
*Effort:* days per cell once the P2 pipeline exists.

**P4 - Structured existence search on the smallest open cells.**
*Task:* orthogonal arrays and their irredundant variants; graph states over $\mathbb{Z}_d$ and Galois rings; 2-unitary/multiunitary ansätze with local-unitary orbit search (the AME$(4,6)$ pattern); stabilizer and near-stabilizer ansätze over mixed alphabets; nonlinear seesaw with validated-numerics lift (interval existence test, then algebraic reconstruction).
*Certificate:* as section 2.1; any exact new state decides a cell positively and is a headline.
*Effort:* open-ended; run as a continuous background search with logged coverage.

**P5 - A new general theorem shrinking $U$.**
*Task:* a parametric result - a new construction family, or a new enumerator-type obstruction - deciding several cells or an infinite family at once; e.g., lifting the AME$(4,6)$ mechanism to other non-prime-power $d$.
*Certificate:* proof for the family plus exact verification on each finite instance touched.
*Value:* strongest realistic outcome short of full resolution.

**P6 - Full resolution:** every cell of the frozen $U$ decided per section 2.

Honest calibration: unlikely in one session; P1–P3 are realistic, and P4 carries genuine upside since the AME$(4,6)$ discovery validated exactly that search pattern.

## 4. Known results and prior art

- Code equivalence and bounds: AME as pure $((n, 1, \lfloor n/2\rfloor+1))_d$ codes; Scott (2004) - bounds and qubit exclusions via LP/shadow machinery; Rains' shadow enumerators (~1998–2000).
- Qubits fully decided: AME$(n,2)$ exists iff $n \in \{2,3,5,6\}$.
- AME$(4,2)$ nonexistence: Higuchi–Sudbery (2000).
- AME$(7,2)$ nonexistence: Huber–Gühne–Siewert (2017), semidefinite/weight-enumerator proof.
- Qubit $n \ge 8$ exclusions: shadow/LP bounds (Rains ~1999–2000; Scott 2004).
- Quantum MacWilliams identities and further nonexistence machinery: Huber–Eltschka–Gühne–Siewert (~2018).
- Constructions: Helwig–Cui and collaborators (~2012–2013), stabilizer/graph-state constructions and large-$d$ existence thresholds; Goyeneche–Życzkowski (~2014), orthogonal arrays and $k$-uniform states; Goyeneche–Alsina–Latorre–Riera–Życzkowski (~2015), combinatorial designs; the Reed–Solomon/MDS route for prime powers $d \ge n-1$ (standard; verify exact thresholds per parity of $n$).
- AME$(4,6)$ exists: Rather–Burchardt–Bruzda–Rajchel-Mieldzioć–Lakshminarayan–Życzkowski (2021), via a 2-unitary matrix of order 36 ("quantum 36 officers"); classically, Euler's problem has no solution at order 6 (Tarry, ~1900), which blocks only minimal-support constructions.
- Open-table tradition: the maintained Huber–Wyderka table of AME existence (online), and the corresponding entry in the community open-problem lists. The precise current $U$ must be pulled and verified at session start; do not trust this prompt or memory for it (verify).
- Application context for perfect tensors: holographic codes, Pastawski–Yoshida–Harlow–Preskill (2015).

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

**Exact marginal checker first.**

- A standalone tool (SageMath/Python, plus an independent C++ implementation): input exact amplitudes (rational/cyclotomic), output exact verification of all balanced marginals.
- Everything else plugs into it. Cost: trivial for $d^n \lesssim 10^7$; exploit sparsity and stabilizer structure beyond.

**Enumerator pipeline (nonexistence).**

- Implement Shor–Laflamme enumerators, local-unitary symmetry reduction, the quantum MacWilliams transform, and shadow inequalities in SageMath over $\mathbb{Q}$.
- LP in exact rational arithmetic (exact simplex; GLPK-exact/QSopt-ex class, or hand-rolled over $\mathbb{Q}$); SDP levels in SDPA-GMP with rational rounding and exact $LDL^T$ verification.
- The relaxations are small (polynomial in $n$, independent of $d^n$): single workstation, minutes to hours per cell.
- Failure mode: relaxation feasible for genuinely open cells - escalate hierarchy level, or add code-theoretic side constraints, each addition accompanied by a written soundness proof.

**Combinatorial search (existence).**

- GAP plus custom C++ for orthogonal arrays and difference schemes; SageMath for graph states over $\mathbb{Z}_d$ and Galois rings.
- For 2-unitary searches: the nonlinear seesaw iteration used in the AME$(4,6)$ discovery (alternate unitarity and duality projections), reimplemented with convergence logging and many restarts.
- Candidate hits go to validated lift: interval-Newton existence proof in Arb, then LLL/algebraic reconstruction (Pari/GP) to exact entries where structure permits.
- Failure modes: seesaw stagnation at nonzero defect (expected for truly nonexistent cells - never evidence of nonexistence); lift failure for solutions with no small algebraic presentation (report as unresolved numerics, never as existence).

**Bookkeeping discipline.**

- The frozen $U$ and every cell's status transitions live in a version-controlled ledger; each transition carries its certificate.

**Workstation budget.**

- P1–P3: fully single-workstation.
- P4: benefits from a small cluster for seesaw restarts, but is feasible locally at reduced coverage.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** Marginal checks, enumerator LPs, and dual certificates in rational or cyclotomic arithmetic; interval arithmetic with directed rounding only inside validated-existence lifts; floating point confined to exploration (seesaw, warm starts).
2. **Independent verification.** The exact marginal checker in two independent implementations (SageMath and C++), compared bit-for-bit on every claimed state; nonexistence certificates re-checked by a standalone rational-arithmetic verifier that knows nothing of the solver; a written soundness memo for every relaxation and every added side constraint.
3. **Reproducibility.** Seeds and schedules for all search runs; solver versions and precision settings; SHA-256 manifest over the table ledger, certificates, states, and code; a driver that re-verifies any cell's dossier from the manifest alone.
4. **Preservation.** All construction/search source, failed searches with their parameters, and superseded certificates preserved; the frozen $U$ and its provenance are part of the permanent record; anything discarded is declared rather than obscured.
5. **Honest reporting.** The report opens with which cells of $U$ were decided and to what standard; distinguishes re-verification (P1–P2) from new results (P3–P5); and never reports numerical near-states or feasible relaxations as decisions.
