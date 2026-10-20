# ZANABUN-01 — Makale Bölüm III: Deney, tartışma ve sonuç

**Sürüm ailesi:** ZANABUN-01 v0.2. Önceki iki bölümle aynı makalenin devamıdır; ayrı makale sayılmaz.

## 7. Sentetik deney

Yöntem dosyası: `07-deneyler-ve-karsi-ornekler/zanabun_hierarchical_witnesses.py`. Python standart kitaplığı; sabit tohum `20261020`; koşul başına 10.000 bağımsız sentetik tekrar; toplam rapor sayısı `N=24`; `τ_0=1`, `τ_g=2`, `σ=1`. Her tekrarda küresel hata, grup hataları ve bireysel hatalar bağımsız olarak yeniden örneklenir. Hedef `θ=0` alınır; ölçüt kök ortalama kare hata (RMSE).

| Bağımsız grup G | Grup başına m | Sentetik RMSE | Analitik RMSE |
|---:|---:|---:|---:|
| 1 | 24 | 2.2638 | 2.2454 |
| 2 | 12 | 1.7301 | 1.7440 |
| 4 | 6 | 1.4413 | 1.4289 |
| 8 | 3 | 1.2392 | 1.2416 |
| 24 | 1 | 1.0931 | 1.0992 |

Bu sayılar bağımsız yerel çalıştırmada denetlenmiştir. Monte Carlo ile analitik hesaplar örnekleme hatası sınırları içinde yakın görünmektedir; deneysel kesinlik veya saha doğrulaması değildir. G artınca grup kaynaklı hata azalır. Küresel hata standart sapması 1 olduğundan analitik RMSE 1'in altına inemez. Sonuçlar yalnızca seçilen dağılım, bağımsızlık ve parametre varsayımları için geçerlidir.

## 8. Rakip açıklamalar ve olumsuz sınamalar

**Ortak kaynak soyunun gizlenmesi:** Farklı kişiler aynı veriyi kopyalamış olabilir. Kaynak soyağacı ve grup-arası kovaryans denetlenmeden “bağımsız ikinci bilen” denemez.

**Hedef değerin bilinmemesi:** Dış `θ` referansı yoksa gerçek RMSE ölçülemez. Bu durumda yalnız uyum, duyarlılık analizi ve gerekçeli belirsizlik sunulmalıdır.

**Gerçek olgunun değişmesi:** Tanıklar farklı zaman veya koşullarda farklı gerçek değerler ölçmüş olabilir. Önce zaman, nesne, koşul ve ölçüm protokolü eşleştirilmeli; gerekiyorsa dinamik `θ_t` modeli kullanılmalıdır.

**Bağımsızlığın yetersizliği:** Yöntemler bağımsız olsa da aynı tesadüfi yanlış sonuca varabilir. Yeni koşullarda kör tekrar, ayırt edici müdahale ve bağımsız dış ölçüt gerekir.

**Teolojik düzeyin karıştırılması:** Matematiksel tanık indisi, yaratıcı ilk özne ile insan ikinci öznenin ontolojik ayrımını temsil etmez. Deney, Ehad–Yek veya Hebûn'un metafizik statüsünü test etmez.

**Dar yanlışlama önerisi:** Bağımsız grup etkilerinin varlığı ve model varsayımları gerçek bir ölçüm düzeninde sağlanırsa, aynı N altında daha fazla bağımsız grup kullanımı beklenen grup kaynaklı hata varyansını azaltmalıdır. Gözlenen grup kovaryansları veya dış ölçüt sonuçları bu öngörüyle uyuşmazsa model gözden geçirilir. Kurucu felsefi iddia bu tek deneyin doğrulanması veya yanlışlanmasıyla eşitlenmez.

## 9. Tartışma

İkinci bilenin onayını salt iki kişinin aynı cevabı vermesine indirgemek, kurucu tanımdaki **sonucun yeniden araştırılması** öğesini kaybettirir. Daha güçlü bir değerlendirme şunları birlikte gerektirir: ikinci kişi sonucu kendi yöntemiyle üretebiliyor mu; iki süreç ortak hata taşıyor mu; sonuç başka koşullarda ayırt edici karşı denemelere dayanıyor mu? Bunların hiçbiri tek bir uzlaşma sayısına indirgenemez.

Doğrusal araştırma ilerlemesi tek ortak hata modelinden grup ve bütçe modeline genişlemektir. Dairesel denetim ise sonuçtan başlangıç varsayımlarına geri dönüp ortak hata ve neden özdeşsizliğini aramaktır. Tarihsel arşivler, bilimsel laboratuvarlar ve çoklu yapay zekâ ajanları için benzer sorular doğabilir; bu alanlar ayrı veri, etik ve literatür gerektirdiğinden burada yeni makale sayılmaz.

## 10. Sonuç

Mutabakat ile dış doğruluk farklıdır. Gerçekten bağımsız kaynak grupları grup düzeyindeki ortak hatayı azaltabilir; küresel yanlılık ve nedensel kimliklenemezlik ayrıca denetlenmelidir. Bu, Zanabûn'un ikinci bilen tarafından sonucun doğrulanması ilkesinin sınanabilir bir alt modelidir; ontolojik veya teolojik bir ispat değildir.

## Açıklamalar

**Veri:** Tamamen sentetik; insan/kişisel veri kullanılmadı. **Yazım:** ChatGPT üretken yapay zekâ desteği kullanıldı; insan araştırmacının son doğrulaması gerekir. **Fon ve çıkar çatışması:** İnsan yazar beyanı henüz alınmadı, bilgi uydurulmadı. **Hakemlik:** Yok. **Gönderim:** Yok ve planlanmıyor.
