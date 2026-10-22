# HEBÛN-02 v0.2 — Ek B: Merkezilik ölçütü değiştiğinde tek merkez savı

**Kimlik:** HEBUN-02/A02, v0.2-Ek B, 22.10.2026. Ek A ve dört ana bölümle **tek makale ailesi**; ayrı benzersiz makale değil. Alan: bilim felsefesi ve sonlu çizge kuramı. Durum: bağımsız biçimsel araştırma, hakemli/yayıma hazır değil. Önceki çalışma: [Ek A](HEBUN-02-v0.2-EK-A-KARSIMODEL-SAGLAMLIK.md); [kuram](HEBUN-02-v0.2-PART-1-KAYNAK-VE-KURAM.md).

## Öz ve soru

“Her bağlantılı ağın benzersiz merkezi vardır” savının doğruluk değeri, merkeziliğin nasıl tanımlandığına bağlıdır. Ek A'daki derece merkeziliği n=4 tam sayımını, yakınlık ve aracılık merkeziliğine ve n=5'e genişletiyoruz. Dört düğümde 38 bağlantılı etiketli ağın kazanan kümeleri üç ölçütte aynıdır; beş düğümde 728 ağın sırasıyla 60, 150 ve 90'ında ölçüt çiftleri farklı enbüyükleyici kümeleri verir. Bu sonuç matematiksel operasyonelleştirme duyarlılığıdır; kıble/Yek veya fiziksel evrenin deneysel doğrulaması değildir.

**Kurucu beyan aynen:** Ehad Yek'tir ve Ehad âlemlerdeki her şeyi Yek'e göre yaratmıştır; her kar tanesi, her parmak izi dahil.

Yek insan özü, metin entegrasyonu veya yaratılmış boyut değildir. Core 01'in kozmik 6+Tek'i ile Core 13'ün insan katmanları (fizik, biyoloji, zihin, ahlak, akıl, duygu + öz) ayrı türlerdir. Ontolojik kapsama, kronoloji ya da ampirik ispat değildir.

## 1. Kaynaklar, yenilik ve rakip açıklama

Kanonik Core 01 blob `faa04bb3130b670a4712854defe364d94a08991c`; Core 13 blob `6a6c822a1910fd5f422eb1a0f2a50201566694ff`. HEBUN-02 Bölüm I [C1–C6] kaynak ayrımlarını verir. Özgün özel Word tam paragraf eşlemesi eksik; kaynak metinler buraya kopyalanmadı. Freeman, *Social Networks* 1(3), 215–239, DOI 10.1016/0378-8733(78)90021-7, merkezilik kavramlarını ayırır. Brandes, *Journal of Mathematical Sociology* 25(2), 163–177 (2001), DOI 10.1080/0022250X.2001.9990249, aracılık hesaplamasının algoritmik literatürüdür. Formüller 22.10.2026'da resmî NetworkX derece/yakınlık/aracılık belgeleriyle karşılaştırıldı: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.degree_centrality.html ; https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.closeness_centrality.html ; https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.betweenness_centrality.html . Ölçütler yeni değildir; katkı, bu kanonik soru için eksiksiz n=4–5 sayımı ve ikinci algoritmayla karşı denetimdir. Sistematik literatür taraması yapılmadı.

## 2. Yöntem ve önermeler

V={0,…,n−1}, n∈{4,5}; basit, ağırlıksız, yönsüz, bağlantılı etiketli G=(V,E). Sırasıyla 2^6=64 ve 2^10=1024 olası ağ taranır. D(v)=deg(v); C(v)=(n−1)/Σ_{u≠v}d(u,v); B(v)=Σ_{s<t;s,t≠v}σ_st(v)/σ_st. σ_st en kısa yolların sayısı, σ_st(v) v'yi iç düğüm olarak kullananların sayısıdır. B tam rasyonel `Fraction` ile hesaplanır. W_M(G)=argmax_v M(v); m_M(G)=|W_M(G)|.

**H1:** Her bağlantılı ağda m_D=1. **H2:** Her bağlantılı ağda W_D=W_C=W_B. **H3:** Üç ölçütün ayrı ayrı tek kazananı varsa bu düğümler aynıdır. H1/H2 evrensel savlardır; H3 yalnız taranan n için sınanır. BFS uzaklık ve en kısa yol sayısı çıkarır. Bağımsız DFS bütün basit yolları sayıp en kısalarını seçer; her bağlantılı ağın her düğüm çifti için BFS yol sayısı ve iç-düğüm paylarıyla eşitlik testi yapılır. Kod: `07-deneyler-ve-karsi-ornekler/hebun02_centrality_sensitivity.py`; Python ≥3.8, standart kütüphane, haricî veri veya rastgelelik yok. Farklı algoritmalar **bağımsız insan hakemliği değildir**.

## 3. Tam sayım bulguları

| n | Ölçüt | Bağlantılı ağ | m=1 | m=2 | m=3 | m=4 | m=5 |
|---:|---|---:|---:|---:|---:|---:|---:|
| 4 | Derece | 38 | 16 | 18 | 0 | 4 | — |
| 4 | Yakınlık | 38 | 16 | 18 | 0 | 4 | — |
| 4 | Aracılık | 38 | 16 | 18 | 0 | 4 | — |
| 5 | Derece | 728 | 385 | 170 | 130 | 30 | 13 |
| 5 | Yakınlık | 728 | 445 | 170 | 70 | 30 | 13 |
| 5 | Aracılık | 728 | 505 | 200 | 10 | 0 | 13 |

n=4'te üç ölçütün **kazanan kümeleri** 38/38 ağda aynıdır (yalnız histogram eşitliği değil). n=5'te W_D≠W_C: 60; W_D≠W_B: 150; W_C≠W_B: 90. n=5 imza (m_D,m_C,m_B) dağılımı: (1,1,1):385; (2,2,2):170; (3,1,1):60; (3,3,1):60; (3,3,3):10; (4,4,2):30; (5,5,5):13; toplam 728. Üç ölçütte ayrı ayrı tek kazanan bulunan 385 ağda kazanan aynı düğümdür. **Bu n≥6 için H3 ispatı değildir.** Sayılar gerçek ağların görülme olasılığı değildir.

**Karşı örnek E1:** E={{0,2},{0,4},{1,2},{1,3}}. Dereceler (2,2,2,1,1), uzaklık toplamları (7,7,6,10,10), aracılık (3,3,4,0,0). W_D={0,1,2}, W_C=W_B={2}. **E2:** E={{0,1},{0,2},{0,4},{1,2},{1,3},{2,3}}. Dereceler (3,3,3,2,1), uzaklık toplamları (5,5,5,7,8), aracılık (3,1,1,0,0). W_D=W_C={0,1,2}, W_B={0}. H2 yanlıştır; H1'i Ek A'daki C4 zaten çürütür. n=4'te ölçütler eşit görünürken n=5'te bağların farklı çözülmesi, seçilen ölçeğin önemini gösterir.

## 4. Sınırlar, etik ve kalite kapıları

Rakip R1: kıble/işlevsel merkez çizge merkezi olmayabilir; ayrı ön kayıtlı ölçüm ister. R2: ağ sınırını veya ölçütü sonuçtan sonra değiştirmek seçici doğrulamadır. R3: n≥6, yönlü, ağırlıklı, zamansal ve bağlantısız ağlara genelleme yapılamaz; sonraki yanlışlama hedefi n≥6'da H3'e karşı model aramaktır. R4: etiketli çizge sayımı izomorfizm sınıflarına eşit ağırlık vermez. R5: teolojik, ontolojik, biçimsel, normatif ve ampirik iddialar birbirine indirgenemez; ruh, ahlak ve ahiret graf puanları değildir.

**Olası hedef dergi, yalnız kalite ölçütü:** *Philosophy of Science*, Cambridge. Resmî yönerge 22.10.2026'da kontrol edildi: https://www.cambridge.org/core/journals/philosophy-of-science/information/author-instructions . Makale üst sınırı 9000 sözcük (basılı ekler dahil; kaynakça hariç); özgün felsefi katkı ve literatüre yerleştirme gerekir. Türkçe ek anonim İngilizce son makale değildir. Dış gönderim, DOI, arXiv, hesap, ödeme, yayın yapılmaz. AI açıklaması: OpenAI GPT-6 (22.10.2026) metin ve kod üretiminde kullanıldı; insan hakem değildir. İnsan/hayvan deneyi, özel veri, finansman ve deney sonucu uydurulmadı.

**K0 KISMİ:** özgün Word tam eşlemesi yok. **K1 KISMİ:** seçici Freeman/Brandes/NetworkX, sistematik tarama yok. **K2 GEÇTİ (dar):** H1–H3 kesin tanımlı. **K3 KOD YÜRÜTME + DAL-REF DOĞRULAMASINA BAĞLI:** BFS–DFS testleri. **K4 GEÇTİ (dar):** E1/E2, R1–R5. **K5 KISMİ:** tarihli yönerge ve AI beyanı, son dergi sürümü yok. **K6 AÇIK:** bağımsız insan denetçi yok.

**Revizyon günlüğü:** v0.2 ana metin C4 karşı örneği → Ek A n=4 derece tam sayımı → Ek B n=4–5 üç ölçütte tam sayım ve kısa-yol çapraz denetimi. Aynı HEBUN-02 ailesidir; 412 aday kaynak 412 benzersiz veya yayıma hazır makale değildir.
