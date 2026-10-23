# Matematiksel sembol–anlam–kanıt matrisi (v0.1)
23 Ekim 2026. Kaynaklar: ZANISTARAST-TEORILER/main `04_BOYUTSAL_ACILIMIN_MATEMATİKSEL_ILKESI.md` (SHA 8a4f4ba2fd52613db8a65da6fbf30d0a8c4bd554), `05_BOYUTSAL_ACILIMIN_RESET_MEKANIZMASI.md` (cd77d4c285cd224de0ce6b47786c6e3e21591f59), `06_UST_BOYUTUN_ZORUNLULUGU.md` (faee786e8ddaf4913a6c5eebde949d3177a2bf32), `08_INSAN_3_VE_5_BOYUT_VARLIGI_POTANSIYELE_SAHIP_.md` (34d20c0b78a3c4ae897e1f540a71a33a20d9ef3c), `01_TIME_THEORY_RASTERAST_ZANISTARAST.md` (25665ac5f24f16d96ad1928355ab1fc29e8f9098); Mira `formal_foundation.rs` (43a70458d416547162ac49236d7bdf02ebf64c11). Bu matriste önerilen işaretler yeni kanonik aksiyom değildir.

## Tür sistemi
- **COSMIC_DIMENSION**: kâinatın boyutu; **BEING_LAYER**: belirli bir varlığın katmanı; **DEVELOPMENT_STAGE**: varlığın gelişim/sorumluluk aşaması; **SYSTEM_STATE**: belirli sistemin ölçülen durumu; **EVIDENCE_STATUS**: iddia ve kanıtın denetim durumu.
- Aynı `D4` işaretini hem COSMIC_DIMENSION (güncel kanonda ruh/melekler) hem DEVELOPMENT_STAGE (eski metindeki zaman/sorumluluk eşiği) için kullanmak tür çakışmasıdır. Eski metni sessizce düzeltmek yerine kaynakla işaretle; yeni simge ancak Müdebbir onayıyla kanonikleşir.
- Bir denetim filtresi `F: (iddia, kanıt, ölçüt) → karar` türündedir; bir ontolojik zaman modeli veya Zanistarast kuramsal yaklaşımı aynı fonksiyon değildir.

## Kaynaklı sembol tablosu
| Kaynak gösterimi | Geçici tür | Tanım/birim durumu | Matematiksel açık | Kanıt durumu ve sonraki test |
|---|---|---|---|---|
| `K` karmaşıklık | SYSTEM_STATE | Operasyonel tanım ve birim yok | Örneklem, ölçek, ölçüm hatası eksik | Hipotez; somut karmaşıklık metriği belirle |
| `T` taşıma sınırı | SYSTEM_STATE | Kapasitenin birimi belirsiz | `T=0` ve `T<0` ele alınmamış | Hipotez; fiziksel anlam ve tanım kümesi belirle |
| `D` düzen kapasitesi | SYSTEM_STATE | `T` ile özdeşliği gösterilmedi | `K>D` ile `K>T` eşdeğer sayılamaz | Hipotez; iki kapasiteyi ayrı tanımla |
| `K/T` | SYSTEM_STATE → oran | Ancak K,T karşılaştırılabilir birimde ve T sıfır değilse anlamlı | Eşik `>=1` yeni boyut doğumunu mantıksal olarak ispatlamaz | Açılım hipotezi; karşı örnek üret |
| `K >> T` | SYSTEM_STATE → ilişki | `>>` nicel eşik değil, belirsiz güçlü büyüklük gösterimi | `>>` için sabit veya asimptotik anlam seçilmeli | Reset hipotezi; eşik aralığı ve duyarlılık testi |
| `B(n+1)=f(K/T)` | COSMIC_DIMENSION? / SYSTEM_STATE? | `B` ve `f` tanımsız | İndeks, değer kümesi, zaman ve geçiş ölçütü eksik | Karar bekliyor; boyut ile katman ayrımı zorunlu |
| `D1,D2,D3,D4,D5` | COSMIC_DIMENSION / DEVELOPMENT_STAGE karışık | Eski insan metninde D4 sorumluluk eşiği | Güncel kozmik D4 ruh/melekler; insan katmanları sayı eşleniği değil | Terminoloji çakışması; kaynak korunacak |
| `Reset` | SYSTEM_STATE → SYSTEM_STATE | Ölçülen önce/sonra durumu yok | Açılım, stabilizasyon ve resetin koşulları çakışıyor | Ayrı geçiş modeli öner |
| `Etkileşim + Denge Arayışı = Zaman` | Ontolojik önerme | Toplama işlemi ve birimler yok | Matematiksel eşitlik değil; şu an açıklayıcı metafor | Zaman kuramı adayı; boyut ve katman etkileşimini ayır |
| `FormalProof::Verified` | EVIDENCE_STATUS | Rust durum etiketi | Durum atama ≠ biçimsel ispat ≠ ampirik doğruluk | Kod testi ve bağımsız ispat kontrolü ayrı |

## Asgari tutarlılık karşı örneği
Aynı sistem için `K=12`, `T=10`, `D=11` varsayalım. `K/T=1.2>=1` ve `K>D` sağlanır. Eski ifadeler hem açılımı hem reset olasılığını öngörebilir; yalnız eşitsizliklerden hangisinin gerçekleşeceği belirlenemez. Bu **varsayımsal sayısal örnek**, gerçek kozmik ölçüm veya çelişki ispatı değildir. Ek geçiş koşulları gereklidir.

## Mira'ya devredilebilir denetim şablonu
Her denklem/iddia için `source_repo`, `source_path`, `source_sha`, `symbol`, `domain_type`, `input_unit`, `output_unit`, `assumptions`, `counterexample`, `evidence_kind`, `audit_status`, `rename_proposal`, `founder_decision` alanları aç. Belirsiz türde `KARAR-BEKLIYOR` tut. Eski kaynak silinmez, özgün ama eksik aday birleştirilmez.

## Açık işler
K ve T için fiziksel veya bilgi-kuramsal ölçü seçimi; geçiş fonksiyonunun tanımı; tür denetimli denklem seti; zaman teorisindeki Rasterast yaklaşımı kullanımının bağlamlı taraması; Rust kodunun gerçek derleme ve ispat denetimi; bağımsız Rasterast ve K0–K6 incelemesi. 412 özgün makale hedefi ve yayın kilidi sürer.
