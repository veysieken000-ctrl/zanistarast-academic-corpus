# HEBÛN-02 v0.2 — II. Tipli model ve çıkarılamazlık ispatları

[I. Kaynak](HEBUN-02-v0.2-PART-1-KAYNAK-VE-KURAM.md), [III. Karşı örnekler](HEBUN-02-v0.2-PART-3-KARSI-ORNEKLER.md), [IV. Etik ve kalite](HEBUN-02-v0.2-PART-4-YONTEM-ETIK-KALITE.md) ile **tek makaledir**.

## 4. İddia ve kanıt türleri

Her sav `(kimlik, kaynak_blob, pasaj, tür, kapsam, karşı_örnek, durum)` olarak tutulur. Türler: **T** teolojik/kurucu; **O** ontolojik-felsefi; **A** analoji; **F** biçimsel; **E** ampirik; **N** normatif. T/O/A'dan E'ye geçiş için gözlenebilir değişken ve bağımsız veri köprüsü gerekir. Matematiksel ispat yalnız açık aksiyomlar altında geçerlidir.

Ayrık nesne tipleri: `D` kozmik boyut; `S` kozmik evre; `H` insan katmanı; `X` ampirik örnek; `P` kurucu ilke; `Q` sav. İlişkiler `evresi:S×D→Bool`, `insan_katmani:H→Bool`, `ornektir:X×S→Bool`, `kapsar:D×D→Bool`, `turu:Q→{T,O,A,F,E,N}`. Bu **bizim biçimsel analiz aracımızdır**, kurucunun yeni kanonik aksiyomu değildir.

| Boyut (D) | Evre 1 (S) | Evre 2 (S) | Epistemik sınır |
|---|---|---|---|
| Fizik | atom | yıldız–gezegenler | ontolojik sınıflama; fiziksel örnekler ayrıca test edilir |
| Biyoloji | tek hücreliler | çok hücreliler | ontolojik sınıflama; biyolojik olgular ayrıca test edilir |
| Zihin | zekâ | akıl | felsefi-işlemsel ayrım; ölçüm gerekli |
| Ruh | ruh | melekler | teolojik/ontolojik |
| Ahlak | fıtrî | iradeli | ontolojik/normatif |
| Hüküm–ahiret | hesap/hüküm | hükmün sonucu | Core 01 kaynak varyantı; teolojik |
| Yek | evre değil | yaratılmış boyut değil | kurucu ilke |

Core 13 insan dizisi **fizik, biyoloji, zihin, ahlak, akıl, duygu + öz** ayrı H tipindedir. Öz, Yek'in tanımı değildir. Kurucu beyan aynen: **Ehad Yek'tir ve Ehad âlemlerdeki her şeyi Yek'e göre yaratmıştır; her kar tanesi, her parmak izi dahil.**

## 5. Kapsama ile küme içerme ve tarih ayrımı

Kurucu kapsama zinciri K: `kapsar(Biyoloji,Fizik)`, `kapsar(Zihin,Biyoloji)`, `kapsar(Ruh,Zihin)`, `kapsar(Ahlak,Ruh)`. Geçişlilik eklenirse `kapsar(Ahlak,Fizik)` gibi sonuçlar türetilir. Kapsama **ontolojik açıklama bağımlılığı** olarak okunur; her biyolojik varlığın bütün fiziksel varlıkları içerdiği veya ruhun ölçülmüş fizik yasası olduğu anlamına gelmez. Hüküm/ahiret fiziksel kapsama aksiyomuna sessizce dönüştürülmez. “Birinci/ikinci evre” isimleri tek başına bütün varlıklar için zaman kronolojisi veya zorunlu soy ağacı vermez.

## 6. Önerme 1 — kapsama zaman sırasını gerektirmez

**Sav:** K'dan “bütün fiziksel örnekler bütün biyolojik örneklerden daha eskidir” sonucu çıkarılamaz.

**Karşı-model ispatı:** Sabit D, K ilişkileri ve `X={x,y}` olsun. x atom, y tek hücreli örneği diye etiketlensin. M modelinde `t(x)=1,t(y)=2`; M' modelinde `t(x)=3,t(y)=2` olsun. K aksiyomlarında zaman fonksiyonu t geçmediğinden iki model K'yı aynı biçimde sağlar; fakat hedef zaman cümlesi M'de doğru, M'nde yanlıştır. Mantıksal sonuç bütün modellerde doğru olmalıdır; dolayısıyla sonuç K'dan türetilemez. **QED.** Modellerin gerçek evren kronolojisi olduğu iddia edilmez.

## 7. Önerme 2 — kozmik evre tablosu insan katmanlarını belirlemez

`D,S,evresi,kapsar` aynı tutulsun. M'de `H={fizik,biyoloji,zihin,ahlak,akıl,duygu,öz}`, M'nde `H={h1,h2}` seçilsin. Kozmik aksiyomlarda H için zorunlu içerik veya `S→H` eşlemesi bulunmadığından iki model de kozmik öncülleri sağlar; fakat insan katmanları farklıdır. Demek ki insan katmanları kozmik aksiyomlardan **çıkmaz**; Core 13 ayrı kaynak olarak okunmalıdır. **QED.** “Core 13'te altıncı katman duygu; o hâlde kozmik altıncı boyut duygu” ifadesi tip hatasıdır.

## 8. Önerme 3 — tek merkez evrenselliğine karşı-model

Yönsüz dört-düğüm çevrim `V={0,1,2,3}`, `E={(0,1),(1,2),(2,3),(3,0)}` olsun. Her düğümün derecesi 2, normalize derece-merkeziliği `2/(4−1)=2/3` olur. Bu ölçüte göre **benzersiz merkez yoktur**. Güneş/gezegen veya kalp/dolaşım analojisinden bütün ağlarda tek merkez sonucu çıkmaz. Bu ispat bütün merkez tanımlarını reddetmez; başka ölçüt öne sürülürse önceden tanımlanmalı ve yeni sınama yapılmalıdır. Kıble ontolojik ilkesi ile benzersiz geometrik ağ merkezi farklı iddialardır.

## 9. Mantıksal sonucun sınırı

Üç önerme 6+Tek'in gerçek dünyada doğrulandığını veya bütünüyle yanlışlandığını göstermez; yalnız bazı sonuçların **mevcut aksiyomlardan çıkarılamadığını** kanıtlar. Ehad/Yek, ruh, melek, yaratılış ve ahiret matematiksel veya deneysel sonuç gibi sunulmaz. İnsanın iradeli ahlakı atomun fıtrî işleyişiyle özdeş değildir. Doğrusal kapsama ile dairesel karşı denetim birlikte işler.
