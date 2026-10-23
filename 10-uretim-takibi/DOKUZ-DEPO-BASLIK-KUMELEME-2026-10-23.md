# Dokuz depo — başlık normalizasyonu ve olası tekrar kümeleri
**23 Ekim 2026 | ön inceleme | yayın ve özgünlük kararı değil**

## Kapsam ve yöntem
Dokuz ilişkili GitHub deposunun `main` dallarındaki 494 başlık filtresi eşleşmesi, dosya uzantısı ve biçim farkları kaldırılarak karşılaştırıldı. Basit normalizasyon: Unicode aksanlarını ayırma, küçük harf, md/html/txt/docx/pdf uzantısını çıkarma, dosya başındaki makale/paper/article numaralarını ve sürüm/son/taslak işaretlerini çıkarma, noktalama yerine boşluk. **Bu bir aday bulma filtresidir; anlamsal eşdeğerlik ispatı değildir.**

- Başlık filtresinden geçen dosya: **494**
- Farklı normalize başlık: **483**
- Birden fazla dosyaya sahip başlık kümesi: **9**
- Bu kümelerdeki toplam dosya: **20**
- Normalizasyonla birleşen fazla kayıt: **11**
- 494 dosyanın Git blob SHA'sı: **494 farklı SHA** (birebir byte kopyası yok)

## İncelenecek dokuz küme
1. `00 time theory unified mind` — `ZANISTARAST-TEORILER/theories/08_ZAMAN_THEORY/00_TIME_THEORY_UNIFIED_MIND.md`; `zanistarast-ai-native-model/00_TIME_THEORY_UNIFIED_MIND.html`
2. `01 time theory rasterast zanistarast` — aynı iki depodaki `01_TIME_THEORY_RASTERAST_ZANISTARAST` md/html
3. `02 unified mind theory zanistarast` — aynı iki depodaki `02_UNIFIED_MIND_THEORY_ZANISTARAST` md/html
4. `03 time mind synthesis zanistarast` — aynı iki depodaki `03_TIME_MIND_SYNTHESIS_ZANISTARAST` md/html
5. `core` — `zanistarast-formal-foundations/CORE.md`, `zanistarast-ai-native-model/core.html`, `zanistarast-ai-native-model/makale-12-core.html`
6. `article system` — `zanistarast-ai-native-model/article-system.html`, `backend/_article_system.txt`, `backend/knowledge/_article_system.txt`
7. `paper` — `zanistarast-ai-native-model/docs/paper-draft.md`, `paper.html`
8. `merkez cevre yasasi` — `zanistarast-ai-native-model/makale-01-06-merkez-cevre-yasasi.html`, `makale-04-07-merkez-cevre-yasasi.html`
9. `insan dunyasi mana ve sanat` — `zanistarast-ai-native-model/makale-02-01-insan-dunyasi-mana-ve-sanat.html`, `makale-03-17-insan-dunyasi-mana-ve-sanat.html`

## Bilimsel sayı disiplini
483 **benzersiz normalize başlık** sayısıdır, 483 özgün makale adayı sayısı değildir. `core`, `article system`, `paper` gibi başlıklar muhtemel sistem/şablon belgeleridir; araştırma sorusu ve özgün katkı görülmeden aday sayılamaz. Aynı başlık altında farklı bilimsel sorular bulunabilir; farklı başlıklar da aynı çalışmanın tekrarları olabilir.

**Sonraki adım:** Dokuz kümenin metinlerini okuyup gerçek araştırma sorusu/tez/yöntem farklarını sınıflandırmak; sonra başlığı eşleşmeyen semantik tekrarları taramak. ZAN/NEW/KOP/BEL için kesin sayı henüz yoktur. Akademik araştırma dalındaki 27 aday ayrı çapraz eşleştirme gerektirir. 412 hedefi ve yayın kilidi değişmez.
