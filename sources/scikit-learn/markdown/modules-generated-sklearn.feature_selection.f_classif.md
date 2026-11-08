[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_selection.f_classif.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_selection.f_classif.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_selection.f_classif.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_selection.f_classif.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_selection.f_classif.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_selection.f_classif.html)

Collapse Sidebar Expand Sidebar

f\_classif[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#f-classif "Link to this heading")

===========================================================================================================================================

sklearn.feature\_selection.f\_classif(_X_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_selection/_univariate_selection.py#L118)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif "Link to this definition")

Compute the ANOVA F-value for the provided sample.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_selection.html#univariate-feature-selection)
.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The set of regressors that will be tested sequentially.

**y**array-like of shape (n\_samples,)

The target vector.

Returns:

**f\_statistic**ndarray of shape (n\_features,)

F-statistic for each feature.

**p\_values**ndarray of shape (n\_features,)

P-values associated with the F-statistic.

See also

[`chi2`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2 "sklearn.feature_selection.chi2")

Chi-squared stats of non-negative features for classification tasks.

[`f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")

F-value between label/feature for regression tasks.

Examples

\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.feature\_selection import f\_classif
\>>> X, y \= make\_classification(
...     n\_samples\=100, n\_features\=10, n\_informative\=2, n\_clusters\_per\_class\=1,
...     shuffle\=False, random\_state\=42
... )
\>>> f\_statistic, p\_values \= f\_classif(X, y)
\>>> f\_statistic
array(\[2.21e+02, 7.02e-01, 1.70e+00, 9.31e-01,\
       5.41e+00, 3.25e-01, 4.71e-02, 5.72e-01,\
       7.54e-01, 8.90e-02\])
\>>> p\_values
array(\[7.14e-27, 4.04e-01, 1.96e-01, 3.37e-01,\
       2.21e-02, 5.70e-01, 8.29e-01, 4.51e-01,\
       3.87e-01, 7.66e-01\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_thumb.png)

[Univariate Feature Selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html)

Univariate Feature Selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_pipeline_thumb.png)

[Pipeline ANOVA SVM](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection_pipeline.html)

Pipeline ANOVA SVM

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_anova_thumb.png)

[SVM-Anova: SVM with univariate feature selection](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html)

SVM-Anova: SVM with univariate feature selection

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)