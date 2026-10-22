# ZANABUN-01 v1.4 — IV. Yanlışlama, etik, kaynaklar ve kalite

Bu bölüm [I](ZANABUN-01-v1.4-PART-1.md), [II](ZANABUN-01-v1.4-PART-2.md), [III](ZANABUN-01-v1.4-PART-3.md) ile **tek** makaledir.

## 9. Önceden kayıtlanabilir ampirik sınama — yapılmadı

Birden fazla kararlı ve önceden tanımlı hedefte A/B kaynaklarının cihaz, operatör, yazılım, eğitim verisi ve kalibrasyon kökleri belgelenir. Ayrı bir kalibrasyon altkümesinde a,b,v_A,v_B,c_alt,c_üst sınırları gerekçelendirilir ve **kör testten önce dondurulur**. İki kaynakla ortak kökü bulunmayan, belirsizliği ayrıca raporlanan izlenebilir dış referans aranır. Karşılaştırmalar: A-tek, yanlılığı yok sayan ağırlık, v1.3 tek yanlı minimaks, v1.4 çift yanlı/kovaryans minimaks. Birincil ölçüt kör testte kare hata; ikincil ölçütler belirsizlik kapsaması, kalibrasyon istikrarı, maliyet ve başarısız hedef oranıdır. a/b sınırı veya c_üst aşılırsa, θ değişirse ya da dış referans ortak kalibrasyon kullanırsa modelin uygulama garantisi geçersiz sayılır. **Saha testi, insan deneyi, p-değeri ve hakemlik yapılmadı.**

## 10. Dört iddia türü ve etik

**Teolojik:** Ehad/Yek, ruh/melekler, hüküm/ahiret matematikle ispatlanmaz. **Felsefi:** Hebûn'un varlık/ahlak ve ontolojik ikinci bilen açıklaması kavramsal tartışmadır. **Formel:** II. bölümdeki minimaks önermesi belirtilen varsayımlarda ispatlanmıştır. **Ampirik:** Gerçek kaynakların hata ve bağımsızlık sınırları henüz ölçülmemiştir. Bu ayrım “çok onay = mutlak hakikat” sonucunu engeller.

Veri yalnız sentetiktir; insan/hayvan katılımcı ve özel tam metin aktarımı yoktur. OpenAI GPT-6, 22.10.2026'da kaynak okuma, metin, ispat ve Python denetimine yardımcı oldu; AI insan yazar/hakem değildir. Finansman ve çıkar çatışması hakkında doğrulanmış beyan bulunmadığından uydurulmaz.

**Yalnız hedef dergi kalite kıstası:** *Episteme* (Cambridge University Press), resmî yönerge **22.10.2026** kontrol edildi [J1]. 12.000 sözcük sınırı (not/kaynakça dahil), çift aralık, 12 punto Times New Roman, anonim metin ve ayrı anonim özet, üretken AI kullanımının açıklanması gerekir. Bu Türkçe Markdown çalışma İngilizce/anonymize edilmiş son dergi dosyası değildir; kapsamlı literatür ve bağımsız hakem kontrolü eksiktir. **Gönderim yapılmaz.**

## 11. Sonuç

İkinci kanıt kanalının adı farklı olsa da yanlılık ve ortak kalibrasyon nedeniyle en kötü risk altında sayısal ağırlığı sıfır olabilir. Eşit yanlılık sınırlarında ise pozitif ağırlık gerekçelendirilebilir. Bağımsız ikinci bilenin araştırma sorumluluğu, bir ölçüm ortalamasındaki sayısal ağırlığa indirgenmez. Özgün katkı, Zanabûn'un sonuç denetimini kaynak soyağacı, yanlışlanabilir hata bütçesi ve sınırlı bir matematiksel karar kuralıyla eleştirel sınamaktır.

## 12. Kaynakça ve sürüm izi

- [C1] Özgün Zanabûn: veysieken000-ctrl/zanistarast-ontology, papers/zanabun.md, blob **ee68095b8d87ba8a580492cfd4c98b86e0a0f21a** (22.10 doğrudan okundu).
- [C2] Core 01: veysieken000-ctrl/zanistarast-ai-native-model, core-01.html, blob **faa04bb3130b670a4712854defe364d94a08991c**; Core 03: core-03.html, blob **6895cf5e3c1ff5bc23d6c57767e9b180c5022d2b** (22.10 okundu).
- [C3] Yerel ikinci-bilen kanoniği: 01-kanonik-denetim/HEBUN-VARLIK-AHLAK-IKINCI-BILEN-ONTOLOJIK-TANIM-2026-10-21.md, blob **f1fc84a7bc7596fe8c2dcd1edf3beeb46792bfd3**; hiyerarşi blob **7610181fefe589940390b253153db679a129bfcd**.
- [C4] ZANABUN-01 v1.0 tam metin, blob **fe8a084c5c53ec7556aae2c441ef4e641ba99180**.
- [C5] ZANABUN-01 v1.3 dört bölüm, blob'lar **3f23175d13d2306494703a3ac194684e35d28ed3**, **19c2971e141b83173e8e41e6d43594b327e683ee**, **5f7b7f5a174883e180942fd29213ddc188bfa80b**, **14607bb17264d69b86d970ff1f086b80bf364b74**.
- [C6] Core 13: core-13-zanistarast-medeniyet-modeli.html, blob **6a6c822a1910fd5f422eb1a0f2a50201566694ff** (22.10 doğrudan okundu).
- [L1] Taylor & Kuyatt (1994), *NIST TN 1297*, §5 ve Ek A: https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty (resmî 22.10 kontrolü).
- [L2] Eldar, Ben-Tal & Nemirovski (2004), *IEEE TSP* 52(8), 2177–2188, DOI 10.1109/TSP.2004.831144; önceki künye, tam metin bu turda okunmadı.
- [L3] Lam, Zhang & Zhang (2023), *Operations Research* 71(6), 2352–2373, DOI 10.1287/opre.2022.2319; önceki künye, tam metin bu turda okunmadı.
- [J1] *Episteme* resmî https://www.cambridge.org/core/journals/episteme/information/author-instructions/preparing-your-materials (22.10.2026).

**Revizyon:** v1.0 ortak hata → v1.2 eşitsiz kümeler → v1.3 tek yanlı minimaks → **v1.4 iki yanlılık, kovaryans aralığı, sıfır ağırlık eşiği, tam aritmetik çapraz kontrol ve Core 13 doğrudan okuma**. Tek makale ailesidir; 412 aday kaynak 412 benzersiz/yayıma hazır makale değildir.
