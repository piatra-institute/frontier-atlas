#!/usr/bin/env python3
"""Exact bounded-sum checker for prime powers p^k, k>=2, repetitions allowed."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import sympy as sp

def prime_powers(n:int)->list[int]:
    vals=set()
    for p in list(sp.primerange(2,int(math.isqrt(n))+1)):
        x=p*p
        while x<=n:
            vals.add(x); x*=p
    return sorted(vals)
def representation(n:int,max_terms=5):
    vals=prime_powers(n); memo={}
    def dfs(rem,start,terms):
        key=(rem,start,terms)
        if key in memo:return memo[key]
        if terms==0:return [] if rem==0 else None
        for i in range(start,len(vals)):
            x=vals[i]
            if x>rem:break
            ans=dfs(rem-x,i,terms-1)
            if ans is not None: memo[key]=[x]+ans; return memo[key]
        memo[key]=None; return None
    for m in range(2,max_terms+1):
        ans=dfs(n,0,m)
        if ans is not None:return ans
    return None
def check(payload):
    n=int(payload['n']); ans=representation(n,5)
    return {"n":n,"in_domain":n>23,"representation":ans,"terms":None if ans is None else len(ans),
            "counterexample":bool(n>23 and ans is None)}
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('payload',type=Path); a=ap.parse_args()
    print(json.dumps(check(json.loads(a.payload.read_text())),indent=2,sort_keys=True))
