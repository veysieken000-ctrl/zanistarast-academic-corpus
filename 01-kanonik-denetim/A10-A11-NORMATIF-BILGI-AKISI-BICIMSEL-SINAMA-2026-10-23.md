# A10–A11: normatif meşruiyet ve bilgi akışının ayrı biçimsel sınaması

23 Ekim 2026. Kaynaklar: A10 (SHA 95e2ff4bb13a48a3366186f1b88e32729bc1f3e3), A11 (SHA 5c1537cdc95397bf1954e4b6711e4cd658e00cb3), araştırma dalı. Bu kayıt matematiksel model önerisidir; teorem ispatı veya ampirik sonuç değildir.

## A10 — normatif gerekçelendirme modeli
Karar kümesi `Q`, yetki kullanan aktörler `A`, etkilenenler `P` olsun. Her `q ∈ Q` için:
- `Y(q)`: açık ve sınırlandırılmış yetki kaydı;
- `G(q)`: erişilebilir gerekçe;
- `H(q)`: hak ve zarar değerlendirmesi;
- `I(q)`: itiraz olanağı;
- `D(q)`: düzeltme ve hesap verme mekanizması.

**Aday gerekli koşul:** `LegitimacyCandidate(q) => Y(q) ∧ G(q) ∧ H(q) ∧ I(q) ∧ D(q)`. Ters yöndeki çıkarım henüz kurulmaz: beş prosedürün varlığı kararı otomatik meşru yapmaz. Rıza, adalet, yetkinin kaynağı ve zararların dağılımı için ek normatif öncüller gerekir. Yek–Komel ontolojisinden doğrudan meşruiyet sonucu çıkarılamaz.

**Karşı örnek:** Beş alanın hepsi kâğıt üzerinde dolu olsa bile gerekçe yanlış veri içeriyorsa veya itiraz fiilen engelleniyorsa meşruiyet iddiası başarısız olabilir. Bu nedenle alanların varlığı ile gerçek işlerliği ayrı ölçülür.

## A11 — bilgi akışı ve bağımsız denetim modeli
Yönlü grafik `G=(V,E)`: düğümler temsil edilenler, temsilciler, karar merkezleri ve denetçilerdir. Kenarlar bilgi iletimi, yetki devri veya itiraz kanalı olarak **türlenir**; bu üç ilişki aynı kenar sayılmaz.

Aday ölçümler:
- `reach(p,q)`: etkilenen `p` kişisinin `q` kararının gerekçesine erişebilmesi (ikili veya dereceli ölçüm);
- `appeal(p,q)`: kişinin itirazını bağımsız incelemeye iletebilmesi;
- `provenance(e)`: delilin kaynak ve değişiklik geçmişinin izlenebilmesi;
- `independent(a,q)`: denetçi `a` için kaynak, çıkar ve yönetim bağımlılığına ilişkin risk değerlendirmesi;
- `latency(q)`: tespit edilen hata ile gerekçeli düzeltme arasındaki süre (zaman birimi tanımlanmalı).

**Sınama sorusu:** Merkezileşme veya dağıtıklık derecesi sabit tutulduğunda, bilgi yolu kopukluğu ve bağımlı denetçi sayısı hata tespitini/düzeltmeyi nasıl etkiler? Bu soru için gözlemsel veya simülasyon verisi gereklidir; burada veri üretilmemiştir.

**Karşı örnek:** Bir ağda tüm düğümler merkeze bağlı olsa bile merkez yalnız olumlu raporları geçiriyorsa yüksek bağlantılılık bilgi kalitesini garanti etmez. Çok sayıda denetçi aynı kaynağı kullanıyorsa sayıca çoğalma bağımsız doğrulama sayılmaz.

## A10 ile A11'in tür farkı
A10'un çıktısı **normatif gerekçe koşulları**; A11'in çıktısı **graf üzerindeki erişim, bağımlılık ve düzeltme ölçümleri**. `LegitimacyCandidate` ile `reach` veya `latency` eşdeğer değildir. İyi işleyen iletişim ağı meşruiyet için yeterli değildir; meşru ilke de tek başına iyi bilgi akışı sağlamaz. Ortak Rasterast denetimi bu iki araştırmayı birleştirme nedeni değildir.

## Rasterast denetim soruları
1. Her değişkenin evreni, birimi, veri kaynağı ve belirsizliği tanımlı mı?
2. A10'un gereklilik iddiası karşıt normatif kuramlarla sınandı mı?
3. A11'in graf kenarları ve ölçümleri gözlemlenebilir mi?
4. İtiraz mekanizmasının varlığı ile fiilî erişilebilirliği ayrıldı mı?
5. Denetçi ve delil kaynaklarının ortak hata ilişkisi gösterildi mi?
6. Simülasyon, kavramsal uygunluk ve gerçek dünya doğrulaması ayrı raporlandı mı?

## Üretim ve kalite kararı
A10 ve A11 ayrı BAGIMSIZ-EKSIK adayları olarak kalır. Bu şema onların özgün araştırma katkısını ayrıştırır, fakat henüz geçerlenmiş ölçüm veya kanıt sunmaz. K0–K6 açık, Müdebbir onayı ve 412 makalenin kanonik bütünlüğü olmadan yayın yok.
