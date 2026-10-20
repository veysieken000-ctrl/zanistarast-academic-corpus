# Akademik üretim panosu

**20 Ekim 2026 başlangıç kaydı.** Sayılar tahmin/iddia değil, kayıt türlerine göre ayrılır.

| Ölçü | Kanıtlanmış durum |
|---|---|
| Tarihsel ilk envanter | 2.062 dosya / 412 aday kaynak / 407 farklı Git blob (16 Ekim 2026) |
| Güncel tam metin taranan kaynak | Henüz doğrulanmadı |
| Akademik olarak ayrıştırılmış benzersiz makale | Henüz doğrulanmadı |
| Yayıma hazır makale | Henüz doğrulanmadı |
| Bu depodaki çekirdek geliştirme dosyası | ZANABUN-01 araştırma dosyası (yayıma hazır değil) |
| Bu depodaki kaynak indeksi | Başlangıç indeksi |
| Bu depodaki akademik mimari | Bu dalda kurulum |

## Günlük kayıt şablonu

`Tarih | Makale ID | Yapılan gerçek metin/deney çalışması | Kaynak SHA | Yeni commit SHA | K0–K6 durumu | Eksik | Sonraki iş`

**Sayım ilkesi:** Bir dosya veya revizyon otomatik yeni makale değildir. Yalnız doğrulanmış gerçek metin, yöntem, literatür ve test gelişmeleri ilerleme sayılır. 20.00 yalnız çözülemeyen kritik sorular; 21.00 tek günlük Türkçe rapor.

## 21 Ekim 2026 — ZANABUN-01 doğrulanmış üretim

Tam araştırma metni: `02-cekirdek-makaleler/ZANABUN-01-BAGIMSIZ-DOGRULAMA-ORTAK-HATA-VE-KAYNAK-SOYAGACI-TAM-MAKALE.md`, commit `8199e50632c760a7df2de33498d165d3d6e6c63a` (geri okundu).

Yeniden üretilebilir sentetik deney: `07-deneyler-ve-karsi-ornekler/zanabun01_provenance_clusters.py`, commit `a8028189de8717a8a45d524459d443ee8ec0e55a` (geri okundu). Yerel Python çalıştırması: 5 koşul x 20.000 tekrar, PASS. Bunlar gerçek insan verileri değildir.

Kaynak: özgün Zanabûn `ee68095b8d87ba8a580492cfd4c98b86e0a0f21a`, Core 03 `6895cf5e3c1ff5bc23d6c57767e9b180c5022d2b`, ikinci-bilen notu `330db69e2146656281ebc32aa33439666ec54ce4`. Harici literatür ve Episteme yönergesi 21.10.2026 kontrol edildi.

K0 geçti; K1 kısmi; K2 model içi geçti; K3 sentetik geçti; K4 kısmi; K5 kısmi; K6 açık. Önceki ZANABUN-01'in yeni sürümüdür, ayrı benzersiz makale değildir. Hakemli/yayıma hazır diye sayılmaz. Sonraki iş: bağımsız uygulama, gerçek veri ve HEBUN-ZANABUN-02.
