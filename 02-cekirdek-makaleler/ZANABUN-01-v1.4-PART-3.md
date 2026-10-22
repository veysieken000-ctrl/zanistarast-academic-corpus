# ZANABUN-01 v1.4 — III. Kesin sonuçlar ve karşı örnekler

Bu bölüm [I](ZANABUN-01-v1.4-PART-1.md), [II](ZANABUN-01-v1.4-PART-2.md), [IV](ZANABUN-01-v1.4-PART-4.md) ile tek makaledir.

## 6. Kurgusal kesin hesap

n_A=7, n_B=1, ω²=1/4, τ²=4, σ²=1 seçilirse v_A=29/7 ve v_B=5 olur. **Bunlar gerçek veri değildir.** c_üst=4 uygulanabilirdir: 16 < (29/7)·5.

| Senaryo | a | b | c_üst | t* | En kötü MSE | A-tek MSE |
|---|---:|---:|---:|---:|---:|---:|
| v1.3 özel durum | 0 | 10 | 0 | 29/764 | 809/191 | 123/28 |
| İki yanlı, ilişkisiz | 1 | 3 | 0 | 15/92 | 116/23 | 151/28 |
| Eşit yanlılık | 2 | 2 | 0 | 29/64 | 417/64 | 235/28 |
| Ortak kök belirsizliği | 1 | 3 | 4 | 0 | 151/28 | 151/28 |
| B yanlı + ortaklık | 0 | 10 | 4 | 1/708 | 1555/354 | 123/28 |
| İki yanlı + ortaklık | 2 | 3 | 4 | 0 | 235/28 | 235/28 |
| Yanlılık yok + ortaklık | 0 | 0 | 4 | 1/8 | 35/8 | 123/28 |

a=1,b=3,c_üst=0 için A=36/7, B=14, C=3, D=92/7, t*=15/92 olur. Yalnız c_üst=4 yapılırsa C=7>A=36/7 ve t*=0'a düşer. Eşit yanlılık sınırlarında ise t*=29/64 pozitif kalır. Böylece “ayrı ikinci kaynak her zaman katkı yapar” ve “iki yanlı kaynak asla birleşmez” aşırı genellemelerinin ikisi de yanlıştır.

## 7. Tam aritmetik ile yeniden üretim

Python 3 komutu: python3 07-deneyler-ve-karsi-ornekler/zanabun01_v14_dual_bias_covariance_exact.py. Kod yalnız fractions.Fraction ve itertools.product kullanır; dış veri ve rastgelelik yoktur. Kaynak düzeyindeki risk ile 7+1 raporun **64 kovaryans çiftini** doğrudan toplayan ayrı hesap karşılaştırılır. Dört yanlılık işareti, iki kovaryans ucu, 1001 rasyonel ağırlık, v1.3 özel durumu ve ortak kayma özdeşleşemezliği assert ile sınanır. Beklenen sonuç: “PASS: seven scenarios, exact 8x8 covariance, endpoint grid, identifiability”. Bu bağımsız insan deneyi değil, model içi çapraz kontroldür.

## 8. Yanlışlayıcı karşı örnekler

**Ortak kök:** c_üst=0 varsayılıp gerçek kalibrasyonda c≈4 saptanırsa 15/92 ağırlığının minimaks güvencesi bağlamda geçersizleşir. **Eşit yanlılık:** a=b=2,c_üst=0 durumunda B'yi dışlamak zorunlu değildir. **Mutabakat:** θ=0 iken dört rapor 5 ise iç varyans 0, dış hata 5'tir (v1.0'dan eski örnek). **Özdeşleşebilirlik:** θ+α ve θ+β raporları, her h için θ'=θ+h, α'=α−h, β'=β−h altında değişmez. Ortak kalibrasyon kullanan dış referans bu sorunu otomatik çözmez.

Doğrusal akış özgün kaynak → model → ispat → kesin tablo; dairesel denetim tablodan geriye a/b sınırları, c_üst, ortak cihaz/yazılım, sabit hedef, kör referans, veri sızıntısı ve seçici raporlamayı araştırır. Tek bir mutabakat bu rakip açıklamaları ayıramaz.
