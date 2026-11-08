[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_selection.chi2.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_selection.chi2.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_selection.chi2.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_selection.chi2.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_selection.chi2.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_selection.chi2.html)

Collapse Sidebar Expand Sidebar

chi2[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#chi2 "Link to this heading")

===========================================================================================================================

sklearn.feature\_selection.chi2(_X_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_univariate_selection.py#L193)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2 "Link to this definition")

Compute chi-squared stats between each non-negative feature and class.

This score can be used to select the `n_features` features with the highest values for the test chi-squared statistic from X, which must contain only **non-negative integer feature values** such as booleans or frequencies (e.g., term counts in document classification), relative to the classes.

If some of your features are continuous, you need to bin them, for example by using [`KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
.

Recall that the chi-square test measures dependence between stochastic variables, so using this function “weeds out” the features that are the most likely to be independent of class and therefore irrelevant for classification.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_selection.html#univariate-feature-selection)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Sample vectors.

**y**array-like of shape (n\_samples,)

Target vector (class labels).

Returns:

**chi2**ndarray of shape (n\_features,)

Chi2 statistics for each feature.

**p\_values**ndarray of shape (n\_features,)

P-values for each feature.

See also

[`f_classif`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif "sklearn.feature_selection.f_classif")

ANOVA F-value between label/feature for classification tasks.

[`f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")

F-value between label/feature for regression tasks.

Notes

Complexity of this algorithm is O(n\_classes \* n\_features).

Examples

\>>> import numpy as np
\>>> from sklearn.feature\_selection import chi2
\>>> X \= np.array(\[\[1, 1, 3\],\
...               \[0, 1, 5\],\
...               \[5, 4, 1\],\
...               \[6, 6, 2\],\
...               \[1, 4, 0\],\
...               \[0, 0, 0\]\])
\>>> y \= np.array(\[1, 1, 0, 0, 2, 2\])
\>>> chi2\_stats, p\_values \= chi2(X, y)
\>>> chi2\_stats
array(\[15.3,  6.5       ,  8.9\])
\>>> p\_values
array(\[0.000456, 0.0387, 0.0116 \])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_mixed_types_thumb.png)

[Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)

Column Transformer with Mixed Types

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)