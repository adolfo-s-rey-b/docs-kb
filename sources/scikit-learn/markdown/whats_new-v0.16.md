[Skip to main content](https://scikit-learn.org/stable/whats_new/v0.16.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v0.16.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v0.16.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v0.16.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v0.16.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v0.16.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v0.16.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v0.16.html)

Collapse Sidebar Expand Sidebar

Version 0.16[#](https://scikit-learn.org/stable/whats_new/v0.16.html#version-0-16 "Link to this heading")

==========================================================================================================

Version 0.16.1[#](https://scikit-learn.org/stable/whats_new/v0.16.html#version-0-16-1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**April 14, 2015**

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.16.html#changelog "Link to this heading")

#### Bug fixes[#](https://scikit-learn.org/stable/whats_new/v0.16.html#bug-fixes "Link to this heading")

*   Allow input data larger than `block_size` in [`covariance.LedoitWolf`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html#sklearn.covariance.LedoitWolf "sklearn.covariance.LedoitWolf")
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Fix a bug in [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
     deduplication that caused unstable result in [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     by [Jan Hendrik Metzen](https://jmetzen.github.io/)
    .
    
*   Fix sorting of labels in [`preprocessing.label_binarize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html#sklearn.preprocessing.label_binarize "sklearn.preprocessing.label_binarize")
     by Michael Heilman.
    
*   Fix several stability and convergence issues in [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
     and [`cross_decomposition.PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
     by [Andreas Müller](https://amueller.github.io/)
    
*   Fix a bug in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     when `precompute_distances=False` on fortran-ordered data.
    
*   Fix a speed regression in [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    ’s `predict` and `predict_proba` by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Fix a regression where `utils.shuffle` converted lists and dataframes to arrays, by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    

Version 0.16[#](https://scikit-learn.org/stable/whats_new/v0.16.html#changes-0-16 "Link to this heading")

----------------------------------------------------------------------------------------------------------

**March 26, 2015**

### Highlights[#](https://scikit-learn.org/stable/whats_new/v0.16.html#highlights "Link to this heading")

*   Speed improvements (notably in [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
    ), reduced memory requirements, bug-fixes and better default settings.
    
*   Multinomial Logistic regression and a path algorithm in [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
    .
    
*   Out-of core learning of PCA via [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
    .
    
*   Probability calibration of classifiers using [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
    .
    
*   [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
     clustering method for large-scale datasets.
    
*   Scalable approximate nearest neighbors search with Locality-sensitive hashing forests in `neighbors.LSHForest`.
    
*   Improved error messages and better validation when using malformed input data.
    
*   More robust integration with pandas dataframes.
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.16.html#id2 "Link to this heading")

#### New features[#](https://scikit-learn.org/stable/whats_new/v0.16.html#new-features "Link to this heading")

*   The new `neighbors.LSHForest` implements locality-sensitive hashing for approximate nearest neighbors search. By [Maheshakya Wijewardena](https://github.com/maheshakya)
    .
    
*   Added [`svm.LinearSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR "sklearn.svm.LinearSVR")
    . This class uses the liblinear implementation of Support Vector Regression which is much faster for large sample sizes than [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
     with linear kernel. By [Fabian Pedregosa](https://fa.bianp.net/)
     and Qiang Luo.
    
*   Incremental fit for [`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
    .
    
*   Added `sample_weight` support to [`dummy.DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
     and [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
    . By [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Added the [`metrics.label_ranking_average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html#sklearn.metrics.label_ranking_average_precision_score "sklearn.metrics.label_ranking_average_precision_score")
     metrics. By [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Add the [`metrics.coverage_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.coverage_error.html#sklearn.metrics.coverage_error "sklearn.metrics.coverage_error")
     metrics. By [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Added [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
    . By [Manoj Kumar](https://manojbits.wordpress.com/)
    , [Fabian Pedregosa](https://fa.bianp.net/)
    , [Gael Varoquaux](https://gael-varoquaux.info/)
     and [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   Added `warm_start` constructor parameter to make it possible for any trained forest model to grow additional trees incrementally. By [Laurent Direr](https://github.com/ldirer)
    .
    
*   Added `sample_weight` support to [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
    . By [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    .
    
*   Added [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
    , an implementation of the PCA algorithm that supports out-of-core learning with a `partial_fit` method. By [Kyle Kastner](https://kastnerkyle.github.io/)
    .
    
*   Averaged SGD for [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     and [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     By [Danny Sullivan](https://github.com/dsullivan7)
    .
    
*   Added `cross_val_predict` function which computes cross-validated estimates. By [Luis Pedro Coelho](https://luispedro.org/)
    
*   Added [`linear_model.TheilSenRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "sklearn.linear_model.TheilSenRegressor")
    , a robust generalized-median-based estimator. By [Florian Wilhelm](https://github.com/FlorianWilhelm)
    .
    
*   Added [`metrics.median_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")
    , a robust metric. By [Gael Varoquaux](https://gael-varoquaux.info/)
     and [Florian Wilhelm](https://github.com/FlorianWilhelm)
    .
    
*   Add [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
    , an online clustering algorithm. By [Manoj Kumar](https://manojbits.wordpress.com/)
    , [Alexandre Gramfort](https://alexandre.gramfort.net/)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   Added shrinkage support to [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     using two new solvers. By [Clemens Brunner](https://github.com/cle1109)
     and [Martin Billinger](https://tnsre.embs.org/author/martinbillinger/)
    .
    
*   Added [`kernel_ridge.KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
    , an implementation of kernelized ridge regression. By [Mathieu Blondel](http://www.mblondel.org/)
     and [Jan Hendrik Metzen](https://jmetzen.github.io/)
    .
    
*   All solvers in [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     now support `sample_weight`. By [Mathieu Blondel](http://www.mblondel.org/)
    .
    
*   Added `cross_validation.PredefinedSplit` cross-validation for fixed user-provided cross-validation folds. By [Thomas Unterthiner](https://github.com/untom)
    .
    
*   Added [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
    , an approach for calibrating the predicted probabilities of a classifier. By [Alexandre Gramfort](https://alexandre.gramfort.net/)
    , [Jan Hendrik Metzen](https://jmetzen.github.io/)
    , [Mathieu Blondel](http://www.mblondel.org/)
     and [Balazs Kegl](https://github.com/kegl)
    .
    

#### Enhancements[#](https://scikit-learn.org/stable/whats_new/v0.16.html#enhancements "Link to this heading")

*   Add option `return_distance` in `hierarchical.ward_tree` to return distances between nodes for both structured and unstructured versions of the algorithm. By [Matteo Visconti di Oleggio Castello](http://www.mvdoc.me/)
    . The same option was added in `hierarchical.linkage_tree`. By [Manoj Kumar](https://manojbits.wordpress.com/)
    
*   Add support for sample weights in scorer objects. Metrics with sample weight support will automatically benefit from it. By [Noel Dawe](https://github.com/ndawe)
     and [Vlad Niculae](https://vene.ro/)
    .
    
*   Added `newton-cg` and `lbfgs` solver support in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    . By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Add `selection="random"` parameter to implement stochastic coordinate descent for [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
    , [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     and related. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Add `sample_weight` parameter to `metrics.jaccard_similarity_score` and [`metrics.log_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
    . By [Jatin Shah](https://github.com/jatinshah)
    .
    
*   Support sparse multilabel indicator representation in [`preprocessing.LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
     and [`multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
     (by [Hamzeh Alsalhi](https://github.com/hamsal)
     with thanks to Rohit Sivaprasad), as well as evaluation metrics (by [Joel Nothman](https://joelnothman.com/)
    ).
    
*   Add `sample_weight` parameter to `metrics.jaccard_similarity_score`. By `Jatin Shah`.
    
*   Add support for multiclass in `metrics.hinge_loss`. Added `labels=None` as optional parameter. By `Saurabh Jha`.
    
*   Add `sample_weight` parameter to `metrics.hinge_loss`. By `Saurabh Jha`.
    
*   Add `multi_class="multinomial"` option in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     to implement a Logistic Regression solver that minimizes the cross-entropy or multinomial loss instead of the default One-vs-Rest setting. Supports `lbfgs` and `newton-cg` solvers. By [Lars Buitinck](https://github.com/larsmans)
     and [Manoj Kumar](https://manojbits.wordpress.com/)
    . Solver option `newton-cg` by Simon Wu.
    
*   `DictVectorizer` can now perform `fit_transform` on an iterable in a single pass, when giving the option `sort=False`. By [Dan Blanchard](https://github.com/dan-blanchard)
    .
    
*   [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     can now be configured to work with estimators that may fail and raise errors on individual folds. This option is controlled by the `error_score` parameter. This does not affect errors raised on re-fit. By [Michal Romaniuk](https://github.com/romaniukm)
    .
    
*   Add `digits` parameter to `metrics.classification_report` to allow report to show different precision of floating point numbers. By [Ian Gilmore](https://github.com/agileminor)
    .
    
*   Add a quantile prediction strategy to the [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
    . By [Aaron Staple](https://github.com/staple)
    .
    
*   Add `handle_unknown` option to [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     to handle unknown categorical features more gracefully during transform. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Added support for sparse input data to decision trees and their ensembles. By [Fares Hedyati](https://www.eecs.berkeley.edu/~fareshed)
     and [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Optimized [`cluster.AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
     by reducing the number of memory allocations of large temporary data-structures. By [Antony Lee](https://www.ocf.berkeley.edu/~antonyl/)
    .
    
*   Parallelization of the computation of feature importances in random forest. By [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
     and [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Add `n_iter_` attribute to estimators that accept a `max_iter` attribute in their constructor. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Added decision function for [`multiclass.OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
     By [Raghav RV](https://github.com/raghavrv)
     and [Kyle Beauchamp](https://github.com/kyleabeauchamp)
    .
    
*   `neighbors.kneighbors_graph` and `radius_neighbors_graph` support non-Euclidean metrics. By [Manoj Kumar](https://manojbits.wordpress.com/)
    
*   Parameter `connectivity` in [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     and family now accept callables that return a connectivity matrix. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Sparse support for [`metrics.pairwise.paired_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_distances.html#sklearn.metrics.pairwise.paired_distances "sklearn.metrics.pairwise.paired_distances")
    . By [Joel Nothman](https://joelnothman.com/)
    .
    
*   [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
     now supports sparse input and sample weights and has been optimized: the inner loop has been rewritten in Cython and radius neighbors queries are now computed in batch. By [Joel Nothman](https://joelnothman.com/)
     and [Lars Buitinck](https://github.com/larsmans)
    .
    
*   Add `class_weight` parameter to automatically weight samples by class frequency for [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
     and [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
    . By [Trevor Stephens](https://trevorstephens.com/)
    .
    
*   `grid_search.RandomizedSearchCV` now does sampling without replacement if all parameters are given as lists. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   Parallelized calculation of [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     is now supported for scipy metrics and custom callables. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   Allow the fitting and scoring of all clustering algorithms in [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
    . By [Andreas Müller](https://amueller.github.io/)
    .
    
*   More robust seeding and improved error messages in [`cluster.MeanShift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Make the stopping criterion for `mixture.GMM`, `mixture.DPGMM` and `mixture.VBGMM` less dependent on the number of samples by thresholding the average log-likelihood change instead of its sum over all samples. By [Hervé Bredin](https://herve.niderb.fr/)
    .
    
*   The outcome of [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
     was made deterministic by flipping the sign of eigenvectors. By [Hasil Sharma](https://github.com/Hasil-Sharma)
    .
    
*   Significant performance and memory usage improvements in [`preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
    . By [Eric Martin](http://www.ericmart.in/)
    .
    
*   Numerical stability improvements for [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
     and [`preprocessing.scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html#sklearn.preprocessing.scale "sklearn.preprocessing.scale")
    . By [Nicolas Goix](https://ngoix.github.io/)
    
*   [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     fitted on sparse input now implements `decision_function`. By [Rob Zinkov](https://www.zinkov.com/)
     and [Andreas Müller](https://amueller.github.io/)
    .
    
*   `cross_validation.train_test_split` now preserves the input type, instead of converting to numpy arrays.
    

#### Documentation improvements[#](https://scikit-learn.org/stable/whats_new/v0.16.html#documentation-improvements "Link to this heading")

*   Added example of using [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     for heterogeneous input. By [Matt Terry](https://github.com/mrterry)
    
*   Documentation on scorers was improved, to highlight the handling of loss functions. By [Matt Pico](https://github.com/MattpSoftware)
    .
    
*   A discrepancy between liblinear output and scikit-learn’s wrappers is now noted. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Improved documentation generation: examples referring to a class or function are now shown in a gallery on the class/function’s API reference page. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   More explicit documentation of sample generators and of data transformation. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   [`sklearn.neighbors.BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
     and [`sklearn.neighbors.KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
     used to point to empty pages stating that they are aliases of BinaryTree. This has been fixed to show the correct class docs. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Added silhouette plots for analysis of KMeans clustering using [`metrics.silhouette_samples`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html#sklearn.metrics.silhouette_samples "sklearn.metrics.silhouette_samples")
     and [`metrics.silhouette_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")
    . See [Selecting the number of clusters with silhouette analysis on KMeans clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html#sphx-glr-auto-examples-cluster-plot-kmeans-silhouette-analysis-py)
    

#### Bug fixes[#](https://scikit-learn.org/stable/whats_new/v0.16.html#id3 "Link to this heading")

*   Metaestimators now support ducktyping for the presence of `decision_function`, `predict_proba` and other methods. This fixes behavior of `grid_search.GridSearchCV`, `grid_search.RandomizedSearchCV`, [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
    , [`feature_selection.RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
    , [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
     when nested. By [Joel Nothman](https://joelnothman.com/)
    
*   The `scoring` attribute of grid-search and cross-validation methods is no longer ignored when a `grid_search.GridSearchCV` is given as a base estimator or the base estimator doesn’t have predict.
    
*   The function `hierarchical.ward_tree` now returns the children in the same order for both the structured and unstructured versions. By [Matteo Visconti di Oleggio Castello](http://www.mvdoc.me/)
    .
    
*   [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
     now correctly handles cases when `step` is not equal to 1. By [Nikolay Mayorov](https://github.com/nmayorov)
    
*   The [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     now undoes whitening in its `inverse_transform`. Also, its `components_` now always have unit length. By [Michael Eickenberg](https://github.com/eickenberg)
    .
    
*   Fix incomplete download of the dataset when `datasets.download_20newsgroups` is called. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Various fixes to the Gaussian processes subpackage by Vincent Dubourg and Jan Hendrik Metzen.
    
*   Calling `partial_fit` with `class_weight=='auto'` throws an appropriate error message and suggests a workaround. By [Danny Sullivan](https://github.com/dsullivan7)
    .
    
*   [`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
     with `gamma=g` formerly approximated [`rbf_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html#sklearn.metrics.pairwise.rbf_kernel "sklearn.metrics.pairwise.rbf_kernel")
     with `gamma=g/2.`; the definition of `gamma` is now consistent, which may substantially change your results if you use a fixed value. (If you cross-validated over `gamma`, it probably doesn’t matter too much.) By [Dougal Sutherland](https://github.com/dougalsutherland)
    .
    
*   Pipeline object delegates the `classes_` attribute to the underlying estimator. It allows, for instance, to make bagging of a pipeline object. By [Arnaud Joly](http://www.ajoly.org/)
    
*   [`neighbors.NearestCentroid`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")
     now uses the median as the centroid when metric is set to `manhattan`. It was using the mean before. By [Manoj Kumar](https://manojbits.wordpress.com/)
    
*   Fix numerical stability issues in [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     and [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     by clipping large gradients and ensuring that weight decay rescaling is always positive (for large l2 regularization and large learning rate values). By [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    
*   When `compute_full_tree` is set to “auto”, the full tree is built when n\_clusters is high and is early stopped when n\_clusters is low, while the behavior should be vice versa in [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     (and friends). This has been fixed By [Manoj Kumar](https://manojbits.wordpress.com/)
    
*   Fix lazy centering of data in [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
     and [`linear_model.lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")
    . It was centered around one. It has been changed to be centered around the origin. By [Manoj Kumar](https://manojbits.wordpress.com/)
    
*   Fix handling of precomputed affinity matrices in [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     when using connectivity constraints. By [Cathy Deng](https://github.com/cathydeng)
    
*   Correct `partial_fit` handling of `class_prior` for [`sklearn.naive_bayes.MultinomialNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB "sklearn.naive_bayes.MultinomialNB")
     and [`sklearn.naive_bayes.BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
    . By [Trevor Stephens](https://trevorstephens.com/)
    .
    
*   Fixed a crash in [`metrics.precision_recall_fscore_support`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "sklearn.metrics.precision_recall_fscore_support")
     when using unsorted `labels` in the multi-label setting. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   Avoid skipping the first nearest neighbor in the methods `radius_neighbors`, `kneighbors`, `kneighbors_graph` and `radius_neighbors_graph` in [`sklearn.neighbors.NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
     and family, when the query data is not the same as fit data. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Fix log-density calculation in the `mixture.GMM` with tied covariance. By [Will Dawson](http://www.dawsonresearch.com/)
    
*   Fixed a scaling error in [`feature_selection.SelectFdr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFdr.html#sklearn.feature_selection.SelectFdr "sklearn.feature_selection.SelectFdr")
     where a factor `n_features` was missing. By [Andrew Tulloch](https://tullo.ch/)
    
*   Fix zero division in [`neighbors.KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
     and related classes when using distance weighting and having identical data points. By [Garret-R](https://github.com/Garrett-R)
    .
    
*   Fixed round off errors with non positive-definite covariance matrices in GMM. By [Alexis Mignon](https://github.com/AlexisMignon)
    .
    
*   Fixed an error in the computation of conditional probabilities in [`naive_bayes.BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
    . By [Hanna Wallach](https://dirichlet.net/)
    .
    
*   Make the method `radius_neighbors` of [`neighbors.NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
     return the samples lying on the boundary for `algorithm='brute'`. By [Yan Yi](http://seowyanyi.org/)
    .
    
*   Flip sign of `dual_coef_` of [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     to make it consistent with the documentation and `decision_function`. By Artem Sobolev.
    
*   Fixed handling of ties in [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
    . We now use the weighted average of targets (secondary method). By [Andreas Müller](https://amueller.github.io/)
     and [Michael Bommarito](https://bommaritollc.com/)
    .
    

### API changes summary[#](https://scikit-learn.org/stable/whats_new/v0.16.html#api-changes-summary "Link to this heading")

*   `GridSearchCV` and `cross_val_score` and other meta-estimators don’t convert pandas DataFrames into arrays any more, allowing DataFrame specific operations in custom estimators.
    
*   `multiclass.fit_ovr`, `multiclass.predict_ovr`, `predict_proba_ovr`, `multiclass.fit_ovo`, `multiclass.predict_ovo`, `multiclass.fit_ecoc` and `multiclass.predict_ecoc` are deprecated. Use the underlying estimators instead.
    
*   Nearest neighbors estimators used to take arbitrary keyword arguments and pass these to their distance metric. This will no longer be supported in scikit-learn 0.18; use the `metric_params` argument instead.
    
*   `n_jobs` parameter of the fit method shifted to the constructor of the
    
    LinearRegression class.
    
*   The `predict_proba` method of [`multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
     now returns two probabilities per sample in the multiclass case; this is consistent with other estimators and with the method’s documentation, but previous versions accidentally returned only the positive probability. Fixed by Will Lamond and [Lars Buitinck](https://github.com/larsmans)
    .
    
*   Change default value of precompute in [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     and [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     to False. Setting precompute to “auto” was found to be slower when n\_samples > n\_features since the computation of the Gram matrix is computationally expensive and outweighs the benefit of fitting the Gram for just one alpha. `precompute="auto"` is now deprecated and will be removed in 0.18 By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Expose `positive` option in [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
     and [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
     which constrains coefficients to be positive. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Users should now supply an explicit `average` parameter to [`sklearn.metrics.f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")
    , [`sklearn.metrics.fbeta_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#sklearn.metrics.fbeta_score "sklearn.metrics.fbeta_score")
    , [`sklearn.metrics.recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")
     and [`sklearn.metrics.precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")
     when performing multiclass or multilabel (i.e. not binary) classification. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   `scoring` parameter for cross validation now accepts `'f1_micro'`, `'f1_macro'` or `'f1_weighted'`. `'f1'` is now for binary classification only. Similar changes apply to `'precision'` and `'recall'`. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   The `fit_intercept`, `normalize` and `return_models` parameters in [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
     and [`linear_model.lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")
     have been removed. They were deprecated since 0.14
    
*   From now onwards, all estimators will uniformly raise `NotFittedError` when any of the `predict` like methods are called before the model is fit. By [Raghav RV](https://github.com/raghavrv)
    .
    
*   Input data validation was refactored for more consistent input validation. The `check_arrays` function was replaced by `check_array` and `check_X_y`. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   Allow `X=None` in the methods `radius_neighbors`, `kneighbors`, `kneighbors_graph` and `radius_neighbors_graph` in [`sklearn.neighbors.NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
     and family. If set to None, then for every sample this avoids setting the sample itself as the first nearest neighbor. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Add parameter `include_self` in [`neighbors.kneighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html#sklearn.neighbors.kneighbors_graph "sklearn.neighbors.kneighbors_graph")
     and [`neighbors.radius_neighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.radius_neighbors_graph.html#sklearn.neighbors.radius_neighbors_graph "sklearn.neighbors.radius_neighbors_graph")
     which has to be explicitly set by the user. If set to True, then the sample itself is considered as the first nearest neighbor.
    
*   `thresh` parameter is deprecated in favor of new `tol` parameter in `GMM`, `DPGMM` and `VBGMM`. See `Enhancements` section for details. By [Hervé Bredin](https://herve.niderb.fr/)
    .
    
*   Estimators will treat input with dtype object as numeric when possible. By [Andreas Müller](https://amueller.github.io/)
    
*   Estimators now raise `ValueError` consistently when fitted on empty data (less than 1 sample or less than 1 feature for 2D input). By [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   The `shuffle` option of [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    , [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
    , [`linear_model.Perceptron`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron")
    , [`linear_model.PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier")
     and [`linear_model.PassiveAggressiveRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model.PassiveAggressiveRegressor")
     now defaults to `True`.
    
*   [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
     now uses a deterministic initialization. The `random_state` parameter is deprecated. By [Erich Schubert](https://github.com/kno10)
    .
    

### Code Contributors[#](https://scikit-learn.org/stable/whats_new/v0.16.html#code-contributors "Link to this heading")

A. Flaxman, Aaron Schumacher, Aaron Staple, abhishek thakur, Akshay, akshayah3, Aldrian Obaja, Alexander Fabisch, Alexandre Gramfort, Alexis Mignon, Anders Aagaard, Andreas Mueller, Andreas van Cranenburgh, Andrew Tulloch, Andrew Walker, Antony Lee, Arnaud Joly, banilo, Barmaley.exe, Ben Davies, Benedikt Koehler, bhsu, Boris Feld, Borja Ayerdi, Boyuan Deng, Brent Pedersen, Brian Wignall, Brooke Osborn, Calvin Giles, Cathy Deng, Celeo, cgohlke, chebee7i, Christian Stade-Schuldt, Christof Angermueller, Chyi-Kwei Yau, CJ Carey, Clemens Brunner, Daiki Aminaka, Dan Blanchard, danfrankj, Danny Sullivan, David Fletcher, Dmitrijs Milajevs, Dougal J. Sutherland, Erich Schubert, Fabian Pedregosa, Florian Wilhelm, floydsoft, Félix-Antoine Fortin, Gael Varoquaux, Garrett-R, Gilles Louppe, gpassino, gwulfs, Hampus Bengtsson, Hamzeh Alsalhi, Hanna Wallach, Harry Mavroforakis, Hasil Sharma, Helder, Herve Bredin, Hsiang-Fu Yu, Hugues SALAMIN, Ian Gilmore, Ilambharathi Kanniah, Imran Haque, isms, Jake VanderPlas, Jan Dlabal, Jan Hendrik Metzen, Jatin Shah, Javier López Peña, jdcaballero, Jean Kossaifi, Jeff Hammerbacher, Joel Nothman, Jonathan Helmus, Joseph, Kaicheng Zhang, Kevin Markham, Kyle Beauchamp, Kyle Kastner, Lagacherie Matthieu, Lars Buitinck, Laurent Direr, leepei, Loic Esteve, Luis Pedro Coelho, Lukas Michelbacher, maheshakya, Manoj Kumar, Manuel, Mario Michael Krell, Martin, Martin Billinger, Martin Ku, Mateusz Susik, Mathieu Blondel, Matt Pico, Matt Terry, Matteo Visconti dOC, Matti Lyra, Max Linke, Mehdi Cherti, Michael Bommarito, Michael Eickenberg, Michal Romaniuk, MLG, mr.Shu, Nelle Varoquaux, Nicola Montecchio, Nicolas, Nikolay Mayorov, Noel Dawe, Okal Billy, Olivier Grisel, Óscar Nájera, Paolo Puggioni, Peter Prettenhofer, Pratap Vardhan, pvnguyen, queqichao, Rafael Carrascosa, Raghav R V, Rahiel Kasim, Randall Mason, Rob Zinkov, Robert Bradshaw, Saket Choudhary, Sam Nicholls, Samuel Charron, Saurabh Jha, sethdandridge, sinhrks, snuderl, Stefan Otte, Stefan van der Walt, Steve Tjoa, swu, Sylvain Zimmer, tejesh95, terrycojones, Thomas Delteil, Thomas Unterthiner, Tomas Kazmar, trevorstephens, tttthomasssss, Tzu-Ming Kuo, ugurcaliskan, ugurthemaster, Vinayak Mehta, Vincent Dubourg, Vjacheslav Murashkin, Vlad Niculae, wadawson, Wei Xue, Will Lamond, Wu Jiang, x0l, Xinfan Meng, Yan Yi, Yu-Chin

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)