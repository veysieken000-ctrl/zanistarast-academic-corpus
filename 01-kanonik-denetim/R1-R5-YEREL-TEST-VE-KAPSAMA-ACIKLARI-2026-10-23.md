# R1–R5 tarayıcısı: ilk yerel test ve kapsama açıkları

23 Ekim 2026. Python 3 `unittest` ile, GitHub'da kayıtlı tarayıcının aynı `PATTERNS` ve `scan` mantığını yerel geçici dizine aktararak 8 sentetik regresyon testi çalıştırıldı: **8 geçti, 0 başarısız**. Bu bir **yerel eşdeğer mantık sınaması**dır; GitHub Actions/CI çalıştırması veya depodaki tam kodun doğrudan checkout edilerek çalıştırılması değildir.

## Pozitif sonuçlar
R1 eski D4/zaman ifadesi; R2 geometrik merkez/ilk Yek; R3 prosedür/meşruiyet; R4 reach/doğruluk; R5 Rasterast/ikili filtre; olumsuzlama bağlamı; ilgisiz cümle; satır numarası testleri geçti.

## İlave negatif keşif testleri
| Örnek | Beklenen uzman incelemesi | Mevcut eşleştirme |
|---|---|---|
| `Merkezde olmak ontolojik kökeni kanıtlamaz` | Merkez–ontoloji ilişkisini bağlamıyla incele | Uyarı yok |
| `prosedür meşruiyeti garantiler` | Prosedürden meşruiyete sıçrama | Uyarı yok |
| `Rasterast yalnızca filtredir` | Rasterast'ın indirgenmesi | Uyarı yok |
| `iki onay bağımsız kanıt sayılmaz` | Olumsuzlama nedeniyle yanlış alarmı ayır | R4, REVIEW_ONLY; olumsuzlama işareti var |

İlk üç örnek **kapsama açığı** gösterir. Sonuncusu bilinçli inceleme-uyarısıdır; doğrulanmış kanonik ihlal değildir. Sekiz regresyon testinin geçmesi yüksek duyarlılık/özgüllük ispatı değildir.

## Düzeltme gereksinimleri
1. Türkçe çekim ekleri (`meşruiyeti`), kısa ve uzun ifade varyantları, `yalnızca filtredir` gibi yüklem türleri için yeni örüntüler.
2. Negatif/alıntı/karşı örnek cümleleri için salt aynı satırdaki anahtar sözcük yerine bağlamsal sınıflandırma.
3. Her R1–R5 kuralı için pozitif, negatif, alıntı ve sınır testleri; gerçek makalelerden elle etiketlenmiş altın küme.
4. Tam depo checkout ve CI testleri, sonra hassasiyet/duyarlılık ölçümü. Mevcut turda bunlar yapılmadı.
5. Uyarılar otomatik silme, değiştirme, birleştirme veya yayın kararı vermez.

412 özgün makale hedefi ve K0–K6/yayın kilidi korunur.
