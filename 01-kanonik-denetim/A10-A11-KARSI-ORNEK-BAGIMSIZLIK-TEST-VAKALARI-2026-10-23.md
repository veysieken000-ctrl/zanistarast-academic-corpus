# A10–A11: karşı örnek ve bağımsız denetim test vakaları

23 Ekim 2026. Bu test vakaları sentetiktir; gerçek kurumlar hakkında ölçüm, istatistik veya deneysel doğrulama değildir. Dayanak: A10 ve A11 araştırma taslakları ile A10–A11 biçimsel sınama notu. Hedef, makalelerin farklı çıktılarının gerçekten ayırt edilebilir olup olmadığını denetlemektir.

## Test tasarımının sabitleri
A10: `Y,G,H,I,D` sırasıyla yetki sınırı, gerekçe, hak/zarar değerlendirmesi, itiraz ve düzeltme alanlarıdır. `P=Y∧G∧H∧I∧D` yalnız önerilen **prosedürel asgari koşul** olarak kullanılır; `P=1` gerçek meşruiyet kanıtı değildir. Alanın kayıtlı olması ve fiilen işlemesi farklıdır.

A11: `reach`, `appeal`, `independent`, `latency` türlenmiş bilgi akış grafının ölçümleridir. `reach=1` mesajın ulaşmasıdır, mesajın doğru olduğu anlamına gelmez. `independent=1` de ancak önceden tanımlanmış çıkar ve ortak kaynak koşullarına göre değerlendirilebilir.

## Ayrıştırıcı sentetik vakalar
| Vaka | A10 normatif soru | A11 ağ/denetim sorusu | Beklenen bulgu |
|---|---|---|---|
| V1 Biçimsel itiraz | İtiraz kanalı kâğıt üzerinde var ama yaptırım korkusu nedeniyle kullanılamıyor | Kenar var, fiilî `appeal=0` | Kayıtlı prosedür, işlerlik değildir |
| V2 Yanlış gerekçe | Beş prosedür alanı dolu; gerekçe bilerek yanlış bilgiye dayanıyor | `reach=1`, `provenance` zayıf | Erişim doğruluğu veya meşruiyeti ispatlamaz |
| V3 Ortak kaynak | İki denetçi aynı hatalı raporu onaylıyor | İki düğüm ama tek kök kanıt | Onay sayısı bağımsız kanıt sayısı değildir |
| V4 Hızlı merkez | Merkez açık gerekçe ve hak değerlendirmesi sunuyor | `latency` düşük; çevre bilgisi filtreleniyor | Hız bilgi bütünlüğü yerine geçmez |
| V5 Dağıtık tıkanma | Katılım var, sonuçtan kimin sorumlu olduğu belirsiz | Çok sayıda yatay kenar, karar yolu yok | Dağıtıklık tek başına hesap verebilirlik değildir |
| V6 Adil ilke, bozuk ağ | Normatif ilke gerekçeli | Çevreden merkeze itiraz yolu kesik | A10'un ilke düzeyi A11'in işleyişini garanti etmez |
| V7 İyi ağ, haksız karar | Bilgi ve itiraz yolları güçlü | `reach=1`, düşük `latency` | A11'in iyi işlemesi A10'un normatif meşruiyetini garanti etmez |

## Açık mantıksal ayrım
`P(q)=1` ancak tanımlanan beş prosedürel kaydın sağlandığını ifade eder. `P(q)=1 ⇒ Legitimate(q)` **kurulmamıştır**. `reach(p,q)=1 ⇒ Correct(q)` **yanlıştır**. `two_approvals(q) ⇒ two_independent_sources(q)` ortak kaynak grafı bilinmeden kurulamaz. Bu negatif testler biçimsel ayrımı güçlendirir, kuramı ampirik olarak kanıtlamaz.

## Mira için yürütülebilir test veri şeması önerisi
Her vaka `case_id`, `article_id`, `claim`, `input_assumptions`, `expected_failure`, `evidence_status`, `independence_graph`, `rasterast_review`, `founder_decision` alanlarıyla saklanmalı. Önce sentetik örneklerde mantık testleri, sonra izinli/anonimleştirilmiş kurum verileriyle dış geçerleme planlanmalı. Bu turda kod testi veya gerçek veri analizi yapılmamıştır.

## Kalite kapıları
A10: normatif teorilerle karşılaştırma ve gerekçeli yetki ölçütleri açık. A11: graf verisi, bağımsızlık testi, gözlemlenebilir ölçüm ve sonuç düzeltme süreleri açık. İki aday `BAGIMSIZ-EKSIK`; gerçek tekrar kararı yok. K0–K6 ve 412 makale yayın kilidi sürer.
