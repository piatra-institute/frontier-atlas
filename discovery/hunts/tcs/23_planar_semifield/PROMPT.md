# 23. A new planar function / commutative semifield of open order

**Find.** A planar (perfect nonlinear) function f: F_q -> F_q in odd characteristic, q = p^m, that is not equivalent to a catalogued one, or equivalently a new commutative semifield of an order where the classification is incomplete. Planar functions have the property that x -> f(x+a) - f(x) is a bijection for every a != 0; they are equivalent to commutative semifields and to certain projective planes, and new families at specific orders remain to be found.

**What counts as a win.** One explicit polynomial f over F_q that is planar and is shown inequivalent to known families (via a computed isotopy/CCZ invariant that differs). One-sided: a new planar function is a result.

**Checker (seconds).** For each a != 0, tabulate the map x -> f(x+a) - f(x) over F_q and assert it is a bijection (planarity). For small q (a few thousand elements) this is q(q-1) field operations, milliseconds. Then compute an equivalence invariant (e.g. the nuclei / kernel structure of the associated semifield, or a rank invariant) and compare to known families.

**Search plan.** Structured/algebraic: search Dembowski-Ostrom polynomials (planar candidates are typically DO) over F_{p^m} with orderly enumeration modulo equivalence; twist/scion constructions from known semifields; Groebner/CAS (Sage/GAP) for the planarity system at fixed coefficient patterns.

**Prior art (verify).** Dembowski & Ostrom (1968); Coulter & Matthews (1997) planar functions; Pott's surveys on commutative semifields and planar functions; semifield-order classification tables (verify which orders remain open).
