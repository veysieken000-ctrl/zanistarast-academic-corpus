"""MK-001–003 / MK-013–015: bidirectional review impact scanner (stdlib only).

Usage: python3 01-kanonik-denetim/mantik_aktarim_etki_tarama.py [changed/path ...]
Without arguments, compares tracked files to the inventory baseline git blob SHAs.
Advisory only; no automatic edits, approvals or publication.
"""
import hashlib
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
INVENTORY = HERE / "mantik_aktarim_baglantilari.json"


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def load_inventory(path=INVENTORY):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    nodes = data["nodes"]
    edges = data["edges"]
    ids = {node["id"] for node in nodes}
    if len(ids) != len(nodes) or len({node["path"] for node in nodes}) != len(nodes):
        raise ValueError("Duplicate node ID or path")
    if any(edge["source"] not in ids or edge["target"] not in ids
           or edge["source"] == edge["target"] for edge in edges):
        raise ValueError("Invalid transfer edge")
    if len({edge["id"] for edge in edges}) != len(edges):
        raise ValueError("Duplicate edge ID")
    if data.get("schema_version", 0) < 2:
        raise ValueError("Traceable edge schema v2 required")
    node_by_id = {node["id"]: node for node in nodes}
    required = ("source_section", "target_section", "transferable_claim",
                "counterexample", "evidence_status", "review_status",
                "source_baseline_sha", "target_baseline_sha")
    for edge in edges:
        if any(not isinstance(edge.get(field), str) or not edge[field].strip()
               for field in required):
            raise ValueError(f"Missing traceable reasoning: {edge['id']}")
        if edge["source_baseline_sha"] != node_by_id[edge["source"]]["baseline_blob_sha"]:
            raise ValueError(f"Source SHA mismatch: {edge['id']}")
        if edge["target_baseline_sha"] != node_by_id[edge["target"]]["baseline_blob_sha"]:
            raise ValueError(f"Target SHA mismatch: {edge['id']}")
        if edge["review_status"] != "PENDING_INDEPENDENT_RASTERAST":
            raise ValueError(f"Unreviewed edge cannot be approved: {edge['id']}")
    return data


def changed_since_baseline(data, root=ROOT):
    changed = []
    for node in data["nodes"]:
        file = Path(root) / node["path"]
        if not file.is_file() or git_blob_sha(file.read_bytes()) != node["baseline_blob_sha"]:
            changed.append(node["path"])
    return changed


def affected_reviews(data, changed_paths):
    paths = {node["path"]: node["id"] for node in data["nodes"]}
    ids = set(paths[path] for path in changed_paths if path in paths)
    found = []
    for edge in data["edges"]:
        if edge["source"] in ids or edge["target"] in ids:
            found.append({
                "edge_id": edge["id"],
                "source": edge["source"],
                "target": edge["target"],
                "mk": edge["mk"],
                "risk": edge["risk"],
                "source_section": edge["source_section"],
                "target_section": edge["target_section"],
                "transferable_claim": edge["transferable_claim"],
                "counterexample": edge["counterexample"],
                "evidence_status": edge["evidence_status"],
                "review_status": edge["review_status"],
                "triggered_by": sorted(ids & {edge["source"], edge["target"]}),
                "status": "REVIEW_ONLY",
            })
    return found


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    data = load_inventory()
    changed = argv if argv else changed_since_baseline(data)
    result = {
        "changed_tracked_paths": sorted(set(changed)),
        "affected_reviews": affected_reviews(data, changed),
        "status": "REVIEW_ONLY",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
