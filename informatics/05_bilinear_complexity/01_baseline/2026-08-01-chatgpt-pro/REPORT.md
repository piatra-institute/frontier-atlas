# Worked attempt report

## Exact result

For the ordinary bilinear complexity over the binary field,

\[
\boxed{R_{\mathbb F_2}(\langle 2,2,3\rangle)=11.}
\]

Here \(\langle2,2,3\rangle\) is the structure tensor of

\[
\mathbb F_2^{2\times2}\times\mathbb F_2^{2\times3}\longrightarrow
\mathbb F_2^{2\times3},\qquad (A,B)\longmapsto AB.
\]

This is a **P1 reproduction of a known exact rank**, not a new mathematical record. The session changed the initially proposed field from \(\mathbb Q\) to \(\mathbb F_2\) after the prior-art audit because the available 2026 proof-certificate framework and the field-specific exact statement are over \(\mathbb F_2\). Nothing in this package is claimed over \(\mathbb Q\), \(\mathbb R\), or any other field.

## Literature audit, 2026-08-01

The relevant checked sources were:

1. J. E. Hopcroft and L. R. Kerr, *On Minimizing the Number of Multiplications Necessary for Matrix Multiplication*, SIAM Journal on Applied Mathematics 20 (1971), DOI 10.1137/0120004. Its abstract gives the \(p\times2\) by \(2\times n\) construction with \(\lceil(3pn+\max(n,p))/2\rceil\) multiplications and identifies optimal special cases.
2. Chengu Wang, *Automated Lower Bounds for Bilinear Complexity over Finite Fields*, arXiv:2603.07280v10, 30 July 2026. This revision postdates the prompt by seven days. Its complete matrix table records, over \(\mathbb F_2\), lower and upper bounds 11 for \(\langle2,2,3\rangle\), with the upper bound described as a rank-7 \(\langle2,2,2\rangle\) block plus a rank-4 \(\langle2,2,1\rangle\) block. It also records the exact value 15 for \(\langle2,3,3\rangle\) over \(\mathbb F_2\).
3. Wang's current repository `wcgbg/tensor-rank-lower-bound`, including `certs/matrix/cert_matrix_q02_n223.pb.txt`. The retrieved current text certificate has SHA-256 `cf930d9358d56e21dc953cd2618820ad788a364444bcb5fe16bb0cf4926a169b` and records lower/upper bound 11, the restriction-orbit data, and backtracking proof sizes 13 and 1303. The prior matrix-specific certificate is also preserved as a legacy provenance artifact.

A field qualifier is essential. In particular, the prompt's unqualified \([14,15]\) line for \(\langle2,3,3\rangle\) should not be carried into a binary-field session: arXiv v10 records \(R_{\mathbb F_2}(\langle2,3,3\rangle)=15\). This report makes no assertion about its rank over \(\mathbb Q\).

## Tensor and coordinate convention

Write

\[
A=\begin{pmatrix}a_{00}&a_{01}\\a_{10}&a_{11}\end{pmatrix},\qquad
B=(b_{jk})_{j=0,1;\,k=0,1,2}.
\]

Coordinates are ordered as

\[
A=(a_{00},a_{01},a_{10},a_{11}),
\]

\[
B=(b_{00},b_{01},b_{02},b_{10},b_{11},b_{12}),
\]

and outputs as

\[
C=(C_{00},C_{01},C_{02},C_{10},C_{11},C_{12}).
\]

The target tensor has coefficient 1 precisely at

\[
T[(i,j),(j,k),(i,k)]=1,
\]

for \(i,j\in\{0,1\}\) and \(k\in\{0,1,2\}\), and coefficient 0 elsewhere. This is the same matrix-multiplication tensor as

\[
\sum_{i,j,k}a_{ij}\otimes b_{jk}\otimes c_{ki},
\]

with a row-major reindexing of the third factor.

## Upper bound: explicit rank 11

The decomposition in `decomposition.json` applies the seven-product Strassen scheme to the first two columns of \(B\), then computes the third column with four scalar products. In human-readable notation, with

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
B=\begin{pmatrix}e&f&g\\h&i&j\end{pmatrix},
\]

compute over \(\mathbb F_2\):

\[
\begin{aligned}
p_1&=(a+d)(e+i), &p_2&=(c+d)e,\\
p_3&=a(f+i), &p_4&=d(h+e),\\
p_5&=(a+b)i, &p_6&=(c+a)(e+f),\\
p_7&=(b+d)(h+i),\\
p_8&=ag, &p_9&=bj,\\
p_{10}&=cg, &p_{11}&=dj.
\end{aligned}
\]

Then

\[
AB=\begin{pmatrix}
p_1+p_4+p_5+p_7 & p_3+p_5 & p_8+p_9\\
p_2+p_4 & p_1+p_2+p_3+p_6 & p_{10}+p_{11}
\end{pmatrix}.
\]

`verify_upper.py` independently checks:

- all \(4\cdot6\cdot6=144\) structure-tensor coefficients;
- all \(2^4\cdot2^6=1024\) pairs of input matrices.

Both checks pass exactly. The decomposition hash is:

`c92c56d638a303dc15365c7b3bf42cc55f14236a2936e6075d321e164b795279`.

Therefore

\[
R_{\mathbb F_2}(\langle2,2,3\rangle)\le 11.
\]

## Lower bound architecture

### Restriction encoding

A linear form on the entries of \(A\) is encoded by the four-bit integer

\[
r=r_{00}+2r_{01}+4r_{10}+8r_{11}.
\]

A restriction subspace \(S\subseteq(\mathbb F_2^{2\times2})^*\) means that inputs are restricted to

\[
S^\perp=\{A:\langle R,A\rangle=0\text{ for every }R\in S\}.
\]

The verifier exhausts every generating subset of the 15 nonzero four-bit vectors and deduplicates them into exactly 67 linear subspaces. Under the left-right action of

\[
\mathrm{GL}_2(\mathbb F_2)\times\mathrm{GL}_2(\mathbb F_2),
\]

these split into exactly 11 orbits, distributed by codimension as

\[
1,2,5,2,1.
\]

Using inverses or transposes in the action gives the same orbit partition because these operations permute the six elements of \(\mathrm{GL}_2(\mathbb F_2)\).

### Verified orbit bounds

The following table gives the chosen representatives and the independently recomputed flattening ranks. The three entries are the ranks of the \(A|BC\), \(B|AC\), and \(C|AB\) flattenings.

| Orbit | Restrictions | Flattening ranks | Certified lower bound | Method |
|---:|---|---:|---:|---|
| 0 | 1,2,4,8 | (0,0,0) | 0 | zero tensor |
| 1 | 1,2,4 | (1,3,3) | 3 | flattening |
| 2 | 1,6,8 | (1,6,6) | 6 | flattening |
| 3 | 1,2 | (2,6,3) | 6 | flattening |
| 4 | 1,4 | (2,3,6) | 6 | flattening |
| 5 | 1,6 | (2,6,6) | 9 | exact two-slice rank metric |
| 6 | 1,8 | (2,6,6) | 6 | flattening |
| 7 | 6,13 | (2,6,6) | 9 | rank inequalities; redundant 13-leaf tree |
| 8 | 1 | (3,6,6) | 9 | further restriction to orbit 5 |
| 9 | 6 | (3,6,6) | 9 | further restriction to orbit 5 |
| 10 | none | (4,6,6) | 11 | 1303-leaf substitution tree |

### Difficult two-slice orbit 5

After restrictions \(S=\langle1,6\rangle\), the first tensor factor has dimension 2, so the tensor is represented by two \(6\times6\) binary matrices \(M_0,M_1\).

For any two-slice tensor over \(\mathbb F_2\),

\[
R(M_0,M_1)=\min_Z\bigl(\operatorname{rank}Z+\operatorname{rank}(M_0+Z)+\operatorname{rank}(M_1+Z)\bigr).
\]

Reason: every nonzero first-factor vector is one of \((1,0),(0,1),(1,1)\). Grouping rank-one summands by these three labels yields matrices \(X,Y,Z\) with \(M_0=X+Z\) and \(M_1=Y+Z\). Ordinary matrix rank is the minimum number of rank-one matrix summands, giving both inequalities in the formula.

For this orbit, \(Z=0\) gives ranks \((0,6,3)\), hence an upper bound 9. To exclude a value at most 8, at least one of the three matrix ranks would have to be at most 2. `two_slice_rank9.cpp` exhausts every binary \(6\times6\) matrix of rank at most 2:

\[
\begin{aligned}
N_0&=1,\\
N_1&=(2^6-1)^2=3969,\\
N_2&={6\brack2}_2^2\,|\mathrm{GL}_2(\mathbb F_2)|
=651^2\cdot6=2{,}542{,}806.
\end{aligned}
\]

It therefore checks \(2{,}546{,}776\) low-rank matrices and all three centers, totaling \(7{,}640{,}328\) candidate \(Z\) values. The minimum encountered is 9. Consequently orbit 5 has exact rank 9.

As an adversarial implementation test, `tests/test_two_slice_formula.py` computes the exact ranks of all 256 tensors in \(\mathbb F_2^2\otimes\mathbb F_2^2\otimes\mathbb F_2^2\) by breadth-first search over rank-one tensors and confirms the formula for every case.

### Orbit 7

For orbit 7, the two slices satisfy

\[
\operatorname{rank}M_0=
\operatorname{rank}M_1=
\operatorname{rank}(M_0+M_1)=6.
\]

For every \(Z\), the three triangle inequalities give

\[
\begin{aligned}
\operatorname{rank}Z+\operatorname{rank}(M_0+Z)&\ge6,\\
\operatorname{rank}Z+\operatorname{rank}(M_1+Z)&\ge6,\\
\operatorname{rank}(M_0+Z)+\operatorname{rank}(M_1+Z)&\ge6.
\end{aligned}
\]

Their sum proves that the two-slice objective is at least 9. A separate substitution tree with 13 leaves also proves the same lower bound, matching the upstream proof-size metadata.

### Substitution/backtracking lemma

Fix a base restriction space \(S\), and suppose a putative decomposition has \(r\) product slots with first-factor forms \(u_1,\ldots,u_r\) in the quotient by \(S\). For a selected set of slots \(I\), impose all restrictions \(u_i=0\), \(i\in I\). Every selected product disappears, so

\[
R(T_S)\ge |I|+R\left(T_{S+\operatorname{span}\{u_i:i\in I\}}\right).
\]

To disprove rank at most \(r_0-1\), a shorter decomposition may be padded to exactly \(r_0-1\) slots with zero tensors. Such zero slots can be assigned arbitrary nonzero first-factor labels, so it suffices to enumerate multisets of nonzero quotient vectors. Sorting them removes permutation symmetry.

A leaf certificate provides a selected subset \(I\) whose size plus an already verified stricter-orbit lower bound is at least the target. An internal node contains every legal next nonincreasing vector. Thus a finite prefix-complete tree covers every padded putative decomposition.

The two checked trees are:

| Base orbit | Target | Candidate quotient vectors | Leaves | Internal nodes | Maximum depth |
|---:|---:|---|---:|---:|---:|
| 7 | 9 | 1,2,3 | 13 | 27 | 7 |
| 10, unrestricted | 11 | 1 through 15 | 1303 | 896 | 10 |

For the unrestricted tree, leaf closures use the already verified lower bounds of orbits 5, 7, 8, and 9. `verify_lower.py` checks every leaf inequality, rejects circular or non-strict restrictions, reconstructs the entire prefix tree, and confirms that no branch is omitted.

The full certificate hash is:

`b9f1970a4b475d00f0bd44726397256138cc46e4fcab05264c2669c84153a241`.

Therefore

\[
R_{\mathbb F_2}(\langle2,2,3\rangle)\ge11.
\]

Combined with the explicit decomposition,

\[
R_{\mathbb F_2}(\langle2,2,3\rangle)=11.
\]

## Verification separation and trust base

The search and verification paths are deliberately separated:

- `generate_backtracking_certificate.py` discovers and serializes the finite trees.
- `verify_lower.py` does not import the generator. It independently reconstructs subspaces, orbits, tensors, flattenings, and tree coverage.
- `two_slice_rank9.cpp` performs the large rank-metric enumeration using a separate implementation and language.
- `verify_upper.py` consumes a manually fixed decomposition and independently checks both coefficients and function values.
- `reproduce_certificates.sh` regenerates both JSON certificates and byte-compares them with the preserved copies.

The trust base consists of exact finite-field arithmetic, elementary Gaussian elimination, the standard tensor-rank flattening inequality, the elementary two-slice formula proved above, and the substitution inequality. There is no floating point, numerical tensor decomposition, SAT solver oracle, Gröbner black box, or unverified symmetry ansatz.

Review level is **agent**. The artifacts have been self-adversarially checked by independent programs but have not received human or community peer review.

## Adversarial audit and rejected lines

Three failures or pivots were preserved in the attempt denominator:

1. **Field pivot.** The session initially announced \(\mathbb Q\), then changed to \(\mathbb F_2\) after literature verification. A finite-field lower bound is not transported to \(\mathbb Q\).
2. **Rejected subspace implementation.** The first row-reduction representation incorrectly produced 270 apparent subspaces instead of the known finite count 67. It was discarded and replaced by an exact subspace-as-bitmask representation. The final verifier independently confirms 67.
3. **Rejected exact-rank inference for orbit 7.** A rank-at-most-2-centered enumeration found no value below 10 for orbit 7, but that search does not cover the possible rank pattern \((3,3,3)\). The would-be exact-rank-10 conclusion was rejected. Only the rigorously justified lower bound 9 is used, and it has two independent proofs.

These corrections are evidence that failed checks altered the result rather than being ignored.

## Cost and attempts

- Major mathematical attempts: 1 field pivot; 2 subspace encodings; 1 upper-bound construction; 2 restricted two-slice analyses; 2 finite-tree generations; 1 independent full replay.
- Final certificate generation: 3.01 seconds wall time.
- Formula test: 1.22 seconds.
- Upper verifier: 1.41 seconds.
- Lower verifier: 3.82 seconds.
- Maximum recorded resident memory: approximately 112 MB.
- Hardware scope: one x86-64 container CPU environment; no external paid compute.
- Currency cost and model-token spend are not exposed by the runtime and therefore cannot be truthfully reported.

The exact timings are preserved in `logs/timing.txt`.

## What is and is not established

Established:

\[
R_{\mathbb F_2}(\langle2,2,3\rangle)=11
\]

for ordinary bilinear tensor rank, with a checked length-11 decomposition and a replayed finite lower-bound certificate.

Not established:

- any new rank record;
- the rank of this tensor over \(\mathbb Q\), \(\mathbb R\), or \(\mathbb F_p\) for \(p\ne2\);
- border rank;
- exact ranks of any other target named in the prompt.
