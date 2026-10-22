#!/usr/bin/env python3
"""HEBUN-02/A02 Ek C: exact graph audit, n=2..6; Python 3.8+, stdlib only."""
from collections import deque
from fractions import Fraction
from itertools import combinations, permutations

W = ((0,1),(0,3),(0,5),(1,2),(1,3),(1,4),(2,3),(2,4))

def graph(n, edges):
    a = [set() for _ in range(n)]
    for u,v in edges:
        a[u].add(v); a[v].add(u)
    return a

def bfs(a, s):
    n=len(a); d=[-1]*n; paths=[0]*n
    d[s]=0; paths[s]=1; q=deque([s])
    while q:
        u=q.popleft()
        for v in a[u]:
            if d[v]<0: d[v]=d[u]+1; q.append(v)
            if d[v]==d[u]+1: paths[v]+=paths[u]
    return d,paths

def scores(a):
    n=len(a); data=[bfs(a,s) for s in range(n)]
    if -1 in data[0][0]: return None
    deg=tuple(map(len,a))
    close=tuple(-sum(data[v][0]) for v in range(n))
    between=[Fraction(0) for _ in range(n)]
    for s,t in combinations(range(n),2):
        ds,ps=data[s]
        for v in range(n):
            if v not in (s,t) and ds[v]+data[v][0][t]==ds[t]:
                between[v]+=Fraction(ps[v]*data[v][1][t],ps[t])
    return deg,close,tuple(between)

def top(x):
    return frozenset(i for i,v in enumerate(x) if v==max(x))

def dfs_paths(a,s,t):
    todo=[(s,(s,))]; paths=[]
    while todo:
        u,path=todo.pop()
        if u==t: paths.append(path)
        else:
            for v in a[u]:
                if v not in path: todo.append((v,path+(v,)))
    shortest=min(map(len,paths))
    return [p for p in paths if len(p)==shortest]

def witness():
    a=graph(6,W); d,c,b=scores(a)
    assert d==(3,4,3,3,2,1)
    assert c==(-7,-6,-8,-7,-9,-11)
    assert b==(Fraction(4),Fraction(7,2),Fraction(1,2),Fraction(1),Fraction(0),Fraction(0))
    assert tuple(map(top,(d,c,b)))==(frozenset({1}),frozenset({1}),frozenset({0}))
    check=[Fraction(0) for _ in range(6)]
    for s,t in combinations(range(6),2):
        paths=dfs_paths(a,s,t); dist,counts=bfs(a,s)
        assert len(paths)==counts[t] and len(paths[0])-1==dist[t]
        for v in range(6):
            if v not in (s,t):
                check[v]+=Fraction(sum(v in p[1:-1] for p in paths),len(paths))
    assert tuple(check)==b
    print('witness: degree/closeness winner=1; betweenness winner=0; DFS=PASS')

def audit(n):
    pairs=tuple(combinations(range(n),2)); total=unique=0; wrong=set()
    for mask in range(1<<len(pairs)):
        e=[pair for bit,pair in enumerate(pairs) if mask>>bit&1]
        val=scores(graph(n,e))
        if val is None: continue
        total+=1; tops=tuple(map(top,val))
        if all(len(t)==1 for t in tops):
            unique+=1
            if len({next(iter(t)) for t in tops})>1: wrong.add(mask)
    assert total=={2:1,3:4,4:38,5:728,6:26704}[n]
    assert len(wrong)==(720 if n==6 else 0)
    if n==6:
        bits={e:i for i,e in enumerate(pairs)}
        orbit=set()
        for p in permutations(range(n)):
            mask=0
            for u,v in W:
                mask|=1<<bits[tuple(sorted((p[u],p[v])))]
            orbit.add(mask)
        assert len(orbit)==720 and wrong==orbit
    print('n=%d connected=%d unique=%d unique-disagree=%d' %
          (n,total,unique,len(wrong)))

if __name__=='__main__':
    witness()
    for n in range(2,7): audit(n)
    print('PASS: exhaustive n<=6; one unlabeled disagreement class at n=6')
    print('LIMIT: formal synthetic graphs, not empirical or theological proof')
