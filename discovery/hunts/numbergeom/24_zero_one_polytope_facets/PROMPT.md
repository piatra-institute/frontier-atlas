# 0/1-polytope with more facets than the record

**Find.** A 0/1-polytope in dimension d (vertices a subset of {0,1}^d) with more facets than the largest published facet count for that dimension, for a small d where the maximum is unknown.

**What counts as a win (one-sided).** One vertex set in {0,1}^d whose convex hull has facet count above the current record. A single polytope beats the record; failure proves nothing.

**Checker (seconds).** Compute the facets of the 0/1-polytope exactly (exact convex hull / LP over rationals) and count them. For small d and moderate vertex counts this is exact and fast; re-derive the facet count with an independent hull routine.

**Search plan.** Search vertex subsets of {0,1}^d that maximize facets: local search adding/removing vertices, scored by facet count; start from known facet-rich families (cut polytopes, cyclic-like 0/1 configurations); ILP/CP heuristics. Exact facet enumeration only on promising candidates to control cost.

**Prior art (verify).** The maximum number of facets of a d-dimensional 0/1-polytope is known only for small d and otherwise bounded; the growth rate and exact small values are open. See Guenter Ziegler, "Lectures on 0/1-polytopes" (ca. 2000), and Bahr-Ziegler and related facet-count tables. Confirm the record for the target d before starting (verify).
