# Exact fixed-vertex reduction

## 1. Strongly regular graph equation

For an `srg(v,k,lambda,mu)`, its adjacency matrix satisfies

\[
A^2=(k-\mu)I+(\lambda-\mu)A+\mu J.
\]

For `(v,k,lambda,mu)=(99,14,1,2)`,

\[
A^2=12I-A+2J.
\]

## 2. First neighborhood

Fix a vertex `x`. Each vertex in `Gamma(x)` has exactly `lambda=1` neighbor inside `Gamma(x)`. Since `|Gamma(x)|=14`,

\[
G[\Gamma(x)]\cong 7K_2.
\]

Label the 14 vertices by `0,...,13`, with mate involution

\[
m(u)=u\mathbin{\mathrm{xor}}1.
\]

Let `L` be the adjacency matrix of this fixed matching.

## 3. Canonical labeling of the second layer

Every vertex `z` nonadjacent to `x` has exactly `mu=2` neighbors in `Gamma(x)`.

Those two neighbors cannot be a matched pair. If they were adjacent, they would have both `x` and `z` as common neighbors, contradicting `lambda=1`.

Conversely, every nonmatched pair `{u,v}` in `Gamma(x)` is nonadjacent, so it has exactly two common neighbors. One is `x`; the other is a unique vertex in `Gamma_2(x)`.

Therefore

\[
\Gamma_2(x)\longleftrightarrow E(C),
\qquad
C=K_{14}-7K_2=K_{2,2,2,2,2,2,2}.
\]

The number of labels is

\[
|E(C)|=\binom{14}{2}-7=84.
\]

Let `M` be the unsigned `84 x 14` edge-vertex incidence matrix of `C`, and let

\[
T=J-I-L
\]

be the adjacency matrix of `C`.

## 4. Block adjacency matrix

Let `B` be the unknown adjacency matrix induced by `Gamma_2(x)`. With vertex order

```text
x | Gamma(x) | Gamma_2(x)
```

the full matrix is

\[
A=
\begin{pmatrix}
0 & \mathbf 1^T & 0\\
\mathbf 1 & L & M^T\\
0 & M & B
\end{pmatrix}.
\]

## 5. Exact reduced equations

The `(Gamma_2,Gamma)` block of `A^2=12I-A+2J` gives

\[
ML+BM=-M+2J.
\]

Since each row of `M` contains two ones,

\[
MJ=2J,
\]

and hence

\[
BM=M(J-I-L)=MT.
\tag{R1}
\]

The `(Gamma_2,Gamma_2)` block gives

\[
MM^T+B^2=12I-B+2J,
\]

or

\[
B^2=12I-B-MM^T+2J.
\tag{R2}
\]

The remaining blocks follow from

\[
L^2=I,
\qquad
M^TM=12I+T,
\qquad
T=J-I-L.
\]

Thus a binary symmetric zero-diagonal `B` satisfies `(R1)` and `(R2)` if and only if the reconstructed `A` is an `srg(99,14,1,2)`.

## 6. Entrywise incidence equation

Index a row of `B` by base edge `e` and a base point by `u`. Equation `(R1)` is

\[
\sum_{f\ni u}B_{ef}
=
2-\mathbf 1_{u\in e}-\mathbf 1_{m(u)\in e}.
\tag{R3}
\]

Summing `(R3)` over all 14 values of `u` counts every neighbor of `e` twice and forces

\[
\deg_B(e)=12.
\]

For a fixed base point `u`, let

\[
S_u=\{e\in E(C):u\in e\}.
\]

Then `|S_u|=12`, and `(R3)` shows that every vertex of `B[S_u]` has degree one. Therefore each `B[S_u]` is a perfect matching.

## 7. Entrywise common-neighbor equation

For distinct base edges `e,f`,

\[
(MM^T)_{ef}=|e\cap f|.
\]

Equation `(R2)` yields

\[
|N_B(e)\cap N_B(f)|=2-|e\cap f|-B_{ef}.
\tag{R4}
\]

Therefore:

| Base-edge relation | `B_ef` | Common `B`-neighbors |
|---|---:|---:|
| overlap | 1 | 0 |
| overlap | 0 | 1 |
| disjoint | 1 | 1 |
| disjoint | 0 | 2 |

## 8. Forced 2-factor and triangle decomposition

The 14 perfect matchings `B[S_u]` have six edges each. Every `B`-vertex corresponds to a base edge `{a,b}` and belongs to exactly `S_a` and `S_b`, so the union of these matching edges is a spanning 2-regular graph `H` on 84 vertices. It contains

\[
14\cdot6=84
\]

edges.

Since `B` is 12-regular,

\[
|E(B)|=84\cdot12/2=504.
\]

The remaining 420 edges join disjoint base edges. Every such adjacent pair has exactly one common `B`-neighbor by `(R4)`. That common neighbor must be disjoint from both endpoints, or an adjacent overlapping pair would acquire a forbidden common neighbor. Thus the 420 edges split into

\[
420/3=140
\]

edge-disjoint triangles on triples of pairwise disjoint base edges.

Hence

\[
B=H\;\dot\cup\;140\text{ edge-disjoint triangles}.
\]

## 9. Spectrum of the reduced matrix

The known matrix `T` has spectrum

\[
12^1,\quad 0^7,\quad (-2)^6.
\]

Equation `BM=MT` fixes the action of `B` on `col(M)`. On `ker(M^T)`, equation `(R2)` becomes

\[
B^2+B-12I=0.
\]

Trace then gives

\[
\operatorname{Spec}(B)
=
\{12^1,3^{40},0^7,(-2)^6,(-4)^{30}\}.
\]

This spectrum is a redundant necessary check, not a substitute for `(R1)` and `(R2)`.
