# ZANABUN-01 — 21 Ekim 2026 doğrulanmış ilerleme ve kalite kaydı

**Sürüm ailesi:** ZANABUN-01 v1.0. **Yeni benzersiz makale sayısı:** 0; önceki taslağın kapsamlı geliştirilmiş tam araştırma metni. **Durum:** İç denetim; dergiye hazır değil.

## Okuma sırası ve gerçek üretim

1. '02-cekirdek-makaleler/ZANABUN-01-BAGIMSIZ-DOGRULAMA-ORTAK-HATA-TAM-MAKALE.md': Başlık, Türkçe/İngilizce özet, 1–6. bölümler, matematiksel model, yöntem ve çalıştırılmış sentetik sonuçlar.
2. '02-cekirdek-makaleler/ZANABUN-01-MAKALE-DEVAM-07-10.md': 7–10. bölümler; hipotezler, itirazlar, etik ve sonuç.
3. '02-cekirdek-makaleler/ZANABUN-01-KAYNAKCA-VE-MATEMATIK-EKI.md': Gerçek kaynakça, özgün kaynak blob SHA'ları, ikinci matematik kontrolü.
4. '07-deneyler-ve-karsi-ornekler/zanabun01_clustered_witness_trial.py': 30.000 tekrar/koşul, sabit tohum 20261021, yalnız standart Python modülleri.

Bu dosyalar **tek makale ve yöntem ekidir**; ayrı makaleler olarak sayılmaz. Metnin tek dosyada birleştirilmesi sonraki biçimleme adımıdır.

## Gerçek çalıştırma kanıtı

21 Ekim 2026'da 'python3 zanabun01_clustered_witness_trial.py' komutu yerel Python 3 ortamında çalıştırıldı. Deterministik cebirsel testler ve simülasyon toleransları geçti.

| Koşul | Simülasyon RMSE | Analitik RMSE |
|---|---:|---:|
| G=1, n=8 | 2.0916 | 2.0917 |
| G=2, n=8 | 1.5406 | 1.5411 |
| G=4, n=8 | 1.1718 | 1.1726 |
| G=8, n=8 | 0.9401 | 0.9354 |
| G=4, n=8, sabit b=1 | 1.5312 | 1.5411 |
| Ortak hata yok, n=8 | 0.3525 | 0.3536 |

**Önemli:** Bunlar sentetik hesap çıktısıdır; saha verisi, insan deneyi, teolojik ispat veya bağımsız hakem incelemesi değildir.

## Hedef dergi kıstası — resmî yönerge denetimi

**Dergi:** *Philosophy of Science* (Cambridge University Press). **Yönerge kontrol tarihi:** 21.10.2026.

- https://www.cambridge.org/core/journals/philosophy-of-science/information/author-instructions
- https://www.cambridge.org/core/journals/philosophy-of-science/information/author-instructions/preparing-your-materials
- https://www.cambridge.org/core/journals/philosophy-of-science/information/journal-policies/publishing-ethics

Resmî yönergeye göre araştırma makalesi sınırı 9.000 sözcük; ilk değerlendirme için yaklaşık 100 sözcüklük özet, anonim incelemeye uygun metin; nihai biçimde yazar-tarih/Chicago atıfları, uygun DOI ve etik/AI beyanları beklenir. **Bu çalışma Türkçedir; İngilizce tam metin ve son biçim kontrolü yapılmadığı için tam uyum iddia edilmez.** Bu dergi yalnız kalite ölçütüdür; gönderim yapılmayacaktır.

## K0–K6

| Kapı | Durum | Kanıt / açık iş |
|---|---|---|
| K0 Kaynak | Kısmen geçti | Özgün Zanabûn ve 18 Ekim kurucu açıklaması doğrudan okundu, blob SHA kaydedildi. Core 03 tam karşılaştırması açık. |
| K1 Ayrışma | Geçti | Önceki ZANABUN-01 sürümü geliştirildi; yeni benzersiz makale sayılmadı. |
| K2 Metin | Geçti — araştırma metni | Özet, giriş, yöntem, sentetik bulgu, itiraz, sonuç; üç bağlı dosya. Tek dosya biçimlemesi açık. |
| K3 Literatür | Kısmen | NIST, PNAS ve dergi resmî sayfaları doğrulandı; sistematik tarama ve yakın felsefi görüşlerle kapsamlı karşılaştırma açık. |
| K4 Denetim | Kısmen | Matematik, karşı örnek, çalıştırılmış kod mevcut; gerçek veri ve bağımsız insan denetimi yok. |
| K5 Etik | Kısmen | Sentetik veri, AI katkısı ve gönderim yasağı açık; insan sorumluluk/telif denetimi açık. |
| K6 Dergi biçimi | Kısmen | Yönerge tarihi ve kuralları kaydedildi; İngilizce uyarlama ve son biçim kontrolü açık. |

**Revizyon günlüğü:** v1.0 — özgün kaynaktaki iki tanıklık sunumu ayrıştırıldı; önceki tek düzeyli ortak hata modeli hiyerarşik kalibrasyon-kümesi modeline genişletildi; çalışan yeni deney, üç literatür karşılaştırması, ikinci-bilen protokolü ve altı güçlü itiraz eklendi.

**Koruma:** Yalnız Academic Corpus'un 'research/chatgpt-academic-2026-10-20' dalına yazıldı. Eski kaynaklar, main, canlı site ve Mira'nın çalışma alanları değiştirilmedi.
