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
