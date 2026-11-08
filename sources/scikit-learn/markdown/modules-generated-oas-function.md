[Skip to main content](https://scikit-learn.org/stable/modules/generated/oas-function.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/oas-function.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/oas-function.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/oas-function.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/oas-function.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/oas-function.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/oas-function.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/oas-function.html)

Collapse Sidebar Expand Sidebar

oas[#](https://scikit-learn.org/stable/modules/generated/oas-function.html#oas "Link to this heading")

=======================================================================================================

sklearn.covariance.oas(_X_, _\*_, _assume\_centered\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_shrunk_covariance.py#L617)
[#](https://scikit-learn.org/stable/modules/generated/oas-function.html#sklearn.covariance.oas "Link to this definition")

Estimate covariance with the Oracle Approximating Shrinkage.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/covariance.html#shrunk-covariance)
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Data from which to compute the covariance estimate.

**assume\_centered**bool, default=False

If True, data will not be centered before computation. Useful to work with data whose mean is significantly equal to zero but is not exactly zero. If False, data will be centered before computation.

Returns:

**shrunk\_cov**array-like of shape (n\_features, n\_features)

Shrunk covariance.

**shrinkage**float

Coefficient in the convex combination used for the computation of the shrunk estimate.

Notes

The regularised covariance is:

(1 - shrinkage) \* cov + shrinkage \* mu \* np.identity(n\_features),

where mu = trace(cov) / n\_features and shrinkage is given by the OAS formula (see [\[1\]](https://scikit-learn.org/stable/modules/generated/oas-function.html#rca3a42e5ec35-1)
).

The shrinkage formulation implemented here differs from Eq. 23 in [\[1\]](https://scikit-learn.org/stable/modules/generated/oas-function.html#rca3a42e5ec35-1)
. In the original article, formula (23) states that 2/p (p being the number of features) is multiplied by Trace(cov\*cov) in both the numerator and denominator, but this operation is omitted because for a large p, the value of 2/p is so small that it doesn’t affect the value of the estimator.

References

\[1\] ([1](https://scikit-learn.org/stable/modules/generated/oas-function.html#id1)
,[2](https://scikit-learn.org/stable/modules/generated/oas-function.html#id2)
)

[“Shrinkage algorithms for MMSE covariance estimation.”, Chen, Y., Wiesel, A., Eldar, Y. C., & Hero, A. O. IEEE Transactions on Signal Processing, 58(10), 5016-5029, 2010.](https://arxiv.org/abs/0907.4698)

Examples

\>>> import numpy as np
\>>> from sklearn.covariance import oas
\>>> rng \= np.random.RandomState(0)
\>>> real\_cov \= \[\[.8, .3\], \[.3, .4\]\]
\>>> X \= rng.multivariate\_normal(mean\=\[0, 0\], cov\=real\_cov, size\=500)
\>>> shrunk\_cov, shrinkage \= oas(X)
\>>> shrunk\_cov
array(\[\[0.7533, 0.2763\],\
       \[0.2763, 0.3964\]\])
\>>> shrinkage
np.float64(0.0195)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)