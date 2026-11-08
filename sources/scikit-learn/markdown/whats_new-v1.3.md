[Skip to main content](https://scikit-learn.org/stable/whats_new/v1.3.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v1.3.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v1.3.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v1.3.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v1.3.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v1.3.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v1.3.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v1.3.html)

Collapse Sidebar Expand Sidebar

Version 1.3[#](https://scikit-learn.org/stable/whats_new/v1.3.html#version-1-3 "Link to this heading")

=======================================================================================================

For a short description of the main highlights of the release, please refer to [Release Highlights for scikit-learn 1.3](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html#sphx-glr-auto-examples-release-highlights-plot-release-highlights-1-3-0-py)
.

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 1.3.2[#](https://scikit-learn.org/stable/whats_new/v1.3.html#version-1-3-2 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**October 2023**

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.3.html#changelog "Link to this heading")

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-datasets "Link to this heading")

*   Fix All dataset fetchers now accept `data_home` as any object that implements the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")
     interface, for instance, [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")
    . [#27468](https://github.com/scikit-learn/scikit-learn/pull/27468)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-decomposition "Link to this heading")

*   Fix Fixes a bug in [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
     by forcing the output of the internal [`preprocessing.KernelCenterer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KernelCenterer.html#sklearn.preprocessing.KernelCenterer "sklearn.preprocessing.KernelCenterer")
     to be a default array. When the arpack solver is used, it expects an array with a `dtype` attribute. [#27583](https://github.com/scikit-learn/scikit-learn/pull/27583)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-metrics "Link to this heading")

*   Fix Fixes a bug for metrics using `zero_division=np.nan` (e.g. [`precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")
    ) within a parallel loop (e.g. [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
    ) where the singleton for `np.nan` will be different in the sub-processes. [#27573](https://github.com/scikit-learn/scikit-learn/pull/27573)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-tree "Link to this heading")

*   Fix Do not leak data via non-initialized memory in decision tree pickle files and make the generation of those files deterministic. [#27580](https://github.com/scikit-learn/scikit-learn/pull/27580)
     by [Loïc Estève](https://github.com/lesteve)
    .
    

Version 1.3.1[#](https://scikit-learn.org/stable/whats_new/v1.3.html#version-1-3-1 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**September 2023**

### Changed models[#](https://scikit-learn.org/stable/whats_new/v1.3.html#changed-models "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   Fix Ridge models with `solver='sparse_cg'` may have slightly different results with scipy>=1.12, because of an underlying change in the scipy solver (see [scipy#18488](https://github.com/scipy/scipy/pull/18488)
     for more details) [#26814](https://github.com/scikit-learn/scikit-learn/pull/26814)
     by [Loïc Estève](https://github.com/lesteve)
    

### Changes impacting all modules[#](https://scikit-learn.org/stable/whats_new/v1.3.html#changes-impacting-all-modules "Link to this heading")

*   Fix The `set_output` API correctly works with list input. [#27044](https://github.com/scikit-learn/scikit-learn/pull/27044)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id1 "Link to this heading")

#### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-calibration "Link to this heading")

*   Fix [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     can now handle models that produce large prediction scores. Before it was numerically unstable. [#26913](https://github.com/scikit-learn/scikit-learn/pull/26913)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-cluster "Link to this heading")

*   Fix [`cluster.BisectingKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans")
     could crash when predicting on data with a different scale than the data used to fit the model. [#27167](https://github.com/scikit-learn/scikit-learn/pull/27167)
     by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Fix [`cluster.BisectingKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans")
     now works with data that has a single feature. [#27243](https://github.com/scikit-learn/scikit-learn/pull/27243)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.cross_decomposition`](https://scikit-learn.org/stable/api/sklearn.cross_decomposition.html#module-sklearn.cross_decomposition "sklearn.cross_decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-cross-decomposition "Link to this heading")

*   Fix [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
     now automatically ravels the output of `predict` if fitted with one dimensional `y`. [#26602](https://github.com/scikit-learn/scikit-learn/pull/26602)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-ensemble "Link to this heading")

*   Fix Fix a bug in [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
     with `algorithm="SAMME"` where the decision function of each weak learner should be symmetric (i.e. the sum of the scores should sum to zero for a sample). [#26521](https://github.com/scikit-learn/scikit-learn/pull/26521)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-feature-selection "Link to this heading")

*   Fix [`feature_selection.mutual_info_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html#sklearn.feature_selection.mutual_info_regression "sklearn.feature_selection.mutual_info_regression")
     now correctly computes the result when `X` is of integer dtype. [#26748](https://github.com/scikit-learn/scikit-learn/pull/26748)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-impute "Link to this heading")

*   Fix [`impute.KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
     now correctly adds a missing indicator column in `transform` when `add_indicator` is set to `True` and missing values are observed during `fit`. [#26600](https://github.com/scikit-learn/scikit-learn/pull/26600)
     by [Shreesha Kumar Bhat](https://github.com/Shreesha3112)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id2 "Link to this heading")

*   Fix Scorers used with [`metrics.get_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html#sklearn.metrics.get_scorer "sklearn.metrics.get_scorer")
     handle properly multilabel-indicator matrix. [#27002](https://github.com/scikit-learn/scikit-learn/pull/27002)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.mixture`](https://scikit-learn.org/stable/api/sklearn.mixture.html#module-sklearn.mixture "sklearn.mixture")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-mixture "Link to this heading")

*   Fix The initialization of [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     from user-provided `precisions_init` for `covariance_type` of `full` or `tied` was not correct, and has been fixed. [#26416](https://github.com/scikit-learn/scikit-learn/pull/26416)
     by [Yang Tao](https://github.com/mchikyt3)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-neighbors "Link to this heading")

*   Fix [`neighbors.KNeighborsClassifier.predict`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.predict "sklearn.neighbors.KNeighborsClassifier.predict")
     no longer raises an exception for `pandas.DataFrames` input. [#26772](https://github.com/scikit-learn/scikit-learn/pull/26772)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix Reintroduce `sklearn.neighbors.BallTree.valid_metrics` and `sklearn.neighbors.KDTree.valid_metrics` as public class attributes. [#26754](https://github.com/scikit-learn/scikit-learn/pull/26754)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Fix [`sklearn.model_selection.HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
     no longer raises when the input to the `param_distributions` parameter is a list of dicts. [#26893](https://github.com/scikit-learn/scikit-learn/pull/26893)
     by [Stefanie Senger](https://github.com/StefanieSenger)
    .
    
*   Fix Neighbors based estimators now correctly work when `metric="minkowski"` and the metric parameter `p` is in the range `0 < p < 1`, regardless of the `dtype` of `X`. [#26760](https://github.com/scikit-learn/scikit-learn/pull/26760)
     by [Shreesha Kumar Bhat](https://github.com/Shreesha3112)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-preprocessing "Link to this heading")

*   Fix [`preprocessing.LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder")
     correctly accepts `y` as a keyword argument. [#26940](https://github.com/scikit-learn/scikit-learn/pull/26940)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     shows a more informative error message when `sparse_output=True` and the output is configured to be pandas. [#26931](https://github.com/scikit-learn/scikit-learn/pull/26931)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id3 "Link to this heading")

*   Fix [`tree.plot_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree")
     now accepts `class_names=True` as documented. [#26903](https://github.com/scikit-learn/scikit-learn/pull/26903)
     by [Thomas Roehr](https://github.com/2maz)
    
*   Fix The `feature_names` parameter of [`tree.plot_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree")
     now accepts any kind of array-like instead of just a list. [#27292](https://github.com/scikit-learn/scikit-learn/pull/27292)
     by [Rahil Parikh](https://github.com/rprkh)
    .
    

Version 1.3.0[#](https://scikit-learn.org/stable/whats_new/v1.3.html#version-1-3-0 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**June 2023**

### Changed models[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id4 "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   Enhancement [`multiclass.OutputCodeClassifier.predict`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier.predict "sklearn.multiclass.OutputCodeClassifier.predict")
     now uses a more efficient pairwise distance reduction. As a consequence, the tie-breaking strategy is different and thus the predicted labels may be different. [#25196](https://github.com/scikit-learn/scikit-learn/pull/25196)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Enhancement The `fit_transform` method of [`decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
     is more efficient but may produce different results as in previous versions when `transform_algorithm` is not the same as `fit_algorithm` and the number of iterations is small. [#24871](https://github.com/scikit-learn/scikit-learn/pull/24871)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    
*   Enhancement The `sample_weight` parameter now will be used in centroids initialization for [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    , [`cluster.BisectingKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans")
     and [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
    . This change will break backward compatibility, since numbers generated from same random seeds will be different. [#25752](https://github.com/scikit-learn/scikit-learn/pull/25752)
     by [Hleb Levitski](https://github.com/glevv)
    , [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    , [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Treat more consistently small values in the `W` and `H` matrices during the `fit` and `transform` steps of [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     and [`decomposition.MiniBatchNMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")
     which can produce different results than previous versions. [#25438](https://github.com/scikit-learn/scikit-learn/pull/25438)
     by [Yotam Avidar-Constantini](https://github.com/yotamcons)
    .
    
*   Fix [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
     may produce different results through `inverse_transform` if `gamma` is `None`. Now it will be chosen correctly as `1/n_features` of the data that it is fitted on, while previously it might be incorrectly chosen as `1/n_features` of the data passed to `inverse_transform`. A new attribute `gamma_` is provided for revealing the actual value of `gamma` used each time the kernel is called. [#26337](https://github.com/scikit-learn/scikit-learn/pull/26337)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    

### Changed displays[#](https://scikit-learn.org/stable/whats_new/v1.3.html#changed-displays "Link to this heading")

*   Enhancement [`model_selection.LearningCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay "sklearn.model_selection.LearningCurveDisplay")
     displays both the train and test curves by default. You can set `score_type="test"` to keep the past behaviour. [#25120](https://github.com/scikit-learn/scikit-learn/pull/25120)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`model_selection.ValidationCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ValidationCurveDisplay.html#sklearn.model_selection.ValidationCurveDisplay "sklearn.model_selection.ValidationCurveDisplay")
     now accepts passing a list to the `param_range` parameter. [#27311](https://github.com/scikit-learn/scikit-learn/pull/27311)
     by [Arturo Amor](https://github.com/ArturoAmorQ)
    .
    

### Changes impacting all modules[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id5 "Link to this heading")

*   Enhancement The `get_feature_names_out` method of the following classes now raises a `NotFittedError` if the instance is not fitted. This ensures the error is consistent in all estimators with the `get_feature_names_out` method.
    
    *   [`impute.MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")
        
    *   [`feature_extraction.DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
        
    *   [`feature_extraction.text.TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
        
    *   [`feature_selection.GenericUnivariateSelect`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect "sklearn.feature_selection.GenericUnivariateSelect")
        
    *   [`feature_selection.RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
        
    *   [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
        
    *   [`feature_selection.SelectFdr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFdr.html#sklearn.feature_selection.SelectFdr "sklearn.feature_selection.SelectFdr")
        
    *   [`feature_selection.SelectFpr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFpr.html#sklearn.feature_selection.SelectFpr "sklearn.feature_selection.SelectFpr")
        
    *   [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
        
    *   [`feature_selection.SelectFwe`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFwe.html#sklearn.feature_selection.SelectFwe "sklearn.feature_selection.SelectFwe")
        
    *   [`feature_selection.SelectKBest`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
        
    *   [`feature_selection.SelectPercentile`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile")
        
    *   [`feature_selection.SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
        
    *   [`feature_selection.VarianceThreshold`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html#sklearn.feature_selection.VarianceThreshold "sklearn.feature_selection.VarianceThreshold")
        
    *   [`kernel_approximation.AdditiveChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.AdditiveChi2Sampler.html#sklearn.kernel_approximation.AdditiveChi2Sampler "sklearn.kernel_approximation.AdditiveChi2Sampler")
        
    *   [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
        
    *   [`impute.KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
        
    *   [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
        
    *   [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
        
    *   [`preprocessing.Binarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Binarizer.html#sklearn.preprocessing.Binarizer "sklearn.preprocessing.Binarizer")
        
    *   [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
        
    *   [`preprocessing.MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")
        
    *   [`preprocessing.MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
        
    *   [`preprocessing.Normalizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer")
        
    *   [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
        
    *   [`preprocessing.PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
        
    *   [`preprocessing.QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
        
    *   [`preprocessing.RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
        
    *   [`preprocessing.SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
        
    *   [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
        
    *   [`random_projection.GaussianRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection "sklearn.random_projection.GaussianRandomProjection")
        
    *   [`random_projection.SparseRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection")
        
    
    The `NotFittedError` displays an informative message asking to fit the instance with the appropriate arguments.
    
    [#25294](https://github.com/scikit-learn/scikit-learn/pull/25294)
    , [#25308](https://github.com/scikit-learn/scikit-learn/pull/25308)
    , [#25291](https://github.com/scikit-learn/scikit-learn/pull/25291)
    , [#25367](https://github.com/scikit-learn/scikit-learn/pull/25367)
    , [#25402](https://github.com/scikit-learn/scikit-learn/pull/25402)
    , by [John Pangas](https://github.com/jpangas)
    , [Rahil Parikh](https://github.com/rprkh)
     , and [Alex Buzenet](https://github.com/albuzenet)
    .
    
*   Enhancement Added a multi-threaded Cython routine to the compute squared Euclidean distances (sometimes followed by a fused reduction operation) for a pair of datasets consisting of a sparse CSR matrix and a dense NumPy.
    
    This can improve the performance of following functions and estimators:
    
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
        
    
    A typical example of this performance improvement happens when passing a sparse CSR matrix to the `predict` or `transform` method of estimators that rely on a dense NumPy representation to store their fitted parameters (or the reverse).
    
    For instance, [`sklearn.neighbors.NearestNeighbors.kneighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.kneighbors "sklearn.neighbors.NearestNeighbors.kneighbors")
     is now up to 2 times faster for this case on commonly available laptops.
    
    [#25044](https://github.com/scikit-learn/scikit-learn/pull/25044)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Enhancement All estimators that internally rely on OpenMP multi-threading (via Cython) now use a number of threads equal to the number of physical (instead of logical) cores by default. In the past, we observed that using as many threads as logical cores on SMT hosts could sometimes cause severe performance problems depending on the algorithms and the shape of the data. Note that it is still possible to manually adjust the number of threads used by OpenMP as documented in [Parallelism](https://scikit-learn.org/stable/computing/parallelism.html#parallelism)
    .
    
    [#26082](https://github.com/scikit-learn/scikit-learn/pull/26082)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
     and [Olivier Grisel](https://github.com/ogrisel)
    .
    

### Experimental / Under Development[#](https://scikit-learn.org/stable/whats_new/v1.3.html#experimental-under-development "Link to this heading")

*   Major Feature [Metadata routing](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
    ’s related base methods are included in this release. This feature is only available via the `enable_metadata_routing` feature flag which can be enabled using [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
     and [`sklearn.config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context")
    . For now this feature is mostly useful for third party developers to prepare their code base for metadata routing, and we strongly recommend that they also hide it behind the same feature flag, rather than having it enabled by default. [#24027](https://github.com/scikit-learn/scikit-learn/pull/24027)
     by [Adrin Jalali](https://github.com/adrinjalali)
    , [Benjamin Bossan](https://github.com/BenjaminBossan)
    , and [Omar Salman](https://github.com/OmarManzoor)
    .
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id6 "Link to this heading")

#### `sklearn`[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn "Link to this heading")

*   Feature Added a new option `skip_parameter_validation`, to the function [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
     and context manager [`sklearn.config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context")
    , that allows to skip the validation of the parameters passed to the estimators and public functions. This can be useful to speed up the code but should be used with care because it can lead to unexpected behaviors or raise obscure error messages when setting invalid parameters. [#25815](https://github.com/scikit-learn/scikit-learn/pull/25815)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-base "Link to this heading")

*   Feature A `__sklearn_clone__` protocol is now available to override the default behavior of [`base.clone`](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#sklearn.base.clone "sklearn.base.clone")
    . [#24568](https://github.com/scikit-learn/scikit-learn/pull/24568)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`base.TransformerMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin")
     now currently keeps a namedtuple’s class if `transform` returns a namedtuple. [#26121](https://github.com/scikit-learn/scikit-learn/pull/26121)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id7 "Link to this heading")

*   Fix [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     now does not enforce sample alignment on `fit_params`. [#25805](https://github.com/scikit-learn/scikit-learn/pull/25805)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id8 "Link to this heading")

*   Major Feature Added [`cluster.HDBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
    , a modern hierarchical density-based clustering algorithm. Similarly to [`cluster.OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
    , it can be seen as a generalization of [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
     by allowing for hierarchical instead of flat clustering, however it varies in its approach from [`cluster.OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
    . This algorithm is very robust with respect to its hyperparameters’ values and can be used on a wide variety of data without much, if any, tuning.
    
    This implementation is an adaptation from the original implementation of HDBSCAN in [scikit-learn-contrib/hdbscan](https://github.com/scikit-learn-contrib/hdbscan)
    , by [Leland McInnes](https://github.com/lmcinnes)
     et al.
    
    [#26385](https://github.com/scikit-learn/scikit-learn/pull/26385)
     by [Meekail Zain](https://github.com/micky774)
    
*   Enhancement The `sample_weight` parameter now will be used in centroids initialization for [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    , [`cluster.BisectingKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans")
     and [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
    . This change will break backward compatibility, since numbers generated from same random seeds will be different. [#25752](https://github.com/scikit-learn/scikit-learn/pull/25752)
     by [Hleb Levitski](https://github.com/glevv)
    , [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    , [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    , [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     and [`cluster.k_means`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.k_means.html#sklearn.cluster.k_means "sklearn.cluster.k_means")
     now correctly handle the combination of `n_init="auto"` and `init` being an array-like, running one initialization in that case. [#26657](https://github.com/scikit-learn/scikit-learn/pull/26657)
     by [Binesh Bannerjee](https://github.com/bnsh)
    .
    
*   API Change The `sample_weight` parameter in `predict` for [`cluster.KMeans.predict`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans.predict "sklearn.cluster.KMeans.predict")
     and [`cluster.MiniBatchKMeans.predict`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans.predict "sklearn.cluster.MiniBatchKMeans.predict")
     is now deprecated and will be removed in v1.5. [#25251](https://github.com/scikit-learn/scikit-learn/pull/25251)
     by [Hleb Levitski](https://github.com/glevv)
    .
    
*   API Change The `Xred` argument in [`cluster.FeatureAgglomeration.inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration.inverse_transform "sklearn.cluster.FeatureAgglomeration.inverse_transform")
     is renamed to `Xt` and will be removed in v1.5. [#26503](https://github.com/scikit-learn/scikit-learn/pull/26503)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-compose "Link to this heading")

*   Fix [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     raises an informative error when the individual transformers of `ColumnTransformer` output pandas dataframes with indexes that are not consistent with each other and the output is configured to be pandas. [#26286](https://github.com/scikit-learn/scikit-learn/pull/26286)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     correctly sets the output of the remainder when `set_output` is called. [#26323](https://github.com/scikit-learn/scikit-learn/pull/26323)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.covariance`](https://scikit-learn.org/stable/api/sklearn.covariance.html#module-sklearn.covariance "sklearn.covariance")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-covariance "Link to this heading")

*   Fix Allows `alpha=0` in [`covariance.GraphicalLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLasso.html#sklearn.covariance.GraphicalLasso "sklearn.covariance.GraphicalLasso")
     to be consistent with [`covariance.graphical_lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.graphical_lasso.html#sklearn.covariance.graphical_lasso "sklearn.covariance.graphical_lasso")
    . [#26033](https://github.com/scikit-learn/scikit-learn/pull/26033)
     by [Genesis Valencia](https://github.com/genvalen)
    .
    
*   Fix [`covariance.empirical_covariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.empirical_covariance.html#sklearn.covariance.empirical_covariance "sklearn.covariance.empirical_covariance")
     now gives an informative error message when input is not appropriate. [#26108](https://github.com/scikit-learn/scikit-learn/pull/26108)
     by [Quentin Barthélemy](https://github.com/qbarthelemy)
    .
    
*   API Change Deprecates `cov_init` in [`covariance.graphical_lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.graphical_lasso.html#sklearn.covariance.graphical_lasso "sklearn.covariance.graphical_lasso")
     in 1.3 since the parameter has no effect. It will be removed in 1.5. [#26033](https://github.com/scikit-learn/scikit-learn/pull/26033)
     by [Genesis Valencia](https://github.com/genvalen)
    .
    
*   API Change Adds `costs_` fitted attribute in [`covariance.GraphicalLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLasso.html#sklearn.covariance.GraphicalLasso "sklearn.covariance.GraphicalLasso")
     and [`covariance.GraphicalLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")
    . [#26033](https://github.com/scikit-learn/scikit-learn/pull/26033)
     by [Genesis Valencia](https://github.com/genvalen)
    .
    
*   API Change Adds `covariance` parameter in [`covariance.GraphicalLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLasso.html#sklearn.covariance.GraphicalLasso "sklearn.covariance.GraphicalLasso")
    . [#26033](https://github.com/scikit-learn/scikit-learn/pull/26033)
     by [Genesis Valencia](https://github.com/genvalen)
    .
    
*   API Change Adds `eps` parameter in [`covariance.GraphicalLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLasso.html#sklearn.covariance.GraphicalLasso "sklearn.covariance.GraphicalLasso")
    , [`covariance.graphical_lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.graphical_lasso.html#sklearn.covariance.graphical_lasso "sklearn.covariance.graphical_lasso")
    , and [`covariance.GraphicalLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")
    . [#26033](https://github.com/scikit-learn/scikit-learn/pull/26033)
     by [Genesis Valencia](https://github.com/genvalen)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id9 "Link to this heading")

*   Enhancement Allows to overwrite the parameters used to open the ARFF file using the parameter `read_csv_kwargs` in [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     when using the pandas parser. [#26433](https://github.com/scikit-learn/scikit-learn/pull/26433)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     returns improved data types when `as_frame=True` and `parser="liac-arff"`. [#26386](https://github.com/scikit-learn/scikit-learn/pull/26386)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Following the ARFF specs, only the marker `"?"` is now considered as a missing values when opening ARFF files fetched using [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     when using the pandas parser. The parameter `read_csv_kwargs` allows to overwrite this behaviour. [#26551](https://github.com/scikit-learn/scikit-learn/pull/26551)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     will consistently use `np.nan` as missing marker with both parsers `"pandas"` and `"liac-arff"`. [#26579](https://github.com/scikit-learn/scikit-learn/pull/26579)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change The `data_transposed` argument of [`datasets.make_sparse_coded_signal`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_coded_signal.html#sklearn.datasets.make_sparse_coded_signal "sklearn.datasets.make_sparse_coded_signal")
     is deprecated and will be removed in v1.5. [#25784](https://github.com/scikit-learn/scikit-learn/pull/25784)
     by [@Jérémie du Boisberranger](https://github.com/J%C3%A9r%C3%A9mie%20du%20Boisberranger)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id10 "Link to this heading")

*   Efficiency [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
     and [`decomposition.MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")
     are now faster for small batch sizes by avoiding duplicate validations. [#25490](https://github.com/scikit-learn/scikit-learn/pull/25490)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Enhancement [`decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
     now accepts the parameter `callback` for consistency with the function [`decomposition.dict_learning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#sklearn.decomposition.dict_learning "sklearn.decomposition.dict_learning")
    . [#24871](https://github.com/scikit-learn/scikit-learn/pull/24871)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    
*   Fix Treat more consistently small values in the `W` and `H` matrices during the `fit` and `transform` steps of [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     and [`decomposition.MiniBatchNMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")
     which can produce different results than previous versions. [#25438](https://github.com/scikit-learn/scikit-learn/pull/25438)
     by [Yotam Avidar-Constantini](https://github.com/yotamcons)
    .
    
*   API Change The `W` argument in [`decomposition.NMF.inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF.inverse_transform "sklearn.decomposition.NMF.inverse_transform")
     and [`decomposition.MiniBatchNMF.inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF.inverse_transform "sklearn.decomposition.MiniBatchNMF.inverse_transform")
     is renamed to `Xt` and will be removed in v1.5. [#26503](https://github.com/scikit-learn/scikit-learn/pull/26503)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.discriminant_analysis`](https://scikit-learn.org/stable/api/sklearn.discriminant_analysis.html#module-sklearn.discriminant_analysis "sklearn.discriminant_analysis")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-discriminant-analysis "Link to this heading")

*   Enhancement [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     now supports the [PyTorch](https://pytorch.org/)
    . See [Array API support (experimental)](https://scikit-learn.org/stable/modules/array_api.html#array-api)
     for more details. [#25956](https://github.com/scikit-learn/scikit-learn/pull/25956)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id11 "Link to this heading")

*   Feature [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     now supports the Gamma deviance loss via `loss="gamma"`. Using the Gamma deviance as loss function comes in handy for modelling skewed distributed, strictly positive valued targets. [#22409](https://github.com/scikit-learn/scikit-learn/pull/22409)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Feature Compute a custom out-of-bag score by passing a callable to [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
     and [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
    . [#25177](https://github.com/scikit-learn/scikit-learn/pull/25177)
     by [Tim Head](https://betatim.github.io/)
    .
    
*   Feature [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     now exposes out-of-bag scores via the `oob_scores_` or `oob_score_` attributes. [#24882](https://github.com/scikit-learn/scikit-learn/pull/24882)
     by [Ashwin Mathur](https://github.com/awinml)
    .
    
*   Efficiency [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     predict time is now faster (typically by a factor of 8 or more). Internally, the estimator now precomputes decision path lengths per tree at `fit` time. It is therefore not possible to load an estimator trained with scikit-learn 1.2 to make it predict with scikit-learn 1.3: retraining with scikit-learn 1.3 is required. [#25186](https://github.com/scikit-learn/scikit-learn/pull/25186)
     by [Felipe Breve Siola](https://github.com/fsiola)
    .
    
*   Efficiency [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
     and [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
     with `warm_start=True` now only recomputes out-of-bag scores when there are actually more `n_estimators` in subsequent `fit` calls. [#26318](https://github.com/scikit-learn/scikit-learn/pull/26318)
     by [Joshua Choo Yun Keat](https://github.com/choo8)
    .
    
*   Enhancement [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
     and [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
     expose the `allow_nan` tag from the underlying estimator. [#25506](https://github.com/scikit-learn/scikit-learn/pull/25506)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`ensemble.RandomForestClassifier.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.fit "sklearn.ensemble.RandomForestClassifier.fit")
     sets `max_samples = 1` when `max_samples` is a float and `round(n_samples * max_samples) < 1`. [#25601](https://github.com/scikit-learn/scikit-learn/pull/25601)
     by [Jan Fidor](https://github.com/JanFidor)
    .
    
*   Fix [`ensemble.IsolationForest.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest.fit "sklearn.ensemble.IsolationForest.fit")
     no longer warns about missing feature names when called with `contamination` not `"auto"` on a pandas dataframe. [#25931](https://github.com/scikit-learn/scikit-learn/pull/25931)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    
*   Fix [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     and [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     treats negative values for categorical features consistently as missing values, following LightGBM’s and pandas’ conventions. [#25629](https://github.com/scikit-learn/scikit-learn/pull/25629)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Fix deprecation of `base_estimator` in [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
     and [`ensemble.AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
     that was introduced in [#23819](https://github.com/scikit-learn/scikit-learn/pull/23819)
    . [#26242](https://github.com/scikit-learn/scikit-learn/pull/26242)
     by [Marko Toplak](https://github.com/markotoplak)
    .
    

#### [`sklearn.exceptions`](https://scikit-learn.org/stable/api/sklearn.exceptions.html#module-sklearn.exceptions "sklearn.exceptions")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-exceptions "Link to this heading")

*   Feature Added [`exceptions.InconsistentVersionWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.InconsistentVersionWarning.html#sklearn.exceptions.InconsistentVersionWarning "sklearn.exceptions.InconsistentVersionWarning")
     which is raised when a scikit-learn estimator is unpickled with a scikit-learn version that is inconsistent with the scikit-learn version the estimator was pickled with. [#25297](https://github.com/scikit-learn/scikit-learn/pull/25297)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-feature-extraction "Link to this heading")

*   API Change [`feature_extraction.image.PatchExtractor`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#sklearn.feature_extraction.image.PatchExtractor "sklearn.feature_extraction.image.PatchExtractor")
     now follows the transformer API of scikit-learn. This class is defined as a stateless transformer meaning that it is not required to call `fit` before calling `transform`. Parameter validation only happens at `fit` time. [#24230](https://github.com/scikit-learn/scikit-learn/pull/24230)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id12 "Link to this heading")

*   Enhancement All selectors in [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
     will preserve a DataFrame’s dtype when transformed. [#25102](https://github.com/scikit-learn/scikit-learn/pull/25102)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`feature_selection.SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
    ’s `cv` parameter now supports generators. [#25973](https://github.com/scikit-learn/scikit-learn/pull/25973)
     by `Yao Xiao <Charlie-XIAO>`.
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id13 "Link to this heading")

*   Enhancement Added the parameter `fill_value` to [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
    . [#25232](https://github.com/scikit-learn/scikit-learn/pull/25232)
     by [Thijs van Weezel](https://github.com/ValueInvestorThijs)
    .
    
*   Fix [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     now correctly preserves the Pandas Index when the `set_config(transform_output="pandas")`. [#26454](https://github.com/scikit-learn/scikit-learn/pull/26454)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-inspection "Link to this heading")

*   Enhancement Added support for `sample_weight` in [`inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
     and [`inspection.PartialDependenceDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
    . This allows for weighted averaging when aggregating for each value of the grid we are making the inspection on. The option is only available when `method` is set to `brute`. [#25209](https://github.com/scikit-learn/scikit-learn/pull/25209)
     and [#26644](https://github.com/scikit-learn/scikit-learn/pull/26644)
     by [Carlo Lemos](https://github.com/vitaliset)
    .
    
*   API Change [`inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
     returns a [`utils.Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")
     with new key: `grid_values`. The `values` key is deprecated in favor of `grid_values` and the `values` key will be removed in 1.5. [#21809](https://github.com/scikit-learn/scikit-learn/pull/21809)
     and [#25732](https://github.com/scikit-learn/scikit-learn/pull/25732)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.kernel_approximation`](https://scikit-learn.org/stable/api/sklearn.kernel_approximation.html#module-sklearn.kernel_approximation "sklearn.kernel_approximation")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-kernel-approximation "Link to this heading")

*   Fix [`kernel_approximation.AdditiveChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.AdditiveChi2Sampler.html#sklearn.kernel_approximation.AdditiveChi2Sampler "sklearn.kernel_approximation.AdditiveChi2Sampler")
     is now stateless. The `sample_interval_` attribute is deprecated and will be removed in 1.5. [#25190](https://github.com/scikit-learn/scikit-learn/pull/25190)
     by [Vincent Maladière](https://github.com/Vincent-Maladiere)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-linear-model "Link to this heading")

*   Efficiency Avoid data scaling when `sample_weight=None` and other unnecessary data copies and unexpected dense to sparse data conversion in [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
    . [#26207](https://github.com/scikit-learn/scikit-learn/pull/26207)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Enhancement [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    , [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     and [`linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
     now preserve dtype for `numpy.float32`. [#25587](https://github.com/scikit-learn/scikit-learn/pull/25587)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    
*   Enhancement The `n_iter_` attribute has been included in [`linear_model.ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
     to expose the actual number of iterations required to reach the stopping criterion. [#25697](https://github.com/scikit-learn/scikit-learn/pull/25697)
     by [John Pangas](https://github.com/jpangas)
    .
    
*   Fix Use a more robust criterion to detect convergence of [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     with `penalty="l1"` and `solver="liblinear"` on linearly separable problems. [#25214](https://github.com/scikit-learn/scikit-learn/pull/25214)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Fix Fix a crash when calling `fit` on [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     with `solver="newton-cholesky"` and `max_iter=0` which failed to inspect the state of the model prior to the first parameter update. [#26653](https://github.com/scikit-learn/scikit-learn/pull/26653)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   API Change Deprecates `n_iter` in favor of `max_iter` in [`linear_model.BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
     and [`linear_model.ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
    . `n_iter` will be removed in scikit-learn 1.5. This change makes those estimators consistent with the rest of estimators. [#25697](https://github.com/scikit-learn/scikit-learn/pull/25697)
     by [John Pangas](https://github.com/jpangas)
    .
    

#### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-manifold "Link to this heading")

*   Fix [`manifold.Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
     now correctly preserves the Pandas Index when the `set_config(transform_output="pandas")`. [#26454](https://github.com/scikit-learn/scikit-learn/pull/26454)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id14 "Link to this heading")

*   Feature Adds `zero_division=np.nan` to multiple classification metrics: [`metrics.precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")
    , [`metrics.recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")
    , [`metrics.f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")
    , [`metrics.fbeta_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#sklearn.metrics.fbeta_score "sklearn.metrics.fbeta_score")
    , [`metrics.precision_recall_fscore_support`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "sklearn.metrics.precision_recall_fscore_support")
    , [`metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
    . When `zero_division=np.nan` and there is a zero division, the metric is undefined and is excluded from averaging. When not used for averages, the value returned is `np.nan`. [#25531](https://github.com/scikit-learn/scikit-learn/pull/25531)
     by [Marc Torrellas Socastro](https://github.com/marctorsoc)
    .
    
*   Feature [`metrics.average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
     now supports the multiclass case. [#17388](https://github.com/scikit-learn/scikit-learn/pull/17388)
     by [Geoffrey Bolmier](https://github.com/gbolmier)
     and [#24769](https://github.com/scikit-learn/scikit-learn/pull/24769)
     by [Ashwin Mathur](https://github.com/awinml)
    .
    
*   Efficiency The computation of the expected mutual information in [`metrics.adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")
     is now faster when the number of unique labels is large and its memory usage is reduced in general. [#25713](https://github.com/scikit-learn/scikit-learn/pull/25713)
     by [Kshitij Mathur](https://github.com/Kshitij68)
    , [Guillaume Lemaitre](https://github.com/glemaitre)
    , [Omar Salman](https://github.com/OmarManzoor)
     and [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Enhancement [`metrics.silhouette_samples`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html#sklearn.metrics.silhouette_samples "sklearn.metrics.silhouette_samples")
     now accepts a sparse matrix of pairwise distances between samples, or a feature array. [#18723](https://github.com/scikit-learn/scikit-learn/pull/18723)
     by [Sahil Gupta](https://github.com/sahilgupta2105)
     and [#24677](https://github.com/scikit-learn/scikit-learn/pull/24677)
     by [Ashwin Mathur](https://github.com/awinml)
    .
    
*   Enhancement A new parameter `drop_intermediate` was added to [`metrics.precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")
    , [`metrics.PrecisionRecallDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
    , [`metrics.PrecisionRecallDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")
    , which drops some suboptimal thresholds to create lighter precision-recall curves. [#24668](https://github.com/scikit-learn/scikit-learn/pull/24668)
     by [@dberenbaum](https://github.com/dberenbaum)
    .
    
*   Enhancement [`metrics.RocCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")
     and [`metrics.RocCurveDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")
     now accept two new keywords, `plot_chance_level` and `chance_level_kw` to plot the baseline chance level. This line is exposed in the `chance_level_` attribute. [#25987](https://github.com/scikit-learn/scikit-learn/pull/25987)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    
*   Enhancement [`metrics.PrecisionRecallDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
     and [`metrics.PrecisionRecallDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")
     now accept two new keywords, `plot_chance_level` and `chance_level_kw` to plot the baseline chance level. This line is exposed in the `chance_level_` attribute. [#26019](https://github.com/scikit-learn/scikit-learn/pull/26019)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    
*   Fix [`metrics.pairwise.manhattan_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html#sklearn.metrics.pairwise.manhattan_distances "sklearn.metrics.pairwise.manhattan_distances")
     now supports readonly sparse datasets. [#25432](https://github.com/scikit-learn/scikit-learn/pull/25432)
     by [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Fix Fixed [`metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
     so that empty input will return `np.nan`. Previously, “macro avg” and `weighted avg` would return e.g. `f1-score=np.nan` and `f1-score=0.0`, being inconsistent. Now, they both return `np.nan`. [#25531](https://github.com/scikit-learn/scikit-learn/pull/25531)
     by [Marc Torrellas Socastro](https://github.com/marctorsoc)
    .
    
*   Fix [`metrics.ndcg_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html#sklearn.metrics.ndcg_score "sklearn.metrics.ndcg_score")
     now gives a meaningful error message for input of length 1. [#25672](https://github.com/scikit-learn/scikit-learn/pull/25672)
     by [Lene Preuss](https://github.com/lene)
     and [Wei-Chun Chu](https://github.com/wcchu)
    .
    
*   Fix [`metrics.log_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
     raises a warning if the values of the parameter `y_pred` are not normalized, instead of actually normalizing them in the metric. Starting from 1.5 this will raise an error. [#25299](https://github.com/scikit-learn/scikit-learn/pull/25299)
     by [@Omar Salman <OmarManzoor](https://github.com/Omar%20Salman%20%3COmarManzoor)
    .
    
*   Fix In [`metrics.roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
    , use the threshold value `np.inf` instead of arbitrary `max(y_score) + 1`. This threshold is associated with the ROC curve point `tpr=0` and `fpr=0`. [#26194](https://github.com/scikit-learn/scikit-learn/pull/26194)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix The `'matching'` metric has been removed when using SciPy>=1.9 to be consistent with `scipy.spatial.distance` which does not support `'matching'` anymore. [#26264](https://github.com/scikit-learn/scikit-learn/pull/26264)
     by [Barata T. Onggo](https://github.com/magnusbarata)
    
*   API Change The `eps` parameter of the [`metrics.log_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
     has been deprecated and will be removed in 1.5. [#25299](https://github.com/scikit-learn/scikit-learn/pull/25299)
     by [Omar Salman](https://github.com/OmarManzoor)
    .
    

#### [`sklearn.gaussian_process`](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#module-sklearn.gaussian_process "sklearn.gaussian_process")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-gaussian-process "Link to this heading")

*   Fix [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
     has a new argument `n_targets`, which is used to decide the number of outputs when sampling from the prior distributions. [#23099](https://github.com/scikit-learn/scikit-learn/pull/23099)
     by [Zhehao Liu](https://github.com/MaxwellLZH)
    .
    

#### [`sklearn.mixture`](https://scikit-learn.org/stable/api/sklearn.mixture.html#module-sklearn.mixture "sklearn.mixture")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id15 "Link to this heading")

*   Efficiency [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     is more efficient now and will bypass unnecessary initialization if the weights, means, and precisions are given by users. [#26021](https://github.com/scikit-learn/scikit-learn/pull/26021)
     by [Jiawei Zhang](https://github.com/jiawei-zhang-a)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-model-selection "Link to this heading")

*   Major Feature Added the class [`model_selection.ValidationCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ValidationCurveDisplay.html#sklearn.model_selection.ValidationCurveDisplay "sklearn.model_selection.ValidationCurveDisplay")
     that allows easy plotting of validation curves obtained by the function [`model_selection.validation_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve "sklearn.model_selection.validation_curve")
    . [#25120](https://github.com/scikit-learn/scikit-learn/pull/25120)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change The parameter `log_scale` in the method `plot` of the class [`model_selection.LearningCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay "sklearn.model_selection.LearningCurveDisplay")
     has been deprecated in 1.3 and will be removed in 1.5. The default scale can be overridden by setting it directly on the `ax` object and will be set automatically from the spacing of the data points otherwise. [#25120](https://github.com/scikit-learn/scikit-learn/pull/25120)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Enhancement [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
     accepts a new parameter `return_indices` to return the train-test indices of each cv split. [#25659](https://github.com/scikit-learn/scikit-learn/pull/25659)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.multioutput`](https://scikit-learn.org/stable/api/sklearn.multioutput.html#module-sklearn.multioutput "sklearn.multioutput")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-multioutput "Link to this heading")

*   Fix [`getattr`](https://docs.python.org/3/library/functions.html#getattr "(in Python v3.14)")
     on [`multioutput.MultiOutputRegressor.partial_fit`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor.partial_fit "sklearn.multioutput.MultiOutputRegressor.partial_fit")
     and [`multioutput.MultiOutputClassifier.partial_fit`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.partial_fit "sklearn.multioutput.MultiOutputClassifier.partial_fit")
     now correctly raise an `AttributeError` if done before calling `fit`. [#26333](https://github.com/scikit-learn/scikit-learn/pull/26333)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.naive_bayes`](https://scikit-learn.org/stable/api/sklearn.naive_bayes.html#module-sklearn.naive_bayes "sklearn.naive_bayes")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-naive-bayes "Link to this heading")

*   Fix [`naive_bayes.GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
     does not raise anymore a `ZeroDivisionError` when the provided `sample_weight` reduces the problem to a single class in `fit`. [#24140](https://github.com/scikit-learn/scikit-learn/pull/24140)
     by [Jonathan Ohayon](https://github.com/Johayon)
     and [Chiara Marmo](https://github.com/cmarmo)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id16 "Link to this heading")

*   Enhancement The performance of [`neighbors.KNeighborsClassifier.predict`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.predict "sklearn.neighbors.KNeighborsClassifier.predict")
     and of [`neighbors.KNeighborsClassifier.predict_proba`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.predict_proba "sklearn.neighbors.KNeighborsClassifier.predict_proba")
     has been improved when `n_neighbors` is large and `algorithm="brute"` with non Euclidean metrics. [#24076](https://github.com/scikit-learn/scikit-learn/pull/24076)
     by [Meekail Zain](https://github.com/micky774)
    , [Julien Jerphanion](https://github.com/jjerphan)
    .
    
*   Fix Remove support for `KulsinskiDistance` in [`neighbors.BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
    . This dissimilarity is not a metric and cannot be supported by the BallTree. [#25417](https://github.com/scikit-learn/scikit-learn/pull/25417)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change The support for metrics other than `euclidean` and `manhattan` and for callables in [`neighbors.NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
     is deprecated and will be removed in version 1.5. [#24083](https://github.com/scikit-learn/scikit-learn/pull/24083)
     by [Valentin Laurent](https://github.com/Valentin-Laurent)
    .
    

#### [`sklearn.neural_network`](https://scikit-learn.org/stable/api/sklearn.neural_network.html#module-sklearn.neural_network "sklearn.neural_network")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-neural-network "Link to this heading")

*   Fix [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
     and [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     reports the right `n_iter_` when `warm_start=True`. It corresponds to the number of iterations performed on the current call to `fit` instead of the total number of iterations performed since the initialization of the estimator. [#25443](https://github.com/scikit-learn/scikit-learn/pull/25443)
     by [Marvin Krawutschke](https://github.com/Marvvxi)
    .
    

#### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-pipeline "Link to this heading")

*   Feature [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     can now use indexing notation (e.g. `feature_union["scalar"]`) to access transformers by name. [#25093](https://github.com/scikit-learn/scikit-learn/pull/25093)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     can now access the `feature_names_in_` attribute if the `X` value seen during `.fit` has a `columns` attribute and all columns are strings. e.g. when `X` is a `pandas.DataFrame` [#25220](https://github.com/scikit-learn/scikit-learn/pull/25220)
     by [Ian Thompson](https://github.com/it176131)
    .
    
*   Fix [`pipeline.Pipeline.fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.fit_transform "sklearn.pipeline.Pipeline.fit_transform")
     now raises an `AttributeError` if the last step of the pipeline does not support `fit_transform`. [#26325](https://github.com/scikit-learn/scikit-learn/pull/26325)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id17 "Link to this heading")

*   Major Feature Introduces [`preprocessing.TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
     which is a categorical encoding based on target mean conditioned on the value of the category. [#25334](https://github.com/scikit-learn/scikit-learn/pull/25334)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Feature [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     now supports grouping infrequent categories into a single feature. Grouping infrequent categories is enabled by specifying how to select infrequent categories with `min_frequency` or `max_categories`. [#25677](https://github.com/scikit-learn/scikit-learn/pull/25677)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement [`preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
     now calculates the number of expanded terms a-priori when dealing with sparse `csr` matrices in order to optimize the choice of `dtype` for `indices` and `indptr`. It can now output `csr` matrices with `np.int32` `indices/indptr` components when there are few enough elements, and will automatically use `np.int64` for sufficiently large matrices. [#20524](https://github.com/scikit-learn/scikit-learn/pull/20524)
     by [niuk-a](https://github.com/niuk-a)
     and [#23731](https://github.com/scikit-learn/scikit-learn/pull/23731)
     by [Meekail Zain](https://github.com/micky774)
    
*   Enhancement A new parameter `sparse_output` was added to [`preprocessing.SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
    , available as of SciPy 1.8. If `sparse_output=True`, [`preprocessing.SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
     returns a sparse CSR matrix. [#24145](https://github.com/scikit-learn/scikit-learn/pull/24145)
     by [Christian Lorentzen](https://github.com/lorentzenchr)
    .
    
*   Enhancement Adds a `feature_name_combiner` parameter to [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
    . This specifies a custom callable to create feature names to be returned by [`preprocessing.OneHotEncoder.get_feature_names_out`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder.get_feature_names_out "sklearn.preprocessing.OneHotEncoder.get_feature_names_out")
    . The callable combines input arguments `(input_feature, category)` to a string. [#22506](https://github.com/scikit-learn/scikit-learn/pull/22506)
     by [Mario Kostelac](https://github.com/mariokostelac)
    .
    
*   Enhancement Added support for `sample_weight` in [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
    . This allows specifying the parameter `sample_weight` for each sample to be used while fitting. The option is only available when `strategy` is set to `quantile` and `kmeans`. [#24935](https://github.com/scikit-learn/scikit-learn/pull/24935)
     by [Seladus](https://github.com/seladus)
    , [Guillaume Lemaitre](https://github.com/glemaitre)
    , and [Dea María Léon](https://github.com/deamarialeon)
    , [#25257](https://github.com/scikit-learn/scikit-learn/pull/25257)
     by [Hleb Levitski](https://github.com/glevv)
    .
    
*   Enhancement Subsampling through the `subsample` parameter can now be used in [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
     regardless of the strategy used. [#26424](https://github.com/scikit-learn/scikit-learn/pull/26424)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix [`preprocessing.PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
     now correctly preserves the Pandas Index when the `set_config(transform_output="pandas")`. [#26454](https://github.com/scikit-learn/scikit-learn/pull/26454)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`preprocessing.PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
     now correctly raises error when using `method="box-cox"` on data with a constant `np.nan` column. [#26400](https://github.com/scikit-learn/scikit-learn/pull/26400)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    .
    
*   Fix [`preprocessing.PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
     with `method="yeo-johnson"` now leaves constant features unchanged instead of transforming with an arbitrary value for the `lambdas_` fitted parameter. [#26566](https://github.com/scikit-learn/scikit-learn/pull/26566)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   API Change The default value of the `subsample` parameter of [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
     will change from `None` to `200_000` in version 1.5 when `strategy="kmeans"` or `strategy="uniform"`. [#26424](https://github.com/scikit-learn/scikit-learn/pull/26424)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-svm "Link to this heading")

*   API Change `dual` parameter now accepts `auto` option for [`svm.LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
     and [`svm.LinearSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR "sklearn.svm.LinearSVR")
    . [#26093](https://github.com/scikit-learn/scikit-learn/pull/26093)
     by [Hleb Levitski](https://github.com/glevv)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#id18 "Link to this heading")

*   Major Feature [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
     and [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
     support missing values when `splitter='best'` and criterion is `gini`, `entropy`, or `log_loss`, for classification or `squared_error`, `friedman_mse`, or `poisson` for regression. [#23595](https://github.com/scikit-learn/scikit-learn/pull/23595)
    , [#26376](https://github.com/scikit-learn/scikit-learn/pull/26376)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Enhancement Adds a `class_names` parameter to [`tree.export_text`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html#sklearn.tree.export_text "sklearn.tree.export_text")
    . This allows specifying the parameter `class_names` for each target class in ascending numerical order. [#25387](https://github.com/scikit-learn/scikit-learn/pull/25387)
     by [William M](https://github.com/Akbeeh)
     and [crispinlogan](https://github.com/crispinlogan)
    .
    
*   Fix [`tree.export_graphviz`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz "sklearn.tree.export_graphviz")
     and [`tree.export_text`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html#sklearn.tree.export_text "sklearn.tree.export_text")
     now accepts `feature_names` and `class_names` as array-like rather than lists. [#26289](https://github.com/scikit-learn/scikit-learn/pull/26289)
     by [Yao Xiao](https://github.com/Charlie-XIAO)
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-utils "Link to this heading")

*   Fix Fixes [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     to properly convert pandas extension arrays. [#25813](https://github.com/scikit-learn/scikit-learn/pull/25813)
     and [#26106](https://github.com/scikit-learn/scikit-learn/pull/26106)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     now supports pandas DataFrames with extension arrays and object dtypes by returning an ndarray with object dtype. [#25814](https://github.com/scikit-learn/scikit-learn/pull/25814)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   API Change `utils.estimator_checks.check_transformers_unfitted_stateless` has been introduced to ensure stateless transformers don’t raise `NotFittedError` during `transform` with no prior call to `fit` or `fit_transform`. [#25190](https://github.com/scikit-learn/scikit-learn/pull/25190)
     by [Vincent Maladière](https://github.com/Vincent-Maladiere)
    .
    
*   API Change A `FutureWarning` is now raised when instantiating a class which inherits from a deprecated base class (i.e. decorated by [`utils.deprecated`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.deprecated.html#sklearn.utils.deprecated "sklearn.utils.deprecated")
    ) and which overrides the `__init__` method. [#25733](https://github.com/scikit-learn/scikit-learn/pull/25733)
     by [Brigitta Sipőcz](https://github.com/bsipocz)
     and [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.semi_supervised`](https://scikit-learn.org/stable/api/sklearn.semi_supervised.html#module-sklearn.semi_supervised "sklearn.semi_supervised")
[#](https://scikit-learn.org/stable/whats_new/v1.3.html#sklearn-semi-supervised "Link to this heading")

*   Enhancement [`semi_supervised.LabelSpreading.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading.fit "sklearn.semi_supervised.LabelSpreading.fit")
     and [`semi_supervised.LabelPropagation.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation.fit "sklearn.semi_supervised.LabelPropagation.fit")
     now accepts sparse metrics. [#19664](https://github.com/scikit-learn/scikit-learn/pull/19664)
     by [Kaushik Amar Das](https://github.com/cozek)
    .
    

#### Miscellaneous[#](https://scikit-learn.org/stable/whats_new/v1.3.html#miscellaneous "Link to this heading")

*   Enhancement Replace obsolete exceptions `EnvironmentError`, `IOError` and `WindowsError`. [#26466](https://github.com/scikit-learn/scikit-learn/pull/26466)
     by [Dimitri Papadopoulos ORfanos](https://github.com/DimitriPapadopoulos)
    .
    

Code and documentation contributors

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 1.2, including:

2357juan, Abhishek Singh Kushwah, Adam Handke, Adam Kania, Adam Li, adienes, Admir Demiraj, adoublet, Adrin Jalali, A.H.Mansouri, Ahmedbgh, Ala-Na, Alex Buzenet, AlexL, Ali H. El-Kassas, amay, András Simon, André Pedersen, Andrew Wang, Ankur Singh, annegnx, Ansam Zedan, Anthony22-dev, Artur Hermano, Arturo Amor, as-90, ashah002, Ashish Dutt, Ashwin Mathur, AymericBasset, Azaria Gebremichael, Barata Tripramudya Onggo, Benedek Harsanyi, Benjamin Bossan, Bharat Raghunathan, Binesh Bannerjee, Boris Feld, Brendan Lu, Brevin Kunde, cache-missing, Camille Troillard, Carla J, carlo, Carlo Lemos, c-git, Changyao Chen, Chiara Marmo, Christian Lorentzen, Christian Veenhuis, Christine P. Chai, crispinlogan, Da-Lan, DanGonite57, Dave Berenbaum, davidblnc, david-cortes, Dayne, Dea María Léon, Denis, Dimitri Papadopoulos Orfanos, Dimitris Litsidis, Dmitry Nesterov, Dominic Fox, Dominik Prodinger, Edern, Ekaterina Butyugina, Elabonga Atuo, Emir, farhan khan, Felipe Siola, futurewarning, Gael Varoquaux, genvalen, Hleb Levitski, Guillaume Lemaitre, gunesbayir, Haesun Park, hujiahong726, i-aki-y, Ian Thompson, Ido M, Ily, Irene, Jack McIvor, jakirkham, James Dean, JanFidor, Jarrod Millman, JB Mountford, Jérémie du Boisberranger, Jessicakk0711, Jiawei Zhang, Joey Ortiz, JohnathanPi, John Pangas, Joshua Choo Yun Keat, Joshua Hedlund, JuliaSchoepp, Julien Jerphanion, jygerardy, ka00ri, Kaushik Amar Das, Kento Nozawa, Kian Eliasi, Kilian Kluge, Lene Preuss, Linus, Logan Thomas, Loic Esteve, Louis Fouquet, Lucy Liu, Madhura Jayaratne, Marc Torrellas Socastro, Maren Westermann, Mario Kostelac, Mark Harfouche, Marko Toplak, Marvin Krawutschke, Masanori Kanazu, mathurinm, Matt Haberland, Max Halford, maximeSaur, Maxwell Liu, m. bou, mdarii, Meekail Zain, Mikhail Iljin, murezzda, Nawazish Alam, Nicola Fanelli, Nightwalkx, Nikolay Petrov, Nishu Choudhary, NNLNR, npache, Olivier Grisel, Omar Salman, ouss1508, PAB, Pandata, partev, Peter Piontek, Phil, pnucci, Pooja M, Pooja Subramaniam, precondition, Quentin Barthélemy, Rafal Wojdyla, Raghuveer Bhat, Rahil Parikh, Ralf Gommers, ram vikram singh, Rushil Desai, Sadra Barikbin, SANJAI\_3, Sashka Warner, Scott Gigante, Scott Gustafson, searchforpassion, Seoeun Hong, Shady el Gewily, Shiva chauhan, Shogo Hida, Shreesha Kumar Bhat, sonnivs, Sortofamudkip, Stanislav (Stanley) Modrak, Stefanie Senger, Steven Van Vaerenbergh, Tabea Kossen, Théophile Baranger, Thijs van Weezel, Thomas A Caswell, Thomas Germer, Thomas J. Fan, Tim Head, Tim P, Tom Dupré la Tour, tomiock, tspeng, Valentin Laurent, Veghit, VIGNESH D, Vijeth Moudgalya, Vinayak Mehta, Vincent M, Vincent-violet, Vyom Pathak, William M, windiana42, Xiao Yuan, Yao Xiao, Yaroslav Halchenko, Yotam Avidar-Constantini, Yuchen Zhou, Yusuf Raji, zeeshan lone

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)