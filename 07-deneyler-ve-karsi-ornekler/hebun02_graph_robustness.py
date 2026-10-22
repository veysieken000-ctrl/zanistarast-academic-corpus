#!/usr/bin/env python3
"""Exact enumeration of all simple undirected labeled graphs on 4 vertices.
A synthetic robustness audit of HEBUN-02; not a frequency estimate of nature.
Python 3.8+ standard library only.
"""
from itertools import combinations

V = tuple(range(4))
POSSIBLE = tuple(combinations(V, 2))

def graph(mask):
    return tuple(edge for i, edge in enumerate(POSSIBLE) if mask & (1 << i))

def connected(edges):
    reached = {0}
    while True:
        updated = reached | {v for u, v in edges if u in reached} | {u for u, v in edges if v in reached}
        if updated == reached:
            return len(reached) == len(V)
        reached = updated

def degree_winners(edges):
    degree = {v: sum(v in e for e in edges) for v in V}
    m = max(degree.values())
    return frozenset(v for v in V if degree[v] == m)

def main():
    counts = {1: 0, 2: 0, 3: 0, 4: 0}
    connected_total = 0
    for mask in range(1 << len(POSSIBLE)):
        edges = graph(mask)
        if not connected(edges):
            continue
        connected_total += 1
        counts[len(degree_winners(edges))] += 1
    assert len(POSSIBLE) == 6
    assert connected_total == 38, connected_total
    assert sum(counts.values()) == connected_total
    cycle = ((0,1),(1,2),(2,3),(3,0))
    star = ((0,1),(0,2),(0,3))
    path = ((0,1),(1,2),(2,3))
    complete = POSSIBLE
    assert degree_winners(cycle) == frozenset(V)
    assert degree_winners(star) == frozenset({0})
    assert degree_winners(path) == frozenset({1,2})
    assert degree_winners(complete) == frozenset(V)
    assert counts[1] > 0 and sum(counts[k] for k in (2,3,4)) > 0
    print('PASS exhaustive n=4: 64 labeled simple undirected graphs; 38 connected')
    print('Degree-centrality maximizer multiplicities:', counts)
    print('PASS C4=4, star=1, path=2, K4=4 maximizers')
    print('LIMIT: combinatorial synthetic audit; no inference to real-network frequency')

if __name__ == '__main__':
    main()
