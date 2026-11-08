[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.empirical_covariance.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.covariance.empirical_covariance.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.empirical_covariance.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.covariance.empirical_covariance.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.covariance.empirical_covariance.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.covariance.empirical_covariance.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.covariance.empirical_covariance.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.covariance.empirical_covariance.html)

Collapse Sidebar Expand Sidebar

empirical\_covariance[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.empirical_covariance.html#empirical-covariance "Link to this heading")

=====================================================================================================================================================================

sklearn.covariance.empirical\_covariance(_X_, _\*_, _assume\_centered\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/covariance/_empirical_covariance.py#L58)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.empirical_covariance.html#sklearn.covariance.empirical_covariance "Link to this definition")

Compute the Maximum likelihood covariance estimator.

Parameters:

**X**ndarray of shape (n\_samples, n\_features)

Data from which to compute the covariance estimate.

**assume\_centered**bool, default=False

If `True`, data will not be centered before computation. Useful when working with data whose mean is almost, but not exactly zero. If `False`, data will be centered before computation.

Returns:

**covariance**ndarray of shape (n\_features, n\_features)

Empirical covariance (Maximum Likelihood Estimator).

Examples

\>>> from sklearn.covariance import empirical\_covariance
\>>> X \= \[\[1,1,1\],\[1,1,1\],\[1,1,1\],\
...      \[0,0,0\],\[0,0,0\],\[0,0,0\]\]
\>>> empirical\_covariance(X)
array(\[\[0.25, 0.25, 0.25\],\
       \[0.25, 0.25, 0.25\],\
       \[0.25, 0.25, 0.25\]\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.empirical_covariance.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_covariance_estimation_thumb.png)

[Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html)

Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)