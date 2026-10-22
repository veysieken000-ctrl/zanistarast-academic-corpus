#!/usr/bin/env python3
"""HEBUN-02 v0.2: finite typed countermodels, not an empirical test.
Run: python3 07-deneyler-ve-karsi-ornekler/hebun02_typed_countermodels.py
Requires Python >=3.8, standard library only. No external data/randomness.
"""
DIMENSIONS = ('fizik', 'biyoloji', 'zihin', 'ruh', 'ahlak', 'hukum_ahiret')
STAGES = {
    'fizik': ('atom', 'yildiz_gezegen'),
    'biyoloji': ('tek_hucreli', 'cok_hucreli'),
    'zihin': ('zeka', 'akil'),
    'ruh': ('ruh', 'melekler'),
    'ahlak': ('fitri_ahlak', 'iradeli_ahlak'),
    'hukum_ahiret': ('hesap_hukum', 'hukmun_sonucu'),
}
HUMAN = ('fizik', 'biyoloji', 'zihin', 'ahlak', 'akil', 'duygu', 'oz')
PRINCIPLES = frozenset(('yek',))
COVERS = frozenset((('biyoloji', 'fizik'), ('zihin', 'biyoloji'),
                    ('ruh', 'zihin'), ('ahlak', 'ruh')))

def validate(stages, human, principles, covers):
    """Structural type checker; does not test metaphysical truth."""
    errors = []
    if set(stages) != set(DIMENSIONS):
        errors.append('dimension keys do not match Core 01')
    if any(len(v) != 2 for v in stages.values()):
        errors.append('stage arity is not two')
    if 'duygu' in stages:
        errors.append('human emotion miscast as cosmic dimension')
    if 'yek' in stages or 'yek' in DIMENSIONS:
        errors.append('Yek miscast as created cosmic dimension')
    if 'duygu' not in human or 'oz' not in human:
        errors.append('Core 13 human layers missing')
    if 'yek' not in principles:
        errors.append('Yek principle missing')
    if any(a not in DIMENSIONS or b not in DIMENSIONS for a,b in covers):
        errors.append('ill-typed cover relation')
    return errors

def closure(edges):
    result = set(edges)
    while True:
        nxt = result | {(a,c) for a,b in result for b2,c in result if b == b2}
        if nxt == result:
            return frozenset(result)
        result = nxt

def center_degrees(nodes, edges):
    return {v: sum(v in e for e in edges) for v in nodes}

def run():
    assert validate(STAGES, HUMAN, PRINCIPLES, COVERS) == []
    bad = dict(STAGES)
    bad['duygu'] = ('emotion1', 'emotion2')
    assert 'human emotion miscast as cosmic dimension' in validate(bad, HUMAN, PRINCIPLES, COVERS)
    bad2 = dict(STAGES)
    bad2['yek'] = ('a', 'b')
    assert 'Yek miscast as created cosmic dimension' in validate(bad2, HUMAN, PRINCIPLES, COVERS)
    transitive = closure(COVERS)
    assert ('ahlak', 'fizik') in transitive
    assert ('hukum_ahiret', 'fizik') not in transitive
    # Same ontology, distinct time assignments: chronology is not entailed.
    model1 = {'x': 1, 'y': 2}
    model2 = {'x': 3, 'y': 2}
    assert model1['x'] < model1['y']
    assert not model2['x'] < model2['y']
    ontology1 = (STAGES, COVERS, model1)
    ontology2 = (STAGES, COVERS, model2)
    assert ontology1[:2] == ontology2[:2]
    # Same cosmic premises, different human interpretations.
    human2 = ('h1', 'h2')
    cosmic_model1 = (STAGES, COVERS, HUMAN)
    cosmic_model2 = (STAGES, COVERS, human2)
    assert cosmic_model1[:2] == cosmic_model2[:2]
    assert cosmic_model1[2] != cosmic_model2[2]
    # C4: all four nodes tie under degree centrality.
    nodes = (0, 1, 2, 3)
    edges = ((0, 1), (1, 2), (2, 3), (3, 0))
    degrees = center_degrees(nodes, edges)
    assert degrees == {0: 2, 1: 2, 2: 2, 3: 2}
    assert len([v for v,d in degrees.items() if d == max(degrees.values())]) == 4
    # Counterexample fixture to universal three-particle atom claim: 1H.
    protium = {'protons': 1, 'neutrons': 0, 'electrons': 1}
    assert protium['neutrons'] == 0
    print('PASS: typed Core 01/Core 13 separation; transitive closure;')
    print('PASS: two non-entailment witnesses; C4 degree tie; hydrogen-1 fixture')
    print('LIMIT: logical/synthetic checks only; no empirical or peer validation')

if __name__ == '__main__':
    run()
