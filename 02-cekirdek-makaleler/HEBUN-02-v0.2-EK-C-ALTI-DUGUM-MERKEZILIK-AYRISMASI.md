# HEBÛN-02/A02 v0.2 — Ek C: Altı düğümde benzersiz merkezlerin ayrışması

**Kimlik:** HEBUN-02/A02, Ek C (22.10.2026). Bu metin [Ek B](HEBUN-02-v0.2-EK-B-MERKEZILIK-OLCUT-DUYARLILIGI.md) ve dört ana bölümle **tek makale ailesidir**; yeni bağımsız makale değildir. **Alan:** bilim felsefesi, sonlu çizge kuramı, ölçüm kuramı. **Durum:** bağımsız hesaplamalı kuramsal araştırma; hakemli veya yayıma hazır değildir.

## Öz
Kozmik merkez–çevre (kıble) analojisinden ağlarda ölçütten bağımsız bir merkez çıkıp çıkmadığı sorusu, ölçülebilir çizge savı olarak ayrıştırılır. Önceki Ek B'de dört ve beş düğümlü bağlantılı ağlarda derece, yakınlık ve aracılık merkeziliklerinin üçü de benzersiz maksimuma sahipse aynı düğümün seçildiği bulunmuştu. Bu ek, altı düğümde bunun yanlış olduğunu gösterir: 26.704 bağlantılı etiketli çizgeden 720'sinde üç ölçüt de benzersiz maksimum verirken en az biri başka düğümü seçer. Bu 720 çizge tek bir izomorfizm sınıfıdır. Sonuç teolojik bir iddiayı değil, ampirik olarak okunmaya zorlanan ölçüt-bağımsız evrenselliği sınırlar.

## 1. Araştırma sorusu, kanonik sınır ve literatür
**Soru:** Sonlu, basit, yönsüz, ağırlıksız ve bağlantılı ağlarda derece, yakınlık ve aracılık merkeziliği ayrı ayrı benzersiz kazanan üretiyorsa kazanan zorunlu olarak aynı mıdır? En küçük karşı örneğin düğüm sayısı kaçtır?

**Kurucu beyan aynen:** Ehad Yek'tir ve Ehad âlemlerdeki her şeyi Yek'e göre yaratmıştır; her kar tanesi, her parmak izi dahil.

Bu beyan teolojik/kurucudur; Yek ne insan özü ne de yaratılmış yedinci katmandır. Core 01'in 6+Tek kozmik boyutları ve Core 13'ün insan katmanları birbirine sayısal olarak eşlenmez. Doğrusal kapsama ontolojik açıklama bağımlılığıdır; çizge merkeziliği bir kozmik boyut veya ruhun deneysel ölçüsü değildir. Bu ek yalnız Ek B'de açıkça tanımlanan **çizge yorumunun** matematiksel sınırını araştırır. Freeman (1978/1979) derece, yakınlık ve aracılık kavramlarını ayırır; Brandes (2001) aracılık için hesaplama yöntemini ele alır. Bu yöntemlerin keşfi veya ilk çizge karşı örneğinin dünya literatüründe keşfi iddia edilmez; özgün katkı, HEBUN-02'deki H3 savının tam sonlu denetimidir.

**Kanonik kaynak kimlikleri:** Core 01 `core-01.html`, blob `faa04bb3130b670a4712854defe364d94a08991c`; Core 13 `core-13-zanistarast-medeniyet-modeli.html`, blob `6a6c822a1910fd5f422eb1a0f2a50201566694ff`. Ana makalenin Bölüm I'i [C1–C6] kaynak hiyerarşisini ve özgün Word'ün tam paragraf eşlemesi eksikliğini kaydeder; özel tam metin buraya aktarılmadı.

## 2. Yöntem ve yanlışlanabilir H3
Düğüm kümesi `V={0,…,n−1}` ve `n∈{2,3,4,5,6}` olsun. Bütün `2^(n(n−1)/2)` basit etiketli ağların kenar altkümeleri taranır; bağlantısızlar dışlanır. `D(v)=deg(v)`; `C(v)=(n−1)/Σ_{u≠v}d(v,u)`; `B(v)=Σ_{s<t;s,t≠v}σ_st(v)/σ_st`. Bütün çiftler arasında en kısa yol sayıları `σ`, kesirleri `Fraction` ile **tam** hesaplanır. `W_M=argmax_v M(v)` tanımlanır. H3: `|W_D|=|W_C|=|W_B|=1 ⇒ W_D=W_C=W_B`. Yakınlıkta `−Σd` ile maksimum almak, bağlantılı sabit n için aynı kazananı verir.

## 3. Sonuç: en küçük karşı örnek ve sınıf kanıtı
| n | Bağlantılı etiketli ağ | Üç ölçütte de benzersiz kazanan | Üçü benzersizken farklı kazanan |
|---:|---:|---:|---:|
| 2 | 1 | 0 | 0 |
| 3 | 4 | 3 | 0 |
| 4 | 38 | 16 | 0 |
| 5 | 728 | 385 | 0 |
| 6 | 26.704 | 13.248 | **720** |

**Açık tanık W:** `E={(0,1),(0,3),(0,5),(1,2),(1,3),(1,4),(2,3),(2,4)}`. Derece puanları `(3,4,3,3,2,1)`, uzaklık toplamları `(7,6,8,7,9,11)`, normalize edilmemiş aracılık puanları `(4,7/2,1/2,1,0,0)`. Böylece `W_D={1}`, `W_C={1}`, `W_B={0}`. Üç kazanan da benzersizdir, fakat aynı değildir: **H3 yanlıştır.** Kesirlerin sayımı, bütün 15 düğüm çifti için bağımsız basit-yol DFS taramasıyla yeniden doğrulanmıştır; bu bir bilgisayar doğrulaması, insan hakemliği değildir.

**Minimalite (sınırlı ve kesin):** n=2–5 arası bütün bağlantılı etiketli ağların eksiksiz taramasında karşı örnek yoktur; n=6 tanığı vardır. Bu nedenle belirtilen üç merkezilik tanımı ve çizge sınıfı altında **en küçük düğüm sayısı altıdır**. n=6'daki 720 ayrışma çizgesinin tümü, W'nin 6! düğüm yeniden etiketlemesinden elde edilen 720 ayrı kenar kümesiyle **tam aynı kümedir**. Dolayısıyla W'nin otomorfizma grubu yalnız özdeşliktir ve bu boyutta ayrışma üreten **tek etiketsiz izomorfizm sınıfı** vardır. 720/26.704 oranı yalnız etiketli çizgelerin sayım oranıdır; gerçek ağlarda görülme olasılığı veya etiketsiz sınıfların eşit ağırlıklı oranı değildir.

## 4. Rakip açıklamalar ve ikinci kontrol
**R1 (işlevsel merkez):** Kıble bir ağın derece/yakınlık/aracılık tepe düğümüyle özdeş olmayabilir; karşı örnek ontolojik kıbleyi yanlışlamaz. **R2 (ölçüt seçimi):** Ölçütler veri görüldükten sonra değişirse H3'ün testi geriye dönük kurtarılır; merkez ölçütü önceden kaydedilmelidir. **R3 (model sınırı):** Yönlü, ağırlıklı, zamansal veya bağlantısız ağlara sonuç doğrudan taşınmaz. **R4 (hesaplama):** BFS en kısa-yol çarpım formülü, tanık W'de bütün basit yolları ayrı sayan DFS ile çapraz denetlenir; ayrıca W'nin bütün yeniden etiketlemeleriyle toplam ayrışma kümesi karşılaştırılır. Bunlar aynı araştırmacının algoritmik kontrolleridir, bağımsız insan değerlendirmesi değildir. **R5 (ampirik açıklama):** Güneş–gezegen veya kalp–dolaşım örneklerinden bütün soyut ağların aynı merkezi taşıdığı sonucu çıkmaz.

## 5. Yeniden üretim, etik, hedef dergi ve kalite
Kod: `07-deneyler-ve-karsi-ornekler/hebun02_six_node_unique_center.py`. Çalıştırma: `python3 07-deneyler-ve-karsi-ornekler/hebun02_six_node_unique_center.py`; Python ≥3.8, yalnız standart kütüphane, sabit örnek, rastgelelik veya dış veri yok. Tam tarama, tanık puanları, bağımsız DFS ve 720'lik yeniden etiketleme kümesi `assert` ile sınanır. Bu ek **yeni insan/hayvan deneyi, örneklem, p-değeri veya fiziksel ölçüm içermez**. AI: OpenAI GPT-6 metin ve kod araştırmasında kullanıldı; bağımsız hakem veya deney sonucu uydurulmadı.

**Yalnız kalite kıstası olarak olası hedef:** *Philosophy of Science* (Cambridge). 22.10.2026 tarihinde resmî [yazar yönergesi](https://www.cambridge.org/core/journals/philosophy-of-science/information/author-instructions) ve [hazırlık/atıf sayfası](https://www.cambridge.org/core/journals/philosophy-of-science/information/author-instructions/preparing-your-materials) kontrol edildi: araştırma makalesi 9.000 sözcük (kaynakça hariç, basılı ekler dahil), özet 100 sözcük, anonim değerlendirmeye uygun metin ve yazar–tarih atıf sistemi. Bu Türkçe ek dergiye uygun tamamlanmış İngilizce makale değildir. **Dış gönderim, DOI alma, arXiv, hesap açma, ödeme veya yayın yoktur.**

**K0 KISMİ:** Core blob kimlikleri biliniyor, özgün Word paragraf eşlemesi eksik. **K1 KISMİ:** Freeman/Brandes seçici karşılaştırması, sistematik literatür taraması yok. **K2 GEÇTİ (dar):** H3 ve çizge sınıfı kesin. **K3 GEÇTİ (dar, yerel yürütmeye bağlı):** sentetik tam sayım ve DFS; ampirik veri yok. **K4 GEÇTİ (dar):** R1–R5 ve W karşı örneği. **K5 KISMİ:** güncel resmî yönerge kontrolü, dergiye uygun tam metin yok. **K6 AÇIK:** bağımsız insan hakem yok. Commit ve dal-ref geri okuma doğrulanmadan K3'ün depo-kayıt durumu tamamlandı sayılmaz.

## Kaynakça
- Brandes, Ulrik. 2001. “A Faster Algorithm for Betweenness Centrality.” *Journal of Mathematical Sociology* 25(2):163–177. https://doi.org/10.1080/0022250X.2001.9990249 .
- Freeman, Linton C. 1978/1979. “Centrality in Social Networks: Conceptual Clarification.” *Social Networks* 1(3):215–239. https://doi.org/10.1016/0378-8733(78)90021-7 .
- Cambridge University Press. *Philosophy of Science*, author instructions and preparing your materials, erişim/kontrol: 22.10.2026 (bağlantılar yukarıda).

**Revizyon günlüğü:** HEBUN-02 v0.2 ana makale C4 → Ek A n=4 derece tam sayımı → Ek B n=4–5 üç ölçüt → **Ek C n=2–6 minimal benzersiz-kazanan ayrışması ve izomorfizm sınıfı**. Tek HEBUN-02 ailesi; 412 aday 412 benzersiz veya yayıma hazır makale değildir.
