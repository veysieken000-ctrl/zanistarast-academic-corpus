"""MK-016 pilot: distinguish approval count from evidence-source independence.

This is a structural counterexample detector, not a statistical estimator
of independence, truth, reliability, or peer-review completion.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Approval:
    reviewer: str
    claim: str
    data_sources: frozenset[str]
    methods: frozenset[str]

    def __post_init__(self):
        if not self.reviewer.strip() or not self.claim.strip():
            raise ValueError("reviewer and claim required")
        if not self.data_sources or not self.methods:
            raise ValueError("sources and methods required")


def audit_approvals(approvals):
    """Return layer-specific shared dependency flags; never certify independence."""
    if not approvals:
        return {"claim": None, "approval_count": 0, "unique_reviewers": 0,
                "shared_data_pairs": [], "shared_method_pairs": [],
                "status": "INSUFFICIENT_INFORMATION"}
    claims = {a.claim for a in approvals}
    if len(claims) != 1:
        raise ValueError("Cannot compare approvals for different claims")
    if len({a.reviewer for a in approvals}) != len(approvals):
        raise ValueError("One reviewer must not be counted as distinct reviewers")
    shared_data, shared_methods = [], []
    for i, a in enumerate(approvals):
        for b in approvals[i + 1:]:
            data = sorted(a.data_sources & b.data_sources)
            methods = sorted(a.methods & b.methods)
            if data:
                shared_data.append({"reviewers": [a.reviewer, b.reviewer],
                                    "sources": data})
            if methods:
                shared_methods.append({"reviewers": [a.reviewer, b.reviewer],
                                       "methods": methods})
    return {
        "claim": approvals[0].claim,
        "approval_count": len(approvals),
        "unique_reviewers": len(approvals),
        "distinct_data_source_labels": len(set().union(
            *(a.data_sources for a in approvals))),
        "shared_data_pairs": shared_data,
        "shared_method_pairs": shared_methods,
        "status": ("SHARED_DEPENDENCY_REVIEW" if shared_data or shared_methods
                   else "NO_DECLARED_SHARED_DEPENDENCY_NOT_PROOF_OF_INDEPENDENCE"),
    }


def pilot_cases():
    return {
        "same_faulty_device": audit_approvals([
            Approval("S1", "P", frozenset({"D1"}), frozenset({"M1"})),
            Approval("S2", "P", frozenset({"D1"}), frozenset({"M2"})),
        ]),
        "distinct_declared_data": audit_approvals([
            Approval("S1", "P", frozenset({"D1"}), frozenset({"M1"})),
            Approval("S2", "P", frozenset({"D2"}), frozenset({"M2"})),
        ]),
        "same_data_different_methods": audit_approvals([
            Approval("S1", "P", frozenset({"D1"}), frozenset({"M1"})),
            Approval("S2", "P", frozenset({"D1"}), frozenset({"M2"})),
        ]),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(pilot_cases(), ensure_ascii=False, indent=2))
