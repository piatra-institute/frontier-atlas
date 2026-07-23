#!/usr/bin/env python3
"""Pure-standard-library exact verifier for saturation certificates of the 604-code.

It checks five Q(sqrt(2)) Handelman identities covering every strict chamber of
six central hyperplanes in the last three coordinates, modulo exact symmetries.
Together these identities prove that every point in the polar of the antipodal
604-code has squared norm at most 3. A direct exact witness has squared norm 3.
Thus the fixed 604-code is saturated with a strict margin: a kissing vector in
the norm-2 convention would require squared norm 4 and cannot be adjoined.

This is NOT a universal upper bound for the 11-dimensional kissing number.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
from math import gcd, lcm
import hashlib, json, platform, time

N=11
Q=tuple[F,F]  # a+b*sqrt(2)
Exp=tuple[int,...]
Poly=dict[Exp,Q]
Q0=(F(0),F(0));Q1=(F(1),F(0));ZERO=(0,)*N
PAIRS=[(0,6),(1,4),(2,5),(3,7)]
FF=[
 [(1,2,3),(4,5,7),(0,2,7),(3,5,6),(0,3,4),(1,6,7),(0,1,5),(2,4,6)],
 [(1,2,7),(3,4,5),(0,5,7),(2,3,6),(0,1,3),(4,6,7),(0,2,4),(1,5,6)],
 [(1,3,5),(2,4,7),(0,2,3),(5,6,7),(0,1,7),(3,4,6),(0,4,5),(1,2,6)],
]
H=set(sum(FF,[]))
U=[[F(2,3),F(1,3),F(2,3)],[F(2,3),F(-2,3),F(-1,3)],[F(1,3),F(2,3),F(-2,3)]]
UN=[(2,1,2),(2,-2,-1),(1,2,-2)]
CERTS={
 '----+-':('certificates/deg3_exact_certificate_mmmmpm.json',3),
 '-+---+':('certificates/deg4_exact_certificate_mpmmmp.json',4),
 '------':('certificates/deg3_exact_certificate_mmmmmm.json',3),
 '-+----':('certificates/deg3_exact_certificate_mpmmmm.json',3),
 '-----+':('certificates/deg3_exact_certificate_mmmmmp.json',3),
}

def qa(a=0,b=0):return (F(a),F(b))
def qadd(x:Q,y:Q)->Q:return (x[0]+y[0],x[1]+y[1])
def qmul(x:Q,y:Q)->Q:return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qscale(k,x:Q)->Q:return (F(k)*x[0],F(k)*x[1])
def qpositive(x:Q)->bool:
 a,b=x
 if b==0:return a>0
 if b>0:return a>=0 or 2*b*b>a*a
 return a>0 and a*a>2*b*b

def padd(P:Poly,Qp:Poly)->Poly:
 R=dict(P)
 for e,c in Qp.items():
  R[e]=qadd(R.get(e,Q0),c)
  if R[e]==Q0:del R[e]
 return R

def pscale(a:Q,P:Poly)->Poly:
 return {e:qmul(a,c) for e,c in P.items() if qmul(a,c)!=Q0}

def pmul(P:Poly,Qp:Poly)->Poly:
 R:Poly={}
 for e,a in P.items():
  for f,b in Qp.items():
   h=tuple(e[i]+f[i] for i in range(N));R[h]=qadd(R.get(h,Q0),qmul(a,b))
 return {e:c for e,c in R.items() if c!=Q0}

def affine(c:Q,a:tuple[Q,...])->Poly:
 P={ZERO:c} if c!=Q0 else {}
 for i,v in enumerate(a):
  if v!=Q0:
   e=[0]*N;e[i]=1;P[tuple(e)]=v
 return P

def make_generators(bits:str):
 assert len(bits)==6 and set(bits)<={'+','-'}
 sz=[1 if c=='+' else -1 for c in bits[:3]];sw=[1 if c=='+' else -1 for c in bits[3:]]
 gs=[];names=[]
 def add(c,a,name):
  key=(c,tuple(a));assert key not in gs
  gs.append(key);names.append(name)
 for i in range(8):
  a=[Q0]*N;a=a.copy();a[i]=qa(1);add(qa(),a,f'p{i}')
  a=[Q0]*N;a=a.copy();a[i]=qa(-1);add(qa(1),a,f'1-p{i}')
 for k in range(3):
  a=[Q0]*N;a=a.copy();a[8+k]=qa(sz[k]);add(qa(),a,f'sz{k}')
 for j in range(3):
  a=[Q0]*N;a=a.copy()
  for k in range(3):a[8+k]=qa(sw[j]*U[j][k])
  add(qa(),a,f'sw{j}')
 for r,s in combinations(range(4),2):
  a=[Q0]*N;a=a.copy()
  for i in PAIRS[r]+PAIRS[s]:a[i]=qa(-1)
  add(qa(2),a,f'pair{r}{s}')
 for k,fam in enumerate(FF):
  for ti,T in enumerate(fam):
   a=[Q0]*N;a=a.copy()
   for i in T:a[i]=qa(-1)
   a[8+k]=qa(-sz[k]);add(qa(2),a,f'L{k}.{ti}')
 for r,P in enumerate(PAIRS):
  for j in range(3):
   a=[Q0]*N;a=a.copy()
   for i in P:a[i]=qa(-1)
   for k in range(3):a[8+k]=(F(0),-F(sw[j])*U[j][k])
   add(qa(2),a,f'E1.{r}.{j}')
 for i,j in combinations(range(3),2):
  a=[Q0]*N;a=a.copy()
  for k in range(3):a[8+k]=qa(-(sw[i]*U[i][k]+sw[j]*U[j][k]))
  add(qa(0,1),a,f'E2.{i}.{j}')
 assert len(gs)==67 and len(set(gs))==67
 return gs,names

def transform_form(form,T):
 c,a=form;out=[Q0]*N
 for j in range(N):
  s=Q0
  for i in range(N):
   if T[i][j]:s=qadd(s,qscale(T[i][j],a[i]))
  out[j]=s
 return c,tuple(out)

def build_groups():
 PG=[]
 for sp in permutations(range(4)):
  for flips in product((0,1),repeat=4):
   g=[None]*8
   for r,(a,b) in enumerate(PAIRS):
    c,d=PAIRS[sp[r]]
    if flips[r]:c,d=d,c
    g[a]=c;g[b]=d
   gt=tuple(g)
   if {tuple(sorted(gt[i] for i in t)) for t in H}==H:PG.append(gt)
 ZG=[]
 for pp in permutations(range(3)):
  for ss in product((-1,1),repeat=3):
   R=[[0]*3 for _ in range(3)]
   for i in range(3):R[i][pp[i]]=ss[i]
   ok=True
   for row in UN:
    tr=[sum(row[k]*R[j][k] for k in range(3)) for j in range(3)]
    if not any(tr==list(u) or tr==[-x for x in u] for u in UN):ok=False;break
   if ok:ZG.append(tuple(tuple(r) for r in R))
 assert len(PG)==48 and len(set(PG))==48
 assert len(ZG)==12 and len(set(ZG))==12
 return PG,ZG

def block_transform(g,R):
 T=[[0]*N for _ in range(N)]
 for i in range(8):T[g[i]][i]=1
 for i in range(3):
  for j in range(3):T[8+i][8+j]=R[i][j]
 return T

def sign_bits(z):
 vals=[z[0],z[1],z[2]]+[sum(UN[j][k]*z[k] for k in range(3)) for j in range(3)]
 if 0 in vals:return None
 return ''.join('+' if v>0 else '-' for v in vals)

def rref_nullspace(cols):
 """Nullspace basis of a 3 x k rational matrix given by column vectors."""
 k=len(cols);A=[[F(cols[j][i]) for j in range(k)] for i in range(3)]
 piv=[];r=0
 for c in range(k):
  p=next((i for i in range(r,3) if A[i][c]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];v=A[r][c];A[r]=[x/v for x in A[r]]
  for i in range(3):
   if i!=r and A[i][c]:
    v=A[i][c];A[i]=[A[i][j]-v*A[r][j] for j in range(k)]
  piv.append(c);r+=1
  if r==3:break
 free=[c for c in range(k) if c not in piv];basis=[]
 for f in free:
  v=[F(0)]*k;v[f]=F(1)
  for ri,p in enumerate(piv):v[p]=-A[ri][f]
  basis.append(v)
 return basis

def dependence_certificate(signed_normals):
 for k in range(2,5):
  for idxs in combinations(range(6),k):
   basis=rref_nullspace([signed_normals[i] for i in idxs])
   candidates=[]
   if len(basis)==1:candidates=[basis[0],[-x for x in basis[0]]]
   elif basis:
    for cs in product(range(-4,5),repeat=len(basis)):
     if not any(cs):continue
     v=[sum(F(cs[j])*basis[j][i] for j in range(len(basis))) for i in range(k)]
     candidates.append(v)
   for v in candidates:
    if all(x>=0 for x in v) and any(x>0 for x in v):
     den=1
     for x in v:den=lcm(den,x.denominator)
     ints=[int(x*den) for x in v];gg=0
     for x in ints:gg=gcd(gg,abs(x))
     ints=[x//gg for x in ints]
     full=[0]*6
     for i,x in zip(idxs,ints):full[i]=x
     assert all(x>=0 for x in full) and any(full)
     assert all(sum(full[j]*signed_normals[j][r] for j in range(6))==0 for r in range(3))
     return full
 return None

def chamber_audit():
 witnesses={}
 for B in range(1,13):
  for z in product(range(-B,B+1),repeat=3):
   if z==(0,0,0):continue
   b=sign_bits(z)
   if b is not None and b not in witnesses:witnesses[b]=z
 allbits=[''.join(x) for x in product('+-',repeat=6)]
 infeasible={}
 normals=[(1,0,0),(0,1,0),(0,0,1)]+UN
 for bits in allbits:
  if bits in witnesses:continue
  sn=[tuple((1 if bits[i]=='+' else -1)*x for x in normals[i]) for i in range(6)]
  dep=dependence_certificate(sn)
  if dep is None:raise AssertionError(('unclassified chamber',bits))
  infeasible[bits]=dep
 assert len(witnesses)==32 and len(infeasible)==32
 # Exact check witnesses.
 for b,z in witnesses.items():assert sign_bits(z)==b
 return witnesses,infeasible

def verify_certificate(root,bits,filename,degree):
 cert=json.loads((root/filename).read_text())
 assert cert['schema']=='handelman-orbit-certificate-v1' and cert['bits']==bits and cert['degree']==degree
 forms,names=make_generators(bits);assert cert['generator_names']==names
 aff=[affine(c,a) for c,a in forms]
 total:Poly={};products=0;seen=set()
 assert len(cert['selected_orbits'])==len(cert['coefficients'])
 for orbit_raw,coef_raw in zip(cert['selected_orbits'],cert['coefficients']):
  orbit={tuple(int(i) for i in co) for co in orbit_raw}
  assert len(orbit)==len(orbit_raw) and orbit
  assert all(tuple(sorted(co))==co and 1<=len(co)<=degree and all(0<=i<67 for i in co) for co in orbit)
  assert seen.isdisjoint(orbit);seen.update(orbit)
  a=F(*coef_raw['a']);b=F(*coef_raw['b']);coef=(a,b);assert qpositive(coef)
  orbit_sum:Poly={}
  for co in orbit:
   P={ZERO:Q1}
   for i in co:P=pmul(P,aff[i])
   orbit_sum=padd(orbit_sum,P);products+=1
  total=padd(total,pscale(coef,orbit_sum))
 target={ZERO:qa(3)}
 for i in range(N):
  e=[0]*N;e[i]=2;target[tuple(e)]=qa(-1)
 assert total==target, (bits,len(total),len(target),next((e for e in set(total)|set(target) if total.get(e,Q0)!=target.get(e,Q0)),None))
 return {'degree':degree,'orbit_terms':len(cert['selected_orbits']),'expanded_products':products,'polynomial_terms_checked':len(set(total)|set(target))}

def direct_polar_witness(root):
 obj=json.loads((root/'construction_604.json').read_text());V=obj['vectors']
 # y=(1,1,1,0,...,0), represented after multiplying coordinates by 3.
 y=[(0,0)]*11;y=y.copy()
 for i in (0,1,2):y[i]=(3,0)
 def dot(v,w):
  a=b=0
  for (x1,x2),(y1,y2) in zip(v,w):a+=x1*y1+2*x2*y2;b+=x1*y2+x2*y1
  return a,b
 for v in V:
  d=dot([tuple(x) for x in v],y)
  # Both code and y are scaled by 3, so |original dot|<=2 is |scaled dot|<=18.
  assert d[1]==0 and abs(d[0])<=18
 return {'coordinates':[1,1,1,0,0,0,0,0,0,0,0],'squared_norm':3}

def main():
 t0=time.time();root=Path(__file__).resolve().parent
 reports={b:verify_certificate(root,b,*CERTS[b]) for b in CERTS}
 witnesses,infeasible=chamber_audit();PG,ZG=build_groups()
 allbits=[''.join(x) for x in product('+-',repeat=6)]
 formsets={b:frozenset(make_generators(b)[0]) for b in allbits};reverse={v:k for k,v in formsets.items()};assert len(reverse)==64
 # Find the exact global constraint-system symmetry group and its action on chambers.
 base='++++++';global_actions=[]
 for g in PG:
  for R in ZG:
   T=block_transform(g,R);S=frozenset(transform_form(f,T) for f in formsets[base])
   if S in reverse:
    action={}
    for b in allbits:
     Sb=frozenset(transform_form(f,T) for f in formsets[b]);assert Sb in reverse
     action[b]=reverse[Sb]
    global_actions.append((g,R,action))
 assert len(global_actions)==96
 feasible=set(witnesses);assert all(set(a[b] for b in feasible)==feasible for _,_,a in global_actions)
 # Compute feasible chamber orbits.
 unseen=set(feasible);orbits=[]
 while unseen:
  b=min(unseen);O={a[b] for _,_,a in global_actions};assert O<=feasible
  orbits.append(O);unseen-=O
 rep_orbits={next(r for r in CERTS if r in O):O for O in orbits if any(r in O for r in CERTS)}
 assert len(orbits)==len(rep_orbits)==5 and set().union(*rep_orbits.values())==feasible
 assert sorted(len(O) for O in orbits)==[2,6,6,6,12]
 # Every feasible chamber must map to one certified representative.
 mappings={}
 for b in sorted(feasible):
  found=None
  for g,R,a in global_actions:
   if a[b] in CERTS:found=(a[b],g,R);break
  assert found is not None;mappings[b]=found[0]
 witness=direct_polar_witness(root)
 report={
  'status':'PASS','python':platform.python_version(),'platform':platform.platform(),
  'construction_sha256':hashlib.sha256((root/'construction_604.json').read_bytes()).hexdigest(),
  'exact_arithmetic':'Q(sqrt(2)) using fractions; no floating point in mathematical checks',
  'hyperplane_sign_patterns':64,'strictly_feasible_chambers':32,'gordan_infeasibility_certificates':32,
  'global_constraint_symmetries':96,'feasible_chamber_orbits':5,
  'certified_representatives':{r:{**reports[r],'orbit_size':len(rep_orbits[r])} for r in CERTS},
  'all_feasible_chambers_mapped_to_certificate':True,
  'polar_squared_radius_upper_bound':3,'polar_squared_radius_witness':witness,
  'polar_squared_radius_exact':3,
  'conclusion':'No norm-2 vector can be adjoined to the fixed 604-point norm-2 code; the code is saturated.',
  'universal_kissing_upper_bound_proved':False,
  'elapsed_seconds':round(time.time()-t0,6),
 }
 (root/'verification_saturation_604.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 print(json.dumps(report,indent=2,sort_keys=True))
 return 0
if __name__=='__main__':raise SystemExit(main())
