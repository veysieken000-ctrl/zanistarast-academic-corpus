# BİLİM-01 — Bilginin türü, dayanağı ve epistemik statüsü

**22 Ekim 2026 · v0.1 · araştırma taslağı · yayıma hazır değil**

## Amaç
Zanistarast araştırma külliyatında bir iddianın ne tür bir önerme olduğunu, hangi kaynaklara dayandığını ve hangi denetimlerden geçtiğini birbirinden ayırmak.

## Kaynak sınırı
Özgün kaynak: `6-Bilim (1).docx`. Belgenin paragraf düzeyinde yeniden okunması henüz tamamlanmadı. Bu nedenle aşağıdaki üç eksenli tablo **araştırmacı önerisidir**; kurucunun özgün metninden doğrudan alıntı veya uygulanmış Mira yazılımı standardı değildir.

Kanonik çerçeve: Hebûn ontolojik temel, Zanabûn bilginin oluşumu ve gerekçelendirilmesi, Rasterast karşı-delil ve epistemik statü denetimi. Mira araştırır, Rasterast doğrular, Müdebbir yayın kararını verir.

## Araştırma sorusu
Aynı külliyattaki ontolojik, teolojik, normatif, analojik ve ampirik iddialar hangi ortak kayıt düzeniyle, fakat kendi yöntemleri korunarak değerlendirilebilir?

## Ayırıcı Tek adayı
Her önerme için üç ayrı alan tutulması:
1. **Tür:** ontolojik, teolojik, kavramsal, normatif, matematiksel, analojik veya ampirik.
2. **Dayanak:** özgün belge, gerekçeli argüman, gözlem, deney, veri veya bağımsız değerlendirme.
3. **Denetim durumu:** kaynak bekliyor, kaynak izlendi, karşı-delil arandı, bağımsız inceleme yapıldı, çelişki açık.

Bu sınıflandırmanın özgünlüğü ve etkinliği henüz doğrulanmadı. Durum adları kanonik yazılım enum'ları olarak sunulmaz.

## Örnek kayıtlar
| Önerme | Tür | Mevcut destek sınırı |
|---|---|---|
| Kozmik 6+Tek evre tasnifi | Ontolojik sınıflama | Kurucu kanonik önerme; ampirik doğrulama tamamlanmadı |
| Zekâ ve aklın iki evresi | Kavramsal ve sınanabilir yönleri olan önerme | Araştırma görevi tasarlandı; veri yok |
| İkinci bilenin ontolojik muhataplığı | Ontolojik ve teolojik | Bilimsel bağımsız hakemlikle özdeş değil |
| Bağımsız değerlendirmenin ortak hataları azaltması | Ampirik hipotez | Karşılaştırmalı test yapılmadı |
| Mabûn Ekonomi Modeli | Normatif ve kurumsal model | Model adı kanonik; ekonomik etkiler ölçülmedi |
| Rabûn meclis düzeni | Kurumsal ve normatif önerme | Kaynak incelemesi kısmi; uygulama doğrulanmadı |

## Yöntem
Özgün `6-Bilim (1).docx` belgesinin tüm iddialarını paragraf kimliğiyle çıkar; her iddiayı üç eksende kodla; birbiriyle çelişen etiketleri bağımsız ikinci okuyucuya incelet; olumlu ve olumsuz bulguları sakla. Kavramsal bir iddiaya deney şartı, ampirik bir iddiaya yalnızca kanonik onay yeterli sayılmamalıdır.

## Karşılaştırmalı literatür
- Stanford Encyclopedia of Philosophy, “Scientific Method” (8 Ağustos 2026 güncellemesi): https://plato.stanford.edu/entries/scientific-method/
- Stanford Encyclopedia of Philosophy, “Theory and Observation in Science” (12 Ocak 2026 güncellemesi): https://plato.stanford.edu/entries/science-theory-observation/
- Stanford Encyclopedia of Philosophy, “Scientific Objectivity”: https://plato.stanford.edu/entries/scientific-objectivity/

Bu kaynaklar kurucu modelin doğrulandığını göstermez; bilimsel yöntem ve kanıt değerlendirmesi için karşılaştırma zemini sağlar.

## Newroza Kawa bağlantısı
Bilim, hukuk, eğitim, Rabûn yönetimi, Mabûn Ekonomi Modeli ve sanat araştırmalarında iddia türleri ayrı tutulmalıdır. Tabiata uygunluk, Mabûn Ekonomi Modeli'nin adı değil açıklayıcı benzerlik ilkesidir; kendiliğinden ampirik kanıt değildir.

## Kalite durumu
**K0 açık:** özgün DOCX paragraf eşlemesi. **K1 kısmi:** karşılaştırmalı literatür. **K2 kısmi:** sınıflandırma yöntemi. **K3–K6 açık:** uygulama verisi, dış geçerlik, etik ve bağımsız denetim. **Yayıma hazır değildir.**

## Kaynak izi
- `6-Bilim (1).docx`, kurucu özgün metni.
- `zanistarast-papers/docs/architecture/ZANISTARAST_MIRA_MASTER_ROADMAP.md`.
- `zanistarast-papers/reference-implementation/mira/src/zanistarast_scientific_mission.rs`.

## Ek: Rasterast iddia turu ve kaynak denetimi (22.10.2026)

Bu bolum mevcut uc eksenli siniflandirmayi `RASTERAST-02-KAYNAK-KANIT-BAGIMSIZLIK-DENETIM-PROTOKOLU.md` ile karsilastirir. Ozgun `6-Bilim (1).docx` metninin tam paragraf denetimi yapilmamistir. Asagidaki kodlar arastirma kaydidir; Mira yaziliminin onayli alanlari degildir.

| Kod | Iddia | Tur | Kaynak ve durum |
|---|---|---|---|
| BL-01 | Altinci kozmik boyutun evreleri hesap/hukum ve hukmun sonucudur | Kurucu ontolojik/teolojik tanim | 16.10.2026 tarihli kurucu onayli 6 boyut / 12 evre tablosu; kaynakta dogrulandi, deneysel kanit degil |
| BL-02 | Kor ikinci degerlendirme belirli hata turlerini azaltabilir | Ampirik hipotez | RASTERAST-02 pilot tasarimi; deney henuz yapilmadi |
| BL-03 | Hukum Meclisi altinci kozmik boyutun birinci evresine ozdestir | Kategori esitlemesi | Kurucu tablo ve kurumsal metinler bu ozdesligi desteklemez |
| BL-04 | Mabun Ekonomi Modeli ihtiyac erisimini iyilestirir | Ampirik kurumsal hipotez | Model adi kanonik; etki verisi bulunmuyor |

Kaynakla uyum, bir onermenin kurucu metinde yer aldigini gosterebilir; tek basina deneysel dogruluk saglamaz. Ayni kaynagi tekrar okuyan iki kisi bagimsiz kaynak dogrulamasi yapmis sayilmaz. Ortak veri, yontem ve alinti bagimliligi kaydedilmelidir. K0 kaynak kapisinin tamamlanmasi K1-K6 kapilarinin tamamlandigi anlamina gelmez.

Karsilastirmali dis kaynak: Reiss ve Sprenger, Scientific Objectivity, Stanford Encyclopedia of Philosophy (2020 esasli revizyon): https://plato.stanford.edu/entries/scientific-objectivity/ . Bu kaynak Zanistarast'in kurucu iddialarini dogrulamaz.

**Acik is:** Ozgun bilim DOCX paragraf eslemesi, bagimsiz ikinci okuma ve ampirik sinamalar. **Yayima hazir degil.**

## Ozgun bilim belgesi kimlik denetimi (22.10.2026)

Bagli Google Drive uzerinde `6-Bilim (1).docx` tam adiyla arama sonuc vermedi. `Bilim` aramasinda ise `7-Bilim.docx` adli 32515 baytlik bir belge ve ayni adla kopyalar goruldu. Ozellikle `7-Bilim.docx` (Drive kimligi `14oSElIHPtjTjMRna0zZXTS9n7xt3ACFM`) 25.12.2025 tarihli; diger kopyalar 2026 tarihlidir. **Bu iki dosya adinin ayni eseri temsil ettigi dogrulanmadi.** Yalnizca ad benzerliginden kaynak ozdesligi kurulamaz; 7-Bilim belgesine 6-Bilim icin paragraf numarasi atfedilmez.

Sonraki K0 kontrolu: her iki belgenin varsa icerik karmasini, ilk basligini, bolum yapisini ve paragraf dizisini karsilastirmak; uyusma yoksa ayri eserler olarak kaydetmek. Bu turda Drive dosyasinin tam metni okunmadi. **Ozgun DOCX paragraf eslemesi halen acik, yayin hazirligi tamamlanmadi.**
