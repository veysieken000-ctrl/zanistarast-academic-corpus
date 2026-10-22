#!/usr/bin/env python3
"""HEBUN-02: exact centrality-measure sensitivity for connected labeled n=4,5 graphs.
Python >=3.8, standard library only. Synthetic mathematics, not empirical network sampling.
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations


def graphs(n):
    edges = tuple(combinations(range(n), 2))
    for mask in range(1 << len(edges)):
        adj = [set() for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            if mask & (1 << i):
                adj[a].add(b)
                adj[b].add(a)
        yield tuple(frozenset(a) for a in adj)


def distances_and_paths(adj, start):
    n = len(adj)
    dist = [-1] * n
    sigma = [0] * n
    dist[start], sigma[start] = 0, 1
    q = deque([start])
    while q:
        u = q.popleft()
        for v in sorted(adj[u]):
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
            if dist[v] == dist[u] + 1:
                sigma[v] += sigma[u]
    return dist, sigma


def is_connected(adj):
    return all(d >= 0 for d in distances_and_paths(adj, 0)[0])


def shortest_paths_bruteforce(adj, s, t):
    """Independent exhaustive DFS of simple paths, n<=5."""
    stack = [(s, (s,))]
    paths = []
    while stack:
        u, path = stack.pop()
        if u == t:
            paths.append(path)
        else:
            for v in adj[u]:
                if v not in path:
                    stack.append((v, path + (v,)))
    min_length = min(len(p) for p in paths)
    return [p for p in paths if len(p) == min_length]


def scores(adj):
    n = len(adj)
    all_data = [distances_and_paths(adj, s) for s in range(n)]
    degree = tuple(len(adj[v]) for v in range(n))
    closeness = tuple(-sum(all_data[v][0]) for v in range(n))
    betweenness = [Fraction(0) for _ in range(n)]
    for s, t in combinations(range(n), 2):
        ds, ss = all_data[s]
        for v in range(n):
            if v in (s, t):
                continue
            dv, sv = all_data[v]
            if ds[v] + dv[t] == ds[t]:
                betweenness[v] += Fraction(ss[v] * sv[t], ss[t])
        # Independent enumeration checks both shortest-path counts and intermediaries.
        shortest = shortest_paths_bruteforce(adj, s, t)
        assert len(shortest) == ss[t]
        for v in range(n):
            if v not in (s, t):
                exact = Fraction(sum(v in p[1:-1] for p in shortest), len(shortest))
                formula = (Fraction(ss[v] * all_data[v][1][t], ss[t])
                           if ds[v] + all_data[v][0][t] == ds[t] else Fraction(0))
                assert exact == formula, (n, s, t, v)
    return degree, closeness, tuple(betweenness)


def winners(values):
    maximum = max(values)
    return frozenset(i for i, v in enumerate(values) if v == maximum)


def audit(n):
    hist = {name: Counter() for name in ('degree', 'closeness', 'betweenness')}
    signatures = Counter()
    unique_all = 0
    different_unique = 0
    pairwise_disagree = Counter()
    examples = {}
    connected = 0
    for adj in graphs(n):
        if not is_connected(adj):
            continue
        connected += 1
        names = ('degree', 'closeness', 'betweenness')
        win = dict(zip(names, map(winners, scores(adj))))
        for name in names:
            hist[name][len(win[name])] += 1
        signatures[tuple(len(win[name]) for name in names)] += 1
        if all(len(win[name]) == 1 for name in names):
            unique_all += 1
            if len({next(iter(win[name])) for name in names}) > 1:
                different_unique += 1
                examples.setdefault('unique_different', (adj, win))
        for a, b in combinations(names, 2):
            if win[a] != win[b]:
                pairwise_disagree[(a, b)] += 1
                examples.setdefault(a + '_vs_' + b, (adj, win))
    assert connected == {4: 38, 5: 728}[n]
    assert all(sum(h.values()) == connected for h in hist.values())
    print('n=', n, 'connected=', connected)
    for name in ('degree', 'closeness', 'betweenness'):
        print(name, dict(sorted(hist[name].items())))
    print('all-three-unique=', unique_all, 'unique-different=', different_unique)
    print('pairwise-disagreement=', dict(pairwise_disagree))
    print('signatures=', dict(sorted(signatures.items())))
    for name, (adj, win) in examples.items():
        edges = tuple((u,v) for u in range(n) for v in sorted(adj[u]) if u < v)
        print('example', name, 'edges=', edges, 'winners=', {k: sorted(v) for k,v in win.items()})
    return hist


if __name__ == '__main__':
    for n in (4, 5):
        audit(n)
    print('PASS: exact labeled enumeration; independent shortest-path checks for every connected graph')
    print('LIMIT: graph mathematics only; no observational, theological, or human-review validation')
