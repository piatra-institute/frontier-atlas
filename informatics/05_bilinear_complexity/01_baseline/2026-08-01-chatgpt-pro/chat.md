Worked for 68m 17s

## Reformulated task

> Fix one specific bilinear map, field, and rank notion; produce an explicit exact decomposition for the upper bound and a replayable nonexistence certificate for one fewer multiplication; independently verify both; preserve the complete audit record.

# Certified worked result

| Item | Pinned choice |
| --- | --- |
| Map | $2\times2$ by $2\times3$ matrix multiplication |
| Field | $\mathbb F_2$ |
| Measure | Ordinary bilinear tensor rank |
| Exact result | $\boxed{R_{\mathbb F_2}(\langle2,2,3\rangle)=11}$ |
| Grade | P1, certified reproduction of a known value |
| Review level | Agent |
| Novel result | No |

The field was deliberately changed from the initially announced $\mathbb Q$ target to $\mathbb F_2$. The lower-bound certificate reconstructed here is intrinsically binary-field-specific, and no inference from it to $\mathbb Q$ or $\mathbb R$ is made.

## Literature correction

The prompt revision of 23 July 2026 was overtaken by arXiv v10, revised on 30 July 2026. Its complete table records

$$
R_{\mathbb F_2}(\langle2,2,3\rangle)=11
$$

and also

$$
R_{\mathbb F_2}(\langle2,3,3\rangle)=15.
$$

Thus the prompt's $[14,15]$ bracket for $\langle2,3,3\rangle$ is no longer current **over $\mathbb F_2$**. No corresponding claim is made here for $\mathbb Q$. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv+1](https://arxiv.org/abs/2603.07280?utm_source=chatgpt.com)

The original Hopcroft-Kerr construction gives a $p\times2$ by $2\times n$ multiplication count of

$$
\left\lceil\frac{3pn+\max(p,n)}2\right\rceil,
$$

which gives $11$ at $p=2,n=3$. [![](https://www.google.com/s2/favicons?domain=https://epubs.siam.org&sz=128)SIAM](https://epubs.siam.org/doi/10.1137/0120004)

The current public repository contains the specific binary certificate `cert_matrix_q02_n223.pb.txt` and explicitly separates the verifier trust base from the untrusted search and upper-bound-generation code. [![](https://www.google.com/s2/favicons?domain=https://github.com&sz=128)GitHub+1](https://github.com/wcgbg/tensor-rank-lower-bound)

# Upper bound: explicit 11-product algorithm

Let

$$
A=\begin{pmatrix}a&b\\c&d\end{pmatrix}, \qquad B=\begin{pmatrix}e&f&g\\h&i&j\end{pmatrix}.
$$

Over $\mathbb F_2$, compute

$$
\begin{aligned} p_1&=(a+d)(e+i),& p_2&=(c+d)e,\\ p_3&=a(f+i),& p_4&=d(h+e),\\ p_5&=(a+b)i,& p_6&=(c+a)(e+f),\\ p_7&=(b+d)(h+i),\\ p_8&=ag,& p_9&=bj,\\ p_{10}&=cg,& p_{11}&=dj. \end{aligned}
$$

Then

$$
AB= \begin{pmatrix} p_1+p_4+p_5+p_7 & p_3+p_5 & p_8+p_9\\ p_2+p_4 & p_1+p_2+p_3+p_6 & p_{10}+p_{11} \end{pmatrix}.
$$

The independent upper verifier checked:

-   all $4\cdot6\cdot6=144$ structure-tensor coefficients;

-   all $2^4\cdot2^6=1{,}024$ input pairs.


Therefore,

$$
R_{\mathbb F_2}(\langle2,2,3\rangle)\le 11.
$$

Decomposition SHA-256:

```
```
c92c56d638a303dc15365c7b3bf42cc55f14236a2936e6075d321e164b795279
```
```

# Lower bound: exclusion of every 10-product algorithm

The lower-bound verifier independently reconstructed the restriction geometry on the four-dimensional first tensor factor.

| Exact verification component | Result |
| --- | --- |
| Linear subspaces of $\mathbb F_2^4$ | 67 |
| $\mathrm{GL}_2(\mathbb F_2)^2$ restriction orbits | 11 |
| Orbit counts by codimension | $1,2,5,2,1$ |
| Difficult two-slice rank-$\le2$ matrices enumerated | $2{,}546{,}776$ |
| Three-centered rank-metric cases checked | $7{,}640{,}328$ |
| Exhaustive $2\times2\times2$ formula tests | 256 |
| Restricted orbit-7 tree | 13 leaves |
| Unrestricted rank-10 exclusion tree | 1,303 leaves |
| Unrestricted tree internal nodes | 896 |
| Maximum tree depth | 10 |

## Difficult two-slice restriction

For a binary two-slice tensor represented by $6\times6$ matrices $M_0,M_1$,

$$
R(M_0,M_1)= \min_Z\left[ \operatorname{rank}Z+ \operatorname{rank}(M_0+Z)+ \operatorname{rank}(M_1+Z) \right].
$$

For the difficult restriction orbit, $Z=0$ gives the rank pattern

$$
(0,6,3),
$$

and hence an upper bound of $9$.

If the objective were at most $8$, at least one of its three ranks would be at most $2$. The C++ checker therefore enumerated every binary $6\times6$ matrix of rank $0,1,$ or $2$:

$$
1+63^2+651^2\lvert\mathrm{GL}_2(\mathbb F_2)\rvert = 1+3{,}969+2{,}542{,}806 = 2{,}546{,}776.
$$

Testing all three possible low-rank centers covered $7{,}640{,}328$ cases. No objective below $9$ was found, proving that restricted tensor has exact rank $9$.

A separate Python breadth-first search verified the two-slice identity for all 256 tensors in

$$
\mathbb F_2^2\otimes\mathbb F_2^2\otimes\mathbb F_2^2.
$$

## Full substitution certificate

Assume a decomposition with at most ten products. Pad it to exactly ten slots if necessary, then sort the nonzero first-factor labels in $\mathbb F_2^4$.

At every certificate leaf, a selected subset $I$ of products is killed by adding their first-factor forms as restrictions. The verifier confirms

$$
|I|+ R\!\left(T\text{ after those restrictions}\right)\ge11.
$$

But the restricted tensor would be computed by at most $10-|I|$ surviving products, yielding a contradiction.

The verifier checks that:

1.  every possible next quotient vector appears at every internal node;

2.  all 1,303 leaves are prefix-free;

3.  no branch is omitted;

4.  every leaf reaches a strictly more restricted, previously certified orbit;

5.  every leaf inequality reaches at least $11$;

6.  no circular lower-bound dependency is used.


Thus no rank-10 decomposition exists:

$$
R_{\mathbb F_2}(\langle2,2,3\rangle)\ge11.
$$

Combined with the explicit algorithm,

$$
\boxed{R_{\mathbb F_2}(\langle2,2,3\rangle)=11}.
$$

Full lower-certificate SHA-256:

```
```
b9f1970a4b475d00f0bd44726397256138cc46e4fcab05264c2669c84153a241
```
```

# Adversarial audit

Three material failures or pivots were retained rather than hidden:

1.  **Field pivot:** the attempt began with $\mathbb Q$, but moved to $\mathbb F_2$ once the field-specific certificate literature was checked.

2.  **Rejected subspace implementation:** the first row-reduction implementation incorrectly returned 270 apparent subspaces. It was discarded. The replacement bitmask implementation and independent verifier both return the correct finite count of 67.

3.  **Rejected rank-10 claim for a restricted orbit:** an initial search excluded configurations centered at matrices of rank at most two, but did not exclude a possible $(3,3,3)$ rank pattern. The proposed exact-rank-10 conclusion was rejected. Only the rigorously proved lower bound $9$ is used.


The generator is not imported by the verifier. The large rank-metric enumeration is implemented separately in C++, while tensor, orbit, and tree verification are implemented in Python.

# Replay

```
Bash

```
unzip piatra_bilinear_rank_223_f2_attempt01.zip
cd piatra_bilinear_rank_223_f2_attempt01

./verify_all.sh
./reproduce_certificates.sh
```
```

Tested toolchain:

```
```
Python 3.13.5
G++ 14.2.0
C++17
GNU coreutils 9.7
```
```

The final ZIP was extracted into a fresh directory, and both commands were rerun successfully from the extracted archive.

## Artifacts

-   Download the complete certified package

-   ZIP SHA-256 checksum

-   CLAIM.md

-   REPORT.md

-   ALGORITHM.md

-   SHA-256 manifest


Final archive SHA-256:

```
```
8414de21ad6337e0609a142e405b1a11c65b006b17e98097fa7be1b6a9bee248
```
```

## Scope of the result

Established:

$$
R_{\mathbb F_2}(\langle2,2,3\rangle)=11.
$$

Not established:

-   a new mathematical record;

-   rank over $\mathbb Q$, $\mathbb R$, or $\mathbb F_p$ for $p\ne2$;

-   border rank;

-   any quaternion-rank claim;

-   an exact value for $\langle3,3,3\rangle$.


The delivered result is a complete, replayable **P1 reproduction**, with matching exact upper and lower certificates.

CLAIM.mdDocumentOpen file

REPORT.mdDocumentOpen file

ALGORITHM.mdDocumentOpen file

![](https://www.google.com/s2/favicons?domain=https://epubs.siam.org&sz=32)

![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=32)

Sources
