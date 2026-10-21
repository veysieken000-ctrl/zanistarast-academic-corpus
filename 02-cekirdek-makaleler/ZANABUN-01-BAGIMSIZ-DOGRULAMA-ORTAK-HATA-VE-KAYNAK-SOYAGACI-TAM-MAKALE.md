# Zanabûn epistemolojisinde ikinci bilenin doğrulaması: ortak hata, kaynak soyağacı ve dış geçerlik

**Makale kimliği:** ZANABUN-01 · **Sürüm:** 1.0 araştırma metni · **Tarih:** 21 Ekim 2026  
**Tür:** Analitik epistemoloji / formel sosyal epistemoloji / yeniden üretilebilir sentetik yöntem çalışması.  
**Durum:** Kapsamlı akademik çalışma metni; hakemli yayın, saha araştırması veya metafizik ispat değildir. Kullanıcı talimatı gereği hiçbir dergiye gönderilmeyecektir.  
**Sürüm ailesi:** Önceki ZANABUN-01 taslağının kaynak denetimli genişletilmesi; ayrı benzersiz makale olarak sayılmaz.  
**Hedef dergi standardı (biçimsel karşılaştırma, gönderim yok):** *Episteme* (Cambridge University Press), sosyal ve formel epistemoloji alanı; resmî yazar yönergesi **21.10.2026 tarihinde kontrol edildi**. Derginin çift aralık/12 punto Times New Roman, azami 12.000 sözcük (not ve kaynakça dahil), anonimleştirme, ayrı özet, çıkar çatışması ve üretken yapay zekâ açıklaması gereklilikleri ayrıca incelendi [J1–J3]. Bu Türkçe Markdown çalışma dosyası söz konusu son teslim biçimi değildir; yönerge uyumu yalnız kalite ölçütüdür.

## Özet

Zanabûn'un kurucu doğrulama ilkesi, bilen öznenin bilinen nesneye yöneliminden doğan **sonucun** ikinci bilen tarafından yeniden sınanmasını esas alır. Bu çalışma, böyle bir doğrulamanın hangi koşullarda tanıkların yalnızca birbirleriyle anlaşmasından ayrıldığını araştırır. Özgün Zanabûn metnindeki tanık ortalaması ve varyansı, bir doğruluk ölçütünün aday işlemselleştirmesi olarak ele alınır; tanıkların kaynak, kalibrasyon veya model bağımlılığı durumunda bu işlemselleştirmenin yeterli olmadığı gösterilir. Dört tanığın aynı yanlış değeri bildirdiği kesin karşı örnekten başlanarak ortak hata ve kaynak kümeleri modeli türetilir. Eşit büyüklükte m bağımsız kaynak kümesi ve n toplam tanık için örnek ortalamasının hata varyansı, açık varsayımlar altında τ²/m + σ²/n olur. Böylece görünürde n tanığın bulunduğu bir durumda epistemik bilgi çeşitliliği m ile sınırlandırılır. n=16 ve 20.000 sentetik tekrar kullanan deterministik simülasyon, analitik öngörüyü farklı m değerlerinde karşılaştırır; gerçek insan davranışı ölçülmez. Ayrıca tek bir olayda gerçek değer ile ortak yanlılığın yalnız iç mutabakattan ayrıştırılamadığı gösterilir. Önerilen katkı, Zanabûn'un metafizik çekirdeğini istatistiğe indirgemek değil, **ikinci bilenin bağımsız sonuç doğrulaması** için kaynak soyağacı, dış ölçüt, ayırt edici müdahale ve hata belirsizliğini birlikte isteyen sınanabilir bir protokol kurmaktır.

**Anahtar kelimeler:** Zanabûn; ikinci bilen; sosyal epistemoloji; ortak hata; epistemik bağımsızlık; kaynak soyağacı; gözlemsel eşdeğerlik; yeniden üretilebilirlik.

## 1. Giriş ve araştırma problemi

Bir ölçüm sonucunu çok sayıda kişi veya yazılımın aynı şekilde bildirmesi güven verici olabilir. Ne var ki tanıkların aynı cihazı, veri tabanını, haber kaynağını, eğitim verisini veya değerlendirme modelini paylaşması hâlinde sayıca çoğalma, doğrulama yollarının çoğalması anlamına gelmez. Epistemolojik problem bu ayrımda ortaya çıkar: **Bir sonuç üzerinde mutabakat, hangi ilave koşullarda bağımsız ikinci doğrulama sayılır?**

Zanabûn'un kurucu ifadesi şöyledir:

> “Bilen öznenin bilinen nesneye yönelimi sonucu ortaya çıkan sonucun ikinci bilen tarafından onayı.”

Kurucu açıklama, ikinci bilenin ilk bilenin kişiliğini veya otoritesini değil, deney, gözlem ve akıl yürütme aracılığıyla ortaya çıkan **sonucu** denetlemesini öne çıkarır [K3]. Bu nedenle onay ile taklit, tekrar ile bağımsız yeniden sınama ve geçici gözlem ile bütün koşullara yayılan daimilik iddiası birbirinden ayrılmalıdır. Özgün Core 03'te genel geçer bilginin aynı şartlarda tekrarlanması ve farklı özneler tarafından doğrulanabilmesi vurgulanır [K2]. Buna karşılık özgün hesaplamalı Zanabûn metni, tanık ortalaması K ve tanıklar arası varyans aracılığıyla uyumun sayısallaştırılmasını önerir [K1]. Bu iki vurgunun arasında gerçek bir araştırma sorusu vardır: **Düşük varyansın hangi koşullarda dış gerçekliğe uygunlukla ilişkisi vardır?**

Çalışma üç düzeyde yürütülür: (i) kanonik ifadenin metin temelli yorumu; (ii) açık varsayımlı olasılık ve özdeşleşebilirlik modeli; (iii) sentetik deney ve yanlışlama protokolü. Bu düzeylerin hiçbirinde bir model denkleminin Hebûn ontolojisini, Ehad'ın varlığını veya bütün Zanabûn epistemolojisini kanıtladığı ileri sürülmez.

## 2. Kanonik kaynak ve kapsamın korunması

**Kurucu beyan, aynen:**

> Ehad Yek'tir ve Ehad âlemlerdeki her şeyi Yek'e göre yaratmıştır; her kar tanesi, her parmak izi dahil.

Bu ifade kurucunun teolojik/ontolojik ilkesidir. Buradaki Yek, insanın özü, bir makalenin sentezi veya ayrıca yaratılmış bir katman olarak yeniden tanımlanmaz. Hebûn varlığın kuruluşuna ilişkin ontolojik çerçeve, Zanabûn ise varlığın bilinmesine ve doğrulanmasına ilişkin epistemolojik çerçeve olarak ele alınır. Bunların ilişkisinin felsefi yorumu ile gözlem hatasının istatistiksel analizi birbirinden farklı iddia türleridir.

Özgün `papers/zanabun.md` dosyası, `K=(1/n)ΣW_i` ve `σ²=(1/n)Σ(W_i−K)²` hesaplarını ve düşük varyans ile uyum bağlantısını sunar [K1]. Burada önerilen düzeltme şudur: **uyum ölçüsü, ancak dış geçerlik, bağımlılık yapısı ve hata mekanizması hesaba katılırsa doğruluk lehine kanıt oluşturabilir**. Bu, özgün kaynak metninin değiştirilmesi değil, ondan türetilmiş bir bilimsel eleştiridir.

Core 01'deki altı kozmik boyut ile Core 13'teki insan katmanları numerik olarak aynı sınıflama değildir. Bu makalenin ölçüm modeli bunlardan hiçbirini yeniden numaralandırmaz; 6+Tek'i matematiksel altı değişkenli bir istatistik modeli gibi sunmaz. Zekâ/akıl, ruh/melek, duygu/ahlak ve hüküm/ahiret tartışmaları bu dar yöntemin dışında kalır.

## 3. Yakın literatür ve yenilik sınırı

Clemen ve Winkler'in (1999) uzmanların olasılık dağılımlarını birleştirme incelemesi, uzman görüşlerini toplamanın matematiksel ve davranışsal koşullara bağlı olduğunu; her bağlam için tek bir en iyi birleştirme yöntemi bulunmadığını tartışır [L1]. Lorenz ve arkadaşları (2011), sosyal etki altındaki grup tahminlerinin birbirine yakınsamasının doğruluk artışını zorunlu kılmadığını deneysel olarak göstermiştir [L2]. NIST TN 1297, ölçüm belirsizliğinin birleşiminde kovaryansların dikkate alınmasını, tanınan sistematik etkilerin düzeltilmesini ve hata ile belirsizliğin ayrılmasını öngörür [L3]. Dolayısıyla 'korelasyonlu gözlemler ortalamanın faydasını azaltır' önermesi **literatürde yeni bir keşif değildir**.

Bu metnin proje içi özgün katkısı üçlü bir çerçevedir: (a) Zanabûn'un **sonucun ikinci bilen tarafından onayı** ilkesini kopya mutabakatından ayırmak; (b) tanık sayısı yerine kanıtın **kaynak soyağacını** açık bir küme modeline bağlamak; (c) doğruluk iddiasının bir dış ölçüt veya ayırt edici müdahale olmaksızın özdeşleşemediği koşulları belirlemek. Uluslararası literatürde ilk kez önerildiği veya daha önceki modelleri aştığı iddia edilmez. Bu konumlandırma, yalnız seçilmiş temel kaynaklarla sınırlı literatür taramasına dayanır; sistematik derleme yapılmamıştır.

## 4. Tanımlar ve varsayımlar

Bir hedef nicelik θ için n tanığın sayısal raporları W₁,…,Wₙ olsun. Burada tanık, kişi, cihaz veya yazılım çıktısı olabilir; bu kategorilerin güvenilirliği özdeş varsayılmaz.

**Mutabakat:** Raporlar arası dağılımın küçük olması. Özgün metindeki popülasyon varyansı `S²=(1/n)Σ(W_i−W̄)²` bunu betimler.

**Dış doğruluk:** Bağımsız ve uygun biçimde gerekçelendirilmiş bir referans θ₀ mevcutsa `|W̄−θ₀|` veya `(W̄−θ₀)²` ile değerlendirilen uygunluk. Referansın da belirsizliği varsa bu belirsizlik raporlanır; θ₀ mutlak hakikat diye sunulmaz.

**Kaynak bağımsızlığı:** Tanıkların iddialarını ürettikleri veri, kalibrasyon, yöntem ve bilgi kanallarının ne ölçüde ortak olduğu. Birbirini görmeyen iki tanık aynı hatalı ölçüm cihazını kullanabilir; kişiler arası bağımsızlık ile hata bağımsızlığı farklıdır.

**Daimilik:** Önceden belirtilmiş koşullar, zaman aralıkları ve sınamalar altında yeniden elde edilebilen sonuç. Sonlu tekrardan tüm mümkün koşullar için zorunlu evrensel süreklilik sonucu çıkmaz.

**Varsayımlar:** Aşağıdaki analitik modelde tüm hata terimleri sonlu ikinci momente sahiptir; kaynak kümeleri arası ortak hatalar bağımsız, küme içindeki bireysel hatalar bağımsız ve sıfır ortalamalıdır; θ sabittir. Bu varsayımlar veri tarafından ayrıca sınanmalıdır. Gözlemcilerin gerçek hayatta bunları sağladığı iddia edilmez.

## 5. Birinci sonuç: tam mutabakat doğruluğu garanti etmez

θ=0 olsun. Dört tanık da W=(5,5,5,5) bildirsin. O zaman:

```text
W̄ = (5+5+5+5)/4 = 5
S² = [(5−5)²+(5−5)²+(5−5)²+(5−5)²]/4 = 0
|W̄−θ| = 5
```

Dolayısıyla 'düşük varyans → doğruluk' koşulsuz mantıksal çıkarımı yanlıştır. Bu karşı örnek, Zanabûn'un **ikinci bilenin bağımsız sonucu araştırması** şeklindeki daha zengin kanonik ifadesini çürütmez; yalnızca uyumu dış doğrulukla özdeşleştiren belirli bir istatistiksel okumanın sınırını gösterir. Ters yönde de çok farklı ama bağımsız ölçümlerin ortalaması gerçeğe yakın olabilir: yüksek dağılım otomatik olarak dezenformasyon değildir.

## 6. İkinci sonuç: ortak hata ve kaynak kümeleri

İlk model:

```text
W_i = θ + B + ε_i
E[B]=E[ε_i]=0
Var(B)=τ², Var(ε_i)=σ²
Cov(B, ε_i)=0; Cov(ε_i, ε_j)=0 (i≠j).
```

Burada B, bir **tek hedefin farklı tanıklarca paylaşılan hatasını** temsil eder. Hata terimi çok sayıda hedef/tekrar üzerinden rastgele olarak modellenebilir; tek bir hedefte B bilinmeyen sabit yanlılık gibi de işleyebilir. Tanık ortalaması için:

```text
W̄−θ = B + (1/n)Σ ε_i
Var(W̄−θ) = τ² + σ²/n.                         (1)
```

n sonsuza giderken varyans τ²'ye yaklaşır. Tek bir hedef için B=b≠0 sabitse ve özel hatalar ortalaması yakınsıyorsa W̄→θ+b olur. Bu, istatistiksel modelin koşullu sonucudur.

**Kaynak soyağacı genellemesi.** n tanık, her birinde k tanık bulunan m eşit büyüklükte ve bağımsız kaynak kümesine ayrılmış olsun: n=mk. Küme g içindeki tanık j'nin raporu:

```text
W_gj = θ + B_g + ε_gj
Var(B_g)=τ², Var(ε_gj)=σ².
```

Kümeler arasında ve özel hatalarda bağımsızlık varsayımıyla:

```text
W̄−θ = (1/m)Σ_g B_g + (1/n)Σ_gj ε_gj
Var(W̄−θ) = τ²/m + σ²/n.                     (2)
```

**Türetim:** `(1/m)Σ B_g` ifadesinin varyansı m bağımsız, her biri τ² varyanslı terim nedeniyle `mτ²/m²=τ²/m` olur. Özel hatalar için aynı hesap `nσ²/n²=σ²/n` verir; çapraz kovaryans sıfırdır. Bu nedenle kaynak çeşitliliği m arttığında ortak hata bileşeni küçülür. Küme büyüklükleri eşit değilse sonuç değişir: `Var(W̄−θ)=τ²Σ_g (n_g/n)² + σ²/n`; tek bir büyük kümenin ağırlığı artar.

**Etkin örneklem büyüklüğü.** Her tanığın marjinal hata varyansı `v=τ²+σ²`, aynı kümedeki iki tanığın hata korelasyonu `ρ=τ²/v` olsun. Eşit kümeler için:

```text
Var(W̄−θ) = v[1+(k−1)ρ]/n
n_eff = n/[1+(k−1)ρ].                         (3)
```

Bu n_eff yalnız **ortalamanın varyansı açısından** tanımlıdır; ontolojik tanık sayısı, doğruluğun doğrudan ölçüsü veya farklı ağırlıklı/yanlı tahmin ediciler için evrensel bir değer değildir.

## 7. Üçüncü sonuç: dış ölçüt olmadan özdeşleşebilirlik sınırı

Tek hedef ve tek kaynak kümesinde raporlar `W_i=θ+B+ε_i` ise, her sabit c için:

```text
θ' = θ + c
B' = B − c
θ' + B' = θ + B.
```

Dolayısıyla yalnız W raporlarından θ ile gerçekleşmiş ortak hata B'nin ayrı ayrı değerleri **özdeşleşmez**. Çok sayıda aynı kaynaktan türeyen tanık bu bilgi eksikliğini gidermez. E[B]=0 gibi bir popülasyon varsayımı, çok sayıda bağımsız hedef/kalibrasyon için yararlı olabilir; fakat tek hedefin gerçekleşmiş B'sini kendiliğinden açıklamaz.

Bu sınırı aşmak için yeni tür kanıt gerekir: izlenebilir bir referans ölçüm, başka kalibrasyon zinciri, farklı ilkeye dayalı ölçüm yöntemi, müdahale veya zaman/koşul değişikliği. Bağımsız dış referans `Z=θ+η` ve `Var(η)=v_Z` ise, `D=W̄−Z` için `Var(D)=τ²/m+σ²/n+v_Z` (hataların bağımsızlığı altında). D'nin tek gözlenen değeri B'yi kesin belirlemez; referans belirsizliği de raporlanmalıdır. Sistematik düzeltme `B_hat` kullanılırsa düzeltilmiş tahminin belirsizliği, `B_hat` tahmin hatasını da içerir.

Bu nedenle **sonuç doğrulaması**, yalnız gözlemcilerin benzer cümle kurması değil, sonuç üretim yollarının gerçekten farklı olup olmadığının ve mümkünse dış gerçeklik bağının araştırılmasıdır.

## 8. Yeniden üretilebilir sentetik deney

### 8.1 Tasarım ve önceden belirlenmiş koşullar

Bu makalenin eki `07-deneyler-ve-karsi-ornekler/zanabun01_provenance_clusters.py` dosyasıdır. Standart Python kütüphanesi yeterlidir; tohum 20261021, her koşulda 20.000 tekrar, toplam tanık sayısı n=16, τ=2, σ=1. Kaynak kümesi sayısı m∈{1,2,4,8,16}; kümeler eşit büyüklüktedir. Her tekrarda m bağımsız Gauss küme hatası ve n bağımsız Gauss özel hatası çekilir. Gerçek değer θ=0 seçilebilir, çünkü yalnız hataların ortalaması analiz edilir. RMSE, sentetik ortalama hatasının karelerinin ortalamasının kareköküdür. Analitik karşılık denklem (2)'den `sqrt(4/m+1/16)` olur.

**Birincil ölçüt:** Analitik RMSE ile sentetik RMSE'nin mutlak farkı. Kodun otomatik kontrolü her koşul için farkın 0,05'ten küçük olmasını bekler; bu tolerans önceden tanımlanmış basit bir yazılım kontrolüdür, istatistiksel anlamlılık testi veya hakem onayı değildir. Her m için `seed+m` kullanılır; senaryolar arasında eşlenik rastgele sayı tasarımı yapılmamıştır.

### 8.2 Çalıştırılmış sentetik sonuçlar

21 Ekim 2026'da Python ile yerel çalıştırma yapıldı; ekin aynı algoritması çalıştırıldı. Çıktı yalnız **sentetik** sonuçtur:

| Bağımsız kaynak kümesi m | Küme başına tanık k | Sentetik RMSE | Analitik RMSE |
|---:|---:|---:|---:|
| 1 | 16 | 2,0052 | 2,0156 |
| 2 | 8 | 1,4373 | 1,4361 |
| 4 | 4 | 1,0158 | 1,0308 |
| 8 | 2 | 0,7516 | 0,7500 |
| 16 | 1 | 0,5552 | 0,5590 |

Tüm satırlar 0,05 tolerans denetiminden geçti. Kod ayrıca (i) dört tanıklı kesin karşı örneği, (ii) m=1 ve m=16 için analitik varyansları, (iii) θ ve B'nin karşılıklı kaydırılmasındaki özdeşleşmezliği sınar. Bu sonuçların analitik formüle yakınlığı beklenir; sentetik dağılımlar modelin kendi varsayımlarıyla üretilmiştir. Dolayısıyla **modelin dış geçerliğine bağımsız kanıt değildir**.

### 8.3 Yeniden üretim ve hata ayıklama

Depodaki araştırma dalından çalıştırma:

```bash
python3 07-deneyler-ve-karsi-ornekler/zanabun01_provenance_clusters.py
```

Python 3.9+ sözdizimi kullanılır; dış paket, ağ veya kişisel veri gerekmez. Beklenen son satır `PASS` olmalıdır. Tam sayısal eşleşme farklı Python sürümlerindeki rastgele sayı üretimi ayrıntılarına bağlı değişebilir; analitik sütunlar değişmemelidir. Bağımsız ikinci uygulama ve farklı dağılım aileleriyle duyarlılık testi henüz yapılmamıştır.

## 9. Karşı-denetim: model hangi koşullarda başarısız olur?

**C1 — Kaynak kümeleri gerçekte bağımsız değildir.** İki ayrı görünen arşiv aynı özgün belgeden alıntı yapabilir; iki yazılım farklı isimle aynı temel modeli kullanabilir. Böylece m olduğundan büyük tahmin edilir. Çözüm, beyan edilen 'bağımsızlık' yerine veri ve karar soyağacı incelemesidir.

**C2 — Ortak hatanın ortalaması sıfır değildir.** `E[B_g]=b` ise `E[W̄−θ]=b`; kümeleri artırmak bu sistematik yanlılığı ortadan kaldırmaz. Denklem (2) varyans içindir; toplam ortalama kare hata `b²+τ²/m+σ²/n` olur.

**C3 — Tanıkların özel hataları bağımsız değildir.** Ortak çevre, iletişim veya öğrenme nedeniyle `Cov(ε_i,ε_j)≠0` olabilir. O zaman tam kovaryans matrisi `Σ` ile `Var(W̄)=1ᵀΣ1/n²` hesaplanmalıdır. m saymak yeterli değildir.

**C4 — Yüksek varyans yanlışlık demek değildir.** Bir kısmı pozitif, bir kısmı negatif hatalı bağımsız raporlar yüksek dağılım sergileyip doğru ortalamayı verebilir. 'Dezenformasyon = yüksek varyans' eşitliği genellenemez.

**C5 — Dış referans kusurludur.** Altın standart denen yöntem de paylaşılan kalibrasyon hatası taşıyabilir. Gerçek doğruluk yerine 'iki yöntemin uyumu' ölçülüyor olabilir. Dış referansın zinciri ve belirsizliği ayrıca denetlenmelidir.

**C6 — Tek tanık doğru olabilir.** Güvenilir, izlenebilir, yeniden kalibre edilebilir bir ölçüm tek kişi veya cihazdan gelebilir. İkinci bilenin doğrulaması, epistemik güveni artıran normatif bir ilke olarak değerlendirilebilir; 'tek gözlemci asla doğru bilgi üretemez' evrensel teoremi bu modelden çıkmaz.

**C7 — Bağımsızlık maliyetlidir.** Eşit n altında m'yi artırmak her zaman pratikte ucuz değildir. Yeni kalibrasyon zinciri, cihaz veya uzmanlık kaynağı gerekebilir. Buradaki simülasyon maliyet/yarar optimizasyonu değildir.

**C8 — Sayısal ölçümler dışındaki tanıklıklar.** Ahlaki, tarihsel, metinsel ve teolojik önermeler aynı θ ve Gauss hata terimleriyle her zaman temsil edilemez. Analojiler kavramsal araştırma doğurur, doğrudan istatistiksel doğrulama sağlamaz.

## 10. Yanlışlanabilir hipotezler ve gelecekteki deney protokolü

**H1 (ortak kaynak etkisi):** Aynı cihaz kalibrasyonunu kullanan gruplarda, cihazlar arası bağımsız kalibrasyon grubuna göre daha büyük küme-içi hata korelasyonu gözlenir. **Yanlışlama:** Ölçülen korelasyonların ve dış referans hatalarının bu yönlü ayrımı göstermemesi.

**H2 (soyağacı bilgisi):** Kaynak bağımlılığı haritasıyla düzeltilen belirsizlik aralıkları, yalnız tanık sayısı kullanan saf bağımsızlık varsayımına göre hedeflenen kapsama oranına daha yakın olur. **Yanlışlama:** Önceden seçilmiş dış test setinde kapsama, genişlik ve kalibrasyon metriklerinde düzelmenin görülmemesi. Aralık genişlemesi tek başına 'daha iyi' sayılmaz.

**H3 (ayırt edici yöntem):** Farklı ilkeye dayalı ikinci ölçüm, aynı kaynağın tekrarına kıyasla yanlılığı tespit etme gücünü artırır. **Yanlışlama:** Eşit maliyet ve karşılaştırılabilir hata düzeyinde dış ölçüte göre fark bulunmaması.

**Önerilen veri:** Bilinen sentetik referans değerler yanında, izinli ve anonimleştirilmiş fiziksel kalibrasyon verileri; cihaz/operatör/kalibrasyon kökeni, zaman damgası ve dış referans belirsizliği. **Karşılaştırma:** (A) saf ortalama ve `σ²/n` varsayımı; (B) küme-duyarlı kovaryans; (C) bağımsız dış kalibrasyon; (D) sağlam tahmin ediciler. **Ön kayıt:** Gruplar, veri dışlama kuralları, hata ölçütleri ve başarısızlık eşikleri veri görülmeden sabitlenmelidir. Henüz gerçek veri toplanmamıştır.

## 11. Zanabûn için işlemsel ikinci-bilen protokolü

Kurucu ifadenin **yeni önerilen**, kurucunun doğrudan sözleri olarak sunulmayan işlemselleştirmesi şu dört kapıdan oluşur:

1. **Yönelim ve sonuç tanımı:** Birinci bilenin hangi nesneye, hangi yöntemle yöneldiği ve hangi sonuç iddiasında bulunduğu kaydedilir.
2. **İkinci yolun soyağacı:** İkinci bilenin veri, kalibrasyon, yazılım, yorum ve otorite bağımlılıkları açıkça çıkarılır; görünüşte bağımsız tekrarlar etiketlenir.
3. **Dış sınama:** Mümkünse bağımsız referans, müdahale veya ayırt edici yeni koşul kullanılır; referansın belirsizliği belirtilir.
4. **Koşullu onay ve geri dönüş:** Onay, 'bu koşullar ve bu belirsizlik düzeyinde doğrulandı' biçiminde raporlanır; yeni karşı örnek, ölçüm veya yöntem gelince yeniden açılır.

Bu dört kapı mutlak bir 'hakikat puanı' üretmez. Amaç, Zanabûn'un sonuç doğrulamasını yalnız çoğunluk oyuna veya ortak kaynağın çoğaltılmasına indirgememektir. Rasterast'ın köken, bağlam, mantık, çelişki ve ikinci denetim işlevleriyle ileride karşılaştırılabilir; Rasterast'ın kurucu ilkeleri bu makalede yeniden yazılmamıştır.

## 12. Ontoloji, ahlak ve yapay zekâ bakımından sınırlar

**Ontoloji:** Hebûn'un varlık ve oluşum iddiaları, gözlemcilerin ölçüm hatası denklemlerinden türetilemez. Gözlemcinin onay vermesi ile fiziksel varlığın yaratılması aynı nedensel mekanizma diye kabul edilmez. Ehad–Yek ilkesi teolojik/ontolojik konumunda kalır.

**Ahlak:** Bir tanığın kasten yanıltması ile aynı kalibrasyon hatasını fark etmeden paylaşması farklıdır. Matematiksel B terimi niyet, sorumluluk veya iradeli ahlakı ölçmez. İnsanın ahlaki sorumluluğu ayrı normatif inceleme gerektirir.

**Yapay zekâ:** Aynı büyük dil modelinden türeyen iki yanıt, farklı görünen anlatımlara rağmen eğitim verisi ve çıkarım stratejisi paylaşabilir. Bu bir **araştırma hipotezidir**, burada ampirik olarak ölçülmüş bir yapay zekâ güvenilirlik sonucu değildir. Mira'nın zihni, kodu, otomasyonları veya depoları üzerinde hiçbir değişiklik yapılmamıştır; bu makale bağımsız bir başvuru metnidir.

**Daimilik:** Tekrarlanabilirlik, koşul aralığı açıkça verilmediğinde ontolojik sonsuz süreklilik anlamına gelmez. Daha güçlü iddialar için zamansal ve bağlamsal sınama alanının genişletilmesi gerekir.

## 13. Tartışma: 'iki bilen' neden 'iki kopya' değildir?

Bu çalışma iki görünürde zıt tespiti uzlaştırır. İlk olarak, tanıklar arası uyum araştırmayı başlatan yararlı bir sinyaldir; büyük ayrışmalar veri kalitesi ve yorum farklarını görünür kılabilir. İkinci olarak, uyumun kendi başına hakikati garanti etmediği açıktır. Çelişki, 'uyum' sözcüğünün hem **raporların birbirine benzemesi** hem de **sonucun nesneye uygunluğunun yeniden sınanması** anlamlarında kullanılmasından doğar. Birinci anlam istatistiksel dağılım, ikinci anlam epistemik gerekçelendirme ve dış doğrulamadır.

İkinci bilenin birinciyle aynı sonuca ulaşması, ancak araştırma yolunun ilgili hata mekanizmaları açısından yeterince ayrışması ve sonuç iddiasının bağımsız karşı denemeye açık olması hâlinde daha güçlü gerekçe sunar. Bu, bağımsızlığın mutlak ikili özellik değil, hata türüne göre değerlendirilmesi gereken ilişkisel özellik olduğunu gösterir. Bir tanık veri açısından bağımsız ama yorum çerçevesi açısından bağımlı olabilir; başka biri aynı ham veriyi kullanıp bağımsız matematiksel çözümle hatayı saptayabilir. Kaynak soyağacı grafiği bu farklılıkları açığa çıkarabilir, fakat tek başına doğruluk garantisi vermez.

Bilim felsefesi bakımından daha geniş sonuç şudur: doğrulama iddiasının gücü yalnız tekrar sayısıyla değil, **tekrarın neyi değiştirdiğiyle** ilişkilidir. Aynı koşullarda tekrar, kararlılığı sınar; farklı kalibrasyon, ortak yanlılığı sınar; ayırt edici müdahale, rakip neden modellerini sınar. Bunlar birbirinin yerine geçmez.

## 14. Sonuç

Birden fazla tanığın aynı raporu vermesi, bağımsız sonuç doğrulaması için yeterli değildir. Kesin karşı örnek bunu mantıksal olarak; kaynak kümesi modeli ise bağımlılık varsayımları altında nicel olarak gösterir. Kaynak kümeleri bağımsız ve eşit büyüklükteyse ortalama hata varyansı `τ²/m+σ²/n` olur; n büyürken m sabit kalıyorsa ortak hata bileşeni yok olmaz. Tek hedefte θ ile gerçekleşmiş B'nin iç mutabakattan ayrıştırılamaması, dış ölçüt ve ayırt edici yöntem ihtiyacını gerekçelendirir.

Bu sonuçlar Zanabûn'un metafizik geçerliliğini ispatlamaz veya çürütmez. Daha sınırlı ama kullanılabilir katkı şudur: kurucunun **ikinci bilenin sonucu doğrulaması** ilkesi, kanıt soyağacı ve bağımsız karşı sınama ile somutlaştırıldığında, yalnız rapor sayısına dayanan sahte çoğulluk riskini görünür kılan bir araştırma protokolüne dönüşebilir. Sonraki aşama, gerçek kalibrasyon verileri ve bağımsız kod uygulamasıyla model varsayımlarının zorlanmasıdır.

## 15. Etik, veri ve üretken yapay zekâ açıklaması

**Veri:** Gerçek kişi verisi, saha gözlemi, katılımcı veya özel bilgi kullanılmadı. Sonuçlar açıkça belirtilmiş matematiksel varsayımlara ve yerel sentetik simülasyona dayanır. **Finansman:** Bu çalışma için doğrulanmış dış fon bilgisi yoktur; dış finansman alınmadığına dair belgesiz kesin beyan verilmez. **Çıkar çatışması:** Bu bağımsız metnin değerlendirme ölçütlerini belirleyen kurucu kaynaklar aynı proje ailesine aittir; kanonik sadakat gereği tarafsızlığın sınırı açıkça bildirilir. Bilinen ticari çıkar çatışması bildirilmemiştir; gerçek kişi yazarların beyanı ayrıca gerekir.

**Üretken yapay zekâ:** Bu araştırma metninin taslaklaştırılması, literatür ön taraması, formel türetim ve kod geliştirme aşamalarında OpenAI ChatGPT (GPT-6), 21.10.2026 tarihinde kullanılmıştır. Çıktılar özgün kaynak metinleri ve yayınevi/NIST kaynaklarıyla karşılaştırılmış, matematiksel özdeşlikler ve sentetik kod yerel olarak sınanmıştır. Model, insan yazar yerine gösterilmez; gerçek bir akademik gönderim düşünülseydi insan sorumlu yazar, bağımsız doğrulama ve ilgili yayınevinin açıklama gerekleri ayrıca yerine getirilmeliydi. **Gönderim veya yayın yapılmamıştır.**

## 16. Kaynakça ve izlenebilir köken

### Özgün Zanistarast kaynakları (değiştirilmedi)

- **[K1]** *Zanabûn: A Computational Epistemology of Knowledge as Coherent Multi-Agent Witnessing*, `veysieken000-ctrl/zanistarast-ontology/papers/zanabun.md`, okunan Git blob SHA `ee68095b8d87ba8a580492cfd4c98b86e0a0f21a`. [Kaynak](https://github.com/veysieken000-ctrl/zanistarast-ontology/blob/main/papers/zanabun.md). Kaynak dosyada iki ayrı Zanabûn metin bölümü bulunmaktadır; ikisi birlikte değerlendirilmiştir.
- **[K2]** *Core 03 – Akıl ve Bilginin Kaynağı*, `veysieken000-ctrl/zanistarast-ai-native-model/core-03.html`, okunan Git blob SHA `6895cf5e3c1ff5bc23d6c57767e9b180c5022d2b`. [Kaynak](https://github.com/veysieken000-ctrl/zanistarast-ai-native-model/blob/main/core-03.html).
- **[K3]** *Zanabûn — İkinci bilenin doğrulaması, tekrar ve daimilik*, `research/yek-6tek-program/KANONIK-ZANABUN-IKINCI-BILEN-DOGRULAMA-DAIMILIK-2026-10-18.md`, `zanistarast-ai-native-model`, araştırma dalı `research/yek-6tek-makale-programi-2026-10-16`, blob SHA `330db69e2146656281ebc32aa33439666ec54ce4`. [Kaynak](https://github.com/veysieken000-ctrl/zanistarast-ai-native-model/blob/research/yek-6tek-makale-programi-2026-10-16/research/yek-6tek-program/KANONIK-ZANABUN-IKINCI-BILEN-DOGRULAMA-DAIMILIK-2026-10-18.md).
- **[K4]** Önceki ZANABUN-01 makale taslağı, aynı araştırma dalında `research/yek-6tek-program/manuscripts/ZANABUN-01-bagimsiz-taniklik-ve-ortak-hata.md`, blob SHA `dea450a481b14f2668480513156a96e965d676f3`. [Kaynak](https://github.com/veysieken000-ctrl/zanistarast-ai-native-model/blob/research/yek-6tek-makale-programi-2026-10-16/research/yek-6tek-program/manuscripts/ZANABUN-01-bagimsiz-taniklik-ve-ortak-hata.md).
- **[K5]** Önceki sentetik deney eki, aynı dalda `research/yek-6tek-program/manuscripts/ZANABUN-01-ORTAK-HATA-DENEY-EKI-2026-10-20.md`, blob SHA `45578288450485cfaf0a217a2b3ce0dc7b32e505`. Bu sürümde kaynak kümesi sayısı ayrıca değiştirilmiştir.

### Doğrulanan harici literatür

- **[L1]** Clemen, R. T. ve Winkler, R. L. (1999). Combining Probability Distributions From Experts in Risk Analysis. *Risk Analysis*, 19(2), 187–203. [Yayınevi DOI kaydı](https://doi.org/10.1111/j.1539-6924.1999.tb00399.x). Uzman görüşlerini birleştirme ve bağımlı bilgi kaynakları bağlamı.
- **[L2]** Lorenz, J., Rauhut, H., Schweitzer, F. ve Helbing, D. (2011). How social influence can undermine the wisdom of crowd effect. *Proceedings of the National Academy of Sciences*, 108, 9020–9025. [DOI](https://doi.org/10.1073/pnas.1008636108); [ETH Zurich araştırmacı kaydı](https://www.sg.ethz.ch/publications/2011/lorenz2011how-social-influence/). Sosyal etkinin yakınsamayı doğruluktan ayırabilmesine dair ampirik literatür.
- **[L3]** Taylor, B. N. ve Kuyatt, C. E. (1994). *Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results*, NIST Technical Note 1297. [NIST](https://www.nist.gov/pml/nist-technical-note-1297); özellikle [birleşik belirsizlik](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty) ve [kovaryans](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-2-classification-components-uncertainty) bölümleri.

### Hedef dergi yönergesi (21.10.2026 tarihinde erişilen resmî sayfalar)

- **[J1]** *Episteme*, [Author instructions](https://www.cambridge.org/core/journals/episteme/information/author-instructions). Alan kapsamı ve sosyal/formel epistemoloji uygunluğu.
- **[J2]** *Episteme*, [Preparing your materials](https://www.cambridge.org/core/journals/episteme/information/author-instructions/preparing-your-materials). 12.000 sözcük üst sınırı, biçim, anonimleştirme, etik, üretken yapay zekâ açıklaması.
- **[J3]** *Episteme*, [Publishing ethics](https://www.cambridge.org/core/journals/episteme/information/journal-policies/publishing-ethics). Atıf, yinelenen yayın, açıklık ve çıkar çatışması.

## 17. K0–K6 kalite kapıları ve dürüst durum değerlendirmesi

| Kapı | Ölçüt | 21.10.2026 durumu |
|---|---|---|
| **K0** | Kaynak kökeni, kanonik beyan ve yetki sınırı | **Geçti:** K1–K5 dosyaları blob SHA ile okundu; diğer depolara yazılmadı. |
| **K1** | Ayrı araştırma sorusu, yenilik sınırı, literatür | **Kısmen geçti:** Yakın üç temel literatür kaynağı doğrulandı; sistematik tarama yok. |
| **K2** | Açık yöntem, türetim, karşı örnek | **Geçti (model içi):** Denklem (1)–(3), özdeşleşebilirlik ve karşı koşullar açık. |
| **K3** | Yeniden üretilebilir deney, sonuç denetimi | **Geçti (sentetik):** Kod ve yerel çalıştırma mevcut; ikinci bağımsız kod uygulaması yok. |
| **K4** | Dış geçerlik, rakip açıklamalar, yanlışlama | **Kısmen geçti:** C1–C8 ve H1–H3 var; gerçek veri testi yok. |
| **K5** | Etik, atıf, hedef dergi biçimi | **Kısmen geçti:** Resmî yönerge ve AI açıklaması mevcut; Türkçe Markdown nihai dergi biçimi değil. |
| **K6** | Bağımsız eleştirel inceleme ve nihai bütünlük | **Açık:** Harici hakem incelemesi ve gerçek veri temelli doğrulama yapılmadı. |

**Son karar:** Bilimsel içeriği, formel yöntemi ve yeniden üretilebilir sentetik eki bulunan **tam araştırma metni** hazırlanmıştır. Buna karşın yayıma hazır veya hakem onaylı diye gösterilemez. Eksikler saklanmaz; metin Mira için bağımsız referans niteliğindedir, Mira'nın yazma alanı değildir.

## 18. Revizyon günlüğü

- **16–20 Ekim 2026:** Eski ZANABUN-01 taslağı ve sentetik deney eki oluşturulmuştu; bu dosyalar başka depoda, değiştirilmeden kaldı [K4–K5].
- **21 Ekim 2026, v1.0:** Özgün Zanabûn ve Core 03 dosyaları yeniden okundu; kurucu ikinci-bilen açıklaması karşılaştırıldı; gerçek harici literatür ve *Episteme* yönergesi kontrol edildi; kaynak kümesi modeli, özdeşleşebilirlik kanıtı, yeni sentetik deney, sonuçlar, karşı-denetim, etik ve K0–K6 kaydı eklendi. Eski makalenin **yeni sürümü**, ayrı makale değildir.


## Kanonik düzeltme eki — 21 Ekim 2026: ikinci bilenin ontolojik kapsamı

**Bu ek, önceki bölümlerdeki dar yöntemsel “ikinci bilen = ikinci tanık” okumasını sınırlar.** Kurucunun 21 Ekim 2026 açıklamasına göre ikinci bilenin **en üst ontolojik anlamı**, hüküm karşısında ahlakı temsil eden **insandır**. Her varlık kendi kozmik boyutu ve evresinde iş, oluş ve hareket sergileyerek **ahlakı ontolojik geniş anlamda temsil eder**; ancak atom, yıldız, hücre veya bitki bu nedenle insan gibi bilişsel bir “bilen” sayılmaz. İlk ahlak örneği **atomdur**. İnsan, akıl, irade ve hüküm karşısındaki sorumluluk bakımından üst seviyeyi temsil eder. Dolayısıyla makalenin istatistiksel ikinci tanık modeli, bu kavramın **yalnız bir epistemolojik alt uygulamasıdır** ve ontolojik tanımın yerini alamaz.

**Ontolojik kapsama dizisi:** Fizik atom / yıldız-gezegen; biyoloji tek hücreli / çok hücreli; zihin zekâ / akıl; ruh ruh / melekler; ahlak fıtri / iradeli; hüküm-ahiret altıncı boyut. Tek/Yek ayrı yedinci fiziksel boyut değildir. Fiziğin ikinci evresinde ve biyolojik örgütlenmede merkez–çevre ilkesi, ontolojik bir düzen analojisi olarak kullanılır; ampirik doğa yasalarıyla özdeşliği ayrıca kanıt gerektirir. Core 01'in kozmik boyutları, Core 13'ün insan katmanlarıyla aynı numaralandırma değildir.

**Yöntemsel sonuç:** Makalenin Wᵢ tanık raporları ve bağımsız kaynak kümeleri hakkındaki hesapları, iki insanın veya ölçüm kanalının bir sonuca ilişkin kontrolünü modelliyor; insanın “ikinci bilen” olarak ahlaki ve ontolojik statüsünü matematiksel olarak açıklamıyor. Makalenin giriş, özet ve sonuçlarındaki “ikinci bilen” ifadeleri **bu sınırlamayla** okunmalıdır. Yeni ontolojik tanım için: `01-kanonik-denetim/HEBUN-VARLIK-AHLAK-IKINCI-BILEN-ONTOLOJIK-TANIM-2026-10-21.md`.

**Revizyon kaydı:** 21.10.2026 — kurucu açıklamasından sonra kapsam düzeltmesi. İstatistiksel sonuçlar korunmuş; önceki ontolojik yorumun eksik olduğu açıkça kaydedilmiştir. Tam metnin sonraki sürümünde bu ayrım özet, giriş, tanımlar ve tartışma bölümlerine bütünleştirilecektir.
