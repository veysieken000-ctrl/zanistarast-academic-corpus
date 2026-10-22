# HEBÛN-02 v0.2 — Ek A: “tek merkez” okumasının sonlu ağ evreninde sağlamlık sınaması

**Kimlik:** HEBUN-02/A02, v0.2-Ek A (aynı makale ailesi; yeni benzersiz makale değildir). **Tarih:** 22.10.2026. **Alan:** bilim felsefesi, çizge kuramı, model eleştirisi. **Ana metin:** [Bölüm I](HEBUN-02-v0.2-PART-1-KAYNAK-VE-KURAM.md), [Bölüm II](HEBUN-02-v0.2-PART-2-BICIMSEL-MODEL.md), [Bölüm III](HEBUN-02-v0.2-PART-3-KARSI-ORNEKLER.md), [Bölüm IV](HEBUN-02-v0.2-PART-4-YONTEM-ETIK-KALITE.md). **Durum:** bilimsel yöntem eki; insan hakemliğinden geçmemiştir.

## Özet ve özgün soru

Kıble/merkez–çevre ilkesinin bütün bağlantılı sistemlerde **benzersiz bir derece merkezi** bulunduğu biçimindeki ampirik-matematiksel yorumu, tek bir dört düğümlü çevrimle çürütülebilir. Ancak tek karşı örnek bir istisna diye göz ardı edilebilir. Bu ek, dört düğümlü **bütün** etiketli, yönsüz, basit ve bağlantılı çizgeleri eksiksiz sayarak karşı-modelin duyarlılığını inceler. Altı izomorfizm sınıfından oluşan 38 bağlantılı çizgenin 16'sında tek, 18'inde iki, dördünde dört derece-maksimum düğümü vardır. Bu tam sayım gerçek dünya ağlarının sıklığına ilişkin istatistik değildir. Katkı, kanonik beyanı değiştirmeden belirli bir operasyonelleştirmeyi, olumlu/olumsuz kontroller ve iki bağımsız hesaplama yolu ile denetlemektir.

**Kanonik beyan aynen:** Ehad Yek'tir ve Ehad âlemlerdeki her şeyi Yek'e göre yaratmıştır; her kar tanesi, her parmak izi dahil.

Bu teolojik/kurucu beyan, aşağıdaki çizge önermesinin aksiyomu ya da deneysel sonucu değildir. Yek, insan özü, makale birleştirme aracı veya yaratılmış ek boyut değildir. Core 01'in kozmik 6+Tek dizisi ile Core 13'ün insan katmanları farklı türdedir; bu ek onları birleştirmez.

## A1. Önermenin kapsamı ve yakın literatür

**Hedeflenen koşullu sav (U):** “Her sonlu, bağlantılı, yönsüz, basit ağda normalize derece-merkeziliğini en büyük yapan **tam bir** düğüm vardır.” Buradaki “tam bir” benzersizlik belirtir. Bunun aksine “en az bir maksimum vardır” sonlu ağlarda zaten doğrudur ve merkez–çevre öğretisine ampirik özgünlük sağlamaz.

Linton C. Freeman'ın *Social Networks* 1(3), 215–239'da yayımlanan “Centrality in Social Networks: Conceptual Clarification” makalesi (1978 tarihli künye; bazı kataloglarda 1979; DOI 10.1016/0378-8733(78)90021-7), derece, yakınlık ve aracılık merkeziliğini farklı kavramsal temellerle ayırır. Burada yalnız **derece** ölçütü kullanılır; diğer iki ölçüt hakkında genelleme yapılmaz. NetworkX'in resmî derece-merkeziliği tanımı basit n düğümlü çizgede deg(v)/(n−1) normalizasyonunu verir (22.10.2026 erişim): https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.degree_centrality.html . Freeman künyesi: https://doi.org/10.1016/0378-8733(78)90021-7 .

**Kanonik dayanak:** Core 01 [C1] Git blob `faa04bb3130b670a4712854defe364d94a08991c`; Core 13 [C2] blob `6a6c822a1910fd5f422eb1a0f2a50201566694ff`; HEBUN-02 v0.2 Bölüm I [C1–C6] kaynak hiyerarşisini ve özel Word'ün eşleştirilmemiş olmasını açıklar. Bu ek kaynakları doğrudan yeniden yayımlamaz. “Merkez olmadan çevre olmaz” önermesinin ontolojik yorumu ile (U) eşdeğer sayılmaz.

## A2. Ön kayıt niteliğinde biçimsel yöntem

V={0,1,2,3}, olası kenar kümesi E*= {{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}}. Bir çizge E⊆E* ile belirlenir: tam **2^6=64** etiketli çizge vardır. Dört düğümün hepsinin aynı bağlantılı bileşende olması şartıyla 38'i kabul edilir. Her v için d(v)=|{e∈E:v∈e}|; c(v)=d(v)/3; W(E)={v:c(v)=max_u c(u)}; sonuç değişkeni m(E)=|W(E)|. Hipotez U, bağlantılı her E için m(E)=1 olmasıdır.

**Yöntem kararı:** Önce bağlantılılık, sonra m hesaplanır; kenar ağırlığı, öz döngü, yön, fonksiyonel kıble veya fiziksel yörünge sonradan eklenmez. Aynı düğüm etiketleriyle çizilmiş izomorf çizgeler **etiketli sayımda** ayrı sayılır; bu, doğadaki ağları rastgele ve eş olasılıklı örneklediğimiz anlamına gelmez. Kod: `07-deneyler-ve-karsi-ornekler/hebun02_graph_robustness.py`; Python ≥3.8 standart kütüphane, rastgelelik ve haricî veri yoktur.

## A3. Birinci kanıt: izomorfizm sınıflarıyla tam sayım

Bağlantılı dört-düğümlü basit yönsüz çizgelerin altı izomorfizm tipi vardır. Her sınıftaki **etiketli** çizge sayısı 4!/|Aut(G)| olarak hesaplanır. Tablo ayrıca derece maksimumlarının sayısını verir:

| Tip | Kenar sayısı | Otomorfizm grubu büyüklüğü | Etiketli çizge | m(E) |
|---|---:|---:|---:|---:|
| Yıldız K₁,₃ | 3 | 6 | 4 | 1 |
| Dört düğümlü yol P₄ | 3 | 2 | 12 | 2 |
| Üçgen + bir asılı düğüm | 4 | 2 | 12 | 1 |
| Dört düğümlü çevrim C₄ | 4 | 8 | 3 | 4 |
| K₄'ten bir kenar silinmiş (elmas) | 5 | 4 | 6 | 2 |
| Tam çizge K₄ | 6 | 24 | 1 | 4 |

Toplam 4+12+12+3+6+1=**38**. Tek maksimum: 4+12=**16**; iki maksimum: 12+6=**18**; dört maksimum: 3+1=**4**; üç maksimum: **0**. Her sınıfın bağlantılı olduğu doğrudan kenarlarından görülür. Dört düğümde bağlantılı çizgenin en az üç kenarı olması ve üç/dört/beş/altı kenarlı bağlantılı izomorfizm tiplerinin yukarıda tüketilmesi tamlık kanıtını verir. Böylece U'nun öncülünü sağlayan, fakat sonucunu sağlamayan 22 etiketli çizge vardır. **U yanlıştır.**

## A4. İkinci kontrol: 64 çizgenin kodla taranması

Ayrı algoritma altı olası kenarı altı bitlik maske ile seçer; bağlantılılığı düğüm erişilebilirliğiyle test eder; derece vektöründen maksimum eşitliklerini sayar. Beklenen çıktılar: `connected=38`, `m=1:16`, `m=2:18`, `m=3:0`, `m=4:4`. Bunlar A3'teki grup-simetri hesabından bağımsız **hesaplama yolu** sunar; aynı yazar/model tarafından tasarlandığından bağımsız insan hakemliği değildir. Pozitif kontrol yıldız (m=1); negatif kontroller yol (m=2), çevrim ve tam çizge (m=4). Yalnız C₄ testiyle yetinilmemiştir.

**Tekrarlanabilir komut:** `python3 07-deneyler-ve-karsi-ornekler/hebun02_graph_robustness.py`. Komutun başarı kaydı ancak çalıştırma, Git blob eşitliği ve dal-ref geri okuması tamamlandıktan sonra `10-uretim-takibi` altındaki ayrı kanıtla doğrulanır; kodun depoya yazılması tek başına PASS değildir.

## A5. Alternatif açıklamalar ve yanlışlama sınırları

**Alternatif M1:** Benzersiz merkez yalnız yıldız gibi bazı ağ ailelerinin özelliğidir. Bu, (U)'nun evrenselliğini kaldırır ve hangi sistemlerde beklendiğini önceden sınırlamayı gerektirir. **M2:** “Merkez” derece değil, işlevsel/çekimsel/teolojik bir özelliktir. Bu alternatif C₄'ün derecelerine dayanılarak ne ispatlanır ne reddedilir; ayrı gözlem ölçütü, ağ sınırı ve karşı tahmin ister. **M3:** Ağın benzersiz maksimumu, sistem sınırları veya ölçüm anı değiştirilerek elde edilir. Ölçüt sonuçtan sonra seçilirse yanlışlamaya karşı koruyucu ve seçici bir yeniden tanımlamadır. Bağımsız ağlarda ön kayıt gerekir.

**Duyarlılık:** Etiketli çizge sayılarının oranı `16/38`, gerçek ağlarda merkez bulunma olasılığı değildir. Farklı n, yönlülük, ağırlık, zamansallık, çok katmanlılık ve merkezilik tanımları sonuç dağılımını değiştirebilir. Teolojik Yek veya kıble ilkesi bu sınırlı kombinatorik modelde ölçülmemiştir. Hiçbir insan, hayvan veya özel veri kullanılmamıştır; p-değeri, deneysel bulgu, bilimsel hakem onayı veya evrensel kozmolojik ispat iddia edilmez.

## A6. Dergi/etik, kalite kapıları ve revizyon günlüğü

**Hedef dergi (yalnız kalite ölçütü):** *Philosophy of Science* (Cambridge University Press). Resmî yönerge **22.10.2026** kontrol edildi: araştırma makalesi 9000 sözcük (basılı ekler dahil, kaynakça hariç), yeni felsefi katkının literatüre yerleştirilmesi ve anonim inceleme için hazırlık beklenir: https://www.cambridge.org/core/journals/philosophy-of-science/information/author-instructions . Bu Türkçe çalışma eki anonim İngilizce dergi makalesi değildir. **Dış gönderim, DOI başvurusu, arXiv, ödeme, dergi hesabı veya yayın yapılmaz.** AI açıklaması: OpenAI GPT-6, 22.10.2026, metin, biçimsel argüman ve sentetik kod üretimi; AI insan hakem değildir. Çıkar çatışması ve finansman hakkında doğrulanmamış beyan yoktur.

| Kapı | Ek A durumu | Gerekçe |
|---|---|---|
| K0 kanonik kaynak | KISMİ | Core 01/13 blob referansları mevcut; özgün Word tam paragraf eşlemesi yok. |
| K1 literatür | KISMİ | Freeman ve resmî NetworkX tanımı; sistematik ağ felsefesi taraması yok. |
| K2 formalizasyon | GEÇTİ (dar) | U açık; iki hesaplama yolu, altı izomorfizm tipi, sınır koşulları. |
| K3 tekrarlanabilirlik | KOD ÇALIŞTIRMA KANITINA BAĞLI | 64 çizgenin eksiksiz taranması için kod; gerçek ağ deneyi değil. |
| K4 karşı açıklama | GEÇTİ (dar) | M1–M3, yıldız pozitif kontrolü ve üç negatif kontrol. |
| K5 etik/dergi | KISMİ | Tarihli resmî yönerge ve AI beyanı; son dergi biçimi yok. |
| K6 bağımsız denetim | AÇIK | Analitik ve kodsal yollar ayrı; insan ikinci değerlendirici yok. |

**Revizyon günlüğü:** HEBUN-02 v0.2 Bölüm II'deki tek C₄ tanığı → aynı sürüm ailesinde Ek A: bütün bağlantılı dört-düğümlü çizgelerin sınıflandırılması, tam sayım, olumlu/olumsuz kontroller, operasyonel anlam ayrımı ve yeniden üretim kodu. **412 aday kaynak 412 benzersiz veya yayıma hazır makale değildir.**
