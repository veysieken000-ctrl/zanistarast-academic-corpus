# Rasterast matematiksel işlev ayrımı: ilk kaynak sınaması

23 Ekim 2026. İncelenen metinler: H03 Rasterast tam çekirdeği; eski matematiksel modeller karşılaştırma notu; ikinci bilen düzey ayrımı notu. Bu bir tüm depo taraması değildir.

## Gözlem
H03 özeti Rasterast'ı açıkça bir denetim yöntemi olarak tanımlar; yalnız tek bir filtre fonksiyonu olarak tanımlamaz. H03 kaynak türleri, ortak hata, geri besleme ve düzeltilebilir karar kayıtlarıyla ilgilenir. Eski matematik modelleri notunda Rasterast, sembol tanımı, hesaplanabilirlik, tekrar üretilebilirlik ve modelin ampirik iddiası gibi ayrı denetim sorularına uygulanır. Bu nedenle bütün Rasterast kullanımlarını tek bir evet/hayır filtresine indirgemek metinlerle uyumlu değildir.

## Geçici matematiksel türler
| İşlev | Girdi | Çıktı | Kapsam |
|---|---|---|---|
| Karar filtresi | İddia, kanıt, ölçüt | Geçti/kaldı/belirsiz | Yerel değerlendirme |
| Kanıt soyağacı denetimi | İddialar ve kaynak bağı grafı | Bağımlılık, eksik kanıt, ortak hata kaydı | İddia ağı |
| Zamana yayılan denetim | İddia sürümleri, yeni kanıt | Revizyon geçmişi ve açık sorunlar | Birikimli süreç |
| Matematik model kontrolü | Semboller, tanım kümesi, varsayım, çıktı | Tanımlılık, hesaplanabilirlik, karşı örnek | Biçimsel model |
| Zanistarast genel yaklaşımı | Hebûn, Zanabûn, Rasterast ve ilgili boyut/katman/ahlak soruları | Çok düzeyli açıklama ve araştırma programı | Bütün kuramsal çerçeve |

Bunlar önerilen işlev sınıflarıdır, yeni kanonik adlar değildir. Bir formülde Rasterast adının geçmesi, formülün doğruluğunu veya denetimin başarısını kanıtlamaz.

## Sıradaki inceleme
ZANISTARAST-TEORILER içindeki boyutsal açılım matematiksel ilkesi ve zanistarast-papers içindeki Mira formal_foundation.rs dosyası tam metin olarak okunacak. Her denklemde sembol, boyut/katman düzeyi, değişken türü, işlem, çıktı, varsayım ve test kaydı çıkarılacak. Yeni kavram adı ancak farklı matematiksel işlev gösterilirse Müdebbir'e önerilecek.

Belirsiz kullanımlar otomatik değiştirilmez, makaleler birleştirilmez. 412 makale hedefi ve yayın kilidi korunur.
