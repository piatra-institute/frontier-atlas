# PROMPT FOR EXACT FORMULA SIZE OF EXPLICIT SMALL BOOLEAN FUNCTIONS

## Certified exact De Morgan / \(B_2\) formula sizes and DRAT-verified small formula lower bounds

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 20 of 50
**Area:** complexity & communication
**Modes:** `[search]` `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Formula size - the number of leaves in a Boolean formula - is the model in which the strongest explicit lower bounds for general (non-monotone) computation live, yet the frontier is famously stuck: the best explicit De Morgan formula lower bound is \(n^{3-o(1)}\) (Håstad's shrinkage bound for Andreev's function, with Tal's lower-order refinement), and superlinear-versus-cubic is the whole visible range. Asymptotic progress is a proof problem; but the **exact** formula size of *specific small functions* is a decidable optimization that SAT-based exact synthesis solves outright, and every such exact value carries a machine-checkable optimality proof: a satisfying assignment gives an optimal formula, and a DRAT/LRAT-checked UNSAT proof for size \(s-1\) certifies the matching lower bound. The certifiable product is a table of exact formula sizes for explicit small functions, each with a construction and a checked lower-bound proof, plus any verified small lower bound for a targeted hard function. The on-machine verifier is a formula evaluator plus a DRAT/LRAT checker. A heuristic small formula with no optimality proof, an unreplayable solver run, or an asymptotic gesture where an exact value is asked, is a partial result.

## 1. Exact problem statement

A **De Morgan formula** over inputs \(x_1,\dots,x_n\) is a binary tree whose leaves are labelled by literals \(x_i\) or \(\overline{x_i}\) and whose internal nodes are labelled \(\wedge\) or \(\vee\). Its **size**

\[
L(f)=\min\{\ \#\text{leaves}(\phi)\ :\ \phi\ \text{is a De Morgan formula computing}\ f\ \}
\]

counts the **leaves** in a smallest such formula. A **\(B_2\)-formula** allows every one of the \(16\) binary Boolean gates at internal nodes; its leaf-size is \(L_{B_2}(f)\). We also record **formula depth** \(d(f)\) (tree height) and, for reference, circuit size (DAG, shared subformulas).

**Adopted primary measure.** Exact **De Morgan leaf-size** \(L(f)\) is the primary target (this is the measure of the classical lower bounds); \(L_{B_2}(f)\) and depth are recorded as companions. Negations are free at the leaves in the De Morgan model (De Morgan normal form), so \(L\) counts literal-leaves only. The measures are related by

\[
L_{B_2}(f)\ \le\ L(f),\qquad
\mathrm{size}_{\text{circuit}}(f)\ \le\ L(f),\qquad
d(f)\ \ge\ \log_2 L(f),
\]

so a De Morgan value bounds the \(B_2\), circuit, and depth values, and each is reported under its own model.

**The open landscape (context).** For an *explicit* \(f\),

\[
L(f)=n^{3-o(1)}
\]

is the best asymptotic lower bound; no explicit family is known to need \(n^{3+\varepsilon}\), and even \(\omega(n^{3})\) is open - the Karchmer–Wigderson / KRW composition programme aims here. This prompt does **not** target the asymptotic frontier; it targets **exact \(L(f)\) for specific small \(f\)** and **verified lower bounds at concrete small \(n\)**, where the problem is a finite, certifiable computation.

**The exact question (adopted here).** For a named function \(f\) on \(n\) inputs, determine \(L(f)\) (and \(L_{B_2}(f)\)) **exactly**: the least \(s\) such that a size-\(s\) formula computes \(f\) and no size-\((s-1)\) formula does.

**Starting from the prompt alone.** A reader builds \(f\)'s \(2^n\)-bit truth table from its definition, and for any candidate formula evaluates it on all \(2^n\) inputs to check correctness and counts leaves to check size - so both the upper bound (a formula) and the search encoding are reconstructable from the object.

## 2. Resolution standard

An exact \(L(f)\) is resolved only in **certified two-sided** form:

- **Upper bound:** an explicit formula of size \(s\), serialized as a tree, replayed by an independent evaluator on all \(2^n\) inputs to confirm it computes \(f\), with leaf-count \(=s\).

- **Lower bound (the certified core):** a **DRAT or LRAT proof**, checked by an independent proof checker, that the SAT encoding of "there exists a De Morgan formula of size \(s-1\) computing \(f\)" is UNSAT - establishing \(L(f)\ge s\). The encoding (variables for tree shape, gate/leaf labels, and the propagation of truth values) is part of the artifact and its faithfulness to \(L\) is argued.

Named certified form: **SAT exact synthesis with a DRAT-checked optimality proof**.

**Not accepted as resolution.**

- A small formula found by heuristic minimization with no proof that nothing smaller exists - an upper bound only.

- A solver's "UNSAT" claim without a DRAT/LRAT proof passed through an independent checker.

- A lower bound argued from an asymptotic shrinkage/degree bound where an *exact* small value is requested (asymptotics never give the exact leaf count).

- An encoding whose correspondence to De Morgan leaf-size is not justified (e.g. counting internal nodes, or silently allowing shared subformulas, which is circuit size, not formula size).

- An unreplayable run: encoding, solver version, and proof file not preserved and re-checkable.

- Conflating \(L\) (De Morgan) with \(L_{B_2}\) or with circuit size - each must be reported under its own model.

## 3. Graded partial-result targets

- **P1 - Verified synthesis + checker pipeline.** Implement the "formula of size \(\le s\)" SAT encoding (both De Morgan and \(B_2\)), a formula evaluator, and a DRAT/LRAT checking step; reproduce known exact \(L\) for tiny functions (all \(n\le3\) functions, small symmetric functions).
  *Certificate:* optimal formulas + DRAT-checked UNSAT at \(s-1\) for each.

- **P2 - Exact \(L\) census for \(n=4\).** Compute exact De Morgan leaf-size for a canonical representative of every NPN class of \(4\)-input functions; tabulate against \(L_{B_2}\) and depth.
  *Certificate:* NPN class-count gate; per-class formula + DRAT lower-bound proof; independent evaluation.

- **P3 - Targeted small functions.** Exact \(L\) and \(L_{B_2}\) for named families at small \(n\): \(\mathrm{PARITY}_n\), \(\mathrm{MAJ}_n\), thresholds \(\mathrm{TH}^n_k\), small multiplexers/`MUX`, small instances of Andreev-type functions.
  *Certificate:* two-sided certified per instance; comparison to known formulas (e.g. \(L(\mathrm{PARITY}_n)=n^2\) small cases - verify and certify).

- **P4 - Push \(n=5\) selectively.** Exact \(L\) for chosen \(5\)-input functions (not the full census) where the SAT search closes, reporting the largest \(s\) whose lower bound is DRAT-verified.
  *Certificate:* formula + DRAT proof + solver/resource log.

- **P5 - A verified small lower bound for a hard target.** For a function conjectured hard (a small Andreev instance, an \(\mathrm{MAJ}\)-composition), obtain the strongest **DRAT-certified** lower bound \(L(f)\ge s\) reachable, even if the exact value is not closed.
  *Certificate:* DRAT-checked UNSAT at size \(s-1\); explicit gap to the best known upper bound.

- **P6 - Depth and \(B_2\)-vs-De Morgan small data.** Tabulate exact formula depth and the exact \(L/L_{B_2}\) ratio across the census, contributing certified small-case data on the De Morgan-vs-\(B_2\) gap.
  *Certificate:* certified exact sizes/depths; ratio table with witnesses.

- **P7 - Certified formula-vs-circuit small gap.** For census functions where the exact circuit size is also known (from the sister circuit-size program), tabulate the exact \(L(f)/\mathrm{size}_{\text{circuit}}(f)\) ratio at small \(n\), giving certified data on the cost of forbidding subformula sharing.
  *Certificate:* certified exact formula and circuit sizes; ratio table with witnesses.

## 4. Known results and prior art

- **Shrinkage and the cubic bound.** Håstad (\(\approx\)1998, verify): De Morgan formulas shrink by \(\tilde\Theta(p^2)\) under \(p\)-random restrictions, giving \(L(\text{Andreev})=\tilde\Omega(n^3)\) - the state of the art for explicit functions. Andreev's function (\(\approx\)1987, verify). Subbotovskaya (\(\approx\)1961, verify): the original shrinkage exponent \(1.5\), giving \(n^{1.5}\).

- **Lower-order refinements.** Tal (\(\approx\)2014, verify): \(L(\text{Andreev})=\Omega(n^3/(\log n)^2\log\log n)\), essentially optimal for that function; reproved via Karchmer–Wigderson by Dinur–Meir (\(\approx\)2016, verify). Tal's "Formula lower bounds via the quantum method" (STOC 2017, verify). Cubic \(\mathsf{AC}^0\) formula bounds via shrinkage under projections (arXiv 2012.02210, verify).

- **KRW composition programme.** Karchmer–Raz–Wigderson conjecture (\(\approx\)1995, verify) - a route to \(n^{3+\varepsilon}\) and beyond; Dinur–Meir information-complexity approach (verify). Not a small-case target; context only.

- **Exact synthesis, small functions.** Knuth (TAOCP vol. 4A, verify) computed exact circuit/formula complexity of all functions in \(B_4\) and \(B_5\); SAT-based exact synthesis is standard (Soeken–Mishchenko–De Micheli line, "SAT-based exact synthesis," \(\approx\)2018–2020, verify; Kulikov's SAT-based circuit local improvement, arXiv 2102.12579, verify). Finding exact sizes in \(B_6\) is already at the edge of feasibility (verify).

- **Formula sizes of specific functions.** \(L(\mathrm{PARITY}_n)=n^2\) in the De Morgan model (Khrapchenko lower bound, \(\approx\)1971, verify) - a clean certified target at small \(n\); Khrapchenko's method gives exact small values for several functions.

- **Boolean circuit simplification tooling.** Recent SAT-based simplifiers and local-improvement engines (e.g. "Simplifier: a new tool for Boolean circuit simplification," arXiv 2503.19103, verify) provide strong heuristic *upper* bounds and good starting points, but supply optimality only when paired with a DRAT-checked infeasibility at one size smaller.

**Status as of mid-2026 - re-verify against the current literature before starting any session.**

## 5. Attack plan

**`[search]`/`[cert]` - SAT exact synthesis with proof logging.** Encode "there is a De Morgan formula with \(\le s\) leaves computing \(f\)" as CNF with the following variable groups:

- **shape:** a binary tree of \(s\) leaves and \(s-1\) internal nodes (fixed or selected among canonical shapes);

- **labels:** a gate label per internal node (\(\wedge/\vee\) for De Morgan, one of all \(16\) for \(B_2\)) and a literal label \(x_i/\overline{x_i}\) per leaf;

- **propagation:** Tseitin-style value variables carrying each node's output on each of the \(2^n\) input rows, constrained so the root equals \(f\) on every row.

The search over \(s\) obeys

\[
L(f)=\min\{\,s:\ \text{encoding}(s)\ \text{is SAT}\,\},
\qquad
\text{UNSAT}(s-1)\ \Rightarrow\ L(f)\ge s .
\]

Solve with `kissat`/`CaDiCaL`/`CryptoMiniSat`; binary-search \(s\). **Emit the DRAT proof of the UNSAT at \(s-1\) and run it through an independent DRAT/LRAT checker** (`drat-trim`/`lrat-check`). Add symmetry-breaking (canonical tree shape, leaf ordering) to shrink the search, and prove any symmetry-breaking clause sound.

**`[search]` - enumeration for the census.** NPN canonical generation for the \(n=4\) census (class-count gated), each representative run through the synthesis pipeline.

**Cross-checks.** Compare small exact values against Knuth's tables and Khrapchenko's formula-size bounds; use an exact-synthesis framework (`percy`/mockturtle, verify) as a second implementation.

**Tools.** `kissat`/`CaDiCaL`/`CryptoMiniSat` with DRAT; `drat-trim`/`lrat-check`; custom C++ for the encoding and the formula evaluator; `SageMath` for NPN canonicalization.

**One-workstation scope.** \(n\le4\) exact \(L\): routine; \(n=5\) selected functions: hours-to-days, the UNSAT proofs at the optimal size being the expensive part; \(n=6\): only special functions, and DRAT proofs may be very large.

**Failure modes.** The propagation encoding has \(\Theta(2^n\cdot s)\) clauses - memory-bound past \(n\approx6\); an unsound symmetry-breaking clause silently inflates the lower bound (each must be justified or its DRAT proof will not check against the original encoding); a solver's UNSAT with no proof is not a lower bound; confusing leaf-count with node-count or admitting shared subformulas changes the model.

## 6. Verification and auditability requirements

1. **Exact or certified computation.** Every exact \(L(f)\) is two-sided: an explicit formula (evaluated on all \(2^n\) inputs) and a **DRAT/LRAT-checked** UNSAT proof at size \(s-1\). No lower bound rests on an unchecked solver claim; no upper bound rests on an unevaluated formula.

2. **Independent verification.** A standalone formula evaluator (separate from the encoder) confirms each formula computes \(f\) and counts its leaves; an independent DRAT/LRAT checker validates every UNSAT proof; a second exact-synthesis implementation re-derives headline values.

3. **Reproducibility.** Truth-table and NPN conventions, the exact CNF encoding (with the leaf-size correspondence argument), symmetry-breaking clauses and their soundness, solver and checker versions, and seeds are recorded; a SHA-256 manifest covers every CNF, formula, and proof file; any prior exact size or lower bound being matched/improved is cited with source and access date.

4. **Preservation.** Encoder, evaluator, DRAT proofs, and solver logs are part of the record; large proof files are retained or their loss stated explicitly.

5. **Honest reporting.** The report states, per function and per model (\(L\), \(L_{B_2}\), depth), whether the value is exact (both sides certified) or only a bracket, whether the lower bound is DRAT-verified, and it never presents a heuristic minimized formula as an exact formula size, nor an asymptotic bound as an exact small-case lower bound.
