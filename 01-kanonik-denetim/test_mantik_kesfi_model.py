"""MK-005–MK-012 modelinin regresyon ve karşı-örnek testleri."""
import unittest

from mantik_kesfi_model import (
    Node, NodeType, Edge, EdgeType, TypedGraph,
    sufficient_condition_refuted, candidate_center_roles, distinct_yeks,
    KomelCandidate, TransitionCase, transition_counterexamples,
)


class LogicDiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.g = TypedGraph()
        for name, kind in [
            ("y1", NodeType.CREATED_YEK), ("y2", NodeType.CREATED_YEK),
            ("y3", NodeType.CREATED_YEK), ("y4", NodeType.CREATED_YEK),
            ("komel", NodeType.KOMEL), ("bilen1", NodeType.OBSERVER),
            ("bilen2", NodeType.OBSERVER), ("iddia", NodeType.CLAIM),
            ("delil", NodeType.EVIDENCE),
        ]:
            self.g.add_node(Node(name, kind))

    def test_yek_turemesi(self):
        self.g.add_edge(Edge("y2", "y1", EdgeType.DERIVES_FROM))
        self.g.add_edge(Edge("y3", "y2", EdgeType.DERIVES_FROM))
        self.g.add_edge(Edge("y4", "y3", EdgeType.DERIVES_FROM))
        self.assertEqual(len(self.g.edges), 3)

    def test_yek_komel_uyeligi(self):
        self.g.add_edge(Edge("y1", "komel", EdgeType.MEMBER_OF))
        self.assertEqual(self.g.edges[0].kind, EdgeType.MEMBER_OF)

    def test_second_knower_is_not_second_yek(self):
        with self.assertRaises(TypeError):
            self.g.add_edge(Edge("bilen2", "y1", EdgeType.DERIVES_FROM))

    def test_created_yek_cannot_validate_as_knower(self):
        with self.assertRaises(TypeError):
            self.g.add_edge(Edge("y2", "iddia", EdgeType.VALIDATES))

    def test_evidence_not_yek_origin(self):
        with self.assertRaises(TypeError):
            self.g.add_edge(Edge("delil", "y1", EdgeType.DERIVES_FROM))

    def test_no_self_derivation(self):
        with self.assertRaises(ValueError):
            self.g.add_edge(Edge("y1", "y1", EdgeType.DERIVES_FROM))

    def test_two_approvals_shared_source(self):
        self.g.add_edge(Edge("bilen1", "iddia", EdgeType.VALIDATES))
        self.g.add_edge(Edge("bilen2", "iddia", EdgeType.VALIDATES))
        self.assertEqual(self.g.independent_validations("iddia", {
            "bilen1": "ortak_olcum", "bilen2": "ortak_olcum"
        }), 1)

    def test_two_approvals_distinct_provenance(self):
        self.g.add_edge(Edge("bilen1", "iddia", EdgeType.VALIDATES))
        self.g.add_edge(Edge("bilen2", "iddia", EdgeType.VALIDATES))
        self.assertEqual(self.g.independent_validations("iddia", {
            "bilen1": "kaynak_A", "bilen2": "kaynak_B"
        }), 2)

    def test_missing_provenance_not_assumed_independent(self):
        self.g.add_edge(Edge("bilen1", "iddia", EdgeType.VALIDATES))
        with self.assertRaises(ValueError):
            self.g.independent_validations("iddia", {})

    def test_preparation_not_sufficient(self):
        self.assertTrue(sufficient_condition_refuted([(True, False)]))

    def test_no_counterexample_is_not_proof(self):
        self.assertFalse(sufficient_condition_refuted([(True, True), (False, False)]))

    def test_center_may_be_distributed(self):
        self.assertEqual(candidate_center_roles({
            "coordination": ["node_a", "node_b"]
        }, "coordination"), frozenset({"node_a", "node_b"}))

    def test_center_may_be_absent(self):
        self.assertEqual(candidate_center_roles({}, "geometric"), frozenset())

    def test_center_roles_are_distinct(self):
        roles = {"geometric": ["barycenter"], "normative": ["adalet"]}
        self.assertNotEqual(candidate_center_roles(roles, "geometric"),
                            candidate_center_roles(roles, "normative"))

    def test_four_distinct_yeks(self):
        self.assertTrue(distinct_yeks(["y1", "y2", "y3", "y4"]))

    def test_repeated_identity_detected(self):
        self.assertFalse(distinct_yeks(["y1", "y2", "y1", "y4"]))

    def test_empty_identity_detected(self):
        self.assertFalse(distinct_yeks(["y1", ""]))

    def test_duplicate_node_rejected(self):
        with self.assertRaises(ValueError):
            self.g.add_node(Node("y1", NodeType.CREATED_YEK))

    def test_undefined_endpoint_rejected(self):
        with self.assertRaises(ValueError):
            self.g.add_edge(Edge("y1", "missing", EdgeType.DERIVES_FROM))

    def test_indirect_yek_derivation_cycle_rejected(self):
        self.g.add_edge(Edge("y2", "y1", EdgeType.DERIVES_FROM))
        self.g.add_edge(Edge("y3", "y2", EdgeType.DERIVES_FROM))
        with self.assertRaises(ValueError):
            self.g.add_edge(Edge("y1", "y3", EdgeType.DERIVES_FROM))

    def test_cycle_rejection_keeps_previous_edges(self):
        self.g.add_edge(Edge("y2", "y1", EdgeType.DERIVES_FROM))
        with self.assertRaises(ValueError):
            self.g.add_edge(Edge("y1", "y2", EdgeType.DERIVES_FROM))
        self.assertEqual(len(self.g.edges), 1)

    def test_distinct_provenance_roots_not_independence(self):
        self.g.add_edge(Edge("bilen1", "iddia", EdgeType.VALIDATES))
        self.g.add_edge(Edge("bilen2", "iddia", EdgeType.VALIDATES))
        roots = {"bilen1": "ortak_veri", "bilen2": "ortak_veri"}
        self.assertEqual(self.g.distinct_provenance_roots("iddia", roots), 1)
        self.assertEqual(self.g.independent_validations("iddia", roots), 1)

    def test_missing_or_blank_provenance_rejected(self):
        self.g.add_edge(Edge("bilen1", "iddia", EdgeType.VALIDATES))
        with self.assertRaises(ValueError):
            self.g.distinct_provenance_roots("iddia", {"bilen1": ""})

    def test_provenance_target_must_be_claim(self):
        with self.assertRaises(ValueError):
            self.g.distinct_provenance_roots("y1", {})

    def test_komel_connected_candidate(self):
        candidate = KomelCandidate(
            frozenset({"y1", "y2", "y3"}),
            frozenset({("y1", "y2"), ("y2", "y3")}),
        )
        self.assertTrue(candidate.connected())

    def test_komel_disconnected_candidate(self):
        candidate = KomelCandidate(
            frozenset({"y1", "y2", "y3"}),
            frozenset({("y1", "y2")}),
        )
        self.assertFalse(candidate.connected())

    def test_komel_two_members_required_for_this_model(self):
        with self.assertRaises(ValueError):
            KomelCandidate(frozenset({"y1"}), frozenset())

    def test_komel_unknown_member_rejected(self):
        with self.assertRaises(ValueError):
            KomelCandidate(
                frozenset({"y1", "y2"}),
                frozenset({("y1", "unknown")}),
            )

    def test_komel_self_relation_rejected(self):
        with self.assertRaises(ValueError):
            KomelCandidate(
                frozenset({"y1", "y2"}),
                frozenset({("y1", "y1")}),
            )

    def test_komel_empty_relations_not_connected(self):
        candidate = KomelCandidate(
            frozenset({"y1", "y2"}), frozenset(),
        )
        self.assertFalse(candidate.connected())

    def test_preparation_does_not_entail_transition(self):
        cases = [TransitionCase(True, False, True, False)]
        self.assertEqual(
            transition_counterexamples(cases)["preparation_sufficient_refuted"],
            [0],
        )
        self.assertEqual(
            transition_counterexamples(cases)["combined_sufficient_refuted"],
            [],
        )

    def test_full_transition_hypothesis_can_be_refuted(self):
        cases = [TransitionCase(True, True, True, False)]
        self.assertEqual(
            transition_counterexamples(cases)["combined_sufficient_refuted"],
            [0],
        )

    def test_positive_case_is_not_proof(self):
        cases = [TransitionCase(True, True, True, True)]
        self.assertEqual(
            transition_counterexamples(cases)["combined_sufficient_refuted"],
            [],
        )

    def test_transition_counterexample_indices(self):
        cases = [
            TransitionCase(False, False, False, False),
            TransitionCase(True, False, True, False),
            TransitionCase(True, True, True, False),
        ]
        self.assertEqual(
            transition_counterexamples(cases)["preparation_sufficient_refuted"],
            [1, 2],
        )
        self.assertEqual(
            transition_counterexamples(cases)["combined_sufficient_refuted"],
            [2],
        )

    def test_duplicate_edge_is_idempotent(self):
        edge = Edge("y1", "komel", EdgeType.MEMBER_OF)
        self.g.add_edge(edge)
        self.g.add_edge(edge)
        self.assertEqual(len(self.g.edges), 1)


if __name__ == "__main__":
    unittest.main()
