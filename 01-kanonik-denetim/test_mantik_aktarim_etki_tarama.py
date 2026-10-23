"""Bidirectional paper impact scanner regression tests."""
import tempfile
import unittest
from pathlib import Path

from mantik_aktarim_etki_tarama import (
    affected_reviews, changed_since_baseline, git_blob_sha, load_inventory,
)


class TransferImpactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_inventory()

    def test_five_nodes(self):
        self.assertEqual(len(self.data["nodes"]), 5)

    def test_seven_links(self):
        self.assertEqual(len(self.data["edges"]), 7)

    def test_single_change_finds_bidirectional_neighbors(self):
        path = next(n["path"] for n in self.data["nodes"] if n["id"] == "jeoloji")
        edges = affected_reviews(self.data, [path])
        self.assertEqual({e["edge_id"] for e in edges}, {"T01", "T02", "T07"})

    def test_reverse_direction_is_included(self):
        path = next(n["path"] for n in self.data["nodes"] if n["id"] == "h04")
        edges = affected_reviews(self.data, [path])
        self.assertEqual({e["edge_id"] for e in edges}, {"T02", "T04", "T05"})

    def test_unknown_change_no_review(self):
        self.assertEqual(affected_reviews(self.data, ["README.md"]), [])

    def test_duplicate_changes_do_not_duplicate_edges(self):
        path = next(n["path"] for n in self.data["nodes"] if n["id"] == "h05")
        edges = affected_reviews(self.data, [path, path])
        self.assertEqual(len(edges), 3)

    def test_every_result_review_only(self):
        paths = [n["path"] for n in self.data["nodes"]]
        self.assertTrue(all(x["status"] == "REVIEW_ONLY"
                            for x in affected_reviews(self.data, paths)))

    def test_git_blob_hash_matches_baseline_for_tracked_files(self):
        self.assertEqual(changed_since_baseline(self.data), [])

    def test_modified_file_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for node in self.data["nodes"]:
                file = root / node["path"]
                file.parent.mkdir(parents=True, exist_ok=True)
                file.write_bytes(b"not the original")
            self.assertEqual(len(changed_since_baseline(self.data, root)), 5)

    def test_git_blob_sha_deterministic(self):
        self.assertEqual(git_blob_sha(b"test"), git_blob_sha(b"test"))

    def test_duplicate_nodes_rejected(self):
        import json
        with tempfile.TemporaryDirectory() as tmp:
            bad = dict(self.data)
            bad["nodes"] = self.data["nodes"] + [self.data["nodes"][0]]
            path = Path(tmp) / "bad.json"
            path.write_text(json.dumps(bad))
            with self.assertRaises(ValueError):
                load_inventory(path)

    def test_invalid_edge_rejected(self):
        import json
        with tempfile.TemporaryDirectory() as tmp:
            bad = dict(self.data)
            bad["edges"] = self.data["edges"] + [{
                "id": "T08", "source": "unknown", "target": "h05",
                "mk": "MK-015", "risk": "invalid"
            }]
            path = Path(tmp) / "bad.json"
            path.write_text(json.dumps(bad))
            with self.assertRaises(ValueError):
                load_inventory(path)


if __name__ == "__main__":
    unittest.main()
