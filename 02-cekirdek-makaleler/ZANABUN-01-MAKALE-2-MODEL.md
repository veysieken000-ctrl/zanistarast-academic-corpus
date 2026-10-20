# ZANABUN-01 — Makale Bölüm II: Formalizasyon ve karşı örnekler

**Sürüm ailesi:** ZANABUN-01 v0.2. Bu bölüm `ZANABUN-01-MAKALE-1-GIRIS.md` ile aynı makalenin devamıdır; ayrı makale sayılmaz.

## 3. Tek ortak hata

Ölçülecek hedef `θ` ve tanık raporları `W_i` olsun. `W_i=θ+B+ε_i` modeli kurulsun. `B` bütün tanıklara ortak hata, `ε_i` her tanığın özel hatasıdır. `E[B]=0`, `Var(B)=τ²`, `E[ε_i]=0`, `Var(ε_i)=σ²`, özel hatalar ve B karşılıklı bağımsız olsun. Ortalama `W̄=θ+B+(Σ ε_i)/n` ve:

**(1) `Var(W̄−θ)=τ²+σ²/n`.**

Gözlemci sayısı arttığında yalnız özel hata katkısı azalır. Tek gerçekleşimde ortak sapma sabit `B=b` ise `E[W̄−θ|B=b]=b` ve `MSE(W̄|B=b)=b²+σ²/n`. Bu koşullu ifade, rastgele ortak hata varyansından farklıdır.

**Deterministik karşı örnek:** `θ=0`, raporlar `(5,5,5,5)`. Grup ortalaması 5, grup içi varyans sıfır, dış hata 5'tir. Böylece tam uzlaşma dış doğruluğun yeterli koşulu değildir. Ters yönde, doğru değerin çevresindeki bağımsız gürültülü raporlar birbiriyle uyuşmayabilir; yüksek dağılım otomatik yanlış bilgi demek değildir.

## 4. İki düzeyli kaynak bağımlılığı

G kaynak grubu ve grup başına m tanık için:

`W_gj=θ+B_0+B_g+ε_gj`.

`B_0` bütün gruplarca paylaşılan hata, `B_g` yalnız g grubunun ortak hatası, `ε_gj` bireysel hata olsun. Bu bileşenler sıfır ortalamalı ve bağımsız; varyansları sırasıyla `τ_0²`, `τ_g²`, `σ²` kabul edilsin. Eşit ağırlıklı ortalama hatası:

`W̄−θ=B_0+(Σ_g B_g)/G+(Σ_gj ε_gj)/(Gm)`.

Bağımsızlık varsayımıyla kovaryans terimleri sıfırdır:

**(2) `MSE(W̄)=τ_0²+τ_g²/G+σ²/(Gm)`.**

Sabit `N=Gm` için bireysel hata katkısı `σ²/N` değişmez. Grup sayısı arttıkça `τ_g²/G` azalır, ancak küresel `τ_0²` kalır. Eğer gruplar aynı eğitim verisini, referans ölçeri veya ortak raporu kullanıyorsa `B_g` terimleri bağımsız değildir ve formül (2) yetersiz kalır; grup-arası kovaryans ayrıca hesaplanmalıdır.

## 5. Kimliklenebilirlik ve nedenin tekilliği

Küresel sapma `B_0` sabit bilinmeyen olsun. Herhangi bir `d` için `θ'=θ+d` ve `B'_0=B_0−d` tanımlandığında `θ'+B'_0=θ+B_0` elde edilir. Bu yüzden gözlenen raporlar hedef ve kalibrasyon sapmasını ayrı kimliklendiremez. Bilinen dış standart, ayırt edici müdahale veya açık tanımlayıcı varsayım gerekir. Sıfır ortalamalı rastgele etki varsayımının çoklu bağımsız deneylerde sağladığı çıkarımlar, tek gerçekleşimde kesin dış doğrulukla karıştırılmamalıdır.

Ayrıca `x(t+1)=x(t)` ile `x(t+1)=x(t)^2` modelleri `x(0)=1` altında sonsuz tekrar boyunca aynı gözlemi verir. `x(0)=2` seçilirse bir adım sonra sırasıyla 2 ve 4 öngörürler. Tekrar, gözlem tutarlılığını artırabilir ama tek nedenin kanıtı değildir. Bu örnek yerleşik model ayırt edilebilirliği fikrinin basit gösterimidir.

## 6. Maliyetli kaynak çeşitliliği

Bağımsız bir grup kurmanın maliyeti `c_0>0`, her raporun maliyeti `c_1>0`, toplam bütçe `C=G(c_0+c_1m)` olsun. Formül (2)'de `G=C/(c_0+c_1m)` yerine yazılırsa:

`MSE(m)=τ_0²+[τ_g²(c_0+c_1m)+σ²(c_0/m+c_1)]/C`.

Sürekli m için türev `[τ_g² c_1−σ² c_0/m²]/C` ve `τ_g>0` koşuluyla iç optimum:

**(3) `m*=sqrt(σ² c_0/(τ_g² c_1))`.**

Gerçekte m ve G pozitif tam sayıdır; bütçe aşılmaz, kalan bütçe ve bağımsızlık varsayımları denetlenir. `τ_g=0` olduğunda bu iç optimum tanımsızdır. Bu sonuç klasik maliyetli küme örneklemesi sezgisinin Zanabûn doğrulama tasarımına uyarlanmasıdır, yeni matematiksel keşif değildir.
