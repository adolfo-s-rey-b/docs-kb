[Skip to main content](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.feature_selection.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.feature_selection.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.feature_selection.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.feature_selection.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.feature_selection.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.feature_selection.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.feature_selection.html)

Collapse Sidebar Expand Sidebar

sklearn.feature\_selection[#](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "Link to this heading")

==========================================================================================================================================================

Feature selection algorithms.

These include univariate filter selection methods and the recursive feature elimination algorithm.

**User guide.** See the [Feature selection](https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection)
 section for further details.

|     |     |
| --- | --- |
| [`GenericUnivariateSelect`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect "sklearn.feature_selection.GenericUnivariateSelect") | Univariate feature selector with configurable strategy. |
| [`RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE") | Feature ranking with recursive feature elimination. |
| [`RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV") | Recursive feature elimination with cross-validation to select features. |
| [`SelectFdr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFdr.html#sklearn.feature_selection.SelectFdr "sklearn.feature_selection.SelectFdr") | Filter: Select the p-values for an estimated false discovery rate. |
| [`SelectFpr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFpr.html#sklearn.feature_selection.SelectFpr "sklearn.feature_selection.SelectFpr") | Filter: Select the pvalues below alpha based on a FPR test. |
| [`SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel") | Meta-transformer for selecting features based on importance weights. |
| [`SelectFwe`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFwe.html#sklearn.feature_selection.SelectFwe "sklearn.feature_selection.SelectFwe") | Filter: Select the p-values corresponding to Family-wise error rate. |
| [`SelectKBest`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest") | Select features according to the k highest scores. |
| [`SelectPercentile`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile") | Select features according to a percentile of the highest scores. |
| [`SelectorMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html#sklearn.feature_selection.SelectorMixin "sklearn.feature_selection.SelectorMixin") | Transformer mixin that performs feature selection given a support mask. |
| [`SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector") | Transformer that performs Sequential Feature Selection. |
| [`VarianceThreshold`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html#sklearn.feature_selection.VarianceThreshold "sklearn.feature_selection.VarianceThreshold") | Feature selector that removes all low-variance features. |
| [`chi2`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2 "sklearn.feature_selection.chi2") | Compute chi-squared stats between each non-negative feature and class. |
| [`f_classif`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif "sklearn.feature_selection.f_classif") | Compute the ANOVA F-value for the provided sample. |
| [`f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression") | Univariate linear regression tests returning F-statistic and p-values. |
| [`mutual_info_classif`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#sklearn.feature_selection.mutual_info_classif "sklearn.feature_selection.mutual_info_classif") | Estimate mutual information for a discrete target variable. |
| [`mutual_info_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html#sklearn.feature_selection.mutual_info_regression "sklearn.feature_selection.mutual_info_regression") | Estimate mutual information for a continuous target variable. |
| [`r_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html#sklearn.feature_selection.r_regression "sklearn.feature_selection.r_regression") | Compute Pearson's r for each features and the target. |