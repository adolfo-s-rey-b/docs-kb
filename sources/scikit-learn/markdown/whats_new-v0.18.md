[Skip to main content](https://scikit-learn.org/stable/whats_new/v0.18.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v0.18.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v0.18.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v0.18.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v0.18.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v0.18.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v0.18.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v0.18.html)

Collapse Sidebar Expand Sidebar

Version 0.18[#](https://scikit-learn.org/stable/whats_new/v0.18.html#version-0-18 "Link to this heading")

==========================================================================================================

Warning

Scikit-learn 0.18 is the last major release of scikit-learn to support Python 2.6. Later versions of scikit-learn will require Python 2.7 or above.

Version 0.18.2[#](https://scikit-learn.org/stable/whats_new/v0.18.html#version-0-18-2 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**June 20, 2017**

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.18.html#changelog "Link to this heading")

*   Fixes for compatibility with NumPy 1.13.0: [#7946](https://github.com/scikit-learn/scikit-learn/issues/7946)
     [#8355](https://github.com/scikit-learn/scikit-learn/issues/8355)
     by [Loic Esteve](https://github.com/lesteve)
    .
    
*   Minor compatibility changes in the examples [#9010](https://github.com/scikit-learn/scikit-learn/issues/9010)
     [#8040](https://github.com/scikit-learn/scikit-learn/issues/8040)
     [#9149](https://github.com/scikit-learn/scikit-learn/issues/9149)
    .
    

### Code Contributors[#](https://scikit-learn.org/stable/whats_new/v0.18.html#code-contributors "Link to this heading")

Aman Dalmia, Loic Esteve, Nate Guerin, Sergei Lebedev

Version 0.18.1[#](https://scikit-learn.org/stable/whats_new/v0.18.html#version-0-18-1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**November 11, 2016**

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.18.html#id1 "Link to this heading")

#### Enhancements[#](https://scikit-learn.org/stable/whats_new/v0.18.html#enhancements "Link to this heading")

*   Improved `sample_without_replacement` speed by utilizing numpy.random.permutation for most cases. As a result, samples may differ in this release for a fixed random state. Affected estimators:
    
    *   [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
        
    *   [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
        
    *   [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
        
    *   [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
        
    *   [`random_projection.SparseRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection")
        
    
    This also affects the [`datasets.make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
     method.
    

#### Bug fixes[#](https://scikit-learn.org/stable/whats_new/v0.18.html#bug-fixes "Link to this heading")

*   Fix issue where `min_grad_norm` and `n_iter_without_progress` parameters were not being utilised by [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
    . [#6497](https://github.com/scikit-learn/scikit-learn/issues/6497)
     by [Sebastian Säger](https://github.com/ssaeger)
    
*   Fix bug for svm’s decision values when `decision_function_shape` is `ovr` in [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
    . [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
    ’s decision\_function was incorrect from versions 0.17.0 through 0.18.0. [#7724](https://github.com/scikit-learn/scikit-learn/issues/7724)
     by [Bing Tian Dai](https://github.com/btdai)
    
*   Attribute `explained_variance_ratio` of [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     calculated with SVD and Eigen solver are now of the same length. [#7632](https://github.com/scikit-learn/scikit-learn/issues/7632)
     by [JPFrancoia](https://github.com/JPFrancoia)
    
*   Fixes issue in [Univariate feature selection](https://scikit-learn.org/stable/modules/feature_selection.html#univariate-feature-selection)
     where score functions were not accepting multi-label targets. [#7676](https://github.com/scikit-learn/scikit-learn/issues/7676)
     by [Mohammed Affan](https://github.com/affanv14)
    
*   Fixed setting parameters when calling `fit` multiple times on [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
    . [#7756](https://github.com/scikit-learn/scikit-learn/issues/7756)
     by [Andreas Müller](https://amueller.github.io/)
    
*   Fixes issue in `partial_fit` method of [`multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
     when number of classes used in `partial_fit` was less than the total number of classes in the data. [#7786](https://github.com/scikit-learn/scikit-learn/issues/7786)
     by [Srivatsan Ramesh](https://github.com/srivatsan-ramesh)
    
*   Fixes issue in [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     where the sum of probabilities of each class for a data was not 1, and `CalibratedClassifierCV` now handles the case where the training set has less number of classes than the total data. [#7799](https://github.com/scikit-learn/scikit-learn/issues/7799)
     by [Srivatsan Ramesh](https://github.com/srivatsan-ramesh)
    
*   Fix a bug where [`sklearn.feature_selection.SelectFdr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFdr.html#sklearn.feature_selection.SelectFdr "sklearn.feature_selection.SelectFdr")
     did not exactly implement Benjamini-Hochberg procedure. It formerly may have selected fewer features than it should. [#7490](https://github.com/scikit-learn/scikit-learn/issues/7490)
     by [Peng Meng](https://github.com/mpjlu)
    .
    
*   [`sklearn.manifold.LocallyLinearEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
     now correctly handles integer inputs. [#6282](https://github.com/scikit-learn/scikit-learn/issues/6282)
     by [Jake Vanderplas](https://staff.washington.edu/jakevdp/)
    .
    
*   The `min_weight_fraction_leaf` parameter of tree-based classifiers and regressors now assumes uniform sample weights by default if the `sample_weight` argument is not passed to the `fit` function. Previously, the parameter was silently ignored. [#7301](https://github.com/scikit-learn/scikit-learn/issues/7301)
     by [Nelson Liu](https://github.com/nelson-liu)
    .
    
*   Numerical issue with [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     on centered data when `n_features > n_samples`. [#6178](https://github.com/scikit-learn/scikit-learn/issues/6178)
     by [Bertrand Thirion](https://team.inria.fr/parietal/bertrand-thirions-page)
    
*   Tree splitting criterion classes’ cloning/pickling is now memory safe [#7680](https://github.com/scikit-learn/scikit-learn/issues/7680)
     by [Ibraim Ganiev](https://github.com/olologin)
    .
    
*   Fixed a bug where [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     sets its `n_iters_` attribute in `transform()`. [#7553](https://github.com/scikit-learn/scikit-learn/issues/7553)
     by [Ekaterina Krivich](https://github.com/kiote)
    .
    
*   [`sklearn.linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     now correctly handles string labels. [#5874](https://github.com/scikit-learn/scikit-learn/issues/5874)
     by [Raghav RV](https://github.com/raghavrv)
    .
    
*   Fixed a bug where [`sklearn.model_selection.train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
     raised an error when `stratify` is a list of string labels. [#7593](https://github.com/scikit-learn/scikit-learn/issues/7593)
     by [Raghav RV](https://github.com/raghavrv)
    .
    
*   Fixed a bug where [`sklearn.model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`sklearn.model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     were not pickleable because of a pickling bug in `np.ma.MaskedArray`. [#7594](https://github.com/scikit-learn/scikit-learn/issues/7594)
     by [Raghav RV](https://github.com/raghavrv)
    .
    
*   All cross-validation utilities in [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
     now permit one time cross-validation splitters for the `cv` parameter. Also non-deterministic cross-validation splitters (where multiple calls to `split` produce dissimilar splits) can be used as `cv` parameter. The [`sklearn.model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     will cross-validate each parameter setting on the split produced by the first `split` call to the cross-validation splitter. [#7660](https://github.com/scikit-learn/scikit-learn/issues/7660)
     by [Raghav RV](https://github.com/raghavrv)
    .
    
*   Fix bug where [`preprocessing.MultiLabelBinarizer.fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer.fit_transform "sklearn.preprocessing.MultiLabelBinarizer.fit_transform")
     returned an invalid CSR matrix. [#7750](https://github.com/scikit-learn/scikit-learn/issues/7750)
     by [CJ Carey](https://github.com/perimosocordiae)
    .
    
*   Fixed a bug where [`metrics.pairwise.cosine_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_distances.html#sklearn.metrics.pairwise.cosine_distances "sklearn.metrics.pairwise.cosine_distances")
     could return a small negative distance. [#7732](https://github.com/scikit-learn/scikit-learn/issues/7732)
     by [Artsion](https://github.com/asanakoy)
    .
    

### API changes summary[#](https://scikit-learn.org/stable/whats_new/v0.18.html#api-changes-summary "Link to this heading")

Trees and forests

*   The `min_weight_fraction_leaf` parameter of tree-based classifiers and regressors now assumes uniform sample weights by default if the `sample_weight` argument is not passed to the `fit` function. Previously, the parameter was silently ignored. [#7301](https://github.com/scikit-learn/scikit-learn/issues/7301)
     by [Nelson Liu](https://github.com/nelson-liu)
    .
    
*   Tree splitting criterion classes’ cloning/pickling is now memory safe. [#7680](https://github.com/scikit-learn/scikit-learn/issues/7680)
     by [Ibraim Ganiev](https://github.com/olologin)
    .
    

Linear, kernelized and related models

*   Length of `explained_variance_ratio` of [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     changed for both Eigen and SVD solvers. The attribute has now a length of min(n\_components, n\_classes - 1). [#7632](https://github.com/scikit-learn/scikit-learn/issues/7632)
     by [JPFrancoia](https://github.com/JPFrancoia)
    
*   Numerical issue with [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     on centered data when `n_features > n_samples`. [#6178](https://github.com/scikit-learn/scikit-learn/issues/6178)
     by [Bertrand Thirion](https://team.inria.fr/parietal/bertrand-thirions-page)
    

Version 0.18[#](https://scikit-learn.org/stable/whats_new/v0.18.html#changes-0-18 "Link to this heading")

----------------------------------------------------------------------------------------------------------

**September 28, 2016**

### Model Selection Enhancements and API Changes[#](https://scikit-learn.org/stable/whats_new/v0.18.html#model-selection-enhancements-and-api-changes "Link to this heading")

*   **The model\_selection module**
    
    The new module [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
    , which groups together the functionalities of formerly `sklearn.cross_validation`, `sklearn.grid_search` and `sklearn.learning_curve`, introduces new possibilities such as nested cross-validation and better manipulation of parameter searches with Pandas.
    
    Many things will stay the same but there are some key differences. Read below to know more about the changes.
    
*   **Data-independent CV splitters enabling nested cross-validation**
    
    The new cross-validation splitters, defined in the [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
    , are no longer initialized with any data-dependent parameters such as `y`. Instead they expose a `split` method that takes in the data and yields a generator for the different splits.
    
    This change makes it possible to use the cross-validation splitters to perform nested cross-validation, facilitated by [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     utilities.
    
*   **The enhanced cv\_results\_ attribute**
    
    The new `cv_results_` attribute (of [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
    ) introduced in lieu of the `grid_scores_` attribute is a dict of 1D arrays with elements in each array corresponding to the parameter settings (i.e. search candidates).
    
    The `cv_results_` dict can be easily imported into `pandas` as a `DataFrame` for exploring the search results.
    
    The `cv_results_` arrays include scores for each cross-validation split (with keys such as `'split0_test_score'`), as well as their mean (`'mean_test_score'`) and standard deviation (`'std_test_score'`).
    
    The ranks for the search candidates (based on their mean cross-validation score) is available at `cv_results_['rank_test_score']`.
    
    The parameter values for each parameter is stored separately as numpy masked object arrays. The value, for that search candidate, is masked if the corresponding parameter is not applicable. Additionally a list of all the parameter dicts are stored at `cv_results_['params']`.
    
*   **Parameters n\_folds and n\_iter renamed to n\_splits**
    
    Some parameter names have changed: The `n_folds` parameter in new [`model_selection.KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
    , [`model_selection.GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
     (see below for the name change), and [`model_selection.StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
     is now renamed to `n_splits`. The `n_iter` parameter in [`model_selection.ShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")
    , the new class [`model_selection.GroupShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit "sklearn.model_selection.GroupShuffleSplit")
     and [`model_selection.StratifiedShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")
     is now renamed to `n_splits`.
    
*   **Rename of splitter classes which accepts group labels along with data**
    
    The cross-validation splitters `LabelKFold`, `LabelShuffleSplit`, `LeaveOneLabelOut` and `LeavePLabelOut` have been renamed to [`model_selection.GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
    , [`model_selection.GroupShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit "sklearn.model_selection.GroupShuffleSplit")
    , [`model_selection.LeaveOneGroupOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut "sklearn.model_selection.LeaveOneGroupOut")
     and [`model_selection.LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut")
     respectively.
    
    Note the change from singular to plural form in [`model_selection.LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut")
    .
    
*   **Fit parameter labels renamed to groups**
    
    The `labels` parameter in the `split` method of the newly renamed splitters [`model_selection.GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
    , [`model_selection.LeaveOneGroupOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut "sklearn.model_selection.LeaveOneGroupOut")
    , [`model_selection.LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut")
    , [`model_selection.GroupShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit "sklearn.model_selection.GroupShuffleSplit")
     is renamed to `groups` following the new nomenclature of their class names.
    
*   **Parameter n\_labels renamed to n\_groups**
    
    The parameter `n_labels` in the newly renamed [`model_selection.LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut")
     is changed to `n_groups`.
    
*   Training scores and Timing information
    
    `cv_results_` also includes the training scores for each cross-validation split (with keys such as `'split0_train_score'`), as well as their mean (`'mean_train_score'`) and standard deviation (`'std_train_score'`). To avoid the cost of evaluating training score, set `return_train_score=False`.
    
    Additionally the mean and standard deviation of the times taken to split, train and score the model across all the cross-validation splits is available at the key `'mean_time'` and `'std_time'` respectively.
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.18.html#id3 "Link to this heading")

#### New features[#](https://scikit-learn.org/stable/whats_new/v0.18.html#new-features "Link to this heading")

Classifiers and Regressors

*   The Gaussian Process module has been reimplemented and now offers classification and regression estimators through [`gaussian_process.GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
     and [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
    . Among other things, the new implementation supports kernel engineering, gradient-based hyperparameter optimization or sampling of functions from GP prior and GP posterior. Extensive documentation and examples are provided. By [Jan Hendrik Metzen](https://jmetzen.github.io/)
    .
    
*   Added new supervised learning algorithm: [Multi-layer Perceptron](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#multilayer-perceptron)
     [#3204](https://github.com/scikit-learn/scikit-learn/issues/3204)
     by [Issam H. Laradji](https://github.com/IssamLaradji)
    
*   Added [`linear_model.HuberRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor")
    , a linear model robust to outliers. [#5291](https://github.com/scikit-learn/scikit-learn/issues/5291)
     by [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Added the [`multioutput.MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")
     meta-estimator. It converts single output regressors to multi-output regressors by fitting one regressor per output. By [Tim Head](https://github.com/betatim)
    .
    

Other estimators

*   New [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     and [`mixture.BayesianGaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")
     replace former mixture models, employing faster inference for sounder results. [#7295](https://github.com/scikit-learn/scikit-learn/issues/7295)
     by [Wei Xue](https://github.com/xuewei4d)
     and [Thierry Guillemot](https://github.com/tguillemot)
    .
    
*   Class `decomposition.RandomizedPCA` is now factored into [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     and it is available calling with parameter `svd_solver='randomized'`. The default number of `n_iter` for `'randomized'` has changed to 4. The old behavior of PCA is recovered by `svd_solver='full'`. An additional solver calls `arpack` and performs truncated (non-randomized) SVD. By default, the best solver is selected depending on the size of the input and the number of components requested. [#5299](https://github.com/scikit-learn/scikit-learn/issues/5299)
     by [Giorgio Patrini](https://github.com/giorgiop)
    .
    
*   Added two functions for mutual information estimation: [`feature_selection.mutual_info_classif`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#sklearn.feature_selection.mutual_info_classif "sklearn.feature_selection.mutual_info_classif")
     and [`feature_selection.mutual_info_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html#sklearn.feature_selection.mutual_info_regression "sklearn.feature_selection.mutual_info_regression")
    . These functions can be used in [`feature_selection.SelectKBest`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
     and [`feature_selection.SelectPercentile`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile")
     as score functions. By [Andrea Bravi](https://github.com/AndreaBravi)
     and [Nikolay Mayorov](https://github.com/nmayorov)
    .
    
*   Added the [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     class for anomaly detection based on random forests. By [Nicolas Goix](https://ngoix.github.io/)
    .
    
*   Added `algorithm="elkan"` to [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     implementing Elkan’s fast K-Means algorithm. By [Andreas Müller](https://amueller.github.io/)
    .
    

Model selection and evaluation

*   Added [`metrics.fowlkes_mallows_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fowlkes_mallows_score.html#sklearn.metrics.fowlkes_mallows_score "sklearn.metrics.fowlkes_mallows_score")
    , the Fowlkes Mallows Index which measures the similarity of two clusterings of a set of points By [Arnaud Fouchet](https://github.com/afouchet)
     and [Thierry Guillemot](https://github.com/tguillemot)
    .
    
*   Added `metrics.calinski_harabaz_score`, which computes the Calinski and Harabaz score to evaluate the resulting clustering of a set of points. By [Arnaud Fouchet](https://github.com/afouchet)
     and [Thierry Guillemot](https://github.com/tguillemot)
    .
    
*   Added new cross-validation splitter [`model_selection.TimeSeriesSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")
     to handle time series data. [#6586](https://github.com/scikit-learn/scikit-learn/issues/6586)
     by [YenChen Lin](https://github.com/yenchenlin)
    
*   The cross-validation iterators are replaced by cross-validation splitters available from [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
    , allowing for nested cross-validation. See [Model Selection Enhancements and API Changes](https://scikit-learn.org/stable/whats_new/v0.18.html#model-selection-changes)
     for more information. [#4294](https://github.com/scikit-learn/scikit-learn/issues/4294)
     by [Raghav RV](https://github.com/raghavrv)
    .
    

#### Enhancements[#](https://scikit-learn.org/stable/whats_new/v0.18.html#id4 "Link to this heading")

Trees and ensembles

*   Added a new splitting criterion for [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , the mean absolute error. This criterion can also be used in [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , and the gradient boosting estimators. [#6667](https://github.com/scikit-learn/scikit-learn/issues/6667)
     by [Nelson Liu](https://github.com/nelson-liu)
    .
    
*   Added weighted impurity-based early stopping criterion for decision tree growth. [#6954](https://github.com/scikit-learn/scikit-learn/issues/6954)
     by [Nelson Liu](https://github.com/nelson-liu)
    
*   The random forest, extra tree and decision tree estimators now has a method `decision_path` which returns the decision path of samples in the tree. By [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   A new example has been added unveiling the decision tree structure. By [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Random forest, extra trees, decision trees and gradient boosting estimator accept the parameter `min_samples_split` and `min_samples_leaf` provided as a percentage of the training samples. By [yelite](https://github.com/yelite)
     and [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Gradient boosting estimators accept the parameter `criterion` to specify to splitting criterion used in built decision trees. [#6667](https://github.com/scikit-learn/scikit-learn/issues/6667)
     by [Nelson Liu](https://github.com/nelson-liu)
    .
    
*   The memory footprint is reduced (sometimes greatly) for `ensemble.bagging.BaseBagging` and classes that inherit from it, i.e, [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
    , [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
    , and [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
    , by dynamically generating attribute `estimators_samples_` only when it is needed. By [David Staub](https://github.com/staubda)
    .
    
*   Added `n_jobs` and `sample_weight` parameters for [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     to fit underlying estimators in parallel. [#5805](https://github.com/scikit-learn/scikit-learn/issues/5805)
     by [Ibraim Ganiev](https://github.com/olologin)
    .
    

Linear, kernelized and related models

*   In [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    , the SAG solver is now available in the multinomial case. [#5251](https://github.com/scikit-learn/scikit-learn/issues/5251)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
    , [`svm.LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
     and [`svm.LinearSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR "sklearn.svm.LinearSVR")
     now support `sample_weight`. By [Imaculate](https://github.com/Imaculate)
    .
    
*   Add parameter `loss` to [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
     to measure the error on the samples for every trial. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Prediction of out-of-sample events with Isotonic Regression ([`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
    ) is now much faster (over 1000x in tests with synthetic data). By [Jonathan Arfa](https://github.com/jarfa)
    .
    
*   Isotonic regression ([`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
    ) now uses a better algorithm to avoid `O(n^2)` behavior in pathological cases, and is also generally faster ([##6691](https://github.com/scikit-learn/scikit-learn/issues/#6691)
    ). By [Antony Lee](https://www.ocf.berkeley.edu/~antonyl/)
    .
    
*   [`naive_bayes.GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
     now accepts data-independent class-priors through the parameter `priors`. By [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     and [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     now works with `np.float32` input data without converting it into `np.float64`. This allows to reduce the memory consumption. [#6913](https://github.com/scikit-learn/scikit-learn/issues/6913)
     by [YenChen Lin](https://github.com/yenchenlin)
    .
    
*   [`semi_supervised.LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")
     and [`semi_supervised.LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
     now accept arbitrary kernel functions in addition to strings `knn` and `rbf`. [#5762](https://github.com/scikit-learn/scikit-learn/issues/5762)
     by [Utkarsh Upadhyay](https://github.com/musically-ut)
    .
    

Decomposition, manifold learning and clustering

*   Added `inverse_transform` function to [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     to compute data matrix of original shape. By [Anish Shah](https://github.com/AnishShah)
    .
    
*   [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     and [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     now works with `np.float32` and `np.float64` input data without converting it. This allows to reduce the memory consumption by using `np.float32`. [#6846](https://github.com/scikit-learn/scikit-learn/issues/6846)
     by [Sebastian Säger](https://github.com/ssaeger)
     and [YenChen Lin](https://github.com/yenchenlin)
    .
    

Preprocessing and feature selection

*   [`preprocessing.RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
     now accepts `quantile_range` parameter. [#5929](https://github.com/scikit-learn/scikit-learn/issues/5929)
     by [Konstantin Podshumok](https://github.com/podshumok)
    .
    
*   [`feature_extraction.FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
     now accepts string values. [#6173](https://github.com/scikit-learn/scikit-learn/issues/6173)
     by [Ryad Zenine](https://github.com/ryadzenine)
     and [Devashish Deshpande](https://github.com/dsquareindia)
    .
    
*   Keyword arguments can now be supplied to `func` in [`preprocessing.FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
     by means of the `kw_args` parameter. By [Brian McFee](https://bmcfee.github.io/)
    .
    
*   [`feature_selection.SelectKBest`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
     and [`feature_selection.SelectPercentile`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile")
     now accept score functions that take X, y as input and return only the scores. By [Nikolay Mayorov](https://github.com/nmayorov)
    .
    

Model evaluation and meta-estimators

*   [`multiclass.OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
     and [`multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
     now support `partial_fit`. By [Asish Panda](https://github.com/kaichogami)
     and [Philipp Dowling](https://github.com/phdowling)
    .
    
*   Added support for substituting or disabling [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     and [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     components using the `set_params` interface that powers `sklearn.grid_search`. See [Selecting dimensionality reduction with Pipeline and GridSearchCV](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html#sphx-glr-auto-examples-compose-plot-compare-reduction-py)
     By [Joel Nothman](https://joelnothman.com/)
     and [Robert McGibbon](https://github.com/rmcgibbo)
    .
    
*   The new `cv_results_` attribute of [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     (and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
    ) can be easily imported into pandas as a `DataFrame`. Ref [Model Selection Enhancements and API Changes](https://scikit-learn.org/stable/whats_new/v0.18.html#model-selection-changes)
     for more information. [#6697](https://github.com/scikit-learn/scikit-learn/issues/6697)
     by [Raghav RV](https://github.com/raghavrv)
    .
    
*   Generalization of [`model_selection.cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
    . One can pass method names such as `predict_proba` to be used in the cross validation framework instead of the default `predict`. By [Ori Ziv](https://github.com/zivori)
     and [Sears Merritt](https://github.com/merritts)
    .
    
*   The training scores and time taken for training followed by scoring for each search candidate are now available at the `cv_results_` dict. See [Model Selection Enhancements and API Changes](https://scikit-learn.org/stable/whats_new/v0.18.html#model-selection-changes)
     for more information. [#7325](https://github.com/scikit-learn/scikit-learn/issues/7325)
     by [Eugene Chen](https://github.com/eyc88)
     and [Raghav RV](https://github.com/raghavrv)
    .
    

Metrics

*   Added `labels` flag to [`metrics.log_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
     to explicitly provide the labels when the number of classes in `y_true` and `y_pred` differ. [#7239](https://github.com/scikit-learn/scikit-learn/issues/7239)
     by [Hong Guangguo](https://github.com/hongguangguo)
     with help from [Mads Jensen](https://github.com/indianajensen)
     and [Nelson Liu](https://github.com/nelson-liu)
    .
    
*   Support sparse contingency matrices in cluster evaluation (`metrics.cluster.supervised`) to scale to a large number of clusters. [#7419](https://github.com/scikit-learn/scikit-learn/issues/7419)
     by [Gregory Stupp](https://github.com/stuppie)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   Add `sample_weight` parameter to [`metrics.matthews_corrcoef`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html#sklearn.metrics.matthews_corrcoef "sklearn.metrics.matthews_corrcoef")
    . By [Jatin Shah](https://github.com/jatinshah)
     and [Raghav RV](https://github.com/raghavrv)
    .
    
*   Speed up [`metrics.silhouette_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")
     by using vectorized operations. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Add `sample_weight` parameter to [`metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
    . By [Bernardo Stein](https://github.com/DanielSidhion)
    .
    

Miscellaneous

*   Added `n_jobs` parameter to [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
     to compute the score on the test folds in parallel. By [Manoj Kumar](https://manojbits.wordpress.com/)
    
*   Codebase does not contain C/C++ cython generated files: they are generated during build. Distribution packages will still contain generated C/C++ files. By [Arthur Mensch](https://github.com/arthurmensch)
    .
    
*   Reduce the memory usage for 32-bit float input arrays of `utils.sparse_func.mean_variance_axis` and `utils.sparse_func.incr_mean_variance_axis` by supporting cython fused types. By [YenChen Lin](https://github.com/yenchenlin)
    .
    
*   The `ignore_warnings` now accept a category argument to ignore only the warnings of a specified type. By [Thierry Guillemot](https://github.com/tguillemot)
    .
    
*   Added parameter `return_X_y` and return type `(data, target) : tuple` option to [`datasets.load_iris`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
     dataset [#7049](https://github.com/scikit-learn/scikit-learn/issues/7049)
    , [`datasets.load_breast_cancer`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer "sklearn.datasets.load_breast_cancer")
     dataset [#7152](https://github.com/scikit-learn/scikit-learn/issues/7152)
    , [`datasets.load_digits`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
     dataset, [`datasets.load_diabetes`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
     dataset, [`datasets.load_linnerud`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html#sklearn.datasets.load_linnerud "sklearn.datasets.load_linnerud")
     dataset, `datasets.load_boston` dataset [#7154](https://github.com/scikit-learn/scikit-learn/issues/7154)
     by [Manvendra Singh](https://github.com/manu-chroma)
    .
    
*   Simplification of the `clone` function, deprecate support for estimators that modify parameters in `__init__`. [#5540](https://github.com/scikit-learn/scikit-learn/issues/5540)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   When unpickling a scikit-learn estimator in a different version than the one the estimator was trained with, a `UserWarning` is raised, see [the documentation on model persistence](https://scikit-learn.org/stable/model_persistence.html#persistence-limitations)
     for more details. ([#7248](https://github.com/scikit-learn/scikit-learn/issues/7248)
    ) By [Andreas Müller](https://amueller.github.io/)
    .
    

#### Bug fixes[#](https://scikit-learn.org/stable/whats_new/v0.18.html#id5 "Link to this heading")

Trees and ensembles

*   Random forest, extra trees, decision trees and gradient boosting won’t accept anymore `min_samples_split=1` as at least 2 samples are required to split a decision tree node. By [Arnaud Joly](http://www.ajoly.org/)
    
*   [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     now raises `NotFittedError` if `predict`, `transform` or `predict_proba` are called on the non-fitted estimator. by [Sebastian Raschka](https://sebastianraschka.com/)
    .
    
*   Fix bug where [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
     and [`ensemble.AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
     would perform poorly if the `random_state` was fixed ([#7411](https://github.com/scikit-learn/scikit-learn/issues/7411)
    ). By [Joel Nothman](https://joelnothman.com/)
    .
    
*   Fix bug in ensembles with randomization where the ensemble would not set `random_state` on base estimators in a pipeline or similar nesting. ([#7411](https://github.com/scikit-learn/scikit-learn/issues/7411)
    ). Note, results for [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
     [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
    , [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
     and [`ensemble.AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
     will now differ from previous versions. By [Joel Nothman](https://joelnothman.com/)
    .
    

Linear, kernelized and related models

*   Fixed incorrect gradient computation for `loss='squared_epsilon_insensitive'` in [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     and [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     ([#6764](https://github.com/scikit-learn/scikit-learn/issues/6764)
    ). By [Wenhua Yang](https://github.com/geekoala)
    .
    
*   Fix bug in [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     where `solver='liblinear'` did not accept `class_weights='balanced`. ([#6817](https://github.com/scikit-learn/scikit-learn/issues/6817)
    ). By [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Fix bug in [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
     where an error occurred when there were outliers being labelled and a weight function specified ([#6902](https://github.com/scikit-learn/scikit-learn/issues/6902)
    ). By [LeonieBorne](https://github.com/LeonieBorne)
    .
    
*   Fix [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     sparse decision function to match output with dense in the multioutput case.
    

Decomposition, manifold learning and clustering

*   `decomposition.RandomizedPCA` default number of `iterated_power` is 4 instead of 3. [#5141](https://github.com/scikit-learn/scikit-learn/issues/5141)
     by [Giorgio Patrini](https://github.com/giorgiop)
    .
    
*   [`utils.extmath.randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
     performs 4 power iterations by default, instead of 0. In practice this is enough for obtaining a good approximation of the true eigenvalues/vectors in the presence of noise. When `n_components` is small (`< .1 * min(X.shape)`) `n_iter` is set to 7, unless the user specifies a higher number. This improves precision with few components. [#5299](https://github.com/scikit-learn/scikit-learn/issues/5299)
     by [Giorgio Patrini](https://github.com/giorgiop)
    .
    
*   Whiten/non-whiten inconsistency between components of [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     and `decomposition.RandomizedPCA` (now factored into PCA, see the New features) is fixed. `components_` are stored with no whitening. [#5299](https://github.com/scikit-learn/scikit-learn/issues/5299)
     by [Giorgio Patrini](https://github.com/giorgiop)
    .
    
*   Fixed bug in [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
     where diagonal of unnormalized Laplacian matrix was incorrectly set to 1. [#4995](https://github.com/scikit-learn/scikit-learn/issues/4995)
     by [Peter Fischer](https://github.com/yanlend)
    .
    
*   Fixed incorrect initialization of `utils.arpack.eigsh` on all occurrences. Affects `cluster.bicluster.SpectralBiclustering`, [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
    , [`manifold.LocallyLinearEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
    , and [`manifold.SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
     ([#5012](https://github.com/scikit-learn/scikit-learn/issues/5012)
    ). By [Peter Fischer](https://github.com/yanlend)
    .
    
*   Attribute `explained_variance_ratio_` calculated with the SVD solver of [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     now returns correct results. By [JPFrancoia](https://github.com/JPFrancoia)
    

Preprocessing and feature selection

*   `preprocessing.data._transform_selected` now always passes a copy of `X` to transform function when `copy=True` ([#7194](https://github.com/scikit-learn/scikit-learn/issues/7194)
    ). By [Caio Oliveira](https://github.com/caioaao)
    .
    

Model evaluation and meta-estimators

*   [`model_selection.StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
     now raises error if all n\_labels for individual classes is less than n\_folds. [#6182](https://github.com/scikit-learn/scikit-learn/issues/6182)
     by [Devashish Deshpande](https://github.com/dsquareindia)
    .
    
*   Fixed bug in [`model_selection.StratifiedShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")
     where train and test sample could overlap in some edge cases, see [#6121](https://github.com/scikit-learn/scikit-learn/issues/6121)
     for more details. By [Loic Esteve](https://github.com/lesteve)
    .
    
*   Fix in [`sklearn.model_selection.StratifiedShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")
     to return splits of size `train_size` and `test_size` in all cases ([#6472](https://github.com/scikit-learn/scikit-learn/issues/6472)
    ). By [Andreas Müller](https://amueller.github.io/)
    .
    
*   Cross-validation of [`multiclass.OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
     and [`multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
     now works with precomputed kernels. [#7350](https://github.com/scikit-learn/scikit-learn/issues/7350)
     by [Russell Smith](https://github.com/rsmith54)
    .
    
*   Fix incomplete `predict_proba` method delegation from [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     to [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     ([#7159](https://github.com/scikit-learn/scikit-learn/issues/7159)
    ) by [Yichuan Liu](https://github.com/yl565)
    .
    

Metrics

*   Fix bug in [`metrics.silhouette_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")
     in which clusters of size 1 were incorrectly scored. They should get a score of 0. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   Fix bug in [`metrics.silhouette_samples`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html#sklearn.metrics.silhouette_samples "sklearn.metrics.silhouette_samples")
     so that it now works with arbitrary labels, not just those ranging from 0 to n\_clusters - 1.
    
*   Fix bug where expected and adjusted mutual information were incorrect if cluster contingency cells exceeded `2**16`. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     now converts arrays to boolean arrays when required in `scipy.spatial.distance`. [#5460](https://github.com/scikit-learn/scikit-learn/issues/5460)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Fix sparse input support in [`metrics.silhouette_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")
     as well as example examples/text/document\_clustering.py. By [YenChen Lin](https://github.com/yenchenlin)
    .
    
*   [`metrics.roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
     and [`metrics.precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")
     no longer round `y_score` values when creating ROC curves; this was causing problems for users with very small differences in scores ([#7353](https://github.com/scikit-learn/scikit-learn/issues/7353)
    ).
    

Miscellaneous

*   `model_selection.tests._search._check_param_grid` now works correctly with all types that extends/implements `Sequence` (except string), including range (Python 3.x) and xrange (Python 2.x). [#7323](https://github.com/scikit-learn/scikit-learn/issues/7323)
     by Viacheslav Kovalevskyi.
    
*   [`utils.extmath.randomized_range_finder`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_range_finder.html#sklearn.utils.extmath.randomized_range_finder "sklearn.utils.extmath.randomized_range_finder")
     is more numerically stable when many power iterations are requested, since it applies LU normalization by default. If `n_iter<2` numerical issues are unlikely, thus no normalization is applied. Other normalization options are available: `'none', 'LU'` and `'QR'`. [#5141](https://github.com/scikit-learn/scikit-learn/issues/5141)
     by [Giorgio Patrini](https://github.com/giorgiop)
    .
    
*   Fix a bug where some formats of `scipy.sparse` matrix, and estimators with them as parameters, could not be passed to [`base.clone`](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#sklearn.base.clone "sklearn.base.clone")
    . By [Loic Esteve](https://github.com/lesteve)
    .
    
*   [`datasets.load_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html#sklearn.datasets.load_svmlight_file "sklearn.datasets.load_svmlight_file")
     now is able to read long int QID values. [#7101](https://github.com/scikit-learn/scikit-learn/issues/7101)
     by [Ibraim Ganiev](https://github.com/olologin)
    .
    

### API changes summary[#](https://scikit-learn.org/stable/whats_new/v0.18.html#id6 "Link to this heading")

Linear, kernelized and related models

*   `residual_metric` has been deprecated in [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
    . Use `loss` instead. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Access to public attributes `.X_` and `.y_` has been deprecated in [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
    . By [Jonathan Arfa](https://github.com/jarfa)
    .
    

Decomposition, manifold learning and clustering

*   The old `mixture.DPGMM` is deprecated in favor of the new [`mixture.BayesianGaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")
     (with the parameter `weight_concentration_prior_type='dirichlet_process'`). The new class solves the computational problems of the old class and computes the Gaussian mixture with a Dirichlet process prior faster than before. [#7295](https://github.com/scikit-learn/scikit-learn/issues/7295)
     by [Wei Xue](https://github.com/xuewei4d)
     and [Thierry Guillemot](https://github.com/tguillemot)
    .
    
*   The old `mixture.VBGMM` is deprecated in favor of the new [`mixture.BayesianGaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")
     (with the parameter `weight_concentration_prior_type='dirichlet_distribution'`). The new class solves the computational problems of the old class and computes the Variational Bayesian Gaussian mixture faster than before. [#6651](https://github.com/scikit-learn/scikit-learn/issues/6651)
     by [Wei Xue](https://github.com/xuewei4d)
     and [Thierry Guillemot](https://github.com/tguillemot)
    .
    
*   The old `mixture.GMM` is deprecated in favor of the new [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
    . The new class computes the Gaussian mixture faster than before and some of computational problems have been solved. [#6666](https://github.com/scikit-learn/scikit-learn/issues/6666)
     by [Wei Xue](https://github.com/xuewei4d)
     and [Thierry Guillemot](https://github.com/tguillemot)
    .
    

Model evaluation and meta-estimators

*   The `sklearn.cross_validation`, `sklearn.grid_search` and `sklearn.learning_curve` have been deprecated and the classes and functions have been reorganized into the [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
     module. Ref [Model Selection Enhancements and API Changes](https://scikit-learn.org/stable/whats_new/v0.18.html#model-selection-changes)
     for more information. [#4294](https://github.com/scikit-learn/scikit-learn/issues/4294)
     by [Raghav RV](https://github.com/raghavrv)
    .
    
*   The `grid_scores_` attribute of [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     is deprecated in favor of the attribute `cv_results_`. Ref [Model Selection Enhancements and API Changes](https://scikit-learn.org/stable/whats_new/v0.18.html#model-selection-changes)
     for more information. [#6697](https://github.com/scikit-learn/scikit-learn/issues/6697)
     by [Raghav RV](https://github.com/raghavrv)
    .
    
*   The parameters `n_iter` or `n_folds` in old CV splitters are replaced by the new parameter `n_splits` since it can provide a consistent and unambiguous interface to represent the number of train-test splits. [#7187](https://github.com/scikit-learn/scikit-learn/issues/7187)
     by [YenChen Lin](https://github.com/yenchenlin)
    .
    
*   `classes` parameter was renamed to `labels` in [`metrics.hamming_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "sklearn.metrics.hamming_loss")
    . [#7260](https://github.com/scikit-learn/scikit-learn/issues/7260)
     by [Sebastián Vanrell](https://github.com/srvanrell)
    .
    
*   The splitter classes `LabelKFold`, `LabelShuffleSplit`, `LeaveOneLabelOut` and `LeavePLabelsOut` are renamed to [`model_selection.GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
    , [`model_selection.GroupShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit "sklearn.model_selection.GroupShuffleSplit")
    , [`model_selection.LeaveOneGroupOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut "sklearn.model_selection.LeaveOneGroupOut")
     and [`model_selection.LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut")
     respectively. Also the parameter `labels` in the `split` method of the newly renamed splitters [`model_selection.LeaveOneGroupOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut "sklearn.model_selection.LeaveOneGroupOut")
     and [`model_selection.LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut")
     is renamed to `groups`. Additionally in [`model_selection.LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut")
    , the parameter `n_labels` is renamed to `n_groups`. [#6660](https://github.com/scikit-learn/scikit-learn/issues/6660)
     by [Raghav RV](https://github.com/raghavrv)
    .
    
*   Error and loss names for `scoring` parameters are now prefixed by `'neg_'`, such as `neg_mean_squared_error`. The unprefixed versions are deprecated and will be removed in version 0.20. [#7261](https://github.com/scikit-learn/scikit-learn/issues/7261)
     by [Tim Head](https://github.com/betatim)
    .
    

### Code Contributors[#](https://scikit-learn.org/stable/whats_new/v0.18.html#id7 "Link to this heading")

Aditya Joshi, Alejandro, Alexander Fabisch, Alexander Loginov, Alexander Minyushkin, Alexander Rudy, Alexandre Abadie, Alexandre Abraham, Alexandre Gramfort, Alexandre Saint, alexfields, Alvaro Ulloa, alyssaq, Amlan Kar, Andreas Mueller, andrew giessel, Andrew Jackson, Andrew McCulloh, Andrew Murray, Anish Shah, Arafat, Archit Sharma, Ariel Rokem, Arnaud Joly, Arnaud Rachez, Arthur Mensch, Ash Hoover, asnt, b0noI, Behzad Tabibian, Bernardo, Bernhard Kratzwald, Bhargav Mangipudi, blakeflei, Boyuan Deng, Brandon Carter, Brett Naul, Brian McFee, Caio Oliveira, Camilo Lamus, Carol Willing, Cass, CeShine Lee, Charles Truong, Chyi-Kwei Yau, CJ Carey, codevig, Colin Ni, Dan Shiebler, Daniel, Daniel Hnyk, David Ellis, David Nicholson, David Staub, David Thaler, David Warshaw, Davide Lasagna, Deborah, definitelyuncertain, Didi Bar-Zev, djipey, dsquareindia, edwinENSAE, Elias Kuthe, Elvis DOHMATOB, Ethan White, Fabian Pedregosa, Fabio Ticconi, fisache, Florian Wilhelm, Francis, Francis O’Donovan, Gael Varoquaux, Ganiev Ibraim, ghg, Gilles Louppe, Giorgio Patrini, Giovanni Cherubin, Giovanni Lanzani, Glenn Qian, Gordon Mohr, govin-vatsan, Graham Clenaghan, Greg Reda, Greg Stupp, Guillaume Lemaitre, Gustav Mörtberg, halwai, Harizo Rajaona, Harry Mavroforakis, hashcode55, hdmetor, Henry Lin, Hobson Lane, Hugo Bowne-Anderson, Igor Andriushchenko, Imaculate, Inki Hwang, Isaac Sijaranamual, Ishank Gulati, Issam Laradji, Iver Jordal, jackmartin, Jacob Schreiber, Jake Vanderplas, James Fiedler, James Routley, Jan Zikes, Janna Brettingen, jarfa, Jason Laska, jblackburne, jeff levesque, Jeffrey Blackburne, Jeffrey04, Jeremy Hintz, jeremynixon, Jeroen, Jessica Yung, Jill-Jênn Vie, Jimmy Jia, Jiyuan Qian, Joel Nothman, johannah, John, John Boersma, John Kirkham, John Moeller, jonathan.striebel, joncrall, Jordi, Joseph Munoz, Joshua Cook, JPFrancoia, jrfiedler, JulianKahnert, juliathebrave, kaichogami, KamalakerDadi, Kenneth Lyons, Kevin Wang, kingjr, kjell, Konstantin Podshumok, Kornel Kielczewski, Krishna Kalyan, krishnakalyan3, Kvle Putnam, Kyle Jackson, Lars Buitinck, ldavid, LeiG, LeightonZhang, Leland McInnes, Liang-Chi Hsieh, Lilian Besson, lizsz, Loic Esteve, Louis Tiao, Léonie Borne, Mads Jensen, Maniteja Nandana, Manoj Kumar, Manvendra Singh, Marco, Mario Krell, Mark Bao, Mark Szepieniec, Martin Madsen, MartinBpr, MaryanMorel, Massil, Matheus, Mathieu Blondel, Mathieu Dubois, Matteo, Matthias Ekman, Max Moroz, Michael Scherer, michiaki ariga, Mikhail Korobov, Moussa Taifi, mrandrewandrade, Mridul Seth, nadya-p, Naoya Kanai, Nate George, Nelle Varoquaux, Nelson Liu, Nick James, NickleDave, Nico, Nicolas Goix, Nikolay Mayorov, ningchi, nlathia, okbalefthanded, Okhlopkov, Olivier Grisel, Panos Louridas, Paul Strickland, Perrine Letellier, pestrickland, Peter Fischer, Pieter, Ping-Yao, Chang, practicalswift, Preston Parry, Qimu Zheng, Rachit Kansal, Raghav RV, Ralf Gommers, Ramana.S, Rammig, Randy Olson, Rob Alexander, Robert Lutz, Robin Schucker, Rohan Jain, Ruifeng Zheng, Ryan Yu, Rémy Léone, saihttam, Saiwing Yeung, Sam Shleifer, Samuel St-Jean, Sartaj Singh, Sasank Chilamkurthy, saurabh.bansod, Scott Andrews, Scott Lowe, seales, Sebastian Raschka, Sebastian Saeger, Sebastián Vanrell, Sergei Lebedev, shagun Sodhani, shanmuga cv, Shashank Shekhar, shawpan, shengxiduan, Shota, shuckle16, Skipper Seabold, sklearn-ci, SmedbergM, srvanrell, Sébastien Lerique, Taranjeet, themrmax, Thierry, Thierry Guillemot, Thomas, Thomas Hallock, Thomas Moreau, Tim Head, tKammy, toastedcornflakes, Tom, TomDLT, Toshihiro Kamishima, tracer0tong, Trent Hauck, trevorstephens, Tue Vo, Varun, Varun Jewalikar, Viacheslav, Vighnesh Birodkar, Vikram, Villu Ruusmann, Vinayak Mehta, walter, waterponey, Wenhua Yang, Wenjian Huang, Will Welch, wyseguy7, xyguo, yanlend, Yaroslav Halchenko, yelite, Yen, YenChenLin, Yichuan Liu, Yoav Ram, Yoshiki, Zheng RuiFeng, zivori, Óscar Nájera

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)