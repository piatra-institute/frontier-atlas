#!/usr/bin/env python3
"""Independent exact verifier for the degree-3 Handelman certificate.

The certificate proves, for p in R^8 satisfying the 46 listed nonnegative
linear forms, that sum_i p_i^2 <= 3. It uses only fractions and integer
permutations; no floating-point arithmetic or external packages.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json, platform, time

N=8
Exp=tuple[int,...]
Poly=dict[Exp,F]
ZERO=(0,)*N
PAIRS=[(0,6),(1,4),(2,5),(3,7)]
FAMILIES=[
 [(1,2,3),(4,5,7),(0,2,7),(3,5,6),(0,3,4),(1,6,7),(0,1,5),(2,4,6)],
 [(1,2,7),(3,4,5),(0,5,7),(2,3,6),(0,1,3),(4,6,7),(0,2,4),(1,5,6)],
 [(1,3,5),(2,4,7),(0,2,3),(5,6,7),(0,1,7),(3,4,6),(0,4,5),(1,2,6)],
]
H={tuple(sorted(t)) for fam in FAMILIES for t in fam}

def padd(P:Poly,Q:Poly)->Poly:
    R=dict(P)
    for e,c in Q.items():
        R[e]=R.get(e,F(0))+c
        if not R[e]: del R[e]
    return R

def pscale(a:F,P:Poly)->Poly:
    return {e:a*c for e,c in P.items() if a*c}

def pmul(P:Poly,Q:Poly)->Poly:
    R:Poly={}
    for e,a in P.items():
        for f,b in Q.items():
            h=tuple(e[i]+f[i] for i in range(N))
            R[h]=R.get(h,F(0))+a*b
    return {e:c for e,c in R.items() if c}

def affine(c:int, coeff:list[int])->Poly:
    P={ZERO:F(c)} if c else {}
    for i,a in enumerate(coeff):
        if a:
            e=[0]*N;e[i]=1;P[tuple(e)]=F(a)
    return P

def build_constraints():
    cons=[]; names=[]; keys=[]
    def add(c,a,name,key):
        cons.append(affine(c,a)); names.append(name); keys.append(key)
    for i in range(8):
        a=[0]*8;a[i]=1;add(0,a,f'p{i}',('p',i))
        a=[0]*8;a[i]=-1;add(1,a,f'1-p{i}',('u',i))
    for r,s in combinations(range(4),2):
        S=tuple(sorted(PAIRS[r]+PAIRS[s]));a=[0]*8
        for i in S:a[i]=-1
        add(2,a,f'pair{r}{s}',('q',S))
    for t in sorted(H):
        a=[0]*8
        for i in t:a[i]=-1
        add(2,a,'T'+''.join(map(str,t)),('t',t))
    assert len(cons)==46
    return cons,names,keys

def build_group():
    G=[]
    for spair in permutations(range(4)):
        for flips in product((0,1),repeat=4):
            g=[None]*8
            for r,(a,b) in enumerate(PAIRS):
                c,d=PAIRS[spair[r]]
                if flips[r]:c,d=d,c
                g[a]=c;g[b]=d
            gt=tuple(g)
            if {tuple(sorted(gt[i] for i in t)) for t in H}==H:
                G.append(gt)
    assert len(G)==48 and len(set(G))==48
    return G

def main()->int:
    t0=time.time(); root=Path(__file__).resolve().parent
    cert=json.loads((root/'p_only_handelman_certificate.json').read_text())
    cons,names,keys=build_constraints(); key_to_idx={k:i for i,k in enumerate(keys)}
    G=build_group()
    def map_constraint(i,g):
        kind,obj=keys[i]
        if kind in ('p','u'): k=(kind,g[obj])
        else:k=(kind,tuple(sorted(g[x] for x in obj)))
        return key_to_idx[k]
    actions=[tuple(map_constraint(i,g) for i in range(len(cons))) for g in G]
    assert cert['group_size']==len(G)==48
    assert cert['constraint_count']==len(cons)==46
    assert cert['degree']==3

    total:Poly={}
    orbit_products=0
    for item in cert['terms']:
        num,den=item['coefficient']; coefficient=F(num,den)
        assert coefficient>=0
        rep=tuple(item['representative_indices'])
        assert [names[i] for i in rep]==item['representative']
        orbit={tuple(sorted(act[i] for i in rep)) for act in actions}
        assert len(orbit)==item['orbit_size']
        orbit_sum:Poly={}
        for mon in orbit:
            P={ZERO:F(1)}
            for i in mon:P=pmul(P,cons[i])
            orbit_sum=padd(orbit_sum,P);orbit_products+=1
        total=padd(total,pscale(coefficient,orbit_sum))

    target={ZERO:F(3)}
    for i in range(8):
        e=[0]*8;e[i]=2;target[tuple(e)]=F(-1)
    assert total==target, sorted(set(total)|set(target))[:20]

    report={
      'status':'PASS',
      'python':platform.python_version(),
      'group_size':48,
      'constraints':46,
      'certificate_orbit_terms':len(cert['terms']),
      'expanded_nonnegative_products':orbit_products,
      'maximum_degree':3,
      'identity':'3-sum(p_i^2) = sum positive_coefficients * products(nonnegative_constraints)',
      'elapsed_seconds':round(time.time()-t0,6),
      'floating_point_used':False,
    }
    (root/'verification_p_slice.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(report,indent=2))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
