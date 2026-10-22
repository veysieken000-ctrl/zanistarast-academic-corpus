# H01–H05 çekirdek hızlandırma ve kalite matrisi

**Tarih:** 22 Ekim 2026. **Kapsam:** GitHub'daki beş çekirdek makalenin gerçek metinlerinden yapılan ilk yapısal tarama. **Statü:** Açık kalite kapısı; yayıma hazır değil. Bu kayıt 412 makale sayısına eklenmez.

## Güncel kurucu talimat: bilimsel tanımlara sadakat
**22 Ekim 2026:** “Bilim insanları yani bilimde nasıl tanımlıysa öyle olacak bitti.” Bu talimat uyarınca bilimsel terimin ilgili alan kaynağındaki anlamı esas alınır. Kurucu felsefi veya teolojik kullanımlar ayrıca etiketlenir; bilimsel tanımı değiştiren bulgu sayılmaz. Birden çok bilimsel kullanım varsa alan ve operasyonel tanım belirtilir.

Bu tur H05 §1'de fiziksel güç tanımı düzeltildi; §6'daki fiziksel koşul alanı C_f olarak gösterilerek fiziksel güç P ile karışması önlendi. Önceki P gösterimi tarihsel sürümlerde korunur; gösterim değişikliği yeni ampirik model değildir. H04 §3A'daki kuvvet oranı/güç ayrımı ve H03'teki terim denetimi buna göre güncellendi. H02'de fiziksel düzen ile epistemik onay benzetmesinin ayrımı korundu.

| ID | Dar denetim | Doğrudan kaynak yeri | Sonuç |
|---|---|---|---|
| E37 | Fiziksel güç iş/enerji aktarımının zamana oranıdır | OpenStax College Physics 2e §7.7, What is Power?, denklem 7.69 | H05 §1 tanımı düzeltildi; H04'e geri beslendi |
| E38 | Gücün SI birimi watt; 1 W = 1 J/s | Aynı bölüm, denklem 7.69 sonrası birim açıklaması | Teknik birim H05'e işlendi; genel eylem kapasitesine uygulanmadı |

Bu iki kaynak kontrolü tanım içindir; kurucu beşli çerçevenin veya bütün bilimsel önermelerin doğrulandığı anlamına gelmez. Yeni deney, bağımsız hakem sonucu veya yayın onayı kaydedilmedi.

## Güncel dar kapsamlı kontrol sonucu — 22 Ekim 2026

Bu bölüm önceki tarihsel ölçümlerin yerine güncel durumu okumak içindir. “Yeşil” yalnız adı verilen kontrolün geçtiğini gösterir; makale doğruluğunun tümünü veya yayın iznini göstermez.

| Denetim | Durum | Kanıt / sınır |
|---|---|---|
| Dal ve sürüm tabanı | Yeşil | Son turun tabanı 33e0e974b19638aa19dbccc4669c0033b83683cd; değişiklikler bu beş ana metin üzerinde |
| Yapısal bütünlük | Yeşil | Beşinde öz, anahtar sözcük, yöntem, sonuç ve dış kaynakça mevcut |
| Yerel Markdown kaynak yolları | Yeşil | 27 açık dosya yolu mevcut Git ağacında bulundu; özgün Word içeriğini bu kontrol sınamaz |
| Tablo sütunları | Yeşil | Ana metinlerin bitişik tablo satırlarında sütun sayısı uyuşmazlığı bulunmadı |
| Atıf aktarımındaki belirli bulgular | Yeşil | H01 NIDC kaynakçası tamamlandı; H03 R-H01-02 eski iş durumu düzeltildi |
| Kavramsal geri beslemedeki belirli bulgular | Yeşil | H02 hücre tablosu H01 §6 ile eşlendi; bağımsızlık yanılmazlık sayılmadı; H04 eylem/erdem, H05 yenilik/bilgi ayrıldı |
| Bütün atomik iddiaların bilimsel ve felsefi denetimi | Açık | Blok kapsamı ve ana önerme haritaları bu ölçütün tamamı değildir |
| Bağımsız ikinci alan/argüman denetimi | Açık | Bu kayıt aynı çalışma akışınca hazırlandı; dış değerlendirme sonucu yok |
| Bütünsel Halka 0 kapanışı | Yeşil değil | Önceki iki açık ölçüt kapanmadan dış çekirdek üretimine geçilmez |
| 412 makale yayın kapısı | Kapalı | Bütün envanter, bütünsel uyum ve kurucu nihai onayı koşulları korunur |

### Son sürüm ölçümü
| Makale | Karakter | Benzersiz DOI | Açık yerel dosya yolu hatası |
|---|---:|---:|---:|
| H01 | 25703 | 4 | 0 |
| H02 | 18120 | 1 | 0 |
| H03 | 20938 | 4 | 0 |
| H04 | 14334 | 0 | 0 |
| H05 | 25477 | 5 | 0 |

Karakter sayısı JavaScript metin uzunluğu; DOI sayısı metin örüntüsünün tekilleştirilmesidir. DOI sayısı kanıt gücü değildir. Yerel yol kontrolü Git ağacıyla karşılaştırmadır; dış URL'lerin tamamının şu anda açıldığını iddia etmez.

### Kapanışı bekleyen somut iddia soruları
Bu sorular makalelerin açık araştırma konularından ayrı olarak, mevcut metnin gerekçelendirme yeterliliğinin denetimi içindir. Her yanıt iddia, kaynak yeri/öncül, karşı-örnek, karar ve gerekiyorsa diğer dört metne düzeltme alanlarıyla kaydedilmelidir.

| Kimlik | Denetlenecek yer | Karar verilmesi gereken soru | Beklenen kayıt |
|---|---|---|---|
| D01 | H01 §§4–6, 10A | Komel'in önerilen örgütlenme ölçütleri, verilen fizik ve biyoloji örneklerinde kapsamı aşan çıkarımı gerçekten engelliyor mu? | Örnek bazında mekanizma ve kimlik sınırı; bağımsız alan görüşü |
| D02 | H02 §§2–5C, 7B | Kurucu onay tanımı ile kamusal, düzeltilebilir gerekçelendirme yorumu arasındaki köprü yeterince gerekçeli mi? | Öncül–sonuç incelemesi; döngüsellik ve ortak hata itirazlarına gerekçeli karar |
| D03 | H03 §§3, 7A–7E | Örnek soyağacı kaydı başka bir denetçinin aynı iddia ve kaynak yerine ulaşmasına yeterli mi? | Bağımsız yeniden uygulama; eksik alan ve uyuşmazlık kaydı |
| D04 | H04 §§2–5D | İmkân, bilgi, niyet ve kontrol koşulları normatif sonucu açıkça sınırlıyor mu; evre tablosu tarihsel zorunluluk ima ediyor mu? | Felsefi argüman ve kanonik kapsam incelemesi |
| D05 | H05 §§1–6A | Akıl tanımı ile önerilen davranış göstergeleri arasında döngüsellik veya tanımla ampirik sonucu garanti etme sorunu kalıyor mu? | Karşılaştırmalı biliş ve kavram incelemesi; kaynakların desteklediği dar sonuçlar |

Bu beş soru beş atomik iddia sayımı değildir; inceleme başlıklarıdır. İki özgün kaynağın bütün metin kapsamının taranmış olması, burada beklenen kararları kendiliğinden üretmez. Bağımsız denetçi/sonuç alanları doldurulmadı. Gönderim veya dış kişiye mesaj işlemi yapılmadı. Yeni inceleme bu turdan sonraki commit'i esas almalı; ilgili ana metin değişirse kararın sürüm kapsamı yeniden kontrol edilmelidir.

---

## Doğrulanmış yapısal envanter
| Kimlik | Makale | Metin karakteri | Bölüm yapısı | DOI biçimli kayıt | Dış URL |
|---|---|---:|---|---:|---:|
| H01 | Hebûn | 10.410 | Öz, 11 numaralı bölüm, kaynaklar, kurucu ekler | 0 | 4 |
| H02 | Zanabûn | 7.011 | Öz, 8 numaralı bölüm, kaynaklar, kurucu ekler | 0 | 2 |
| H03 | Rasterast | 8.144 | Öz, 8 numaralı bölüm, kaynak izi, kurucu ekler | 0 | 1 |
| H04 | 6+Tek | 5.795 | Öz, 9 numaralı bölüm, kaynak/sürüm izi | 0 | 0 |
| H05 | Akıl ve Bilgi | 9.316 | Öz, 11 numaralı bölüm, kaynak izi | 0 | 0 |

**Yöntem notu:** Karakterler mevcut Markdown metinleri üzerindendir; URL ve DOI sayıları basit metin örüntüsü sayımıdır. Sıfır DOI, makalenin dayandığı araştırma eklerinde hiç DOI bulunmadığı anlamına gelmez. Bu tarama atıfların bilimsel yeterliliğini henüz ölçmez.

## Çekirdek kalite darboğazları
- **H01:** Ehad–Yek, ikinci Yek, türeme ve Komel tezlerini teolojik yorum / felsefi önerme / fiziksel-biyolojik gözlem olarak iddia düzeyinde etiketle. Nisâ 4:1'den çıkmayan ayrıntıları ayır. Hidrojen-1 karşı-örneğini makale iddiasıyla doğrudan eşle.
- **H02:** İkinci Yek ile ikinci Bilen ayrımını örnek ve yanlışlama koşullarıyla güçlendir; bağımsız doğrulayıcının ölçütlerini tanımla.
- **H03:** Kaynak soyağacı, bağımsız ikinci denetim, ortak hata, karşı-örnek ve geri besleme döngüsü için yeniden uygulanabilir denetim protokolü ekle.
- **H04:** Altı kozmik boyut ile insan katmanlarını ayrı tut; 1. ve 2. evreleri açık tabloya dönüştür; fıtrî ahlak ile iradeli ahlakı karıştırma.
- **H05:** Hayvan zekâsı, duygusal/mantıksal işlem ve insan aklı ayrımını operasyonel göstergelerle tartış; karga çalışmalarını karşı-örnek olarak doğru sınırlarda kullan; ilgili araştırma eklerinin DOI'lerini makale içi iddialara bağla.

## Tekrarlanabilir hızlandırılmış denetim sırası
1. **İddia matrisi:** Her bölümün temel önermesi, statüsü (teolojik/felsefi/ampirik/hipotez/analojik), kanıtı, karşı-örneği ve açık sorusu.
2. **Atıf haritası:** Her ampirik iddiayı birincil kaynak, DOI, yayın tarihi, ilgili paragraf ve araştırma ekiyle eşle.
3. **Kanonik aktarım:** H01 → H02 → H03 → H04 → H05 ve geri dönüş oklarıyla terim ve gerekçe çelişkilerini tarayıp kaynak makaleye geri besle.
4. **Düzeltme:** Her tespit için dosya, bölüm, değişiklik, gerekçe ve denetim izini kaydet; ana metne yansımayan ek düzeltmesini tamamlanmış sayma.
5. **Kalite kapısı:** Yalnız doğrulanmış ölçütleri yeşil işaretle; 412 benzersiz makale, bütünsel geri besleme ve kurucu onayı olmadan 'yayına hazır' deme.

## Hızlanma kararı
Bu beş metnin hepsi GitHub'da mevcut ve sonuç bölümü içeriyor. İlk yapısal taramada **beşinde de ana metin içinde DOI biçimli atıf saptanmadı**; öncelik yeni ekler üretmekten ziyade mevcut eklerin kaynak ve karşı-örneklerini **ana metindeki ilgili iddialara taşımaktır**. Sonraki iş H01 ve H05'ten başlayarak paragraf bazlı kaynak–iddia eşlemesi ve çapraz denetimdir.

**Kurucu yayın kapısı:** `KURUCU-YAYIN-KAPISI-412-MAKALE-GERI-BESLEME-2026-10-22.md`.

## Güncel yeniden ölçüm — kaynak aktarımı ve argüman turu

Üstteki ilk tarama tablosu tarihsel ölçümdür. Aşağıdaki değerler H05 commit'i 1febcee70b6e71c4cb664fa233f03e55af521940 sonrasında daldan yeniden okunan ana metinler içindir. Karakterler JavaScript metin uzunluğu; DOI sayısı, sondaki nokta temizlenerek tekilleştirilmiş metin örüntüsüdür. DOI sayısı bilimsel kalite puanı değildir; H04'ün ders kitabı kaynağında DOI olmaması hata değildir.

| Metin | Karakter | Benzersiz DOI | Ana önerme haritası | Yazım sonrası içerik eşliği |
|---|---:|---:|---|---|
| H01 | 16372 | 2 | Var | Birebir doğrulandı |
| H02 | 12291 | 1 | Var | Birebir doğrulandı |
| H03 | 14174 | 1 | Var | Birebir doğrulandı |
| H04 | 11037 | 0 | Var | Birebir doğrulandı |
| H05 | 16989 | 5 | Var | Birebir doğrulandı |

### Ölçüt bazında durum
| Ölçüt | Durum | Kanıt ve sınır |
|---|---|---|
| Belirtilen önceki beş commit'in dalda bulunması | Doğrulandı | Önceki kaynak aktarımı kaydında merge-base ve dal karşılaştırması |
| Beş ana metne doğrudan kaynak/argüman aktarımı | Doğrulandı | Yeni beş commit ve birebir yeniden okuma |
| Ana önermelerin iddia türü ve dayanak tablosu | Doğrulandı | Beş metnin ana gövdesinde mevcut; bütün cümlelerin tam envanteri değil |
| H01 maya deneyi, H05 iki karga çalışmasının ana yöntem/bulgu kontrolü | Yapıldı | Ana metinler okundu; ham veri, ek video ve bütün ek materyal yeniden analizi değil |
| H05 planlama iddiasına yayımlanmış itiraz ve yanıt | Aktarıldı | 2021 eleştiri ve yanıt DOI'leri ana metinde; yeni tekrar deneyi yok |
| Nisâ 4:1 doğrudan metin/tefsir tam sayfa karşılaştırması | Kısmi | Resmî indeks metni görüldü; sayfa gövdesi alınamadı |
| Özgün Word esas önermelerinin tam envanteri | Açık | Seçilmiş paragraf eşlemeleri mevcut |
| Bağımsız ikinci denetim | Açık | Aynı çalışma akışı kendi kendine bağımsız onay vermedi |
| Akademik çalışma sürümü bütünsel kapanışı | Açık | Önceki açık ölçütler ve son editoryal kontrol sürüyor |
| 412 makale ve nihai yayın kapısı | Kapalı | Tam envanter, bütünsel uyum ve kurucu nihai onay henüz yok |

Son işlem günlüğü: `H01-H05-KAYNAK-AKTARIMI-VE-OZGUN-METIN-DENETIMI-2026-10-22.md`. Kanonik metinler, eski sürümler ve araştırma ekleri korunmuştur. Halka 1 üretimine başlanmamıştır.

## Özgün kaynakların bütün metin kapsamı — üçüncü çalışma turu
İki özgün dosyanın okunabilir metni bütünüyle tarandı: A kaynağı 195 birim/37 blok; B kaynağı 177 birim/28 blok. Toplam **372 birim, 65 anlam bloğu**. Başlıklar dâhil her birim envanterde tam bir kez kapsanır. Bu, bağımsız önerme veya makale sayısı değildir. Ayrıntı: `H01-H05-IKI-OZGUN-KAYNAK-PARAGRAF-KAPSAMA-VE-IDDIA-ENVANTERI-2026-10-22.md`.

“Özgün kaynakların ilk bütün-metin kapsam taraması ve ana önerme ailesi eşlemesi” artık tamamlandı. “Her atomik önermenin dış kaynak/argüman doğrulaması” ve bağımsız ikinci denetim ayrı ölçütlerdir ve açık kalır. Önceki tablolardaki seçilmiş paragraf eşlemesi notları tarihsel durumu gösterir.

| Metin | Bu tur sonrası karakter | Benzersiz DOI | Ana metne aktarım |
|---|---:|---:|---|
| H01 | 19185 | 4 | Kaynak kapsamı düzeltmeleri işlendi |
| H02 | 13609 | 1 | Kaynak kapsamı düzeltmeleri işlendi |
| H03 | 15383 | 1 | Kaynak kapsamı düzeltmeleri işlendi |
| H04 | 12167 | 0 | Kaynak kapsamı düzeltmeleri işlendi |
| H05 | 18425 | 5 | Kaynak kapsamı düzeltmeleri işlendi |

Karakter ve DOI sayımı önceki yöntemle yapılmıştır; bunlar kalite veya bağımsız kanıt puanı değildir. H01'de NIST atom numaraları ve IUPAC element tanımı; H01/H04'te NHGRI hücresel kuruluş kontrolü; H02/H05'te sevgi, doğruluk, duygu ve bilişsel kapasite ayrımları kaynak paragraf izleriyle ana gövdeye işlendi. H03'e bütün-paragraf kapsam taramasının sınırları eklendi.

Tam akademik kapanış, bağımsız ikinci denetim, ilgili birincil kaynak/rivayetlerin kalan kontrolleri ve bütünsel editoryal denetim açık. Dış çekirdeğe geçilmedi; 412 yayın kapısı korunuyor.

## Kaynak yerleri ve iç editoryal kontrol — devam turu

| Makale | Karakter | Benzersiz DOI | Yazar/kurum–kaynakça eşleşmesi |
|---|---:|---:|---|
| H01 | 21422 | 4 | Kontrol edildi |
| H02 | 14396 | 1 | Kontrol edildi |
| H03 | 16309 | 4 | Kontrol edildi |
| H04 | 12051 | 0 | Kontrol edildi |
| H05 | 19039 | 5 | Kontrol edildi |

Ölçüm önceki metin uzunluğu/tekil DOI yöntemiyle yapılır; kalite puanı değildir. Otomatik isim varlığı kontrolü, ilgili paragrafların elle okunan iddia–kaynak karşılaştırmasını tamamlar; onun yerine geçmez. Başlık, öz, anahtar sözcükler, yöntem, argüman, sonuç ve kaynak bölümleri beşinde de mevcuttur. H03'te atıf yapılan karga çalışması ve 2021 eleştiri/yanıtının künyeleri kendi kaynakçasına da eklendi.

### Kaynak erişiminde kapanan dar ölçütler
- Nisâ 4:1: Diyanet 2011 basılı meal s. 87, dipnot 1 ve PDF sayfası 150 doğrudan metin/görüntü kontrolü. Tefsir belgesiyle karıştırılmadı.
- Adelberger: erişilen arXiv:1004.2318v3 yazar sürümü §II, denklem 2 ve ara tepkimeler dizisi incelendi. Kontrol sürümü 2010; dergi künyesi 2011. Bütün 57 sayfanın veya 2011 son sürümün eksiksiz karşılaştırması iddia edilmedi.
- NHGRI DNA ve NCI otonom sinir sistemi: doğrudan resmî tanımlar okundu. Biyolojik bilgi ve otonom işleyişin metafizik yorumlardan ayrıldığı kaynak yerleri işlendi.

### Editoryal düzeltmeler
H01'de H02/H03 için artık yapılmış aktarım gelecek zamanla anlatılmıyor; tamamlanan paragraf kapsam taraması eski “yapılacak” listesinde bırakılmadı. H02'de doğrudan meal atfı eklendi. H03'ün özgün kaynak kapsam notu güncellendi. Kanonik Ek B tekrarları kısaltılıp tanımların ana gövdedeki yerlerine bağlandı. H05'in dilsel aday notları sonuçtan Ek D'ye taşındı; sonuç araştırmanın gerçekten gösterdiği kapsamla sınırlandı. Yerel kaynak yolları bulundukları klasöre göre düzeltildi.

Bu tur **iç editoryal geçiştir**. Bağımsız ikinci denetim, kalan atomik iddia karşılaştırmaları ve bütünsel çekirdek kapanışı tamamlanmış değildir. 412 makale yayın kapısı ile Halka 0 önceliği aynen korunur.

## Öncül–sonuç ve kavramsal kapsam denetimi

Bu tur önceki iç editoryal geçişe ek bir argüman incelemesidir. Aynı çalışma akışı tarafından yapıldı; bağımsız ikinci denetim sayılmaz. Aşağıdaki kayıtlar yeni deney sonuçları değil, ana metindeki çıkarım ve uygulama sınırı düzeltmeleridir.

| ID | Yer | Sorun | Ana metindeki işlem | Sonuç / açık sınır |
|---|---|---|---|---|
| L01 | H01 §4 | Y₁/Y₂ indisinin kapsamı açık değil | İndisler alan ve zaman bağlamına bağlandı; Ehad yaratılmış dizinin halkası yapılmadı | Kanonik anlam açıklığı düzeltildi |
| L02 | H01 §6 | Hücre türemesinden ana kimliğin aynen sürmesi çıkarılıyor | Soy sürekliliği ile sayısal kimlik ayrıldı; mitoz örneğinin kaynak yeri eklendi | Biyolojik örnek daraltıldı; evrensel kimlik modeli henüz yok |
| L03 | H02 Z2 | Özne–nesne rol ayrımından zorunlu ayrı varlıklar sonucu çıkıyor | Kendini bilme olanağı korundu; rol ile varlık sayısı ayrıldı | Kavramsal hata düzeltildi |
| L04 | H02 §2 | İnsan onayı ile ontolojik var etme ilişkisi karışabilir | Onayın P iddiasına yönelmesi; Ehad'ın insan onayına bağımlı olmaması açıklandı | Ontolojik ve epistemik bağımlılık ayrıldı |
| L05 | H03 §7B | Bağımsızlık yalnız kişi veya yayın sayısına indirgenebilir | Veri, araç, analiz ve yorum düzeyleri ayrı kaydedilir | Denetim şeması netleştirildi; hata olasılığı ölçülmedi |
| L06 | H04 §5B/§5D | Boyuttaki evre ayrımından her bireyin tüm evrelere geçişi çıkarılabilir | Sınıflama ile her bireye ait zorunlu gelişim öyküsü ayrıldı | Kapsam daraltıldı |
| L07 | H05 §3 | Her düzene bir bilen önermesinden aynı tek bilen sonucu çıkıyor | Her durum için var olma ile bütün durumlarda aynılık farklı öncüller olarak ayrıldı | Ehad'ın birliği kurucu kabul olarak korundu; eksik çıkarım gizlenmedi |
| L08 | H05 §6 | Kavramsal beşli nicel vektör ve eksik ölçüm sıfır gibi okunabilir | Uygulanamaz, ölçülmedi ve ölçülen değer ayrıldı; ortak puan varsayımı kaldırıldı | Ölçüm tanımı gereği açık; sayısal model doğrulanmadı |

### Kaynak ve geri besleme
H01'de mitozu genellikle izleyen iki yavru hücre oluşumu için NHGRI, *Mitosis*, https://www.genome.gov/genetics-glossary/Mitosis tanımı doğrudan okundu. Bu, bakterilerin bölünmesiyle mitozun eşitlenmesi veya biyolojik tanımdan ontolojik kimliğin otomatik çıkarılması değildir. Bakteri bölünmesi için NCBI Bookshelf araması okunabilir özet sundu; doğrudan sayfa çağrısı doğrulama ekranına döndüğünden bu kaynak ana metnin yeni kanıtı olarak kullanılmadı.

H01'deki ontolojik kimlik, H02'deki kavramsal rol ayrımına; H02'deki iddia onayı, H03'teki kaynak ve yöntem denetimine; H04'teki evre kapsamı, H05'teki değişken uygulanabilirliğine geri beslendi. Hiçbir düzeltme yeni boyut, yeni makale veya yeni ampirik başarı olarak sayılmadı.

### Düzeltme sonrası iç kontroller
Beş metin yeniden birlikte karşılaştırıldı: Yek'in ayrı yaratılmış boyut olmaması; Ehad'ın insan onayına bağımlılaştırılmaması; ikinci Yek/ikinci Bilen ayrımı; fıtrat ve iki ahlak tanımı; tek hücreli/çok hücreli ile zekâ/akıl evreleri; insan katmanlarının sayısal kozmik eşleme olmaması korundu. Yeni iddia ve kaynak yerleri ana metinlere doğrudan işlendi. Bu okuma kaynak doğruluğunun bütün önermeler için bağımsız ispatı değildir.

**Genel durum:** Sekiz argüman/kapsam bulgusu için metin düzeltmesi yapıldı. Deneysel ve felsefi modelin bağımsız sınanması açık; Halka 0 bütünsel kapanışı ve 412 yayın kapısı yeşil değildir.

## D01–D05 iç argüman incelemesinin sonucu
**İnceleme tabanı:** de573d2e7dc083709d06b7871d4a15b90b374ed6. Bu kayıt aynı çalışma akışının incelemesidir; bağımsız ikinci karar değildir.

| Soru | Tespit / ana metindeki işlem | İç sonuç | Açık kalan koşul |
|---|---|---|---|
| D01 | H01 §4B: birim, bileşen, ilişki ve zaman aralığı; yalnız birliktelik ile örgütlenmeyi ayıramayan uygulama için yetersizlik kararı | Kapsam ve olumsuz karar kuralı yazıldı | Ölçütlerin alan örneklerinde bağımsız değerlendirilmesi |
| D02 | H02 §5D: ortak hata olanağından gerekçeli onay gereğine geçiş açık öncüllerle kuruldu; ret/düzeltme olumlu onay sayılmadı | Felsefi köprü ve onay kapsamı yazıldı | Kurucu tanım–yöntem yorumu ilişkisinin bağımsız eleştirisi |
| D03 | H03 §7D-1: sabit commit, tam önerme, tür, kaynak, köprü, bağımsız kanıt yokluğu, karşı-örnek, statü ve geri besleme alanları dolduruldu | Boş şema bir metin kaydına uygulandı | Başka denetçinin yeniden uygulaması ve uyuşmazlık kararı |
| D04 | H04 §4B: bilgi, öngörü, erişim, denetim, zorlama ve imkânsızlık koşulları ayrıldı | Teknik kapasiteden koşulsuz sorumluluk çıkarımı engellendi | Normatif argümanın bağımsız değerlendirilmesi |
| D05 | H05 §5D: tür etiketi ile davranış göstergesi; başarı, mekanizma ve akıl kavramına uygunluk kararları ayrıldı | Tanımla sonucu garanti etme riskine karar kuralları yazıldı | Göstergelerin bağımsız kavramsal/alan incelemesi ve gerektiğinde deneysel sınanması |

H01 §4B'deki Ratcliff göndermesi yeni deney bulgusu eklemez; daha önce okunmuş ve §6'ya aktarılmış kaynağın uygulama sınırıdır. Bu turdaki PMC sayfa çağrıları doğrulama ekranına döndü; yeni doğrudan tam metin erişimi başarılmış gibi kaydedilmedi. H03'teki cihaz kaydı gerçek veri deneyi değil, H02'de yazılı mantıksal karşı-örnektir. Yeni dış araştırma, denetçi sonucu veya hata oranı üretilmedi.

**Durum kararı:** D01–D05 için iç metin işlemleri yapıldı; soruların bağımsız değerlendirme sütunları açık. Bütün atomik iddiaların denetimi tamamlandı denmez. Halka 0 bütünsel kapanışı ve 412 yayın kapısı değişmedi.

## Atomik bilimsel ifade denetimi — E01–E16
**Taban commit:** 5fefc6b13728cc88ac82f15ba28e7e6956a6e6dd. **Tarih:** 22 Ekim 2026. Bu tur seçilmiş 16 açık önerme doğrudan kaynak yerleriyle karşılaştırıldı. Her satırın sonucu ilgili dar önermeye aittir; bilimsel/felsefi metnin tamamına veya bağımsız hakemliğe kapanış vermez. “Destekli” bu kaynak karşılaştırmasının sonucudur; yeni deney yapıldığı anlamına gelmez.

| ID | Ana metin yeri | Denetlenen önerme | Doğrudan kaynak yeri | Karar / ana metin işlemi |
|---|---|---|---|---|
| E01 | H01 §5A | Hidrojen atom numarası 1 | NIST, Hydrogen; Atomic Number | Destekli; mevcut ifade korundu |
| E02 | H01 §5A | Helyum atom numarası 2 | NIST, Helium; Atomic Number | Destekli; mevcut ifade korundu |
| E03 | H01 §5 | Hidrojen-1 nötronsuzdur | NIDC, Isotope Basics; What are Isotopes? | Destekli; yakın atıf NIDC'ye bağlandı |
| E04 | H01 §6 / H05 §1 | DNA genetik bilgi taşır | NHGRI, DNA; Definition | Destekli; bilişsel bilgiyle özdeşlik çıkarılmaz |
| E05 | H01 §6A / H04 §5D | Prokaryotta zarla çevrili çekirdek yoktur | NHGRI, Cell; Definition | Destekli; örgütleyici merkez analojisinin ispatı değil |
| E06 | H01 §6 | Mitozu genellikle iki yavru hücre oluşumu izler | NHGRI, Mitosis; Definition | Destekli; mitoz bakterilerin bölünmesiyle eşitlenmedi |
| E07 | H05 §2 | Farklılaşma hücresel özelleşmeyle ilgilidir | NCI, Cell differentiation; tanım | Kaynak eklendi; evrensel çok hücrelilik mekanizması sonucu kaldırıldı |
| E08 | H04 §3A | Mekanik avantaj kuvvet büyüklüklerinin oranıdır | OpenStax §9.5, denklem 9.29 | Destekli; büyüklük ifadesi açıklandı |
| E09 | H04 §3A | İdeal makine enerji üretmez | OpenStax §9.5 giriş; kuvvet/yol açıklaması | Destekli; normatif sonuca aktarılmadı |
| E10 | H04 §3A | Her araç kuvveti büyütür genellemesi geçmez | OpenStax §9.5, Şekil 9.22b / 9.23c | Karşı-örnekler ana metne eklendi |
| E11 | H02 §5A / H03 §7B | Aynı veriyle hesaplama ve yeni veriyle tekrar farklıdır | NASEM 2019, bölüm 3, s. 45–46, Sonuç 3-1 | Destekli; kaynak yeri netleştirildi |
| E12 | H02 §5D / H03 §7B | Tekrar ilk ekipçe de yapılabilir | NASEM 2019, bölüm 3, s. 45–46 | Destekli; ekip bağımsızlığından ayrıldı |
| E13 | H05 §5A | Jelbert deneylerinde katılımcı sayısı azalır | Jelbert 2014, Subjects / Results | Destekli; ayrılma nedeni ve deney bazlı örneklem yazıldı |
| E14 | H05 §5A | Jelbert kuşlarına taş bırakma eğitimi verilmiştir | Jelbert 2014, Initial Training | Destekli; eğitimsiz çözüm yorumu önlendi |
| E15 | H05 §5A | Dar/geniş tüpte ilk tercih verimliyi göstermedi; U-tüpü başarısı şans üstü değildi | Jelbert 2014, Results, Experiments 4 / 6 | Görev bazlı sonuçlar yazıldı; katılım kaybından ayrıldı |
| E16 | H05 §5A | Bu örneklemden türün tamamında yetenek yokluğu çıkmaz | Jelbert 2014, Discussion; örneklem/kısıtlar | Kaynağın genelleme sınırı korundu |

Kaynak erişimi: NIST H/He veri sayfaları; NIDC Isotope Basics; NHGRI Cell, DNA ve Mitosis; NCI Cell differentiation; OpenStax §9.5; NASEM bölüm 3 ve PLOS'un Jelbert 2014 ana metni doğrudan okundu. Bu tur ham veri, ek video veya deney tekrarı yapılmadı. Aynı kurumsal tanımın iki makalede kullanılması iki bağımsız veri kümesi sayılmadı.

H02'de bu tur öncesi eklenen 5fefc6b13728cc88ac82f15ba28e7e6956a6e6dd commit'i korundu. İki ayrı “7B” başlığı oluştuğu için son eklenen alt bölüm 7C olarak numaralandırıldı; metni silinmedi. NASEM'in yeni veri ayrımı H02'den H03'e; hücresel özelleşmenin kapsamı H05'e; kuvvet kazancının koşullu oluşu H04'e doğrudan işlendi.

**Açık kapsam:** E01–E16 seçilmiş dar önermelerdir; tüm atomik iddiaların tamamlandığına ilişkin payda veya yüzde verilmez. Önceki kaynak envanteri bütün metin kapsamını gösterir; bütün cümlelerin bilimsel doğruluğunu göstermez. Bağımsız ikinci değerlendirme ve bütünsel Halka 0 kapanışı açık; Halka 1 üretimine geçilmedi.

## Nükleer süreç ve bilişsel deneyler — E17–E30
**Taban:** 524f15c4c497ca88733b8acbb1fdc4d23c988a1a. **22 Ekim 2026.** On dört dar önerme kaydedildi: E17–E28'in ilgili kaynak yerlerine doğrudan erişildi; E29–E30'un bu turdaki erişim düzeyi kısmi bırakıldı. Yeniden incelenen önermeler yeni deney veya yeni bağımsız veri diye sayılmaz.

| ID | Yer | Önerme | Kaynak yeri | Karar |
|---|---|---|---|---|
| E17 | H01 §5 | pp zincirinin net bilançosu dört protondan helyum-4 çekirdeği ve lepton ürünlerini gösterir | Adelberger, erişilen 2010 yazar sürümü, §II, denklem 2; PDF s. 6 | Doğrudan destekli; tek çarpışma diye yorumlanmadı |
| E18 | H01 §5 | Net bilanço ile ara nükleer tepkimeler ayrı düzeylerdir | Aynı sürüm, §IB içerik açıklaması / §§III–IX dizisi | Doğrudan destekli; bütün nükleer süreçlere genelleme önlendi |
| E19 | H05 §5A | Kenward örneklemi dört elle büyütülmüş genç kuştur | Kenward 2005, s. 121, yöntem paragrafı | Doğrudan destekli |
| E20 | H05 §5A | İki kuş gösterim aldı, ikisi almadı | Kenward 2005, s. 121, barındırma/gösterim paragrafı | Doğrudan destekli |
| E21 | H05 §5A | Dördü çubuk araç kullandı | Kenward 2005, s. 121, sonuç paragrafı | Doğrudan destekli |
| E22 | H05 §5A | Yaprak parçasıyla yiyecek çıkarma Corbeau için bildirildi | Kenward 2005, s. 121, Pandanus paragrafları | Doğrudan destekli; dört kuşa genişletilmedi |
| E23 | H05 §5A | Gösterim ile barındırma koşulları birlikte değişti | Kenward 2005, s. 121, yöntem | Yöntem bilgisi doğrudan; dengeli nedensel karşılaştırma olmadığı sonucu bu metnin çıkarımı olarak yazıldı |
| E24 | H05 §5A | Dokuz kuş eğitime girdi, dördü kritik teste ulaştı | Boeckle 2020, Methods: Participation of individuals across trials | Doğrudan destekli; paydalar ayrıldı |
| E25 | H05 §5A | Nesne seçimi beş dakika, düzeneğe erişim seçimden on dakika sonraydı | Boeckle 2020, Methods: Procedure | Doğrudan destekli |
| E26 | H05 §5A | Kritik koşullarda dört kuştan üçü ölçütü aştı | Boeckle 2020, Results / Tablo 1; ayrıntılar Tablo 3 | Doğrudan destekli; tür başarı oranı sayılmadı |
| E27 | H05 §5A | Ana şans karşılaştırması beş seçenek içinde bir doğru için %20'dir | Boeckle 2020, Methods: Statistics | Doğrudan destekli; kaynakta çeldirici duyarlılığı da tartışılır |
| E28 | H05 §5B | 2020 yazarları bütün çağrışımsal açıklamaları dışlamadıklarını belirtir | Boeckle 2020, Discussion | Doğrudan destekli; yalnız 2021 eleştirisine atfedilmedi |
| E29 | H01 §6 | On popülasyonda 60 seçilim turu sonrası benzer kümeli biçimler bildirildi | Ratcliff 2012, resmî PMC indeks kaydı / şekil açıklaması | İlk kayıtta kısmi; aşağıdaki E29–E30 kapanışında yayıncı metniyle doğrudan doğrulandı |
| E30 | H01 §6 | Küme mekanizması bölünme sonrası bağlı kalma olarak aktarılır | Ratcliff 2012, önceki turda okunan Results: Mechanism of Cluster Formation | İlk kayıtta yeniden erişim eksikti; aşağıdaki kapanışta ilgili bölüm ve şekil açıklaması doğrudan doğrulandı |

### Erişim ve yorum sınırı
Kenward'ın bir sayfalık Oxford PDF'si, Boeckle 2020'nin yedi sayfalık Cambridge PDF'sindeki ilgili yöntem/sonuç/tartışma ve Adelberger'in açık yazar sürümü §II denklem 2 ile §IB açıklaması doğrudan okundu. Ek video ve ham veri yeniden analiz edilmedi. E23'te barındırma/gösterim karışmasının değerlendirilmesi bizim yöntemsel çıkarımımızdır; kaynağın kendi cümlesi gibi verilmedi.

Ratcliff için PMC çağrısı doğrulama ekranına döndü. PNAS ilk çağrıda yayın kaydı sundu; sonraki bölüm aramaları çerez sayfasına yönlendi. Resmî indeks E29'un dar ifadesini sundu. Bu yüzden önceki tam metin incelemesi silinmedi, fakat yeni doğrudan yeniden okuma tamamlandı denmedi. E29/E30 bu turdaki erişim kısıtı kapanmadan diğer satırlarla aynı statüde gösterilmez.

H01'de net nükleer bilanço/ara süreç ayrımı; H05'te yaprak görevinin birey kapsamı, barındırma koşulu, test paydası, şans düzeyi ve 2020 makalesinin kendi sınırlaması işlendi. H03'e örneklem paydası ve seçenek uzayını kaydetme kuralı geri beslendi. Dış çekirdeğe geçilmedi; bağımsız değerlendirme ve bütünsel kapanış açık.

## E29–E30 erişim ve iddia kontrolünün kapanışı
**Taban:** 058f0cedce7a7cdba1e1ef728a044b73dac22d75. **22 Ekim 2026.** Önceki kısmi kayıtlardan sonra https://www.pnas.org/doi/10.1073/pnas.1115323109 adresindeki yayıncı ana metnine doğrudan erişildi. Başlık, yazarlar, yıl ve DOI H01 kaynakçasıyla eşleşti. Deney düzeni, Results girişi, Mechanism of Cluster Formation ve Şekil 2B açıklaması okundu.

| Kayıt | Güncel karar | Metindeki sonuç |
|---|---|---|
| E29 | İlgili bölüm doğrudan destekli | On popülasyon / 60 aktarım ifadesi korundu; H01 §6 yöntem geçişini belirtti |
| E30 | İlgili bölüm doğrudan destekli | Mekanizma yalnız incelenen kümelere bağlandı; evrensel kümelenme mekanizması yapılmadı |
| E31 | Yeni dar yöntem kontrolü destekli | İlk haftadan sonraki santrifüj aşaması H01'e işlendi; H03'e süreç değişikliğini izleme kuralı aktarıldı |

Bu kapanış erişim ve belirtilen üç önerme içindir. Ham ölçüm, ek video ve bağımsız deney tekrarı yapılmadı. Önceki PMC doğrulama ekranı, PNAS çerez yönlendirmesi, Ottawa PDF 404 ve diğer başarısız çağrılar gerçek erişim sonuçları olarak korunur; son başarı bunları geriye dönük değiştirmez. MuLTEE laboratuvar sayfası alternatif bir açıklama sundu, fakat kapanışın dayanağı yayıncının makale metnidir; aynı araştırmanın ikinci bağımsız deneyi sayılmadı.

IUPAC C01022/A00499 sayfalarının doğrudan çağrıları yine 403 verdi; Nisâ 4:1 dinamik tefsir sayfası okunabilir gövde vermedi. Bu kayıtların önceki resmî indeks düzeyleri tam sayfa okunmuş gibi yükseltilmedi. Bütün atomik iddiaların denetimi ve bağımsız ikinci değerlendirme hâlâ açık.

## E32–E36: tanımın iki anlamı ve tartışma taraflarının iddiaları
**Taban:** 04bafdcc27690a513e916ade1aa3f4acb806f53e. **22 Ekim 2026.** Bu tur kaynakta söylenenle o kaynağa atfedilen yorum ayrıldı. Kararların erişim sınırı aşağıdadır.

| ID | Yer | Denetlenen önerme | Kaynak yeri / erişim | Karar ve işlem |
|---|---|---|---|---|
| E32 | H01 §5A | Element için atom türü ve saf madde anlamları vardır | IUPAC C01022 resmî indeks kaydı; iki tanım | İki anlam ana metne işlendi; doğrudan sayfa kontrolü açık |
| E33 | H01 §5A | Atom numarası proton sayısıdır | IUPAC A00499 resmî indeks metni | Tanım eşleşti; doğrudan erişim 403 olarak korundu |
| E34 | H05 §5B | 2021 yanıtı yeni veri çalışması değildir | Cambridge yazar PDF'si, s. 5, Data accessibility; doğrudan | Destekli; veri kaynağı sayısı artırılmadı |
| E35 | H05 §5B | Yanıt yazarları yüksek düzeyli gelecek kavramını hedefledikleri yorumunu reddeder | Aynı PDF, s. 3; doğrudan | Tarafların iddia atıfları ayrıldı; bu ret eleştirinin yanlışlığını peşinen kanıtlamaz |
| E36 | H05 §5B | Belirli bir açıklamaya karşı kanıt, bütün çağrışımsal süreçleri dışlamaz | Aynı PDF, s. 3; doğrudan | Mekanizma kapsamı ve yazarların kendi sınırı belirtildi |

H03 §7C'ye iddia atfını denetleme kuralı geri beslendi. Eleştirinin PMC tam metin çağrısı doğrulama ekranına, yayıncı çağrısı 403'e döndü; resmî indeks düzeyindeki eleştiri okuması tam sayfa erişimi gibi gösterilmedi. IUPAC sayfa/PDF/JSON çağrıları sonuç vermedi; eski site çağrısı da erişim hatası verdi. Bu iki tanımın kısa resmî indeks metni görüldü; 2025 tam sayfa sürümü doğrudan okundu denmedi.

**Durum:** Üç yanıt önermesinin kaynak yerleri doğrudan kontrol edildi; iki IUPAC tanımının içerik eşlemesi indeks düzeyinde. Bütünsel iddia denetimi ve bağımsız ikinci değerlendirme açık. Sonraki doğrudan erişim başka bir sürüme aitse sürüm farkı ayrıca kaydedilmelidir.
