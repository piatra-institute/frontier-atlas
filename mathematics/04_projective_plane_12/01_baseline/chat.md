You: 

04\_projective\_plane\_12(1).pdf

PDF

read the prompt and solve it

ChatGPT: 

Worked for 93m 4s

## Interpreted task

> Decide completely whether a finite projective plane of order $12$ exists, either by constructing and verifying its $157\times157$ incidence matrix or by supplying an exhaustive, independently checkable nonexistence proof.

## Verdict

**The order-12 projective-plane problem has not been completely resolved here.**

The prompt requires either the full incidence structure or a globally complete nonexistence proof, including the symmetry-free case.

04\_projective\_plane\_12

It explicitly excludes partial reductions, restricted automorphism searches, and uncertified solver failures.

04\_projective\_plane\_12

The latest primary source I located that explicitly discusses the general status, published in October 2025, still identifies order $12$ as the smallest unresolved order. My targeted searches found no subsequent complete resolution. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv](https://arxiv.org/abs/2510.19804)

Accordingly, I followed the prompt’s hard-stop provision: preserve all machine-checkable work and report the strongest rigorously established result without fabricating success.

04\_projective\_plane\_12

## Strongest verified result

Assume that an order-12 plane exists and let $N$ be its incidence matrix.

| Object | Forced property |
| --- | --- |
| Incidence matrix | $\lvert\det N\rvert=13\cdot12^{78}$ |
| Matrix inverse | $N^{-1}=(13N^{T}-J)/156$ |
| Smith normal form | Every invariant factor divides $156$ |
| Modular ranks | $\operatorname{rank}_{\mathbf F_3}N=79$, $\operatorname{rank}_{\mathbf F_{13}}N=156$ |
| Ternary incidence code $C$ | $[157,79,13]_3$ |
| Minimum words of $C$ | Exactly the $314$ signed incidence vectors of the $157$ lines |
| Dual code $D=C^\perp$ | $[157,78,d]_3$ with $d\ge18$ |
| Self-dual extension $E$ | Ternary Type-III self-dual $[160,80]$ |
| Forced low weights in $E$ | $A_3=2,\ A_6=A_9=A_{12}=0,\ A_{15}=942$ |

These conditions are **universal**. They do not assume that the plane has a nontrivial automorphism.

### 1\. Exact ternary-code decomposition

Over $\mathbf F_3$, let $r_i$ denote the incidence vector of line $i$, and define

$$
C=\langle r_1,\ldots,r_{157}\rangle .
$$

Every pair of line vectors, including a vector paired with itself, has scalar product $1\pmod3$. For $c\in C$, let

$$
s(c)=\sum_{x=1}^{157}c_x.
$$

Then every line has the same scalar product with $c$:

$$
r_i\cdot c=s(c).
$$

The difference code

$$
D=\langle r_i-r_j:i,j\rangle
$$

is exactly

$$
D=C^\perp=\{c\in C:s(c)=0\},
$$

with $\dim C=79$ and $\dim D=78$.

Words in $D$ have weight divisible by $3$; words in $C\setminus D$ have weight congruent to $1\pmod3$.

### 2\. Exact classification of the weight-13 words

For $c\in C\setminus D$, every line meets $\operatorname{supp}(c)$, because its line sum is the nonzero quantity $s(c)$. Hence the support is a blocking set and has at least $13$ points.

At equality, the support must be a line. Intersecting it with all other lines then forces every nonzero coefficient to be equal. Therefore the weight-13 words are precisely

$$
\pm r_i,\qquad 1\le i\le157.
$$

There are exactly $2\cdot157=314$ such words.

### 3\. Proof that $D$ has no weight-15 word

Let $0\ne d\in D$, with support $S$.

Because every line sum is zero, every line through a support point must contain another support point. The $13$ lines through a point partition the other support points, giving

$$
|S|-1\ge13.
$$

Since $|S|$ is divisible by $3$, initially $|S|\ge15$.

Suppose $|S|=15$. At every support point, exactly one of its lines is a trisecant of $S$, while the other twelve are bisecants. The trisecants consequently partition $S$ into five triples.

On a bisecant, the two nonzero ternary symbols must be opposite. On a trisecant, all three symbols must be equal. Selecting points from three different triples produces three pairwise bisecants, so their three symbols would have to be pairwise opposite. This is impossible with only the two nonzero values $1$ and $-1$ in $\mathbf F_3$.

Therefore

$$
d(D)\ge18.
$$

The independent integer line-distribution program reaches the same conclusion without using this sign argument.

### 4\. Complete local structure of a hypothetical weight-18 word

Suppose $d\in D$ has weight $18$, with $A$ the $+1$ points and $B$ the $-1$ points.

Exact integer enumeration of every possible line type gives the unique solution

$$
|A|=|B|=9
$$

and

$$
n_{00}=52,\qquad n_{30}=12,\qquad n_{11}=81,\qquad n_{03}=12.
$$

Thus:

-   twelve lines contain three $A$\-points and no $B$\-points;
    
-   twelve lines contain three $B$\-points and no $A$\-points;
    
-   eighty-one lines contain one point of each sign;
    
-   fifty-two lines avoid the support.
    

The twelve triples on each sign class form a $2-(9,3,1)$ design, necessarily an affine plane $AG(2,3)$.

A further incidence argument restricts the number $t$ of parallel classes whose three ambient lines become concurrent:

$$
t\in\{0,1,4\}.
$$

The originally possible values $t=2,3$ are impossible because each nonconcurrent parallel class must match its three pair-intersection points with three distinct nonconcurrent classes on the opposite sign side.

This is a useful local normal form, although I have not established whether the refinement is new in the literature.

### 5\. Forced self-dual code

Define

$$
b_i=(r_i,1,1,0)\in\mathbf F_3^{160}
$$

and

$$
z=(0^{157},1,-1,1).
$$

The vectors $b_i$ and $z$ are mutually orthogonal. Their span has dimension $80$, so it is a ternary self-dual code $E$. Explicitly,

$$
E=\{(u,s+c,s-c,c): u\in C,\ s=s(u),\ c\in\mathbf F_3\}.
$$

The preceding minimum-weight results force:

$$
A_3(E)=2,
$$

corresponding to $\pm z$;

$$
A_6(E)=A_9(E)=A_{12}(E)=0;
$$

and

$$
A_{15}(E)=314\cdot3=942.
$$

## Adversarial checks that failed to produce a contradiction

### Ordinary Gleason enumeration

I imposed the forced low-weight coefficients on the general Type-III self-dual Hamming weight enumerator of length $160$. Even after arbitrarily setting all coefficients at weights $18,21,\ldots,39$ to zero, an exact nonnegative integral formal enumerator exists and sums to $3^{80}$.

Therefore, the one-variable Gleason theorem does **not** rule out the required self-dual code.

### MacWilliams constraints

I also imposed the exact MacWilliams transform between $D$ and $C=D^\perp$, including:

$$
B_i=A_i\quad(3\mid i),
$$
 
$$
B_i=0\quad(i\equiv2\pmod3),
$$
 
$$
B_1=B_4=B_7=B_{10}=0,\qquad B_{13}=314.
$$

The rational linear program is exactly feasible. A floating-point solver had incorrectly suggested infeasibility; the included rational certificate disproves that numerical claim.

The certificate is rational rather than integral, so it does not construct a code. It only shows that these MacWilliams constraints are not by themselves contradictory.

## Why automorphism searches are insufficient

Peer-reviewed work has ruled out a collineation group of order $4$ and concludes that any hypothetical order-12 plane can only have a collineation group of order $1$, $2$, or $3$. In particular, the trivial-automorphism case remains unavoidable. [![](https://www.google.com/s2/favicons?domain=https://onlinelibrary.wiley.com&sz=128)Wiley Online Library](https://onlinelibrary.wiley.com/doi/full/10.1002/jcd.21869)

The known equivalence with a balancedly multi-splittable quaternary Hadamard matrix of order $144$ is exact, but it transfers rather than removes the unresolved existence problem. [![](https://www.google.com/s2/favicons?domain=https://www.combinatorics.org&sz=128)Combinatorics.org](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v30i2p49)

## Exact remaining gap

The strongest current route is now:

1.  Classify or exclude the three weight-18 geometries $t=0,1,4$.
    
2.  Develop complete or genus-2 weight enumerator constraints that incorporate the $314$ signed line vectors, not merely their Hamming weights.
    
3.  Use the ternary code as the invariant in a canonical augmentation search, with proof-producing SAT or exact-cover certificates.
    
4.  Maintain a separate branch with $A_{18}=0$, since the ordinary Gleason calculation remains feasible even with no codewords through weight $39$.
    

No order-10 nonexistence reproduction is included, so the package is a research checkpoint rather than the complete archival artifact demanded for a final resolution.

## Research package

All included checks passed on the supplied environment. The positive incidence verifiers were independently tested on $PG(2,3)$ and $PG(2,5)$.

-   Download the complete research checkpoint
    
-   REPORT.md
    
-   README.md
    
-   SHA-256 manifest
    

ZIP SHA-256:

```
```
f0e32fce6da6e7f4d7d0b422aa8554ea1f67055395d8fb85ac653cef4322ea00
```
```

**Essential conclusion:** the existence question remains unresolved, but any order-12 plane is now reduced to a highly constrained, symmetry-independent ternary-code object. The most concrete new target is the exhaustive treatment of the three possible embedded $AG(2,3)$\-pair configurations arising from a weight-18 dual word.

![](https://www.google.com/s2/favicons?domain=https://www.combinatorics.org&sz=32)

![](https://www.google.com/s2/favicons?domain=https://onlinelibrary.wiley.com&sz=32)

![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=32)

Sources

You: 

what are the next steps?

ChatGPT: 

Worked for 19m 58s

## Rephrased question

> Given the current order-12 projective-plane checkpoint, what is the most productive sequence of mathematical and computational steps toward either a construction or a certified nonexistence proof?

## Best immediate objective

The next milestone should be:

$$
\boxed{\text{Either construct a plane containing a weight-18 dual word, or prove }A_{18}(D)=0.}
$$

Here $D=C^\perp$ is the ternary dual incidence code. Proving $A_{18}(D)=0$ would strengthen

$$
d(D)\ge 18
$$

to

$$
d(D)\ge 21.
$$

This would **not yet resolve the order-12 problem**, but it is the first remaining subproblem that has been reduced to a small number of explicit finite configurations. It is far better targeted than immediately attacking an unconstrained $157\times157$ incidence matrix.

---

# 1\. Correct the literature audit first

The current research package omitted a central paper:

> Marshall Hall Jr. and John Wilkinson, *Ternary and Binary Codes for a Plane of Order 12*, Journal of Combinatorial Theory A 36 (1984), 183–203.

This paper must be obtained and checked line by line against the checkpoint’s coding-theory results. A later expert account reports that Hall and Wilkinson reduced the number of essential weight-enumerator coefficients to 16, compared with three in the successful order-10 computation. [![](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com&sz=128)ScienceDirect+1](https://www.sciencedirect.com/science/article/pii/0097316584900049?utm_source=chatgpt.com)

Create a concordance table:

| Checkpoint result | Hall–Wilkinson status |
| --- | --- |
| $\operatorname{rank}_{\mathbf F_3}N=79$ | Known/new proof? |
| $D=C^\perp$ and $\dim D=78$ | Known? |
| Classification of weight-13 words | Known? |
| $d(D)\ge18$ | Known? |
| Weight-18 distribution $9+9$ | Known? |
| Two embedded $AG(2,3)$ structures | Known? |
| Restriction $u\in\{0,1,4\}$ | Known or potentially new? |
| Forced self-dual $[160,80]$ extension | Known? |

Until this comparison is complete, none of these results should be advertised as novel. The $u\in\{0,1,4\}$ refinement is currently the most plausible genuinely new ingredient, but that is not yet established.

---

# 2\. Formalize the exact weight-18 reduction

Assume $d\in D$ has weight $18$. Its support splits into two nine-point sets,

$$
A=\{d=1\},\qquad B=\{d=-1\}.
$$

The established line distribution is

$$
n_{30}=12,\qquad n_{03}=12,\qquad n_{11}=81,\qquad n_{00}=52.
$$

The twelve triples on $A$ form $AG(2,3)$, and independently the twelve triples on $B$ form another $AG(2,3)$.

For each of the $139$ points $x\notin A\cup B$, let $t(x)$ be the number of $A$\-triple lines through $x$. Counting the nine $A$\-points and nine $B$\-points shows that the number of $B$\-triple lines is also $t(x)$. Then:

$$
\begin{aligned} \text{\(A\)-triple lines through }x &=t,\\ \text{\(B\)-triple lines through }x &=t,\\ \text{cross lines through }x &=9-3t,\\ \text{zero lines through }x &=4+t. \end{aligned}
$$

For $u\in\{0,1,4\}$, the outside-point distribution is:

| $u$ | $x_0$ | $x_1$ | $x_2$ | $x_3$ |
| --- | --- | --- | --- | --- |
| 0 | 31 | 96 | 12 | 0 |
| 1 | 30 | 99 | 9 | 1 |
| 4 | 27 | 108 | 0 | 4 |

Here $u$ is the number of parallel classes whose three affine lines become concurrent in the ambient plane.

This should be written as a rigorous reduction theorem before implementing the search.

---

# 3\. Enumerate the three skeleton families

For each nonconcurrent parallel class, the three pairwise intersections of its lines must be identified with intersections belonging to nonconcurrent classes on the opposite side.

This gives a bipartite graph between the nonconcurrent parallel classes of $A$ and $B$:

| Case | Class-intersection graph | Raw labelled assignments |
| --- | --- | --- |
| $u=0$ | $K_{4,4}$ minus a perfect matching | $6^8=1,679,616$ |
| $u=1$ | $K_{3,3}$ | $6^6=46,656$ |
| $u=4$ | Four paired concurrence points | $4!=24$ |

These are not final isomorphism counts. They should be quotiented by

$$
AGL(2,3)\times AGL(2,3)
$$

together with interchange of $A$ and $B$. Canonical graph labelling should generate one representative per orbit and a manifest recording:

-   the raw number generated;
    
-   the number rejected by normalization;
    
-   the number rejected as isomorphic;
    
-   the number of surviving canonical cases;
    
-   the stabilizer size of each case.
    

This is essential because an UNSAT result is worthless unless the normal forms are proved complete. The original prompt explicitly demands complete case coverage and certificates, rather than a solver failure over an assumed normal form.

04\_projective\_plane\_12

---

# 4\. Encode the 81 cross lines as partial matchings

Identify the 81 possible $A$\-to-$B$ pairs with the edges of $K_{9,9}$.

For every outside point $x$, define a matching

$$
M_x\subseteq A\times B.
$$

An edge $(a,b)\in M_x$ means that the cross line through $a$ and $b$ also contains $x$.

The size of the matching is forced:

$$
|M_x|=9-3t(x).
$$

Thus:

| $t(x)$ | Structure of $M_x$ |
| --- | --- |
| 0 | Perfect matching of $A$ and $B$, size 9 |
| 1 | Bijection between two six-point complements, size 6 |
| 2 | Bijection between two remaining triples, size 3 |
| 3 | Empty matching |

Use Boolean variables

$$
y_{x,a,b}=1\iff (a,b)\in M_x.
$$

The exact constraints are:

### Local matching constraints

Each available $A$\-point and $B$\-point occurs exactly once in $M_x$; points already covered by triple lines through $x$ occur zero times.

### Cross-line size

Every edge of $K_{9,9}$ belongs to exactly eleven outside-point matchings:

$$
\sum_x y_{x,a,b}=11.
$$

Together with its endpoints $a,b$, this gives a cross line of size $13$.

### Unique intersection of disjoint cross lines

For every pair of disjoint edges $e,f\in E(K_{9,9})$,

$$
\#\{x:e,f\in M_x\}=1.
$$

There are

$$
2\binom92^2=2592
$$

such unordered pairs.

### No duplicate intersections

If two outside points already lie together on an $A$\-triple line or a $B$\-triple line, their matchings must be disjoint. More generally,

$$
|M_x\cap M_y|\le1.
$$

These constraints describe the entire cross-line layer, not merely a necessary numerical relaxation.

---

# 5\. Decompose the residual graph into 52 zero lines

After constructing:

-   12 $A$\-triple lines;
    
-   12 $B$\-triple lines;
    
-   81 cross lines;
    

form a graph $R$ on the 139 outside points. Join $x$ and $y$ in $R$ exactly when their pair has not yet appeared on one of those 105 lines.

The remaining 52 lines avoid $A\cup B$, so the final condition is exactly:

$$
E(R)\text{ decomposes into }52\text{ edge-disjoint copies of }K_{13}.
$$

The count checks:

$$
\binom{139}{2} -12\binom{10}{2} -12\binom{10}{2} -81\binom{11}{2} =4056,
$$

while

$$
52\binom{13}{2}=4056.
$$

Therefore no edges are unaccounted for.

This gives an important exact equivalence:

> A projective plane of order $12$ containing a weight-18 dual word exists if and only if one of the three canonical skeleton families admits both the matching system above and the residual $K_{13}$\-decomposition.

If the decomposition succeeds, the result is not merely a partial plane. It is a full projective plane because all $\binom{157}{2}$ point pairs have been covered exactly once.

---

# 6\. Use proof-producing computation

The search should have two independently checked layers.

### Layer A: cross-matchings

Encode the matching conditions in SAT or pseudo-Boolean form. For every UNSAT instance, retain an LRAT, DRAT, or equivalent proof certificate and verify it with an independent checker.

### Layer B: residual $K_{13}$\-decomposition

For each surviving cross-layer solution:

1.  construct $R$;
    
2.  enumerate or canonically generate candidate $13$\-cliques;
    
3.  solve the exact-cover problem;
    
4.  retain either the decomposition or a certified UNSAT proof.
    

The archival package should contain:

```
```
weight18/
  reduction.md
  generate_skeletons.py
  canonicalize.py
  encode_cross.py
  verify_cross.py
  residual_graph.py
  encode_cliques.py
  verify_decomposition.py
  cases.json
  certificates/
  hashes.sha256
```
```

The checker should validate the mathematical objects directly, not merely trust the solver output. That matches the prompt’s requirement for a reduction theorem, complete case tree, solver inputs, proof certificates, checkers, and a case-count audit.

04\_projective\_plane\_12

---

# 7\. Decision tree after the weight-18 search

## Outcome A: a complete configuration is found

Assemble the $157$ lines:

$$
12+12+81+52=157.
$$

Then run at least two independent incidence verifiers checking:

$$
NN^T=N^TN=12I+J.
$$

That would completely solve the problem positively.

## Outcome B: all cases are certified UNSAT

Then publish the theorem

$$
A_{18}(D)=0,\qquad d(D)\ge21.
$$

The next target becomes weight $21$. A preliminary, not yet independently audited integer enumeration found only 20 candidate line-distribution patterns up to sign, with sign-class sizes $9+12$ or $12+9$. Those patterns should be regenerated independently and converted into analogous geometric normal forms.

## Outcome C: the matching layer has many solutions

Use the residual graph earlier in the search. Useful propagation conditions include:

$$
\deg_R(x)=12(4+t(x)),
$$

and every residual neighborhood must be partitionable among the $4+t(x)$ zero lines through $x$. Clique feasibility, divisibility, and common-neighbour bounds can reject matching assignments before they are completed.

---

# 8\. Run one algebraic branch in parallel

The ordinary Hamming weight enumerator has already proved too weak. The next algebraic objects should retain signs and pairwise relationships:

-   complete weight enumerators;
    
-   biweight or genus-2 weight enumerators;
    
-   Jacobi weight enumerators relative to one or two line words;
    
-   harmonic weight enumerators;
    
-   exact linear or semidefinite bounds using the 314 signed weight-13 line vectors.
    

The crucial information lost by the ordinary enumerator is that the 157 line supports intersect pairwise in exactly one coordinate. A stronger enumerator should encode those intersections explicitly.

A successful exact infeasibility certificate here could eliminate weight 18, or conceivably the entire code, without enumerating all geometric cases.

---

# 9\. Keep alternate encodings secondary

Automorphism searches should be auxiliary only. A hypothetical order-12 plane can have collineation-group order only $1$, $2$, or $3$, so the asymmetric case cannot be avoided. [![](https://www.google.com/s2/favicons?domain=https://onlinelibrary.wiley.com&sz=128)Wiley Online Library](https://onlinelibrary.wiley.com/doi/full/10.1002/jcd.21869?utm_source=chatgpt.com)

The equivalent balancedly multi-splittable quaternary Hadamard formulation of order $144$ is worth implementing as an independent cross-check. The equivalence is exact for projective planes of order $n$, but it does not by itself reduce the problem. [![](https://www.google.com/s2/favicons?domain=https://www.combinatorics.org&sz=128)combinatorics.org](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v30i2p49)

A direct unconstrained $157\times157$ SAT model, or equivalently an $\mathrm{OA}(144,13,12,2)$ model, should be the fallback rather than the first move.

---

## Recommended priority order

1.  **Obtain and audit Hall–Wilkinson 1984.**
    
2.  **Write a complete proof of the weight-18 matching-and-clique equivalence.**
    
3.  **Canonically enumerate the $u=0,1,4$ skeletons.**
    
4.  **Run certified cross-matching SAT instances.**
    
5.  **Run certified residual $K_{13}$\-decomposition instances.**
    
6.  **In parallel, develop genus-2 or complete-weight-enumerator constraints.**
    
7.  **If weight 18 is excluded, classify weight-21 words and repeat.**
    
8.  **Only afterward launch a global code-aware canonical augmentation.**
    

## Essential conclusion

The next step is **not** a larger blind search. It is a complete, certificate-producing treatment of the weight-18 configuration.

The ideal next research artifact is one of:

$$
\boxed{\text{a full order-12 plane}}
$$

or

$$
\boxed{\text{a verified theorem that the dual ternary code has no weight-18 words}.}
$$

The second result would still be partial, but it would be a substantial universal theorem applying even to planes with trivial automorphism group, and it would move the problem from $d(D)\ge18$ to the much more restrictive $d(D)\ge21$.

![](https://www.google.com/s2/favicons?domain=https://onlinelibrary.wiley.com&sz=32)

![](https://www.google.com/s2/favicons?domain=https://mathoverflow.net&sz=32)

![](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com&sz=32)

Sources