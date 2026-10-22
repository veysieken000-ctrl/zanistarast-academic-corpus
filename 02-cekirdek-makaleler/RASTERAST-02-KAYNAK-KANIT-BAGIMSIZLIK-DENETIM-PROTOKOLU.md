# RASTERAST-02 — Zanistarast makalelerinde kaynak, kanıt ve bağımsızlık denetimi: Uygulanabilir araştırma protokolü

**Araştırma yöntemi makalesi · 22 Ekim 2026 · Sürüm 1.0 · Hakemli yayına hazır değil**

## Öz
Bu makale Zanabûn'ün ikinci bilen ilkesinin epistemik uygulaması ile Rasterast'ın iddia denetimi işlevini, Zanistarast akademik külliyatı için uygulanabilir bir kayıt protokolüne dönüştürür. Önceki AKIL-03 ikinci bilenin ontolojik muhataplık ve bağımsız değerlendirme düzlemlerini; BİLİM-01 ise iddia türü, dayanak ve denetim statüsünü ayırır. Bu çalışmanın ayrı katkı adayı, **her araştırma iddiasını kaynak kimliği, gerekçe zinciri, karşı-delil, ortak hata ve yeniden değerlendirme sonucu ile izlemeyi sağlayan kayıt şeması**dır. Şema henüz yazılımda uygulanmış veya ampirik olarak doğrulanmış değildir.

## 1. Dayanaklar ve sınır
Birincil araştırma izleri: `AKIL-03-IKINCI-BILEN-ORTAK-ZEMIN-BAGIMSIZ-DOGRULAMA.md` ve `BILIM-01-EPISTEMIK-STATU-VE-KANIT-MATRISI.md` (akademik depodaki önceki çalışmalar). Özgün belgeler `2-Akıl ve bilginin varlığı (2).docx` ve `6-Bilim (1).docx` olarak belirtilmiştir. Bu turda DOCX dosyalarının tam paragraf eşlemesi yapılmadığından bu makaledeki tablo ve kurallar **araştırmacı tarafından önerilen yöntemdir**, kurucunun metninden doğrudan alıntı değildir.

## 2. Ontolojik ilke ile deneysel kontrolün ayrılması
Hebûn ontolojik varlık temelidir. Zanabûn epistemolojisi varlığa yönelen bilenin bilgi adayı üretmesini ve ikinci bilenin gerekçeli değerlendirmesini araştırır. İkinci bilenin ontolojik muhataplık anlamı, laboratuvar hakemi veya iki kişinin aynı fikre katılmasıyla özdeş değildir. Rasterast kaynak, tutarlılık, kanıt ve karşı-delil bakımından bir iddianın durumunu inceler. Bu yöntem bilimsel gözlemle teolojik önermeyi aynı doğrulama sınıfına koymaz.

## 3. Önerilen iddia kayıt şeması
| Alan | Açıklama | Örnek |
|---|---|---|
| claim_id | Tekil önerme kimliği | RST-C-001 |
| source_id | Belge, sürüm, paragraf/satır izi | DOCX-06 §24 |
| claim_text | Kapsamı belirli tek cümlelik önerme | “İkinci inceleme hata bulma oranını artırabilir” |
| claim_type | Ontolojik / teolojik / kavramsal / normatif / analojik / matematiksel / ampirik | Ampirik hipotez |
| evidence | Gözlem, veri, argüman veya kaynak metni | Veri bekliyor |
| reviewer_1 | İlk değerlendiricinin gerekçesi ve kaynağı | Metin analizi |
| reviewer_2 | Bağımsız değerlendiricinin gerekçesi ve kaynağı | Henüz yok |
| shared_dependency | Ortak veri, yöntem veya otorite bağımlılığı | Aynı DOCX |
| counterevidence | Karşı örnek veya çelişen kaynak | Henüz aranmadı |
| disposition | Açık, destekli, çelişkili, reddedildi gibi **öneri etiketleri** | Açık |
| next_test | Sonraki somut sınama | Kör ikinci okuma |

Buradaki örnek belge/paragraf kimlikleri **temsili**dir, gerçekten doğrulanmış kaynak satırları değildir. Statü etiketleri Mira yazılımının resmî enum değerleri olarak ileri sürülmez.

## 4. Kalite kapıları ve başarısızlık koşulları
**K0 Kaynak:** Özgün metnin gerçekten mevcut olması, iddianın bağlamıyla eşleşmesi ve sürümünün kaydı. **K1 Literatür:** Destekleyici ve karşıt hakemli çalışmaların aranması. **K2 Yöntem:** Sorunun, değişkenlerin ve alternatif açıklamaların önceden açıklanması. **K3 Bulgular:** Veri, hesaplama veya argüman zincirinin yeniden incelenebilir olması. **K4 Geçerlik:** Bulguların kapsam sınırı ve başka koşullara aktarılabilirliği. **K5 Etik:** Haklar, çıkar çatışması, araştırma etiği ve zarar riski. **K6 Bağımsız değerlendirme:** İlk çalışmadan ayrı okuyucu veya yöntemle kontrol ve uyuşmazlık kaydı.

**Başarısızlık örnekleri:** Kaynakta bulunmayan ifadeyi kurucuya atfetmek; ontolojik analojiyi ampirik yasa saymak; iki değerlendiricinin aynı hatalı kaynağa bağımlılığını gizlemek; çelişen sonuçları çıkarmak; yayın kararı alınmadan “yayına hazır” işaretlemek.

## 5. Araştırma uygulaması: dört örnek iddia
**A — Biyoloji evreleri:** “İkinci kozmik boyutun evreleri tek hücreli ve çok hücrelidir.” Güncel kurucu kanonik; tarihsel eşeysiz/eşeyli metinlerle farkı kaydedilir. Bu, evrimsel biyolojide evrensel bir fizik yasası kanıtı değildir.

**B — Dördüncü boyut:** “Ruh ve melekler iki evredir; düzen ve zaman işlevdir.” Güncel kurucu ontolojik-teolojik tanım; düzen/zaman ifadesi yanlış diye silinmez. Ruhun ayrılmasıyla bireysel yaşamın sona ermesi ve meleklerin ruhlarının alınmasıyla kozmik düzenin sona ermesi, kurucu teolojik açıklamadır.

**C — İkinci bilen:** “Bağımsız ikinci değerlendirme ortak hataları azaltabilir.” Ampirik hipotezdir. Kör inceleme ile aynı kaynağa dayalı incelemenin hata oranları karşılaştırılabilir; deney henüz yapılmamıştır.

**D — Mabûn:** “Mabûn Ekonomi Modeli kaynak erişimini iyileştirir.” Test gerektiren kurumsal hipotezdir. Model adı kanoniktir, olumlu ekonomik sonuç henüz ölçülmemiştir.

## 6. Tekrar üretilebilir inceleme deneyi
Aynı iddia kümesi için üç inceleme koşulu önerilir: (A) ikinci değerlendirici birincinin sonucunu görür; (B) ikinci değerlendirici kör okuma yapar; (C) ikinci değerlendirici farklı kaynak veya ölçüm aracı kullanır. Önceden tanımlanacak ölçütler yanlış onay oranı, karşı örnek bulma oranı, uyuşmazlık ve inceleme süresidir. Hipotez: Kör ve bağımsız inceleme, bazı hata türlerini azaltabilir. Örneklem, güç analizi, etik izin, veri toplama ve sonuçlar henüz yoktur.

## 7. Akademik karşılaştırma
Reiss ve Sprenger, “Scientific Objectivity”, *Stanford Encyclopedia of Philosophy*: https://plato.stanford.edu/entries/scientific-objectivity/ . “Scientific Method”: https://plato.stanford.edu/entries/scientific-method/ . “Epistemological Problems of Testimony”: https://plato.stanford.edu/entries/testimony-episprob/ . Bu kaynaklar Zanistarast'ın ontolojik tezlerini doğrulamaz; bilimsel nesnellik, yöntem ve tanıklığın epistemik sınırları için karşılaştırma sağlar. Ayrıntılı bibliyografya ve kaynak doğrulaması açık iştir.

## 8. Külliyata uygulanacak iş akışı
1. Her makalede özgün kaynakların ve sürümlerin kimliğini belirt.
2. Her ana sav için ayrı `claim_id` ve iddia türü kaydet.
3. Özgün kaynak, araştırmacı yorumu ve önerilen yeni kuralı ayır.
4. Karşıt kaynak ve olası çürütücü örnekleri açıkça yaz.
5. İkinci okuyucunun bağımsızlık koşulunu ve ortak veri bağımlılığını kaydet.
6. K0–K6 kalite kapılarını kanıt olmadan tamamlandı sayma.
7. Yayın veya gönderim kararını yetkili Müdebbir onayına bırak.

Bu iş akışı henüz bütün depolarda otomatik uygulanmış değildir.

## 9. Sonuç
Rasterast'ın kaynak ve kanıt denetimini bir araştırma şemasına dönüştürmek, Zanistarast makalelerinde kurucu kanonik ile araştırmacı yorumu arasındaki sınırı daha görünür kılabilir. Yöntemin başarısı bağımsız karşılaştırma ile ölçülmelidir. Bu metin özgün kurucu kaynakların yerine geçmez ve **yayıma hazır değildir**.

## Kaynakça
- `AKIL-03-IKINCI-BILEN-ORTAK-ZEMIN-BAGIMSIZ-DOGRULAMA.md`, akademik depo.
- `BILIM-01-EPISTEMIK-STATU-VE-KANIT-MATRISI.md`, akademik depo.
- `2-Akıl ve bilginin varlığı (2).docx`, özgün belge; paragraf eşlemesi açık.
- `6-Bilim (1).docx`, özgün belge; paragraf eşlemesi açık.
- Reiss & Sprenger, “Scientific Objectivity”, SEP.
- “Scientific Method”, SEP.
- “Epistemological Problems of Testimony”, SEP.
