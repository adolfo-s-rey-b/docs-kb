[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.covariance.ledoit_wolf.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.covariance.ledoit_wolf.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.covariance.ledoit_wolf.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.covariance.ledoit_wolf.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.covariance.ledoit_wolf.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.covariance.ledoit_wolf.html)

Collapse Sidebar Expand Sidebar

ledoit\_wolf[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf.html#ledoit-wolf "Link to this heading")

==========================================================================================================================================

sklearn.covariance.ledoit\_wolf(_X_, _\*_, _assume\_centered\=False_, _block\_size\=1000_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_shrunk_covariance.py#L403)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf.html#sklearn.covariance.ledoit_wolf "Link to this definition")

Estimate the shrunk Ledoit-Wolf covariance matrix.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/covariance.html#shrunk-covariance)
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Data from which to compute the covariance estimate.

**assume\_centered**bool, default=False

If True, data will not be centered before computation. Useful to work with data whose mean is significantly equal to zero but is not exactly zero. If False, data will be centered before computation.

**block\_size**int, default=1000

Size of blocks into which the covariance matrix will be split. This is purely a memory optimization and does not affect results.

Returns:

**shrunk\_cov**ndarray of shape (n\_features, n\_features)

Shrunk covariance.

**shrinkage**float

Coefficient in the convex combination used for the computation of the shrunk estimate.

Notes

The regularized (shrunk) covariance is:

(1 - shrinkage) \* cov + shrinkage \* mu \* np.identity(n\_features)

where mu = trace(cov) / n\_features

Examples

\>>> import numpy as np
\>>> from sklearn.covariance import empirical\_covariance, ledoit\_wolf
\>>> real\_cov \= np.array(\[\[.4, .2\], \[.2, .8\]\])
\>>> rng \= np.random.RandomState(0)
\>>> X \= rng.multivariate\_normal(mean\=\[0, 0\], cov\=real\_cov, size\=50)
\>>> covariance, shrinkage \= ledoit\_wolf(X)
\>>> covariance
array(\[\[0.44, 0.16\],\
       \[0.16, 0.80\]\])
\>>> shrinkage
np.float64(0.23)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_cov_thumb.png)

[Sparse inverse covariance estimation](https://scikit-learn.org/stable/auto_examples/covariance/plot_sparse_cov.html)

Sparse inverse covariance estimation

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)