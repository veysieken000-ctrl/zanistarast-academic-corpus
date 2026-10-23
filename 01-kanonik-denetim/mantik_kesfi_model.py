"""Mantık keşfi M1–M6 için yalnızca stdlib kullanan sınama modeli.

Bu program ontolojik, teolojik veya ampirik iddiaları kanıtlamaz.
Tür karışmalarını ve koşulsuz çıkarımları yakalamak için kullanılır.
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import FrozenSet, Optional


class NodeType(str, Enum):
    CREATED_YEK = "CREATED_YEK"
    KOMEL = "KOMEL"
    OBSERVER = "OBSERVER"
    CLAIM = "CLAIM"
    EVIDENCE = "EVIDENCE"


class EdgeType(str, Enum):
    DERIVES_FROM = "DERIVES_FROM"
    MEMBER_OF = "MEMBER_OF"
    VALIDATES = "VALIDATES"
    SUPPORTS = "SUPPORTS"
    REFUTES = "REFUTES"


@dataclass(frozen=True)
class Node:
    identifier: str
    kind: NodeType


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    kind: EdgeType


@dataclass
class TypedGraph:
    nodes: dict = field(default_factory=dict)
    edges: list = field(default_factory=list)

    def add_node(self, node: Node) -> None:
        if not node.identifier or node.identifier in self.nodes:
            raise ValueError("Boş veya yinelenen düğüm kimliği")
        self.nodes[node.identifier] = node

    def add_edge(self, edge: Edge) -> None:
        if edge.source not in self.nodes or edge.target not in self.nodes:
            raise ValueError("İlişki düğümleri kayıtlı olmalı")
        a = self.nodes[edge.source].kind
        b = self.nodes[edge.target].kind
        signatures = {
            EdgeType.DERIVES_FROM: (NodeType.CREATED_YEK, NodeType.CREATED_YEK),
            EdgeType.MEMBER_OF: (NodeType.CREATED_YEK, NodeType.KOMEL),
            EdgeType.VALIDATES: (NodeType.OBSERVER, NodeType.CLAIM),
            EdgeType.SUPPORTS: (NodeType.EVIDENCE, NodeType.CLAIM),
            EdgeType.REFUTES: (NodeType.EVIDENCE, NodeType.CLAIM),
        }
        if (a, b) != signatures[edge.kind]:
            raise TypeError(f"{edge.kind.value} için uygunsuz tür: {a.value} → {b.value}")
        if edge.kind == EdgeType.DERIVES_FROM and edge.source == edge.target:
            raise ValueError("Kendinden türeme bu taslakta yasak")
        if edge not in self.edges:
            self.edges.append(edge)

    def independent_validations(self, claim: str, provenance: dict) -> int:
        """Bağımsızlık garantisi değil: farklı kaynak soyağacı sayısı."""
        roots = set()
        for e in self.edges:
            if e.kind == EdgeType.VALIDATES and e.target == claim:
                if e.source not in provenance:
                    raise ValueError("Onaylayanın kaynak soyağacı belirtilmeli")
                roots.add(provenance[e.source])
        return len(roots)


def sufficient_condition_refuted(cases: list) -> bool:
    """(P => O) önermesi için P doğru ve O yanlış bir karşı örnek var mı?"""
    return any(p and not outcome for p, outcome in cases)


def candidate_center_roles(roles: dict, role: str) -> FrozenSet[str]:
    """Merkez tekil olmak zorunda değildir; boş küme de mümkündür."""
    return frozenset(roles.get(role, ()))


def distinct_yeks(ids: list) -> bool:
    """Yek kimliklerinin çiftler hâlinde ayrılığı; sıra ve ontoloji ispatı değildir."""
    return all(isinstance(x, str) and x.strip() for x in ids) and len(ids) == len(set(ids))
