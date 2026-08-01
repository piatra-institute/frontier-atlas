Worked for 100m 10s

# Determination target

Determine the exact value of $a(7)$ with matching lower and upper certificates; failing that, produce the strongest independently replayable interval and identify the remaining obstruction.

# Result

## $a(7)$ was not determined

This run establishes the following independently replayable interval:

$$
\boxed{236\le a(7)\le 291}.
$$

The lower bound is certified by an explicit $236$\-point cap and three independent line-free checks. The upper bound is certified by exact hyperplane-moment arithmetic, conditional only on the established theorem $a(6)=112$.

No cap larger than $236$ was found, and no proof of $a(7)\le 290$ was completed. Therefore this is a **partial result**, not a resolution of $a(7)$.

There is a 2022 preprint claiming that no $289$\-cap exists, which would give $a(7)\le 288$. Its proof relies on several finite Java searches. The version inspected describes the searches and their normalization but does not include the source, case logs, or a replayable proof trace, and I did not locate an accompanying artifact repository. Consequently:

$$
\begin{aligned} \text{strongest literature claim located:}&\quad 236\le a(7)\le288,\\ \text{independently replayed in this run:}&\quad 236\le a(7)\le291. \end{aligned}
$$

The distinction matters under the prompt’s preservation and independent-verification requirements. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv+3![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv+3![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv+3](https://arxiv.org/abs/2206.09804)

---

# 1\. Certified lower bound: $a(7)\ge236$

I reconstructed the Edel–Bierbrauer/Calderbank–Fishburn construction as three affine layers:

$$
C= \bigl(\{0\}\times(D\cup R)\bigr) \cup \bigl(\{1\}\times(\bar D\cup R)\bigr) \cup \bigl(\{2\}\times U\bigr),
$$

where:

-   $D$ consists of the $80$ signed vectors supported on the ten blocks of a $2\!-\!(6,3,2)$ design;

-   $\bar D$ consists of the $80$ signed vectors supported on the complementary ten triples;

-   $R$ consists of the $32$ full-support vectors having an even number of coordinates equal to $2$;

-   $U$ consists of the $12$ weight-one vectors.


Thus the layer sizes are

$$
112,\quad112,\quad12,
$$

and

$$
|C|=236.
$$

This is the construction described in the prior literature. [![](https://www.google.com/s2/favicons?domain=https://www.yvesedel.de&sz=128)Yves Edel+1](https://www.yvesedel.de/Papers/smallCaps.pdf)

## Independent checks

| Verification method | Work performed | Result |
| --- | --- | --- |
| Pair-completion test | All $\binom{236}{2}=27{,}730$ distinct pairs | PASS |
| Direct triple scan | All $\binom{236}{3}=2{,}162{,}940$ triples | PASS |
| Affine-line enumeration | All $796{,}797$ lines of $\mathrm{AG}(7,3)$ | PASS |

The pair checker tests the precise cap condition

$$
x\ne y\in C\quad\Longrightarrow\quad -x-y\notin C.
$$

The triple checker separately confirms that no distinct $x,y,z\in C$ satisfy $x+y+z=0$. The C++ line checker independently constructs every affine line and verifies that none contains three cap points.

### Lower-bound artifacts

-   cf236.json

-   cf236.csv

-   cf236.txt

-   generate\_cf236.py

-   verify\_pair\_midpoints.py

-   verify\_triples.py

-   verify\_lines.cpp

-   Pair-check log

-   Triple-check log

-   Line-enumeration log


This completes target $P_2$.

---

# 2\. Exact upper certificate: $a(7)\le291$

This is an exact hyperplane-distribution argument, not a floating-point LP result.

It uses the established theorem

$$
a(6)=112,
$$

so every affine hyperplane of $\mathbb F_3^7$ contains at most $112$ points of a cap. Potechin proved the $112$ bound and uniqueness of the maximal six-dimensional cap up to affine equivalence. [![](https://www.google.com/s2/favicons?domain=https://link.springer.com&sz=128)Springer](https://link.springer.com/article/10.1007/s10623-007-9132-z)

Suppose for contradiction that $C$ is a $292$\-cap.

A hyperplane direction partitions $\mathbb F_3^7$ into three parallel hyperplanes. Write the corresponding cap intersection sizes, in decreasing order, as

$$
t=(a,b,c),\qquad a+b+c=292,\qquad 112\ge a\ge b\ge c\ge0.
$$

There are

$$
\frac{3^7-1}{2}=1093
$$

hyperplane directions. Define

$$
P(t)=\binom a2+\binom b2+\binom c2, \qquad Q(t)=\binom a3+\binom b3+\binom c3.
$$

Every pair of cap points occurs together in exactly $364$ hyperplane directions, while every cap triple occurs together in exactly $121$ directions. The latter holds because every triple in a cap is noncollinear. Consequently,

$$
\sum_t n_t=1093,
$$

$$
\sum_t n_tP(t) =364\binom{292}{2} =15{,}464{,}904,
$$

and

$$
\sum_t n_tQ(t) =121\binom{292}{3} =496{,}944{,}580,
$$

where $n_t$ is the number of directions with profile $t$.

There are only $184$ arithmetically admissible sorted triples $t$.

## Exact slack certificate

Take the base profile

$$
A=(98,97,97)
$$

and define

$$
S(t)=43\bigl(Q(t)-Q(A)\bigr) -3932\bigl(P(t)-P(A)\bigr).
$$

Exact enumeration of all $184$ profiles gives

$$
S(t)\ge0
$$

for every admissible $t$. Summing the slack over all directions gives

$$
\sum_t n_tS(t)=2328.
$$

There are two zero-slack profiles:

$$
(98,97,97),\qquad (112,112,68).
$$

Only seven positive-slack profiles have slack at most $2328$, because any profile with larger slack cannot occur. Solving the exact nonnegative integer equation for total slack $2328$ leaves only four possible multiplicity patterns.

In every one of those four patterns, the total $P-P(A)$ contribution from positive-slack profiles is exactly $11$. Hence the remaining excess in the pair moment must be supplied by copies of $(112,112,68)$.

But

$$
P(112,112,68)-P(98,97,97)=645,
$$

whereas the remaining pair excess is

$$
91{,}848.
$$

This is impossible because

$$
91{,}848\equiv258\pmod{645}.
$$

Thus a $292$\-cap cannot exist:

$$
\boxed{a(7)\le291}.
$$

The Python certificate records all $184$ profiles, not merely the exceptional ones. A separately written C++ verifier independently reconstructs the admissible profiles, moment totals, slack partition and modular contradiction.

### Upper-bound artifacts

-   upper291\_certificate.json

-   certify\_upper\_291.py

-   verify\_upper\_291.cpp

-   Python verification log

-   Independent C++ verification log


The only external premise is the published theorem $a(6)\le112$. This run constructed and checked a $112$\-cap, but did not independently reproduce Potechin’s no-$113$\-cap computation.

---

# 3\. Exact structural obstruction at size $291$

The same method gives a strong necessary condition on any hypothetical $291$\-cap.

For the $192$ admissible profiles with

$$
a+b+c=291,\qquad a,b,c\le112,
$$

define the exact slack

$$
S_{291}(t) = 631\bigl(Q(t)-Q(97,97,97)\bigr) - 57531\bigl(P(t)-P(97,97,97)\bigr).
$$

Among all $192$ profiles:

-   the only negative-slack type is

    $$
    (112,112,67);
    $$

-   its slack is

    $$
    -74{,}250;
    $$

-   the aggregate slack forced by the moment identities is

    $$
    -505{,}661.
    $$


Therefore every hypothetical $291$\-cap would have at least

$$
\left\lceil\frac{505{,}661}{74{,}250}\right\rceil=7
$$

hyperplane directions with profile

$$
\boxed{(112,112,67)}.
$$

In particular, such a cap would repeatedly decompose into two maximal $112$\-caps in parallel six-flats and a $67$\-cap in the third parallel six-flat.

This does **not** prove $a(7)\le290$. It isolates the next structural problem:

> Eliminate, up to affine equivalence, pairs of parallel $112$\-caps whose pairwise forbidden sums leave room for a $67$\-cap in the third layer.

### Size-$291$ artifacts

-   standard\_diagram\_291.json

-   certify\_291\_standard\_diagram.py

-   verify\_standard\_diagrams.cpp

-   Python log

-   Independent C++ log


---

# 4\. Arithmetic reconstruction of the claimed $a(7)\le288$ route

For a hypothetical $289$\-cap, exact enumeration gives $208$ possible hyperplane profiles. An exact separating slack function shows that at least one direction must have one of the four profiles

$$
(112,112,65),\quad (112,111,66),\quad (112,110,67),\quad (111,111,67).
$$

This reproduces the arithmetic “standard diagram” underlying the 2022 no-$289$\-cap claim. The cited work then eliminates those large-slice configurations using normalized computer searches. [![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv+2![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=128)arXiv+2](https://arxiv.org/pdf/2206.09804)

I reproduced one explicitly described normalized subsearch—$486$ transformations in the first construction option—and obtained the expected result that all $729$ candidate middle-layer points are blocked. However, I did not reconstruct a completeness proof showing that the tested transformations exhaust every affine-equivalence case required by the theorem.

Therefore the artifacts below certify the moment arithmetic, but **not** the published conclusion $a(7)\le288$.

-   standard\_diagram\_289.json

-   certify\_289\_standard\_diagram.py

-   replay\_thackeray\_option1.cpp

-   Normalized-search replay log


---

# 5\. Adversarial search around the $236$\-cap

## Local exchange obstruction

For each point $p\notin C$, its blockers are the disjoint cap pairs

$$
\{x,y\}\subset C,\qquad x+y+p=0.
$$

The smallest blocker count of an outside point is $10$.

Exact searches established:

1.  There are $24$ outside points with exactly ten blocker pairs.

2.  All

    $$
    24\cdot2^{10}=24{,}576
    $$

    minimal ten-point removal sets unlock exactly one outside point, never two.

3.  Enumeration of $6{,}283{,}264$ distinct eleven-point removal sets also found that none unlocks two outside points.

4.  Across all

    $$
    \binom{1951}{2}=1{,}902{,}225
    $$

    pairs of outside points, the minimum number of original cap points that must be removed to unlock both is $16$.


Consequently, no improving exchange that removes at most $15$ points from this particular $236$\-cap is possible.

This is a local-optimality statement about the explicit construction, not a global upper bound and not proof that $236$ is maximal.

Artifacts:

-   analyze\_cf236.py

-   Blocker analysis log

-   exchange10\_search.json

-   search\_exchange10.py

-   search\_exchange11.cpp

-   Eleven-removal log

-   min\_pair\_unlock.cpp

-   All-pairs removal log


## Three-layer alignment search

Writing a candidate as two $112$\-point layers plus a third allowed layer, I searched alignments of the two maximal layers.

-   All $46{,}080$ monomial linear alignments were enumerated exactly.

-   The largest allowed third layer was $12$.

-   A deterministic sample of $500{,}000$ general invertible $6\times6$ matrices over $\mathbb F_3$ also produced a maximum third-layer allowance of $12$.


Thus the known

$$
112+112+12=236
$$

alignment remained best in the searched family. The monomial result is exhaustive for that subgroup; the $500{,}000$\-matrix result is heuristic and gives no global conclusion.

Artifacts:

-   search\_layer\_monomial.cpp

-   Monomial search log

-   search\_layer\_random\_gl.cpp

-   Random search log


---

# 6\. Six-dimensional pipeline status

An explicit $112$\-cap in $\mathbb F_3^6$ was generated and independently verified by pair, triple and full-line checks.

-   a112.json

-   export\_a112.py

-   Pair-check log

-   Triple-check log

-   Full-line-check log


However, no replayable UNSAT proof or isomorph-free enumeration excluding size $113$ was completed. Thus $P_1$ was only half reproduced.

---

# 7\. Graded outcome

| Target | Outcome |
| --- | --- |
| $P_1$: reproduce $a(6)=112$ | **Partial:** explicit $112$\-cap certified; no independent no-$113$ proof |
| $P_2$: reproduce $236$\-cap | **Achieved** |
| $P_3$: cap larger than $236$ | **Not achieved** |
| $P_4$: certified $U<291$ | **Not achieved**; exact $U=291$ independently reproduced |
| $P_5$: strict improvement on both sides | **Not achieved** |
| $P_6$: determine $a(7)$ | **Not achieved** |

The strongest completed result is therefore

$$
\boxed{236\le a(7)\le291},
$$

plus the exact necessary condition that every $291$\-cap would possess at least seven $(112,112,67)$ hyperplane directions.

---

# 8\. Two technical corrections to the supplied formulation

1.  In characteristic $3$, if

    $$
    x+y+z=0
    $$

    and two variables are equal, then all three are equal. For example,

    $$
    x=y\implies 2x+z=0\implies z=x.
    $$

    Thus the precise diagonal formulation is that the equation has only solutions $x=y=z$ inside a cap.

2.  Arbitrary pairwise-sum uniqueness is a Sidon-type condition and is stronger than being a cap. The correct quadratic-time cap test is

    $$
    \forall\,x\ne y\in C:\quad -x-y\notin C,
    $$

    not general collision-freeness of the multiset $\{x+y\}$.


---

# Audit limitation

The source files, coordinates, certificates and execution logs were preserved, and the central claims have independent Python/C++ implementations. A single archive, solver-version inventory and SHA-256 manifest spanning the directory were **not completed** in this run, so the preservation package does not yet fully satisfy requirement 6.3.

## Essential takeaway

The exact value remains open in this run. The $236$\-point lower witness is fully reproduced, the $291$ upper bound has a compact exact certificate, and the next concrete upper-bound bottleneck is the elimination of the forced $(112,112,67)$ parallel-hyperplane configuration.

cf236.jsonCodeOpen file

cf236.csvSpreadsheetOpen file

cf236.txtDocumentOpen file

generate\_cf236.pyCodeOpen file

verify\_pair\_midpoints.pyCodeOpen file

verify\_triples.pyCodeOpen file

verify\_lines.cppCodeOpen file

upper291\_certificate.jsonCodeOpen file

certify\_upper\_291.pyCodeOpen file

verify\_upper\_291.cppCodeOpen file

standard\_diagram\_291.jsonCodeOpen file

certify\_291\_standard\_diagram.pyCodeOpen file

verify\_standard\_diagrams.cppCodeOpen file

standard\_diagram\_289.jsonCodeOpen file

certify\_289\_standard\_diagram.pyCodeOpen file

replay\_thackeray\_option1.cppCodeOpen file

analyze\_cf236.pyCodeOpen file

exchange10\_search.jsonCodeOpen file

search\_exchange10.pyCodeOpen file

search\_exchange11.cppCodeOpen file

min\_pair\_unlock.cppCodeOpen file

search\_layer\_monomial.cppCodeOpen file

search\_layer\_random\_gl.cppCodeOpen file

a112.jsonCodeOpen file

export\_a112.pyCodeOpen file

22 more

![](https://www.google.com/s2/favicons?domain=https://link.springer.com&sz=32)

![](https://www.google.com/s2/favicons?domain=https://www.yvesedel.de&sz=32)

![](https://www.google.com/s2/favicons?domain=https://arxiv.org&sz=32)

Sources
