"""Mantık keşfi M1–M6 için yalnızca stdlib kullanan sınama modeli.

Bu program ontolojik, teolojik veya ampirik iddiaları kanıtlamaz.
Tür karışmalarını ve koşulsuz çıkarımları yakalamak için kullanılır.
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import FrozenSet


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
        if edge.kind == EdgeType.DERIVES_FROM:
            # child -> parent; prevent circular ancestry.
            if self._reaches_ancestor(edge.target, edge.source):
                raise ValueError("Yek türeme grafında döngü oluşamaz")
        if edge not in self.edges:
            self.edges.append(edge)

    def _reaches_ancestor(self, start: str, goal: str) -> bool:
        stack = [start]
        visited = set()
        while stack:
            current = stack.pop()
            if current == goal:
                return True
            if current in visited:
                continue
            visited.add(current)
            stack.extend(
                edge.target for edge in self.edges
                if edge.kind == EdgeType.DERIVES_FROM and edge.source == current
            )
        return False

    def distinct_provenance_roots(self, claim: str, provenance: dict) -> int:
        """Farklı beyan edilen kaynak kökleri; bağımsızlık ispatı değildir."""
        if claim not in self.nodes or self.nodes[claim].kind != NodeType.CLAIM:
            raise ValueError("Hedef kayıtlı bir CLAIM olmalı")
        roots = set()
        for edge in self.edges:
            if edge.kind == EdgeType.VALIDATES and edge.target == claim:
                if edge.source not in provenance:
                    raise ValueError("Onaylayanın kaynak soyağacı belirtilmeli")
                root = provenance[edge.source]
                if not isinstance(root, str) or not root.strip():
                    raise ValueError("Kaynak kökü boş olamaz")
                roots.add(root)
        return len(roots)

    def independent_validations(self, claim: str, provenance: dict) -> int:
        """Geriye uyumlu eski ad; sonuç yalnız farklı kaynak kökü sayısıdır."""
        return self.distinct_provenance_roots(claim, provenance)



@dataclass(frozen=True)
class KomelCandidate:
    """İlişkisel bütün adayı; yeni bir Yek olduğunu kanıtlamaz."""
    members: FrozenSet[str]
    relations: FrozenSet[tuple]

    def __post_init__(self):
        if len(self.members) < 2:
            raise ValueError("Bu araştırma modelinde en az iki ayrı üye gerekir")
        if any(
            len(relation) != 2 or
            relation[0] not in self.members or relation[1] not in self.members or
            relation[0] == relation[1]
            for relation in self.relations
        ):
            raise ValueError("İlişkiler farklı kayıtlı üyeler arasında olmalı")

    def connected(self) -> bool:
        """Yönsüz bağlantılılık; ontolojik bütünlük veya yeterlilik ispatı değildir."""
        if not self.relations:
            return False
        adjacency = {member: set() for member in self.members}
        for left, right in self.relations:
            adjacency[left].add(right)
            adjacency[right].add(left)
        visited = set()
        stack = [next(iter(self.members))]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            stack.extend(adjacency[node] - visited)
        return visited == set(self.members)


@dataclass(frozen=True)
class TransitionCase:
    """Önkoşul, mekanizma, bağlam ve sonuç ayrı tutulur."""
    preparation: bool
    mechanism: bool
    context: bool
    outcome: bool


def transition_counterexamples(cases: list) -> dict:
    """İki hipoteze karşı örnekler; gözlemsel doğruluk testi değildir."""
    preparation_only = [
        i for i, case in enumerate(cases)
        if case.preparation and not case.outcome
    ]
    combined = [
        i for i, case in enumerate(cases)
        if case.preparation and case.mechanism and case.context
        and not case.outcome
    ]
    return {
        "preparation_sufficient_refuted": preparation_only,
        "combined_sufficient_refuted": combined,
    }



class ClaimDomain(str, Enum):
    EMPIRICAL = "EMPIRICAL"
    HISTORICAL = "HISTORICAL"
    ONTOLOGICAL = "ONTOLOGICAL"
    THEOLOGICAL = "THEOLOGICAL"
    NORMATIVE = "NORMATIVE"


@dataclass(frozen=True)
class ClaimRecord:
    identifier: str
    domain: ClaimDomain
    proposition: str
    evidence_ids: FrozenSet[str] = frozenset()

    def __post_init__(self):
        if not self.identifier.strip() or not self.proposition.strip():
            raise ValueError("İddia kimliği ve önermesi boş olamaz")


@dataclass(frozen=True)
class TransferProposal:
    source: ClaimRecord
    target_domain: ClaimDomain
    transferable_pattern: str
    target_mechanism: str = ""
    target_evidence_ids: FrozenSet[str] = frozenset()

    def assessment(self) -> str:
        """Aday yöntem aktarımı; doğruluk veya meşruiyet hükmü vermez."""
        if not self.transferable_pattern.strip():
            return "REJECT_EMPTY_PATTERN"
        if self.source.domain != self.target_domain:
            if not self.target_mechanism.strip():
                return "REVIEW_MECHANISM_MISSING"
            if not self.target_evidence_ids:
                return "REVIEW_EVIDENCE_MISSING"
            return "CROSS_DOMAIN_REVIEW_REQUIRED"
        if not self.target_evidence_ids:
            return "REVIEW_EVIDENCE_MISSING"
        return "SAME_DOMAIN_REVIEW_REQUIRED"


def center_role_entails_legitimacy(
    center_roles: dict, evidence_of_legitimacy: bool = False
) -> bool:
    """Koordinasyon veya fiziksel merkez tek başına normatif yetki vermez."""
    return bool(evidence_of_legitimacy)


@dataclass(frozen=True)
class ResponsibilityChain:
    knowledge: bool
    deliberate_choice: bool
    action: bool
    outcome_observed: bool
    norm_justified: bool

    def review_flags(self) -> FrozenSet[str]:
        flags = set()
        if self.action and not self.deliberate_choice:
            flags.add("DELIBERATION_NOT_ESTABLISHED")
        if self.deliberate_choice and not self.knowledge:
            flags.add("KNOWLEDGE_NOT_ESTABLISHED")
        if self.action and not self.outcome_observed:
            flags.add("OUTCOME_NOT_OBSERVED")
        if self.action and not self.norm_justified:
            flags.add("NORMATIVE_BASIS_NOT_ESTABLISHED")
        return frozenset(flags)


def sufficient_condition_refuted(cases: list) -> bool:
    """(P => O) önermesi için P doğru ve O yanlış bir karşı örnek var mı?"""
    return any(p and not outcome for p, outcome in cases)


def candidate_center_roles(roles: dict, role: str) -> FrozenSet[str]:
    """Merkez tekil olmak zorunda değildir; boş küme de mümkündür."""
    return frozenset(roles.get(role, ()))


def distinct_yeks(ids: list) -> bool:
    """Yek kimliklerinin çiftler hâlinde ayrılığı; sıra ve ontoloji ispatı değildir."""
    return all(isinstance(x, str) and x.strip() for x in ids) and len(ids) == len(set(ids))


class EvidenceStatus(str, Enum):
    OBSERVED = "OBSERVED"
    MODELLED = "MODELLED"
    ANALOGY = "ANALOGY"
    THEOLOGICAL = "THEOLOGICAL"
    UNKNOWN = "UNKNOWN"


class FunctionalRole(str, Enum):
    RESOURCE = "RESOURCE"
    INFORMATION = "INFORMATION"
    PROCESSING = "PROCESSING"
    CONSTRAINT = "CONSTRAINT"
    VALUE = "VALUE"


@dataclass(frozen=True)
class FunctionalObservation:
    role: FunctionalRole
    description: str
    status: EvidenceStatus
    source: str = ""

    def __post_init__(self):
        if not self.description.strip():
            raise ValueError("İşlev açıklaması boş olamaz")
        if self.status == EvidenceStatus.OBSERVED and not self.source.strip():
            raise ValueError("Gözlenen işlev için izlenebilir kaynak gerekli")


@dataclass(frozen=True)
class FunctionalProfile:
    """R/I/P/C/V; ontolojik boyutlarla birebir eşlenmez."""
    identifier: str
    observations: tuple

    def __post_init__(self):
        if not self.identifier.strip():
            raise ValueError("Profil kimliği boş olamaz")
        if any(not isinstance(x, FunctionalObservation) for x in self.observations):
            raise TypeError("Profil öğeleri FunctionalObservation olmalı")

    def role_statuses(self, role: FunctionalRole) -> FrozenSet[EvidenceStatus]:
        return frozenset(x.status for x in self.observations if x.role == role)

    def review_flags(self) -> FrozenSet[str]:
        flags = set()
        if not self.observations:
            flags.add("NO_OBSERVATIONS")
        if any(x.status == EvidenceStatus.ANALOGY for x in self.observations):
            flags.add("ANALOGY_NOT_IDENTITY")
        if any(x.status == EvidenceStatus.THEOLOGICAL for x in self.observations):
            flags.add("THEOLOGICAL_NOT_EMPIRICAL")
        if not self.role_statuses(FunctionalRole.VALUE):
            flags.add("NORMATIVE_ASSESSMENT_NOT_SPECIFIED")
        return frozenset(flags)


def analogy_transfer_review(source: FunctionalObservation,
                            target: FunctionalObservation) -> str:
    """İşlev benzerliği tek başına mekanizma veya varlık özdeşliği değildir."""
    if source.role != target.role:
        return "REVIEW_ROLE_MISMATCH"
    if (source.status in {EvidenceStatus.ANALOGY, EvidenceStatus.THEOLOGICAL}
            or target.status in {EvidenceStatus.ANALOGY, EvidenceStatus.THEOLOGICAL}):
        return "ANALOGY_ONLY"
    return "EVIDENCE_REVIEW_REQUIRED"
