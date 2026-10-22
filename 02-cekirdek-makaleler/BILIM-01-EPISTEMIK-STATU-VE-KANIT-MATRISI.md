# BİLİM-01 — Bilginin türü, dayanağı ve epistemik statüsü

**22 Ekim 2026 · v0.1 · araştırma taslağı · yayıma hazır değil**

## Amaç
Zanistarast araştırma külliyatında bir iddianın ne tür bir önerme olduğunu, hangi kaynaklara dayandığını ve hangi denetimlerden geçtiğini birbirinden ayırmak.

## Kaynak sınırı
Özgün kaynak: `6-Bilim (1).docx`. Belgenin paragraf düzeyinde yeniden okunması henüz tamamlanmadı. Bu nedenle aşağıdaki üç eksenli tablo **araştırmacı önerisidir**; kurucunun özgün metninden doğrudan alıntı veya uygulanmış Mira yazılımı standardı değildir.

Kanonik çerçeve: Hebûn ontolojik temel, Zanabûn bilginin oluşumu ve gerekçelendirilmesi, Rasterast karşı-delil ve epistemik statü denetimi. Mira araştırır, Rasterast doğrular, Müdebbir yayın kararını verir.

## Araştırma sorusu
Aynı külliyattaki ontolojik, teolojik, normatif, analojik ve ampirik iddialar hangi ortak kayıt düzeniyle, fakat kendi yöntemleri korunarak değerlendirilebilir?

## Ayırıcı Tek adayı
Her önerme için üç ayrı alan tutulması:
1. **Tür:** ontolojik, teolojik, kavramsal, normatif, matematiksel, analojik veya ampirik.
2. **Dayanak:** özgün belge, gerekçeli argüman, gözlem, deney, veri veya bağımsız değerlendirme.
3. **Denetim durumu:** kaynak bekliyor, kaynak izlendi, karşı-delil arandı, bağımsız inceleme yapıldı, çelişki açık.

Bu sınıflandırmanın özgünlüğü ve etkinliği henüz doğrulanmadı. Durum adları kanonik yazılım enum'ları olarak sunulmaz.

## Örnek kayıtlar
| Önerme | Tür | Mevcut destek sınırı |
|---|---|---|
| Kozmik 6+Tek evre tasnifi | Ontolojik sınıflama | Kurucu kanonik önerme; ampirik doğrulama tamamlanmadı |
| Zekâ ve aklın iki evresi | Kavramsal ve sınanabilir yönleri olan önerme | Araştırma görevi tasarlandı; veri yok |
| İkinci bilenin ontolojik muhataplığı | Ontolojik ve teolojik | Bilimsel bağımsız hakemlikle özdeş değil |
| Bağımsız değerlendirmenin ortak hataları azaltması | Ampirik hipotez | Karşılaştırmalı test yapılmadı |
| Mabûn Ekonomi Modeli | Normatif ve kurumsal model | Model adı kanonik; ekonomik etkiler ölçülmedi |
| Rabûn meclis düzeni | Kurumsal ve normatif önerme | Kaynak incelemesi kısmi; uygulama doğrulanmadı |

## Yöntem
Özgün `6-Bilim (1).docx` belgesinin tüm iddialarını paragraf kimliğiyle çıkar; her iddiayı üç eksende kodla; birbiriyle çelişen etiketleri bağımsız ikinci okuyucuya incelet; olumlu ve olumsuz bulguları sakla. Kavramsal bir iddiaya deney şartı, ampirik bir iddiaya yalnızca kanonik onay yeterli sayılmamalıdır.

## Karşılaştırmalı literatür
- Stanford Encyclopedia of Philosophy, “Scientific Method” (8 Ağustos 2026 güncellemesi): https://plato.stanford.edu/entries/scientific-method/
- Stanford Encyclopedia of Philosophy, “Theory and Observation in Science” (12 Ocak 2026 güncellemesi): https://plato.stanford.edu/entries/science-theory-observation/
- Stanford Encyclopedia of Philosophy, “Scientific Objectivity”: https://plato.stanford.edu/entries/scientific-objectivity/

Bu kaynaklar kurucu modelin doğrulandığını göstermez; bilimsel yöntem ve kanıt değerlendirmesi için karşılaştırma zemini sağlar.

## Newroza Kawa bağlantısı
Bilim, hukuk, eğitim, Rabûn yönetimi, Mabûn Ekonomi Modeli ve sanat araştırmalarında iddia türleri ayrı tutulmalıdır. Tabiata uygunluk, Mabûn Ekonomi Modeli'nin adı değil açıklayıcı benzerlik ilkesidir; kendiliğinden ampirik kanıt değildir.

## Kalite durumu
**K0 açık:** özgün DOCX paragraf eşlemesi. **K1 kısmi:** karşılaştırmalı literatür. **K2 kısmi:** sınıflandırma yöntemi. **K3–K6 açık:** uygulama verisi, dış geçerlik, etik ve bağımsız denetim. **Yayıma hazır değildir.**

## Kaynak izi
- `6-Bilim (1).docx`, kurucu özgün metni.
- `zanistarast-papers/docs/architecture/ZANISTARAST_MIRA_MASTER_ROADMAP.md`.
- `zanistarast-papers/reference-implementation/mira/src/zanistarast_scientific_mission.rs`.

## Ek: Rasterast iddia turu ve kaynak denetimi (22.10.2026)

Bu bolum mevcut uc eksenli siniflandirmayi `RASTERAST-02-KAYNAK-KANIT-BAGIMSIZLIK-DENETIM-PROTOKOLU.md` ile karsilastirir. Ozgun `6-Bilim (1).docx` metninin tam paragraf denetimi yapilmamistir. Asagidaki kodlar arastirma kaydidir; Mira yaziliminin onayli alanlari degildir.

| Kod | Iddia | Tur | Kaynak ve durum |
|---|---|---|---|
| BL-01 | Altinci kozmik boyutun evreleri hesap/hukum ve hukmun sonucudur | Kurucu ontolojik/teolojik tanim | 16.10.2026 tarihli kurucu onayli 6 boyut / 12 evre tablosu; kaynakta dogrulandi, deneysel kanit degil |
| BL-02 | Kor ikinci degerlendirme belirli hata turlerini azaltabilir | Ampirik hipotez | RASTERAST-02 pilot tasarimi; deney henuz yapilmadi |
| BL-03 | Hukum Meclisi altinci kozmik boyutun birinci evresine ozdestir | Kategori esitlemesi | Kurucu tablo ve kurumsal metinler bu ozdesligi desteklemez |
| BL-04 | Mabun Ekonomi Modeli ihtiyac erisimini iyilestirir | Ampirik kurumsal hipotez | Model adi kanonik; etki verisi bulunmuyor |

Kaynakla uyum, bir onermenin kurucu metinde yer aldigini gosterebilir; tek basina deneysel dogruluk saglamaz. Ayni kaynagi tekrar okuyan iki kisi bagimsiz kaynak dogrulamasi yapmis sayilmaz. Ortak veri, yontem ve alinti bagimliligi kaydedilmelidir. K0 kaynak kapisinin tamamlanmasi K1-K6 kapilarinin tamamlandigi anlamina gelmez.

Karsilastirmali dis kaynak: Reiss ve Sprenger, Scientific Objectivity, Stanford Encyclopedia of Philosophy (2020 esasli revizyon): https://plato.stanford.edu/entries/scientific-objectivity/ . Bu kaynak Zanistarast'in kurucu iddialarini dogrulamaz.

**Acik is:** Ozgun bilim DOCX paragraf eslemesi, bagimsiz ikinci okuma ve ampirik sinamalar. **Yayima hazir degil.**

## Ozgun bilim belgesi kimlik denetimi (22.10.2026)

Bagli Google Drive uzerinde `6-Bilim (1).docx` tam adiyla arama sonuc vermedi. `Bilim` aramasinda ise `7-Bilim.docx` adli 32515 baytlik bir belge ve ayni adla kopyalar goruldu. Ozellikle `7-Bilim.docx` (Drive kimligi `14oSElIHPtjTjMRna0zZXTS9n7xt3ACFM`) 25.12.2025 tarihli; diger kopyalar 2026 tarihlidir. **Bu iki dosya adinin ayni eseri temsil ettigi dogrulanmadi.** Yalnizca ad benzerliginden kaynak ozdesligi kurulamaz; 7-Bilim belgesine 6-Bilim icin paragraf numarasi atfedilmez.

Sonraki K0 kontrolu: her iki belgenin varsa icerik karmasini, ilk basligini, bolum yapisini ve paragraf dizisini karsilastirmak; uyusma yoksa ayri eserler olarak kaydetmek. Bu turda Drive dosyasinin tam metni okunmadi. **Ozgun DOCX paragraf eslemesi halen acik, yayin hazirligi tamamlanmadi.**

## Drive ozgun bilim metni dogrudan okuma denetimi (22.10.2026)

Google Drive'daki `7-Bilim.docx` (kimlik `14oSElIHPtjTjMRna0zZXTS9n7xt3ACFM`) ve `7-Bilim.docx adli dosyanin kopyasi` (kimlik `1tyti64jI8OUj_5cA-U4ggLgyJIdYjEtW`) baglantilari acilip okunabilir metin olarak alindi. Her ikisi de `VARLIK VE YARATICI BILIMININ TEMELI / BILIM VE INSAN` basligi ile basliyor; baglanti uzerinden donen metin uzunlugu her ikisinde 25037 karakterdir. Bu gozlem ikisinin ikili DOCX karmalarinin ayni oldugunu kanitlamaz. `6-Bilim (1).docx` ile `7-Bilim.docx` arasinda dosya ozdesligi halen teyit edilmemistir.

| Kod | 7-Bilim metninde dogrudan gozlenen | Kaynak statusu |
|---|---|---|
| BL-S01 | Bilgi, bilen oznenin bilinen nesneye yonelimiyle iliskilendiriliyor | Tarihsel kurucu bilim gorusu; dogrudan okundu |
| BL-S02 | Iki bilen oznenin onayi ve onlardan bagimsiz gerceklik vurgulaniyor | Epistemolojik/ontolojik iddia; deneysel kanit degil |
| BL-S03 | Metin, fizik, biyoloji, zihin ve kanun zamanini ardarda tartisiyor | Tarihsel boyutsal zaman anlatimi |
| BL-S04 | Biyoloji aciklamasinda eseysiz bolunme ve eseyli birlesim evre gecisiyle iliskilendiriliyor | Tarihsel metin; guncel tek/ cok hucreli kanonik adlandirmayla karistirilmamali |
| BL-S05 | Dortuncu boyutun bir bolumunde melek ve seytan ifadesi bulunuyor | Tarihsel metin; guncel ruh / melekler evreleriyle farki kaydedilmeli |

**Sinir:** Bu turda Drive baglantilarindan okunabilir metin alindi, ancak DOCX paragraf indisleri ve ikili dosya karmalari hesaplanmadi. Bu nedenle `7-Bilim.docx` icin bile kesin paragraf numarasi atanmadi. Eski metnin olasi fiziksel/kozmolojik ifadeleri de bilimsel dogrulama yerine kaynak iddiasi olarak ele alinmalidir. K0 metin erisimi ilerledi; dosya kimligi ve paragraf eslemesi acik. Yayin hazir degil.

## H07 English source-based critical translation: opening argument (22 October 2026)

**Primary Turkish source:** `hebun-zanabun/articles/makale-06.md`, main branch, title *Varlık ve Yaratıcı Biliminin Temeli / Bilim ve İnsan*. This passage is a close, edited translation of the source's introduction and initial epistemological argument, **not** a translation of the entire paper. The existing H07 English development draft remains an outline.

### Translation — Introduction

As a living species capable of existing in communities, human beings attempt to understand nature and sustain life within it. The desire to exist and to extend the sphere of existence is expressed through adaptation to the natural environment. In the struggle to remain alive, beginning with birth and continuing until death, an individual's impressions become information for that individual. Social knowledge may be understood as an agreement reached through the shared struggle of individuals to live.

The accumulation of knowledge, defined here as the product arising when a knowing subject turns toward a known object, has contributed throughout history to the classification of fields of science. What knowledge is and why it is needed are directly related to what the subject is and what that subject requires. The manuscript characterizes science in terms of knowledge intended to remain generally valid across time. Because knowledge is necessary for humanity, the inquiry seeks the human knower at the foundation of the philosophy of science.

### Translation — The two knowers and a shared reality

Throughout history, people have tried to comprehend existing things and conceptual objects and to attain the knowledge required for science. The consistency and accumulation of information, whether regarded as objective or subjective, are presented as conditions for scientific development. Cultures, discoveries, civilizations, customs, books, inscriptions, tools, historical remains, and symbols all carry accumulated human knowledge.

The author argues that knowledge requires a knowing subject. For enduring knowledge, the author adds a second knowing subject: when one person knows something, a second person must be able to confirm it. The two must also confront a reality independent of both. Reason is described as the shared meeting place of the two knowers, while the independent third term provides a common ground for their judgments. The text then moves from this epistemic account toward a theological argument that universal laws point to a universal knower. **This last inference is the author's philosophical-theological claim, not a conclusion established by repeatable measurement.**

### Critical editorial notes (not part of the translated source)

1. The original uses *bilgi*, *bilim*, and *ilim* in overlapping but distinguishable senses. These are rendered provisionally as knowledge, science, and systematic knowledge; a complete edition must supply a terminology glossary.
2. The source moves from intersubjective confirmation to an independent reality and then to a divine knower. Agreement between two observers does not, by itself, establish truth: common measurement bias is a counterexample. This objection is editorial analysis, not a quotation from the author.
3. The historical source later describes biology with an asexual/sexual progression and contains older fourth-dimension terminology. The later founder-approved cosmic-stage names are unicellular/multicellular and spirit/angels. Translation must preserve historical wording and flag subsequent revisions separately.
4. Source identity: Google Drive holds four `7-Bilim.docx` records with identical readable text (25,037 characters each), but their equivalence to the older filename `6-Bilim (1).docx` has **not** been established. The directly identified GitHub primary source for this English passage is `articles/makale-06.md`, not a presumed filename match.

**Status:** This section is a substantive English source-based translation excerpt plus marked editorial critique. It is not a complete English journal manuscript, and it has not undergone independent peer review.

## H07 English critical translation — 1.1 Science of Being (22 October 2026)

**Source:** `veysieken000-ctrl/hebun-zanabun/articles/makale-06.md`, section 1.1, *Varlık Bilimi*. The paragraphs below are a selective close translation and are not a complete translation of the section. Editorial cautions are explicitly separated.

### Translation: creation, subjects, and an object

From the standpoint of creation and the requirement of two knowing subjects, the author proposes the following account. For an initial knowing subject to disclose its knowledge to another knower, a second subject must exist. Because that second subject depends upon the first for its existence, the first must also bring forth the object through which knowledge becomes visible. The author distinguishes the first subject, the second knower, and the known object or product, and adds a fourth term: a common ordering or law through which their relation can be maintained. In the author's theological reconstruction, the divine first knower creates the spiritual second subject and the physical world through which it acquires embodiment. This is a metaphysical model of creation, not an observed sequence of physical events.

The manuscript then describes creation as beginning with differentiation and the giving of spirit. It associates the origin of physical reality with divine knowledge, will, awareness, and power. It discusses the Big Bang, the Higgs boson, protons, neutrons, and electrons as part of this historical cosmological interpretation. These claims are preserved as claims made by the source, not endorsed here as current physics.

### Translation: three systems of being and their ordering

The author describes a being in terms of center and periphery, internal components, and a law that governs its organization. The first system concerns physical beings and uses atomic components and stellar or planetary structures as examples. The second concerns biological beings and invokes DNA, RNA, proteins, cell division, and the emergence of multicellular organisms. The third concerns beings with minds, connecting nervous systems, senses, memory, intelligence, and reason. The author argues that each system requires an ordering law and associates spirit and angels with the governance of the systems.

The author also treats repeatability, induction, deduction, and confirmation as central to reliable knowledge. The text compares interactions among physical, biological, cognitive, moral, and theological terms and proposes a general pattern in which two subjects participate in the emergence of a third product. It extends this pattern to human production and to an account of the creator and the human knower.

### Editorial scientific and conceptual audit — not source translation

- **Atomic counterexample:** Ordinary hydrogen-1 has one proton and one electron but no neutron. The source's proton–neutron–electron triad cannot be a universal definition of an atom. Hydrogen and helium labels also need correction before a science-journal submission.
- **Biological stages:** The source uses asexual/sexual reproduction to explain a historical transition. The founder-approved later cosmic stages are unicellular/multicellular. Reproduction mode and cellular organization are distinct variables; the latter terminology must not be silently substituted inside a historical quotation.
- **Mind and spirit:** Nervous-system structures are biological descriptions, while intelligence/reason and spirit/angels are separate levels in the author's framework. The latter are theological-ontological categories, not experimentally identified causal forces.
- **Epistemic distinction:** Replication and independent corroboration may improve confidence, but shared systematic error can survive agreement between two observers. The second-knower thesis should be stated as an argument with explicit assumptions, not an automatic proof of truth.
- **Scientific scope:** The historical source's descriptions of the Big Bang, the Higgs boson, black holes, and particle formation need independent physics citations and revision; analogies between these topics and divine creation do not constitute experimental confirmation.

**Completion boundary:** This addition advances H07's English source-based edition of section 1.1. It does not finish section 1.1 paragraph by paragraph, translate the remaining Turkish manuscript, or certify the paper for publication.
