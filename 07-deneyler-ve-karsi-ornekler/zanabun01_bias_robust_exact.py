#!/usr/bin/env python3
"""ZANABUN-01 v1.3: exact constructed-data audit; no observations."""
from fractions import Fraction as F
G,T,S=F(1,4),F(4),F(1)
NA,NB=7,1
VA,VB=T+S/NA,T+S/NB
def risk(t,b,c=F(0)):
    return G+VA*(1-t)**2+VB*t*t+2*c*t*(1-t)+(t*b)**2
def direct(t,b,c=F(0)):
    group=[0]*NA+[1]*NB
    w=[(1-t)/NA]*NA+[t/NB]*NB
    variance=sum((w[i]*w[j]*(G+(T if group[i]==group[j] else c)+(S if i==j else F(0))) for i in range(NA+NB) for j in range(NA+NB)),F(0))
    return variance+(t*b)**2
def main():
    cases=[(0,F(29,64),F(161,64)),(1,F(29,71),F(767,284)),(2,F(29,92),F(71,23)),(5,F(29,239),F(3719,956)),(10,F(29,764),F(809,191)),(20,F(29,2864),F(12461,2864))]
    assert (VA,VB,G+VA)==(F(29,7),F(5),F(123,28))
    for d,wt,mse in cases:
        t=VA/(VA+VB+F(d*d))
        assert t==wt and risk(t,F(d))==mse==direct(t,F(d))==direct(t,F(-d))
        assert mse<=G+VA
        assert all(mse<=risk(F(k,1000),F(d)) for k in range(1001))
        print(d,t,mse,risk(F(29,64),F(d)))
    c=T
    t=(VA-c)/(VA+VB-2*c)
    assert t==F(1,8) and risk(t,F(0),c)==direct(t,F(0),c)==F(35,8)
    assert risk(F(29,64),F(0),c)==direct(F(29,64),F(0),c)==F(2303,512)
    print("PASS: exact bias-robust identities and correlated-source counterexample")
if __name__=="__main__":
    main()
