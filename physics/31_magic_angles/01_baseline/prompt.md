# PROMPT FOR A RIGOROUS THEORY OF MAGIC ANGLES BEYOND THE CHIRAL LIMIT

## Flat bands in the Bistritzer–MacDonald model of twisted bilayer graphene at physical parameters

**PIATRA INSTITUTE**
**Prompt revision:** 23 July 2026
**Rank:** 31 of 50 (Tier 3)
**Source:** top-50 list #15, category B (rigorous many-body and condensed matter)
**Modes:** `[cert]`

**Method:** run under the atlas solver protocol - `../../../SOLVER.md` (be ambitious; plan then pivot; compute and check; adversarially self-verify; report honest partial results).

### Abstract

At the chiral limit of the Bistritzer–MacDonald (BM) model of twisted bilayer graphene, exactly flat bands appear at a discrete set of coupling values - the magic angles - with a complete spectral characterization: the magic values are reciprocals of the spectrum of an explicit compact operator (Tarnopolsky–Kruchkov–Vishwanath 2019; Becker–Embree–Wittsten–Zworski 2021+).
The physical model, with nonzero AA-tunneling $w_0$, has only numerically near-flat bands and essentially no rigorous theory, despite the flat bands being the mechanism behind correlated insulators and superconductivity at $\theta\approx1.1°$.
The problem is exceptionally well matched to `[cert]` mode: the operators have finitely many Fourier harmonics, truncation errors admit explicit bounds, and certified interval linear algebra can convert numerics into theorems - from certified chiral magic angles up to a proof that no exactly flat band survives at $w_0>0$.
The complete resolution defined in section 2 is the target; anything less must be reported as a partial result, never represented as a solution.

## 1. Exact problem statement

**The BM Hamiltonian.** On $L^2(\mathbb{R}^2;\mathbb{C}^4)$ (two layers × two sublattices; spin and valley are spectators), in dimensionless form,

\[
H(\alpha_0,\alpha_1)\;=\;\begin{pmatrix} \sigma\cdot D & T(z) \\ T(z)^* & \sigma\cdot D \end{pmatrix},
\qquad
\sigma\cdot D=\begin{pmatrix} 0 & 2D_{\bar z} \\ 2D_{z} & 0\end{pmatrix},
\]

with $z=x_1+ix_2$, $D_{\bar z}=\tfrac{1}{2i}(\partial_{x_1}+i\partial_{x_2})$, and interlayer tunneling

\[
T(z)\;=\;\sum_{j=0}^{2} T_j\, e^{i\langle z,\,q_j\rangle},
\qquad
T_j=\alpha_0\,\mathbb{1}+\alpha_1\big(\cos(2\pi j/3)\,\sigma_1+\sin(2\pi j/3)\,\sigma_2\big),
\]

where $q_0,q_1,q_2$ are the three moiré momentum-transfer vectors ($|q_j|=1$ after rescaling, $q_0+q_1+q_2=0$), and $\alpha_0,\alpha_1\ge0$ are the dimensionless AA- and AB-tunneling strengths; physically $\alpha_i=w_i/(v_F k_\theta)$, and decreasing twist angle $\theta$ increases $\alpha_i$.
Adopt the Becker–Embree–Wittsten–Zworski (BEWZ) normalization conventions throughout; any result must state its convention and the dictionary to physical $(\theta,w_0,w_1)$.
The Bloch–Floquet decomposition over the moiré lattice $\Lambda$ gives band functions $E_j(k;\alpha_0,\alpha_1)$, $k\in\mathbb{C}/\Lambda^*$, continuous and labeled in nondecreasing order around $E=0$.

**Chiral limit.** At $\alpha_0=0$ the Hamiltonian anticommutes with a chirality operator and block-reduces to

\[
D(\alpha_1)=\begin{pmatrix} 2D_{\bar z} & \alpha_1 U(z) \\ \alpha_1 U(-z) & 2D_{\bar z}\end{pmatrix},
\qquad
U(z)=\sum_{j=0}^{2}\omega^{j} e^{i\langle z,\,q_j\rangle},\quad \omega=e^{2\pi i/3}.
\]

**Definition (magic).** $\alpha_1$ is *magic* if the middle two bands of the chiral model are exactly flat at zero energy: $E(k)=0$ for all $k$. BEWZ theorem: there is a compact Birman–Schwinger operator $\mathcal{B}_k$ (explicit, built from $(2D_{\bar z}-k)^{-1}$ and $U$) whose nonzero spectrum is independent of $k$, such that

\[
\alpha_1 \text{ magic} \iff \alpha_1^{-1}\in \operatorname{Spec}(\mathcal{B}_k)\setminus\{0\}.
\]

The first real magic value is $\alpha_1^{(1)}\approx 0.586$ (twist $\theta_1\approx1.1°$); exact flat-band eigenfunctions are explicit in terms of theta functions (TKV 2019).
Trace identities give exact sum rules for $\sum_j \alpha_j^{-2}$ over magic values (Becker–Humbert–Zworski; verify the exact constant before use).

**The open problem.** For the physical model $\alpha_0>0$ (physical ratio $\alpha_0/\alpha_1 \approx 0.7$–$0.8$ from lattice corrugation):

- **(Q1)** Do exactly flat bands exist for any $(\alpha_0,\alpha_1)$ with $\alpha_0>0$? Conjecture: no - an obstruction proof is a real target.
- **(Q2)** Rigorous quantitative theory of near-flatness: certified bounds on the bandwidth $W(\alpha_0,\alpha_1)=\max_k E_{\mathrm{mid}}(k)-\min_k E_{\mathrm{mid}}(k)$ of the middle bands near the (perturbed) magic parameters, including at the physical ratio.

Both questions are about the single-particle BM continuum model as defined above; interaction effects, lattice relaxation beyond the fixed $(w_0,w_1)$ parameterization, and tight-binding models are out of scope except as motivation.

## 2. Complete-resolution standard

Complete resolution consists of both:

1. **(Q1) resolved:** a theorem, for an explicitly stated parameter region $\mathcal{R}\subset\{(\alpha_0,\alpha_1):\alpha_0>0\}$ that includes a neighborhood of the physical ray $\alpha_0/\alpha_1\in[0.6,0.9]$ up to at least the first magic region, proving either that no $(\alpha_0,\alpha_1)\in\mathcal{R}$ yields an exactly flat middle band, or exhibiting such a point with proof.
   The proof may be computer-assisted if every numerical step is certified per section 6.
2. **(Q2) resolved:** a rigorous asymptotic or uniform description of $\min_{\alpha_1} W(\alpha_0,\alpha_1)$ for small $\alpha_0$ (leading order with certified error), plus a certified two-sided enclosure of $W$ at one physical parameter point.

**Not accepted as resolution:**

- Floating-point band structures, however converged, as evidence for (Q1) or (Q2).
- Chiral-limit results alone (already rigorous territory) presented as progress on $\alpha_0>0$.
- Formal perturbation series in $\alpha_0$ without certified remainder bounds.
- Flat-band existence/nonexistence in modified models (extra symmetries, truncated Fourier models treated as exact, relaxed-lattice effective models) unless accompanied by a certified reduction to the BM model above.
- Statements at a single parameter point presented as covering a region (a point result is P4, valuable but partial).
- "Near-flatness" bounds with implicit constants ($W=O(\alpha_0)$ with unspecified constant) claimed as (Q2).

## 3. Graded partial-result targets

An obstruction proof for (Q1) over the full physical region is genuinely hard; the graded targets are the realistic product.

- **P1 - Certified chiral magic-angle spectrum.**
  Compute interval enclosures of the first $\ge8$ magic values $\alpha_1^{(j)}$ (real and complex) as $1/\lambda$ for $\lambda\in\operatorname{Spec}(\mathcal{B}_k)$, via Fourier truncation with explicit, proved truncation bounds (the kernel data are entire/finite-harmonic; derive explicit Hilbert–Schmidt tail estimates).
  $\mathcal{B}_k$ is non-normal: use certified Fredholm-determinant contour methods or singular-value bounds, not naive eigensolvers.
  Cross-check against the exact trace sum rules evaluated symbolically, and against the TKV theta-function flat-band eigenfunctions verified symbolically at $\alpha_1^{(1)}$.
  *Certificate:* interval enclosures with stated truncation radius and tail bound, plus the symbolic sum-rule check; independent second implementation.
- **P2 - Certified spectral structure at the first magic value.**
  Prove, by certified computation, simplicity (or the known multiplicity-two structure - verify against Becker–Humbert–Zworski) and realness of $\alpha_1^{(1)}$, with an enclosure of width $\le10^{-10}$.
  *Certificate:* winding-number/argument-principle certificates for eigenvalue counts in interval boxes.
- **P3 - Certified perturbation off the chiral limit.**
  Analytic perturbation theory in $\alpha_0$ around $(0,\alpha_1^{(1)})$: compute the leading behavior of the middle-band dispersion and of $\min_{\alpha_1}W(\alpha_0,\cdot)$ with certified error bounds for $\alpha_0\le\alpha_0^{\max}$ explicit.
  Determine the certified leading exponent $\nu$ in $W\sim c\,\alpha_0^{\nu}$ (numerics in the literature suggest the flat band breaks at some definite order - verify; establishing $\nu$ rigorously is new).
  *Certificate:* Kato-style perturbation bounds with all resolvent norms enclosed by interval arithmetic.
- **P4 - Certified bandwidth enclosure at a physical point.**
  At $(\alpha_0/\alpha_1=0.8,\ \alpha_1$ near the bandwidth-minimizing value$)$: two-sided enclosure of $W$ via interval eigenvalue computations (the full $H$ is self-adjoint - standard certified eigenproblem methods apply) at a certified $k$-grid with Lipschitz-in-$k$ bounds.
  A strictly positive lower bound on $W$ at this point proves no exactly flat band there - the first rigorous nonexistence statement at physical parameters.
  *Certificate:* per-$k$ interval enclosures, the $k$-Lipschitz lemma, and disjointness of enclosures at two $k$-points for each middle band.
- **P5 - Nonexistence over a parameter region.**
  Extend P4 from a point to a 2D parameter box via interval continuation (Krawczyk/interval-Newton over $(\alpha_0,\alpha_1)$ rectangles), yielding: no exactly flat middle band for $\alpha_0/\alpha_1\in[0.6,0.9]$, $\alpha_1\in[0.3,0.7]$ (say).
  This is a real theorem answering (Q1) on a physical region - strongest realistic target.
- **P6 - Structural obstruction proof.** A conceptual (non-exhaustive) proof that exact flatness forces $\alpha_0=0$ - e.g. via the theta-function/holomorphic structure that exists only at chirality, or a trace-identity obstruction.
  Strongest short of full resolution (it may not cover quantitative (Q2)).

## 4. Known results and prior art

- Bistritzer–MacDonald 2011: the continuum model; magic angles from numerics.
- Tarnopolsky–Kruchkov–Vishwanath 2019: chiral limit, exact flat bands, theta-function wavefunctions, $\alpha^{(1)}\approx0.586$.
- Becker–Embree–Wittsten–Zworski 2021 (PRB) and 2022 (math sequel): spectral characterization of magic angles via a compact Birman–Schwinger operator; $k$-independence; pseudospectral (non-normality) warnings relevant to certification.
- Watson–Luskin 2021: rigorous existence of the first real magic angle.
- Becker–Humbert–Zworski 2022–2024: trace/sum-rule identities, fine structure, generic simplicity, integrability aspects of the chiral model (verify which statements are proved vs. conjectured).
- Watson–Kong–MacDonald–Luskin ~2022–2023: rigorous derivation of the BM model from microscopic models (verify) - fixes the status of the model itself.
- Cancès–Garrigue–Gontier ~2023: mathematical analysis of moiré/BM-type models from DFT (verify scope).
- Physical parameter values $w_0/w_1\approx0.7$–$0.8$: Koshino et al. / corrugation literature ~2017–2018 (verify the accepted range).
- Rigorous results at $\alpha_0>0$: none known to us beyond soft continuity statements (verify - this absence is the problem).

**Status as of mid-2026 - re-verify against current literature before starting the session.**

## 5. Attack plan

`[cert]` mode; everything below fits a single workstation.

1. **Truncation infrastructure first.** The tunneling term couples momentum-lattice sites over a fixed finite stencil (three harmonics), so the Bloch fiber of $H$ is an explicit banded operator on $\ell^2(\Lambda^*;\mathbb{C}^4)$.
   Prove a clean tail lemma: for eigenvalue problems in $|E|\le E_0$, truncation to $|q|\le R$ incurs error $\le \epsilon(R)$ explicit (Combes–Thomas / Schur-complement resolvent bounds using kinetic growth vs. bounded coupling).
   This lemma is the backbone of every certificate; write it as a standalone, checkable statement.
2. **Chiral spectrum (P1–P2).** Implement $\mathcal{B}_k$ on truncated Fourier space in Arb (acb matrices); certified Fredholm determinant $\det(I-\alpha\mathcal{B}_k)$ via complex interval LU; locate zeros by interval argument-principle contours.
   Non-normality means eigenvalue condition numbers can be huge: track them, and prefer determinant/winding certificates over eigensolver output.
   Cross-validate with the self-adjoint route: $\alpha$ magic iff $0\in\operatorname{Spec}$ of the self-adjoint chiral Hamiltonian fiber for all $k$ - spot-check at random certified $k$.
3. **Self-adjoint band enclosures (P4–P5).**
   Interval symmetric eigensolvers (Arb `arb_mat` eigenvalue bounds, or Gershgorin-after-approximate-diagonalization: conjugate by a float eigenvector matrix, then certified Gershgorin on the interval remainder - standard and cheap).
   Truncations to $\sim10^3$–$10^4$ plane waves in interval arithmetic run in minutes–hours.
4. **Perturbation bounds (P3).** Compute chiral spectral gaps around the flat band with certificates; feed explicit gap enclosures into Kato perturbation series with rigorously summed tails; automate the inequality chain in a small script whose output is the final enclosure.
5. **Expected failure modes.**
- (a) Non-normal spectral instability inflating enclosures - mitigate with determinant methods and higher precision, and report pseudospectral condition data alongside every chiral enclosure.
- (b) Eigenvalue clustering near degeneracies at band crossings breaking the band-labeling argument - handle crossings by tracking spectral projectors of small rank, not individual eigenvalues.
- (c) Tail-lemma constants too pessimistic, forcing $R$ so large that interval linear algebra thrashes - iterate the lemma, not the precision.
- (d) Parameter-box subdivision blow-up in P5 - accept smaller certified boxes and report the covered region exactly; the certified-region boundary is itself a reportable finding.

## 6. Verification and auditability requirements

Instantiating the five template requirements for this problem:

1. **Exact arithmetic.** All enclosures in Arb interval/ball arithmetic with directed rounding; lattice data ($q_j$, $\omega$) as exact algebraic numbers; the truncation lemma's constants derived symbolically.
   Floating point only for exploratory band plots, never cited.
2. **Independent verification.** Each certified enclosure re-checked by a standalone verifier that reads the claimed interval, the truncation radius, and the tail lemma, and re-runs the certified linear algebra with an independent implementation (e.g. python-flint vs. C/Arb); sum-rule symbolic checks in a CAS (SymPy) independent of the numeric stack.
3. **Reproducibility.** Manifests record: truncation radius $R$, precision, contour data for argument-principle certificates, parameter boxes, library versions; SHA-256 over all inputs, code, and certificate files.
4. **Preservation.** Failed continuation boxes (P5) and rejected contours are preserved with their failure diagnostics - the boundary of what could be certified is a scientific finding about the method.
5. **Honest reporting.** The final report states up front whether (Q1)/(Q2) were resolved per section 2 (expected: no) and lists precisely which P-targets were certified, over exactly which parameter sets; single-point results are never phrased as regional; all statements carry their convention dictionary to physical $(\theta,w_0,w_1)$.
