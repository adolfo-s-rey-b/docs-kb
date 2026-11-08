[Skip to main content](https://scikit-learn.org/stable/whats_new/v0.15.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v0.15.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v0.15.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v0.15.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v0.15.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v0.15.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v0.15.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v0.15.html)

Collapse Sidebar Expand Sidebar

Version 0.15[#](https://scikit-learn.org/stable/whats_new/v0.15.html#version-0-15 "Link to this heading")

==========================================================================================================

Version 0.15.2[#](https://scikit-learn.org/stable/whats_new/v0.15.html#version-0-15-2 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**September 4, 2014**

### Bug fixes[#](https://scikit-learn.org/stable/whats_new/v0.15.html#bug-fixes "Link to this heading")

*   Fixed handling of the `p` parameter of the Minkowski distance that was previously ignored in nearest neighbors models. By [Nikolay Mayorov](https://github.com/nmayorov)
    .
    
*   Fixed duplicated alphas in [`linear_model.LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")
     with early stopping on 32 bit Python. By [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
     and [Fabian Pedregosa](https://fa.bianp.net/)
    .
    
*   Fixed the build under Windows when scikit-learn is built with MSVC while NumPy is built with MinGW. By [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
     and [Federico Vaggi](https://github.com/FedericoV)
    .
    
*   Fixed an array index overflow bug in the coordinate descent solver. By [Gael Varoquaux](https://gael-varoquaux.info/)
    .
    
*   Better handling of numpy 1.9 deprecation warnings. By [Gael Varoquaux](https://gael-varoquaux.info/)
    .
    
*   Removed unnecessary data copy in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    . By [Gael Varoquaux](https://gael-varoquaux.info/)
    .
    
*   Explicitly close open files to avoid `ResourceWarnings` under Python 3. By Calvin Giles.
    
*   The `transform` of [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     now projects the input on the most discriminant directions. By Martin Billinger.
    
*   Fixed potential overflow in `_tree.safe_realloc` by [Lars Buitinck](https://github.com/larsmans)
    .
    
*   Performance optimization in [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
    . By Robert Bradshaw.
    
*   `nose` is no longer a runtime dependency to import `sklearn`, only for running the tests. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   Many documentation and website fixes by [Joel Nothman](https://joelnothman.com/)
    , [Lars Buitinck](https://github.com/larsmans)
     [Matt Pico](https://github.com/MattpSoftware)
    , and others.
    

Version 0.15.1[#](https://scikit-learn.org/stable/whats_new/v0.15.html#version-0-15-1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**August 1, 2014**

### Bug fixes[#](https://scikit-learn.org/stable/whats_new/v0.15.html#id1 "Link to this heading")

*   Made `cross_validation.cross_val_score` use `cross_validation.KFold` instead of `cross_validation.StratifiedKFold` on multi-output classification problems. By [Nikolay Mayorov](https://github.com/nmayorov)
    .
    
*   Support unseen labels [`preprocessing.LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
     to restore the default behavior of 0.14.1 for backward compatibility. By [Hamzeh Alsalhi](https://github.com/hamsal)
    .
    
*   Fixed the [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     stopping criterion that prevented early convergence detection. By Edward Raff and [Gael Varoquaux](https://gael-varoquaux.info/)
    .
    
*   Fixed the behavior of [`multiclass.OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
    . in case of ties at the per-class vote level by computing the correct per-class sum of prediction scores. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   Made `cross_validation.cross_val_score` and `grid_search.GridSearchCV` accept Python lists as input data. This is especially useful for cross-validation and model selection of text processing pipelines. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   Fixed data input checks of most estimators to accept input data that implements the NumPy `__array__` protocol. This is the case for for `pandas.Series` and `pandas.DataFrame` in recent versions of pandas. By [Gael Varoquaux](https://gael-varoquaux.info/)
    .
    
*   Fixed a regression for [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     with `class_weight="auto"` on data with non-contiguous labels. By [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    

Version 0.15[#](https://scikit-learn.org/stable/whats_new/v0.15.html#changes-0-15 "Link to this heading")

----------------------------------------------------------------------------------------------------------

**July 15, 2014**

### Highlights[#](https://scikit-learn.org/stable/whats_new/v0.15.html#highlights "Link to this heading")

*   Many speed and memory improvements all across the code
    
*   Huge speed and memory improvements to random forests (and extra trees) that also benefit better from parallel computing.
    
*   Incremental fit to [`BernoulliRBM`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM "sklearn.neural_network.BernoulliRBM")
    
*   Added [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     for hierarchical agglomerative clustering with average linkage, complete linkage and ward strategies.
    
*   Added [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
     for robust regression models.
    
*   Added dimensionality reduction with [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     which can be used to visualize high-dimensional data.
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.15.html#changelog "Link to this heading")

#### New features[#](https://scikit-learn.org/stable/whats_new/v0.15.html#new-features "Link to this heading")

*   Added [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
     and [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
     meta-estimators for ensembling any kind of base estimator. See the [Bagging](https://scikit-learn.org/stable/modules/ensemble.html#bagging)
     section of the user guide for details and examples. By [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   New unsupervised feature selection algorithm [`feature_selection.VarianceThreshold`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html#sklearn.feature_selection.VarianceThreshold "sklearn.feature_selection.VarianceThreshold")
    , by [Lars Buitinck](https://github.com/larsmans)
    .
    
*   Added [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
     meta-estimator for the robust fitting of regression models. By [Johannes Schönberger](https://github.com/ahojnnes)
    .
    
*   Added [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     for hierarchical agglomerative clustering with average linkage, complete linkage and ward strategies, by [Nelle Varoquaux](https://github.com/nellev)
     and [Gael Varoquaux](https://gael-varoquaux.info/)
    .
    
*   Shorthand constructors [`pipeline.make_pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
     and [`pipeline.make_union`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_union.html#sklearn.pipeline.make_union "sklearn.pipeline.make_union")
     were added by [Lars Buitinck](https://github.com/larsmans)
    .
    
*   Shuffle option for `cross_validation.StratifiedKFold`. By [Jeffrey Blackburne](https://github.com/jblackburne)
    .
    
*   Incremental learning (`partial_fit`) for Gaussian Naive Bayes by Imran Haque.
    
*   Added `partial_fit` to [`BernoulliRBM`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM "sklearn.neural_network.BernoulliRBM")
     By [Danny Sullivan](https://github.com/dsullivan7)
    .
    
*   Added `learning_curve` utility to chart performance with respect to training size. See [Plotting Learning Curves and Checking Models’ Scalability](https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html#sphx-glr-auto-examples-model-selection-plot-learning-curve-py)
    . By Alexander Fabisch.
    
*   Add positive option in [`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
     and [`ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    . By Brian Wignall and [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   Added [`linear_model.MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")
     and [`linear_model.MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")
    . By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Added [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
    . By Alexander Fabisch.
    

#### Enhancements[#](https://scikit-learn.org/stable/whats_new/v0.15.html#enhancements "Link to this heading")

*   Add sparse input support to [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
     and [`ensemble.AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
     meta-estimators. By [Hamzeh Alsalhi](https://github.com/hamsal)
    .
    
*   Memory improvements of decision trees, by [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Decision trees can now be built in best-first manner by using `max_leaf_nodes` as the stopping criteria. Refactored the tree code to use either a stack or a priority queue for tree building. By [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
     and [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   Decision trees can now be fitted on fortran- and c-style arrays, and non-continuous arrays without the need to make a copy. If the input array has a different dtype than `np.float32`, a fortran-style copy will be made since fortran-style memory layout has speed advantages. By [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
     and [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   Speed improvement of regression trees by optimizing the the computation of the mean square error criterion. This lead to speed improvement of the tree, forest and gradient boosting tree modules. By [Arnaud Joly](http://www.ajoly.org/)
    
*   The `img_to_graph` and `grid_tograph` functions in [`sklearn.feature_extraction.image`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction.image "sklearn.feature_extraction.image")
     now return `np.ndarray` instead of `np.matrix` when `return_as=np.ndarray`. See the Notes section for more information on compatibility.
    
*   Changed the internal storage of decision trees to use a struct array. This fixed some small bugs, while improving code and providing a small speed gain. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   Reduce memory usage and overhead when fitting and predicting with forests of randomized trees in parallel with `n_jobs != 1` by leveraging new threading backend of joblib 0.8 and releasing the GIL in the tree fitting Cython code. By [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
     and [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   Speed improvement of the `sklearn.ensemble.gradient_boosting` module. By [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
     and [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    .
    
*   Various enhancements to the `sklearn.ensemble.gradient_boosting` module: a `warm_start` argument to fit additional trees, a `max_leaf_nodes` argument to fit GBM style trees, a `monitor` fit argument to inspect the estimator during training, and refactoring of the verbose code. By [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    .
    
*   Faster `sklearn.ensemble.ExtraTrees` by caching feature values. By [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Faster depth-based tree building algorithm such as decision tree, random forest, extra trees or gradient tree boosting (with depth based growing strategy) by avoiding trying to split on found constant features in the sample subset. By [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Add `min_weight_fraction_leaf` pre-pruning parameter to tree-based methods: the minimum weighted fraction of the input samples required to be at a leaf node. By [Noel Dawe](https://github.com/ndawe)
    .
    
*   Added [`metrics.pairwise_distances_argmin_min`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html#sklearn.metrics.pairwise_distances_argmin_min "sklearn.metrics.pairwise_distances_argmin_min")
    , by Philippe Gervais.
    
*   Added predict method to [`cluster.AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
     and [`cluster.MeanShift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")
    , by [Mathieu Blondel](http://www.mblondel.org/)
    .
    
*   Vector and matrix multiplications have been optimised throughout the library by [Denis Engemann](https://denis-engemann.de/)
    , and [Alexandre Gramfort](https://alexandre.gramfort.net/)
    . In particular, they should take less memory with older NumPy versions (prior to 1.7.2).
    
*   Precision-recall and ROC examples now use train\_test\_split, and have more explanation of why these metrics are useful. By [Kyle Kastner](https://kastnerkyle.github.io/)
    
*   The training algorithm for [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     is faster for sparse matrices and has much lower memory complexity, meaning it will scale up gracefully to large datasets. By [Lars Buitinck](https://github.com/larsmans)
    .
    
*   Added svd\_method option with default value to “randomized” to [`decomposition.FactorAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")
     to save memory and significantly speedup computation by [Denis Engemann](https://denis-engemann.de/)
    , and [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   Changed `cross_validation.StratifiedKFold` to try and preserve as much of the original ordering of samples as possible so as not to hide overfitting on datasets with a non-negligible level of samples dependency. By [Daniel Nouri](https://danielnouri.org/)
     and [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Add multi-output support to [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
     by John Novak.
    
*   Support for precomputed distance matrices in nearest neighbor estimators by [Robert Layton](https://twitter.com/robertlayton)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   Norm computations optimized for NumPy 1.6 and later versions by [Lars Buitinck](https://github.com/larsmans)
    . In particular, the k-means algorithm no longer needs a temporary data structure the size of its input.
    
*   [`dummy.DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
     can now be used to predict a constant output value. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
     has now a strategy parameter which allows to predict the mean, the median of the training set or a constant output value. By [Maheshakya Wijewardena](https://github.com/maheshakya)
    .
    
*   Multi-label classification output in multilabel indicator format is now supported by [`metrics.roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
     and [`metrics.average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
     by [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Significant performance improvements (more than 100x speedup for large problems) in [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
     by [Andrew Tulloch](https://tullo.ch/)
    .
    
*   Speed and memory usage improvements to the SGD algorithm for linear models: it now uses threads, not separate processes, when `n_jobs>1`. By [Lars Buitinck](https://github.com/larsmans)
    .
    
*   Grid search and cross validation allow NaNs in the input arrays so that preprocessors such as `preprocessing.Imputer` can be trained within the cross validation loop, avoiding potentially skewed results.
    
*   Ridge regression can now deal with sample weights in feature space (only sample space until then). By [Michael Eickenberg](https://github.com/eickenberg)
    . Both solutions are provided by the Cholesky solver.
    
*   Several classification and regression metrics now support weighted samples with the new `sample_weight` argument: [`metrics.accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
    , [`metrics.zero_one_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "sklearn.metrics.zero_one_loss")
    , [`metrics.precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")
    , [`metrics.average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
    , [`metrics.f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")
    , [`metrics.fbeta_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#sklearn.metrics.fbeta_score "sklearn.metrics.fbeta_score")
    , [`metrics.recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")
    , [`metrics.roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
    , [`metrics.explained_variance_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score "sklearn.metrics.explained_variance_score")
    , [`metrics.mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
    , [`metrics.mean_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
    , [`metrics.r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
    . By [Noel Dawe](https://github.com/ndawe)
    .
    
*   Speed up of the sample generator [`datasets.make_multilabel_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "sklearn.datasets.make_multilabel_classification")
    . By [Joel Nothman](https://joelnothman.com/)
    .
    

#### Documentation improvements[#](https://scikit-learn.org/stable/whats_new/v0.15.html#documentation-improvements "Link to this heading")

*   The Working With Text Data tutorial has now been worked in to the main documentation’s tutorial section. Includes exercises and skeletons for tutorial presentation. Original tutorial created by several authors including [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    , Lars Buitinck and many others. Tutorial integration into the scikit-learn documentation by [Jaques Grobler](https://github.com/jaquesgrobler)
    
*   Added [Computational Performance](https://scikit-learn.org/stable/computing/computational_performance.html#computational-performance)
     documentation. Discussion and examples of prediction latency / throughput and different factors that have influence over speed. Additional tips for building faster models and choosing a relevant compromise between speed and predictive power. By [Eustache Diemert](https://github.com/oddskool)
    .
    

#### Bug fixes[#](https://scikit-learn.org/stable/whats_new/v0.15.html#id3 "Link to this heading")

*   Fixed bug in [`decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
     : `partial_fit` was not working properly.
    
*   Fixed bug in `linear_model.stochastic_gradient` : `l1_ratio` was used as `(1.0 - l1_ratio)` .
    
*   Fixed bug in [`multiclass.OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
     with string labels.
    
*   Fixed a bug in [`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
     and [`ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    : they would not pre-compute the Gram matrix with `precompute=True` or `precompute="auto"` and `n_samples > n_features`. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Fixed incorrect estimation of the degrees of freedom in [`feature_selection.f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")
     when variates are not centered. By [Virgile Fritsch](https://github.com/VirgileFritsch)
    .
    
*   Fixed a race condition in parallel processing with `pre_dispatch != "all"` (for instance, in `cross_val_score`). By [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Raise error in [`cluster.FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")
     and `cluster.WardAgglomeration` when no samples are given, rather than returning meaningless clustering.
    
*   Fixed bug in `gradient_boosting.GradientBoostingRegressor` with `loss='huber'`: `gamma` might have not been initialized.
    
*   Fixed feature importances as computed with a forest of randomized trees when fit with `sample_weight != None` and/or with `bootstrap=True`. By [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    

### API changes summary[#](https://scikit-learn.org/stable/whats_new/v0.15.html#api-changes-summary "Link to this heading")

*   `sklearn.hmm` is deprecated. Its removal is planned for the 0.17 release.
    
*   Use of `covariance.EllipticEnvelop` has now been removed after deprecation. Please use [`covariance.EllipticEnvelope`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")
     instead.
    
*   `cluster.Ward` is deprecated. Use [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     instead.
    
*   `cluster.WardClustering` is deprecated. Use
    
*   [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     instead.
    
*   `cross_validation.Bootstrap` is deprecated. `cross_validation.KFold` or `cross_validation.ShuffleSplit` are recommended instead.
    
*   Direct support for the sequence of sequences (or list of lists) multilabel format is deprecated. To convert to and from the supported binary indicator matrix format, use [`preprocessing.MultiLabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer "sklearn.preprocessing.MultiLabelBinarizer")
    . By [Joel Nothman](https://joelnothman.com/)
    .
    
*   Add score method to [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     following the model of probabilistic PCA and deprecate `ProbabilisticPCA` model whose score implementation is not correct. The computation now also exploits the matrix inversion lemma for faster computation. By [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   The score method of [`decomposition.FactorAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")
     now returns the average log-likelihood of the samples. Use score\_samples to get log-likelihood of each sample. By [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   Generating boolean masks (the setting `indices=False`) from cross-validation generators is deprecated. Support for masks will be removed in 0.17. The generators have produced arrays of indices by default since 0.10. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   1-d arrays containing strings with `dtype=object` (as used in Pandas) are now considered valid classification targets. This fixes a regression from version 0.13 in some classifiers. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   Fix wrong `explained_variance_ratio_` attribute in `RandomizedPCA`. By [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   Fit alphas for each `l1_ratio` instead of `mean_l1_ratio` in [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
     and [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
    . This changes the shape of `alphas_` from `(n_alphas,)` to `(n_l1_ratio, n_alphas)` if the `l1_ratio` provided is a 1-D array like object of length greater than one. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Fix [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
     and [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
     when fitting intercept and input data is sparse. The automatic grid of alphas was not computed correctly and the scaling with normalize was wrong. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Fix wrong maximal number of features drawn (`max_features`) at each split for decision trees, random forests and gradient tree boosting. Previously, the count for the number of drawn features started only after one non constant features in the split. This bug fix will affect computational and generalization performance of those algorithms in the presence of constant features. To get back previous generalization performance, you should modify the value of `max_features`. By [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Fix wrong maximal number of features drawn (`max_features`) at each split for [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
     and [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
    . Previously, only non constant features in the split was counted as drawn. Now constant features are counted as drawn. Furthermore at least one feature must be non constant in order to make a valid split. This bug fix will affect computational and generalization performance of extra trees in the presence of constant features. To get back previous generalization performance, you should modify the value of `max_features`. By [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Fix [`utils.class_weight.compute_class_weight`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html#sklearn.utils.class_weight.compute_class_weight "sklearn.utils.class_weight.compute_class_weight")
     when `class_weight=="auto"`. Previously it was broken for input of non-integer `dtype` and the weighted array that was returned was wrong. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Fix `cross_validation.Bootstrap` to return `ValueError` when `n_train + n_test > n`. By [Ronald Phlypo](https://github.com/rphlypo)
    .
    

### People[#](https://scikit-learn.org/stable/whats_new/v0.15.html#people "Link to this heading")

List of contributors for release 0.15 by number of commits.

*   312 Olivier Grisel
    
*   275 Lars Buitinck
    
*   221 Gael Varoquaux
    
*   148 Arnaud Joly
    
*   134 Johannes Schönberger
    
*   119 Gilles Louppe
    
*   113 Joel Nothman
    
*   111 Alexandre Gramfort
    
*   95 Jaques Grobler
    
*   89 Denis Engemann
    
*   83 Peter Prettenhofer
    
*   83 Alexander Fabisch
    
*   62 Mathieu Blondel
    
*   60 Eustache Diemert
    
*   60 Nelle Varoquaux
    
*   49 Michael Bommarito
    
*   45 Manoj-Kumar-S
    
*   28 Kyle Kastner
    
*   26 Andreas Mueller
    
*   22 Noel Dawe
    
*   21 Maheshakya Wijewardena
    
*   21 Brooke Osborn
    
*   21 Hamzeh Alsalhi
    
*   21 Jake VanderPlas
    
*   21 Philippe Gervais
    
*   19 Bala Subrahmanyam Varanasi
    
*   12 Ronald Phlypo
    
*   10 Mikhail Korobov
    
*   8 Thomas Unterthiner
    
*   8 Jeffrey Blackburne
    
*   8 eltermann
    
*   8 bwignall
    
*   7 Ankit Agrawal
    
*   7 CJ Carey
    
*   6 Daniel Nouri
    
*   6 Chen Liu
    
*   6 Michael Eickenberg
    
*   6 ugurthemaster
    
*   5 Aaron Schumacher
    
*   5 Baptiste Lagarde
    
*   5 Rajat Khanduja
    
*   5 Robert McGibbon
    
*   5 Sergio Pascual
    
*   4 Alexis Metaireau
    
*   4 Ignacio Rossi
    
*   4 Virgile Fritsch
    
*   4 Sebastian Säger
    
*   4 Ilambharathi Kanniah
    
*   4 sdenton4
    
*   4 Robert Layton
    
*   4 Alyssa
    
*   4 Amos Waterland
    
*   3 Andrew Tulloch
    
*   3 murad
    
*   3 Steven Maude
    
*   3 Karol Pysniak
    
*   3 Jacques Kvam
    
*   3 cgohlke
    
*   3 cjlin
    
*   3 Michael Becker
    
*   3 hamzeh
    
*   3 Eric Jacobsen
    
*   3 john collins
    
*   3 kaushik94
    
*   3 Erwin Marsi
    
*   2 csytracy
    
*   2 LK
    
*   2 Vlad Niculae
    
*   2 Laurent Direr
    
*   2 Erik Shilts
    
*   2 Raul Garreta
    
*   2 Yoshiki Vázquez Baeza
    
*   2 Yung Siang Liau
    
*   2 abhishek thakur
    
*   2 James Yu
    
*   2 Rohit Sivaprasad
    
*   2 Roland Szabo
    
*   2 amormachine
    
*   2 Alexis Mignon
    
*   2 Oscar Carlsson
    
*   2 Nantas Nardelli
    
*   2 jess010
    
*   2 kowalski87
    
*   2 Andrew Clegg
    
*   2 Federico Vaggi
    
*   2 Simon Frid
    
*   2 Félix-Antoine Fortin
    
*   1 Ralf Gommers
    
*   1 t-aft
    
*   1 Ronan Amicel
    
*   1 Rupesh Kumar Srivastava
    
*   1 Ryan Wang
    
*   1 Samuel Charron
    
*   1 Samuel St-Jean
    
*   1 Fabian Pedregosa
    
*   1 Skipper Seabold
    
*   1 Stefan Walk
    
*   1 Stefan van der Walt
    
*   1 Stephan Hoyer
    
*   1 Allen Riddell
    
*   1 Valentin Haenel
    
*   1 Vijay Ramesh
    
*   1 Will Myers
    
*   1 Yaroslav Halchenko
    
*   1 Yoni Ben-Meshulam
    
*   1 Yury V. Zaytsev
    
*   1 adrinjalali
    
*   1 ai8rahim
    
*   1 alemagnani
    
*   1 alex
    
*   1 benjamin wilson
    
*   1 chalmerlowe
    
*   1 dzikie drożdże
    
*   1 jamestwebber
    
*   1 matrixorz
    
*   1 popo
    
*   1 samuela
    
*   1 François Boulogne
    
*   1 Alexander Measure
    
*   1 Ethan White
    
*   1 Guilherme Trein
    
*   1 Hendrik Heuer
    
*   1 IvicaJovic
    
*   1 Jan Hendrik Metzen
    
*   1 Jean Michel Rouly
    
*   1 Eduardo Ariño de la Rubia
    
*   1 Jelle Zijlstra
    
*   1 Eddy L O Jansson
    
*   1 Denis
    
*   1 John
    
*   1 John Schmidt
    
*   1 Jorge Cañardo Alastuey
    
*   1 Joseph Perla
    
*   1 Joshua Vredevoogd
    
*   1 José Ricardo
    
*   1 Julien Miotte
    
*   1 Kemal Eren
    
*   1 Kenta Sato
    
*   1 David Cournapeau
    
*   1 Kyle Kelley
    
*   1 Daniele Medri
    
*   1 Laurent Luce
    
*   1 Laurent Pierron
    
*   1 Luis Pedro Coelho
    
*   1 DanielWeitzenfeld
    
*   1 Craig Thompson
    
*   1 Chyi-Kwei Yau
    
*   1 Matthew Brett
    
*   1 Matthias Feurer
    
*   1 Max Linke
    
*   1 Chris Filo Gorgolewski
    
*   1 Charles Earl
    
*   1 Michael Hanke
    
*   1 Michele Orrù
    
*   1 Bryan Lunt
    
*   1 Brian Kearns
    
*   1 Paul Butler
    
*   1 Paweł Mandera
    
*   1 Peter
    
*   1 Andrew Ash
    
*   1 Pietro Zambelli
    
*   1 staubda
    

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)