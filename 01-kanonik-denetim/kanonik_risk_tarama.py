#!/usr/bin/env python3
"""R1–R5 conservative, review-only canonical risk scanner. Stdlib only.
Usage: python3 01-kanonik-denetim/kanonik_risk_tarama.py --root . --rules 01-kanonik-denetim/KANONIK-AKTARIM-RISK-KURALLARI-R1-R5-2026-10-23.json --output risk-uyarilari.json
No automatic correction, deletion, merging or publication.
"""
import argparse
import json
import re
from pathlib import Path

PATTERNS = {
 "R1": [r"(?i)(?:4[.]?\s*boyut|D4).{0,110}(?:zaman|sorumluluk\s*eşiği)",
        r"(?i)(?:zaman|sorumluluk\s*eşiği).{0,110}(?:4[.]?\s*boyut|D4)"],
 "R2": [r"(?i)(?:geometrik|fiziksel)\s+merkez.{0,120}(?:ilk\s+yek|ontolojik\s+(?:ilk|köken|kanıt))"],
 "R3": [r"(?i)(?:prosedür|usul|P\(q\)).{0,120}(?:meşruiyet\s+(?:kanıtıdır|garantiler)|meşrudur)"],
 "R4": [r"(?i)(?:erişim|reach|iki\s+onay).{0,110}(?:bağımsız\s+kanıt(?:tır)?|doğruluğu\s+kanıtlar)"],
 "R5": [r"(?i)Rasterast.{0,100}(?:yalnızca|sadece)\s+(?:bir\s+)?(?:geçti.kaldı|ikili\s+filtre)"]
}
# Supplemental patterns for inflected Turkish and short-form claims.
PATTERNS["R2"].append(r"(?i)merkez(?:de)?\s+olmak.{0,100}ontolojik\s+(?:köken|ilk|başlangıç)")
PATTERNS["R3"].append(r"(?i)(?:prosedür|usul).{0,120}meşruiyet(?:i|in)?\s+garantiler")
PATTERNS["R5"].append(r"(?i)Rasterast.{0,100}(?:yalnızca|sadece)\s+(?:bir\s+)?filtredir")
NEGATIONS = re.compile(r"(?i)(?:değildir|değil|sayılamaz|özdeş\s+değildir|yanlıştır|kanıtlamaz|indirgenemez|otomatik\s+olarak|karıştırılma)")
def scan(root, rules, paths):
    ids = {r["id"] for r in rules["rules"]}
    results = []
    for path in paths:
        if not path.is_file() or path.suffix.lower() not in {".md", ".txt"}:
            continue
        for line_no, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for rid, expressions in PATTERNS.items():
                if rid not in ids:
                    continue
                if any(re.search(pattern, line) for pattern in expressions):
                    # Negation is a *context* signal, not a guarantee of safety.
                    results.append({"file": str(path.relative_to(root)), "line": line_no,
                                    "rule_id": rid, "status": "REVIEW_ONLY",
                                    "negation_or_quotation_context": bool(NEGATIONS.search(line)),
                                    "excerpt": line[:350]})
    return results
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=".")
    p.add_argument("--rules", required=True)
    p.add_argument("--output", default="risk-uyarilari.json")
    args = p.parse_args()
    root = Path(args.root).resolve()
    rules = json.loads(Path(args.rules).read_text(encoding="utf-8"))
    paths = sorted(root.rglob("*.md"))
    findings = scan(root, rules, paths)
    result = {"status": "heuristic_review_only", "scanned_files": len(paths),
              "warning_count": len(findings), "warnings": findings}
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"scanned_files": len(paths), "warning_count": len(findings)}, ensure_ascii=False))
if __name__ == "__main__":
    main()
