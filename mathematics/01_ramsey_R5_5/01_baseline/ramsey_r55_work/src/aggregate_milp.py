#!/usr/bin/env python3
"""Aggregate degree/neighborhood MILP relaxation for hypothetical R(5,5,n)."""
from math import comb
import json
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

# Exact extrema e(4,5,k), E(4,5,k) from Angeltveit--McKay, Appendix A.
EXT={
 17:(41,79),18:(50,85),19:(57,92),20:(68,100),
 21:(77,107),22:(88,114),23:(101,122),24:(116,132),
}

def solve(n,maximize=False):
    ds=list(range(n-1-24,25))
    D=len(ds)
    # x_d, A_d=sum edges in neighborhoods, C_d=sum complement-edges in antineighborhoods,
    # m, T, Tbar
    ix={d:i for i,d in enumerate(ds)}
    ia={d:D+i for i,d in enumerate(ds)}
    ic={d:2*D+i for i,d in enumerate(ds)}
    im=3*D; it=im+1; ib=im+2; nv=im+3
    c=np.zeros(nv); c[im]=-1 if maximize else 1
    lb=np.zeros(nv); ub=np.full(nv,np.inf)
    for d in ds: ub[ix[d]]=n
    ub[im]=comb(n,2); ub[it]=comb(n,3); ub[ib]=comb(n,3)
    rows=[]; lo=[]; hi=[]
    def add(coefs,l,h):
        r=np.zeros(nv)
        for j,v in coefs.items():r[j]=v
        rows.append(r);lo.append(l);hi.append(h)
    add({ix[d]:1 for d in ds},n,n)
    add({**{ix[d]:d for d in ds},im:-2},0,0)
    add({**{ia[d]:1 for d in ds},it:-3},0,0)
    add({**{ic[d]:1 for d in ds},ib:-3},0,0)
    # Goodman: T+Tbar = C(n,3)-1/2 sum d(n-1-d)x_d
    add({**{ix[d]:d*(n-1-d) for d in ds},it:2,ib:2},2*comb(n,3),2*comb(n,3))
    for d in ds:
        L,U=EXT[d]
        k=n-1-d; Lk,Uk=EXT[k]
        add({ia[d]:1,ix[d]:-L},0,np.inf)
        add({ia[d]:1,ix[d]:-U},-np.inf,0)
        add({ic[d]:1,ix[d]:-Lk},0,np.inf)
        add({ic[d]:1,ix[d]:-Uk},-np.inf,0)
    # For every edge uv, |N(u) intersect N(v)| <= 13 because it is an R(3,5)-graph.
    # Summing codegrees gives 3T; apply the same statement to the complement.
    add({it:3,im:-13},-np.inf,0)
    add({ib:3,im:13},-np.inf,13*comb(n,2))
    # Inclusion-exclusion lower bounds on edge codegrees, summed over all edges;
    # and the complementary analogue.
    add({it:3,im:n,**{ix[d]:-d*d for d in ds}},0,np.inf)
    add({ib:3,im:-n,**{ix[d]:-(n-1-d)**2 for d in ds}},-n*comb(n,2),np.inf)
    cons=LinearConstraint(np.array(rows),np.array(lo),np.array(hi))
    res=milp(c,integrality=np.ones(nv),bounds=Bounds(lb,ub),constraints=cons,
             options={'time_limit':30})
    if not res.success:return {'n':n,'success':False,'message':res.message}
    z=np.rint(res.x).astype(int)
    return {'n':n,'success':True,'objective':'max_edges' if maximize else 'min_edges',
            'm':int(z[im]),'T':int(z[it]),'Tbar':int(z[ib]),
            'degree_counts':{str(d):int(z[ix[d]]) for d in ds if z[ix[d]]},
            'message':res.message}

if __name__=='__main__':
 ans=[]
 for n in range(42,47):
  ans.extend([solve(n,False),solve(n,True)])
 print(json.dumps(ans,indent=2))
 open('../results/aggregate_milp_results.json','w').write(json.dumps(ans,indent=2)+'\n')
