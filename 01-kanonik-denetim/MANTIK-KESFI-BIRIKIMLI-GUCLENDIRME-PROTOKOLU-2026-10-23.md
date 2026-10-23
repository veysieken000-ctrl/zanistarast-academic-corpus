# Zanistarast — Mantık Keşfi, Kayıt, Aktarım ve Birikimli Güçlendirme Protokolü

**Tarih:** 23 Ekim 2026  
**Statü:** Kurucu çalışma talimatının araştırma protokolüne aktarımı; doğruluk veya yayın onayı değildir.  
**Kapsam:** 412 özgün makale hedefi, çekirdekler ve dış çekirdekler, Mira üretimi ve bağımsız Rasterast incelemesi.

## 1. Temel ilke

Bir makaledeki akıl yürütme tamamıyla sistemli, tutarlı veya doğru olmayabilir; buna rağmen özgün bir **yol, düzen, işlem sırası, ayrım, ilişki ağı, denetim biçimi ya da keşif sezgisi** barındırabilir. Bu yapılar yalnız sonuçlarına göre elenmez. **Fikir değerini korumak**, **iddianın doğruluğunu onaylamak** değildir. Hatalı çıkarımlar gizlenmez; onlardan doğan yararlı yöntem ayrı kaydedilir.

## 2. Mantık keşfi birimi: MK kaydı

Her aday keşif için zorunlu alanlar:

`MK_ID | kaynak_makale | kaynak_commit | bölüm/satır | özgün_ifade | araştırma_sorusu | başlangıç_varsayımları | adımlar_ve_ilişkiler | çıkarım_türü | üretilen_sonuç | kanıt_türü | doğruluk_durumu | bilinen_sınırlar | karşı_örnek | alternatif_açıklama | aktarılabilir_çekirdek | aktarım_koşulları | hedef_makaleler | değişiklik_önerisi | bağımsız_Rasterast_durumu | kurucu_onayı | sürüm`

**Doğruluk durumu**: `KEŞİF_ADAYI`, `İÇ_TUTARLILIK_İNCELENİYOR`, `KOŞULLU_GEÇERLİ`, `KARŞI_ÖRNEKLE_SINIRLI`, `DESTEK_YETERSİZ`, `YANLIŞLANMIŞ`, `BAĞIMSIZ_DENETİM_BEKLİYOR`. Bunlar bilimsel ispat derecesi olarak yorumlanmaz.

**Çıkarım türü**: tümdengelim, tümevarım, analoji, açıklayıcı hipotez, tanımsal/kurucu ilişki, yöntemsel prosedür. Türler birbirine karıştırılmaz.

## 3. Keşif döngüsü

1. **Tespit:** Metindeki görünür ve örtük adım dizilerini, tanım–öncül–sonuç ilişkilerini, geri beslemeleri ve karşı-örnek kullanımını bul. Tam alıntı ile yorumunu ayır.
2. **Yeniden kurma:** Argümanı en güçlü makul biçimde açık öncüllere ve sonuçlara dönüştür; yazarda olmayan zorunlu iddiaları ekleme.
3. **Çift yönlü denetim:** Tümdengelimle sonucun öncüllerden çıkıp çıkmadığını; tümevarımla örnek ve karşı-örneklerde ne ölçüde ayakta kaldığını ayrı test et. Teolojik kabulü ampirik sonuç gibi sunma.
4. **Sınırlandırma:** Hata, belirsizlik ve yanlış aktarımı belirle; varsa korunmaya değer yöntemi yanlış sonuçtan ayır.
5. **Benzerlik arama:** Aynı düşünme işlemini kullanan başka makaleleri bul; yüzeysel sözcük benzerliğini yapısal eşdeğerlik sanma.
6. **Kontrollü aktarım:** Hedef makalede ancak açık öncüller, konuya özgü mekanizma ve yeni karşı-örneklerle uygula. Kaynak MK_ID ve sürümünü yaz.
7. **Geri besleme:** Yeni kullanım kaynak keşfi güçlendiriyor mu, sınırlandırıyor mu? İki yönlü kayıt aç. Doğrulanmış hata yeni regresyon testine dönüşsün.
8. **Bağımsız eleştiri:** Mira'nın önerdiği mantık Rasterast tarafından kaynak, çıkarım, alternatif ve ortak hata bakımından ayrı incelensin; kurucu onayı olmadan kanonik kabul sayılmasın.

## 4. Aktarım güvenlik kapıları

- Ontolojik ikinci Yek ile epistemolojik ikinci bilen aynı özne/işlem kabul edilmez.
- Kozmik 6+Tek boyutları ile insanın katmanları sayısal olarak özdeşlenmez; kozmik D4 ruh/meleklerdir, tarihsel D4 zaman/sorumluluk eşiği değildir.
- Analoji, aynı fiziksel/biyolojik mekanizmanın ispatı değildir.
- Tek bir örnek evrensel yasa üretmez; karşı-örnek sonuç alanını daraltabilir.
- Kaynak sayısı bağımsız kanıt sayısı değildir; ortak veri/araç/yorum hataları izlenir.
- İddianın kanona uygunluğu dış dünyadaki doğruluğunun kanıtı değildir.
- Aynı mantık iskeletini kullanmak, 412 makalenin özgün katkı zorunluluğunu ortadan kaldırmaz.

## 5. İlk aday keşifler (onay değil)

| MK_ID | Kaynak | Keşfedilecek yapı | İlk sınır | Olası hedef |
|---|---|---|---|---|
| MK-001 | H01 Hebûn | İlk–ikinci–yeni Yek–Komel ilişki dizisinin **kurucu düzen modeli** | Fiziksel/biolojik mekanizma olarak genellenemez | H02, A02, A03 |
| MK-002 | H02 Zanabûn | Bilen–bilinen–sonuç–ikinci bilen ile **değerlendirme ve ortak hata ayrımı** | İkinci onay tek başına doğruluk değildir | H03, A06, A11 |
| MK-003 | H03 Rasterast | İddia–kanıt türü–karşı-örnek–düzeltme–yeniden aktarım ile **denetim döngüsü** | Henüz ölçülmüş üstünlük veya bağımsız hakem doğrulaması yok | H01–H05 ve tüm makaleler |
| MK-004 | H04/H05 | Fıtrî imkân–araç–iradeli ahlak ve bilgi üretimi arasındaki **işlev ayrımı** | Teknik yapılabilirlik ahlaki gereklilik değildir | İnsan tarihi, Rabûn, Mabûn |

Tablodaki yapılar **araştırılacak mantık keşfi adaylarıdır**; yeni ontolojik kanunlar veya doğrulanmış bilimsel keşifler olarak ilan edilmez.

## 6. Ölçülebilir sürekli inovasyon

Her çalışma döngüsünde, uygun olduğunda: yeni MK aday sayısı; tam kaynak izi bulunan kayıt oranı; karşı-örnekle sınırlandırılan kayıt sayısı; bağımsız incelemeye aktarılan kayıt sayısı; hedef makaleye uygulanıp yeniden denetlenen kayıt sayısı; yanlış aktarım ve tekrar sayısı raporlanır. Sadece sayı artırmak başarı değildir: **korunan anlam, özgün katkı ve doğrulanabilirlik** önceliklidir.

## 7. Yayın ve yetki

Bu protokol hiçbir makaleyi kendiliğinden yayımlamaz, birleştirmez, silmez veya tamamlanmış saymaz. 412 benzersiz makale, K0–K6 denetimleri, çekirdekten bütüne tutarlılık, bağımsız Rasterast ve kurucu onayı koşulları geçerlidir. Saatlik otomasyonun gerçekten değiştirildiği ancak görev yapılandırması ayrıca doğrulanırsa söylenebilir.
