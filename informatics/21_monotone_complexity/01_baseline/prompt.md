# PROMPT FOR EXACT MONOTONE CIRCUIT AND MONOTONE FORMULA COMPLEXITY OF SPECIFIC FUNCTIONS

## Certified exact monotone complexity of small monotone Boolean functions via SAT exact synthesis

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 21 of 50
**Area:** complexity & communication
**Modes:** `[search]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Monotone complexity is the one setting in which strong, superpolynomial lower bounds for explicit functions are actually known - Razborov's clique lower bound and its exponential strengthenings show that natural monotone functions require enormous monotone circuits. But those results are asymptotic; the **exact** monotone circuit and monotone formula complexity of *specific small functions* is largely uncomputed, and it is a finite, certifiable optimization: SAT-based exact synthesis over the monotone basis \(\{\wedge,\vee\}\) finds an optimal monotone circuit/formula and, via a DRAT/LRAT-checked UNSAT proof at one size smaller, certifies its optimality. The certifiable product is a table of exact monotone circuit sizes and monotone formula sizes for named small monotone functions (thresholds, small clique/matching functions, small monotone symmetric functions), each with a construction and a checked lower-bound proof. The on-machine verifier is a monotone-circuit evaluator plus a DRAT/LRAT checker. A heuristic monotone circuit without an optimality proof, an unreplayable solver run, or an asymptotic bound where an exact value is asked, is a partial result.

## 1. Exact problem statement

A **monotone circuit** over inputs \(x_1,\dots,x_n\) is a directed acyclic graph whose sources are the inputs and whose internal gates are \(\wedge\) (AND) or \(\vee\) (OR) of fan-in \(2\) - **no negations, no constants**. Its **size** is the number of gates. A **monotone formula** is a monotone circuit whose underlying graph is a tree (fan-out \(1\)); its **size**

\[
L_+(f)=\min\{\ \#\text{leaves}(\phi)\ :\ \phi\ \text{a monotone formula computing}\ f\ \}
\]

counts leaves. The monotone **circuit** complexity is

\[
C_+(f)=\min\{\ \#\text{gates}(C)\ :\ C\ \text{a monotone circuit computing}\ f\ \}.
\]

Only **monotone** functions (\(x\le y\Rightarrow f(x)\le f(y)\) coordinatewise) have finite monotone complexity; the target functions are all monotone.

**Adopted measures.** Two primary targets, reported separately: monotone **circuit** size \(C_+(f)\) (fan-in-2 \(\wedge/\vee\), gates counted, fan-out unrestricted so subresults are shared) and monotone **formula** leaf-size \(L_+(f)\) (tree, no sharing). Depth is a companion. Fan-in is fixed at \(2\) unless a variant is explicitly studied. Writing \(C(f)\) and \(L(f)\) for the general-basis circuit and formula sizes, the models are related by

\[
C(f)\ \le\ C_+(f),\qquad L(f)\ \le\ L_+(f),\qquad C_+(f)\ \le\ L_+(f),
\]

and for some monotone \(f\) the monotone-over-general gaps are exponential - the phenomenon the small-case data quantifies exactly.

**Named target functions.**

1. **Threshold** \(\mathrm{TH}^n_k\) (at least \(k\) of \(n\) inputs true) - monotone, small \(n\); \(\mathrm{MAJ}_n\) as the central case.

2. **Small clique functions** \(\mathrm{CLIQUE}(m,k)\) on \(\binom m2\) edge-inputs (contains a \(k\)-clique) for tiny \(m\) - the Razborov target, at sizes where exact computation is possible.

3. **Small perfect-matching / connectivity** functions on tiny graphs.

4. **Monotone symmetric** functions and small **monotone slice** functions.

**The exact question (adopted here).** For a named monotone \(f\), determine \(C_+(f)\) and \(L_+(f)\) **exactly** - the least size for which a monotone circuit/formula computes \(f\) and one size smaller is impossible.

**Starting from the prompt alone.** A reader builds \(f\)'s truth table from its definition (and checks monotonicity directly), evaluates any candidate monotone circuit on all \(2^n\) inputs to confirm correctness, and counts gates/leaves - so both the upper-bound object and the search encoding are reconstructable.

## 2. Resolution standard

An exact \(C_+(f)\) or \(L_+(f)\) is resolved only in **certified two-sided** form:

- **Upper bound:** an explicit monotone circuit/formula, serialized (gate list or tree), replayed by an independent evaluator on all \(2^n\) inputs to confirm it computes \(f\) using only \(\wedge/\vee\), with the claimed size.

- **Lower bound (certified core):** a **DRAT/LRAT proof**, independently checked, that the SAT encoding of "there is a monotone circuit (resp. formula) of size \(s-1\) computing \(f\)" is UNSAT - establishing the exact value \(s\). The encoding's fidelity to the monotone model (basis restricted to \(\wedge/\vee\), correct gate/leaf counting, DAG versus tree) is argued.

Named certified form: **SAT exact synthesis over the monotone basis with a DRAT-checked optimality proof**.

**Not accepted as resolution.**

- A monotone circuit from heuristic minimization with no proof of optimality - an upper bound only.

- A solver "UNSAT" without a DRAT/LRAT proof through an independent checker.

- A lower bound imported from Razborov-style asymptotics where an *exact* small value is asked (the approximation method gives \(\Omega(\cdot)\), never the exact gate count).

- An encoding that admits negations or constants (that is general, not monotone, complexity) or that confuses circuit size (shared DAG) with formula size (tree).

- An unreplayable run: encoding, solver version, and proof not preserved.

- Reporting \(C_+\) and \(L_+\) interchangeably - they differ (formulas forbid sharing) and each is a separate certified value.

- A size reported under an unstated fan-in convention - fan-in-2 is the adopted default, and any unbounded-fan-in variant is a different measure that must be labelled as such.

## 3. Graded partial-result targets

- **P1 - Verified monotone-synthesis + checker pipeline.** Encode "monotone circuit/formula of size \(\le s\) computing \(f\)"; build a monotone-circuit evaluator and DRAT checking; reproduce exact \(C_+,L_+\) for tiny monotone functions (all monotone \(f\) on \(n\le3\)).
  *Certificate:* optimal circuits/formulas + DRAT-checked UNSAT at \(s-1\).

- **P2 - Exact monotone census for \(n=4\).** Compute \(C_+\) and \(L_+\) for **every** monotone function on \(4\) inputs (the free distributive lattice; the Dedekind number \(D(4)=168\) counts them, the non-degenerate ones being the targets).
  *Certificate:* function count matches the known Dedekind/monotone count; per-function two-sided certified sizes.

- **P3 - Thresholds and majority.** Exact \(C_+(\mathrm{TH}^n_k)\) and \(L_+(\mathrm{TH}^n_k)\) for small \(n\) (target \(n\le6\)), including \(\mathrm{MAJ}_n\); compare against known monotone-formula constructions (the AKS-sorting-network route asymptotically - verify - but exact small values are the product).
  *Certificate:* two-sided certified per instance.

- **P4 - Small clique functions.** Exact \(C_+\) and \(L_+\) for \(\mathrm{CLIQUE}(m,k)\) at the smallest nontrivial \(m\) (e.g. \(\mathrm{CLIQUE}(4,3),\mathrm{CLIQUE}(5,3)\)), giving the first *exact* monotone complexities for the Razborov family.
  *Certificate:* two-sided certified; explicit edge-input encoding.

- **P5 - Push \(n=5\) / selected functions.** Exact monotone sizes for chosen \(5\)-input monotone functions and small matching/connectivity functions where the SAT search closes; report the largest \(s\) with a DRAT-verified lower bound.
  *Certificate:* circuit/formula + DRAT proof + resource log.

- **P6 - Monotone-vs-general gap, small data.** For functions where both this program and the general-basis program (Rank 20 / circuit-size work) have exact values, tabulate the exact monotone-vs-non-monotone size ratio at small \(n\).
  *Certificate:* certified exact sizes in both models; ratio table with witnesses.

- **P7 - Monotone depth small data.** Compute exact monotone formula depth for the threshold and small clique/matching targets and compare with the Karchmer–Wigderson-game predictions at small \(n\).
  *Certificate:* certified exact depths (two-sided via DRAT); comparison table with witnesses.

## 4. Known results and prior art

- **Razborov's clique lower bound.** Razborov (\(\approx\)1985, "Lower bounds on the monotone complexity of some Boolean functions," verify): superpolynomial monotone lower bound for CLIQUE via the approximation (sunflower) method; strengthened to exponential by Alon–Boppana (\(\approx\)1987, verify): detecting \(k\)-cliques needs monotone circuits \(\exp(\Omega((m/\log m)^{1/3}))\) for suitable \(k\). Textbook treatment: Jukna, *Boolean Function Complexity* (verify).

- **Monotone formula / depth.** Karchmer–Wigderson (\(\approx\)1990, verify): monotone formula depth via communication (the KW game); monotone-depth lower bounds for \(st\)-connectivity. Raz–Wigderson (\(\approx\)1992, verify): monotone-depth lower bound for matching.

- **Monotone circuit-vs-formula and monotone-vs-general.** Known separations: monotone functions with small general but large monotone complexity (Razborov's matching; Tardos' \(\approx\)1988 exponential monotone-vs-general gap, verify). Monotone circuits with local oracles and clique bounds (arXiv 1704.06241, verify).

- **Monotone formulas for majority.** \(\mathrm{MAJ}_n\) has monotone formulas of polynomial size - Valiant's probabilistic \(O(n^{5.3})\) construction (\(\approx\)1984, verify) and the \(O(n\log n)\)-depth AKS sorting network (\(\approx\)1983, verify) - but the *exact* small-\(n\) monotone formula and circuit sizes of \(\mathrm{MAJ}_n\) are not tabulated; the P3 census supplies them.

- **Exact synthesis (method).** SAT-based exact synthesis over restricted bases is standard (Soeken–Mishchenko–De Micheli, \(\approx\)2018–2020, verify); Knuth's exact circuit tables for \(B_4,B_5\) (TAOCP 4A, verify). Exact synthesis is routinely restricted to a chosen operator set - the monotone basis is such a restriction - so the tooling transfers directly.

- **Small monotone data.** Dedekind numbers \(D(n)\) count monotone functions (\(D(4)=168\), \(D(5)=7581\), \(D(6)=7\,828\,354\), verify); a certified table of *exact monotone complexities* across these classes is not standard and is the P2–P4 product.

**Status as of mid-2026 - re-verify against the current literature before starting any session.**

## 5. Attack plan

**`[search]` - SAT exact synthesis over \(\{\wedge,\vee\}\), with proof logging.** Encode "monotone circuit of \(\le s\) fan-in-2 gates computing \(f\)": variables select, for each gate, its two operands (inputs or lower-indexed gates) and its type (\(\wedge/\vee\)); Tseitin variables propagate each gate's value on all \(2^n\) rows; the output gate must equal \(f\) on every row. For **formulas**, forbid fan-out \(>1\) (tree constraint) and count leaves. The search obeys

\[
C_+(f)=\min\{\,s:\ \text{encoding}(s)\ \text{is SAT}\,\},
\qquad
\text{UNSAT}(s-1)\ \Rightarrow\ C_+(f)\ge s,
\]

and analogously for \(L_+\). Solve with `kissat`/`CaDiCaL`/`CryptoMiniSat`; **emit the DRAT proof of the UNSAT at \(s-1\) and check it independently** (`drat-trim`/`lrat-check`). Add sound symmetry-breaking (gate ordering, operand canonicalization) and justify each clause.

**`[search]` - monotone enumeration.** For the \(n=4\) census, enumerate monotone functions (antichains of the Boolean lattice) with the count gated against \(D(4)=168\); run each through the pipeline.

**Cross-checks.** Compare small threshold/majority values against known monotone-formula constructions; use a second exact-synthesis framework (`percy`/mockturtle restricted to \(\wedge,\vee\), verify).

**Tools.** `kissat`/`CaDiCaL`/`CryptoMiniSat` with DRAT; `drat-trim`/`lrat-check`; custom C++ for encoding, monotone enumeration, and evaluation; `SageMath` for lattice/antichain enumeration.

**One-workstation scope.** Monotone \(n\le4\) census: routine; thresholds and CLIQUE at tiny \(m\), \(n=5\): hours-to-days, with the optimal-size UNSAT proofs the bottleneck; \(n=6\): only special functions, DRAT proofs may be very large.

**Failure modes.** The propagation encoding is \(\Theta(2^n\cdot s)\) clauses - memory-bound past \(n\approx6\); an unsound symmetry-breaking clause inflates the certified lower bound (justify each, or its DRAT proof fails against the base encoding); accidentally admitting negations/constants leaves the monotone model; conflating circuit (shared) and formula (tree) sizes; the CLIQUE edge-input arity \(\binom m2\) grows fast (\(m=5\) already gives \(10\) inputs).

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every exact \(C_+(f)\) / \(L_+(f)\) is two-sided: an explicit monotone circuit/formula (evaluated on all \(2^n\) inputs, basis confirmed \(\wedge/\vee\) only) and a **DRAT/LRAT-checked** UNSAT proof at size \(s-1\). No lower bound rests on an unchecked solver claim.

2. **Independent verification.** A standalone monotone-circuit evaluator (separate from the encoder) confirms each solution computes \(f\) with the stated size and basis; an independent DRAT/LRAT checker validates each UNSAT proof; a second exact-synthesis implementation re-derives headline values; the monotone census count is gated against the Dedekind number.

3. **Reproducibility.** Truth-table and (for CLIQUE) edge-input conventions, the CNF encoding with its monotone-model correspondence argument, symmetry-breaking clauses and soundness, solver/checker versions, and seeds recorded; a SHA-256 manifest covers every CNF, circuit/formula, and proof file; any prior exact monotone size being matched/improved cited with source and access date.

4. **Preservation.** Encoder, evaluator, enumeration code, DRAT proofs, and logs are part of the record; large proof files are retained or their loss stated explicitly.

5. **Honest reporting.** The report states, per function and per model (\(C_+\), \(L_+\), depth), whether the value is exact (both sides certified) or a bracket, whether the lower bound is DRAT-verified, and it never presents a heuristic monotone circuit as an exact size, an asymptotic Razborov bound as an exact small-case value, or a monotone result under the wrong (non-monotone, or circuit-versus-formula) model.
