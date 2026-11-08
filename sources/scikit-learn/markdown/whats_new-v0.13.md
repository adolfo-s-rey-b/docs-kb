[Skip to main content](https://scikit-learn.org/stable/whats_new/v0.13.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v0.13.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v0.13.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v0.13.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v0.13.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v0.13.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v0.13.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v0.13.html)

Collapse Sidebar Expand Sidebar

Version 0.13[#](https://scikit-learn.org/stable/whats_new/v0.13.html#version-0-13 "Link to this heading")

==========================================================================================================

Version 0.13.1[#](https://scikit-learn.org/stable/whats_new/v0.13.html#version-0-13-1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**February 23, 2013**

The 0.13.1 release only fixes some bugs and does not add any new functionality.

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.13.html#changelog "Link to this heading")

*   Fixed a testing error caused by the function `cross_validation.train_test_split` being interpreted as a test by [Yaroslav Halchenko](http://www.onerussian.com/)
    .
    
*   Fixed a bug in the reassignment of small clusters in the [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     by [Gael Varoquaux](https://gael-varoquaux.info/)
    .
    
*   Fixed default value of `gamma` in [`decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
     by [Lars Buitinck](https://github.com/larsmans)
    .
    
*   Updated joblib to `0.7.0d` by [Gael Varoquaux](https://gael-varoquaux.info/)
    .
    
*   Fixed scaling of the deviance in [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     by [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    .
    
*   Better tie-breaking in [`multiclass.OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Other small improvements to tests and documentation.
    

### People[#](https://scikit-learn.org/stable/whats_new/v0.13.html#people "Link to this heading")

List of contributors for release 0.13.1 by number of commits.

*   16 [Lars Buitinck](https://github.com/larsmans)
    
*   12 [Andreas Müller](https://amueller.github.io/)
    
*   8 [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   5 Robert Marchman
    
*   3 [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    
*   2 Hrishikesh Huilgolkar
    
*   1 Bastiaan van den Berg
    
*   1 Diego Molla
    
*   1 [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    
*   1 [Mathieu Blondel](http://www.mblondel.org/)
    
*   1 [Nelle Varoquaux](https://github.com/nellev)
    
*   1 Rafael Cunha de Almeida
    
*   1 Rolando Espinoza La fuente
    
*   1 [Vlad Niculae](https://vene.ro/)
    
*   1 [Yaroslav Halchenko](http://www.onerussian.com/)
    

Version 0.13[#](https://scikit-learn.org/stable/whats_new/v0.13.html#changes-0-13 "Link to this heading")

----------------------------------------------------------------------------------------------------------

**January 21, 2013**

### New Estimator Classes[#](https://scikit-learn.org/stable/whats_new/v0.13.html#new-estimator-classes "Link to this heading")

*   [`dummy.DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
     and [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
    , two data-independent predictors by [Mathieu Blondel](http://www.mblondel.org/)
    . Useful to sanity-check your estimators. See [Dummy estimators](https://scikit-learn.org/stable/modules/model_evaluation.html#dummy-estimators)
     in the user guide. Multioutput support added by [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   [`decomposition.FactorAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")
    , a transformer implementing the classical factor analysis, by [Christian Osendorfer](https://osdf.github.io/)
     and [Alexandre Gramfort](https://alexandre.gramfort.net/)
    . See [Factor Analysis](https://scikit-learn.org/stable/modules/decomposition.html#fa)
     in the user guide.
    
*   [`feature_extraction.FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
    , a transformer implementing the “hashing trick” for fast, low-memory feature extraction from string fields by [Lars Buitinck](https://github.com/larsmans)
     and [`feature_extraction.text.HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
     for text documents by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
     See [Feature hashing](https://scikit-learn.org/stable/modules/feature_extraction.html#feature-hashing)
     and [Vectorizing a large text corpus with the hashing trick](https://scikit-learn.org/stable/modules/feature_extraction.html#hashing-vectorizer)
     for the documentation and sample usage.
    
*   [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
    , a transformer that concatenates results of several other transformers by [Andreas Müller](https://amueller.github.io/)
    . See [FeatureUnion: composite feature spaces](https://scikit-learn.org/stable/modules/compose.html#feature-union)
     in the user guide.
    
*   [`random_projection.GaussianRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection "sklearn.random_projection.GaussianRandomProjection")
    , [`random_projection.SparseRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection")
     and the function [`random_projection.johnson_lindenstrauss_min_dim`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html#sklearn.random_projection.johnson_lindenstrauss_min_dim "sklearn.random_projection.johnson_lindenstrauss_min_dim")
    . The first two are transformers implementing Gaussian and sparse random projection matrix by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
     and [Arnaud Joly](http://www.ajoly.org/)
    . See [Random Projection](https://scikit-learn.org/stable/modules/random_projection.html#random-projection)
     in the user guide.
    
*   [`kernel_approximation.Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
    , a transformer for approximating arbitrary kernels by [Andreas Müller](https://amueller.github.io/)
    . See [Nystroem Method for Kernel Approximation](https://scikit-learn.org/stable/modules/kernel_approximation.html#nystroem-kernel-approx)
     in the user guide.
    
*   [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
    , a transformer that computes binary encodings of categorical features by [Andreas Müller](https://amueller.github.io/)
    . See [Encoding categorical features](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-categorical-features)
     in the user guide.
    
*   [`linear_model.PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier")
     and [`linear_model.PassiveAggressiveRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model.PassiveAggressiveRegressor")
    , predictors implementing an efficient stochastic optimization for linear models by [Rob Zinkov](https://www.zinkov.com/)
     and [Mathieu Blondel](http://www.mblondel.org/)
    . See [Passive Aggressive Algorithms](https://scikit-learn.org/stable/modules/linear_model.html#passive-aggressive)
     in the user guide.
    
*   [`ensemble.RandomTreesEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")
    , a transformer for creating high-dimensional sparse representations using ensembles of totally random trees by [Andreas Müller](https://amueller.github.io/)
    . See [Totally Random Trees Embedding](https://scikit-learn.org/stable/modules/ensemble.html#random-trees-embedding)
     in the user guide.
    
*   [`manifold.SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
     and function [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
    , implementing the “laplacian eigenmaps” transformation for non-linear dimensionality reduction by Wei Li. See [Spectral Embedding](https://scikit-learn.org/stable/modules/manifold.html#spectral-embedding)
     in the user guide.
    
*   [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
     by [Fabian Pedregosa](https://fa.bianp.net/)
    , [Alexandre Gramfort](https://alexandre.gramfort.net/)
     and [Nelle Varoquaux](https://github.com/nellev)
    ,
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.13.html#id2 "Link to this heading")

*   [`metrics.zero_one_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "sklearn.metrics.zero_one_loss")
     (formerly `metrics.zero_one`) now has an option for normalized output that reports the fraction of misclassifications, rather than the raw number of misclassifications. By Kyle Beauchamp.
    
*   [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
     and all derived ensemble models now support sample weighting, by [Noel Dawe](https://github.com/ndawe)
     and [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   Speedup improvement when using bootstrap samples in forests of randomized trees, by [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
     and [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   Partial dependence plots for [Gradient-boosted trees](https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting)
     in `ensemble.partial_dependence.partial_dependence` by [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    . See [Partial Dependence and Individual Conditional Expectation Plots](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#sphx-glr-auto-examples-inspection-plot-partial-dependence-py)
     for an example.
    
*   The table of contents on the website has now been made expandable by [Jaques Grobler](https://github.com/jaquesgrobler)
    .
    
*   [`feature_selection.SelectPercentile`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile")
     now breaks ties deterministically instead of returning all equally ranked features.
    
*   [`feature_selection.SelectKBest`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
     and [`feature_selection.SelectPercentile`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile")
     are more numerically stable since they use scores, rather than p-values, to rank results. This means that they might sometimes select different features than they did previously.
    
*   Ridge regression and ridge classification fitting with `sparse_cg` solver no longer has quadratic memory complexity, by [Lars Buitinck](https://github.com/larsmans)
     and [Fabian Pedregosa](https://fa.bianp.net/)
    .
    
*   Ridge regression and ridge classification now support a new fast solver called `lsqr`, by [Mathieu Blondel](http://www.mblondel.org/)
    .
    
*   Speed up of [`metrics.precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")
     by Conrad Lee.
    
*   Added support for reading/writing svmlight files with pairwise preference attribute (qid in svmlight file format) in [`datasets.dump_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.dump_svmlight_file.html#sklearn.datasets.dump_svmlight_file "sklearn.datasets.dump_svmlight_file")
     and [`datasets.load_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html#sklearn.datasets.load_svmlight_file "sklearn.datasets.load_svmlight_file")
     by [Fabian Pedregosa](https://fa.bianp.net/)
    .
    
*   Faster and more robust [`metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
     and [Clustering performance evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation)
     by Wei Li.
    
*   `cross_validation.cross_val_score` now works with precomputed kernels and affinity matrices, by [Andreas Müller](https://amueller.github.io/)
    .
    
*   LARS algorithm made more numerically stable with heuristics to drop regressors too correlated as well as to stop the path when numerical noise becomes predominant, by [Gael Varoquaux](https://gael-varoquaux.info/)
    .
    
*   Faster implementation of [`metrics.precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")
     by Conrad Lee.
    
*   New kernel `metrics.chi2_kernel` by [Andreas Müller](https://amueller.github.io/)
    , often used in computer vision applications.
    
*   Fix of longstanding bug in [`naive_bayes.BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
     fixed by Shaun Jackman.
    
*   Implemented `predict_proba` in [`multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
    , by Andrew Winterman.
    
*   Improve consistency in gradient boosting: estimators [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     and [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     use the estimator [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
     instead of the `tree._tree.Tree` data structure by [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Fixed a floating point exception in the [decision trees](https://scikit-learn.org/stable/modules/tree.html#tree)
     module, by Seberg.
    
*   Fix [`metrics.roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
     fails when y\_true has only one class by Wei Li.
    
*   Add the [`metrics.mean_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
     function which computes the mean absolute error. The [`metrics.mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
    , [`metrics.mean_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
     and [`metrics.r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
     metrics support multioutput by [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Fixed `class_weight` support in [`svm.LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
     and [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     by [Andreas Müller](https://amueller.github.io/)
    . The meaning of `class_weight` was reversed as erroneously higher weight meant less positives of a given class in earlier releases.
    
*   Improve narrative documentation and consistency in [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
     for regression and classification metrics by [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Fixed a bug in [`sklearn.svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     when using csr-matrices with unsorted indices by Xinfan Meng and [Andreas Müller](https://amueller.github.io/)
    .
    
*   [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
    : Add random reassignment of cluster centers with little observations attached to them, by [Gael Varoquaux](https://gael-varoquaux.info/)
    .
    

### API changes summary[#](https://scikit-learn.org/stable/whats_new/v0.13.html#api-changes-summary "Link to this heading")

*   Renamed all occurrences of `n_atoms` to `n_components` for consistency. This applies to [`decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
    , [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
    , [`decomposition.dict_learning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#sklearn.decomposition.dict_learning "sklearn.decomposition.dict_learning")
    , [`decomposition.dict_learning_online`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html#sklearn.decomposition.dict_learning_online "sklearn.decomposition.dict_learning_online")
    .
    
*   Renamed all occurrences of `max_iters` to `max_iter` for consistency. This applies to `semi_supervised.LabelPropagation` and `semi_supervised.label_propagation.LabelSpreading`.
    
*   Renamed all occurrences of `learn_rate` to `learning_rate` for consistency in `ensemble.BaseGradientBoosting` and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
    .
    
*   The module `sklearn.linear_model.sparse` is gone. Sparse matrix support was already integrated into the “regular” linear models.
    
*   `sklearn.metrics.mean_square_error`, which incorrectly returned the accumulated error, was removed. Use [`metrics.mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
     instead.
    
*   Passing `class_weight` parameters to `fit` methods is no longer supported. Pass them to estimator constructors instead.
    
*   GMMs no longer have `decode` and `rvs` methods. Use the `score`, `predict` or `sample` methods instead.
    
*   The `solver` fit option in Ridge regression and classification is now deprecated and will be removed in v0.14. Use the constructor option instead.
    
*   `feature_extraction.text.DictVectorizer` now returns sparse matrices in the CSR format, instead of COO.
    
*   Renamed `k` in `cross_validation.KFold` and `cross_validation.StratifiedKFold` to `n_folds`, renamed `n_bootstraps` to `n_iter` in `cross_validation.Bootstrap`.
    
*   Renamed all occurrences of `n_iterations` to `n_iter` for consistency. This applies to `cross_validation.ShuffleSplit`, `cross_validation.StratifiedShuffleSplit`, [`utils.extmath.randomized_range_finder`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_range_finder.html#sklearn.utils.extmath.randomized_range_finder "sklearn.utils.extmath.randomized_range_finder")
     and [`utils.extmath.randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
    .
    
*   Replaced `rho` in [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     and [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     by `l1_ratio`. The `rho` parameter had different meanings; `l1_ratio` was introduced to avoid confusion. It has the same meaning as previously `rho` in [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     and `(1-rho)` in [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    .
    
*   [`linear_model.LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")
     and [`linear_model.Lars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html#sklearn.linear_model.Lars "sklearn.linear_model.Lars")
     now store a list of paths in the case of multiple targets, rather than an array of paths.
    
*   The attribute `gmm` of `hmm.GMMHMM` was renamed to `gmm_` to adhere more strictly with the API.
    
*   `cluster.spectral_embedding` was moved to [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
    .
    
*   Renamed `eig_tol` in [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
    , [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     to `eigen_tol`, renamed `mode` to `eigen_solver`.
    
*   Renamed `mode` in [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
     and [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     to `eigen_solver`.
    
*   `classes_` and `n_classes_` attributes of [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
     and all derived ensemble models are now flat in case of single output problems and nested in case of multi-output problems.
    
*   The `estimators_` attribute of [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     and [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     is now an array of [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    .
    
*   Renamed `chunk_size` to `batch_size` in [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
     and [`decomposition.MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")
     for consistency.
    
*   [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     and [`svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
     now provide a `classes_` attribute and support arbitrary dtypes for labels `y`. Also, the dtype returned by `predict` now reflects the dtype of `y` during `fit` (used to be `np.float`).
    
*   Changed default test\_size in `cross_validation.train_test_split` to None, added possibility to infer `test_size` from `train_size` in `cross_validation.ShuffleSplit` and `cross_validation.StratifiedShuffleSplit`.
    
*   Renamed function `sklearn.metrics.zero_one` to `sklearn.metrics.zero_one_loss`. Be aware that the default behavior in `sklearn.metrics.zero_one_loss` is different from `sklearn.metrics.zero_one`: `normalize=False` is changed to `normalize=True`.
    
*   Renamed function `metrics.zero_one_score` to [`metrics.accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
    .
    
*   [`datasets.make_circles`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
     now has the same number of inner and outer points.
    
*   In the Naive Bayes classifiers, the `class_prior` parameter was moved from `fit` to `__init__`.
    

### People[#](https://scikit-learn.org/stable/whats_new/v0.13.html#id3 "Link to this heading")

List of contributors for release 0.13 by number of commits.

*   364 [Andreas Müller](https://amueller.github.io/)
    
*   143 [Arnaud Joly](http://www.ajoly.org/)
    
*   137 [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    
*   131 [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   117 [Mathieu Blondel](http://www.mblondel.org/)
    
*   108 [Lars Buitinck](https://github.com/larsmans)
    
*   106 Wei Li
    
*   101 [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    
*   65 [Vlad Niculae](https://vene.ro/)
    
*   54 [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    
*   40 [Jaques Grobler](https://github.com/jaquesgrobler)
    
*   38 [Alexandre Gramfort](https://alexandre.gramfort.net/)
    
*   30 [Rob Zinkov](https://www.zinkov.com/)
    
*   19 Aymeric Masurelle
    
*   18 Andrew Winterman
    
*   17 [Fabian Pedregosa](https://fa.bianp.net/)
    
*   17 Nelle Varoquaux
    
*   16 [Christian Osendorfer](https://osdf.github.io/)
    
*   14 [Daniel Nouri](https://danielnouri.org/)
    
*   13 [Virgile Fritsch](https://github.com/VirgileFritsch)
    
*   13 syhw
    
*   12 [Satrajit Ghosh](https://www.mit.edu/~satra/)
    
*   10 Corey Lynch
    
*   10 Kyle Beauchamp
    
*   9 Brian Cheung
    
*   9 Immanuel Bayer
    
*   9 mr.Shu
    
*   8 Conrad Lee
    
*   8 [James Bergstra](http://www-etud.iro.umontreal.ca/~bergstrj/)
    
*   7 Tadej Janež
    
*   6 Brian Cajes
    
*   6 [Jake Vanderplas](https://staff.washington.edu/jakevdp/)
    
*   6 Michael
    
*   6 Noel Dawe
    
*   6 Tiago Nunes
    
*   6 cow
    
*   5 Anze
    
*   5 Shiqiao Du
    
*   4 Christian Jauvin
    
*   4 Jacques Kvam
    
*   4 Richard T. Guy
    
*   4 [Robert Layton](https://twitter.com/robertlayton)
    
*   3 Alexandre Abraham
    
*   3 Doug Coleman
    
*   3 Scott Dickerson
    
*   2 ApproximateIdentity
    
*   2 John Benediktsson
    
*   2 Mark Veronda
    
*   2 Matti Lyra
    
*   2 Mikhail Korobov
    
*   2 Xinfan Meng
    
*   1 Alejandro Weinstein
    
*   1 [Alexandre Passos](https://atpassos.me/)
    
*   1 Christoph Deil
    
*   1 Eugene Nizhibitsky
    
*   1 Kenneth C. Arnold
    
*   1 Luis Pedro Coelho
    
*   1 Miroslav Batchkarov
    
*   1 Pavel
    
*   1 Sebastian Berg
    
*   1 Shaun Jackman
    
*   1 Subhodeep Moitra
    
*   1 bob
    
*   1 dengemann
    
*   1 emanuele
    
*   1 x006
    

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)