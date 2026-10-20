# ZANABUN-01 — Kaynak, dergi standardı ve kalite denetimi

**Makale kimliği:** ZANABUN-01 v0.2 (20.10.2026). **Okuma sırası:** [I. Giriş](ZANABUN-01-MAKALE-1-GIRIS.md) → [II. Model](ZANABUN-01-MAKALE-2-MODEL.md) → [III. Sonuçlar](ZANABUN-01-MAKALE-3-SONUCLAR.md). Bunlar **tek bir makalenin üç bölümü**dür; üç farklı makale değildir. [Tekrar üretilebilir kod](../07-deneyler-ve-karsi-ornekler/zanabun_hierarchical_witnesses.py) ve [ilk deney protokolü](../07-deneyler-ve-karsi-ornekler/ZANABUN-01-HIYERARSIK-HATA-PROTOKOLU.md) aynı aileye aittir.

## Doğrudan okunan özgün kaynaklar

- `veysieken000-ctrl/zanistarast-ontology` / `papers/zanabun.md`, Git blob `ee68095b8d87ba8a580492cfd4c98b86e0a0f21a`. Ortalama/varyans işlemselleştirmesi ve epistemolojik öneriler.
- `veysieken000-ctrl/zanistarast-ai-native-model` / `core-03.html`, blob `6895cf5e3c1ff5bc23d6c57767e9b180c5022d2b`. Bilginin başka öznelerce tekrar doğrulanması, duygu/akıl bağlamı.
- Aynı repo, `research/yek-6tek-makale-programi-2026-10-16` dalı / `research/yek-6tek-program/KANONIK-ZANABUN-IKINCI-BILEN-DOGRULAMA-DAIMILIK-2026-10-18.md`, blob `330db69e2146656281ebc32aa33439666ec54ce4`. İkinci bilenin **sonucu** yeniden araştırması.
- Önceki aynı makale ailesi: `research/yek-6tek-program/manuscripts/ZANABUN-01-bagimsiz-taniklik-ve-ortak-hata.md`, blob `dea450a481b14f2668480513156a96e965d676f3`. Kaynak depoda bırakıldı, değiştirilmedi.

## Denetlenmiş dış kaynaklar

1. National Academies of Sciences, Engineering, and Medicine. (2019). *Reproducibility and Replicability in Science*. National Academies Press. https://doi.org/10.17226/25303
2. National Institute of Standards and Technology. *Technical Note 1297: 5. Combined Standard Uncertainty*. https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty
3. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press. https://doi.org/10.1017/CBO9780511803161

Bu seçki tam sistematik literatür taraması değildir. Özellikle sosyal epistemoloji, tanıklık bağımsızlığı, küme örneklemesi ve uzman yargılarının birleştirilmesi literatüründe yakınlık ve yenilik incelemesi genişletilmelidir.

## Hedef dergi kalite kıstası

**Olası dergi:** *Synthese*, epistemoloji / bilim felsefesi. **Resmî yönerge incelenme tarihi:** 20 Ekim 2026. https://link.springer.com/journal/11229/submission-guidelines

Kontrol edilen sayfa: çift anonim hakemlik, 150–250 kelimelik özet, 4–6 anahtar kelime, yazar-yıl atıf sistemi, kaynak dosyalarının korunması, bilimsel etik ve çıkar beyanları, üretken yapay zekâ kullanımının açıklanması. Dergi, tipik makale boyunu yaklaşık 15–30 basılı sayfa olarak belirtir; burada henüz bu olgunluk yoktur. **Yalnızca kalite referansı; gönderim, hesap, DOI, ücret veya yayın işlemi yoktur.** Yapay zekâ modeline yazarlık atfedilmez.

## Kalite kapıları K0–K6

- **K0 Kaynak:** Geçti. Dört özgün kaynağın yol ve blob SHA'sı kayıtlı.
- **K1 Kanoniklik:** Kısmi. Kurucu tanım ve Ehad–Yek aynen korundu; uyumun hakikat sayılmasıyla ilgili yorum farkı daha geniş kaynak taramasında izlenecek.
- **K2 Literatür:** Kısmi. Üç gerçek dış kaynak kontrol edildi; tam yenilik incelemesi eksik.
- **K3 Formalizasyon:** Geçti (model içi). Ortak hata, hiyerarşi, kimliklenemezlik, maliyet ve karşı örnek mevcut.
- **K4 Yeniden üretim:** Kısmi. Kod GitHub'a işlendi; sabit tohumlu yerel çalıştırma sayıları kontrol edildi. Ayrı ikinci uygulama ve çevre kaydı eksik.
- **K5 Etik:** Kısmi. Sentetik veri ve AI açıklaması var; insan yazarın fon/çıkar beyanı doğrulanmadı.
- **K6 Dergi düzeyi:** Açık. Kapsamlı literatür, çift anonim bütünleşik metin, uzunluk ve bağımsız uzman eleştirisi gerekiyor.

## Revizyon günlüğü

**v0.1:** Tek ortak hata, deterministik karşı örnek, sentetik deney eki (eski araştırma dalında). **v0.2, 20.10.2026:** Kaynaklar yeniden okundu; bağımsız kaynak grubu modeli, kimliklenebilirlik ispatı, maliyet duyarlılığı, 10.000 tekrarlı deney, resmi *Synthese* yönergesi ve K0–K6 denetimi eklendi. Bu içerikler önceki çalışmanın yeni sürümüdür.
