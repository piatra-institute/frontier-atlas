#!/usr/bin/env python3
"""Exact standard-diagram consequence for a hypothetical 289-cap in AG(7,3).

Premise: a(6) <= 112. For every hyperplane direction, sort the three slice
sizes as (a,b,c). Exact first-three-moment double counting and the separating
line below imply that at least one direction has one of four exceptional
profiles. This is the arithmetic part of Thackeray's published 288 upper
bound; it does not reproduce the structural elimination of those profiles.
"""
from __future__ import annotations
import json
from math import comb
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CERT=ROOT/'certificates'/'standard_diagram_289.json'
M=289; HMAX=112
DIRECTIONS=(3**7-1)//2
PAIR_MULT=(3**6-1)//2
TRIPLE_MULT=(3**5-1)//2
EXCEPTIONAL={(112,112,65),(112,111,66),(112,110,67),(111,111,67)}

def P(t): return sum(comb(x,2) for x in t)
def Q(t): return sum(comb(x,3) for x in t)
def slack(t): return 86*Q(t)-7793*P(t)+70_101_168

def main():
    types=[]
    for a in range(HMAX+1):
        for b in range(a+1):
            c=M-a-b
            if 0<=c<=b: types.append((a,b,c))
    assert len(types)==208
    rows=[{'type':list(t),'P':P(t),'Q':Q(t),'slack':slack(t)} for t in types]
    neg={t:slack(t) for t in types if slack(t)<0}
    zero={t for t in types if slack(t)==0}
    assert set(neg)==EXCEPTIONAL
    assert zero=={(97,96,96),(111,110,68)}
    assert all(slack(t)>=0 for t in types if t not in EXCEPTIONAL)

    total_P=PAIR_MULT*comb(M,2)
    total_Q=TRIPLE_MULT*comb(M,3)
    total_slack=86*total_Q-7793*total_P+DIRECTIONS*70_101_168
    assert total_P==15_148_224
    assert total_Q==481_732_944
    assert total_slack==-499_824

    cert={
      'claim':'Every hypothetical 289-cap has a hyperplane direction with one of four listed profiles.',
      'premise':'a(6) <= 112',
      'parameters':{'n':7,'hypothetical_cap_size':M,'hyperplane_cap_max':HMAX,
                    'directions':DIRECTIONS,'pair_multiplicity':PAIR_MULT,
                    'triple_multiplicity':TRIPLE_MULT},
      'slack_formula':'86*Q-7793*P+70101168',
      'moment_totals':{'sum_P':total_P,'sum_Q':total_Q,'sum_slack':total_slack},
      'zero_slack_types':[list(t) for t in sorted(zero)],
      'negative_slack_types':[{'type':list(t),'slack':neg[t]} for t in sorted(neg,reverse=True)],
      'all_admissible_types':rows,
      'scope':'Arithmetic standard diagram only; no structural elimination of the exceptional profiles.'
    }
    CERT.parent.mkdir(parents=True,exist_ok=True)
    CERT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print('PASS: exact 289 standard-diagram check')
    print(f'admissible sorted slice types checked: {len(types)}')
    print(f'aggregate slack: {total_slack}')
    print('the only negative-slack types are:')
    for t in sorted(EXCEPTIONAL,reverse=True): print(t,slack(t))
    print('CONCLUSION (assuming a(6)<=112): every hypothetical 289-cap has at least one listed direction')
    print(CERT)

if __name__=='__main__': main()
