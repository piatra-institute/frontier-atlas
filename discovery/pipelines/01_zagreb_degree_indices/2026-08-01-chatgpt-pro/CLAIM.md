# Claim

**Claim.** No new result. B0 (engine calibration). The degree-index refutation pipeline
was validated by independently rediscovering KNOWN facts; it swept settled published
bounds, which can only reproduce.
1. **Known counterexample reproduced.** The Hansen-Vukicevic comparison `M1/n <= M2/m`
   fails on a 17-vertex bicyclic graph (graph6 `P]oCGGC@?G?_@?@??_?G?@??`). Independently
   verified here (Claude Code): my own networkx decode gives n=17, m=18, M1=172, M2=182,
   and the exact integer test `m*M1 - n*M2 = 2 > 0`, so `M1/n > M2/m`. But this graph and
   its infinite family are already published (Caporossi-Hansen-Vukicevic). A reconstruction,
   not a discovery.
2. **Known typo reproduced.** The literal forgotten-index formula `F <= 2M2 + m(n-2)` fails
   at the star K_{1,3} (`F=30 > 24`); the corrected `F <= 2M2 + m(n-2)^2` holds (`30 <= 30`).
   The missing square is a known Che-Chen correction.
3. **All 13 corrected/properly-stated literature bounds survived** the 273,192-graph census
   (matching A001349) and the adversarial family sweep. Nothing new fell.

**Checker.** Independent (Claude Code): networkx decode + exact integer `m*M1 - n*M2` on the
HV witness (2 > 0, confirmed); exact F/M2 on K_{1,3} (confirmed). The run's own package:
`verify_witnesses.py`, exact rational/integer arithmetic, two independent graph6 decoders,
enumeration counts vs A001349. Toolchain: Python 3.12 + networkx (verification).

**Trust base.** Exact integer/rational arithmetic, no floating point; two decoders; witnesses
self-certifying (small graphs). Census exhaustive only through n=9 (the smallest HV
counterexample is order 17, so lower orders exclude nothing new).

**Review level.** self + agent. ChatGPT Pro generated; Claude Code independently verified the
two witnesses. Not human-refereed.

**Provenance.** ChatGPT Pro, 2026-08-01. Verification: Claude Code (Opus), 2026-08-02.

**Cost and attempts.** 273,192 graphs enumerated (n<=9); 59 auto-fit candidates. No open-problem
result: the class (classical Zagreb/degree indices) is settled, so the sweep only reproduces.
Retained as a regression benchmark, not a live target (see `../PROMPT.md` SETTLED marker).
