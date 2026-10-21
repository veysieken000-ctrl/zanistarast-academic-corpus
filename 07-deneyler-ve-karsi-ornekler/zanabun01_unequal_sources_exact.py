#!/usr/bin/env python3
"""ZANABUN-01 v1.2. Exact constructed-data covariance audit; no human data."""
from fractions import Fraction as F
G, T, S = F(1,4), F(4), F(1)

def component(sizes, biases):
    n=sum(sizes)
    p=[F(x,n) for x in sizes]
    bias=sum((x*F(b) for x,b in zip(p,biases)), F(0))
    variance=G+T*sum((x*x for x in p),F(0))+S/n
    return bias,variance,variance+bias*bias

def covariance(sizes,biases):
    labels=[g for g,size in enumerate(sizes) for _ in range(size)]
    n=len(labels)
    bias=sum((F(biases[g]) for g in labels),F(0))/n
    total=F(0)
    for i,gi in enumerate(labels):
        for j,gj in enumerate(labels):
            total+=G+(T if gi==gj else 0)+(S if i==j else 0)
    var=total/(n*n)
    return bias,var,var+bias*bias

def main():
    cases=[
        ([8],[0],F(35,8),F(35,8)),
        ([4,4],[0,0],F(19,8),F(19,8)),
        ([7,1],[0,0],F(7,2),F(7,2)),
        ([2,2,2,2],[0,0,0,0],F(11,8),F(11,8)),
        ([7,1],[0,10],F(7,2),F(81,16))]
    print("groups,bias,variance,mse,effective_sources")
    for sizes,biases,expected_var,expected_mse in cases:
        a,b=component(sizes,biases),covariance(sizes,biases)
        assert a==b and a[1:]==(expected_var,expected_mse),(sizes,a,b)
        effective=F(sum(sizes)**2,sum(x*x for x in sizes))
        print(sizes,a[0],a[1],a[2],effective,sep=",")
    assert component([7,1],[0,10])[2]>component([8],[0])[2]
    assert component([7,1],[0,0])[1]>component([4,4],[0,0])[1]
    va,vb=T+S/7,T+S
    wa,wb=vb/(va+vb),va/(va+vb)
    assert (wa,wb)==(F(35,64),F(29,64))
    assert G+wa*wa*va+wb*wb*vb==F(161,64)
    print("PASS: exact identities, covariance cross-check, counterexamples")

if __name__=="__main__":
    main()
