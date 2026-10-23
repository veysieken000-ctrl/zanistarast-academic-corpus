# Boyutsal açılım formülü ve Mira Rust biçimsel temel: matematiksel ayrıştırma

23 Ekim 2026. Okunan kaynaklar: ZANISTARAST-TEORILER/theories/01-BOYUTSAL-ACILIM-TEORISI/04_BOYUTSAL_ACILIMIN_MATEMATİKSEL_ILKESI.md (SHA 8a4f4ba2fd52613db8a65da6fbf30d0a8c4bd554); zanistarast-papers/reference-implementation/mira/src/formal_foundation.rs (SHA 43a70458d416547162ac49236d7bdf02ebf64c11).

## Eski formülün gerçek statüsü
Kaynak, K > T durumundan üst boyut zorunluluğunu, K/T >= 1 eşiğinden yeni boyut açılmasını ve B(n+1)=f(K/T) ifadesini ileri sürüyor. K ve T'nin nicel tanımı, ölçü birimi, örneklem alanı, f'nin fonksiyon biçimi, eşik ölçümü, belirsizlik ve alternatif açıklamalar verilmediği için bu çıkarımlar matematiksel teorem veya deneyle doğrulanmış kozmik yasa olarak sunulamaz. K/T ancak T sıfırdan farklı ve K ile T aynı boyutlu niceliklerse boyutsuz oran olabilir. T=0 durumu tanımsızdır. K/T >=1 eşitsizliği tek başına yeni bir varlık düzeyinin oluştuğunu mantıksal olarak gerektirmez; bu sonuç ayrıca bir geçiş aksiyomu ve bağımsız kanıt gerektirir.

## Boyut ve katman ayrımı
Müdebbir'in kurucu ayrımı: boyutlar kâinatı, katmanlar varlıkları anlatır. B(n) ifadesinin kâinatın boyut indeksi mi, belirli bir varlığın katman seviyesi mi, yoksa genel karmaşıklık durumu mu olduğu açıkça belirtilmelidir. Üç farklı araştırma sorusu aynı denklem diye birleştirilemez. Fizikten biyolojiye geçiş örneği bir kozmik boyut savıdır; tek bir varlığın katman değişimi olarak sessizce yorumlanamaz.

## Mira biçimsel kodundaki ayrı işlevler
Okunan Rust dosyasında FormalFoundationKind aksiyom/tanım/yüklem/teorem/lemma/ispat türlerini ayırır. FormalAxiom ve FormalDefinition için kayıt geçerliliği; FormalTheorem için bağımlılık kimlikleri ve proof_id; FormalProof için Draft, AwaitingVerification, Verified, Rejected durumları bulunur. is_valid gibi kontroller boş alanları ve kayıt türünü sınar; mark_verified ise durumu değiştirir. Bu kontroller bilimsel doğruluğun bağımsız matematiksel ispatı değildir. Özellikle mark_verified çağrısının tek başına ispat adımlarını bir teorem ispatlayıcısıyla doğruladığı varsayılmamalıdır. Kodun tamamı için derleme/test sonucu bu incelemede üretilmedi.

## Rasterast ve Zanistarast adlandırma sınırı
Bir eşik modeli Zanistarast'ın kozmik boyut hipotezi olabilir; Rasterast'ın kendisiyle özdeş değildir. Rasterast bu modelin tanımlılığını, varsayımlarını, karşı örneklerini ve kanıt durumunu denetleyen yöntem veya süreç olarak kullanılabilir. Tek bir karar filtresi, sürüm boyunca denetim süreci ve bütün Zanistarast yaklaşımı farklı matematiksel türlerdir. Yeni isim önerileri Müdebbir onayı olmadan kanonikleşmez.

## Sonraki sınamalar
1. K ve T için ölçülebilir operasyonel tanım, birim, T=0 ve ölçüm hatası belirle.
2. f'nin tanım/değer kümesi, süreklilik veya eşik davranışı ve geçiş önermesinin varsayımlarını yaz.
3. B(n) için kozmik boyut, varlık katmanı veya durum değişkeni türünü zorunlu alan yap.
4. Alternatif sonuçları sınayan karşı örnek kur: K/T >=1 olduğu halde yeni boyut oluşmayan sistem.
5. Rust testleri, derleme, ispat durumu ve dış bilimsel geçerlemeyi ayrı raporla.
6. Bağımsız Rasterast denetimi ve kurucu onayı olmadan PASS verme.

Eski kaynak korunur, otomatik silme veya yeniden adlandırma yapılmaz. Bu kayıt bir araştırma denetimidir; 412 makale hedefi ve yayın kilidi sürer.
