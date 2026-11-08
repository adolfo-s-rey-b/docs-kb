[Skip to main content](https://scikit-learn.org/stable/whats_new/v0.24.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v0.24.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v0.24.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v0.24.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v0.24.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v0.24.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v0.24.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v0.24.html)

Collapse Sidebar Expand Sidebar

Version 0.24[#](https://scikit-learn.org/stable/whats_new/v0.24.html#version-0-24 "Link to this heading")

==========================================================================================================

For a short description of the main highlights of the release, please refer to [Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html#sphx-glr-auto-examples-release-highlights-plot-release-highlights-0-24-0-py)
.

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 0.24.2[#](https://scikit-learn.org/stable/whats_new/v0.24.html#version-0-24-2 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**April 2021**

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.24.html#changelog "Link to this heading")

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-compose "Link to this heading")

*   Fix `compose.ColumnTransformer.get_feature_names` does not call `get_feature_names` on transformers with an empty column selection. [#19579](https://github.com/scikit-learn/scikit-learn/pull/19579)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.cross_decomposition`](https://scikit-learn.org/stable/api/sklearn.cross_decomposition.html#module-sklearn.cross_decomposition "sklearn.cross_decomposition")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-cross-decomposition "Link to this heading")

*   Fix Fixed a regression in [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
    . [#19646](https://github.com/scikit-learn/scikit-learn/pull/19646)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
     raises warning for constant y residuals instead of a `StopIteration` error. [#19922](https://github.com/scikit-learn/scikit-learn/pull/19922)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-decomposition "Link to this heading")

*   Fix Fixed a bug in [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
    ’s `inverse_transform`. [#19732](https://github.com/scikit-learn/scikit-learn/pull/19732)
     by [Kei Ishikawa](https://github.com/kstoneriv3)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-ensemble "Link to this heading")

*   Fix Fixed a bug in [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     `fit` with `sample_weight` parameter and `least_absolute_deviation` loss function. [#19407](https://github.com/scikit-learn/scikit-learn/pull/19407)
     by [Vadim Ushtanit](https://github.com/vadim-ushtanit)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-feature-extraction "Link to this heading")

*   Fix Fixed a bug to support multiple strings for a category when `sparse=False` in [`feature_extraction.DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
    . [#19982](https://github.com/scikit-learn/scikit-learn/pull/19982)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.gaussian_process`](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#module-sklearn.gaussian_process "sklearn.gaussian_process")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-gaussian-process "Link to this heading")

*   Fix Avoid explicitly forming inverse covariance matrix in [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
     when set to output standard deviation. With certain covariance matrices this inverse is unstable to compute explicitly. Calling Cholesky solver mitigates this issue in computation. [#19939](https://github.com/scikit-learn/scikit-learn/pull/19939)
     by [Ian Halvic](https://github.com/iwhalvic)
    .
    
*   Fix Avoid division by zero when scaling constant target in [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
    . It was due to a std. dev. equal to 0. Now, such case is detected and the std. dev. is affected to 1 avoiding a division by zero and thus the presence of NaN values in the normalized target. [#19703](https://github.com/scikit-learn/scikit-learn/pull/19703)
     by [@sobkevich](https://github.com/sobkevich)
    , [Boris Villazón-Terrazas](https://github.com/boricles)
     and [Alexandr Fonari](https://github.com/afonari)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-linear-model "Link to this heading")

*   Fix : Fixed a bug in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    : the sample\_weight object is not modified anymore. [#19182](https://github.com/scikit-learn/scikit-learn/pull/19182)
     by [Yosuke KOBAYASHI](https://github.com/m7142yosuke)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-metrics "Link to this heading")

*   Fix [`metrics.top_k_accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html#sklearn.metrics.top_k_accuracy_score "sklearn.metrics.top_k_accuracy_score")
     now supports multiclass problems where only two classes appear in `y_true` and all the classes are specified in `labels`. [#19721](https://github.com/scikit-learn/scikit-learn/pull/19721)
     by [Joris Clement](https://github.com/flyingdutchman23)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-model-selection "Link to this heading")

*   Fix [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     and [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     now correctly show the score for single metrics and verbose > 2. [#19659](https://github.com/scikit-learn/scikit-learn/pull/19659)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Some values in the `cv_results_` attribute of [`model_selection.HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
     and [`model_selection.HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
     were not properly converted to numpy arrays. [#19211](https://github.com/scikit-learn/scikit-learn/pull/19211)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix The `fit` method of the successive halving parameter search ([`model_selection.HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
    , and [`model_selection.HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
    ) now correctly handles the `groups` parameter. [#19847](https://github.com/scikit-learn/scikit-learn/pull/19847)
     by [Xiaoyu Chai](https://github.com/xiaoyuchai)
    .
    

#### [`sklearn.multioutput`](https://scikit-learn.org/stable/api/sklearn.multioutput.html#module-sklearn.multioutput "sklearn.multioutput")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-multioutput "Link to this heading")

*   Fix [`multioutput.MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")
     now works with estimators that dynamically define `predict` during fitting, such as [`ensemble.StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
    . [#19308](https://github.com/scikit-learn/scikit-learn/pull/19308)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-preprocessing "Link to this heading")

*   Fix Validate the constructor parameter `handle_unknown` in [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     to only allow for `'error'` and `'use_encoded_value'` strategies. [#19234](https://github.com/scikit-learn/scikit-learn/pull/19234)
     by `Guillaume Lemaitre <glemaitre>`.
    
*   Fix Fix encoder categories having dtype=’S’ [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     and [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
    . [#19727](https://github.com/scikit-learn/scikit-learn/pull/19727)
     by [Andrew Delong](https://github.com/andrewdelong)
    .
    
*   Fix [`preprocessing.OrdinalEncoder.transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder.transform "sklearn.preprocessing.OrdinalEncoder.transform")
     correctly handles unknown values for string dtypes. [#19888](https://github.com/scikit-learn/scikit-learn/pull/19888)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`preprocessing.OneHotEncoder.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.fit "sklearn.preprocessing.OneHotEncoder.fit")
     no longer alters the `drop` parameter. [#19924](https://github.com/scikit-learn/scikit-learn/pull/19924)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.semi_supervised`](https://scikit-learn.org/stable/api/sklearn.semi_supervised.html#module-sklearn.semi_supervised "sklearn.semi_supervised")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-semi-supervised "Link to this heading")

*   Fix Avoid NaN during label propagation in [`LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")
    . [#19271](https://github.com/scikit-learn/scikit-learn/pull/19271)
     by [Zhaowei Wang](https://github.com/ThuWangzw)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-tree "Link to this heading")

*   Fix Fix a bug in `fit` of `tree.BaseDecisionTree` that caused segmentation faults under certain conditions. `fit` now deep copies the `Criterion` object to prevent shared concurrent accesses. [#19580](https://github.com/scikit-learn/scikit-learn/pull/19580)
     by [Samuel Brice](https://github.com/samdbrice)
     and [Alex Adamson](https://github.com/aadamson)
     and [Wil Yegelwel](https://github.com/wyegelwel)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-utils "Link to this heading")

*   Fix Better contains the CSS provided by [`utils.estimator_html_repr`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_html_repr.html#sklearn.utils.estimator_html_repr "sklearn.utils.estimator_html_repr")
     by giving CSS ids to the html representation. [#19417](https://github.com/scikit-learn/scikit-learn/pull/19417)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

Version 0.24.1[#](https://scikit-learn.org/stable/whats_new/v0.24.html#version-0-24-1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**January 2021**

### Packaging[#](https://scikit-learn.org/stable/whats_new/v0.24.html#packaging "Link to this heading")

The 0.24.0 scikit-learn wheels were not working with MacOS <1.15 due to `libomp`. The version of `libomp` used to build the wheels was too recent for older macOS versions. This issue has been fixed for 0.24.1 scikit-learn wheels. Scikit-learn wheels published on PyPI.org now officially support macOS 10.13 and later.

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id1 "Link to this heading")

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id2 "Link to this heading")

*   Fix Fix numerical stability bug that could happen in [`metrics.adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")
     and [`metrics.mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mutual_info_score.html#sklearn.metrics.mutual_info_score "sklearn.metrics.mutual_info_score")
     with NumPy 1.20+. [#19179](https://github.com/scikit-learn/scikit-learn/pull/19179)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.semi_supervised`](https://scikit-learn.org/stable/api/sklearn.semi_supervised.html#module-sklearn.semi_supervised "sklearn.semi_supervised")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id3 "Link to this heading")

*   Fix [`semi_supervised.SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
     is now accepting meta-estimator (e.g. [`ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
    ). The validation of this estimator is done on the fitted estimator, once we know the existence of the method `predict_proba`. [#19126](https://github.com/scikit-learn/scikit-learn/pull/19126)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

Version 0.24.0[#](https://scikit-learn.org/stable/whats_new/v0.24.html#version-0-24-0 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**December 2020**

### Changed models[#](https://scikit-learn.org/stable/whats_new/v0.24.html#changed-models "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   Fix [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
     behaviour is now more consistent between 32-bits and 64-bits data when the kernel has small positive eigenvalues.
    
*   Fix [`decomposition.TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
     becomes deterministic by exposing a `random_state` parameter.
    
*   Fix [`linear_model.Perceptron`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron")
     when `penalty='elasticnet'`.
    
*   Fix Change in the random sampling procedures for the center initialization of [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    .
    

Details are listed in the changelog below.

(While we are trying to better inform users by providing this information, we cannot assure that this list is complete.)

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id4 "Link to this heading")

#### [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-base "Link to this heading")

*   Fix [`base.BaseEstimator.get_params`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator.get_params "sklearn.base.BaseEstimator.get_params")
     now will raise an `AttributeError` if a parameter cannot be retrieved as an instance attribute. Previously it would return `None`. [#17448](https://github.com/scikit-learn/scikit-learn/pull/17448)
     by [Juan Carlos Alfaro Jiménez](https://github.com/alfaro96)
    .
    

#### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-calibration "Link to this heading")

*   Efficiency [`calibration.CalibratedClassifierCV.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV.fit "sklearn.calibration.CalibratedClassifierCV.fit")
     now supports parallelization via `joblib.Parallel` using argument `n_jobs`. [#17107](https://github.com/scikit-learn/scikit-learn/pull/17107)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Enhancement Allow [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     use with prefit [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     where data is not `X` is not array-like, sparse matrix or dataframe at the start. [#17546](https://github.com/scikit-learn/scikit-learn/pull/17546)
     by [Lucy Liu](https://github.com/lucyleeow)
    .
    
*   Enhancement Add `ensemble` parameter to [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
    , which enables implementation of calibration via an ensemble of calibrators (current method) or just one calibrator using all the data (similar to the built-in feature of [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
     estimators with the `probabilities=True` parameter). [#17856](https://github.com/scikit-learn/scikit-learn/pull/17856)
     by [Lucy Liu](https://github.com/lucyleeow)
     and [Andrea Esuli](https://github.com/aesuli)
    .
    

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-cluster "Link to this heading")

*   Enhancement [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     has a new parameter `compute_distances`. When set to `True`, distances between clusters are computed and stored in the `distances_` attribute even when the parameter `distance_threshold` is not used. This new parameter is useful to produce dendrogram visualizations, but introduces a computational and memory overhead. [#17984](https://github.com/scikit-learn/scikit-learn/pull/17984)
     by [Michael Riedmann](https://github.com/mriedmann)
    , [Emilie Delattre](https://github.com/EmilieDel)
    , and [Francesco Casalegno](https://github.com/FrancescoCasalegno)
    .
    
*   Enhancement [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     and [`cluster.spectral_clustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")
     have a new keyword argument `verbose`. When set to `True`, additional messages will be displayed which can aid with debugging. [#18052](https://github.com/scikit-learn/scikit-learn/pull/18052)
     by [Sean O. Stalley](https://github.com/sstalley)
    .
    
*   Enhancement Added [`cluster.kmeans_plusplus`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.kmeans_plusplus.html#sklearn.cluster.kmeans_plusplus "sklearn.cluster.kmeans_plusplus")
     as public function. Initialization by KMeans++ can now be called separately to generate initial cluster centroids. [#17937](https://github.com/scikit-learn/scikit-learn/pull/17937)
     by [@g-walsh](https://github.com/g-walsh)
    
*   API Change [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     attributes, `counts_` and `init_size_`, are deprecated and will be removed in 1.1 (renaming of 0.26). [#17864](https://github.com/scikit-learn/scikit-learn/pull/17864)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id5 "Link to this heading")

*   Fix [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     will skip transformers the column selector is a list of bools that are False. [#17616](https://github.com/scikit-learn/scikit-learn/pull/17616)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     now displays the remainder in the diagram display. [#18167](https://github.com/scikit-learn/scikit-learn/pull/18167)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     enforces strict count and order of column names between `fit` and `transform` by raising an error instead of a warning, following the deprecation cycle. [#18256](https://github.com/scikit-learn/scikit-learn/pull/18256)
     by [Madhura Jayratne](https://github.com/madhuracj)
    .
    

#### [`sklearn.covariance`](https://scikit-learn.org/stable/api/sklearn.covariance.html#module-sklearn.covariance "sklearn.covariance")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-covariance "Link to this heading")

*   API Change Deprecates `cv_alphas_` in favor of `cv_results_['alphas']` and `grid_scores_` in favor of split scores in `cv_results_` in [`covariance.GraphicalLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")
    . `cv_alphas_` and `grid_scores_` will be removed in version 1.1 (renaming of 0.26). [#16392](https://github.com/scikit-learn/scikit-learn/pull/16392)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.cross_decomposition`](https://scikit-learn.org/stable/api/sklearn.cross_decomposition.html#module-sklearn.cross_decomposition "sklearn.cross_decomposition")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id6 "Link to this heading")

*   Fix Fixed a bug in [`cross_decomposition.PLSSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD "sklearn.cross_decomposition.PLSSVD")
     which would sometimes return components in the reversed order of importance. [#17095](https://github.com/scikit-learn/scikit-learn/pull/17095)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix Fixed a bug in [`cross_decomposition.PLSSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD "sklearn.cross_decomposition.PLSSVD")
    , [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
    , and [`cross_decomposition.PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
    , which would lead to incorrect predictions for `est.transform(Y)` when the training data is single-target. [#17095](https://github.com/scikit-learn/scikit-learn/pull/17095)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix Increases the stability of [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
     [#18746](https://github.com/scikit-learn/scikit-learn/pull/18746)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change The bounds of the `n_components` parameter is now restricted:
    
    *   into `[1, min(n_samples, n_features, n_targets)]`, for [`cross_decomposition.PLSSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD "sklearn.cross_decomposition.PLSSVD")
        , [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
        , and [`cross_decomposition.PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
        .
        
    *   into `[1, n_features]` or [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
        .
        
    
    An error will be raised in 1.1 (renaming of 0.26). [#17095](https://github.com/scikit-learn/scikit-learn/pull/17095)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   API Change For [`cross_decomposition.PLSSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD "sklearn.cross_decomposition.PLSSVD")
    , [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
    , and [`cross_decomposition.PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
    , the `x_scores_` and `y_scores_` attributes were deprecated and will be removed in 1.1 (renaming of 0.26). They can be retrieved by calling `transform` on the training data. The `norm_y_weights` attribute will also be removed. [#17095](https://github.com/scikit-learn/scikit-learn/pull/17095)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   API Change For [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
    , [`cross_decomposition.PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
    , [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
    , and [`cross_decomposition.PLSSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD "sklearn.cross_decomposition.PLSSVD")
    , the `x_mean_`, `y_mean_`, `x_std_`, and `y_std_` attributes were deprecated and will be removed in 1.1 (renaming of 0.26). [#18768](https://github.com/scikit-learn/scikit-learn/pull/18768)
     by [Maren Westermann](https://github.com/marenwestermann)
    .
    
*   Fix [`decomposition.TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
     becomes deterministic by using the `random_state`. It controls the weights’ initialization of the underlying ARPACK solver. :pr:\` #18302\` by [Gaurav Desai](https://github.com/gauravkdesai)
     and [Ivan Panico](https://github.com/FollowKenny)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-datasets "Link to this heading")

*   Feature [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     now validates md5 checksum of arff files downloaded or cached to ensure data integrity. [#14800](https://github.com/scikit-learn/scikit-learn/pull/14800)
     by [Shashank Singh](https://github.com/shashanksingh28)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   Enhancement [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     now allows argument `as_frame` to be ‘auto’, which tries to convert returned data to pandas DataFrame unless data is sparse. [#17396](https://github.com/scikit-learn/scikit-learn/pull/17396)
     by [Jiaxiang](https://github.com/fujiaxiang)
    .
    
*   Enhancement [`datasets.fetch_covtype`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#sklearn.datasets.fetch_covtype "sklearn.datasets.fetch_covtype")
     now supports the optional argument `as_frame`; when it is set to True, the returned Bunch object’s `data` and `frame` members are pandas DataFrames, and the `target` member is a pandas Series. [#17491](https://github.com/scikit-learn/scikit-learn/pull/17491)
     by [Alex Liang](https://github.com/tianchuliang)
    .
    
*   Enhancement [`datasets.fetch_kddcup99`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99 "sklearn.datasets.fetch_kddcup99")
     now supports the optional argument `as_frame`; when it is set to True, the returned Bunch object’s `data` and `frame` members are pandas DataFrames, and the `target` member is a pandas Series. [#18280](https://github.com/scikit-learn/scikit-learn/pull/18280)
     by [Alex Liang](https://github.com/tianchuliang)
     and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Enhancement [`datasets.fetch_20newsgroups_vectorized`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized")
     now supports loading as a pandas `DataFrame` by setting `as_frame=True`. [#17499](https://github.com/scikit-learn/scikit-learn/pull/17499)
     by [Brigitta Sipőcz](https://github.com/bsipocz)
     and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change The default value of `as_frame` in [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     is changed from False to ‘auto’. [#17610](https://github.com/scikit-learn/scikit-learn/pull/17610)
     by [Jiaxiang](https://github.com/fujiaxiang)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id7 "Link to this heading")

*   API Change For [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
    , the `init` value, when ‘init=None’ and n\_components <= min(n\_samples, n\_features) will be changed from `'nndsvd'` to `'nndsvda'` in 1.1 (renaming of 0.26). [#18525](https://github.com/scikit-learn/scikit-learn/pull/18525)
     by [Chiara Marmo](https://github.com/cmarmo)
    .
    
*   Enhancement [`decomposition.FactorAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")
     now supports the optional argument `rotation`, which can take the value `None`, `'varimax'` or `'quartimax'`. [#11064](https://github.com/scikit-learn/scikit-learn/pull/11064)
     by [Jona Sassenhagen](https://github.com/jona-sassenhagen)
    .
    
*   Enhancement [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     now supports the optional parameter `regularization`, which can take the values `None`, ‘components’, ‘transformation’ or ‘both’, in accordance with `decomposition.NMF.non_negative_factorization`. [#17414](https://github.com/scikit-learn/scikit-learn/pull/17414)
     by [Bharat Raghunathan](https://github.com/bharatr21)
    .
    
*   Fix [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
     behaviour is now more consistent between 32-bits and 64-bits data input when the kernel has small positive eigenvalues. Small positive eigenvalues were not correctly discarded for 32-bits data. [#18149](https://github.com/scikit-learn/scikit-learn/pull/18149)
     by [Sylvain Marié](https://github.com/smarie)
    .
    
*   Fix Fix [`decomposition.SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")
     such that it follows scikit-learn API and supports cloning. The attribute `components_` is deprecated in 0.24 and will be removed in 1.1 (renaming of 0.26). This attribute was redundant with the `dictionary` attribute and constructor parameter. [#17679](https://github.com/scikit-learn/scikit-learn/pull/17679)
     by [Xavier Dupré](https://github.com/sdpython)
    .
    
*   Fix [`decomposition.TruncatedSVD.fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD.fit_transform "sklearn.decomposition.TruncatedSVD.fit_transform")
     consistently returns the same as [`decomposition.TruncatedSVD.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD.fit "sklearn.decomposition.TruncatedSVD.fit")
     followed by [`decomposition.TruncatedSVD.transform`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD.transform "sklearn.decomposition.TruncatedSVD.transform")
    . [#18528](https://github.com/scikit-learn/scikit-learn/pull/18528)
     by [Albert Villanova del Moral](https://github.com/albertvillanova)
     and [Ruifeng Zheng](https://github.com/zhengruifeng)
    .
    

#### [`sklearn.discriminant_analysis`](https://scikit-learn.org/stable/api/sklearn.discriminant_analysis.html#module-sklearn.discriminant_analysis "sklearn.discriminant_analysis")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-discriminant-analysis "Link to this heading")

*   Enhancement [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     can now use custom covariance estimate by setting the `covariance_estimator` parameter. [#14446](https://github.com/scikit-learn/scikit-learn/pull/14446)
     by [Hugo Richard](https://github.com/hugorichard)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id8 "Link to this heading")

*   Major Feature [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     and [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     now have native support for categorical features with the `categorical_features` parameter. [#18394](https://github.com/scikit-learn/scikit-learn/pull/18394)
     by [Nicolas Hug](https://github.com/NicolasHug)
     and [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     and [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     now support the method `staged_predict`, which allows monitoring of each stage. [#16985](https://github.com/scikit-learn/scikit-learn/pull/16985)
     by [Hao Chun Chang](https://github.com/haochunchang)
    .
    
*   Efficiency break cyclic references in the tree nodes used internally in [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     and [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     to allow for the timely garbage collection of large intermediate datastructures and to improve memory usage in `fit`. [#18334](https://github.com/scikit-learn/scikit-learn/pull/18334)
     by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
     [Nicolas Hug](https://github.com/NicolasHug)
    , [Thomas Fan](https://github.com/thomasjpfan)
     and [Andreas Müller](https://amueller.github.io/)
    .
    
*   Efficiency Histogram initialization is now done in parallel in [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     and [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     which results in speed improvement for problems that build a lot of nodes on multicore machines. [#18341](https://github.com/scikit-learn/scikit-learn/pull/18341)
     by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    , [Nicolas Hug](https://github.com/NicolasHug)
    , [Thomas Fan](https://github.com/thomasjpfan)
    , and [Egor Smirnov](https://github.com/SmirnovEgorRu)
    .
    
*   Fix Fixed a bug in [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     and [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     which can now accept data with `uint8` dtype in `predict`. [#18410](https://github.com/scikit-learn/scikit-learn/pull/18410)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   API Change The parameter `n_classes_` is now deprecated in [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     and returns `1`. [#17702](https://github.com/scikit-learn/scikit-learn/pull/17702)
     by [Simona Maggio](https://github.com/simonamaggio)
    .
    
*   API Change Mean absolute error (‘mae’) is now deprecated for the parameter `criterion` in [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     and [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
    . [#18326](https://github.com/scikit-learn/scikit-learn/pull/18326)
     by [Madhura Jayaratne](https://github.com/madhuracj)
    .
    

#### [`sklearn.exceptions`](https://scikit-learn.org/stable/api/sklearn.exceptions.html#module-sklearn.exceptions "sklearn.exceptions")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-exceptions "Link to this heading")

*   API Change `exceptions.ChangedBehaviorWarning` and `exceptions.NonBLASDotWarning` are deprecated and will be removed in 1.1 (renaming of 0.26). [#17804](https://github.com/scikit-learn/scikit-learn/pull/17804)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id9 "Link to this heading")

*   Enhancement [`feature_extraction.DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
     accepts multiple values for one categorical feature. [#17367](https://github.com/scikit-learn/scikit-learn/pull/17367)
     by [Peng Yu](https://github.com/yupbank)
     and [Chiara Marmo](https://github.com/cmarmo)
    .
    
*   Fix [`feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     raises an issue if a custom token pattern which captures more than one group is provided. [#15427](https://github.com/scikit-learn/scikit-learn/pull/15427)
     by [Gangesh Gudmalwar](https://github.com/ggangesh)
     and [Erin R Hoffman](https://github.com/hoffm386)
    .
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-feature-selection "Link to this heading")

*   Feature Added [`feature_selection.SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
     which implements forward and backward sequential feature selection. [#6545](https://github.com/scikit-learn/scikit-learn/pull/6545)
     by [Sebastian Raschka](https://sebastianraschka.com/)
     and [#17159](https://github.com/scikit-learn/scikit-learn/pull/17159)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Feature A new parameter `importance_getter` was added to [`feature_selection.RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
    , [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
     and [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
    , allowing the user to specify an attribute name/path or a `callable` for extracting feature importance from the estimator. [#15361](https://github.com/scikit-learn/scikit-learn/pull/15361)
     by [Venkatachalam N](https://github.com/venkyyuvy)
    .
    
*   Efficiency Reduce memory footprint in [`feature_selection.mutual_info_classif`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#sklearn.feature_selection.mutual_info_classif "sklearn.feature_selection.mutual_info_classif")
     and [`feature_selection.mutual_info_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html#sklearn.feature_selection.mutual_info_regression "sklearn.feature_selection.mutual_info_regression")
     by calling [`neighbors.KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
     for counting nearest neighbors. [#17878](https://github.com/scikit-learn/scikit-learn/pull/17878)
     by [Noel Rogers](https://github.com/noelano)
    .
    
*   Enhancement [`feature_selection.RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
     supports the option for the number of `n_features_to_select` to be given as a float representing the percentage of features to select. [#17090](https://github.com/scikit-learn/scikit-learn/pull/17090)
     by [Lisa Schwetlick](https://github.com/lschwetlick)
     and [Marija Vlajic Wheeler](https://github.com/marijavlajic)
    .
    

#### [`sklearn.gaussian_process`](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#module-sklearn.gaussian_process "sklearn.gaussian_process")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id10 "Link to this heading")

*   Enhancement A new method `gaussian_process.kernel._check_bounds_params` is called after fitting a Gaussian Process and raises a `ConvergenceWarning` if the bounds of the hyperparameters are too tight. [#12638](https://github.com/scikit-learn/scikit-learn/issues/12638)
     by [Sylvain Lannuzel](https://github.com/SylvainLan)
    .
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-impute "Link to this heading")

*   Feature [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     now supports a list of strings when `strategy='most_frequent'` or `strategy='constant'`. [#17526](https://github.com/scikit-learn/scikit-learn/pull/17526)
     by [Ayako YAGI](https://github.com/yagi-3)
     and [Juan Carlos Alfaro Jiménez](https://github.com/alfaro96)
    .
    
*   Feature Added method [`impute.SimpleImputer.inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer.inverse_transform "sklearn.impute.SimpleImputer.inverse_transform")
     to revert imputed data to original when instantiated with `add_indicator=True`. [#17612](https://github.com/scikit-learn/scikit-learn/pull/17612)
     by [Srimukh Sripada](https://github.com/d3b0unce)
    .
    
*   Fix replace the default values in [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     of `min_value` and `max_value` parameters to `-np.inf` and `np.inf`, respectively instead of `None`. However, the behaviour of the class does not change since `None` was defaulting to these values already. [#16493](https://github.com/scikit-learn/scikit-learn/pull/16493)
     by [Darshan N](https://github.com/DarshanGowda0)
    .
    
*   Fix [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     will not attempt to set the estimator’s `random_state` attribute, allowing to use it with more external classes. [#15636](https://github.com/scikit-learn/scikit-learn/pull/15636)
     by [David Cortes](https://github.com/david-cortes)
    .
    
*   Efficiency [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     is now faster with `object` dtype array. when `strategy='most_frequent'` in [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
    . [#18987](https://github.com/scikit-learn/scikit-learn/pull/18987)
     by [David Katz](https://github.com/DavidKatz-il)
    .
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-inspection "Link to this heading")

*   Feature [`inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
     and `inspection.plot_partial_dependence` now support calculating and plotting Individual Conditional Expectation (ICE) curves controlled by the `kind` parameter. [#16619](https://github.com/scikit-learn/scikit-learn/pull/16619)
     by [Madhura Jayratne](https://github.com/madhuracj)
    .
    
*   Feature Add `sample_weight` parameter to [`inspection.permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
    . [#16906](https://github.com/scikit-learn/scikit-learn/pull/16906)
     by [Roei Kahny](https://github.com/RoeiKa)
    .
    
*   API Change Positional arguments are deprecated in [`inspection.PartialDependenceDisplay.plot`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.plot "sklearn.inspection.PartialDependenceDisplay.plot")
     and will error in 1.1 (renaming of 0.26). [#18293](https://github.com/scikit-learn/scikit-learn/pull/18293)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.isotonic`](https://scikit-learn.org/stable/api/sklearn.isotonic.html#module-sklearn.isotonic "sklearn.isotonic")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-isotonic "Link to this heading")

*   Feature Expose fitted attributes `X_thresholds_` and `y_thresholds_` that hold the de-duplicated interpolation thresholds of an [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
     instance for model inspection purpose. [#16289](https://github.com/scikit-learn/scikit-learn/pull/16289)
     by [Masashi Kishimoto](https://github.com/kishimoto-banana)
     and [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Enhancement [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
     now accepts 2d array with 1 feature as input array. [#17379](https://github.com/scikit-learn/scikit-learn/pull/17379)
     by [Jiaxiang](https://github.com/fujiaxiang)
    .
    
*   Fix Add tolerance when determining duplicate X values to prevent inf values from being predicted by [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
    . [#18639](https://github.com/scikit-learn/scikit-learn/pull/18639)
     by [Lucy Liu](https://github.com/lucyleeow)
    .
    

#### [`sklearn.kernel_approximation`](https://scikit-learn.org/stable/api/sklearn.kernel_approximation.html#module-sklearn.kernel_approximation "sklearn.kernel_approximation")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-kernel-approximation "Link to this heading")

*   Feature Added class [`kernel_approximation.PolynomialCountSketch`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch "sklearn.kernel_approximation.PolynomialCountSketch")
     which implements the Tensor Sketch algorithm for polynomial kernel feature map approximation. [#13003](https://github.com/scikit-learn/scikit-learn/pull/13003)
     by [Daniel López Sánchez](https://github.com/lopeLH)
    .
    
*   Efficiency [`kernel_approximation.Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
     now supports parallelization via `joblib.Parallel` using argument `n_jobs`. [#18545](https://github.com/scikit-learn/scikit-learn/pull/18545)
     by [Laurenz Reitsam](https://github.com/LaurenzReitsam)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id11 "Link to this heading")

*   Feature [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
     now forces coefficients to be all positive when `positive` is set to `True`. [#17578](https://github.com/scikit-learn/scikit-learn/pull/17578)
     by [Joseph Knox](https://github.com/jknox13)
    , [Nelle Varoquaux](https://github.com/NelleV)
     and [Chiara Marmo](https://github.com/cmarmo)
    .
    
*   Enhancement [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     now supports finding an optimal regularization value `alpha` for each target separately by setting `alpha_per_target=True`. This is only supported when using the default efficient leave-one-out cross-validation scheme `cv=None`. [#6624](https://github.com/scikit-learn/scikit-learn/pull/6624)
     by [Marijn van Vliet](https://github.com/wmvanvliet)
    .
    
*   Fix Fixes bug in [`linear_model.TheilSenRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "sklearn.linear_model.TheilSenRegressor")
     where `predict` and `score` would fail when `fit_intercept=False` and there was one feature during fitting. [#18121](https://github.com/scikit-learn/scikit-learn/pull/18121)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Fixes bug in [`linear_model.ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
     where `predict` was raising an error when `normalize=True` and `return_std=True` because `X_offset_` and `X_scale_` were undefined. [#18607](https://github.com/scikit-learn/scikit-learn/pull/18607)
     by [fhaselbeck](https://github.com/fhaselbeck)
    .
    
*   Fix Added the missing `l1_ratio` parameter in [`linear_model.Perceptron`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron")
    , to be used when `penalty='elasticnet'`. This changes the default from 0 to 0.15. [#18622](https://github.com/scikit-learn/scikit-learn/pull/18622)
     by [Haesun Park](https://github.com/rickiepark)
    .
    

#### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-manifold "Link to this heading")

*   Efficiency Fixed [#10493](https://github.com/scikit-learn/scikit-learn/issues/10493)
    . Improve Local Linear Embedding (LLE) that raised `MemoryError` exception when used with large inputs. [#17997](https://github.com/scikit-learn/scikit-learn/pull/17997)
     by [Bertrand Maisonneuve](https://github.com/bmaisonn)
    .
    
*   Enhancement Add `square_distances` parameter to [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
    , which provides backward compatibility during deprecation of legacy squaring behavior. Distances will be squared by default in 1.1 (renaming of 0.26), and this parameter will be removed in 1.3. [#17662](https://github.com/scikit-learn/scikit-learn/pull/17662)
     by [Joshua Newton](https://github.com/joshuacwnewton)
    .
    
*   Fix [`manifold.MDS`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
     now correctly sets its `_pairwise` attribute. [#18278](https://github.com/scikit-learn/scikit-learn/pull/18278)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id12 "Link to this heading")

*   Feature Added [`metrics.cluster.pair_confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html#sklearn.metrics.cluster.pair_confusion_matrix "sklearn.metrics.cluster.pair_confusion_matrix")
     implementing the confusion matrix arising from pairs of elements from two clusterings. [#17412](https://github.com/scikit-learn/scikit-learn/pull/17412)
     by [Uwe F Mayer](https://github.com/ufmayer)
    .
    
*   Feature new metric [`metrics.top_k_accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html#sklearn.metrics.top_k_accuracy_score "sklearn.metrics.top_k_accuracy_score")
    . It’s a generalization of [`metrics.top_k_accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html#sklearn.metrics.top_k_accuracy_score "sklearn.metrics.top_k_accuracy_score")
    , the difference is that a prediction is considered correct as long as the true label is associated with one of the `k` highest predicted scores. [`metrics.accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
     is the special case of `k = 1`. [#16625](https://github.com/scikit-learn/scikit-learn/pull/16625)
     by [Geoffrey Bolmier](https://github.com/gbolmier)
    .
    
*   Feature Added [`metrics.det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")
     to compute Detection Error Tradeoff curve classification metric. [#10591](https://github.com/scikit-learn/scikit-learn/pull/10591)
     by [Jeremy Karnowski](https://github.com/jkarnows)
     and [Daniel Mohns](https://github.com/dmohns)
    .
    
*   Feature Added `metrics.plot_det_curve` and [`metrics.DetCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay "sklearn.metrics.DetCurveDisplay")
     to ease the plot of DET curves. [#18176](https://github.com/scikit-learn/scikit-learn/pull/18176)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Feature Added [`metrics.mean_absolute_percentage_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html#sklearn.metrics.mean_absolute_percentage_error "sklearn.metrics.mean_absolute_percentage_error")
     metric and the associated scorer for regression problems. [#10708](https://github.com/scikit-learn/scikit-learn/issues/10708)
     fixed with the PR [#15007](https://github.com/scikit-learn/scikit-learn/pull/15007)
     by [Ashutosh Hathidara](https://github.com/ashutosh1919)
    . The scorer and some practical test cases were taken from PR [#10711](https://github.com/scikit-learn/scikit-learn/pull/10711)
     by [Mohamed Ali Jamaoui](https://github.com/mohamed-ali)
    .
    
*   Feature Added [`metrics.rand_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#sklearn.metrics.rand_score "sklearn.metrics.rand_score")
     implementing the (unadjusted) Rand index. [#17412](https://github.com/scikit-learn/scikit-learn/pull/17412)
     by [Uwe F Mayer](https://github.com/ufmayer)
    .
    
*   Feature `metrics.plot_confusion_matrix` now supports making colorbar optional in the matplotlib plot by setting `colorbar=False`. [#17192](https://github.com/scikit-learn/scikit-learn/pull/17192)
     by [Avi Gupta](https://github.com/avigupta2612)
    
*   Enhancement Add `sample_weight` parameter to [`metrics.median_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")
    . [#17225](https://github.com/scikit-learn/scikit-learn/pull/17225)
     by [Lucy Liu](https://github.com/lucyleeow)
    .
    
*   Enhancement Add `pos_label` parameter in `metrics.plot_precision_recall_curve` in order to specify the positive class to be used when computing the precision and recall statistics. [#17569](https://github.com/scikit-learn/scikit-learn/pull/17569)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Enhancement Add `pos_label` parameter in `metrics.plot_roc_curve` in order to specify the positive class to be used when computing the roc auc statistics. [#17651](https://github.com/scikit-learn/scikit-learn/pull/17651)
     by [Clara Matos](https://github.com/claramatos)
    .
    
*   Fix Fixed a bug in [`metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
     which was raising AttributeError when called with `output_dict=True` for 0-length values. [#17777](https://github.com/scikit-learn/scikit-learn/pull/17777)
     by [Shubhanshu Mishra](https://github.com/napsternxg)
    .
    
*   Fix Fixed a bug in [`metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
     which was raising AttributeError when called with `output_dict=True` for 0-length values. [#17777](https://github.com/scikit-learn/scikit-learn/pull/17777)
     by [Shubhanshu Mishra](https://github.com/napsternxg)
    .
    
*   Fix Fixed a bug in [`metrics.jaccard_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")
     which recommended the `zero_division` parameter when called with no true or predicted samples. [#17826](https://github.com/scikit-learn/scikit-learn/pull/17826)
     by [Richard Decal](https://github.com/crypdick)
     and [Joseph Willard](https://github.com/josephwillard)
    
*   Fix bug in [`metrics.hinge_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hinge_loss.html#sklearn.metrics.hinge_loss "sklearn.metrics.hinge_loss")
     where error occurs when `y_true` is missing some labels that are provided explicitly in the `labels` parameter. [#17935](https://github.com/scikit-learn/scikit-learn/pull/17935)
     by [Cary Goltermann](https://github.com/Ultramann)
    .
    
*   Fix Fix scorers that accept a pos\_label parameter and compute their metrics from values returned by `decision_function` or `predict_proba`. Previously, they would return erroneous values when pos\_label was not corresponding to `classifier.classes_[1]`. This is especially important when training classifiers directly with string labeled target classes. [#18114](https://github.com/scikit-learn/scikit-learn/pull/18114)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Fixed bug in `metrics.plot_confusion_matrix` where error occurs when `y_true` contains labels that were not previously seen by the classifier while the `labels` and `display_labels` parameters are set to `None`. [#18405](https://github.com/scikit-learn/scikit-learn/pull/18405)
     by [Thomas J. Fan](https://github.com/thomasjpfan)
     and [Yakov Pchelintsev](https://github.com/kyouma)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id13 "Link to this heading")

*   Major Feature Added (experimental) parameter search estimators [`model_selection.HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
     and [`model_selection.HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
     which implement Successive Halving, and can be used as a drop-in replacements for [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     and [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    . [#13900](https://github.com/scikit-learn/scikit-learn/pull/13900)
     by [Nicolas Hug](https://github.com/NicolasHug)
    , [Joel Nothman](https://joelnothman.com/)
     and [Andreas Müller](https://amueller.github.io/)
    .
    
*   Feature [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     and [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     now have the method `score_samples` [#17478](https://github.com/scikit-learn/scikit-learn/pull/17478)
     by [Teon Brooks](https://github.com/teonbrooks)
     and [Mohamed Maskani](https://github.com/maskani-moh)
    .
    
*   Enhancement [`model_selection.TimeSeriesSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")
     has two new keyword arguments `test_size` and `gap`. `test_size` allows the out-of-sample time series length to be fixed for all folds. `gap` removes a fixed number of samples between the train and test set on each fold. [#13204](https://github.com/scikit-learn/scikit-learn/pull/13204)
     by [Kyle Kosic](https://github.com/kykosic)
    .
    
*   Enhancement [`model_selection.permutation_test_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#sklearn.model_selection.permutation_test_score "sklearn.model_selection.permutation_test_score")
     and [`model_selection.validation_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve "sklearn.model_selection.validation_curve")
     now accept fit\_params to pass additional estimator parameters. [#18527](https://github.com/scikit-learn/scikit-learn/pull/18527)
     by [Gaurav Dhingra](https://github.com/gxyd)
    , [Julien Jerphanion](https://github.com/jjerphan)
     and [Amanda Dsouza](https://github.com/amy12xx)
    .
    
*   Enhancement [`model_selection.cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
    , [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
    , [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    , and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     allows estimator to fail scoring and replace the score with `error_score`. If `error_score="raise"`, the error will be raised. [#18343](https://github.com/scikit-learn/scikit-learn/pull/18343)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
     and [Devi Sandeep](https://github.com/dsandeep0138)
    .
    
*   Enhancement [`model_selection.learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
     now accept fit\_params to pass additional estimator parameters. [#18595](https://github.com/scikit-learn/scikit-learn/pull/18595)
     by [Amanda Dsouza](https://github.com/amy12xx)
    .
    
*   Fix Fixed the `len` of [`model_selection.ParameterSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterSampler.html#sklearn.model_selection.ParameterSampler "sklearn.model_selection.ParameterSampler")
     when all distributions are lists and `n_iter` is more than the number of unique parameter combinations. [#18222](https://github.com/scikit-learn/scikit-learn/pull/18222)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix A fix to raise warning when one or more CV splits of [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     results in non-finite scores. [#18266](https://github.com/scikit-learn/scikit-learn/pull/18266)
     by [Subrat Sahu](https://github.com/subrat93)
    , [Nirvan](https://github.com/Nirvan101)
     and [Arthur Book](https://github.com/ArthurBook)
    .
    
*   Enhancement [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    , [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     and [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
     support `scoring` being a callable returning a dictionary of multiple metric names/values association. [#15126](https://github.com/scikit-learn/scikit-learn/pull/15126)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.multiclass`](https://scikit-learn.org/stable/api/sklearn.multiclass.html#module-sklearn.multiclass "sklearn.multiclass")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-multiclass "Link to this heading")

*   Enhancement [`multiclass.OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
     now accepts the inputs with missing values. Hence, estimators which can handle missing values (may be a pipeline with imputation step) can be used as a estimator for multiclass wrappers. [#17987](https://github.com/scikit-learn/scikit-learn/pull/17987)
     by [Venkatachalam N](https://github.com/venkyyuvy)
    .
    
*   Fix A fix to allow [`multiclass.OutputCodeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier")
     to accept sparse input data in its `fit` and `predict` methods. The check for validity of the input is now delegated to the base estimator. [#17233](https://github.com/scikit-learn/scikit-learn/pull/17233)
     by [Zolisa Bleki](https://github.com/zoj613)
    .
    

#### [`sklearn.multioutput`](https://scikit-learn.org/stable/api/sklearn.multioutput.html#module-sklearn.multioutput "sklearn.multioutput")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id14 "Link to this heading")

*   Enhancement [`multioutput.MultiOutputClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier")
     and [`multioutput.MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")
     now accepts the inputs with missing values. Hence, estimators which can handle missing values (may be a pipeline with imputation step, HistGradientBoosting estimators) can be used as a estimator for multiclass wrappers. [#17987](https://github.com/scikit-learn/scikit-learn/pull/17987)
     by [Venkatachalam N](https://github.com/venkyyuvy)
    .
    
*   Fix A fix to accept tuples for the `order` parameter in [`multioutput.ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
    . [#18124](https://github.com/scikit-learn/scikit-learn/pull/18124)
     by [Gus Brocchini](https://github.com/boldloop)
     and [Amanda Dsouza](https://github.com/amy12xx)
    .
    

#### [`sklearn.naive_bayes`](https://scikit-learn.org/stable/api/sklearn.naive_bayes.html#module-sklearn.naive_bayes "sklearn.naive_bayes")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-naive-bayes "Link to this heading")

*   Enhancement Adds a parameter `min_categories` to [`naive_bayes.CategoricalNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html#sklearn.naive_bayes.CategoricalNB "sklearn.naive_bayes.CategoricalNB")
     that allows a minimum number of categories per feature to be specified. This allows categories unseen during training to be accounted for. [#16326](https://github.com/scikit-learn/scikit-learn/pull/16326)
     by [George Armstrong](https://github.com/gwarmstrong)
    .
    
*   API Change The attributes `coef_` and `intercept_` are now deprecated in [`naive_bayes.MultinomialNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB "sklearn.naive_bayes.MultinomialNB")
    , [`naive_bayes.ComplementNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html#sklearn.naive_bayes.ComplementNB "sklearn.naive_bayes.ComplementNB")
    , [`naive_bayes.BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
     and [`naive_bayes.CategoricalNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html#sklearn.naive_bayes.CategoricalNB "sklearn.naive_bayes.CategoricalNB")
    , and will be removed in v1.1 (renaming of 0.26). [#17427](https://github.com/scikit-learn/scikit-learn/pull/17427)
     by [Juan Carlos Alfaro Jiménez](https://github.com/alfaro96)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-neighbors "Link to this heading")

*   Efficiency Speed up `seuclidean`, `wminkowski`, `mahalanobis` and `haversine` metrics in `neighbors.DistanceMetric` by avoiding unexpected GIL acquiring in Cython when setting `n_jobs>1` in [`neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
    , [`neighbors.KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
    , [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
    , [`neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
    , [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     and by validating data out of loops. [#17038](https://github.com/scikit-learn/scikit-learn/pull/17038)
     by [Wenbo Zhao](https://github.com/webber26232)
    .
    
*   Efficiency `neighbors.NeighborsBase` benefits of an improved `algorithm = 'auto'` heuristic. In addition to the previous set of rules, now, when the number of features exceeds 15, `brute` is selected, assuming the data intrinsic dimensionality is too high for tree-based methods. [#17148](https://github.com/scikit-learn/scikit-learn/pull/17148)
     by [Geoffrey Bolmier](https://github.com/gbolmier)
    .
    
*   Fix `neighbors.BinaryTree` will raise a `ValueError` when fitting on data array having points with different dimensions. [#18691](https://github.com/scikit-learn/scikit-learn/pull/18691)
     by [Chiara Marmo](https://github.com/cmarmo)
    .
    
*   Fix [`neighbors.NearestCentroid`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")
     with a numerical `shrink_threshold` will raise a `ValueError` when fitting on data with all constant features. [#18370](https://github.com/scikit-learn/scikit-learn/pull/18370)
     by [Trevor Waite](https://github.com/trewaite)
    .
    
*   Fix In methods `radius_neighbors` and `radius_neighbors_graph` of [`neighbors.NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
    , [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
    , [`neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
    , and [`neighbors.RadiusNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer "sklearn.neighbors.RadiusNeighborsTransformer")
    , using `sort_results=True` now correctly sorts the results even when fitting with the “brute” algorithm. [#18612](https://github.com/scikit-learn/scikit-learn/pull/18612)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    

#### [`sklearn.neural_network`](https://scikit-learn.org/stable/api/sklearn.neural_network.html#module-sklearn.neural_network "sklearn.neural_network")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-neural-network "Link to this heading")

*   Efficiency Neural net training and prediction are now a little faster. [#17603](https://github.com/scikit-learn/scikit-learn/pull/17603)
    , [#17604](https://github.com/scikit-learn/scikit-learn/pull/17604)
    , [#17606](https://github.com/scikit-learn/scikit-learn/pull/17606)
    , [#17608](https://github.com/scikit-learn/scikit-learn/pull/17608)
    , [#17609](https://github.com/scikit-learn/scikit-learn/pull/17609)
    , [#17633](https://github.com/scikit-learn/scikit-learn/pull/17633)
    , [#17661](https://github.com/scikit-learn/scikit-learn/pull/17661)
    , [#17932](https://github.com/scikit-learn/scikit-learn/pull/17932)
     by [Alex Henrie](https://github.com/alexhenrie)
    .
    
*   Enhancement Avoid converting float32 input to float64 in [`neural_network.BernoulliRBM`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM "sklearn.neural_network.BernoulliRBM")
    . [#16352](https://github.com/scikit-learn/scikit-learn/pull/16352)
     by [Arthur Imbert](https://github.com/Henley13)
    .
    
*   Enhancement Support 32-bit computations in [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     and [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
    . [#17759](https://github.com/scikit-learn/scikit-learn/pull/17759)
     by [Srimukh Sripada](https://github.com/d3b0unce)
    .
    
*   Fix Fix method [`neural_network.MLPClassifier.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier.fit "sklearn.neural_network.MLPClassifier.fit")
     not iterating to `max_iter` if warm started. [#18269](https://github.com/scikit-learn/scikit-learn/pull/18269)
     by [Norbert Preining](https://github.com/norbusan)
     and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-pipeline "Link to this heading")

*   Enhancement References to transformers passed through `transformer_weights` to [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     that aren’t present in `transformer_list` will raise a `ValueError`. [#17876](https://github.com/scikit-learn/scikit-learn/pull/17876)
     by [Cary Goltermann](https://github.com/Ultramann)
    .
    
*   Fix A slice of a [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     now inherits the parameters of the original pipeline (`memory` and `verbose`). [#18429](https://github.com/scikit-learn/scikit-learn/pull/18429)
     by [Albert Villanova del Moral](https://github.com/albertvillanova)
     and [Paweł Biernat](https://github.com/pwl)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id15 "Link to this heading")

*   Feature [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     now supports missing values by treating them as a category. [#17317](https://github.com/scikit-learn/scikit-learn/pull/17317)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature Add a new `handle_unknown` parameter with a `use_encoded_value` option, along with a new `unknown_value` parameter, to [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     to allow unknown categories during transform and set the encoded value of the unknown categories. [#17406](https://github.com/scikit-learn/scikit-learn/pull/17406)
     by [Felix Wick](https://github.com/FelixWick)
     and [#18406](https://github.com/scikit-learn/scikit-learn/pull/18406)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Feature Add `clip` parameter to [`preprocessing.MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
    , which clips the transformed values of test data to `feature_range`. [#17833](https://github.com/scikit-learn/scikit-learn/pull/17833)
     by [Yashika Sharma](https://github.com/yashika51)
    .
    
*   Feature Add `sample_weight` parameter to [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
    . Allows setting individual weights for each sample. [#18510](https://github.com/scikit-learn/scikit-learn/pull/18510)
     and [#18447](https://github.com/scikit-learn/scikit-learn/pull/18447)
     and [#16066](https://github.com/scikit-learn/scikit-learn/pull/16066)
     and [#18682](https://github.com/scikit-learn/scikit-learn/pull/18682)
     by [Maria Telenczuk](https://github.com/maikia)
     and [Albert Villanova](https://github.com/albertvillanova)
     and [@panpiort8](https://github.com/panpiort8)
     and [Alex Gramfort](https://github.com/agramfort)
    .
    
*   Enhancement Verbose output of [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     has been improved for readability. [#16935](https://github.com/scikit-learn/scikit-learn/pull/16935)
     by [Raghav Rajagopalan](https://github.com/raghavrv)
     and [Chiara Marmo](https://github.com/cmarmo)
    .
    
*   Enhancement Add `unit_variance` to [`preprocessing.RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
    , which scales output data such that normally distributed features have a variance of 1. [#17193](https://github.com/scikit-learn/scikit-learn/pull/17193)
     by [Lucy Liu](https://github.com/lucyleeow)
     and [Mabel Villalba](https://github.com/mabelvj)
    .
    
*   Enhancement Add `dtype` parameter to [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
    . [#16335](https://github.com/scikit-learn/scikit-learn/pull/16335)
     by [Arthur Imbert](https://github.com/Henley13)
    .
    
*   Fix Raise error on [`sklearn.preprocessing.OneHotEncoder.inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.inverse_transform "sklearn.preprocessing.OneHotEncoder.inverse_transform")
     when `handle_unknown='error'` and `drop=None` for samples encoded as all zeros. [#14982](https://github.com/scikit-learn/scikit-learn/pull/14982)
     by [Kevin Winata](https://github.com/kwinata)
    .
    

#### [`sklearn.semi_supervised`](https://scikit-learn.org/stable/api/sklearn.semi_supervised.html#module-sklearn.semi_supervised "sklearn.semi_supervised")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id16 "Link to this heading")

*   Major Feature Added [`semi_supervised.SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
    , a meta-classifier that allows any supervised classifier to function as a semi-supervised classifier that can learn from unlabeled data. [#11682](https://github.com/scikit-learn/scikit-learn/issues/11682)
     by [Oliver Rausch](https://github.com/orausch)
     and [Patrice Becker](https://github.com/pr0duktiv)
    .
    
*   Fix Fix incorrect encoding when using unicode string dtypes in [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     and [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
    . [#15763](https://github.com/scikit-learn/scikit-learn/pull/15763)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#sklearn-svm "Link to this heading")

*   Enhancement invoke SciPy BLAS API for SVM kernel function in `fit`, `predict` and related methods of [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
    , [`svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
    , [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
    , [`svm.NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
    , [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
    . [#16530](https://github.com/scikit-learn/scikit-learn/pull/16530)
     by [Shuhua Fan](https://github.com/jim0421)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id17 "Link to this heading")

*   Feature [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
     now supports the new splitting criterion `'poisson'` useful for modeling count data. [#17386](https://github.com/scikit-learn/scikit-learn/pull/17386)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Enhancement [`tree.plot_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree")
     now uses colors from the matplotlib configuration settings. [#17187](https://github.com/scikit-learn/scikit-learn/pull/17187)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   API Change The parameter `X_idx_sorted` is now deprecated in [`tree.DecisionTreeClassifier.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.fit "sklearn.tree.DecisionTreeClassifier.fit")
     and [`tree.DecisionTreeRegressor.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor.fit "sklearn.tree.DecisionTreeRegressor.fit")
    , and has no effect. [#17614](https://github.com/scikit-learn/scikit-learn/pull/17614)
     by [Juan Carlos Alfaro Jiménez](https://github.com/alfaro96)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v0.24.html#id18 "Link to this heading")

*   Enhancement Add `check_methods_sample_order_invariance` to [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
    , which checks that estimator methods are invariant if applied to the same dataset with different sample order [#17598](https://github.com/scikit-learn/scikit-learn/pull/17598)
     by [Jason Ngo](https://github.com/ngojason9)
    .
    
*   Enhancement Add support for weights in `utils.sparse_func.incr_mean_variance_axis`. By [Maria Telenczuk](https://github.com/maikia)
     and [Alex Gramfort](https://github.com/agramfort)
    .
    
*   Fix Raise ValueError with clear error message in [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     for sparse DataFrames with mixed types. [#17992](https://github.com/scikit-learn/scikit-learn/pull/17992)
     by [Thomas J. Fan](https://github.com/thomasjpfan)
     and [Alex Shacked](https://github.com/alexshacked)
    .
    
*   Fix Allow serialized tree based models to be unpickled on a machine with different endianness. [#17644](https://github.com/scikit-learn/scikit-learn/pull/17644)
     by [Qi Zhang](https://github.com/qzhang90)
    .
    
*   Fix Check that we raise proper error when axis=1 and the dimensions do not match in `utils.sparse_func.incr_mean_variance_axis`. By [Alex Gramfort](https://github.com/agramfort)
    .
    

#### Miscellaneous[#](https://scikit-learn.org/stable/whats_new/v0.24.html#miscellaneous "Link to this heading")

*   Enhancement Calls to `repr` are now faster when `print_changed_only=True`, especially with meta-estimators. [#18508](https://github.com/scikit-learn/scikit-learn/pull/18508)
     by [Nathan C.](https://github.com/Xethan)
    .
    

Code and documentation contributors

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 0.23, including:

Abo7atm, Adam Spannbauer, Adrin Jalali, adrinjalali, Agamemnon Krasoulis, Akshay Deodhar, Albert Villanova del Moral, Alessandro Gentile, Alex Henrie, Alex Itkes, Alex Liang, Alexander Lenail, alexandracraciun, Alexandre Gramfort, alexshacked, Allan D Butler, Amanda Dsouza, amy12xx, Anand Tiwari, Anderson Nelson, Andreas Mueller, Ankit Choraria, Archana Subramaniyan, Arthur Imbert, Ashutosh Hathidara, Ashutosh Kushwaha, Atsushi Nukariya, Aura Munoz, AutoViz and Auto\_ViML, Avi Gupta, Avinash Anakal, Ayako YAGI, barankarakus, barberogaston, beatrizsmg, Ben Mainye, Benjamin Bossan, Benjamin Pedigo, Bharat Raghunathan, Bhavika Devnani, Biprateep Dey, bmaisonn, Bo Chang, Boris Villazón-Terrazas, brigi, Brigitta Sipőcz, Bruno Charron, Byron Smith, Cary Goltermann, Cat Chenal, CeeThinwa, chaitanyamogal, Charles Patel, Chiara Marmo, Christian Kastner, Christian Lorentzen, Christoph Deil, Christos Aridas, Clara Matos, clmbst, Coelhudo, crispinlogan, Cristina Mulas, Daniel López, Daniel Mohns, darioka, Darshan N, david-cortes, Declan O’Neill, Deeksha Madan, Elizabeth DuPre, Eric Fiegel, Eric Larson, Erich Schubert, Erin Khoo, Erin R Hoffman, eschibli, Felix Wick, fhaselbeck, Forrest Koch, Francesco Casalegno, Frans Larsson, Gael Varoquaux, Gaurav Desai, Gaurav Sheni, genvalen, Geoffrey Bolmier, George Armstrong, George Kiragu, Gesa Stupperich, Ghislain Antony Vaillant, Gim Seng, Gordon Walsh, Gregory R. Lee, Guillaume Chevalier, Guillaume Lemaitre, Haesun Park, Hannah Bohle, Hao Chun Chang, Harry Scholes, Harsh Soni, Henry, Hirofumi Suzuki, Hitesh Somani, Hoda1394, Hugo Le Moine, hugorichard, indecisiveuser, Isuru Fernando, Ivan Wiryadi, j0rd1smit, Jaehyun Ahn, Jake Tae, James Hoctor, Jan Vesely, Jeevan Anand Anne, JeroenPeterBos, JHayes, Jiaxiang, Jie Zheng, Jigna Panchal, jim0421, Jin Li, Joaquin Vanschoren, Joel Nothman, Jona Sassenhagen, Jonathan, Jorge Gorbe Moya, Joseph Lucas, Joshua Newton, Juan Carlos Alfaro Jiménez, Julien Jerphanion, Justin Huber, Jérémie du Boisberranger, Kartik Chugh, Katarina Slama, kaylani2, Kendrick Cetina, Kenny Huynh, Kevin Markham, Kevin Winata, Kiril Isakov, kishimoto, Koki Nishihara, Krum Arnaudov, Kyle Kosic, Lauren Oldja, Laurenz Reitsam, Lisa Schwetlick, Louis Douge, Louis Guitton, Lucy Liu, Madhura Jayaratne, maikia, Manimaran, Manuel López-Ibáñez, Maren Westermann, Maria Telenczuk, Mariam-ke, Marijn van Vliet, Markus Löning, Martin Scheubrein, Martina G. Vilas, Martina Megasari, Mateusz Górski, mathschy, mathurinm, Matthias Bussonnier, Max Del Giudice, Michael, Milan Straka, Muoki Caleb, N. Haiat, Nadia Tahiri, Ph. D, Naoki Hamada, Neil Botelho, Nicolas Hug, Nils Werner, noelano, Norbert Preining, oj\_lappi, Oleh Kozynets, Olivier Grisel, Pankaj Jindal, Pardeep Singh, Parthiv Chigurupati, Patrice Becker, Pete Green, pgithubs, Poorna Kumar, Prabakaran Kumaresshan, Probinette4, pspachtholz, pwalchessen, Qi Zhang, rachel fischoff, Rachit Toshniwal, Rafey Iqbal Rahman, Rahul Jakhar, Ram Rachum, RamyaNP, rauwuckl, Ravi Kiran Boggavarapu, Ray Bell, Reshama Shaikh, Richard Decal, Rishi Advani, Rithvik Rao, Rob Romijnders, roei, Romain Tavenard, Roman Yurchak, Ruby Werman, Ryotaro Tsukada, sadak, Saket Khandelwal, Sam, Sam Ezebunandu, Sam Kimbinyi, Sarah Brown, Saurabh Jain, Sean O. Stalley, Sergio, Shail Shah, Shane Keller, Shao Yang Hong, Shashank Singh, Shooter23, Shubhanshu Mishra, simonamaggio, Soledad Galli, Srimukh Sripada, Stephan Steinfurt, subrat93, Sunitha Selvan, Swier, Sylvain Marié, SylvainLan, t-kusanagi2, Teon L Brooks, Terence Honles, Thijs van den Berg, Thomas J Fan, Thomas J. Fan, Thomas S Benjamin, Thomas9292, Thorben Jensen, tijanajovanovic, Timo Kaufmann, tnwei, Tom Dupré la Tour, Trevor Waite, ufmayer, Umberto Lupo, Venkatachalam N, Vikas Pandey, Vinicius Rios Fuck, Violeta, watchtheblur, Wenbo Zhao, willpeppo, xavier dupré, Xethan, Xue Qianming, xun-tang, yagi-3, Yakov Pchelintsev, Yashika Sharma, Yi-Yan Ge, Yue Wu, Yutaro Ikeda, Zaccharie Ramzi, zoj613, Zhao Feng.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)