"""MK-013–015: seven-link bidirectional review impact scanner (stdlib only).

Usage: python3 01-kanonik-denetim/mantik_aktarim_etki_tarama.py [changed/path ...]
Without arguments, compares tracked files to the inventory baseline git blob SHAs.
Advisory only; no automatic edits, approvals or publication.
"""
import hashlib
import json
import subprocess
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
