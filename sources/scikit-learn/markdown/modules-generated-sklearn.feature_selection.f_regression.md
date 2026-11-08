[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_selection.f_regression.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_selection.f_regression.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_selection.f_regression.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_selection.f_regression.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_selection.f_regression.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_selection.f_regression.html)

Collapse Sidebar Expand Sidebar

f\_regression[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#f-regression "Link to this heading")

====================================================================================================================================================

sklearn.feature\_selection.f\_regression(_X_, _y_, _\*_, _center\=True_, _force\_finite\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_univariate_selection.py#L397)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "Link to this definition")

Univariate linear regression tests returning F-statistic and p-values.

Quick linear model for testing the effect of a single regressor, sequentially for many regressors.

This is done in 2 steps:

1.  The cross correlation between each regressor and the target is computed using [`r_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html#sklearn.feature_selection.r_regression "sklearn.feature_selection.r_regression")
     as:
    
    E\[(X\[:, i\] \- mean(X\[:, i\])) \* (y \- mean(y))\] / (std(X\[:, i\]) \* std(y))
    
    Copy to clipboard
    
2.  It is converted to an F score and then to a p-value.
    

[`f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")
 is derived from [`r_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html#sklearn.feature_selection.r_regression "sklearn.feature_selection.r_regression")
 and will rank features in the same order if all the features are positively correlated with the target.

Note however that contrary to [`f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")
, [`r_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html#sklearn.feature_selection.r_regression "sklearn.feature_selection.r_regression")
 values lie in \[-1, 1\] and can thus be negative. [`f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")
 is therefore recommended as a feature selection criterion to identify potentially predictive feature for a downstream classifier, irrespective of the sign of the association with the target variable.

Furthermore [`f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")
 returns p-values while [`r_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html#sklearn.feature_selection.r_regression "sklearn.feature_selection.r_regression")
 does not.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_selection.html#univariate-feature-selection)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data matrix.

**y**array-like of shape (n\_samples,)

The target vector.

**center**bool, default=True

Whether or not to center the data matrix `X` and the target vector `y`. By default, `X` and `y` will be centered.

**force\_finite**bool, default=True

Whether or not to force the F-statistics and associated p-values to be finite. There are two cases where the F-statistic is expected to not be finite:

*   when the target `y` or some features in `X` are constant. In this case, the Pearson’s R correlation is not defined leading to obtain `np.nan` values in the F-statistic and p-value. When `force_finite=True`, the F-statistic is set to `0.0` and the associated p-value is set to `1.0`.
    
*   when a feature in `X` is perfectly correlated (or anti-correlated) with the target `y`. In this case, the F-statistic is expected to be `np.inf`. When `force_finite=True`, the F-statistic is set to `np.finfo(dtype).max` and the associated p-value is set to `0.0`.
    

Added in version 1.1.

Returns:

**f\_statistic**ndarray of shape (n\_features,)

F-statistic for each feature.

**p\_values**ndarray of shape (n\_features,)

P-values associated with the F-statistic.

See also

[`r_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html#sklearn.feature_selection.r_regression "sklearn.feature_selection.r_regression")

Pearson’s R between label/feature for regression tasks.

[`f_classif`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif "sklearn.feature_selection.f_classif")

ANOVA F-value between label/feature for classification tasks.

[`chi2`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2 "sklearn.feature_selection.chi2")

Chi-squared stats of non-negative features for classification tasks.

[`SelectKBest`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")

Select features based on the k highest scores.

[`SelectFpr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFpr.html#sklearn.feature_selection.SelectFpr "sklearn.feature_selection.SelectFpr")

Select features based on a false positive rate test.

[`SelectFdr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFdr.html#sklearn.feature_selection.SelectFdr "sklearn.feature_selection.SelectFdr")

Select features based on an estimated false discovery rate.

[`SelectFwe`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFwe.html#sklearn.feature_selection.SelectFwe "sklearn.feature_selection.SelectFwe")

Select features based on family-wise error rate.

[`SelectPercentile`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile")

Select features based on percentile of the highest scores.

Examples

\>>> from sklearn.datasets import make\_regression
\>>> from sklearn.feature\_selection import f\_regression
\>>> X, y \= make\_regression(
...     n\_samples\=50, n\_features\=3, n\_informative\=1, noise\=1e-4, random\_state\=42
... )
\>>> f\_statistic, p\_values \= f\_regression(X, y)
\>>> f\_statistic
array(\[1.21, 2.67e13, 2.66\])
\>>> p\_values
array(\[0.276, 1.54e-283, 0.11\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_agglomeration_vs_univariate_selection_thumb.png)

[Feature agglomeration vs. univariate selection](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)

Feature agglomeration vs. univariate selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_f_test_vs_mi_thumb.png)

[Comparison of F-test and mutual information](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_f_test_vs_mi.html)

Comparison of F-test and mutual information

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)