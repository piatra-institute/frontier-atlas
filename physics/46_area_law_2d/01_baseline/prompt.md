# PROMPT FOR THE TWO-DIMENSIONAL AREA LAW FOR GAPPED LOCAL HAMILTONIANS

## Entanglement entropy bounded by boundary length: beyond the one-dimensional proof

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 46 of 50 (Tier 4)
**Source:** top-50 list #11, category B (rigorous many-body and condensed matter)
**Modes:** `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

The area-law conjecture asserts that ground states of gapped, finite-range, bounded-strength local Hamiltonians on two-dimensional lattices have entanglement entropy across any region bounded by a constant times the boundary length. In one dimension this is a theorem (Hastings 2007), with the modern proofs running through approximate ground-state projectors (AGSPs; Arad–Kitaev–Landau–Vazirani); in two dimensions the general case is open, with the frustration-free case reportedly settled by Anshu–Arad–Gosset (c. 2022 - verify exact scope: gap hypothesis local or global, ground-space degeneracy, lattice class) after their earlier subvolume law. This is a Tier 4 prompt: no frontal assault is expected, and none should be attempted before the infrastructure targets are done. The problem earns its slot because the AGSP framework is theorem-dense, combinatorial, and unusually formalizable - the realistic products are machine-checked infrastructure (the AGSP-implies-entanglement-bound lemma, Chebyshev AGSP constructions with explicit constants), verified quantitative improvements, extensions on restricted 2D classes, and a precise citable statement of why the 1D argument fails in 2D. The complete resolution defined in section 2 is the target, and anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

Let $\Lambda_L = ([1, L] \times [1, L]) \cap \mathbb{Z}^2$, on-site dimension $d < \infty$, $\mathcal{H} = \bigotimes_{x \in \Lambda_L} \mathbb{C}^d$. A Hamiltonian

\[
H \;=\; \sum_{X \subset \Lambda_L} h_X
\]

is $(r, J)$-local if each $h_X = h_X^\dagger$ is supported on a set $X$ of diameter $\le r$, $\|h_X\| \le J$, and each site lies in at most $z$ terms; $r, J, z, d$ are constants independent of $L$. Assume a uniform spectral gap:

\[
E_1(H) - E_0(H) \;\ge\; \gamma \;>\; 0 \quad \text{for all } L,
\]

with, in the base case, a unique ground state $|\Omega_L\rangle$. For a region $A \subset \Lambda_L$ with boundary $\partial A$ (sites of $A$ adjacent to $A^c$), let $\rho_A = \operatorname{Tr}_{A^c} |\Omega_L\rangle\langle\Omega_L|$ and $S(\rho_A) = -\operatorname{Tr} \rho_A \log_2 \rho_A$ (base-2 logarithm fixed throughout; state it in every artifact).

**Target theorem (2D area law).** There exists $C = C(d, r, J, z, \gamma) < \infty$, independent of $L$ and $A$, such that for every rectangular region $A$ (strong form: every simply connected $A$),

\[
S(\rho_A) \;\le\; C\,|\partial A| .
\]

Conventions and variants:

- A bound $S(\rho_A) \le C\,|\partial A|\,\mathrm{polylog}|\partial A|$ is named "area law up to polylog" and counts as an essentially complete resolution if proved for the general gapped case; it must still be labeled exactly.
- Frustration-free means $h_X \ge 0$ and $H|\Omega\rangle = 0$; the general (frustrated) gapped case is the open target.
- Degenerate ground spaces: the theorem should hold for every state in the ground space with $C$ depending on the degeneracy; state exactly which variant is proved.

Key definition for everything below. A $(D, \Delta)$-AGSP for $(H, |\Omega\rangle)$ across a bipartition cut is an operator $K$ with

\[
K|\Omega\rangle = |\Omega\rangle, \qquad
\|K|\psi\rangle\|^2 \le \Delta \ \text{ for normalized } |\psi\rangle \perp |\Omega\rangle, \qquad
\operatorname{SR}(K) \le D,
\]

where $\operatorname{SR}$ is the operator Schmidt rank across the cut. The 1D bootstrap lemma (Arad–Landau–Vazirani style): existence of a $(D, \Delta)$-AGSP with $D \cdot \Delta \le 1/2$ implies ground-state entanglement $O(\log D)$ across the cut. Exact constants are part of every deliverable.

Entanglement conventions, fixed once:

- $S(\rho)$ is the von Neumann entropy in bits; Rényi variants $S_\alpha$ may be used internally but every headline bound is stated for $S = S_1$ (and $S_\alpha \ge S_1$ for $\alpha < 1$ conversions must be explicit).
- $\operatorname{SR}(K)$ across a cut $A : A^c$ is the minimal $D$ with $K = \sum_{j=1}^{D} L_j \otimes R_j$, $L_j$ on $A$, $R_j$ on $A^c$.
- "Cut" in 2D means the boundary between $A$ and $A^c$; its length $\ell = |\partial A|$ enters all trade-offs.

## 2. Complete-resolution standard

A complete resolution is a full proof of the Target theorem for general gapped $(r, J)$-local Hamiltonians in 2D (frustration allowed), with an explicit constant $C(d, r, J, z, \gamma)$ or an explicit polylog weakening, in a form checkable line by line. Computer-assisted steps must carry certificates and independent checkers; formalized components must compile against a pinned Mathlib version.

**Not accepted as resolution:**

- The 1D theorem, restated or re-proved, in any packaging.
- The frustration-free 2D case - if the Anshu–Arad–Gosset result verifies as complete - presented as the general case; frustration-freeness is a severe restriction and the physical conjecture concerns generic gapped systems.
- Commuting-projector or fixed-point models (string-nets, quantum doubles) presented as evidence beyond their class.
- Area laws assuming exponential decay of correlations *plus* additional unproven hypotheses (uniform approximate Markov property, bounded conditional mutual information) unless the hypothesis is itself proved from the gap.
- Numerical entropy-scaling studies (DMRG/PEPS) of example models, at any size.
- Random or generic-case statements ("for most gapped Hamiltonians").
- Subvolume bounds ($S \lesssim |A|^{c}$, $c < 1$) or super-area bounds ($S \lesssim |\partial A|^{1+\epsilon}$) represented as area laws - valuable partial results, to be labeled exactly as what they are.
- Bounds only on Rényi entropies $S_\alpha$ with $\alpha > 1$ presented as the theorem ($S_\alpha \le S_1$ for $\alpha > 1$, so such bounds are strictly weaker; $\alpha < 1$ bounds do imply $S_1$ bounds and are acceptable if stated with the conversion).
- Mutual-information or correlation-decay statements presented as entropy bounds without the (generally false in this direction) conversion proved.

## 3. Graded partial-result targets

Ordered from most accessible to strongest short of resolution; each is independently valuable and certifiable. For a Tier 4 prompt the expected session product is P1–P3 solid, P4 or P5 partial.

**P1 - Verified 1D pipeline with explicit constants.**
- Task: reconstruct the 1D area-law proof in the AGSP formalism with every constant explicit and optimized - Hamiltonian truncation near the cut, Chebyshev-polynomial AGSP with the degree/rank/shrinkage trade-off tracked in exact rational arithmetic, and the bootstrap lemma.
- Certificate: a self-contained document plus a machine-checked constant ledger (Chebyshev tail bounds certified in Arb; rank counting exact combinatorics).
- Value: the literature's constants are scattered and partly implicit; a verified ledger is reusable infrastructure and the training ground for all 2D bookkeeping.

**P2 - Lean 4 formalization of the bootstrap lemma.**
- Task: formalize (i) Schmidt decomposition and entanglement entropy across a bipartition of $\mathbb{C}^m \otimes \mathbb{C}^n$; (ii) the $(D, \Delta)$-AGSP definition; (iii) the theorem "$D\Delta \le 1/2$ implies Schmidt-coefficient decay and $S = O(\log D)$" with explicit constants.
- Certificate: a compiling Lean artifact against a pinned Mathlib commit.
- Value: bounded-scope finite-dimensional linear algebra, hard but doable; likely the first formalized theorem of entanglement theory at this level (verify no prior formalization exists) and a citable reusable component.

**P3 - Commuting and fixed-point 2D classes, unified and extended.**
- Task: write down, with complete proofs, the area law for 2D commuting-projector Hamiltonians via the structure theory of Bravyi–Vyalyi / Aharonov–Eldar (verify what the published statements actually cover - the folklore outruns the literature), including degenerate topological ground spaces, with explicit constants; extend to the widest class the structure theory permits.
- Certificate: complete proofs; a Lean formalization of the qubit commuting case is the stretch goal.
- Value: converts folklore into citable theorems and stress-tests the definitions of P2 on the one 2D class where everything is exactly solvable.

**P4 - The 2D frustration-free frontier, audited.**
- Task: take the Anshu–Arad–Gosset 2D frustration-free proof (and the subvolume predecessor), verify it line by line, extract all constants, and produce (a) an audited technical summary with any gaps or fixable errors documented, (b) the sharpest statement their method actually proves (region class; local vs. global gap; degeneracy), (c) at least one concrete strengthening - better constants, wider region class, or weaker gap hypothesis - with proof.
- Certificate: the audit document with every nontrivial estimate re-derived; the strengthening as a theorem.
- Value: the current frontier has not been independently audited at this granularity; the audit both de-risks the field's citation graph and locates the exact wall.

**P5 - The obstruction theorem.**
- Task: state and prove precise obstruction results explaining why 1D AGSP technology does not tensor to 2D. Quantify: a cut of length $\ell$ has $\|H_{\mathrm{cut}}\| = \Theta(\ell)$, Chebyshev shrinkage delivers $\Delta = \exp(-O(\mathrm{deg}/\sqrt{\ell}))$ while entanglement rank grows like $D = \exp(\Omega(\cdot))$ in the same parameters, so the win condition $D\Delta \le 1/2$ fails for the naive scheme - derive the exact trade-off inequality on $(D, \Delta, \ell, \gamma)$ that any improved 2D AGSP construction must beat, and classify which improvements would suffice.
- Certificate: theorem-grade statements with proofs; toy-model sharpness checks (below) certified.
- Value: turns folklore into the citable "win condition" - the strategic heart of this prompt and the map for all future sessions.

**P6 - Conditional 2D area laws with clean hypotheses.**
- Task: strongest short of resolution - theorems "hypothesis $\mathcal{X}$ implies the 2D area law" with $\mathcal{X}$ strictly weaker than existing inputs and independently plausible. Candidates: a 2D analogue of the 1D truncation lemma; uniform polynomial growth of relevant Schmidt vectors under coarse-graining; approximate-Markov structure of gapped ground states with certified error (note: gap $\Rightarrow$ exponential clustering, Hastings–Koma 2006 and Nachtergaele–Sims 2006, IS proved in any dimension and may be used freely).
- Certificate: each conditional theorem fully proved, hypotheses stated in a form falsifiable by future work.
- Value: maps assumption-space; each arrow is a standalone product.

## 4. Known results and prior art

- Hastings (2007): the 1D area law for gapped systems; the founding result, with exponential-in-$1/\gamma$-type constants.
- Irani (2010); Gottesman–Hastings (2010): translation-invariant 1D models with large (polynomial-in-spin) ground-state entanglement - calibrate how the constants must depend on $d$ and $\gamma$; any claimed bound violating these examples is wrong.
- Hastings–Koma (2006); Nachtergaele–Sims (2006): gap implies exponential clustering - proved in all dimensions; free input.
- Arad–Landau–Vazirani (2012); Arad–Kitaev–Landau–Vazirani (2013): the AGSP framework and the exponentially improved 1D bounds (verify the exact $d$ and $\gamma$ dependence of the best current 1D constant).
- Brandão–Horodecki (2013): 1D area law from exponential decay of correlations alone - an independent route whose 1D-specific steps should be identified in P5.
- Landau–Vazirani–Vidick (2015): algorithmic corollary (ground states of gapped 1D systems in polynomial time) - context for why AGSPs matter beyond entropy.
- Arad–Landau–Vazirani–Vidick (c. 2017): rigorous RG / rapid-mixing-adjacent refinements of the 1D machinery (verify exact contribution before citing).
- Anshu–Arad–Gosset (c. 2019): subvolume law for 2D frustration-free systems; (c. 2022, STOC): area law for 2D frustration-free spin systems (verify hypotheses precisely - this is the single most important pre-session verification task).
- Gosset–Huang and related (c. 2016+): degenerate and gapless-adjacent refinements in 1D (verify).
- Masanes (2009): area-type bounds from physical assumptions - a prototype of the P6 conditional style.
- Bravyi–Vyalyi (2003); Aharonov–Eldar (2011+): structure of commuting-projector ground spaces - the backbone of P3.
- Kuwahara and collaborators (c. 2020s): thermal area laws, long-range generalizations (adjacent; verify scope).
- Eisert–Cramer–Plenio (2010): review - orientation only, never citation for a theorem.
- Vidick and collaborators; Abrahamsen (c. 2019+): further AGSP-based results for trees and special interaction graphs (verify which exist and their exact scope).
- Hastings (2007b, "An area law for one-dimensional quantum systems") vs. later expositions: the constants differ between versions - the P1 ledger must pick one lineage and say so.
- Counterexample side: Aharonov et al. and later work on gapless/degenerate models with entropy violations of naive generalizations (verify) - useful for calibrating which hypotheses in the Target theorem are load-bearing.
- Search explicitly for post-2022 progress: frustrated 2D partial results, improved frustration-free constants, higher-dimensional frustration-free claims, and any formalization efforts.

Status as of mid-2026 - re-verify against current literature before starting the session.

## 5. Attack plan

Mode `[proof]`. This is a proof-infrastructure prompt; computation serves the proofs.

1. **Constant ledger (P1).** A worksheet (SymPy plus Arb) tracking the 1D AGSP parameters: Chebyshev degree $\ell \mapsto$ shrinkage $\Delta(\ell)$ via explicit, interval-certified Chebyshev tail bounds; truncation-induced norm errors; entanglement-rank counting $D(\ell)$ as exact combinatorics. Output: the certified minimal entropy bound the modern 1D proof yields for given $(d, J, \gamma)$. Runs anywhere. Expected failure mode: implicit constants in the source papers that resist extraction - re-derive from scratch; the re-derivation is itself a deliverable.
2. **Lean 4 targets (P2), strictly ordered.** (i) Audit Mathlib for existing Schmidt-decomposition/SVD support; (ii) entropy monotonicity under rank truncation (Eckart–Young-type step); (iii) the bootstrap lemma. Keep all spaces concrete ($\mathbb{C}^m \otimes \mathbb{C}^n$) to avoid abstraction friction. Expected failure mode: entropy lemmas (concavity, continuity) missing from Mathlib - formalize minimal bespoke versions; they are reusable and citable on their own.
3. **Audit protocol (P4).** Line-by-line re-derivation with a numbered estimate registry; every inequality either re-proved or flagged with its exact location. Cost is attention, not compute.
4. **Obstruction quantification (P5).** Symbolic worksheet for the $(D, \Delta, \ell, \gamma)$ win-condition inequality; small exact toy models - $\ell \times 2$ ladders with certified sparse diagonalization (Julia, interval certification) - to test sharpness of the rank counting. The certified toy spectra are ground truth for whether the obstruction bound is tight or slack.
5. **What not to attempt.** No open-ended search for a new 2D proof strategy before P5 is complete; no PEPS numerics as evidence of anything; Tier 4 discipline throughout - infrastructure and obstruction clarity first, opportunism second.
6. **Workstation budget.** Everything here is CPU-light; the binding resources are Lean engineering time and audit attention. Plan the session accordingly (this prompt is deliberately compute-poor and proof-rich).
7. **Order of battle.** P1 first (it trains the constant discipline); P2 and P3 in parallel after; P4 before any P6 conditional is drafted, since the audit determines which hypotheses are already theorems.
8. **Honest calibration.** The general 2D theorem has resisted the strongest groups in Hamiltonian complexity for nearly two decades; a session that delivers P1 + P2 + a sharp P5 obstruction inequality has met this prompt's bar in full. State this calibration in the report rather than apologizing for it.

## 6. Verification and auditability requirements

1. **Exact arithmetic.** All ledger constants as exact rationals or certified intervals (Arb); polynomial-approximation bounds certified, never quoted from floating-point fits; toy-model spectra interval-certified with directed rounding.
2. **Independent verification.** The constant ledger re-evaluated by an independent implementation (Python/mpmath against Julia/Arb); Lean artifacts rebuilt in clean CI against the pinned Mathlib commit; the P4 audit cross-read in a separate session against the numbered registry.
3. **Reproducibility.** Pinned versions throughout (Lean toolchain, Mathlib commit, Arb/FLINT, Julia); all worksheets, registries, and toy-model inputs under a SHA-256 manifest.
4. **Preservation.** Failed formalization branches and abandoned obstruction ansätze preserved with notes - for a Tier 4 infrastructure prompt the negative record is much of the value; anything unpreserved must be declared explicitly rather than obscured.
5. **Honest reporting.** The report opens by stating that the general 2D area law was not proved (unless it was), then lists which P-targets reached certificate standard, the exact class of 2D Hamiltonians for which an area law is now verified or audited, all Lean artifacts with their formal statements, and the sharpest proved form of the obstruction inequality. Subvolume and polylog-weakened bounds are always labeled as such, and the frustration-free/frustrated distinction is never blurred.
