[Skip to main content](https://scikit-learn.org/stable/whats_new/v0.21.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v0.21.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v0.21.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v0.21.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v0.21.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v0.21.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v0.21.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v0.21.html)

Collapse Sidebar Expand Sidebar

Version 0.21[#](https://scikit-learn.org/stable/whats_new/v0.21.html#version-0-21 "Link to this heading")

==========================================================================================================

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 0.21.3[#](https://scikit-learn.org/stable/whats_new/v0.21.html#version-0-21-3 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**July 30, 2019**

### Changed models[#](https://scikit-learn.org/stable/whats_new/v0.21.html#changed-models "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   The v0.20.0 release notes failed to mention a backwards incompatibility in [`metrics.make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
     when `needs_proba=True` and `y_true` is binary. Now, the scorer function is supposed to accept a 1D `y_pred` (i.e., probability of the positive class, shape `(n_samples,)`), instead of a 2D `y_pred` (i.e., shape `(n_samples, 2)`).
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.21.html#changelog "Link to this heading")

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-cluster "Link to this heading")

*   Fix Fixed a bug in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     where computation with `init='random'` was single threaded for `n_jobs > 1` or `n_jobs = -1`. [#12955](https://github.com/scikit-learn/scikit-learn/pull/12955)
     by [Prabakaran Kumaresshan](https://github.com/nixphix)
    .
    
*   Fix Fixed a bug in [`cluster.OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
     where users were unable to pass float `min_samples` and `min_cluster_size`. [#14496](https://github.com/scikit-learn/scikit-learn/pull/14496)
     by [Fabian Klopfer](https://github.com/someusername1)
     and [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   Fix Fixed a bug in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     where KMeans++ initialisation could rarely result in an IndexError. [#11756](https://github.com/scikit-learn/scikit-learn/issues/11756)
     by [Joel Nothman](https://joelnothman.com/)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-compose "Link to this heading")

*   Fix Fixed an issue in [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     where using DataFrames whose column order differs between `fit` and `transform` could lead to silently passing incorrect columns to the `remainder` transformer. [#14237](https://github.com/scikit-learn/scikit-learn/pull/14237)
     by `Andreas Schuderer <schuderer>`.
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-datasets "Link to this heading")

*   Fix [`datasets.fetch_california_housing`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")
    , [`datasets.fetch_covtype`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#sklearn.datasets.fetch_covtype "sklearn.datasets.fetch_covtype")
    , [`datasets.fetch_kddcup99`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99 "sklearn.datasets.fetch_kddcup99")
    , [`datasets.fetch_olivetti_faces`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#sklearn.datasets.fetch_olivetti_faces "sklearn.datasets.fetch_olivetti_faces")
    , [`datasets.fetch_rcv1`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_rcv1.html#sklearn.datasets.fetch_rcv1 "sklearn.datasets.fetch_rcv1")
    , and [`datasets.fetch_species_distributions`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_species_distributions.html#sklearn.datasets.fetch_species_distributions "sklearn.datasets.fetch_species_distributions")
     try to persist the previously cache using the new `joblib` if the cached data was persisted using the deprecated `sklearn.externals.joblib`. This behavior is set to be deprecated and removed in v0.23. [#14197](https://github.com/scikit-learn/scikit-learn/pull/14197)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-ensemble "Link to this heading")

*   Fix Fix zero division error in [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
    . [#14024](https://github.com/scikit-learn/scikit-learn/pull/14024)
     by `Nicolas Hug <NicolasHug>`.
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-impute "Link to this heading")

*   Fix Fixed a bug in [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     and [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     so that no errors are thrown when there are missing values in training data. [#13974](https://github.com/scikit-learn/scikit-learn/pull/13974)
     by `Frank Hoang <fhoang7>`.
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-inspection "Link to this heading")

*   Fix Fixed a bug in `inspection.plot_partial_dependence` where `target` parameter was not being taken into account for multiclass problems. [#14393](https://github.com/scikit-learn/scikit-learn/pull/14393)
     by [Guillem G. Subies](https://github.com/guillemgsubies)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-linear-model "Link to this heading")

*   Fix Fixed a bug in [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     where `refit=False` would fail depending on the `'multiclass'` and `'penalty'` parameters (regression introduced in 0.21). [#14087](https://github.com/scikit-learn/scikit-learn/pull/14087)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix Compatibility fix for [`linear_model.ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
     and Scipy>=1.3.0. Adapts to upstream changes to the default `pinvh` cutoff threshold which otherwise results in poor accuracy in some cases. [#14067](https://github.com/scikit-learn/scikit-learn/pull/14067)
     by [Tim Staley](https://github.com/timstaley)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-neighbors "Link to this heading")

*   Fix Fixed a bug in [`neighbors.NeighborhoodComponentsAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis")
     where the validation of initial parameters `n_components`, `max_iter` and `tol` required too strict types. [#14092](https://github.com/scikit-learn/scikit-learn/pull/14092)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-tree "Link to this heading")

*   Fix Fixed bug in [`tree.export_text`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html#sklearn.tree.export_text "sklearn.tree.export_text")
     when the tree has one feature and a single feature name is passed in. [#14053](https://github.com/scikit-learn/scikit-learn/pull/14053)
     by `Thomas Fan`.
    
*   Fix Fixed an issue with [`tree.plot_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree")
     where it displayed entropy calculations even for `gini` criterion in DecisionTreeClassifiers. [#13947](https://github.com/scikit-learn/scikit-learn/pull/13947)
     by [Frank Hoang](https://github.com/fhoang7)
    .
    

Version 0.21.2[#](https://scikit-learn.org/stable/whats_new/v0.21.html#version-0-21-2 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**24 May 2019**

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id1 "Link to this heading")

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-decomposition "Link to this heading")

*   Fix Fixed a bug in [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
     improving numerical stability when `Y` is close to zero. [#13903](https://github.com/scikit-learn/scikit-learn/pull/13903)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-metrics "Link to this heading")

*   Fix Fixed a bug in [`metrics.pairwise.euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html#sklearn.metrics.pairwise.euclidean_distances "sklearn.metrics.pairwise.euclidean_distances")
     where a part of the distance matrix was left un-instanciated for sufficiently large float32 datasets (regression introduced in 0.21). [#13910](https://github.com/scikit-learn/scikit-learn/pull/13910)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-preprocessing "Link to this heading")

*   Fix Fixed a bug in [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     where the new `drop` parameter was not reflected in `get_feature_names`. [#13894](https://github.com/scikit-learn/scikit-learn/pull/13894)
     by [James Myatt](https://github.com/jamesmyatt)
    .
    

#### `sklearn.utils.sparsefuncs`[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-utils-sparsefuncs "Link to this heading")

*   Fix Fixed a bug where `min_max_axis` would fail on 32-bit systems for certain large inputs. This affects [`preprocessing.MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")
    , [`preprocessing.normalize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html#sklearn.preprocessing.normalize "sklearn.preprocessing.normalize")
     and [`preprocessing.LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
    . [#13741](https://github.com/scikit-learn/scikit-learn/pull/13741)
     by [Roddy MacSween](https://github.com/rlms)
    .
    

Version 0.21.1[#](https://scikit-learn.org/stable/whats_new/v0.21.html#version-0-21-1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**17 May 2019**

This is a bug-fix release to primarily resolve some packaging issues in version 0.21.0. It also includes minor documentation improvements and some bug fixes.

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id2 "Link to this heading")

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id3 "Link to this heading")

*   Fix Fixed a bug in [`inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
     to only check classifier and not regressor for the multiclass-multioutput case. [#14309](https://github.com/scikit-learn/scikit-learn/pull/14309)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id4 "Link to this heading")

*   Fix Fixed a bug in [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     where it would raise `AttributeError` for boolean metrics when `X` had a boolean dtype and `Y == None`. [#13864](https://github.com/scikit-learn/scikit-learn/issues/13864)
     by [Paresh Mathur](https://github.com/rick2047)
    .
    
*   Fix Fixed two bugs in [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     when `n_jobs > 1`. First it used to return a distance matrix with same dtype as input, even for integer dtype. Then the diagonal was not zeros for euclidean metric when `Y` is `X`. [#13877](https://github.com/scikit-learn/scikit-learn/issues/13877)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id5 "Link to this heading")

*   Fix Fixed a bug in [`neighbors.KernelDensity`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
     which could not be restored from a pickle if `sample_weight` had been used. [#13772](https://github.com/scikit-learn/scikit-learn/issues/13772)
     by [Aditya Vyas](https://github.com/aditya1702)
    .
    

Version 0.21.0[#](https://scikit-learn.org/stable/whats_new/v0.21.html#version-0-21-0 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**May 2019**

### Changed models[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id6 "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     for multiclass classification. Fix
    
*   [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     with ‘eigen’ solver. Fix
    
*   [`linear_model.BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
     Fix
    
*   Decision trees and derived ensembles when both `max_depth` and `max_leaf_nodes` are set. Fix
    
*   [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     with ‘saga’ solver. Fix
    
*   [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     Fix
    
*   [`sklearn.feature_extraction.text.HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
    , [`sklearn.feature_extraction.text.TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
    , and [`sklearn.feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     Fix
    
*   [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     Fix
    
*   [`svm.SVC.decision_function`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.decision_function "sklearn.svm.SVC.decision_function")
     and [`multiclass.OneVsOneClassifier.decision_function`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier.decision_function "sklearn.multiclass.OneVsOneClassifier.decision_function")
    . Fix
    
*   [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     and any derived classifiers. Fix
    
*   Any model using the `linear_model._sag.sag_solver` function with a `0` seed, including [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    , [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
    , [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    , and [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     with ‘sag’ solver. Fix
    
*   [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     when using leave-one-out cross-validation with sparse inputs. Fix
    

Details are listed in the changelog below.

(While we are trying to better inform users by providing this information, we cannot assure that this list is complete.)

### Known Major Bugs[#](https://scikit-learn.org/stable/whats_new/v0.21.html#known-major-bugs "Link to this heading")

*   The default `max_iter` for [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     is too small for many solvers given the default `tol`. In particular, we accidentally changed the default `max_iter` for the liblinear solver from 1000 to 100 iterations in [#3591](https://github.com/scikit-learn/scikit-learn/pull/3591)
     released in version 0.16. In a future release we hope to choose better default `max_iter` and `tol` heuristically depending on the solver (see [#13317](https://github.com/scikit-learn/scikit-learn/pull/13317)
    ).
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id7 "Link to this heading")

Support for Python 3.4 and below has been officially dropped.

#### [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-base "Link to this heading")

*   API Change The R2 score used when calling `score` on a regressor will use `multioutput='uniform_average'` from version 0.23 to keep consistent with [`metrics.r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
    . This will influence the `score` method of all the multioutput regressors (except for [`multioutput.MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")
    ). [#13157](https://github.com/scikit-learn/scikit-learn/pull/13157)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    

#### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-calibration "Link to this heading")

*   Enhancement Added support to bin the data passed into [`calibration.calibration_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html#sklearn.calibration.calibration_curve "sklearn.calibration.calibration_curve")
     by quantiles instead of uniformly between 0 and 1. [#13086](https://github.com/scikit-learn/scikit-learn/pull/13086)
     by [Scott Cole](https://github.com/srcole)
    .
    
*   Enhancement Allow n-dimensional arrays as input for `calibration.CalibratedClassifierCV`. [#13485](https://github.com/scikit-learn/scikit-learn/pull/13485)
     by [William de Vazelhes](https://github.com/wdevazelhes)
    .
    

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id8 "Link to this heading")

*   Major Feature A new clustering algorithm: [`cluster.OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
    : an algorithm related to [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
    , that has hyperparameters easier to set and that scales better, by [Shane](https://github.com/espg)
    , [Adrin Jalali](https://github.com/adrinjalali)
    , [Erich Schubert](https://github.com/kno10)
    , [Hanmin Qin](https://github.com/qinhanmin2014)
    , and [Assia Benbihi](https://github.com/assiaben)
    .
    
*   Fix Fixed a bug where [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
     could occasionally raise an AttributeError. [#13651](https://github.com/scikit-learn/scikit-learn/pull/13651)
     by [Joel Nothman](https://joelnothman.com/)
    .
    
*   Fix Fixed a bug in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     where empty clusters weren’t correctly relocated when using sample weights. [#13486](https://github.com/scikit-learn/scikit-learn/pull/13486)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   API Change The `n_components_` attribute in [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     and [`cluster.FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")
     has been renamed to `n_connected_components_`. [#13427](https://github.com/scikit-learn/scikit-learn/pull/13427)
     by [Stephane Couvreur](https://github.com/scouvreur)
    .
    
*   Enhancement [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     and [`cluster.FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")
     now accept a `distance_threshold` parameter which can be used to find the clusters instead of `n_clusters`. [#9069](https://github.com/scikit-learn/scikit-learn/issues/9069)
     by [Vathsala Achar](https://github.com/VathsalaAchar)
     and [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id9 "Link to this heading")

*   API Change [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     is no longer an experimental feature. [#13835](https://github.com/scikit-learn/scikit-learn/pull/13835)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id10 "Link to this heading")

*   Fix Added support for 64-bit group IDs and pointers in SVMLight files. [#10727](https://github.com/scikit-learn/scikit-learn/pull/10727)
     by [Bryan K Woods](https://github.com/bryan-woods)
    .
    
*   Fix [`datasets.load_sample_images`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_images.html#sklearn.datasets.load_sample_images "sklearn.datasets.load_sample_images")
     returns images with a deterministic order. [#13250](https://github.com/scikit-learn/scikit-learn/pull/13250)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id11 "Link to this heading")

*   Enhancement [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
     now has deterministic output (resolved sign ambiguity in eigenvalue decomposition of the kernel matrix). [#13241](https://github.com/scikit-learn/scikit-learn/pull/13241)
     by [Aurélien Bellet](https://github.com/bellet)
    .
    
*   Fix Fixed a bug in [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
    , `fit().transform()` now produces the correct output (the same as `fit_transform()`) in case of non-removed zero eigenvalues (`remove_zero_eig=False`). `fit_inverse_transform` was also accelerated by using the same trick as `fit_transform` to compute the transform of `X`. [#12143](https://github.com/scikit-learn/scikit-learn/pull/12143)
     by [Sylvain Marié](https://github.com/smarie)
    
*   Fix Fixed a bug in [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     where `init = 'nndsvd'`, `init = 'nndsvda'`, and `init = 'nndsvdar'` are allowed when `n_components < n_features` instead of `n_components <= min(n_samples, n_features)`. [#11650](https://github.com/scikit-learn/scikit-learn/pull/11650)
     by [Hossein Pourbozorg](https://github.com/hossein-pourbozorg)
     and [Zijie (ZJ) Poh](https://github.com/zjpoh)
    .
    
*   API Change The default value of the `init` argument in [`decomposition.non_negative_factorization`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.non_negative_factorization.html#sklearn.decomposition.non_negative_factorization "sklearn.decomposition.non_negative_factorization")
     will change from `random` to `None` in version 0.23 to make it consistent with [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
    . A FutureWarning is raised when the default value is used. [#12988](https://github.com/scikit-learn/scikit-learn/pull/12988)
     by [Zijie (ZJ) Poh](https://github.com/zjpoh)
    .
    

#### [`sklearn.discriminant_analysis`](https://scikit-learn.org/stable/api/sklearn.discriminant_analysis.html#module-sklearn.discriminant_analysis "sklearn.discriminant_analysis")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-discriminant-analysis "Link to this heading")

*   Enhancement [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     now preserves `float32` and `float64` dtypes. [#8769](https://github.com/scikit-learn/scikit-learn/pull/8769)
     and [#11000](https://github.com/scikit-learn/scikit-learn/pull/11000)
     by [Thibault Sejourne](https://github.com/thibsej)
    
*   Fix A `ChangedBehaviourWarning` is now raised when [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     is given as parameter `n_components > min(n_features, n_classes - 1)`, and `n_components` is changed to `min(n_features, n_classes - 1)` if so. Previously the change was made, but silently. [#11526](https://github.com/scikit-learn/scikit-learn/pull/11526)
     by [William de Vazelhes](https://github.com/wdevazelhes)
    .
    
*   Fix Fixed a bug in [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     where the predicted probabilities would be incorrectly computed in the multiclass case. [#6848](https://github.com/scikit-learn/scikit-learn/pull/6848)
    , by [Agamemnon Krasoulis](https://github.com/agamemnonc)
     and `Guillaume Lemaitre <glemaitre>`.
    
*   Fix Fixed a bug in [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     where the predicted probabilities would be incorrectly computed with `eigen` solver. [#11727](https://github.com/scikit-learn/scikit-learn/pull/11727)
    , by [Agamemnon Krasoulis](https://github.com/agamemnonc)
    .
    

#### [`sklearn.dummy`](https://scikit-learn.org/stable/api/sklearn.dummy.html#module-sklearn.dummy "sklearn.dummy")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-dummy "Link to this heading")

*   Fix Fixed a bug in [`dummy.DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
     where the `predict_proba` method was returning int32 array instead of float64 for the `stratified` strategy. [#13266](https://github.com/scikit-learn/scikit-learn/pull/13266)
     by [Christos Aridas](https://github.com/chkoar)
    .
    
*   Fix Fixed a bug in [`dummy.DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
     where it was throwing a dimension mismatch error in prediction time if a column vector `y` with `shape=(n, 1)` was given at `fit` time. [#13545](https://github.com/scikit-learn/scikit-learn/pull/13545)
     by [Nick Sorros](https://github.com/nsorros)
     and [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id12 "Link to this heading")

*   Major Feature Add two new implementations of gradient boosting trees: [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
    . The implementation of these estimators is inspired by [LightGBM](https://github.com/Microsoft/LightGBM)
     and can be orders of magnitude faster than [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     and [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     when the number of samples is larger than tens of thousands of samples. The API of these new estimators is slightly different, and some of the features from [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     are not yet supported.
    
    These new estimators are experimental, which means that their results or their API might change without any deprecation cycle. To use them, you need to explicitly import `enable_hist_gradient_boosting`:
    
    \>>> \# explicitly require this experimental feature
    \>>> from sklearn.experimental import enable\_hist\_gradient\_boosting  \# noqa
    \>>> \# now you can import normally from sklearn.ensemble
    \>>> from sklearn.ensemble import HistGradientBoostingClassifier
    
    Copy to clipboard
    
    Note
    
    Update: since version 1.0, these estimators are not experimental anymore and you don’t need to use `from sklearn.experimental import enable_hist_gradient_boosting`.
    
    [#12807](https://github.com/scikit-learn/scikit-learn/pull/12807)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Feature Add [`ensemble.VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
     which provides an equivalent of [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     for regression problems. [#12513](https://github.com/scikit-learn/scikit-learn/pull/12513)
     by [Ramil Nugmanov](https://github.com/stsouko)
     and [Mohamed Ali Jamaoui](https://github.com/mohamed-ali)
    .
    
*   Efficiency Make [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     prefer threads over processes when running with `n_jobs > 1` as the underlying decision tree fit calls do release the GIL. This change reduces memory usage and communication overhead. [#12543](https://github.com/scikit-learn/scikit-learn/pull/12543)
     by [Isaac Storch](https://github.com/istorch)
     and [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Efficiency Make [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     more memory efficient by avoiding keeping in memory each tree prediction. [#13260](https://github.com/scikit-learn/scikit-learn/pull/13260)
     by [Nicolas Goix](https://ngoix.github.io/)
    .
    
*   Efficiency [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     now uses chunks of data at prediction step, thus capping the memory usage. [#13283](https://github.com/scikit-learn/scikit-learn/pull/13283)
     by [Nicolas Goix](https://ngoix.github.io/)
    .
    
*   Efficiency [`sklearn.ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     and [`sklearn.ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     now keep the input `y` as `float64` to avoid it being copied internally by trees. [#13524](https://github.com/scikit-learn/scikit-learn/pull/13524)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Enhancement Minimized the validation of X in [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
     and [`ensemble.AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
     [#13174](https://github.com/scikit-learn/scikit-learn/pull/13174)
     by [Christos Aridas](https://github.com/chkoar)
    .
    
*   Enhancement [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     now exposes `warm_start` parameter, allowing iterative addition of trees to an isolation forest. [#13496](https://github.com/scikit-learn/scikit-learn/pull/13496)
     by [Peter Marko](https://github.com/petibear)
    .
    
*   Fix The values of `feature_importances_` in all random forest based models (i.e. [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
    , [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
    , [`ensemble.RandomTreesEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")
    , [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
    , and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
    ) now:
    
    *   sum up to `1`
        
    *   all the single node trees in feature importance calculation are ignored
        
    *   in case all trees have only one single node (i.e. a root node), feature importances will be an array of all zeros.
        
    
    [#13636](https://github.com/scikit-learn/scikit-learn/pull/13636)
     and [#13620](https://github.com/scikit-learn/scikit-learn/pull/13620)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Fix Fixed a bug in [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
    , which didn’t support scikit-learn estimators as the initial estimator. Also added support of initial estimator which does not support sample weights. [#12436](https://github.com/scikit-learn/scikit-learn/pull/12436)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
     and [#12983](https://github.com/scikit-learn/scikit-learn/pull/12983)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix Fixed the output of the average path length computed in [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     when the input is either 0, 1 or 2. [#13251](https://github.com/scikit-learn/scikit-learn/pull/13251)
     by [Albert Thomas](https://github.com/albertcthomas)
     and [joshuakennethjones](https://github.com/joshuakennethjones)
    .
    
*   Fix Fixed a bug in [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     where the gradients would be incorrectly computed in multiclass classification problems. [#12715](https://github.com/scikit-learn/scikit-learn/pull/12715)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix Fixed a bug in [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     where validation sets for early stopping were not sampled with stratification. [#13164](https://github.com/scikit-learn/scikit-learn/pull/13164)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix Fixed a bug in [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     where the default initial prediction of a multiclass classifier would predict the classes priors instead of the log of the priors. [#12983](https://github.com/scikit-learn/scikit-learn/pull/12983)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix Fixed a bug in [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
     where the `predict` method would error for multiclass multioutput forests models if any targets were strings. [#12834](https://github.com/scikit-learn/scikit-learn/pull/12834)
     by [Elizabeth Sander](https://github.com/elsander)
    .
    
*   Fix Fixed a bug in `ensemble.gradient_boosting.LossFunction` and `ensemble.gradient_boosting.LeastSquaresError` where the default value of `learning_rate` in `update_terminal_regions` is not consistent with the document and the caller functions. Note however that directly using these loss functions is deprecated. [#6463](https://github.com/scikit-learn/scikit-learn/pull/6463)
     by [movelikeriver](https://github.com/movelikeriver)
    .
    
*   Fix `ensemble.partial_dependence` (and consequently the new version [`sklearn.inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
    ) now takes sample weights into account for the partial dependence computation when the gradient boosting model has been trained with sample weights. [#13193](https://github.com/scikit-learn/scikit-learn/pull/13193)
     by [Samuel O. Ronsin](https://github.com/samronsin)
    .
    
*   API Change `ensemble.partial_dependence` and `ensemble.plot_partial_dependence` are now deprecated in favor of [`inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
     and `inspection.plot_partial_dependence<sklearn.inspection.plot_partial_dependence>`. [#12599](https://github.com/scikit-learn/scikit-learn/pull/12599)
     by [Trevor Stephens](https://github.com/trevorstephens)
     and [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     and [`ensemble.VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
     were failing during `fit` in one of the estimators was set to `None` and `sample_weight` was not `None`. [#13779](https://github.com/scikit-learn/scikit-learn/pull/13779)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     and [`ensemble.VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
     accept `'drop'` to disable an estimator in addition to `None` to be consistent with other estimators (i.e., [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     and [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
    ). [#13780](https://github.com/scikit-learn/scikit-learn/pull/13780)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### `sklearn.externals`[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-externals "Link to this heading")

*   API Change Deprecated `externals.six` since we have dropped support for Python 2.7. [#12916](https://github.com/scikit-learn/scikit-learn/pull/12916)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-feature-extraction "Link to this heading")

*   Fix If `input='file'` or `input='filename'`, and a callable is given as the `analyzer`, [`sklearn.feature_extraction.text.HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
    , [`sklearn.feature_extraction.text.TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
    , and [`sklearn.feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     now read the data from the file(s) and then pass it to the given `analyzer`, instead of passing the file name(s) or the file object(s) to the analyzer. [#13641](https://github.com/scikit-learn/scikit-learn/pull/13641)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id13 "Link to this heading")

*   Major Feature Added [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
    , which is a strategy for imputing missing values by modeling each feature with missing values as a function of other features in a round-robin fashion. [#8478](https://github.com/scikit-learn/scikit-learn/pull/8478)
     and [#12177](https://github.com/scikit-learn/scikit-learn/pull/12177)
     by [Sergey Feldman](https://github.com/sergeyf)
     and [Ben Lawson](https://github.com/benlawson)
    .
    
    The API of IterativeImputer is experimental and subject to change without any deprecation cycle. To use them, you need to explicitly import `enable_iterative_imputer`:
    
    \>>> from sklearn.experimental import enable\_iterative\_imputer  \# noqa
    \>>> \# now you can import normally from sklearn.impute
    \>>> from sklearn.impute import IterativeImputer
    
    Copy to clipboard
    
*   Feature The [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     and [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     have a new parameter `'add_indicator'`, which simply stacks a [`impute.MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")
     transform into the output of the imputer’s transform. That allows a predictive estimator to account for missingness. [#12583](https://github.com/scikit-learn/scikit-learn/pull/12583)
    , [#13601](https://github.com/scikit-learn/scikit-learn/pull/13601)
     by [Danylo Baibak](https://github.com/DanilBaibak)
    .
    
*   Fix In [`impute.MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")
     avoid implicit densification by raising an exception if input is sparse and `missing_values` property is set to 0. [#13240](https://github.com/scikit-learn/scikit-learn/pull/13240)
     by [Bartosz Telenczuk](https://github.com/btel)
    .
    
*   Fix Fixed two bugs in [`impute.MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")
    . First, when `X` is sparse, all the non-zero non missing values used to become explicit False in the transformed data. Then, when `features='missing-only'`, all features used to be kept if there were no missing values at all. [#13562](https://github.com/scikit-learn/scikit-learn/pull/13562)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id14 "Link to this heading")

(new subpackage)

*   Feature Partial dependence plots (`inspection.plot_partial_dependence`) are now supported for any regressor or classifier (provided that they have a `predict_proba` method). [#12599](https://github.com/scikit-learn/scikit-learn/pull/12599)
     by [Trevor Stephens](https://github.com/trevorstephens)
     and [Nicolas Hug](https://github.com/NicolasHug)
    .
    

#### [`sklearn.isotonic`](https://scikit-learn.org/stable/api/sklearn.isotonic.html#module-sklearn.isotonic "sklearn.isotonic")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-isotonic "Link to this heading")

*   Feature Allow different dtypes (such as float32) in [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
    . [#8769](https://github.com/scikit-learn/scikit-learn/pull/8769)
     by [Vlad Niculae](https://github.com/vene)
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id15 "Link to this heading")

*   Enhancement [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     now preserves `float32` and `float64` dtypes. [#8769](https://github.com/scikit-learn/scikit-learn/issues/8769)
     and [#11000](https://github.com/scikit-learn/scikit-learn/issues/11000)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    , and [Joan Massich](https://github.com/massich)
    
*   Feature [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     now support Elastic-Net penalty, with the ‘saga’ solver. [#11646](https://github.com/scikit-learn/scikit-learn/pull/11646)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Feature Added [`linear_model.lars_path_gram`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path_gram.html#sklearn.linear_model.lars_path_gram "sklearn.linear_model.lars_path_gram")
    , which is [`linear_model.lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")
     in the sufficient stats mode, allowing users to compute [`linear_model.lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")
     without providing `X` and `y`. [#11699](https://github.com/scikit-learn/scikit-learn/pull/11699)
     by [Kuai Yu](https://github.com/yukuairoy)
    .
    
*   Efficiency `linear_model.make_dataset` now preserves `float32` and `float64` dtypes, reducing memory consumption in stochastic gradient, SAG and SAGA solvers. [#8769](https://github.com/scikit-learn/scikit-learn/pull/8769)
     and [#11000](https://github.com/scikit-learn/scikit-learn/pull/11000)
     by [Nelle Varoquaux](https://github.com/NelleV)
    , [Arthur Imbert](https://github.com/Henley13)
    , [Guillaume Lemaitre](https://github.com/glemaitre)
    , and [Joan Massich](https://github.com/massich)
    
*   Enhancement [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     now supports an unregularized objective when `penalty='none'` is passed. This is equivalent to setting `C=np.inf` with l2 regularization. Not supported by the liblinear solver. [#12860](https://github.com/scikit-learn/scikit-learn/pull/12860)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Enhancement `sparse_cg` solver in [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     now supports fitting the intercept (i.e. `fit_intercept=True`) when inputs are sparse. [#13336](https://github.com/scikit-learn/scikit-learn/pull/13336)
     by [Bartosz Telenczuk](https://github.com/btel)
    .
    
*   Enhancement The coordinate descent solver used in `Lasso`, `ElasticNet`, etc. now issues a `ConvergenceWarning` when it completes without meeting the desired tolerance. [#11754](https://github.com/scikit-learn/scikit-learn/pull/11754)
     and [#13397](https://github.com/scikit-learn/scikit-learn/pull/13397)
     by [Brent Fagan](https://github.com/brentfagan)
     and [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Fix Fixed a bug in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     with ‘saga’ solver, where the weights would not be correctly updated in some cases. [#11646](https://github.com/scikit-learn/scikit-learn/pull/11646)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Fix Fixed the posterior mean, posterior covariance and returned regularization parameters in [`linear_model.BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
    . The posterior mean and the posterior covariance were not the ones computed with the last update of the regularization parameters and the returned regularization parameters were not the final ones. Also fixed the formula of the log marginal likelihood used to compute the score when `compute_score=True`. [#12174](https://github.com/scikit-learn/scikit-learn/pull/12174)
     by [Albert Thomas](https://github.com/albertcthomas)
    .
    
*   Fix Fixed a bug in [`linear_model.LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
    , where user input `copy_X=False` at instance creation would be overridden by default parameter value `copy_X=True` in `fit`. [#12972](https://github.com/scikit-learn/scikit-learn/pull/12972)
     by [Lucio Fernandez-Arjona](https://github.com/luk-f-a)
    
*   Fix Fixed a bug in [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
     that was not returning the same coefficients and intercepts with `fit_intercept=True` in sparse and dense case. [#13279](https://github.com/scikit-learn/scikit-learn/pull/13279)
     by [Alexandre Gramfort](https://alexandre.gramfort.net/)
    
*   Fix Fixed a bug in [`linear_model.HuberRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor")
     that was broken when `X` was of dtype bool. [#13328](https://github.com/scikit-learn/scikit-learn/pull/13328)
     by [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   Fix Fixed a performance issue of `saga` and `sag` solvers when called in a [`joblib.Parallel`](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html#joblib.Parallel "(in joblib v1.7)")
     setting with `n_jobs > 1` and `backend="threading"`, causing them to perform worse than in the sequential case. [#13389](https://github.com/scikit-learn/scikit-learn/pull/13389)
     by [Pierre Glaser](https://github.com/pierreglaser)
    .
    
*   Fix Fixed a bug in `linear_model.stochastic_gradient.BaseSGDClassifier` that was not deterministic when trained in a multi-class setting on several threads. [#13422](https://github.com/scikit-learn/scikit-learn/pull/13422)
     by [Clément Doumouro](https://github.com/ClemDoum)
    .
    
*   Fix Fixed bug in [`linear_model.ridge_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html#sklearn.linear_model.ridge_regression "sklearn.linear_model.ridge_regression")
    , [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     and [`linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
     that caused unhandled exception for arguments `return_intercept=True` and `solver=auto` (default) or any other solver different from `sag`. [#13363](https://github.com/scikit-learn/scikit-learn/pull/13363)
     by [Bartosz Telenczuk](https://github.com/btel)
    
*   Fix [`linear_model.ridge_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html#sklearn.linear_model.ridge_regression "sklearn.linear_model.ridge_regression")
     will now raise an exception if `return_intercept=True` and solver is different from `sag`. Previously, only warning was issued. [#13363](https://github.com/scikit-learn/scikit-learn/pull/13363)
     by [Bartosz Telenczuk](https://github.com/btel)
    
*   Fix [`linear_model.ridge_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html#sklearn.linear_model.ridge_regression "sklearn.linear_model.ridge_regression")
     will choose `sparse_cg` solver for sparse inputs when `solver=auto` and `sample_weight` is provided (previously `cholesky` solver was selected). [#13363](https://github.com/scikit-learn/scikit-learn/pull/13363)
     by [Bartosz Telenczuk](https://github.com/btel)
    
*   API Change The use of [`linear_model.lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")
     with `X=None` while passing `Gram` is deprecated in version 0.21 and will be removed in version 0.23. Use [`linear_model.lars_path_gram`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path_gram.html#sklearn.linear_model.lars_path_gram "sklearn.linear_model.lars_path_gram")
     instead. [#11699](https://github.com/scikit-learn/scikit-learn/pull/11699)
     by [Kuai Yu](https://github.com/yukuairoy)
    .
    
*   API Change `linear_model.logistic_regression_path` is deprecated in version 0.21 and will be removed in version 0.23. [#12821](https://github.com/scikit-learn/scikit-learn/pull/12821)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     with leave-one-out cross-validation now correctly fits an intercept when `fit_intercept=True` and the design matrix is sparse. [#13350](https://github.com/scikit-learn/scikit-learn/issues/13350)
     by [Jérôme Dockès](https://github.com/jeromedockes)
    

#### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-manifold "Link to this heading")

*   Efficiency Make [`manifold.trustworthiness`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.trustworthiness.html#sklearn.manifold.trustworthiness "sklearn.manifold.trustworthiness")
     use an inverted index instead of an `np.where` lookup to find the rank of neighbors in the input space. This improves efficiency in particular when computed with lots of neighbors and/or small datasets. [#9907](https://github.com/scikit-learn/scikit-learn/pull/9907)
     by [William de Vazelhes](https://github.com/wdevazelhes)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id16 "Link to this heading")

*   Feature Added the [`metrics.max_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.max_error.html#sklearn.metrics.max_error "sklearn.metrics.max_error")
     metric and a corresponding `'max_error'` scorer for single output regression. [#12232](https://github.com/scikit-learn/scikit-learn/pull/12232)
     by [Krishna Sangeeth](https://github.com/whiletruelearn)
    .
    
*   Feature Add [`metrics.multilabel_confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html#sklearn.metrics.multilabel_confusion_matrix "sklearn.metrics.multilabel_confusion_matrix")
    , which calculates a confusion matrix with true positive, false positive, false negative and true negative counts for each class. This facilitates the calculation of set-wise metrics such as recall, specificity, fall out and miss rate. [#11179](https://github.com/scikit-learn/scikit-learn/pull/11179)
     by [Shangwu Yao](https://github.com/ShangwuYao)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   Feature [`metrics.jaccard_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")
     has been added to calculate the Jaccard coefficient as an evaluation metric for binary, multilabel and multiclass tasks, with an interface analogous to [`metrics.f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")
    . [#13151](https://github.com/scikit-learn/scikit-learn/pull/13151)
     by [Gaurav Dhingra](https://github.com/gxyd)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   Feature Added [`metrics.pairwise.haversine_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.haversine_distances.html#sklearn.metrics.pairwise.haversine_distances "sklearn.metrics.pairwise.haversine_distances")
     which can be accessed with `metric='pairwise'` through [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     and estimators. (Haversine distance was previously available for nearest neighbors calculation.) [#12568](https://github.com/scikit-learn/scikit-learn/pull/12568)
     by [Wei Xue](https://github.com/xuewei4d)
    , [Emmanuel Arias](https://github.com/eamanu)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   Efficiency Faster [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     with `n_jobs` > 1 by using a thread-based backend, instead of process-based backends. [#8216](https://github.com/scikit-learn/scikit-learn/pull/8216)
     by [Pierre Glaser](https://github.com/pierreglaser)
     and [Romuald Menuet](https://github.com/zanospi)
    
*   Efficiency The pairwise manhattan distances with sparse input now uses the BLAS shipped with scipy instead of the bundled BLAS. [#12732](https://github.com/scikit-learn/scikit-learn/pull/12732)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    
*   Enhancement Use label `accuracy` instead of `micro-average` on [`metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
     to avoid confusion. `micro-average` is only shown for multi-label or multi-class with a subset of classes because it is otherwise identical to accuracy. [#12334](https://github.com/scikit-learn/scikit-learn/pull/12334)
     by [Emmanuel Arias](https://github.com/eamanu@eamanu.com)
    , [Joel Nothman](https://joelnothman.com/)
     and [Andreas Müller](https://amueller.github.io/)
    
*   Enhancement Added `beta` parameter to [`metrics.homogeneity_completeness_v_measure`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_completeness_v_measure.html#sklearn.metrics.homogeneity_completeness_v_measure "sklearn.metrics.homogeneity_completeness_v_measure")
     and [`metrics.v_measure_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")
     to configure the tradeoff between homogeneity and completeness. [#13607](https://github.com/scikit-learn/scikit-learn/pull/13607)
     by [Stephane Couvreur](https://github.com/scouvreur)
     and and [Ivan Sanchez](https://github.com/ivsanro1)
    .
    
*   Fix The metric [`metrics.r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
     is degenerate with a single sample and now it returns NaN and raises [`exceptions.UndefinedMetricWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.UndefinedMetricWarning.html#sklearn.exceptions.UndefinedMetricWarning "sklearn.exceptions.UndefinedMetricWarning")
    . [#12855](https://github.com/scikit-learn/scikit-learn/pull/12855)
     by [Pawel Sendyk](https://github.com/psendyk)
    .
    
*   Fix Fixed a bug where [`metrics.brier_score_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
     will sometimes return incorrect result when there’s only one class in `y_true`. [#13628](https://github.com/scikit-learn/scikit-learn/pull/13628)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   Fix Fixed a bug in [`metrics.label_ranking_average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html#sklearn.metrics.label_ranking_average_precision_score "sklearn.metrics.label_ranking_average_precision_score")
     where sample\_weight wasn’t taken into account for samples with degenerate labels. [#13447](https://github.com/scikit-learn/scikit-learn/pull/13447)
     by [Dan Ellis](https://github.com/dpwe)
    .
    
*   API Change The parameter `labels` in [`metrics.hamming_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "sklearn.metrics.hamming_loss")
     is deprecated in version 0.21 and will be removed in version 0.23. [#10580](https://github.com/scikit-learn/scikit-learn/pull/10580)
     by [Reshama Shaikh](https://github.com/reshamas)
     and [Sandra Mitrovic](https://github.com/SandraMNE)
    .
    
*   Fix The function [`metrics.pairwise.euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html#sklearn.metrics.pairwise.euclidean_distances "sklearn.metrics.pairwise.euclidean_distances")
    , and therefore several estimators with `metric='euclidean'`, suffered from numerical precision issues with `float32` features. Precision has been increased at the cost of a small drop of performance. [#13554](https://github.com/scikit-learn/scikit-learn/pull/13554)
     by [@Celelibi](https://github.com/Celelibi)
     and [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   API Change `metrics.jaccard_similarity_score` is deprecated in favour of the more consistent [`metrics.jaccard_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")
    . The former behavior for binary and multiclass targets is broken. [#13151](https://github.com/scikit-learn/scikit-learn/pull/13151)
     by [Joel Nothman](https://joelnothman.com/)
    .
    

#### [`sklearn.mixture`](https://scikit-learn.org/stable/api/sklearn.mixture.html#module-sklearn.mixture "sklearn.mixture")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-mixture "Link to this heading")

*   Fix Fixed a bug in `mixture.BaseMixture` and therefore on estimators based on it, i.e. [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     and [`mixture.BayesianGaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")
    , where `fit_predict` and `fit.predict` were not equivalent. [#13142](https://github.com/scikit-learn/scikit-learn/pull/13142)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-model-selection "Link to this heading")

*   Feature Classes [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     now allow for refit=callable to add flexibility in identifying the best estimator. See [Balance model complexity and cross-validated score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#sphx-glr-auto-examples-model-selection-plot-grid-search-refit-callable-py)
    . [#11354](https://github.com/scikit-learn/scikit-learn/pull/11354)
     by [Wenhao Zhang](https://github.com/wenhaoz@ucla.edu)
    , [Joel Nothman](https://joelnothman.com/)
     and [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Enhancement Classes [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    , [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
    , and methods [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
    , [`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
    , [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
    , now print train scores when `return_train_scores` is True and `verbose` > 2. For [`learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
    , and [`validation_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve "sklearn.model_selection.validation_curve")
     only the latter is required. [#12613](https://github.com/scikit-learn/scikit-learn/pull/12613)
     and [#12669](https://github.com/scikit-learn/scikit-learn/pull/12669)
     by [Marc Torrellas](https://github.com/marctorrellas)
    .
    
*   Enhancement Some [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
     classes and `model_selection.train_test_split` now raise `ValueError` when the resulting training set is empty. [#12861](https://github.com/scikit-learn/scikit-learn/pull/12861)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix Fixed a bug where [`model_selection.StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
     shuffles each class’s samples with the same `random_state`, making `shuffle=True` ineffective. [#13124](https://github.com/scikit-learn/scikit-learn/pull/13124)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   Fix Added ability for [`model_selection.cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
     to handle multi-label (and multioutput-multiclass) targets with `predict_proba`\-type methods. [#8773](https://github.com/scikit-learn/scikit-learn/pull/8773)
     by [Stephen Hoover](https://github.com/stephen-hoover)
    .
    
*   Fix Fixed an issue in [`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
     where `method="predict_proba"` returned always `0.0` when one of the classes was excluded in a cross-validation fold. [#13366](https://github.com/scikit-learn/scikit-learn/pull/13366)
     by [Guillaume Fournier](https://github.com/gfournier)
    

#### [`sklearn.multiclass`](https://scikit-learn.org/stable/api/sklearn.multiclass.html#module-sklearn.multiclass "sklearn.multiclass")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-multiclass "Link to this heading")

*   Fix Fixed an issue in [`multiclass.OneVsOneClassifier.decision_function`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier.decision_function "sklearn.multiclass.OneVsOneClassifier.decision_function")
     where the decision\_function value of a given sample was different depending on whether the decision\_function was evaluated on the sample alone or on a batch containing this same sample due to the scaling used in decision\_function. [#10440](https://github.com/scikit-learn/scikit-learn/pull/10440)
     by [Jonathan Ohayon](https://github.com/Johayon)
    .
    

#### [`sklearn.multioutput`](https://scikit-learn.org/stable/api/sklearn.multioutput.html#module-sklearn.multioutput "sklearn.multioutput")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-multioutput "Link to this heading")

*   Fix Fixed a bug in [`multioutput.MultiOutputClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier")
     where the `predict_proba` method incorrectly checked for `predict_proba` attribute in the estimator object. [#12222](https://github.com/scikit-learn/scikit-learn/pull/12222)
     by [Rebekah Kim](https://github.com/rebekahkim)
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id17 "Link to this heading")

*   Major Feature Added [`neighbors.NeighborhoodComponentsAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis")
     for metric learning, which implements the Neighborhood Components Analysis algorithm. [#10058](https://github.com/scikit-learn/scikit-learn/pull/10058)
     by [William de Vazelhes](https://github.com/wdevazelhes)
     and [John Chiotellis](https://github.com/johny-c)
    .
    
*   API Change Methods in [`neighbors.NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
     : [`kneighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.kneighbors "sklearn.neighbors.NearestNeighbors.kneighbors")
    , [`radius_neighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.radius_neighbors "sklearn.neighbors.NearestNeighbors.radius_neighbors")
    , [`kneighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.kneighbors_graph "sklearn.neighbors.NearestNeighbors.kneighbors_graph")
    , [`radius_neighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.radius_neighbors_graph "sklearn.neighbors.NearestNeighbors.radius_neighbors_graph")
     now raise `NotFittedError`, rather than `AttributeError`, when called before `fit` [#12279](https://github.com/scikit-learn/scikit-learn/pull/12279)
     by [Krishna Sangeeth](https://github.com/whiletruelearn)
    .
    

#### [`sklearn.neural_network`](https://scikit-learn.org/stable/api/sklearn.neural_network.html#module-sklearn.neural_network "sklearn.neural_network")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-neural-network "Link to this heading")

*   Fix Fixed a bug in [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     and [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
     where the option `shuffle=False` was being ignored. [#12582](https://github.com/scikit-learn/scikit-learn/pull/12582)
     by [Sam Waterbury](https://github.com/samwaterbury)
    .
    
*   Fix Fixed a bug in [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     where validation sets for early stopping were not sampled with stratification. In the multilabel case however, splits are still not stratified. [#13164](https://github.com/scikit-learn/scikit-learn/pull/13164)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    

#### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-pipeline "Link to this heading")

*   Feature [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     can now use indexing notation (e.g. `my_pipeline[0:-1]`) to extract a subsequence of steps as another Pipeline instance. A Pipeline can also be indexed directly to extract a particular step (e.g. `my_pipeline['svc']`), rather than accessing `named_steps`. [#2568](https://github.com/scikit-learn/scikit-learn/pull/2568)
     by [Joel Nothman](https://joelnothman.com/)
    .
    
*   Feature Added optional parameter `verbose` in [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
    , [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     and [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     and corresponding `make_` helpers for showing progress and timing of each step. [#11364](https://github.com/scikit-learn/scikit-learn/pull/11364)
     by [Baze Petrushev](https://github.com/petrushev)
    , [Karan Desai](https://github.com/karandesai-96)
    , [Joel Nothman](https://joelnothman.com/)
    , and [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     now supports using `'passthrough'` as a transformer, with the same effect as `None`. [#11144](https://github.com/scikit-learn/scikit-learn/pull/11144)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     implements `__len__` and therefore `len(pipeline)` returns the number of steps in the pipeline. [#13439](https://github.com/scikit-learn/scikit-learn/pull/13439)
     by [Lakshya KD](https://github.com/LakshKD)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id18 "Link to this heading")

*   Feature [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     now supports dropping one feature per category with a new drop parameter. [#12908](https://github.com/scikit-learn/scikit-learn/pull/12908)
     by [Drew Johnston](https://github.com/drewmjohnston)
    .
    
*   Efficiency [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     and [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     now handle pandas DataFrames more efficiently. [#13253](https://github.com/scikit-learn/scikit-learn/pull/13253)
     by [@maikia](https://github.com/maikia)
    .
    
*   Efficiency Make [`preprocessing.MultiLabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer "sklearn.preprocessing.MultiLabelBinarizer")
     cache class mappings instead of calculating it every time on the fly. [#12116](https://github.com/scikit-learn/scikit-learn/pull/12116)
     by [Ekaterina Krivich](https://github.com/kiote)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   Efficiency [`preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
     now supports compressed sparse row (CSR) matrices as input for degrees 2 and 3. This is typically much faster than the dense case as it scales with matrix density and expansion degree (on the order of density^degree), and is much, much faster than the compressed sparse column (CSC) case. [#12197](https://github.com/scikit-learn/scikit-learn/pull/12197)
     by [Andrew Nystrom](https://github.com/awnystrom)
    .
    
*   Efficiency Speed improvement in [`preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
    , in the dense case. Also added a new parameter `order` which controls output order for further speed performances. [#12251](https://github.com/scikit-learn/scikit-learn/pull/12251)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Fix Fixed the calculation overflow when using a float16 dtype with [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
    . [#13007](https://github.com/scikit-learn/scikit-learn/pull/13007)
     by [Raffaello Baluyot](https://github.com/baluyotraf)
    
*   Fix Fixed a bug in [`preprocessing.QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
     and [`preprocessing.quantile_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#sklearn.preprocessing.quantile_transform "sklearn.preprocessing.quantile_transform")
     to force n\_quantiles to be at most equal to n\_samples. Values of n\_quantiles larger than n\_samples were either useless or resulting in a wrong approximation of the cumulative distribution function estimator. [#13333](https://github.com/scikit-learn/scikit-learn/pull/13333)
     by [Albert Thomas](https://github.com/albertcthomas)
    .
    
*   API Change The default value of `copy` in [`preprocessing.quantile_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#sklearn.preprocessing.quantile_transform "sklearn.preprocessing.quantile_transform")
     will change from False to True in 0.23 in order to make it more consistent with the default `copy` values of other functions in [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
     and prevent unexpected side effects by modifying the value of `X` inplace. [#13459](https://github.com/scikit-learn/scikit-learn/pull/13459)
     by [Hunter McGushion](https://github.com/HunterMcGushion)
    .
    

#### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-svm "Link to this heading")

*   Fix Fixed an issue in [`svm.SVC.decision_function`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.decision_function "sklearn.svm.SVC.decision_function")
     when `decision_function_shape='ovr'`. The decision\_function value of a given sample was different depending on whether the decision\_function was evaluated on the sample alone or on a batch containing this same sample due to the scaling used in decision\_function. [#10440](https://github.com/scikit-learn/scikit-learn/pull/10440)
     by [Jonathan Ohayon](https://github.com/Johayon)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#id19 "Link to this heading")

*   Feature Decision Trees can now be plotted with matplotlib using `tree.plot_tree` without relying on the `dot` library, removing a hard-to-install dependency. [#8508](https://github.com/scikit-learn/scikit-learn/pull/8508)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Feature Decision Trees can now be exported in a human readable textual format using [`tree.export_text`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html#sklearn.tree.export_text "sklearn.tree.export_text")
    . [#6261](https://github.com/scikit-learn/scikit-learn/pull/6261)
     by `Giuseppe Vettigli <JustGlowing>`.
    
*   Feature `get_n_leaves()` and `get_depth()` have been added to `tree.BaseDecisionTree` and consequently all estimators based on it, including [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
    , and [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
    . [#12300](https://github.com/scikit-learn/scikit-learn/pull/12300)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   Fix Trees and forests did not previously `predict` multi-output classification targets with string labels, despite accepting them in `fit`. [#11458](https://github.com/scikit-learn/scikit-learn/pull/11458)
     by [Mitar Milutinovic](https://github.com/mitar)
    .
    
*   Fix Fixed an issue with `tree.BaseDecisionTree` and consequently all estimators based on it, including [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
    , and [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
    , where they used to exceed the given `max_depth` by 1 while expanding the tree if `max_leaf_nodes` and `max_depth` were both specified by the user. Please note that this also affects all ensemble methods using decision trees. [#12344](https://github.com/scikit-learn/scikit-learn/pull/12344)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v0.21.html#sklearn-utils "Link to this heading")

*   Feature [`utils.resample`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.resample.html#sklearn.utils.resample "sklearn.utils.resample")
     now accepts a `stratify` parameter for sampling according to class distributions. [#13549](https://github.com/scikit-learn/scikit-learn/pull/13549)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   API Change Deprecated `warn_on_dtype` parameter from [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     and [`utils.check_X_y`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html#sklearn.utils.check_X_y "sklearn.utils.check_X_y")
    . Added explicit warning for dtype conversion in `check_pairwise_arrays` if the `metric` being passed is a pairwise boolean metric. [#13382](https://github.com/scikit-learn/scikit-learn/pull/13382)
     by [Prathmesh Savale](https://github.com/praths007)
    .
    

#### Multiple modules[#](https://scikit-learn.org/stable/whats_new/v0.21.html#multiple-modules "Link to this heading")

*   Major Feature The `__repr__()` method of all estimators (used when calling `print(estimator)`) has been entirely re-written, building on Python’s pretty printing standard library. All parameters are printed by default, but this can be altered with the `print_changed_only` option in [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
    . [#11705](https://github.com/scikit-learn/scikit-learn/pull/11705)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Major Feature Add estimators tags: these are annotations of estimators that allow programmatic inspection of their capabilities, such as sparse matrix support, supported output types and supported methods. Estimator tags also determine the tests that are run on an estimator when `check_estimator` is called. Read more in the [User Guide](https://scikit-learn.org/stable/developers/develop.html#estimator-tags)
    . [#8022](https://github.com/scikit-learn/scikit-learn/pull/8022)
     by [Andreas Müller](https://github.com/amueller)
    .
    
*   Efficiency Memory copies are avoided when casting arrays to a different dtype in multiple estimators. [#11973](https://github.com/scikit-learn/scikit-learn/pull/11973)
     by [Roman Yurchak](https://github.com/rth)
    .
    
*   Fix Fixed a bug in the implementation of the `our_rand_r` helper function that was not behaving consistently across platforms. [#13422](https://github.com/scikit-learn/scikit-learn/pull/13422)
     by [Madhura Parikh](https://github.com/jdnc)
     and [Clément Doumouro](https://github.com/ClemDoum)
    .
    

#### Miscellaneous[#](https://scikit-learn.org/stable/whats_new/v0.21.html#miscellaneous "Link to this heading")

*   Enhancement Joblib is no longer vendored in scikit-learn, and becomes a dependency. Minimal supported version is joblib 0.11, however using version >= 0.13 is strongly recommended. [#13531](https://github.com/scikit-learn/scikit-learn/pull/13531)
     by [Roman Yurchak](https://github.com/rth)
    .
    

### Changes to estimator checks[#](https://scikit-learn.org/stable/whats_new/v0.21.html#changes-to-estimator-checks "Link to this heading")

These changes mostly affect library developers.

*   Add `check_fit_idempotent` to [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
    , which checks that when `fit` is called twice with the same data, the output of `predict`, `predict_proba`, `transform`, and `decision_function` does not change. [#12328](https://github.com/scikit-learn/scikit-learn/pull/12328)
     by [Nicolas Hug](https://github.com/NicolasHug)
    
*   Many checks can now be disabled or configured with [Estimator Tags](https://scikit-learn.org/stable/developers/develop.html#estimator-tags)
    . [#8022](https://github.com/scikit-learn/scikit-learn/pull/8022)
     by [Andreas Müller](https://github.com/amueller)
    .
    

Code and documentation contributors

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 0.20, including:

adanhawth, Aditya Vyas, Adrin Jalali, Agamemnon Krasoulis, Albert Thomas, Alberto Torres, Alexandre Gramfort, amourav, Andrea Navarrete, Andreas Mueller, Andrew Nystrom, assiaben, Aurélien Bellet, Bartosz Michałowski, Bartosz Telenczuk, bauks, BenjaStudio, bertrandhaut, Bharat Raghunathan, brentfagan, Bryan Woods, Cat Chenal, Cheuk Ting Ho, Chris Choe, Christos Aridas, Clément Doumouro, Cole Smith, Connossor, Corey Levinson, Dan Ellis, Dan Stine, Danylo Baibak, daten-kieker, Denis Kataev, Didi Bar-Zev, Dillon Gardner, Dmitry Mottl, Dmitry Vukolov, Dougal J. Sutherland, Dowon, drewmjohnston, Dror Atariah, Edward J Brown, Ekaterina Krivich, Elizabeth Sander, Emmanuel Arias, Eric Chang, Eric Larson, Erich Schubert, esvhd, Falak, Feda Curic, Federico Caselli, Frank Hoang, Fibinse Xavier\`, Finn O’Shea, Gabriel Marzinotto, Gabriel Vacaliuc, Gabriele Calvo, Gael Varoquaux, GauravAhlawat, Giuseppe Vettigli, Greg Gandenberger, Guillaume Fournier, Guillaume Lemaitre, Gustavo De Mari Pereira, Hanmin Qin, haroldfox, hhu-luqi, Hunter McGushion, Ian Sanders, JackLangerman, Jacopo Notarstefano, jakirkham, James Bourbeau, Jan Koch, Jan S, janvanrijn, Jarrod Millman, jdethurens, jeremiedbb, JF, joaak, Joan Massich, Joel Nothman, Jonathan Ohayon, Joris Van den Bossche, josephsalmon, Jérémie Méhault, Katrin Leinweber, ken, kms15, Koen, Kossori Aruku, Krishna Sangeeth, Kuai Yu, Kulbear, Kushal Chauhan, Kyle Jackson, Lakshya KD, Leandro Hermida, Lee Yi Jie Joel, Lily Xiong, Lisa Sarah Thomas, Loic Esteve, louib, luk-f-a, maikia, mail-liam, Manimaran, Manuel López-Ibáñez, Marc Torrellas, Marco Gaido, Marco Gorelli, MarcoGorelli, marineLM, Mark Hannel, Martin Gubri, Masstran, mathurinm, Matthew Roeschke, Max Copeland, melsyt, mferrari3, Mickaël Schoentgen, Ming Li, Mitar, Mohammad Aftab, Mohammed AbdelAal, Mohammed Ibraheem, Muhammad Hassaan Rafique, mwestt, Naoya Iijima, Nicholas Smith, Nicolas Goix, Nicolas Hug, Nikolay Shebanov, Oleksandr Pavlyk, Oliver Rausch, Olivier Grisel, Orestis, Osman, Owen Flanagan, Paul Paczuski, Pavel Soriano, pavlos kallis, Pawel Sendyk, peay, Peter, Peter Cock, Peter Hausamann, Peter Marko, Pierre Glaser, pierretallotte, Pim de Haan, Piotr Szymański, Prabakaran Kumaresshan, Pradeep Reddy Raamana, Prathmesh Savale, Pulkit Maloo, Quentin Batista, Radostin Stoyanov, Raf Baluyot, Rajdeep Dua, Ramil Nugmanov, Raúl García Calvo, Rebekah Kim, Reshama Shaikh, Rohan Lekhwani, Rohan Singh, Rohan Varma, Rohit Kapoor, Roman Feldbauer, Roman Yurchak, Romuald M, Roopam Sharma, Ryan, Rüdiger Busche, Sam Waterbury, Samuel O. Ronsin, SandroCasagrande, Scott Cole, Scott Lowe, Sebastian Raschka, Shangwu Yao, Shivam Kotwalia, Shiyu Duan, smarie, Sriharsha Hatwar, Stephen Hoover, Stephen Tierney, Stéphane Couvreur, surgan12, SylvainLan, TakingItCasual, Tashay Green, thibsej, Thomas Fan, Thomas J Fan, Thomas Moreau, Tom Dupré la Tour, Tommy, Tulio Casagrande, Umar Farouk Umar, Utkarsh Upadhyay, Vinayak Mehta, Vishaal Kapoor, Vivek Kumar, Vlad Niculae, vqean3, Wenhao Zhang, William de Vazelhes, xhan, Xing Han Lu, xinyuliu12, Yaroslav Halchenko, Zach Griffith, Zach Miller, Zayd Hammoudeh, Zhuyi Xue, Zijie (ZJ) Poh, ^\_\_^

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)