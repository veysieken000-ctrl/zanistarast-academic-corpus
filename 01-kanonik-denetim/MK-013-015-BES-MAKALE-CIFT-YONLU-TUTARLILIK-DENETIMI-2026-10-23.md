# MK-013–015 — Beş makale çift yönlü tutarlılık denetimi

Tarih: 23 Ekim 2026. **Durum: kaynaklı masa başı mantık denetimi; bağımsız Rasterast tamamlanmadı.**

## Kapsam ve kaynak sabitleme

- Varlık Tarihi: `02-cekirdek-makaleler/VARLIK-TARIHI-01-BOYUTSAL-ACILIM-KANONIK-SENTEZ.md`, aktarım commit `4bea105fda513ca9c52cfc70273a8b0a4de180fb`.
- Jeoloji: `02-cekirdek-makaleler/JEOLOJI-01-FIZIKSEL-ZEMINDEN-BIYOLOJIK-ORTAMA-HEBUN-SENTEZI.md`, commit `12897ccdde2ef458a584153a1362db8f955761bd`.
- İnsan Tarihi: `02-cekirdek-makaleler/INSAN-TARIHI-01-AKIL-IRADELI-AHLAK-NEWROZA-KAWA.md`, commit `fbb158e80855b41f8fb9eeee5b6f18372a11263e`.
- H04: `02-cekirdek-makaleler/NK-ZS-H04-A02-TR-v03-FITRI-IMKAN-ARAC-IRADELI-AHLAK.md`, commit `1d0dd747dc45deb5403809764eb30ac1c07f2bcc`.
- H05: `02-cekirdek-makaleler/NK-ZS-H05-AKIL-FITRAT-ZEKA-BILGI-GUC-v03-KATMANLI-DUZEN.md`, commit `4ffae9c811721372428d4ef27b4b4f591a676c7b`.
- Önceki kaynaklı uygulama matrisi: `01-kanonik-denetim/MK-013-015-UYGULAMA-FIZIK-BIYOLOJI-ZIHIN-RUH-AHLAK-2026-10-23.md`.
- Test modeli: `01-kanonik-denetim/mantik_kesfi_model.py`; 64 mantık regresyon testi. CI doğrulama örnekleri: `39948494108` ve son insan tarihi değişikliği için `39949613483` (success).

## Çift yönlü aktarım kapıları

| Kaynak → hedef | Ters denetim | Aktarılabilir çekirdek | Kanıt ve çelişki kapısı | Durum |
|---|---|---|---|---|
| Varlık Tarihi → Jeoloji | Jeoloji → Varlık Tarihi | Enerji/ortam/örüntü ve önkoşul ayrımı | Yıldız/atom örgütlenmesi canlılığın zorunlu doğuşunu kanıtlamaz | KOŞULLU ANALOGY |
| Jeoloji → H04 | H04 → Jeoloji | Hazırlık ≠ mekanizma ≠ sonuç | İrade ve ahlak jeokimyasal mekanizmaya indirgenemez | KOŞULLU ANALOGY |
| H05 → İnsan Tarihi | İnsan Tarihi → H05 | Öğrenme, bellek, çıkarım, gerekçe, seçim ayrımı | Hayvan bilişi yok sayılamaz; akıl tezi deneysel olarak otomatik doğrulanmaz | İNCELEME |
| H04 → İnsan Tarihi | İnsan Tarihi → H04 | Araçla seçenek genişlemesi ve ahlaki değerlendirme ayrımı | Araç artışı → ahlaki ilerleme önermesi için karşı örnek aranır | KOŞULLU ANALOGY |
| H05 → H04 | H04 → H05 | R/I/P/C/V işlevsel profil; fiziksel ve normatif kanun ayrımı | Ruh=yazılım veya D4=kanun eşitlemesi yasak; D4 ruh/melek korunur | KANONİK SINIR |
| Varlık Tarihi → H05 | H05 → Varlık Tarihi | Fiziksel taşıyıcı ve bilgi/işlem kavramları | Fizik=yalnız güç; bilgi=yalnız biyoloji iddiası genellenemez | İNCELEME |
| Jeoloji → İnsan Tarihi | İnsan Tarihi → Jeoloji | Geçiş ve eşik varsayımı için karşı-örnek üretimi | Jeolojik ve toplumsal tarih arasında aynı nedensel yasa ileri sürülemez | KOŞULLU ANALOGY |

Bu tablo **bütün olası 10 ikilinin eksiksiz bağımsız denetimi değildir**; kaynaklı 7 aktarım hattı ve ters sorgulama yönlerini içerir.

## Denetim bulguları: yeni kanıt değil, risk sınıfları

**R-01 — İşlevsel profilin boyutlaştırılması.** `R/I/P/C/V` fizik–biyoloji–zihin–ruh–ahlak sıralaması olarak yorumlanırsa kozmik 6+Tek kanon bozulur. **Önlem:** işlev soruları ve kozmik boyutlar ayrı tablolar; insan katmanları ayrı şema.

**R-02 — Fiziksel gücün genelleştirilmesi.** H05'in watt ile ölçülen güç tanımı, “güç” sözcüğünün bütün metafizik, kurumsal ve ahlaki kullanımlarını ölçmez. **Önlem:** birim ve alan etiketleri.

**R-03 — Hazırlık/yeterlilik karışması.** Jeolojik ortam, biyolojik sonuç için yeterli olduğu gösterilmedikçe `P ⇒ O` yazılamaz. H04'te araç bulunması doğru tercih garantisi değildir. **Önlem:** `P ∧ ¬O` karşı-örnek testi.

**R-04 — Ruh/kod özdeşleştirmesi.** H05'in ruh–düzen/kanun açıklaması ile yazılım benzetmesi ontolojik ve ampirik aynı iddia değildir. **Önlem:** `ANALOGY` / `THEOLOGICAL` ayrımı; yeni kanonik iddia Müdebbir onayı gerektirir.

**R-05 — Hayvan/insan çıkarımının genellenmesi.** H05 ve İnsan Tarihi'ndeki bilişsel karşılaştırmalar görev, tür ve öğrenme bağlamı olmadan “hayvan akıl yürütemez” veya “her hayvan insanla aynı akla sahiptir” sonucunu desteklemez. **Önlem:** ölçülebilir görev ve karşıt örnek kaydı.

**R-06 — Merkez/kanun/meşruiyet karışması.** Fiziksel veya kurumsal merkez ile normatif haklılık farklı önermelerdir. **Önlem:** koordinasyon işlevinden ahlaki hükme doğrudan sıçrama engeli.

**R-07 — Eski evre anlatımının kanonlaştırılması.** Güncel kozmik D4 ruh→melekler, D5 fıtrî→iradeli ahlak, D6 hesap/hüküm→sonuç/ahiret karşılığı; eski dosyalardaki alternatif adlandırmalar tarihsel kaynak olarak tutulur, kurucu eşitlik yapılmaz.

## Yeniden kullanılabilir inceleme prosedürü

Her yeni aktarım için `MK_ID; kaynak_yol; kaynak_commit; kaynak_bölüm; hedef_yol; hedef_commit; hedef_bölüm; iddia_türü; gizli_öncül; benzer_işlev; farklı_mekanizma; karşı_örnek; kanıt_statüsü; Rasterast_durumu; kurucu_onayı` kaydı aç. Hedefte bir iddia güçlendirilirse kaynağa geri dönerek terim ve öncülleri yeniden denetle. Kaynak/kanıt eksikse **BEKLEME/İNCELEME** durumunu koru; otomatik kanonik onay veya makale sayısı artışı yapma.

## Sınır ve sonraki deney

Bu denetim, ilgili metinlere eklenen araştırma bölümlerinin karşılıklı tutarlılık sorularını listeler; bağımsız alan uzmanı değerlendirmesi, jeoloji veya tarihsel saha verisi ve gerçek verimlilik ölçümü yapılmadı. Sonraki aşama: riskleri makine tarafından denetlenebilir kaynak–hedef bağlantı envanterine dönüştürmek, değişen dosyalar için regresyon uyarısı üretmek ve gerçek insan incelemesiyle doğrulamak.

**Yayın kilidi:** 412 benzersiz makale, K0–K6, bağımsız Rasterast, kurucu Müdebbir onayı.
