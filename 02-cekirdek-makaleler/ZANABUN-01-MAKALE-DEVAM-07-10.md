# ZANABUN-01 — Makalenin Devamı: Bölüm 7–10

**Bu dosya ayrı bir makale değildir.** Tam makalenin 1–6. bölümleri 'ZANABUN-01-BAGIMSIZ-DOGRULAMA-ORTAK-HATA-TAM-MAKALE.md' dosyasındadır. Bu dosya aynı ZANABUN-01 v1.0 metninin devamıdır. Kaynakça, ekler ve denetim kaydı aynı kimlikli ek dosyadadır.

## 7. Yanlışlama planı, alternatif açıklamalar ve itirazlar

**H1 — bağımsız kümeler.** Aynı bireysel hata düzeyi ve sabit tanık sayısında, yöntem-kümesi etkisi gerçekten bağımsız ve \(\tau_c^2>0\) ise dengeli daha çok küme dış ölçüt RMSE'sini azaltmalıdır. Gerçek veride kümeler arası bağımsızlık varsayımı bozulursa öngörü geçerli olmayabilir.

**H2 — görünür uyum.** Tek kümede tanıklar arası varyans, küresel veya ortak kalibrasyon kaymasını tanılamak için yeterli değildir. Farklı izlenebilir referanslarla ölçüm yapmak, salt tanık sayısını artırmaktan daha bilgilendirici olabilir.

**H3 — tanımlanabilirlik.** Dış ölçüt bulunmadığında, \(\theta\) ile sabit yanlılık \(b\) ayrıştırılamayabilir. Bu durumda rapor “doğrulandı” değil, “verilen varsayımlarla uyumlu” olmalıdır.

**Önerilen gerçek dünya sınaması:** Bilinen standart nesnenin, tek ortak kalibrasyon protokolü ve birbirinden bağımsız izlenebilir kalibrasyon protokolleriyle ölçülmesi; sıranın rastgeleleştirilmesi; operatörlerin diğer raporlara kör tutulması; cihaz, yazılım, referans ve kalibrasyon kayıtlarının saklanması; önceden belirlenmiş RMSE, belirsizlik kapsaması ve maliyetin karşılaştırılması. Pilot varyans bileşenleri ve pratik etki eşiği olmadan örneklem büyüklüğü hesaplanamaz. **Bu gerçek dünya deneyi yapılmadı.**

**İtiraz 1 — Bağımsız yöntem daha kötü olabilir.** Evet. Yeni kalibrasyonun kendi sistematik hatası veya daha büyük özel gürültüsü varsa yöntem çeşitliliği her zaman iyi değildir. Denklem (2), diğer varyans bileşenleri sabitken geçerlidir. Maliyet, kaynak kalitesi ve uzmanlık hesaba katılmadan “çeşitlilik” reçetesi genellenemez.

**İtiraz 2 — Tek kişi de doğru bilgi üretebilir.** Evet. Tekil gözlemci doğru sonuca ulaşabilir; ikinci bilenin sınaması doğruluğun ontolojik olarak var olmasının ön koşulu değildir. Kurucu epistemik doğrulama idealinin toplumsal niteliği ile “tek kişi asla doğru bilemez” şeklindeki güçlü ampirik iddia aynı değildir.

**İtiraz 3 — Uyum varyanstan daha geniştir.** Evet. Mantıksal tutarlılık, bağlamsal uygunluk, zamansal devamlılık ve deneysel doğrulama tek sayıya indirgenemez. Karşı örnek **Zanabûn'un tamamını çürütmez**; özgün metindeki düşük-varyans temsilinin tek başına yetersizliğini gösterir.

**İtiraz 4 — Ayrı gözlemler aynı yanlış kuramı paylaşabilir.** Evet. İki cihazın kalibrasyonu ayrı olsa bile her ikisi aynı yanlış fiziksel model, veri dönüşümü veya standart varsayımını kullanabilir. Hiyerarşide bu küresel \(U\) veya sabit \(b\) bileşenidir. Köken haritası bunu yakalayamadığında “bağımsızlık” yalnız yüzeysel kalır.

**İtiraz 5 — Dış gerçek değere erişim her zaman mümkün değildir.** Evet. Tarih, kozmoloji, ahlak veya metafizikte doğrudan altın standart bulunmayabilir. Farklı öngörülerin ayrıştırılması, rakip açıklamaların belirtilmesi ve belirsizliğin korunması gerekir. Sayısal ölçüm modeli bütün bilgi türlerine evrensel ispat olarak taşınamaz.

**İtiraz 6 — Örneklem seçimi.** Aynı sonucu veren tanıklar seçilip farklı sonuçlar dışlanırsa gözlenen uyum yanlı olur. Ön kayıt, dışlanan raporların açıklanması ve başarısız tekrarların saklanması gerekir. Hiyerarşik model bu seçilim etkisini doğrudan temsil etmez.

## 8. Disiplinlerarası araştırma soruları

**Tarihsel belgeler:** Üç kronik aynı kayıp metni kopyalıyorsa üç bağımsız tarihsel kaynak değildir. Belge köken ağı ortak hatayı hangi koşullarda ayırt edebilir? Bu makalede arşiv verisi incelenmedi.

**Çoklu yapay zekâ ajanları:** Farklı ajanlar aynı temel modelden, arama sonucundan veya eğitim verisinden besleniyorsa görünürdeki oydaşma tekil kaynağın tekrar üretimi olabilir. Yöntem ve veri kökeni ayrışması dış test başarısını iyileştirir mi? Bu makalede AI sistemi test edilmedi.

**Rasterast ve kurumlar:** Karar denetiminde farklı meclis veya danışmanların aynı kaynağı tekrar etmesi bağımsız kanıt oluşturmayabilir. İzlenebilir kanıt kökeni ile karar kalitesi arasında hangi ilişki vardır? Rabûn, Mabûn veya Newroza Kawa kurumları bu çalışmada deneysel olarak sınanmadı.

Bunlar **ZANABUN-01'in türev araştırma sorularıdır**. Ayrı veri, özgün soru, literatür boşluğu ve sonuç olmadıkça ayrı benzersiz makale sayılmazlar.

## 9. Etik, veri ve iddia statüsü

İnsan katılımcı, gerçek kişisel veri, hayvan deneyi veya hassas kayıt kullanılmadı. Sayısal sonuçlar sentetik ve koddan yeniden üretilebilir. “30.000 tekrar” gerçek kişilerin tekrarına değil, bilgisayarın oluşturduğu yapay çekilişlere karşılık gelir. Parametreler örnek amaçlıdır; genelleme için ampirik kalibrasyon gerekir.

Metin ve yöntem geliştirmesinde ChatGPT kullanıldı; bu kullanım bağımsız insan hakemliği veya uzman imzası anlamına gelmez. Yapay zekâ yazar olarak gösterilmez. Kaynak doğruluğu, çıkar çatışmaları ve sonraki kullanımın insan sorumluluğu korunur. **Dergiye gönderim, DOI, arXiv veya ücretli işlem yapılmaz.**

**İddia sınıfları:** Ehad–Yek beyanı teolojik/kurucu; Hebûn–Zanabûn ilişkisi felsefi/ontolojik; denklem (1)–(2) tanımlı varsayımlarda matematiksel; simülasyon kodun sentetik davranışı; H1–H3 gerçek veriyle sınanmayı bekleyen ampirik önerilerdir. Bu sınıflar birbirine dönüştürülemez.

## 10. Sonuç

Tanıklar arası uzlaşma ile nesneye ilişkin doğruluk farklıdır. Ortak hata, çok sayıda aynı raporun bilgi değerini sınırlar; tek bir kaynak kümesindeki gözlemci varyansı ortak hatayı saklayabilir. Hiyerarşik model, eşit tanık sayısında gerçekten bağımsız kalibrasyon kümelerinin belirli bir hata bileşenini azaltabildiğini, fakat küresel hata ve sabit yanlılığın kaldığını gösterir. Sentetik deney bu analitik sonucun yeniden üretilebilir hesap gösterimidir.

Zanabûn'un “ikinci bilen tarafından sonucun onayı” ilkesi açısından yöntemsel sonuç, **ikinci raporun varlığı değil, ikinci sınamanın kanıt kökeni ve yanlışlama gücüdür**. Bu öneri kurucu ontolojinin matematiksel ispatı değildir; epistemik doğrulamayı daha izlenebilir ve eleştiriye açık kılan, sınırları belirtilmiş bir araştırma katkısıdır.
