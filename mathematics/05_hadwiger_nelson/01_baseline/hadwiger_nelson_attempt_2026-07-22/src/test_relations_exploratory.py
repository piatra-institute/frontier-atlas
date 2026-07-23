from __future__ import annotations
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
import networkx as nx, numpy as np, json, re, time
from numba import njit

G=nx.Graph()
for line in (ROOT / 'data' / '510.edge').read_text().splitlines():
 p=line.split()
 if not p:continue
 if p[0]=='p':N=int(p[2]);G.add_nodes_from(range(N))
 elif p[0]=='e':G.add_edge(int(p[1])-1,int(p[2])-1)
K=5
d=nx.coloring.greedy_color(G,strategy='DSATUR')
base=np.array([d[i] for i in range(N)],dtype=np.int32)
assert base.max()<K

@njit(cache=True)
def tabu_search(indptr, indices, init, k, max_iter, seed):
    np.random.seed(seed)
    n=len(init); colors=init.copy(); ncc=np.zeros((n,k),np.int32)
    for v in range(n):
        for p in range(indptr[v],indptr[v+1]): ncc[v,colors[indices[p]]] += 1
    conflicts=0
    for v in range(n): conflicts += ncc[v,colors[v]]
    conflicts//=2; best=conflicts; tabu=np.zeros((n,k),np.int32)
    for it in range(1,max_iter+1):
        if conflicts==0: return True,colors,it,best
        bd=10**9; bv=-1; bc=-1; count=0
        for v in range(n):
            old=colors[v]
            if ncc[v,old]==0: continue
            oldc=ncc[v,old]
            for c in range(k):
                if c==old: continue
                delta=ncc[v,c]-oldc
                if tabu[v,c]>it and conflicts+delta>=best: continue
                if delta<bd:
                    bd=delta;bv=v;bc=c;count=1
                elif delta==bd:
                    count+=1
                    if np.random.randint(count)==0: bv=v;bc=c
        if bv<0: continue
        old=colors[bv]
        tabu[bv,old]=it+5+np.random.randint(10)+conflicts//10
        for p in range(indptr[bv],indptr[bv+1]):
            w=indices[p];ncc[w,old]-=1;ncc[w,bc]+=1
        colors[bv]=bc;conflicts+=bd
        if conflicts<best: best=conflicts
    return False,colors,max_iter,best

def build(pattern,u,v,w):
    # pattern 0 AAA, 1 AAB(u=v), 2 ABA(u=w), 3 ABB(v=w), 4 ABC
    classes=[{i} for i in range(N)]
    # union-find
    par=list(range(N))
    def find(x):
        while par[x]!=x:par[x]=par[par[x]];x=par[x]
        return x
    def union(a,b):
        a=find(a);b=find(b)
        if a!=b:par[b]=a
    if pattern==0: union(u,v);union(u,w)
    elif pattern==1:union(u,v)
    elif pattern==2:union(u,w)
    elif pattern==3:union(v,w)
    roots={find(i) for i in range(N)}; roots=sorted(roots); mp={r:j for j,r in enumerate(roots)}
    old2new=[mp[find(i)] for i in range(N)]
    H=nx.Graph();H.add_nodes_from(range(len(roots)))
    for a,b in G.edges():
        aa,bb=old2new[a],old2new[b]
        if aa==bb:return None,None,None # impossible due equality of adjacent
        H.add_edge(aa,bb)
    if pattern in (1,2,3):
        # inequality between merged pair and singleton
        if pattern==1:a,b=old2new[u],old2new[w]
        elif pattern==2:a,b=old2new[u],old2new[v]
        else:a,b=old2new[v],old2new[u]
        if a==b:return None,None,None
        H.add_edge(a,b)
    elif pattern==4:
        H.add_edge(old2new[u],old2new[v]);H.add_edge(old2new[u],old2new[w]);H.add_edge(old2new[v],old2new[w])
    # initial map from base, choose representative; may violate contractions/extra edges
    init=np.array([base[roots[i]] for i in range(len(roots))],dtype=np.int32)
    return H,old2new,init

def csr(H):
 ip=[0];ix=[]
 for x in range(H.number_of_nodes()):ix.extend(H.neighbors(x));ip.append(len(ix))
 return np.array(ip,np.int32),np.array(ix,np.int32)

def solve(pattern,u,v,w,idx,restarts=10,max_iter=100000):
 H,mapping,init=build(pattern,u,v,w)
 if H is None:return False,None,0,0
 gd=nx.coloring.greedy_color(H,strategy='DSATUR')
 gc=np.array([gd[i] for i in range(H.number_of_nodes())],dtype=np.int32)
 if gc.max()<K:
  return True,gc,0,0
 ip,ix=csr(H); best=999
 for r in range(restarts):
  st=init.copy()
  rr=np.random.default_rng(1234567+idx*100+r)
  if r or True:
   ids=rr.choice(len(st),min(len(st),10+3*r),replace=False);st[ids]=rr.integers(0,K,size=len(ids))
  ok,c,it,b=tabu_search(ip,ix,st,K,max_iter,7654321+idx*100+r)
  best=min(best,b)
  if ok:return True,c,it,b
 return False,None,restarts*max_iter,best

# parse examples first 1000
examples=[]
for line in (ROOT / 'notes' / 'triple_scan_sample_missing_patterns.txt').read_text().splitlines():
 m=re.match(r'(\d+) (\d+) (\d+) mask=(\d+)',line)
 if m:examples.append(tuple(map(int,m.groups())))
print('examples',len(examples),flush=True)
names=['AAA','AAB','ABA','ABB','ABC']
results=[];idx=0
for u,v,w,mask in examples[:500]:
 for p in range(5):
  if mask>>p&1:
   t=time.time();ok,c,it,b=solve(p,u-1,v-1,w-1,idx,restarts=8,max_iter=100000);dt=time.time()-t
   rec={'triple':[u,v,w],'pattern':names[p],'found':ok,'best':int(b),'iterations':int(it),'seconds':dt}
   print(rec,flush=True);results.append(rec);idx+=1
   if not ok:
    ROOT / 'notes' / 'relation_candidates.json'.write_text(json.dumps(results,indent=2))
    print('STOP candidate',rec,flush=True);raise SystemExit
ROOT / 'notes' / 'relation_candidates.json'.write_text(json.dumps(results,indent=2))
