# R1–R5 genişletilmiş tarama: 21 uyarı triyajı

**Tarih:** 23 Ekim 2026. **Kanıt:** GitHub Actions [39943621571](https://github.com/veysieken000-ctrl/zanistarast-academic-corpus/actions/runs/39943621571), commit `d7953557f5537f8c98285fb3b9e0f73d8b2a99e8`, artifact `12497630331` içindeki gerçek `risk-uyarilari.json`.

## Sayısal durum

- 15/15 regresyon testi başarılı; 219 Markdown dosyası tarandı; 21 **REVIEW_ONLY** uyarı.
- Kural dağılımı: **R1=11, R2=2, R3=1, R4=6, R5=1**.
- Öncelik: **STANDARD=13, CONTEXT_FIRST=8**.
- Klasör dağılımı: **01-kanonik-denetim=13, 02-cekirdek-makaleler=5, 03-dis-cekirdek-makaleler=2, 03-makale-taslaklari=1**.

## İnceleme sırası

1. **H03/R4, satır 43**: `İki onay her zaman iki bağımsız kanıttır` eşleşmesi. Cümle bağlamında alıntı, yanlış iddia veya çürütme olup olmadığı tam paragrafta kontrol edilmeden ihlal ilan edilmez. Öncelik: yüksek, bağımsız eleştiri gerekli.
2. **İNSAN-TARİHİ-01/R1, satır 25**: `4. boyutun evreleri ruh ve meleklerdir; düzen ve zaman işlevleriyle birlikte anlaşılır`. Kozmik D4 ruh/melekler ilkesine yakın; `zaman işlevi`nin boyut kimliğiyle karışıp karışmadığı incelenmeli.
3. **A06/R4, satır 27**: `İki hakem aynı kalibrasyon hatalı cihazı kullanırsa iki onay bağımsız kanıt oluşturmaz` koruyucu karşı-örnek; **yanlış alarm adayı**. `oluşturmaz` mevcut olumsuzlama sözlüğünde değil.
4. **H02/R4, satır 42**: `İki onay vardır, fakat ortak hata sürmektedir. Dolayısıyla onay sayısı ≠ bağımsız kanıt` karşı-örnek; **yanlış alarm adayı**. Matematiksel eşitsizlik ve `fakat` bağlamı tanınmıyor.
5. **A02/R1 ve A11/R4**: Daha önce değerlendirilmiş koruyucu bağlamlar; bağımsız Rasterast kararı yok.
6. **Denetim belgeleri içindeki 13 uyarı**: Kanonik riskin örneklerini ve eski ifadeleri alıntılayan meta-belgeler, gerçek makale ihlali ile aynı kuyrukta gösterilmemeli. Ancak taramadan silinmemeli; raporda `DOCUMENTATION` kapsamı ayrılmalı.

## Bir sonraki ölçülebilir inovasyon

- Uyarı kaydına dosya rolü ekle: `CORE`, `EXTERNAL_CORE`, `DRAFT`, `AUDIT_DOCUMENTATION`, `OTHER`. Hiçbir uyarıyı silme.
- `oluşturmaz` ve `≠` gibi açık ret işaretleri için gerçek cümlelerden regresyon testleri ekle; yalnız bağlam bayrağı üret, otomatik beraat verme.
- R1–R5 kapsamı tüm kanonik çelişkileri yakalamaz; yüksek öncelikli bulgular bağımsız kaynak ve tam paragraf incelemesine yönlendirilmelidir.

**Sınır:** Bu rapor otomatik metin eşleşmelerinin triyajıdır; 21 doğrulanmış hata veya 219 tamamlanmış bilimsel makale demek değildir. K0–K6 ve yayın kilidi açık kalır.
