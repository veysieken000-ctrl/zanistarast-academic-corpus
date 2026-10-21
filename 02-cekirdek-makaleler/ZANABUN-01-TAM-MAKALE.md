# ZANABUN-01 — Bağımsız Tanıklık, Ortak Hata ve Yöntem Çeşitliliği

**Araştırma makalesi, v0.2, 21 Ekim 2026.** Alan: bilim felsefesi, sosyal epistemoloji ve ölçüm kuramı. Dergiye gönderilmedi; hakem değerlendirmesinden geçmedi.

## Öz

Zanabûn epistemolojisinin ikinci bilenin sonucu bağımsız biçimde doğrulaması ilkesi, tanıklar arası basit mutabakattan daha güçlüdür. Bu çalışma özgün metindeki tanıklık ortalaması ve varyansı önerilerini ortak hata modeliyle inceler. Kusursuz mutabakatın yanlış sonuçla bağdaşabildiği bir karşı örnek sunar; yöntem kümeli hata ayrıştırmasıyla farklı yöntemlerin bazı ortak hata bileşenlerini azaltabileceğini, fakat tüm yöntemlere ortak hatayı gideremeyeceğini gösterir. Bulgular matematiksel model sonuçlarıdır; gerçek tanık verisi veya teolojik ispat değildir.

## 1. Kurucu Çerçeve

Zanabûn kurucu formülü: “Bilen öznenin bilinen nesneye yönelimi sonucu ortaya çıkan sonucun ikinci bilen tarafından onayı.” İkinci bilen birinci öznenin otoritesini değil, ortaya çıkan sonucu kendi gözlem, deney ve akıl yürütmesiyle denetler. Kanonik teolojik beyan aynen: “Ehad Yek'tir ve Ehad âlemlerdeki her şeyi Yek'e göre yaratmıştır; her kar tanesi, her parmak izi dahil.” Bu ifade aşağıdaki matematiksel sonuçlardan türetilmemiştir.

## 2. Tanık Mutabakatının Sınırı

Özgün metinde K = (1/n) Σ W_i ve V = (1/n) Σ(W_i-K)^2 önerilir. Bu büyüklükler tanıkların yakınlığını ölçer; dış gerçekliğe uygunluğu garanti etmez. θ=0 ve W=(5,5,5,5) için K=5, V=0, |K-θ|=5. Bu örnek Zanabûn'un tümünü değil, yalnız düşük varyansı doğrulukla özdeşleştiren dar işlemsel yorumu çürütür.

## 3. Ortak Hata ve Yöntem Çeşitliliği

X_i = θ + B + ε_i olsun. B tüm gözlemcilere ortak, ε_i özel hatadır. Bağımsız ve sıfır ortalamalı bileşenlerin varyansları sırasıyla τ² ve σ² ise Var(X̄-θ)=τ²+σ²/n. n büyürken ortak bileşen kalır. Bu, bilinen kovaryans özdeşliğinin uygulamasıdır; yeni matematik teoremi değildir.

Dengeli m yöntem kümesinde n gözlem için X_gi = θ+B_0+B_g+ε_gi yazılsın. B_0 tüm yöntemlere ortak, B_g yalnız g yöntemine ortak hatadır. Bağımsız sıfır ortalamalı bileşenler altında Var(X̄-θ)=τ_0²+τ_g²/m+σ²/n. n=16, τ_0=1, τ_g=2, σ=1 için m=1 durumunda teorik RMSE=2.25, m=4 durumunda yaklaşık 1.43614'tür. Bu sayılar saha gözlemi değildir.

## 4. Kaynak Soyu

Özgün Zanabûn: veysieken000-ctrl/zanistarast-ontology, papers/zanabun.md, blob ee68095b8d87ba8a580492cfd4c98b86e0a0f21a. Önceki taslak: zanistarast-ai-native-model, research/yek-6tek-makale-programi-2026-10-16, research/yek-6tek-program/manuscripts/ZANABUN-01-bagimsiz-taniklik-ve-ortak-hata.md, blob dea450a481b14f2668480513156a96e965d676f3. Bu metin aynı ZANABUN-01 sürüm ailesidir; yeni bağımsız makale olarak sayılmaz.


## 5. Özdeşlik, Bağımsızlık ve Belirlenebilirlik

Tanıkların ayrı kişiler olması hata kaynaklarının ayrı olduğu anlamına gelmez. İki gözlemci aynı sensör kalibrasyonunu, aynı veri kümesini, aynı haber ajansını veya aynı model çıktısını kullanabilir. Bu durumda kurumsal ve kişisel ayrılık, yöntemsel bağımsızlık için yeterli değildir. Tanık sayısı n ile bağımsız kanıt kanalı sayısı m farklı büyüklüklerdir. Bağımsızlık değerlendirmesi kaynak soyağacı, kalibrasyon geçmişi, ortak eğitim verisi, ortak örneklem ve eşzamanlı çevresel etkenleri ayrı ayrı izlemelidir.

Daha güçlü bir sınırlama vardır: yalnızca X_i=θ+B+ε_i gözleniyorsa, sabit ve bilinmeyen B altında θ tek başına belirlenemez. Herhangi bir c için θ'=θ+c ve B'=B-c dönüşümü tüm X_i gözlemlerini değiştirmez. Dolayısıyla sınırsız tanık sayısı bile, dış dayanak olmadan θ ile ortak yanlılığı ayırt edemez. Bu bir özdeşlik problemidir; tanık sayısının yetersizliğiyle karıştırılmamalıdır. Sıfır ortalamalı rassal B varsayımı, tekrarlanan bağımsız deneyler üzerinden bir popülasyon modelidir; tek bir deneyde gözlenen ortak yanlılığın sıfır olduğu anlamına gelmez.

## 6. Etkin Tanık Sayısı

Eşit varyanslı tanık hatalarının ikili korelasyonu ρ ve her birinin varyansı s² ise ortalamanın varyansı s²[1+(n-1)ρ]/n olur. Bu, bağımsız gözlemci sayısına eşdeğer n_eff=n/[1+(n-1)ρ] tanımını verir. n=16 ve ρ=0.25 için n_eff yaklaşık 3.3684'tür. Bu sayı bağımsız bilgi miktarının tüm boyutlarını ölçmez; yalnız eşdeğer varyanslı, değiştirilebilir korelasyon modelinin etkin örneklem karşılığıdır. Negatif korelasyon ve eşitsiz güvenilirlik hâllerinde yorum ayrıca değişir.

## 7. Yanlışlamaya Yönelik Deney Tasarımı

Önceden kayıt altına alınacak bir sentetik karşılaştırmada toplam tanık sayısı n=16 sabit tutulur. A koşulu tek yöntem kümesi, B koşulu dört yöntem kümesi, C koşulu on altı yöntem kümesidir. Tüm koşullarda küresel hata standart sapması 1, yöntem hatası 2, özel hata 1 alınır. Her sentetik tekrar yeni küresel, yöntemsel ve özel hatalar üretir; dış referans θ bilinir. Birincil sonuç ortalamanın referansa göre kök ortalama kare hatasıdır (RMSE). İkincil sonuç tanıklar arası varyanstır; ikincil sonuç doğruluk göstergesi diye yorumlanmaz. Analitik beklentiler sırasıyla 2.25, yaklaşık 1.43614 ve yaklaşık 1.14564 RMSE'dir. Bu beklenen değerler simülasyon sonucu değil, model hesabıdır.

Yanlışlama ölçütleri: (i) kodda bağımsız hata üretimi varsayımı sağlandığı hâlde simülasyon tahminleri analitik değerlere tolerans içinde yaklaşmazsa uygulama hatası araştırılır; (ii) yöntem çeşitliliği yeni ortak yanlılık yaratıyorsa modelin bağımsızlık varsayımı reddedilir; (iii) bağımsız dış ölçüt mevcut değilse doğruluk iddiası askıda tutulur. Kontrol olarak yöntem grupları aynı küresel kaynağa bağlandığında ortak hata tabanı korunmalıdır.

## 8. Kurucu İlkenin İşlemselleştirilmesi

İkinci bilenin doğrulaması için önerilen üç koşul birlikte raporlanır: (a) aynı sorunun açık ve değişmeyen tanımı, (b) ilk sonucun dışında veri, yöntem veya kalibrasyon kanalı, (c) mümkünse önceden belirlenmiş dış referans veya ayırt edici müdahale. Bunlar Zanabûn'un özgün metninde tamamlanmış bir algoritma olarak mevcut değildir; bu makalenin önerdiği denetim şemasıdır. Felsefi anlamdaki gerekçelendirme, güvenilirlik ve doğruluk kavramları bu üç teknik koşula indirgenmez.
