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
