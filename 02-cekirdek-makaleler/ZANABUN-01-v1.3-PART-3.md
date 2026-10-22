# ZANABUN-01 v1.3 — III. Kesin sonuçlar, karşı örnekler ve ikinci denetim

Bu bölüm [I](ZANABUN-01-v1.3-PART-1.md), [II](ZANABUN-01-v1.3-PART-2.md) ve [IV](ZANABUN-01-v1.3-PART-4.md) ile tek araştırma makalesidir.

### 6. Kesin kurgu deneyi

`n_A=7`, `n_B=1`, `omega2=1/4`, `tau2=4`, `sigma2=1` seçilsin. Bu durumda `v_A=29/7`, `v_B=5`. **Bunlar gözlenmiş ölçüm veya insan davranışı verisi değil, matematiksel olarak seçilmiş sayılardır.** Yanlılık sınırı `d` değişirken, [II]'deki (2)–(3) formüllerinden:

| d | B'nin minimaks ağırlığı | Minimax en kötü MSE | B ağırlığı 29/64 alınırsa en kötü MSE |
|---:|---:|---:|---:|
| 0 | 29/64 | 161/64 = 2.515625 | 2.515625 |
| 1 | 29/71 | 767/284 ≈ 2.700704 | 2.720947 |
| 2 | 29/92 | 71/23 ≈ 3.086957 | 3.336914 |
| 5 | 29/239 | 3719/956 ≈ 3.890167 | 7.648682 |
| 10 | 29/764 | 809/191 ≈ 4.235602 | 23.047852 |
| 20 | 29/2864 | 12461/2864 ≈ 4.350908 | 84.644531 |

A'yı tek başına kullanmanın riski `omega2+v_A=123/28≈4.392857`'dir. Ondalıklar yuvarlanmıştır; doğrulama **kesin kesirlerle** yapılır.

### 7. Modelin kendi iddiasını sınayan karşı örnekler

**K1 — Bağımsız ama yanlı kaynak:** B'nin rastgele hatası bağımsız kalsa bile `d=10` olduğunda yanlılığı yok sayan `29/64` ağırlığı 23'ün üzerinde en kötü MSE verir. A-tek riski 4.393 iken “bağımsız” etiketinin tek başına doğruluk garantisi yoktur.

**K2 — Gizli ortak kök:** B ile A'nın küme hataları tamamen ortak olsun: `c=tau2=4`, `d=0`. (4)'ün minimizeri `t=1/8`, risk `35/8=4.375` olur. Bağımsızlık varsayımıyla seçilen `t=29/64` ise `2303/512≈4.498047` verir. İki kaynak adının bulunması iki ayrı kalibrasyon zinciri bulunduğunu göstermez.

**K3 — Mutabakat doğruluk değildir:** `theta=0` iken dört raporun hepsi 5 olsun. Raporlar arası varyans sıfır, dış hata 5'tir. Bu, v1.0'ın eski karşı örneğidir; yeni bir keşif diye sayılmaz.

**K4 — A kaynağı da yanlı olabilir:** A'nın sabit `a` yanlılığı varsa tahminin kare yanlılığı `[(1-t)*a+t*delta]^2` olur. Bu durumda (2)'deki tek-yanlılık varsayımı ve garantisi artık geçerli değildir.

**K5 — Hedef zamanla değişebilir:** A ve B aynı anda farklı hedef durumlarını ölçüyorsa sabit `theta` varsayımı bozulur; rapor ayrılığı hata değil gerçek değişim olabilir.

### 8. Tekrar üretim ve doğrusal–dairesel denetim

Araştırma dalında `python3 07-deneyler-ve-karsi-ornekler/zanabun01_bias_robust_exact.py` komutunu çalıştırın. Yalnız Python standart kütüphanesindeki `fractions.Fraction` kullanılır. Kod altı `d` değerini kesin kesirlerle hesaplar, her satır için 8 raporun **64 kovaryans çiftini** doğrudan toplar, `delta=±d` uçlarını ve 1001 aday ağırlığı denetler; ayrıca `c=4` bağımlılık karşı örneğini sınar. Beklenen son satır: `PASS: exact bias-robust identities and correlated-source counterexample`. İki hesap yolu aynı varsayımları kullanan **yazılım çapraz denetimidir**; bağımsız insan hakem veya gerçek saha deneyi değildir.

**Doğrusal derinleşme:** kaynak ifadesi → model → varsayımlar → türev → optimum → kesin tablo. **Dairesel karşı denetim:** tablodaki iyileşmeden geriye doğru `d` sınırının dayanağı, `c` kovaryansı, A'nın yanlılığı, hedefin kararlılığı ve referansın bağımsızlığı sorgulanır. Ortak hata arama, önerilen karar kuralını dogmatik bir “doğruluk formülü”ne dönüştürmemek için zorunludur.

### 9. Sonuçların yorum sınırı

B'ye çok az sayısal ağırlık verilmesi, B'nin araştırma sürecinde önemsiz olduğunu göstermez: B, yeni bir hata mekanizmasını açığa çıkarabilir. Bir tahmin edicideki ağırlık ile insanın ikinci bilen olarak epistemik ve ahlaki sorumluluğu farklı kavramlardır. Dolayısıyla (2) Zanabûn'un ontolojik bütünlüğünü değil, yalnız belirtilen hata sınıfında **ölçüm sonucunun birleştirilmesini** ele alır.
