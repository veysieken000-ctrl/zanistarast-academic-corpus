# A06 — İkinci bilenin bağımsızlığı ve ortak hata modeli
**23.10.2026 | Araştırma taslağı v01 | Yayına hazır değil**

## Öz
Zanabûn'da ikinci bilenin onayı, iki kişinin aynı görüşte olmasının kesin doğruluk sayılması değildir. Bu çalışma H02'nin epistemik rol ayrımını, H03'ün kanıt soyağacı denetimiyle birleştirir ve bağımsız değerlendiriciler arasındaki ortak hatayı ölçülebilir hale getirir. Yeni ampirik veri sunmaz; sınanabilir bir protokol önerir.

## Kurucu kapsam
Ehad–Yek ontolojik kabulü teolojik/kurucu statüdedir. İlk Yek, ikinci Yek ve ilişkilerinden yeni Yekler ile Komel düzeni, insan hakemlerinin hata olasılığıyla özdeşleştirilmez. İkinci bilenin onayı felsefi/epistemik ilkedir; ampirik güvenilirlik ayrıca sınanır. Kozmik 6+Tek ve insan katmanları sayısal olarak özdeş değildir.

## Matematiksel model
Altın standardı bilinen ikili bir görevde doğru sınıf T, hakem yanıtları R1 ve R2, hata göstergeleri E_i=1{R_i≠T} olsun. p_i=P(E_i=1) ve q=P(E1=1,E2=1).
**q=p1*p2+Cov(E1,E2).** Bağımsız hata göstergelerinde q=p1*p2 olur. Genel sınırlar: max(0,p1+p2−1) ≤ q ≤ min(p1,p2).
p1=p2=p ve hata korelasyonu ρ ise q=p²+ρp(1−p). ρ keyfî seçilemez; ortak olasılık sınırlarına uymalıdır.
İkili görevde yalnız iki hakem anlaştığında karar kabul edilirse, tüm görevlerde yanlış kabul olasılığı q'dur. Kabul edilenler içindeki yanlış oranı ise q/P(kabul) olup aynı şey değildir.

### Varsayımsal hesap
p=0,10 olduğunda:
| ρ | q | P(kabul) | P(yanlış\|kabul) |
|---:|---:|---:|---:|
| 0 | 0,010 | 0,820 | %1,22 |
| 0,5 | 0,055 | 0,910 | %6,04 |
| 1 | 0,100 | 1,000 | %10,00 |

Bu rakamlar saha verisi değildir. Hakemlerin uzlaşması yükselirken ortak yanlış kabul de yükselebilir. Çok sınıflı görevlerde iki yanlış yanıtın aynı olması zorunlu değildir; bu denklem o duruma doğrudan taşınamaz.

## Karşı-örnek ve sınırlar
İki hakem aynı kalibrasyon hatalı cihazı kullanırsa iki onay bağımsız kanıt oluşturmaz. Farklı analizler aynı veri toplama yanlılığını taşıyabilir. Farklı web sayfaları aynı birincil haberi kopyalayabilir. Görev zorluğu, hakem hataları arasında görünür ilişki oluşturabilir. Altın standart bilinmiyorsa yalnız uzlaşmadan p veya q çıkarılamaz.

## Sınanabilir araştırma önerisi
Altın standardı bağımsız belirlenmiş ikili maddeler, zorluklarına göre tabakalanır. İkinci değerlendirme üç koşulda karşılaştırılır: (A) ilk kararı görerek aynı veri ve araç, (B) ilk kararı görmeden aynı veri ve farklı analiz, (C) ilk kararı görmeden bağımsız veri/araç. Birincil sonuç yanlış kabul olasılığıdır. Askıya alma oranı, hata saptama süresi, maliyet ve kaynak bağımlılığı da raporlanır. Örneklem büyüklüğü pilot ve güç analiziyle belirlenecektir; veri henüz toplanmadı.

## Yeniden kullanılabilir inovasyon: Çift Sayacı
Her makale için **bağımsız kişi sayısı** ile **bağımsız kanıt zinciri sayısı** ayrı tutulur. Kanıt zincirinin veri, cihaz, kod, kaynak ve yorum bağımlılıkları belgelenmeden ikinci sayaç artırılmaz. Aynı iddianın birden çok kez tekrarı bağımsız delil değildir.

Önerilen kayıt alanları: claim_id; makale_id; iddia_metni; kanıt_statüsü (teolojik/felsefi/matematiksel/ampirik/analojik); kaynak_id; kaynak_türü; veri_kökeni; cihaz; kod; değerlendiren; körlük; ortak_hata_riski; karşı_örnek; etkilenen_çekirdek; kapı_durumu.

## Tümdengelim–tümevarım geri beslemesi
Tümdengelim: H02'nin ikinci bilen tanımından, H03'ün bağımsız kaynak ilkesine ve A06'nın karar/hata ölçütüne geçilir. Tümevarım: ilerideki denetimlerde gözlenen ortak hata örüntüleri, H02–H03'ün yöntemsel kapsamını yeniden sınamak için kaydedilir; kurucu teolojik kabul ampirik bulguyla otomatik doğrulanmış sayılmaz.

## K0–K6 durum
K0 kısmi: özgün Akıl ve Bilginin Kaynağı DOCX ile paragraf/sürüm izi yeniden sabitlenmeli.
K1 açık: kapsamlı rakip literatür ve özgünlük taraması.
K2 taslak: formül, karar kuralı, deney protokolü; uzman incelemesi yok.
K3 kısmi: matematik ve karşı-örnekler var; pilot veri yok.
K4 kısmi: ikili sınıf/altın standart sınırları belirtildi.
K5 açık: etik ve hedef dergi kontrolü.
K6 açık: bağımsız Rasterast denetimi ve kurucu onayı yok.

## Kaynaklar ve iz
- H02: `02-cekirdek-makaleler/NK-ZS-H02-A04-TR-v02-IKINCI-YEK-IKINCI-BILEN.md`
- H03: yetkili daldaki güncel Rasterast çekirdek metni; yol ve sürüm ayrıca doğrulanacak.
- Kurucu özgün metin: *2-Akıl ve bilginin varlığı.docx* (Google Drive, belge kimliği 1MOKZhk0VslI4aWwOtcDDsLb4WKSPdeyM).
- National Academies of Sciences, Engineering, and Medicine (2019), *Reproducibility and Replicability in Science*, DOI 10.17226/25303.
- Dawid, A. P. ve Skene, A. M. (1979), *Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm*, DOI 10.2307/2346806.

**Yayın kilidi:** 412 makalenin tamamı, bütünsel uyum, bağımsız denetim ve kurucu onayı olmadan yayın yok. A06 tamamlanmış makale değil, özgün aday taslağıdır.
