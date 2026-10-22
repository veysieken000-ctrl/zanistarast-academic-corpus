# ZANABUN-01 v1.3 — II. Matematiksel model, önerme ve ispat

Bu dosya [I. bölüm](ZANABUN-01-v1.3-PART-1.md), [III. bölüm](ZANABUN-01-v1.3-PART-3.md) ve [IV. bölüm](ZANABUN-01-v1.3-PART-4.md) ile **tek** makaledir.

### 3. Model ve varsayımlar

Sabit skaler gerçek hedef `theta` için A kümesinde `n_A`, B kümesinde `n_B` rapor olsun:

```text
W_Aj = theta + G + U_A + e_Aj
W_Bj = theta + G + delta + U_B + e_Bj
```

`G` sıfır ortalamalı, varyansı `omega2` olan tüm raporlara ortak hata; `U_A,U_B` sıfır ortalamalı, her biri `tau2` varyanslı ve başlangıçta bağımsız küme hataları; `e_gj` sıfır ortalamalı, `sigma2` varyanslı bağımsız özel hatalardır. Rastgele terimler ortak `G` paylaşımı dışında bağımsız kabul edilir. B'nin bilinmeyen **sabit** yanlılığı `delta` için dış kalibrasyonla savunulması gereken `|delta|<=d` varsayılır; A'nın artık sabit yanlılığı olmadığı ayrıca varsayılır. Bunlar gerçek kişilere veya cihazlara ilişkin ölçülmüş sonuçlar değildir.

Küme ortalamaları `Y_A,Y_B` olsun. `v_A=tau2+sigma2/n_A`, `v_B=tau2+sigma2/n_B`. Konveks doğrusal tahmin `T_t=(1-t)Y_A+tY_B` için `0<=t<=1`. Doğrudan beklenti ve varyans hesabı:

```text
Bias(T_t)=t*delta
Var(T_t-theta)=omega2+(1-t)^2*v_A+t^2*v_B
MSE(t,delta)=omega2+(1-t)^2*v_A+t^2*v_B+t^2*delta^2.   (1)
```

Ortak `G` terimi, kaynak sayısı artsa da bu modelde kalan bir hata tabanıdır. MSE, teolojik veya ahlaki doğruluğun evrensel ölçüsü değildir.

### 4. Önerme 1 — Sınırlı yanlılık için minimaks ağırlık

`v_A>0`, `v_B>=0`, `d>=0` ve model varsayımları altında, `sup_{|delta|<=d} MSE(t,delta)` ifadesinin `0<=t<=1` aralığındaki tek minimizeri:

```text
t_star = v_A/(v_A+v_B+d^2)                                  (2)
R_star = omega2+v_A*(v_B+d^2)/(v_A+v_B+d^2).                (3)
```

**İspat:** (1)'de `t^2*delta^2` en büyük değerini `delta=±d` uçlarında alır. En kötü durum riski `omega2+v_A*(1-t)^2+(v_B+d^2)*t^2` olur. Birinci türev `-2*v_A+2*t*(v_A+v_B+d^2)`, ikinci türev kesin pozitif `2*(v_A+v_B+d^2)` olduğundan (2) tek minimumdur; `0<t_star<=1` sağlanır. Yerine koyunca (3) elde edilir. İspat tamam.

`d=0` iken olağan ters-varyans ağırlığı bulunur. `d` büyüdükçe B'nin ağırlığı azalır; sonlu `d` için sıfır olmaz. Eğer yanlılık sınırsızsa her `t>0` için en kötü MSE sonsuzdur ve bu **konveks doğrusal sınıfta** `t=0` minimaks seçimdir. `R_star<=omega2+v_A`, yani A-tek riskinden yüksek değildir; ancak bu yalnız **doğru varsayımlar altında** geçerli bir garantidir. Doğrusal olmayan tahmin ediciler için genel optimum iddia edilmez.

### 5. Önerme 2 — Gizli bağımlılık

`Cov(U_A,U_B)=c` olursa:

```text
R_c(t)=omega2+v_A*(1-t)^2+v_B*t^2+2*c*t*(1-t)+d^2*t^2.   (4)
```

`v_A+v_B+d^2-2*c>0` ise türevden çıkan durağan nokta `(v_A-c)/(v_A+v_B+d^2-2*c)` olup konveks ağırlık için `[0,1]` aralığına kırpılır. Böylece ayrı isimler veya ayrı raporlar hata bağımsızlığı kanıtı değildir. Kaynak soyağacı ve kovaryans bilinmiyorsa (2)'nin koşulları doğrulanmış sayılmaz.

**İddia türleri:** Ehad/Yek kurucu teoloji; ikinci bilenin ontolojik kapsamı felsefi/kanonik yorum; (1)–(4) koşullu matematik; gerçek dünyada `d,c` değerlerinin ölçülmesi ise **henüz yapılmamış** ampirik iştir.
