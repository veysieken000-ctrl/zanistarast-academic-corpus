#!/usr/bin/env python3
"""ZANABUN-01 v1.4. Exact synthetic dual-bias covariance audit; no human data."""
from fractions import Fraction as F
from itertools import product

NA, NB = 7, 1
OMEGA, TAU, SIGMA = F(1,4), F(4), F(1)
VA, VB = TAU + SIGMA/NA, TAU + SIGMA/NB

def risk(t, bias_a, bias_b, cov):
    return (OMEGA + (1-t)**2*VA + t*t*VB + 2*cov*t*(1-t)
            + ((1-t)*bias_a + t*bias_b)**2)

def direct_risk(t, bias_a, bias_b, cov):
    weights = [(1-t)/NA]*NA + [t/NB]*NB
    group = [0]*NA + [1]*NB
    variance = sum((weights[i]*weights[j]*(OMEGA +
               (TAU if group[i]==group[j] else cov) +
               (SIGMA if i==j else F(0)))
               for i in range(NA+NB) for j in range(NA+NB)), F(0))
    bias = sum((weights[i]*(bias_a if group[i]==0 else bias_b)
                for i in range(NA+NB)), F(0))
    return variance + bias*bias

def worst_risk(t,a,b,c_lo,c_hi):
    return max(risk(t,x,y,c) for x,y,c in product((-a,a),(-b,b),(c_lo,c_hi)))

def optimum(a,b,c_hi):
    A,B,C = VA+a*a, VB+b*b, c_hi+a*b
    D = A+B-2*C
    if D < 0:
        raise ValueError("infeasible covariance")
    if D == 0:
        assert A==B==C
        return F(0)
    return max(F(0),min(F(1),(A-C)/D))

def main():
    print("ZANABUN-01 v1.4: EXACT SYNTHETIC MATHEMATICAL AUDIT")
    assert (VA,VB)==(F(29,7),F(5))
    cases=[("one_sided_v13",0,10,0,0),
           ("both_biased_independent",1,3,0,0),
           ("equal_bias_bounds",2,2,0,0),
           ("correlation_uncertain",1,3,0,4),
           ("correlation_high",0,10,0,4),
           ("both_biased_correlated",2,3,0,4),
           ("no_bias_but_correlated",0,0,0,4)]
    for name,aa,bb,cl,ch in cases:
        a,b,c_lo,c_hi=F(aa),F(bb),F(cl),F(ch)
        assert c_hi*c_hi<=VA*VB
        t=optimum(a,b,c_hi)
        result=worst_risk(t,a,b,c_lo,c_hi)
        assert result==risk(t,a,b,c_hi)==direct_risk(t,a,b,c_hi)
        assert result<=OMEGA+VA+a*a
        assert all(result<=worst_risk(F(i,1000),a,b,c_lo,c_hi)
                   for i in range(1001))
        for xa,xb,cc in product((-a,a),(-b,b),(c_lo,c_hi)):
            assert risk(t,xa,xb,cc)==direct_risk(t,xa,xb,cc)
        print(name,"weight",t,"worst_mse",result,"A_only",OMEGA+VA+a*a,
              "bias_blind",worst_risk(F(29,64),a,b,c_lo,c_hi))
    assert optimum(F(0),F(10),F(0))==F(29,764)
    assert optimum(F(2),F(2),F(0))==F(29,64)
    assert optimum(F(1),F(3),F(0))==F(15,92)
    assert optimum(F(1),F(3),F(4))==0
    assert optimum(F(0),F(10),F(4))==F(1,708)
    theta,a,b,shift=F(0),F(2),F(3),F(7)
    assert (theta+a,theta+b)==(theta+shift+a-shift,theta+shift+b-shift)
    print("PASS: seven scenarios, exact 8x8 covariance, endpoint grid, identifiability")

if __name__=="__main__":
    main()
