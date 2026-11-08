[Skip to main content](https://scikit-learn.org/stable/whats_new/v1.4.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v1.4.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v1.4.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v1.4.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v1.4.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v1.4.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v1.4.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v1.4.html)

Collapse Sidebar Expand Sidebar

Version 1.4[#](https://scikit-learn.org/stable/whats_new/v1.4.html#version-1-4 "Link to this heading")

=======================================================================================================

For a short description of the main highlights of the release, please refer to [Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html#sphx-glr-auto-examples-release-highlights-plot-release-highlights-1-4-0-py)
.

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 1.4.2[#](https://scikit-learn.org/stable/whats_new/v1.4.html#version-1-4-2 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**April 2024**

This release only includes support for numpy 2.

Version 1.4.1[#](https://scikit-learn.org/stable/whats_new/v1.4.html#version-1-4-1 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**February 2024**

### Changed models[#](https://scikit-learn.org/stable/whats_new/v1.4.html#changed-models "Link to this heading")

*   API Change The `tree_.value` attribute in [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
     and [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
     changed from a weighted absolute count of number of samples to a weighted fraction of the total number of samples. [#27639](https://github.com/scikit-learn/scikit-learn/pull/27639)
     by [Samuel Ronsin](https://github.com/samronsin)
    .
    

### Metadata Routing[#](https://scikit-learn.org/stable/whats_new/v1.4.html#metadata-routing "Link to this heading")

*   Fix Fix routing issue with [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     when used inside another meta-estimator. [#28188](https://github.com/scikit-learn/scikit-learn/pull/28188)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Fix No error is raised when no metadata is passed to a metaestimator that includes a sub-estimator which doesn’t support metadata routing. [#28256](https://github.com/scikit-learn/scikit-learn/pull/28256)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Fix Fix [`multioutput.MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")
     and [`multioutput.MultiOutputClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier")
     to work with estimators that don’t consume any metadata when metadata routing is enabled. [#28240](https://github.com/scikit-learn/scikit-learn/pull/28240)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

### DataFrame Support[#](https://scikit-learn.org/stable/whats_new/v1.4.html#dataframe-support "Link to this heading")

*   Enhancement Fix Pandas and Polars dataframe are validated directly without ducktyping checks. [#28195](https://github.com/scikit-learn/scikit-learn/pull/28195)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

### Changes impacting many modules[#](https://scikit-learn.org/stable/whats_new/v1.4.html#changes-impacting-many-modules "Link to this heading")

*   Efficiency Fix Partial revert of [#28191](https://github.com/scikit-learn/scikit-learn/pull/28191)
     to avoid a performance regression for estimators relying on euclidean pairwise computation with sparse matrices. The impacted estimators are:
    
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
        
    
    [#28235](https://github.com/scikit-learn/scikit-learn/pull/28235)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Fix Fixes a bug for all scikit-learn transformers when using `set_output` with `transform` set to `pandas` or `polars`. The bug could lead to wrong naming of the columns of the returned dataframe. [#28262](https://github.com/scikit-learn/scikit-learn/pull/28262)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix When users try to use a method in [`StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
    , [`StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
    , [`StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
    , [`SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
    , [`RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
    , [`SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
    , [`OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
    , [`OutputCodeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier")
     or [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
     that their sub-estimators don’t implement, the `AttributeError` now reraises in the traceback. [#28167](https://github.com/scikit-learn/scikit-learn/pull/28167)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.4.html#changelog "Link to this heading")

#### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-calibration "Link to this heading")

*   Fix `calibration.CalibratedClassifierCV` supports [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
     with float32 output from the inner estimator. [#28247](https://github.com/scikit-learn/scikit-learn/pull/28247)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-cluster "Link to this heading")

*   Fix [`cluster.AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
     now avoids assigning multiple different clusters for equal points. [#28121](https://github.com/scikit-learn/scikit-learn/pull/28121)
     by [Pietro Peterlongo](https://github.com/pietroppeter)
     and [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    
*   Fix Avoid infinite loop in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     when the number of clusters is larger than the number of non-duplicate samples. [#28165](https://github.com/scikit-learn/scikit-learn/pull/28165)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-compose "Link to this heading")

*   Fix [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     now transforms into a polars dataframe when `verbose_feature_names_out=True` and the transformers internally used several times the same columns. Previously, it would raise a due to duplicated column names. [#28262](https://github.com/scikit-learn/scikit-learn/pull/28262)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-ensemble "Link to this heading")

*   Fix `HistGradientBoostingClassifier` and `HistGradientBoostingRegressor` when fitted on `pandas` `DataFrame` with extension dtypes, for example `pd.Int64Dtype` [#28385](https://github.com/scikit-learn/scikit-learn/pull/28385)
     by [Loïc Estève](https://github.com/lesteve)
    .
    
*   Fix Fixes error message raised by [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     when the target is multilabel or multiclass-multioutput in a DataFrame format. [#27702](https://github.com/scikit-learn/scikit-learn/pull/27702)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-impute "Link to this heading")

*   Fix : [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     now raises an error in `.fit` and `.transform` if `fill_value` can not be cast to input value dtype with `casting='same_kind'`. [#28365](https://github.com/scikit-learn/scikit-learn/pull/28365)
     by [Leo Grinsztajn](https://github.com/LeoGrin)
    .
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-inspection "Link to this heading")

*   Fix [`inspection.permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
     now handles properly `sample_weight` together with subsampling (i.e. `max_features` < 1.0). [#28184](https://github.com/scikit-learn/scikit-learn/pull/28184)
     by [Michael Mayer](https://github.com/mayer79)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-linear-model "Link to this heading")

*   Fix [`linear_model.ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
     now handles pandas input types for `predict(X, return_std=True)`. [#28377](https://github.com/scikit-learn/scikit-learn/pull/28377)
     by [Eddie Bergman](https://github.com/eddiebergman)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-preprocessing "Link to this heading")

*   Fix make [`preprocessing.FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
     more lenient and overwrite output column names with the `get_feature_names_out` in the following cases: (i) the input and output column names remain the same (happen when using NumPy `ufunc`); (ii) the input column names are numbers; (iii) the output will be set to Pandas or Polars dataframe. [#28241](https://github.com/scikit-learn/scikit-learn/pull/28241)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`preprocessing.FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
     now also warns when `set_output` is called with `transform="polars"` and `func` does not return a Polars dataframe or `feature_names_out` is not specified. [#28263](https://github.com/scikit-learn/scikit-learn/pull/28263)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`preprocessing.TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
     no longer fails when `target_type="continuous"` and the input is read-only. In particular, it now works with pandas copy-on-write mode enabled. [#28233](https://github.com/scikit-learn/scikit-learn/pull/28233)
     by [John Hopfensperger](https://github.com/s-banach)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-tree "Link to this heading")

*   Fix [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
     and [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
     are handling missing values properly. The internal criterion was not initialized when no missing values were present in the data, leading to potentially wrong criterion values. [#28295](https://github.com/scikit-learn/scikit-learn/pull/28295)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
     and [#28327](https://github.com/scikit-learn/scikit-learn/pull/28327)
     by [Adam Li](https://github.com/adam2392)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-utils "Link to this heading")

*   Enhancement Fix [`utils.metaestimators.available_if`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metaestimators.available_if.html#sklearn.utils.metaestimators.available_if "sklearn.utils.metaestimators.available_if")
     now reraises the error from the `check` function as the cause of the `AttributeError`. [#28198](https://github.com/scikit-learn/scikit-learn/pull/28198)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`utils._safe_indexing`](https://scikit-learn.org/stable/modules/generated/sklearn.utils._safe_indexing.html#sklearn.utils._safe_indexing "sklearn.utils._safe_indexing")
     now raises a `ValueError` when `X` is a Python list and `axis=1`, as documented in the docstring. [#28222](https://github.com/scikit-learn/scikit-learn/pull/28222)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

Version 1.4.0[#](https://scikit-learn.org/stable/whats_new/v1.4.html#version-1-4-0 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**January 2024**

### Changed models[#](https://scikit-learn.org/stable/whats_new/v1.4.html#id1 "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   Efficiency [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     now have much better convergence for solvers `"lbfgs"` and `"newton-cg"`. Both solvers can now reach much higher precision for the coefficients depending on the specified `tol`. Additionally, lbfgs can make better use of `tol`, i.e., stop sooner or reach higher precision. Note: The lbfgs is the default solver, so this change might affect many models. This change also means that with this new version of scikit-learn, the resulting coefficients `coef_` and `intercept_` of your models will change for these two solvers (when fit on the same data again). The amount of change depends on the specified `tol`, for small values you will get more precise results. [#26721](https://github.com/scikit-learn/scikit-learn/pull/26721)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Fix fixes a memory leak seen in PyPy for estimators using the Cython loss functions. [#27670](https://github.com/scikit-learn/scikit-learn/pull/27670)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

### Changes impacting all modules[#](https://scikit-learn.org/stable/whats_new/v1.4.html#changes-impacting-all-modules "Link to this heading")

*   Major Feature Transformers now support polars output with `set_output(transform="polars")`. [#27315](https://github.com/scikit-learn/scikit-learn/pull/27315)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement All estimators now recognize the column names from any dataframe that adopts the [DataFrame Interchange Protocol](https://data-apis.org/dataframe-protocol/latest/purpose_and_scope.html)
    . Dataframes that return a correct representation through `np.asarray(df)` is expected to work with our estimators and functions. [#26464](https://github.com/scikit-learn/scikit-learn/pull/26464)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement The HTML representation of estimators now includes a link to the documentation and is color-coded to denote whether the estimator is fitted or not (unfitted estimators are orange, fitted estimators are blue). [#26616](https://github.com/scikit-learn/scikit-learn/pull/26616)
     by [Riccardo Cappuzzo](https://github.com/rcap107)
    , [Ines Ibnukhsein](https://github.com/Ines1999)
    , [Gael Varoquaux](https://github.com/GaelVaroquaux)
    , [Joel Nothman](https://joelnothman.com/)
     and [Lilian Boulard](https://github.com/LilianBoulard)
    .
    
*   Fix Fixed a bug in most estimators and functions where setting a parameter to a large integer would cause a `TypeError`. [#26648](https://github.com/scikit-learn/scikit-learn/pull/26648)
     by [Naoise Holohan](https://github.com/naoise-h)
    .
    

### Metadata Routing[#](https://scikit-learn.org/stable/whats_new/v1.4.html#id2 "Link to this heading")

The following models now support metadata routing in one or more of their methods. Refer to the [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

*   Feature `LarsCV` and `LassoLarsCV` now support metadata routing in their `fit` method and route metadata to the CV splitter. [#27538](https://github.com/scikit-learn/scikit-learn/pull/27538)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    
*   Feature [`multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
    , [`multiclass.OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
     and [`multiclass.OutputCodeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier")
     now support metadata routing in their `fit` and `partial_fit`, and route metadata to the underlying estimator’s `fit` and `partial_fit`. [#27308](https://github.com/scikit-learn/scikit-learn/pull/27308)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    
*   Feature [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     now supports metadata routing according to [metadata routing user guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
    . [#26789](https://github.com/scikit-learn/scikit-learn/pull/26789)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Feature [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
    , [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
    , and [`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
     now support metadata routing. The metadata are routed to the estimator’s `fit`, the scorer, and the CV splitter’s `split`. The metadata is accepted via the new `params` parameter. `fit_params` is deprecated and will be removed in version 1.6. `groups` parameter is also not accepted as a separate argument when metadata routing is enabled and should be passed via the `params` parameter. [#26896](https://github.com/scikit-learn/scikit-learn/pull/26896)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Feature [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    , [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
    , [`HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
    , and [`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
     now support metadata routing in their `fit` and `score`, and route metadata to the underlying estimator’s `fit`, the CV splitter, and the scorer. [#27058](https://github.com/scikit-learn/scikit-learn/pull/27058)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Feature [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     now supports metadata routing according to [metadata routing user guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
    . [#27005](https://github.com/scikit-learn/scikit-learn/pull/27005)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Feature [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     now supports metadata routing. [`linear_model.LogisticRegressionCV.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.fit "sklearn.linear_model.LogisticRegressionCV.fit")
     now accepts `**params` which are passed to the underlying splitter and scorer. [`linear_model.LogisticRegressionCV.score`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.score "sklearn.linear_model.LogisticRegressionCV.score")
     now accepts `**score_params` which are passed to the underlying scorer. [#26525](https://github.com/scikit-learn/scikit-learn/pull/26525)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    
*   Feature [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
     now supports metadata routing in `fit` and `partial_fit`. [#27490](https://github.com/scikit-learn/scikit-learn/pull/27490)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    
*   Feature [`linear_model.OrthogonalMatchingPursuitCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuitCV.html#sklearn.linear_model.OrthogonalMatchingPursuitCV "sklearn.linear_model.OrthogonalMatchingPursuitCV")
     now supports metadata routing. Its `fit` now accepts `**fit_params`, which are passed to the underlying splitter. [#27500](https://github.com/scikit-learn/scikit-learn/pull/27500)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    
*   Feature `ElasticNetCV`, `LassoCV`, `MultiTaskElasticNetCV` and `MultiTaskLassoCV` now support metadata routing and route metadata to the CV splitter. [#27478](https://github.com/scikit-learn/scikit-learn/pull/27478)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    
*   Fix All meta-estimators for which metadata routing is not yet implemented now raise a `NotImplementedError` on `get_metadata_routing` and on `fit` if metadata routing is enabled and any metadata is passed to them. [#27389](https://github.com/scikit-learn/scikit-learn/pull/27389)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

### Support for SciPy sparse arrays[#](https://scikit-learn.org/stable/whats_new/v1.4.html#support-for-scipy-sparse-arrays "Link to this heading")

Several estimators are now supporting SciPy sparse arrays. The following functions and classes are impacted:

**Functions:**

*   [`cluster.compute_optics_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.compute_optics_graph.html#sklearn.cluster.compute_optics_graph "sklearn.cluster.compute_optics_graph")
     in [#27104](https://github.com/scikit-learn/scikit-learn/pull/27104)
     by [Maren Westermann](https://github.com/marenwestermann)
     and in [#27250](https://github.com/scikit-learn/scikit-learn/pull/27250)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`cluster.kmeans_plusplus`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.kmeans_plusplus.html#sklearn.cluster.kmeans_plusplus "sklearn.cluster.kmeans_plusplus")
     in [#27179](https://github.com/scikit-learn/scikit-learn/pull/27179)
     by [Nurseit Kamchyev](https://github.com/Bncer)
    ;
    
*   [`decomposition.non_negative_factorization`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.non_negative_factorization.html#sklearn.decomposition.non_negative_factorization "sklearn.decomposition.non_negative_factorization")
     in [#27100](https://github.com/scikit-learn/scikit-learn/pull/27100)
     by [Isaac Virshup](https://github.com/ivirshup)
    ;
    
*   [`feature_selection.f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")
     in [#27239](https://github.com/scikit-learn/scikit-learn/pull/27239)
     by [Yaroslav Korobko](https://github.com/Tialo)
    ;
    
*   [`feature_selection.r_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html#sklearn.feature_selection.r_regression "sklearn.feature_selection.r_regression")
     in [#27239](https://github.com/scikit-learn/scikit-learn/pull/27239)
     by [Yaroslav Korobko](https://github.com/Tialo)
    ;
    
*   [`manifold.trustworthiness`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.trustworthiness.html#sklearn.manifold.trustworthiness "sklearn.manifold.trustworthiness")
     in [#27250](https://github.com/scikit-learn/scikit-learn/pull/27250)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
     in [#27240](https://github.com/scikit-learn/scikit-learn/pull/27240)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     in [#27250](https://github.com/scikit-learn/scikit-learn/pull/27250)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`metrics.pairwise_distances_chunked`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html#sklearn.metrics.pairwise_distances_chunked "sklearn.metrics.pairwise_distances_chunked")
     in [#27250](https://github.com/scikit-learn/scikit-learn/pull/27250)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`metrics.pairwise.pairwise_kernels`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html#sklearn.metrics.pairwise.pairwise_kernels "sklearn.metrics.pairwise.pairwise_kernels")
     in [#27250](https://github.com/scikit-learn/scikit-learn/pull/27250)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`utils.multiclass.type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
     in [#27274](https://github.com/scikit-learn/scikit-learn/pull/27274)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    

**Classes:**

*   [`cluster.HDBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
     in [#27250](https://github.com/scikit-learn/scikit-learn/pull/27250)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     in [#27179](https://github.com/scikit-learn/scikit-learn/pull/27179)
     by [Nurseit Kamchyev](https://github.com/Bncer)
    ;
    
*   [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     in [#27179](https://github.com/scikit-learn/scikit-learn/pull/27179)
     by [Nurseit Kamchyev](https://github.com/Bncer)
    ;
    
*   [`cluster.OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
     in [#27104](https://github.com/scikit-learn/scikit-learn/pull/27104)
     by [Maren Westermann](https://github.com/marenwestermann)
     and in [#27250](https://github.com/scikit-learn/scikit-learn/pull/27250)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     in [#27161](https://github.com/scikit-learn/scikit-learn/pull/27161)
     by [Bharat Raghunathan](https://github.com/bharatr21)
    ;
    
*   [`decomposition.MiniBatchNMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")
     in [#27100](https://github.com/scikit-learn/scikit-learn/pull/27100)
     by [Isaac Virshup](https://github.com/ivirshup)
    ;
    
*   [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     in [#27100](https://github.com/scikit-learn/scikit-learn/pull/27100)
     by [Isaac Virshup](https://github.com/ivirshup)
    ;
    
*   [`feature_extraction.text.TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
     in [#27219](https://github.com/scikit-learn/scikit-learn/pull/27219)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`manifold.Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
     in [#27250](https://github.com/scikit-learn/scikit-learn/pull/27250)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`manifold.SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
     in [#27240](https://github.com/scikit-learn/scikit-learn/pull/27240)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     in [#27250](https://github.com/scikit-learn/scikit-learn/pull/27250)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     in [#27277](https://github.com/scikit-learn/scikit-learn/pull/27277)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     in [#27277](https://github.com/scikit-learn/scikit-learn/pull/27277)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`impute.KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
     in [#27277](https://github.com/scikit-learn/scikit-learn/pull/27277)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`kernel_approximation.PolynomialCountSketch`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch "sklearn.kernel_approximation.PolynomialCountSketch")
     in [#27301](https://github.com/scikit-learn/scikit-learn/pull/27301)
     by [Lohit SundaramahaLingam](https://github.com/lohitslohit)
    ;
    
*   [`neural_network.BernoulliRBM`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM "sklearn.neural_network.BernoulliRBM")
     in [#27252](https://github.com/scikit-learn/scikit-learn/pull/27252)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    ;
    
*   [`preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
     in [#27166](https://github.com/scikit-learn/scikit-learn/pull/27166)
     by [Mohit Joshi](https://github.com/work-mohit)
    ;
    
*   [`random_projection.GaussianRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection "sklearn.random_projection.GaussianRandomProjection")
     in [#27314](https://github.com/scikit-learn/scikit-learn/pull/27314)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    ;
    
*   [`random_projection.SparseRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection")
     in [#27314](https://github.com/scikit-learn/scikit-learn/pull/27314)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    

### Support for Array API[#](https://scikit-learn.org/stable/whats_new/v1.4.html#support-for-array-api "Link to this heading")

Several estimators and functions support the [Array API](https://data-apis.org/array-api/latest/)
. Such changes allow for using the estimators and functions with other libraries such as JAX, CuPy, and PyTorch. This therefore enables some GPU-accelerated computations.

See [Array API support (experimental)](https://scikit-learn.org/stable/modules/array_api.html#array-api)
 for more details.

**Functions:**

*   [`sklearn.metrics.accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
     and [`sklearn.metrics.zero_one_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "sklearn.metrics.zero_one_loss")
     in [#27137](https://github.com/scikit-learn/scikit-learn/pull/27137)
     by [Edoardo Abati](https://github.com/EdAbati)
    ;
    
*   [`sklearn.model_selection.train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
     in [#26855](https://github.com/scikit-learn/scikit-learn/pull/26855)
     by [Tim Head](https://betatim.github.io/)
    ;
    
*   [`is_multilabel`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.is_multilabel.html#sklearn.utils.multiclass.is_multilabel "sklearn.utils.multiclass.is_multilabel")
     in [#27601](https://github.com/scikit-learn/scikit-learn/pull/27601)
     by [Yaroslav Korobko](https://github.com/Tialo)
    .
    

**Classes:**

*   [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     for the `full` and `randomized` solvers (with QR power iterations) in [#26315](https://github.com/scikit-learn/scikit-learn/pull/26315)
    , [#27098](https://github.com/scikit-learn/scikit-learn/pull/27098)
     and [#27431](https://github.com/scikit-learn/scikit-learn/pull/27431)
     by [Mateusz Sokół](https://github.com/mtsokol)
    , [Olivier Grisel](https://github.com/ogrisel)
     and [Edoardo Abati](https://github.com/EdAbati)
    ;
    
*   [`preprocessing.KernelCenterer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KernelCenterer.html#sklearn.preprocessing.KernelCenterer "sklearn.preprocessing.KernelCenterer")
     in [#27556](https://github.com/scikit-learn/scikit-learn/pull/27556)
     by [Edoardo Abati](https://github.com/EdAbati)
    ;
    
*   [`preprocessing.MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")
     in [#27110](https://github.com/scikit-learn/scikit-learn/pull/27110)
     by [Edoardo Abati](https://github.com/EdAbati)
    ;
    
*   [`preprocessing.MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
     in [#26243](https://github.com/scikit-learn/scikit-learn/pull/26243)
     by [Tim Head](https://betatim.github.io/)
    ;
    
*   [`preprocessing.Normalizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer")
     in [#27558](https://github.com/scikit-learn/scikit-learn/pull/27558)
     by [Edoardo Abati](https://github.com/EdAbati)
    .
    

### Private Loss Function Module[#](https://scikit-learn.org/stable/whats_new/v1.4.html#private-loss-function-module "Link to this heading")

*   Fix The gradient computation of the binomial log loss is now numerically more stable for very large, in absolute value, input (raw predictions). Before, it could result in `np.nan`. Among the models that profit from this change are [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
    , [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    . [#28048](https://github.com/scikit-learn/scikit-learn/pull/28048)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.4.html#id3 "Link to this heading")

#### [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-base "Link to this heading")

*   Enhancement [`base.ClusterMixin.fit_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClusterMixin.html#sklearn.base.ClusterMixin.fit_predict "sklearn.base.ClusterMixin.fit_predict")
     and [`base.OutlierMixin.fit_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.base.OutlierMixin.html#sklearn.base.OutlierMixin.fit_predict "sklearn.base.OutlierMixin.fit_predict")
     now accept `**kwargs` which are passed to the `fit` method of the estimator. [#26506](https://github.com/scikit-learn/scikit-learn/pull/26506)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Enhancement [`base.TransformerMixin.fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin.fit_transform "sklearn.base.TransformerMixin.fit_transform")
     and [`base.OutlierMixin.fit_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.base.OutlierMixin.html#sklearn.base.OutlierMixin.fit_predict "sklearn.base.OutlierMixin.fit_predict")
     now raise a warning if `transform` / `predict` consume metadata, but no custom `fit_transform` / `fit_predict` is defined in the class inheriting from them correspondingly. [#26831](https://github.com/scikit-learn/scikit-learn/pull/26831)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Enhancement [`base.clone`](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#sklearn.base.clone "sklearn.base.clone")
     now supports `dict` as input and creates a copy. [#26786](https://github.com/scikit-learn/scikit-learn/pull/26786)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   API Change [`process_routing`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#sklearn.utils.metadata_routing.process_routing "sklearn.utils.metadata_routing.process_routing")
     now has a different signature. The first two (the object and the method) are positional only, and all metadata are passed as keyword arguments. [#26909](https://github.com/scikit-learn/scikit-learn/pull/26909)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#id4 "Link to this heading")

*   Enhancement The internal objective and gradient of the `sigmoid` method of [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     have been replaced by the private loss module. [#27185](https://github.com/scikit-learn/scikit-learn/pull/27185)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#id5 "Link to this heading")

*   Fix The `degree` parameter in the [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     constructor now accepts real values instead of only integral values in accordance with the `degree` parameter of the [`sklearn.metrics.pairwise.polynomial_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html#sklearn.metrics.pairwise.polynomial_kernel "sklearn.metrics.pairwise.polynomial_kernel")
    . [#27668](https://github.com/scikit-learn/scikit-learn/pull/27668)
     by [Nolan McMahon](https://github.com/NolantheNerd)
    .
    
*   Fix Fixes a bug in [`cluster.OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
     where the cluster correction based on predecessor was not using the right indexing. It would lead to inconsistent results dependent on the order of the data. [#26459](https://github.com/scikit-learn/scikit-learn/pull/26459)
     by [Haoying Zhang](https://github.com/stevezhang1999)
     and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Improve error message when checking the number of connected components in the `fit` method of [`cluster.HDBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
    . [#27678](https://github.com/scikit-learn/scikit-learn/pull/27678)
     by [Ganesh Tata](https://github.com/tataganesh)
    .
    
*   Fix Create copy of precomputed sparse matrix within the `fit` method of [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
     to avoid in-place modification of the sparse matrix. [#27651](https://github.com/scikit-learn/scikit-learn/pull/27651)
     by [Ganesh Tata](https://github.com/tataganesh)
    .
    
*   Fix Raises a proper `ValueError` when `metric="precomputed"` and requested storing centers via the parameter `store_centers`. [#27898](https://github.com/scikit-learn/scikit-learn/pull/27898)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change `kdtree` and `balltree` values are now deprecated and are renamed as `kd_tree` and `ball_tree` respectively for the `algorithm` parameter of [`cluster.HDBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
     ensuring consistency in naming convention. `kdtree` and `balltree` values will be removed in 1.6. [#26744](https://github.com/scikit-learn/scikit-learn/pull/26744)
     by [Shreesha Kumar Bhat](https://github.com/Shreesha3112)
    .
    
*   API Change The option `metric=None` in [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     and [`cluster.FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")
     is deprecated in version 1.4 and will be removed in version 1.6. Use the default value instead. [#27828](https://github.com/scikit-learn/scikit-learn/pull/27828)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#id6 "Link to this heading")

*   Major Feature Adds [polars](https://www.pola.rs/)
     input support to [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     through the [DataFrame Interchange Protocol](https://data-apis.org/dataframe-protocol/latest/purpose_and_scope.html)
    . The minimum supported version for polars is `0.19.12`. [#26683](https://github.com/scikit-learn/scikit-learn/pull/26683)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`cluster.spectral_clustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")
     and [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     now raise an explicit error message indicating that sparse matrices and arrays with `np.int64` indices are not supported. [#27240](https://github.com/scikit-learn/scikit-learn/pull/27240)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    
*   API Change outputs that use pandas extension dtypes and contain `pd.NA` in [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     now result in a `FutureWarning` and will cause a `ValueError` in version 1.6, unless the output container has been configured as “pandas” with `set_output(transform="pandas")`. Before, such outputs resulted in numpy arrays of dtype `object` containing `pd.NA` which could not be converted to numpy floats and caused errors when passed to other scikit-learn estimators. [#27734](https://github.com/scikit-learn/scikit-learn/pull/27734)
     by [Jérôme Dockès](https://github.com/jeromedockes)
    .
    

#### [`sklearn.covariance`](https://scikit-learn.org/stable/api/sklearn.covariance.html#module-sklearn.covariance "sklearn.covariance")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-covariance "Link to this heading")

*   Enhancement Allow [`covariance.shrunk_covariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.shrunk_covariance.html#sklearn.covariance.shrunk_covariance "sklearn.covariance.shrunk_covariance")
     to process multiple covariance matrices at once by handling nd-arrays. [#25275](https://github.com/scikit-learn/scikit-learn/pull/25275)
     by [Quentin Barthélemy](https://github.com/qbarthelemy)
    .
    
*   API Change Fix [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     now replaces `"passthrough"` with a corresponding [`FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
     in the fitted `transformers_` attribute. [#27204](https://github.com/scikit-learn/scikit-learn/pull/27204)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-datasets "Link to this heading")

*   Enhancement [`datasets.make_sparse_spd_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html#sklearn.datasets.make_sparse_spd_matrix "sklearn.datasets.make_sparse_spd_matrix")
     now uses a more memory-efficient sparse layout. It also accepts a new keyword `sparse_format` that allows specifying the output format of the sparse matrix. By default `sparse_format=None`, which returns a dense numpy ndarray as before. [#27438](https://github.com/scikit-learn/scikit-learn/pull/27438)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    
*   Fix [`datasets.dump_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.dump_svmlight_file.html#sklearn.datasets.dump_svmlight_file "sklearn.datasets.dump_svmlight_file")
     now does not raise `ValueError` when `X` is read-only, e.g., a `numpy.memmap` instance. [#28111](https://github.com/scikit-learn/scikit-learn/pull/28111)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    
*   API Change [`datasets.make_sparse_spd_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html#sklearn.datasets.make_sparse_spd_matrix "sklearn.datasets.make_sparse_spd_matrix")
     deprecated the keyword argument `dim` in favor of `n_dim`. `dim` will be removed in version 1.6. [#27718](https://github.com/scikit-learn/scikit-learn/pull/27718)
     by [Adam Li](https://github.com/adam2392)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-decomposition "Link to this heading")

*   Feature [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     now supports [`scipy.sparse.sparray`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.sparray.html#scipy.sparse.sparray "(in SciPy v1.18.0)")
     and [`scipy.sparse.spmatrix`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.spmatrix.html#scipy.sparse.spmatrix "(in SciPy v1.18.0)")
     inputs when using the `arpack` solver. When used on sparse data like [`datasets.fetch_20newsgroups_vectorized`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized")
     this can lead to speed-ups of 100x (single threaded) and 70x lower memory usage. Based on [Alexander Tarashansky](https://github.com/atarashansky)
    ’s implementation in [scanpy](https://github.com/scverse/scanpy)
    . [#18689](https://github.com/scikit-learn/scikit-learn/pull/18689)
     by [Isaac Virshup](https://github.com/ivirshup)
     and [Andrey Portnoy](https://github.com/andportnoy)
    .
    
*   Enhancement An “auto” option was added to the `n_components` parameter of [`decomposition.non_negative_factorization`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.non_negative_factorization.html#sklearn.decomposition.non_negative_factorization "sklearn.decomposition.non_negative_factorization")
    , [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     and [`decomposition.MiniBatchNMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")
     to automatically infer the number of components from W or H shapes when using a custom initialization. The default value of this parameter will change from `None` to `auto` in version 1.6. [#26634](https://github.com/scikit-learn/scikit-learn/pull/26634)
     by [Alexandre Landeau](https://github.com/AlexL)
     and [Alexandre Vigny](https://github.com/avigny)
    .
    
*   Fix [`decomposition.dict_learning_online`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html#sklearn.decomposition.dict_learning_online "sklearn.decomposition.dict_learning_online")
     does not ignore anymore the parameter `max_iter`. [#27834](https://github.com/scikit-learn/scikit-learn/pull/27834)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix The `degree` parameter in the [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
     constructor now accepts real values instead of only integral values in accordance with the `degree` parameter of the [`sklearn.metrics.pairwise.polynomial_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html#sklearn.metrics.pairwise.polynomial_kernel "sklearn.metrics.pairwise.polynomial_kernel")
    . [#27668](https://github.com/scikit-learn/scikit-learn/pull/27668)
     by [Nolan McMahon](https://github.com/NolantheNerd)
    .
    
*   API Change The option `max_iter=None` in [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
    , [`decomposition.MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")
    , and [`decomposition.dict_learning_online`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html#sklearn.decomposition.dict_learning_online "sklearn.decomposition.dict_learning_online")
     is deprecated and will be removed in version 1.6. Use the default value instead. [#27834](https://github.com/scikit-learn/scikit-learn/pull/27834)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#id7 "Link to this heading")

*   Major Feature [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
     and [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
     support missing values when the criterion is `gini`, `entropy`, or `log_loss`, for classification or `squared_error`, `friedman_mse`, or `poisson` for regression. [#26391](https://github.com/scikit-learn/scikit-learn/pull/26391)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Major Feature [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     support `categorical_features="from_dtype"`, which treats columns with Pandas or Polars Categorical dtype as categories in the algorithm. `categorical_features="from_dtype"` will become the default in v1.6. Categorical features no longer need to be encoded with numbers. When categorical features are numbers, the maximum value no longer needs to be smaller than `max_bins`; only the number of (unique) categories must be smaller than `max_bins`. [#26411](https://github.com/scikit-learn/scikit-learn/pull/26411)
     by [Thomas Fan](https://github.com/thomasjpfan)
     and [#27835](https://github.com/scikit-learn/scikit-learn/pull/27835)
     by [Jérôme Dockès](https://github.com/jeromedockes)
    .
    
*   Major Feature [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     got the new parameter `max_features` to specify the proportion of randomly chosen features considered in each split. [#27139](https://github.com/scikit-learn/scikit-learn/pull/27139)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Feature [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
     and [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
     now support monotonic constraints, useful when features are supposed to have a positive/negative effect on the target. Missing values in the train data and multi-output targets are not supported. [#13649](https://github.com/scikit-learn/scikit-learn/pull/13649)
     by [Samuel Ronsin](https://github.com/samronsin)
    , initiated by [Patrick O’Reilly](https://github.com/pat-oreilly)
    .
    
*   Efficiency [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     are now a bit faster by reusing the parent node’s histogram as children node’s histogram in the subtraction trick. In effect, less memory has to be allocated and deallocated. [#27865](https://github.com/scikit-learn/scikit-learn/pull/27865)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Efficiency [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     is faster, for binary and in particular for multiclass problems thanks to the private loss function module. [#26278](https://github.com/scikit-learn/scikit-learn/pull/26278)
     and [#28095](https://github.com/scikit-learn/scikit-learn/pull/28095)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Efficiency Improves runtime and memory usage for [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     when trained on sparse data. [#26957](https://github.com/scikit-learn/scikit-learn/pull/26957)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Efficiency [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     is now faster when `scoring` is a predefined metric listed in [`metrics.get_scorer_names`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer_names.html#sklearn.metrics.get_scorer_names "sklearn.metrics.get_scorer_names")
     and early stopping is enabled. [#26163](https://github.com/scikit-learn/scikit-learn/pull/26163)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement A fitted property, `estimators_samples_`, was added to all Forest methods, including [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
     and [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
    , which allows to retrieve the training sample indices used for each tree estimator. [#26736](https://github.com/scikit-learn/scikit-learn/pull/26736)
     by [Adam Li](https://github.com/adam2392)
    .
    
*   Fix Fixes [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     when the input is a sparse matrix and `contamination` is set to a float value. [#27645](https://github.com/scikit-learn/scikit-learn/pull/27645)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Raises a `ValueError` in [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
     and [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
     when requesting OOB score with multioutput model for the targets being all rounded to integer. It was recognized as a multiclass problem. [#27817](https://github.com/scikit-learn/scikit-learn/pull/27817)
     by [Daniele Ongari](https://github.com/danieleongari)
    
*   Fix Changes estimator tags to acknowledge that [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
    , [`ensemble.VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
    , [`ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
    , [`ensemble.StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
    , support missing values if all `estimators` support missing values. [#27710](https://github.com/scikit-learn/scikit-learn/pull/27710)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Support loading pickles of [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     when the pickle has been generated on a platform with a different bitness. A typical example is to train and pickle the model on 64 bit machine and load the model on a 32 bit machine for prediction. [#28074](https://github.com/scikit-learn/scikit-learn/pull/28074)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
     and [Loïc Estève](https://github.com/lesteve)
    .
    
*   API Change In [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
    , the `algorithm` argument `SAMME.R` was deprecated and will be removed in 1.6. [#26830](https://github.com/scikit-learn/scikit-learn/pull/26830)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-feature-extraction "Link to this heading")

*   API Change Changed error type from [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "(in Python v3.14)")
     to [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError")
     in unfitted instances of [`feature_extraction.DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
     for the following methods: [`feature_extraction.DictVectorizer.inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.inverse_transform "sklearn.feature_extraction.DictVectorizer.inverse_transform")
    , [`feature_extraction.DictVectorizer.restrict`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.restrict "sklearn.feature_extraction.DictVectorizer.restrict")
    , [`feature_extraction.DictVectorizer.transform`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer.transform "sklearn.feature_extraction.DictVectorizer.transform")
    . [#24838](https://github.com/scikit-learn/scikit-learn/pull/24838)
     by [Lorenz Hertel](https://github.com/LoHertel)
    .
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-feature-selection "Link to this heading")

*   Enhancement [`feature_selection.SelectKBest`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
    , [`feature_selection.SelectPercentile`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile")
    , and [`feature_selection.GenericUnivariateSelect`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect "sklearn.feature_selection.GenericUnivariateSelect")
     now support unsupervised feature selection by providing a `score_func` taking `X` and `y=None`. [#27721](https://github.com/scikit-learn/scikit-learn/pull/27721)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Enhancement [`feature_selection.SelectKBest`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
     and [`feature_selection.GenericUnivariateSelect`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect "sklearn.feature_selection.GenericUnivariateSelect")
     with `mode='k_best'` now shows a warning when `k` is greater than the number of features. [#27841](https://github.com/scikit-learn/scikit-learn/pull/27841)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`feature_selection.RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
     and [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
     do not check for nans during input validation. [#21807](https://github.com/scikit-learn/scikit-learn/pull/21807)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#id8 "Link to this heading")

*   Enhancement [`inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
     now accepts a parameter `class_of_interest` to select the class of interest when plotting the response provided by `response_method="predict_proba"` or `response_method="decision_function"`. It allows to plot the decision boundary for both binary and multiclass classifiers. [#27291](https://github.com/scikit-learn/scikit-learn/pull/27291)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`inspection.DecisionBoundaryDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
     and [`inspection.PartialDependenceDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
     now return the correct type for subclasses. [#27675](https://github.com/scikit-learn/scikit-learn/pull/27675)
     by [John Cant](https://github.com/johncant)
    .
    
*   API Change [`inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
     raises an `AttributeError` instead of a `ValueError` when an estimator does not implement the requested response method. [#27291](https://github.com/scikit-learn/scikit-learn/pull/27291)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.kernel_ridge`](https://scikit-learn.org/stable/api/sklearn.kernel_ridge.html#module-sklearn.kernel_ridge "sklearn.kernel_ridge")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-kernel-ridge "Link to this heading")

*   Fix The `degree` parameter in the [`kernel_ridge.KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
     constructor now accepts real values instead of only integral values in accordance with the `degree` parameter of the [`sklearn.metrics.pairwise.polynomial_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html#sklearn.metrics.pairwise.polynomial_kernel "sklearn.metrics.pairwise.polynomial_kernel")
    . [#27668](https://github.com/scikit-learn/scikit-learn/pull/27668)
     by [Nolan McMahon](https://github.com/NolantheNerd)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#id9 "Link to this heading")

*   Efficiency [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     now have much better convergence for solvers `"lbfgs"` and `"newton-cg"`. Both solvers can now reach much higher precision for the coefficients depending on the specified `tol`. Additionally, lbfgs can make better use of `tol`, i.e., stop sooner or reach higher precision. This is accomplished by better scaling of the objective function, i.e., using average per sample losses instead of sum of per sample losses. [#26721](https://github.com/scikit-learn/scikit-learn/pull/26721)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Efficiency [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     with solver `"newton-cg"` can now be considerably faster for some data and parameter settings. This is accomplished by a better line search convergence check for negligible loss improvements that takes into account gradient information. [#26721](https://github.com/scikit-learn/scikit-learn/pull/26721)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Efficiency Solver `"newton-cg"` in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     uses a little less memory. The effect is proportional to the number of coefficients (`n_features * n_classes`). [#27417](https://github.com/scikit-learn/scikit-learn/pull/27417)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Fix Ensure that the `sigma_` attribute of [`linear_model.ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
     and [`linear_model.BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
     always has a `float32` dtype when fitted on `float32` data, even with the type promotion rules of NumPy 2. [#27899](https://github.com/scikit-learn/scikit-learn/pull/27899)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   API Change The attribute `loss_function_` of [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     and [`linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
     has been deprecated and will be removed in version 1.6. [#27979](https://github.com/scikit-learn/scikit-learn/pull/27979)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-metrics "Link to this heading")

*   Efficiency Computing pairwise distances via [`metrics.DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "sklearn.metrics.DistanceMetric")
     for CSR x CSR, Dense x CSR, and CSR x Dense datasets is now 1.5x faster. [#26765](https://github.com/scikit-learn/scikit-learn/pull/26765)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Efficiency Computing distances via [`metrics.DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "sklearn.metrics.DistanceMetric")
     for CSR x CSR, Dense x CSR, and CSR x Dense now uses ~50% less memory, and outputs distances in the same dtype as the provided data. [#27006](https://github.com/scikit-learn/scikit-learn/pull/27006)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Enhancement Improve the rendering of the plot obtained with the [`metrics.PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")
     and [`metrics.RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")
     classes. The x- and y-axis limits are set to \[0, 1\] and the aspect ratio between both axes is set to be 1 to get a square plot. [#26366](https://github.com/scikit-learn/scikit-learn/pull/26366)
     by [Mojdeh Rastgoo](https://github.com/mrastgoo)
    .
    
*   Enhancement Added `neg_root_mean_squared_log_error_scorer` as scorer [#26734](https://github.com/scikit-learn/scikit-learn/pull/26734)
     by [Alejandro Martin Gil](https://github.com/101AlexMartin)
    .
    
*   Enhancement [`metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
     now warns when only one label was found in `y_true` and `y_pred`. [#27650](https://github.com/scikit-learn/scikit-learn/pull/27650)
     by [Lucy Liu](https://github.com/lucyleeow)
    .
    
*   Fix computing pairwise distances with [`metrics.pairwise.euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html#sklearn.metrics.pairwise.euclidean_distances "sklearn.metrics.pairwise.euclidean_distances")
     no longer raises an exception when `X` is provided as a `float64` array and `X_norm_squared` as a `float32` array. [#27624](https://github.com/scikit-learn/scikit-learn/pull/27624)
     by [Jérôme Dockès](https://github.com/jeromedockes)
    .
    
*   Fix `f1_score` now provides correct values when handling various cases in which division by zero occurs by using a formulation that does not depend on the precision and recall values. [#27577](https://github.com/scikit-learn/scikit-learn/pull/27577)
     by [Omar Salman](https://github.com/OmarManzoor)
     and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`metrics.make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
     now raises an error when using a regressor on a scorer requesting a non-thresholded decision function (from `decision_function` or `predict_proba`). Such scorers are specific to classification. [#26840](https://github.com/scikit-learn/scikit-learn/pull/26840)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`metrics.DetCurveDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_predictions "sklearn.metrics.DetCurveDisplay.from_predictions")
    , [`metrics.PrecisionRecallDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")
    , [`metrics.PredictionErrorDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")
    , and [`metrics.RocCurveDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")
     now return the correct type for subclasses. [#27675](https://github.com/scikit-learn/scikit-learn/pull/27675)
     by [John Cant](https://github.com/johncant)
    .
    
*   API Change Deprecated `needs_threshold` and `needs_proba` from [`metrics.make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
    . These parameters will be removed in version 1.6. Instead, use `response_method` that accepts `"predict"`, `"predict_proba"` or `"decision_function"` or a list of such values. `needs_proba=True` is equivalent to `response_method="predict_proba"` and `needs_threshold=True` is equivalent to `response_method=("decision_function", "predict_proba")`. [#26840](https://github.com/scikit-learn/scikit-learn/pull/26840)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change The `squared` parameter of [`metrics.mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
     and [`metrics.mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html#sklearn.metrics.mean_squared_log_error "sklearn.metrics.mean_squared_log_error")
     is deprecated and will be removed in 1.6. Use the new functions [`metrics.root_mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#sklearn.metrics.root_mean_squared_error "sklearn.metrics.root_mean_squared_error")
     and [`metrics.root_mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_log_error.html#sklearn.metrics.root_mean_squared_log_error "sklearn.metrics.root_mean_squared_log_error")
     instead. [#26734](https://github.com/scikit-learn/scikit-learn/pull/26734)
     by [Alejandro Martin Gil](https://github.com/101AlexMartin)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-model-selection "Link to this heading")

*   Enhancement [`model_selection.learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
     raises a warning when every cross validation fold fails. [#26299](https://github.com/scikit-learn/scikit-learn/pull/26299)
     by [Rahil Parikh](https://github.com/rprkh)
    .
    
*   Fix [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    , [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
    , and [`model_selection.HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
     now don’t change the given object in the parameter grid if it’s an estimator. [#26786](https://github.com/scikit-learn/scikit-learn/pull/26786)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.multioutput`](https://scikit-learn.org/stable/api/sklearn.multioutput.html#module-sklearn.multioutput "sklearn.multioutput")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-multioutput "Link to this heading")

*   Enhancement Add method `predict_log_proba` to [`multioutput.ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
    . [#27720](https://github.com/scikit-learn/scikit-learn/pull/27720)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#sklearn-neighbors "Link to this heading")

*   Efficiency [`sklearn.neighbors.KNeighborsRegressor.predict`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor.predict "sklearn.neighbors.KNeighborsRegressor.predict")
     and [`sklearn.neighbors.KNeighborsClassifier.predict_proba`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.predict_proba "sklearn.neighbors.KNeighborsClassifier.predict_proba")
     now efficiently support pairs of dense and sparse datasets. [#27018](https://github.com/scikit-learn/scikit-learn/pull/27018)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Efficiency The performance of [`neighbors.RadiusNeighborsClassifier.predict`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.predict "sklearn.neighbors.RadiusNeighborsClassifier.predict")
     and of [`neighbors.RadiusNeighborsClassifier.predict_proba`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier.predict_proba "sklearn.neighbors.RadiusNeighborsClassifier.predict_proba")
     has been improved when `radius` is large and `algorithm="brute"` with non-Euclidean metrics. [#26828](https://github.com/scikit-learn/scikit-learn/pull/26828)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    
*   Fix Improve error message for [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
     when it is invoked with `n_samples=n_neighbors`. [#23317](https://github.com/scikit-learn/scikit-learn/pull/23317)
     by [Bharat Raghunathan](https://github.com/bharatr21)
    .
    
*   Fix [`neighbors.KNeighborsClassifier.predict`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.predict "sklearn.neighbors.KNeighborsClassifier.predict")
     and [`neighbors.KNeighborsClassifier.predict_proba`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.predict_proba "sklearn.neighbors.KNeighborsClassifier.predict_proba")
     now raise an error when the weights of all neighbors of some sample are zero. This can happen when `weights` is a user-defined function. [#26410](https://github.com/scikit-learn/scikit-learn/pull/26410)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    
*   API Change [`neighbors.KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
     now accepts [`metrics.DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "sklearn.metrics.DistanceMetric")
     objects directly via the `metric` keyword argument allowing for the use of accelerated third-party [`metrics.DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "sklearn.metrics.DistanceMetric")
     objects. [#26267](https://github.com/scikit-learn/scikit-learn/pull/26267)
     by [Meekail Zain](https://github.com/micky774)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#id10 "Link to this heading")

*   Efficiency [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     avoids calculating missing indices twice to improve efficiency. [#27017](https://github.com/scikit-learn/scikit-learn/pull/27017)
     by [Xuefeng Xu](https://github.com/xuefeng-xu)
    .
    
*   Efficiency Improves efficiency in [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     and [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     in checking `nan`. [#27760](https://github.com/scikit-learn/scikit-learn/pull/27760)
     by [Xuefeng Xu](https://github.com/xuefeng-xu)
    .
    
*   Enhancement Improves warnings in [`preprocessing.FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
     when `func` returns a pandas dataframe and the output is configured to be pandas. [#26944](https://github.com/scikit-learn/scikit-learn/pull/26944)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`preprocessing.TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
     now supports `target_type` ‘multiclass’. [#26674](https://github.com/scikit-learn/scikit-learn/pull/26674)
     by [Lucy Liu](https://github.com/lucyleeow)
    .
    
*   Fix [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     and [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     raise an exception when `nan` is a category and is not the last in the user’s provided categories. [#27309](https://github.com/scikit-learn/scikit-learn/pull/27309)
     by [Xuefeng Xu](https://github.com/xuefeng-xu)
    .
    
*   Fix [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     and [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     raise an exception if the user provided categories contain duplicates. [#27328](https://github.com/scikit-learn/scikit-learn/pull/27328)
     by [Xuefeng Xu](https://github.com/xuefeng-xu)
    .
    
*   Fix [`preprocessing.FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
     raises an error at `transform` if the output of `get_feature_names_out` is not consistent with the column names of the output container if those are defined. [#27801](https://github.com/scikit-learn/scikit-learn/pull/27801)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Raise a `NotFittedError` in [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     when calling `transform` without calling `fit` since `categories` always requires to be checked. [#27821](https://github.com/scikit-learn/scikit-learn/pull/27821)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#id11 "Link to this heading")

*   Feature [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
     and [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
     now support monotonic constraints, useful when features are supposed to have a positive/negative effect on the target. Missing values in the train data and multi-output targets are not supported. [#13649](https://github.com/scikit-learn/scikit-learn/pull/13649)
     by [Samuel Ronsin](https://github.com/samronsin)
    , initiated by [Patrick O’Reilly](https://github.com/pat-oreilly)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.4.html#id12 "Link to this heading")

*   Enhancement [`sklearn.utils.estimator_html_repr`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_html_repr.html#sklearn.utils.estimator_html_repr "sklearn.utils.estimator_html_repr")
     dynamically adapts diagram colors based on the browser’s `prefers-color-scheme`, providing improved adaptability to dark mode environments. [#26862](https://github.com/scikit-learn/scikit-learn/pull/26862)
     by [Andrew Goh Yisheng](https://github.com/9y5)
    , [Thomas Fan](https://github.com/thomasjpfan)
    , [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Enhancement [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
     and [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
     now have a `consumes` method which can be used to check whether a given set of parameters would be consumed. [#26831](https://github.com/scikit-learn/scikit-learn/pull/26831)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Enhancement Make [`sklearn.utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     attempt to output `int32`\-indexed CSR and COO arrays when converting from DIA arrays if the number of non-zero entries is small enough. This ensures that estimators implemented in Cython and that do not accept `int64`\-indexed sparse datastucture, now consistently accept the same sparse input formats for SciPy sparse matrices and arrays. [#27372](https://github.com/scikit-learn/scikit-learn/pull/27372)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`sklearn.utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     should accept both matrix and array from the sparse SciPy module. The previous implementation would fail if `copy=True` by calling specific NumPy `np.may_share_memory` that does not work with SciPy sparse array and does not return the correct result for SciPy sparse matrix. [#27336](https://github.com/scikit-learn/scikit-learn/pull/27336)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix `check_estimators_pickle` with `readonly_memmap=True` now relies on joblib’s own capability to allocate aligned memory mapped arrays when loading a serialized estimator instead of calling a dedicated private function that would crash when OpenBLAS misdetects the CPU architecture. [#27614](https://github.com/scikit-learn/scikit-learn/pull/27614)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Fix Error message in [`check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     when a sparse matrix was passed but `accept_sparse` is `False` now suggests to use `.toarray()` and not `X.toarray()`. [#27757](https://github.com/scikit-learn/scikit-learn/pull/27757)
     by [Lucy Liu](https://github.com/lucyleeow)
    .
    
*   Fix Fix the function [`check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     to output the right error message when the input is a Series instead of a DataFrame. [#28090](https://github.com/scikit-learn/scikit-learn/pull/28090)
     by [Stan Furrer](https://github.com/stanFurrer)
     and [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    
*   API Change `sklearn.utils.extmath.log_logistic` is deprecated and will be removed in 1.6. Use `-np.logaddexp(0, -x)` instead. [#27544](https://github.com/scikit-learn/scikit-learn/pull/27544)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    

Code and documentation contributors

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 1.3, including:

101AlexMartin, Abhishek Singh Kushwah, Adam Li, Adarsh Wase, Adrin Jalali, Advik Sinha, Alex, Alexander Al-Feghali, Alexis IMBERT, AlexL, Alex Molas, Anam Fatima, Andrew Goh, andyscanzio, Aniket Patil, Artem Kislovskiy, Arturo Amor, ashah002, avm19, Ben Holmes, Ben Mares, Benoit Chevallier-Mames, Bharat Raghunathan, Binesh Bannerjee, Brendan Lu, Brevin Kunde, Camille Troillard, Carlo Lemos, Chad Parmet, Christian Clauss, Christian Lorentzen, Christian Veenhuis, Christos Aridas, Cindy Liang, Claudio Salvatore Arcidiacono, Connor Boyle, cynthias13w, DaminK, Daniele Ongari, Daniel Schmitz, Daniel Tinoco, David Brochart, Deborah L. Haar, DevanshKyada27, Dimitri Papadopoulos Orfanos, Dmitry Nesterov, DUONG, Edoardo Abati, Eitan Hemed, Elabonga Atuo, Elisabeth Günther, Emma Carballal, Emmanuel Ferdman, epimorphic, Erwan Le Floch, Fabian Egli, Filip Karlo Došilović, Florian Idelberger, Franck Charras, Gael Varoquaux, Ganesh Tata, Hleb Levitski, Guillaume Lemaitre, Haoying Zhang, Harmanan Kohli, Ily, ioangatop, IsaacTrost, Isaac Virshup, Iwona Zdzieblo, Jakub Kaczmarzyk, James McDermott, Jarrod Millman, JB Mountford, Jérémie du Boisberranger, Jérôme Dockès, Jiawei Zhang, Joel Nothman, John Cant, John Hopfensperger, Jona Sassenhagen, Jon Nordby, Julien Jerphanion, Kennedy Waweru, kevin moore, Kian Eliasi, Kishan Ved, Konstantinos Pitas, Koustav Ghosh, Kushan Sharma, ldwy4, Linus, Lohit SundaramahaLingam, Loic Esteve, Lorenz, Louis Fouquet, Lucy Liu, Luis Silvestrin, Lukáš Folwarczný, Lukas Geiger, Malte Londschien, Marcus Fraaß, Marek Hanuš, Maren Westermann, Mark Elliot, Martin Larralde, Mateusz Sokół, mathurinm, mecopur, Meekail Zain, Michael Higgins, Miki Watanabe, Milton Gomez, MN193, Mohammed Hamdy, Mohit Joshi, mrastgoo, Naman Dhingra, Naoise Holohan, Narendra Singh dangi, Noa Malem-Shinitski, Nolan, Nurseit Kamchyev, Oleksii Kachaiev, Olivier Grisel, Omar Salman, partev, Peter Hull, Peter Steinbach, Pierre de Fréminville, Pooja Subramaniam, Puneeth K, qmarcou, Quentin Barthélemy, Rahil Parikh, Rahul Mahajan, Raj Pulapakura, Raphael, Ricardo Peres, Riccardo Cappuzzo, Roman Lutz, Salim Dohri, Samuel O. Ronsin, Sandip Dutta, Sayed Qaiser Ali, scaja, scikit-learn-bot, Sebastian Berg, Shreesha Kumar Bhat, Shubhal Gupta, Søren Fuglede Jørgensen, Stefanie Senger, Tamara, Tanjina Afroj, THARAK HEGDE, thebabush, Thomas J. Fan, Thomas Roehr, Tialo, Tim Head, tongyu, Venkatachalam N, Vijeth Moudgalya, Vincent M, Vivek Reddy P, Vladimir Fokow, Xiao Yuan, Xuefeng Xu, Yang Tao, Yao Xiao, Yuchen Zhou, Yuusuke Hiramatsu

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)