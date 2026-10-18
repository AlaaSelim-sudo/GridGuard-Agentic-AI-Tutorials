"""Regression checks for the physical and policy boundaries used in the lessons."""
from .framework import *
def main():
 v,r1,r2=SCENARIOS[0],SCENARIOS[2],SCENARIOS[3]
 assert not evaluate(v,'PV_100')['verified']
 assert evaluate(v,'PV_30')['verified']
 assert 'thermal' in evaluate(v,'PV_40')['failure_reasons']
 assert not evaluate(r1,'hold')['verified']
 assert evaluate(r1,'short_all')['verified']
 assert 'fault_quarantine' in evaluate(r1,'reclose_fault')['failure_reasons']
 assert 'mv_radiality' in evaluate(r1,'both_ties')['failure_reasons']
 assert 'thermal' in evaluate(r2,'short_all')['failure_reasons']
 assert evaluate(r2,'short_shed_75')['verified']
 assert not evaluate(r2,'long_all')['simulated']
 assert not evaluate(v,'unknown')['simulated']
 assert 'stale_telemetry' in evaluate(r1,'short_all',{'age_s':120})['failure_reasons']
 assert evaluate(r1,'short_all',{'reported_vmax':1.035})['verified']
 a=evaluate(v,'PV_30');evaluate(r2,'short_shed_90');b=evaluate(v,'PV_30')
 assert abs(a['score']-b['score'])<1e-7, 'A preceding candidate contaminated the reset model'
 assert a['metrics']['topology_hash']==b['metrics']['topology_hash']
 print('15 regression assertions passed: constraints, rejection, residual limit and reset independence.')
if __name__=='__main__':main()
