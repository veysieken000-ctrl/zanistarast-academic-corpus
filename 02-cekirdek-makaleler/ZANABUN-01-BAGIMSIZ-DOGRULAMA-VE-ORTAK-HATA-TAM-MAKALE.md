# Zanabûn'da İkinci Bilenin Onayı: Mutabakat, Ortak Hata ve Bağımsız Kalibrasyonun Epistemik Sınırları

**Makale kimliği:** ZANABUN-01 | **Sürüm:** v0.2, 21 Ekim 2026 | **Tür:** Bilim felsefesi / sosyal epistemoloji / formal yöntem makalesi | **Durum:** Tam yapılı akademik araştırma metni; dış hakemlik yapılmadı ve yayıma hazır ilan edilmedi. **Yazar ve kurumsal aidiyet:** Kullanıcının nihai akademik sorumluluk beyanı olmadan atanmamıştır. **Üretim:** ChatGPT destekli bağımsız araştırma; ayrıntılı kullanım beyanı aşağıdadır. **Makale ailesi:** Eski ZANABUN-01 taslağının genişletilmiş devamıdır, ikinci bir benzersiz makale değildir.

## Öz

Birden çok gözlemcinin aynı sonucu bildirmesi, aynı hatayı paylaşmaları hâlinde doğruluğu garanti etmez. Bu makale, Zanabûn'un ikinci bilen tarafından sonucun yeniden doğrulanması ilkesini, gözlemciler arası mutabakatla özdeşleştirmeden inceler. Önce kaynak metindeki tanıklık-uyum formülasyonuyla kurucunun sonuç doğrulaması beyanı ayrıştırılır. Ardından ortak hata, kalibrasyon aileleri ve bütün ailelerin paylaştığı hata için iç içe bir ölçüm modeli kurulur. Sabit gözlemci sayısında bağımsız kalibrasyon ailelerini artırmanın yalnız aile düzeyindeki ortak hatayı azalttığı; küresel hata ve sabit yanlılığı gideremediği gösterilir. Sentetik deney analitik beklentiyi sınar. Katkı, yeni bir istatistik teoremi değil, Zanabûn'a uygulanmış sınır koşulları ve denetlenebilir doğrulama protokolüdür.

**Anahtar sözcükler:** Zanabûn; Hebûn; sosyal epistemoloji; bağımsız doğrulama; ortak hata; ölçüm belirsizliği; kalibrasyon; epistemik bağımlılık.

## 1. Giriş ve araştırma problemi

İki ayrı kişinin aynı iddiayı tekrarlaması ile iki kişinin aynı sonucu farklı yollarla sınaması arasında önemli bir epistemik fark vardır. İlkinde tanıklıkların sayısı artar; ikincisinde ise sonuca götüren yöntem, ölçüt ve hata kaynakları kısmen bağımsız olabilir. Zanabûn'un kurucu ifadesi, “Bilen öznenin bilinen nesneye yönelimi sonucu ortaya çıkan sonucun ikinci bilen tarafından onayı”dır. Burada ikinci bilenin onayladığı şey ilk bilenin statüsü değil, araştırma sonucudur. Kurucuya ait 18 Ekim 2026 açıklamasında bu onay, ikinci kişinin deney, gözlem ve akıl yürütmeyle aynı sonucu elde etmesi ve bundan düzenin devamlılığı hakkında hüküm vermesi şeklinde somutlaştırılmıştır [K2].

Buna karşılık özgün çevrimiçi Zanabûn metninde tanık raporlarının ortalaması ve varyansı kullanılarak düşük varyansın hakikat uyumuna işaret ettiği öne sürülür [K1]. Bu yaklaşım, gözlemcilerin birbirinden bağımsız hata kaynaklarına sahip olduğu açıkça varsayılmadığında, aynı yanlış kaynaktan beslenen bir topluluğun çok yüksek uyum gösterebilmesini yeterince ayırt etmez. Araştırma sorumuz şudur: **İkinci bilenin doğrulaması, hangi bağımsızlık ve dış geçerlik koşullarında yalnızca tekrar değil, daha güvenilir bir sonuç kontrolü sayılabilir?**

Bu çalışma üç katkı yapar. İlk olarak kurucu tanım, mevcut kaynak metnindeki sayısal uyum ölçüsünden ayrı bir kavramsal katman olarak korunur. İkinci olarak tek bir ortak hata yerine aile düzeyi ve tüm ailelerce paylaşılan hata ayrıştırılır. Üçüncü olarak gözlemci sayısını sabit tutan ve bağımsız kalibrasyon ailelerini değiştiren bir karşı sınama tasarlanır. Bunlar bir felsefi ilkenin matematiksel olarak kanıtlandığı iddiası değil, **o ilkenin belirli ölçüm uygulamalarının hangi durumlarda başarısız olabileceğine** ilişkin model-tabanlı sonuçlardır.

## 2. Kaynak eleştirisi ve kavramsal sınır

Zanistarast'ın özgün metni [K1], “knowledge = coherent multi-agent witnessing” yaklaşımını ve K = (1/n)ΣW_i ile tanıklar arası varyans ölçüsünü içerir. Metnin bir bölümünde yanlış bilginin yüksek varyansla ilişkilendirilmesi de önerilir. Bu, doğruluk için **operasyonel bir öneridir**; düşük varyansın tek başına yeterli koşul olduğu matematiksel olarak gösterilmemiştir. Kurucunun [K2] kaydında ise ikinci bilenin *sonucu* yeniden araştırması belirleyicidir. İki metin birbiriyle otomatik olarak aynı anlama indirgenmemelidir: istatistiksel uyum, bağımsız sınamanın yalnızca olası bir gözlenebilir belirtisidir.

Kanonik teolojik ifade aynen şöyledir: **“Ehad Yek'tir ve Ehad âlemlerdeki her şeyi Yek'e göre yaratmıştır; her kar tanesi, her parmak izi dahil.”** Bu ifade bu makalede kurucu inanç/ontolojik beyan olarak kaydedilir; örneklem ortalaması, kalibrasyon veya simülasyon yoluyla doğrulanmış bir fiziksel hipotez gibi sunulmaz. Yek, insan özü, metin birleştirme tekniği veya ayrı yaratılmış katman olarak yeniden tanımlanmaz. Hebûn'un varlık/oluş ontolojisiyle Zanabûn'un bilgi/doğrulama epistemolojisi ilişkili olsa da **gözlemcinin onayı fiziksel varlığı yaratan bir mekanizma değildir**. Bu model yalnız epistemik raporların hata yapısını inceler. Kozmik 6+Tek ile insan katmanları Core 01/Core 13 numaraları birbirine eşitlenmez; bu makalenin ölçüm modeli herhangi bir kozmik boyutu ölçtüğü iddiasını taşımaz.

## 3. Yakın literatür ve özgün katkının sınırı

Hardwig'in “Epistemic Dependence” çalışması, modern bilgide başkalarının epistemik emeğine bağımlılık sorununu ele alır (1985). Goldman'ın uzman tanıklığını değerlendirme incelemesi, çoklu tanıklığın niteliği ve güvenilirliğine dair ayrı bir tartışma zemini sunar (2001). Dietrich ve Spiekermann (2013), Condorcet geleneğindeki seçmen bağımsızlığı varsayımının çoğu gerçek bağlamda ihlal edilebildiğini ve bağımlılık hesaba katıldığında büyük gruplar için daha ihtiyatlı sonuçlar elde edildiğini gösterir. Bu çalışmaların hiçbiri burada ilk kez keşfedilen bir ortak-hata teoreminin varlığını desteklemez; tersine **epistemik bağımlılık sorununun yerleşik** olduğunu gösterir.

Metrologide NIST TN 1297, birleşik ölçüm belirsizliğinin kovaryanslar uygun şekilde dikkate alınarak hesaplanmasını ve tanınan sistematik etkiler için düzeltme uygulanmasını önerir (Taylor ve Kuyatt 1994). JCGM 100:2008 de belirsizliğin değerlendirilmesi için genel çerçeveyi verir. Bu nedenle matematiksel yenilik iddiası sınırlıdır: özgün olan, **Zanabûn'un sonuç doğrulaması söylemini bağımsız kalibrasyon aileleri, dış ölçüt ve epistemik köken denetimi ile yeniden işlemselleştiren proje içi yöntem önerisidir**. Bunun alan literatüründe önceden aynen önerilmediği henüz sistematik taramayla kanıtlanmamıştır.

## 4. Kavramlar ve varsayımlar

Hedef ölçülebilir nicelik θ olsun. i gözlemcisinin raporu W_i, dış referansın değeri θ* ve grup içi rapor varyansı S² ile gösterilsin. **Mutabakat**, küçük S²; **dış doğruluk**, |ortalama(W)-θ*| veya uygun kayıp fonksiyonu; **bağımsızlık**, tanıkların raporlarının koşullu hata yapısına ilişkin bir varsayımdır. Bu üçü birbirinin tanımı değildir. θ* ölçüm belirsizliği olan bir referans ise hata hesabında referansın belirsizliği ayrıca hesaba katılmalıdır.

Birinci varsayım (A1): Aynı niceliği ve aynı birimi ölçen raporlar karşılaştırılır. İkinci (A2): Hata bileşenlerinin ortalamaları sıfırdır; aşağıda ayrıca belirtilen sabit yanlılık b bunun istisnasıdır. Üçüncü (A3): Farklı ailelerin yerel kalibrasyon hataları birbirinden bağımsız, özel hatalar da bağımsızdır. Dördüncü (A4): Tüm ailelerce paylaşılan küresel hata bileşeni diğer bileşenlerden bağımsızdır. Beşinci (A5): Her gözlemci bir aileye aittir; aile üyelikleri veri kökeni ve kalibrasyon kayıtlarından çıkarılabilir. Bu varsayımlar gerçek kişiler için **otomatik doğru kabul edilmez**; özellikle A3 ve A5 deneysel olarak sorgulanmalıdır.

## 5. İlk karşı örnek: sıfır uyuşmazlık, yanlış ölçüm

θ = 0 ve dört gözlemci için W = (5,5,5,5) olsun. Ortalama 5, raporlar arası popülasyon varyansı 0 ve dış ölçüte göre mutlak hata 5'tir. Böylece “S²=0 ise rapor edilen değer doğrudur” önermesi yanlışlanır. Karşı örnek, Zanabûn'un kurucu sonuç-onayı ilkesini mantıksal olarak çürütmez: gerçekten bağımsız ikinci bilen, bu dört raporun aynı bozuk ölçüm aracından çıktığını araştırabilir. Çürütülen, **yalnız rapor içi uyumu hakikatin yeter koşulu yapan dar işlemsel yorumdur**.

Bir başka uç durumda, gözlemcilerin farklı raporlar vermesi de her zaman yanlış bilgilendirme değildir: heterojen ama dürüst ölçümler, farklı koşullar veya meşru ölçüm belirsizlikleri nedeniyle yüksek varyans gösterebilir. Dolayısıyla yüksek varyans yanlış bilgi için de yeterli koşul değildir. İddialar epistemik sınıflandırma bakımından çift yönlü sınanmalıdır.

## 6. İç içe hata modeli

Toplam N = Gm gözlemci, G ayrı kalibrasyon ailesi ve her ailede m gözlemci bulunsun. g ailesinin j gözlemcisi için

W_gj = θ + b + B₀ + B_g + ε_gj

yazalım. Burada b sabit ama bilinmeyen yanlılık; B₀ bütün ailelerin paylaştığı, ortalaması sıfır ve varyansı τ₀² olan hata; B_g yalnız g ailesine özgü, ortalaması sıfır ve varyansı τ² olan kalibrasyon hatası; ε_gj ortalaması sıfır ve varyansı σ² olan bireysel gürültüdür. A2–A4 uyarınca belirtilen bileşenler bağımsızdır. Ailelerin eşit büyüklükte olduğu ilk analiz için varsayılmıştır; gerçek veri eşitsizse ağırlıklar yeniden tanımlanmalıdır.

Genel ortalama T = (1/N)Σ_gΣ_j W_gj olduğundan

T − θ = b + B₀ + (1/G)Σ_g B_g + (1/N)Σ_gΣ_j ε_gj.

**Önerme 1 (model içi MSE ayrışımı).** Yukarıdaki varsayımlarla

E[(T−θ)²] = b² + τ₀² + τ²/G + σ²/N.

**Kanıt.** E[T−θ]=b. Bağımsız, sıfır ortalamalı bileşenlerin varyansları toplamı Var(T−θ)=τ₀² + G(τ²/G²) + N(σ²/N²) olur. MSE = Var + bias² özdeşliği sonucu verir. QED. Bu, standart varyans cebiridir; özgün teorem diye sunulmaz.

**Sonuç 1.** N sabitken ve G artırılabiliyorken aile düzeyindeki ortak hata katkısı τ²/G azalır; özel gürültü katkısı σ²/N değişmez. Fakat b² ve τ₀² bileşenleri aynı kalır. Bağımsız yöntem çeşitliliği ancak gerçekten **bağımsızlaşan hata bileşeni** üzerinde etkilidir.

**Sonuç 2.** G sabitken aile başına gözlemci sayısı m sonsuza gitse bile MSE → b²+τ₀²+τ²/G olur. Dolayısıyla aynı kalibrasyon zincirine yeni gözlemci eklemek, tek başına sistematik doğruluk garantisi sağlamaz.

**Sonuç 3 (yanıltıcı çoğulluk).** Bir ailedeki raporlar arasında korelasyon pozitif olduğunda bağımsızmış gibi hesaplanan standart hata küçük gösterilebilir. b=τ₀=0, tek aile ve τ>0 koşulunda gerçek ortalama varyansı τ²+σ²/N iken hatalı bağımsızlık hesabı yaklaşık (τ²+σ²)/N kullanır; N büyüdükçe iki değer arasındaki fark açılır. Bu farkı “gözlemci sayısı” değil hata bağımlılığı açıklar.

## 7. Tanımlanabilirlik: aynı veriden ne öğrenilemez?

Yalnızca bir aileden tek hedef için N rapor toplandığında, sabit b ile θ birbirinden ayrıştırılamaz: (θ,b) ve (θ+c,b−c) aynı gözlemlerin beklenen değerini verir. Birçok aile olsa da hepsinin paylaştığı **sabit** b, dış referans veya ayrı tanımlayıcı koşul olmaksızın hedef değerden ayrılamaz. Rastgele B₀ için dağılımsal bir ön model kurmak da tek bir gözlem setinden gerçekleşmiş B₀ değerini kesin olarak ortaya çıkarmaz.

Birden çok bağımsız aile ve birden çok ölçüm koşulu olduğunda aile içi/arası varyans bileşenleri hakkında daha fazla bilgi elde edilebilir; ancak bu sonuç rastgele etki modeli, yeterli tekrar ve ölçüm tasarımına bağlıdır. **Bir grafikte farklı görünen iki yolun bağımsız olduğu kanıtlanmadıkça**, aile sayısı G gerçekte olduğundan büyük sayılmamalıdır. Ortak veri seti, ortak cihaz, aynı yazılım hatası, aynı danışman kaynağı veya aynı yanlış referans tüm yolları yeniden bağlayabilir.

Önerilen köken denetimi, her sonuç için dört alan kaydeder: (i) kullanılan ham kaynak/örnek, (ii) cihaz ve kalibrasyon zinciri, (iii) analiz kodu/yöntem sürümü, (iv) dış referans ve doğrulama koşulu. Birbirini yalnızca yeniden anlatan iki tanık ayrı kalibrasyon ailesi sayılmaz. Bu kayıtlar **bağımsızlık için delil** sağlar ama tek başına olasılıksal bağımsızlığı ispatlamaz.

## 8. Sentetik karşılaştırmalı deney

Modelin denetlenebilir sonuçları için θ=0, N=16, τ=2, σ=1 seçildi. G ∈ {1,4,16}; aile başına m=N/G gözlemci kullanıldı. Küresel ortak hata standart sapması τ₀ ∈ {0,1} ve seçilmiş bir koşulda sabit yanlılık b=1 alındı. Her koşul için 12.000 sentetik tekrar, Python standart kütüphanesinin Mersenne Twister üretecinde 20261021 tohumu kullanıldı. Her tekrarda yeni küresel hata, aile hataları ve özel hatalar üretildi. Sonuç metriği, θ'ya göre örnek ortalamasının karekök ortalama karesel hatası (RMSE) idi. Kod yolu: 07-deneyler-ve-karsi-ornekler/zanabun01_independent_calibration_families.py.

| G | τ₀ | b | Sentetik RMSE | Analitik RMSE |
|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 2.0057 | 2.0156 |
| 4 | 0 | 0 | 1.0345 | 1.0308 |
| 16 | 0 | 0 | 0.5597 | 0.5590 |
| 1 | 1 | 0 | 2.2546 | 2.2500 |
| 4 | 1 | 0 | 1.4371 | 1.4361 |
| 16 | 1 | 0 | 1.1531 | 1.1456 |
| 4 | 1 | 1 | 1.7605 | 1.7500 |

Bu tablo **gerçek kişi, laboratuvar veya toplum verisi değildir**. Değerler 21 Ekim 2026'da yerel Python hesaplamasında üretilmiştir; kodun depoya alınması ve bağımsız yeniden çalıştırılması ayrıca kontrol edilir. G=1'den G=16'ya geçişte yalnız aileye özgü hata bileşeninin ortalamada seyrelmesi beklenir. τ₀=1 varken 16 ailede bile teorik RMSE 1'in altına inemez. b=1 koşulunda sabit yanlılık MSE'ye 1 ekler. Bu gözlemler analitik modelin sayısal tutarlılık kontrolüdür; Zanabûn'un ontolojik geçerliliği veya insan tanıkların davranışı hakkında ampirik kanıt değildir.

### 8.1 Önceden belirlenebilir dış doğrulama protokolü

Gerçek dünyaya taşınabilecek bir çalışma için önce hedef nicelik ve bağımsız referans yöntemi ilan edilir. Aynı sayıda ölçümle (A) tek kalibrasyon zinciri, (B) belgelenmiş bağımsız zincirler, (C) görünüşte farklı ama ortak referanslı zincirler karşılaştırılır. Ana sonuç dış referansa göre mutlak hata veya RMSE; ikincil sonuç raporlar arası uyum ve maliyettir. Deneyden önce kabul edilebilir referans belirsizliği, körleme, cihaz rastgeleleştirmesi, olası veri dışlama gerekçeleri ve istatistiksel belirsizlik yöntemi kayda geçirilmelidir. Beklenen sıralama, A3 geçerli ve ortak hata baskınsa B'nin A'dan daha düşük dış hata göstermesidir; C'nin B gibi görünmesi bağımsızlık varsayımının yanlış tanımlandığına işaret edebilir.

## 9. Alternatif açıklamalar ve güçlü itirazlar

**İtiraz 1 — tanıklık ölçüm değildir.** İnsan tanıklığında güvenirlik, anlam, niyet, öğrenme ve sosyal baskı vardır; skaler Gauss gürültüsü bunların tamamını temsil etmez. Yanıt: model, kurucu ilkenin yalnız **ölçülebilir rapor** alt durumuna uygulanır; tüm epistemolojiyi sayısallaştırdığı iddia edilmez.

**İtiraz 2 — ikinci bilenin aynı sonucu bulması yine de önemlidir.** Doğrudur. Bağımsız ve ayırt edici koşullarda tekrar, tek rapora göre kanıtı güçlendirebilir. Buradaki olumsuz sonuç “tekrar değersizdir” değil, “tekrarın değeri hata yollarının yapısına bağlıdır” biçimindedir.

**İtiraz 3 — farklı yöntemler farklı sistematik hata doğurur.** Doğrudur. Bağımsız aileler eşit varyanslı olmayabilir; bu durumda eşit ağırlıklı ortalama verimsiz, hatta bazı koşullarda daha kötü olabilir. Ölçüm kalitesi, yöntem maliyeti ve ağırlıkların önceden belirlenmesi gerekir. Çok yöntemlilik otomatik üstünlük garantisi değildir.

**İtiraz 4 — doğruluğun dış ölçütü de yanlıdır.** Doğrudur. Bir dış referans, kendi kalibrasyon zincirinin belirsizliğini ve izlenebilirliğini açıklamıyorsa yeni ortak hata kaynağıdır. Doğrulama, gerekirse ikinci bir farklı fiziksel ilke veya bağımsız referansla yeniden denenmelidir.

**İtiraz 5 — tekrarlanan sonuç nedenin tekliğini göstermez.** Doğrudur. Örneğin x_(t+1)=x_t ve x_(t+1)=x_t² modelleri x₀=1 koşulunda aynı sonsuz gözlem dizisini üretir; x₀=2 koşulu modelleri ayırır. Bu, ayrı HEBUN–ZANABUN-02 araştırmasının gözlemsel eşdeğerlik meselesidir. Burada yalnız **sonuç doğrulaması ile nedenin tanımlanması** arasındaki ayrımı vurgulamak için kullanılmıştır.

## 10. Yanlışlama koşulları, sınırlılıklar ve araştırma gündemi

Bu modelin ampirik sınaması şu durumlarda beklenenden sapabilir: aile hataları bağımsız değilse, aileler arası varyans kalibrasyonla birlikte artıyorsa, bireysel ölçümler farklı hedefleri ölçüyorsa, referans hatalıysa, hata dağılımları ağır kuyrukluysa veya sabit maliyet altında G'nin artması cihaz başına kaliteyi düşürüyorsa. Bu sonuçlar kurucu Zanabûn ilkesini değil, A1–A5 ile tanımlanan **özel modelin** uygunluğunu sorgulatır.

Bir sonraki gerçek araştırma, bilinen kalibrasyon zincirleri olan ölçüm verisi veya açık ve etik kullanımlı çok-laboratuvar karşılaştırması gerektirir. Hipotez H1: bağımsız zincirler, ortak yanlılık baskınsa aynı N'de daha düşük dış hata verir. H2: köken grafiğiyle hesaplanan bağımlılık, yalnız rapor korelasyonundan daha iyi dış hata tahmini sağlayabilir; bu iddia **henüz sınanmadı**. H3: referans ortaklığı hesaba katıldığında görünen çeşitlilik kazancının bir kısmı kaybolur. H2 için alternatif hipotez, köken kayıtlarının gerçek hata kovaryansını öngörmemesidir; kör doğrulama gerekir.

Etik açıdan bu çalışmada insan katılımcı, kişisel veri, gizli belge veya dış laboratuvar verisi yoktur. Teolojik beyanlar inanç/ontoloji sınıfında; cebirsel önermeler model içi mantıksal sonuç sınıfında; tablo yalnız sentetik hesap sınıfındadır. Araştırmanın en büyük sınırı, **gerçek Zanabûn uygulamasının bağımsız doğrulama başarısının ölçülmemiş** olmasıdır. Özgünlük de yerleşik sosyal epistemoloji ve metrologi literatürüne göre sistematik tarama tamamlanmadan kesin ilan edilemez.

## 11. Sonuç

Zanabûn'un ikinci bilen tarafından *sonucun* onaylanması fikri, raporların düşük varyansından daha güçlü bir araştırma talebi olarak yorumlanabilir. Ortak hatalı tanıklar kusursuz mutabakat içinde yanılabilir; aynı kökenden gelen çok sayıda rapor tek bir bağımsız doğrulama yolu gibi davranabilir. İç içe model, sabit N'de bağımsız kalibrasyon ailelerinin artmasının yalnız aile düzeyindeki hatayı azaltabileceğini; küresel ortak hata ve sabit yanlılığın kaldığını gösterir. Dolayısıyla doğrulama protokolü, tanık sayısına ek olarak **kaynak kökeni, bağımsız yöntem, dış ölçüt, ayırt edici koşul ve kalan belirsizlik** kaydetmelidir. Bu sonuç, kurucu ontolojinin doğrulandığı iddiası değil, onun epistemik alt modelinin daha eleştirel biçimde sınanmasına yönelik akademik katkıdır.

## Beyanlar

**Veri ve kod:** Yalnız sentetik veri üretildi. Deney kodu Academic Corpus'un aynı araştırma dalında tutulur. Sayısal sonuçlar belirlenmiş tohum ve parametrelerle tekrar üretilebilir; farklı Python sürümlerinde rastgele sayı ayrıntıları değişebilir. **Finansman:** Bu çalışma için doğrulanmış bir dış finansman beyanı bulunmuyor; finansman yokluğu bağımsız olarak teyit edilmiş sayılmaz. **Çıkar çatışması:** Kullanıcının/nihai yazarın beyanı henüz alınmadı. **Yapay zekâ yardımı:** Metin, model ayrışımı, literatür taraması ve sentetik deney tasarımı 21 Ekim 2026 tarihinde OpenAI ChatGPT (GPT-6) kullanılarak hazırlanmıştır; akademik sorumluluk için insan denetimi gerekir. **Hakemlik:** Dış hakem incelemesi yapılmadı. **Gönderim:** Dergiye, DOI servisine veya arXiv'e hiçbir gönderim yapılmayacaktır.

## Kaynakça (doğrulanmış bibliyografik çekirdek)

- Dietrich, Franz, ve Kai Spiekermann. 2013. “Epistemic Democracy with Defensible Premises.” *Economics & Philosophy* 29 (1): 87–120. https://doi.org/10.1017/S0266267113000096.
- Goldman, Alvin I. 2001. “Experts: Which Ones Should You Trust?” *Philosophy and Phenomenological Research* 63 (1): 85–110. https://doi.org/10.1111/j.1933-1592.2001.tb00093.x.
- Hardwig, John. 1985. “Epistemic Dependence.” *The Journal of Philosophy* 82 (7): 335–49. https://doi.org/10.2307/2026523.
- Joint Committee for Guides in Metrology (JCGM). 2008. *Evaluation of Measurement Data—Guide to the Expression of Uncertainty in Measurement.* JCGM 100:2008. https://doi.org/10.59161/JCGM100-2008E.
- Taylor, Barry N., ve Chris E. Kuyatt. 1994. *Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results.* NIST Technical Note 1297 (1994 ed.). https://www.nist.gov/pml/nist-technical-note-1297.

### Birincil Zanistarast kaynakları ve sürüm izleri

- [K1] `veysieken000-ctrl/zanistarast-ontology`, `papers/zanabun.md`, incelenen Git blob SHA: `ee68095b8d87ba8a580492cfd4c98b86e0a0f21a`. Orijinal hesaplama ve uyum iddiaları.
- [K2] `veysieken000-ctrl/zanistarast-ai-native-model`, dal `research/yek-6tek-makale-programi-2026-10-16`, `research/yek-6tek-program/KANONIK-ZANABUN-IKINCI-BILEN-DOGRULAMA-DAIMILIK-2026-10-18.md`, blob SHA `330db69e2146656281ebc32aa33439666ec54ce4`.
- [K3] Aynı eski depo/dal, `research/yek-6tek-program/manuscripts/ZANABUN-01-bagimsiz-taniklik-ve-ortak-hata.md`, blob SHA `dea450a481b14f2668480513156a96e965d676f3`. v0.1 sürüm ailesi.
- [K4] Aynı eski depo/dal, `research/yek-6tek-program/manuscripts/ZANABUN-01-ORTAK-HATA-DENEY-EKI-2026-10-20.md`, blob SHA `45578288450485cfaf0a217a2b3ce0dc7b32e505`. İlk sentetik ek; ayrı makale değildir.
- [K5] Aynı eski depo/dal, `research/yek-6tek-program/experiments/zanabun_common_error_trial.py`, blob SHA `37588200906b85147349cb7b169ed8b570a5e068`. Önceki tek-aile deneyi.

## Hedef dergi standart eşleştirmesi — 21 Ekim 2026

**Kalite kıstası olarak seçilen dergi:** *Philosophy of Science* (Cambridge University Press/Philosophy of Science Association). Resmî sayfalar 21.10.2026 tarihinde incelendi: https://www.cambridge.org/core/journals/philosophy-of-science/information/author-instructions ; https://www.cambridge.org/core/journals/philosophy-of-science/information/author-instructions/preparing-your-materials ; https://www.cambridge.org/core/journals/philosophy-of-science/information/journal-policies/publishing-ethics . Araştırma makalesi için 9.000 sözcük sınırı (özet, notlar, metin içi atıf, görsel/tablo ve basılı ekler dahil; kaynakça ve çevrimiçi ekler hariç); yaklaşık 100 sözcüklük özet; anonim değerlendirmeye uygunluk; yazar-tarih/Chicago kaynakça ve mevcut DOI'lerin gösterilmesi; üretici yapay zekâ kullanımının açıklanması. Bu metin Türkçedir; derginin yayın diliyle uygunluk, tam stil denetimi ve bağımsız hakemlik henüz sağlanmadı. Bu bir **kalite referansıdır, gönderim niyeti değildir**.

## Kalite kapıları K0–K6 (21.10.2026)

- **K0 kaynak — kısmen geçti:** K1–K5 özgün dosyaları ve blob SHA'ları okundu; Core 03 ve bütün kanonik külliyatın karşılaştırması henüz bitmedi.
- **K1 ayrışma — geçti (aile düzeyi):** ZANABUN-01 v0.2; v0.1 ve ekleriyle aynı makale ailesi, ikinci bağımsız makale sayılmadı.
- **K2 tam metin — geçti (yapısal):** Özet, giriş, kaynak eleştirisi, literatür, yöntem, kanıt, sentetik sonuç, tartışma, sınırlar, sonuç, beyanlar, kaynakça var. Dış akademik olgunluk onayı değildir.
- **K3 literatür — kısmen geçti:** Beş doğrulanmış temel kaynak var; sistematik en-yakın-çalışma ve 2020 sonrası araştırma taraması eksik.
- **K4 karşı denetim — kısmen geçti:** Deterministik karşı örnek, model içi ispat, sentetik hesap, alternatif açıklamalar var; kodun ayrı ortamda yeniden çalıştırılması ve gerçek veri sınaması açık.
- **K5 etik — kısmen geçti:** AI, sentetik veri ve teoloji/kanıt ayrımı açık; insan yazarlık/çıkar çatışması/finansman teyidi yok.
- **K6 dergi biçimi — kısmen geçti:** Resmî 21.10.2026 yönergeleri doğrulandı; İngilizce ve nihai biçim denetimi yapılmadı. **Yayıma hazır değildir.**

**Revizyon günlüğü:** 16–20 Ekim 2026 tarihli v0.1 ve deney eki kaynak alındı; 21 Ekim 2026'da kaynak K1/K2 karşılaştırması, yeni iç içe hata modeli, tanımlanabilirlik sınırı, 7 koşullu sentetik deney, dış referans protokolü, gerçek literatür ve hedef dergi eşleştirmesiyle v0.2 üretildi. Eski depolara yazılmadı.
