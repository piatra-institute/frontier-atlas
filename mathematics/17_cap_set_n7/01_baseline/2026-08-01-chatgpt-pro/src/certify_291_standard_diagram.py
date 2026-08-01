#!/usr/bin/env python3
"""Exact structural consequence for a hypothetical 291-cap in AG(7,3).

Assuming a(6)<=112, every such cap would have at least seven hyperplane
directions with sorted slices (112,112,67). This does not itself rule out 291.
"""
from __future__ import annotations
import json
from math import comb
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CERT=ROOT/'certificates'/'standard_diagram_291.json'
M=291; D=1093; PM=364; TM=121
P=lambda t:sum(comb(x,2) for x in t)
Q=lambda t:sum(comb(x,3) for x in t)
BASE=(97,97,97); OTHERZERO=(112,111,68); BAD=(112,112,67)
P0,Q0=P(BASE),Q(BASE)
def slack(t):return 631*(Q(t)-Q0)-57531*(P(t)-P0)
def main():
 types=[]
 for a in range(113):
  for b in range(a+1):
   c=M-a-b
   if 0<=c<=b:types.append((a,b,c))
 assert len(types)==192
 rows=[{'type':list(t),'P':P(t),'Q':Q(t),'slack':slack(t)} for t in types]
 neg=[t for t in types if slack(t)<0];zero=[t for t in types if slack(t)==0]
 assert neg==[BAD];assert zero==[BASE,OTHERZERO]
 assert slack(BAD)==-74250
 TP=PM*comb(M,2);TQ=TM*comb(M,3)
 total=631*(TQ-D*Q0)-57531*(TP-D*P0)
 assert TP==15_358_980 and TQ==491_838_985 and total==-505_661
 minimum=(-total+(-slack(BAD))-1)//(-slack(BAD));assert minimum==7
 cert={'claim':'Every hypothetical 291-cap has at least seven (112,112,67) hyperplane directions.',
       'premise':'a(6) <= 112','parameters':{'n':7,'hypothetical_cap_size':M,'directions':D,
       'pair_multiplicity':PM,'triple_multiplicity':TM},
       'slack_formula':'631*(Q-Q(97,97,97))-57531*(P-P(97,97,97))',
       'zero_slack_types':[list(BASE),list(OTHERZERO)],
       'only_negative_type':{'type':list(BAD),'slack':slack(BAD)},
       'moment_totals':{'sum_P':TP,'sum_Q':TQ,'sum_slack':total},
       'minimum_number_of_negative_directions':minimum,'all_admissible_types':rows,
       'scope':'Necessary structure only; not an upper bound below 291.'}
 CERT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
 print('PASS: exact 291 standard-diagram check')
 print('admissible sorted slice types checked:',len(types))
 print('aggregate slack:',total)
 print('only negative type:',BAD,slack(BAD))
 print('CONCLUSION: every hypothetical 291-cap has at least 7 directions of type (112,112,67)')
 print(CERT)
if __name__=='__main__':main()
