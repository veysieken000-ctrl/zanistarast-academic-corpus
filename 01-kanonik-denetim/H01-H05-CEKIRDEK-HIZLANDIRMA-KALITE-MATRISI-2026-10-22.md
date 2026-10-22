# H01–H05 çekirdek hızlandırma ve kalite matrisi

**Tarih:** 22 Ekim 2026. **Kapsam:** GitHub'daki beş çekirdek makalenin gerçek metinlerinden yapılan ilk yapısal tarama. **Statü:** Açık kalite kapısı; yayıma hazır değil. Bu kayıt 412 makale sayısına eklenmez.

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
