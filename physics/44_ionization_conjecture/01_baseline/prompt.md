# PROMPT FOR PROVING THE IONIZATION CONJECTURE

## Maximum negative ionization of nonrelativistic Coulomb atoms, with Hund's first rule as companion target

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 44 of 50 (Tier 4)
**Source:** top-50 list #20, category B (rigorous many-body and condensed matter)
**Modes:** `[proof]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

Chemistry knows that a neutral atom binds at most one or two extra electrons; the many-body Schrödinger equation has never been made to say so.
The ionization conjecture asserts that a fixed nucleus of charge $Z$ binds at most $Z+C$ electrons for a universal small constant $C$ (strong form: $C=1$), while the best unconditional bounds remain $N<2Z+1$ (Lieb 1984) and $N<1.22\,Z+3Z^{1/3}$ (Nam 2012) - for hydrogen these say only that $\mathrm{H}^{2-}$ does not exist.
The conjecture is proven in Hartree–Fock theory (Solovej 2003) and in Thomas–Fermi-type theories, so the obstruction is genuinely many-body correlation.
This is a Tier 4 `[proof]` problem: full resolution is unlikely in a session and the graded targets - certified small-atom spectral enclosures in the Yan–Drake precision tradition, certified sharpening of Lieb's and Nam's optimization steps for small $Z$, formalization of the Hartree–Fock proof, and a rigorous run at Hund's first rule for a real atom - are the goal.
The complete resolution defined in section 2 is the target standard; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

**Hamiltonian.** For nuclear charge $Z>0$ (fixed, infinite mass) and $N$ electrons,

\[
H(N,Z)\;=\;\sum_{i=1}^{N}\Big(-\tfrac12\Delta_{x_i}-\frac{Z}{|x_i|}\Big)\;+\;\sum_{1\le i<j\le N}\frac{1}{|x_i-x_j|}
\]

acting on the fermionic space $\mathcal{H}_N=\bigwedge^{N} L^2(\mathbb{R}^3;\mathbb{C}^{q})$, $q=2$ (spin), in standard Hartree atomic units ($\hbar=m_e=e=1$, kinetic term $-\tfrac12\Delta$).
The mathematical literature (Lieb, Nam, Solovej) often uses $-\Delta$; all cited constants must be converted explicitly to this convention before use - convention drift is a real error source here.
Ground-state energy $E(N,Z)=\inf\operatorname{spec}_{\mathcal{H}_N}H(N,Z)$; $E(0,Z)=0$. The HVZ theorem locates the essential spectrum:

\[
\operatorname{ess\,spec}\,H(N,Z)\;=\;[\,E(N-1,Z),\ \infty),
\]

so *binding*, $E(N,Z)<E(N-1,Z)$, implies existence of a ground state. Define the maximum electron number

\[
N_c(Z)\;=\;\max\{N:\ E(N,Z)<E(N-1,Z)\}.
\]

(Monotonicity subtleties: adopt this definition; Zhislin 1960 gives $N_c(Z)\ge \lceil Z\rceil$ for integer-compatible $Z$, i.e. binding for all $N<Z+1$.)

**Ionization conjecture (adopted forms).**

- **Weak form:** there is a universal constant $C$ (independent of $Z$) with $N_c(Z)\le Z+C$ for all $Z\ge1$.
- **Strong form:** $N_c(Z)\le Z+1$ for all real $Z\ge1$ (no atomic dianions).

Both are open for every formulation of "universal"; even $N_c(Z)\le Z+o(Z)$ with explicit rate beyond the known $O(Z^{5/7})$-type asymptotics (verify exponent attribution in section 4) is open territory at the level of constants.
Real (non-integer) $Z$ is the natural analytic setting; claims must state whether they hold for all real $Z\ge1$ or only integers.

**Reference values (engineering ground truth, standard a.u.; none of these is certified - certifying the first two is target P1).**

- $E(1,Z)=-Z^2/2$ exactly (hydrogenic).
- $E(2,2)\approx-2.903724377$ (helium; Hylleraas-tradition variational values, Yan–Drake / Schwartz).
- $E(2,1)\approx-0.527751016$ ($\mathrm{H}^-$), giving the hydrogen electron affinity $\approx0.0277510$.
- Carbon term gaps (experimental, NIST tables - verify): $^3P\!-\!^1D\approx0.0464$, $^3P\!-\!^1S\approx0.0986$.

**Companion target (Hund's first rule).** For a fixed atom (fixed integer $Z=N$) with an open shell - carbon ($Z=6$, configuration $2p^2$) is the first fully nontrivial case - prove from $H(N,Z)$ alone that the ground state has the maximal spin multiplicity of the configuration: for carbon, that the ground level is a spin-triplet ($^3P$ below $^1D$ and $^1S$). No rigorous derivation at physical $Z$ exists for any open-shell atom; the known results are perturbative in the isoelectronic limit $Z\to\infty$ at fixed $N$ (Friesecke–Goddard 2009).

## 2. Complete-resolution standard

Complete resolution of the main problem is a proof of the weak form: an explicit universal $C$ and a complete proof that $N_c(Z)\le Z+C$ for all $Z\ge1$ on $\bigwedge^N L^2(\mathbb{R}^3;\mathbb{C}^2)$, with every computer-assisted step certified per section 6.
The strong form $C=1$ is the ideal; any universal $C$ (even $C=10$) meets the standard.
Complete resolution of the companion is a proof of the $^3P$ ground level of the carbon Hamiltonian $H(6,6)$ (or of Hund's first rule for any atom with $N\ge5$), unconditional at the physical parameter values.

**Not accepted as resolution:**

- Bounds of the form $N_c\le(1+\epsilon)Z+C_\epsilon$ with $\epsilon>0$ (improvements of Nam's $1.22$ are P-targets, not resolutions).
- The conjecture proven in Hartree–Fock, Thomas–Fermi, Thomas–Fermi–Weizsäcker, Müller, or any density-functional/reduced model (all either done or not the question).
- Asymptotic statements $N_c(Z)-Z=O(Z^{a})$ without universal-constant control at small $Z$ (valuable, but partial).
- Bosonic or spinless variants; smeared nuclei; pseudo-relativistic or confined modifications.
- Hund's rule in the $Z\to\infty$ isoelectronic limit (known), in restricted variational subspaces (e.g. within the $1s^22s^22p^2$ configuration space only), or from non-certified numerics.
- A bound for one specific $Z$ (or finitely many) presented as the universal statement - small-$Z$ theorems are P-targets and must be labeled as such.
- Numerical evidence of any precision, for either target, without rigorous error control.

## 3. Graded partial-result targets

Tier 4 calibration: expect the session's value to come from P1–P4; P5–P6 are stretch.

- **P1 - Certified helium-class enclosures (toolchain validation).**
  Two-sided certified enclosures of $E(2,2)$ (helium) and $E(2,1)$ ($\mathrm{H}^-$), using Hylleraas-type bases with *exact rational* matrix elements (the needed integrals have closed forms; assemble in exact arithmetic), variational upper bounds by interval generalized-eigenvalue computation, and lower bounds via Temple/Lehmann–Goerisch with certified $\langle H^2\rangle$.
  Target width $\le10^{-5}$ Hartree; compare against Yan–Drake-tradition values as (non-certified) ground truth.
  A certified $E(2,1)<E(1,1)=-\tfrac12$ *proves* $\mathrm{H}^-$ binds - a complete, checkable mini-theorem.
  *Certificate:* exact matrix-element tables plus interval eigenvalue transcripts, with an independent checker re-verifying the variational inequality from the raw matrices.
- **P2 - Certified sharpening of Lieb's bound at small $Z$.**
  Lieb's 1984 argument ($N<2Z+1$) has quantifiable slack.
  Localize the slack (the $\langle |x_i|^{-1}\rangle$ vs. repulsion comparison), and optimize the auxiliary inequalities with certified computations targeting concrete small-$Z$ statements - the flagship goal: $N_c(2)\le3$ (currently Lieb gives only $N_c(2)\le4$).
  Any certified improvement of $N_c(Z)$ for one specific small $Z$ is a standalone theorem, publishable on its own.
  *Certificate:* the improved inequality chain written in full, with each auxiliary spectral or integral quantity enclosed by interval arithmetic and independently re-checked.
- **P3 - Certified reproduction and improvement of Nam's coefficient.**
  Re-derive Nam 2012 ($N_c<1.22Z+3Z^{1/3}$) to its final finite-dimensional optimization; certify the $1.22$; then search the same inequality family (choices of weight functions in the Benguria–Lieb-type moment argument) for a certified smaller coefficient.
  Machine-checkable ground truth throughout; even $1.21$ is a frontier move. *Certificate:* as P2.
- **P4 - Hartree–Fock proof: explicit constant and partial formalization.**
  Solovej's 2003 HF proof yields a universal but untracked constant.
  (a) Extract an explicit numerical $C^{\mathrm{HF}}$ by making every step quantitative, certifying the computational lemmas; (b) formalize in Lean 4 a self-contained core component (candidate: the semiclassical/TF outer-region comparison lemma, or Lieb's $2Z+1$ argument itself, which is short and essentially algebraic after one integration-by-parts identity).
  *Certificate:* compiling Lean artifact for (b); fully explicit constant chain for (a).
- **P5 - Hund's first rule for carbon, certified-computational route.**
  Strategy: certified upper bound on the $^3P$ energy (symmetry-adapted correlated basis, exact matrix elements) plus certified *lower* bounds on the lowest $^1D$/$^1S$-symmetry energies (Lehmann–Goerisch in the corresponding symmetry sectors - the spin-spatial symmetry decomposition of $\bigwedge^6$ makes the sectors well-defined).
  Needed separation: the physical $^3P$–$^1D$ gap is $\approx1.26$ eV $\approx0.046$ Hartree; certified 6-electron lower bounds at that accuracy are at the edge of feasibility - be honest that this may fail, and report the achieved enclosure widths regardless.
  Success would be the first rigorous Hund's-rule statement for a real atom.
- **P6 - Conditional structure theorems.**
  Prove implications of the form: if the ground-state one-body density satisfies an explicit (in principle checkable) decay or screening estimate uniformly in $Z$, then $N_c(Z)\le Z+C$.
  Sharpen the known heuristic screening picture into precise conditional theorems, isolating the exact missing estimate.
  *Certificate:* complete proofs; the value is the precise reduction, stated so that future certified computations could discharge the hypothesis for specific $Z$.

## 4. Known results and prior art

- Zhislin 1960: binding for $N<Z+1$ (existence side).
- Ruskai 1982; Sigal 1982–1984: first finiteness bounds $N_c(Z)=O(Z)$-type (verify exact forms).
- Lieb 1984: $N_c(Z)<2Z+1$ for all $Z$ - one page of beautiful algebra; implies $\mathrm{H}^{2-}$ unbound.
- Lieb–Sigal–Simon–Thirring 1988: asymptotic neutrality $N_c(Z)/Z\to1$.
- Fefferman–Seco ~1990 and Seco–Sigal–Solovej 1990: quantitative excess-charge asymptotics $N_c(Z)\le Z+O(Z^{a})$ with $a=5/7$ attributed in this tradition (verify the exponent and to which paper it belongs before citing).
- Nam 2012 (Comm. Math. Phys.): $N_c(Z)<1.22\,Z+3Z^{1/3}$ - current best linear coefficient.
- Solovej 2003 (Ann. of Math.): ionization conjecture in Hartree–Fock theory, $N_c^{\mathrm{HF}}\le Z+C$ universal.
- Lieb–Simon 1977: Thomas–Fermi ($N_c^{\mathrm{TF}}=Z$); Benguria–Lieb 1985: TFW binds at most $Z+C$; Frank–Nam–Van den Bosch 2018: ionization bound in Müller theory (verify scope).
- Benguria–Lieb 1983 / Solovej ~1990s: bosonic atoms bind $\sim t_cZ$ with $t_c\approx1.21$ - shows fermionic statistics is not the mechanism behind $1.22$-type coefficients being $>1$; instructive contrast.
- Hill 1977: proof that $\mathrm{H}^-$ has exactly one bound state (verify) - the model example of a rigorous small-atom spectral statement.
- Yan–Drake 1990s–2000s (and C. Schwartz 2006): ultra-high-precision Hylleraas-type helium/lithium energies - variational upper bounds of reference quality; not interval-certified, hence "ground truth" only in the engineering sense.
- Lehmann/Temple lower-bound methodology; Goerisch-method certified eigenvalue enclosures (Behnke–Goerisch 1990s; Plum school) - the certified-lower-bound toolbox for P1/P5.
- Friesecke–Goddard 2009 (SIAM J. Math. Anal.): ground-state term symbols, including Hund-consistent ordering, for $N\le10$ in the $Z\to\infty$ isoelectronic limit.
- Recent activity: improvements or formalizations post-2023 not known to us (verify - in particular any sharpening of Nam's coefficient).

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

`[proof]` mode with heavy certified-computation support; all listed computations fit a single workstation.

1. **Exact Hylleraas engine (P1).** SymPy/FLINT generation of closed-form integrals $\int r_1^ar_2^br_{12}^c e^{-\alpha r_1-\beta r_2}$ with rational $\alpha,\beta$; assemble $H$, $S$, and $H^2$ matrices as exact rationals; interval generalized eigenproblem in Arb (upper bounds are Rayleigh quotients - rigorous by evaluation; Temple/Lehmann–Goerisch lower bounds need a certified lower bound on the second eigenvalue - bootstrap from a small basis plus operator comparison with hydrogenic Hamiltonians).
   Expected failure mode: catastrophic conditioning of Hylleraas bases at size $\gtrsim500$ - exact arithmetic sidesteps instability but costs time; restrict basis growth, target $10^{-5}$, not spectroscopy.
2. **Lieb/Nam optimization bench (P2–P3).**
   Transcribe both proofs into explicit inequality pipelines; identify every free function/parameter; explore in floating point; certify winners in Arb.
   Expected failure mode: the slack in Lieb's argument may be structurally tied to the $2Z$ coefficient (known to be asymptotically improvable only via different methods) - small-$Z$ specialization is precisely where slack should be extractable; if $N_c(2)\le3$ resists, report the certified best coefficient achieved at $Z=2$.
3. **Symmetry-sector machinery (P5).** Build the $S,L$ symmetry-adapted 6-electron bases with exact Clebsch–Gordan/rational coefficients (sparse exact linear algebra; sector dimensions kept in the $10^4$–$10^5$ range with explicitly correlated Gaussians assembled under directed rounding - ECG matrix elements are analytic).
   Expected failure mode: certified lower bounds in the singlet sectors too weak by an order of magnitude - fall back to boron ($^2P$, $N=5$) or to reporting the conditional gap statement.
4. **Lean 4 (P4b).** Lieb's $2Z+1$ proof as formalization target: needs $\bigwedge^N$ structure, Coulomb form bounds, one IMS-free algebraic identity - no semiclassics; realistic scope.
   Expected failure mode: mathlib gaps in unbounded-form theory - formalize the finite-dimensional/quadratic-form skeleton and state the analytic inputs as tracked hypotheses if necessary, reporting exactly which remain.
5. **Convention hygiene pass.** Before any constant is certified, produce a one-page conversion table between this prompt's Hartree units and the $-\Delta$ conventions of Lieb 1984, Nam 2012, and Solovej 2003, machine-checked on the hydrogenic case.
   Expected failure mode: silent factor-of-2 or factor-of-4 drift in cited constants - the table is mandatory, not optional.
6. **Do not attempt** full many-body asymptotics ($Z^{5/7}$-type analysis) computationally; it is not workstation-shaped and not certifiable at session scale.

## 6. Verification and auditability requirements

Instantiating the five template requirements for this problem:

1. **Exact arithmetic.** Matrix elements exact rational (Hylleraas) or interval with directed rounding (ECG); all inequality-chain constants in Arb; no floating-point number appears in any claimed bound.
2. **Independent verification.** A standalone checker per claim: reads the exact matrices/certified intervals and re-verifies the final inequality (Rayleigh quotient, Temple condition, or coefficient bound) without the assembly code; dual implementations (python-flint and C/Arb) for P2/P3 final constants; Lean artifacts checked by the kernel with `#print axioms`.
3. **Reproducibility.** Basis definitions (exponents, nonlinear parameters as exact rationals), precision settings, and versions recorded; SHA-256 manifest over matrices, certificates, scripts, and Lean sources.
4. **Preservation.** Failed optimization branches in P2/P3 (weight-function families that provably cannot beat $1.22$) are findings; preserve the search space map, not only winners.
5. **Honest reporting.** The final report opens by stating that the ionization conjecture (weak and strong) remains open unless section 2 was met (expected), lists achieved P-targets with enclosure widths and exact hypotheses, and never lets an HF, conditional, restricted-sector, or asymptotic statement appear without its qualifier in the same sentence.
