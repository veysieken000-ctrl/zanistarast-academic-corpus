# MK-016 — H02/H03 gerçek metin kaynak-soyağacı pilotu

Tarih: 23 Ekim 2026. Durum: **metinlerde açıkça görülen atıfların yapısal denetimi**. Haricî kaynakların içerikleri burada yeniden doğrulanmadı; bağımsız Rasterast bekliyor.

## İncelenen sürümler

- H02: `02-cekirdek-makaleler/NK-ZS-H02-A04-TR-v02-IKINCI-YEK-IKINCI-BILEN.md`; pilot sırasında okunan Git blob `f6976f89a73c2c56ede63387d305b8649baf1b51`. Bölümler: “Kaynaklar”, “Ek C — Özgün metin karşılaştırması”, “Terminoloji güncellemesi”.
- H03: `02-cekirdek-makaleler/NK-ZS-H03-A14-TR-v02-RASTERAST-BIRIKIMLI-KANIT-DENETIMI.md`; pilot sırasında okunan Git blob `0a1d2ac3e68a3d59b7b22d5c3517f232ff4264e6`. Bölümler: “Ek C — Özgün kaynak izi”, “Ek D — Kurmancî terimlerin Rasterast denetimi”.
- Pilot kod: `01-kanonik-denetim/mk016_kanit_bagimlilik.py`; test: `test_mk016_kanit_bagimlilik.py`.

## Metinde gerçekten görülen ortak kaynaklar

| Kaynak soyu | H02 izi | H03 izi | Yapısal çıkarım |
|---|---|---|---|
| `SRC-CANON-20261022` | “Kaynaklar”: `EHAD-YEK-IKINCI-YEK-TUREME-KURUCU-KANON-2026-10-22.md` | “Kaynaklar” içindeki aynı kurucu kanon dosyası | Aynı kurucu metne atıf, iki bağımsız ontolojik doğrulama sayılmaz |
| `SRC-H01-V03` | “Kaynaklar”: H01 Hebûn v03 | “Kaynaklar”: H01 v03 | H01'e iki atıf, iki ayrı ontolojik kaynak değildir |
| `SRC-ORIGINAL-AKIL` | “Ek C”: *Akıl ve Bilginin Kaynağı* P5/P43, özgün Word bağlantısı | “Ek C”: aynı özgün Word dosyasından P5/P43 tartışmasının H02'ye yönlendirildiği yazılı | H03'ün H02 üzerinden aktardığı değerlendirme, bağımsız yeni bir özgün belge değildir |
| `SRC-DIYANET-NISA` | “Kaynaklar”: Nisâ 4:1 Diyanet tefsiri | “Kaynaklar”: aynı tefsir URL'si | Ortak tefsir bağlantısı, bağımsız iki teolojik kaynak değildir |
| `SRC-TERM-20261023` | “Terminoloji güncellemesi”: `IKINCI-BILEN-DUZEY-AYRIMI-KAVRAM-TASLAGI-2026-10-23.md` | “Ek D”: aynı terim kaydına açık atıf | Terim kaydı iki makalede kullanılmış; iki ayrı dilsel doğrulama yapılmış sayılmaz |

## Bağımlılık zinciri ve ilk denetim

Örnek yönlü grafik: `SRC-ORIGINAL-AKIL → H02(Ek C) → H03(Ek C)`; ayrıca `SRC-CANON-20261022 → H02` ve `SRC-CANON-20261022 → H03`. Bu oklar metinlerin **atıf ilişkisini** temsil eder; H03'ün özgün Word'ü hiçbir zaman doğrudan görmediği anlamına gelmez. H03 Ek C, iki özgün Word dosyasının okunduğunu da bildirir; bu nedenle H03'ün kaynak erişimi ile H02'den alınan yorumu ayrı değerlendirilmelidir.

**MK-019 keşif adayı — Kaynak erişimi ≠ yorum bağımsızlığı.** İki yazar aynı birincil kaynağı doğrudan okuyabilir; bu, onların yorumlarının birbirinden bağımsız olduğu anlamına gelmez. Tersi de geçerlidir: ortak veri kullanımı iki farklı yöntemin bütün eleştirel değerini ortadan kaldırmaz. Veri kaynağı, metne erişim, yorum zinciri, yöntem ve onay bağımsızlığı ayrı etiketlenmelidir.

**MK-020 keşif adayı — Atıf tekrarı ≠ kanıt çoğalması.** Birincil belgenin H02 ve H03'te iki kez anılması, o belgenin kanıt sayısını artırmaz. Kanıt çoğalması iddiası için bağımsız birincil malzeme veya bağımsız sınama türü gerekir. Aynı metnin farklı yöntemlerle eleştirisi ayrıca yararlı olabilir; ancak bu “iki ayrı veri kaynağı” değildir.

## Sonuç, sınırlamalar ve sonraki uygulama

1. **Gerçek metin izi bulundu:** H02 ve H03'ün yukarıdaki beş ortak kaynak ailesine atıf yaptığı, dosyaların ilgili bölümlerinde görülüyor.
2. **Bağımsızlık kanıtlanmadı:** Ortak atıf tek başına aynı hatanın gerçekleştiğini göstermez; iki metnin bağımsız değerlendirme kalitesi ayrıca sınanmalıdır.
3. **Sonraki uygulama alanları:** İnsan Tarihi'nde ortak arşiv anlatıları; Jeoloji'de ortak ölçüm/veri setleri; H05'te ortak eğitim kümesi. Önce gerçek kaynak kimlikleri çıkarılmalı; temsili D1/D2 test örnekleri gerçek kaynakmış gibi gösterilmemelidir.
4. **Hızlanma rampasına henüz aktarılmadı:** MK-019–020 yalnızca inovasyon havuzu adaylarıdır. Uygulama ölçümü, bağımsız Rasterast ve kurucu onayı beklenir.

Kanonik sınır: İkinci ontolojik Yek ile ikinci epistemik bilen ayrıdır; kurucu teolojik iddia ile ampirik kanıt ayrı değerlendirilir. 412 makale, K0–K6 ve yayın kilidi korunur.
