#!/usr/bin/env python3
"""Pure-standard-library exact verifier for construction_604.json.

All arithmetic is in Z[sqrt(2)] after multiplying coordinates by 3.
No floating-point arithmetic is used in any mathematical check.
"""
from __future__ import annotations
import hashlib, json, platform, time
from collections import Counter
from itertools import combinations
from pathlib import Path

Pair = tuple[int,int]  # a+b*sqrt(2)

def qadd(x: Pair, y: Pair) -> Pair:
    return x[0]+y[0], x[1]+y[1]

def qmul(x: Pair, y: Pair) -> Pair:
    a,b=x; c,d=y
    return a*c+2*b*d, a*d+b*c

def qdot(v, w) -> Pair:
    a=b=0
    for (x,y),(u,z) in zip(v,w):
        a += x*u + 2*y*z
        b += x*z + y*u
    return a,b

def qle_int(q: Pair, c: int) -> bool:
    """Return exactly whether a+b*sqrt(2) <= c, with integers a,b,c."""
    a,b=q; d=c-a
    if b == 0:
        return d >= 0
    if b > 0:
        return d >= 0 and d*d >= 2*b*b
    # b < 0. If d>=0 the inequality is automatic; otherwise square after sign reversal.
    return d >= 0 or 2*b*b >= d*d

def qle(x: Pair, y: Pair) -> bool:
    return qle_int((x[0]-y[0],x[1]-y[1]),0)

def qneg(v):
    return tuple((-a,-b) for a,b in v)

def main() -> int:
    t0=time.time()
    root=Path(__file__).resolve().parent
    path=root/'construction_604.json'
    raw=path.read_bytes()
    obj=json.loads(raw)
    vectors=[tuple((int(a),int(b)) for a,b in v) for v in obj['vectors']]
    labels=obj['labels']

    digest=hashlib.sha256(raw).hexdigest()
    assert digest == (root/'construction_604.sha256').read_text().split()[0]
    assert obj['dimension']==11 and obj['cardinality']==604
    assert len(vectors)==604 and all(len(v)==11 for v in vectors)
    assert len(set(vectors))==604, 'repeated vectors'

    # Every scaled vector has norm^2=36, hence every original vector has norm^2=4.
    norms=[qdot(v,v) for v in vectors]
    assert set(norms)=={(36,0)}, Counter(norms)

    # Every pair has scaled dot product <=18, hence original dot product <=2;
    # after division by norm 2, the unit-vector inner product is <=1/2.
    hist=Counter(); max_dot=None; max_pair=None; contacts=0
    for i,j in combinations(range(604),2):
        d=qdot(vectors[i],vectors[j])
        hist[d]+=1
        assert qle_int(d,18), (i,j,labels[i],labels[j],d)
        if d==(18,0): contacts+=1
        if max_dot is None or not qle(d,max_dot):
            max_dot=d; max_pair=(i,j)
    assert max_dot==(18,0), (max_dot,max_pair)

    # The code is antipodal: 302 lines, each represented by v and -v.
    Vset=set(vectors)
    assert all(qneg(v) in Vset for v in vectors)
    assert len({min(v,qneg(v)) for v in vectors})==302

    # Exact frame operator S=sum_v v v^T in scaled coordinates.
    S=[[(0,0) for _ in range(11)] for __ in range(11)]
    for v in vectors:
        for i in range(11):
            for j in range(11):
                S[i][j]=qadd(S[i][j],qmul(v[i],v[j]))
    expected=[2016]*8+[1872]*3
    for i in range(11):
        for j in range(11):
            assert S[i][j] == ((expected[i],0) if i==j else (0,0)), (i,j,S[i][j])
    # S is positive definite, so the coordinate matrix has rank exactly 11.

    # Audit the 30 supports used in B.
    supports=[tuple(s) for s in obj['supports']]
    assert len(supports)==30 and len(set(supports))==30
    assert all(len(s)==4 and len(set(s))==4 for s in supports)
    assert max(len(set(a)&set(b)) for a,b in combinations(supports,2))<=2

    report={
        'status':'PASS',
        'python':platform.python_version(),
        'platform':platform.platform(),
        'sha256':digest,
        'dimension':11,
        'cardinality':604,
        'unordered_pairs_checked':604*603//2,
        'distinct_vectors':604,
        'scaled_squared_norm':[36,0],
        'original_squared_norm':4,
        'maximum_scaled_dot':[18,0],
        'maximum_original_dot':2,
        'maximum_unit_inner_product':'1/2',
        'contact_pairs':contacts,
        'antipodal_lines':302,
        'scaled_frame_diagonal':expected,
        'original_frame_diagonal':[x//9 for x in expected],
        'rank':11,
        'elapsed_seconds':round(time.time()-t0,6),
        'inner_product_histogram':{f'{a}{b:+d}*sqrt(2)':n for (a,b),n in sorted(hist.items())},
    }
    out=root/'verification_604.json'
    out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='inner_product_histogram'},indent=2))
    print(f'Wrote {out}')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
