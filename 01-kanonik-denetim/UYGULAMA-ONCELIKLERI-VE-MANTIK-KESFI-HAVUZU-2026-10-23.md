# Uygulama öncelikleri ve yeni mantık keşfi havuzu

**Tarih:** 2026-10-23 · **Durum:** araştırma uygulaması; hızlanma rampalarına toplu aktarım henüz yapılmayacak.

## Seçim yöntemi
Öncelik: (i) kanonik hata yayılma etkisi, (ii) karşı-örnekle sınanabilirlik, (iii) kaynak ve sürüm izlenebilirliği, (iv) birden çok makaleye yeniden kullanım. Sayısal hız/kalite kazanımı ölçülmedi; öncelik sırası kuramsal çalışma planıdır.

| Öncelik | Uygulama alanı / makale | Bağlantılar | İlk somut uygulama | Çıktı |
|---|---|---|---|---|
| P0 | H02 Zanabûn + H03 Rasterast | T08–T10, T13 | Ortak veri kaynağına dayanan iki onayın bağımsızlık karşı-örneği; ontolojik ikinci Yek ayrımı | İddia–kanıt–bağımlılık kayıtları |
| P0 | H01 Hebûn + Varlık Tarihi | T10–T12 | Ehad/Tek/Yek→Komel türemesini fiziksel oluşumla karıştırmayan türlenmiş öncül tablosu | Kanonik köprü sınırları |
| P1 | Jeoloji + Varlık Tarihi | T01, T12 | Hazırlık–mekanizma–sonuç; yeterlilik/karşı-örnek testi | Denenebilir önerme şablonu |
| P1 | H05 Akıl/Bilgi/Güç + İnsan Tarihi | T03, T13–T14 | Öğrenme–çıkarım–gerekçelendirme ayrımı | Bilişsel iddia sınırları |
| P1 | H04 Fıtrî İmkân + İnsan Tarihi | T02, T04, T15 | Araç ve güç artışı ≠ ahlaki ilerleme | Normatif karşı-örnek matrisi |
| P2 | Ruh/melekler, kod/kanun analojileri (H05 ve kaynak arşivi) | T05 | Yazılım, fizik kanunu, düzen ve ruh için tür kontrolü | ANALOGY_ONLY etiketli keşif |
| P2 | Matematiksel soyutlama | tüm bağlantılar | Türlenmiş yönlü grafik, bağımlı kanıt kaynakları, karşı-örnek kapsaması | Yeni test adayı |

## Pilot uygulama: H02 → H03, T09

**Önerme P:** “İki değerlendiricinin P iddiasını onaylaması, P için iki bağımsız kanıt bulunduğunu gösterir.”

**Karşı-model:** S₁ ve S₂ aynı hatalı ölçüm cihazından üretilen tek veri kaynağı D'yi kullanır. Her ikisi de P'yi onaylar. İki onay olmasına rağmen kanıt zinciri tek ortak D'ye bağlıdır. Dolayısıyla onay sayısı kanıt bağımsızlığının kanıtı değildir.

**Yeni keşif adayı MK-016 — Kanıt soyunun tekilleştirilmesi.** Değerlendirici sayısı `n` ile bağımsız kaynak sayısı `k` farklı değişkenlerdir. Kaynak bağımlılık grafiğinde iki onay aynı D düğümüne bağlanıyorsa bağımsızlık varsayımı reddedilmeli veya belirsiz bırakılmalıdır. `k ≤ n` genel yasa olarak değil, bu özel örnekte `n=2, k=1` şeklinde kullanılır; bir değerlendirici birden fazla bağımsız kaynak da inceleyebilir. **Statü:** mantıksal karşı-örnek, ampirik doğrulama değil.

**Aktarım adayları:** H03 kaynak soyağacı, İnsan Tarihi'nde aynı arşiv belgesinden türeyen iki anlatı, Jeoloji'de aynı veri setini tekrar kullanan iki analiz, H05'te aynı eğitim kümesini paylaşan iki model. Aynı bağımlılık yapısı bulunmadan “aynı hata” iddiası kurulmaz.

**Deneme örneği:** İki makale aynı veri setini ayrı yorumlarsa iki yayın vardır ama bağımsız iki veri kaynağı olmayabilir. İkinci bir bağımsız veri kaynağı, farklı ölçüm veya farklı yöntem elde edilirse bağımsızlık durumu yeniden incelenir.

**Karşı-örnek arama:** Aynı veri kaynağını kullanan iki bağımsız yöntem, bazı yöntemsel hata türlerini ayrı yakalayabilir. Dolayısıyla “ortak veri ⇒ bütün denetim değersiz” sonucu da yanlıştır. Bağımsızlık en az veri, yöntem, değerlendiren ve çıkarım katmanlarında ayrı sorulmalıdır.

## MK-017 — Önkoşul ve yeterlilik ayrımı (Jeoloji/H04)

`A`: uygun ortam, `B`: biyolojik sonuç. `A` ile `B` arasındaki geçişin mekanizması ayrıca gösterilmeden `A ⇒ B` kurulamaz. İnsan araçları için `A`: yeni kapasite, `B`: iyi eylem; benzer mantıksal uyarı geçerli ama fiziksel ve ahlaki mekanizmalar aynı değildir. **Statü:** alanlar arası mantık şeması, deneysel yasa değil.

## MK-018 — İşlev benzerliği ile varlık özdeşliğinin ayrılması

Ruh/düzen/yazılım, fiziksel güç/kurumsal güç ve merkez/otorite eşleştirmelerinde aynı sözcük ya da işlev bulunması, ontolojik özdeşlik çıkarımı için yeterli değildir. Kaynak ve hedefin ayrı tanım, kanıt türü ve karşı-örnek alanları korunur. **Statü:** analoji sınırı, kanonik ontoloji değişikliği değil.

## Havuzdan hızlanma rampasına geçiş kapısı

Bu dosyadaki MK-016–018 **keşif adaylarıdır**. Şimdilik mevcut hızlanma rampası politikaları değiştirilmez. Toplu aktarım için her adayda `kaynak_makale, bölüm, öncül, karşı-model, uygulanmış_hedef, test_sonucu, sınırlama, Rasterast_durumu, kurucu_kararı` kayıtları ve gerçek zaman/hata ölçümleri istenir. Pilot H02–H03 uygulanmadan ve test edilmeden verimlilik artışı ilan edilmez.

**Kanonik sınırlar:** Ontolojik ikinci Yek ≠ epistemolojik ikinci bilen; Hebûn/Zanabûn/Rasterast ayrımı; 6+Tek ve insan katmanları; bağımsız Rasterast, K0–K6 ve 412 makale yayın kilidi sürer.
