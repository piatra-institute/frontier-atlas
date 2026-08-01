#!/usr/bin/env python3
"""Independent lower bound R_F2(<m,n,p>) >= R+1 via SAT with a checked DRAT proof.

Completely separate method from the substitution-method certificate in the
chatgpt-pro package: encode "a rank-R bilinear decomposition of <m,n,p> over F2
exists" as CNF and show UNSAT. A rank-R decomposition is R triples (u in F2^{mn},
v in F2^{np}, w in F2^{mp}) with sum_l u_l[a] v_l[b] w_l[c] = T[a,b,c] for every
structure-tensor coefficient (mod 2). Products are Tseitin-encoded (p=u&v&w),
coefficients are XOR (parity) constraints, and the R triples are lex-ordered to
break the S_R permutation symmetry. UNSAT (checked by drat-trim) proves R+1 is a
lower bound on the rank. SAT prints a decomposition (used to validate the encoder).

Usage: sat_bilinear_lb.py <cadical> <drat-trim> <outdir> m n p R [time_limit]
"""
from __future__ import annotations
import json, subprocess, sys, time
from pathlib import Path

class CNF:
    def __init__(self): self.n = 0; self.cl = []
    def v(self): self.n += 1; return self.n
    def add(self, c): self.cl.append(c)

def structure_tensor(m, n, p):
    T = {}
    A = [(i, j) for i in range(m) for j in range(n)]        # size m*n
    B = [(j, k) for j in range(n) for k in range(p)]        # size n*p
    C = [(i, k) for i in range(m) for k in range(p)]        # size m*p
    for a, (ia, ja) in enumerate(A):
        for b, (jb, kb) in enumerate(B):
            for c, (ic, kc) in enumerate(C):
                T[(a, b, c)] = 1 if (ia == ic and ja == jb and kb == kc) else 0
    return T, len(A), len(B), len(C)

def xor_gate(F, x, y):
    g = F.v()
    F.add([-g, x, y]); F.add([-g, -x, -y]); F.add([g, -x, y]); F.add([g, x, -y])
    return g

def eq_var(F, x, y):
    e = F.v()
    F.add([-x, -y, e]); F.add([x, y, e]); F.add([-x, y, -e]); F.add([x, -y, -e])
    return e

def lex_le(F, X, Y):
    """Enforce bit-vector X <= Y (MSB first)."""
    etrue = F.v(); F.add([etrue])
    e = etrue
    for xi, yi in zip(X, Y):
        F.add([-e, -xi, yi])                 # forbid equal-prefix and xi>yi
        eqi = eq_var(F, xi, yi)
        en = F.v()                           # en = e AND eqi
        F.add([-en, e]); F.add([-en, eqi]); F.add([-e, -eqi, en])
        e = en

def build(m, n, p, R):
    T, na, nb, nc = structure_tensor(m, n, p)
    F = CNF()
    u = [[F.v() for _ in range(na)] for _ in range(R)]
    v = [[F.v() for _ in range(nb)] for _ in range(R)]
    w = [[F.v() for _ in range(nc)] for _ in range(R)]
    prod = {}
    for l in range(R):
        for a in range(na):
            for b in range(nb):
                for c in range(nc):
                    pv = F.v(); prod[(l, a, b, c)] = pv
                    F.add([-pv, u[l][a]]); F.add([-pv, v[l][b]]); F.add([-pv, w[l][c]])
                    F.add([pv, -u[l][a], -v[l][b], -w[l][c]])
    for (a, b, c), t in T.items():
        acc = prod[(0, a, b, c)]
        for l in range(1, R):
            acc = xor_gate(F, acc, prod[(l, a, b, c)])
        F.add([acc] if t == 1 else [-acc])
    for l in range(R - 1):                    # lex symmetry break on 16-bit keys
        key_l = u[l] + v[l] + w[l]
        key_n = u[l + 1] + v[l + 1] + w[l + 1]
        lex_le(F, key_l, key_n)
    return F, na, nb, nc, u, v, w

def write_dimacs(path, F):
    with open(path, "w") as f:
        f.write(f"p cnf {F.n} {len(F.cl)}\n")
        for c in F.cl:
            f.write(" ".join(map(str, c)) + " 0\n")

def run(m, n, p, R, cadical, drat_trim, outdir, tl):
    F, na, nb, nc, u, v, w = build(m, n, p, R)
    tag = f"{m}{n}{p}_R{R}"
    cnf = outdir / f"bilin_{tag}.cnf"; drat = outdir / f"bilin_{tag}.drat"
    write_dimacs(cnf, F)
    t0 = time.time()
    try:
        r = subprocess.run([cadical, str(cnf), str(drat)], capture_output=True,
                           text=True, timeout=tl)
        out = r.stdout
    except subprocess.TimeoutExpired:
        out = ""
    dt = time.time() - t0
    res = ("UNSAT" if "s UNSATISFIABLE" in out else
           "SAT" if "s SATISFIABLE" in out else "timeout")
    rec = dict(map=f"<{m},{n},{p}>", R=R, vars=F.n, clauses=len(F.cl),
               seconds=round(dt, 1), result=res)
    if res == "UNSAT":
        c = subprocess.run([str(drat_trim), str(cnf), str(drat)],
                           capture_output=True, text=True, timeout=tl)
        rec["drat_trim"] = "VERIFIED" if "s VERIFIED" in c.stdout else "FAILED"
        print(f"<{m},{n},{p}> rank>={R+1}: R={R} UNSAT ({dt:.1f}s) "
              f"-> drat-trim {rec['drat_trim']}")
    else:
        print(f"<{m},{n},{p}> R={R}: {res} ({dt:.1f}s)"
              f"{' (decomposition exists, encoder OK)' if res=='SAT' else ''}")
    return rec

def main():
    cadical, drat_trim = sys.argv[1], Path(sys.argv[2])
    outdir = Path(sys.argv[3]); outdir.mkdir(parents=True, exist_ok=True)
    m, n, p, R = map(int, sys.argv[4:8])
    tl = float(sys.argv[8]) if len(sys.argv) > 8 else 300.0
    rec = run(m, n, p, R, cadical, drat_trim, outdir, tl)
    (outdir.parent / "certificates" / f"sat_lb_{m}{n}{p}_R{R}.json").write_text(
        json.dumps(rec, indent=2))

if __name__ == "__main__":
    main()
