#!/usr/bin/env python3
"""Deterministic regression checks for the R1–R5 review-only scanner."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).with_name("kanonik_risk_tarama.py")
spec = importlib.util.spec_from_file_location("kanonik_risk_tarama", MODULE)
scanner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scanner)

RULES = {"rules": [{"id": key} for key in scanner.PATTERNS]}

class ScannerTests(unittest.TestCase):
    def run_case(self, sentence):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "case.md"
            path.write_text(sentence + "\n", encoding="utf-8")
            return scanner.scan(root, RULES, [path])

    def test_r1_legacy_dimension_conflict(self):
        self.assertIn("R1", {x["rule_id"] for x in self.run_case("4. Boyut = Zaman + sorumluluk eşiği")})

    def test_r1_explicit_negation_is_review_not_auto_failure(self):
        findings = self.run_case("4. boyut zaman değildir")
        self.assertTrue(findings)
        self.assertTrue(findings[0]["negation_or_quotation_context"])
        self.assertEqual(findings[0]["status"], "REVIEW_ONLY")

    def test_r2_geometric_center_claim(self):
        self.assertIn("R2", {x["rule_id"] for x in self.run_case("geometrik merkez ilk Yek demektir")})

    def test_r3_procedure_legitimacy_claim(self):
        self.assertIn("R3", {x["rule_id"] for x in self.run_case("prosedür meşruiyet garantiler")})

    def test_r4_access_truth_claim(self):
        self.assertIn("R4", {x["rule_id"] for x in self.run_case("reach doğruluğu kanıtlar")})

    def test_r5_filter_reduction(self):
        self.assertIn("R5", {x["rule_id"] for x in self.run_case("Rasterast sadece ikili filtre")})

    def test_no_unrelated_alert(self):
        self.assertEqual([], self.run_case("Kozmik boyut ve insan katmanı farklı kavramlardır."))

    def test_line_number(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "case.md"
            path.write_text("Başlık\n4. boyut zaman değildir\n", encoding="utf-8")
            findings = scanner.scan(root, RULES, [path])
            self.assertEqual(2, findings[0]["line"])

if __name__ == "__main__":
    unittest.main()
