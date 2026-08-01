# Batch sweep: refute list/total/distinguishing coloring conjectures

**Mode:** one ChatGPT Pro session, code sandbox, batch throughput.
**Goal:** an explicit graph violating a stated coloring-variant conjecture, or hardened survivors. Refutation is the clean win. Precedent exists: the list-square-coloring conjecture (Kostochka-Woodall) was disproved by computer-aided construction (Kim-Park, 2015).

**Family + panel.** Connected graphs; list chromatic (choosability) ch, total chromatic χ'', edge chromatic χ', adjacent-vertex-distinguishing chromatic, game chromatic, and Grundy (greedy) chromatic. Track Δ, and χ, χ' for comparison.

**Enumerate.** nauty `geng`, connected graphs to n=9 (A001349: 1,1,2,6,21,112,853,11117,261080); bipartite and planar subfamilies separately (many variant conjectures are class-restricted).

**Conjecture generation.** Anchor on named statements: the Total Coloring Conjecture χ''≤Δ+2 (Behzad-Vizing; open, verified small); choosability = chromatic gaps; the adjacent-vertex-distinguishing conjectures (Zhang et al.); and the general pattern that list versions can strictly exceed their non-list counterparts. Auto-fit variant-vs-Δ bounds on n≤7.

**Adversarial families.** Complete bipartite K_{k,k} and its blow-ups (the classic choosability-gap source), Cartesian products of paths/cycles (grids, tori), line graphs, and near-regular graphs at the Δ boundary.

**Checker (exact).** For choosability, verify non-k-choosability by an exact search over a specific bad list assignment (a certificate is a list assignment admitting no proper colouring, checked by SAT-UNSAT); for total/AVD, verify a proper colouring exists and the lower bound holds by exact search. Emit violators in graph6 plus the certificate.

**Verification discipline.** Generator is not verifier: re-verify each colouring and each non-colourability certificate with a second independent solver. Cite each conjecture and note which are proven vs open. Report candidates generated / broken / survived, graph6 witnesses with list assignments.
