[Skip to main content](https://scikit-learn.org/stable/whats_new/v0.22.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v0.22.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v0.22.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v0.22.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v0.22.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v0.22.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v0.22.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v0.22.html)

Collapse Sidebar Expand Sidebar

Version 0.22[#](https://scikit-learn.org/stable/whats_new/v0.22.html#version-0-22 "Link to this heading")

==========================================================================================================

For a short description of the main highlights of the release, please refer to [Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html#sphx-glr-auto-examples-release-highlights-plot-release-highlights-0-22-0-py)
.

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 0.22.2.post1[#](https://scikit-learn.org/stable/whats_new/v0.22.html#version-0-22-2-post1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

**March 3 2020**

The 0.22.2.post1 release includes a packaging fix for the source distribution but the content of the packages is otherwise identical to the content of the wheels with the 0.22.2 version (without the .post1 suffix). Both contain the following changes.

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.22.html#changelog "Link to this heading")

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-impute "Link to this heading")

*   Efficiency Reduce [`impute.KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
     asymptotic memory usage by chunking pairwise distance computation. [#16397](https://github.com/scikit-learn/scikit-learn/pull/16397)
     by [Joel Nothman](https://joelnothman.com/)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-metrics "Link to this heading")

*   Fix Fixed a bug in `metrics.plot_roc_curve` where the name of the estimator was passed in the [`metrics.RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")
     instead of the parameter `name`. It results in a different plot when calling [`metrics.RocCurveDisplay.plot`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.plot "sklearn.metrics.RocCurveDisplay.plot")
     for the subsequent times. [#16500](https://github.com/scikit-learn/scikit-learn/pull/16500)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Fixed a bug in `metrics.plot_precision_recall_curve` where the name of the estimator was passed in the [`metrics.PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")
     instead of the parameter `name`. It results in a different plot when calling [`metrics.PrecisionRecallDisplay.plot`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.plot "sklearn.metrics.PrecisionRecallDisplay.plot")
     for the subsequent times. [#16505](https://github.com/scikit-learn/scikit-learn/pull/16505)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-neighbors "Link to this heading")

*   Fix Fix a bug which converted a list of arrays into a 2-D object array instead of a 1-D array containing NumPy arrays. This bug was affecting [`neighbors.NearestNeighbors.radius_neighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.radius_neighbors "sklearn.neighbors.NearestNeighbors.radius_neighbors")
    . [#16076](https://github.com/scikit-learn/scikit-learn/pull/16076)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
     and [Alex Shacked](https://github.com/alexshacked)
    .
    

Version 0.22.1[#](https://scikit-learn.org/stable/whats_new/v0.22.html#version-0-22-1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**January 2 2020**

This is a bug-fix release to primarily resolve some packaging issues in version 0.22.0. It also includes minor documentation improvements and some bug fixes.

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.22.html#id1 "Link to this heading")

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-cluster "Link to this heading")

*   Fix [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     with `algorithm="elkan"` now uses the same stopping criterion as with the default `algorithm="full"`. [#15930](https://github.com/scikit-learn/scikit-learn/pull/15930)
     by [@inder128](https://github.com/inder128)
    .
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-inspection "Link to this heading")

*   Fix [`inspection.permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
     will return the same `importances` when a `random_state` is given for both `n_jobs=1` or `n_jobs>1` both with shared memory backends (thread-safety) and isolated memory, process-based backends. Also avoid casting the data as object dtype and avoid read-only error on large dataframes with `n_jobs>1` as reported in [#15810](https://github.com/scikit-learn/scikit-learn/issues/15810)
    . Follow-up of [#15898](https://github.com/scikit-learn/scikit-learn/pull/15898)
     by [Shivam Gargsya](https://github.com/shivamgargsya)
    . [#15933](https://github.com/scikit-learn/scikit-learn/pull/15933)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
     and [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Fix `inspection.plot_partial_dependence` and [`inspection.PartialDependenceDisplay.plot`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.plot "sklearn.inspection.PartialDependenceDisplay.plot")
     now consistently checks the number of axes passed in. [#15760](https://github.com/scikit-learn/scikit-learn/pull/15760)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#id2 "Link to this heading")

*   Fix `metrics.plot_confusion_matrix` now raises error when `normalize` is invalid. Previously, it runs fine with no normalization. [#15888](https://github.com/scikit-learn/scikit-learn/pull/15888)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   Fix `metrics.plot_confusion_matrix` now colors the label color correctly to maximize contrast with its background. [#15936](https://github.com/scikit-learn/scikit-learn/pull/15936)
     by [Thomas Fan](https://github.com/thomasjpfan)
     and [@DizietAsahi](https://github.com/DizietAsahi)
    .
    
*   Fix [`metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
     does no longer ignore the value of the `zero_division` keyword argument. [#15879](https://github.com/scikit-learn/scikit-learn/pull/15879)
     by [Bibhash Chandra Mitra](https://github.com/Bibyutatsu)
    .
    
*   Fix Fixed a bug in `metrics.plot_confusion_matrix` to correctly pass the `values_format` parameter to the [`metrics.ConfusionMatrixDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay "sklearn.metrics.ConfusionMatrixDisplay")
     plot() call. [#15937](https://github.com/scikit-learn/scikit-learn/pull/15937)
     by [Stephen Blystone](https://github.com/blynotes)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-model-selection "Link to this heading")

*   Fix [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     accept scalar values provided in `fit_params`. Change in 0.22 was breaking backward compatibility. [#15863](https://github.com/scikit-learn/scikit-learn/pull/15863)
     by [Adrin Jalali](https://github.com/adrinjalali)
     and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.naive_bayes`](https://scikit-learn.org/stable/api/sklearn.naive_bayes.html#module-sklearn.naive_bayes "sklearn.naive_bayes")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-naive-bayes "Link to this heading")

*   Fix Removed `abstractmethod` decorator for the method `_check_X` in `naive_bayes.BaseNB` that could break downstream projects inheriting from this deprecated public base class. [#15996](https://github.com/scikit-learn/scikit-learn/pull/15996)
     by [Brigitta Sipőcz](https://github.com/bsipocz)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-preprocessing "Link to this heading")

*   Fix [`preprocessing.QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
     now guarantees the `quantiles_` attribute to be completely sorted in non-decreasing manner. [#15751](https://github.com/scikit-learn/scikit-learn/pull/15751)
     by [Tirth Patel](https://github.com/tirthasheshpatel)
    .
    

#### [`sklearn.semi_supervised`](https://scikit-learn.org/stable/api/sklearn.semi_supervised.html#module-sklearn.semi_supervised "sklearn.semi_supervised")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-semi-supervised "Link to this heading")

*   Fix [`semi_supervised.LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")
     and [`semi_supervised.LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
     now allow callable kernel function to return sparse weight matrix. [#15868](https://github.com/scikit-learn/scikit-learn/pull/15868)
     by [Niklas Smedemark-Margulies](https://github.com/nik-sm)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-utils "Link to this heading")

*   Fix [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     now correctly converts pandas DataFrame with boolean columns to floats. [#15797](https://github.com/scikit-learn/scikit-learn/pull/15797)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`utils.validation.check_is_fitted`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
     accepts back an explicit `attributes` argument to check for specific attributes as explicit markers of a fitted estimator. When no explicit `attributes` are provided, only the attributes that end with an underscore and do not start with double underscore are used as “fitted” markers. The `all_or_any` argument is also no longer deprecated. This change is made to restore some backward compatibility with the behavior of this utility in version 0.21. [#15947](https://github.com/scikit-learn/scikit-learn/pull/15947)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

Version 0.22.0[#](https://scikit-learn.org/stable/whats_new/v0.22.html#version-0-22-0 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**December 3 2019**

### Website update[#](https://scikit-learn.org/stable/whats_new/v0.22.html#website-update "Link to this heading")

[Our website](https://scikit-learn.org/)
 was revamped and given a fresh new look. [#14849](https://github.com/scikit-learn/scikit-learn/pull/14849)
 by [Thomas Fan](https://github.com/thomasjpfan)
.

### Clear definition of the public API[#](https://scikit-learn.org/stable/whats_new/v0.22.html#clear-definition-of-the-public-api "Link to this heading")

Scikit-learn has a public API, and a private API.

We do our best not to break the public API, and to only introduce backward-compatible changes that do not require any user action. However, in cases where that’s not possible, any change to the public API is subject to a deprecation cycle of two minor versions. The private API isn’t publicly documented and isn’t subject to any deprecation cycle, so users should not rely on its stability.

A function or object is public if it is documented in the [API Reference](https://scikit-learn.org/dev/modules/classes.html)
 and if it can be imported with an import path without leading underscores. For example `sklearn.pipeline.make_pipeline` is public, while `sklearn.pipeline._name_estimators` is private. `sklearn.ensemble._gb.BaseEnsemble` is private too because the whole `_gb` module is private.

Up to 0.22, some tools were de-facto public (no leading underscore), while they should have been private in the first place. In version 0.22, these tools have been made properly private, and the public API space has been cleaned. In addition, importing from most sub-modules is now deprecated: you should for example use `from sklearn.cluster import Birch` instead of `from sklearn.cluster.birch import Birch` (in practice, `birch.py` has been moved to `_birch.py`).

Note

All the tools in the public API should be documented in the [API Reference](https://scikit-learn.org/dev/modules/classes.html)
. If you find a public tool (without leading underscore) that isn’t in the API reference, that means it should either be private or documented. Please let us know by opening an issue!

This work was tracked in [issue 9250](https://github.com/scikit-learn/scikit-learn/issues/9250)
 and [issue 12927](https://github.com/scikit-learn/scikit-learn/issues/12927)
.

### Deprecations: using `FutureWarning` from now on[#](https://scikit-learn.org/stable/whats_new/v0.22.html#deprecations-using-futurewarning-from-now-on "Link to this heading")

When deprecating a feature, previous versions of scikit-learn used to raise a `DeprecationWarning`. Since the `DeprecationWarnings` aren’t shown by default by Python, scikit-learn needed to resort to a custom warning filter to always show the warnings. That filter would sometimes interfere with users custom warning filters.

Starting from version 0.22, scikit-learn will show `FutureWarnings` for deprecations, [as recommended by the Python documentation](https://docs.python.org/3/library/exceptions.html#FutureWarning)
. `FutureWarnings` are always shown by default by Python, so the custom filter has been removed and scikit-learn no longer hinders with user filters. [#15080](https://github.com/scikit-learn/scikit-learn/pull/15080)
 by [Nicolas Hug](https://github.com/NicolasHug)
.

### Changed models[#](https://scikit-learn.org/stable/whats_new/v0.22.html#changed-models "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     when `n_jobs=1`. Fix
    
*   [`decomposition.SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")
    , [`decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
    , and [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
     Fix
    
*   [`decomposition.SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")
     with `algorithm='lasso_lars'` Fix
    
*   [`decomposition.SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")
     where `normalize_components` has no effect due to deprecation.
    
*   [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     Fix , Feature , Enhancement .
    
*   [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     when `X` has features with no missing values. Feature
    
*   [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     when `X` is sparse. Fix
    
*   [`model_selection.StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
     and any use of `cv=int` with a classifier. Fix
    
*   [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
     when using scipy >= 1.3 Fix
    

Details are listed in the changelog below.

(While we are trying to better inform users by providing this information, we cannot assure that this list is complete.)

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.22.html#id4 "Link to this heading")

#### [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-base "Link to this heading")

*   API Change From version 0.24 [`base.BaseEstimator.get_params`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator.get_params "sklearn.base.BaseEstimator.get_params")
     will raise an AttributeError rather than return None for parameters that are in the estimator’s constructor but not stored as attributes on the instance. [#14464](https://github.com/scikit-learn/scikit-learn/pull/14464)
     by [Joel Nothman](https://joelnothman.com/)
    .
    

#### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-calibration "Link to this heading")

*   Fix Fixed a bug that made [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     fail when given a `sample_weight` parameter of type `list` (in the case where `sample_weights` are not supported by the wrapped estimator). [#13575](https://github.com/scikit-learn/scikit-learn/pull/13575)
     by [William de Vazelhes](https://github.com/wdevazelhes)
    .
    

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#id5 "Link to this heading")

*   Feature [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     now accepts precomputed sparse neighbors graph as input. [#10482](https://github.com/scikit-learn/scikit-learn/issues/10482)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
     and [Kumar Ashutosh](https://github.com/thechargedneutron)
    .
    
*   Enhancement [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     now accepts a `n_components` parameter. This parameter extends `SpectralClustering` class functionality to match [`cluster.spectral_clustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")
    . [#13726](https://github.com/scikit-learn/scikit-learn/pull/13726)
     by [Shuzhe Xiao](https://github.com/fdas3213)
    .
    
*   Fix Fixed a bug where [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     produced inconsistent results between `n_jobs=1` and `n_jobs>1` due to the handling of the random state. [#9288](https://github.com/scikit-learn/scikit-learn/pull/9288)
     by [Bryan Yang](https://github.com/bryanyang0528)
    .
    
*   Fix Fixed a bug where `elkan` algorithm in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     was producing Segmentation Fault on large arrays due to integer index overflow. [#15057](https://github.com/scikit-learn/scikit-learn/pull/15057)
     by [Vladimir Korolev](https://github.com/balodja)
    .
    
*   Fix [`MeanShift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")
     now accepts a [max\_iter](https://scikit-learn.org/stable/glossary.html#term-max_iter)
     with a default value of 300 instead of always using the default 300. It also now exposes an `n_iter_` indicating the maximum number of iterations performed on each seed. [#15120](https://github.com/scikit-learn/scikit-learn/pull/15120)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Fix [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     and [`cluster.FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")
     now raise an error if `affinity='cosine'` and `X` has samples that are all-zeros. [#7943](https://github.com/scikit-learn/scikit-learn/pull/7943)
     by [@mthorrell](https://github.com/mthorrell)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-compose "Link to this heading")

*   Feature Adds [`compose.make_column_selector`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")
     which is used with [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     to select DataFrame columns on the basis of name and dtype. [#12303](https://github.com/scikit-learn/scikit-learn/pull/12303)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Fixed a bug in [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     which failed to select the proper columns when using a boolean list, with NumPy older than 1.12. [#14510](https://github.com/scikit-learn/scikit-learn/pull/14510)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Fixed a bug in [`compose.TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
     which did not pass `**fit_params` to the underlying regressor. [#14890](https://github.com/scikit-learn/scikit-learn/pull/14890)
     by [Miguel Cabrera](https://github.com/mfcabrera)
    .
    
*   Fix The [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     now requires the number of features to be consistent between `fit` and `transform`. A `FutureWarning` is raised now, and this will raise an error in 0.24. If the number of features isn’t consistent and negative indexing is used, an error is raised. [#14544](https://github.com/scikit-learn/scikit-learn/pull/14544)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.cross_decomposition`](https://scikit-learn.org/stable/api/sklearn.cross_decomposition.html#module-sklearn.cross_decomposition "sklearn.cross_decomposition")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-cross-decomposition "Link to this heading")

*   Feature [`cross_decomposition.PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
     and [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
     have a new function `inverse_transform` to transform data to the original space. [#15304](https://github.com/scikit-learn/scikit-learn/pull/15304)
     by [Jaime Ferrando Huertas](https://github.com/jiwidi)
    .
    
*   Enhancement [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
     now properly checks the eigenvalues found by the solver for numerical or conditioning issues. This ensures consistency of results across solvers (different choices for `eigen_solver`), including approximate solvers such as `'randomized'` and `'lobpcg'` (see [#12068](https://github.com/scikit-learn/scikit-learn/issues/12068)
    ). [#12145](https://github.com/scikit-learn/scikit-learn/pull/12145)
     by [Sylvain Marié](https://github.com/smarie)
    
*   Fix Fixed a bug where [`cross_decomposition.PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
     and [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
     were raising an error when fitted with a target matrix `Y` in which the first column was constant. [#13609](https://github.com/scikit-learn/scikit-learn/issues/13609)
     by [Camila Williamson](https://github.com/camilaagw)
    .
    
*   Fix [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
     now produces the same results with scipy 1.3 and previous scipy versions. [#15661](https://github.com/scikit-learn/scikit-learn/pull/15661)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-datasets "Link to this heading")

*   Feature [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     now supports heterogeneous data using pandas by setting `as_frame=True`. [#13902](https://github.com/scikit-learn/scikit-learn/pull/13902)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     now includes the `target_names` in the returned Bunch. [#15160](https://github.com/scikit-learn/scikit-learn/pull/15160)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement The parameter `return_X_y` was added to [`datasets.fetch_20newsgroups`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
     and [`datasets.fetch_olivetti_faces`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#sklearn.datasets.fetch_olivetti_faces "sklearn.datasets.fetch_olivetti_faces")
     . [#14259](https://github.com/scikit-learn/scikit-learn/pull/14259)
     by [Sourav Singh](https://github.com/souravsingh)
    .
    
*   Enhancement [`datasets.make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
     now accepts array-like `weights` parameter, i.e. list or numpy.array, instead of list only. [#14764](https://github.com/scikit-learn/scikit-learn/pull/14764)
     by [Cat Chenal](https://github.com/CatChenal)
    .
    
*   Enhancement The parameter `normalize` was added to
    
    [`datasets.fetch_20newsgroups_vectorized`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized")
    . [#14740](https://github.com/scikit-learn/scikit-learn/pull/14740)
     by [Stéphan Tulkens](https://github.com/stephantul)
    
*   Fix Fixed a bug in [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
    , which failed to load an OpenML dataset that contains an ignored feature. [#14623](https://github.com/scikit-learn/scikit-learn/pull/14623)
     by [Sarra Habchi](https://github.com/HabchiSarra)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-decomposition "Link to this heading")

*   Efficiency [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     with `solver="mu"` fitted on sparse input matrices now uses batching to avoid briefly allocating an array with size (#non-zero elements, n\_components). [#15257](https://github.com/scikit-learn/scikit-learn/pull/15257)
     by [Mart Willocx](https://github.com/Maocx)
    .
    
*   Enhancement [`decomposition.dict_learning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#sklearn.decomposition.dict_learning "sklearn.decomposition.dict_learning")
     and [`decomposition.dict_learning_online`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html#sklearn.decomposition.dict_learning_online "sklearn.decomposition.dict_learning_online")
     now accept `method_max_iter` and pass it to [`decomposition.sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")
    . [#12650](https://github.com/scikit-learn/scikit-learn/issues/12650)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Enhancement [`decomposition.SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")
    , [`decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
    , and [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
     now take a `transform_max_iter` parameter and pass it to either [`decomposition.dict_learning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#sklearn.decomposition.dict_learning "sklearn.decomposition.dict_learning")
     or [`decomposition.sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")
    . [#12650](https://github.com/scikit-learn/scikit-learn/issues/12650)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Enhancement [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
     now accepts sparse matrices as input, converting them to dense in batches thereby avoiding the need to store the entire dense matrix at once. [#13960](https://github.com/scikit-learn/scikit-learn/pull/13960)
     by [Scott Gigante](https://github.com/scottgigante)
    .
    
*   Fix [`decomposition.sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")
     now passes the `max_iter` to the underlying [`linear_model.LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")
     when `algorithm='lasso_lars'`. [#12650](https://github.com/scikit-learn/scikit-learn/issues/12650)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.dummy`](https://scikit-learn.org/stable/api/sklearn.dummy.html#module-sklearn.dummy "sklearn.dummy")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-dummy "Link to this heading")

*   Fix [`dummy.DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
     now handles checking the existence of the provided constant in multioutput cases. [#14908](https://github.com/scikit-learn/scikit-learn/pull/14908)
     by [Martina G. Vilas](https://github.com/martinagvilas)
    .
    
*   API Change The default value of the `strategy` parameter in [`dummy.DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
     will change from `'stratified'` in version 0.22 to `'prior'` in 0.24. A FutureWarning is raised when the default value is used. [#15382](https://github.com/scikit-learn/scikit-learn/pull/15382)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change The `outputs_2d_` attribute is deprecated in [`dummy.DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
     and [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
    . It is equivalent to `n_outputs > 1`. [#14933](https://github.com/scikit-learn/scikit-learn/pull/14933)
     by [Nicolas Hug](https://github.com/NicolasHug)
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-ensemble "Link to this heading")

*   Major Feature Added [`ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
     and [`ensemble.StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
     to stack predictors using a final classifier or regressor. [#11047](https://github.com/scikit-learn/scikit-learn/pull/11047)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
     and [Caio Oliveira](https://github.com/caioaao)
     and [#15138](https://github.com/scikit-learn/scikit-learn/pull/15138)
     by [Jon Cusick](https://github.com/jcusick13)
    ..
    
*   Major Feature Many improvements were made to [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
    :
    
    *   Feature Estimators now natively support dense data with missing values both for training and predicting. They also support infinite values. [#13911](https://github.com/scikit-learn/scikit-learn/pull/13911)
         and [#14406](https://github.com/scikit-learn/scikit-learn/pull/14406)
         by [Nicolas Hug](https://github.com/NicolasHug)
        , [Adrin Jalali](https://github.com/adrinjalali)
         and [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
        .
        
    *   Feature Estimators now have an additional `warm_start` parameter that enables warm starting. [#14012](https://github.com/scikit-learn/scikit-learn/pull/14012)
         by [Johann Faouzi](https://github.com/johannfaouzi)
        .
        
    *   Feature [`inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
         and `inspection.plot_partial_dependence` now support the fast ‘recursion’ method for both estimators. [#13769](https://github.com/scikit-learn/scikit-learn/pull/13769)
         by [Nicolas Hug](https://github.com/NicolasHug)
        .
        
    *   Enhancement for [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
         the training loss or score is now monitored on a class-wise stratified subsample to preserve the class balance of the original training set. [#14194](https://github.com/scikit-learn/scikit-learn/pull/14194)
         by [Johann Faouzi](https://github.com/johannfaouzi)
        .
        
    *   Enhancement [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
         now supports the ‘least\_absolute\_deviation’ loss. [#13896](https://github.com/scikit-learn/scikit-learn/pull/13896)
         by [Nicolas Hug](https://github.com/NicolasHug)
        .
        
    *   Fix Estimators now bin the training and validation data separately to avoid any data leak. [#13933](https://github.com/scikit-learn/scikit-learn/pull/13933)
         by [Nicolas Hug](https://github.com/NicolasHug)
        .
        
    *   Fix Fixed a bug where early stopping would break with string targets. [#14710](https://github.com/scikit-learn/scikit-learn/pull/14710)
         by [Guillaume Lemaitre](https://github.com/glemaitre)
        .
        
    *   Fix [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
         now raises an error if `categorical_crossentropy` loss is given for a binary classification problem. [#14869](https://github.com/scikit-learn/scikit-learn/pull/14869)
         by [Adrin Jalali](https://github.com/adrinjalali)
        .
        
    
    Note that pickles from 0.21 will not work in 0.22.
    
*   Enhancement Addition of `max_samples` argument allows limiting size of bootstrap samples to be less than size of dataset. Added to [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
    , [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
    . [#14682](https://github.com/scikit-learn/scikit-learn/pull/14682)
     by [Matt Hancock](https://github.com/notmatthancock)
     and [#5963](https://github.com/scikit-learn/scikit-learn/pull/5963)
     by [Pablo Duboue](https://github.com/DrDub)
    .
    
*   Fix [`ensemble.VotingClassifier.predict_proba`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.predict_proba "sklearn.ensemble.VotingClassifier.predict_proba")
     will no longer be present when `voting='hard'`. [#14287](https://github.com/scikit-learn/scikit-learn/pull/14287)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix The `named_estimators_` attribute in [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     and [`ensemble.VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
     now correctly maps to dropped estimators. Previously, the `named_estimators_` mapping was incorrect whenever one of the estimators was dropped. [#15375](https://github.com/scikit-learn/scikit-learn/pull/15375)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Run by default [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     on both [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     and [`ensemble.VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
    . It leads to solve issues regarding shape consistency during `predict` which was failing when the underlying estimators were not outputting consistent array dimensions. Note that it should be replaced by refactoring the common tests in the future. [#14305](https://github.com/scikit-learn/scikit-learn/pull/14305)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
     computes probabilities based on the decision function as in the literature. Thus, `predict` and `predict_proba` give consistent results. [#14114](https://github.com/scikit-learn/scikit-learn/pull/14114)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Stacking and Voting estimators now ensure that their underlying estimators are either all classifiers or all regressors. [`ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
    , [`ensemble.StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
    , and [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     and [`ensemble.VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
     now raise consistent error messages. [#15084](https://github.com/scikit-learn/scikit-learn/pull/15084)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`ensemble.AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
     where the loss should be normalized by the max of the samples with non-null weights only. [#14294](https://github.com/scikit-learn/scikit-learn/pull/14294)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change `presort` is now deprecated in [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
    , and the parameter has no effect. Users are recommended to use [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     instead. [#14907](https://github.com/scikit-learn/scikit-learn/pull/14907)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-feature-extraction "Link to this heading")

*   Enhancement A warning will now be raised if a parameter choice means that another parameter will be unused on calling the fit() method for [`feature_extraction.text.HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
    , [`feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     and [`feature_extraction.text.TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
    . [#14602](https://github.com/scikit-learn/scikit-learn/pull/14602)
     by [Gaurav Chawla](https://github.com/getgaurav2)
    .
    
*   Fix Functions created by `build_preprocessor` and `build_analyzer` of `feature_extraction.text.VectorizerMixin` can now be pickled. [#14430](https://github.com/scikit-learn/scikit-learn/pull/14430)
     by [Dillon Niederhut](https://github.com/deniederhut)
    .
    
*   Fix `feature_extraction.text.strip_accents_unicode` now correctly removes accents from strings that are in NFKD normalized form. [#15100](https://github.com/scikit-learn/scikit-learn/pull/15100)
     by [Daniel Grady](https://github.com/DGrady)
    .
    
*   Fix Fixed a bug that caused [`feature_extraction.DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
     to raise an `OverflowError` during the `transform` operation when producing a `scipy.sparse` matrix on large input data. [#15463](https://github.com/scikit-learn/scikit-learn/pull/15463)
     by [Norvan Sahiner](https://github.com/norvan)
    .
    
*   API Change Deprecated unused `copy` param for [`feature_extraction.text.TfidfVectorizer.transform`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.transform "sklearn.feature_extraction.text.TfidfVectorizer.transform")
     it will be removed in v0.24. [#14520](https://github.com/scikit-learn/scikit-learn/pull/14520)
     by [Guillem G. Subies](https://github.com/guillemgsubies)
    .
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-feature-selection "Link to this heading")

*   Enhancement Updated the following [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
     estimators to allow NaN/Inf values in `transform` and `fit`: [`feature_selection.RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
    , [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
    , [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
    , and [`feature_selection.VarianceThreshold`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html#sklearn.feature_selection.VarianceThreshold "sklearn.feature_selection.VarianceThreshold")
    . Note that if the underlying estimator of the feature selector does not allow NaN/Inf then it will still error, but the feature selectors themselves no longer enforce this restriction unnecessarily. [#11635](https://github.com/scikit-learn/scikit-learn/issues/11635)
     by [Alec Peters](https://github.com/adpeters)
    .
    
*   Fix Fixed a bug where [`feature_selection.VarianceThreshold`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html#sklearn.feature_selection.VarianceThreshold "sklearn.feature_selection.VarianceThreshold")
     with `threshold=0` did not remove constant features due to numerical instability, by using range rather than variance in this case. [#13704](https://github.com/scikit-learn/scikit-learn/pull/13704)
     by [Roddy MacSween](https://github.com/rlms)
    .
    

#### [`sklearn.gaussian_process`](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#module-sklearn.gaussian_process "sklearn.gaussian_process")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-gaussian-process "Link to this heading")

*   Feature Gaussian process models on structured data: [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
     and [`gaussian_process.GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
     can now accept a list of generic objects (e.g. strings, trees, graphs, etc.) as the `X` argument to their training/prediction methods. A user-defined kernel should be provided for computing the kernel matrix among the generic objects, and should inherit from `gaussian_process.kernels.GenericKernelMixin` to notify the GPR/GPC model that it handles non-vectorial samples. [#15557](https://github.com/scikit-learn/scikit-learn/pull/15557)
     by [Yu-Hang Tang](https://github.com/yhtang)
    .
    
*   Efficiency [`gaussian_process.GaussianProcessClassifier.log_marginal_likelihood`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier.log_marginal_likelihood "sklearn.gaussian_process.GaussianProcessClassifier.log_marginal_likelihood")
     and [`gaussian_process.GaussianProcessRegressor.log_marginal_likelihood`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor.log_marginal_likelihood "sklearn.gaussian_process.GaussianProcessRegressor.log_marginal_likelihood")
     now accept a `clone_kernel=True` keyword argument. When set to `False`, the kernel attribute is modified, but may result in a performance improvement. [#14378](https://github.com/scikit-learn/scikit-learn/pull/14378)
     by [Masashi Shibata](https://github.com/c-bata)
    .
    
*   API Change From version 0.24 [`gaussian_process.kernels.Kernel.get_params`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Kernel.html#sklearn.gaussian_process.kernels.Kernel.get_params "sklearn.gaussian_process.kernels.Kernel.get_params")
     will raise an `AttributeError` rather than return `None` for parameters that are in the estimator’s constructor but not stored as attributes on the instance. [#14464](https://github.com/scikit-learn/scikit-learn/pull/14464)
     by [Joel Nothman](https://joelnothman.com/)
    .
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#id6 "Link to this heading")

*   Major Feature Added [`impute.KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
    , to impute missing values using k-Nearest Neighbors. [#12852](https://github.com/scikit-learn/scikit-learn/issues/12852)
     by [Ashim Bhattarai](https://github.com/ashimb9)
     and [Thomas Fan](https://github.com/thomasjpfan)
     and [#15010](https://github.com/scikit-learn/scikit-learn/pull/15010)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Feature [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     has new `skip_compute` flag that is False by default, which, when True, will skip computation on features that have no missing values during the fit phase. [#13773](https://github.com/scikit-learn/scikit-learn/issues/13773)
     by [Sergey Feldman](https://github.com/sergeyf)
    .
    
*   Efficiency [`impute.MissingIndicator.fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator.fit_transform "sklearn.impute.MissingIndicator.fit_transform")
     avoid repeated computation of the masked matrix. [#14356](https://github.com/scikit-learn/scikit-learn/pull/14356)
     by [Harsh Soni](https://github.com/harsh020)
    .
    
*   Fix [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     now works when there is only one feature. By [Sergey Feldman](https://github.com/sergeyf)
    .
    
*   Fix Fixed a bug in [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     where features were imputed in the reverse desired order with `imputation_order` either `"ascending"` or `"descending"`. [#15393](https://github.com/scikit-learn/scikit-learn/pull/15393)
     by [Venkatachalam N](https://github.com/venkyyuvy)
    .
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#id7 "Link to this heading")

*   Major Feature [`inspection.permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
     has been added to measure the importance of each feature in an arbitrary trained model with respect to a given scoring function. [#13146](https://github.com/scikit-learn/scikit-learn/issues/13146)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature [`inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
     and `inspection.plot_partial_dependence` now support the fast ‘recursion’ method for [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
    . [#13769](https://github.com/scikit-learn/scikit-learn/pull/13769)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Enhancement `inspection.plot_partial_dependence` has been extended to now support the new visualization API described in the [User Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
    . [#14646](https://github.com/scikit-learn/scikit-learn/pull/14646)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
     accepts pandas DataFrame and [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     containing [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
    . In addition `inspection.plot_partial_dependence` will use the column names by default when a dataframe is passed. [#14028](https://github.com/scikit-learn/scikit-learn/pull/14028)
     and [#15429](https://github.com/scikit-learn/scikit-learn/pull/15429)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.kernel_approximation`](https://scikit-learn.org/stable/api/sklearn.kernel_approximation.html#module-sklearn.kernel_approximation "sklearn.kernel_approximation")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-kernel-approximation "Link to this heading")

*   Fix Fixed a bug where [`kernel_approximation.Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
     raised a `KeyError` when using `kernel="precomputed"`. [#14706](https://github.com/scikit-learn/scikit-learn/pull/14706)
     by [Venkatachalam N](https://github.com/venkyyuvy)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-linear-model "Link to this heading")

*   Efficiency The ‘liblinear’ logistic regression solver is now faster and requires less memory. [#14108](https://github.com/scikit-learn/scikit-learn/pull/14108)
    , [#14170](https://github.com/scikit-learn/scikit-learn/pull/14170)
    , [#14296](https://github.com/scikit-learn/scikit-learn/pull/14296)
     by [Alex Henrie](https://github.com/alexhenrie)
    .
    
*   Enhancement [`linear_model.BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
     now accepts hyperparameters `alpha_init` and `lambda_init` which can be used to set the initial value of the maximization procedure in [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
    . [#13618](https://github.com/scikit-learn/scikit-learn/pull/13618)
     by [Yoshihiro Uchida](https://github.com/c56pony)
    .
    
*   Fix [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     now correctly fits an intercept when `X` is sparse, `solver="auto"` and `fit_intercept=True`, because the default solver in this configuration has changed to `sparse_cg`, which can fit an intercept with sparse data. [#13995](https://github.com/scikit-learn/scikit-learn/pull/13995)
     by [Jérôme Dockès](https://github.com/jeromedockes)
    .
    
*   Fix [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     with `solver='sag'` now accepts F-ordered and non-contiguous arrays and makes a conversion instead of failing. [#14458](https://github.com/scikit-learn/scikit-learn/pull/14458)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
     no longer forces `precompute=False` when fitting the final model. [#14591](https://github.com/scikit-learn/scikit-learn/pull/14591)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Fix [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     and [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
     now correctly scores when `cv=None`. [#14864](https://github.com/scikit-learn/scikit-learn/pull/14864)
     by [Venkatachalam N](https://github.com/venkyyuvy)
    .
    
*   Fix Fixed a bug in [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     where the `scores_`, `n_iter_` and `coefs_paths_` attribute would have a wrong ordering with `penalty='elastic-net'`. [#15044](https://github.com/scikit-learn/scikit-learn/pull/15044)
     by [Nicolas Hug](https://github.com/NicolasHug)
    
*   Fix [`linear_model.MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")
     and [`linear_model.MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")
     with X of dtype int and `fit_intercept=True`. [#15086](https://github.com/scikit-learn/scikit-learn/pull/15086)
     by [Alex Gramfort](https://github.com/agramfort)
    .
    
*   Fix The liblinear solver now supports `sample_weight`. [#15038](https://github.com/scikit-learn/scikit-learn/pull/15038)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-manifold "Link to this heading")

*   Feature [`manifold.Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
    , [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
    , and [`manifold.SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
     now accept precomputed sparse neighbors graph as input. [#10482](https://github.com/scikit-learn/scikit-learn/issues/10482)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
     and [Kumar Ashutosh](https://github.com/thechargedneutron)
    .
    
*   Feature Exposed the `n_jobs` parameter in [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     for multi-core calculation of the neighbors graph. This parameter has no impact when `metric="precomputed"` or (`metric="euclidean"` and `method="exact"`). [#15082](https://github.com/scikit-learn/scikit-learn/issues/15082)
     by [Roman Yurchak](https://github.com/rth)
    .
    
*   Efficiency Improved efficiency of [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     when `method="barnes-hut"` by computing the gradient in parallel. [#13213](https://github.com/scikit-learn/scikit-learn/pull/13213)
     by [Thomas Moreau](https://github.com/tommoral)
    
*   Fix Fixed a bug where [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
     (and therefore [`manifold.SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
     and [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
    ) computed wrong eigenvalues with `eigen_solver='amg'` when `n_samples < 5 * n_components`. [#14647](https://github.com/scikit-learn/scikit-learn/pull/14647)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Fix Fixed a bug in [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
     used in [`manifold.SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
     and [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     where `eigen_solver="amg"` would sometimes result in a LinAlgError. [#13393](https://github.com/scikit-learn/scikit-learn/issues/13393)
     by [Andrew Knyazev](https://github.com/lobpcg)
     [#13707](https://github.com/scikit-learn/scikit-learn/pull/13707)
     by [Scott White](https://github.com/whitews)
    
*   API Change Deprecate `training_data_` unused attribute in [`manifold.Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
    . [#10482](https://github.com/scikit-learn/scikit-learn/issues/10482)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#id8 "Link to this heading")

*   Major Feature `metrics.plot_roc_curve` has been added to plot roc curves. This function introduces the visualization API described in the [User Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
    . [#14357](https://github.com/scikit-learn/scikit-learn/pull/14357)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature Added a new parameter `zero_division` to multiple classification metrics: [`metrics.precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")
    , [`metrics.recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")
    , [`metrics.f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")
    , [`metrics.fbeta_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#sklearn.metrics.fbeta_score "sklearn.metrics.fbeta_score")
    , [`metrics.precision_recall_fscore_support`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "sklearn.metrics.precision_recall_fscore_support")
    , [`metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
    . This allows to set returned value for ill-defined metrics. [#14900](https://github.com/scikit-learn/scikit-learn/pull/14900)
     by [Marc Torrellas Socastro](https://github.com/marctorrellas)
    .
    
*   Feature Added the [`metrics.pairwise.nan_euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html#sklearn.metrics.pairwise.nan_euclidean_distances "sklearn.metrics.pairwise.nan_euclidean_distances")
     metric, which calculates euclidean distances in the presence of missing values. [#12852](https://github.com/scikit-learn/scikit-learn/issues/12852)
     by [Ashim Bhattarai](https://github.com/ashimb9)
     and [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature New ranking metrics [`metrics.ndcg_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html#sklearn.metrics.ndcg_score "sklearn.metrics.ndcg_score")
     and [`metrics.dcg_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.dcg_score.html#sklearn.metrics.dcg_score "sklearn.metrics.dcg_score")
     have been added to compute Discounted Cumulative Gain and Normalized Discounted Cumulative Gain. [#9951](https://github.com/scikit-learn/scikit-learn/pull/9951)
     by [Jérôme Dockès](https://github.com/jeromedockes)
    .
    
*   Feature `metrics.plot_precision_recall_curve` has been added to plot precision recall curves. [#14936](https://github.com/scikit-learn/scikit-learn/pull/14936)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature `metrics.plot_confusion_matrix` has been added to plot confusion matrices. [#15083](https://github.com/scikit-learn/scikit-learn/pull/15083)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature Added multiclass support to [`metrics.roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
     with corresponding scorers `'roc_auc_ovr'`, `'roc_auc_ovo'`, `'roc_auc_ovr_weighted'`, and `'roc_auc_ovo_weighted'`. [#12789](https://github.com/scikit-learn/scikit-learn/pull/12789)
     and [#15274](https://github.com/scikit-learn/scikit-learn/pull/15274)
     by [Kathy Chen](https://github.com/kathyxchen)
    , [Mohamed Maskani](https://github.com/maskani-moh)
    , and [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature Add [`metrics.mean_tweedie_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html#sklearn.metrics.mean_tweedie_deviance "sklearn.metrics.mean_tweedie_deviance")
     measuring the Tweedie deviance for a given `power` parameter. Also add mean Poisson deviance [`metrics.mean_poisson_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html#sklearn.metrics.mean_poisson_deviance "sklearn.metrics.mean_poisson_deviance")
     and mean Gamma deviance [`metrics.mean_gamma_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_gamma_deviance.html#sklearn.metrics.mean_gamma_deviance "sklearn.metrics.mean_gamma_deviance")
     that are special cases of the Tweedie deviance for `power=1` and `power=2` respectively. [#13938](https://github.com/scikit-learn/scikit-learn/pull/13938)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
     and [Roman Yurchak](https://github.com/rth)
    .
    
*   Efficiency Improved performance of [`metrics.pairwise.manhattan_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html#sklearn.metrics.pairwise.manhattan_distances "sklearn.metrics.pairwise.manhattan_distances")
     in the case of sparse matrices. [#15049](https://github.com/scikit-learn/scikit-learn/pull/15049)
     by `Paolo Toccaceli <ptocca>`.
    
*   Enhancement The parameter `beta` in [`metrics.fbeta_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#sklearn.metrics.fbeta_score "sklearn.metrics.fbeta_score")
     is updated to accept the zero and `float('+inf')` value. [#13231](https://github.com/scikit-learn/scikit-learn/pull/13231)
     by [Dong-hee Na](https://github.com/corona10)
    .
    
*   Enhancement Added parameter `squared` in [`metrics.mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
     to return root mean squared error. [#13467](https://github.com/scikit-learn/scikit-learn/pull/13467)
     by [Urvang Patel](https://github.com/urvang96)
    .
    
*   Enhancement Allow computing averaged metrics in the case of no true positives. [#14595](https://github.com/scikit-learn/scikit-learn/pull/14595)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Enhancement Multilabel metrics now supports list of lists as input. [#14865](https://github.com/scikit-learn/scikit-learn/pull/14865)
     [Srivatsan Ramesh](https://github.com/srivatsan-ramesh)
    , [Herilalaina Rakotoarison](https://github.com/herilalaina)
    , [Léonard Binet](https://github.com/leonardbinet)
    .
    
*   Enhancement [`metrics.median_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")
     now supports `multioutput` parameter. [#14732](https://github.com/scikit-learn/scikit-learn/pull/14732)
     by [Agamemnon Krasoulis](https://github.com/agamemnonc)
    .
    
*   Enhancement ‘roc\_auc\_ovr\_weighted’ and ‘roc\_auc\_ovo\_weighted’ can now be used as the [scoring](https://scikit-learn.org/stable/glossary.html#term-scoring)
     parameter of model-selection tools. [#14417](https://github.com/scikit-learn/scikit-learn/pull/14417)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
     accepts a parameters `normalize` allowing to normalize the confusion matrix by column, rows, or overall. [#15625](https://github.com/scikit-learn/scikit-learn/pull/15625)
     by `Guillaume Lemaitre <glemaitre>`.
    
*   Fix Raise a ValueError in [`metrics.silhouette_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")
     when a precomputed distance matrix contains non-zero diagonal entries. [#12258](https://github.com/scikit-learn/scikit-learn/pull/12258)
     by [Stephen Tierney](https://github.com/sjtrny)
    .
    
*   API Change `scoring="neg_brier_score"` should be used instead of `scoring="brier_score_loss"` which is now deprecated. [#14898](https://github.com/scikit-learn/scikit-learn/pull/14898)
     by [Stefan Matcovici](https://github.com/stefan-matcovici)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#id9 "Link to this heading")

*   Efficiency Improved performance of multimetric scoring in [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
    , [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    , and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
    . [#14593](https://github.com/scikit-learn/scikit-learn/pull/14593)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`model_selection.learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
     now accepts parameter `return_times` which can be used to retrieve computation times in order to plot model scalability (see learning\_curve example). [#13938](https://github.com/scikit-learn/scikit-learn/pull/13938)
     by [Hadrien Reboul](https://github.com/H4dr1en)
    .
    
*   Enhancement [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     now accepts lists of parameter distributions. [#14549](https://github.com/scikit-learn/scikit-learn/pull/14549)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Fix Reimplemented [`model_selection.StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
     to fix an issue where one test set could be `n_classes` larger than another. Test sets should now be near-equally sized. [#14704](https://github.com/scikit-learn/scikit-learn/pull/14704)
     by [Joel Nothman](https://joelnothman.com/)
    .
    
*   Fix The `cv_results_` attribute of [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     now only contains unfitted estimators. This potentially saves a lot of memory since the state of the estimators isn’t stored. [##15096](https://github.com/scikit-learn/scikit-learn/pull/#15096)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   API Change [`model_selection.KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
     and [`model_selection.StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
     now raise a warning if `random_state` is set but `shuffle` is False. This will raise an error in 0.24.
    

#### [`sklearn.multioutput`](https://scikit-learn.org/stable/api/sklearn.multioutput.html#module-sklearn.multioutput "sklearn.multioutput")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-multioutput "Link to this heading")

*   Fix [`multioutput.MultiOutputClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier")
     now has attribute `classes_`. [#14629](https://github.com/scikit-learn/scikit-learn/pull/14629)
     by [Agamemnon Krasoulis](https://github.com/agamemnonc)
    .
    
*   Fix [`multioutput.MultiOutputClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier")
     now has `predict_proba` as property and can be checked with `hasattr`. [#15488](https://github.com/scikit-learn/scikit-learn/issues/15488)
     [#15490](https://github.com/scikit-learn/scikit-learn/pull/15490)
     by [Rebekah Kim](https://github.com/rebekahkim)
    

#### [`sklearn.naive_bayes`](https://scikit-learn.org/stable/api/sklearn.naive_bayes.html#module-sklearn.naive_bayes "sklearn.naive_bayes")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#id10 "Link to this heading")

*   Major Feature Added [`naive_bayes.CategoricalNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html#sklearn.naive_bayes.CategoricalNB "sklearn.naive_bayes.CategoricalNB")
     that implements the Categorical Naive Bayes classifier. [#12569](https://github.com/scikit-learn/scikit-learn/pull/12569)
     by [Tim Bicker](https://github.com/timbicker)
     and [Florian Wilhelm](https://github.com/FlorianWilhelm)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#id11 "Link to this heading")

*   Major Feature Added [`neighbors.KNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
     and [`neighbors.RadiusNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer "sklearn.neighbors.RadiusNeighborsTransformer")
    , which transform input dataset into a sparse neighbors graph. They give finer control on nearest neighbors computations and enable easy pipeline caching for multiple use. [#10482](https://github.com/scikit-learn/scikit-learn/issues/10482)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Feature [`neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
    , [`neighbors.KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
    , [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
    , [`neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
    , and [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
     now accept precomputed sparse neighbors graph as input. [#10482](https://github.com/scikit-learn/scikit-learn/issues/10482)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
     and [Kumar Ashutosh](https://github.com/thechargedneutron)
    .
    
*   Feature [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
     now supports predicting probabilities by using `predict_proba` and supports more outlier\_label options: ‘most\_frequent’, or different outlier\_labels for multi-outputs. [#9597](https://github.com/scikit-learn/scikit-learn/pull/9597)
     by [Wenbo Zhao](https://github.com/webber26232)
    .
    
*   Efficiency Efficiency improvements for [`neighbors.RadiusNeighborsClassifier.predict`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.predict "sklearn.neighbors.RadiusNeighborsClassifier.predict")
    . [#9597](https://github.com/scikit-learn/scikit-learn/pull/9597)
     by [Wenbo Zhao](https://github.com/webber26232)
    .
    
*   Fix [`neighbors.KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
     now throws error when `metric='precomputed'` and fit on non-square data. [#14336](https://github.com/scikit-learn/scikit-learn/pull/14336)
     by [Gregory Dexter](https://github.com/gdex1)
    .
    

#### [`sklearn.neural_network`](https://scikit-learn.org/stable/api/sklearn.neural_network.html#module-sklearn.neural_network "sklearn.neural_network")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-neural-network "Link to this heading")

*   Feature Add `max_fun` parameter in `neural_network.BaseMultilayerPerceptron`, [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
    , and [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     to give control over maximum number of function evaluation to not meet `tol` improvement. [#9274](https://github.com/scikit-learn/scikit-learn/issues/9274)
     by [Daniel Perry](https://github.com/daniel-perry)
    .
    

#### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-pipeline "Link to this heading")

*   Enhancement [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     now supports [score\_samples](https://scikit-learn.org/stable/glossary.html#term-score_samples)
     if the final estimator does. [#13806](https://github.com/scikit-learn/scikit-learn/pull/13806)
     by [Anaël Beaugnon](https://github.com/ab-anssi)
    .
    
*   Fix The `fit` in [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     now accepts `fit_params` to pass to the underlying transformers. [#15119](https://github.com/scikit-learn/scikit-learn/pull/15119)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   API Change `None` as a transformer is now deprecated in [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
    . Please use `'drop'` instead. [#15053](https://github.com/scikit-learn/scikit-learn/pull/15053)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#id12 "Link to this heading")

*   Efficiency [`preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
     is now faster when the input data is dense. [#13290](https://github.com/scikit-learn/scikit-learn/pull/13290)
     by [Xavier Dupré](https://github.com/sdpython)
    .
    
*   Enhancement Avoid unnecessary data copy when fitting preprocessors [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
    , [`preprocessing.MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
    , [`preprocessing.MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")
    , [`preprocessing.RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
     and [`preprocessing.QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
     which results in a slight performance improvement. [#13987](https://github.com/scikit-learn/scikit-learn/pull/13987)
     by [Roman Yurchak](https://github.com/rth)
    .
    
*   Fix KernelCenterer now throws error when fit on non-square [`preprocessing.KernelCenterer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KernelCenterer.html#sklearn.preprocessing.KernelCenterer "sklearn.preprocessing.KernelCenterer")
     [#14336](https://github.com/scikit-learn/scikit-learn/pull/14336)
     by [Gregory Dexter](https://github.com/gdex1)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#id13 "Link to this heading")

*   Fix [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and `model_selection.RandomizedSearchCV` now supports the `_pairwise` property, which prevents an error during cross-validation for estimators with pairwise inputs (such as [`neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
     when [metric](https://scikit-learn.org/stable/glossary.html#term-metric)
     is set to ‘precomputed’). [#13925](https://github.com/scikit-learn/scikit-learn/pull/13925)
     by [Isaac S. Robson](https://github.com/isrobson)
     and [#15524](https://github.com/scikit-learn/scikit-learn/pull/15524)
     by [Xun Tang](https://github.com/xun-tang)
    .
    

#### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-svm "Link to this heading")

*   Enhancement [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     and [`svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
     now accept a `break_ties` parameter. This parameter results in [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
     breaking the ties according to the confidence values of [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
    , if `decision_function_shape='ovr'`, and the number of target classes > 2. [#12557](https://github.com/scikit-learn/scikit-learn/pull/12557)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Enhancement SVM estimators now throw a more specific error when `kernel='precomputed'` and fit on non-square data. [#14336](https://github.com/scikit-learn/scikit-learn/pull/14336)
     by [Gregory Dexter](https://github.com/gdex1)
    .
    
*   Fix [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
    , [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
    , [`svm.NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
     and [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
     when received values negative or zero for parameter `sample_weight` in method fit(), generated an invalid model. This behavior occurred only in some border scenarios. Now in these cases, fit() will fail with an Exception. [#14286](https://github.com/scikit-learn/scikit-learn/pull/14286)
     by [Alex Shacked](https://github.com/alexshacked)
    .
    
*   Fix The `n_support_` attribute of [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
     and [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
     was previously non-initialized, and had size 2. It has now size 1 with the correct value. [#15099](https://github.com/scikit-learn/scikit-learn/pull/15099)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix fixed a bug in `BaseLibSVM._sparse_fit` where n\_SV=0 raised a ZeroDivisionError. [#14894](https://github.com/scikit-learn/scikit-learn/pull/14894)
     by [Danna Naser](https://github.com/danna-naser)
    .
    
*   Fix The liblinear solver now supports `sample_weight`. [#15038](https://github.com/scikit-learn/scikit-learn/pull/15038)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-tree "Link to this heading")

*   Feature Adds minimal cost complexity pruning, controlled by `ccp_alpha`, to [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
    , [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
    , [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
    , [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
    , [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
    , and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
    . [#12887](https://github.com/scikit-learn/scikit-learn/pull/12887)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change `presort` is now deprecated in [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
     and [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , and the parameter has no effect. [#14907](https://github.com/scikit-learn/scikit-learn/pull/14907)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   API Change The `classes_` and `n_classes_` attributes of [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
     are now deprecated. [#15028](https://github.com/scikit-learn/scikit-learn/pull/15028)
     by [Mei Guan](https://github.com/meiguan)
    , [Nicolas Hug](https://github.com/NicolasHug)
    , and [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#id14 "Link to this heading")

*   Feature [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     can now generate checks by setting `generate_only=True`. Previously, running [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     will stop when the first check fails. With `generate_only=True`, all checks can run independently and report the ones that are failing. Read more in [Rolling your own estimator](https://scikit-learn.org/stable/developers/develop.html#rolling-your-own-estimator)
    . [#14381](https://github.com/scikit-learn/scikit-learn/pull/14381)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature Added a pytest specific decorator, [`parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks")
    , to parametrize estimator checks for a list of estimators. [#14381](https://github.com/scikit-learn/scikit-learn/pull/14381)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature A new random variable, `utils.fixes.loguniform` implements a log-uniform random variable (e.g., for use in RandomizedSearchCV). For example, the outcomes `1`, `10` and `100` are all equally likely for `loguniform(1, 100)`. See [#11232](https://github.com/scikit-learn/scikit-learn/issues/11232)
     by [Scott Sievert](https://github.com/stsievert)
     and [Nathaniel Saul](https://github.com/sauln)
    , and [SciPy PR 10815](https://github.com/scipy/scipy/pull/10815)
    .
    
*   Enhancement `utils.safe_indexing` (now deprecated) accepts an `axis` parameter to index array-like across rows and columns. The column indexing can be done on NumPy array, SciPy sparse matrix, and Pandas DataFrame. An additional refactoring was done. [#14035](https://github.com/scikit-learn/scikit-learn/pull/14035)
     and [#14475](https://github.com/scikit-learn/scikit-learn/pull/14475)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Enhancement [`utils.extmath.safe_sparse_dot`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html#sklearn.utils.extmath.safe_sparse_dot "sklearn.utils.extmath.safe_sparse_dot")
     works between 3D+ ndarray and sparse matrix. [#14538](https://github.com/scikit-learn/scikit-learn/pull/14538)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     is now raising an error instead of casting NaN to integer. [#14872](https://github.com/scikit-learn/scikit-learn/pull/14872)
     by [Roman Yurchak](https://github.com/rth)
    .
    
*   Fix [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     will now correctly detect numeric dtypes in pandas dataframes, fixing a bug where `float32` was upcast to `float64` unnecessarily. [#15094](https://github.com/scikit-learn/scikit-learn/pull/15094)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   API Change The following utils have been deprecated and are now private:
    
    *   `choose_check_classifiers_labels`
        
    *   `enforce_estimator_tags_y`
        
    *   `mocking.MockDataFrame`
        
    *   `mocking.CheckingClassifier`
        
    *   `optimize.newton_cg`
        
    *   `random.random_choice_csc`
        
    *   `utils.choose_check_classifiers_labels`
        
    *   `utils.enforce_estimator_tags_y`
        
    *   `utils.optimize.newton_cg`
        
    *   `utils.random.random_choice_csc`
        
    *   `utils.safe_indexing`
        
    *   `utils.mocking`
        
    *   `utils.fast_dict`
        
    *   `utils.seq_dataset`
        
    *   `utils.weight_vector`
        
    *   `utils.fixes.parallel_helper` (removed)
        
    *   All of `utils.testing` except for `all_estimators` which is now in `utils`.
        

#### [`sklearn.isotonic`](https://scikit-learn.org/stable/api/sklearn.isotonic.html#module-sklearn.isotonic "sklearn.isotonic")
[#](https://scikit-learn.org/stable/whats_new/v0.22.html#sklearn-isotonic "Link to this heading")

*   Fix Fixed a bug where [`isotonic.IsotonicRegression.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression.fit "sklearn.isotonic.IsotonicRegression.fit")
     raised error when `X.dtype == 'float32'` and `X.dtype != y.dtype`. [#14902](https://github.com/scikit-learn/scikit-learn/pull/14902)
     by [Lucas](https://github.com/lostcoaster)
    .
    

#### Miscellaneous[#](https://scikit-learn.org/stable/whats_new/v0.22.html#miscellaneous "Link to this heading")

*   Fix Port `lobpcg` from SciPy which implement some bug fixes but only available in 1.3+. [#13609](https://github.com/scikit-learn/scikit-learn/pull/13609)
     and [#14971](https://github.com/scikit-learn/scikit-learn/pull/14971)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change Scikit-learn now converts any input data structure implementing a duck array to a numpy array (using `__array__`) to ensure consistent behavior instead of relying on `__array_function__` (see [NEP 18](https://numpy.org/neps/nep-0018-array-function-protocol.html)
    ). [#14702](https://github.com/scikit-learn/scikit-learn/pull/14702)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   API Change Replace manual checks with `check_is_fitted`. Errors thrown when using a non-fitted estimators are now more uniform. [#13013](https://github.com/scikit-learn/scikit-learn/pull/13013)
     by [Agamemnon Krasoulis](https://github.com/agamemnonc)
    .
    

### Changes to estimator checks[#](https://scikit-learn.org/stable/whats_new/v0.22.html#changes-to-estimator-checks "Link to this heading")

These changes mostly affect library developers.

*   Estimators are now expected to raise a `NotFittedError` if `predict` or `transform` is called before `fit`; previously an `AttributeError` or `ValueError` was acceptable. [#13013](https://github.com/scikit-learn/scikit-learn/pull/13013)
     by by [Agamemnon Krasoulis](https://github.com/agamemnonc)
    .
    
*   Binary only classifiers are now supported in estimator checks. Such classifiers need to have the `binary_only=True` estimator tag. [#13875](https://github.com/scikit-learn/scikit-learn/pull/13875)
     by [Trevor Stephens](https://trevorstephens.com/)
    .
    
*   Estimators are expected to convert input data (`X`, `y`, `sample_weights`) to [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
     and never call `__array_function__` on the original datatype that is passed (see [NEP 18](https://numpy.org/neps/nep-0018-array-function-protocol.html)
    ). [#14702](https://github.com/scikit-learn/scikit-learn/pull/14702)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   `requires_positive_X` estimator tag (for models that require X to be non-negative) is now used by [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     to make sure a proper error message is raised if X contains some negative entries. [#14680](https://github.com/scikit-learn/scikit-learn/pull/14680)
     by [Alex Gramfort](https://github.com/agramfort)
    .
    
*   Added check that pairwise estimators raise error on non-square data [#14336](https://github.com/scikit-learn/scikit-learn/pull/14336)
     by [Gregory Dexter](https://github.com/gdex1)
    .
    
*   Added two common multioutput estimator tests `utils.estimator_checks.check_classifier_multioutput` and `utils.estimator_checks.check_regressor_multioutput`. [#13392](https://github.com/scikit-learn/scikit-learn/pull/13392)
     by [Rok Mihevc](https://github.com/rok)
    .
    
*   Fix Added `check_transformer_data_not_an_array` to checks where missing
    
*   Fix The estimators tags resolution now follows the regular MRO. They used to be overridable only once. [#14884](https://github.com/scikit-learn/scikit-learn/pull/14884)
     by [Andreas Müller](https://amueller.github.io/)
    .
    

Code and documentation contributors

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 0.21, including:

Aaron Alphonsus, Abbie Popa, Abdur-Rahmaan Janhangeer, abenbihi, Abhinav Sagar, Abhishek Jana, Abraham K. Lagat, Adam J. Stewart, Aditya Vyas, Adrin Jalali, Agamemnon Krasoulis, Alec Peters, Alessandro Surace, Alexandre de Siqueira, Alexandre Gramfort, alexgoryainov, Alex Henrie, Alex Itkes, alexshacked, Allen Akinkunle, Anaël Beaugnon, Anders Kaseorg, Andrea Maldonado, Andrea Navarrete, Andreas Mueller, Andreas Schuderer, Andrew Nystrom, Angela Ambroz, Anisha Keshavan, Ankit Jha, Antonio Gutierrez, Anuja Kelkar, Archana Alva, arnaudstiegler, arpanchowdhry, ashimb9, Ayomide Bamidele, Baran Buluttekin, barrycg, Bharat Raghunathan, Bill Mill, Biswadip Mandal, blackd0t, Brian G. Barkley, Brian Wignall, Bryan Yang, c56pony, camilaagw, cartman\_nabana, catajara, Cat Chenal, Cathy, cgsavard, Charles Vesteghem, Chiara Marmo, Chris Gregory, Christian Lorentzen, Christos Aridas, Dakota Grusak, Daniel Grady, Daniel Perry, Danna Naser, DatenBergwerk, David Dormagen, deeplook, Dillon Niederhut, Dong-hee Na, Dougal J. Sutherland, DrGFreeman, Dylan Cashman, edvardlindelof, Eric Larson, Eric Ndirangu, Eunseop Jeong, Fanny, federicopisanu, Felix Divo, flaviomorelli, FranciDona, Franco M. Luque, Frank Hoang, Frederic Haase, g0g0gadget, Gabriel Altay, Gabriel do Vale Rios, Gael Varoquaux, ganevgv, gdex1, getgaurav2, Gideon Sonoiya, Gordon Chen, gpapadok, Greg Mogavero, Grzegorz Szpak, Guillaume Lemaitre, Guillem García Subies, H4dr1en, hadshirt, Hailey Nguyen, Hanmin Qin, Hannah Bruce Macdonald, Harsh Mahajan, Harsh Soni, Honglu Zhang, Hossein Pourbozorg, Ian Sanders, Ingrid Spielman, J-A16, jaehong park, Jaime Ferrando Huertas, James Hill, James Myatt, Jay, jeremiedbb, Jérémie du Boisberranger, jeromedockes, Jesper Dramsch, Joan Massich, Joanna Zhang, Joel Nothman, Johann Faouzi, Jonathan Rahn, Jon Cusick, Jose Ortiz, Kanika Sabharwal, Katarina Slama, kellycarmody, Kennedy Kang’ethe, Kensuke Arai, Kesshi Jordan, Kevad, Kevin Loftis, Kevin Winata, Kevin Yu-Sheng Li, Kirill Dolmatov, Kirthi Shankar Sivamani, krishna katyal, Lakshmi Krishnan, Lakshya KD, LalliAcqua, lbfin, Leland McInnes, Léonard Binet, Loic Esteve, loopyme, lostcoaster, Louis Huynh, lrjball, Luca Ionescu, Lutz Roeder, MaggieChege, Maithreyi Venkatesh, Maltimore, Maocx, Marc Torrellas, Marie Douriez, Markus, Markus Frey, Martina G. Vilas, Martin Oywa, Martin Thoma, Masashi SHIBATA, Maxwell Aladago, mbillingr, m-clare, Meghann Agarwal, m.fab, Micah Smith, miguelbarao, Miguel Cabrera, Mina Naghshhnejad, Ming Li, motmoti, mschaffenroth, mthorrell, Natasha Borders, nezar-a, Nicolas Hug, Nidhin Pattaniyil, Nikita Titov, Nishan Singh Mann, Nitya Mandyam, norvan, notmatthancock, novaya, nxorable, Oleg Stikhin, Oleksandr Pavlyk, Olivier Grisel, Omar Saleem, Owen Flanagan, panpiort8, Paolo, Paolo Toccaceli, Paresh Mathur, Paula, Peng Yu, Peter Marko, pierretallotte, poorna-kumar, pspachtholz, qdeffense, Rajat Garg, Raphaël Bournhonesque, Ray, Ray Bell, Rebekah Kim, Reza Gharibi, Richard Payne, Richard W, rlms, Robert Juergens, Rok Mihevc, Roman Feldbauer, Roman Yurchak, R Sanjabi, RuchitaGarde, Ruth Waithera, Sackey, Sam Dixon, Samesh Lakhotia, Samuel Taylor, Sarra Habchi, Scott Gigante, Scott Sievert, Scott White, Sebastian Pölsterl, Sergey Feldman, SeWook Oh, she-dares, Shreya V, Shubham Mehta, Shuzhe Xiao, SimonCW, smarie, smujjiga, Sönke Behrends, Soumirai, Sourav Singh, stefan-matcovici, steinfurt, Stéphane Couvreur, Stephan Tulkens, Stephen Cowley, Stephen Tierney, SylvainLan, th0rwas, theoptips, theotheo, Thierno Ibrahima DIOP, Thomas Edwards, Thomas J Fan, Thomas Moreau, Thomas Schmitt, Tilen Kusterle, Tim Bicker, Timsaur, Tim Staley, Tirth Patel, Tola A, Tom Augspurger, Tom Dupré la Tour, topisan, Trevor Stephens, ttang131, Urvang Patel, Vathsala Achar, veerlosar, Venkatachalam N, Victor Luzgin, Vincent Jeanselme, Vincent Lostanlen, Vladimir Korolev, vnherdeiro, Wenbo Zhao, Wendy Hu, willdarnell, William de Vazelhes, wolframalpha, xavier dupré, xcjason, x-martian, xsat, xun-tang, Yinglr, yokasre, Yu-Hang “Maxin” Tang, Yulia Zamriy, Zhao Feng

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)