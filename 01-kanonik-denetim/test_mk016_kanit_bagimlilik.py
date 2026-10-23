import unittest

from mk016_kanit_bagimlilik import Approval, audit_approvals, pilot_cases


class MK016Tests(unittest.TestCase):
    def test_shared_data_flagged(self):
        x = pilot_cases()["same_faulty_device"]
        self.assertEqual(x["approval_count"], 2)
        self.assertEqual(x["distinct_data_source_labels"], 1)
        self.assertEqual(x["status"], "SHARED_DEPENDENCY_REVIEW")
        self.assertEqual(x["shared_data_pairs"][0]["sources"], ["D1"])

    def test_different_data_not_certified_independent(self):
        x = pilot_cases()["distinct_declared_data"]
        self.assertEqual(x["shared_data_pairs"], [])
        self.assertEqual(x["status"],
                         "NO_DECLARED_SHARED_DEPENDENCY_NOT_PROOF_OF_INDEPENDENCE")

    def test_shared_data_different_methods_still_flagged(self):
        x = pilot_cases()["same_data_different_methods"]
        self.assertTrue(x["shared_data_pairs"])
        self.assertFalse(x["shared_method_pairs"])

    def test_shared_method_separately_flagged(self):
        x = audit_approvals([
            Approval("A", "P", frozenset({"D1"}), frozenset({"M"})),
            Approval("B", "P", frozenset({"D2"}), frozenset({"M"})),
        ])
        self.assertFalse(x["shared_data_pairs"])
        self.assertTrue(x["shared_method_pairs"])

    def test_empty_is_unknown(self):
        self.assertEqual(audit_approvals([])["status"], "INSUFFICIENT_INFORMATION")

    def test_duplicate_reviewer_rejected(self):
        with self.assertRaises(ValueError):
            audit_approvals([
                Approval("A", "P", frozenset({"D1"}), frozenset({"M1"})),
                Approval("A", "P", frozenset({"D2"}), frozenset({"M2"})),
            ])

    def test_different_claims_rejected(self):
        with self.assertRaises(ValueError):
            audit_approvals([
                Approval("A", "P", frozenset({"D1"}), frozenset({"M1"})),
                Approval("B", "Q", frozenset({"D2"}), frozenset({"M2"})),
            ])

    def test_missing_provenance_rejected(self):
        with self.assertRaises(ValueError):
            Approval("A", "P", frozenset(), frozenset({"M1"}))

    def test_single_approval_not_certified(self):
        x = audit_approvals([
            Approval("A", "P", frozenset({"D1"}), frozenset({"M1"}))
        ])
        self.assertEqual(x["approval_count"], 1)
        self.assertIn("NOT_PROOF", x["status"])


if __name__ == "__main__":
    unittest.main()
