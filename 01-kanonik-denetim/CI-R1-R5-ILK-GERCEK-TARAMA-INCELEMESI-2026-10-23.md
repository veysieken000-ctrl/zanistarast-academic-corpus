# R1–R5: İlk gerçek GitHub Actions taramasının incelemesi

Tarih: 23 Ekim 2026. Kaynak: GitHub Actions çalışma **39942806411**, commit **bbcc40815e5d2491aa682c3db273b3efb5729f15**, iş **120378110874**, çıktı artifact **12496488207** (`risk-uyarilari.json`). Çalışma sonucu **success**; GitHub günlükleri **11/11 unittest başarılı**, **20 Markdown makale tarandı**, **2 REVIEW_ONLY uyarısı** gösteriyor. Bu sonuçlar yalnız belirtilen commit anına aittir.

## Gerçek uyarıların elle değerlendirilmesi
| Dosya ve satır | Kural | Kanıtın bağlamı | İnceleme sonucu |
|---|---|---|---|
| A02, satır 54 | R1 | `D4` hem kozmik ruh/melek boyutu hem tarihsel zaman/sorumluluk eşiği anlamında anılıyor; metin bu ikisini **tür çakışması** olarak ayırıyor | **Koruyucu açıklama / yanlış alarm adayı**; ihlal doğrulanmadı |
| A11, satır 45 | R4 | `İki denetçi aynı hatalı rapordan beslendiğinde iki onay bağımsız kanıt sayılmaz` cümlesi bağımsızlık hatasını **reddediyor** | **Koruyucu karşı-örnek / yanlış alarm adayı**; ihlal doğrulanmadı |

Bu uyarıların ikisi de otomatik hataya veya makale reddine dönüştürülmemeli. Bağımsız Rasterast değerlendirmesi yapılmadığından inceleme durumu `CONTEXT_REVIEWED_NOT_INDEPENDENTLY_AUDITED` olarak tutulur.

## Öğrenilen teknik sınırlar
1. Tarayıcı aynı satırda anahtar sözcükleri gördüğünde, açıklayıcı/olumsuzlayıcı bağlamı ayırt etmeden uyarı oluşturuyor. `negation_or_quotation_context=true` yardımcı ama tek başına karar değil.
2. `excerpt` yalnız ilk 350 karakteri sakladığından A02'deki tam uyarı ifadesi kesiliyor. Sonraki sürümde eşleşmenin başlangıç/bitiş aralığı, tam cümle ve gerekirse bağlam penceresi kaydedilmeli.
3. Testlerin 11/11 geçmesi tüm Türkçe ifade varyantlarının yakalandığını kanıtlamaz. Özellikle yanlış negatifler için uzman etiketli örnekler gerekir.
4. Tarama 20 dış çekirdek makalesiyle sınırlı; 412 makale ve diğer depolar henüz taranmadı.
5. GitHub Actions ilk çalışması `bbcc...` commit'indeki sürümü sınadı; sonraki regex düzeltmelerinin CI sonucunu temsil etmez.

## Bir sonraki inovasyon döngüsü
- A02/R1 ve A11/R4 cümlelerini **koruyucu bağlam** regresyon örneklerine dönüştür.
- `matched_span` ve `line_excerpt` alanlarını ekle; uyarıların denetlenebilirliğini artır.
- Kural uyarısı ile doğrulanmış kanonik ihlali kesin ayır; yanlış alarm ve kaçırılan hata ölçümleri için elle etiketli küme oluştur.
- Yeni CI çalışmasıyla güncel commit'i tekrar doğrula.

Yayın kilidi ve K0–K6 açık kalır. Bu rapor makaleleri yayınlanabilir ilan etmez.
