# ZANABUN-01 v1.4 — II. Model ve ispat

[I. bölüm](ZANABUN-01-v1.4-PART-1.md), [III. bölüm](ZANABUN-01-v1.4-PART-3.md), [IV. bölüm](ZANABUN-01-v1.4-PART-4.md) ile tek makaledir.

## 4. Varsayımlar

Sabit skaler hedef θ için A ve B kaynaklarından sırasıyla n_A ve n_B rapor elde edilsin:

    W_Aj = θ + G + α + U_A + ε_Aj
    W_Bj = θ + G + β + U_B + ε_Bj

G ortak sıfır ortalamalı hata, Var(G)=ω²; U_A,U_B sıfır ortalamalı kaynak hataları, Cov(U_A,U_B)=c; ε bağımsız özel hatadır. Yazılmayan çapraz kovaryanslar sıfır varsayılır. G dışındaki kaynak ortalamalarının varyansları v_A=τ_A²+σ_A²/n_A ve v_B=τ_B²+σ_B²/n_B olsun. Sabit yanlılık sınırları |α|≤a, |β|≤b (a,b≥0); kaynak kovaryans aralığı c_alt≤c≤c_üst. Kovaryans matrisi pozitif yarı-belirli olmalıdır: |c|≤√(v_A v_B). Sınırların dış kalibrasyonla savunulması gerekir; burada ölçülmüş değildir.

Y_A,Y_B kaynak ortalamaları için konveks tahmin T_t=(1−t)Y_A+tY_B, 0≤t≤1:

    MSE(t,α,β,c) = ω² + v_A(1−t)² + v_B t²
                    + 2c t(1−t) + [(1−t)α+tβ]².       (1)

ω² ağırlıktan bağımsız ortak hata tabanıdır.

## 5. Önerme 1: iki yanlılık ve kovaryans aralığında minimaks

A=v_A+a², B=v_B+b², C=c_üst+ab, D=A+B−2C olsun. En kötü durum riskinin tam ifadesi:

    R(t)=ω²+A(1−t)²+B t²+2C t(1−t).                (2)

D>0 için tek minimaks konveks ağırlık:

    t*=min{1,max{0,(A−C)/D}}.                       (3)

D=0 ve model uygulanabilir ise A=B=C, dolayısıyla tüm t değerleri aynı riski verir.

**İspat.** t ve 1−t negatif olmadığından |(1−t)α+tβ|≤(1−t)a+tb; iki yanlılığın aynı işaretli sınır uçlarında eşitlik vardır. 2t(1−t)≥0 olduğundan en kötü kovaryans c_üst'tür. (1)'e konunca (2) elde edilir. R'(t)=−2(A−C)+2Dt; R''(t)=2D. Ayrıca D=(v_A+v_B−2c_üst)+(a−b)²≥0; ilk terim geçerli kovaryans matrisinde kaynak farkının varyansıdır. D>0 için türev sıfırı (A−C)/D olup [0,1] aralığına kırpılır. D=0 halinde her iki negatif olmayan terim sıfırdır; A=B=C çıkar. QED.

**Eşik:** D>0 için t*=0 ancak ve ancak C≥A ise. C<A ise küçük pozitif t A-tek riskini kesin azaltır. Bu, ontolojik ikinci bilenin gereksizliği değil, belirtilen MSE altında ikinci ölçüm kanalının **sayısal ağırlığı** hakkındadır.

**Eski model:** a=0, c_üst=0, b=d için (3), v1.3'ün v_A/(v_A+v_B+d²) formülüne indirgenir. **Karşı durum:** a=b ve c_üst=0 olduğunda aynı işaretli en kötü yanlılık ortak sabit kaymadır; ağırlık yine yalnız varyanslara göre belirlenir. “Her iki kaynak yanlıysa ikincisi dışlanır” genellemesi yanlıştır.

**Sınır:** c_üst fiziksel kovaryans koşulunu ve kaynak soyağacı kayıtlarını sağlamalıdır. Negatif ağırlıklara veya doğrusal olmayan tahmincilere bu sonuç genellenmez. Normal dağılım zorunlu değildir; sonlu ikinci momentler yeterlidir. Güven aralığı, dış geçerlik ve bütün zamanlar için daimilik bu matematikten çıkmaz. Kalibrasyon ve test veri sızıntısı varsa sınırlar ayrıca yeniden denetlenmelidir.
