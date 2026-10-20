# ZANABUN-01 — Bağımsız tanıklık ve ortak hata

**Durum:** Çekirdek makale geliştirme dosyası; hakemli/yayıma hazır değil. **Kategori:** Epistemoloji ve bilim felsefesi.

## Özgün kaynak
[Önceki çekirdek makale taslağı](https://github.com/veysieken000-ctrl/zanistarast-ai-native-model/blob/research/yek-6tek-makale-programi-2026-10-16/research/yek-6tek-program/manuscripts/ZANABUN-01-bagimsiz-taniklik-ve-ortak-hata.md). Tam metnin kaynak sadakati karşılaştırması henüz tamamlanmadı; bu dosya ayrı bir yeni benzersiz makale olarak sayılmaz.

## Araştırma sorusu
“Bilen öznenin bilinen nesneye yönelimi sonucu ortaya çıkan sonucun ikinci bilen tarafından onayı” ilkesinde ikinci bilenin onayı hangi koşullarda güvenilir doğrulama sayılabilir? Ortak hata taşıyan iki veya daha çok tanık neden birbirini doğruluyor görünür?

## Çalışma hipotezi
Bağımsız doğrulama, yalnız tanık sayısına değil ölçüm/gözlem bağımlılığına, ortak hata kaynaklarına ve bağımsız karşı denemelere bağlıdır. Bu hipotez Zanabûn'un metafizik doğruluğunu kanıtlamaz; bir epistemik doğrulama modelinin güvenilirlik koşullarını araştırır.

## Formal karşı örnek
`X_i = θ + B + ε_i`, burada `θ` hedef büyüklük, `B` tüm tanıkların paylaştığı ortak hata, `ε_i` bağımsız ortalaması sıfır olan ölçüm gürültüsüdür. Ortalama `X̄_n = θ + B + (1/n)Σ ε_i`. Bağımsız gürültünün varyansı `σ²/n` azalsa bile sabit `B ≠ 0` için ortalama `θ+B` değerine yaklaşır, `θ` değerine değil. Dolayısıyla tanık sayısının artması ortak yanlılığı tek başına ortadan kaldırmaz.

## Test ve karşı örnek planı
- Senaryo A: `B=0`; n arttıkça örnek ortalamasının hata varyansı küçülür.
- Senaryo B: `B≠0`; n arttıkça hata `B` etrafında kalır.
- Senaryo C: bağımsız farklı kalibrasyon yöntemiyle `B` ölçülür veya azaltılır; karşılaştırma yapılır.
- Karşı örnek: iki görünüşte bağımsız tanığın aynı yanlış veri kaynağına dayanması.

## Literatür ve doğrulama boşluğu
Ölçüm teorisi, korelasyonlu hatalar, bilimsel tekrarlanabilirlik ve sosyal epistemoloji literatürüyle gerçek bibliyografik karşılaştırma henüz yapılmadı. Kaynak uydurulmaz. [Önceki deney eki](https://github.com/veysieken000-ctrl/zanistarast-ai-native-model/blob/research/yek-6tek-makale-programi-2026-10-16/research/yek-6tek-program/manuscripts/ZANABUN-01-ORTAK-HATA-DENEY-EKI-2026-10-20.md) ve [kod](https://github.com/veysieken000-ctrl/zanistarast-ai-native-model/blob/research/yek-6tek-makale-programi-2026-10-16/research/yek-6tek-program/experiments/zanabun_common_error_trial.py) kaynak kontrolüyle içeri alınacaktır.

## Kanıt, etik ve hazırlık
Yukarıdaki cebirsel sonuç matematiksel model içindeki sonuçtur; dış dünyada deney yapıldığı veya ontolojik tez ispatlandığı anlamına gelmez. Veri uydurma yoktur; sentetik simülasyon gerçek veri diye sunulamaz. Hazırlık: **yöntem/karşı örnek mevcut; literatür, kapsamlı kaynak karşılaştırması, bağımsız test ve hedef dergi uygunluğu eksik**.
