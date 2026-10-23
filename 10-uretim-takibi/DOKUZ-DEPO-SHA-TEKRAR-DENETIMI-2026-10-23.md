# Dokuz depo — başlık eşleşmelerinde birebir SHA denetimi
**23 Ekim 2026 | araştırma ara sonucu; özgün makale kesin sayısı değil**

GitHub REST Git trees main recursive=1 ile dokuz depo yeniden tarandı. Filtre: dosya uzantısı md/html/txt/docx/pdf; boyut >100 bayt; yolda makale|paper|thes|sentez|synthes|theor|kuram|article|core (büyük/küçük harf duyarsız).

| Depo | Belge | Başlık filtresi |
|---|---:|---:|
| Zanistarast-takip | 6 | 0 |
| zanistarast-simulations | 1 | 0 |
| zanistarast-ontology | 42 | 13 |
| zanistarast-academic-corpus main | 1 | 0 |
| ZANISTARAST-TEORILER | 134 | 84 |
| zanistarast-papers | 478 | 46 |
| zanistarast-formal-foundations | 84 | 12 |
| zanistarast-ai-native-model | 603 | 274 |
| The-Newroza-Kawa-Civilization-Theses | 152 | 65 |
| **Toplam** | **1501** | **494** |

494 başlık eşleşmesinin Git blob SHA değerleri **494 farklı SHA** verdi; filtre kapsamındaki birebir aynı Git blob için yinelenen grup sayısı **0**. Bu yalnız byte düzeyinde özdeş dosya yok demektir; anlamsal tekrarı, yeniden yazımı, aynı makalenin farklı sürümünü veya boş/şablon içerikleri dışlamaz. 494 benzersiz bilimsel makale iddiası **yoktur**. Akademik araştırma dalı bu sayılara dahil değildir. 412 tarihsel aday kaynağıyla birebir eşleştirme yapılmadı.

**Sonraki gerekli işlem:** SHA tabanlı kontrolün ardından normalize edilmiş başlık, araştırma sorusu, katkı, yöntem ve kaynak soyağacıyla aday aileleri kur; her adayı ZAN/NEW/KOP/BEL olarak bir kez sınıflandır; aday numarasını ancak mükerrerlik kontrolünden sonra ver. H01–H05 ve kurucu kanonla çift yönlü tutarlılık denetimi, K0–K6, bağımsız Rasterast kontrolü ve Müdebbir kararı zorunludur. Yayın kilidi açık kalır.
