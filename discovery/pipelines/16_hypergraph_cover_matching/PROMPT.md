# Batch sweep: refute hypergraph cover/matching/coloring bounds

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit hypergraph violating a stated bound, or hardened survivors. Refutation is the clean win.

**Family + panel.** Uniform and r-partite hypergraphs; invariants: cover number τ, matching number ν, fractional τ_f and ν_f, chromatic number, and edge count. Anchor conjectures: Ryser's conjecture τ ≤ (r−1)ν for r-partite r-uniform hypergraphs (open for r≥6; proven r≤3 via Aharoni 2001) and the Erdos matching conjecture (max edges of a k-uniform hypergraph with ν < s; open in general).

**Enumerate.** Exhaustive small hypergraphs: all r-partite r-uniform hypergraphs on small part sizes (r=3,4,5) up to isomorphism; k-uniform hypergraphs on n≤8 vertices for the matching conjecture. Sanity-check set-system counts against direct enumeration.

**Conjecture generation.** Test Ryser and Erdos-matching on generated instances plus auto-fit τ-vs-ν and edge-count-vs-ν bounds. Include the τ/ν ratio, whose extremal cases (truncated projective planes) are the known Ryser-tight examples.

**Adversarial families.** Truncated projective planes and affine planes (the classical Ryser-extremal r-partite hypergraphs), sunflower families, complete r-partite hypergraphs, and random r-partite hypergraphs at the τ=(r−1)ν boundary.

**Checker (exact).** Compute τ and ν exactly by ILP (set cover / set packing) with certificates: a cover and a matching plus LP-duality bounds proving optimality. Verify r-partiteness and uniformity. Emit violators as explicit edge lists.

**Verification discipline.** Generator is not verifier: recompute τ, ν with a second exact solver; verify each cover covers all edges and each matching is disjoint. Cite Ryser/Erdos and note which r,k are already settled. Report candidates generated / broken / survived, with explicit hypergraph witnesses.
