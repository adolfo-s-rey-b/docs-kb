[Skip to main content](https://scikit-learn.org/stable/whats_new/v1.2.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v1.2.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v1.2.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v1.2.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v1.2.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v1.2.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v1.2.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v1.2.html)

Collapse Sidebar Expand Sidebar

Version 1.2[#](https://scikit-learn.org/stable/whats_new/v1.2.html#version-1-2 "Link to this heading")

=======================================================================================================

For a short description of the main highlights of the release, please refer to [Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html#sphx-glr-auto-examples-release-highlights-plot-release-highlights-1-2-0-py)
.

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 1.2.2[#](https://scikit-learn.org/stable/whats_new/v1.2.html#version-1-2-2 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**March 2023**

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.2.html#changelog "Link to this heading")

#### [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-base "Link to this heading")

*   Fix When `set_output(transform="pandas")`, [`base.TransformerMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin")
     maintains the index if the [transform](https://scikit-learn.org/stable/glossary.html#term-transform)
     output is already a DataFrame. [#25747](https://github.com/scikit-learn/scikit-learn/pull/25747)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-calibration "Link to this heading")

*   Fix A deprecation warning is raised when using the `base_estimator__` prefix to set parameters of the estimator used in [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
    . [#25477](https://github.com/scikit-learn/scikit-learn/pull/25477)
     by [Tim Head](https://github.com/betatim)
    .
    

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-cluster "Link to this heading")

*   Fix Fixed a bug in [`cluster.BisectingKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans")
    , preventing `fit` from randomly failing due to a permutation of the labels when running multiple inits. [#25563](https://github.com/scikit-learn/scikit-learn/pull/25563)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-compose "Link to this heading")

*   Fix Fixes a bug in [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     which now supports empty selection of columns when `set_output(transform="pandas")`. [#25570](https://github.com/scikit-learn/scikit-learn/pull/25570)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-ensemble "Link to this heading")

*   Fix A deprecation warning is raised when using the `base_estimator__` prefix to set parameters of the estimator used in [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
    , [`ensemble.AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
    , [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
    , and [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
    . [#25477](https://github.com/scikit-learn/scikit-learn/pull/25477)
     by [Tim Head](https://github.com/betatim)
    .
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-feature-selection "Link to this heading")

*   Fix Fixed a regression where a negative `tol` would not be accepted any more by [`feature_selection.SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
    . [#25664](https://github.com/scikit-learn/scikit-learn/pull/25664)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-inspection "Link to this heading")

*   Fix Raise a more informative error message in [`inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
     when dealing with mixed data type categories that cannot be sorted by [`numpy.unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "(in NumPy v2.5)")
    . This problem usually happens when categories are `str` and missing values are present using `np.nan`. [#25774](https://github.com/scikit-learn/scikit-learn/pull/25774)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.isotonic`](https://scikit-learn.org/stable/api/sklearn.isotonic.html#module-sklearn.isotonic "sklearn.isotonic")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-isotonic "Link to this heading")

*   Fix Fixes a bug in [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
     where [`isotonic.IsotonicRegression.predict`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression.predict "sklearn.isotonic.IsotonicRegression.predict")
     would return a pandas DataFrame when the global configuration sets `transform_output="pandas"`. [#25500](https://github.com/scikit-learn/scikit-learn/pull/25500)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-preprocessing "Link to this heading")

*   Fix `preprocessing.OneHotEncoder.drop_idx_` now properly references the dropped category in the `categories_` attribute when there are infrequent categories. [#25589](https://github.com/scikit-learn/scikit-learn/pull/25589)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     now correctly supports `encoded_missing_value` or `unknown_value` set to a categories’ cardinality when there is missing values in the training data. [#25704](https://github.com/scikit-learn/scikit-learn/pull/25704)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-tree "Link to this heading")

*   Fix Fixed a regression in [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
     and [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
     where an error was no longer raised in version 1.2 when `min_sample_split=1`. [#25744](https://github.com/scikit-learn/scikit-learn/pull/25744)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-utils "Link to this heading")

*   Fix Fixes a bug in [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     which now correctly performs non-finite validation with the Array API specification. [#25619](https://github.com/scikit-learn/scikit-learn/pull/25619)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`utils.multiclass.type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
     can identify pandas nullable data types as classification targets. [#25638](https://github.com/scikit-learn/scikit-learn/pull/25638)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

Version 1.2.1[#](https://scikit-learn.org/stable/whats_new/v1.2.html#version-1-2-1 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**January 2023**

### Changed models[#](https://scikit-learn.org/stable/whats_new/v1.2.html#changed-models "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   Fix The fitted components in [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
     might differ. The online updates of the sufficient statistics now properly take the sizes of the batches into account. [#25354](https://github.com/scikit-learn/scikit-learn/pull/25354)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix The `categories_` attribute of [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     now always contains an array of ``object`s when using predefined categories that are strings. Predefined categories encoded as bytes will no longer work with `X`` encoded as strings. [#25174](https://github.com/scikit-learn/scikit-learn/pull/25174)
     by [Tim Head](https://github.com/betatim)
    .
    

### Changes impacting all modules[#](https://scikit-learn.org/stable/whats_new/v1.2.html#changes-impacting-all-modules "Link to this heading")

*   Fix Support `pandas.Int64` dtyped `y` for classifiers and regressors. [#25089](https://github.com/scikit-learn/scikit-learn/pull/25089)
     by [Tim Head](https://github.com/betatim)
    .
    
*   Fix Remove spurious warnings for estimators internally using neighbors search methods. [#25129](https://github.com/scikit-learn/scikit-learn/pull/25129)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Fix Fix a bug where the current configuration was ignored in estimators using `n_jobs > 1`. This bug was triggered for tasks dispatched by the auxiliary thread of `joblib` as [`sklearn.get_config`](https://scikit-learn.org/stable/modules/generated/sklearn.get_config.html#sklearn.get_config "sklearn.get_config")
     used to access an empty thread local configuration instead of the configuration visible from the thread where `joblib.Parallel` was first called. [#25363](https://github.com/scikit-learn/scikit-learn/pull/25363)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id1 "Link to this heading")

#### [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id2 "Link to this heading")

*   Fix Fix a regression in `BaseEstimator.__getstate__` that would prevent certain estimators from being pickled when using Python 3.11. [#25188](https://github.com/scikit-learn/scikit-learn/pull/25188)
     by [Benjamin Bossan](https://github.com/BenjaminBossan)
    .
    
*   Fix Inheriting from [`base.TransformerMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin")
     will only wrap the `transform` method if the class defines `transform` itself. [#25295](https://github.com/scikit-learn/scikit-learn/pull/25295)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-datasets "Link to this heading")

*   Fix Fixes an inconsistency in [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     between liac-arff and pandas parser when a leading space is introduced after the delimiter. The ARFF specs require ignoring the leading space. [#25312](https://github.com/scikit-learn/scikit-learn/pull/25312)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Fixes a bug in [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     when using `parser="pandas"` where single quote and backslash escape characters were not properly handled. [#25511](https://github.com/scikit-learn/scikit-learn/pull/25511)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-decomposition "Link to this heading")

*   Fix Fixed a bug in [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
     where the online updates of the sufficient statistics were not correct when calling `partial_fit` on batches of different sizes. [#25354](https://github.com/scikit-learn/scikit-learn/pull/25354)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix [`decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
     better supports readonly NumPy arrays. In particular, it better supports large datasets which are memory-mapped when it is used with coordinate descent algorithms (i.e. when `fit_algorithm='cd'`). [#25172](https://github.com/scikit-learn/scikit-learn/pull/25172)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id3 "Link to this heading")

*   Fix [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
     and [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
     now support sparse readonly datasets. [#25341](https://github.com/scikit-learn/scikit-learn/pull/25341)
     by [Julien Jerphanion](https://github.com/jjerphan)
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-feature-extraction "Link to this heading")

*   Fix [`feature_extraction.FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
     raises an informative error when the input is a list of strings. [#25094](https://github.com/scikit-learn/scikit-learn/pull/25094)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-linear-model "Link to this heading")

*   Fix Fix a regression in [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     and [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     that makes them unusable with the `verbose` parameter set to a value greater than 0. [#25250](https://github.com/scikit-learn/scikit-learn/pull/25250)
     by [Jérémie Du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-manifold "Link to this heading")

*   Fix [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     now works correctly when output type is set to pandas [#25370](https://github.com/scikit-learn/scikit-learn/pull/25370)
     by [Tim Head](https://github.com/betatim)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-model-selection "Link to this heading")

*   Fix [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
     with multimetric scoring in case of some failing scorers the non-failing scorers now return proper scores instead of `error_score` values. [#23101](https://github.com/scikit-learn/scikit-learn/pull/23101)
     by [András Simon](https://github.com/simonandras)
     and [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.neural_network`](https://scikit-learn.org/stable/api/sklearn.neural_network.html#module-sklearn.neural_network "sklearn.neural_network")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-neural-network "Link to this heading")

*   Fix [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     and [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
     no longer raise warnings when fitting data with feature names. [#24873](https://github.com/scikit-learn/scikit-learn/pull/24873)
     by [Tim Head](https://github.com/betatim)
    .
    
*   Fix Improves error message in [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     and [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
    , when `early_stopping=True` and `partial_fit` is called. [#25694](https://github.com/scikit-learn/scikit-learn/pull/25694)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id4 "Link to this heading")

*   Fix [`preprocessing.FunctionTransformer.inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer.inverse_transform "sklearn.preprocessing.FunctionTransformer.inverse_transform")
     correctly supports DataFrames that are all numerical when `check_inverse=True`. [#25274](https://github.com/scikit-learn/scikit-learn/pull/25274)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`preprocessing.SplineTransformer.get_feature_names_out`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer.get_feature_names_out "sklearn.preprocessing.SplineTransformer.get_feature_names_out")
     correctly returns feature names when `extrapolations="periodic"`. [#25296](https://github.com/scikit-learn/scikit-learn/pull/25296)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id5 "Link to this heading")

*   Fix [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
     [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
     and [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
     now support sparse readonly datasets. [#25341](https://github.com/scikit-learn/scikit-learn/pull/25341)
     by [Julien Jerphanion](https://github.com/jjerphan)
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id6 "Link to this heading")

*   Fix Restore [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
    ’s behaviour for pandas Series of type boolean. The type is maintained, instead of converting to `float64.` [#25147](https://github.com/scikit-learn/scikit-learn/pull/25147)
     by [Tim Head](https://github.com/betatim)
    .
    
*   API Change `utils.fixes.delayed` is deprecated in 1.2.1 and will be removed in 1.5. Instead, import [`utils.parallel.delayed`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.delayed.html#sklearn.utils.parallel.delayed "sklearn.utils.parallel.delayed")
     and use it in conjunction with the newly introduced [`utils.parallel.Parallel`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#sklearn.utils.parallel.Parallel "sklearn.utils.parallel.Parallel")
     to ensure proper propagation of the scikit-learn configuration to the workers. [#25363](https://github.com/scikit-learn/scikit-learn/pull/25363)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

Version 1.2.0[#](https://scikit-learn.org/stable/whats_new/v1.2.html#version-1-2-0 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**December 2022**

### Changed models[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id7 "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   Enhancement The default `eigen_tol` for [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
    , [`manifold.SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
    , [`cluster.spectral_clustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")
    , and [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
     is now `None` when using the `'amg'` or `'lobpcg'` solvers. This change improves numerical stability of the solver, but may result in a different model.
    
*   Enhancement [`linear_model.GammaRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html#sklearn.linear_model.GammaRegressor "sklearn.linear_model.GammaRegressor")
    , [`linear_model.PoissonRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")
     and [`linear_model.TweedieRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html#sklearn.linear_model.TweedieRegressor "sklearn.linear_model.TweedieRegressor")
     can reach higher precision with the lbfgs solver, in particular when `tol` is set to a tiny value. Moreover, `verbose` is now properly propagated to L-BFGS-B. [#23619](https://github.com/scikit-learn/scikit-learn/pull/23619)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Enhancement The default value for `eps` [`metrics.log_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
     has changed from `1e-15` to `"auto"`. `"auto"` sets `eps` to `np.finfo(y_pred.dtype).eps`. [#24354](https://github.com/scikit-learn/scikit-learn/pull/24354)
     by [Safiuddin Khaja](https://github.com/Safikh)
     and [gsiisg](https://github.com/gsiisg)
    .
    
*   Fix Make sign of `components_` deterministic in [`decomposition.SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")
    . [#23935](https://github.com/scikit-learn/scikit-learn/pull/23935)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix The `components_` signs in [`decomposition.FastICA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")
     might differ. It is now consistent and deterministic with all SVD solvers. [#22527](https://github.com/scikit-learn/scikit-learn/pull/22527)
     by [Meekail Zain](https://github.com/micky774)
     and [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix The condition for early stopping has now been changed in `linear_model._sgd_fast._plain_sgd` which is used by [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     and [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    . The old condition did not disambiguate between training and validation set and had an effect of overscaling the error tolerance. This has been fixed in [#23798](https://github.com/scikit-learn/scikit-learn/pull/23798)
     by [Harsh Agrawal](https://github.com/Harsh14901)
    .
    
*   Fix For [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     ranks corresponding to nan scores will all be set to the maximum possible rank. [#24543](https://github.com/scikit-learn/scikit-learn/pull/24543)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change The default value of `tol` was changed from `1e-3` to `1e-4` for [`linear_model.ridge_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html#sklearn.linear_model.ridge_regression "sklearn.linear_model.ridge_regression")
    , [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     and [`linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
    . [#24465](https://github.com/scikit-learn/scikit-learn/pull/24465)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    

### Changes impacting all modules[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id8 "Link to this heading")

*   Major Feature The `set_output` API has been adopted by all transformers. Meta-estimators that contain transformers such as [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     or [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     also define a `set_output`. For details, see [SLEP018](https://scikit-learn-enhancement-proposals.readthedocs.io/en/latest/slep018/proposal.html)
    . [#23734](https://github.com/scikit-learn/scikit-learn/pull/23734)
     and [#24699](https://github.com/scikit-learn/scikit-learn/pull/24699)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Efficiency Low-level routines for reductions on pairwise distances for dense float32 datasets have been refactored. The following functions and estimators now benefit from improved performances in terms of hardware scalability and speed-ups:
    
    *   [`sklearn.metrics.pairwise_distances_argmin`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "sklearn.metrics.pairwise_distances_argmin")
        
    *   [`sklearn.metrics.pairwise_distances_argmin_min`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html#sklearn.metrics.pairwise_distances_argmin_min "sklearn.metrics.pairwise_distances_argmin_min")
        
    *   [`sklearn.cluster.AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
        
    *   [`sklearn.cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
        
    *   [`sklearn.cluster.MeanShift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")
        
    *   [`sklearn.cluster.OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
        
    *   [`sklearn.cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
        
    *   [`sklearn.feature_selection.mutual_info_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html#sklearn.feature_selection.mutual_info_regression "sklearn.feature_selection.mutual_info_regression")
        
    *   [`sklearn.neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
        
    *   [`sklearn.neighbors.KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
        
    *   [`sklearn.neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
        
    *   [`sklearn.neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
        
    *   [`sklearn.neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
        
    *   [`sklearn.neighbors.NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
        
    *   [`sklearn.manifold.Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
        
    *   [`sklearn.manifold.LocallyLinearEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
        
    *   [`sklearn.manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
        
    *   [`sklearn.manifold.trustworthiness`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.trustworthiness.html#sklearn.manifold.trustworthiness "sklearn.manifold.trustworthiness")
        
    *   [`sklearn.semi_supervised.LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")
        
    *   [`sklearn.semi_supervised.LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
        
    
    For instance [`sklearn.neighbors.NearestNeighbors.kneighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.kneighbors "sklearn.neighbors.NearestNeighbors.kneighbors")
     and [`sklearn.neighbors.NearestNeighbors.radius_neighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.radius_neighbors "sklearn.neighbors.NearestNeighbors.radius_neighbors")
     can respectively be up to ×20 and ×5 faster than previously on a laptop.
    
    Moreover, implementations of those two algorithms are now suitable for machine with many cores, making them usable for datasets consisting of millions of samples.
    
    [#23865](https://github.com/scikit-learn/scikit-learn/pull/23865)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Enhancement Finiteness checks (detection of NaN and infinite values) in all estimators are now significantly more efficient for float32 data by leveraging NumPy’s SIMD optimized primitives. [#23446](https://github.com/scikit-learn/scikit-learn/pull/23446)
     by [Meekail Zain](https://github.com/micky774)
    
*   Enhancement Finiteness checks (detection of NaN and infinite values) in all estimators are now faster by utilizing a more efficient stop-on-first second-pass algorithm. [#23197](https://github.com/scikit-learn/scikit-learn/pull/23197)
     by [Meekail Zain](https://github.com/micky774)
    
*   Enhancement Support for combinations of dense and sparse datasets pairs for all distance metrics and for float32 and float64 datasets has been added or has seen its performance improved for the following estimators:
    
    *   [`sklearn.metrics.pairwise_distances_argmin`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "sklearn.metrics.pairwise_distances_argmin")
        
    *   [`sklearn.metrics.pairwise_distances_argmin_min`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html#sklearn.metrics.pairwise_distances_argmin_min "sklearn.metrics.pairwise_distances_argmin_min")
        
    *   [`sklearn.cluster.AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
        
    *   [`sklearn.cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
        
    *   [`sklearn.cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
        
    *   [`sklearn.neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
        
    *   [`sklearn.neighbors.KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
        
    *   [`sklearn.neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
        
    *   [`sklearn.neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
        
    *   [`sklearn.neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
        
    *   [`sklearn.neighbors.NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
        
    *   [`sklearn.manifold.Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
        
    *   [`sklearn.manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
        
    *   [`sklearn.manifold.trustworthiness`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.trustworthiness.html#sklearn.manifold.trustworthiness "sklearn.manifold.trustworthiness")
        
    
    [#23604](https://github.com/scikit-learn/scikit-learn/pull/23604)
     and [#23585](https://github.com/scikit-learn/scikit-learn/pull/23585)
     by [Julien Jerphanion](https://github.com/jjerphan)
    , [Olivier Grisel](https://github.com/ogrisel)
    , and [Thomas Fan](https://github.com/thomasjpfan)
    , [#24556](https://github.com/scikit-learn/scikit-learn/pull/24556)
     by [Vincent Maladière](https://github.com/Vincent-Maladiere)
    .
    
*   Fix Systematically check the sha256 digest of dataset tarballs used in code examples in the documentation. [#24617](https://github.com/scikit-learn/scikit-learn/pull/24617)
     by [Olivier Grisel](https://github.com/ogrisel)
     and [Thomas Fan](https://github.com/thomasjpfan)
    . Thanks to [Sim4n6](https://huntr.dev/users/sim4n6)
     for the report.
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id9 "Link to this heading")

#### [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id10 "Link to this heading")

*   Enhancement Introduces [`base.ClassNamePrefixFeaturesOutMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html#sklearn.base.ClassNamePrefixFeaturesOutMixin "sklearn.base.ClassNamePrefixFeaturesOutMixin")
     and [`base.ClassNamePrefixFeaturesOutMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html#sklearn.base.ClassNamePrefixFeaturesOutMixin "sklearn.base.ClassNamePrefixFeaturesOutMixin")
     mixins that define [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     for common transformer use cases. [#24688](https://github.com/scikit-learn/scikit-learn/pull/24688)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id11 "Link to this heading")

*   API Change Rename `base_estimator` to `estimator` in [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     to improve readability and consistency. The parameter `base_estimator` is deprecated and will be removed in 1.4. [#22054](https://github.com/scikit-learn/scikit-learn/pull/22054)
     by [Kevin Roice](https://github.com/kevroi)
    .
    

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id12 "Link to this heading")

*   Efficiency [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     with `algorithm="lloyd"` is now faster and uses less memory. [#24264](https://github.com/scikit-learn/scikit-learn/pull/24264)
     by [Vincent Maladiere](https://github.com/Vincent-Maladiere)
    .
    
*   Enhancement The `predict` and `fit_predict` methods of [`cluster.OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
     now accept sparse data type for input data. [#14736](https://github.com/scikit-learn/scikit-learn/pull/14736)
     by [Hunt Zhan](https://github.com/huntzhan)
    , [#20802](https://github.com/scikit-learn/scikit-learn/pull/20802)
     by [Brandon Pokorny](https://github.com/Clickedbigfoot)
    , and [#22965](https://github.com/scikit-learn/scikit-learn/pull/22965)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Enhancement [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
     now preserves dtype for `numpy.float32` inputs. [#22968](https://github.com/scikit-learn/scikit-learn/pull/22968)
     by `Meekail Zain <micky774>`.
    
*   Enhancement [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     and [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     now accept a new `'auto'` option for `n_init` which changes the number of random initializations to one when using `init='k-means++'` for efficiency. This begins deprecation for the default values of `n_init` in the two classes and both will have their defaults changed to `n_init='auto'` in 1.4. [#23038](https://github.com/scikit-learn/scikit-learn/pull/23038)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Enhancement [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     and [`cluster.spectral_clustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")
     now propagate the `eigen_tol` parameter to all choices of `eigen_solver`. Includes a new option `eigen_tol="auto"` and begins deprecation to change the default from `eigen_tol=0` to `eigen_tol="auto"` in version 1.3. [#23210](https://github.com/scikit-learn/scikit-learn/pull/23210)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Fix [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     now supports readonly attributes when predicting. [#24258](https://github.com/scikit-learn/scikit-learn/pull/24258)
     by [Thomas Fan](https://github.com/thomasjpfan)
    
*   API Change The `affinity` attribute is now deprecated for [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     and will be renamed to `metric` in v1.4. [#23470](https://github.com/scikit-learn/scikit-learn/pull/23470)
     by [Meekail Zain](https://github.com/micky774)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id13 "Link to this heading")

*   Enhancement Introduce the new parameter `parser` in [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
    . `parser="pandas"` allows to use the very CPU and memory efficient `pandas.read_csv` parser to load dense ARFF formatted dataset files. It is possible to pass `parser="liac-arff"` to use the old LIAC parser. When `parser="auto"`, dense datasets are loaded with “pandas” and sparse datasets are loaded with “liac-arff”. Currently, `parser="liac-arff"` by default and will change to `parser="auto"` in version 1.4 [#21938](https://github.com/scikit-learn/scikit-learn/pull/21938)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Enhancement [`datasets.dump_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.dump_svmlight_file.html#sklearn.datasets.dump_svmlight_file "sklearn.datasets.dump_svmlight_file")
     is now accelerated with a Cython implementation, providing 2-4x speedups. [#23127](https://github.com/scikit-learn/scikit-learn/pull/23127)
     by [Meekail Zain](https://github.com/micky774)
    
*   Enhancement Path-like objects, such as those created with pathlib are now allowed as paths in [`datasets.load_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html#sklearn.datasets.load_svmlight_file "sklearn.datasets.load_svmlight_file")
     and [`datasets.load_svmlight_files`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_files.html#sklearn.datasets.load_svmlight_files "sklearn.datasets.load_svmlight_files")
    . [#19075](https://github.com/scikit-learn/scikit-learn/pull/19075)
     by [Carlos Ramos Carreño](https://github.com/vnmabus)
    .
    
*   Fix Make sure that [`datasets.fetch_lfw_people`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html#sklearn.datasets.fetch_lfw_people "sklearn.datasets.fetch_lfw_people")
     and [`datasets.fetch_lfw_pairs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_pairs.html#sklearn.datasets.fetch_lfw_pairs "sklearn.datasets.fetch_lfw_pairs")
     internally crop images based on the `slice_` parameter. [#24951](https://github.com/scikit-learn/scikit-learn/pull/24951)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id14 "Link to this heading")

*   Efficiency [`decomposition.FastICA.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA.fit "sklearn.decomposition.FastICA.fit")
     has been optimised w.r.t its memory footprint and runtime. [#22268](https://github.com/scikit-learn/scikit-learn/pull/22268)
     by [MohamedBsh](https://github.com/Bsh)
    .
    
*   Enhancement [`decomposition.SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")
     and [`decomposition.MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")
     now implement an `inverse_transform` function. [#23905](https://github.com/scikit-learn/scikit-learn/pull/23905)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Enhancement [`decomposition.FastICA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")
     now allows the user to select how whitening is performed through the new `whiten_solver` parameter, which supports `svd` and `eigh`. `whiten_solver` defaults to `svd` although `eigh` may be faster and more memory efficient in cases where `num_features > num_samples`. [#11860](https://github.com/scikit-learn/scikit-learn/pull/11860)
     by [Pierre Ablin](https://github.com/pierreablin)
    , [#22527](https://github.com/scikit-learn/scikit-learn/pull/22527)
     by [Meekail Zain](https://github.com/micky774)
     and [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`decomposition.LatentDirichletAllocation`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "sklearn.decomposition.LatentDirichletAllocation")
     now preserves dtype for `numpy.float32` input. [#24528](https://github.com/scikit-learn/scikit-learn/pull/24528)
     by [Takeshi Oura](https://github.com/takoika)
     and [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix Make sign of `components_` deterministic in [`decomposition.SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")
    . [#23935](https://github.com/scikit-learn/scikit-learn/pull/23935)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change The `n_iter` parameter of [`decomposition.MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")
     is deprecated and replaced by the parameters `max_iter`, `tol`, and `max_no_improvement` to be consistent with [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
    . `n_iter` will be removed in version 1.3. [#23726](https://github.com/scikit-learn/scikit-learn/pull/23726)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change The `n_features_` attribute of [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     is deprecated in favor of `n_features_in_` and will be removed in 1.4. [#24421](https://github.com/scikit-learn/scikit-learn/pull/24421)
     by [Kshitij Mathur](https://github.com/Kshitij68)
    .
    

#### [`sklearn.discriminant_analysis`](https://scikit-learn.org/stable/api/sklearn.discriminant_analysis.html#module-sklearn.discriminant_analysis "sklearn.discriminant_analysis")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-discriminant-analysis "Link to this heading")

*   Major Feature [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     now supports the [Array API](https://data-apis.org/array-api/latest/)
     for `solver="svd"`. Array API support is considered experimental and might evolve without being subjected to our usual rolling deprecation cycle policy. See [Array API support (experimental)](https://scikit-learn.org/stable/modules/array_api.html#array-api)
     for more details. [#22554](https://github.com/scikit-learn/scikit-learn/pull/22554)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Validate parameters only in `fit` and not in `__init__` for [`discriminant_analysis.QuadraticDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis "sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis")
    . [#24218](https://github.com/scikit-learn/scikit-learn/pull/24218)
     by [Stefanie Molin](https://github.com/stefmolin)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id15 "Link to this heading")

*   Major Feature [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     now support interaction constraints via the argument `interaction_cst` of their constructors. [#21020](https://github.com/scikit-learn/scikit-learn/pull/21020)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    . Using interaction constraints also makes fitting faster. [#24856](https://github.com/scikit-learn/scikit-learn/pull/24856)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Feature Adds `class_weight` to [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
    . [#22014](https://github.com/scikit-learn/scikit-learn/pull/22014)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Efficiency Improve runtime performance of [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     by avoiding data copies. [#23252](https://github.com/scikit-learn/scikit-learn/pull/23252)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
    .
    
*   Enhancement [`ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
     now accepts any kind of base estimator. [#24538](https://github.com/scikit-learn/scikit-learn/pull/24538)
     by [Guillem G Subies](https://github.com/GuillemGSubies)
    .
    
*   Enhancement Make it possible to pass the `categorical_features` parameter of [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     as feature names. [#24889](https://github.com/scikit-learn/scikit-learn/pull/24889)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Enhancement [`ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
     now supports multilabel-indicator target [#24146](https://github.com/scikit-learn/scikit-learn/pull/24146)
     by [Nicolas Peretti](https://github.com/nicoperetti)
    , [Nestor Navarro](https://github.com/nestornav)
    , [Nati Tomattis](https://github.com/natitomattis)
    , and [Vincent Maladiere](https://github.com/Vincent-Maladiere)
    .
    
*   Enhancement [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     now accept their `monotonic_cst` parameter to be passed as a dictionary in addition to the previously supported array-like format. Such dictionary have feature names as keys and one of `-1`, `0`, `1` as value to specify monotonicity constraints for each feature. [#24855](https://github.com/scikit-learn/scikit-learn/pull/24855)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Enhancement Interaction constraints for [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     can now be specified as strings for two common cases: “no\_interactions” and “pairwise” interactions. [#24849](https://github.com/scikit-learn/scikit-learn/pull/24849)
     by [Tim Head](https://github.com/betatim)
    .
    
*   Fix Fixed the issue where [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
     outputs NaN in feature importance when fitted with very small sample weight. [#20415](https://github.com/scikit-learn/scikit-learn/pull/20415)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
    .
    
*   Fix [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     no longer error when predicting on categories encoded as negative values and instead consider them a member of the “missing category”. [#24283](https://github.com/scikit-learn/scikit-learn/pull/24283)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
    , with `verbose>=1`, print detailed timing information on computing histograms and finding best splits. The time spent in the root node was previously missing and is now included in the printed information. [#24894](https://github.com/scikit-learn/scikit-learn/pull/24894)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   API Change Rename the constructor parameter `base_estimator` to `estimator` in the following classes: [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
    , [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
    , [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
    , [`ensemble.AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
    . `base_estimator` is deprecated in 1.2 and will be removed in 1.4. [#23819](https://github.com/scikit-learn/scikit-learn/pull/23819)
     by [Adrian Trujillo](https://github.com/trujillo9616)
     and [Edoardo Abati](https://github.com/EdAbati)
    .
    
*   API Change Rename the fitted attribute `base_estimator_` to `estimator_` in the following classes: [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
    , [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
    , [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
    , [`ensemble.AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
    , [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
    , [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
    , [`ensemble.RandomTreesEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")
    , [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
    . `base_estimator_` is deprecated in 1.2 and will be removed in 1.4. [#23819](https://github.com/scikit-learn/scikit-learn/pull/23819)
     by [Adrian Trujillo](https://github.com/trujillo9616)
     and [Edoardo Abati](https://github.com/EdAbati)
    .
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id16 "Link to this heading")

*   Fix Fix a bug in [`feature_selection.mutual_info_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html#sklearn.feature_selection.mutual_info_regression "sklearn.feature_selection.mutual_info_regression")
     and [`feature_selection.mutual_info_classif`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#sklearn.feature_selection.mutual_info_classif "sklearn.feature_selection.mutual_info_classif")
    , where the continuous features in `X` should be scaled to a unit variance independently if the target `y` is continuous or discrete. [#24747](https://github.com/scikit-learn/scikit-learn/pull/24747)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    

#### [`sklearn.gaussian_process`](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#module-sklearn.gaussian_process "sklearn.gaussian_process")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-gaussian-process "Link to this heading")

*   Fix Fix [`gaussian_process.kernels.Matern`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern "sklearn.gaussian_process.kernels.Matern")
     gradient computation with `nu=0.5` for PyPy (and possibly other non CPython interpreters). [#24245](https://github.com/scikit-learn/scikit-learn/pull/24245)
     by [Loïc Estève](https://github.com/lesteve)
    .
    
*   Fix The `fit` method of [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
     will not modify the input X in case a custom kernel is used, with a `diag` method that returns part of the input X. [#24405](https://github.com/scikit-learn/scikit-learn/pull/24405)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-impute "Link to this heading")

*   Enhancement Added `keep_empty_features` parameter to [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
    , [`impute.KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
     and [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
    , preventing removal of features containing only missing values when transforming. [#16695](https://github.com/scikit-learn/scikit-learn/pull/16695)
     by [Vitor Santa Rosa](https://github.com/vitorsrg)
    .
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id17 "Link to this heading")

*   Major Feature Extended [`inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
     and [`inspection.PartialDependenceDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "sklearn.inspection.PartialDependenceDisplay")
     to handle categorical features. [#18298](https://github.com/scikit-learn/scikit-learn/pull/18298)
     by [Madhura Jayaratne](https://github.com/madhuracj)
     and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
     now raises error if input data is not 2-dimensional. [#25077](https://github.com/scikit-learn/scikit-learn/pull/25077)
     by [Arturo Amor](https://github.com/ArturoAmorQ)
    .
    

#### [`sklearn.kernel_approximation`](https://scikit-learn.org/stable/api/sklearn.kernel_approximation.html#module-sklearn.kernel_approximation "sklearn.kernel_approximation")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-kernel-approximation "Link to this heading")

*   Enhancement [`kernel_approximation.RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
     now preserves dtype for `numpy.float32` inputs. [#24317](https://github.com/scikit-learn/scikit-learn/pull/24317)
     by `Tim Head <betatim>`.
    
*   Enhancement [`kernel_approximation.SkewedChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.SkewedChi2Sampler.html#sklearn.kernel_approximation.SkewedChi2Sampler "sklearn.kernel_approximation.SkewedChi2Sampler")
     now preserves dtype for `numpy.float32` inputs. [#24350](https://github.com/scikit-learn/scikit-learn/pull/24350)
     by [Rahil Parikh](https://github.com/rprkh)
    .
    
*   Enhancement [`kernel_approximation.RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
     now accepts `'scale'` option for parameter `gamma`. [#24755](https://github.com/scikit-learn/scikit-learn/pull/24755)
     by [Hleb Levitski](https://github.com/glevv)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id18 "Link to this heading")

*   Enhancement [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    , [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
    , [`linear_model.GammaRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html#sklearn.linear_model.GammaRegressor "sklearn.linear_model.GammaRegressor")
    , [`linear_model.PoissonRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")
     and [`linear_model.TweedieRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html#sklearn.linear_model.TweedieRegressor "sklearn.linear_model.TweedieRegressor")
     got a new solver `solver="newton-cholesky"`. This is a 2nd order (Newton) optimisation routine that uses a Cholesky decomposition of the hessian matrix. When `n_samples >> n_features`, the `"newton-cholesky"` solver has been observed to converge both faster and to a higher precision solution than the `"lbfgs"` solver on problems with one-hot encoded categorical variables with some rare categorical levels. [#24637](https://github.com/scikit-learn/scikit-learn/pull/24637)
     and [#24767](https://github.com/scikit-learn/scikit-learn/pull/24767)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Enhancement [`linear_model.GammaRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html#sklearn.linear_model.GammaRegressor "sklearn.linear_model.GammaRegressor")
    , [`linear_model.PoissonRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")
     and [`linear_model.TweedieRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html#sklearn.linear_model.TweedieRegressor "sklearn.linear_model.TweedieRegressor")
     can reach higher precision with the lbfgs solver, in particular when `tol` is set to a tiny value. Moreover, `verbose` is now properly propagated to L-BFGS-B. [#23619](https://github.com/scikit-learn/scikit-learn/pull/23619)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Fix [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     and [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     will raise an error when all the validation samples have zero sample weight. [#23275](https://github.com/scikit-learn/scikit-learn/pull/23275)
     by `Zhehao Liu <MaxwellLZH>`.
    
*   Fix [`linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
     no longer performs parameter validation in the constructor. All validation is now handled in `fit()` and `partial_fit()`. [#24433](https://github.com/scikit-learn/scikit-learn/pull/24433)
     by [Yogendrasingh](https://github.com/iofall)
    , [Arisa Y.](https://github.com/arisayosh)
     and [Tim Head](https://github.com/betatim)
    .
    
*   Fix Fix average loss calculation when early stopping is enabled in [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     and [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    . Also updated the condition for early stopping accordingly. [#23798](https://github.com/scikit-learn/scikit-learn/pull/23798)
     by [Harsh Agrawal](https://github.com/Harsh14901)
    .
    
*   API Change The default value for the `solver` parameter in [`linear_model.QuantileRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
     will change from `"interior-point"` to `"highs"` in version 1.4. [#23637](https://github.com/scikit-learn/scikit-learn/pull/23637)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change String option `"none"` is deprecated for `penalty` argument in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    , and will be removed in version 1.4. Use `None` instead. [#23877](https://github.com/scikit-learn/scikit-learn/pull/23877)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
    .
    
*   API Change The default value of `tol` was changed from `1e-3` to `1e-4` for [`linear_model.ridge_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html#sklearn.linear_model.ridge_regression "sklearn.linear_model.ridge_regression")
    , [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     and [`linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
    . [#24465](https://github.com/scikit-learn/scikit-learn/pull/24465)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    

#### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id19 "Link to this heading")

*   Feature Adds option to use the normalized stress in [`manifold.MDS`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
    . This is enabled by setting the new `normalize` parameter to `True`. [#10168](https://github.com/scikit-learn/scikit-learn/pull/10168)
     by [Łukasz Borchmann](https://github.com/Borchmann)
    , [#12285](https://github.com/scikit-learn/scikit-learn/pull/12285)
     by [Matthias Miltenberger](https://github.com/mattmilten)
    , [#13042](https://github.com/scikit-learn/scikit-learn/pull/13042)
     by [Matthieu Parizy](https://github.com/matthieu-pa)
    , [#18094](https://github.com/scikit-learn/scikit-learn/pull/18094)
     by [Roth E Conrad](https://github.com/rotheconrad)
     and [#22562](https://github.com/scikit-learn/scikit-learn/pull/22562)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Enhancement Adds `eigen_tol` parameter to [`manifold.SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
    . Both [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
     and [`manifold.SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
     now propagate `eigen_tol` to all choices of `eigen_solver`. Includes a new option `eigen_tol="auto"` and begins deprecation to change the default from `eigen_tol=0` to `eigen_tol="auto"` in version 1.3. [#23210](https://github.com/scikit-learn/scikit-learn/pull/23210)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Enhancement [`manifold.Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
     now preserves dtype for `np.float32` inputs. [#24714](https://github.com/scikit-learn/scikit-learn/pull/24714)
     by [Rahil Parikh](https://github.com/rprkh)
    .
    
*   API Change Added an `"auto"` option to the `normalized_stress` argument in [`manifold.MDS`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
     and [`manifold.smacof`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.smacof.html#sklearn.manifold.smacof "sklearn.manifold.smacof")
    . Note that `normalized_stress` is only valid for non-metric MDS, therefore the `"auto"` option enables `normalized_stress` when `metric=False` and disables it when `metric=True`. `"auto"` will become the default value for `normalized_stress` in version 1.4. [#23834](https://github.com/scikit-learn/scikit-learn/pull/23834)
     by [Meekail Zain](https://github.com/micky774)
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-metrics "Link to this heading")

*   Feature [`metrics.ConfusionMatrixDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_estimator "sklearn.metrics.ConfusionMatrixDisplay.from_estimator")
    , [`metrics.ConfusionMatrixDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_predictions "sklearn.metrics.ConfusionMatrixDisplay.from_predictions")
    , and [`metrics.ConfusionMatrixDisplay.plot`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.plot "sklearn.metrics.ConfusionMatrixDisplay.plot")
     accepts a `text_kw` parameter which is passed to matplotlib’s `text` function. [#24051](https://github.com/scikit-learn/scikit-learn/pull/24051)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature [`metrics.class_likelihood_ratios`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#sklearn.metrics.class_likelihood_ratios "sklearn.metrics.class_likelihood_ratios")
     is added to compute the positive and negative likelihood ratios derived from the confusion matrix of a binary classification problem. [#22518](https://github.com/scikit-learn/scikit-learn/pull/22518)
     by [Arturo Amor](https://github.com/ArturoAmorQ)
    .
    
*   Feature Add [`metrics.PredictionErrorDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay "sklearn.metrics.PredictionErrorDisplay")
     to plot residuals vs predicted and actual vs predicted to qualitatively assess the behavior of a regressor. The display can be created with the class methods [`metrics.PredictionErrorDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_estimator "sklearn.metrics.PredictionErrorDisplay.from_estimator")
     and [`metrics.PredictionErrorDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")
    . [#18020](https://github.com/scikit-learn/scikit-learn/pull/18020)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Feature [`metrics.roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
     now supports micro-averaging (`average="micro"`) for the One-vs-Rest multiclass case (`multi_class="ovr"`). [#24338](https://github.com/scikit-learn/scikit-learn/pull/24338)
     by [Arturo Amor](https://github.com/ArturoAmorQ)
    .
    
*   Enhancement Adds an `"auto"` option to `eps` in [`metrics.log_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
    . This option will automatically set the `eps` value depending on the data type of `y_pred`. In addition, the default value of `eps` is changed from `1e-15` to the new `"auto"` option. [#24354](https://github.com/scikit-learn/scikit-learn/pull/24354)
     by [Safiuddin Khaja](https://github.com/Safikh)
     and [gsiisg](https://github.com/gsiisg)
    .
    
*   Fix Allows `csr_matrix` as input for parameter: `y_true` of the [`metrics.label_ranking_average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html#sklearn.metrics.label_ranking_average_precision_score "sklearn.metrics.label_ranking_average_precision_score")
     metric. [#23442](https://github.com/scikit-learn/scikit-learn/pull/23442)
     by [Sean Atukorala](https://github.com/ShehanAT)
    
*   Fix [`metrics.ndcg_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html#sklearn.metrics.ndcg_score "sklearn.metrics.ndcg_score")
     will now trigger a warning when the `y_true` value contains a negative value. Users may still use negative values, but the result may not be between 0 and 1. Starting in v1.4, passing in negative values for `y_true` will raise an error. [#22710](https://github.com/scikit-learn/scikit-learn/pull/22710)
     by [Conroy Trinh](https://github.com/trinhcon)
     and [#23461](https://github.com/scikit-learn/scikit-learn/pull/23461)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Fix [`metrics.log_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
     with `eps=0` now returns a correct value of 0 or `np.inf` instead of `nan` for predictions at the boundaries (0 or 1). It also accepts integer input. [#24365](https://github.com/scikit-learn/scikit-learn/pull/24365)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   API Change The parameter `sum_over_features` of [`metrics.pairwise.manhattan_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html#sklearn.metrics.pairwise.manhattan_distances "sklearn.metrics.pairwise.manhattan_distances")
     is deprecated and will be removed in 1.4. [#24630](https://github.com/scikit-learn/scikit-learn/pull/24630)
     by [Rushil Desai](https://github.com/rusdes)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id20 "Link to this heading")

*   Feature Added the class [`model_selection.LearningCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay "sklearn.model_selection.LearningCurveDisplay")
     that allows to make easy plotting of learning curves obtained by the function [`model_selection.learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
    . [#24084](https://github.com/scikit-learn/scikit-learn/pull/24084)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix For all `SearchCV` classes and scipy >= 1.10, rank corresponding to a nan score is correctly set to the maximum possible rank, rather than `np.iinfo(np.int32).min`. [#24141](https://github.com/scikit-learn/scikit-learn/pull/24141)
     by [Loïc Estève](https://github.com/lesteve)
    .
    
*   Fix In both [`model_selection.HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
     and [`model_selection.HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
     parameter combinations with a NaN score now share the lowest rank. [#24539](https://github.com/scikit-learn/scikit-learn/pull/24539)
     by [Tim Head](https://github.com/betatim)
    .
    
*   Fix For [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     ranks corresponding to nan scores will all be set to the maximum possible rank. [#24543](https://github.com/scikit-learn/scikit-learn/pull/24543)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.multioutput`](https://scikit-learn.org/stable/api/sklearn.multioutput.html#module-sklearn.multioutput "sklearn.multioutput")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-multioutput "Link to this heading")

*   Feature Added boolean `verbose` flag to classes: [`multioutput.ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
     and [`multioutput.RegressorChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.RegressorChain.html#sklearn.multioutput.RegressorChain "sklearn.multioutput.RegressorChain")
    . [#23977](https://github.com/scikit-learn/scikit-learn/pull/23977)
     by [Eric Fiegel](https://github.com/efiegel)
    , [Chiara Marmo](https://github.com/cmarmo)
    , [Lucy Liu](https://github.com/lucyleeow)
    , and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.naive_bayes`](https://scikit-learn.org/stable/api/sklearn.naive_bayes.html#module-sklearn.naive_bayes "sklearn.naive_bayes")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-naive-bayes "Link to this heading")

*   Feature Add methods `predict_joint_log_proba` to all naive Bayes classifiers. [#23683](https://github.com/scikit-learn/scikit-learn/pull/23683)
     by [Andrey Melnik](https://github.com/avm19)
    .
    
*   Enhancement A new parameter `force_alpha` was added to [`naive_bayes.BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
    , [`naive_bayes.ComplementNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html#sklearn.naive_bayes.ComplementNB "sklearn.naive_bayes.ComplementNB")
    , [`naive_bayes.CategoricalNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html#sklearn.naive_bayes.CategoricalNB "sklearn.naive_bayes.CategoricalNB")
    , and [`naive_bayes.MultinomialNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB "sklearn.naive_bayes.MultinomialNB")
    , allowing user to set parameter alpha to a very small number, greater or equal 0, which was earlier automatically changed to `1e-10` instead. [#16747](https://github.com/scikit-learn/scikit-learn/pull/16747)
     by [@arka204](https://github.com/arka204)
    , [#18805](https://github.com/scikit-learn/scikit-learn/pull/18805)
     by [@hongshaoyang](https://github.com/hongshaoyang)
    , [#22269](https://github.com/scikit-learn/scikit-learn/pull/22269)
     by [Meekail Zain](https://github.com/micky774)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-neighbors "Link to this heading")

*   Feature Adds new function [`neighbors.sort_graph_by_row_values`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html#sklearn.neighbors.sort_graph_by_row_values "sklearn.neighbors.sort_graph_by_row_values")
     to sort a CSR sparse graph such that each row is stored with increasing values. This is useful to improve efficiency when using precomputed sparse distance matrices in a variety of estimators and avoid an `EfficiencyWarning`. [#23139](https://github.com/scikit-learn/scikit-learn/pull/23139)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Efficiency [`neighbors.NearestCentroid`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")
     is faster and requires less memory as it better leverages CPUs’ caches to compute predictions. [#24645](https://github.com/scikit-learn/scikit-learn/pull/24645)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Enhancement [`neighbors.KernelDensity`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
     bandwidth parameter now accepts definition using Scott’s and Silverman’s estimation methods. [#10468](https://github.com/scikit-learn/scikit-learn/pull/10468)
     by [Ruben](https://github.com/icfly2)
     and [#22993](https://github.com/scikit-learn/scikit-learn/pull/22993)
     by [Jovan Stojanovic](https://github.com/jovan-stojanovic)
    .
    
*   Enhancement `neighbors.NeighborsBase` now accepts Minkowski semi-metric (i.e. when 0<p<1 for `metric="minkowski"`) for `algorithm="auto"` or `algorithm="brute"`. [#24750](https://github.com/scikit-learn/scikit-learn/pull/24750)
     by [Rudresh Veerkhare](https://github.com/RudreshVeerkhare)
    
*   Fix [`neighbors.NearestCentroid`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")
     now raises an informative error message at fit-time instead of failing with a low-level error message at predict-time. [#23874](https://github.com/scikit-learn/scikit-learn/pull/23874)
     by [Juan Gomez](https://github.com/2357juan)
    .
    
*   Fix Set `n_jobs=None` by default (instead of `1`) for [`neighbors.KNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
     and [`neighbors.RadiusNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer "sklearn.neighbors.RadiusNeighborsTransformer")
    . [#24075](https://github.com/scikit-learn/scikit-learn/pull/24075)
     by [Valentin Laurent](https://github.com/Valentin-Laurent)
    .
    
*   Enhancement [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
     now preserves dtype for `numpy.float32` inputs. [#22665](https://github.com/scikit-learn/scikit-learn/pull/22665)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    

#### [`sklearn.neural_network`](https://scikit-learn.org/stable/api/sklearn.neural_network.html#module-sklearn.neural_network "sklearn.neural_network")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id21 "Link to this heading")

*   Fix [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     and [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
     always expose the parameters `best_loss_`, `validation_scores_`, and `best_validation_score_`. `best_loss_` is set to `None` when `early_stopping=True`, while `validation_scores_` and `best_validation_score_` are set to `None` when `early_stopping=False`. [#24683](https://github.com/scikit-learn/scikit-learn/pull/24683)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-pipeline "Link to this heading")

*   Enhancement [`pipeline.FeatureUnion.get_feature_names_out`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion.get_feature_names_out "sklearn.pipeline.FeatureUnion.get_feature_names_out")
     can now be used when one of the transformers in the [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     is `"passthrough"`. [#24058](https://github.com/scikit-learn/scikit-learn/pull/24058)
     by [Diederik Perdok](https://github.com/diederikwp)
    
*   Enhancement The [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     class now has a `named_transformers` attribute for accessing transformers by name. [#20331](https://github.com/scikit-learn/scikit-learn/pull/20331)
     by [Christopher Flynn](https://github.com/crflynn)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id22 "Link to this heading")

*   Enhancement [`preprocessing.FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
     will always try to set `n_features_in_` and `feature_names_in_` regardless of the `validate` parameter. [#23993](https://github.com/scikit-learn/scikit-learn/pull/23993)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`preprocessing.LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder")
     correctly encodes NaNs in `transform`. [#22629](https://github.com/scikit-learn/scikit-learn/pull/22629)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change The `sparse` parameter of [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     is now deprecated and will be removed in version 1.4. Use `sparse_output` instead. [#24412](https://github.com/scikit-learn/scikit-learn/pull/24412)
     by [Rushil Desai](https://github.com/rusdes)
    .
    

#### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#sklearn-svm "Link to this heading")

*   API Change The `class_weight_` attribute is now deprecated for [`svm.NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
    , [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
    , [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
    . [#22898](https://github.com/scikit-learn/scikit-learn/pull/22898)
     by [Meekail Zain](https://github.com/micky774)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id23 "Link to this heading")

*   Enhancement [`tree.plot_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree")
    , [`tree.export_graphviz`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz "sklearn.tree.export_graphviz")
     now uses a lower case `x[i]` to represent feature `i`. [#23480](https://github.com/scikit-learn/scikit-learn/pull/23480)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.2.html#id24 "Link to this heading")

*   Feature A new module exposes development tools to discover estimators (i.e. [`utils.discovery.all_estimators`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.discovery.all_estimators.html#sklearn.utils.discovery.all_estimators "sklearn.utils.discovery.all_estimators")
    ), displays (i.e. [`utils.discovery.all_displays`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.discovery.all_displays.html#sklearn.utils.discovery.all_displays "sklearn.utils.discovery.all_displays")
    ) and functions (i.e. [`utils.discovery.all_functions`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.discovery.all_functions.html#sklearn.utils.discovery.all_functions "sklearn.utils.discovery.all_functions")
    ) in scikit-learn. [#21469](https://github.com/scikit-learn/scikit-learn/pull/21469)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Enhancement [`utils.extmath.randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
     now accepts an argument, `lapack_svd_driver`, to specify the lapack driver used in the internal deterministic SVD used by the randomized SVD algorithm. [#20617](https://github.com/scikit-learn/scikit-learn/pull/20617)
     by [Srinath Kailasa](https://github.com/skailasa)
    
*   Enhancement [`utils.validation.column_or_1d`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.column_or_1d.html#sklearn.utils.validation.column_or_1d "sklearn.utils.validation.column_or_1d")
     now accepts a `dtype` parameter to specific `y`’s dtype. [#22629](https://github.com/scikit-learn/scikit-learn/pull/22629)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement `utils.extmath.cartesian` now accepts arrays with different `dtype` and will cast the output to the most permissive `dtype`. [#25067](https://github.com/scikit-learn/scikit-learn/pull/25067)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`utils.multiclass.type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
     now properly handles sparse matrices. [#14862](https://github.com/scikit-learn/scikit-learn/pull/14862)
     by [Léonard Binet](https://github.com/leonardbinet)
    .
    
*   Fix HTML representation no longer errors when an estimator class is a value in `get_params`. [#24512](https://github.com/scikit-learn/scikit-learn/pull/24512)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     now takes into account the `requires_positive_X` tag correctly. [#24667](https://github.com/scikit-learn/scikit-learn/pull/24667)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     now supports Pandas Series with `pd.NA` by raising a better error message or returning a compatible `ndarray`. [#25080](https://github.com/scikit-learn/scikit-learn/pull/25080)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change The extra keyword parameters of [`utils.extmath.density`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.density.html#sklearn.utils.extmath.density "sklearn.utils.extmath.density")
     are deprecated and will be removed in 1.4. [#24523](https://github.com/scikit-learn/scikit-learn/pull/24523)
     by [Mia Bajic](https://github.com/clytaemnestra)
    .
    

Code and documentation contributors

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 1.1, including:

2357juan, 3lLobo, Adam J. Stewart, Adam Kania, Adam Li, Aditya Anulekh, Admir Demiraj, adoublet, Adrin Jalali, Ahmedbgh, Aiko, Akshita Prasanth, Ala-Na, Alessandro Miola, Alex, Alexandr, Alexandre Perez-Lebel, Alex Buzenet, Ali H. El-Kassas, aman kumar, Amit Bera, András Simon, Andreas Grivas, Andreas Mueller, Andrew Wang, angela-maennel, Aniket Shirsat, Anthony22-dev, Antony Lee, anupam, Apostolos Tsetoglou, Aravindh R, Artur Hermano, Arturo Amor, as-90, ashah002, Ashwin Mathur, avm19, Azaria Gebremichael, b0rxington, Badr MOUFAD, Bardiya Ak, Bartłomiej Gońda, BdeGraaff, Benjamin Bossan, Benjamin Carter, berkecanrizai, Bernd Fritzke, Bhoomika, Biswaroop Mitra, Brandon TH Chen, Brett Cannon, Bsh, cache-missing, carlo, Carlos Ramos Carreño, ceh, chalulu, Changyao Chen, Charles Zablit, Chiara Marmo, Christian Lorentzen, Christian Ritter, Christian Veenhuis, christianwaldmann, Christine P. Chai, Claudio Salvatore Arcidiacono, Clément Verrier, crispinlogan, Da-Lan, DanGonite57, Daniela Fernandes, DanielGaerber, darioka, Darren Nguyen, davidblnc, david-cortes, David Gilbertson, David Poznik, Dayne, Dea María Léon, Denis, Dev Khant, Dhanshree Arora, Diadochokinetic, diederikwp, Dimitri Papadopoulos Orfanos, Dimitris Litsidis, drewhogg, Duarte OC, Dwight Lindquist, Eden Brekke, Edern, Edoardo Abati, Eleanore Denies, EliaSchiavon, Emir, ErmolaevPA, Fabrizio Damicelli, fcharras, Felipe Siola, Flynn, francesco-tuveri, Franck Charras, ftorres16, Gael Varoquaux, Geevarghese George, genvalen, GeorgiaMayDay, Gianr Lazz, Hleb Levitski, Glòria Macià Muñoz, Guillaume Lemaitre, Guillem García Subies, Guitared, gunesbayir, Haesun Park, Hansin Ahuja, Hao Chun Chang, Harsh Agrawal, harshit5674, hasan-yaman, henrymooresc, Henry Sorsky, Hristo Vrigazov, htsedebenham, humahn, i-aki-y, Ian Thompson, Ido M, Iglesys, Iliya Zhechev, Irene, ivanllt, Ivan Sedykh, Jack McIvor, jakirkham, JanFidor, Jason G, Jérémie du Boisberranger, Jiten Sidhpura, jkarolczak, João David, JohnathanPi, John Koumentis, John P, John Pangas, johnthagen, Jordan Fleming, Joshua Choo Yun Keat, Jovan Stojanovic, Juan Carlos Alfaro Jiménez, juanfe88, Juan Felipe Arias, JuliaSchoepp, Julien Jerphanion, jygerardy, ka00ri, Kanishk Sachdev, Kanissh, Kaushik Amar Das, Kendall, Kenneth Prabakaran, Kento Nozawa, kernc, Kevin Roice, Kian Eliasi, Kilian Kluge, Kilian Lieret, Kirandevraj, Kraig, krishna kumar, krishna vamsi, Kshitij Kapadni, Kshitij Mathur, Lauren Burke, Léonard Binet, lingyi1110, Lisa Casino, Logan Thomas, Loic Esteve, Luciano Mantovani, Lucy Liu, Maascha, Madhura Jayaratne, madinak, Maksym, Malte S. Kurz, Mansi Agrawal, Marco Edward Gorelli, Marco Wurps, Maren Westermann, Maria Telenczuk, Mario Kostelac, martin-kokos, Marvin Krawutschke, Masanori Kanazu, mathurinm, Matt Haberland, mauroantonioserrano, Max Halford, Maxi Marufo, maximeSaur, Maxim Smolskiy, Maxwell, m. bou, Meekail Zain, Mehgarg, mehmetcanakbay, Mia Bajić, Michael Flaks, Michael Hornstein, Michel de Ruiter, Michelle Paradis, Mikhail Iljin, Misa Ogura, Moritz Wilksch, mrastgoo, Naipawat Poolsawat, Naoise Holohan, Nass, Nathan Jacobi, Nawazish Alam, Nguyễn Văn Diễn, Nicola Fanelli, Nihal Thukarama Rao, Nikita Jare, nima10khodaveisi, Nima Sarajpoor, nitinramvelraj, NNLNR, npache, Nwanna-Joseph, Nymark Kho, o-holman, Olivier Grisel, Olle Lukowski, Omar Hassoun, Omar Salman, osman tamer, ouss1508, Oyindamola Olatunji, PAB, Pandata, partev, Paulo Sergio Soares, Petar Mlinarić, Peter Jansson, Peter Steinbach, Philipp Jung, Piet Brömmel, Pooja M, Pooja Subramaniam, priyam kakati, puhuk, Rachel Freeland, Rachit Keerti Das, Rafal Wojdyla, Raghuveer Bhat, Rahil Parikh, Ralf Gommers, ram vikram singh, Ravi Makhija, Rehan Guha, Reshama Shaikh, Richard Klima, Rob Crockett, Robert Hommes, Robert Juergens, Robin Lenz, Rocco Meli, Roman4oo, Ross Barnowski, Rowan Mankoo, Rudresh Veerkhare, Rushil Desai, Sabri Monaf Sabri, Safikh, Safiuddin Khaja, Salahuddin, Sam Adam Day, Sandra Yojana Meneses, Sandro Ephrem, Sangam, SangamSwadik, SANJAI\_3, SarahRemus, Sashka Warner, SavkoMax, Scott Gigante, Scott Gustafson, Sean Atukorala, sec65, SELEE, seljaks, Shady el Gewily, Shane, shellyfung, Shinsuke Mori, Shiva chauhan, Shoaib Khan, Shogo Hida, Shrankhla Srivastava, Shuangchi He, Simon, sonnivs, Sortofamudkip, Srinath Kailasa, Stanislav (Stanley) Modrak, Stefanie Molin, stellalin7, Stéphane Collot, Steven Van Vaerenbergh, Steve Schmerler, Sven Stehle, Tabea Kossen, TheDevPanda, the-syd-sre, Thijs van Weezel, Thomas Bonald, Thomas Germer, Thomas J. Fan, Ti-Ion, Tim Head, Timofei Kornev, toastedyeast, Tobias Pitters, Tom Dupré la Tour, tomiock, Tom Mathews, Tom McTiernan, tspeng, Tyler Egashira, Valentin Laurent, Varun Jain, Vera Komeyer, Vicente Reyes-Puerta, Vinayak Mehta, Vincent M, Vishal, Vyom Pathak, wattai, wchathura, WEN Hao, William M, x110, Xiao Yuan, Xunius, yanhong-zhao-ef, Yusuf Raji, Z Adil Khwaja, zeeshan lone

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)