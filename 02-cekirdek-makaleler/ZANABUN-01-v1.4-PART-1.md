# ZANABUN-01 v1.4 — İki yanlı kaynakta bağımsız onayın sınırları
## I. Özet, kanonik zemin ve literatür

**Makale kimliği:** ZANABUN-01. **Sürüm ailesi:** v1.0 → v1.2 → v1.3 → v1.4, tek makale; dört ayrı makale değildir. **22.10.2026.** Alan: analitik/formel sosyal epistemoloji. Bu dosya II–IV bölümleriyle tek araştırma metnidir. Hakemli, gerçek verili veya yayıma hazır değildir; dergiye gönderim, DOI, arXiv, ücret, hesap veya yayın yapılmayacaktır.

### Özet

İkinci kaynağın ayrı olması, hatalarının ilk kaynaktan bağımsız veya yanlılıksız olduğu anlamına gelmez. Zanabûn'un sonucun ikinci bilen tarafından onaylanması ilkesinin dar yöntemsel sınırlarını araştıran bu çalışma, iki kaynakta da sınırlı sistematik yanlılık ve belirsiz hata kovaryansı varken konveks tahmin ağırlığının minimaks çözümünü türetir. Sıfır ortalamalı kaynak hata varyansları v_A,v_B, yanlılık sınırları a,b ve kovaryans üst sınırı c_üst olsun. A=v_A+a², B=v_B+b², C=c_üst+ab için, uygun pozitif payda altında ikinci kaynağın minimaks ağırlığı t*=clip[(A−C)/(A+B−2C),0,1] bulunur. C≥A durumunda ağırlık sıfırdır. Yedi kurgusal senaryo, tam kesir hesabı, 8×8 tanık kovaryansı, yanlılık uçları ve ağırlık ızgarasıyla sınanır. Sonuçlar yalnız model varsayımlarında geçerlidir; ontolojik veya teolojik kanıt, gerçek insan deneyi veya evrensel matematik keşfi iddia edilmez.

**Anahtar kelimeler:** Zanabûn, Hebûn, ikinci bilen, epistemik bağımsızlık, ortak hata, kovaryans, sınırlı yanlılık, minimaks, yeniden üretilebilirlik.

### 1. Özgün araştırma sorusu

Kurucu epistemik ifade: “Bilen öznenin bilinen nesneye yönelimi sonucu ortaya çıkan sonucun ikinci bilen tarafından onayı.” **Soru:** Her iki kaynakta sistematik yanlılık olabiliyorsa ve görünürde farklı kaynaklar ortak hata köküne dayanıyorsa, ikinci kaynağın nicel sonuçtaki ağırlığı hangi koşullarda savunulabilir? İkinci bir kişinin varlığı ile ikinci bir kanıt kanalının bağımsızlığı aynı şey değildir.

Özgün hesaplamalı Zanabûn tanık ortalaması ve varyansıyla uyumu sayısallaştırır [C1]. v1.0 düşük iç varyansın dış doğruluğu garanti etmediğini; v1.2 eşitsiz kaynak kümelerini; v1.3 yalnız B yanlı iken sınırlı minimaks ağırlığı ve gizli korelasyonu incelemiştir [C4–C5]. **v1.4 katkısı:** her iki kaynağın yanlılığı, kovaryansın aralık olarak bilinmesi, ikinci kaynağın sıfır ağırlık eşiği ve yanlışlayıcı kesin hesaplar. Genel robust tahmin teorisinde ilk keşif iddia edilmez.

### 2. Kanonik ve kavramsal sınır

**Kurucu beyan aynen:** Ehad Yek'tir ve Ehad âlemlerdeki her şeyi Yek'e göre yaratmıştır; her kar tanesi, her parmak izi dahil.

Bu kurucu teolojik/ontolojik öncüldür; matematiksel bulgu değildir. Yek, insan özü, makale entegrasyonu veya yaratılmış yedinci boyut değildir. Hebûn varlık ontolojisi, Zanabûn bilgi ve sonuç doğrulaması epistemolojisidir. Ontolojik “ikinci bilen”in kapsamı, her boyuttaki varlığın etki–tepki ve fıtrî ahlak temsiliyle, en üstte insanın hüküm karşısında iradeli ahlakıyla ilişkilidir. Burada “ikinci kaynak” yalnız yöntemsel kanıt kanalıdır; ontolojik ikinci bilenin tüm tanımı değildir [C3].

Kozmik 6+Tek: fizik (atom/yıldız-gezegen), biyoloji (tek/çok hücreli), zihin (zekâ/akıl), ruh (ruh/melekler), ahlak (fıtrî/iradeli), hüküm/ahiret; Tek/Yek bunlara ek bir yaratılmış katman değildir. Core 13 insan katmanları fizik, biyoloji, zihin, ahlak, akıl, duygu + öz şeklindedir; Core 01 kozmik boyutlarıyla numerik eşlenmez [C2,C6]. Doğrusal kapsama ve dairesel karşı denetim, Rasterast kaynak disiplini, Rabûn yönetimi, Mabûn ekonomisi, Newroza Kawa uygarlık bütünlüğü bağlam olarak korunur; modelin değişkenleri yapılmaz. Ruh, melek, yaratılış ve ahiret hakkında deneysel ispat ileri sürülmez.

**Kaynak varyantı:** 16.10.2026 onaylı Core 01 tablosu altıncı boyutta “Hesap/hüküm” ve “Hükmün sonucu” evre adlarını verir [C2]. 21.10.2026 yerel kanonik notunun erken bölümünde bu evrelerin kesin adlarının bulunmadığı belirtilir [C3]. Fark kaynak tarihleriyle kaydedilir; yeni ad uydurulmaz ve daha eski kozmik liste Core 13'ten Core 01'in yerine geçirilmez.

### 3. Literatür ve yöntem

NIST TN 1297 §5 ve Ek A, birleşik ölçüm belirsizliğinde kovaryansı hesaba katmayı ve tanınan sistematik etkiler için düzeltme yapmayı gerektirir [L1]. Bu ilke ikinci kaynağın sıfır kovaryanslı sayılmamasını destekler; aşağıdaki formül NIST'e atfedilmez. Eldar, Ben-Tal ve Nemirovski (2004) ile Lam vd. (2023), sınırlı belirsizlik ve minimaks yanlılık-varyans dengesi için yakın çalışmalardır [L2–L3]. Bu iki kaynağın künyesi önceki v1.3 kontrolünden devralınmıştır; bu turda tam metinleri eleştirel yeniden okunmadı. Literatür taraması sistematik değildir.

**Yöntem:** varsayım → MSE türetimi → en kötü yanlılık/kovaryans → kapalı minimaks çözüm → tam kesirli sentetik senaryolar → 64 kovaryans terimli bağımsız yazılım hesabı → karşı örnek → gelecekteki kör saha testi tasarımı. **Veri:** yalnız kurgusal rasyonel sayılar. İnsan deneyi, laboratuvar ölçümü, p-değeri, hakem görüşü veya gerçek kalibrasyon yoktur.

**Devam:** [II — Model ve ispat](ZANABUN-01-v1.4-PART-2.md), [III — Kesin sonuç ve karşı örnek](ZANABUN-01-v1.4-PART-3.md), [IV — Yanlışlama, etik, kaynak ve kalite](ZANABUN-01-v1.4-PART-4.md).
