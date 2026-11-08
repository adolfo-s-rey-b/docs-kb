[Skip to main content](https://scikit-learn.org/stable/whats_new/v1.9.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v1.9.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v1.9.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v1.9.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v1.9.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v1.9.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v1.9.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v1.9.html)

Collapse Sidebar Expand Sidebar

Version 1.9[#](https://scikit-learn.org/stable/whats_new/v1.9.html#version-1-9 "Link to this heading")

=======================================================================================================

For a short description of the main highlights of the release, please refer to [Release Highlights for scikit-learn 1.9](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_9_0.html#sphx-glr-auto-examples-release-highlights-plot-release-highlights-1-9-0-py)
.

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 1.9.1[#](https://scikit-learn.org/stable/whats_new/v1.9.html#version-1-9-1 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**September 2026**

### Support for Array API[#](https://scikit-learn.org/stable/whats_new/v1.9.html#support-for-array-api "Link to this heading")

*   Fix Fixed classification metrics to accept pandas labels when array API dispatch is enabled and predictions are from a different array API namespace or device. By [Olivier Grisel](https://github.com/ogrisel)
    . [#34779](https://github.com/scikit-learn/scikit-learn/pull/34779)
    

### Metadata routing[#](https://scikit-learn.org/stable/whats_new/v1.9.html#metadata-routing "Link to this heading")

Refer to the [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

*   Fix Metadata is now correctly routed to the sub-estimator of meta-estimators such as [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
    , [`feature_selection.RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
    , [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
    , [`feature_selection.SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
    , and [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     when they are used as an intermediate step of a [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
    , i.e. when their composite `fit_transform` method is the target of the routing. Previously, metadata such as `sample_weight` was silently dropped in this case. By [Adrin Jalali](https://github.com/adrinjalali)
     and [Kyle Schluns](https://github.com/kschluns)
    . [#30869](https://github.com/scikit-learn/scikit-learn/pull/30869)
    
*   Fix [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
     now correctly routes metadata via `predict` and `predict_proba` dynamically to the corresponding method on the sub-estimator. By [Stefanie Senger](https://github.com/StefanieSenger)
    . [#34188](https://github.com/scikit-learn/scikit-learn/pull/34188)
    
*   Fix [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
    ’s [`fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.fit_transform "sklearn.pipeline.Pipeline.fit_transform")
     and [`fit_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.fit_predict "sklearn.pipeline.Pipeline.fit_predict")
     now correctly apply `transform_input` to metadata routed to intermediate steps, matching [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.fit "sklearn.pipeline.Pipeline.fit")
    . By [Stefanie Senger](https://github.com/StefanieSenger)
    . [#34201](https://github.com/scikit-learn/scikit-learn/pull/34201)
    
*   Fix [`compose.TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
     now correctly routes metadata such as `sample_weight` to its default regressor ([`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
    ) when metadata routing is enabled. By [Stefanie Senger](https://github.com/StefanieSenger)
    . [#34224](https://github.com/scikit-learn/scikit-learn/pull/34224)
    

### Callbacks[#](https://scikit-learn.org/stable/whats_new/v1.9.html#callbacks "Link to this heading")

*   Fix Fixed a bug where fitting an estimator with a [`callback.ScoringMonitor`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#sklearn.callback.ScoringMonitor "sklearn.callback.ScoringMonitor")
     and a parallel backend using multi-processing could fail with “Could not pickle the task to send it to the workers”. By [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    . [#34821](https://github.com/scikit-learn/scikit-learn/pull/34821)
    

### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-cluster "Link to this heading")

*   Fix [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
     and [`cluster.dbscan`](https://scikit-learn.org/stable/modules/generated/dbscan-function.html#sklearn.cluster.dbscan "sklearn.cluster.dbscan")
     no longer raise a spurious [`EfficiencyWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.EfficiencyWarning.html#sklearn.exceptions.EfficiencyWarning "sklearn.exceptions.EfficiencyWarning")
     when given a precomputed sparse distance matrix. By [Vadim](https://github.com/Tweezky66)
    . [#34399](https://github.com/scikit-learn/scikit-learn/pull/34399)
    
*   Fix [`cluster.OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
     no longer raises a [`EfficiencyWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.EfficiencyWarning.html#sklearn.exceptions.EfficiencyWarning "sklearn.exceptions.EfficiencyWarning")
     when fitted on a precomputed sparse distance matrix. By [Dea María Léon](https://github.com/deamarialeon)
    . [#34692](https://github.com/scikit-learn/scikit-learn/pull/34692)
    

### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-datasets "Link to this heading")

*   Fix [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     now correctly recovers from a corrupted download by re-downloading it, instead of raising an error. By [Roman Yurchak](https://github.com/rth)
    . [#34262](https://github.com/scikit-learn/scikit-learn/pull/34262)
    
*   Fix [`datasets.fetch_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html#sklearn.datasets.fetch_file "sklearn.datasets.fetch_file")
     now raises a `ValueError` when `local_filename` is a path instead of a plain filename. By [Dea María Léon](https://github.com/DeaMariaLeon)
    . [#34815](https://github.com/scikit-learn/scikit-learn/pull/34815)
    

### [`sklearn.discriminant_analysis`](https://scikit-learn.org/stable/api/sklearn.discriminant_analysis.html#module-sklearn.discriminant_analysis "sklearn.discriminant_analysis")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-discriminant-analysis "Link to this heading")

*   Fix [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     and [`discriminant_analysis.QuadraticDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis "sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis")
     now return the same results when using `solver="svd"` and `solver="eigen"`. The normalization for `solver="svd"` is changed to `1/n_samples` instead of `1/(n_samples - n_classes)` and `1/(n_samples - 1)`, respectively, which is consistent with the maximum likelihood covariance estimator (same as the `solver="eigen"` default). By [Daniel Herrera-Esposito](https://github.com/dherrera1911)
    . [#33626](https://github.com/scikit-learn/scikit-learn/pull/33626)
    

### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-metrics "Link to this heading")

*   Efficiency Scorers created with [`make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
     no longer deep-copy metadata kwargs on each call, reducing memory usage during model selection and cross-validation. By [Stefanie Senger](https://github.com/StefanieSenger)
    . [#34236](https://github.com/scikit-learn/scikit-learn/pull/34236)
    

### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-neighbors "Link to this heading")

*   Fix [`neighbors.NearestNeighbors.radius_neighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.radius_neighbors "sklearn.neighbors.NearestNeighbors.radius_neighbors")
     now correctly handles an array-like `radius` when `n_jobs > 1` with the `ball_tree` and `kd_tree` algorithms. By [Nicolas Salvy](https://github.com/nicolassalvy)
    . [#34341](https://github.com/scikit-learn/scikit-learn/pull/34341)
    

### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-preprocessing "Link to this heading")

*   Fix Fixed a bug in [`preprocessing.QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
     where fitting on sparse data with `ignore_implicit_zeros=True` and subsampling could compute degenerate quantiles for some features. By [Arthur Lacote](https://github.com/cakedev0)
    . [#32587](https://github.com/scikit-learn/scikit-learn/pull/32587)
    

### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-svm "Link to this heading")

*   Fix Fixed a memory leak when calling the `fit` method of [`svm.LinearSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR "sklearn.svm.LinearSVR")
    . By [Jake VanderPlas](https://github.com/jakevdp)
    . [#34256](https://github.com/scikit-learn/scikit-learn/pull/34256)
    
*   Fix Fixed an out-of-bound write in the `fit` method of [`svm.LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
     memory when using `multi_class="crammer_singer"`. By [Jake VanderPlas](https://github.com/jakevdp)
    . [#34273](https://github.com/scikit-learn/scikit-learn/pull/34273)
    

### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-utils "Link to this heading")

*   Fix The HTML representation of estimators now truncates the output feature list to 100 entries to improve rendering performance for estimators with many output features. By [Dea María Léon](https://github.com/deamarialeon)
    . [#34362](https://github.com/scikit-learn/scikit-learn/pull/34362)
    
*   Fix Array API supporting functions and estimators that handle mixed input namespaces now make negative-stride NumPy arrays contiguous before transferring them to PyTorch through DLPack, avoiding a Python process abort in `torch.from_dlpack`. By [Yin Li](https://github.com/Kevin-Li-2025)
    . [#34380](https://github.com/scikit-learn/scikit-learn/pull/34380)
    
*   Fix The copy-to-clipboard icons in the HTML representation of estimators are now rendered as `<button>` elements with an `aria-label` and a visible focus outline, instead of non-interactive `<i>` elements, so they are reachable and usable with a keyboard and screen readers. By [Dea María Léon](https://github.com/deamarialeon)
    . [#34429](https://github.com/scikit-learn/scikit-learn/pull/34429)
    
*   Fix `set_output(transform="polars")` no longer emits a `DeprecationWarning` with `polars>=1.42.1` by using `how="horizontal_extend"` instead of the deprecated `how="horizontal"` when concatenating polars dataframes. By [Felix Hoehle](https://github.com/fhoehle)
    . [#34447](https://github.com/scikit-learn/scikit-learn/pull/34447)
    

Version 1.9.0[#](https://scikit-learn.org/stable/whats_new/v1.9.html#version-1-9-0 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**June 2026**

### Changed models[#](https://scikit-learn.org/stable/whats_new/v1.9.html#changed-models "Link to this heading")

*   Enhancement The `transform` method of [`preprocessing.PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
     with `method="yeo-johnson"` now uses the numerical more stable function `scipy.stats.yeojohnson` instead of an own implementation. The results may deviate in numerical edge cases or within the precision of floating-point arithmetic. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#33272](https://github.com/scikit-learn/scikit-learn/pull/33272)
    

### Changes impacting many modules[#](https://scikit-learn.org/stable/whats_new/v1.9.html#changes-impacting-many-modules "Link to this heading")

*   Major Feature Introduced a new config key: “sparse\_interface” to control whether functions return sparse objects using SciPy sparse matrix or SciPy sparse array. Use `sklearn.set_config(sparse_interface="sparray")` to have sklearn return sparse arrays. See more at [the SciPy Sparse Migration Guide.](https://docs.scipy.org/doc/scipy/reference/sparse.migration_to_sparray.html)
     The scikit-learn config “sparse\_interface” initially defaults to sparse matrix (“spmatrix”). The plan is to have the default change to sparse array (“sparray”) in a few releases. By [Dan Schult](https://github.com/dschult)
    . [#31177](https://github.com/scikit-learn/scikit-learn/pull/31177)
    
*   Enhancement Scikit-learn accepted a new library dependency: [narwhals](https://github.com/narwhals-dev/narwhals)
    . This is a very lightweight dependency that simplifies the support of dataframe input `X` and dataframe output as specified in the `set_output` API. Examples are pandas and polars dataframes. Narwhals can also help to support more dataframe libraries. Another reason for its adoption was that the dataframe interchange protocol (`__dataframe__`) on which scikit-learn relied so far for non-pandas dataframes got deprecated by polars and has run its course. By [Christian Lorentzen](https://github.com/lorentzenchr)
     and [Marco Gorelli](https://github.com/MarcoGorelli)
    . [#31127](https://github.com/scikit-learn/scikit-learn/pull/31127)
    
*   Enhancement The HTML representation of all scikit-learn estimators inheriting from [`base.BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
     now displays a new block showing the number and names of the output features when using a [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     or a [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
    . A copy-paste button is available for the output features name. By [Dea María Léon](https://github.com/DeaMariaLeon)
    , [Guillaume Lemaitre](https://github.com/glemaitre)
    , [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    , [Olivier Grisel](https://github.com/ogrisel)
    , [Antoine Baker](https://github.com/antoinebaker)
    . [#31937](https://github.com/scikit-learn/scikit-learn/pull/31937)
    
*   Enhancement [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
    , [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     and [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     now raise a clearer error message when an estimator class is passed instead of an instance. By [Anne Beyer](https://github.com/AnneBeyer)
    . [#32888](https://github.com/scikit-learn/scikit-learn/pull/32888)
    
*   Enhancement Checks for response values now provide a clearer error message when estimator does not implement the given `response_method`. By [Quentin Barthélemy](https://github.com/qbarthelemy)
    . [#33126](https://github.com/scikit-learn/scikit-learn/pull/33126)
    
*   Enhancement The HTML representation of all scikit-learn estimators inheriting from [`base.BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
     now includes a table displaying their fitted [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes)
    . These are all the public estimator attributes that are computed during the call to [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
     with a name that ends with an underscore. By [Dea María Léon](https://github.com/DeaMariaLeon)
    , [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    , [Olivier Grisel](https://github.com/ogrisel)
    , [Guillaume Lemaitre](https://github.com/glemaitre)
    , [Antoine Baker](https://github.com/antoinebaker)
    . [#33399](https://github.com/scikit-learn/scikit-learn/pull/33399)
    
*   Fix Raise ValueError when `sample_weight` contains only zero values to prevent meaningless input data during fitting. This change applies to all estimators that support the parameter `sample_weight`. This change also affects metrics that validate sample weights. By [Lucy Liu](https://github.com/lucyleeow)
     and [John Hendricks](https://github.com/j-hendricks)
    . [#32212](https://github.com/scikit-learn/scikit-learn/pull/32212)
    
*   Fix Some parameter descriptions in the HTML representation of estimators were not properly escaped, which could lead to malformed HTML if the description contains characters like `<` or `>`. By [Olivier Grisel](https://github.com/ogrisel)
    . [#32942](https://github.com/scikit-learn/scikit-learn/pull/32942)
    

### Support for Array API[#](https://scikit-learn.org/stable/whats_new/v1.9.html#id1 "Link to this heading")

Additional estimators and functions have been updated to include support for all [Array API](https://data-apis.org/array-api/latest/)
 compliant inputs.

See [Array API support (experimental)](https://scikit-learn.org/stable/modules/array_api.html#array-api)
 for more details.

*   Feature [`sklearn.metrics.d2_absolute_error_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_absolute_error_score.html#sklearn.metrics.d2_absolute_error_score "sklearn.metrics.d2_absolute_error_score")
     and [`sklearn.metrics.d2_pinball_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_pinball_score.html#sklearn.metrics.d2_pinball_score "sklearn.metrics.d2_pinball_score")
     now support array API compatible inputs. By [Virgil Chan](https://github.com/virchan)
    . [#31671](https://github.com/scikit-learn/scikit-learn/pull/31671)
    
*   Feature [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     now supports array API compatible inputs with `solver="lbfgs"`. By [Omar Salman](https://github.com/OmarManzoor)
     and [Olivier Grisel](https://github.com/ogrisel)
    . [#32644](https://github.com/scikit-learn/scikit-learn/pull/32644)
    
*   Feature [`metrics.average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
     now supports Array API compliant inputs. By [Stefanie Senger](https://github.com/StefanieSenger)
    . [#32909](https://github.com/scikit-learn/scikit-learn/pull/32909)
    
*   Feature [`sklearn.metrics.pairwise.paired_manhattan_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html#sklearn.metrics.pairwise.paired_manhattan_distances "sklearn.metrics.pairwise.paired_manhattan_distances")
     now supports array API compatible inputs. By [Bharat Raghunathan](https://github.com/bharatr21)
    . [#32979](https://github.com/scikit-learn/scikit-learn/pull/32979)
    
*   Feature [`metrics.pairwise_distances_argmin`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "sklearn.metrics.pairwise_distances_argmin")
     now supports array API compatible inputs. By [Bharat Raghunathan](https://github.com/bharatr21)
    . [#32985](https://github.com/scikit-learn/scikit-learn/pull/32985)
    
*   Feature [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
    , [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    , [`linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
    , [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    , and [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     now raise a more informative error message when arrays passed at fit and prediction time use different array API namespaces or devices. A new `sklearn.utils._array_api.move_estimator_to` utility is provided to move an estimator’s fitted array attributes to a different namespace and device. By [Jérôme Dockès](https://github.com/jeromedockes)
     and [Tim Head](https://github.com/betatim)
    . [#33076](https://github.com/scikit-learn/scikit-learn/pull/33076)
    
*   Feature [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     now supports Array API compliant inputs when all its transformers do. By [Olivier Grisel](https://github.com/ogrisel)
    . [#33263](https://github.com/scikit-learn/scikit-learn/pull/33263)
    
*   Feature [`linear_model.PoissonRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")
     now supports array API compatible inputs with `solver="lbfgs"`. By [Christian Lorentzen](https://github.com/lorentzenchr)
     and [Omar Salman](https://github.com/OmarManzoor)
    . [#33348](https://github.com/scikit-learn/scikit-learn/pull/33348)
    
*   Enhancement [`kernel_approximation.Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
     now supports array API compatible inputs. By [Emily Chen](https://github.com/EmilyXinyi)
    . [#29661](https://github.com/scikit-learn/scikit-learn/pull/29661)
    
*   Enhancement [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     now accepts array API compliant arrays with `gcv_mode` set to `auto` or `eigen`. By [Antoine Baker](https://github.com/antoinebaker)
    . [#33020](https://github.com/scikit-learn/scikit-learn/pull/33020)
    
*   Enhancement Internal NumPy CPU conversions now always attempt a generic DLPack-based transfer and only fallback to library-specific methods when necessary. This should ease support for additional array API and DLPack compliant input types without extending the ad hoc conversion helpers. By [Olivier Grisel](https://github.com/ogrisel)
    . [#33623](https://github.com/scikit-learn/scikit-learn/pull/33623)
    
*   Fix Fixed a bug that would cause Cython-based estimators to fail when fit on NumPy inputs when setting `sklearn.set_config(array_api_dispatch=True)`. By [Olivier Grisel](https://github.com/ogrisel)
    . [#32846](https://github.com/scikit-learn/scikit-learn/pull/32846)
    
*   Fix Fixes how `pos_label` is inferred when `pos_label` is set to `None`, in [`sklearn.metrics.brier_score_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
     and [`sklearn.metrics.d2_brier_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_brier_score.html#sklearn.metrics.d2_brier_score "sklearn.metrics.d2_brier_score")
    . By [Lucy Liu](https://github.com/lucyleeow)
    . [#32923](https://github.com/scikit-learn/scikit-learn/pull/32923)
    
*   Fix [`linear_model.ridge_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html#sklearn.linear_model.ridge_regression "sklearn.linear_model.ridge_regression")
     now correctly passes a Python scalar as `fill_value` to `xp.full` when broadcasting alpha for multi-target regression, ensuring compliance with the array API specification. This fixes compatibility issues with some array API backends. By [Olivier Grisel](https://github.com/ogrisel)
    . [#33437](https://github.com/scikit-learn/scikit-learn/pull/33437)
    
*   Fix [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     no longer emits spurious cross-library dtype comparison warnings when called with Array API inputs under `config_context(array_api_dispatch=True)`. By [Olivier Grisel](https://github.com/ogrisel)
    . [#33873](https://github.com/scikit-learn/scikit-learn/pull/33873)
    
*   Fix Fixed support for integer Array API inputs on devices that do not support `float64` in [`preprocessing.MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
    , [`preprocessing.MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")
    , [`preprocessing.KernelCenterer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KernelCenterer.html#sklearn.preprocessing.KernelCenterer "sklearn.preprocessing.KernelCenterer")
    , [`preprocessing.normalize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html#sklearn.preprocessing.normalize "sklearn.preprocessing.normalize")
    , [`utils.extmath.randomized_range_finder`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_range_finder.html#sklearn.utils.extmath.randomized_range_finder "sklearn.utils.extmath.randomized_range_finder")
    , and internal linear-model preprocessing and log-sum-exp utilities. By [Arthur Lacote](https://github.com/cakedev0)
    . [#33898](https://github.com/scikit-learn/scikit-learn/pull/33898)
    
*   Fix Fix passing an array as `alpha` in [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     when using the array API. By [Thomas Moreau](https://github.com/tommoral)
    . [#34004](https://github.com/scikit-learn/scikit-learn/pull/34004)
    
*   Fix [`linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
     and [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
     now store `classes_` in the namespace and on the device of `y` when fitted with array API inputs from mixed namespaces/devices, making them consistent with [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    . By [Arthur Lacote](https://github.com/cakedev0)
    . [#34065](https://github.com/scikit-learn/scikit-learn/pull/34065)
    
*   Fix Fixed a bug where NumPy-fitted estimators could raise an error with `config_context(array_api_dispatch=True)` when making predictions with array-like or SciPy sparse inputs, or when a fitted attribute was sparse, such as after calling [`linear_model.LogisticRegression.sparsify`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression.sparsify "sklearn.linear_model.LogisticRegression.sparsify")
    . By [Arthur Lacote](https://github.com/cakedev0)
    . [#34144](https://github.com/scikit-learn/scikit-learn/pull/34144)
    

### Metadata routing[#](https://scikit-learn.org/stable/whats_new/v1.9.html#id2 "Link to this heading")

Refer to the [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

*   Enhancement [`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
     now routes `groups` to the [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
     internally used for [cross fitting](https://scikit-learn.org/stable/glossary.html#term-0)
     in its [`fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder.fit_transform "sklearn.preprocessing.TargetEncoder.fit_transform")
    . By [Samruddhi Baviskar](https://github.com/samruddhibaviskar11)
     and [Stefanie Senger](https://github.com/StefanieSenger)
    . [#33089](https://github.com/scikit-learn/scikit-learn/pull/33089)
    
*   Fix Scorers now correctly request for metadata, and their `set_score_request` methods correctly detect metadata available in the signature of their `score_func`. Also, [`sklearn.linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     now correctly routes metadata to the underlying scorer when its `.score(...)` method is called. By [Adrin Jalali](https://github.com/adrinjalali)
     [#30859](https://github.com/scikit-learn/scikit-learn/pull/30859)
    
*   Fix If a class explicitly defines a `set_{method}_request` method, it will not be overridden by the metadata routing machinery. By [Adrin Jalali](https://github.com/adrinjalali)
     [#32111](https://github.com/scikit-learn/scikit-learn/pull/32111)
    
*   Fix Metadata routing objects ([`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
    , [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
    , and their per-method requests) no longer deep-copy the owning estimator. Since scikit-learn 1.8, the routing objects hold a reference to the owner estimator for display purposes, which caused [`get_routing_for_object`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.get_routing_for_object.html#sklearn.utils.metadata_routing.get_routing_for_object "sklearn.utils.metadata_routing.get_routing_for_object")
     and [`add_self_request`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter.add_self_request "sklearn.utils.metadata_routing.MetadataRouter.add_self_request")
     to transitively deep-copy the full estimator state, which can fail, and is very inefficient. By [Adrin Jalali](https://github.com/adrinjalali)
    . [#33827](https://github.com/scikit-learn/scikit-learn/pull/33827)
    
*   Fix [`learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
     now correctly routes `sample_weight` to the sub-estimator’s partial\_fit method if `exploit_incremental_learning` is set to `True`. By [Stefanie Senger](https://github.com/StefanieSenger)
    . [#34039](https://github.com/scikit-learn/scikit-learn/pull/34039)
    

### Callbacks[#](https://scikit-learn.org/stable/whats_new/v1.9.html#id3 "Link to this heading")

*   Major Feature This release introduces a new [callback API](https://scikit-learn.org/stable/callbacks.html#callbacks-user)
     to invoke callbacks during the fitting of estimators that support them. It comes with two built-in callbacks:
    
    *   [`sklearn.callback.ProgressBar`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ProgressBar.html#sklearn.callback.ProgressBar "sklearn.callback.ProgressBar")
        , to display progress bars.
        
    *   [`sklearn.callback.ScoringMonitor`](https://scikit-learn.org/stable/modules/generated/sklearn.callback.ScoringMonitor.html#sklearn.callback.ScoringMonitor "sklearn.callback.ScoringMonitor")
        , to compute and log a scoring metric at the end of each iteration.
        
    
    The following estimators support callbacks:
    
    *   [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
         (only with `solver="lbfgs"`).
        
    *   [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
        
    *   [`HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
        
    *   [`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
        
    *   [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
        
    *   [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
        
    *   [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
        
    
    It also provides a public API to implement callback support in custom estimators or or to implement custom callbacks, see the [developer’s guide](https://scikit-learn.org/stable/developers/callbacks.html#callbacks)
    .
    
    This API is experimental for now and may change without the usual deprecation cycle.
    
    By [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    , [François Paugam](https://github.com/FrancoisPgm)
     and [Stefanie Senger](https://github.com/StefanieSenger)
    . [#33322](https://github.com/scikit-learn/scikit-learn/pull/33322)
    

### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#id4 "Link to this heading")

*   Enhancement [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     and [`cluster.FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")
     now accept `metric="l2"` together with `linkage="ward"`. `metric="l2"` is equivalent to `metric="euclidean"`. [#24681](https://github.com/scikit-learn/scikit-learn/pull/24681)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    . [#24681](https://github.com/scikit-learn/scikit-learn/pull/24681)
    
*   Fix [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     now correctly handles sample weights during fitting. When sample weights are not None, mini-batch indices are created by sub-sampling with replacement using the normalized sample weights as probabilities. By [Shruti Nath](https://github.com/snath-xoc)
    , [Olivier Grisel](https://github.com/ogrisel)
    , and [Jeremie du Boisberranger](https://github.com/jeremiedbb)
    . [#30751](https://github.com/scikit-learn/scikit-learn/pull/30751)
    
*   Fix Fixed a bug in [`cluster.BisectingKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans")
     when using a custom callable `init` with `n_clusters > 2`. By [Mohammad Ahmadullah Khan](https://github.com/MAUK9086)
    . [#33148](https://github.com/scikit-learn/scikit-learn/pull/33148)
    

### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-compose "Link to this heading")

*   Fix The dotted line for [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     in its HTML display now includes only its elements. The behaviour when a remainder is used, has also been corrected. By [Dea María Léon](https://github.com/deamarialeon)
    . [#32713](https://github.com/scikit-learn/scikit-learn/pull/32713)
    
*   Fix Fixes the regression that a `KeyError` was thrown when using [`compose.ColumnTransformer.fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer.fit_transform "sklearn.compose.ColumnTransformer.fit_transform")
     with metadata routing and `remainder="passthrough"`. By [Anne Beyer](https://github.com/AnneBeyer)
    . [#33665](https://github.com/scikit-learn/scikit-learn/pull/33665)
    

### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#id5 "Link to this heading")

*   Efficiency Re-enabled compressed caching for [`datasets.fetch_kddcup99`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99 "sklearn.datasets.fetch_kddcup99")
    , reducing on-disk cache size without changing the public API. By [Unique Shrestha](https://github.com/un1u3)
    . [#33118](https://github.com/scikit-learn/scikit-learn/pull/33118)
    
*   Fix Fixed [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     to issue OpenML API calls to `https://www.openml.org/api/v1/` instead of `https://api.openml.org/api/v1/`, which no longer resolves or redirects correctly. By [Olivier Grisel](https://github.com/ogrisel)
    . [#33868](https://github.com/scikit-learn/scikit-learn/pull/33868)
    

### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-decomposition "Link to this heading")

*   Efficiency [`FastICA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")
     with `algorithm='deflation'` and `fun='logcosh'` is now an order of magnitude faster. By [Mohammad Ahmadullah Khan](https://github.com/MAUK9086)
    . [#33269](https://github.com/scikit-learn/scikit-learn/pull/33269)
    
*   Fix Fixed a typo (from `"OR"` to `"QR"`) in the list of allowed values for `power_iteration_normalizer` in [`decomposition.TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
    . By [Olivier Grisel](https://github.com/ogrisel)
    . [#33492](https://github.com/scikit-learn/scikit-learn/pull/33492)
    

### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-ensemble "Link to this heading")

*   Fix Fixed the way [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     compute their bin edges to properly and consistently handle [sample\_weight](https://scikit-learn.org/stable/glossary.html#term-sample_weight)
    . When `sample_weights=None` is passed to `fit` and the number of distinct feature values is less than the specified `max_bins`, the edges are still set to midpoints between consecutive feature values. Otherwise, the bin edges are set to weight-aware quantiles computed using the averaged inverted CDF method. If `n_samples` is larger than the `subsample` parameter, the weights are instead used to subsample the data (with replacement) and the bin edges are set using unweighted quantiles of the subsampled data. By [Shruti Nath](https://github.com/snath-xoc)
     and [Olivier Grisel](https://github.com/ogrisel)
    . [#29641](https://github.com/scikit-learn/scikit-learn/pull/29641)
    
*   Fix [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
     and [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
     now use `sample_weight` to draw the samples instead of forwarding them multiplied by a uniformly sampled mask to the underlying estimators. Furthermore, when `max_samples` is a float, it is now interpreted as a fraction of `sample_weight.sum()` instead of `X.shape[0]`. As sampling is done with replacement, a float `max_samples` greater than `1.0` is now allowed, as well as an integer `max_samples` greater then `X.shape[0]`. The default `max_samples=None` draws `X.shape[0]` samples, irrespective of `sample_weight`. By [Antoine Baker](https://github.com/antoinebaker)
    . [#31529](https://github.com/scikit-learn/scikit-learn/pull/31529)
    
*   Fix Both [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     and [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     with the default `"friedman_mse"` criterion were computing impurity values with an incorrect scaling, leading to unexpected trees in some cases. The implementation now uses `"squared_error"`, which is exactly equivalent to `"friedman_mse"` up to floating-point error discrepancies but computes correct impurity values. By [Arthur Lacote](https://github.com/cakedev0)
    . [#32708](https://github.com/scikit-learn/scikit-learn/pull/32708)
    
*   API Change The `criterion` parameter is now deprecated for classes [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     and [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
    , as both options (`"friedman_mse"` and `"squared_error"`) were producing the same results, up to floating-point rounding discrepancies and a bug in `"friedman_mse"`. By [Arthur Lacote](https://github.com/cakedev0)
    . [#32708](https://github.com/scikit-learn/scikit-learn/pull/32708)
    

### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-feature-extraction "Link to this heading")

*   Fix [`feature_extraction.image.reconstruct_from_patches_2d`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html#sklearn.feature_extraction.image.reconstruct_from_patches_2d "sklearn.feature_extraction.image.reconstruct_from_patches_2d")
     now produces correct results when a patch dimension equals the corresponding image dimension. By [Eden Rochman](https://github.com/EdenRochmanSharabi)
    . [#33643](https://github.com/scikit-learn/scikit-learn/pull/33643)
    

### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-feature-selection "Link to this heading")

*   Enhancement [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
     and [`feature_selection.RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
     now support estimators whose feature importance is a sparse matrix or array, notably by passing a user-defined callable to the parameter `importance_getter`. By [andymucyo-ops](https://github.com/andymucyo-ops)
     and [isaacambrogetti](https://github.com/isaacambrogetti)
    . [#33786](https://github.com/scikit-learn/scikit-learn/pull/33786)
    
*   Fix [`feature_selection.RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
     now uses stable sorting when ranking feature importances. This ensures that the feature selection is deterministic and consistent across runs when feature importances are tied. By [blitchj](https://github.com/blitchj)
    . [#29532](https://github.com/scikit-learn/scikit-learn/pull/29532)
    

### [`sklearn.gaussian_process`](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#module-sklearn.gaussian_process "sklearn.gaussian_process")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-gaussian-process "Link to this heading")

*   Efficiency Constructor signature of Gaussian process kernels is now cached, improving performance on small and medium datasets. By [Stanislav Terliakov](https://github.com/sterliakov)
    . [#33067](https://github.com/scikit-learn/scikit-learn/pull/33067)
    
*   Fix The hyperparameters of the default kernel of [`GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
    , namely `ConstantKernel() * RBF()`, are now optimized when `optimizer` is not `None`. Thus, `gpr = GaussianProcessRegressor().fit(X, y)` uses optimized kernel hyperparameters. By [Matthias De Lozzo](https://github.com/mdelozzo)
    . [#32964](https://github.com/scikit-learn/scikit-learn/pull/32964)
    

### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-inspection "Link to this heading")

*   Enhancement In [`inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
    , `multiclass_colors` now defaults to the more accessible [Petroff color sequence](https://arxiv.org/abs/2107.02270)
     for multiclass problems with up to 10 classes. By [Anne Beyer](https://github.com/AnneBeyer)
    . [#33709](https://github.com/scikit-learn/scikit-learn/pull/33709)
    
*   Fix In [`inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
    , `multiclass_colors` is now also used for multiclass plotting when `response_method="predict"`. By [Anne Beyer](https://github.com/AnneBeyer)
    . [#33015](https://github.com/scikit-learn/scikit-learn/pull/33015)
    
*   Fix In [`inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
    , `n_classes` is now inferred more robustly from the estimator. If it fails for custom estimators, a comprehensive error message is shown. By [Anne Beyer](https://github.com/AnneBeyer)
    . [#33202](https://github.com/scikit-learn/scikit-learn/pull/33202)
    
*   Fix [`inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
     now displays all class boundaries when using `plot_method="contour"` with all response\_methods, and displays all classes in distinct colors when using `plot_method="contourf"` with `response_method="predict"`. By [Anne Beyer](https://github.com/AnneBeyer)
     and [Levente Csibi](https://github.com/leweex95)
    . [#33300](https://github.com/scikit-learn/scikit-learn/pull/33300)
    
*   Fix In [`inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
    , a `ValueError` is now raised if the colormap passed to `multiclass_colors` contains fewer colors than there are classes in multiclass problems. By [Anne Beyer](https://github.com/AnneBeyer)
    . [#33419](https://github.com/scikit-learn/scikit-learn/pull/33419)
    
*   Fix For multiclass data, [`inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
     with `plot_method="contour"` now also displays class-specific contours for `response_method="predict_proba"` and `response_method="decision_function"`. Multiclass class boundary contour lines are now displayed in black by default for all response methods to avoid confusion. By [Anne Beyer](https://github.com/AnneBeyer)
    . [#33471](https://github.com/scikit-learn/scikit-learn/pull/33471)
    
*   Fix In [`inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
    , `multiclass_colors_` now always stores the colors for multiclass problems as a numpy array. By [Anne Beyer](https://github.com/AnneBeyer)
    . [#33651](https://github.com/scikit-learn/scikit-learn/pull/33651)
    

### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-linear-model "Link to this heading")

*   Feature [`linear_model.MultiTaskElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html#sklearn.linear_model.MultiTaskElasticNet "sklearn.linear_model.MultiTaskElasticNet")
    , [`linear_model.MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")
    , [`linear_model.MultiTaskLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model.MultiTaskLasso")
    , and [`linear_model.MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")
     now support fitting on sparse `X` as well as fitting with `sample_weight`. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#33440](https://github.com/scikit-learn/scikit-learn/pull/33440)
    
*   Efficiency [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     with `solver="lbfgs"` now estimates the gradient of the loss at `float32` precision when fitted with `float32` data (`X`) to improve training speed and memory efficiency. Previously, the input data would be implicitly cast to `float64`. If you relied on the previous behavior for numerical reasons, you can explicitly cast your data to `float64` before fitting to reproduce it. By [Omar Salman](https://github.com/OmarManzoor)
     and [Olivier Grisel](https://github.com/ogrisel)
    . [#32644](https://github.com/scikit-learn/scikit-learn/pull/32644)
    
*   Efficiency The [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
    , [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    , [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
    , [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
    , [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
    , [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
     and [`linear_model.BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
     classes now no longer make an unnecessary copy of dense `X, y` input during preprocessing when `copy_X=False` and `sample_weight` is provided. By [Junteng Li](https://github.com/JasonLiJT)
    . [#33041](https://github.com/scikit-learn/scikit-learn/pull/33041)
    
*   Enhancement [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     now correctly handles the case when the `scoring` parameter is set (to something not `None`) and when the CV splits result in folds where some class labels are missing. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#32828](https://github.com/scikit-learn/scikit-learn/pull/32828)
    
*   Enhancement [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
    , [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
     and [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
     now are able to fit Ridge regression, i.e. setting `l1_ratio=0`. Before this PR, the stopping criterion was a formulation of the dual gap that breaks down for `l1_ratio=0`. Now, an alternative dual gap formulation is used for this setting. This reduces the noise of raised warnings. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#32845](https://github.com/scikit-learn/scikit-learn/pull/32845)
    
*   Enhancement Efficiency [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
    , [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    , [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
    , [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
    , [`linear_model.MultiTaskElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html#sklearn.linear_model.MultiTaskElasticNet "sklearn.linear_model.MultiTaskElasticNet")
    , [`linear_model.MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")
     [`linear_model.MultiTaskLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model.MultiTaskLasso")
    , [`linear_model.MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")
     as well as [`linear_model.lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")
     and [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
     are now faster when fit with strong L1 penalty and many features. During gap safe screening of features, the update of the residual is now only performed if the coefficient is not zero. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#33161](https://github.com/scikit-learn/scikit-learn/pull/33161)
    
*   Fix [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
     and [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
     now take the `positive` parameter into account to compute the maximum `alpha` parameter, where all coefficients are zero. This impacts the search grid for the internally tuned `alpha` hyper-parameter stored in the attribute `alphas_`. By [Junteng Li](https://github.com/JasonLiJT)
    . [#32768](https://github.com/scikit-learn/scikit-learn/pull/32768)
    
*   Fix Correct the formulation of `alpha` within [`linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
    . The corrected value is `alpha = nu` instead of `alpha = nu / 2`. Note: This might result in changed values for the fitted attributes like `coef_` and `offset_` as well as the predictions made using this class. By [Omar Salman](https://github.com/OmarManzoor)
    . [#32778](https://github.com/scikit-learn/scikit-learn/pull/32778)
    
*   Fix [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
     now correctly handles the `precompute` parameter when `check_input=False`. Previously, the value of `precompute` was not properly treated which could lead to a ValueError. This also affects [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    , [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
    , [`linear_model.MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")
     and [`linear_model.MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")
    . By [Albert Dorador](https://github.com/adc-trust-ai)
    . [#33014](https://github.com/scikit-learn/scikit-learn/pull/33014)
    
*   Fix The leave-one out errors and model parameters estimated in [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     and [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
     when `cv=None` are now numerically stable in the small `alpha` regime. The default `auto` option is now equivalent to `eigen` and picks the cheaper option: eigendecomposition of the covariance matrix when `n_features <= n_samples`, respectively of the Gram matrix when `n_samples > n_features`. When `store_cv_results=True` and `X` is an integer array, the `cv_results_` attribute was wrongly coerced to the integer dtype of `X`, it now always has a float dtype. By [Antoine Baker](https://github.com/antoinebaker)
    . [#33020](https://github.com/scikit-learn/scikit-learn/pull/33020)
    
*   Fix Fixed a bug in [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     for multiclass settings where large negative values of [`linear_model.SGDClassifier.decision_function`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier.decision_function "sklearn.linear_model.SGDClassifier.decision_function")
     could lead to NaN values. In this case, this fix assigns equal probability for each class. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#33168](https://github.com/scikit-learn/scikit-learn/pull/33168)
    
*   Fix Fix unsigned integer overflow in [`linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
     when fitting with unsigned integer inputs. Internal label binarisation now avoids wrapping -1 for unsigned integer target dtypes. By [Virgil Chan](https://github.com/virchan)
    . [#33441](https://github.com/scikit-learn/scikit-learn/pull/33441)
    
*   Fix The `tol` parameter in [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
     is now set as the `cond` parameter of the [`scipy.linalg.lstsq`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lstsq.html#scipy.linalg.lstsq "(in SciPy v1.18.0)")
     solver when fitting on dense data. Some tests involving [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
     were brittle with the default `cond` values from `scipy` or `numpy`. Here at least the user has control over the `cond` value and can change it if necessary. By [Antoine Baker](https://github.com/antoinebaker)
    . [#33565](https://github.com/scikit-learn/scikit-learn/pull/33565)
    
*   Fix [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     no longer raises a `TypeError` when `refit=False` and `use_legacy_attributes=False` are set together with a non-elasticnet penalty like `l1_ratios=[0.0]`. Previously, `None` was stored in `l1_ratio_` instead of `0.0`, which caused `float()` to fail during post-processing. By [Mohamad Fazeli](https://github.com/Fazel94)
    . [#33902](https://github.com/scikit-learn/scikit-learn/pull/33902)
    
*   Fix [`linear_model.BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
     and [`linear_model.ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
     now center test features during `predict` to correctly compute predictive variance. By [Danilo Silva](https://github.com/danilo-silva-ufsc)
    . [#33918](https://github.com/scikit-learn/scikit-learn/pull/33918)
    
*   API Change Passing `sample_weight` as a positional argument to [`linear_model.LogisticRegressionCV.score`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV.score "sklearn.linear_model.LogisticRegressionCV.score")
     is deprecated and will be removed in version 1.11. Pass it as a keyword argument instead. By [Adrin Jalali](https://github.com/adrinjalali)
     [#30859](https://github.com/scikit-learn/scikit-learn/pull/30859)
     [#30859](https://github.com/scikit-learn/scikit-learn/pull/30859)
    
*   API Change The default value of the `scoring` parameter in [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     will change in version 1.11 from `None`, i.e. accuracy, to `"neg_log_loss"`. This is a much better default scoring function as it aligns with the log loss that logistic regression is minimizing (with regularization). For the meantime, you can silence the warning for this change by explicitly passing a value to `scoring`. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#33333](https://github.com/scikit-learn/scikit-learn/pull/33333)
    
*   API Change The parameter `n_alphas` has been deprecated for [`linear_model.lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")
     and [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
    . This deprecation follows the same deprecation that has happened for [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
     and [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
    . The parameter `alphas` now supports both integers and array-likes, removing the need for `n_alphas`. From now on, only `alphas` should be set, either to and integer to indicate the number of automatically generated alphas or to an array-like of values for the regularization path. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#33855](https://github.com/scikit-learn/scikit-learn/pull/33855)
    

### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-manifold "Link to this heading")

*   Efficiency The way ARPACK eigensolver is called in [`manifold.SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
     and [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     was improved, resulting in faster runtimes. By [Dmitry Kobak](https://github.com/dkobak)
    . [#33262](https://github.com/scikit-learn/scikit-learn/pull/33262)
    
*   Fix [`manifold.MDS.fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS.fit_transform "sklearn.manifold.MDS.fit_transform")
     returns the correct number of components when using `init="classical_mds"`. By [Ben Pedigo](https://github.com/bdpedigo)
    . [#33318](https://github.com/scikit-learn/scikit-learn/pull/33318)
    

### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#id6 "Link to this heading")

*   Major Feature [`metrics.metric_at_thresholds`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.metric_at_thresholds.html#sklearn.metrics.metric_at_thresholds "sklearn.metrics.metric_at_thresholds")
     has been added to compute a metric’s values across all possible thresholds. By [Carlo Lemos](https://github.com/vitaliset)
     and [Lucy Liu](https://github.com/lucyleeow)
    . [#32732](https://github.com/scikit-learn/scikit-learn/pull/32732)
    
*   Feature Add class method `from_cv_results` to [`metrics.PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")
    , which allows easy plotting of multiple precision-recall curves from [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
     results. By [Lucy Liu](https://github.com/lucyleeow)
    . [#30508](https://github.com/scikit-learn/scikit-learn/pull/30508)
    
*   Enhancement [`cohen_kappa_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#sklearn.metrics.cohen_kappa_score "sklearn.metrics.cohen_kappa_score")
     now has a `replace_undefined_by` param, that can be set to define the function’s return value when the metric is undefined (division by zero). By [Stefanie Senger](https://github.com/StefanieSenger)
    . [#31172](https://github.com/scikit-learn/scikit-learn/pull/31172)
    
*   Fix [`metrics.d2_pinball_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_pinball_score.html#sklearn.metrics.d2_pinball_score "sklearn.metrics.d2_pinball_score")
     and [`metrics.d2_absolute_error_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_absolute_error_score.html#sklearn.metrics.d2_absolute_error_score "sklearn.metrics.d2_absolute_error_score")
     now always use the `"averaged_inverted_cdf"` quantile method, both with and without sample weights. Previously, the `"linear"` quantile method was used only for the unweighted case leading the surprising discrepancies when comparing the results with unit weights. Note that all quantile interpolation methods are asymptotically equivalent in the large sample limit, but this fix can cause score value changes on small evaluation sets (without weights). By [Virgil Chan](https://github.com/virchan)
    . [#31671](https://github.com/scikit-learn/scikit-learn/pull/31671)
    
*   Fix [`metrics.accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
    , [`metrics.hamming_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "sklearn.metrics.hamming_loss")
     [`metrics.zero_one_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "sklearn.metrics.zero_one_loss")
    , [`metrics.matthews_corrcoef`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html#sklearn.metrics.matthews_corrcoef "sklearn.metrics.matthews_corrcoef")
     and [`metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
     (when `labels` is not `None`) now raise an error when `y_true` is string and `y_pred` is numeric, for all array-like inputs. Previously, lists and numpy arrays not of `object` dtype did not raise an error for this mixed input case. The above metrics will also raise an error for [label indicator matrix](https://scikit-learn.org/stable/glossary.html#term-label-indicator-matrix)
     inputs of inconsistent size, except for [`metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
     which does not accept label indicator matrix inputs. By [Lucy Liu](https://github.com/lucyleeow)
    . [#33086](https://github.com/scikit-learn/scikit-learn/pull/33086)
    
*   Fix Fixed [`metrics.pairwise_distances_argmin`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "sklearn.metrics.pairwise_distances_argmin")
     and [`metrics.pairwise_distances_argmin_min`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html#sklearn.metrics.pairwise_distances_argmin_min "sklearn.metrics.pairwise_distances_argmin_min")
     to avoid a quadratic-time path when many distances are identical, which could lead to severe slowdowns or even a stack overflow (segmentation fault) on large inputs. By [Arthur Lacote](https://github.com/cakedev0)
    . [#33252](https://github.com/scikit-learn/scikit-learn/pull/33252)
    
*   Fix [`metrics.PrecisionRecallDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
     and [`metrics.PrecisionRecallDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")
     now correctly plot chance level line when `y_true` is a pytorch tensor. By [Lucas Oliveira](https://github.com/lucolivi)
    . [#33405](https://github.com/scikit-learn/scikit-learn/pull/33405)
    
*   Fix `y_pred` was deprecated in favor of `y_proba` for [`metrics.log_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
     and [`metrics.d2_log_loss_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_log_loss_score.html#sklearn.metrics.d2_log_loss_score "sklearn.metrics.d2_log_loss_score")
     as predicted probabilities are expected, not predicted labels. By [Lucy Liu](https://github.com/lucyleeow)
    . [#33740](https://github.com/scikit-learn/scikit-learn/pull/33740)
    
*   Fix [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     no longer raises an error for the euclidean metric when called with `Y_norm_squared` and `n_jobs > 1`. By [Kunle Li](https://github.com/unw9527)
    . [#33876](https://github.com/scikit-learn/scikit-learn/pull/33876)
    
*   API Change Passing the `pos_label` and `sample_weight` parameters of [`metrics.confusion_matrix_at_thresholds`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#sklearn.metrics.confusion_matrix_at_thresholds "sklearn.metrics.confusion_matrix_at_thresholds")
     as positional arguments is deprecated and will be removed in v1.11. By [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    . [#33357](https://github.com/scikit-learn/scikit-learn/pull/33357)
    

### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-model-selection "Link to this heading")

*   Enhancement [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
     now uses `stable` sorting when doing the group distribution. This ensures that the splits are consistent across runs. By [marikabergengren](https://github.com/marikabergengren)
     and [Adrin Jalali](https://github.com/adrinjalali)
    . [#28464](https://github.com/scikit-learn/scikit-learn/pull/28464)
    
*   Fix [`model_selection.StratifiedGroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold "sklearn.model_selection.StratifiedGroupKFold")
     now raises a `ValueError` when `n_splits` is greater than the number of unique groups, preventing degenerate folds. By [Chani Fainendler](https://github.com/gitCHANI2005)
    . [#33176](https://github.com/scikit-learn/scikit-learn/pull/33176)
    
*   Fix Fixed incorrect [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
     when using `scoring="average_precision"` or similar in model selection utilities such as [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     or [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
     with multiclass classifiers. The `pos_label` parameter is only relevant for binary classification and was incorrectly being validated for scorers used on multiclass problems. By [Olivier Grisel](https://github.com/ogrisel)
    . [#33473](https://github.com/scikit-learn/scikit-learn/pull/33473)
    

### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#id7 "Link to this heading")

*   Fix [`neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
     and [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
     now work with string labels when `algorithm="brute"`. By [AAAZZZR](https://github.com/AAAZZZR)
    . [#33048](https://github.com/scikit-learn/scikit-learn/pull/33048)
    
*   Fix Fixed a quadratic-time path in the internal `simultaneous_sort` used by [`neighbors.BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
     and [`neighbors.KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
     queries when many distances are identical, which could lead to severe slowdowns or even a stack overflow (segmentation fault) on large inputs. Neighbor searches with tied distances no longer degrade badly in runtime. By [Arthur Lacote](https://github.com/cakedev0)
    . [#33252](https://github.com/scikit-learn/scikit-learn/pull/33252)
    

### [`sklearn.neural_network`](https://scikit-learn.org/stable/api/sklearn.neural_network.html#module-sklearn.neural_network "sklearn.neural_network")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-neural-network "Link to this heading")

*   Fix [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     with `early_stopping=True` no longer raises a `TypeError` when `y` contains non-numeric class labels (e.g. strings): validation scoring now checks finiteness only for floating predictions. By [Guillaume Lemaitre](https://github.com/glemaitre)
    . [#33774](https://github.com/scikit-learn/scikit-learn/pull/33774)
    

### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-pipeline "Link to this heading")

*   Fix Fixed a bug in [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     with `set_output(transform="polars")` when transformers produce duplicate column names. By [Jérémie du Boisberranger](https://github.com/jeremiedbb)
     and [Levente Csibi](https://github.com/leweex95)
    . [#32106](https://github.com/scikit-learn/scikit-learn/pull/32106)
    
*   Fix [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     now raises an `AttributeError` when accessing attributes that are not available on an empty pipeline. It’s therefore possible to call `dir` on an empty pipeline. By [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    . [#33362](https://github.com/scikit-learn/scikit-learn/pull/33362)
    

### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#id8 "Link to this heading")

*   Fix [`PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
     and [`QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
     now don’t raise a warning in `inverse_transform` related to feature names if `fit` is called using data with feature names. By [Thibault](https://github.com/ThibaultDECO)
     and [Mohammad Ahmadullah Khan](https://github.com/MAUK9086)
    . [#33268](https://github.com/scikit-learn/scikit-learn/pull/33268)
    
*   API Change The `shuffle` and the `random_state` parameters are deprecated on [`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
     and will be removed in version 1.11. Pass a cross-validation generator as `cv` argument to specify the shuffling behaviour instead. By [Stefanie Senger](https://github.com/StefanieSenger)
    . [#33453](https://github.com/scikit-learn/scikit-learn/pull/33453)
    

### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#id9 "Link to this heading")

*   Fix Raise more informative error when fitting [`svm.NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
     with all zero sample weights. By [Lucy Liu](https://github.com/lucyleeow)
     and [John Hendricks](https://github.com/j-hendricks)
    . [#32212](https://github.com/scikit-learn/scikit-learn/pull/32212)
    
*   API Change The `probability` parameter of [`sklearn.svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     and [`sklearn.svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
     is deprecated due to not being thread-safe and will be removed in 1.11. Use [`sklearn.calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     with the respective estimator and `ensemble=False` instead. By [Shruti Nath](https://github.com/snath-xoc)
    . [#32050](https://github.com/scikit-learn/scikit-learn/pull/32050)
    
*   API Change The `probA_` and `probB_` attributes of [`sklearn.svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     and [`sklearn.svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
     are deprecated due to deprecation of the `probability` parameter and will be removed in 1.11. By [Shruti Nath](https://github.com/snath-xoc)
    . [#33388](https://github.com/scikit-learn/scikit-learn/pull/33388)
    

### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#sklearn-tree "Link to this heading")

*   Feature In [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
     and [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , `criterion="absolute_error"` — and, consequently, all criterion options — now support missing values for dense training data `X`. By [Arthur Lacote](https://github.com/cakedev0)
    . [#32119](https://github.com/scikit-learn/scikit-learn/pull/32119)
    
*   Enhancement [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
    , [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
    , [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
    , and [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
     now support combining `monotonic_cst` with missing values in dense training data. This builds on the improvements to missing-value support for dense training data in [#32119](https://github.com/scikit-learn/scikit-learn/pull/32119)
    . By [Samuel O. Ronsin](https://github.com/samronsin)
    . [#27630](https://github.com/scikit-learn/scikit-learn/pull/27630)
    
*   Fix Fix calculation of node impurity in [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , `ensemble.ExtraTreeRegressor` and [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
     when missing values are present for the Poisson criterion. The Poisson criterion was returning invalid impurities (including negative values) when missing values were present. By [Arthur Lacote](https://github.com/cakedev0)
    . [#32119](https://github.com/scikit-learn/scikit-learn/pull/32119)
    
*   Fix Fixed feature-wise NaN detection in trees. Features could be seen as NaN-free for some edge-case patterns, which led to not considering splits with NaNs assigned to the left node for those features. This affects [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
     and [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
    . By [Arthur Lacote](https://github.com/cakedev0)
    . [#32193](https://github.com/scikit-learn/scikit-learn/pull/32193)
    
*   Fix Fixed color conversion in tree export so RGB values with zero channels are correctly converted to two-digit hexadecimal components (for example, `(0, 255, 0)` now yields `#00ff00`). By [Simon-Martin Schröder](https://github.com/moi90)
    . [#33845](https://github.com/scikit-learn/scikit-learn/pull/33845)
    
*   API Change `criterion="friedman_mse"` is now deprecated. This criterion was intended for gradient boosting but was incorrectly implemented in scikit-learn’s trees and was actually behaving identically to `criterion="squared_error"`. Use `criterion="squared_error"` instead. This affects [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
     and [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
    . By [Arthur Lacote](https://github.com/cakedev0)
    . [#32708](https://github.com/scikit-learn/scikit-learn/pull/32708)
    

### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.9.html#id10 "Link to this heading")

*   Enhancement [`utils.get_tags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.get_tags.html#sklearn.utils.get_tags "sklearn.utils.get_tags")
     now provides a clearer error message when a class is passed instead of an estimator instance. By [Achyuthan S](https://github.com/Achyuthan-S)
     and [Anne Beyer](https://github.com/AnneBeyer)
    . [#32565](https://github.com/scikit-learn/scikit-learn/pull/32565)
    
*   Fix The parameter table in the HTML representation of all scikit-learn estimators inheritiging from [`base.BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
    , displays each parameter documentation as a tooltip. The last tooltip of a parameter in the last table of any HTML representation was partially hidden. This issue has been fixed. By [Dea María Léon](https://github.com/DeaMariaLeon)
    . [#32887](https://github.com/scikit-learn/scikit-learn/pull/32887)
    
*   Fix Fixed `utils.stats._weighted_percentile` with `average=True` so zero-weight samples just before the end of the array are handled correctly. This can change results before the end of the array are handled correctly. This can change results when using `sample_weight` with [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
     (`strategy="quantile"`, `quantile_method="averaged_inverted_cdf"`) and in [`metrics.median_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")
    , [`metrics.d2_pinball_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_pinball_score.html#sklearn.metrics.d2_pinball_score "sklearn.metrics.d2_pinball_score")
    , and [`metrics.d2_absolute_error_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_absolute_error_score.html#sklearn.metrics.d2_absolute_error_score "sklearn.metrics.d2_absolute_error_score")
    . By [Arthur Lacote](https://github.com/cakedev0)
    . [#33127](https://github.com/scikit-learn/scikit-learn/pull/33127)
    
*   Fix [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     now correctly rejects pandas `StringDtype` columns when `dtype="numeric"` is requested. In pandas 3, string columns use `StringDtype` instead of `object` dtype, which caused `check_array` to silently accept string data instead of raising a `ValueError`. By [Olivier Grisel](https://github.com/ogrisel)
    . [#33491](https://github.com/scikit-learn/scikit-learn/pull/33491)
    
*   Fix The code path for polars dataframes in [`utils.validation.validate_data`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.validate_data.html#sklearn.utils.validation.validate_data "sklearn.utils.validation.validate_data")
     was made independent of the dataframe interchange protocol `__dataframe__`. This change was necessary to adapt to the recent deprecation of the interchange protocol in polars version 1.40. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#33789](https://github.com/scikit-learn/scikit-learn/pull/33789)
    
*   API Change [`utils.multiclass.unique_labels`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.unique_labels.html#sklearn.utils.multiclass.unique_labels "sklearn.utils.multiclass.unique_labels")
     now accepts `ys_types` parameter, which allows avoiding duplicate calls to [`utils.multiclass.type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
    . By [Lucy Liu](https://github.com/lucyleeow)
    . [#33086](https://github.com/scikit-learn/scikit-learn/pull/33086)
    

Code and documentation contributors

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 1.8, including:

AAAZZZR, ABHISHEK, Adrin Jalali, Agnus Paul, Ajay Raj, Akshita Sure, Albert Dorador Chalar, Alex Kuleshov, alexshacked, Alireza, Amine Abdellaziz, ANAND VENUGOPAL, Andres Nayeem Mejia, Andy, Anne Beyer, antoinebaker, Anton Karpov, Anvay, Arthur, Arthur Lacote, Arturo Amor, Ashutosh Devpura, Auguste Baum, Balaji Seshadri, baynecheke, Ben Pedigo, Bharat Raghunathan, Bodhi Russell Silberling, Bodhi Silberling, Bora Yongacoglu, camxx44, Chaitanya Dasari, Chani Fainendler, Charlie Tonneslan, Christian Lorentzen, Christian Veenhuis, Christian Yoon, Christine P. Chai, CipherCat, clijo, Colin Watson, C. Titus Brown, cui, Daniel Agyapong, Daniel Herrera-Esposito, Daniel R. Cassar, danilo-silva-ufsc, Dan Schult, david-cortes-intel, Dea María Léon, Dhruv Sharma, DhyeyTeraiya, Dimitri Papadopoulos Orfanos, Dmitry Kobak, EdenRochmanSharabi, eeshsaxena, Elizabeth DuPre, Emily (Xinyi) Chen, Eric Prestat, ethanglaser, fabianhenning, fhoehle, Florian Bourgey, François Paugam, Gaetan, Gaétan de Castellane, GarimaGarg222, GAUTAM V DATLA, Guillaume Lemaitre, Harsh Kumar Singh, Hashirama Senju, holodata-ej, Ho Yin Chau, imKartik5451, Isaacc, Itamar Turner-Trauring, Jake Blitch, Jake Vanderplas, James Dean, James Lamb, Jérémie du Boisberranger, Jim Crist-Harif, John Hendricks, Junteng Li, Karthik, Kiyarash Fazeli, Kropiunig, Kunle, Lev, Levente Csibi, Lisa, Loic Esteve, Lucas Colley, Lucas Oliveira, Lucy Liu, Luke Brace, Marco Edward Gorelli, marikabergengren, Martina Cvincekova, Matthias De Lozzo, Mohammad Ahmadullah Khan, Nguyen Cat Luong, Nicolas Salvy, Nikita, Nithurshen, Olivier Grisel, Omar Salman, pavitra danappa byali, pomrakna, prakritim01, Quentin Barthélemy, Ralf Gommers, Ram, Remi Gau, Reshama Shaikh, Riya Jha, Robert Pollak, Roman Yurchak, Rudrendu Paul, Samuel O. Ronsin, Sarvesh V, sauravyadav1008, Sepuri Sai Krishna, Seyi Kuforiji, Shadow\_Lu, shifanaaaa, Shruti Nath, Shubhan Chari, Shyan Paul, Simon-Martin Schröder, Sophia Houhamdi, Stanislav Terliakov, Stefanie Senger, Taoufik KEHAL, Tejas, TejasAnalyst, Thomas J. Fan, Thomas Moreau, Thomas S., Tim Head, Tweezky66, Unique Shrestha, Varun Agnihotri, Vashita, vashita-pandey, Veer Tiwari, Virgil Chan, Wiktor Olszowy, Xiao Yuan, Yann Lechelle, Yin Li

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)