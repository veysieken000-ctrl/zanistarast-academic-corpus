## 4. Karşı örnekler, tanımlanabilirlik ve etkin örnek büyüklüğü

**Önerme A — Tam mutabakat doğruluğu garanti etmez.** θ=0 ve W₁=W₂=W₃=W₄=5 olsun. K=5, V=0, dış hata |K−θ|=5 olur. Dört gözlemci arasındaki farkın sıfır olması, hepsinin ortak yanlılığını ortadan kaldırmaz. İspat, ortalama ve varyans tanımlarına doğrudan yerine koymadır.

**Önerme B — Ayrışma yanlış grup ortalamasını gerektirmez.** θ=0, W₁=−10 ve W₂=10 olsun. K=0, V=100'dür. İki tekil raporun doğru olduğu iddia edilmez; yalnızca yüksek iç varyansın ortalamanın dış ölçüte uygunluğunu mantıken dışlamadığı gösterilir. Bu nedenle özgün dosyadaki “yüksek varyans = yanlış bilgi” yorumu evrensel doğruluk koşulu olamaz.

**Önerme C — Ortak hatanın kalıcılığı.** Denklem (1)'de τ²>0 iken n sonsuza giderse Var(K−θ) değeri τ²'ye yaklaşır. Ortak sabit b varsa K, θ+b çevresine yaklaşır. Çok sayıda tekrar, bağımsız ikinci kanıt zincirinin yerini tutmaz.

**Önerme D — Tek kaynakta tanımlanabilirlik.** B sabit b ve bilinmeyense Wᵢ=θ+b+εᵢ gözlemleri yalnız θ+b toplamını belirler. Her c için (θ+c,b−c) aynı gözlem dağılımını üretir. Dış referans veya ek kısıt yokken θ ile b ayrı tanımlanamaz. Ancak B'nin dağılımı hakkında doğrulanabilir bilgi veya bağımsız gruplardan yeni veri varsa bu sınır değişebilir.

Aynı varyanslı v gözlemlerin ikili korelasyonu ρ≥0 ise Var(K)=v[1+(n−1)ρ]/n. Yalnız bu eş-korelasyon modelinde n_eff=n/[1+(n−1)ρ], ortalamanın varyansı açısından etkin bağımsız gözlem sayısıdır. ρ=1 için n_eff=1; ρ=0 için n_eff=n olur. Bu sayı genel epistemik “hakikat puanı” değildir.

## 5. Bağımsız yöntemlerin biçimsel modeli

Toplam N=mn tanık m yöntem grubuna, her gruba n kişi düşecek biçimde dağılsın. W(g,j)=θ+G+B(g)+ε(g,j) yazılsın. G bütün yöntemlerin, B(g) yalnız g yönteminin paylaştığı hata; ε(g,j) bireysel hata olsun. Bileşenler sıfır ortalamalı ve bağımsız, varyansları sırasıyla γ², τ², σ² ise:

**MSE(K)=γ²+τ²/m+σ²/(mn).** (2)

İspat: K−θ=G+ΣB(g)/m+Σε(g,j)/(mn). Sıfır ortalama nedeniyle MSE varyansa eşittir; bağımsız varyanslar toplanır. Sabit N altında yöntem sayısı m artınca τ²/m azalır; γ² kalır. Yöntemler gerçekte aynı temel kalibrasyon veya veriyi paylaşıyorsa bağımsızlık varsayımı bozulur. Farklı yöntemlerin maliyetleri, kalibrasyon yanlılıkları ve örnek seçimi değişebileceği için sonuç koşullu bir tasarım önerisidir.
