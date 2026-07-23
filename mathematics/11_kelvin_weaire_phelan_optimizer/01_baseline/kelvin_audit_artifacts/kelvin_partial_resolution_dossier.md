# Kelvin and Weaire-Phelan optimizer audit

**Date:** 21 July 2026  
**Status:** Rigorous non-solution dossier. No claim of a complete resolution of the unrestricted Kelvin problem.

## 1. Verdict

For the admissible class and normalization in the supplied prompt, I did not obtain a matching global lower bound for the relaxed Weaire-Phelan foam, a lower-area certified optimizer, or a nonattainment theorem. Therefore the Kelvin problem is not resolved here.

The audit does produce four proof-level conclusions:

1. **A qualitative frustration gap:** there is a dimension-dependent constant \(\varepsilon_3>0\) such that
   \[
   \kappa_3 \ge (36\pi)^{1/3}+\varepsilon_3.
   \]
   Thus the single-cell sphere bound is not merely unattained. It is separated from the honeycomb constant by a positive universal gap.

2. **An exact flat A15 upper competitor:** the equal-volume periodic Laguerre A15 partition has
   \[
   \mathcal A_{\mathrm{A15,flat}}
   =\frac32+\frac{3\sqrt6}{2}
   +\frac{6\sqrt5-4\sqrt6-3}{2\sqrt[3]{16}}
   =5.296950417263704482\ldots.
   \]
   It is not stationary at its triple edges, so a volume-preserving periodic perturbation strictly lowers its area. Consequently
   \[
   \kappa_3<5.296950417263705.
   \]

3. **A no-go theorem for the proposed global periodic paired calibration:** on a closed torus with only prescribed phase volumes, every ordinary convex paired-calibration dual has value at most zero. It therefore cannot certify the positive perimeter of Weaire-Phelan, or of any other nontrivial torus partition, against all volume-constrained competitors.

4. **Finite-defect invariance:** the asymptotic mean-area functional is unchanged by any bounded finite-perimeter modification. Hence global optimality for this functional does not imply local minimality, Plateau regularity, or uniqueness. Those properties require a separate ground-state or compact-perturbation minimality condition.

Combining the first two points gives the rigorous qualitative bracket
\[
4.835975862049408\ldots < \kappa_3 < 5.296950417263705\ldots.
\]
The lower inequality contains an unspecified positive margin; no useful numerical value of \(\varepsilon_3\) is extracted here.

## 2. Exact sphere lower bound

Let \(E=(E_i)\) be an admissible partition, let \(Q_R=[-R/2,R/2]^3\), and write
\[
J_R=\mathcal H^2(J_E\cap Q_R).
\]
For almost every \(R\), put \(F_i=E_i\cap Q_R\) and \(v_i=|F_i|\). The trace identity for a Caccioppoli partition gives
\[
\sum_i P(F_i)=2J_R+\mathcal H^2(\partial Q_R)=2J_R+6R^2.
\]
Every \(v_i\le 1\), because each original cell has volume one. Euclidean isoperimetry gives
\[
P(F_i)\ge c_0v_i^{2/3},\qquad c_0=(36\pi)^{1/3}.
\]
Since \(0\le v_i\le1\), one has \(v_i^{2/3}\ge v_i\). Summing and using \(\sum_i v_i=R^3\),
\[
2J_R+6R^2\ge c_0R^3.
\]
Therefore
\[
\frac{2J_R}{R^3}\ge c_0-\frac6R,
\]
and hence
\[
\boxed{\kappa_3\ge(36\pi)^{1/3}=4.835975862049408\ldots.}
\]

## 3. Positive gap above the sphere value

### Theorem

There exists \(\varepsilon_3>0\) such that every admissible partition satisfies
\[
\mathcal A(E)\ge c_0+\varepsilon_3.
\]

### Proof

Assume to the contrary that a sequence of admissible partitions \(E^{(m)}\) has
\[
\mathcal A(E^{(m)})\downarrow c_0.
\]
Choose \(R_m\to\infty\), at regular radii, so that
\[
\frac{2\mathcal H^2(J_{E^{(m)}}\cap Q_{R_m})}{R_m^3}=c_0+o(1).
\]
For the fragments \(F_i^{(m)}=E_i^{(m)}\cap Q_{R_m}\), with volumes \(v_i^{(m)}\), define
\[
D_m=\sum_i\left[P(F_i^{(m)})-c_0(v_i^{(m)})^{2/3}\right]
+c_0\sum_i\left[(v_i^{(m)})^{2/3}-v_i^{(m)}\right].
\]
Both sums are nonnegative and the trace identity gives
\[
D_m=2\mathcal H^2(J_{E^{(m)}}\cap Q_{R_m})+6R_m^2-c_0R_m^3=o(R_m^3).
\]

Fix \(\eta\in(0,1)\). If \(v\le1-\eta\), then
\[
v^{2/3}-v\ge a_\eta v,
\qquad
 a_\eta=(1-\eta)^{-1/3}-1>0.
\]
It follows that fragments of volume at most \(1-\eta\) carry only \(o(R_m^3)\) total volume. Thus almost all volume lies in fragments with volume in \([1-\eta,1]\).

The sharp quantitative isoperimetric inequality supplies a constant \(C_3>0\) such that, for every finite-perimeter set \(F\),
\[
P(F)-c_0|F|^{2/3}\ge C_3|F|^{2/3}\alpha(F)^2,
\]
where \(\alpha(F)\) is the relative Fraenkel asymmetry, the normalized symmetric-difference distance from a ball of the same volume. Therefore, for every fixed \(\tau>0\), all but \(o(R_m^3)\) of the large fragments are within relative symmetric difference \(\tau\) of some ball.

Let
\[
\delta_K=\frac{\pi}{\sqrt{18}}
\]
be the maximal density of a congruent-sphere packing in \(\mathbb R^3\). Choose \(s<1\) and then \(\eta>0\) so that
\[
s^3(1-\eta)>\delta_K.
\]
For two unit-volume balls whose centers are at distance at most \(2s\) times their radius, the overlap fraction is at least
\[
\ell(s)=\frac{(2+s)(1-s)^2}{2}>0.
\]
After accounting for the small volume variation \([1-\eta,1]\), choose \(\tau\) below the corresponding positive minimum overlap. If two concentric contractions of the approximating balls, each to the fixed volume \(s^3(1-\eta)\), overlapped, then the original approximating balls would overlap by more volume than their two symmetric-difference errors can absorb. The underlying fragments are disjoint, so this is impossible. The fixed contracted balls therefore form a packing.

There are \(R_m^3-o(R_m^3)\) such balls, all contained in a cube of side \(R_m+O(1)\). Periodically replicating a slightly enlarged containing cube gives an infinite congruent-sphere packing whose density tends to at least
\[
s^3(1-\eta)>\delta_K,
\]
contradicting the Kepler sphere-packing theorem. This contradiction proves the existence of \(\varepsilon_3>0\). \(\square\)

### Limitation

The proof uses only the existence of the quantitative-isoperimetric constant \(C_3\). Tracking a practical explicit value through the stability theorem and finite-packing conversion was not completed. The conclusion is a strict universal gap, not a numerically competitive lower bound.

## 4. Exact equal-volume flat A15 competitor

### Construction

Work on the cubic torus \(\mathbb R^3/(2\mathbb Z)^3\), of volume eight. Use the eight periodic sites
\[
\begin{aligned}
&(0,0,0),\quad(1,1,1),\\
&(1/2,0,1),\quad(3/2,0,1),\\
&(0,1,1/2),\quad(0,1,3/2),\\
&(1,1/2,0),\quad(1,3/2,0).
\end{aligned}
\]
The first two are type A, and the other six are type B. Define Laguerre cells using
\[
|x-p_i|^2-w_i\le |x-(p_j+\lambda)|^2-w_j
\]
for every periodic image \(p_j+\lambda\), with
\[
w_A=0,
\qquad
w_B=\delta=\frac54-\sqrt[3]{2}.
\]

Within the relevant fixed combinatorial type, direct polyhedral integration gives
\[
V_A(\delta)=\frac{125}{128}-\frac{75}{32}\delta
+\frac{15}{8}\delta^2-\frac12\delta^3,
\]
\[
V_B(\delta)=\frac{129}{128}+\frac{25}{32}\delta
-\frac58\delta^2+\frac16\delta^3.
\]
The equal-volume equation is
\[
64\delta^3-240\delta^2+300\delta+3=0,
\]
which is exactly
\[
64\left(\delta-\frac54\right)^3+128=0.
\]
Thus \(\delta=5/4-\sqrt[3]{2}\), and
\[
V_A=V_B=1.
\]

Let \(r=\sqrt[3]{2}\). The three face-area orbits are
\[
a=\frac{\sqrt5\,r^2}{8}
\quad\text{(A-B pentagon)},
\]
\[
b=1-\frac{r^2}{4}
\quad\text{(axial B-B hexagon)},
\]
\[
c=\frac{\sqrt6(3-r^2)}{12}
\quad\text{(non-axial B-B pentagon)}.
\]
A type-A cell has boundary area \(S_A=12a\). A type-B cell has boundary area
\[
S_B=4a+2b+8c.
\]
Therefore the mean full boundary area is
\[
\begin{aligned}
U_{A15}
&=\frac{2S_A+6S_B}{8}\\
&=\frac32+\frac{3\sqrt6}{2}
+\frac{6\sqrt5-4\sqrt6-3}{2\sqrt[3]{16}}\\
&=5.29695041726370448224105348429\ldots.
\end{aligned}
\]
This agrees with the exact polyhedral A15 calculation of Kusner and Sullivan after converting their volume and interface-counting convention.

### Strict descent from the flat partition

The flat partition is not stationary. At one class of A-B-B triple edges, the interior sector angle in the type-A cell is
\[
\theta_A=\arccos(-2/5)=113.578178\ldots^\circ,
\]
and another edge class has \(\arccos(-3/5)=126.869898\ldots^\circ\). Neither equals the Plateau value \(120^\circ\).

On a subsegment of such a triple edge, the first variation obtained by moving the junction in its normal plane is the negative pairing with the nonzero sum of the three unit conormals. Choosing the displacement along that sum makes the perimeter derivative strictly negative.

This edge perturbation can create first-order volume errors. They can be canceled by normal variations supported inside planar face patches. A connected adjacency graph supplies \(7\) independent face-patch variations spanning the zero-sum volume subspace of the eight cells. Since the patches are planar and the variations vanish near their boundaries, their first perimeter variations are zero. The implicit-function theorem then gives exact unit volumes for all sufficiently small perturbation parameters while retaining the negative first perimeter derivative.

Hence there exists an admissible periodic partition with area strictly below \(U_{A15}\), and
\[
\boxed{\kappa_3<5.296950417263705.}
\]
This argument does not certify the reported relaxed Weaire-Phelan decimal near \(5.288\).

## 5. No-go theorem for a global periodic paired calibration

Let \(T\) be a flat torus of volume \(|T|\). Prescribe phase volumes \(v_i>0\), with \(\sum_i v_i=|T|\). Let \(\xi_i\in H(\operatorname{div};T)\) be periodic fields and write
\[
f_i=\operatorname{div}\xi_i.
\]
Every well-defined periodic divergence has zero mean:
\[
\int_T f_i=0.
\]
Suppose also that
\[
|\xi_i-\xi_j|\le1.
\]
For any partition \(E=(E_i)\), the standard paired-field estimate is
\[
P_T(E)\ge\sum_i\int_{E_i}f_i.
\]

### Translation obstruction

Take any fixed partition \(A=(A_i)\) with \(|A_i|=v_i\), and translate all phases by \(y\in T\). Averaging over translations gives
\[
\begin{aligned}
\frac1{|T|}\int_T\sum_i\int_{A_i+y} f_i(x)\,dx\,dy
&=\sum_i\frac{v_i}{|T|}\int_T f_i(x)\,dx\\
&=0.
\end{aligned}
\]
Therefore some volume-preserving translate satisfies
\[
\sum_i\int_{A_i+y}f_i\le0.
\]
Consequently, no such family of periodic fields can make the flux functional uniformly at least a positive candidate perimeter over all partitions with the prescribed volumes.

In particular, if the fields saturated a candidate interface so that
\[
P_T(E^*)=\sum_i\int_{E_i^*}f_i>0,
\]
then the flux identity still could not compare \(E^*\) with all equal-volume competitors.

### Convex-dual form

Adding volume multipliers \(\lambda_i\), the strongest pointwise-assignment lower bound of this form is
\[
D(\xi,\lambda)
=\sum_i\lambda_i v_i
+\int_T\min_i\bigl(f_i-\lambda_i\bigr)\,dx.
\]
Put \(\theta_i=v_i/|T|\). Since a minimum does not exceed a convex average,
\[
\min_i(f_i-\lambda_i)
\le\sum_i\theta_i(f_i-\lambda_i).
\]
After integration,
\[
D(\xi,\lambda)\le0.
\]
The zero fields attain zero, so the dual optimum is exactly zero.

This is the dual manifestation of a complete integrality gap: the convex relaxation permits the constant fractional state
\[
u_i(x)=\theta_i,
\]
which has the correct volumes and zero total variation.

### Consequence

A positive global lower certificate on a closed torus must contain information that excludes the uniform fractional mixture. Viable options include:

- fixed phase traces on block boundaries;
- explicit topology or cell-complex integrality constraints;
- a nonconvex lifted hierarchy with cut or cycle inequalities;
- singular or nonlocal terms whose validity is proved for integral partitions;
- a reduction theorem to a finite integral class, followed by local calibrations.

Ordinary smooth periodic fields, pointwise pairwise norm constraints, and global volume multipliers are insufficient.

## 6. Finite-defect invariance

### Proposition

Let \(E\) and \(F\) be admissible partitions whose interfaces differ only inside a bounded set \(K\), and assume both interface measures in \(K\) are finite. Then
\[
\mathcal A(E)=\mathcal A(F).
\]

### Proof

For every sufficiently large \(R\),
\[
\left|
\mathcal H^2(J_E\cap Q_R)-
\mathcal H^2(J_F\cap Q_R)
\right|
\le
\mathcal H^2(J_E\cap K)+\mathcal H^2(J_F\cap K)=C.
\]
Multiplication by \(2/R^3\) and passage to the limsup gives equality. \(\square\)

### Consequences

1. A compactly supported area-decreasing perturbation does not lower \(\mathcal A\); it changes only \(O(1)\) area against \(O(R^3)\) volume.
2. Therefore an \(\mathcal A\)-optimizer need not be locally minimizing.
3. Plateau angles, constant mean curvature, and Taylor-type singularity regularity do not follow from \(\mathcal A\)-optimality alone.
4. Equality cases are necessarily nonunique under bounded volume-preserving defects.

A sound formulation should either:

- identify partitions modulo zero-density defects; or
- require a **ground-state condition**: no compactly supported volume-preserving perturbation lowers the unnormalized perimeter; or
- minimize a finite-volume or stationary-random free energy from which local minimality follows.

## 7. Exact remaining gap

A complete resolution still requires all of the following:

1. A rigorous continuum definition and existence theorem for the relaxed A15 foam, or for another candidate.
2. A certified upper enclosure for that continuum candidate, including lattice, volume, curvature, Plateau-angle, topology, and discretization errors.
3. An integrality-sensitive universal lower bound reaching the same value.
4. A theorem connecting finite-torus or block results with the unrestricted thermodynamic functional.
5. An equality analysis compatible with finite-defect invariance.

The central failed route is now precise: a classical global periodic paired calibration cannot perform item 3. The highest-value replacement experiment is a **boundary-conditioned block certificate**. One should calibrate A15 inside a block with fixed phase traces, prove a quantitative penalty for incompatible traces, and then tile or average the block inequality. This preserves the verification advantage of calibrations while removing the closed-torus fractional-mixture obstruction.

## 8. Reproducible artifacts

- `verify_flat_a15.py`: exact SymPy checks of the weight equation, unit volumes, face-area orbits, and normalized area.
- `flat_a15_candidate.json`: machine-readable lattice, sites, weights, exact formulas, and normalization.

## 9. References used in the proof architecture

- N. Fusco, F. Maggi, A. Pratelli, *The sharp quantitative isoperimetric inequality*, Annals of Mathematics 168 (2008), 941-980.
- T. Hales and collaborators, proof and formal verification of the Kepler sphere-packing theorem.
- R. Kusner, J. M. Sullivan, *Comparing the Weaire-Phelan equal-volume foam to Kelvin's foam*, Forma 11 (1996), 233-242.
- J. Fischer, S. Hensel, T. Laux, T. M. Simon, *Local minimizers of the interface length functional based on a concept of local paired calibrations*, arXiv:2212.11840.
- A. Cesaroni, M. Novaga, *Minimal periodic foams with equal cells* and *Minimal periodic foams with fixed inradius*.
