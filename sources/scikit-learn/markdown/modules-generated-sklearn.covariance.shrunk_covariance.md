[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.shrunk_covariance.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.covariance.shrunk_covariance.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.shrunk_covariance.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.covariance.shrunk_covariance.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.covariance.shrunk_covariance.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.covariance.shrunk_covariance.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.covariance.shrunk_covariance.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.covariance.shrunk_covariance.html)

Collapse Sidebar Expand Sidebar

shrunk\_covariance[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.shrunk_covariance.html#shrunk-covariance "Link to this heading")

============================================================================================================================================================

sklearn.covariance.shrunk\_covariance(_emp\_cov_, _shrinkage\=0.1_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_shrunk_covariance.py#L102)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.shrunk_covariance.html#sklearn.covariance.shrunk_covariance "Link to this definition")

Calculate covariance matrices shrunk on the diagonal.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/covariance.html#shrunk-covariance)
.

Parameters:

**emp\_cov**array-like of shape (…, n\_features, n\_features)

Covariance matrices to be shrunk, at least 2D ndarray.

**shrinkage**float, default=0.1

Coefficient in the convex combination used for the computation of the shrunk estimate. Range is \[0, 1\].

Returns:

**shrunk\_cov**ndarray of shape (…, n\_features, n\_features)

Shrunk covariance matrices.

Notes

The regularized (shrunk) covariance is given by:

(1 \- shrinkage) \* cov + shrinkage \* mu \* np.identity(n\_features)

Copy to clipboard

where `mu = trace(cov) / n_features`.

Examples

\>>> import numpy as np
\>>> from sklearn.datasets import make\_gaussian\_quantiles
\>>> from sklearn.covariance import empirical\_covariance, shrunk\_covariance
\>>> real\_cov \= np.array(\[\[.8, .3\], \[.3, .4\]\])
\>>> rng \= np.random.RandomState(0)
\>>> X \= rng.multivariate\_normal(mean\=\[0, 0\], cov\=real\_cov, size\=500)
\>>> shrunk\_covariance(empirical\_covariance(X))
array(\[\[0.739, 0.254\],\
       \[0.254, 0.411\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)