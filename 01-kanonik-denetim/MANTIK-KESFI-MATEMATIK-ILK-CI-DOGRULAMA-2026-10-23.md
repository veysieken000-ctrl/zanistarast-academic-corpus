# Mantık keşfi matematik rampası — ilk CI doğrulaması

Tarih: 23 Ekim 2026. Kaynak: GitHub Actions çalışma [39945864117](https://github.com/veysieken000-ctrl/zanistarast-academic-corpus/actions/runs/39945864117), commit `bdc59deface0a3d5f21250c44487d73dbc504b5a`.

## Doğrulanan

- GitHub Actions iş sonucu: **success**.
- R1–R5 regresyon testleri: **18/18 başarılı**.
- Mantık keşfi `test_mantik_kesfi_model.py`: **20/20 başarılı**.
- Markdown taraması: **223 dosya, 28 REVIEW_ONLY uyarı**.
- Uyarı artifact'i yüklendi; bu kayıt, içeriklerinin tek tek insan tarafından denetlendiğini iddia etmez.

## Modellerin sınırı

`mantik_kesfi_model.py` şunları **sözdizimsel ve türsel** olarak kontrol eder: yaratılmış Yek kimliği, türeme/üyelik/onay ayrımı, aynı kaynağa bağlı iki onayın kaynak kökü sayısı, yeterlilik iddiasına karşı örnek, merkez rollerinin çokluğu ve dört Yek kimliğinin çiftler hâlinde ayrılığı.

Testlerin başarılı olması Ehad/Yek ontolojisini, Komel'in fiziksel gerçekliğini, jeolojik geçişleri, merkez yasasını veya insan tarihi açıklamalarını **kanıtlamaz**. Kaynak soyağacının farklı olması da tek başına istatistiksel veya epistemik bağımsızlığı kanıtlamaz.

## Sıradaki iyileştirme ve dikkat

- `independent_validations` adı ileride `distinct_provenance_roots` olarak düzeltilmeli: hesaplanan şey bağımsızlık değil kaynak-kök sayısıdır.
- `DERIVES_FROM` yönü açıkça `child → parent` olarak belgelenmeli; döngü ve çoklu ebeveyn politikası ayrıca sınanmalı.
- `sufficient_condition_refuted` yalnız `P ∧ ¬O` karşı örneğini arar; gözlem hatası, nedensellik ve temsil sorunlarını çözmez.
- 28 uyarının dokümantasyon ve makale rolleri ayrı raporlanmalı; otomatik temizleme yapılmamalı.
- Mantık keşfi kayıtları MK-005–MK-012 için tam kaynak ve gerçek karşı örneklerle büyütülmeli.

Yayın kilidi, 412 benzersiz makale, K0–K6, bağımsız Rasterast ve kurucu onayı koşulları değişmez.
