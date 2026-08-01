#!/usr/bin/env python3
"""Export the explicit 112-cap in F_3^6 used as the Calderbank-Fishburn layer."""
from __future__ import annotations
import csv,json
from itertools import product
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
D={(0,1,2),(1,2,5),(0,1,3),(1,3,4),(0,2,4),(1,4,5),(0,3,5),(2,3,4),(0,4,5),(2,3,5)}
def build():
 out=[]
 for v in product(range(3),repeat=6):
  s=tuple(i for i,x in enumerate(v) if x)
  if (len(s)==3 and s in D) or (len(s)==6 and sum(x==2 for x in v)%2==0):out.append(v)
 assert len(out)==112
 return sorted(out)
def main():
 A=build();base=ROOT/'a112'
 (base.with_suffix('.json')).write_text(json.dumps(A,separators=(',',':'))+'\n')
 with base.with_suffix('.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow([f'x{i}' for i in range(6)]);w.writerows(A)
 (base.with_suffix('.txt')).write_text('\n'.join(''.join(map(str,p)) for p in A)+'\n')
 print('generated 112 points')
 for s in ['json','csv','txt']:print(base.with_suffix('.'+s))
if __name__=='__main__':main()
