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

    def test_r2_center_ontological_origin_negative_context(self):
        findings = self.run_case("Merkezde olmak ontolojik kökeni kanıtlamaz")
        self.assertIn("R2", {x["rule_id"] for x in findings})
        self.assertTrue(findings[0]["negation_or_quotation_context"])

    def test_r3_inflected_legitimacy(self):
        self.assertIn("R3", {x["rule_id"] for x in self.run_case("prosedür meşruiyeti garantiler")})

    def test_r5_short_filter(self):
        self.assertIn("R5", {x["rule_id"] for x in self.run_case("Rasterast yalnızca filtredir")})

    def test_matched_span_and_full_line(self):
        sentence = "Ön bilgi: " + "4. boyut zaman değildir" + " — bağlam."
        findings = self.run_case(sentence)
        self.assertTrue(findings)
        item = findings[0]
        start, end = item["matched_span"]
        self.assertEqual(sentence[start:end], item["matched_text"])
        self.assertEqual(sentence, item["line_excerpt"])
        self.assertEqual("REVIEW_ONLY", item["status"])

    def test_a11_counterexample_is_review_only(self):
        sentence = "İki denetçi aynı hatalı rapordan beslendiğinde iki onay bağımsız kanıt sayılmaz."
        findings = self.run_case(sentence)
        self.assertIn("R4", {x["rule_id"] for x in findings})
        self.assertTrue(any(x["negation_or_quotation_context"] for x in findings))

    def test_context_priority_without_suppressing_warning(self):
        findings = self.run_case("İki onay bağımsız kanıt sayılmaz")
        self.assertEqual(1, len(findings))
        self.assertEqual("CONTEXT_FIRST", findings[0]["review_priority"])
        self.assertEqual("REVIEW_ONLY", findings[0]["status"])

    def test_standard_priority_for_unqualified_claim(self):
        findings = self.run_case("Rasterast sadece ikili filtre")
        self.assertEqual(1, len(findings))
        self.assertEqual("STANDARD", findings[0]["review_priority"])

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
