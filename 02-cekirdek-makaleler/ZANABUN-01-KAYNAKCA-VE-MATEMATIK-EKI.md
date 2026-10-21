# ZANABUN-01 — Kaynakça ve matematik eki

**Aynı makale ailesi:** ZANABUN-01 v1.0, 21.10.2026. Ayrı makale değildir. Ana metin 1–6. bölümler; 'ZANABUN-01-MAKALE-DEVAM-07-10.md' 7–10. bölümlerdir.

## References

Hong, Lu, and Scott E. Page. 2004. “Groups of Diverse Problem Solvers Can Outperform Groups of High-Ability Problem Solvers.” *Proceedings of the National Academy of Sciences* 101 (46): 16385–89. https://doi.org/10.1073/pnas.0403723101. PNAS yayın sayfasından doğrulandı.

Lorenz, Jan, Heiko Rauhut, Frank Schweitzer, and Dirk Helbing. 2011. “How Social Influence Can Undermine the Wisdom of Crowd Effect.” *Proceedings of the National Academy of Sciences* 108 (22): 9020–25. https://doi.org/10.1073/pnas.1008636108. PubMed PMID 21576485 ve ETH Zürich kurum kaydından doğrulandı.

National Institute of Standards and Technology (NIST). *Technical Note 1297*, sections “2. Classification of Components of Uncertainty” and “5. Combined Standard Uncertainty.” https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-2-classification-components-uncertainty ve https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty. Resmî NIST metninden doğrulandı. Web sayfası tarihi özgün teknik notun ilk yayın yılı değildir.

Zanistarast Ontology Project. t.y. “Zanabûn: A Computational Epistemology of Knowledge as Coherent Multi-Agent Witnessing.” Özgün kaynak: 'veysieken000-ctrl/zanistarast-ontology/papers/zanabun.md'. Git **blob** SHA: ee68095b8d87ba8a580492cfd4c98b86e0a0f21a. Dosyada aynı konu için iki ardışık metin vardır.

Zanistarast Research Program. 2026. “Zanabûn — İkinci bilenin doğrulaması, tekrar ve daimilik.” 18 Ekim kurucu açıklaması kaydı, eski araştırma dalında 'research/yek-6tek-program/KANONIK-ZANABUN-IKINCI-BILEN-DOGRULAMA-DAIMILIK-2026-10-18.md'. Blob SHA: 330db69e2146656281ebc32aa33439666ec54ce4.

Zanistarast Research Program. 2026. “Zanabûn Epistemolojisinde Tanıklık Tutarlılığı, Bağımsızlık ve Ortak Hata.” Önceki taslak, eski araştırma dalında 'research/yek-6tek-program/manuscripts/ZANABUN-01-bagimsiz-taniklik-ve-ortak-hata.md'. Blob SHA: dea450a481b14f2668480513156a96e965d676f3.

**Kaynak kökeni notu:** Blob SHA dosya içeriğini tanımlar; commit SHA değildir. Eski kaynaklar yerlerinde bırakıldı, değiştirilmedi.

## Ek A — İkinci matematik kontrolü

Hiyerarşik modelde ortalama hata \(e=b+U+\sum_g(m_g/n)C_g+n^{-1}\sum_{gi}\varepsilon_{gi}\). Rastgele bileşenler bağımsız ve sıfır ortalamalıysa \(E(e)=b\), \(\operatorname{MSE}=E(e^2)=b^2+\operatorname{Var}(e)\). \(C_g\) katsayısı \(m_g/n\) olduğundan varyans katkısı \(\tau_c^2\sum_g(m_g/n)^2\)'dir. Özel hata katkısı \(\sigma^2/n\), küresel katkı \(\tau_0^2\)'dir. Ana metindeki denklem (1) bu toplamdan çıkar.

Cauchy–Schwarz: \((\sum_gm_g)^2\leq G\sum_gm_g^2\). \(\sum_gm_g=n\) olduğundan \(\sum_g(m_g/n)^2\geq1/G\). Eşit küme büyüklüklerinde eşitlik vardır. \(n/G\) tamsayı değilse en yakın dengeli tamsayı dağılımı tercih edilir.

Tek kümede \(W_i-\overline W=\varepsilon_i-\overline\varepsilon\); dolayısıyla \(n^{-1}\sum_i(W_i-\overline W)^2\)'nin beklenen değeri \((n-1)\sigma^2/n\)'dir. Ortak hata, yalnız bu grup içi varyanstan tanımlanamaz. Gerçek dünyada kümeler arası bağımsızlık yoksa denklem (1)'e kovaryans terimleri eklenmelidir.

**Negatif kontrol:** \(\tau_0=\tau_c=b=0\) ise \(\operatorname{MSE}=\sigma^2/n\); böyle bir dünyada kalibrasyon-kümesi çeşitliliğinin bağımsız faydası olduğu iddia edilmez. Ağır kuyruklar, farklı hassasiyetler ve örneklem seçimi kapsam dışıdır.

## Eski deney ailesi

20 Ekim 2026 eski deney eki: 'research/yek-6tek-program/manuscripts/ZANABUN-01-ORTAK-HATA-DENEY-EKI-2026-10-20.md' (Git blob SHA 45578288450485cfaf0a217a2b3ce0dc7b32e505). Önceki kod: 'research/yek-6tek-program/experiments/zanabun_common_error_trial.py' (Git blob SHA 37588200906b85147349cb7b169ed8b570a5e068). Yeni hiyerarşik deney aynı sürüm ailesinin yöntem geliştirmesidir; yeni benzersiz makale değildir.
