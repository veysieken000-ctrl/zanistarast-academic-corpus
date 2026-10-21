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
