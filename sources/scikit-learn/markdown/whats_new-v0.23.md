[Skip to main content](https://scikit-learn.org/stable/whats_new/v0.23.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v0.23.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v0.23.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v0.23.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v0.23.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v0.23.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v0.23.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v0.23.html)

Collapse Sidebar Expand Sidebar

Version 0.23[#](https://scikit-learn.org/stable/whats_new/v0.23.html#version-0-23 "Link to this heading")

==========================================================================================================

For a short description of the main highlights of the release, please refer to [Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html#sphx-glr-auto-examples-release-highlights-plot-release-highlights-0-23-0-py)
.

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 0.23.2[#](https://scikit-learn.org/stable/whats_new/v0.23.html#version-0-23-2 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

### Changed models[#](https://scikit-learn.org/stable/whats_new/v0.23.html#changed-models "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   Fix `inertia_` attribute of [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     and [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
    .
    

Details are listed in the changelog below.

(While we are trying to better inform users by providing this information, we cannot assure that this list is complete.)

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.23.html#changelog "Link to this heading")

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-cluster "Link to this heading")

*   Fix Fixed a bug in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     where rounding errors could prevent convergence to be declared when `tol=0`. [#17959](https://github.com/scikit-learn/scikit-learn/pull/17959)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix Fixed a bug in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     and [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     where the reported inertia was incorrectly weighted by the sample weights. [#17848](https://github.com/scikit-learn/scikit-learn/pull/17848)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix Fixed a bug in [`cluster.MeanShift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")
     with `bin_seeding=True`. When the estimated bandwidth is 0, the behavior is equivalent to `bin_seeding=False`. [#17742](https://github.com/scikit-learn/scikit-learn/pull/17742)
     by [Jeremie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix Fixed a bug in [`cluster.AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
    , that gives incorrect clusters when the array dtype is float32. [#17995](https://github.com/scikit-learn/scikit-learn/pull/17995)
     by [Thomaz Santana](https://github.com/Wikilicious)
     and [Amanda Dsouza](https://github.com/amy12xx)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-decomposition "Link to this heading")

*   Fix Fixed a bug in [`decomposition.MiniBatchDictionaryLearning.partial_fit`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning.partial_fit "sklearn.decomposition.MiniBatchDictionaryLearning.partial_fit")
     which should update the dictionary by iterating only once over a mini-batch. [#17433](https://github.com/scikit-learn/scikit-learn/pull/17433)
     by [Chiara Marmo](https://github.com/cmarmo)
    .
    
*   Fix Avoid overflows on Windows in [`decomposition.IncrementalPCA.partial_fit`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA.partial_fit "sklearn.decomposition.IncrementalPCA.partial_fit")
     for large `batch_size` and `n_samples` values. [#17985](https://github.com/scikit-learn/scikit-learn/pull/17985)
     by [Alan Butler](https://github.com/aldee153)
     and [Amanda Dsouza](https://github.com/amy12xx)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-ensemble "Link to this heading")

*   Fix Fixed bug in `ensemble.MultinomialDeviance` where the average of logloss was incorrectly calculated as sum of logloss. [#17694](https://github.com/scikit-learn/scikit-learn/pull/17694)
     by [Markus Rempfler](https://github.com/rempfler)
     and [Tsutomu Kusanagi](https://github.com/t-kusanagi2)
    .
    
*   Fix Fixes [`ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
     and [`ensemble.StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
     compatibility with estimators that do not define `n_features_in_`. [#17357](https://github.com/scikit-learn/scikit-learn/pull/17357)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-feature-extraction "Link to this heading")

*   Fix Fixes bug in [`feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     where sample order invariance was broken when `max_features` was set and features had the same count. [#18016](https://github.com/scikit-learn/scikit-learn/pull/18016)
     by [Thomas Fan](https://github.com/thomasjpfan)
    , [Roman Yurchak](https://github.com/rth)
    , and [Joel Nothman](https://joelnothman.com/)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-linear-model "Link to this heading")

*   Fix [`linear_model.lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")
     does not overwrite `X` when `X_copy=True` and `Gram='auto'`. [#17914](https://github.com/scikit-learn/scikit-learn/pull/17914)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-manifold "Link to this heading")

*   Fix Fixed a bug where [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     would raise an error if `metric='seuclidean'` and `X` is not type `np.float64`. [#15730](https://github.com/scikit-learn/scikit-learn/pull/15730)
     by [Forrest Koch](https://github.com/ForrestCKoch)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-metrics "Link to this heading")

*   Fix Fixed a bug in [`metrics.mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
     where the average of multiple RMSE values was incorrectly calculated as the root of the average of multiple MSE values. [#17309](https://github.com/scikit-learn/scikit-learn/pull/17309)
     by [Swier Heeres](https://github.com/swierh)
    .
    

#### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-pipeline "Link to this heading")

*   Fix [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     raises a deprecation warning when `None` is included in `transformer_list`. [#17360](https://github.com/scikit-learn/scikit-learn/pull/17360)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-utils "Link to this heading")

*   Fix Fix [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     so that all test cases support the `binary_only` estimator tag. [#17812](https://github.com/scikit-learn/scikit-learn/pull/17812)
     by [Bruno Charron](https://github.com/brcharron)
    .
    

Version 0.23.1[#](https://scikit-learn.org/stable/whats_new/v0.23.html#version-0-23-1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**May 18 2020**

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.23.html#id1 "Link to this heading")

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#id2 "Link to this heading")

*   Efficiency [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     efficiency has been improved for very small datasets. In particular it cannot spawn idle threads any more. [#17210](https://github.com/scikit-learn/scikit-learn/pull/17210)
     and [#17235](https://github.com/scikit-learn/scikit-learn/pull/17235)
     by [Jeremie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix Fixed a bug in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     where the sample weights provided by the user were modified in place. [#17204](https://github.com/scikit-learn/scikit-learn/pull/17204)
     by [Jeremie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### Miscellaneous[#](https://scikit-learn.org/stable/whats_new/v0.23.html#miscellaneous "Link to this heading")

*   Fix Fixed a bug in the `repr` of third-party estimators that use a `**kwargs` parameter in their constructor, when `changed_only` is True which is now the default. [#17205](https://github.com/scikit-learn/scikit-learn/pull/17205)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    

Version 0.23.0[#](https://scikit-learn.org/stable/whats_new/v0.23.html#version-0-23-0 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**May 12 2020**

### Enforcing keyword-only arguments[#](https://scikit-learn.org/stable/whats_new/v0.23.html#enforcing-keyword-only-arguments "Link to this heading")

In an effort to promote clear and non-ambiguous use of the library, most constructor and function parameters are now expected to be passed as keyword arguments (i.e. using the `param=value` syntax) instead of positional. To ease the transition, a `FutureWarning` is raised if a keyword-only parameter is used as positional. In version 1.0 (renaming of 0.25), these parameters will be strictly keyword-only, and a `TypeError` will be raised. [#15005](https://github.com/scikit-learn/scikit-learn/issues/15005)
 by [Joel Nothman](https://joelnothman.com/)
, [Adrin Jalali](https://github.com/adrinjalali)
, [Thomas Fan](https://github.com/thomasjpfan)
, and [Nicolas Hug](https://github.com/NicolasHug)
. See [SLEP009](https://scikit-learn-enhancement-proposals.readthedocs.io/en/latest/slep009/proposal.html)
 for more details.

### Changed models[#](https://scikit-learn.org/stable/whats_new/v0.23.html#id3 "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   Fix [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
    , [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
    , and [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
    .
    
*   Fix [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     with `algorithm="elkan"` and `algorithm="full"`.
    
*   Fix [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
    
*   Fix `compose.ColumnTransformer.get_feature_names`
    
*   Fix [`compose.ColumnTransformer.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer.fit "sklearn.compose.ColumnTransformer.fit")
    
*   Fix [`datasets.make_multilabel_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "sklearn.datasets.make_multilabel_classification")
    
*   Fix [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     with `n_components='mle'`
    
*   Enhancement [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     and [`decomposition.non_negative_factorization`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.non_negative_factorization.html#sklearn.decomposition.non_negative_factorization "sklearn.decomposition.non_negative_factorization")
     with float32 dtype input.
    
*   Fix [`decomposition.KernelPCA.inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA.inverse_transform "sklearn.decomposition.KernelPCA.inverse_transform")
    
*   API Change [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
    
*   Fix `estimator_samples_` in [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
    , [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
     and [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
    
*   Fix [`ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
     and [`ensemble.StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
     with `sample_weight`
    
*   Fix [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
    
*   Fix [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
     with `sample_weight`.
    
*   Fix [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
    
*   Fix [`metrics.mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
     with `squared` and `multioutput='raw_values'`.
    
*   Fix [`metrics.mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mutual_info_score.html#sklearn.metrics.mutual_info_score "sklearn.metrics.mutual_info_score")
     with negative scores.
    
*   Fix [`metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
     with zero length `y_true` and `y_pred`
    
*   Fix [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
    
*   Fix [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
     with `partial_fit` and sparse input.
    
*   Fix [`preprocessing.Normalizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer")
     with norm=’max’
    
*   Fix Any model using the `svm.libsvm` or the `svm.liblinear` solver, including [`svm.LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
    , [`svm.LinearSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR "sklearn.svm.LinearSVR")
    , [`svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
    , [`svm.NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
    , [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
    , [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
    , [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
    , [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    .
    
*   Fix [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
     and [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     as well as `predict` method of [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
    , and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     and read-only float32 input in `predict`, `decision_path` and `predict_proba`.
    

Details are listed in the changelog below.

(While we are trying to better inform users by providing this information, we cannot assure that this list is complete.)

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.23.html#id4 "Link to this heading")

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#id5 "Link to this heading")

*   Efficiency [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
     implementation of the predict method avoids high memory footprint by calculating the distances matrix using a chunked scheme. [#16149](https://github.com/scikit-learn/scikit-learn/pull/16149)
     by [Jeremie du Boisberranger](https://github.com/jeremiedbb)
     and [Alex Shacked](https://github.com/alexshacked)
    .
    
*   Efficiency Major Feature The critical parts of [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     have a more optimized implementation. Parallelism is now over the data instead of over initializations allowing better scalability. [#11950](https://github.com/scikit-learn/scikit-learn/pull/11950)
     by [Jeremie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Enhancement [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     now supports sparse data when `solver = "elkan"`. [#11950](https://github.com/scikit-learn/scikit-learn/pull/11950)
     by [Jeremie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Enhancement [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     has a faster and more memory efficient implementation of single linkage clustering. [#11514](https://github.com/scikit-learn/scikit-learn/pull/11514)
     by [Leland McInnes](https://github.com/lmcinnes)
    .
    
*   Fix [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     with `algorithm="elkan"` now converges with `tol=0` as with the default `algorithm="full"`. [#16075](https://github.com/scikit-learn/scikit-learn/pull/16075)
     by [Erich Schubert](https://github.com/kno10)
    .
    
*   Fix Fixed a bug in [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
     where the `n_clusters` parameter could not have a `np.int64` type. [#16484](https://github.com/scikit-learn/scikit-learn/pull/16484)
     by [Jeremie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     add specific error when distance matrix is not square and `affinity=precomputed`. [#16257](https://github.com/scikit-learn/scikit-learn/pull/16257)
     by [Simona Maggio](https://github.com/simonamaggio)
    .
    
*   API Change The `n_jobs` parameter of [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    , [`cluster.SpectralCoclustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering "sklearn.cluster.SpectralCoclustering")
     and [`cluster.SpectralBiclustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering "sklearn.cluster.SpectralBiclustering")
     is deprecated. They now use OpenMP based parallelism. For more details on how to control the number of threads, please refer to our [Parallelism](https://scikit-learn.org/stable/computing/parallelism.html#parallelism)
     notes. [#11950](https://github.com/scikit-learn/scikit-learn/pull/11950)
     by [Jeremie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   API Change The `precompute_distances` parameter of [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     is deprecated. It has no effect. [#11950](https://github.com/scikit-learn/scikit-learn/pull/11950)
     by [Jeremie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   API Change The `random_state` parameter has been added to [`cluster.AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
    . [#16801](https://github.com/scikit-learn/scikit-learn/pull/16801)
     by [@rcwoolston](https://github.com/rcwoolston)
     and [Chiara Marmo](https://github.com/cmarmo)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-compose "Link to this heading")

*   Efficiency [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     is now faster when working with dataframes and strings are used to specific subsets of data for transformers. [#16431](https://github.com/scikit-learn/scikit-learn/pull/16431)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     method `get_feature_names` now supports `'passthrough'` columns, with the feature name being either the column name for a dataframe, or `'xi'` for column index `i`. [#14048](https://github.com/scikit-learn/scikit-learn/pull/14048)
     by [Lewis Ball](https://github.com/lrjball)
    .
    
*   Fix [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     method `get_feature_names` now returns correct results when one of the transformer steps applies on an empty list of columns [#15963](https://github.com/scikit-learn/scikit-learn/pull/15963)
     by [Roman Yurchak](https://github.com/rth)
    .
    
*   Fix [`compose.ColumnTransformer.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer.fit "sklearn.compose.ColumnTransformer.fit")
     will error when selecting a column name that is not unique in the dataframe. [#16431](https://github.com/scikit-learn/scikit-learn/pull/16431)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-datasets "Link to this heading")

*   Efficiency [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     has reduced memory usage because it no longer stores the full dataset text stream in memory. [#16084](https://github.com/scikit-learn/scikit-learn/pull/16084)
     by [Joel Nothman](https://joelnothman.com/)
    .
    
*   Feature [`datasets.fetch_california_housing`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")
     now supports heterogeneous data using pandas by setting `as_frame=True`. [#15950](https://github.com/scikit-learn/scikit-learn/pull/15950)
     by [Stephanie Andrews](https://github.com/gitsteph)
     and [Reshama Shaikh](https://github.com/reshamas)
    .
    
*   Feature embedded dataset loaders [`datasets.load_breast_cancer`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer "sklearn.datasets.load_breast_cancer")
    , [`datasets.load_diabetes`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
    , [`datasets.load_digits`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
    , [`datasets.load_iris`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
    , [`datasets.load_linnerud`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html#sklearn.datasets.load_linnerud "sklearn.datasets.load_linnerud")
     and [`datasets.load_wine`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine "sklearn.datasets.load_wine")
     now support loading as a pandas `DataFrame` by setting `as_frame=True`. [#15980](https://github.com/scikit-learn/scikit-learn/pull/15980)
     by [@wconnell](https://github.com/wconnell)
     and [Reshama Shaikh](https://github.com/reshamas)
    .
    
*   Enhancement Added `return_centers` parameter in [`datasets.make_blobs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
    , which can be used to return centers for each cluster. [#15709](https://github.com/scikit-learn/scikit-learn/pull/15709)
     by [@shivamgargsya](https://github.com/shivamgargsya)
     and [Venkatachalam N](https://github.com/venkyyuvy)
    .
    
*   Enhancement Functions [`datasets.make_circles`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
     and [`datasets.make_moons`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")
     now accept two-element tuple. [#15707](https://github.com/scikit-learn/scikit-learn/pull/15707)
     by [Maciej J Mikulski](https://github.com/mjmikulski)
    .
    
*   Fix [`datasets.make_multilabel_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "sklearn.datasets.make_multilabel_classification")
     now generates `ValueError` for arguments `n_classes < 1` OR `length < 1`. [#16006](https://github.com/scikit-learn/scikit-learn/pull/16006)
     by [Rushabh Vasani](https://github.com/rushabh-v)
    .
    
*   API Change The `StreamHandler` was removed from `sklearn.logger` to avoid double logging of messages in common cases where a handler is attached to the root logger, and to follow the Python logging documentation recommendation for libraries to leave the log message handling to users and application code. [#16451](https://github.com/scikit-learn/scikit-learn/pull/16451)
     by [Christoph Deil](https://github.com/cdeil)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#id6 "Link to this heading")

*   Enhancement [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     and [`decomposition.non_negative_factorization`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.non_negative_factorization.html#sklearn.decomposition.non_negative_factorization "sklearn.decomposition.non_negative_factorization")
     now preserves float32 dtype. [#16280](https://github.com/scikit-learn/scikit-learn/pull/16280)
     by [Jeremie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Enhancement [`decomposition.TruncatedSVD.transform`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD.transform "sklearn.decomposition.TruncatedSVD.transform")
     is now faster on given sparse `csc` matrices. [#16837](https://github.com/scikit-learn/scikit-learn/pull/16837)
     by [@wornbb](https://github.com/wornbb)
    .
    
*   Fix [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     with a float `n_components` parameter, will exclusively choose the components that explain the variance greater than `n_components`. [#15669](https://github.com/scikit-learn/scikit-learn/pull/15669)
     by [Krishna Chaitanya](https://github.com/krishnachaitanya9)
    
*   Fix [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     with `n_components='mle'` now correctly handles small eigenvalues, and does not infer 0 as the correct number of components. [#16224](https://github.com/scikit-learn/scikit-learn/pull/16224)
     by [Lisa Schwetlick](https://github.com/lschwetlick)
    , and [Gelavizh Ahmadi](https://github.com/gelavizh1)
     and [Marija Vlajic Wheeler](https://github.com/marijavlajic)
     and [#16841](https://github.com/scikit-learn/scikit-learn/pull/16841)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
     method `inverse_transform` now applies the correct inverse transform to the transformed data. [#16655](https://github.com/scikit-learn/scikit-learn/pull/16655)
     by [Lewis Ball](https://github.com/lrjball)
    .
    
*   Fix Fixed bug that was causing [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
     to sometimes raise `invalid value encountered in multiply` during `fit`. [#16718](https://github.com/scikit-learn/scikit-learn/pull/16718)
     by [Gui Miotto](https://github.com/gui-miotto)
    .
    
*   Feature Added `n_components_` attribute to [`decomposition.SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")
     and [`decomposition.MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")
    . [#16981](https://github.com/scikit-learn/scikit-learn/pull/16981)
     by [Mateusz Górski](https://github.com/Reksbril)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#id7 "Link to this heading")

*   Major Feature [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     now support [sample\_weight](https://scikit-learn.org/stable/glossary.html#term-sample_weight)
    . [#14696](https://github.com/scikit-learn/scikit-learn/pull/14696)
     by [Adrin Jalali](https://github.com/adrinjalali)
     and [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Feature Early stopping in [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     is now determined with a new `early_stopping` parameter instead of `n_iter_no_change`. Default value is ‘auto’, which enables early stopping if there are at least 10,000 samples in the training set. [#14516](https://github.com/scikit-learn/scikit-learn/pull/14516)
     by [Johann Faouzi](https://github.com/johannfaouzi)
    .
    
*   Major Feature [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     now support monotonic constraints, useful when features are supposed to have a positive/negative effect on the target. [#15582](https://github.com/scikit-learn/scikit-learn/pull/15582)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   API Change Added boolean `verbose` flag to classes: [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     and [`ensemble.VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
    . [#16069](https://github.com/scikit-learn/scikit-learn/pull/16069)
     by [Sam Bail](https://github.com/spbail)
    , [Hanna Bruce MacDonald](https://github.com/hannahbrucemacdonald)
    , [Reshama Shaikh](https://github.com/reshamas)
    , and [Chiara Marmo](https://github.com/cmarmo)
    .
    
*   API Change Fixed a bug in [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     that would not respect the `max_leaf_nodes` parameter if the criteria was reached at the same time as the `max_depth` criteria. [#16183](https://github.com/scikit-learn/scikit-learn/pull/16183)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix Changed the convention for `max_depth` parameter of [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
    . The depth now corresponds to the number of edges to go from the root to the deepest leaf. Stumps (trees with one split) are now allowed. [#16182](https://github.com/scikit-learn/scikit-learn/pull/16182)
     by [Santhosh B](https://github.com/santhoshbala18)
    
*   Fix Fixed a bug in [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
    , [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
     and [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     where the attribute `estimators_samples_` did not generate the proper indices used during `fit`. [#16437](https://github.com/scikit-learn/scikit-learn/pull/16437)
     by [Jin-Hwan CHO](https://github.com/chofchof)
    .
    
*   Fix Fixed a bug in [`ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
     and [`ensemble.StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
     where the `sample_weight` argument was not being passed to `cross_val_predict` when evaluating the base estimators on cross-validation folds to obtain the input to the meta estimator. [#16539](https://github.com/scikit-learn/scikit-learn/pull/16539)
     by [Bill DeRose](https://github.com/wderose)
    .
    
*   Feature Added additional option `loss="poisson"` to [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
    , which adds Poisson deviance with log-link useful for modeling count data. [#16692](https://github.com/scikit-learn/scikit-learn/pull/16692)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    
*   Fix Fixed a bug where [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     and [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     would fail with multiple calls to fit when `warm_start=True`, `early_stopping=True`, and there is no validation set. [#16663](https://github.com/scikit-learn/scikit-learn/pull/16663)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#id8 "Link to this heading")

*   Efficiency [`feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     now sorts features after pruning them by document frequency. This improves performances for datasets with large vocabularies combined with `min_df` or `max_df`. [#15834](https://github.com/scikit-learn/scikit-learn/pull/15834)
     by [Santiago M. Mola](https://github.com/smola)
    .
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-feature-selection "Link to this heading")

*   Enhancement Added support for multioutput data in [`feature_selection.RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
     and [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
    . [#16103](https://github.com/scikit-learn/scikit-learn/pull/16103)
     by [Divyaprabha M](https://github.com/divyaprabha123)
    .
    
*   API Change Adds [`feature_selection.SelectorMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html#sklearn.feature_selection.SelectorMixin "sklearn.feature_selection.SelectorMixin")
     back to public API. [#16132](https://github.com/scikit-learn/scikit-learn/pull/16132)
     by [@trimeta](https://github.com/trimeta)
    .
    

#### [`sklearn.gaussian_process`](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#module-sklearn.gaussian_process "sklearn.gaussian_process")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-gaussian-process "Link to this heading")

*   Enhancement [`gaussian_process.kernels.Matern`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern "sklearn.gaussian_process.kernels.Matern")
     returns the RBF kernel when `nu=np.inf`. [#15503](https://github.com/scikit-learn/scikit-learn/pull/15503)
     by [Sam Dixon](https://github.com/sam-dixon)
    .
    
*   Fix Fixed bug in [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
     that caused predicted standard deviations to only be between 0 and 1 when WhiteKernel is not used. [#15782](https://github.com/scikit-learn/scikit-learn/pull/15782)
     by [@plgreenLIRU](https://github.com/plgreenLIRU)
    .
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-impute "Link to this heading")

*   Enhancement [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     accepts both scalar and array-like inputs for `max_value` and `min_value`. Array-like inputs allow a different max and min to be specified for each feature. [#16403](https://github.com/scikit-learn/scikit-learn/pull/16403)
     by [Narendra Mukherjee](https://github.com/narendramukherjee)
    .
    
*   Enhancement [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
    , [`impute.KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
    , and [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     accepts pandas’ nullable integer dtype with missing values. [#16508](https://github.com/scikit-learn/scikit-learn/pull/16508)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-inspection "Link to this heading")

*   Feature [`inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
     and `inspection.plot_partial_dependence` now support the fast ‘recursion’ method for [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
     and [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    . [#15864](https://github.com/scikit-learn/scikit-learn/pull/15864)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#id9 "Link to this heading")

*   Major Feature Added generalized linear models (GLM) with non normal error distributions, including [`linear_model.PoissonRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")
    , [`linear_model.GammaRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html#sklearn.linear_model.GammaRegressor "sklearn.linear_model.GammaRegressor")
     and [`linear_model.TweedieRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html#sklearn.linear_model.TweedieRegressor "sklearn.linear_model.TweedieRegressor")
     which use Poisson, Gamma and Tweedie distributions respectively. [#14300](https://github.com/scikit-learn/scikit-learn/pull/14300)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    , [Roman Yurchak](https://github.com/rth)
    , and [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Major Feature Support of `sample_weight` in [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     and [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     for dense feature matrix `X`. [#15436](https://github.com/scikit-learn/scikit-learn/pull/15436)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Efficiency [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     and [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
     now do not allocate a potentially large array to store dual coefficients for all hyperparameters during its `fit`, nor an array to store all error or LOO predictions unless `store_cv_values` is `True`. [#15652](https://github.com/scikit-learn/scikit-learn/pull/15652)
     by [Jérôme Dockès](https://github.com/jeromedockes)
    .
    
*   Enhancement [`linear_model.LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")
     and [`linear_model.Lars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html#sklearn.linear_model.Lars "sklearn.linear_model.Lars")
     now support a `jitter` parameter that adds random noise to the target. This might help with stability in some edge cases. [#15179](https://github.com/scikit-learn/scikit-learn/pull/15179)
     by [@angelaambroz](https://github.com/angelaambroz)
    .
    
*   Fix Fixed a bug where if a `sample_weight` parameter was passed to the fit method of [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
    , it would not be passed to the wrapped `base_estimator` during the fitting of the final model. [#15773](https://github.com/scikit-learn/scikit-learn/pull/15773)
     by [Jeremy Alexandre](https://github.com/J-A16)
    .
    
*   Fix Add `best_score_` attribute to [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     and [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
    . [#15655](https://github.com/scikit-learn/scikit-learn/pull/15655)
     by [Jérôme Dockès](https://github.com/jeromedockes)
    .
    
*   Fix Fixed a bug in [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
     to pass a specific scoring strategy. Before the internal estimator outputs score instead of predictions. [#14848](https://github.com/scikit-learn/scikit-learn/pull/14848)
     by [Venkatachalam N](https://github.com/venkyyuvy)
    .
    
*   Fix [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     will now avoid an unnecessary iteration when `solver='newton-cg'` by checking for inferior or equal instead of strictly inferior for maximum of `absgrad` and `tol` in `utils.optimize._newton_cg`. [#16266](https://github.com/scikit-learn/scikit-learn/pull/16266)
     by [Rushabh Vasani](https://github.com/rushabh-v)
    .
    
*   API Change Deprecated public attributes `standard_coef_`, `standard_intercept_`, `average_coef_`, and `average_intercept_` in [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    , [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
    , [`linear_model.PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier")
    , [`linear_model.PassiveAggressiveRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model.PassiveAggressiveRegressor")
    . [#16261](https://github.com/scikit-learn/scikit-learn/pull/16261)
     by [Carlos Brandt](https://github.com/chbrandt)
    .
    
*   Fix Efficiency [`linear_model.ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
     is more stable and much faster when `n_samples > n_features`. It can now scale to hundreds of thousands of samples. The stability fix might imply changes in the number of non-zero coefficients and in the predicted output. [#16849](https://github.com/scikit-learn/scikit-learn/pull/16849)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix Fixed a bug in [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    , [`linear_model.MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")
    , [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
     and [`linear_model.MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")
     where fitting would fail when using joblib loky backend. [#14264](https://github.com/scikit-learn/scikit-learn/pull/14264)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Efficiency Speed up [`linear_model.MultiTaskLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model.MultiTaskLasso")
    , [`linear_model.MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")
    , [`linear_model.MultiTaskElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html#sklearn.linear_model.MultiTaskElasticNet "sklearn.linear_model.MultiTaskElasticNet")
    , [`linear_model.MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")
     by avoiding slower BLAS Level 2 calls on small arrays [#17021](https://github.com/scikit-learn/scikit-learn/pull/17021)
     by [Alex Gramfort](https://github.com/agramfort)
     and [Mathurin Massias](https://github.com/mathurinm)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#id10 "Link to this heading")

*   Enhancement [`metrics.pairwise_distances_chunked`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html#sklearn.metrics.pairwise_distances_chunked "sklearn.metrics.pairwise_distances_chunked")
     now allows its `reduce_func` to not have a return value, enabling in-place operations. [#16397](https://github.com/scikit-learn/scikit-learn/pull/16397)
     by [Joel Nothman](https://joelnothman.com/)
    .
    
*   Fix Fixed a bug in [`metrics.mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
     to not ignore argument `squared` when argument `multioutput='raw_values'`. [#16323](https://github.com/scikit-learn/scikit-learn/pull/16323)
     by [Rushabh Vasani](https://github.com/rushabh-v)
    
*   Fix Fixed a bug in [`metrics.mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mutual_info_score.html#sklearn.metrics.mutual_info_score "sklearn.metrics.mutual_info_score")
     where negative scores could be returned. [#16362](https://github.com/scikit-learn/scikit-learn/pull/16362)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Fixed a bug in [`metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
     that would raise an error when `y_true` and `y_pred` were length zero and `labels` was not `None`. In addition, we raise an error when an empty list is given to the `labels` parameter. [#16442](https://github.com/scikit-learn/scikit-learn/pull/16442)
     by [Kyle Parsons](https://github.com/parsons-kyle-89)
    .
    
*   API Change Changed the formatting of values in [`metrics.ConfusionMatrixDisplay.plot`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.plot "sklearn.metrics.ConfusionMatrixDisplay.plot")
     and `metrics.plot_confusion_matrix` to pick the shorter format (either ‘2g’ or ‘d’). [#16159](https://github.com/scikit-learn/scikit-learn/pull/16159)
     by [Rick Mackenbach](https://github.com/Rick-Mackenbach)
     and [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change From version 0.25, [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     will no longer automatically compute the `VI` parameter for Mahalanobis distance and the `V` parameter for seuclidean distance if `Y` is passed. The user will be expected to compute this parameter on the training data of their choice and pass it to `pairwise_distances`. [#16993](https://github.com/scikit-learn/scikit-learn/pull/16993)
     by [Joel Nothman](https://joelnothman.com/)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-model-selection "Link to this heading")

*   Enhancement [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     yields stack trace information in fit failed warning messages in addition to previously emitted type and details. [#15622](https://github.com/scikit-learn/scikit-learn/pull/15622)
     by [Gregory Morse](https://github.com/GregoryMorse)
    .
    
*   Fix [`model_selection.cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
     supports `method="predict_proba"` when `y=None`. [#15918](https://github.com/scikit-learn/scikit-learn/pull/15918)
     by [Luca Kubin](https://github.com/lkubin)
    .
    
*   Fix `model_selection.fit_grid_point` is deprecated in 0.23 and will be removed in 0.25. [#16401](https://github.com/scikit-learn/scikit-learn/pull/16401)
     by [Arie Pratama Sutiono](https://github.com/ariepratama)
    

#### [`sklearn.multioutput`](https://scikit-learn.org/stable/api/sklearn.multioutput.html#module-sklearn.multioutput "sklearn.multioutput")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-multioutput "Link to this heading")

*   Feature [`multioutput.MultiOutputRegressor.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor.fit "sklearn.multioutput.MultiOutputRegressor.fit")
     and [`multioutput.MultiOutputClassifier.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.fit "sklearn.multioutput.MultiOutputClassifier.fit")
     now can accept `fit_params` to pass to the `estimator.fit` method of each step. [#15953](https://github.com/scikit-learn/scikit-learn/issues/15953)
     [#15959](https://github.com/scikit-learn/scikit-learn/pull/15959)
     by [Ke Huang](https://github.com/huangk10)
    .
    
*   Enhancement [`multioutput.RegressorChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.RegressorChain.html#sklearn.multioutput.RegressorChain "sklearn.multioutput.RegressorChain")
     now supports `fit_params` for `base_estimator` during `fit`. [#16111](https://github.com/scikit-learn/scikit-learn/pull/16111)
     by [Venkatachalam N](https://github.com/venkyyuvy)
    .
    

#### [`sklearn.naive_bayes`](https://scikit-learn.org/stable/api/sklearn.naive_bayes.html#module-sklearn.naive_bayes "sklearn.naive_bayes")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-naive-bayes "Link to this heading")

*   Fix A correctly formatted error message is shown in [`naive_bayes.CategoricalNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html#sklearn.naive_bayes.CategoricalNB "sklearn.naive_bayes.CategoricalNB")
     when the number of features in the input differs between `predict` and `fit`. [#16090](https://github.com/scikit-learn/scikit-learn/pull/16090)
     by [Madhura Jayaratne](https://github.com/madhuracj)
    .
    

#### [`sklearn.neural_network`](https://scikit-learn.org/stable/api/sklearn.neural_network.html#module-sklearn.neural_network "sklearn.neural_network")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-neural-network "Link to this heading")

*   Efficiency [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     and [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
     has reduced memory footprint when using stochastic solvers, `'sgd'` or `'adam'`, and `shuffle=True`. [#14075](https://github.com/scikit-learn/scikit-learn/pull/14075)
     by [@meyer89](https://github.com/meyer89)
    .
    
*   Fix Increases the numerical stability of the logistic loss function in [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     by clipping the probabilities. [#16117](https://github.com/scikit-learn/scikit-learn/pull/16117)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#id11 "Link to this heading")

*   Enhancement [`inspection.PartialDependenceDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "sklearn.inspection.PartialDependenceDisplay")
     now exposes the deciles lines as attributes so they can be hidden or customized. [#15785](https://github.com/scikit-learn/scikit-learn/pull/15785)
     by [Nicolas Hug](https://github.com/NicolasHug)
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-preprocessing "Link to this heading")

*   Feature argument `drop` of [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     will now accept value ‘if\_binary’ and will drop the first category of each feature with two categories. [#16245](https://github.com/scikit-learn/scikit-learn/pull/16245)
     by [Rushabh Vasani](https://github.com/rushabh-v)
    .
    
*   Enhancement [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
    ’s `drop_idx_` ndarray can now contain `None`, where `drop_idx_[i] = None` means that no category is dropped for index `i`. [#16585](https://github.com/scikit-learn/scikit-learn/pull/16585)
     by [Chiara Marmo](https://github.com/cmarmo)
    .
    
*   Enhancement [`preprocessing.MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")
    , [`preprocessing.MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
    , [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
    , [`preprocessing.PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
    , [`preprocessing.QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
    , [`preprocessing.RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
     now supports pandas’ nullable integer dtype with missing values. [#16508](https://github.com/scikit-learn/scikit-learn/pull/16508)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Efficiency [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     is now faster at transforming. [#15762](https://github.com/scikit-learn/scikit-learn/pull/15762)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Fix a bug in [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
     which was incorrectly computing statistics when calling `partial_fit` on sparse inputs. [#16466](https://github.com/scikit-learn/scikit-learn/pull/16466)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Fix a bug in [`preprocessing.Normalizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer")
     with norm=’max’, which was not taking the absolute value of the maximum values before normalizing the vectors. [#16632](https://github.com/scikit-learn/scikit-learn/pull/16632)
     by [Maura Pintor](https://github.com/Maupin1991)
     and [Battista Biggio](https://github.com/bbiggio)
    .
    

#### [`sklearn.semi_supervised`](https://scikit-learn.org/stable/api/sklearn.semi_supervised.html#module-sklearn.semi_supervised "sklearn.semi_supervised")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-semi-supervised "Link to this heading")

*   Fix [`semi_supervised.LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
     and [`semi_supervised.LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")
     avoids divide by zero warnings when normalizing `label_distributions_`. [#15946](https://github.com/scikit-learn/scikit-learn/pull/15946)
     by [@ngshya](https://github.com/ngshya)
    .
    

#### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-svm "Link to this heading")

*   Fix Efficiency Improved `libsvm` and `liblinear` random number generators used to randomly select coordinates in the coordinate descent algorithms. Platform-dependent C `rand()` was used, which is only able to generate numbers up to `32767` on windows platform (see this [blog post](https://codeforces.com/blog/entry/61587)
    ) and also has poor randomization power as suggested by [this presentation](https://channel9.msdn.com/Events/GoingNative/2013/rand-Considered-Harmful)
    . It was replaced with C++11 `mt19937`, a Mersenne Twister that correctly generates 31bits/63bits random numbers on all platforms. In addition, the crude “modulo” postprocessor used to get a random number in a bounded interval was replaced by the tweaked Lemire method as suggested by [this blog post](https://www.pcg-random.org/posts/bounded-rands.html)
    . Any model using the `svm.libsvm` or the `svm.liblinear` solver, including [`svm.LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
    , [`svm.LinearSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR "sklearn.svm.LinearSVR")
    , [`svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
    , [`svm.NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
    , [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
    , [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
    , [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
    , [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    , is affected. In particular users can expect a better convergence when the number of samples (LibSVM) or the number of features (LibLinear) is large. [#13511](https://github.com/scikit-learn/scikit-learn/pull/13511)
     by [Sylvain Marié](https://github.com/smarie)
    .
    
*   Fix Fix use of custom kernel not taking float entries such as string kernels in [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     and [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
    . Note that custom kernels are now expected to validate their input where they previously received valid numeric arrays. [#11296](https://github.com/scikit-learn/scikit-learn/pull/11296)
     by [Alexandre Gramfort](https://alexandre.gramfort.net/)
     and [Georgi Peev](https://github.com/georgipeev)
    .
    
*   API Change [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
     and [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
     attributes, `probA_` and `probB_`, are now deprecated as they were not useful. [#15558](https://github.com/scikit-learn/scikit-learn/pull/15558)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#sklearn-tree "Link to this heading")

*   Fix [`tree.plot_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree")
     `rotate` parameter was unused and has been deprecated. [#15806](https://github.com/scikit-learn/scikit-learn/pull/15806)
     by [Chiara Marmo](https://github.com/cmarmo)
    .
    
*   Fix Fix support of read-only float32 array input in `predict`, `decision_path` and `predict_proba` methods of [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
     and [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     as well as `predict` method of [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
    , and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
    . [#16331](https://github.com/scikit-learn/scikit-learn/pull/16331)
     by [Alexandre Batisse](https://github.com/batalex)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v0.23.html#id12 "Link to this heading")

*   Major Feature Estimators can now be displayed with a rich html representation. This can be enabled in Jupyter notebooks by setting `display='diagram'` in [`set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
    . The raw html can be returned by using [`utils.estimator_html_repr`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_html_repr.html#sklearn.utils.estimator_html_repr "sklearn.utils.estimator_html_repr")
    . [#14180](https://github.com/scikit-learn/scikit-learn/pull/14180)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement improve error message in [`utils.validation.column_or_1d`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.column_or_1d.html#sklearn.utils.validation.column_or_1d "sklearn.utils.validation.column_or_1d")
    . [#15926](https://github.com/scikit-learn/scikit-learn/pull/15926)
     by [Loïc Estève](https://github.com/lesteve)
    .
    
*   Enhancement add warning in [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     for pandas sparse DataFrame. [#16021](https://github.com/scikit-learn/scikit-learn/pull/16021)
     by [Rushabh Vasani](https://github.com/rushabh-v)
    .
    
*   Enhancement [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     now constructs a sparse matrix from a pandas DataFrame that contains only `SparseArray` columns. [#16728](https://github.com/scikit-learn/scikit-learn/pull/16728)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     supports pandas’ nullable integer dtype with missing values when `force_all_finite` is set to `False` or `'allow-nan'` in which case the data is converted to floating point values where `pd.NA` values are replaced by `np.nan`. As a consequence, all [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
     transformers that accept numeric inputs with missing values represented as `np.nan` now also accepts being directly fed pandas dataframes with ``pd.Int* or `pd.Uint*`` typed columns that use `pd.NA` as a missing value marker. [#16508](https://github.com/scikit-learn/scikit-learn/pull/16508)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change Passing classes to [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     and [`utils.estimator_checks.parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks")
     is now deprecated, and support for classes will be removed in 0.24. Pass instances instead. [#17032](https://github.com/scikit-learn/scikit-learn/pull/17032)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   API Change The private utility `_safe_tags` in `utils.estimator_checks` was removed, hence all tags should be obtained through `estimator._get_tags()`. Note that Mixins like `RegressorMixin` must come _before_ base classes in the MRO for `_get_tags()` to work properly. [#16950](https://github.com/scikit-learn/scikit-learn/pull/16950)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix `utils.all_estimators` now only returns public estimators. [#15380](https://github.com/scikit-learn/scikit-learn/pull/15380)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### Miscellaneous[#](https://scikit-learn.org/stable/whats_new/v0.23.html#id13 "Link to this heading")

*   Major Feature Adds a HTML representation of estimators to be shown in a jupyter notebook or lab. This visualization is activated by setting the `display` option in [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
    . [#14180](https://github.com/scikit-learn/scikit-learn/pull/14180)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement `scikit-learn` now works with `mypy` without errors. [#16726](https://github.com/scikit-learn/scikit-learn/pull/16726)
     by [Roman Yurchak](https://github.com/rth)
    .
    
*   API Change Most estimators now expose a `n_features_in_` attribute. This attribute is equal to the number of features passed to the `fit` method. See [SLEP010](https://scikit-learn-enhancement-proposals.readthedocs.io/en/latest/slep010/proposal.html)
     for details. [#16112](https://github.com/scikit-learn/scikit-learn/pull/16112)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   API Change Estimators now have a `requires_y` tags which is False by default except for estimators that inherit from `~sklearn.base.RegressorMixin` or `~sklearn.base.ClassifierMixin`. This tag is used to ensure that a proper error message is raised when y was expected but None was passed. [#16622](https://github.com/scikit-learn/scikit-learn/pull/16622)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   API Change The default setting `print_changed_only` has been changed from False to True. This means that the `repr` of estimators is now more concise and only shows the parameters whose default value has been changed when printing an estimator. You can restore the previous behaviour by using `sklearn.set_config(print_changed_only=False)`. Also, note that it is always possible to quickly inspect the parameters of any estimator using `est.get_params(deep=False)`. [#17061](https://github.com/scikit-learn/scikit-learn/pull/17061)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    

Code and documentation contributors

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 0.22, including:

Abbie Popa, Adrin Jalali, Aleksandra Kocot, Alexandre Batisse, Alexandre Gramfort, Alex Henrie, Alex Itkes, Alex Liang, alexshacked, Alonso Silva Allende, Ana Casado, Andreas Mueller, Angela Ambroz, Ankit810, Arie Pratama Sutiono, Arunav Konwar, Baptiste Maingret, Benjamin Beier Liu, bernie gray, Bharathi Srinivasan, Bharat Raghunathan, Bibhash Chandra Mitra, Brian Wignall, brigi, Brigitta Sipőcz, Carlos H Brandt, CastaChick, castor, cgsavard, Chiara Marmo, Chris Gregory, Christian Kastner, Christian Lorentzen, Corrie Bartelheimer, Daniël van Gelder, Daphne, David Breuer, david-cortes, dbauer9, Divyaprabha M, Edward Qian, Ekaterina Borovikova, ELNS, Emily Taylor, Erich Schubert, Eric Leung, Evgeni Chasnovski, Fabiana, Facundo Ferrín, Fan, Franziska Boenisch, Gael Varoquaux, Gaurav Sharma, Geoffrey Bolmier, Georgi Peev, gholdman1, Gonthier Nicolas, Gregory Morse, Gregory R. Lee, Guillaume Lemaitre, Gui Miotto, Hailey Nguyen, Hanmin Qin, Hao Chun Chang, HaoYin, Hélion du Mas des Bourboux, Himanshu Garg, Hirofumi Suzuki, huangk10, Hugo van Kemenade, Hye Sung Jung, indecisiveuser, inderjeet, J-A16, Jérémie du Boisberranger, Jin-Hwan CHO, JJmistry, Joel Nothman, Johann Faouzi, Jon Haitz Legarreta Gorroño, Juan Carlos Alfaro Jiménez, judithabk6, jumon, Kathryn Poole, Katrina Ni, Kesshi Jordan, Kevin Loftis, Kevin Markham, krishnachaitanya9, Lam Gia Thuan, Leland McInnes, Lisa Schwetlick, lkubin, Loic Esteve, lopusz, lrjball, lucgiffon, lucyleeow, Lucy Liu, Lukas Kemkes, Maciej J Mikulski, Madhura Jayaratne, Magda Zielinska, maikia, Mandy Gu, Manimaran, Manish Aradwad, Maren Westermann, Maria, Mariana Meireles, Marie Douriez, Marielle, Mateusz Górski, mathurinm, Matt Hall, Maura Pintor, mc4229, meyer89, m.fab, Michael Shoemaker, Michał Słapek, Mina Naghshhnejad, mo, Mohamed Maskani, Mojca Bertoncelj, narendramukherjee, ngshya, Nicholas Won, Nicolas Hug, nicolasservel, Niklas, @nkish, Noa Tamir, Oleksandr Pavlyk, olicairns, Oliver Urs Lenz, Olivier Grisel, parsons-kyle-89, Paula, Pete Green, Pierre Delanoue, pspachtholz, Pulkit Mehta, Qizhi Jiang, Quang Nguyen, rachelcjordan, raduspaimoc, Reshama Shaikh, Riccardo Folloni, Rick Mackenbach, Ritchie Ng, Roman Feldbauer, Roman Yurchak, Rory Hartong-Redden, Rüdiger Busche, Rushabh Vasani, Sambhav Kothari, Samesh Lakhotia, Samuel Duan, SanthoshBala18, Santiago M. Mola, Sarat Addepalli, scibol, Sebastian Kießling, SergioDSR, Sergul Aydore, Shiki-H, shivamgargsya, SHUBH CHATTERJEE, Siddharth Gupta, simonamaggio, smarie, Snowhite, stareh, Stephen Blystone, Stephen Marsh, Sunmi Yoon, SylvainLan, talgatomarov, tamirlan1, th0rwas, theoptips, Thomas J Fan, Thomas Li, Thomas Schmitt, Tim Nonner, Tim Vink, Tiphaine Viard, Tirth Patel, Titus Christian, Tom Dupré la Tour, trimeta, Vachan D A, Vandana Iyer, Venkatachalam N, waelbenamara, wconnell, wderose, wenliwyan, Windber, wornbb, Yu-Hang “Maxin” Tang

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)