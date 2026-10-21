# ZANABUN-01 — General covariance and dependence audit

For a vector of n reports with covariance matrix Sigma, the arithmetic mean has variance (1/n squared) times the sum of all entries of Sigma. If the off-diagonal covariances are positive, a naive formula that sums only diagonal variances understates uncertainty. The equal-correlation effective-sample-size expression in section 3 is only a special case of this identity.

An independence audit should identify whether observers share a calibration device, reference standard, original document, training source, or earlier reported answer. Independence cannot be inferred from separate names or different interfaces. If the covariance matrix is unknown, report uncertainty under plausible dependence scenarios rather than declaring a precise effective sample size. A robust sensitivity analysis compares zero dependence, moderate positive dependence, and an extreme common-source case.
