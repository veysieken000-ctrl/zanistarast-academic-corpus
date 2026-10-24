# H03 / A14 — Araştırma Eki 01: Rasterast Kanıt Soyağacı ve İkinci Denetim

**Zanistarast Bilimsel Sentezi | Newroza Kawa | Türkçe | 22.10.2026**  
**Bağlı ana metin:** `NK-ZS-H03-A14-TR-v01-RASTERAST-KANIT-DENETIMI.md`  
**Statü:** Bilimsel yöntem ve kaynak denetimi eki. Tamamlanmış deney, nihai dergi makalesi veya kurucu metnin birebir aktarımı değildir.

## Öz

Bu araştırma eki Rasterast'ın, Hebûn ontolojisi ve Zanabûn epistemolojisi içinde ortaya konulan iddiaları anlamlarını değiştirmeden değerlendirmesi için bir kaynak-soyağacı modeli önerir. İddia, kurucu kaynak, editoryal yorum, mantıksal çıkarım ve ampirik kanıt ayrı kayıtlar olarak tutulur. İkinci bilenin onayı, bağımsız inceleme ile aynı kaynaktan tekrarlanan onay arasında ayrıştırılır. Hebûn'un merkez–çevre önermesi ve Zanabûn'un ikinci bilen ilkesi iki uygulama örneğidir. Yöntem, henüz gerçek araştırma verisi üzerinde geçerlenmemiştir.

## Güncel ikinci Bilen ve ahlak denetimi
Ontolojik muhataplık, epistemik ikinci Bilenin bağımsız onayı ve insanın iradeli ahlakla hüküm karşısındaki sorumluluğu farklı iddia türleridir. Fıtrî ahlak, varlık düzeninin tezahürü anlamındadır; cansız varlığa bilinçli onay atfedilmez. Rasterast kaynak soyağacı, bu üç anlamın teolojik yorum, felsefi çıkarım ve ampirik denetim olarak ayrı kaydedilmesini gerektirir.

## 1. Araştırma problemi

Bir makaledeki her önerme aynı bilgi statüsünde değildir. Kurucu ontolojik bir beyanın özgün metinde bulunması, onun laboratuvarda doğrulandığı anlamına gelmez. Bir matematiksel çıkarımın belirli aksiyomlardan geçerli olması da bu aksiyomların doğa hakkında doğru olduğunu göstermez. Rasterast, bu ayrımları gizlemek yerine denetlenebilir hale getirmelidir.

## 2. Kaynak-soyağacı kayıtları

Her iddia `claim_id` ile tanımlanır. Kaydında `source_repo`, `source_path`, `source_sha`, `source_paragraph`, `canonical_status`, `claim_kind`, `inference_steps`, `evidence_ids`, `counterevidence_ids`, `shared_dependencies`, `reviewer_independence` ve `review_status` alanları tutulur.

**İlişki türleri:** `kaynaklanır`, `yorumlar`, `destekler`, `itiraz_eder`, `yeniden_sınar`, `çevirir`. Aynı kaynak dosyasından türeyen iki metin iki bağımsız kanıt gibi sayılmaz. Eksik SHA veya paragraf, tahminle doldurulmaz; `doğrulanmadı` olarak işaretlenir.

## 3. İddia türleri

- **K:** Kurucu ontolojik, teolojik veya normatif önerme.
- **M:** Belirtilmiş öncüllerden çıkarılan mantıksal sonuç.
- **E:** Gözlem veya deneyle sınanabilecek ampirik iddia.
- **A:** Benzetme ve açıklayıcı analoji.
- **Y:** Sonraki araştırmacının editoryal yorumu.

Bu etiketler önermenin doğru veya yanlış olduğunu tek başına belirlemez; hangi doğrulama yolunun uygun olduğunu gösterir.

## 4. Örnek 1 — Hebûn

**H03-EK01-C001 [K]:** Kurucu merkez–çevre/kıble ilkesi, güneş–gezegen, kalp–kan ve anne–baba–yavru örnekleriyle açıklanır.  
**H03-EK01-C002 [E olarak okunursa]:** “Her örgütlenmiş sistemde benzersiz tek merkez vardır.”  
**Karşı-model:** Dört düğümlü çevrim grafında düğümlerin derece-merkeziliği eşittir; bu ölçüte göre tek merkez yoktur.

**Denetim sonucu:** Karşı-model, C002'nin belirli matematiksel yorumunu sınırlar. C001'in tüm ontolojik anlamlarını otomatik olarak yanlışlamaz. İddianın evrensel doğa yasası mı yoksa kurucu ilişkisel ilke mi olduğu ayrıca belirtilmelidir.

## 5. Örnek 2 — Zanabûn

**H03-EK01-C003 [K]:** Bilen öznenin bilinen nesneye yönelimi sonucu ortaya çıkan sonucun ikinci bilen tarafından onayı.  
**H03-EK01-C004 [Y]:** Bilimsel araştırmada ikinci değerlendirme bağımsız kaynak ve yöntem kullandığında kamusal gerekçelendirmeyi güçlendirebilir.  
**Karşı-örnek:** Aynı hatalı kalibrasyonla çalışan iki inceleyici mutabık kalabilir, fakat ikisi de yanılabilir.

**Denetim sonucu:** Kurucu onay kavramı korunur; salt mutabakatın deneysel doğruluğa yeterli olmadığı kaydedilir. Bu iki önerme aynı şey değildir.

## 6. İkinci denetimin bağımsızlığı

İki inceleme aynı birincil kaynağı, aynı hesaplama kodunu, aynı aygıtı veya aynı öncülü paylaşıyorsa bağımsızlık derecesi düşebilir. Rasterast kaydı, denetçilerin isimlerinden çok **kanıt zincirlerinin ayrışmasını** göstermelidir. Uyuşmazlık varsa silinmez; kaynak, yöntem ve yorum farkı ayrı açıklanır.

## 7. K0–K6 yayın kapıları

**K0:** Özgün kaynak ve kurucu sürüm.  
**K1:** Doğrudan alan literatürü, karşıt görüş ve doğru künye.  
**K2:** Tanımlar, argüman ve yöntem.  
**K3:** Kanıt, veri veya biçimsel çıkarımın yeniden denetlenmesi.  
**K4:** Alanlar arası aktarım sınırları.  
**K5:** Gerçek hedef dergi yönergesi, araştırma etiği ve beyanlar.  
**K6:** Bağımsız eleştiri, uyuşmazlıklar ve kurucu nihai onay.

## 8. Üçlü çekirdek eşlemesi

| Makale | Ana soru | Birincil kanıt sorumluluğu |
|---|---|---|
| 01 Hebûn | Varlık hangi sistem ve boyutlarla açıklanır? | Kurucu ontoloji ve kavramsal tutarlılık |
| 02 Zanabûn | Bilgi hangi ilişkide kurulur ve onaylanır? | İkinci bilen ve gerekçelendirme argümanı |
| 03 Rasterast | İddia hangi kaynak ve kanıtla savunulur? | Kaynak soy ağacı, karşı delil ve bağımsız denetim |

## 9. Sonuç ve eksikler

Rasterast, kurucu kanonu dışarıdaki bir okulun kurallarına dönüştürmek için değil, onun savlarının anlamını ve kanıt durumunu görünür kılmak için kullanılır. Bu ekin protokolü henüz gerçek bir 27-makale örnekleminde ölçülmüş değildir. Kaynak DOCX'lerin tam paragraf eşlemesi, kaynakların SHA doğrulaması, alan literatürü, resmî dergi yönergeleri ve bağımsız inceleme hâlâ gereklidir.

**Önceki çalışma:** `RASTERAST-02-KAYNAK-KANIT-BAGIMSIZLIK-DENETIM-PROTOKOLU.md`; dosya değiştirilmemiştir. **İngilizce nihai sürüm ve arşivleme yapılmadı.**


## 24 Ekim 2026 — H03 bütünleştirme kaynak kaydı

Yukarıdaki 22 Ekim eki tarihsel araştırma kaydıdır. Güncel H03 ana metni, H02'nin `350ccc54af162c22ccfe5496bba2a2265caaa588` sürümündeki §4.1'i kullanır; eski H02 §5/5A konumları güncel konum sayılmaz. Aşağıdaki kaynaklar okundu ve yöntem sentezinde karşılaştırıldı. Kaynak iddialarının hepsinin doğrulandığı anlamına gelmez.

| Depo ve sabit kaynak | Blob SHA | Kullanım ve sınır |
|---|---|---|
| [hebun-zanabun: makaleler/00-katmanli-varlık-okumasi/00_rasterast-okuma-yaklasimi.md](https://github.com/veysieken000-ctrl/hebun-zanabun/blob/3297457ec00995740f9e2c226b3713edd43266ae/makaleler/00-katmanli-varl%C4%B1k-okumasi/00_rasterast-okuma-yaklasimi.md) | `8daa9af63154c8532fa9f63d7a63430d7fbc364f` | Bağlam ve okuma; benzerlik mekanizma ispatı değildir. |
| [hebun-zanabun: makaleler/00-katmanli-varlık-okumasi/07_rasterast-metodu-ve-tanıklık-proplemi.md](https://github.com/veysieken000-ctrl/hebun-zanabun/blob/3297457ec00995740f9e2c226b3713edd43266ae/makaleler/00-katmanli-varl%C4%B1k-okumasi/07_rasterast-metodu-ve-tan%C4%B1kl%C4%B1k-proplemi.md) | `4a7a95c8b4da95d914575cc5216ff7ab73d8b793` | Tanıklık sınırı; gözlenmeme yokluk ispatı değildir. |
| [hebun-zanabun: rasterast/Rasterast-Serisi/01_Ontolojik_Sabitleme_İlkesi.md](https://github.com/veysieken000-ctrl/hebun-zanabun/blob/3297457ec00995740f9e2c226b3713edd43266ae/rasterast/Rasterast-Serisi/01_Ontolojik_Sabitleme_%C4%B0lkesi.md) | `f61388e3ae6b261d17b3cef29d458b8124c56ddd` | Ontolojik kabul ile uygulama ayrımı. |
| [hebun-zanabun: rasterast/Rasterast-Serisi/02_Epistemik_Dogrulama_ve_İki_Bilen_İlkesi.md](https://github.com/veysieken000-ctrl/hebun-zanabun/blob/3297457ec00995740f9e2c226b3713edd43266ae/rasterast/Rasterast-Serisi/02_Epistemik_Dogrulama_ve_%C4%B0ki_Bilen_%C4%B0lkesi.md) | `19c5b714d5721d90ccb17cbc00d2006dea44793f` | Onay ile bağımsız kanıt ayrımı. |
| [hebun-zanabun: rasterast/Rasterast-Serisi/03_Katmanlar_Arasi_Uyum_ve_Hiyerarsik-Tutarlilik.md](https://github.com/veysieken000-ctrl/hebun-zanabun/blob/3297457ec00995740f9e2c226b3713edd43266ae/rasterast/Rasterast-Serisi/03_Katmanlar_Arasi_Uyum_ve_Hiyerarsik-Tutarlilik.md) | `99479f5c9cc85a410820e8307e60cf2e88319d42` | Katman aktarımının sınırı. |
| [hebun-zanabun: rasterast/Rasterast-Serisi/12_6+Tek_Modelinin_Deneysel_ve_Sosyolojik_Test_Cercevesi.md](https://github.com/veysieken000-ctrl/hebun-zanabun/blob/3297457ec00995740f9e2c226b3713edd43266ae/rasterast/Rasterast-Serisi/12_6+Tek_Modelinin_Deneysel_ve_Sosyolojik_Test_Cercevesi.md) | `25606fceef28b8d322c5b22296170acc692bef73` | Sınama önerisi ile elde edilmiş bulgu ayrımı. |
| [zanistarast-ai-native-model: civilizational-knowledge/RASTERAST_DOGRULAMA_FILTRESI_SABIT_ILKELER_2026-10-15.md](https://github.com/veysieken000-ctrl/zanistarast-ai-native-model/blob/2f9cf84dc04033c6bd40ad7359d682a21d19abc0/civilizational-knowledge/RASTERAST_DOGRULAMA_FILTRESI_SABIT_ILKELER_2026-10-15.md) | `9c9b11cc75ff3db3b9aa9db8d4847701a9cf74cf` | Kaynak, bağlam, belirsizlik ve karar durumları. |
| [zanistarast-ai-native-model: core/rasterast-hallucination-filter.md](https://github.com/veysieken000-ctrl/zanistarast-ai-native-model/blob/2f9cf84dc04033c6bd40ad7359d682a21d19abc0/core/rasterast-hallucination-filter.md) | `e8e6cfd81801ada363f5e0cf56b4010a286d9b8b` | Uydurma kaynak ve sahte kesinliğin denetimi. |
| [zanistarast-ai-native-model: backend/knowledge/D0_rasterast_method.txt](https://github.com/veysieken000-ctrl/zanistarast-ai-native-model/blob/2f9cf84dc04033c6bd40ad7359d682a21d19abc0/backend/knowledge/D0_rasterast_method.txt) | `0e760f7bd3e617c64764009eac7da8434ddeb67d` | Tutarlılık dış doğruluk için yeterli değildir. |
| [zanistarast-ai-native-model: papers/L2-validation-rasterast.md](https://github.com/veysieken000-ctrl/zanistarast-ai-native-model/blob/2f9cf84dc04033c6bd40ad7359d682a21d19abc0/papers/L2-validation-rasterast.md) | `9487b8dd9857997a640f1228f10bdd22eb44f2d0` | Alanlar arası yapısal aktarımın sınırı. |
| [zanistarast-papers: docs/architecture/CANONICAL_RABUN_CORPUS_CORE_AND_RASTERAST_BOUNDARY_2026-09-17.md](https://github.com/veysieken000-ctrl/zanistarast-papers/blob/73218d1558acf1d827359c5a0a5b5ae8062e86ef/docs/architecture/CANONICAL_RABUN_CORPUS_CORE_AND_RASTERAST_BOUNDARY_2026-09-17.md) | `9ded9031ea9f44eb80ff71a4149b8ea9cf006072` | Rabûn yönetimi ile Rasterast denetiminin ayrımı. |
| [zanistarast-papers: formal-foundations/book-ii/07-rasterast-logic.md](https://github.com/veysieken000-ctrl/zanistarast-papers/blob/73218d1558acf1d827359c5a0a5b5ae8062e86ef/formal-foundations/book-ii/07-rasterast-logic.md) | `0ccc0d13fac8146ceb520e10db1aa7dda0802227` | Tanım ile gerçekleşmiş yazılım doğrulamasının ayrımı. |
| [zanistarast-papers: core-review/14-proof-audit.md](https://github.com/veysieken000-ctrl/zanistarast-papers/blob/73218d1558acf1d827359c5a0a5b5ae8062e86ef/core-review/14-proof-audit.md) | `e7c0c89124a2825f8bbde4a3285ecfd7dd9e68d1` | Öncül, çıkarım ve gizli bağımlılık denetimi. |
| [zanistarast-formal-foundations: mathematics/operators/05_RASTERAST_OPERATOR.md](https://github.com/veysieken000-ctrl/zanistarast-formal-foundations/blob/1bfb206dc8f0ad5e57bb5a75f8cae8eca90ca5fa/mathematics/operators/05_RASTERAST_OPERATOR.md) | `180d04d56c79b60887c2f5ea7df758230e293a72` | Operatör çıktı türü ve eşik uyumsuzluğu. |
| [zanistarast-formal-foundations: proofs/operators/RASTERAST_PROOFS.md](https://github.com/veysieken000-ctrl/zanistarast-formal-foundations/blob/1bfb206dc8f0ad5e57bb5a75f8cae8eca90ca5fa/proofs/operators/RASTERAST_PROOFS.md) | `0abaa2df33f3dd8991b3ae8be7d92de29c35ec46` | Tanımı tekrarlamak uygulama ispatı değildir. |
| [The-Newroza-Kawa-Civilization-Theses: arastirma/methodology/00_METHOD_RASTERAST_HISTORIOGRAPHY.md](https://github.com/veysieken000-ctrl/The-Newroza-Kawa-Civilization-Theses/blob/aea0210ef192cc1a8aa24e9293d55e095634795d/arastirma/methodology/00_METHOD_RASTERAST_HISTORIOGRAPHY.md) | `119168fdee7b11111d0365a556329b61acf5c59a` | Tarihsel merkez modeli; nedensellikte döngüsellik sınırı. |

H01 ve H05'in önceki kaynak incelemeleri, ana metnin §8'indeki örneklerde açıkça devralınır. Bu turda yeni deney, hayvan bilişi yeniden analizi veya otomatik kod çalıştırması yapılmış sayılmaz. Mevcut kaydın tekrar kullanılabilmesi için kaynak sürümü, kapsam ve hangi sonucun ona dayandığı birlikte korunur.
