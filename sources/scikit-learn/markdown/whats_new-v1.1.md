[Skip to main content](https://scikit-learn.org/stable/whats_new/v1.1.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v1.1.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v1.1.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v1.1.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v1.1.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v1.1.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v1.1.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v1.1.html)

Collapse Sidebar Expand Sidebar

Version 1.1[#](https://scikit-learn.org/stable/whats_new/v1.1.html#version-1-1 "Link to this heading")

=======================================================================================================

For a short description of the main highlights of the release, please refer to [Release Highlights for scikit-learn 1.1](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html#sphx-glr-auto-examples-release-highlights-plot-release-highlights-1-1-0-py)
.

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 1.1.3[#](https://scikit-learn.org/stable/whats_new/v1.1.html#version-1-1-3 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**October 2022**

This bugfix release only includes fixes for compatibility with the latest SciPy release >= 1.9.2. Notable changes include:

*   Fix Include `msvcp140.dll` in the scikit-learn wheels since it has been removed in the latest SciPy wheels. [#24631](https://github.com/scikit-learn/scikit-learn/pull/24631)
     by [Chiara Marmo](https://github.com/cmarmo)
    .
    
*   Enhancement Create wheels for Python 3.11. [#24446](https://github.com/scikit-learn/scikit-learn/pull/24446)
     by [Chiara Marmo](https://github.com/cmarmo)
    .
    

Other bug fixes will be available in the next 1.2 release, which will be released in the coming weeks.

Note that support for 32-bit Python on Windows has been dropped in this release. This is due to the fact that SciPy 1.9.2 also dropped the support for that platform. Windows users are advised to install the 64-bit version of Python instead.

Version 1.1.2[#](https://scikit-learn.org/stable/whats_new/v1.1.html#version-1-1-2 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**August 2022**

### Changed models[#](https://scikit-learn.org/stable/whats_new/v1.1.html#changed-models "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   Fix [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     now throws a `ValueError` when fit with `perplexity>=n_samples` to ensure mathematical correctness of the algorithm. [#10805](https://github.com/scikit-learn/scikit-learn/pull/10805)
     by [Mathias Andersen](https://github.com/MrMathias)
     and [#23471](https://github.com/scikit-learn/scikit-learn/pull/23471)
     by [Meekail Zain](https://github.com/micky774)
    .
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.1.html#changelog "Link to this heading")

*   Fix A default HTML representation is shown for meta-estimators with invalid parameters. [#24015](https://github.com/scikit-learn/scikit-learn/pull/24015)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Add support for F-contiguous arrays for estimators and functions whose back-end have been changed in 1.1. [#23990](https://github.com/scikit-learn/scikit-learn/pull/23990)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Fix Wheels are now available for MacOS 10.9 and greater. [#23833](https://github.com/scikit-learn/scikit-learn/pull/23833)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-base "Link to this heading")

*   Fix The `get_params` method of the [`base.BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
     class now supports estimators with `type`\-type params that have the `get_params` method. [#24017](https://github.com/scikit-learn/scikit-learn/pull/24017)
     by [Henry Sorsky](https://github.com/hsorsky)
    .
    

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-cluster "Link to this heading")

*   Fix Fixed a bug in [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
     that could trigger an error when splitting a node if there are duplicates in the dataset. [#23395](https://github.com/scikit-learn/scikit-learn/pull/23395)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-feature-selection "Link to this heading")

*   Fix [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
     defaults to selection threshold 1e-5 when the estimator is either [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     or [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
     with `l1_ratio` equals 1 or [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
    . [#23636](https://github.com/scikit-learn/scikit-learn/pull/23636)
     by [Hao Chun Chang](https://github.com/haochunchang)
    .
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-impute "Link to this heading")

*   Fix [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     uses the dtype seen in `fit` for `transform` when the dtype is object. [#22063](https://github.com/scikit-learn/scikit-learn/pull/22063)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-linear-model "Link to this heading")

*   Fix Use dtype-aware tolerances for the validation of gram matrices (passed by users or precomputed). [#22059](https://github.com/scikit-learn/scikit-learn/pull/22059)
     by [Malte S. Kurz](https://github.com/MalteKurz)
    .
    
*   Fix Fixed an error in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     with `solver="newton-cg"`, `fit_intercept=True`, and a single feature. [#23608](https://github.com/scikit-learn/scikit-learn/pull/23608)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    

#### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-manifold "Link to this heading")

*   Fix [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     now throws a `ValueError` when fit with `perplexity>=n_samples` to ensure mathematical correctness of the algorithm. [#10805](https://github.com/scikit-learn/scikit-learn/pull/10805)
     by [Mathias Andersen](https://github.com/MrMathias)
     and [#23471](https://github.com/scikit-learn/scikit-learn/pull/23471)
     by [Meekail Zain](https://github.com/micky774)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-metrics "Link to this heading")

*   Fix Fixed error message of [`metrics.coverage_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.coverage_error.html#sklearn.metrics.coverage_error "sklearn.metrics.coverage_error")
     for 1D array input. [#23548](https://github.com/scikit-learn/scikit-learn/pull/23548)
     by [Hao Chun Chang](https://github.com/haochunchang)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-preprocessing "Link to this heading")

*   Fix [`preprocessing.OrdinalEncoder.inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.inverse_transform "sklearn.preprocessing.OrdinalEncoder.inverse_transform")
     correctly handles use cases where `unknown_value` or `encoded_missing_value` is `nan`. [#24087](https://github.com/scikit-learn/scikit-learn/pull/24087)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-tree "Link to this heading")

*   Fix Fixed invalid memory access bug during fit in [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
     and [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    . [#23273](https://github.com/scikit-learn/scikit-learn/pull/23273)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

Version 1.1.1[#](https://scikit-learn.org/stable/whats_new/v1.1.html#version-1-1-1 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**May 2022**

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id1 "Link to this heading")

*   Enhancement The error message is improved when importing [`model_selection.HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
    , [`model_selection.HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
    , or [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     without importing the experimental flag. [#23194](https://github.com/scikit-learn/scikit-learn/pull/23194)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement Added an extension in doc/conf.py to automatically generate the list of estimators that handle NaN values. [#23198](https://github.com/scikit-learn/scikit-learn/pull/23198)
     by [Lise Kleiber](https://github.com/lisekleiber)
    , [Zhehao Liu](https://github.com/MaxwellLZH)
     and [Chiara Marmo](https://github.com/cmarmo)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-datasets "Link to this heading")

*   Fix Avoid timeouts in [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     by not passing a `timeout` argument, [#23358](https://github.com/scikit-learn/scikit-learn/pull/23358)
     by [Loïc Estève](https://github.com/lesteve)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-decomposition "Link to this heading")

*   Fix Avoid spurious warning in [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
     when `n_samples == n_components`. [#23264](https://github.com/scikit-learn/scikit-learn/pull/23264)
     by [Lucy Liu](https://github.com/lucyleeow)
    .
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id2 "Link to this heading")

*   Fix The `partial_fit` method of [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
     now conducts validation for `max_features` and `feature_names_in` parameters. [#23299](https://github.com/scikit-learn/scikit-learn/pull/23299)
     by [Long Bao](https://github.com/lorentzbao)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id3 "Link to this heading")

*   Fix Fixes [`metrics.precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")
     to compute precision-recall at 100% recall. The Precision-Recall curve now displays the last point corresponding to a classifier that always predicts the positive class: recall=100% and precision=class balance. [#23214](https://github.com/scikit-learn/scikit-learn/pull/23214)
     by [Stéphane Collot](https://github.com/stephanecollot)
     and [Max Baak](https://github.com/mbaak)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id4 "Link to this heading")

*   Fix [`preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
     with `degree` equal to 0 will raise error when `include_bias` is set to False, and outputs a single constant array when `include_bias` is set to True. [#23370](https://github.com/scikit-learn/scikit-learn/pull/23370)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id5 "Link to this heading")

*   Fix Fixes performance regression with low cardinality features for [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
    , and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
    . [#23410](https://github.com/scikit-learn/scikit-learn/pull/23410)
     by [Loïc Estève](https://github.com/lesteve)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-utils "Link to this heading")

*   Fix [`utils.class_weight.compute_sample_weight`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_sample_weight.html#sklearn.utils.class_weight.compute_sample_weight "sklearn.utils.class_weight.compute_sample_weight")
     now works with sparse `y`. [#23115](https://github.com/scikit-learn/scikit-learn/pull/23115)
     by [kernc](https://github.com/kernc)
    .
    

Version 1.1.0[#](https://scikit-learn.org/stable/whats_new/v1.1.html#version-1-1-0 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**May 2022**

### Minimal dependencies[#](https://scikit-learn.org/stable/whats_new/v1.1.html#minimal-dependencies "Link to this heading")

Version 1.1.0 of scikit-learn requires python 3.8+, numpy 1.17.3+ and scipy 1.3.2+. Optional minimal dependency is matplotlib 3.1.2+.

### Changed models[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id6 "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   Efficiency [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     now defaults to `algorithm="lloyd"` instead of `algorithm="auto"`, which was equivalent to `algorithm="elkan"`. Lloyd’s algorithm and Elkan’s algorithm converge to the same solution, up to numerical rounding errors, but in general Lloyd’s algorithm uses much less memory, and it is often faster.
    
*   Efficiency Fitting [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
    , and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     is on average 15% faster than in previous versions thanks to a new sort algorithm to find the best split. Models might be different because of a different handling of splits with tied criterion values: both the old and the new sorting algorithm are unstable sorting algorithms. [#22868](https://github.com/scikit-learn/scikit-learn/pull/22868)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix The eigenvectors initialization for [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     and [`manifold.SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
     now samples from a Gaussian when using the `'amg'` or `'lobpcg'` solver. This change improves numerical stability of the solver, but may result in a different model.
    
*   Fix [`feature_selection.f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")
     and [`feature_selection.r_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html#sklearn.feature_selection.r_regression "sklearn.feature_selection.r_regression")
     will now return finite score by default instead of `np.nan` and `np.inf` for some corner case. You can use `force_finite=False` if you really want to get non-finite values and keep the old behavior.
    
*   Fix Panda’s DataFrames with all non-string columns such as a MultiIndex no longer warns when passed into an Estimator. Estimators will continue to ignore the column names in DataFrames with non-string columns. For `feature_names_in_` to be defined, columns must be all strings. [#22410](https://github.com/scikit-learn/scikit-learn/pull/22410)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
     changed handling of bin edges slightly, which might result in a different encoding with the same data.
    
*   Fix [`calibration.calibration_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html#sklearn.calibration.calibration_curve "sklearn.calibration.calibration_curve")
     changed handling of bin edges slightly, which might result in a different output curve given the same data.
    
*   Fix [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     now uses the correct variance-scaling coefficient which may result in different model behavior.
    
*   Fix [`feature_selection.SelectFromModel.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.fit "sklearn.feature_selection.SelectFromModel.fit")
     and [`feature_selection.SelectFromModel.partial_fit`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel.partial_fit "sklearn.feature_selection.SelectFromModel.partial_fit")
     can now be called with `prefit=True`. `estimators_` will be a deep copy of `estimator` when `prefit=True`. [#23271](https://github.com/scikit-learn/scikit-learn/pull/23271)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id7 "Link to this heading")

*   Efficiency Low-level routines for reductions on pairwise distances for dense float64 datasets have been refactored. The following functions and estimators now benefit from improved performances in terms of hardware scalability and speed-ups:
    
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
    
    [#21987](https://github.com/scikit-learn/scikit-learn/pull/21987)
    , [#22064](https://github.com/scikit-learn/scikit-learn/pull/22064)
    , [#22065](https://github.com/scikit-learn/scikit-learn/pull/22065)
    , [#22288](https://github.com/scikit-learn/scikit-learn/pull/22288)
     and [#22320](https://github.com/scikit-learn/scikit-learn/pull/22320)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Enhancement All scikit-learn models now generate a more informative error message when some input contains unexpected `NaN` or infinite values. In particular the message contains the input name (“X”, “y” or “sample\_weight”) and if an unexpected `NaN` value is found in `X`, the error message suggests potential solutions. [#21219](https://github.com/scikit-learn/scikit-learn/pull/21219)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Enhancement All scikit-learn models now generate a more informative error message when setting invalid hyper-parameters with `set_params`. [#21542](https://github.com/scikit-learn/scikit-learn/pull/21542)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Enhancement Removes random unique identifiers in the HTML representation. With this change, jupyter notebooks are reproducible as long as the cells are run in the same order. [#23098](https://github.com/scikit-learn/scikit-learn/pull/23098)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Estimators with `non_deterministic` tag set to `True` will skip both `check_methods_sample_order_invariance` and `check_methods_subset_invariance` tests. [#22318](https://github.com/scikit-learn/scikit-learn/pull/22318)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
    .
    
*   API Change The option for using the log loss, aka binomial or multinomial deviance, via the `loss` parameters was made more consistent. The preferred way is by setting the value to `"log_loss"`. Old option names are still valid and produce the same models, but are deprecated and will be removed in version 1.3.
    
    *   For [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
        , the `loss` parameter name “deviance” is deprecated in favor of the new name “log\_loss”, which is now the default. [#23036](https://github.com/scikit-learn/scikit-learn/pull/23036)
         by [Christian Lorentzen](https://github.com/lorentzenchr)
        .
        
    *   For [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
        , the `loss` parameter names “auto”, “binary\_crossentropy” and “categorical\_crossentropy” are deprecated in favor of the new name “log\_loss”, which is now the default. [#23040](https://github.com/scikit-learn/scikit-learn/pull/23040)
         by [Christian Lorentzen](https://github.com/lorentzenchr)
        .
        
    *   For [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
        , the `loss` parameter name “log” is deprecated in favor of the new name “log\_loss”. [#23046](https://github.com/scikit-learn/scikit-learn/pull/23046)
         by [Christian Lorentzen](https://github.com/lorentzenchr)
        .
        
*   API Change Rich html representation of estimators is now enabled by default in Jupyter notebooks. It can be deactivated by setting `display='text'` in [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
    . [#22856](https://github.com/scikit-learn/scikit-learn/pull/22856)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-calibration "Link to this heading")

*   Enhancement [`calibration.calibration_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html#sklearn.calibration.calibration_curve "sklearn.calibration.calibration_curve")
     accepts a parameter `pos_label` to specify the positive class label. [#21032](https://github.com/scikit-learn/scikit-learn/pull/21032)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Enhancement [`calibration.CalibratedClassifierCV.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV.fit "sklearn.calibration.CalibratedClassifierCV.fit")
     now supports passing `fit_params`, which are routed to the `base_estimator`. [#18170](https://github.com/scikit-learn/scikit-learn/pull/18170)
     by [Benjamin Bossan](https://github.com/BenjaminBossan)
    .
    
*   Enhancement [`calibration.CalibrationDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay "sklearn.calibration.CalibrationDisplay")
     accepts a parameter `pos_label` to add this information to the plot. [#21038](https://github.com/scikit-learn/scikit-learn/pull/21038)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`calibration.calibration_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html#sklearn.calibration.calibration_curve "sklearn.calibration.calibration_curve")
     handles bin edges more consistently now. [#14975](https://github.com/scikit-learn/scikit-learn/pull/14975)
     by [Andreas Müller](https://amueller.github.io/)
     and [#22526](https://github.com/scikit-learn/scikit-learn/pull/22526)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   API Change [`calibration.calibration_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html#sklearn.calibration.calibration_curve "sklearn.calibration.calibration_curve")
    ’s `normalize` parameter is now deprecated and will be removed in version 1.3. It is recommended that a proper probability (i.e. a classifier’s [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
     positive class) is used for `y_prob`. [#23095](https://github.com/scikit-learn/scikit-learn/pull/23095)
     by [Jordan Silke](https://github.com/jsilke)
    .
    

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id8 "Link to this heading")

*   Major Feature [`cluster.BisectingKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans")
     introducing Bisecting K-Means algorithm [#20031](https://github.com/scikit-learn/scikit-learn/pull/20031)
     by [Michal Krawczyk](https://github.com/michalkrawczyk)
    , [Tom Dupre la Tour](https://github.com/TomDLT)
     and [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Enhancement [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     and [`cluster.spectral_clustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")
     now include the new `'cluster_qr'` method that clusters samples in the embedding space as an alternative to the existing `'kmeans'` and `'discrete'` methods. See [`cluster.spectral_clustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")
     for more details. [#21148](https://github.com/scikit-learn/scikit-learn/pull/21148)
     by [Andrew Knyazev](https://github.com/lobpcg)
    .
    
*   Enhancement Adds [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     to [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
    , [`cluster.FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")
    , [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    , [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
    . [#22255](https://github.com/scikit-learn/scikit-learn/pull/22255)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     now raises consistent error messages when passed invalid values for `n_clusters`, `n_init`, `gamma`, `n_neighbors`, `eigen_tol` or `degree`. [#21881](https://github.com/scikit-learn/scikit-learn/pull/21881)
     by [Hugo Vassard](https://github.com/hvassard)
    .
    
*   Enhancement [`cluster.AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
     now returns cluster centers and labels if they exist, even if the model has not fully converged. When returning these potentially-degenerate cluster centers and labels, a new warning message is shown. If no cluster centers were constructed, then the cluster centers remain an empty list with labels set to `-1` and the original warning message is shown. [#22217](https://github.com/scikit-learn/scikit-learn/pull/22217)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Efficiency In [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    , the default `algorithm` is now `"lloyd"` which is the full classical EM-style algorithm. Both `"auto"` and `"full"` are deprecated and will be removed in version 1.3. They are now aliases for `"lloyd"`. The previous default was `"auto"`, which relied on Elkan’s algorithm. Lloyd’s algorithm uses less memory than Elkan’s, it is faster on many datasets, and its results are identical, hence the change. [#21735](https://github.com/scikit-learn/scikit-learn/pull/21735)
     by [Aurélien Geron](https://github.com/ageron)
    .
    
*   Fix [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    ’s `init` parameter now properly supports array-like input and NumPy string scalars. [#22154](https://github.com/scikit-learn/scikit-learn/pull/22154)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-compose "Link to this heading")

*   Fix [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     now removes validation errors from `__init__` and `set_params` methods. [#22537](https://github.com/scikit-learn/scikit-learn/pull/22537)
     by [iofall](https://github.com/iofall)
     and [Arisa Y.](https://github.com/arisayosh)
    .
    
*   Fix [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     functionality in [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     was broken when columns were specified using `slice`. This is fixed in [#22775](https://github.com/scikit-learn/scikit-learn/pull/22775)
     and [#22913](https://github.com/scikit-learn/scikit-learn/pull/22913)
     by [randomgeek78](https://github.com/randomgeek78)
    .
    

#### [`sklearn.covariance`](https://scikit-learn.org/stable/api/sklearn.covariance.html#module-sklearn.covariance "sklearn.covariance")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-covariance "Link to this heading")

*   Fix [`covariance.GraphicalLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")
     now accepts NumPy array for the parameter `alphas`. [#22493](https://github.com/scikit-learn/scikit-learn/pull/22493)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.cross_decomposition`](https://scikit-learn.org/stable/api/sklearn.cross_decomposition.html#module-sklearn.cross_decomposition "sklearn.cross_decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-cross-decomposition "Link to this heading")

*   Enhancement the `inverse_transform` method of [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
    , [`cross_decomposition.PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
     and [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
     now allows reconstruction of a `X` target when a `Y` parameter is given. [#19680](https://github.com/scikit-learn/scikit-learn/pull/19680)
     by [Robin Thibaut](https://github.com/robinthibaut)
    .
    
*   Enhancement Adds [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     to all transformers in the [`cross_decomposition`](https://scikit-learn.org/stable/api/sklearn.cross_decomposition.html#module-sklearn.cross_decomposition "sklearn.cross_decomposition")
     module: [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
    , [`cross_decomposition.PLSSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD "sklearn.cross_decomposition.PLSSVD")
    , [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
    , and [`cross_decomposition.PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
    . [#22119](https://github.com/scikit-learn/scikit-learn/pull/22119)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix The shape of the [coef\_](https://scikit-learn.org/stable/glossary.html#term-coef_)
     attribute of [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
    , [`cross_decomposition.PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
     and [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
     will change in version 1.3, from `(n_features, n_targets)` to `(n_targets, n_features)`, to be consistent with other linear models and to make it work with interface expecting a specific shape for `coef_` (e.g. [`feature_selection.RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
    ). [#22016](https://github.com/scikit-learn/scikit-learn/pull/22016)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change add the fitted attribute `intercept_` to [`cross_decomposition.PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
    , [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
    , and [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
    . The method `predict` is indeed equivalent to `Y = X @ coef_ + intercept_`. [#22015](https://github.com/scikit-learn/scikit-learn/pull/22015)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id9 "Link to this heading")

*   Feature [`datasets.load_files`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_files.html#sklearn.datasets.load_files "sklearn.datasets.load_files")
     now accepts an ignore list and an allow list based on file extensions. [#19747](https://github.com/scikit-learn/scikit-learn/pull/19747)
     by [Tony Attalla](https://github.com/tonyattalla)
     and [#22498](https://github.com/scikit-learn/scikit-learn/pull/22498)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Enhancement [`datasets.make_swiss_roll`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#sklearn.datasets.make_swiss_roll "sklearn.datasets.make_swiss_roll")
     now supports the optional argument hole; when set to True, it returns the swiss-hole dataset. [#21482](https://github.com/scikit-learn/scikit-learn/pull/21482)
     by [Sebastian Pujalte](https://github.com/pujaltes)
    .
    
*   Enhancement [`datasets.make_blobs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
     no longer copies data during the generation process, therefore uses less memory. [#22412](https://github.com/scikit-learn/scikit-learn/pull/22412)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
    .
    
*   Enhancement [`datasets.load_diabetes`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
     now accepts the parameter `scaled`, to allow loading unscaled data. The scaled version of this dataset is now computed from the unscaled data, and can produce slightly different results than in previous version (within a 1e-4 absolute tolerance). [#16605](https://github.com/scikit-learn/scikit-learn/pull/16605)
     by [Mandy Gu](https://github.com/happilyeverafter95)
    .
    
*   Enhancement [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     now has two optional arguments `n_retries` and `delay`. By default, [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     will retry 3 times in case of a network failure with a delay between each try. [#21901](https://github.com/scikit-learn/scikit-learn/pull/21901)
     by [Rileran](https://github.com/rileran)
    .
    
*   Fix [`datasets.fetch_covtype`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#sklearn.datasets.fetch_covtype "sklearn.datasets.fetch_covtype")
     is now concurrent-safe: data is downloaded to a temporary directory before being moved to the data directory. [#23113](https://github.com/scikit-learn/scikit-learn/pull/23113)
     by [Ilion Beyst](https://github.com/iasoon)
    .
    
*   API Change [`datasets.make_sparse_coded_signal`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_coded_signal.html#sklearn.datasets.make_sparse_coded_signal "sklearn.datasets.make_sparse_coded_signal")
     now accepts a parameter `data_transposed` to explicitly specify the shape of matrix `X`. The default behavior `True` is to return a transposed matrix `X` corresponding to a `(n_features, n_samples)` shape. The default value will change to `False` in version 1.3. [#21425](https://github.com/scikit-learn/scikit-learn/pull/21425)
     by [Gabriel Stefanini Vicente](https://github.com/g4brielvs)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id10 "Link to this heading")

*   Major Feature Added a new estimator [`decomposition.MiniBatchNMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")
    . It is a faster but less accurate version of non-negative matrix factorization, better suited for large datasets. [#16948](https://github.com/scikit-learn/scikit-learn/pull/16948)
     by [Chiara Marmo](https://github.com/cmarmo)
    , [Patricio Cerda](https://github.com/pcerda)
     and [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Enhancement [`decomposition.dict_learning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#sklearn.decomposition.dict_learning "sklearn.decomposition.dict_learning")
    , [`decomposition.dict_learning_online`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html#sklearn.decomposition.dict_learning_online "sklearn.decomposition.dict_learning_online")
     and [`decomposition.sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")
     preserve dtype for `numpy.float32`. [`decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
    , [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
     and [`decomposition.SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")
     preserve dtype for `numpy.float32`. [#22002](https://github.com/scikit-learn/scikit-learn/pull/22002)
     by [Takeshi Oura](https://github.com/takoika)
    .
    
*   Enhancement [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     exposes a parameter `n_oversamples` to tune [`utils.extmath.randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
     and get accurate results when the number of features is large. [#21109](https://github.com/scikit-learn/scikit-learn/pull/21109)
     by [Smile](https://github.com/x-shadow-man)
    .
    
*   Enhancement The [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
     and [`decomposition.dict_learning_online`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html#sklearn.decomposition.dict_learning_online "sklearn.decomposition.dict_learning_online")
     have been refactored and now have a stopping criterion based on a small change of the dictionary or objective function, controlled by the new `max_iter`, `tol` and `max_no_improvement` parameters. In addition, some of their parameters and attributes are deprecated.
    
    *   the `n_iter` parameter of both is deprecated. Use `max_iter` instead.
        
    *   the `iter_offset`, `return_inner_stats`, `inner_stats` and `return_n_iter` parameters of [`decomposition.dict_learning_online`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html#sklearn.decomposition.dict_learning_online "sklearn.decomposition.dict_learning_online")
         serve internal purpose and are deprecated.
        
    *   the `inner_stats_`, `iter_offset_` and `random_state_` attributes of [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
         serve internal purpose and are deprecated.
        
    *   the default value of the `batch_size` parameter of both will change from 3 to 256 in version 1.3.
        
    
    [#18975](https://github.com/scikit-learn/scikit-learn/pull/18975)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Enhancement [`decomposition.SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")
     and [`decomposition.MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")
     preserve dtype for `numpy.float32`. [#22111](https://github.com/scikit-learn/scikit-learn/pull/22111)
     by [Takeshi Oura](https://github.com/takoika)
    .
    
*   Enhancement [`decomposition.TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
     now allows `n_components == n_features`, if `algorithm='randomized'`. [#22181](https://github.com/scikit-learn/scikit-learn/pull/22181)
     by [Zach Deane-Mayer](https://github.com/zachmayer)
    .
    
*   Enhancement Adds [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     to all transformers in the [`decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
     module: [`decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
    , [`decomposition.FactorAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")
    , [`decomposition.FastICA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")
    , [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
    , [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
    , [`decomposition.LatentDirichletAllocation`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "sklearn.decomposition.LatentDirichletAllocation")
    , [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
    , [`decomposition.MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")
    , [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
    , [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
    , [`decomposition.SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")
    , and [`decomposition.TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
    . [#21334](https://github.com/scikit-learn/scikit-learn/pull/21334)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`decomposition.TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
     exposes the parameter `n_oversamples` and `power_iteration_normalizer` to tune [`utils.extmath.randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
     and get accurate results when the number of features is large, the rank of the matrix is high, or other features of the matrix make low rank approximation difficult. [#21705](https://github.com/scikit-learn/scikit-learn/pull/21705)
     by [Jay S. Stanley III](https://github.com/stanleyjs)
    .
    
*   Enhancement [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     exposes the parameter `power_iteration_normalizer` to tune [`utils.extmath.randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
     and get more accurate results when low rank approximation is difficult. [#21705](https://github.com/scikit-learn/scikit-learn/pull/21705)
     by [Jay S. Stanley III](https://github.com/stanleyjs)
    .
    
*   Fix [`decomposition.FastICA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")
     now validates input parameters in `fit` instead of `__init__`. [#21432](https://github.com/scikit-learn/scikit-learn/pull/21432)
     by [Hannah Bohle](https://github.com/hhnnhh)
     and [Maren Westermann](https://github.com/marenwestermann)
    .
    
*   Fix [`decomposition.FastICA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")
     now accepts `np.float32` data without silent upcasting. The dtype is preserved by `fit` and `fit_transform` and the main fitted attributes use a dtype of the same precision as the training data. [#22806](https://github.com/scikit-learn/scikit-learn/pull/22806)
     by [Jihane Bennis](https://github.com/JihaneBennis)
     and [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Fix [`decomposition.FactorAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")
     now validates input parameters in `fit` instead of `__init__`. [#21713](https://github.com/scikit-learn/scikit-learn/pull/21713)
     by [Haya](https://github.com/HayaAlmutairi)
     and [Krum Arnaudov](https://github.com/krumeto)
    .
    
*   Fix [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
     now validates input parameters in `fit` instead of `__init__`. [#21567](https://github.com/scikit-learn/scikit-learn/pull/21567)
     by [Maggie Chege](https://github.com/MaggieChege)
    .
    
*   Fix [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     and [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
     more safely calculate precision using the inverse of the covariance matrix if `self.noise_variance_` is zero. [#22300](https://github.com/scikit-learn/scikit-learn/pull/22300)
     by [Meekail Zain](https://github.com/micky774)
     and [#15948](https://github.com/scikit-learn/scikit-learn/pull/15948)
     by [@sysuresh](https://github.com/sysuresh)
    .
    
*   Fix Greatly reduced peak memory usage in [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     when calling `fit` or `fit_transform`. [#22553](https://github.com/scikit-learn/scikit-learn/pull/22553)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   API Change [`decomposition.FastICA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")
     now supports unit variance for whitening. The default value of its `whiten` argument will change from `True` (which behaves like `'arbitrary-variance'`) to `'unit-variance'` in version 1.3. [#19490](https://github.com/scikit-learn/scikit-learn/pull/19490)
     by [Facundo Ferrin](https://github.com/fferrin)
     and [Julien Jerphanion](https://github.com/jjerphan)
    .
    

#### [`sklearn.discriminant_analysis`](https://scikit-learn.org/stable/api/sklearn.discriminant_analysis.html#module-sklearn.discriminant_analysis "sklearn.discriminant_analysis")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-discriminant-analysis "Link to this heading")

*   Enhancement Adds [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     to [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
    . [#22120](https://github.com/scikit-learn/scikit-learn/pull/22120)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     now uses the correct variance-scaling coefficient which may result in different model behavior. [#15984](https://github.com/scikit-learn/scikit-learn/pull/15984)
     by [Okon Samuel](https://github.com/OkonSamuel)
     and [#22696](https://github.com/scikit-learn/scikit-learn/pull/22696)
     by [Meekail Zain](https://github.com/micky774)
    .
    

#### [`sklearn.dummy`](https://scikit-learn.org/stable/api/sklearn.dummy.html#module-sklearn.dummy "sklearn.dummy")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-dummy "Link to this heading")

*   Fix [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
     no longer overrides the `constant` parameter during `fit`. [#22486](https://github.com/scikit-learn/scikit-learn/pull/22486)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-ensemble "Link to this heading")

*   Major Feature Added additional option `loss="quantile"` to [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     for modelling quantiles. The quantile level can be specified with the new parameter `quantile`. [#21800](https://github.com/scikit-learn/scikit-learn/pull/21800)
     and [#20567](https://github.com/scikit-learn/scikit-learn/pull/20567)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Efficiency `fit` of [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     now calls [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     with parameter `force_all_finite=False` for non initial warm-start runs as it has already been checked before. [#22159](https://github.com/scikit-learn/scikit-learn/pull/22159)
     by [Geoffrey Paris](https://github.com/Geoffrey-Paris)
    .
    
*   Enhancement [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     is faster, for binary and in particular for multiclass problems thanks to the new private loss function module. [#20811](https://github.com/scikit-learn/scikit-learn/pull/20811)
    , [#20567](https://github.com/scikit-learn/scikit-learn/pull/20567)
     and [#21814](https://github.com/scikit-learn/scikit-learn/pull/21814)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Enhancement Adds support to use pre-fit models with `cv="prefit"` in [`ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
     and [`ensemble.StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
    . [#16748](https://github.com/scikit-learn/scikit-learn/pull/16748)
     by [Siqi He](https://github.com/siqi-he)
     and [#22215](https://github.com/scikit-learn/scikit-learn/pull/22215)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Enhancement [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
     and [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
     have the new `criterion="log_loss"`, which is equivalent to `criterion="entropy"`. [#23047](https://github.com/scikit-learn/scikit-learn/pull/23047)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Enhancement Adds [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     to [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
    , [`ensemble.VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
    , [`ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
    , and [`ensemble.StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
    . [#22695](https://github.com/scikit-learn/scikit-learn/pull/22695)
     and [#22697](https://github.com/scikit-learn/scikit-learn/pull/22697)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`ensemble.RandomTreesEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")
     now has an informative [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     function that includes both tree index and leaf index in the output feature names. [#21762](https://github.com/scikit-learn/scikit-learn/pull/21762)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
     and [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Efficiency Fitting a [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
    , [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
    , and [`ensemble.RandomTreesEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")
     is now faster in a multiprocessing setting, especially for subsequent fits with `warm_start` enabled. [#22106](https://github.com/scikit-learn/scikit-learn/pull/22106)
     by [Pieter Gijsbers](https://github.com/PGijsbers)
    .
    
*   Fix Change the parameter `validation_fraction` in [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     so that an error is raised if anything other than a float is passed in as an argument. [#21632](https://github.com/scikit-learn/scikit-learn/pull/21632)
     by [Genesis Valencia](https://github.com/genvalen)
    .
    
*   Fix Removed a potential source of CPU oversubscription in [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     when CPU resource usage is limited, for instance using cgroups quota in a docker container. [#22566](https://github.com/scikit-learn/scikit-learn/pull/22566)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     no longer warn when fitting on a pandas DataFrame with a non-default `scoring` parameter and early\_stopping enabled. [#22908](https://github.com/scikit-learn/scikit-learn/pull/22908)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Fixes HTML repr for [`ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
     and [`ensemble.StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
    . [#23097](https://github.com/scikit-learn/scikit-learn/pull/23097)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change The attribute `loss_` of [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     has been deprecated and will be removed in version 1.3. [#23079](https://github.com/scikit-learn/scikit-learn/pull/23079)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   API Change Changed the default of `max_features` to 1.0 for [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
     and to `"sqrt"` for [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    . Note that these give the same fit results as before, but are much easier to understand. The old default value `"auto"` has been deprecated and will be removed in version 1.3. The same changes are also applied for [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
     and [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
    . [#20803](https://github.com/scikit-learn/scikit-learn/pull/20803)
     by [Brian Sun](https://github.com/bsun94)
    .
    
*   Efficiency Improve runtime performance of [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     by skipping repetitive input checks. [#23149](https://github.com/scikit-learn/scikit-learn/pull/23149)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-feature-extraction "Link to this heading")

*   Feature [`feature_extraction.FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
     now supports PyPy. [#23023](https://github.com/scikit-learn/scikit-learn/pull/23023)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`feature_extraction.FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
     now validates input parameters in `transform` instead of `__init__`. [#21573](https://github.com/scikit-learn/scikit-learn/pull/21573)
     by [Hannah Bohle](https://github.com/hhnnhh)
     and [Maren Westermann](https://github.com/marenwestermann)
    .
    
*   Fix [`feature_extraction.text.TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
     now does not create a [`feature_extraction.text.TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
     at `__init__` as required by our API. [#21832](https://github.com/scikit-learn/scikit-learn/pull/21832)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id11 "Link to this heading")

*   Feature Added auto mode to [`feature_selection.SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
    . If the argument `n_features_to_select` is `'auto'`, select features until the score improvement does not exceed the argument `tol`. The default value of `n_features_to_select` changed from `None` to `'warn'` in 1.1 and will become `'auto'` in 1.3. `None` and `'warn'` will be removed in 1.3. [#20145](https://github.com/scikit-learn/scikit-learn/pull/20145)
     by [murata-yu](https://github.com/murata-yu)
    .
    
*   Feature Added the ability to pass callables to the `max_features` parameter of [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
    . Also introduced new attribute `max_features_` which is inferred from `max_features` and the data during `fit`. If `max_features` is an integer, then `max_features_ = max_features`. If `max_features` is a callable, then `max_features_ = max_features(X)`. [#22356](https://github.com/scikit-learn/scikit-learn/pull/22356)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Enhancement [`feature_selection.GenericUnivariateSelect`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect "sklearn.feature_selection.GenericUnivariateSelect")
     preserves float32 dtype. [#18482](https://github.com/scikit-learn/scikit-learn/pull/18482)
     by [Thierry Gameiro](https://github.com/titigmr)
     and [Daniel Kharsa](https://github.com/aflatoune)
     and [#22370](https://github.com/scikit-learn/scikit-learn/pull/22370)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Enhancement Add a parameter `force_finite` to [`feature_selection.f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")
     and [`feature_selection.r_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html#sklearn.feature_selection.r_regression "sklearn.feature_selection.r_regression")
    . This parameter allows to force the output to be finite in the case where a feature or the target is constant or that the feature and target are perfectly correlated (only for the F-statistic). [#17819](https://github.com/scikit-learn/scikit-learn/pull/17819)
     by [Juan Carlos Alfaro Jiménez](https://github.com/alfaro96)
    .
    
*   Efficiency Improve runtime performance of [`feature_selection.chi2`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2 "sklearn.feature_selection.chi2")
     with boolean arrays. [#22235](https://github.com/scikit-learn/scikit-learn/pull/22235)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Efficiency Reduced memory usage of [`feature_selection.chi2`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2 "sklearn.feature_selection.chi2")
    . [#21837](https://github.com/scikit-learn/scikit-learn/pull/21837)
     by [Louis Wagner](https://github.com/lrwagner)
    .
    

#### [`sklearn.gaussian_process`](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#module-sklearn.gaussian_process "sklearn.gaussian_process")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-gaussian-process "Link to this heading")

*   Fix `predict` and `sample_y` methods of [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
     now return arrays of the correct shape in single-target and multi-target cases, and for both `normalize_y=False` and `normalize_y=True`. [#22199](https://github.com/scikit-learn/scikit-learn/pull/22199)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    , [Aidar Shakerimoff](https://github.com/AidarShakerimoff)
     and [Tenavi Nakamura-Zimmerer](https://github.com/Tenavi)
    .
    
*   Fix [`gaussian_process.GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
     raises a more informative error if `CompoundKernel` is passed via `kernel`. [#22223](https://github.com/scikit-learn/scikit-learn/pull/22223)
     by [MarcoM](https://github.com/marcozzxx810)
    .
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id12 "Link to this heading")

*   Enhancement [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     now warns with feature names when features which are skipped due to the lack of any observed values in the training set. [#21617](https://github.com/scikit-learn/scikit-learn/pull/21617)
     by [Christian Ritter](https://github.com/chritter)
    .
    
*   Enhancement Added support for `pd.NA` in [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
    . [#21114](https://github.com/scikit-learn/scikit-learn/pull/21114)
     by [Ying Xiong](https://github.com/yxiong)
    .
    
*   Enhancement Adds [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     to [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
    , [`impute.KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
    , [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
    , and [`impute.MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")
    . [#21078](https://github.com/scikit-learn/scikit-learn/pull/21078)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change The `verbose` parameter was deprecated for [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
    . A warning will always be raised upon the removal of empty columns. [#21448](https://github.com/scikit-learn/scikit-learn/pull/21448)
     by [Oleh Kozynets](https://github.com/OlehKSS)
     and [Christian Ritter](https://github.com/chritter)
    .
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-inspection "Link to this heading")

*   Feature Add a display to plot the boundary decision of a classifier by using the method [`inspection.DecisionBoundaryDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
    . [#16061](https://github.com/scikit-learn/scikit-learn/pull/16061)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement In [`inspection.PartialDependenceDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
    , allow `kind` to accept a list of strings to specify which type of plot to draw for each feature interaction. [#19438](https://github.com/scikit-learn/scikit-learn/pull/19438)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Enhancement [`inspection.PartialDependenceDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
    , [`inspection.PartialDependenceDisplay.plot`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.plot "sklearn.inspection.PartialDependenceDisplay.plot")
    , and `inspection.plot_partial_dependence` now support plotting centered Individual Conditional Expectation (cICE) and centered PDP curves controlled by setting the parameter `centered`. [#18310](https://github.com/scikit-learn/scikit-learn/pull/18310)
     by [Johannes Elfner](https://github.com/JoElfner)
     and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.isotonic`](https://scikit-learn.org/stable/api/sklearn.isotonic.html#module-sklearn.isotonic "sklearn.isotonic")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-isotonic "Link to this heading")

*   Enhancement Adds [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     to [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
    . [#22249](https://github.com/scikit-learn/scikit-learn/pull/22249)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.kernel_approximation`](https://scikit-learn.org/stable/api/sklearn.kernel_approximation.html#module-sklearn.kernel_approximation "sklearn.kernel_approximation")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-kernel-approximation "Link to this heading")

*   Enhancement Adds [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     to [`kernel_approximation.AdditiveChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.AdditiveChi2Sampler.html#sklearn.kernel_approximation.AdditiveChi2Sampler "sklearn.kernel_approximation.AdditiveChi2Sampler")
    . [`kernel_approximation.Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
    , [`kernel_approximation.PolynomialCountSketch`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch "sklearn.kernel_approximation.PolynomialCountSketch")
    , [`kernel_approximation.RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
    , and [`kernel_approximation.SkewedChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.SkewedChi2Sampler.html#sklearn.kernel_approximation.SkewedChi2Sampler "sklearn.kernel_approximation.SkewedChi2Sampler")
    . [#22137](https://github.com/scikit-learn/scikit-learn/pull/22137)
     and [#22694](https://github.com/scikit-learn/scikit-learn/pull/22694)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id13 "Link to this heading")

*   Feature [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
    , [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    , [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     and [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
     support `sample_weight` for sparse input `X`. [#22808](https://github.com/scikit-learn/scikit-learn/pull/22808)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Feature [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     with `solver="lsqr"` now supports to fit sparse input with `fit_intercept=True`. [#22950](https://github.com/scikit-learn/scikit-learn/pull/22950)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Enhancement [`linear_model.QuantileRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
     support sparse input for the highs based solvers. [#21086](https://github.com/scikit-learn/scikit-learn/pull/21086)
     by [Venkatachalam Natchiappan](https://github.com/venkyyuvy)
    . In addition, those solvers now use the CSC matrix right from the beginning which speeds up fitting. [#22206](https://github.com/scikit-learn/scikit-learn/pull/22206)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Enhancement [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     is faster for `solvers="lbfgs"` and `solver="newton-cg"`, for binary and in particular for multiclass problems thanks to the new private loss function module. In the multiclass case, the memory consumption has also been reduced for these solvers as the target is now label encoded (mapped to integers) instead of label binarized (one-hot encoded). The more classes, the larger the benefit. [#21808](https://github.com/scikit-learn/scikit-learn/pull/21808)
    , [#20567](https://github.com/scikit-learn/scikit-learn/pull/20567)
     and [#21814](https://github.com/scikit-learn/scikit-learn/pull/21814)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Enhancement [`linear_model.GammaRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html#sklearn.linear_model.GammaRegressor "sklearn.linear_model.GammaRegressor")
    , [`linear_model.PoissonRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")
     and [`linear_model.TweedieRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html#sklearn.linear_model.TweedieRegressor "sklearn.linear_model.TweedieRegressor")
     are faster for `solvers="lbfgs"`. [#22548](https://github.com/scikit-learn/scikit-learn/pull/22548)
    , [#21808](https://github.com/scikit-learn/scikit-learn/pull/21808)
     and [#20567](https://github.com/scikit-learn/scikit-learn/pull/20567)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Enhancement Rename parameter `base_estimator` to `estimator` in [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
     to improve readability and consistency. `base_estimator` is deprecated and will be removed in 1.3. [#22062](https://github.com/scikit-learn/scikit-learn/pull/22062)
     by [Adrian Trujillo](https://github.com/trujillo9616)
    .
    
*   Enhancement [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     and other linear model classes using coordinate descent show error messages when non-finite parameter weights are produced. [#22148](https://github.com/scikit-learn/scikit-learn/pull/22148)
     by [Christian Ritter](https://github.com/chritter)
     and [Norbert Preining](https://github.com/norbusan)
    .
    
*   Enhancement [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     and [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     now raise consistent error messages when passed invalid values for `l1_ratio`, `alpha`, `max_iter` and `tol`. [#22240](https://github.com/scikit-learn/scikit-learn/pull/22240)
     by [Arturo Amor](https://github.com/ArturoAmorQ)
    .
    
*   Enhancement [`linear_model.BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
     and [`linear_model.ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
     now preserve float32 dtype. [#9087](https://github.com/scikit-learn/scikit-learn/pull/9087)
     by [Arthur Imbert](https://github.com/Henley13)
     and [#22525](https://github.com/scikit-learn/scikit-learn/pull/22525)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Enhancement [`linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
     is now supporting multilabel classification. [#19689](https://github.com/scikit-learn/scikit-learn/pull/19689)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Enhancement [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     and [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
     now raise consistent error message when passed invalid values for `alphas`. [#21606](https://github.com/scikit-learn/scikit-learn/pull/21606)
     by [Arturo Amor](https://github.com/ArturoAmorQ)
    .
    
*   Enhancement [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     and [`linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
     now raise consistent error message when passed invalid values for `alpha`, `max_iter` and `tol`. [#21341](https://github.com/scikit-learn/scikit-learn/pull/21341)
     by [Arturo Amor](https://github.com/ArturoAmorQ)
    .
    
*   Enhancement [`linear_model.orthogonal_mp_gram`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html#sklearn.linear_model.orthogonal_mp_gram "sklearn.linear_model.orthogonal_mp_gram")
     preserves dtype for `numpy.float32`. [#22002](https://github.com/scikit-learn/scikit-learn/pull/22002)
     by [Takeshi Oura](https://github.com/takoika)
    .
    
*   Fix [`linear_model.LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
     now correctly computes AIC and BIC. An error is now raised when `n_features > n_samples` and when the noise variance is not provided. [#21481](https://github.com/scikit-learn/scikit-learn/pull/21481)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
     and [Andrés Babino](https://github.com/ababino)
    .
    
*   Fix [`linear_model.TheilSenRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "sklearn.linear_model.TheilSenRegressor")
     now validates input parameter `max_subpopulation` in `fit` instead of `__init__`. [#21767](https://github.com/scikit-learn/scikit-learn/pull/21767)
     by [Maren Westermann](https://github.com/marenwestermann)
    .
    
*   Fix [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
     now produces correct warning when `l1_ratio=0`. [#21724](https://github.com/scikit-learn/scikit-learn/pull/21724)
     by [Yar Khine Phyo](https://github.com/yarkhinephyo)
    .
    
*   Fix [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     now set the `n_iter_` attribute with a shape that respects the docstring and that is consistent with the shape obtained when using the other solvers in the one-vs-rest setting. Previously, it would record only the maximum of the number of iterations for each binary sub-problem while now all of them are recorded. [#21998](https://github.com/scikit-learn/scikit-learn/pull/21998)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Fix The property `family` of [`linear_model.TweedieRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html#sklearn.linear_model.TweedieRegressor "sklearn.linear_model.TweedieRegressor")
     is not validated in `__init__` anymore. Instead, this (private) property is deprecated in [`linear_model.GammaRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html#sklearn.linear_model.GammaRegressor "sklearn.linear_model.GammaRegressor")
    , [`linear_model.PoissonRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")
     and [`linear_model.TweedieRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html#sklearn.linear_model.TweedieRegressor "sklearn.linear_model.TweedieRegressor")
    , and will be removed in 1.3. [#22548](https://github.com/scikit-learn/scikit-learn/pull/22548)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Fix The `coef_` and `intercept_` attributes of [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
     are now correctly computed in the presence of sample weights when the input is sparse. [#22891](https://github.com/scikit-learn/scikit-learn/pull/22891)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix The `coef_` and `intercept_` attributes of [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     with `solver="sparse_cg"` and `solver="lbfgs"` are now correctly computed in the presence of sample weights when the input is sparse. [#22899](https://github.com/scikit-learn/scikit-learn/pull/22899)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     and [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     now compute the validation error correctly when early stopping is enabled. [#23256](https://github.com/scikit-learn/scikit-learn/pull/23256)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
    .
    
*   API Change [`linear_model.LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
     now exposes `noise_variance` as a parameter in order to provide an estimate of the noise variance. This is particularly relevant when `n_features > n_samples` and the estimator of the noise variance cannot be computed. [#21481](https://github.com/scikit-learn/scikit-learn/pull/21481)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id14 "Link to this heading")

*   Feature [`manifold.Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
     now supports radius-based neighbors via the `radius` argument. [#19794](https://github.com/scikit-learn/scikit-learn/pull/19794)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
    .
    
*   Enhancement [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
     and [`manifold.SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
     support `np.float32` dtype and will preserve this dtype. [#21534](https://github.com/scikit-learn/scikit-learn/pull/21534)
     by [Andrew Knyazev](https://github.com/lobpcg)
    .
    
*   Enhancement Adds [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     to [`manifold.Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
     and [`manifold.LocallyLinearEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
    . [#22254](https://github.com/scikit-learn/scikit-learn/pull/22254)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement added `metric_params` to [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     constructor for additional parameters of distance metric to use in optimization. [#21805](https://github.com/scikit-learn/scikit-learn/pull/21805)
     by [Jeanne Dionisi](https://github.com/jeannedionisi)
     and [#22685](https://github.com/scikit-learn/scikit-learn/pull/22685)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Enhancement [`manifold.trustworthiness`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.trustworthiness.html#sklearn.manifold.trustworthiness "sklearn.manifold.trustworthiness")
     raises an error if `n_neighbours >= n_samples / 2` to ensure a correct support for the function. [#18832](https://github.com/scikit-learn/scikit-learn/pull/18832)
     by [Hong Shao Yang](https://github.com/hongshaoyang)
     and [#23033](https://github.com/scikit-learn/scikit-learn/pull/23033)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Fix [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
     now uses Gaussian instead of the previous uniform on \[0, 1\] random initial approximations to eigenvectors in eigen\_solvers `lobpcg` and `amg` to improve their numerical stability. [#21565](https://github.com/scikit-learn/scikit-learn/pull/21565)
     by [Andrew Knyazev](https://github.com/lobpcg)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id15 "Link to this heading")

*   Feature [`metrics.r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
     and [`metrics.explained_variance_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score "sklearn.metrics.explained_variance_score")
     have a new `force_finite` parameter. Setting this parameter to `False` will return the actual non-finite score in case of perfect predictions or constant `y_true`, instead of the finite approximation (`1.0` and `0.0` respectively) currently returned by default. [#17266](https://github.com/scikit-learn/scikit-learn/pull/17266)
     by [Sylvain Marié](https://github.com/smarie)
    .
    
*   Feature [`metrics.d2_pinball_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_pinball_score.html#sklearn.metrics.d2_pinball_score "sklearn.metrics.d2_pinball_score")
     and [`metrics.d2_absolute_error_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_absolute_error_score.html#sklearn.metrics.d2_absolute_error_score "sklearn.metrics.d2_absolute_error_score")
     calculate the D2 regression score for the pinball loss and the absolute error respectively. [`metrics.d2_absolute_error_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_absolute_error_score.html#sklearn.metrics.d2_absolute_error_score "sklearn.metrics.d2_absolute_error_score")
     is a special case of [`metrics.d2_pinball_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_pinball_score.html#sklearn.metrics.d2_pinball_score "sklearn.metrics.d2_pinball_score")
     with a fixed quantile parameter `alpha=0.5` for ease of use and discovery. The D2 scores are generalizations of the `r2_score` and can be interpreted as the fraction of deviance explained. [#22118](https://github.com/scikit-learn/scikit-learn/pull/22118)
     by [Ohad Michel](https://github.com/ohadmich)
    .
    
*   Enhancement [`metrics.top_k_accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html#sklearn.metrics.top_k_accuracy_score "sklearn.metrics.top_k_accuracy_score")
     raises an improved error message when `y_true` is binary and `y_score` is 2d. [#22284](https://github.com/scikit-learn/scikit-learn/pull/22284)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`metrics.roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
     now supports `average=None` in the multiclass case when `multiclass='ovr'` which will return the score per class. [#19158](https://github.com/scikit-learn/scikit-learn/pull/19158)
     by [Nicki Skafte](https://github.com/SkafteNicki)
    .
    
*   Enhancement Adds `im_kw` parameter to [`metrics.ConfusionMatrixDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_estimator "sklearn.metrics.ConfusionMatrixDisplay.from_estimator")
     [`metrics.ConfusionMatrixDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_predictions "sklearn.metrics.ConfusionMatrixDisplay.from_predictions")
    , and [`metrics.ConfusionMatrixDisplay.plot`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.plot "sklearn.metrics.ConfusionMatrixDisplay.plot")
    . The `im_kw` parameter is passed to the `matplotlib.pyplot.imshow` call when plotting the confusion matrix. [#20753](https://github.com/scikit-learn/scikit-learn/pull/20753)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`metrics.silhouette_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")
     now supports integer input for precomputed distances. [#22108](https://github.com/scikit-learn/scikit-learn/pull/22108)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Fixed a bug in [`metrics.normalized_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#sklearn.metrics.normalized_mutual_info_score "sklearn.metrics.normalized_mutual_info_score")
     which could return unbounded values. [#22635](https://github.com/scikit-learn/scikit-learn/pull/22635)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix Fixes [`metrics.precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")
     and [`metrics.average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
     when true labels are all negative. [#19085](https://github.com/scikit-learn/scikit-learn/pull/19085)
     by [Varun Agrawal](https://github.com/varunagrawal)
    .
    
*   API Change `metrics.SCORERS` is now deprecated and will be removed in 1.3. Please use [`metrics.get_scorer_names`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer_names.html#sklearn.metrics.get_scorer_names "sklearn.metrics.get_scorer_names")
     to retrieve the names of all available scorers. [#22866](https://github.com/scikit-learn/scikit-learn/pull/22866)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   API Change Parameters `sample_weight` and `multioutput` of [`metrics.mean_absolute_percentage_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html#sklearn.metrics.mean_absolute_percentage_error "sklearn.metrics.mean_absolute_percentage_error")
     are now keyword-only, in accordance with [SLEP009](https://scikit-learn-enhancement-proposals.readthedocs.io/en/latest/slep009/proposal.html)
    . A deprecation cycle was introduced. [#21576](https://github.com/scikit-learn/scikit-learn/pull/21576)
     by [Paul-Emile Dugnat](https://github.com/pedugnat)
    .
    
*   API Change The `"wminkowski"` metric of [`metrics.DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "sklearn.metrics.DistanceMetric")
     is deprecated and will be removed in version 1.3. Instead the existing `"minkowski"` metric now takes in an optional `w` parameter for weights. This deprecation aims at remaining consistent with SciPy 1.8 convention. [#21873](https://github.com/scikit-learn/scikit-learn/pull/21873)
     by [Yar Khine Phyo](https://github.com/yarkhinephyo)
    .
    
*   API Change [`metrics.DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "sklearn.metrics.DistanceMetric")
     has been moved from [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
     to [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
    . Using `neighbors.DistanceMetric` for imports is still valid for backward compatibility, but this alias will be removed in 1.3. [#21177](https://github.com/scikit-learn/scikit-learn/pull/21177)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    

#### [`sklearn.mixture`](https://scikit-learn.org/stable/api/sklearn.mixture.html#module-sklearn.mixture "sklearn.mixture")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-mixture "Link to this heading")

*   Enhancement [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     and [`mixture.BayesianGaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")
     can now be initialized using k-means++ and random data points. [#20408](https://github.com/scikit-learn/scikit-learn/pull/20408)
     by [Gordon Walsh](https://github.com/g-walsh)
    , [Alberto Ceballos](https://github.com/alceballosa)
     and [Andres Rios](https://github.com/ariosramirez)
    .
    
*   Fix Fix a bug that correctly initializes `precisions_cholesky_` in [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     when providing `precisions_init` by taking its square root. [#22058](https://github.com/scikit-learn/scikit-learn/pull/22058)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     now normalizes `weights_` more safely, preventing rounding errors when calling [`mixture.GaussianMixture.sample`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture.sample "sklearn.mixture.GaussianMixture.sample")
     with `n_components=1`. [#23034](https://github.com/scikit-learn/scikit-learn/pull/23034)
     by [Meekail Zain](https://github.com/micky774)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-model-selection "Link to this heading")

*   Enhancement it is now possible to pass `scoring="matthews_corrcoef"` to all model selection tools with a `scoring` argument to use the Matthews correlation coefficient (MCC). [#22203](https://github.com/scikit-learn/scikit-learn/pull/22203)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Enhancement raise an error during cross-validation when the fits for all the splits failed. Similarly raise an error during grid-search when the fits for all the models and all the splits failed. [#21026](https://github.com/scikit-learn/scikit-learn/pull/21026)
     by [Loïc Estève](https://github.com/lesteve)
    .
    
*   Fix [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    , [`model_selection.HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
     now validates input parameters in `fit` instead of `__init__`. [#21880](https://github.com/scikit-learn/scikit-learn/pull/21880)
     by [Mrinal Tyagi](https://github.com/MrinalTyagi)
    .
    
*   Fix [`model_selection.learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
     now supports `partial_fit` with regressors. [#22982](https://github.com/scikit-learn/scikit-learn/pull/22982)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.multiclass`](https://scikit-learn.org/stable/api/sklearn.multiclass.html#module-sklearn.multiclass "sklearn.multiclass")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-multiclass "Link to this heading")

*   Enhancement [`multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
     now supports a `verbose` parameter so progress on fitting can be seen. [#22508](https://github.com/scikit-learn/scikit-learn/pull/22508)
     by [Chris Combs](https://github.com/combscCode)
    .
    
*   Fix [`multiclass.OneVsOneClassifier.predict`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier.predict "sklearn.multiclass.OneVsOneClassifier.predict")
     returns correct predictions when the inner classifier only has a [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
    . [#22604](https://github.com/scikit-learn/scikit-learn/pull/22604)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-neighbors "Link to this heading")

*   Enhancement Adds [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     to [`neighbors.RadiusNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer "sklearn.neighbors.RadiusNeighborsTransformer")
    , [`neighbors.KNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
     and [`neighbors.NeighborhoodComponentsAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis")
    . [#22212](https://github.com/scikit-learn/scikit-learn/pull/22212)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Fix [`neighbors.KernelDensity`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
     now validates input parameters in `fit` instead of `__init__`. [#21430](https://github.com/scikit-learn/scikit-learn/pull/21430)
     by [Desislava Vasileva](https://github.com/DessyVV)
     and [Lucy Jimenez](https://github.com/LucyJimenez)
    .
    
*   Fix [`neighbors.KNeighborsRegressor.predict`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor.predict "sklearn.neighbors.KNeighborsRegressor.predict")
     now works properly when given an array-like input if `KNeighborsRegressor` is first constructed with a callable passed to the `weights` parameter. [#22687](https://github.com/scikit-learn/scikit-learn/pull/22687)
     by [Meekail Zain](https://github.com/micky774)
    .
    

#### [`sklearn.neural_network`](https://scikit-learn.org/stable/api/sklearn.neural_network.html#module-sklearn.neural_network "sklearn.neural_network")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-neural-network "Link to this heading")

*   Enhancement [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     and [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
     show error messages when optimizers produce non-finite parameter weights. [#22150](https://github.com/scikit-learn/scikit-learn/pull/22150)
     by [Christian Ritter](https://github.com/chritter)
     and [Norbert Preining](https://github.com/norbusan)
    .
    
*   Enhancement Adds [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     to [`neural_network.BernoulliRBM`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM "sklearn.neural_network.BernoulliRBM")
    . [#22248](https://github.com/scikit-learn/scikit-learn/pull/22248)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-pipeline "Link to this heading")

*   Enhancement Added support for “passthrough” in [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
    . Setting a transformer to “passthrough” will pass the features unchanged. [#20860](https://github.com/scikit-learn/scikit-learn/pull/20860)
     by [Shubhraneel Pal](https://github.com/shubhraneel)
    .
    
*   Fix [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     now does not validate hyper-parameters in `__init__` but in `.fit()`. [#21888](https://github.com/scikit-learn/scikit-learn/pull/21888)
     by [iofall](https://github.com/iofall)
     and [Arisa Y.](https://github.com/arisayosh)
    .
    
*   Fix [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     does not validate hyper-parameters in `__init__`. Validation is now handled in `.fit()` and `.fit_transform()`. [#21954](https://github.com/scikit-learn/scikit-learn/pull/21954)
     by [iofall](https://github.com/iofall)
     and [Arisa Y.](https://github.com/arisayosh)
    .
    
*   Fix Defines `__sklearn_is_fitted__` in [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     to return correct result with [`utils.validation.check_is_fitted`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
    . [#22953](https://github.com/scikit-learn/scikit-learn/pull/22953)
     by [randomgeek78](https://github.com/randomgeek78)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id16 "Link to this heading")

*   Feature [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     now supports grouping infrequent categories into a single feature. Grouping infrequent categories is enabled by specifying how to select infrequent categories with `min_frequency` or `max_categories`. [#16018](https://github.com/scikit-learn/scikit-learn/pull/16018)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement Adds a `subsample` parameter to [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
    . This allows specifying a maximum number of samples to be used while fitting the model. The option is only available when `strategy` is set to `quantile`. [#21445](https://github.com/scikit-learn/scikit-learn/pull/21445)
     by [Felipe Bidu](https://github.com/fbidu)
     and [Amanda Dsouza](https://github.com/amy12xx)
    .
    
*   Enhancement Adds `encoded_missing_value` to [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     to configure the encoded value for missing data. [#21988](https://github.com/scikit-learn/scikit-learn/pull/21988)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement Added the `get_feature_names_out` method and a new parameter `feature_names_out` to [`preprocessing.FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
    . You can set `feature_names_out` to ‘one-to-one’ to use the input features names as the output feature names, or you can set it to a callable that returns the output feature names. This is especially useful when the transformer changes the number of features. If `feature_names_out` is None (which is the default), then `get_output_feature_names` is not defined. [#21569](https://github.com/scikit-learn/scikit-learn/pull/21569)
     by [Aurélien Geron](https://github.com/ageron)
    .
    
*   Enhancement Adds [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     to [`preprocessing.Normalizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer")
    , [`preprocessing.KernelCenterer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KernelCenterer.html#sklearn.preprocessing.KernelCenterer "sklearn.preprocessing.KernelCenterer")
    , [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
    , and [`preprocessing.Binarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Binarizer.html#sklearn.preprocessing.Binarizer "sklearn.preprocessing.Binarizer")
    . [#21079](https://github.com/scikit-learn/scikit-learn/pull/21079)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`preprocessing.PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
     with `method='yeo-johnson'` better supports significantly non-Gaussian data when searching for an optimal lambda. [#20653](https://github.com/scikit-learn/scikit-learn/pull/20653)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`preprocessing.LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
     now validates input parameters in `fit` instead of `__init__`. [#21434](https://github.com/scikit-learn/scikit-learn/pull/21434)
     by [Krum Arnaudov](https://github.com/krumeto)
    .
    
*   Fix [`preprocessing.FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
     with `check_inverse=True` now provides informative error message when input has mixed dtypes. [#19916](https://github.com/scikit-learn/scikit-learn/pull/19916)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
    .
    
*   Fix [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
     handles bin edges more consistently now. [#14975](https://github.com/scikit-learn/scikit-learn/pull/14975)
     by [Andreas Müller](https://amueller.github.io/)
     and [#22526](https://github.com/scikit-learn/scikit-learn/pull/22526)
     by [Meekail Zain](https://github.com/micky774)
    .
    
*   Fix Adds [`preprocessing.KBinsDiscretizer.get_feature_names_out`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer.get_feature_names_out "sklearn.preprocessing.KBinsDiscretizer.get_feature_names_out")
     support when `encode="ordinal"`. [#22735](https://github.com/scikit-learn/scikit-learn/pull/22735)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.random_projection`](https://scikit-learn.org/stable/api/sklearn.random_projection.html#module-sklearn.random_projection "sklearn.random_projection")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-random-projection "Link to this heading")

*   Enhancement Adds an `inverse_transform` method and a `compute_inverse_transform` parameter to [`random_projection.GaussianRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection "sklearn.random_projection.GaussianRandomProjection")
     and [`random_projection.SparseRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection")
    . When the parameter is set to True, the pseudo-inverse of the components is computed during `fit` and stored as `inverse_components_`. [#21701](https://github.com/scikit-learn/scikit-learn/pull/21701)
     by [Aurélien Geron](https://github.com/ageron)
    .
    
*   Enhancement [`random_projection.SparseRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection")
     and [`random_projection.GaussianRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection "sklearn.random_projection.GaussianRandomProjection")
     preserve dtype for `numpy.float32`. [#22114](https://github.com/scikit-learn/scikit-learn/pull/22114)
     by [Takeshi Oura](https://github.com/takoika)
    .
    
*   Enhancement Adds [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     to all transformers in the [`sklearn.random_projection`](https://scikit-learn.org/stable/api/sklearn.random_projection.html#module-sklearn.random_projection "sklearn.random_projection")
     module: [`random_projection.GaussianRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection "sklearn.random_projection.GaussianRandomProjection")
     and [`random_projection.SparseRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection")
    . [#21330](https://github.com/scikit-learn/scikit-learn/pull/21330)
     by [Loïc Estève](https://github.com/lesteve)
    .
    

#### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#sklearn-svm "Link to this heading")

*   Enhancement [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
    , [`svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
    , [`svm.NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
    , [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     and [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
     now expose `n_iter_`, the number of iterations of the libsvm optimization routine. [#21408](https://github.com/scikit-learn/scikit-learn/pull/21408)
     by [Juan Martín Loyola](https://github.com/jmloyola)
    .
    
*   Enhancement [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
    , [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
    , [`svm.NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
    , [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
    , [`svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
     now raise an error when the dual-gap estimation produces non-finite parameter weights. [#22149](https://github.com/scikit-learn/scikit-learn/pull/22149)
     by [Christian Ritter](https://github.com/chritter)
     and [Norbert Preining](https://github.com/norbusan)
    .
    
*   Fix [`svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
    , [`svm.NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
    , [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
    , [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
    , [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
     now validate input parameters in `fit` instead of `__init__`. [#21436](https://github.com/scikit-learn/scikit-learn/pull/21436)
     by [Haidar Almubarak](https://github.com/Haidar13)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id17 "Link to this heading")

*   Enhancement [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
     and [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
     have the new `criterion="log_loss"`, which is equivalent to `criterion="entropy"`. [#23047](https://github.com/scikit-learn/scikit-learn/pull/23047)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Fix Fix a bug in the Poisson splitting criterion for [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    . [#22191](https://github.com/scikit-learn/scikit-learn/pull/22191)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   API Change Changed the default value of `max_features` to 1.0 for [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
     and to `"sqrt"` for [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
    , which will not change the fit result. The original default value `"auto"` has been deprecated and will be removed in version 1.3. Setting `max_features` to `"auto"` is also deprecated for [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
     and [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    . [#22476](https://github.com/scikit-learn/scikit-learn/pull/22476)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.1.html#id18 "Link to this heading")

*   Enhancement [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     and [`utils.multiclass.type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
     now accept an `input_name` parameter to make the error message more informative when passed invalid input data (e.g. with NaN or infinite values). [#21219](https://github.com/scikit-learn/scikit-learn/pull/21219)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Enhancement [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     returns a float ndarray with `np.nan` when passed a `Float32` or `Float64` pandas extension array with `pd.NA`. [#21278](https://github.com/scikit-learn/scikit-learn/pull/21278)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`utils.estimator_html_repr`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_html_repr.html#sklearn.utils.estimator_html_repr "sklearn.utils.estimator_html_repr")
     shows a more helpful error message when running in a jupyter notebook that is not trusted. [#21316](https://github.com/scikit-learn/scikit-learn/pull/21316)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`utils.estimator_html_repr`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_html_repr.html#sklearn.utils.estimator_html_repr "sklearn.utils.estimator_html_repr")
     displays an arrow on the top left corner of the HTML representation to show how the elements are clickable. [#21298](https://github.com/scikit-learn/scikit-learn/pull/21298)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     with `dtype=None` returns numeric arrays when passed in a pandas DataFrame with mixed dtypes. `dtype="numeric"` will also make better infer the dtype when the DataFrame has mixed dtypes. [#22237](https://github.com/scikit-learn/scikit-learn/pull/22237)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`utils.check_scalar`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_scalar.html#sklearn.utils.check_scalar "sklearn.utils.check_scalar")
     now has better messages when displaying the type. [#22218](https://github.com/scikit-learn/scikit-learn/pull/22218)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Changes the error message of the `ValidationError` raised by [`utils.check_X_y`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html#sklearn.utils.check_X_y "sklearn.utils.check_X_y")
     when y is None so that it is compatible with the `check_requires_y_none` estimator check. [#22578](https://github.com/scikit-learn/scikit-learn/pull/22578)
     by [Claudio Salvatore Arcidiacono](https://github.com/ClaudioSalvatoreArcidiacono)
    .
    
*   Fix [`utils.class_weight.compute_class_weight`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html#sklearn.utils.class_weight.compute_class_weight "sklearn.utils.class_weight.compute_class_weight")
     now only requires that all classes in `y` have a weight in `class_weight`. An error is still raised when a class is present in `y` but not in `class_weight`. [#22595](https://github.com/scikit-learn/scikit-learn/pull/22595)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`utils.estimator_html_repr`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_html_repr.html#sklearn.utils.estimator_html_repr "sklearn.utils.estimator_html_repr")
     has an improved visualization for nested meta-estimators. [#21310](https://github.com/scikit-learn/scikit-learn/pull/21310)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`utils.check_scalar`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_scalar.html#sklearn.utils.check_scalar "sklearn.utils.check_scalar")
     raises an error when `include_boundaries={"left", "right"}` and the boundaries are not set. [#22027](https://github.com/scikit-learn/scikit-learn/pull/22027)
     by [Marie Lanternier](https://github.com/mlant)
    .
    
*   Fix [`utils.metaestimators.available_if`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metaestimators.available_if.html#sklearn.utils.metaestimators.available_if "sklearn.utils.metaestimators.available_if")
     correctly returns a bounded method that can be pickled. [#23077](https://github.com/scikit-learn/scikit-learn/pull/23077)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
    ’s argument is now called `estimator` (previous name was `Estimator`). [#22188](https://github.com/scikit-learn/scikit-learn/pull/22188)
     by [Mathurin Massias](https://github.com/mathurinm)
    .
    
*   API Change `utils.metaestimators.if_delegate_has_method` is deprecated and will be removed in version 1.3. Use [`utils.metaestimators.available_if`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metaestimators.available_if.html#sklearn.utils.metaestimators.available_if "sklearn.utils.metaestimators.available_if")
     instead. [#22830](https://github.com/scikit-learn/scikit-learn/pull/22830)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

Code and documentation contributors

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 1.0, including:

2357juan, Abhishek Gupta, adamgonzo, Adam Li, adijohar, Aditya Kumawat, Aditya Raghuwanshi, Aditya Singh, Adrian Trujillo Duron, Adrin Jalali, ahmadjubair33, AJ Druck, aj-white, Alan Peixinho, Alberto Mario Ceballos-Arroyo, Alek Lefebvre, Alex, Alexandr, Alexandre Gramfort, alexanmv, almeidayoel, Amanda Dsouza, Aman Sharma, Amar pratap singh, Amit, amrcode, András Simon, Andreas Grivas, Andreas Mueller, Andrew Knyazev, Andriy, Angus L’Herrou, Ankit Sharma, Anne Ducout, Arisa, Arth, arthurmello, Arturo Amor, ArturoAmor, Atharva Patil, aufarkari, Aurélien Geron, avm19, Ayan Bag, baam, Bardiya Ak, Behrouz B, Ben3940, Benjamin Bossan, Bharat Raghunathan, Bijil Subhash, bmreiniger, Brandon Truth, Brenden Kadota, Brian Sun, cdrig, Chalmer Lowe, Chiara Marmo, Chitteti Srinath Reddy, Chloe-Agathe Azencott, Christian Lorentzen, Christian Ritter, christopherlim98, Christoph T. Weidemann, Christos Aridas, Claudio Salvatore Arcidiacono, combscCode, Daniela Fernandes, darioka, Darren Nguyen, Dave Eargle, David Gilbertson, David Poznik, Dea María Léon, Dennis Osei, DessyVV, Dev514, Dimitri Papadopoulos Orfanos, Diwakar Gupta, Dr. Felix M. Riese, drskd, Emiko Sano, Emmanouil Gionanidis, EricEllwanger, Erich Schubert, Eric Larson, Eric Ndirangu, ErmolaevPA, Estefania Barreto-Ojeda, eyast, Fatima GASMI, Federico Luna, Felix Glushchenkov, fkaren27, Fortune Uwha, FPGAwesome, francoisgoupil, Frans Larsson, ftorres16, Gabor Berei, Gabor Kertesz, Gabriel Stefanini Vicente, Gabriel S Vicente, Gael Varoquaux, GAURAV CHOUDHARY, Gauthier I, genvalen, Geoffrey-Paris, Giancarlo Pablo, glennfrutiz, gpapadok, Guillaume Lemaitre, Guillermo Tomás Fernández Martín, Gustavo Oliveira, Haidar Almubarak, Hannah Bohle, Hansin Ahuja, Haoyin Xu, Haya, Helder Geovane Gomes de Lima, henrymooresc, Hideaki Imamura, Himanshu Kumar, Hind-M, hmasdev, hvassard, i-aki-y, iasoon, Inclusive Coding Bot, Ingela, iofall, Ishan Kumar, Jack Liu, Jake Cowton, jalexand3r, J Alexander, Jauhar, Jaya Surya Kommireddy, Jay Stanley, Jeff Hale, je-kr, JElfner, Jenny Vo, Jérémie du Boisberranger, Jihane, Jirka Borovec, Joel Nothman, Jon Haitz Legarreta Gorroño, Jordan Silke, Jorge Ciprián, Jorge Loayza, Joseph Chazalon, Joseph Schwartz-Messing, Jovan Stojanovic, JSchuerz, Juan Carlos Alfaro Jiménez, Juan Martin Loyola, Julien Jerphanion, katotten, Kaushik Roy Chowdhury, Ken4git, Kenneth Prabakaran, kernc, Kevin Doucet, KimAYoung, Koushik Joshi, Kranthi Sedamaki, krishna kumar, krumetoft, lesnee, Lisa Casino, Logan Thomas, Loic Esteve, Louis Wagner, LucieClair, Lucy Liu, Luiz Eduardo Amaral, Magali, MaggieChege, Mai, mandjevant, Mandy Gu, Manimaran, MarcoM, Marco Wurps, Maren Westermann, Maria Boerner, MarieS-WiMLDS, Martel Corentin, martin-kokos, mathurinm, Matías, matjansen, Matteo Francia, Maxwell, Meekail Zain, Megabyte, Mehrdad Moradizadeh, melemo2, Michael I Chen, michalkrawczyk, Micky774, milana2, millawell, Ming-Yang Ho, Mitzi, miwojc, Mizuki, mlant, Mohamed Haseeb, Mohit Sharma, Moonkyung94, mpoemsl, MrinalTyagi, Mr. Leu, msabatier, murata-yu, N, Nadirhan Şahin, Naipawat Poolsawat, NartayXD, nastegiano, nathansquan, nat-salt, Nicki Skafte Detlefsen, Nicolas Hug, Niket Jain, Nikhil Suresh, Nikita Titov, Nikolay Kondratyev, Ohad Michel, Oleksandr Husak, Olivier Grisel, partev, Patrick Ferreira, Paul, pelennor, PierreAttard, Piet Brömmel, Pieter Gijsbers, Pinky, poloso, Pramod Anantharam, puhuk, Purna Chandra Mansingh, QuadV, Rahil Parikh, Randall Boyes, randomgeek78, Raz Hoshia, Reshama Shaikh, Ricardo Ferreira, Richard Taylor, Rileran, Rishabh, Robin Thibaut, Rocco Meli, Roman Feldbauer, Roman Yurchak, Ross Barnowski, rsnegrin, Sachin Yadav, sakinaOuisrani, Sam Adam Day, Sanjay Marreddi, Sebastian Pujalte, SEELE, SELEE, Seyedsaman (Sam) Emami, ShanDeng123, Shao Yang Hong, sharmadharmpal, shaymerNaturalint, Shuangchi He, Shubhraneel Pal, siavrez, slishak, Smile, spikebh, sply88, Srinath Kailasa, Stéphane Collot, Sultan Orazbayev, Sumit Saha, Sven Eschlbeck, Sven Stehle, Swapnil Jha, Sylvain Marié, Takeshi Oura, Tamires Santana, Tenavi, teunpe, Theis Ferré Hjortkjær, Thiruvenkadam, Thomas J. Fan, t-jakubek, toastedyeast, Tom Dupré la Tour, Tom McTiernan, TONY GEORGE, Tyler Martin, Tyler Reddy, Udit Gupta, Ugo Marchand, Varun Agrawal, Venkatachalam N, Vera Komeyer, victoirelouis, Vikas Vishwakarma, Vikrant khedkar, Vladimir Chernyy, Vladimir Kim, WeijiaDu, Xiao Yuan, Yar Khine Phyo, Ying Xiong, yiyangq, Yosshi999, Yuki Koyama, Zach Deane-Mayer, Zeel B Patel, zempleni, zhenfisher, 赵丰 (Zhao Feng)

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)