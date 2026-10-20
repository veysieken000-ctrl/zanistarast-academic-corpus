## 6. Yeniden üretilebilir sentetik deney ve sonuçlar

Bağımsız deney dosyası: [ZANABUN-01-bagimsiz-yontem-deneyi.py](../07-deneyler-ve-karsi-ornekler/ZANABUN-01-bagimsiz-yontem-deneyi.py). Yalnız Python standart kütüphanesi kullanılır. Sabit tohum 20261021; her koşulda 20.000 sentetik tekrar; toplam 16 gözlemci; bireysel hata standart sapması 1, yöntem düzeyindeki hata standart sapması 2. Küresel hata ilgili koşulda standart sapma 1'dir. θ=0 tasarım gereği bilinir.

21.10.2026 tarihli yerel çalıştırma, deterministik karşı örnekleri, tanımlanabilirlik dönüşümünü ve analitik-sentetik hata toleranslarını başarıyla denetledi. Çalıştırma komutu: python3 07-deneyler-ve-karsi-ornekler/ZANABUN-01-bagimsiz-yontem-deneyi.py .

| Tasarım | Bağımsız yöntem m | Sentetik RMSE | Analitik RMSE |
|---|---:|---:|---:|
| Tek yöntem, 16 gözlemci | 1 | 2.0107 | 2.0156 |
| Dört yöntem, dörder gözlemci | 4 | 1.0362 | 1.0308 |
| On altı yöntem, birer gözlemci | 16 | 0.5627 | 0.5590 |
| On altı yöntem ve küresel ortak hata | 16 | 1.1471 | 1.1456 |
| Ortak hatasız kontrol | 1 | 0.2505 | 0.2500 |

İlk üç koşulda toplam gözlemci sayısı sabittir. Yöntem hatalarının birbirinden bağımsız olduğu **model varsayımı** altında yöntem sayısı arttıkça RMSE düşer. Dördüncü koşul, tüm yöntemlerin paylaşabileceği küresel hata G eklendiğinde kazancın sınırlı olduğunu gösterir. Beşinci koşulda ortak hata yoktur ve sırf yöntem çoğaltmak ek yarar sağlamaz.

Bu deney bir doğa gözlemi, insan katılımcı araştırması veya teolojik test değildir. Kodun analitik öngörüyle uyumu yalnız matematiksel uygulamanın iç denetimidir. Gerçek tanıkların Gaussian veya bağımsız olduğu kanıtlanmış değildir.

## 7. Saha araştırması için ayırt edici sınama

Henüz yürütülmemiş bir ölçüm çalışmasında, aynı niceliği ölçen iki veya daha fazla ayrı kalibrasyon zinciri ve mümkün olduğunca kör ölçüm operatörleri kullanılmalıdır. Ölçüm birimi, koşullar, referans belirsizliği, örneklem büyüklüğü ve hedef hata farkı **veri toplanmadan önce** belirlenmelidir. Ölçüm sırası ve çevresel koşullar rastgeleleştirilmeli; gruplar eşit kaynak maliyetinde karşılaştırılmalıdır.

Birincil sonuç: belirsizliği belgelenmiş dış referansa göre kare hata. İkincil sonuçlar: iç varyans, yöntemler arası kovaryans, belirsizlik kalibrasyonu ve maliyet. Negatif kontroller: ortak kalibrasyon hatası ve yöntemler arası gizli bağımlılık. Yöntem çeşitliliği önceden belirlenen ölçütlerde kazanç sağlamazsa önerilen ampirik alt hipotez zayıflar. Başarısız sonuçlar, dışlanan ölçümler ve protokol sapmaları raporlanmalıdır.

**Durum:** Saha verisi yoktur; insan deneyi veya etik kurul izni alınmış olduğu ileri sürülmez. Gerçek referansın hatasız olduğu varsayılmamalıdır.
