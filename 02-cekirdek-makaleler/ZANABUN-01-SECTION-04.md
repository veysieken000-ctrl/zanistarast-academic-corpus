# ZANABUN-01 — Independent calibration groups at fixed observation budget

Suppose N reports are split equally among G groups, each containing N/G observers. Within a group, reports share a centered calibration error B_g of variance tau squared. Assume errors B_g are independent across groups; each observer also has independent private noise of variance sigma squared. The grand mean's error variance is tau squared / G + sigma squared / N.

**Proposition.** Holding N, tau squared greater than zero, and sigma squared constant, increasing the number G of independent calibration groups reduces the expected squared error of the grand mean.

**Proof.** The private term sigma squared / N remains constant. The common-error term tau squared / G decreases strictly with G. QED.

This conclusion depends on the groups having genuinely independent error sources. Distinct names, people, instruments, or AI agents do not automatically supply independence if they reuse the same reference, model, or dataset. At fixed cost, diversity may increase private variance or require fewer observations; in that case the proposition's assumptions fail and the advantage may disappear. If the group biases are themselves correlated, additional covariance terms must be included. The model does not prove that diversity always wins; it specifies one mechanism by which a second method can supply more useful confirmation than repeated outputs of the first method.
