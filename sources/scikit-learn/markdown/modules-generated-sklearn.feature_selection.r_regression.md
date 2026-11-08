[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_selection.r_regression.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_selection.r_regression.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_selection.r_regression.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_selection.r_regression.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_selection.r_regression.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_selection.r_regression.html)

Collapse Sidebar Expand Sidebar

r\_regression[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html#r-regression "Link to this heading")

====================================================================================================================================================

sklearn.feature\_selection.r\_regression(_X_, _y_, _\*_, _center\=True_, _force\_finite\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_univariate_selection.py#L292)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html#sklearn.feature_selection.r_regression "Link to this definition")

Compute Pearson’s r for each features and the target.

Pearson’s r is also known as the Pearson correlation coefficient.

Linear model for testing the individual effect of each of many regressors. This is a scoring function to be used in a feature selection procedure, not a free standing feature selection procedure.

The cross correlation between each regressor and the target is computed as:

E\[(X\[:, i\] \- mean(X\[:, i\])) \* (y \- mean(y))\] / (std(X\[:, i\]) \* std(y))

Copy to clipboard

For more on usage see the [User Guide](https://scikit-learn.org/stable/modules/feature_selection.html#univariate-feature-selection)
.

Added in version 1.0.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data matrix.

**y**array-like of shape (n\_samples,)

The target vector.

**center**bool, default=True

Whether or not to center the data matrix `X` and the target vector `y`. By default, `X` and `y` will be centered.

**force\_finite**bool, default=True

Whether or not to force the Pearson’s R correlation to be finite. In the particular case where some features in `X` or the target `y` are constant, the Pearson’s R correlation is not defined. When `force_finite=False`, a correlation of `np.nan` is returned to acknowledge this case. When `force_finite=True`, this value will be forced to a minimal correlation of `0.0`.

Added in version 1.1.

Returns:

**correlation\_coefficient**ndarray of shape (n\_features,)

Pearson’s R correlation coefficients of features.

See also

[`f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")

Univariate linear regression tests returning f-statistic and p-values.

[`mutual_info_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html#sklearn.feature_selection.mutual_info_regression "sklearn.feature_selection.mutual_info_regression")

Mutual information for a continuous target.

[`f_classif`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif "sklearn.feature_selection.f_classif")

ANOVA F-value between label/feature for classification tasks.

[`chi2`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2 "sklearn.feature_selection.chi2")

Chi-squared stats of non-negative features for classification tasks.

Examples

\>>> from sklearn.datasets import make\_regression
\>>> from sklearn.feature\_selection import r\_regression
\>>> X, y \= make\_regression(
...     n\_samples\=50, n\_features\=3, n\_informative\=1, noise\=1e-4, random\_state\=42
... )
\>>> r\_regression(X, y)
array(\[-0.157,  1.        , -0.229\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)