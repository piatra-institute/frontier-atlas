from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
import networkx as nx, numpy as np
from numba import njit

PAIRS=[(1,97),(1,100),(1,159),(1,160),(1,179),(1,180),(1,198),(1,211),(1,212),(1,215),(1,233),(1,269),(6,91),(7,85),(26,85),(32,91),(37,46),(88,97),(91,98),(91,100)]
G=nx.Graph()
for line in (ROOT / 'data' / '510.edge').read_text().splitlines():
 p=line.split()
 if not p: continue
 if p[0]=='p': N=int(p[2]); G.add_nodes_from(range(N))
 elif p[0]=='e': G.add_edge(int(p[1])-1,int(p[2])-1)
base_dict=nx.coloring.greedy_color(G,strategy='DSATUR')
base=np.array([base_dict[i] for i in range(N)],np.int32)

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

def csr(H):
    ip=[0]; ix=[]
    for x in range(H.number_of_nodes()):
        ix.extend(H.neighbors(x));ip.append(len(ix))
    return np.array(ip,np.int32),np.array(ix,np.int32)

def contract_pair(a,b):
    if a>b:a,b=b,a
    roots=[i for i in range(N) if i!=b]
    mp={old:i for i,old in enumerate(roots)}
    def f(x): return mp[a] if x==b else mp[x]
    H=nx.Graph(); H.add_nodes_from(range(N-1))
    for u,v in G.edges():
        x,y=f(u),f(v)
        if x==y: raise ValueError('adjacent pair')
        H.add_edge(x,y)
    old2new=np.array([f(i) for i in range(N)],np.int32)
    return H, roots, old2new

out=[]
for idx,(aa,bb) in enumerate(PAIRS):
    a,b=aa-1,bb-1
    H,roots,old2new=contract_pair(a,b)
    gd=nx.coloring.greedy_color(H,strategy='DSATUR')
    gc=np.array([gd[i] for i in range(N-1)],np.int32)
    if gc.max()<5:
        c=gc; print((aa,bb),'DSATUR')
    else:
        ip,ix=csr(H)
        # initialize from representative colors, perturb each restart
        init=np.array([base[roots[i]] for i in range(N-1)],np.int32)
        ok=False
        for r in range(50):
            rr=np.random.default_rng(2026072200+idx*100+r)
            st=init.copy()
            ids=rr.choice(len(st),min(len(st),20+3*r),replace=False)
            st[ids]=rr.integers(0,5,size=len(ids))
            found,c,it,best=tabu_search(ip,ix,st,5,250000,2026072300+idx*100+r)
            if found:
                print((aa,bb),'TABU',r,it,best); ok=True; break
        if not ok: raise RuntimeError(f'failed {(aa,bb)}')
    row=np.array([c[old2new[i]] for i in range(N)],np.uint8)
    assert row[a]==row[b]
    assert row.max()<5
    assert all(row[u]!=row[v] for u,v in G.edges())
    out.append(row)
np.save(ROOT / 'data' / '510_targeted_same_20.npy',np.array(out,np.uint8))
print('saved',len(out))
