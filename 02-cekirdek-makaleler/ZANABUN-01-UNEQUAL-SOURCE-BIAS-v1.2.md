# ZANABUN-01 v1.2 — Unequal provenance, shared roots and biased independent witnesses

**Identity:** ZANABUN-01 manuscript family; analytical extension dated 22 October 2026. This is not a new distinct paper and contains no human-subject observations, journal submission or peer review.

## Canonical scope and question

Exact founding statement: Ehad Yek'tir ve Ehad âlemlerdeki her şeyi Yek'e göre yaratmıştır; her kar tanesi, her parmak izi dahil.

The Zanabûn formulation concerns the first knower's orientation to a known object and the second knower's examination of the resulting claim. Hebûn is its ontological foundation; the human-world epistemic application does not exhaust the broader ontological identity and mutual address of beings. Yek is not a newly created layer, a human essence or a paper-integration label. Cosmic 6+Tek (physics, biology, mind, spirit, morality, judgment/afterlife, plus Tek) differs from Core 13 human layers; emotion is not the sixth cosmic dimension. Distinctions between intelligence and reason, spirit and angels, innate and volitional morality, linear inclusion and circular scrutiny remain intact. Rasterast, Rabûn, Mabûn and Newroza Kawa are not revised by this statistical argument. Theology, philosophical ontology, formal model and empirical evidence are separate categories.

**Original question:** Under what conditions does adding an apparently independent second source make the estimate *less* accurate? This is a narrowly formal investigation, not a purported experimental demonstration of metaphysical premises.

## Mathematical model and proof

Let n witness reports be allocated to m source clusters of sizes n_g, with n=sum(n_g). For a fixed target theta, set W_gj = theta + b_g + G + B_g + e_gj. Here b_g is a fixed cluster bias; G is a shared global error; B_g is a cluster-level error; e_gj is private error. The random terms have zero means, finite variances omega^2, tau^2 and sigma^2, and are mutually independent. Define p_g=n_g/n and bbar=sum(p_g*b_g).

Then Bias(mean W)=bbar; Var(mean W - theta)=omega^2+tau^2*sum(p_g^2)+sigma^2/n; MSE(mean W)=bbar^2+omega^2+tau^2*sum(p_g^2)+sigma^2/n. Proof: mean W-theta=bbar+G+sum(p_g*B_g)+(1/n)*sum(e_gj). Independence makes cross-covariances vanish, and MSE equals variance plus squared bias. If clusters are correlated, an extra 2*sum_{g<h}(p_g*p_h*Cov(B_g,B_h)) is necessary. For equal clusters, zero bias and no global effect, the previous tau^2/m+sigma^2/n formula is recovered.

Define effective source count m_eff=1/sum(p_g^2). Cauchy-Schwarz gives 1<=m_eff<=m, with equality at m only for equal clusters. This is a variance-related summary, not a measure of truth, morality or ontological persons.

## Exact counterexamples

Set n=8, omega^2=1/4, tau^2=4, sigma^2=1 and theta=0. All numbers are **constructed mathematical examples**, not observations.

| Cluster sizes | Fixed biases | m_eff | Variance | MSE |
|---|---|---:|---:|---:|
| [8] | [0] | 1 | 35/8 = 4.375 | 4.375 |
| [4,4] | [0,0] | 2 | 19/8 = 2.375 | 2.375 |
| [7,1] | [0,0] | 32/25 = 1.28 | 7/2 = 3.5 | 3.5 |
| [2,2,2,2] | [0,0,0,0] | 4 | 11/8 = 1.375 | 1.375 |
| [7,1] | [0,10] | 1.28 | 7/2 = 3.5 | 81/16 = 5.0625 |

Counterexample A: two source clusters need not provide the same variance reduction; [7,1] is less informative than [4,4]. Counterexample B: reassigning one of eight reports to an independent but biased source raises MSE from 4.375 to 5.0625 despite increasing the number of sources. This is a fixed-n comparison, not an assertion that more reports were collected. Counterexample C: omega^2>0 is an uncertainty floor that proliferating independent clusters cannot remove.

## Alternative weighting and falsifiability

For unbiased group means Y_g, write v_g=tau^2+sigma^2/n_g. A weighted estimator T=sum(a_g*Y_g), sum(a_g)=1, has variance omega^2+sum(a_g^2*v_g). Lagrange optimization gives a_g=(1/v_g)/sum(1/v_h). In the [7,1] case, v_A=29/7, v_B=5, a_A=35/64, a_B=29/64, and the minimum variance is 161/64=2.515625, below the unweighted-witness variance 3.5. This optimum assumes no fixed group bias; with b_B=10 it can perform worse.

Rival explanations for agreement are shared calibration (G), hidden source reuse (Cov(B_g,B_h)), systematic bias (b_g), or time-varying theta. On one target, replacing theta by theta+c and every b_g by b_g-c leaves reports unchanged: an external reference is needed for absolute identification. An eventual empirical test would preregister blinded measurements from independently calibrated sources, use traceable external standards with their own uncertainty, and evaluate held-out squared errors and covariance predictions. Such a test has **not** been performed.

## Reproducibility and limits

Run `python3 07-deneyler-ve-karsi-ornekler/zanabun01_unequal_sources_exact.py`. Python standard library Fraction arithmetic checks each result by (1) group-level variance components and (2) direct summation of every pairwise witness covariance. This second algebraic implementation is not an independent human reviewer. Expected final line: `PASS: exact identities, covariance cross-check, counterexamples`.

The epistemic conclusion is limited: the second knower's verification should audit evidence lineage, possible common roots, bias and external reference, rather than counting agreeing sources. No theological proposition is statistically proved or refuted.
