# A02, A03, A10, A11 ile H01–H05 çapraz tutarlılık denetimi

23 Ekim 2026. Araştırma dalında beş çekirdek metnin içerikleri ve dört dış çekirdek metnin son sürümleri karşılaştırıldı. Çekirdek kaynak blob SHA'ları: H01 `691ea95d550ad221bacc55fa50008232cc31bb86`; H02 `f6976f89a73c2c56ede63387d305b8649baf1b51`; H03 `0a1d2ac3e68a3d59b7b22d5c3517f232ff4264e6`; H04 `93627510bc8dd0694b22e2de481d510da6d0f25c`; H05 `830c2d563a71cb6569958f90a188f870bbfe83f4`. Bu, kaynaklı kavramsal incelemedir; bağımsız hakemlik veya otomatik kanıt denetimi değildir.

## Çapraz bağımlılık matrisi
| Dış çekirdek | H01 ontoloji | H02 Zanabûn | H03 Rasterast | H04 kozmik/fıtrî ahlak | H05 akıl/bilgi | Ayırıcı özgün çıktı |
|---|---|---|---|---|---|---|
| A02 | Yek/Komel, Ehad yaratılmış boyut değil | Ontolojik ikinci Yek ≠ epistemik ikinci bilen | Kanıt türü ve kategori hatası | 6+Tek, D4 ruh/melek, D5 geniş ahlak | İnsan katmanları ≠ kozmik boyut numaraları | Boyutlar arası kategori hatası testleri |
| A03 | Yek kimliği ≠ merkez konumu | Epistemik referans ≠ geometrik merkez | Analojinin kaynak ve sınır denetimi | Farklı boyutlarda mekanizma aktarım sınırı | Bilgi üretimi ≠ tek fiziksel merkez | Analojinin geçerlilik/bozulma koşulları |
| A10 | Yek–Komel ≠ otomatik siyasal meşruiyet | Gerekçe ve ikinci değerlendirme | Karar öncesi/sırası/sonrası denetim | İradeli ahlak ve normatif sorumluluk | Bilgi kapasitesi ≠ ahlaken iyi karar | Gerekçeli yetkinin normatif koşulları |
| A11 | Ontolojik birlik ≠ merkezî otorite | İkinci onayın bağımsızlığı | Ortak kaynak, hata ve geri besleme | Fıtrî/iradeli ahlak ayrımı korunmalı | Bilgi üretimi ≠ bilgi kanalı erişimi | Temsil, bilgi akışı ve denetim grafı |

## Gözlenen uyumlar
1. H01 ve H02 ontolojik ikinci Yek ile epistemik ikinci bileni ayırır. A02/A03/A10/A11 bu rolleri aynı aktör ya da aynı mekanizma saymıyor.
2. H04 ve H05, insanın iç katmanları ile kozmik 6+Tek boyutlarının numara numara özdeş olmadığını açıkça söyler. A02'nin yeni `COSMIC_DIMENSION` / `BEING_LAYER` / `DEVELOPMENT_STAGE` türleri bu ayrımı korur.
3. H03, Rasterast'ı kaynak soyağacı, ortak hata ve bağımsız denetim olarak ele alır. A11'in ortak kaynaktan gelen iki onayı bağımsız saymaması H03 ile uyumludur.
4. H04 ve H05, araç/bilgi kapasitesinin otomatik olarak güzel ahlak doğurmadığını söyler. A10'un bilgi veya prosedür kalitesini normatif meşruiyetle özdeşleştirmemesi bu ayrımla uyumludur.

## Açık riskler ve engelleme kuralları
- **R1:** Eski `D4 = zaman/sorumluluk eşiği` kullanımı güncel kozmik `D4 = ruh/melekler` ile çakışıyor. A02 tür denetimi uygulanmadan eski metin doğrudan çekirdeğe aktarılmaz.
- **R2:** A03'ün merkez analojisi H01'in ilk Yek ontolojisine fiziksel merkez kanıtı olarak eklenemez.
- **R3:** A10'daki `P=Y∧G∧H∧I∧D` aday prosedür koşulu H04'teki iradeli ahlak veya teolojik hüküm için matematiksel yeterlilik ispatı sayılamaz.
- **R4:** A11'in ağdaki `reach`, `appeal` ve `latency` ölçümleri H02'nin epistemik ikinci bilen onayının yerini otomatik almaz; erişim, bağımsızlık ve doğruluk farklı özelliklerdir.
- **R5:** H03'ün kapsamlı Rasterast denetimi yalnız tek bir ikili filtreden ibaret gösterilmemeli; süreç, kaynak ve ortak hata bileşenleri korunmalıdır.

## Sonuç ve devredilecek işler
Bu örneklemde **doğrudan yeni bir çekirdek çelişkisi tespit edilmedi**; bununla birlikte beş risk için uygulama ve kaynak denetimi açıktır. Bu ifade 412 makalenin tamamının tutarlı olduğunu veya K0–K6'nın kapandığını söylemez. Dört makale `BAGIMSIZ-EKSIK` statüsünü korur. Sonraki adım R1–R5 için makinece okunabilir kontrol kayıtları, özgün DOCX paragraf izi ve bağımsız Rasterast eleştirisidir. Yayın kilidi korunur.
