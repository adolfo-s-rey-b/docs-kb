[Skip to main content](https://scikit-learn.org/stable/whats_new/v1.0.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v1.0.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v1.0.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v1.0.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v1.0.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v1.0.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v1.0.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v1.0.html)

Collapse Sidebar Expand Sidebar

Version 1.0[#](https://scikit-learn.org/stable/whats_new/v1.0.html#version-1-0 "Link to this heading")

=======================================================================================================

For a short description of the main highlights of the release, please refer to [Release Highlights for scikit-learn 1.0](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html#sphx-glr-auto-examples-release-highlights-plot-release-highlights-1-0-0-py)
.

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 1.0.2[#](https://scikit-learn.org/stable/whats_new/v1.0.html#version-1-0-2 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**December 2021**

*   Fix [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
    , [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
    , and [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     do not raise warning when fitted on a pandas DataFrame anymore. [#21578](https://github.com/scikit-learn/scikit-learn/pull/21578)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.0.html#changelog "Link to this heading")

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-cluster "Link to this heading")

*   Fix Fixed an infinite loop in [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     by moving an iteration counter from try to except. [#21271](https://github.com/scikit-learn/scikit-learn/pull/21271)
     by [Tyler Martin](https://github.com/martintb)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-datasets "Link to this heading")

*   Fix [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     is now thread safe. Data is first downloaded to a temporary subfolder and then renamed. [#21833](https://github.com/scikit-learn/scikit-learn/pull/21833)
     by [Siavash Rezazadeh](https://github.com/siavrez)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-decomposition "Link to this heading")

*   Fix Fixed the constraint on the objective function of [`decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
    , [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
    , [`decomposition.SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")
     and [`decomposition.MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")
     to be convex and match the referenced article. [#19210](https://github.com/scikit-learn/scikit-learn/pull/19210)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-ensemble "Link to this heading")

*   Fix [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
    , [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
    , and [`ensemble.RandomTreesEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")
     now raise a `ValueError` when `bootstrap=False` and `max_samples` is not `None`. [#21295](https://github.com/scikit-learn/scikit-learn/pull/21295)
     [Haoyin Xu](https://github.com/PSSF23)
    .
    
*   Fix Solve a bug in [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     where the exponential loss was computing the positive gradient instead of the negative one. [#22050](https://github.com/scikit-learn/scikit-learn/pull/22050)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-feature-selection "Link to this heading")

*   Fix Fixed [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
     by improving support for base estimators that do not set `feature_names_in_`. [#21991](https://github.com/scikit-learn/scikit-learn/pull/21991)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-impute "Link to this heading")

*   Fix Fix a bug in [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
     where the method `predict` was performing an `argmax` on the scores obtained from `decision_function` instead of returning the multilabel indicator matrix. [#19869](https://github.com/scikit-learn/scikit-learn/pull/19869)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-linear-model "Link to this heading")

*   Fix [`linear_model.LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
     now correctly computes AIC and BIC. An error is now raised when `n_features > n_samples` and when the noise variance is not provided. [#21481](https://github.com/scikit-learn/scikit-learn/pull/21481)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
     and [Andrés Babino](https://github.com/ababino)
    .
    

#### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-manifold "Link to this heading")

*   Fix Fixed an unnecessary error when fitting [`manifold.Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
     with a precomputed dense distance matrix where the neighbors graph has multiple disconnected components. [#21915](https://github.com/scikit-learn/scikit-learn/pull/21915)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-metrics "Link to this heading")

*   Fix All [`sklearn.metrics.DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "sklearn.metrics.DistanceMetric")
     subclasses now correctly support read-only buffer attributes. This fixes a regression introduced in 1.0.0 with respect to 0.24.2. [#21694](https://github.com/scikit-learn/scikit-learn/pull/21694)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Fix All `sklearn.metrics.MinkowskiDistance` now accepts a weight parameter that makes it possible to write code that behaves consistently both with scipy 1.8 and earlier versions. In turn this means that all neighbors-based estimators (except those that use `algorithm="kd_tree"`) now accept a weight parameter with `metric="minkowski"` to yield results that are always consistent with `scipy.spatial.distance.cdist`. [#21741](https://github.com/scikit-learn/scikit-learn/pull/21741)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    

#### [`sklearn.multiclass`](https://scikit-learn.org/stable/api/sklearn.multiclass.html#module-sklearn.multiclass "sklearn.multiclass")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-multiclass "Link to this heading")

*   Fix [`multiclass.OneVsRestClassifier.predict_proba`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier.predict_proba "sklearn.multiclass.OneVsRestClassifier.predict_proba")
     does not error when fitted on constant integer targets. [#21871](https://github.com/scikit-learn/scikit-learn/pull/21871)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-neighbors "Link to this heading")

*   Fix [`neighbors.KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
     and [`neighbors.BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
     correctly support read-only buffer attributes. [#21845](https://github.com/scikit-learn/scikit-learn/pull/21845)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-preprocessing "Link to this heading")

*   Fix Fixes compatibility bug with NumPy 1.22 in [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
    . [#21517](https://github.com/scikit-learn/scikit-learn/pull/21517)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-tree "Link to this heading")

*   Fix Prevents [`tree.plot_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree")
     from drawing out of the boundary of the figure. [#21917](https://github.com/scikit-learn/scikit-learn/pull/21917)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Support loading pickles of decision tree models when the pickle has been generated on a platform with a different bitness. A typical example is to train and pickle the model on 64 bit machine and load the model on a 32 bit machine for prediction. [#21552](https://github.com/scikit-learn/scikit-learn/pull/21552)
     by [Loïc Estève](https://github.com/lesteve)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-utils "Link to this heading")

*   Fix [`utils.estimator_html_repr`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_html_repr.html#sklearn.utils.estimator_html_repr "sklearn.utils.estimator_html_repr")
     now escapes all the estimator descriptions in the generated HTML. [#21493](https://github.com/scikit-learn/scikit-learn/pull/21493)
     by [Aurélien Geron](https://github.com/ageron)
    .
    

Version 1.0.1[#](https://scikit-learn.org/stable/whats_new/v1.0.html#version-1-0-1 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**October 2021**

### Fixed models[#](https://scikit-learn.org/stable/whats_new/v1.0.html#fixed-models "Link to this heading")

*   Fix Non-fit methods in the following classes do not raise a UserWarning when fitted on DataFrames with valid feature names: [`covariance.EllipticEnvelope`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")
    , [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
    , [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
    , [`neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
    , [`neighbors.KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
    , [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
    , [`neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
    . [#21199](https://github.com/scikit-learn/scikit-learn/pull/21199)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-calibration "Link to this heading")

*   Fix Fixed [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     to take into account `sample_weight` when computing the base estimator prediction when `ensemble=False`. [#20638](https://github.com/scikit-learn/scikit-learn/pull/20638)
     by [Julien Bohné](https://github.com/JulienB-78)
    .
    
*   Fix Fixed a bug in [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     with `method="sigmoid"` that was ignoring the `sample_weight` when computing the Bayesian priors. [#21179](https://github.com/scikit-learn/scikit-learn/pull/21179)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id1 "Link to this heading")

*   Fix Fixed a bug in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    , ensuring reproducibility and equivalence between sparse and dense input. [#21195](https://github.com/scikit-learn/scikit-learn/pull/21195)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id2 "Link to this heading")

*   Fix Fixed a bug that could produce a segfault in rare cases for [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
    . [#21130](https://github.com/scikit-learn/scikit-learn/pull/21130)
     [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    

#### [`sklearn.gaussian_process`](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#module-sklearn.gaussian_process "sklearn.gaussian_process")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-gaussian-process "Link to this heading")

*   Fix Compute `y_std` properly with multi-target in [`sklearn.gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
     allowing proper normalization in multi-target scene. [#20761](https://github.com/scikit-learn/scikit-learn/pull/20761)
     by [Patrick de C. T. R. Ferreira](https://github.com/patrickctrf)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-feature-extraction "Link to this heading")

*   Efficiency Fixed an efficiency regression introduced in version 1.0.0 in the `transform` method of [`feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     which no longer checks for uppercase characters in the provided vocabulary. [#21251](https://github.com/scikit-learn/scikit-learn/pull/21251)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix Fixed a bug in [`feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     and [`feature_extraction.text.TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
     by raising an error when ‘min\_idf’ or ‘max\_idf’ are floating-point numbers greater than 1. [#20752](https://github.com/scikit-learn/scikit-learn/pull/20752)
     by [Alek Lefebvre](https://github.com/AlekLefebvre)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id3 "Link to this heading")

*   Fix Improves stability of [`linear_model.LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")
     for different versions of openblas. [#21340](https://github.com/scikit-learn/scikit-learn/pull/21340)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     now raises a better error message when the solver does not support sparse matrices with int64 indices. [#21093](https://github.com/scikit-learn/scikit-learn/pull/21093)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id4 "Link to this heading")

*   Fix [`neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
    , [`neighbors.KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
    , [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
    , [`neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
     with `metric="precomputed"` raises an error for `bsr` and `dok` sparse matrices in methods: `fit`, `kneighbors` and `radius_neighbors`, due to handling of explicit zeros in `bsr` and `dok` [sparse graph](https://scikit-learn.org/stable/glossary.html#term-sparse-graph)
     formats. [#21199](https://github.com/scikit-learn/scikit-learn/pull/21199)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-pipeline "Link to this heading")

*   Fix [`pipeline.Pipeline.get_feature_names_out`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.get_feature_names_out "sklearn.pipeline.Pipeline.get_feature_names_out")
     correctly passes feature names out from one step of a pipeline to the next. [#21351](https://github.com/scikit-learn/scikit-learn/pull/21351)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-svm "Link to this heading")

*   Fix [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     and [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
     check for an inconsistency in its internal representation and raise an error instead of segfaulting. This fix also resolves [CVE-2020-28975](https://nvd.nist.gov/vuln/detail/CVE-2020-28975)
    . [#21336](https://github.com/scikit-learn/scikit-learn/pull/21336)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id5 "Link to this heading")

*   Enhancement `utils.validation._check_sample_weight` can perform a non-negativity check on the sample weights. It can be turned on using the only\_non\_negative bool parameter. Estimators that check for non-negative weights are updated: [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
     (here the previous error message was misleading), [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
    , [`ensemble.AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
    , [`neighbors.KernelDensity`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
    . [#20880](https://github.com/scikit-learn/scikit-learn/pull/20880)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
     and [András Simon](https://github.com/simonandras)
    .
    
*   Fix Solve a bug in `sklearn.utils.metaestimators.if_delegate_has_method` where the underlying check for an attribute did not work with NumPy arrays. [#21145](https://github.com/scikit-learn/scikit-learn/pull/21145)
     by [Zahlii](https://github.com/Zahlii)
    .
    

#### Miscellaneous[#](https://scikit-learn.org/stable/whats_new/v1.0.html#miscellaneous "Link to this heading")

*   Fix Fitting an estimator on a dataset that has no feature names, that was previously fitted on a dataset with feature names no longer keeps the old feature names stored in the `feature_names_in_` attribute. [#21389](https://github.com/scikit-learn/scikit-learn/pull/21389)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

Version 1.0.0[#](https://scikit-learn.org/stable/whats_new/v1.0.html#version-1-0-0 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**September 2021**

### Minimal dependencies[#](https://scikit-learn.org/stable/whats_new/v1.0.html#minimal-dependencies "Link to this heading")

Version 1.0.0 of scikit-learn requires python 3.7+, numpy 1.14.6+ and scipy 1.1.0+. Optional minimal dependency is matplotlib 2.2.2+.

### Enforcing keyword-only arguments[#](https://scikit-learn.org/stable/whats_new/v1.0.html#enforcing-keyword-only-arguments "Link to this heading")

In an effort to promote clear and non-ambiguous use of the library, most constructor and function parameters must now be passed as keyword arguments (i.e. using the `param=value` syntax) instead of positional. If a keyword-only parameter is used as positional, a `TypeError` is now raised. [#15005](https://github.com/scikit-learn/scikit-learn/issues/15005)
 [#20002](https://github.com/scikit-learn/scikit-learn/pull/20002)
 by [Joel Nothman](https://joelnothman.com/)
, [Adrin Jalali](https://github.com/adrinjalali)
, [Thomas Fan](https://github.com/thomasjpfan)
, [Nicolas Hug](https://github.com/NicolasHug)
, and [Tom Dupre la Tour](https://github.com/TomDLT)
. See [SLEP009](https://scikit-learn-enhancement-proposals.readthedocs.io/en/latest/slep009/proposal.html)
 for more details.

### Changed models[#](https://scikit-learn.org/stable/whats_new/v1.0.html#changed-models "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   Fix [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     now avoids numerical underflow issues during affinity matrix computation.
    
*   Fix [`manifold.Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
     now connects disconnected components of the neighbors graph along some minimum distance pairs, instead of changing every infinite distances to zero.
    
*   Fix The splitting criterion of [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
     and [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
     can be impacted by a fix in the handling of rounding errors. Previously some extra spurious splits could occur.
    
*   Fix [`model_selection.train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
     with a `stratify` parameter and [`model_selection.StratifiedShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")
     may lead to slightly different results.
    

Details are listed in the changelog below.

(While we are trying to better inform users by providing this information, we cannot assure that this list is complete.)

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id6 "Link to this heading")

*   API Change The option for using the squared error via `loss` and `criterion` parameters was made more consistent. The preferred way is by setting the value to `"squared_error"`. Old option names are still valid, produce the same models, but are deprecated and will be removed in version 1.2. [#19310](https://github.com/scikit-learn/scikit-learn/pull/19310)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
    *   For [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
        , `criterion="mse"` is deprecated, use `"squared_error"` instead which is now the default.
        
    *   For [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
        , `loss="ls"` is deprecated, use `"squared_error"` instead which is now the default.
        
    *   For [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
        , `criterion="mse"` is deprecated, use `"squared_error"` instead which is now the default.
        
    *   For [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
        , `loss="least_squares"` is deprecated, use `"squared_error"` instead which is now the default.
        
    *   For [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
        , `loss="squared_loss"` is deprecated, use `"squared_error"` instead.
        
    *   For [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
        , `loss="squared_loss"` is deprecated, use `"squared_error"` instead which is now the default.
        
    *   For [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
        , `criterion="mse"` is deprecated, use `"squared_error"` instead which is now the default.
        
    *   For [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
        , `criterion="mse"` is deprecated, use `"squared_error"` instead which is now the default.
        
*   API Change The option for using the absolute error via `loss` and `criterion` parameters was made more consistent. The preferred way is by setting the value to `"absolute_error"`. Old option names are still valid, produce the same models, but are deprecated and will be removed in version 1.2. [#19733](https://github.com/scikit-learn/scikit-learn/pull/19733)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
    *   For [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
        , `criterion="mae"` is deprecated, use `"absolute_error"` instead.
        
    *   For [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
        , `loss="lad"` is deprecated, use `"absolute_error"` instead.
        
    *   For [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
        , `criterion="mae"` is deprecated, use `"absolute_error"` instead.
        
    *   For [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
        , `loss="least_absolute_deviation"` is deprecated, use `"absolute_error"` instead.
        
    *   For [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
        , `loss="absolute_loss"` is deprecated, use `"absolute_error"` instead which is now the default.
        
    *   For [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
        , `criterion="mae"` is deprecated, use `"absolute_error"` instead.
        
    *   For [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
        , `criterion="mae"` is deprecated, use `"absolute_error"` instead.
        
*   API Change `np.matrix` usage is deprecated in 1.0 and will raise a `TypeError` in 1.2. [#20165](https://github.com/scikit-learn/scikit-learn/pull/20165)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
     has been added to the transformer API to get the names of the output features. `get_feature_names` has in turn been deprecated. [#18444](https://github.com/scikit-learn/scikit-learn/pull/18444)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change All estimators store `feature_names_in_` when fitted on pandas Dataframes. These feature names are compared to names seen in non-`fit` methods, e.g. `transform` and will raise a `FutureWarning` if they are not consistent, see also [Release Highlights for scikit-learn 1.0](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html#sphx-glr-auto-examples-release-highlights-plot-release-highlights-1-0-0-py)
    . These `FutureWarning` s will become `ValueError` s in 1.2. [#18010](https://github.com/scikit-learn/scikit-learn/pull/18010)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-base "Link to this heading")

*   Fix [`config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context")
     is now threadsafe. [#18736](https://github.com/scikit-learn/scikit-learn/pull/18736)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id7 "Link to this heading")

*   Feature [`calibration.CalibrationDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay "sklearn.calibration.CalibrationDisplay")
     added to plot calibration curves. [#17443](https://github.com/scikit-learn/scikit-learn/pull/17443)
     by [Lucy Liu](https://github.com/lucyleeow)
    .
    
*   Fix The `predict` and `predict_proba` methods of [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     can now properly be used on prefitted pipelines. [#19641](https://github.com/scikit-learn/scikit-learn/pull/19641)
     by [Alek Lefebvre](https://github.com/AlekLefebvre)
    .
    
*   Fix Fixed an error when using a [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     as `base_estimator` in [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
    . [#20087](https://github.com/scikit-learn/scikit-learn/pull/20087)
     by [Clément Fauchereau](https://github.com/clement-f)
    .
    

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id8 "Link to this heading")

*   Efficiency The `"k-means++"` initialization of [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     and [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     is now faster, especially in multicore settings. [#19002](https://github.com/scikit-learn/scikit-learn/pull/19002)
     by [Jon Crall](https://github.com/Erotemic)
     and [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Efficiency [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     with `algorithm='elkan'` is now faster in multicore settings. [#19052](https://github.com/scikit-learn/scikit-learn/pull/19052)
     by [Yusuke Nagasaka](https://github.com/YusukeNagasaka)
    .
    
*   Efficiency [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     is now faster in multicore settings. [#17622](https://github.com/scikit-learn/scikit-learn/pull/17622)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Efficiency [`cluster.OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
     can now cache the output of the computation of the tree, using the `memory` parameter. [#19024](https://github.com/scikit-learn/scikit-learn/pull/19024)
     by [Frankie Robertson](https://github.com/frankier)
    .
    
*   Enhancement The `predict` and `fit_predict` methods of [`cluster.AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
     now accept sparse data type for input data. [#20117](https://github.com/scikit-learn/scikit-learn/pull/20117)
     by [Venkatachalam Natchiappan](https://github.com/venkyyuvy)
    
*   Fix Fixed a bug in [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     where the sample weights were partially ignored when the input is sparse. [#17622](https://github.com/scikit-learn/scikit-learn/pull/17622)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix Improved convergence detection based on center change in [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     which was almost never achievable. [#17622](https://github.com/scikit-learn/scikit-learn/pull/17622)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     now supports readonly memory-mapped datasets. [#19883](https://github.com/scikit-learn/scikit-learn/pull/19883)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Fix [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     correctly connects components when connectivity and affinity are both precomputed and the number of connected components is greater than 1. [#20597](https://github.com/scikit-learn/scikit-learn/pull/20597)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`cluster.FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")
     does not accept a `**params` kwarg in the `fit` function anymore, resulting in a more concise error message. [#20899](https://github.com/scikit-learn/scikit-learn/pull/20899)
     by [Adam Li](https://github.com/adam2392)
    .
    
*   Fix Fixed a bug in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    , ensuring reproducibility and equivalence between sparse and dense input. [#20200](https://github.com/scikit-learn/scikit-learn/pull/20200)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   API Change [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
     attributes, `fit_` and `partial_fit_`, are deprecated and will be removed in 1.2. [#19297](https://github.com/scikit-learn/scikit-learn/pull/19297)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change the default value for the `batch_size` parameter of [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     was changed from 100 to 1024 due to efficiency reasons. The `n_iter_` attribute of [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     now reports the number of started epochs and the `n_steps_` attribute reports the number of mini batches processed. [#17622](https://github.com/scikit-learn/scikit-learn/pull/17622)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   API Change [`cluster.spectral_clustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")
     raises an improved error when passed a `np.matrix`. [#20560](https://github.com/scikit-learn/scikit-learn/pull/20560)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-compose "Link to this heading")

*   Enhancement [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     now records the output of each transformer in `output_indices_`. [#18393](https://github.com/scikit-learn/scikit-learn/pull/18393)
     by [Luca Bittarello](https://github.com/lbittarello)
    .
    
*   Enhancement [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     now allows DataFrame input to have its columns appear in a changed order in `transform`. Further, columns that are dropped will not be required in transform, and additional columns will be ignored if `remainder='drop'`. [#19263](https://github.com/scikit-learn/scikit-learn/pull/19263)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement Adds `**predict_params` keyword argument to [`compose.TransformedTargetRegressor.predict`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor.predict "sklearn.compose.TransformedTargetRegressor.predict")
     that passes keyword argument to the regressor. [#19244](https://github.com/scikit-learn/scikit-learn/pull/19244)
     by [Ricardo](https://github.com/ricardojnf)
    .
    
*   Fix `compose.ColumnTransformer.get_feature_names` supports non-string feature names returned by any of its transformers. However, note that `get_feature_names` is deprecated, use `get_feature_names_out` instead. [#18459](https://github.com/scikit-learn/scikit-learn/pull/18459)
     by [Albert Villanova del Moral](https://github.com/albertvillanova)
     and [Alonso Silva Allende](https://github.com/alonsosilvaallende)
    .
    
*   Fix [`compose.TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
     now takes nD targets with an adequate transformer. [#18898](https://github.com/scikit-learn/scikit-learn/pull/18898)
     by [Oras Phongpanagnam](https://github.com/panangam)
    .
    
*   API Change Adds `verbose_feature_names_out` to [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
    . This flag controls the prefixing of feature names out in [get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
    . [#18444](https://github.com/scikit-learn/scikit-learn/pull/18444)
     and [#21080](https://github.com/scikit-learn/scikit-learn/pull/21080)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.covariance`](https://scikit-learn.org/stable/api/sklearn.covariance.html#module-sklearn.covariance "sklearn.covariance")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-covariance "Link to this heading")

*   Fix Adds arrays check to [`covariance.ledoit_wolf`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf.html#sklearn.covariance.ledoit_wolf "sklearn.covariance.ledoit_wolf")
     and [`covariance.ledoit_wolf_shrinkage`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf_shrinkage.html#sklearn.covariance.ledoit_wolf_shrinkage "sklearn.covariance.ledoit_wolf_shrinkage")
    . [#20416](https://github.com/scikit-learn/scikit-learn/pull/20416)
     by [Hugo Defois](https://github.com/defoishugo)
    .
    
*   API Change Deprecates the following keys in `cv_results_`: `'mean_score'`, `'std_score'`, and `'split(k)_score'` in favor of `'mean_test_score'` `'std_test_score'`, and `'split(k)_test_score'`. [#20583](https://github.com/scikit-learn/scikit-learn/pull/20583)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id9 "Link to this heading")

*   Enhancement [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     now supports categories with missing values when returning a pandas dataframe. [#19365](https://github.com/scikit-learn/scikit-learn/pull/19365)
     by [Thomas Fan](https://github.com/thomasjpfan)
     and [Amanda Dsouza](https://github.com/amy12xx)
     and [EL-ATEIF Sara](https://github.com/elateifsara)
    .
    
*   Enhancement [`datasets.fetch_kddcup99`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99 "sklearn.datasets.fetch_kddcup99")
     raises a better message when the cached file is invalid. [#19669](https://github.com/scikit-learn/scikit-learn/pull/19669)
     [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement Replace usages of `__file__` related to resource file I/O with `importlib.resources` to avoid the assumption that these resource files (e.g. `iris.csv`) already exist on a filesystem, and by extension to enable compatibility with tools such as `PyOxidizer`. [#20297](https://github.com/scikit-learn/scikit-learn/pull/20297)
     by [Jack Liu](https://github.com/jackzyliu)
    .
    
*   Fix Shorten data file names in the openml tests to better support installing on Windows and its default 260 character limit on file names. [#20209](https://github.com/scikit-learn/scikit-learn/pull/20209)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`datasets.fetch_kddcup99`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99 "sklearn.datasets.fetch_kddcup99")
     returns dataframes when `return_X_y=True` and `as_frame=True`. [#19011](https://github.com/scikit-learn/scikit-learn/pull/19011)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change Deprecates `datasets.load_boston` in 1.0 and it will be removed in 1.2. Alternative code snippets to load similar datasets are provided. Please report to the docstring of the function for details. [#20729](https://github.com/scikit-learn/scikit-learn/pull/20729)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id10 "Link to this heading")

*   Enhancement added a new approximate solver (randomized SVD, available with `eigen_solver='randomized'`) to [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
    . This significantly accelerates computation when the number of samples is much larger than the desired number of components. [#12069](https://github.com/scikit-learn/scikit-learn/pull/12069)
     by [Sylvain Marié](https://github.com/smarie)
    .
    
*   Fix Fixes incorrect multiple data-conversion warnings when clustering boolean data. [#19046](https://github.com/scikit-learn/scikit-learn/pull/19046)
     by [Surya Prakash](https://github.com/jdsurya)
    .
    
*   Fix Fixed [`decomposition.dict_learning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#sklearn.decomposition.dict_learning "sklearn.decomposition.dict_learning")
    , used by [`decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
    , to ensure determinism of the output. Achieved by flipping signs of the SVD output which is used to initialize the code. [#18433](https://github.com/scikit-learn/scikit-learn/pull/18433)
     by [Bruno Charron](https://github.com/brcharron)
    .
    
*   Fix Fixed a bug in [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
    , [`decomposition.MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")
     and [`decomposition.dict_learning_online`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html#sklearn.decomposition.dict_learning_online "sklearn.decomposition.dict_learning_online")
     where the update of the dictionary was incorrect. [#19198](https://github.com/scikit-learn/scikit-learn/pull/19198)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix Fixed a bug in [`decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
    , [`decomposition.SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")
    , [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
    , [`decomposition.MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")
    , [`decomposition.dict_learning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#sklearn.decomposition.dict_learning "sklearn.decomposition.dict_learning")
     and [`decomposition.dict_learning_online`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html#sklearn.decomposition.dict_learning_online "sklearn.decomposition.dict_learning_online")
     where the restart of unused atoms during the dictionary update was not working as expected. [#19198](https://github.com/scikit-learn/scikit-learn/pull/19198)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   API Change In [`decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
    , [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
    , [`decomposition.dict_learning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#sklearn.decomposition.dict_learning "sklearn.decomposition.dict_learning")
     and [`decomposition.dict_learning_online`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html#sklearn.decomposition.dict_learning_online "sklearn.decomposition.dict_learning_online")
    , `transform_alpha` will be equal to `alpha` instead of 1.0 by default starting from version 1.2 [#19159](https://github.com/scikit-learn/scikit-learn/pull/19159)
     by [Benoît Malézieux](https://github.com/bmalezieux)
    .
    
*   API Change Rename variable names in [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
     to improve readability. `lambdas_` and `alphas_` are renamed to `eigenvalues_` and `eigenvectors_`, respectively. `lambdas_` and `alphas_` are deprecated and will be removed in 1.2. [#19908](https://github.com/scikit-learn/scikit-learn/pull/19908)
     by [Kei Ishikawa](https://github.com/kstoneriv3)
    .
    
*   API Change The `alpha` and `regularization` parameters of [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     and [`decomposition.non_negative_factorization`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.non_negative_factorization.html#sklearn.decomposition.non_negative_factorization "sklearn.decomposition.non_negative_factorization")
     are deprecated and will be removed in 1.2. Use the new parameters `alpha_W` and `alpha_H` instead. [#20512](https://github.com/scikit-learn/scikit-learn/pull/20512)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.dummy`](https://scikit-learn.org/stable/api/sklearn.dummy.html#module-sklearn.dummy "sklearn.dummy")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-dummy "Link to this heading")

*   API Change Attribute `n_features_in_` in [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
     and [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
     is deprecated and will be removed in 1.2. [#20960](https://github.com/scikit-learn/scikit-learn/pull/20960)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id11 "Link to this heading")

*   Enhancement [`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     take cgroups quotas into account when deciding the number of threads used by OpenMP. This avoids performance problems caused by over-subscription when using those classes in a docker container for instance. [#20477](https://github.com/scikit-learn/scikit-learn/pull/20477)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     are no longer experimental. They are now considered stable and are subject to the same deprecation cycles as all other estimators. [#19799](https://github.com/scikit-learn/scikit-learn/pull/19799)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Enhancement Improve the HTML rendering of the [`ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
     and [`ensemble.StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
    . [#19564](https://github.com/scikit-learn/scikit-learn/pull/19564)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement Added Poisson criterion to [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    . [#19836](https://github.com/scikit-learn/scikit-learn/pull/19836)
     by [Brian Sun](https://github.com/bsun94)
    .
    
*   Fix Do not allow to compute out-of-bag (OOB) score in [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
     and [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
     with multiclass-multioutput target since scikit-learn does not provide any metric supporting this type of target. Additional private refactoring was performed. [#19162](https://github.com/scikit-learn/scikit-learn/pull/19162)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Improve numerical precision for weights boosting in [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
     and [`ensemble.AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
     to avoid underflows. [#10096](https://github.com/scikit-learn/scikit-learn/pull/10096)
     by [Fenil Suchak](https://github.com/fenilsuchak)
    .
    
*   Fix Fixed the range of the argument `max_samples` to be `(0.0, 1.0]` in [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , where `max_samples=1.0` is interpreted as using all `n_samples` for bootstrapping. [#20159](https://github.com/scikit-learn/scikit-learn/pull/20159)
     by [@murata-yu](https://github.com/murata-yu)
    .
    
*   Fix Fixed a bug in [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
     and [`ensemble.AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
     where the `sample_weight` parameter got overwritten during `fit`. [#20534](https://github.com/scikit-learn/scikit-learn/pull/20534)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change Removes `tol=None` option in [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
    . Please use `tol=0` for the same behavior. [#19296](https://github.com/scikit-learn/scikit-learn/pull/19296)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id12 "Link to this heading")

*   Fix Fixed a bug in [`feature_extraction.text.HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
     where some input strings would result in negative indices in the transformed data. [#19035](https://github.com/scikit-learn/scikit-learn/pull/19035)
     by [Liu Yu](https://github.com/ly648499246)
    .
    
*   Fix Fixed a bug in [`feature_extraction.DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
     by raising an error with unsupported value type. [#19520](https://github.com/scikit-learn/scikit-learn/pull/19520)
     by [Jeff Zhao](https://github.com/kamiyaa)
    .
    
*   Fix Fixed a bug in [`feature_extraction.image.img_to_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.img_to_graph.html#sklearn.feature_extraction.image.img_to_graph "sklearn.feature_extraction.image.img_to_graph")
     and [`feature_extraction.image.grid_to_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.grid_to_graph.html#sklearn.feature_extraction.image.grid_to_graph "sklearn.feature_extraction.image.grid_to_graph")
     where singleton connected components were not handled properly, resulting in a wrong vertex indexing. [#18964](https://github.com/scikit-learn/scikit-learn/pull/18964)
     by [Bertrand Thirion](https://team.inria.fr/parietal/bertrand-thirions-page)
    .
    
*   Fix Raise a warning in [`feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     with `lowercase=True` when there are vocabulary entries with uppercase characters to avoid silent misses in the resulting feature vectors. [#19401](https://github.com/scikit-learn/scikit-learn/pull/19401)
     by [Zito Relova](https://github.com/zitorelova)
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id13 "Link to this heading")

*   Feature [`feature_selection.r_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html#sklearn.feature_selection.r_regression "sklearn.feature_selection.r_regression")
     computes Pearson’s R correlation coefficients between the features and the target. [#17169](https://github.com/scikit-learn/scikit-learn/pull/17169)
     by [Dmytro Lituiev](https://github.com/DSLituiev)
     and [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Enhancement [`feature_selection.RFE.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE.fit "sklearn.feature_selection.RFE.fit")
     accepts additional estimator parameters that are passed directly to the estimator’s `fit` method. [#20380](https://github.com/scikit-learn/scikit-learn/pull/20380)
     by [Iván Pulido](https://github.com/ijpulidos)
    , [Felipe Bidu](https://github.com/fbidu)
    , [Gil Rutter](https://github.com/g-rutter)
    , and [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Fix Fix a bug in [`isotonic.isotonic_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.isotonic_regression.html#sklearn.isotonic.isotonic_regression "sklearn.isotonic.isotonic_regression")
     where the `sample_weight` passed by a user were overwritten during `fit`. [#20515](https://github.com/scikit-learn/scikit-learn/pull/20515)
     by [Carsten Allefeld](https://github.com/allefeld)
    .
    
*   Fix Change [`feature_selection.SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
     to allow for unsupervised modelling so that the `fit` signature need not do any `y` validation and allow for `y=None`. [#19568](https://github.com/scikit-learn/scikit-learn/pull/19568)
     by [Shyam Desai](https://github.com/ShyamDesai)
    .
    
*   API Change Raises an error in [`feature_selection.VarianceThreshold`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html#sklearn.feature_selection.VarianceThreshold "sklearn.feature_selection.VarianceThreshold")
     when the variance threshold is negative. [#20207](https://github.com/scikit-learn/scikit-learn/pull/20207)
     by [Tomohiro Endo](https://github.com/europeanplaice)
    
*   API Change Deprecates `grid_scores_` in favor of split scores in `cv_results_` in [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
    . `grid_scores_` will be removed in version 1.2. [#20161](https://github.com/scikit-learn/scikit-learn/pull/20161)
     by [Shuhei Kayawari](https://github.com/wowry)
     and [@arka204](https://github.com/arka204)
    .
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-inspection "Link to this heading")

*   Enhancement Add `max_samples` parameter in [`inspection.permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
    . It enables to draw a subset of the samples to compute the permutation importance. This is useful to keep the method tractable when evaluating feature importance on large datasets. [#20431](https://github.com/scikit-learn/scikit-learn/pull/20431)
     by [Oliver Pfaffel](https://github.com/o1iv3r)
    .
    
*   Enhancement Add kwargs to format ICE and PD lines separately in partial dependence plots `inspection.plot_partial_dependence` and [`inspection.PartialDependenceDisplay.plot`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.plot "sklearn.inspection.PartialDependenceDisplay.plot")
    . [#19428](https://github.com/scikit-learn/scikit-learn/pull/19428)
     by [Mehdi Hamoumi](https://github.com/mhham)
    .
    
*   Fix Allow multiple scorers input to [`inspection.permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
    . [#19411](https://github.com/scikit-learn/scikit-learn/pull/19411)
     by [Simona Maggio](https://github.com/simonamaggio)
    .
    
*   API Change [`inspection.PartialDependenceDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "sklearn.inspection.PartialDependenceDisplay")
     exposes a class method: [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
    . `inspection.plot_partial_dependence` is deprecated in favor of the class method and will be removed in 1.2. [#20959](https://github.com/scikit-learn/scikit-learn/pull/20959)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.kernel_approximation`](https://scikit-learn.org/stable/api/sklearn.kernel_approximation.html#module-sklearn.kernel_approximation "sklearn.kernel_approximation")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-kernel-approximation "Link to this heading")

*   Fix Fix a bug in [`kernel_approximation.Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
     where the attribute `component_indices_` did not correspond to the subset of sample indices used to generate the approximated kernel. [#20554](https://github.com/scikit-learn/scikit-learn/pull/20554)
     by [Xiangyin Kong](https://github.com/kxytim)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id14 "Link to this heading")

*   Major Feature Added [`linear_model.QuantileRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
     which implements linear quantile regression with L1 penalty. [#9978](https://github.com/scikit-learn/scikit-learn/pull/9978)
     by [David Dale](https://github.com/avidale)
     and [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Feature The new [`linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
     provides an SGD implementation of the linear One-Class SVM. Combined with kernel approximation techniques, this implementation approximates the solution of a kernelized One Class SVM while benefiting from a linear complexity in the number of samples. [#10027](https://github.com/scikit-learn/scikit-learn/pull/10027)
     by [Albert Thomas](https://github.com/albertcthomas)
    .
    
*   Feature Added `sample_weight` parameter to [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
     and [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    . [#16449](https://github.com/scikit-learn/scikit-learn/pull/16449)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Feature Added new solver `lbfgs` (available with `solver="lbfgs"`) and `positive` argument to [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    . When `positive` is set to `True`, forces the coefficients to be positive (only supported by `lbfgs`). [#20231](https://github.com/scikit-learn/scikit-learn/pull/20231)
     by [Toshihiro Nakae](https://github.com/tnakae)
    .
    
*   Efficiency The implementation of [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     has been optimised for dense matrices when using `solver='newton-cg'` and `multi_class!='multinomial'`. [#19571](https://github.com/scikit-learn/scikit-learn/pull/19571)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Enhancement `fit` method preserves dtype for numpy.float32 in [`linear_model.Lars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html#sklearn.linear_model.Lars "sklearn.linear_model.Lars")
    , [`linear_model.LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")
    , [`linear_model.LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")
    , [`linear_model.LarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV "sklearn.linear_model.LarsCV")
     and [`linear_model.LassoLarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV")
    . [#20155](https://github.com/scikit-learn/scikit-learn/pull/20155)
     by [Takeshi Oura](https://github.com/takoika)
    .
    
*   Enhancement Validate user-supplied gram matrix passed to linear models via the `precompute` argument. [#19004](https://github.com/scikit-learn/scikit-learn/pull/19004)
     by [Adam Midvidy](https://github.com/amidvidy)
    .
    
*   Fix [`linear_model.ElasticNet.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet.fit "sklearn.linear_model.ElasticNet.fit")
     no longer modifies `sample_weight` in place. [#19055](https://github.com/scikit-learn/scikit-learn/pull/19055)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     and [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     no longer have a `dual_gap_` not corresponding to their objective. [#19172](https://github.com/scikit-learn/scikit-learn/pull/19172)
     by [Mathurin Massias](https://github.com/mathurinm)
    
*   Fix `sample_weight` are now fully taken into account in linear models when `normalize=True` for both feature centering and feature scaling. [#19426](https://github.com/scikit-learn/scikit-learn/pull/19426)
     by [Alexandre Gramfort](https://github.com/agramfort)
     and [Maria Telenczuk](https://github.com/maikia)
    .
    
*   Fix Points with residuals equal to `residual_threshold` are now considered as inliers for [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
    . This allows fitting a model perfectly on some datasets when `residual_threshold=0`. [#19499](https://github.com/scikit-learn/scikit-learn/pull/19499)
     by [Gregory Strubel](https://github.com/gregorystrubel)
    .
    
*   Fix Sample weight invariance for [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     was fixed in [#19616](https://github.com/scikit-learn/scikit-learn/pull/19616)
     by [Oliver Grisel](https://github.com/ogrisel)
     and [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Fix The dictionary `params` in [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
     and [`linear_model.lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")
     should only contain parameter of the coordinate descent solver. Otherwise, an error will be raised. [#19391](https://github.com/scikit-learn/scikit-learn/pull/19391)
     by [Shao Yang Hong](https://github.com/hongshaoyang)
    .
    
*   API Change Raise a warning in [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
     that from version 1.2, `min_samples` need to be set explicitly for models other than [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
    . [#19390](https://github.com/scikit-learn/scikit-learn/pull/19390)
     by [Shao Yang Hong](https://github.com/hongshaoyang)
    .
    
*   API Change : The parameter `normalize` of [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
     is deprecated and will be removed in 1.2. Motivation for this deprecation: `normalize` parameter did not take any effect if `fit_intercept` was set to False and therefore was deemed confusing. The behavior of the deprecated `LinearModel(normalize=True)` can be reproduced with a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     with `LinearModel` (where `LinearModel` is [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
    , [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    , [`RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
    , [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     or [`RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
    ) as follows: `make_pipeline(StandardScaler(with_mean=False), LinearModel())`. The `normalize` parameter in [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
     was deprecated in [#17743](https://github.com/scikit-learn/scikit-learn/pull/17743)
     by [Maria Telenczuk](https://github.com/maikia)
     and [Alexandre Gramfort](https://github.com/agramfort)
    . Same for [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    , [`RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
    , [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
    , and [`RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
    , in: [#17772](https://github.com/scikit-learn/scikit-learn/pull/17772)
     by [Maria Telenczuk](https://github.com/maikia)
     and [Alexandre Gramfort](https://github.com/agramfort)
    . Same for [`BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
    , [`ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
     in: [#17746](https://github.com/scikit-learn/scikit-learn/pull/17746)
     by [Maria Telenczuk](https://github.com/maikia)
    . Same for [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
    , [`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
    , [`ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
    , [`ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    , [`MultiTaskLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model.MultiTaskLasso")
    , [`MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")
    , [`MultiTaskElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html#sklearn.linear_model.MultiTaskElasticNet "sklearn.linear_model.MultiTaskElasticNet")
    , [`MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")
    , in: [#17785](https://github.com/scikit-learn/scikit-learn/pull/17785)
     by [Maria Telenczuk](https://github.com/maikia)
     and [Alexandre Gramfort](https://github.com/agramfort)
    .
    
*   API Change The `normalize` parameter of [`OrthogonalMatchingPursuit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html#sklearn.linear_model.OrthogonalMatchingPursuit "sklearn.linear_model.OrthogonalMatchingPursuit")
     and [`OrthogonalMatchingPursuitCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuitCV.html#sklearn.linear_model.OrthogonalMatchingPursuitCV "sklearn.linear_model.OrthogonalMatchingPursuitCV")
     will default to False in 1.2 and will be removed in 1.4. [#17750](https://github.com/scikit-learn/scikit-learn/pull/17750)
     by [Maria Telenczuk](https://github.com/maikia)
     and [Alexandre Gramfort](https://github.com/agramfort)
    . Same for [`Lars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html#sklearn.linear_model.Lars "sklearn.linear_model.Lars")
     [`LarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV "sklearn.linear_model.LarsCV")
     [`LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")
     [`LassoLarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV")
     [`LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
    , in [#17769](https://github.com/scikit-learn/scikit-learn/pull/17769)
     by [Maria Telenczuk](https://github.com/maikia)
     and [Alexandre Gramfort](https://github.com/agramfort)
    .
    
*   API Change Keyword validation has moved from `__init__` and `set_params` to `fit` for the following estimators conforming to scikit-learn’s conventions: [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    , [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
    , [`SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
    , [`PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier")
    , and [`PassiveAggressiveRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model.PassiveAggressiveRegressor")
    . [#20683](https://github.com/scikit-learn/scikit-learn/pull/20683)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id15 "Link to this heading")

*   Enhancement Implement `'auto'` heuristic for the `learning_rate` in [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
    . It will become default in 1.2. The default initialization will change to `pca` in 1.2. PCA initialization will be scaled to have standard deviation 1e-4 in 1.2. [#19491](https://github.com/scikit-learn/scikit-learn/pull/19491)
     by [Dmitry Kobak](https://github.com/dkobak)
    .
    
*   Fix Change numerical precision to prevent underflow issues during affinity matrix computation for [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
    . [#19472](https://github.com/scikit-learn/scikit-learn/pull/19472)
     by [Dmitry Kobak](https://github.com/dkobak)
    .
    
*   Fix [`manifold.Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
     now uses `scipy.sparse.csgraph.shortest_path` to compute the graph shortest path. It also connects disconnected components of the neighbors graph along some minimum distance pairs, instead of changing every infinite distances to zero. [#20531](https://github.com/scikit-learn/scikit-learn/pull/20531)
     by [Roman Yurchak](https://github.com/rth)
     and [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Fix Decrease the numerical default tolerance in the lobpcg call in [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
     to prevent numerical instability. [#21194](https://github.com/scikit-learn/scikit-learn/pull/21194)
     by [Andrew Knyazev](https://github.com/lobpcg)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id16 "Link to this heading")

*   Feature [`metrics.mean_pinball_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
     exposes the pinball loss for quantile regression. [#19415](https://github.com/scikit-learn/scikit-learn/pull/19415)
     by [Xavier Dupré](https://github.com/sdpython)
     and [Oliver Grisel](https://github.com/ogrisel)
    .
    
*   Feature [`metrics.d2_tweedie_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_tweedie_score.html#sklearn.metrics.d2_tweedie_score "sklearn.metrics.d2_tweedie_score")
     calculates the D^2 regression score for Tweedie deviances with power parameter `power`. This is a generalization of the `r2_score` and can be interpreted as percentage of Tweedie deviance explained. [#17036](https://github.com/scikit-learn/scikit-learn/pull/17036)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Feature [`metrics.mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html#sklearn.metrics.mean_squared_log_error "sklearn.metrics.mean_squared_log_error")
     now supports `squared=False`. [#20326](https://github.com/scikit-learn/scikit-learn/pull/20326)
     by [Uttam kumar](https://github.com/helper-uttam)
    .
    
*   Efficiency Improved speed of [`metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
     when labels are integral. [#9843](https://github.com/scikit-learn/scikit-learn/pull/9843)
     by [Jon Crall](https://github.com/Erotemic)
    .
    
*   Enhancement A fix to raise an error in [`metrics.hinge_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hinge_loss.html#sklearn.metrics.hinge_loss "sklearn.metrics.hinge_loss")
     when `pred_decision` is 1d whereas it is a multiclass classification or when `pred_decision` parameter is not consistent with the `labels` parameter. [#19643](https://github.com/scikit-learn/scikit-learn/pull/19643)
     by [Pierre Attard](https://github.com/PierreAttard)
    .
    
*   Fix [`metrics.ConfusionMatrixDisplay.plot`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.plot "sklearn.metrics.ConfusionMatrixDisplay.plot")
     uses the correct max for colormap. [#19784](https://github.com/scikit-learn/scikit-learn/pull/19784)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Samples with zero `sample_weight` values do not affect the results from [`metrics.det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")
    , [`metrics.precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")
     and [`metrics.roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
    . [#18328](https://github.com/scikit-learn/scikit-learn/pull/18328)
     by [Albert Villanova del Moral](https://github.com/albertvillanova)
     and [Alonso Silva Allende](https://github.com/alonsosilvaallende)
    .
    
*   Fix avoid overflow in [`metrics.adjusted_rand_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#sklearn.metrics.adjusted_rand_score "sklearn.metrics.adjusted_rand_score")
     with large amount of data. [#20312](https://github.com/scikit-learn/scikit-learn/pull/20312)
     by [Divyanshu Deoli](https://github.com/divyanshudeoli)
    .
    
*   API Change [`metrics.ConfusionMatrixDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay "sklearn.metrics.ConfusionMatrixDisplay")
     exposes two class methods [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_estimator "sklearn.metrics.ConfusionMatrixDisplay.from_estimator")
     and [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_predictions "sklearn.metrics.ConfusionMatrixDisplay.from_predictions")
     allowing to create a confusion matrix plot using an estimator or the predictions. `metrics.plot_confusion_matrix` is deprecated in favor of these two class methods and will be removed in 1.2. [#18543](https://github.com/scikit-learn/scikit-learn/pull/18543)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change [`metrics.PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")
     exposes two class methods [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
     and [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")
     allowing to create a precision-recall curve using an estimator or the predictions. `metrics.plot_precision_recall_curve` is deprecated in favor of these two class methods and will be removed in 1.2. [#20552](https://github.com/scikit-learn/scikit-learn/pull/20552)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change [`metrics.DetCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay "sklearn.metrics.DetCurveDisplay")
     exposes two class methods [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_estimator "sklearn.metrics.DetCurveDisplay.from_estimator")
     and [`from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_predictions "sklearn.metrics.DetCurveDisplay.from_predictions")
     allowing to create a confusion matrix plot using an estimator or the predictions. `metrics.plot_det_curve` is deprecated in favor of these two class methods and will be removed in 1.2. [#19278](https://github.com/scikit-learn/scikit-learn/pull/19278)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.mixture`](https://scikit-learn.org/stable/api/sklearn.mixture.html#module-sklearn.mixture "sklearn.mixture")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-mixture "Link to this heading")

*   Fix Ensure that the best parameters are set appropriately in the case of divergency for [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     and [`mixture.BayesianGaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")
    . [#20030](https://github.com/scikit-learn/scikit-learn/pull/20030)
     by [Tingshan Liu](https://github.com/tliu68)
     and [Benjamin Pedigo](https://github.com/bdpedigo)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-model-selection "Link to this heading")

*   Feature added [`model_selection.StratifiedGroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold "sklearn.model_selection.StratifiedGroupKFold")
    , that combines [`model_selection.StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
     and [`model_selection.GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
    , providing an ability to split data preserving the distribution of classes in each split while keeping each group within a single split. [#18649](https://github.com/scikit-learn/scikit-learn/pull/18649)
     by [Leandro Hermida](https://github.com/hermidalc)
     and [Rodion Martynov](https://github.com/marrodion)
    .
    
*   Enhancement warn only once in the main process for per-split fit failures in cross-validation. [#20619](https://github.com/scikit-learn/scikit-learn/pull/20619)
     by [Loïc Estève](https://github.com/lesteve)
    
*   Enhancement The `model_selection.BaseShuffleSplit` base class is now public. [#20056](https://github.com/scikit-learn/scikit-learn/pull/20056)
     by [@pabloduque0](https://github.com/pabloduque0)
    .
    
*   Fix Avoid premature overflow in [`model_selection.train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
    . [#20904](https://github.com/scikit-learn/scikit-learn/pull/20904)
     by [Tomasz Jakubek](https://github.com/t-jakubek)
    .
    

#### [`sklearn.naive_bayes`](https://scikit-learn.org/stable/api/sklearn.naive_bayes.html#module-sklearn.naive_bayes "sklearn.naive_bayes")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-naive-bayes "Link to this heading")

*   Fix The `fit` and `partial_fit` methods of the discrete naive Bayes classifiers ([`naive_bayes.BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
    , [`naive_bayes.CategoricalNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html#sklearn.naive_bayes.CategoricalNB "sklearn.naive_bayes.CategoricalNB")
    , [`naive_bayes.ComplementNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html#sklearn.naive_bayes.ComplementNB "sklearn.naive_bayes.ComplementNB")
    , and [`naive_bayes.MultinomialNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB "sklearn.naive_bayes.MultinomialNB")
    ) now correctly handle the degenerate case of a single class in the training set. [#18925](https://github.com/scikit-learn/scikit-learn/pull/18925)
     by [David Poznik](https://github.com/dpoznik)
    .
    
*   API Change The attribute `sigma_` is now deprecated in [`naive_bayes.GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
     and will be removed in 1.2. Use `var_` instead. [#18842](https://github.com/scikit-learn/scikit-learn/pull/18842)
     by [Hong Shao Yang](https://github.com/hongshaoyang)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id17 "Link to this heading")

*   Enhancement The creation of [`neighbors.KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
     and [`neighbors.BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
     has been improved for their worst-cases time complexity from O(n2) to O(n). [#19473](https://github.com/scikit-learn/scikit-learn/pull/19473)
     by [jiefangxuanyan](https://github.com/jiefangxuanyan)
     and [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Fix `neighbors.DistanceMetric` subclasses now support readonly memory-mapped datasets. [#19883](https://github.com/scikit-learn/scikit-learn/pull/19883)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Fix [`neighbors.NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
    , [`neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
    , [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
    , [`neighbors.KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
     and [`neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
     do not validate `weights` in `__init__` and validate `weights` in `fit` instead. [#20072](https://github.com/scikit-learn/scikit-learn/pull/20072)
     by [Juan Carlos Alfaro Jiménez](https://github.com/alfaro96)
    .
    
*   API Change The parameter `kwargs` of [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
     is deprecated and will be removed in 1.2. [#20842](https://github.com/scikit-learn/scikit-learn/pull/20842)
     by [Juan Martín Loyola](https://github.com/jmloyola)
    .
    

#### [`sklearn.neural_network`](https://scikit-learn.org/stable/api/sklearn.neural_network.html#module-sklearn.neural_network "sklearn.neural_network")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#sklearn-neural-network "Link to this heading")

*   Fix [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     and [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
     now correctly support continued training when loading from a pickled file. [#19631](https://github.com/scikit-learn/scikit-learn/pull/19631)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id18 "Link to this heading")

*   API Change The `predict_proba` and `predict_log_proba` methods of the [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     now support passing prediction kwargs to the final estimator. [#19790](https://github.com/scikit-learn/scikit-learn/pull/19790)
     by [Christopher Flynn](https://github.com/crflynn)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id19 "Link to this heading")

*   Feature The new [`preprocessing.SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
     is a feature preprocessing tool for the generation of B-splines, parametrized by the polynomial `degree` of the splines, number of knots `n_knots` and knot positioning strategy `knots`. [#18368](https://github.com/scikit-learn/scikit-learn/pull/18368)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    . [`preprocessing.SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
     also supports periodic splines via the `extrapolation` argument. [#19483](https://github.com/scikit-learn/scikit-learn/pull/19483)
     by [Malte Londschien](https://github.com/mlondschien)
    . [`preprocessing.SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
     supports sample weights for knot position strategy `"quantile"`. [#20526](https://github.com/scikit-learn/scikit-learn/pull/20526)
     by [Malte Londschien](https://github.com/mlondschien)
    .
    
*   Feature [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     supports passing through missing values by default. [#19069](https://github.com/scikit-learn/scikit-learn/pull/19069)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     now supports `handle_unknown='ignore'` and dropping categories. [#19041](https://github.com/scikit-learn/scikit-learn/pull/19041)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature [`preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
     now supports passing a tuple to `degree`, i.e. `degree=(min_degree, max_degree)`. [#20250](https://github.com/scikit-learn/scikit-learn/pull/20250)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Efficiency [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
     is faster and more memory efficient. [#20652](https://github.com/scikit-learn/scikit-learn/pull/20652)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Efficiency Changed `algorithm` argument for [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     in [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
     from `auto` to `full`. [#19934](https://github.com/scikit-learn/scikit-learn/pull/19934)
     by [Hleb Levitski](https://github.com/glevv)
    .
    
*   Efficiency The implementation of `fit` for [`preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
     transformer is now faster. This is especially noticeable on large sparse input. [#19734](https://github.com/scikit-learn/scikit-learn/pull/19734)
     by [Fred Robinson](https://github.com/frrad)
    .
    
*   Fix The [`preprocessing.StandardScaler.inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler.inverse_transform "sklearn.preprocessing.StandardScaler.inverse_transform")
     method now raises error when the input data is 1D. [#19752](https://github.com/scikit-learn/scikit-learn/pull/19752)
     by [Zhehao Liu](https://github.com/Max1993Liu)
    .
    
*   Fix [`preprocessing.scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html#sklearn.preprocessing.scale "sklearn.preprocessing.scale")
    , [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
     and similar scalers detect near-constant features to avoid scaling them to very large values. This problem happens in particular when using a scaler on sparse data with a constant column with sample weights, in which case centering is typically disabled. [#19527](https://github.com/scikit-learn/scikit-learn/pull/19527)
     by [Oliver Grisel](https://github.com/ogrisel)
     and [Maria Telenczuk](https://github.com/maikia)
     and [#19788](https://github.com/scikit-learn/scikit-learn/pull/19788)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix [`preprocessing.StandardScaler.inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler.inverse_transform "sklearn.preprocessing.StandardScaler.inverse_transform")
     now correctly handles integer dtypes. [#19356](https://github.com/scikit-learn/scikit-learn/pull/19356)
     by [@makoeppel](https://github.com/makoeppel)
    .
    
*   Fix [`preprocessing.OrdinalEncoder.inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.inverse_transform "sklearn.preprocessing.OrdinalEncoder.inverse_transform")
     is not supporting sparse matrix and raises the appropriate error message. [#19879](https://github.com/scikit-learn/scikit-learn/pull/19879)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix The `fit` method of [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     will not raise error when `handle_unknown='ignore'` and unknown categories are given to `fit`. [#19906](https://github.com/scikit-learn/scikit-learn/pull/19906)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
    .
    
*   Fix Fix a regression in [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     where large Python numeric would raise an error due to overflow when casted to C type (`np.float64` or `np.int64`). [#20727](https://github.com/scikit-learn/scikit-learn/pull/20727)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`preprocessing.FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
     does not set `n_features_in_` based on the input to `inverse_transform`. [#20961](https://github.com/scikit-learn/scikit-learn/pull/20961)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change The `n_input_features_` attribute of [`preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
     is deprecated in favor of `n_features_in_` and will be removed in 1.2. [#20240](https://github.com/scikit-learn/scikit-learn/pull/20240)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id20 "Link to this heading")

*   API Change The parameter `**params` of [`svm.OneClassSVM.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM.fit "sklearn.svm.OneClassSVM.fit")
     is deprecated and will be removed in 1.2. [#20843](https://github.com/scikit-learn/scikit-learn/pull/20843)
     by [Juan Martín Loyola](https://github.com/jmloyola)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id21 "Link to this heading")

*   Enhancement Add `fontname` argument in [`tree.export_graphviz`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz "sklearn.tree.export_graphviz")
     for non-English characters. [#18959](https://github.com/scikit-learn/scikit-learn/pull/18959)
     by [Zero](https://github.com/Zeroto521)
     and [wstates](https://github.com/wstates)
    .
    
*   Fix Improves compatibility of [`tree.plot_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree")
     with high DPI screens. [#20023](https://github.com/scikit-learn/scikit-learn/pull/20023)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Fixed a bug in [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
     where a node could be split whereas it should not have been due to incorrect handling of rounding errors. [#19336](https://github.com/scikit-learn/scikit-learn/pull/19336)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   API Change The `n_features_` attribute of [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
     and [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
     is deprecated in favor of `n_features_in_` and will be removed in 1.2. [#20272](https://github.com/scikit-learn/scikit-learn/pull/20272)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.0.html#id22 "Link to this heading")

*   Enhancement Deprecated the default value of the `random_state=0` in [`randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
    . Starting in 1.2, the default value of `random_state` will be set to `None`. [#19459](https://github.com/scikit-learn/scikit-learn/pull/19459)
     by [Cindy Bezuidenhout](https://github.com/cinbez)
     and [Clifford Akai-Nettey](https://github.com/cliffordEmmanuel)
    .
    
*   Enhancement Added helper decorator [`utils.metaestimators.available_if`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metaestimators.available_if.html#sklearn.utils.metaestimators.available_if "sklearn.utils.metaestimators.available_if")
     to provide flexibility in metaestimators making methods available or unavailable on the basis of state, in a more readable way. [#19948](https://github.com/scikit-learn/scikit-learn/pull/19948)
     by [Joel Nothman](https://joelnothman.com/)
    .
    
*   Enhancement [`utils.validation.check_is_fitted`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
     now uses `__sklearn_is_fitted__` if available, instead of checking for attributes ending with an underscore. This also makes [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     and [`preprocessing.FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
     pass `check_is_fitted(estimator)`. [#20657](https://github.com/scikit-learn/scikit-learn/pull/20657)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Fix Fixed a bug in [`utils.sparsefuncs.mean_variance_axis`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.mean_variance_axis.html#sklearn.utils.sparsefuncs.mean_variance_axis "sklearn.utils.sparsefuncs.mean_variance_axis")
     where the precision of the computed variance was very poor when the real variance is exactly zero. [#19766](https://github.com/scikit-learn/scikit-learn/pull/19766)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix The docstrings of properties that are decorated with [`utils.deprecated`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.deprecated.html#sklearn.utils.deprecated "sklearn.utils.deprecated")
     are now properly wrapped. [#20385](https://github.com/scikit-learn/scikit-learn/pull/20385)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix `utils.stats._weighted_percentile` now correctly ignores zero-weighted observations smaller than the smallest observation with positive weight for `percentile=0`. Affected classes are [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
     for `quantile=0` and `ensemble.HuberLossFunction` and `ensemble.HuberLossFunction` for `alpha=0`. [#20528](https://github.com/scikit-learn/scikit-learn/pull/20528)
     by [Malte Londschien](https://github.com/mlondschien)
    .
    
*   Fix [`utils._safe_indexing`](https://scikit-learn.org/stable/modules/generated/sklearn.utils._safe_indexing.html#sklearn.utils._safe_indexing "sklearn.utils._safe_indexing")
     explicitly takes a dataframe copy when integer indices are provided avoiding to raise a warning from Pandas. This warning was previously raised in resampling utilities and functions using those utilities (e.g. [`model_selection.train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
    , [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
    , [`model_selection.cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
    , [`model_selection.cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
    ). [#20673](https://github.com/scikit-learn/scikit-learn/pull/20673)
     by [Joris Van den Bossche](https://github.com/jorisvandenbossche)
    .
    
*   Fix Fix a regression in `utils.is_scalar_nan` where large Python numbers would raise an error due to overflow in C types (`np.float64` or `np.int64`). [#20727](https://github.com/scikit-learn/scikit-learn/pull/20727)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Support for `np.matrix` is deprecated in [`check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     in 1.0 and will raise a `TypeError` in 1.2. [#20165](https://github.com/scikit-learn/scikit-learn/pull/20165)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change `utils._testing.assert_warns` and `utils._testing.assert_warns_message` are deprecated in 1.0 and will be removed in 1.2. Used `pytest.warns` context manager instead. Note that these functions were not documented and part from the public API. [#20521](https://github.com/scikit-learn/scikit-learn/pull/20521)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   API Change Fixed several bugs in `utils.graph.graph_shortest_path`, which is now deprecated. Use `scipy.sparse.csgraph.shortest_path` instead. [#20531](https://github.com/scikit-learn/scikit-learn/pull/20531)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    

Code and documentation contributors

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 0.24, including:

Abdulelah S. Al Mesfer, Abhinav Gupta, Adam J. Stewart, Adam Li, Adam Midvidy, Adrian Garcia Badaracco, Adrian Sadłocha, Adrin Jalali, Agamemnon Krasoulis, Alberto Rubiales, Albert Thomas, Albert Villanova del Moral, Alek Lefebvre, Alessia Marcolini, Alexandr Fonari, Alihan Zihna, Aline Ribeiro de Almeida, Amanda, Amanda Dsouza, Amol Deshmukh, Ana Pessoa, Anavelyz, Andreas Mueller, Andrew Delong, Ashish, Ashvith Shetty, Atsushi Nukariya, Aurélien Geron, Avi Gupta, Ayush Singh, baam, BaptBillard, Benjamin Pedigo, Bertrand Thirion, Bharat Raghunathan, bmalezieux, Brian Rice, Brian Sun, Bruno Charron, Bryan Chen, bumblebee, caherrera-meli, Carsten Allefeld, CeeThinwa, Chiara Marmo, chrissobel, Christian Lorentzen, Christopher Yeh, Chuliang Xiao, Clément Fauchereau, cliffordEmmanuel, Conner Shen, Connor Tann, David Dale, David Katz, David Poznik, Dimitri Papadopoulos Orfanos, Divyanshu Deoli, dmallia17, Dmitry Kobak, DS\_anas, Eduardo Jardim, EdwinWenink, EL-ATEIF Sara, Eleni Markou, EricEllwanger, Eric Fiegel, Erich Schubert, Ezri-Mudde, Fatos Morina, Felipe Rodrigues, Felix Hafner, Fenil Suchak, flyingdutchman23, Flynn, Fortune Uwha, Francois Berenger, Frankie Robertson, Frans Larsson, Frederick Robinson, frellwan, Gabriel S Vicente, Gael Varoquaux, genvalen, Geoffrey Thomas, geroldcsendes, Hleb Levitski, Glen, Glòria Macià Muñoz, gregorystrubel, groceryheist, Guillaume Lemaitre, guiweber, Haidar Almubarak, Hans Moritz Günther, Haoyin Xu, Harris Mirza, Harry Wei, Harutaka Kawamura, Hassan Alsawadi, Helder Geovane Gomes de Lima, Hugo DEFOIS, Igor Ilic, Ikko Ashimine, Isaack Mungui, Ishaan Bhat, Ishan Mishra, Iván Pulido, iwhalvic, J Alexander, Jack Liu, James Alan Preiss, James Budarz, James Lamb, Jannik, Jeff Zhao, Jennifer Maldonado, Jérémie du Boisberranger, Jesse Lima, Jianzhu Guo, jnboehm, Joel Nothman, JohanWork, John Paton, Jonathan Schneider, Jon Crall, Jon Haitz Legarreta Gorroño, Joris Van den Bossche, José Manuel Nápoles Duarte, Juan Carlos Alfaro Jiménez, Juan Martin Loyola, Julien Jerphanion, Julio Batista Silva, julyrashchenko, JVM, Kadatatlu Kishore, Karen Palacio, Kei Ishikawa, kmatt10, kobaski, Kot271828, Kunj, KurumeYuta, kxytim, lacrosse91, LalliAcqua, Laveen Bagai, Leonardo Rocco, Leonardo Uieda, Leopoldo Corona, Loic Esteve, LSturtew, Luca Bittarello, Luccas Quadros, Lucy Jiménez, Lucy Liu, ly648499246, Mabu Manaileng, Manimaran, makoeppel, Marco Gorelli, Maren Westermann, Mariangela, Maria Telenczuk, marielaraj, Martin Hirzel, Mateo Noreña, Mathieu Blondel, Mathis Batoul, mathurinm, Matthew Calcote, Maxime Prieur, Maxwell, Mehdi Hamoumi, Mehmet Ali Özer, Miao Cai, Michal Karbownik, michalkrawczyk, Mitzi, mlondschien, Mohamed Haseeb, Mohamed Khoualed, Muhammad Jarir Kanji, murata-yu, Nadim Kawwa, Nanshan Li, naozin555, Nate Parsons, Neal Fultz, Nic Annau, Nicolas Hug, Nicolas Miller, Nico Stefani, Nigel Bosch, Nikita Titov, Nodar Okroshiashvili, Norbert Preining, novaya, Ogbonna Chibuike Stephen, OGordon100, Oliver Pfaffel, Olivier Grisel, Oras Phongpanangam, Pablo Duque, Pablo Ibieta-Jimenez, Patric Lacouth, Paulo S. Costa, Paweł Olszewski, Peter Dye, PierreAttard, Pierre-Yves Le Borgne, PranayAnchuri, Prince Canuma, putschblos, qdeffense, RamyaNP, ranjanikrishnan, Ray Bell, Rene Jean Corneille, Reshama Shaikh, ricardojnf, RichardScottOZ, Rodion Martynov, Rohan Paul, Roman Lutz, Roman Yurchak, Samuel Brice, Sandy Khosasi, Sean Benhur J, Sebastian Flores, Sebastian Pölsterl, Shao Yang Hong, shinehide, shinnar, shivamgargsya, Shooter23, Shuhei Kayawari, Shyam Desai, simonamaggio, Sina Tootoonian, solosilence, Steven Kolawole, Steve Stagg, Surya Prakash, swpease, Sylvain Marié, Takeshi Oura, Terence Honles, TFiFiE, Thomas A Caswell, Thomas J. Fan, Tim Gates, TimotheeMathieu, Timothy Wolodzko, Tim Vink, t-jakubek, t-kusanagi, tliu68, Tobias Uhmann, tom1092, Tomás Moreyra, Tomás Ronald Hughes, Tom Dupré la Tour, Tommaso Di Noto, Tomohiro Endo, TONY GEORGE, Toshihiro NAKAE, tsuga, Uttam kumar, vadim-ushtanit, Vangelis Gkiastas, Venkatachalam N, Vilém Zouhar, Vinicius Rios Fuck, Vlasovets, waijean, Whidou, xavier dupré, xiaoyuchai, Yasmeen Alsaedy, yoch, Yosuke KOBAYASHI, Yu Feng, YusukeNagasaka, yzhenman, Zero, ZeyuSun, ZhaoweiWang, Zito, Zito Relova

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)