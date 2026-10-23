"""Bidirectional paper impact scanner regression tests."""
import tempfile
import unittest
from pathlib import Path

from mantik_aktarim_etki_tarama import (
    affected_reviews, changed_since_baseline, git_blob_sha, load_inventory,
    impact_metrics,
)


class TransferImpactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_inventory()

    def test_eight_nodes(self):
        self.assertEqual(len(self.data["nodes"]), 8)

    def test_fifteen_links(self):
        self.assertEqual(len(self.data["edges"]), 15)

    def test_single_change_finds_bidirectional_neighbors(self):
        path = next(n["path"] for n in self.data["nodes"] if n["id"] == "jeoloji")
        edges = affected_reviews(self.data, [path])
        self.assertEqual({e["edge_id"] for e in edges}, {"T01", "T02", "T07", "T12"})

    def test_reverse_direction_is_included(self):
        path = next(n["path"] for n in self.data["nodes"] if n["id"] == "h04")
        edges = affected_reviews(self.data, [path])
        self.assertEqual({e["edge_id"] for e in edges}, {"T02", "T04", "T05", "T15"})

    def test_h01_impacts_h02_h03_varlik_jeoloji(self):
        path = next(n["path"] for n in self.data["nodes"] if n["id"] == "h01")
        edges = affected_reviews(self.data, [path])
        self.assertEqual({e["edge_id"] for e in edges},
                         {"T08", "T10", "T11", "T12"})

    def test_h02_reverse_triggers_h01_h03_h05(self):
        path = next(n["path"] for n in self.data["nodes"] if n["id"] == "h02")
        edges = affected_reviews(self.data, [path])
        self.assertEqual({e["edge_id"] for e in edges},
                         {"T08", "T09", "T13"})

    def test_h03_impacts_history_and_morality(self):
        path = next(n["path"] for n in self.data["nodes"] if n["id"] == "h03")
        edges = affected_reviews(self.data, [path])
        self.assertEqual({e["edge_id"] for e in edges},
                         {"T09", "T10", "T14", "T15"})

    def test_all_edges_have_traceable_reasoning(self):
        fields = ("source_section", "target_section", "transferable_claim",
                  "counterexample", "evidence_status", "review_status",
                  "source_baseline_sha", "target_baseline_sha")
        for edge in self.data["edges"]:
            for field in fields:
                self.assertTrue(edge.get(field), f"{edge['id']} missing {field}")

    def test_edge_baselines_match_nodes(self):
        nodes = {n["id"]: n for n in self.data["nodes"]}
        for edge in self.data["edges"]:
            self.assertEqual(edge["source_baseline_sha"],
                             nodes[edge["source"]]["baseline_blob_sha"])
            self.assertEqual(edge["target_baseline_sha"],
                             nodes[edge["target"]]["baseline_blob_sha"])

    def test_no_edge_is_marked_independently_approved(self):
        self.assertTrue(all(e["review_status"] == "PENDING_INDEPENDENT_RASTERAST"
                            for e in self.data["edges"]))

    def test_missing_counterexample_rejected_by_loader(self):
        import copy
        import json
        with tempfile.TemporaryDirectory() as tmp:
            bad = copy.deepcopy(self.data)
            bad["edges"][0]["counterexample"] = ""
            path = Path(tmp) / "bad.json"
            path.write_text(json.dumps(bad))
            with self.assertRaises(ValueError):
                load_inventory(path)

    def test_source_sha_mismatch_rejected_by_loader(self):
        import copy
        import json
        with tempfile.TemporaryDirectory() as tmp:
            bad = copy.deepcopy(self.data)
            bad["edges"][0]["source_baseline_sha"] = "0" * 40
            path = Path(tmp) / "bad.json"
            path.write_text(json.dumps(bad))
            with self.assertRaises(ValueError):
                load_inventory(path)

    def test_unreviewed_edge_cannot_claim_approval(self):
        import copy
        import json
        with tempfile.TemporaryDirectory() as tmp:
            bad = copy.deepcopy(self.data)
            bad["edges"][0]["review_status"] = "APPROVED"
            path = Path(tmp) / "bad.json"
            path.write_text(json.dumps(bad))
            with self.assertRaises(ValueError):
                load_inventory(path)

    def test_advisory_contains_traceable_counterexample(self):
        path = next(n["path"] for n in self.data["nodes"] if n["id"] == "h01")
        edges = affected_reviews(self.data, [path])
        self.assertTrue(all(e["counterexample"] and e["source_section"]
                            and e["target_section"] for e in edges))

    def test_metrics_no_changed_papers(self):
        metrics = impact_metrics(self.data, [])
        self.assertEqual(metrics["tracked_papers"], 8)
        self.assertEqual(metrics["tracked_links"], 15)
        self.assertEqual(metrics["affected_links"], 0)
        self.assertEqual(metrics["affected_link_share"], 0.0)

    def test_metrics_h01_four_affected_links(self):
        path = next(n["path"] for n in self.data["nodes"] if n["id"] == "h01")
        metrics = impact_metrics(self.data, [path])
        self.assertEqual(metrics["changed_tracked_papers"], 1)
        self.assertEqual(metrics["affected_links"], 4)
        self.assertEqual(metrics["affected_papers"], 5)
        self.assertEqual(metrics["affected_link_share"], round(4 / 15, 4))

    def test_metrics_no_unearned_speed_claim(self):
        paths = [n["path"] for n in self.data["nodes"]]
        metrics = impact_metrics(self.data, paths)
        self.assertIsNone(metrics["time_saved_minutes"])
        self.assertEqual(metrics["independent_reviews_completed"], 0)
        self.assertEqual(metrics["affected_links"], 15)

    def test_metrics_unknown_path_does_not_inflate(self):
        metrics = impact_metrics(self.data, ["not-tracked.md"])
        self.assertEqual(metrics["changed_tracked_papers"], 0)
        self.assertEqual(metrics["affected_papers"], 0)

    def test_unknown_change_no_review(self):
        self.assertEqual(affected_reviews(self.data, ["README.md"]), [])

    def test_duplicate_changes_do_not_duplicate_edges(self):
        path = next(n["path"] for n in self.data["nodes"] if n["id"] == "h05")
        edges = affected_reviews(self.data, [path, path])
        self.assertEqual(len(edges), 4)

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
            self.assertEqual(len(changed_since_baseline(self.data, root)), 8)

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
