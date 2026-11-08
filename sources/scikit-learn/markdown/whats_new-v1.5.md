[Skip to main content](https://scikit-learn.org/stable/whats_new/v1.5.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v1.5.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v1.5.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v1.5.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v1.5.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v1.5.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v1.5.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v1.5.html)

Collapse Sidebar Expand Sidebar

Version 1.5[#](https://scikit-learn.org/stable/whats_new/v1.5.html#version-1-5 "Link to this heading")

=======================================================================================================

For a short description of the main highlights of the release, please refer to [Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html#sphx-glr-auto-examples-release-highlights-plot-release-highlights-1-5-0-py)
.

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 1.5.2[#](https://scikit-learn.org/stable/whats_new/v1.5.html#version-1-5-2 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**September 2024**

### Changes impacting many modules[#](https://scikit-learn.org/stable/whats_new/v1.5.html#changes-impacting-many-modules "Link to this heading")

*   Fix Fixed performance regression in a few Cython modules in `sklearn._loss`, `sklearn.manifold`, `sklearn.metrics` and `sklearn.utils`, which were built without OpenMP support. [#29694](https://github.com/scikit-learn/scikit-learn/pull/29694)
     by [Loïc Estèvce](https://github.com/lesteve)
    .
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.5.html#changelog "Link to this heading")

#### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-calibration "Link to this heading")

*   Fix Raise error when [`LeaveOneOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#sklearn.model_selection.LeaveOneOut "sklearn.model_selection.LeaveOneOut")
     used in `cv`, matching what would happen if `KFold(n_splits=n_samples)` was used. [#29545](https://github.com/scikit-learn/scikit-learn/pull/29545)
     by [Lucy Liu](https://github.com/lucyleeow)
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-compose "Link to this heading")

*   Fix Fixed [`compose.TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
     not to raise `UserWarning` if transform output is set to `pandas` or `polars`, since it isn’t a transformer. [#29401](https://github.com/scikit-learn/scikit-learn/pull/29401)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-decomposition "Link to this heading")

*   Fix Increase rank deficiency threshold in the whitening step of [`decomposition.FastICA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")
     with `whiten_solver="eigh"` to improve the platform-agnosticity of the estimator. [#29612](https://github.com/scikit-learn/scikit-learn/pull/29612)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-metrics "Link to this heading")

*   Fix Fix a regression in [`metrics.accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
     and in [`metrics.zero_one_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "sklearn.metrics.zero_one_loss")
     causing an error for Array API dispatch with multilabel inputs. [#29336](https://github.com/scikit-learn/scikit-learn/pull/29336)
     by [Edoardo Abati](https://github.com/EdAbati)
    .
    

#### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-svm "Link to this heading")

*   Fix Fixed a regression in [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     and [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
     such that we accept `C=float("inf")`. [#29780](https://github.com/scikit-learn/scikit-learn/pull/29780)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

Version 1.5.1[#](https://scikit-learn.org/stable/whats_new/v1.5.html#version-1-5-1 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**July 2024**

### Changes impacting many modules[#](https://scikit-learn.org/stable/whats_new/v1.5.html#id1 "Link to this heading")

*   Fix Fixed a regression in the validation of the input data of all estimators where an unexpected error was raised when passing a DataFrame backed by a read-only buffer. [#29018](https://github.com/scikit-learn/scikit-learn/pull/29018)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix Fixed a regression causing a dead-lock at import time in some settings. [#29235](https://github.com/scikit-learn/scikit-learn/pull/29235)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.5.html#id2 "Link to this heading")

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#id3 "Link to this heading")

*   Efficiency Fix a performance regression in [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     where the full input data was copied for each transformer when `n_jobs > 1`. [#29330](https://github.com/scikit-learn/scikit-learn/pull/29330)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#id4 "Link to this heading")

*   Fix Fix a regression in [`metrics.r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
    . Passing torch CPU tensors with array API dispatched disabled would complain about non-CPU devices instead of implicitly converting those inputs as regular NumPy arrays. [#29119](https://github.com/scikit-learn/scikit-learn/pull/29119)
     by [@Olivier Grisel](https://github.com/Olivier%20Grisel)
    .
    
*   Fix Fix a regression in [`metrics.zero_one_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "sklearn.metrics.zero_one_loss")
     causing an error for Array API dispatch with multilabel inputs. [#29269](https://github.com/scikit-learn/scikit-learn/pull/29269)
     by [Yaroslav Korobko](https://github.com/Tialo)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-model-selection "Link to this heading")

*   Fix Fix a regression in [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     for parameter grids that have heterogeneous parameter values. [#29078](https://github.com/scikit-learn/scikit-learn/pull/29078)
     by [Loïc Estève](https://github.com/lesteve)
    .
    
*   Fix Fix a regression in [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     for parameter grids that have estimators as parameter values. [#29179](https://github.com/scikit-learn/scikit-learn/pull/29179)
     by [Marco Gorelli](https://github.com/MarcoGorelli)
    .
    
*   Fix Fix a regression in [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     for parameter grids that have arrays of different sizes as parameter values. [#29314](https://github.com/scikit-learn/scikit-learn/pull/29314)
     by [Marco Gorelli](https://github.com/MarcoGorelli)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-tree "Link to this heading")

*   Fix Fix an issue in [`tree.export_graphviz`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz "sklearn.tree.export_graphviz")
     and [`tree.plot_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree")
     that could potentially result in exception or wrong results on 32bit OSes. [#29327](https://github.com/scikit-learn/scikit-learn/pull/29327)
     by [Loïc Estève](https://github.com/lesteve)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-utils "Link to this heading")

*   API Change `utils.validation.check_array` has a new parameter, `force_writeable`, to control the writeability of the output array. If set to `True`, the output array will be guaranteed to be writeable and a copy will be made if the input array is read-only. If set to `False`, no guarantee is made about the writeability of the output array. [#29018](https://github.com/scikit-learn/scikit-learn/pull/29018)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

Version 1.5.0[#](https://scikit-learn.org/stable/whats_new/v1.5.html#version-1-5-0 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**May 2024**

### Security[#](https://scikit-learn.org/stable/whats_new/v1.5.html#security "Link to this heading")

*   Fix [`feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     and [`feature_extraction.text.TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
     no longer store discarded tokens from the training set in their `stop_words_` attribute. This attribute would hold too frequent (above `max_df`) but also too rare tokens (below `min_df`). This fixes a potential security issue (data leak) if the discarded rare tokens hold sensitive information from the training set without the model developer’s knowledge.
    
    Note: users of those classes are encouraged to either retrain their pipelines with the new scikit-learn version or to manually clear the `stop_words_` attribute from previously trained instances of those transformers. This attribute was designed only for model inspection purposes and has no impact on the behavior of the transformers. [#28823](https://github.com/scikit-learn/scikit-learn/pull/28823)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    

### Changed models[#](https://scikit-learn.org/stable/whats_new/v1.5.html#changed-models "Link to this heading")

*   Efficiency The subsampling in [`preprocessing.QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
     is now more efficient for dense arrays but the fitted quantiles and the results of `transform` may be slightly different than before (keeping the same statistical properties). [#27344](https://github.com/scikit-learn/scikit-learn/pull/27344)
     by [Xuefeng Xu](https://github.com/xuefeng-xu)
    .
    
*   Enhancement [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
    , [`decomposition.SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")
     and [`decomposition.TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
     now set the sign of the `components_` attribute based on the component values instead of using the transformed data as reference. This change is needed to be able to offer consistent component signs across all `PCA` solvers, including the new `svd_solver="covariance_eigh"` option introduced in this release.
    

### Changes impacting many modules[#](https://scikit-learn.org/stable/whats_new/v1.5.html#id5 "Link to this heading")

*   Fix Raise `ValueError` with an informative error message when passing 1D sparse arrays to methods that expect 2D sparse inputs. [#28988](https://github.com/scikit-learn/scikit-learn/pull/28988)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   API Change The name of the input of the `inverse_transform` method of estimators has been standardized to `X`. As a consequence, `Xt` is deprecated and will be removed in version 1.7 in the following estimators: [`cluster.FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")
    , [`decomposition.MiniBatchNMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")
    , [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
    , [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    , [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
    , [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     and [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
    . [#28756](https://github.com/scikit-learn/scikit-learn/pull/28756)
     by [Will Dean](https://github.com/wd60622)
    .
    

### Support for Array API[#](https://scikit-learn.org/stable/whats_new/v1.5.html#support-for-array-api "Link to this heading")

Additional estimators and functions have been updated to include support for all [Array API](https://data-apis.org/array-api/latest/)
 compliant inputs.

See [Array API support (experimental)](https://scikit-learn.org/stable/modules/array_api.html#array-api)
 for more details.

**Functions:**

*   [`sklearn.metrics.r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
     now supports Array API compliant inputs. [#27904](https://github.com/scikit-learn/scikit-learn/pull/27904)
     by [Eric Lindgren](https://github.com/elindgren)
    , [Franck Charras](https://github.com/fcharras)
    , [Olivier Grisel](https://github.com/ogrisel)
     and [Tim Head](https://github.com/betatim)
    .
    

**Classes:**

*   [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     now supports the Array API for the `svd` solver. See [Array API support (experimental)](https://scikit-learn.org/stable/modules/array_api.html#array-api)
     for more details. [#27800](https://github.com/scikit-learn/scikit-learn/pull/27800)
     by [Franck Charras](https://github.com/fcharras)
    , [Olivier Grisel](https://github.com/ogrisel)
     and [Tim Head](https://github.com/betatim)
    .
    

### Support for building with Meson[#](https://scikit-learn.org/stable/whats_new/v1.5.html#support-for-building-with-meson "Link to this heading")

From scikit-learn 1.5 onwards, Meson is the main supported way to build scikit-learn.

Unless we discover a major blocker, setuptools support will be dropped in scikit-learn 1.6. The 1.5.x releases will support building scikit-learn with setuptools.

Meson support for building scikit-learn was added in [#28040](https://github.com/scikit-learn/scikit-learn/pull/28040)
 by [Loïc Estève](https://github.com/lesteve)

### Metadata Routing[#](https://scikit-learn.org/stable/whats_new/v1.5.html#metadata-routing "Link to this heading")

The following models now support metadata routing in one or more of their methods. Refer to the [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

*   Feature [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     now supports metadata routing in its `fit` method. [#28187](https://github.com/scikit-learn/scikit-learn/pull/28187)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    
*   Feature [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
     and [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
     now support metadata routing. The fit methods now accept `**fit_params` which are passed to the underlying estimators via their `fit` methods. [#28432](https://github.com/scikit-learn/scikit-learn/pull/28432)
     by [Adam Li](https://github.com/adam2392)
     and [Benjamin Bossan](https://github.com/BenjaminBossan)
    .
    
*   Feature [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     and [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
     now support metadata routing in their `fit` method and route metadata to the underlying [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     object or the underlying scorer. [#27560](https://github.com/scikit-learn/scikit-learn/pull/27560)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    
*   Feature `GraphicalLassoCV` now supports metadata routing in its `fit` method and routes metadata to the CV splitter. [#27566](https://github.com/scikit-learn/scikit-learn/pull/27566)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    
*   Feature [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
     now supports metadata routing in its `fit`, `score` and `predict` methods and route metadata to its underlying estimator’s `fit`, `score` and `predict` methods. [#28261](https://github.com/scikit-learn/scikit-learn/pull/28261)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    
*   Feature [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     and [`ensemble.VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
     now support metadata routing and pass `**fit_params` to the underlying estimators via their `fit` methods. [#27584](https://github.com/scikit-learn/scikit-learn/pull/27584)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    
*   Feature [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     now supports metadata routing in its `fit` and `fit_transform` methods and route metadata to the underlying transformers’ `fit` and `fit_transform`. [#28205](https://github.com/scikit-learn/scikit-learn/pull/28205)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    
*   Fix Fix an issue when resolving default routing requests set via class attributes. [#28435](https://github.com/scikit-learn/scikit-learn/pull/28435)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Fix Fix an issue when `set_{method}_request` methods are used as unbound methods, which can happen if one tries to decorate them. [#28651](https://github.com/scikit-learn/scikit-learn/pull/28651)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Fix Prevent a `RecursionError` when estimators with the default `scoring` param (`None`) route metadata. [#28712](https://github.com/scikit-learn/scikit-learn/pull/28712)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.5.html#id6 "Link to this heading")

#### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#id7 "Link to this heading")

*   Fix Fixed a regression in [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     where an error was wrongly raised with string targets. [#28843](https://github.com/scikit-learn/scikit-learn/pull/28843)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-cluster "Link to this heading")

*   Fix The [`cluster.MeanShift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")
     class now properly converges for constant data. [#28951](https://github.com/scikit-learn/scikit-learn/pull/28951)
     by [Akihiro Kuno](https://github.com/akikuno)
    .
    
*   Fix Create copy of precomputed sparse matrix within the `fit` method of [`OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
     to avoid in-place modification of the sparse matrix. [#28491](https://github.com/scikit-learn/scikit-learn/pull/28491)
     by [Thanh Lam Dang](https://github.com/lamdang2k)
    .
    
*   Fix [`cluster.HDBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
     now supports all metrics supported by [`sklearn.metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     when `algorithm="brute"` or `"auto"`. [#28664](https://github.com/scikit-learn/scikit-learn/pull/28664)
     by [Manideep Yenugula](https://github.com/myenugula)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#id8 "Link to this heading")

*   Feature A fitted [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     now implements `__getitem__` which returns the fitted transformers by name. [#27990](https://github.com/scikit-learn/scikit-learn/pull/27990)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`compose.TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
     now raises an error in `fit` if only `inverse_func` is provided without `func` (that would default to identity) being explicitly set as well. [#28483](https://github.com/scikit-learn/scikit-learn/pull/28483)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    
*   Enhancement [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     can now expose the “remainder” columns in the fitted `transformers_` attribute as column names or boolean masks, rather than column indices. [#27657](https://github.com/scikit-learn/scikit-learn/pull/27657)
     by [Jérôme Dockès](https://github.com/jeromedockes)
    .
    
*   Fix Fixed a bug in [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     with `n_jobs > 1`, where the intermediate selected columns were passed to the transformers as read-only arrays. [#28822](https://github.com/scikit-learn/scikit-learn/pull/28822)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.cross_decomposition`](https://scikit-learn.org/stable/api/sklearn.cross_decomposition.html#module-sklearn.cross_decomposition "sklearn.cross_decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-cross-decomposition "Link to this heading")

*   Fix The `coef_` fitted attribute of [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
     now takes into account both the scale of `X` and `Y` when `scale=True`. Note that the previous predicted values were not affected by this bug. [#28612](https://github.com/scikit-learn/scikit-learn/pull/28612)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change Deprecates `Y` in favor of `y` in the methods `fit`, `transform` and `inverse_transform` of: [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
    , [`cross_decomposition.PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
    , and [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
    , and methods `fit` and `transform` of: [`cross_decomposition.PLSSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD "sklearn.cross_decomposition.PLSSVD")
    . `Y` will be removed in version 1.7. [#28604](https://github.com/scikit-learn/scikit-learn/pull/28604)
     by [David Leon](https://github.com/davidleon123)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-datasets "Link to this heading")

*   Enhancement Adds optional arguments `n_retries` and `delay` to functions [`datasets.fetch_20newsgroups`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
    , [`datasets.fetch_20newsgroups_vectorized`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized")
    , [`datasets.fetch_california_housing`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")
    , [`datasets.fetch_covtype`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#sklearn.datasets.fetch_covtype "sklearn.datasets.fetch_covtype")
    , [`datasets.fetch_kddcup99`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99 "sklearn.datasets.fetch_kddcup99")
    , [`datasets.fetch_lfw_pairs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_pairs.html#sklearn.datasets.fetch_lfw_pairs "sklearn.datasets.fetch_lfw_pairs")
    , [`datasets.fetch_lfw_people`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html#sklearn.datasets.fetch_lfw_people "sklearn.datasets.fetch_lfw_people")
    , [`datasets.fetch_olivetti_faces`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#sklearn.datasets.fetch_olivetti_faces "sklearn.datasets.fetch_olivetti_faces")
    , [`datasets.fetch_rcv1`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_rcv1.html#sklearn.datasets.fetch_rcv1 "sklearn.datasets.fetch_rcv1")
    , and [`datasets.fetch_species_distributions`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_species_distributions.html#sklearn.datasets.fetch_species_distributions "sklearn.datasets.fetch_species_distributions")
    . By default, the functions will retry up to 3 times in case of network failures. [#28160](https://github.com/scikit-learn/scikit-learn/pull/28160)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
     and [Filip Karlo Došilović](https://github.com/fkdosilovic)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#id9 "Link to this heading")

*   Efficiency [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     with `svd_solver="full"` now assigns a contiguous `components_` attribute instead of a non-contiguous slice of the singular vectors. When `n_components << n_features`, this can save some memory and, more importantly, help speed-up subsequent calls to the `transform` method by more than an order of magnitude by leveraging cache locality of BLAS GEMM on contiguous arrays. [#27491](https://github.com/scikit-learn/scikit-learn/pull/27491)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Enhancement [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     now automatically selects the ARPACK solver for sparse inputs when `svd_solver="auto"` instead of raising an error. [#28498](https://github.com/scikit-learn/scikit-learn/pull/28498)
     by [Thanh Lam Dang](https://github.com/lamdang2k)
    .
    
*   Enhancement [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     now supports a new solver option named `svd_solver="covariance_eigh"` which offers an order of magnitude speed-up and reduced memory usage for datasets with a large number of data points and a small number of features (say, `n_samples >> 1000 > n_features`). The `svd_solver="auto"` option has been updated to use the new solver automatically for such datasets. This solver also accepts sparse input data. [#27491](https://github.com/scikit-learn/scikit-learn/pull/27491)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Fix [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     fit with `svd_solver="arpack"`, `whiten=True` and a value for `n_components` that is larger than the rank of the training set, no longer returns infinite values when transforming hold-out data. [#27491](https://github.com/scikit-learn/scikit-learn/pull/27491)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    

#### [`sklearn.dummy`](https://scikit-learn.org/stable/api/sklearn.dummy.html#module-sklearn.dummy "sklearn.dummy")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-dummy "Link to this heading")

*   Enhancement [`dummy.DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
     and [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
     now have the `n_features_in_` and `feature_names_in_` attributes after `fit`. [#27937](https://github.com/scikit-learn/scikit-learn/pull/27937)
     by [Marco vd Boom](https://github.com/tvdboom)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-ensemble "Link to this heading")

*   Efficiency Improves runtime of `predict` of [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     by avoiding to call `predict_proba`. [#27844](https://github.com/scikit-learn/scikit-learn/pull/27844)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Efficiency [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     are now a tiny bit faster by pre-sorting the data before finding the thresholds for binning. [#28102](https://github.com/scikit-learn/scikit-learn/pull/28102)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Fix Fixes a bug in [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     when `monotonic_cst` is specified for non-categorical features. [#28925](https://github.com/scikit-learn/scikit-learn/pull/28925)
     by [Xiao Yuan](https://github.com/yuanx749)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-feature-extraction "Link to this heading")

*   Efficiency [`feature_extraction.text.TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
     is now faster and more memory-efficient by using a NumPy vector instead of a sparse matrix for storing the inverse document frequency. [#18843](https://github.com/scikit-learn/scikit-learn/pull/18843)
     by [Paolo Montesel](https://github.com/thebabush)
    .
    
*   Enhancement [`feature_extraction.text.TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
     now preserves the data type of the input matrix if it is `np.float64` or `np.float32`. [#28136](https://github.com/scikit-learn/scikit-learn/pull/28136)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-feature-selection "Link to this heading")

*   Enhancement [`feature_selection.mutual_info_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html#sklearn.feature_selection.mutual_info_regression "sklearn.feature_selection.mutual_info_regression")
     and [`feature_selection.mutual_info_classif`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#sklearn.feature_selection.mutual_info_classif "sklearn.feature_selection.mutual_info_classif")
     now support `n_jobs` parameter. [#28085](https://github.com/scikit-learn/scikit-learn/pull/28085)
     by [Neto Menoci](https://github.com/netomenoci)
     and [Florin Andrei](https://github.com/FlorinAndrei)
    .
    
*   Enhancement The `cv_results_` attribute of [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
     has a new key, `n_features`, containing an array with the number of features selected at each step. [#28670](https://github.com/scikit-learn/scikit-learn/pull/28670)
     by [Miguel Silva](https://github.com/miguelcsilva)
    .
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-impute "Link to this heading")

*   Enhancement [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     now supports custom strategies by passing a function in place of a strategy name. [#28053](https://github.com/scikit-learn/scikit-learn/pull/28053)
     by [Mark Elliot](https://github.com/mark-thm)
    .
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-inspection "Link to this heading")

*   Fix [`inspection.DecisionBoundaryDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
     no longer warns about missing feature names when provided a `polars.DataFrame`. [#28718](https://github.com/scikit-learn/scikit-learn/pull/28718)
     by [Patrick Wang](https://github.com/patrickkwang)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-linear-model "Link to this heading")

*   Enhancement Solver `"newton-cg"` in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     now emits information when `verbose` is set to positive values. [#27526](https://github.com/scikit-learn/scikit-learn/pull/27526)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Fix [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
    , [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    , [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     and [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
     now explicitly don’t accept large sparse data formats. [#27576](https://github.com/scikit-learn/scikit-learn/pull/27576)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    
*   Fix [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     and `RidgeClassifierCV` correctly pass `sample_weight` to the underlying scorer when `cv` is None. [#27560](https://github.com/scikit-learn/scikit-learn/pull/27560)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    
*   Fix `n_nonzero_coefs_` attribute in [`linear_model.OrthogonalMatchingPursuit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html#sklearn.linear_model.OrthogonalMatchingPursuit "sklearn.linear_model.OrthogonalMatchingPursuit")
     will now always be `None` when `tol` is set, as `n_nonzero_coefs` is ignored in this case. [#28557](https://github.com/scikit-learn/scikit-learn/pull/28557)
     by [Lucy Liu](https://github.com/lucyleeow)
    .
    
*   API Change [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     and [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
     will now allow `alpha=0` when `cv != None`, which is consistent with [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     and [`linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
    . [#28425](https://github.com/scikit-learn/scikit-learn/pull/28425)
     by [Lucy Liu](https://github.com/lucyleeow)
    .
    
*   API Change Passing `average=0` to disable averaging is deprecated in [`linear_model.PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier")
    , [`linear_model.PassiveAggressiveRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model.PassiveAggressiveRegressor")
    , [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    , [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     and [`linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
    . Pass `average=False` instead. [#28582](https://github.com/scikit-learn/scikit-learn/pull/28582)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   API Change Parameter `multi_class` was deprecated in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
    . `multi_class` will be removed in 1.8, and internally, for 3 and more classes, it will always use multinomial. If you still want to use the one-vs-rest scheme, you can use `OneVsRestClassifier(LogisticRegression(..))`. [#28703](https://github.com/scikit-learn/scikit-learn/pull/28703)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   API Change Parameters `store_cv_values` and `cv_values_` are deprecated in favor of `store_cv_results` and `cv_results_` in `~linear_model.RidgeCV` and `~linear_model.RidgeClassifierCV`. [#28915](https://github.com/scikit-learn/scikit-learn/pull/28915)
     by [Lucy Liu](https://github.com/lucyleeow)
    .
    

#### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-manifold "Link to this heading")

*   API Change Deprecates `n_iter` in favor of `max_iter` in [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
    . `n_iter` will be removed in version 1.7. This makes [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     consistent with the rest of the estimators. [#28471](https://github.com/scikit-learn/scikit-learn/pull/28471)
     by [Lucy Liu](https://github.com/lucyleeow)
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#id10 "Link to this heading")

*   Feature [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     accepts calculating pairwise distances for non-numeric arrays as well. This is supported through custom metrics only. [#27456](https://github.com/scikit-learn/scikit-learn/pull/27456)
     by [Venkatachalam N](https://github.com/venkyyuvy)
    , [Kshitij Mathur](https://github.com/Kshitij68)
     and [Julian Libiseller-Egger](https://github.com/julibeg)
    .
    
*   Feature [`sklearn.metrics.check_scoring`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.check_scoring.html#sklearn.metrics.check_scoring "sklearn.metrics.check_scoring")
     now returns a multi-metric scorer when `scoring` as a `dict`, `set`, `tuple`, or `list`. [#28360](https://github.com/scikit-learn/scikit-learn/pull/28360)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature [`metrics.d2_log_loss_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_log_loss_score.html#sklearn.metrics.d2_log_loss_score "sklearn.metrics.d2_log_loss_score")
     has been added which calculates the D^2 score for the log loss. [#28351](https://github.com/scikit-learn/scikit-learn/pull/28351)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    
*   Efficiency Improve efficiency of functions [`brier_score_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
    , [`calibration_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html#sklearn.calibration.calibration_curve "sklearn.calibration.calibration_curve")
    , [`det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")
    , [`precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")
    , [`roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
     when `pos_label` argument is specified. Also improve efficiency of methods `from_estimator` and `from_predictions` in [`RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")
    , [`PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")
    , [`DetCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay "sklearn.metrics.DetCurveDisplay")
    , [`CalibrationDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay "sklearn.calibration.CalibrationDisplay")
    . [#28051](https://github.com/scikit-learn/scikit-learn/pull/28051)
     by [Pierre de Fréminville](https://github.com/pidefrem)
    .
    
*   Fix [`metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
     now shows only accuracy and not micro-average when input is a subset of labels. [#28399](https://github.com/scikit-learn/scikit-learn/pull/28399)
     by [Vineet Joshi](https://github.com/vjoshi253)
    .
    
*   Fix Fix OpenBLAS 0.3.26 dead-lock on Windows in pairwise distances computation. This is likely to affect neighbor-based algorithms. [#28692](https://github.com/scikit-learn/scikit-learn/pull/28692)
     by [Loïc Estève](https://github.com/lesteve)
    .
    
*   API Change [`metrics.precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")
     deprecated the keyword argument `probas_pred` in favor of `y_score`. `probas_pred` will be removed in version 1.7. [#28092](https://github.com/scikit-learn/scikit-learn/pull/28092)
     by [Adam Li](https://github.com/adam2392)
    .
    
*   API Change [`metrics.brier_score_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
     deprecated the keyword argument `y_prob` in favor of `y_proba`. `y_prob` will be removed in version 1.7. [#28092](https://github.com/scikit-learn/scikit-learn/pull/28092)
     by [Adam Li](https://github.com/adam2392)
    .
    
*   API Change For classifiers and classification metrics, labels encoded as bytes is deprecated and will raise an error in v1.7. [#18555](https://github.com/scikit-learn/scikit-learn/pull/18555)
     by [Kaushik Amar Das](https://github.com/cozek)
    .
    

#### [`sklearn.mixture`](https://scikit-learn.org/stable/api/sklearn.mixture.html#module-sklearn.mixture "sklearn.mixture")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-mixture "Link to this heading")

*   Fix The `converged_` attribute of [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     and [`mixture.BayesianGaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")
     now reflects the convergence status of the best fit whereas it was previously `True` if any of the fits converged. [#26837](https://github.com/scikit-learn/scikit-learn/pull/26837)
     by [Krsto Proroković](https://github.com/krstopro)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#id11 "Link to this heading")

*   Major Feature [`model_selection.TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
     finds the decision threshold of a binary classifier that maximizes a classification metric through cross-validation. [`model_selection.FixedThresholdClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")
     is an alternative when one wants to use a fixed decision threshold without any tuning scheme. [#26120](https://github.com/scikit-learn/scikit-learn/pull/26120)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Enhancement [CV splitters](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
     that ignores the group parameter now raises a warning when groups are passed in to [split](https://scikit-learn.org/stable/glossary.html#term-split)
    . [#28210](https://github.com/scikit-learn/scikit-learn/pull/28210)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement The HTML diagram representation of [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    , [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
    , [`HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
    , and [`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
     will show the best estimator when `refit=True`. [#28722](https://github.com/scikit-learn/scikit-learn/pull/28722)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
     and [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix the `cv_results_` attribute (of [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    ) now returns masked arrays of the appropriate NumPy dtype, as opposed to always returning dtype `object`. [#28352](https://github.com/scikit-learn/scikit-learn/pull/28352)
     by [Marco Gorelli](https://github.com/MarcoGorelli)
    .
    
*   Fix [`model_selection.train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
     works with Array API inputs. Previously indexing was not handled correctly leading to exceptions when using strict implementations of the Array API like CuPY. [#28407](https://github.com/scikit-learn/scikit-learn/pull/28407)
     by [Tim Head](https://github.com/betatim)
    .
    

#### [`sklearn.multioutput`](https://scikit-learn.org/stable/api/sklearn.multioutput.html#module-sklearn.multioutput "sklearn.multioutput")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-multioutput "Link to this heading")

*   Enhancement `chain_method` parameter added to [`multioutput.ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
    . [#27700](https://github.com/scikit-learn/scikit-learn/pull/27700)
     by [Lucy Liu](https://github.com/lucyleeow)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-neighbors "Link to this heading")

*   Fix Fixes [`neighbors.NeighborhoodComponentsAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis")
     such that `get_feature_names_out` returns the correct number of feature names. [#28306](https://github.com/scikit-learn/scikit-learn/pull/28306)
     by [Brendan Lu](https://github.com/brendanlu)
    .
    

#### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-pipeline "Link to this heading")

*   Feature [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     can now use the `verbose_feature_names_out` attribute. If `True`, `get_feature_names_out` will prefix all feature names with the name of the transformer that generated that feature. If `False`, `get_feature_names_out` will not prefix any feature names and will error if feature names are not unique. [#25991](https://github.com/scikit-learn/scikit-learn/pull/25991)
     by [Jiawei Zhang](https://github.com/jiawei-zhang-a)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#sklearn-preprocessing "Link to this heading")

*   Enhancement [`preprocessing.QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
     and [`preprocessing.quantile_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#sklearn.preprocessing.quantile_transform "sklearn.preprocessing.quantile_transform")
     now supports disabling subsampling explicitly. [#27636](https://github.com/scikit-learn/scikit-learn/pull/27636)
     by [Ralph Urlus](https://github.com/rurlus)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#id12 "Link to this heading")

*   Enhancement Plotting trees in matplotlib via [`tree.plot_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree")
     now show a “True/False” label to indicate the directionality the samples traverse given the split condition. [#28552](https://github.com/scikit-learn/scikit-learn/pull/28552)
     by [Adam Li](https://github.com/adam2392)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.5.html#id13 "Link to this heading")

*   Fix [`_safe_indexing`](https://scikit-learn.org/stable/modules/generated/sklearn.utils._safe_indexing.html#sklearn.utils._safe_indexing "sklearn.utils._safe_indexing")
     now works correctly for polars DataFrame when `axis=0` and supports indexing polars Series. [#28521](https://github.com/scikit-learn/scikit-learn/pull/28521)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    
*   API Change `utils.IS_PYPY` is deprecated and will be removed in version 1.7. [#28768](https://github.com/scikit-learn/scikit-learn/pull/28768)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   API Change `utils.tosequence` is deprecated and will be removed in version 1.7. [#28763](https://github.com/scikit-learn/scikit-learn/pull/28763)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   API Change `utils.parallel_backend` and `utils.register_parallel_backend` are deprecated and will be removed in version 1.7. Use `joblib.parallel_backend` and `joblib.register_parallel_backend` instead. [#28847](https://github.com/scikit-learn/scikit-learn/pull/28847)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   API Change Raise informative warning message in [`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
     when represented as bytes. For classifiers and classification metrics, labels encoded as bytes is deprecated and will raise an error in v1.7. [#18555](https://github.com/scikit-learn/scikit-learn/pull/18555)
     by [Kaushik Amar Das](https://github.com/cozek)
    .
    
*   API Change `utils.estimator_checks.check_estimator_sparse_data` was split into two functions: `utils.estimator_checks.check_estimator_sparse_matrix` and `utils.estimator_checks.check_estimator_sparse_array`. [#27576](https://github.com/scikit-learn/scikit-learn/pull/27576)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    

Code and documentation contributors

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 1.4, including:

101AlexMartin, Abdulaziz Aloqeely, Adam J. Stewart, Adam Li, Adarsh Wase, Adeyemi Biola, Aditi Juneja, Adrin Jalali, Advik Sinha, Aisha, Akash Srivastava, Akihiro Kuno, Alan Guedes, Alberto Torres, Alexis IMBERT, alexqiao, Ana Paula Gomes, Anderson Nelson, Andrei Dzis, Arif Qodari, Arnaud Capitaine, Arturo Amor, Aswathavicky, Audrey Flanders, awwwyan, baggiponte, Bharat Raghunathan, bme-git, brdav, Brendan Lu, Brigitta Sipőcz, Bruno, Cailean Carter, Cemlyn, Christian Lorentzen, Christian Veenhuis, Cindy Liang, Claudio Salvatore Arcidiacono, Connor Boyle, Conrad Stevens, crispinlogan, David Matthew Cherney, Davide Chicco, davidleon123, dependabot\[bot\], DerWeh, dinga92, Dipan Banik, Drew Craeton, Duarte São José, DUONG, Eddie Bergman, Edoardo Abati, Egehan Gunduz, Emad Izadifar, EmilyXinyi, Erich Schubert, Evelyn, Filip Karlo Došilović, Franck Charras, Gael Varoquaux, Gönül Aycı, Guillaume Lemaitre, Gyeongjae Choi, Harmanan Kohli, Hong Xiang Yue, Ian Faust, Ilya Komarov, itsaphel, Ivan Wiryadi, Jack Bowyer, Javier Marin Tur, Jérémie du Boisberranger, Jérôme Dockès, Jiawei Zhang, João Morais, Joe Cainey, Joel Nothman, Johanna Bayer, John Cant, John Enblom, John Hopfensperger, jpcars, jpienaar-tuks, Julian Chan, Julian Libiseller-Egger, Julien Jerphanion, KanchiMoe, Kaushik Amar Das, keyber, Koustav Ghosh, kraktus, Krsto Proroković, Lars, ldwy4, LeoGrin, lihaitao, Linus Sommer, Loic Esteve, Lucy Liu, Lukas Geiger, m-maggi, manasimj, Manuel Labbé, Manuel Morales, Marco Edward Gorelli, Marco Wolsza, Maren Westermann, Marija Vlajic, Mark Elliot, Martin Helm, Mateusz Sokół, mathurinm, Mavs, Michael Dawson, Michael Higgins, Michael Mayer, miguelcsilva, Miki Watanabe, Mohammed Hamdy, myenugula, Nathan Goldbaum, Naziya Mahimkar, nbrown-ScottLogic, Neto, Nithish Bolleddula, notPlancha, Olivier Grisel, Omar Salman, ParsifalXu, Patrick Wang, Pierre de Fréminville, Piotr, Priyank Shroff, Priyansh Gupta, Priyash Shah, Puneeth K, Rahil Parikh, raisadz, Raj Pulapakura, Ralf Gommers, Ralph Urlus, Randolf Scholz, renaissance0ne, Reshama Shaikh, Richard Barnes, Robert Pollak, Roberto Rosati, Rodrigo Romero, rwelsch427, Saad Mahmood, Salim Dohri, Sandip Dutta, SarahRemus, scikit-learn-bot, Shaharyar Choudhry, Shubham, sperret6, Stefanie Senger, Steffen Schneider, Suha Siddiqui, Thanh Lam DANG, thebabush, Thomas, Thomas J. Fan, Thomas Lazarus, Tialo, Tim Head, Tuhin Sharma, Tushar Parimi, VarunChaduvula, Vineet Joshi, virchan, Waël Boukhobza, Weyb, Will Dean, Xavier Beltran, Xiao Yuan, Xuefeng Xu, Yao Xiao, yareyaredesuyo, Ziad Amerr, Štěpán Sršeň

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)