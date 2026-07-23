You: 

kelvin\_weaire\_phelan\_optimizer\_prompt(1).pdf

PDF

read and solve this

ChatGPT: 

Worked for 52m 29s

## Reformulated task

> Read the supplied research prompt and attempt a complete solution of the unrestricted three-dimensional Kelvin problem: determine the honeycomb constant $\kappa_3$, prove or disprove attainment, identify a global optimizer, and decide whether the relaxed Weaire-Phelan A15 foam is globally optimal.

The PDF correctly excludes conclusions based only on periodicity, fixed topology, numerical relaxation, local stability, or a non-sharp lower bound.

kelvin\_weaire\_phelan\_optimizer\_…

# Verdict

**I did not obtain a complete solution of the Kelvin problem.**

The latest rigorous source I found still describes the problem as open even under some much stronger periodic and lattice restrictions, and Brakke’s official Surface Evolver material likewise states that there is no proof of Weaire-Phelan optimality. [![](https://www.google.com/s2/favicons?domain=https://londmathsoc.onlinelibrary.wiley.com&sz=128)London Mathematical Society+1](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112%2Fmtk.70020)

Under the PDF’s own standard, the correct output is therefore a **rigorous non-solution dossier**, rather than a numerical claim presented as a theorem.

kelvin\_weaire\_phelan\_optimizer\_…

Nevertheless, the analysis produces four substantive theorem-level deductions.

| Result | Mathematical consequence |
| --- | --- |
| Strict frustration gap above the sphere bound | $\kappa_3>(36\pi)^{1/3}$, not merely $\ge$ |
| Exact flat A15 construction | A fully algebraic admissible competitor with area $5.296950417263704\ldots$ |
| Periodic-calibration no-go theorem | The PDF’s highest-priority classical calibration route cannot work as stated |
| Finite-defect invariance | The asymptotic functional cannot by itself imply Plateau regularity or uniqueness |

Together they give the rigorous bracket

$$
\boxed{ 4.835975862049408\ldots < \kappa_3 < 5.296950417263705\ldots }
$$

The lower inequality has an unquantified positive margin. It is not close enough to the reported relaxed Weaire-Phelan value near $5.288$ to decide optimality.

---

# 1\. A strict universal gap above the sphere bound

Let

$$
c_0=(36\pi)^{1/3}=4.835975862049408\ldots,
$$

the surface area of a unit-volume sphere.

For an admissible partition $E=(E_i)$, set

$$
F_i=E_i\cap Q_R,\qquad v_i=|F_i|,\qquad J_R=\mathcal H^2(J_E\cap Q_R).
$$

For almost every $R$, the trace formula for a Caccioppoli partition gives

$$
\sum_i P(F_i)=2J_R+6R^2.
$$

Because each entire cell has volume one,

$$
0\le v_i\le1.
$$

Euclidean isoperimetry therefore yields

$$
P(F_i)\ge c_0v_i^{2/3}\ge c_0v_i.
$$

Summing over all fragments and using $\sum_i v_i=R^3$,

$$
2J_R+6R^2\ge c_0R^3,
$$

hence

$$
\kappa_3\ge c_0.
$$

The important improvement is that equality cannot even be approached.

## Theorem

There exists a dimension-dependent constant $\varepsilon_3>0$ such that

$$
\boxed{\kappa_3\ge(36\pi)^{1/3}+\varepsilon_3.}
$$

## Proof mechanism

Suppose partitions $E^{(m)}$ approached $c_0$. Choose cubes $Q_{R_m}$, $R_m\to\infty$, for which the normalized area approaches $c_0$. Define the nonnegative total deficit

$$
\begin{aligned} D_m={}& \sum_i\left[P(F_i^{(m)})-c_0(v_i^{(m)})^{2/3}\right]\\ &+c_0\sum_i\left[(v_i^{(m)})^{2/3}-v_i^{(m)}\right]. \end{aligned}
$$

The trace identity gives

$$
D_m=o(R_m^3).
$$

This has two consequences:

1.  The second sum implies that fragments with volume bounded away from one occupy only $o(R_m^3)$ total volume.
    
2.  The sharp quantitative isoperimetric inequality implies that almost every remaining fragment is close, in relative symmetric difference, to a ball of the same volume. [![](https://www.google.com/s2/favicons?domain=https://annals.math.princeton.edu&sz=128)Annals of Mathematics](https://annals.math.princeton.edu/2008/168-3/p06)
    

Choose $s<1$ and $\eta>0$ such that

$$
s^3(1-\eta)>\delta_K, \qquad \delta_K=\frac{\pi}{\sqrt{18}},
$$

where $\delta_K$ is the maximum density of a congruent-sphere packing in $\mathbb R^3$. [![](https://www.google.com/s2/favicons?domain=https://annals.math.princeton.edu&sz=128)Annals of Mathematics](https://annals.math.princeton.edu/2005/162-3/p01)

For every good fragment, contract its approximating ball concentrically to fixed volume

$$
s^3(1-\eta).
$$

These contracted balls must be disjoint. Otherwise, the two original approximating balls would overlap by a definite positive volume, greater than the symmetric-difference errors can absorb, contradicting disjointness of the partition fragments.

There are $R_m^3-o(R_m^3)$ such congruent balls in a cube of side $R_m+O(1)$. Periodically repeating a slightly enlarged containing cube produces a sphere packing with limiting density at least

$$
s^3(1-\eta)>\delta_K,
$$

contradicting the Kepler theorem.

Therefore the sphere value is separated from $\kappa_3$ by a strictly positive universal gap.

### Limitation

This argument proves existence of $\varepsilon_3>0$, but does not extract a useful numerical value. Doing so would require explicit constants in the quantitative isoperimetric stability estimate and an effective finite-volume packing estimate.

---

# 2\. Exact equal-volume flat A15 competitor

The flat A15 structure can be reconstructed as an exact periodic Laguerre, or power-diagram, partition.

Take the cubic torus

$$
T=\mathbb R^3/(2\mathbb Z)^3, \qquad |T|=8,
$$

with two type-A sites and six type-B sites. In the convention

$$
|x-p_i|^2-w_i\le |x-p_j-\lambda|^2-w_j,
$$

use

$$
w_A=0, \qquad w_B=\delta=\frac54-\sqrt[3]{2}.
$$

For the two cell orbits, exact polyhedral integration gives

$$
V_A(\delta) = \frac{125}{128} -\frac{75}{32}\delta +\frac{15}{8}\delta^2 -\frac12\delta^3,
$$
 
$$
V_B(\delta) = \frac{129}{128} +\frac{25}{32}\delta -\frac58\delta^2 +\frac16\delta^3.
$$

The equal-volume condition reduces to

$$
64\delta^3-240\delta^2+300\delta+3=0,
$$

or equivalently,

$$
64\left(\delta-\frac54\right)^3+128=0.
$$

Thus

$$
\delta=\frac54-\sqrt[3]{2}
$$

and exactly

$$
V_A=V_B=1.
$$

Let $r=\sqrt[3]{2}$. The three face-area orbits are

$$
a=\frac{\sqrt5\,r^2}{8}, \qquad b=1-\frac{r^2}{4}, \qquad c=\frac{\sqrt6(3-r^2)}{12}.
$$

A type-A cell has area $12a$, while a type-B cell has area

$$
4a+2b+8c.
$$

Therefore the mean full cell-boundary area is

$$
\begin{aligned} U_{\mathrm{A15,flat}} &= \frac{2(12a)+6(4a+2b+8c)}8\\[2mm] &= \frac32+\frac{3\sqrt6}{2} +\frac{6\sqrt5-4\sqrt6-3}{2\sqrt[3]{16}}\\[2mm] &= 5.29695041726370448224105348429\ldots. \end{aligned}
$$

This agrees, after converting volume and interface-counting conventions, with the exact polyhedral A15 calculation of Kusner and Sullivan. [![](https://www.google.com/s2/favicons?domain=https://www.researchgate.net&sz=128)ResearchGate](https://www.researchgate.net/publication/250020835_Comparing_the_Weaire-Phelan_equal-volume_foam_to_Kelvin%27s_foam)

Hence

$$
\kappa_3\le U_{\mathrm{A15,flat}}.
$$

## Strict improvement over the flat partition

The flat partition is not stationary. Some triple-edge sector angles are

$$
\arccos(-2/5)=113.578178\ldots^\circ
$$

and

$$
\arccos(-3/5)=126.869898\ldots^\circ,
$$

rather than the Plateau value $120^\circ$.

Move a subsegment of such a junction in the direction of the nonzero sum of its three unit conormals. The first perimeter variation is strictly negative.

This initially produces small first-order volume errors. They can be canceled using normal variations supported inside seven planar face patches forming a spanning tree of the eight-cell adjacency graph:

-   these variations span the seven-dimensional zero-sum volume subspace;
    
-   the patches are planar, so their first area variations vanish;
    
-   the implicit-function theorem then restores all eight unit volumes exactly.
    

Therefore an exact-volume periodic perturbation has strictly smaller area:

$$
\boxed{ \kappa_3 < 5.296950417263705. }
$$

This proves a strict analytic descent from the polyhedral A15 structure. It does **not** rigorously certify the fully relaxed Weaire-Phelan value near $5.288$.

---

# 3\. The proposed global periodic paired calibration is impossible as stated

The PDF identifies a periodic paired calibration as the highest-priority proof experiment.

kelvin\_weaire\_phelan\_optimizer\_…

There is a fundamental convex-duality obstruction.

## No-go theorem

Let $T$ be a closed flat torus with prescribed phase volumes $v_i$, and let

$$
\xi_i\in H(\operatorname{div};T)
$$

be single-valued periodic fields satisfying

$$
|\xi_i-\xi_j|\le1.
$$

Write

$$
f_i=\operatorname{div}\xi_i.
$$

Since $T$ has no boundary,

$$
\int_T f_i=0
$$

for every $i$.

Adding arbitrary volume multipliers $\lambda_i$, the strongest pointwise-assignment dual lower bound of this form is

$$
D(\xi,\lambda) = \sum_i\lambda_i v_i+ \int_T\min_i\bigl(f_i-\lambda_i\bigr)\,dx.
$$

Set

$$
\theta_i=\frac{v_i}{|T|}.
$$

Because a minimum is no larger than any convex average,

$$
\min_i(f_i-\lambda_i) \le \sum_i\theta_i(f_i-\lambda_i).
$$

Integrating,

$$
\begin{aligned} D(\xi,\lambda) &\le \sum_i\lambda_i v_i+ \sum_i\theta_i\int_Tf_i -|T|\sum_i\theta_i\lambda_i\\ &=0. \end{aligned}
$$

The zero fields attain zero, so the dual optimum is exactly zero.

But every nontrivial partition into positive-volume phases has positive perimeter. Thus the ordinary convex paired-calibration relaxation has a **complete integrality gap**.

The corresponding relaxed zero-energy state is simply

$$
u_i(x)=\theta_i,
$$

a uniform fractional mixture having the correct volumes and zero total variation.

## Translation version of the obstruction

For any fixed equal-volume partition $A=(A_i)$,

$$
\frac1{|T|} \int_T \sum_i\int_{A_i+y}f_i(x)\,dx\,dy =0.
$$

Therefore some translate of $A$ has calibration flux at most zero. A positive candidate perimeter cannot consequently be obtained as a uniform lower bound over all translated competitors.

## Consequence

This does not rule out every possible calibration. It rules out:

-   ordinary smooth or $H(\operatorname{div})$ periodic fields;
    
-   pointwise pairwise norm constraints;
    
-   global volume multipliers;
    
-   no additional integral, trace, or topology information.
    

Localized paired calibrations can work when boundary traces are fixed, as in the Fischer-Hensel-Laux-Simon framework. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv](https://arxiv.org/abs/2212.11840)

A viable Kelvin certificate therefore needs at least one of:

1.  fixed phase traces on block boundaries;
    
2.  an explicit mismatch penalty between neighboring blocks;
    
3.  integral cell-complex constraints, such as cut or cycle inequalities;
    
4.  a finite topology-reduction theorem followed by local certificates;
    
5.  singular or nonlocal dual objects whose validity is proved specifically for integral partitions.
    

This is the most consequential correction to the PDF’s proposed architecture.

---

# 4\. The asymptotic objective is invariant under bounded defects

Suppose two admissible partitions $E$ and $F$ differ only inside a bounded region $K$, with finite interface measure there. Then, for sufficiently large $R$,

$$
\left| \mathcal H^2(J_E\cap Q_R) - \mathcal H^2(J_F\cap Q_R) \right| \le C_K.
$$

After multiplication by $2/R^3$ and passage to the limsup,

$$
\boxed{\mathcal A(E)=\mathcal A(F).}
$$

## Implications

An optimizer for $\mathcal A$:

-   need not be locally perimeter-minimizing;
    
-   need not obey Plateau angles at a deliberately inserted bounded defect;
    
-   need not possess the regularity of a minimizing cluster;
    
-   cannot be unique as an ordinary partition.
    

For example, one can introduce a bounded, volume-preserving exchange between finitely many cells, adding irregular interfaces but leaving $\mathcal A$ unchanged.

Consequently, the problem should distinguish between:

$$
\text{minimum energy density}
$$

and

$$
\text{ground-state representative}.
$$

A corrected optimizer theorem should either:

-   identify partitions modulo zero-density modifications; or
    
-   add the condition that no compactly supported volume-preserving perturbation lowers the unnormalized perimeter.
    

Without such a condition, the regularity program in the PDF does not follow merely from global $\mathcal A$\-optimality.

---

# Exact remaining gap

A complete solution still requires three genuinely unresolved bridges:

1.  **Certified continuum upper bound.** Construct the relaxed A15 foam as an exact analytic or variational object and rigorously enclose its area, volumes, pressures, singular curves, and lattice parameters.
    
2.  **Integrality-sensitive universal lower bound.** It must reach the same value. The ordinary closed-torus convex calibration cannot do this.
    
3.  **Thermodynamic-limit theorem.** A finite-block or periodic result must be transferred to the unrestricted $\mathbb R^3$ functional without silently assuming bounded diameters, periodicity, finite topology, or controlled boundary traces.
    

The most promising corrected experiment is a **boundary-conditioned block certificate**:

$$
P_B(E) \ge c_{\mathrm{A15}}|B| - C\,\mathcal M\!\left( \operatorname{Tr}_{\partial B}E, \operatorname{Tr}_{\partial B}E_{\mathrm{A15}} \right),
$$

where $\mathcal M$ measures phase-trace incompatibility. One would then need a gluing or averaging theorem showing that mismatch penalties cannot disappear while lowering bulk area.

That route removes the uniform-fractional-mixture obstruction while preserving the checkability advantage of calibrations.

# Artifacts

-   Complete audit package  
    SHA-256: `d9a7759e32ded87cf7bfae81f0ec9a3f785f1d11146bccad0c896aaac25b1b3e`
    
-   kelvin\_partial\_resolution\_dossier.md
    
-   verify\_flat\_a15.py
    
-   flat\_a15\_candidate.json
    

The script verifies exact unit volumes, the algebraic weight, all three face-area orbits, the normalized area, and an independent numerical reconstruction of both cell types.

## Essential conclusion

The unrestricted Kelvin problem remains unresolved. This audit nevertheless establishes:

$$
(36\pi)^{1/3}+\varepsilon_3 \le \kappa_3 < 5.296950417263705, \qquad \varepsilon_3>0,
$$

provides an exact reproducible A15 competitor, proves that the PDF’s proposed classical periodic calibration cannot supply the required global lower bound, and identifies a necessary correction to the optimizer formulation itself.

![](https://www.google.com/s2/favicons?domain=https://annals.math.princeton.edu&sz=32)

![](https://www.google.com/s2/favicons?domain=https://kenbrakke.com&sz=32)

![](https://www.google.com/s2/favicons?domain=https://londmathsoc.onlinelibrary.wiley.com&sz=32)

Sources