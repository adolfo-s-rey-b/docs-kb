[Skip to main content](https://scikit-learn.org/stable/whats_new/older_versions.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/older_versions.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/older_versions.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/older_versions.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/older_versions.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/older_versions.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/older_versions.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/older_versions.html)

Collapse Sidebar Expand Sidebar

Older Versions[#](https://scikit-learn.org/stable/whats_new/older_versions.html#older-versions "Link to this heading")

=======================================================================================================================

Version 0.12.1[#](https://scikit-learn.org/stable/whats_new/older_versions.html#version-0-12-1 "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

**October 8, 2012**

The 0.12.1 release is a bug-fix release with no additional features, but is instead a set of bug fixes

### Changelog[#](https://scikit-learn.org/stable/whats_new/older_versions.html#changelog "Link to this heading")

*   Improved numerical stability in spectral embedding by [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   Doctest under windows 64bit by [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   Documentation fixes for elastic net by [Andreas Müller](https://amueller.github.io/)
     and [Alexandre Gramfort](https://alexandre.gramfort.net/)
    
*   Proper behavior with fortran-ordered NumPy arrays by [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   Make GridSearchCV work with non-CSR sparse matrix by [Lars Buitinck](https://github.com/larsmans)
    
*   Fix parallel computing in MDS by [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   Fix Unicode support in count vectorizer by [Andreas Müller](https://amueller.github.io/)
    
*   Fix MinCovDet breaking with X.shape = (3, 1) by [Virgile Fritsch](https://github.com/VirgileFritsch)
    
*   Fix clone of SGD objects by [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    
*   Stabilize GMM by [Virgile Fritsch](https://github.com/VirgileFritsch)
    

### People[#](https://scikit-learn.org/stable/whats_new/older_versions.html#people "Link to this heading")

*   14 [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    
*   12 [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   10 [Andreas Müller](https://amueller.github.io/)
    
*   5 [Lars Buitinck](https://github.com/larsmans)
    
*   3 [Virgile Fritsch](https://github.com/VirgileFritsch)
    
*   1 [Alexandre Gramfort](https://alexandre.gramfort.net/)
    
*   1 [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    
*   1 [Mathieu Blondel](http://www.mblondel.org/)
    

Version 0.12[#](https://scikit-learn.org/stable/whats_new/older_versions.html#version-0-12 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

**September 4, 2012**

### Changelog[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id1 "Link to this heading")

*   Various speed improvements of the [decision trees](https://scikit-learn.org/stable/modules/tree.html#tree)
     module, by [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     and [`GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     now support feature subsampling via the `max_features` argument, by [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    .
    
*   Added Huber and Quantile loss functions to [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
    , by [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    .
    
*   [Decision trees](https://scikit-learn.org/stable/modules/tree.html#tree)
     and [forests of randomized trees](https://scikit-learn.org/stable/modules/ensemble.html#forest)
     now support multi-output classification and regression problems, by [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   Added [`LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder")
    , a simple utility class to normalize labels or transform non-numerical labels, by [Mathieu Blondel](http://www.mblondel.org/)
    .
    
*   Added the epsilon-insensitive loss and the ability to make probabilistic predictions with the modified huber loss in [Stochastic Gradient Descent](https://scikit-learn.org/stable/modules/sgd.html#sgd)
    , by [Mathieu Blondel](http://www.mblondel.org/)
    .
    
*   Added [Multi-dimensional Scaling (MDS)](https://scikit-learn.org/stable/modules/manifold.html#multidimensional-scaling)
    , by Nelle Varoquaux.
    
*   SVMlight file format loader now detects compressed (gzip/bzip2) files and decompresses them on the fly, by [Lars Buitinck](https://github.com/larsmans)
    .
    
*   SVMlight file format serializer now preserves double precision floating point values, by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   A common testing framework for all estimators was added, by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Understandable error messages for estimators that do not accept sparse input by [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   Speedups in hierarchical clustering by [Gael Varoquaux](https://gael-varoquaux.info/)
    . In particular building the tree now supports early stopping. This is useful when the number of clusters is not small compared to the number of samples.
    
*   Add MultiTaskLasso and MultiTaskElasticNet for joint feature selection, by [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   Added `metrics.auc_score` and [`metrics.average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
     convenience functions by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Improved sparse matrix support in the [Feature selection](https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection)
     module by [Andreas Müller](https://amueller.github.io/)
    .
    
*   New word boundaries-aware character n-gram analyzer for the [Text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
     module by [@kernc](https://github.com/kernc)
    .
    
*   Fixed bug in spectral clustering that led to single point clusters by [Andreas Müller](https://amueller.github.io/)
    .
    
*   In [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
    , added an option to ignore infrequent words, `min_df` by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Add support for multiple targets in some linear models (ElasticNet, Lasso and OrthogonalMatchingPursuit) by [Vlad Niculae](https://vene.ro/)
     and [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   Fixes in `decomposition.ProbabilisticPCA` score function by Wei Li.
    
*   Fixed feature importance computation in [Gradient-boosted trees](https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting)
    .
    

### API changes summary[#](https://scikit-learn.org/stable/whats_new/older_versions.html#api-changes-summary "Link to this heading")

*   The old `scikits.learn` package has disappeared; all code should import from `sklearn` instead, which was introduced in 0.9.
    
*   In [`metrics.roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
    , the `thresholds` array is now returned with its order reversed, in order to keep it consistent with the order of the returned `fpr` and `tpr`.
    
*   In `hmm` objects, like `hmm.GaussianHMM`, `hmm.MultinomialHMM`, etc., all parameters must be passed to the object when initialising it and not through `fit`. Now `fit` will only accept the data as an input parameter.
    
*   For all SVM classes, a faulty behavior of `gamma` was fixed. Previously, the default gamma value was only computed the first time `fit` was called and then stored. It is now recalculated on every call to `fit`.
    
*   All `Base` classes are now abstract meta classes so that they can not be instantiated.
    
*   [`cluster.ward_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.ward_tree.html#sklearn.cluster.ward_tree "sklearn.cluster.ward_tree")
     now also returns the parent array. This is necessary for early-stopping in which case the tree is not completely built.
    
*   In [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     the parameters `min_n` and `max_n` were joined to the parameter `n_gram_range` to enable grid-searching both at once.
    
*   In [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
    , words that appear only in one document are now ignored by default. To reproduce the previous behavior, set `min_df=1`.
    
*   Fixed API inconsistency: [`linear_model.SGDClassifier.predict_proba`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier.predict_proba "sklearn.linear_model.SGDClassifier.predict_proba")
     now returns 2d array when fit on two classes.
    
*   Fixed API inconsistency: [`discriminant_analysis.QuadraticDiscriminantAnalysis.decision_function`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.decision_function "sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.decision_function")
     and [`discriminant_analysis.LinearDiscriminantAnalysis.decision_function`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis.decision_function "sklearn.discriminant_analysis.LinearDiscriminantAnalysis.decision_function")
     now return 1d arrays when fit on two classes.
    
*   Grid of alphas used for fitting [`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
     and [`ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
     is now stored in the attribute `alphas_` rather than overriding the init parameter `alphas`.
    
*   Linear models when alpha is estimated by cross-validation store the estimated value in the `alpha_` attribute rather than just `alpha` or `best_alpha`.
    
*   [`GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     now supports [`staged_predict_proba`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.staged_predict_proba "sklearn.ensemble.GradientBoostingClassifier.staged_predict_proba")
    , and [`staged_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.staged_predict "sklearn.ensemble.GradientBoostingClassifier.staged_predict")
    .
    
*   `svm.sparse.SVC` and other sparse SVM classes are now deprecated. All classes in the [Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html#svm)
     module now automatically select the sparse or dense representation based on the input.
    
*   All clustering algorithms now interpret the array `X` given to `fit` as input data, in particular [`SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
     and [`AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
     which previously expected affinity matrices.
    
*   For clustering algorithms that take the desired number of clusters as a parameter, this parameter is now called `n_clusters`.
    

### People[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id2 "Link to this heading")

*   267 [Andreas Müller](https://amueller.github.io/)
    
*   94 [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    
*   89 [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   79 [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    
*   60 [Mathieu Blondel](http://www.mblondel.org/)
    
*   57 [Alexandre Gramfort](https://alexandre.gramfort.net/)
    
*   52 [Vlad Niculae](https://vene.ro/)
    
*   45 [Lars Buitinck](https://github.com/larsmans)
    
*   44 Nelle Varoquaux
    
*   37 [Jaques Grobler](https://github.com/jaquesgrobler)
    
*   30 Alexis Mignon
    
*   30 Immanuel Bayer
    
*   27 [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    
*   16 Subhodeep Moitra
    
*   13 Yannick Schwartz
    
*   12 [@kernc](https://github.com/kernc)
    
*   11 [Virgile Fritsch](https://github.com/VirgileFritsch)
    
*   9 Daniel Duckworth
    
*   9 [Fabian Pedregosa](https://fa.bianp.net/)
    
*   9 [Robert Layton](https://twitter.com/robertlayton)
    
*   8 John Benediktsson
    
*   7 Marko Burjek
    
*   5 [Nicolas Pinto](https://twitter.com/npinto)
    
*   4 Alexandre Abraham
    
*   4 [Jake Vanderplas](https://staff.washington.edu/jakevdp/)
    
*   3 [Brian Holt](http://personal.ee.surrey.ac.uk/Personal/B.Holt)
    
*   3 [Edouard Duchesnay](https://duchesnay.github.io/)
    
*   3 Florian Hoenig
    
*   3 flyingimmidev
    
*   2 Francois Savard
    
*   2 Hannes Schulz
    
*   2 Peter Welinder
    
*   2 [Yaroslav Halchenko](http://www.onerussian.com/)
    
*   2 Wei Li
    
*   1 Alex Companioni
    
*   1 Brandyn A. White
    
*   1 Bussonnier Matthias
    
*   1 Charles-Pierre Astolfi
    
*   1 Dan O’Huiginn
    
*   1 David Cournapeau
    
*   1 Keith Goodman
    
*   1 Ludwig Schwardt
    
*   1 Olivier Hervieu
    
*   1 Sergio Medina
    
*   1 Shiqiao Du
    
*   1 Tim Sheerman-Chase
    
*   1 buguen
    

Version 0.11[#](https://scikit-learn.org/stable/whats_new/older_versions.html#version-0-11 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

**May 7, 2012**

### Changelog[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id3 "Link to this heading")

#### Highlights[#](https://scikit-learn.org/stable/whats_new/older_versions.html#highlights "Link to this heading")

*   Gradient boosted regression trees ([Gradient-boosted trees](https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting)
    ) for classification and regression by [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
     and [Scott White](https://twitter.com/scottblanc)
     .
    
*   Simple dict-based feature loader with support for categorical variables ([`DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
    ) by [Lars Buitinck](https://github.com/larsmans)
    .
    
*   Added Matthews correlation coefficient ([`metrics.matthews_corrcoef`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html#sklearn.metrics.matthews_corrcoef "sklearn.metrics.matthews_corrcoef")
    ) and added macro and micro average options to [`precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")
    , [`metrics.recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")
     and [`f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")
     by [Satrajit Ghosh](https://www.mit.edu/~satra/)
    .
    
*   [Out of Bag Estimates](https://scikit-learn.org/stable/modules/grid_search.html#out-of-bag)
     of generalization error for [Ensembles: Gradient boosting, random forests, bagging, voting, stacking](https://scikit-learn.org/stable/modules/ensemble.html#ensemble)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Randomized sparse linear models for feature selection, by [Alexandre Gramfort](https://alexandre.gramfort.net/)
     and [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   [Label Propagation](https://scikit-learn.org/stable/modules/semi_supervised.html#label-propagation)
     for semi-supervised learning, by Clay Woolam. **Note** the semi-supervised API is still work in progress, and may change.
    
*   Added BIC/AIC model selection to classical [Gaussian mixture models](https://scikit-learn.org/stable/modules/mixture.html#gmm)
     and unified the API with the remainder of scikit-learn, by [Bertrand Thirion](https://team.inria.fr/parietal/bertrand-thirions-page)
    
*   Added `sklearn.cross_validation.StratifiedShuffleSplit`, which is a `sklearn.cross_validation.ShuffleSplit` with balanced splits, by Yannick Schwartz.
    
*   [`NearestCentroid`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")
     classifier added, along with a `shrink_threshold` parameter, which implements **shrunken centroid classification**, by [Robert Layton](https://twitter.com/robertlayton)
    .
    

#### Other changes[#](https://scikit-learn.org/stable/whats_new/older_versions.html#other-changes "Link to this heading")

*   Merged dense and sparse implementations of [Stochastic Gradient Descent](https://scikit-learn.org/stable/modules/sgd.html#sgd)
     module and exposed utility extension types for sequential datasets `seq_dataset` and weight vectors `weight_vector` by [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    .
    
*   Added `partial_fit` (support for online/minibatch learning) and warm\_start to the [Stochastic Gradient Descent](https://scikit-learn.org/stable/modules/sgd.html#sgd)
     module by [Mathieu Blondel](http://www.mblondel.org/)
    .
    
*   Dense and sparse implementations of [Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html#svm)
     classes and [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     merged by [Lars Buitinck](https://github.com/larsmans)
    .
    
*   Regressors can now be used as base estimator in the [Multiclass and multioutput algorithms](https://scikit-learn.org/stable/modules/multiclass.html#multiclass)
     module by [Mathieu Blondel](http://www.mblondel.org/)
    .
    
*   Added n\_jobs option to [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     and [`metrics.pairwise.pairwise_kernels`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html#sklearn.metrics.pairwise.pairwise_kernels "sklearn.metrics.pairwise.pairwise_kernels")
     for parallel computation, by [Mathieu Blondel](http://www.mblondel.org/)
    .
    
*   [K-means](https://scikit-learn.org/stable/modules/clustering.html#k-means)
     can now be run in parallel, using the `n_jobs` argument to either [K-means](https://scikit-learn.org/stable/modules/clustering.html#k-means)
     or [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    , by [Robert Layton](https://twitter.com/robertlayton)
    .
    
*   Improved [Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
     and [Tuning the hyper-parameters of an estimator](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)
     documentation and introduced the new `cross_validation.train_test_split` helper function by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    
*   [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     members `coef_` and `intercept_` changed sign for consistency with `decision_function`; for `kernel==linear`, `coef_` was fixed in the one-vs-one case, by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Performance improvements to efficient leave-one-out cross-validated Ridge regression, esp. for the `n_samples > n_features` case, in [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
    , by Reuben Fletcher-Costin.
    
*   Refactoring and simplification of the [Text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
     API and fixed a bug that caused possible negative IDF, by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Beam pruning option in `_BaseHMM` module has been removed since it is difficult to Cythonize. If you are interested in contributing a Cython version, you can use the python version in the git history as a reference.
    
*   Classes in [Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html#neighbors)
     now support arbitrary Minkowski metric for nearest neighbors searches. The metric can be specified by argument `p`.
    

### API changes summary[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id4 "Link to this heading")

*   `covariance.EllipticEnvelop` is now deprecated. Please use [`EllipticEnvelope`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")
     instead.
    
*   `NeighborsClassifier` and `NeighborsRegressor` are gone in the module [Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html#neighbors)
    . Use the classes [`KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
    , [`RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
    , [`KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
     and/or [`RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
     instead.
    
*   Sparse classes in the [Stochastic Gradient Descent](https://scikit-learn.org/stable/modules/sgd.html#sgd)
     module are now deprecated.
    
*   In `mixture.GMM`, `mixture.DPGMM` and `mixture.VBGMM`, parameters must be passed to an object when initialising it and not through `fit`. Now `fit` will only accept the data as an input parameter.
    
*   methods `rvs` and `decode` in `GMM` module are now deprecated. `sample` and `score` or `predict` should be used instead.
    
*   attribute `_scores` and `_pvalues` in univariate feature selection objects are now deprecated. `scores_` or `pvalues_` should be used instead.
    
*   In [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    , [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
    , [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     and [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
    , the `class_weight` parameter is now an initialization parameter, not a parameter to fit. This makes grid searches over this parameter possible.
    
*   LFW `data` is now always shape `(n_samples, n_features)` to be consistent with the Olivetti faces dataset. Use `images` and `pairs` attribute to access the natural images shapes instead.
    
*   In [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
    , the meaning of the `multi_class` parameter changed. Options now are `'ovr'` and `'crammer_singer'`, with `'ovr'` being the default. This does not change the default behavior but hopefully is less confusing.
    
*   Class `feature_selection.text.Vectorizer` is deprecated and replaced by `feature_selection.text.TfidfVectorizer`.
    
*   The preprocessor / analyzer nested structure for text feature extraction has been removed. All those features are now directly passed as flat constructor arguments to `feature_selection.text.TfidfVectorizer` and `feature_selection.text.CountVectorizer`, in particular the following parameters are now used:
    
*   `analyzer` can be `'word'` or `'char'` to switch the default analysis scheme, or use a specific python callable (as previously).
    
*   `tokenizer` and `preprocessor` have been introduced to make it still possible to customize those steps with the new API.
    
*   `input` explicitly control how to interpret the sequence passed to `fit` and `predict`: filenames, file objects or direct (byte or Unicode) strings.
    
*   charset decoding is explicit and strict by default.
    
*   the `vocabulary`, fitted or not is now stored in the `vocabulary_` attribute to be consistent with the project conventions.
    
*   Class `feature_selection.text.TfidfVectorizer` now derives directly from `feature_selection.text.CountVectorizer` to make grid search trivial.
    
*   methods `rvs` in `_BaseHMM` module are now deprecated. `sample` should be used instead.
    
*   Beam pruning option in `_BaseHMM` module is removed since it is difficult to be Cythonized. If you are interested, you can look in the history codes by git.
    
*   The SVMlight format loader now supports files with both zero-based and one-based column indices, since both occur “in the wild”.
    
*   Arguments in class [`ShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")
     are now consistent with [`StratifiedShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")
    . Arguments `test_fraction` and `train_fraction` are deprecated and renamed to `test_size` and `train_size` and can accept both `float` and `int`.
    
*   Arguments in class `Bootstrap` are now consistent with [`StratifiedShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")
    . Arguments `n_test` and `n_train` are deprecated and renamed to `test_size` and `train_size` and can accept both `float` and `int`.
    
*   Argument `p` added to classes in [Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html#neighbors)
     to specify an arbitrary Minkowski metric for nearest neighbors searches.
    

### People[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id5 "Link to this heading")

*   282 [Andreas Müller](https://amueller.github.io/)
    
*   239 [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    
*   198 [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   129 [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    
*   114 [Mathieu Blondel](http://www.mblondel.org/)
    
*   103 Clay Woolam
    
*   96 [Lars Buitinck](https://github.com/larsmans)
    
*   88 [Jaques Grobler](https://github.com/jaquesgrobler)
    
*   82 [Alexandre Gramfort](https://alexandre.gramfort.net/)
    
*   50 [Bertrand Thirion](https://team.inria.fr/parietal/bertrand-thirions-page)
    
*   42 [Robert Layton](https://twitter.com/robertlayton)
    
*   28 flyingimmidev
    
*   26 [Jake Vanderplas](https://staff.washington.edu/jakevdp/)
    
*   26 Shiqiao Du
    
*   21 [Satrajit Ghosh](https://www.mit.edu/~satra/)
    
*   17 [David Marek](https://davidmarek.cz/)
    
*   17 [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    
*   14 [Vlad Niculae](https://vene.ro/)
    
*   11 Yannick Schwartz
    
*   10 [Fabian Pedregosa](https://fa.bianp.net/)
    
*   9 fcostin
    
*   7 Nick Wilson
    
*   5 Adrien Gaidon
    
*   5 [Nicolas Pinto](https://twitter.com/npinto)
    
*   4 [David Warde-Farley](http://www-etud.iro.umontreal.ca/~wardefar/)
    
*   5 Nelle Varoquaux
    
*   5 Emmanuelle Gouillart
    
*   3 Joonas Sillanpää
    
*   3 Paolo Losi
    
*   2 Charles McCarthy
    
*   2 Roy Hyunjin Han
    
*   2 Scott White
    
*   2 ibayer
    
*   1 Brandyn White
    
*   1 Carlos Scheidegger
    
*   1 Claire Revillet
    
*   1 Conrad Lee
    
*   1 [Edouard Duchesnay](https://duchesnay.github.io/)
    
*   1 Jan Hendrik Metzen
    
*   1 Meng Xinfan
    
*   1 [Rob Zinkov](https://www.zinkov.com/)
    
*   1 Shiqiao
    
*   1 Udi Weinsberg
    
*   1 Virgile Fritsch
    
*   1 Xinfan Meng
    
*   1 Yaroslav Halchenko
    
*   1 jansoe
    
*   1 Leon Palafox
    

Version 0.10[#](https://scikit-learn.org/stable/whats_new/older_versions.html#version-0-10 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

**January 11, 2012**

### Changelog[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id6 "Link to this heading")

*   Python 2.5 compatibility was dropped; the minimum Python version needed to use scikit-learn is now 2.6.
    
*   [Sparse inverse covariance](https://scikit-learn.org/stable/modules/covariance.html#sparse-inverse-covariance)
     estimation using the graph Lasso, with associated cross-validated estimator, by [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   New [Tree](https://scikit-learn.org/stable/modules/tree.html#tree)
     module by [Brian Holt](http://personal.ee.surrey.ac.uk/Personal/B.Holt)
    , [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    , [Satrajit Ghosh](https://www.mit.edu/~satra/)
     and [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    . The module comes with complete documentation and examples.
    
*   Fixed a bug in the RFE module by [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
     (issue #378).
    
*   Fixed a memory leak in [Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html#svm)
     module by [Brian Holt](http://personal.ee.surrey.ac.uk/Personal/B.Holt)
     (issue #367).
    
*   Faster tests by [Fabian Pedregosa](https://fa.bianp.net/)
     and others.
    
*   Silhouette Coefficient cluster analysis evaluation metric added as [`silhouette_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")
     by Robert Layton.
    
*   Fixed a bug in [K-means](https://scikit-learn.org/stable/modules/clustering.html#k-means)
     in the handling of the `n_init` parameter: the clustering algorithm used to be run `n_init` times but the last solution was retained instead of the best solution by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Minor refactoring in [Stochastic Gradient Descent](https://scikit-learn.org/stable/modules/sgd.html#sgd)
     module; consolidated dense and sparse predict methods; Enhanced test time performance by converting model parameters to fortran-style arrays after fitting (only multi-class).
    
*   Adjusted Mutual Information metric added as [`adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")
     by Robert Layton.
    
*   Models like SVC/SVR/LinearSVC/LogisticRegression from libsvm/liblinear now support scaling of C regularization parameter by the number of samples by [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   New [Ensemble Methods](https://scikit-learn.org/stable/modules/ensemble.html#ensemble)
     module by [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
     and [Brian Holt](http://personal.ee.surrey.ac.uk/Personal/B.Holt)
    . The module comes with the random forest algorithm and the extra-trees method, along with documentation and examples.
    
*   [Novelty and Outlier Detection](https://scikit-learn.org/stable/modules/outlier_detection.html#outlier-detection)
    : outlier and novelty detection, by [Virgile Fritsch](https://github.com/VirgileFritsch)
    .
    
*   [Kernel Approximation](https://scikit-learn.org/stable/modules/kernel_approximation.html#kernel-approximation)
    : a transform implementing kernel approximation for fast SGD on non-linear kernels by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Fixed a bug due to atom swapping in [Orthogonal Matching Pursuit (OMP)](https://scikit-learn.org/stable/modules/linear_model.html#omp)
     by [Vlad Niculae](https://vene.ro/)
    .
    
*   [Sparse coding with a precomputed dictionary](https://scikit-learn.org/stable/modules/decomposition.html#sparsecoder)
     by [Vlad Niculae](https://vene.ro/)
    .
    
*   [Mini Batch K-Means](https://scikit-learn.org/stable/modules/clustering.html#mini-batch-kmeans)
     performance improvements by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   [K-means](https://scikit-learn.org/stable/modules/clustering.html#k-means)
     support for sparse matrices by [Mathieu Blondel](http://www.mblondel.org/)
    .
    
*   Improved documentation for developers and for the [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
     module, by [Jake Vanderplas](https://staff.washington.edu/jakevdp/)
    .
    
*   Vectorized 20newsgroups dataset loader ([`fetch_20newsgroups_vectorized`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized")
    ) by [Mathieu Blondel](http://www.mblondel.org/)
    .
    
*   [Multiclass and multioutput algorithms](https://scikit-learn.org/stable/modules/multiclass.html#multiclass)
     by [Lars Buitinck](https://github.com/larsmans)
    .
    
*   Utilities for fast computation of mean and variance for sparse matrices by [Mathieu Blondel](http://www.mblondel.org/)
    .
    
*   Make [`scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html#sklearn.preprocessing.scale "sklearn.preprocessing.scale")
     and `sklearn.preprocessing.Scaler` work on sparse matrices by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    
*   Feature importances using decision trees and/or forest of trees, by [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   Parallel implementation of forests of randomized trees by [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   `sklearn.cross_validation.ShuffleSplit` can subsample the train sets as well as the test sets by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Errors in the build of the documentation fixed by [Andreas Müller](https://amueller.github.io/)
    .
    

### API changes summary[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id7 "Link to this heading")

Here are the code migration instructions when upgrading from scikit-learn version 0.9:

*   Some estimators that may overwrite their inputs to save memory previously had `overwrite_` parameters; these have been replaced with `copy_` parameters with exactly the opposite meaning.
    
    This particularly affects some of the estimators in [`linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
    . The default behavior is still to copy everything passed in.
    
*   The SVMlight dataset loader [`load_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html#sklearn.datasets.load_svmlight_file "sklearn.datasets.load_svmlight_file")
     no longer supports loading two files at once; use `load_svmlight_files` instead. Also, the (unused) `buffer_mb` parameter is gone.
    
*   Sparse estimators in the [Stochastic Gradient Descent](https://scikit-learn.org/stable/modules/sgd.html#sgd)
     module use dense parameter vector `coef_` instead of `sparse_coef_`. This significantly improves test time performance.
    
*   The [Covariance estimation](https://scikit-learn.org/stable/modules/covariance.html#covariance)
     module now has a robust estimator of covariance, the Minimum Covariance Determinant estimator.
    
*   Cluster evaluation metrics in [`cluster`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics.cluster "sklearn.metrics.cluster")
     have been refactored but the changes are backwards compatible. They have been moved to the `metrics.cluster.supervised`, along with `metrics.cluster.unsupervised` which contains the Silhouette Coefficient.
    
*   The `permutation_test_score` function now behaves the same way as `cross_val_score` (i.e. uses the mean score across the folds.)
    
*   Cross Validation generators now use integer indices (`indices=True`) by default instead of boolean masks. This makes it more intuitive to use with sparse matrix data.
    
*   The functions used for sparse coding, `sparse_encode` and `sparse_encode_parallel` have been combined into [`sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")
    , and the shapes of the arrays have been transposed for consistency with the matrix factorization setting, as opposed to the regression setting.
    
*   Fixed an off-by-one error in the SVMlight/LibSVM file format handling; files generated using [`dump_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.dump_svmlight_file.html#sklearn.datasets.dump_svmlight_file "sklearn.datasets.dump_svmlight_file")
     should be re-generated. (They should continue to work, but accidentally had one extra column of zeros prepended.)
    
*   `BaseDictionaryLearning` class replaced by `SparseCodingMixin`.
    
*   `sklearn.utils.extmath.fast_svd` has been renamed [`randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
     and the default oversampling is now fixed to 10 additional random vectors instead of doubling the number of components to extract. The new behavior follows the reference paper.
    

### People[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id8 "Link to this heading")

The following people contributed to scikit-learn since last release:

*   246 [Andreas Müller](https://amueller.github.io/)
    
*   242 [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    
*   220 [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    
*   183 [Brian Holt](http://personal.ee.surrey.ac.uk/Personal/B.Holt)
    
*   166 [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   144 [Lars Buitinck](https://github.com/larsmans)
    
*   73 [Vlad Niculae](https://vene.ro/)
    
*   65 [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    
*   64 [Fabian Pedregosa](https://fa.bianp.net/)
    
*   60 Robert Layton
    
*   55 [Mathieu Blondel](http://www.mblondel.org/)
    
*   52 [Jake Vanderplas](https://staff.washington.edu/jakevdp/)
    
*   44 Noel Dawe
    
*   38 [Alexandre Gramfort](https://alexandre.gramfort.net/)
    
*   24 [Virgile Fritsch](https://github.com/VirgileFritsch)
    
*   23 [Satrajit Ghosh](https://www.mit.edu/~satra/)
    
*   3 Jan Hendrik Metzen
    
*   3 Kenneth C. Arnold
    
*   3 Shiqiao Du
    
*   3 Tim Sheerman-Chase
    
*   3 [Yaroslav Halchenko](http://www.onerussian.com/)
    
*   2 Bala Subrahmanyam Varanasi
    
*   2 DraXus
    
*   2 Michael Eickenberg
    
*   1 Bogdan Trach
    
*   1 Félix-Antoine Fortin
    
*   1 Juan Manuel Caicedo Carvajal
    
*   1 Nelle Varoquaux
    
*   1 [Nicolas Pinto](https://twitter.com/npinto)
    
*   1 Tiziano Zito
    
*   1 Xinfan Meng
    

Version 0.9[#](https://scikit-learn.org/stable/whats_new/older_versions.html#version-0-9 "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

**September 21, 2011**

scikit-learn 0.9 was released on September 2011, three months after the 0.8 release and includes the new modules [Manifold learning](https://scikit-learn.org/stable/modules/manifold.html#manifold)
, [The Dirichlet Process](https://scikit-learn.org/stable/modules/mixture.html#dirichlet-process)
 as well as several new algorithms and documentation improvements.

This release also includes the dictionary-learning work developed by [Vlad Niculae](https://vene.ro/)
 as part of the [Google Summer of Code](https://developers.google.com/open-source/gsoc)
 program.

[![banner2](https://scikit-learn.org/stable/_images/sphx_glr_plot_omp_thumb.png)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_omp.html)
 [![banner1](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_thumb.png)](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html)
 [![banner3](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_pca_thumb.png)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html)

### Changelog[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id9 "Link to this heading")

*   New [Manifold learning](https://scikit-learn.org/stable/modules/manifold.html#manifold)
     module by [Jake Vanderplas](https://staff.washington.edu/jakevdp/)
     and [Fabian Pedregosa](https://fa.bianp.net/)
    .
    
*   New [Dirichlet Process](https://scikit-learn.org/stable/modules/mixture.html#dirichlet-process)
     Gaussian Mixture Model by [Alexandre Passos](https://atpassos.me/)
    
*   [Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html#neighbors)
     module refactoring by [Jake Vanderplas](https://staff.washington.edu/jakevdp/)
     : general refactoring, support for sparse matrices in input, speed and documentation improvements. See the next section for a full list of API changes.
    
*   Improvements on the [Feature selection](https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection)
     module by [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
     : refactoring of the RFE classes, documentation rewrite, increased efficiency and minor API changes.
    
*   [Sparse principal components analysis (SparsePCA and MiniBatchSparsePCA)](https://scikit-learn.org/stable/modules/decomposition.html#sparsepca)
     by [Vlad Niculae](https://vene.ro/)
    , [Gael Varoquaux](https://gael-varoquaux.info/)
     and [Alexandre Gramfort](https://alexandre.gramfort.net/)
    
*   Printing an estimator now behaves independently of architectures and Python version thanks to [Jean Kossaifi](https://github.com/JeanKossaifi)
    .
    
*   [Loader for libsvm/svmlight format](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#libsvm-loader)
     by [Mathieu Blondel](http://www.mblondel.org/)
     and [Lars Buitinck](https://github.com/larsmans)
    
*   Documentation improvements: thumbnails in example gallery by [Fabian Pedregosa](https://fa.bianp.net/)
    .
    
*   Important bugfixes in [Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html#svm)
     module (segfaults, bad performance) by [Fabian Pedregosa](https://fa.bianp.net/)
    .
    
*   Added [Multinomial Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html#multinomial-naive-bayes)
     and [Bernoulli Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html#bernoulli-naive-bayes)
     by [Lars Buitinck](https://github.com/larsmans)
    
*   Text feature extraction optimizations by Lars Buitinck
    
*   Chi-Square feature selection ([`feature_selection.chi2`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2 "sklearn.feature_selection.chi2")
    ) by [Lars Buitinck](https://github.com/larsmans)
    .
    
*   [Generated datasets](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
     module refactoring by [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    
*   [Multiclass and multioutput algorithms](https://scikit-learn.org/stable/modules/multiclass.html#multiclass)
     by [Mathieu Blondel](http://www.mblondel.org/)
    
*   Ball tree rewrite by [Jake Vanderplas](https://staff.washington.edu/jakevdp/)
    
*   Implementation of [DBSCAN](https://scikit-learn.org/stable/modules/clustering.html#dbscan)
     algorithm by Robert Layton
    
*   Kmeans predict and transform by Robert Layton
    
*   Preprocessing module refactoring by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    
*   Faster mean shift by Conrad Lee
    
*   New `Bootstrap`, [Random permutations cross-validation a.k.a. Shuffle & Split](https://scikit-learn.org/stable/modules/cross_validation.html#shufflesplit)
     and various other improvements in cross validation schemes by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
     and [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   Adjusted Rand index and V-Measure clustering evaluation metrics by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    
*   Added [`Orthogonal Matching Pursuit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html#sklearn.linear_model.OrthogonalMatchingPursuit "sklearn.linear_model.OrthogonalMatchingPursuit")
     by [Vlad Niculae](https://vene.ro/)
    
*   Added 2D-patch extractor utilities in the [Feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#feature-extraction)
     module by [Vlad Niculae](https://vene.ro/)
    
*   Implementation of [`LassoLarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV")
     (cross-validated Lasso solver using the Lars algorithm) and [`LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
     (BIC/AIC model selection in Lars) by [Gael Varoquaux](https://gael-varoquaux.info/)
     and [Alexandre Gramfort](https://alexandre.gramfort.net/)
    
*   Scalability improvements to [`metrics.roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
     by Olivier Hervieu
    
*   Distance helper functions [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     and [`metrics.pairwise.pairwise_kernels`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html#sklearn.metrics.pairwise.pairwise_kernels "sklearn.metrics.pairwise.pairwise_kernels")
     by Robert Layton
    
*   [`Mini-Batch K-Means`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     by Nelle Varoquaux and Peter Prettenhofer.
    
*   mldata utilities by Pietro Berkes.
    
*   [The Olivetti faces dataset](https://scikit-learn.org/stable/datasets/real_world.html#olivetti-faces-dataset)
     by [David Warde-Farley](http://www-etud.iro.umontreal.ca/~wardefar/)
    .
    

### API changes summary[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id10 "Link to this heading")

Here are the code migration instructions when upgrading from scikit-learn version 0.8:

*   The `scikits.learn` package was renamed `sklearn`. There is still a `scikits.learn` package alias for backward compatibility.
    
    Third-party projects with a dependency on scikit-learn 0.9+ should upgrade their codebase. For instance, under Linux / MacOSX just run (make a backup first!):
    
    find \-name "\*.py" | xargs sed \-i 's/\\bscikits.learn\\b/sklearn/g'
    
    Copy to clipboard
    
*   Estimators no longer accept model parameters as `fit` arguments: instead all parameters must be only be passed as constructor arguments or using the now public `set_params` method inherited from [`BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
    .
    
    Some estimators can still accept keyword arguments on the `fit` but this is restricted to data-dependent values (e.g. a Gram matrix or an affinity matrix that are precomputed from the `X` data matrix.
    
*   The `cross_val` package has been renamed to `cross_validation` although there is also a `cross_val` package alias in place for backward compatibility.
    
    Third-party projects with a dependency on scikit-learn 0.9+ should upgrade their codebase. For instance, under Linux / MacOSX just run (make a backup first!):
    
    find \-name "\*.py" | xargs sed \-i 's/\\bcross\_val\\b/cross\_validation/g'
    
    Copy to clipboard
    
*   The `score_func` argument of the `sklearn.cross_validation.cross_val_score` function is now expected to accept `y_test` and `y_predicted` as only arguments for classification and regression tasks or `X_test` for unsupervised estimators.
    
*   `gamma` parameter for support vector machine algorithms is set to `1 / n_features` by default, instead of `1 / n_samples`.
    
*   The `sklearn.hmm` has been marked as orphaned: it will be removed from scikit-learn in version 0.11 unless someone steps up to contribute documentation, examples and fix lurking numerical stability issues.
    
*   `sklearn.neighbors` has been made into a submodule. The two previously available estimators, `NeighborsClassifier` and `NeighborsRegressor` have been marked as deprecated. Their functionality has been divided among five new classes: `NearestNeighbors` for unsupervised neighbors searches, `KNeighborsClassifier` & `RadiusNeighborsClassifier` for supervised classification problems, and `KNeighborsRegressor` & `RadiusNeighborsRegressor` for supervised regression problems.
    
*   `sklearn.ball_tree.BallTree` has been moved to `sklearn.neighbors.BallTree`. Using the former will generate a warning.
    
*   `sklearn.linear_model.LARS()` and related classes (LassoLARS, LassoLARSCV, etc.) have been renamed to `sklearn.linear_model.Lars()`.
    
*   All distance metrics and kernels in `sklearn.metrics.pairwise` now have a Y parameter, which by default is None. If not given, the result is the distance (or kernel similarity) between each sample in Y. If given, the result is the pairwise distance (or kernel similarity) between samples in X to Y.
    
*   `sklearn.metrics.pairwise.l1_distance` is now called `manhattan_distance`, and by default returns the pairwise distance. For the component wise distance, set the parameter `sum_over_features` to `False`.
    

Backward compatibility package aliases and other deprecated classes and functions will be removed in version 0.11.

### People[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id11 "Link to this heading")

38 people contributed to this release.

*   387 [Vlad Niculae](https://vene.ro/)
    
*   320 [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    
*   192 [Lars Buitinck](https://github.com/larsmans)
    
*   179 [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   168 [Fabian Pedregosa](https://fa.bianp.net/)
     ([INRIA](https://www.inria.fr/)
    , [Parietal Team](http://parietal.saclay.inria.fr/)
    )
    
*   127 [Jake Vanderplas](https://staff.washington.edu/jakevdp/)
    
*   120 [Mathieu Blondel](http://www.mblondel.org/)
    
*   85 [Alexandre Passos](https://atpassos.me/)
    
*   67 [Alexandre Gramfort](https://alexandre.gramfort.net/)
    
*   57 [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    
*   56 [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    
*   42 Robert Layton
    
*   38 Nelle Varoquaux
    
*   32 [Jean Kossaifi](https://github.com/JeanKossaifi)
    
*   30 Conrad Lee
    
*   22 Pietro Berkes
    
*   18 andy
    
*   17 David Warde-Farley
    
*   12 Brian Holt
    
*   11 Robert
    
*   8 Amit Aides
    
*   8 [Virgile Fritsch](https://github.com/VirgileFritsch)
    
*   7 [Yaroslav Halchenko](http://www.onerussian.com/)
    
*   6 Salvatore Masecchia
    
*   5 Paolo Losi
    
*   4 Vincent Schut
    
*   3 Alexis Metaireau
    
*   3 Bryan Silverthorn
    
*   3 [Andreas Müller](https://amueller.github.io/)
    
*   2 Minwoo Jake Lee
    
*   1 Emmanuelle Gouillart
    
*   1 Keith Goodman
    
*   1 Lucas Wiman
    
*   1 [Nicolas Pinto](https://twitter.com/npinto)
    
*   1 Thouis (Ray) Jones
    
*   1 Tim Sheerman-Chase
    

Version 0.8[#](https://scikit-learn.org/stable/whats_new/older_versions.html#version-0-8 "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

**May 11, 2011**

scikit-learn 0.8 was released on May 2011, one month after the first “international” [scikit-learn coding sprint](https://github.com/scikit-learn/scikit-learn/wiki/Upcoming-events)
 and is marked by the inclusion of important modules: [Hierarchical clustering](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)
, [Cross decomposition](https://scikit-learn.org/stable/modules/cross_decomposition.html#cross-decomposition)
, [Non-negative matrix factorization (NMF or NNMF)](https://scikit-learn.org/stable/modules/decomposition.html#nmf)
, initial support for Python 3 and by important enhancements and bug fixes.

### Changelog[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id12 "Link to this heading")

Several new modules were introduced during this release:

*   New [Hierarchical clustering](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)
     module by Vincent Michel, [Bertrand Thirion](https://team.inria.fr/parietal/bertrand-thirions-page)
    , [Alexandre Gramfort](https://alexandre.gramfort.net/)
     and [Gael Varoquaux](https://gael-varoquaux.info/)
    .
    
*   [Kernel Principal Component Analysis (kPCA)](https://scikit-learn.org/stable/modules/decomposition.html#kernel-pca)
     implementation by [Mathieu Blondel](http://www.mblondel.org/)
    
*   [The Labeled Faces in the Wild face recognition dataset](https://scikit-learn.org/stable/datasets/real_world.html#labeled-faces-in-the-wild-dataset)
     by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   New [Cross decomposition](https://scikit-learn.org/stable/modules/cross_decomposition.html#cross-decomposition)
     module by [Edouard Duchesnay](https://duchesnay.github.io/)
    .
    
*   [Non-negative matrix factorization (NMF or NNMF)](https://scikit-learn.org/stable/modules/decomposition.html#nmf)
     module [Vlad Niculae](https://vene.ro/)
    
*   Implementation of the [Oracle Approximating Shrinkage](https://scikit-learn.org/stable/modules/covariance.html#oracle-approximating-shrinkage)
     algorithm by [Virgile Fritsch](https://github.com/VirgileFritsch)
     in the [Covariance estimation](https://scikit-learn.org/stable/modules/covariance.html#covariance)
     module.
    

Some other modules benefited from significant improvements or cleanups.

*   Initial support for Python 3: builds and imports cleanly, some modules are usable while others have failing tests by [Fabian Pedregosa](https://fa.bianp.net/)
    .
    
*   [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     is now usable from the Pipeline object by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Guide [How to optimize for speed](https://scikit-learn.org/stable/developers/performance.html#performance-howto)
     by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Fixes for memory leaks in libsvm bindings, 64-bit safer BallTree by Lars Buitinck.
    
*   bug and style fixing in [K-means](https://scikit-learn.org/stable/modules/clustering.html#k-means)
     algorithm by Jan Schlüter.
    
*   Add attribute converged to Gaussian Mixture Models by Vincent Schut.
    
*   Implemented `transform`, `predict_log_proba` in [`LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     By [Mathieu Blondel](http://www.mblondel.org/)
    .
    
*   Refactoring in the [Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html#svm)
     module and bug fixes by [Fabian Pedregosa](https://fa.bianp.net/)
    , [Gael Varoquaux](https://gael-varoquaux.info/)
     and Amit Aides.
    
*   Refactored SGD module (removed code duplication, better variable naming), added interface for sample weight by [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    .
    
*   Wrapped BallTree with Cython by Thouis (Ray) Jones.
    
*   Added function [`svm.l1_min_c`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.l1_min_c.html#sklearn.svm.l1_min_c "sklearn.svm.l1_min_c")
     by Paolo Losi.
    
*   Typos, doc style, etc. by [Yaroslav Halchenko](http://www.onerussian.com/)
    , [Gael Varoquaux](https://gael-varoquaux.info/)
    , [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    , Yann Malet, [Nicolas Pinto](https://twitter.com/npinto)
    , Lars Buitinck and [Fabian Pedregosa](https://fa.bianp.net/)
    .
    

### People[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id13 "Link to this heading")

People that made this release possible preceded by number of commits:

*   159 [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    
*   96 [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   96 [Vlad Niculae](https://vene.ro/)
    
*   94 [Fabian Pedregosa](https://fa.bianp.net/)
    
*   36 [Alexandre Gramfort](https://alexandre.gramfort.net/)
    
*   32 Paolo Losi
    
*   31 [Edouard Duchesnay](https://duchesnay.github.io/)
    
*   30 [Mathieu Blondel](http://www.mblondel.org/)
    
*   25 [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    
*   22 [Nicolas Pinto](https://twitter.com/npinto)
    
*   11 [Virgile Fritsch](https://github.com/VirgileFritsch)
    
*   7 Lars Buitinck
    
*   6 Vincent Michel
    
*   5 [Bertrand Thirion](https://team.inria.fr/parietal/bertrand-thirions-page)
    
*   4 Thouis (Ray) Jones
    
*   4 Vincent Schut
    
*   3 Jan Schlüter
    
*   2 Julien Miotte
    
*   2 [Matthieu Perrot](http://brainvisa.info/biblio/lnao/en/Author/PERROT-M.html)
    
*   2 Yann Malet
    
*   2 [Yaroslav Halchenko](http://www.onerussian.com/)
    
*   1 Amit Aides
    
*   1 [Andreas Müller](https://amueller.github.io/)
    
*   1 Feth Arezki
    
*   1 Meng Xinfan
    

Version 0.7[#](https://scikit-learn.org/stable/whats_new/older_versions.html#version-0-7 "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

**March 2, 2011**

scikit-learn 0.7 was released in March 2011, roughly three months after the 0.6 release. This release is marked by the speed improvements in existing algorithms like k-Nearest Neighbors and K-Means algorithm and by the inclusion of an efficient algorithm for computing the Ridge Generalized Cross Validation solution. Unlike the preceding release, no new modules were added to this release.

### Changelog[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id14 "Link to this heading")

*   Performance improvements for Gaussian Mixture Model sampling \[Jan Schlüter\].
    
*   Implementation of efficient leave-one-out cross-validated Ridge in [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     \[[Mathieu Blondel](http://www.mblondel.org/)\
    \]
    
*   Better handling of collinearity and early stopping in [`linear_model.lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")
     \[[Alexandre Gramfort](https://alexandre.gramfort.net/)\
     and [Fabian Pedregosa](https://fa.bianp.net/)\
    \].
    
*   Fixes for liblinear ordering of labels and sign of coefficients \[Dan Yamins, Paolo Losi, [Mathieu Blondel](http://www.mblondel.org/)\
     and [Fabian Pedregosa](https://fa.bianp.net/)\
    \].
    
*   Performance improvements for Nearest Neighbors algorithm in high-dimensional spaces \[[Fabian Pedregosa](https://fa.bianp.net/)\
    \].
    
*   Performance improvements for [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     \[[Gael Varoquaux](https://gael-varoquaux.info/)\
     and [James Bergstra](http://www-etud.iro.umontreal.ca/~bergstrj/)\
    \].
    
*   Sanity checks for SVM-based classes \[[Mathieu Blondel](http://www.mblondel.org/)\
    \].
    
*   Refactoring of `neighbors.NeighborsClassifier` and [`neighbors.kneighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html#sklearn.neighbors.kneighbors_graph "sklearn.neighbors.kneighbors_graph")
    : added different algorithms for the k-Nearest Neighbor Search and implemented a more stable algorithm for finding barycenter weights. Also added some developer documentation for this module, see [notes\_neighbors](https://github.com/scikit-learn/scikit-learn/wiki/Neighbors-working-notes)
     for more information \[[Fabian Pedregosa](https://fa.bianp.net/)\
    \].
    
*   Documentation improvements: Added `pca.RandomizedPCA` and [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     to the class reference. Also added references of matrices used for clustering and other fixes \[[Gael Varoquaux](https://gael-varoquaux.info/)\
    , [Fabian Pedregosa](https://fa.bianp.net/)\
    , [Mathieu Blondel](http://www.mblondel.org/)\
    , [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)\
    , Virgile Fritsch , Emmanuelle Gouillart\]
    
*   Binded decision\_function in classes that make use of [liblinear](https://www.csie.ntu.edu.tw/~cjlin/liblinear/)
    , dense and sparse variants, like [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
     or [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     \[[Fabian Pedregosa](https://fa.bianp.net/)\
    \].
    
*   Performance and API improvements to [`metrics.pairwise.euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html#sklearn.metrics.pairwise.euclidean_distances "sklearn.metrics.pairwise.euclidean_distances")
     and to `pca.RandomizedPCA` \[[James Bergstra](http://www-etud.iro.umontreal.ca/~bergstrj/)\
    \].
    
*   Fix compilation issues under NetBSD \[Kamel Ibn Hassen Derouiche\]
    
*   Allow input sequences of different lengths in `hmm.GaussianHMM` \[[Ron Weiss](https://www.ee.columbia.edu/~ronw/)\
    \].
    
*   Fix bug in affinity propagation caused by incorrect indexing \[Xinfan Meng\]
    

### People[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id15 "Link to this heading")

People that made this release possible preceded by number of commits:

*   85 [Fabian Pedregosa](https://fa.bianp.net/)
    
*   67 [Mathieu Blondel](http://www.mblondel.org/)
    
*   20 [Alexandre Gramfort](https://alexandre.gramfort.net/)
    
*   19 [James Bergstra](http://www-etud.iro.umontreal.ca/~bergstrj/)
    
*   14 Dan Yamins
    
*   13 [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    
*   12 [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   4 [Edouard Duchesnay](https://duchesnay.github.io/)
    
*   4 [Ron Weiss](https://www.ee.columbia.edu/~ronw/)
    
*   2 Satrajit Ghosh
    
*   2 Vincent Dubourg
    
*   1 Emmanuelle Gouillart
    
*   1 Kamel Ibn Hassen Derouiche
    
*   1 Paolo Losi
    
*   1 VirgileFritsch
    
*   1 [Yaroslav Halchenko](http://www.onerussian.com/)
    
*   1 Xinfan Meng
    

Version 0.6[#](https://scikit-learn.org/stable/whats_new/older_versions.html#version-0-6 "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

**December 21, 2010**

scikit-learn 0.6 was released on December 2010. It is marked by the inclusion of several new modules and a general renaming of old ones. It is also marked by the inclusion of new example, including applications to real-world datasets.

### Changelog[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id16 "Link to this heading")

*   New [stochastic gradient](https://scikit-learn.org/stable/modules/sgd.html)
     descent module by Peter Prettenhofer. The module comes with complete documentation and examples.
    
*   Improved svm module: memory consumption has been reduced by 50%, heuristic to automatically set class weights, possibility to assign weights to samples (see [SVM: Weighted samples](https://scikit-learn.org/stable/auto_examples/svm/plot_weighted_samples.html#sphx-glr-auto-examples-svm-plot-weighted-samples-py)
     for an example).
    
*   New [Gaussian Processes](https://scikit-learn.org/stable/modules/gaussian_process.html#gaussian-process)
     module by Vincent Dubourg. This module also has great documentation and some very neat examples. See example\_gaussian\_process\_plot\_gp\_regression.py or example\_gaussian\_process\_plot\_gp\_probabilistic\_classification\_after\_regression.py for a taste of what can be done.
    
*   It is now possible to use liblinear’s Multi-class SVC (option multi\_class in [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
    )
    
*   New features and performance improvements of text feature extraction.
    
*   Improved sparse matrix support, both in main classes ([`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    ) as in modules sklearn.svm.sparse and sklearn.linear\_model.sparse.
    
*   Lots of cool new examples and a new section that uses real-world datasets was created. These include: [Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html#sphx-glr-auto-examples-applications-plot-face-recognition-py)
    , [Species distribution modeling](https://scikit-learn.org/stable/auto_examples/applications/plot_species_distribution_modeling.html#sphx-glr-auto-examples-applications-plot-species-distribution-modeling-py)
    , [Wikipedia principal eigenvector](https://scikit-learn.org/stable/auto_examples/applications/plot_wikipedia_principal_eigenvector.html#sphx-glr-auto-examples-applications-plot-wikipedia-principal-eigenvector-py)
     and others.
    
*   Faster [Least Angle Regression](https://scikit-learn.org/stable/modules/linear_model.html#least-angle-regression)
     algorithm. It is now 2x faster than the R version on worst case and up to 10x times faster on some cases.
    
*   Faster coordinate descent algorithm. In particular, the full path version of lasso ([`linear_model.lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")
    ) is more than 200x times faster than before.
    
*   It is now possible to get probability estimates from a [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     model.
    
*   module renaming: the glm module has been renamed to linear\_model, the gmm module has been included into the more general mixture model and the sgd module has been included in linear\_model.
    
*   Lots of bug fixes and documentation improvements.
    

### People[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id17 "Link to this heading")

People that made this release possible preceded by number of commits:

*   207 [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    
*   167 [Fabian Pedregosa](https://fa.bianp.net/)
    
*   97 [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    
*   68 [Alexandre Gramfort](https://alexandre.gramfort.net/)
    
*   59 [Mathieu Blondel](http://www.mblondel.org/)
    
*   55 [Gael Varoquaux](https://gael-varoquaux.info/)
    
*   33 Vincent Dubourg
    
*   21 [Ron Weiss](https://www.ee.columbia.edu/~ronw/)
    
*   9 Bertrand Thirion
    
*   3 [Alexandre Passos](https://atpassos.me/)
    
*   3 Anne-Laure Fouque
    
*   2 Ronan Amicel
    
*   1 [Christian Osendorfer](https://osdf.github.io/)
    

Version 0.5[#](https://scikit-learn.org/stable/whats_new/older_versions.html#version-0-5 "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

**October 11, 2010**

### Changelog[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id18 "Link to this heading")

### New classes[#](https://scikit-learn.org/stable/whats_new/older_versions.html#new-classes "Link to this heading")

*   Support for sparse matrices in some classifiers of modules `svm` and `linear_model` (see `svm.sparse.SVC`, `svm.sparse.SVR`, `svm.sparse.LinearSVC`, `linear_model.sparse.Lasso`, `linear_model.sparse.ElasticNet`)
    
*   New [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     object to compose different estimators.
    
*   Recursive Feature Elimination routines in module [Feature selection](https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection)
    .
    
*   Addition of various classes capable of cross validation in the linear\_model module ([`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
    , [`ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    , etc.).
    
*   New, more efficient LARS algorithm implementation. The Lasso variant of the algorithm is also implemented. See [`lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")
    , [`Lars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html#sklearn.linear_model.Lars "sklearn.linear_model.Lars")
     and [`LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")
    .
    
*   New Hidden Markov Models module (see classes `hmm.GaussianHMM`, `hmm.MultinomialHMM`, `hmm.GMMHMM`)
    
*   New module feature\_extraction (see [class reference](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#feature-extraction-ref)
    )
    
*   New FastICA algorithm in module sklearn.fastica
    

### Documentation[#](https://scikit-learn.org/stable/whats_new/older_versions.html#documentation "Link to this heading")

*   Improved documentation for many modules, now separating narrative documentation from the class reference. As an example, see [documentation for the SVM module](https://scikit-learn.org/stable/modules/svm.html)
     and the complete [class reference](https://scikit-learn.org/stable/modules/classes.html)
    .
    

### Fixes[#](https://scikit-learn.org/stable/whats_new/older_versions.html#fixes "Link to this heading")

*   API changes: adhere variable names to PEP-8, give more meaningful names.
    
*   Fixes for svm module to run on a shared memory context (multiprocessing).
    
*   It is again possible to generate latex (and thus PDF) from the sphinx docs.
    

### Examples[#](https://scikit-learn.org/stable/whats_new/older_versions.html#examples "Link to this heading")

*   new examples using some of the mlcomp datasets: `sphx_glr_auto_examples_mlcomp_sparse_document_classification.py` (since removed) and [Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#sphx-glr-auto-examples-text-plot-document-classification-20newsgroups-py)
    
*   Many more examples. [See here](https://scikit-learn.org/stable/auto_examples/index.html)
     the full list of examples.
    

### External dependencies[#](https://scikit-learn.org/stable/whats_new/older_versions.html#external-dependencies "Link to this heading")

*   Joblib is now a dependency of this package, although it is shipped with (sklearn.externals.joblib).
    

### Removed modules[#](https://scikit-learn.org/stable/whats_new/older_versions.html#removed-modules "Link to this heading")

*   Module ann (Artificial Neural Networks) has been removed from the distribution. Users wanting this sort of algorithms should take a look into pybrain.
    

### Misc[#](https://scikit-learn.org/stable/whats_new/older_versions.html#misc "Link to this heading")

*   New sphinx theme for the web page.
    

### Authors[#](https://scikit-learn.org/stable/whats_new/older_versions.html#authors "Link to this heading")

The following is a list of authors for this release, preceded by number of commits:

*   262 Fabian Pedregosa
    
*   240 Gael Varoquaux
    
*   149 Alexandre Gramfort
    
*   116 Olivier Grisel
    
*   40 Vincent Michel
    
*   38 Ron Weiss
    
*   23 Matthieu Perrot
    
*   10 Bertrand Thirion
    
*   7 Yaroslav Halchenko
    
*   9 VirgileFritsch
    
*   6 Edouard Duchesnay
    
*   4 Mathieu Blondel
    
*   1 Ariel Rokem
    
*   1 Matthieu Brucher
    

Version 0.4[#](https://scikit-learn.org/stable/whats_new/older_versions.html#version-0-4 "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

**August 26, 2010**

### Changelog[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id19 "Link to this heading")

Major changes in this release include:

*   Coordinate Descent algorithm (Lasso, ElasticNet) refactoring & speed improvements (roughly 100x times faster).
    
*   Coordinate Descent Refactoring (and bug fixing) for consistency with R’s package GLMNET.
    
*   New metrics module.
    
*   New GMM module contributed by Ron Weiss.
    
*   Implementation of the LARS algorithm (without Lasso variant for now).
    
*   feature\_selection module redesign.
    
*   Migration to GIT as version control system.
    
*   Removal of obsolete attrselect module.
    
*   Rename of private compiled extensions (added underscore).
    
*   Removal of legacy unmaintained code.
    
*   Documentation improvements (both docstring and rst).
    
*   Improvement of the build system to (optionally) link with MKL. Also, provide a lite BLAS implementation in case no system-wide BLAS is found.
    
*   Lots of new examples.
    
*   Many, many bug fixes …
    

### Authors[#](https://scikit-learn.org/stable/whats_new/older_versions.html#id20 "Link to this heading")

The committer list for this release is the following (preceded by number of commits):

*   143 Fabian Pedregosa
    
*   35 Alexandre Gramfort
    
*   34 Olivier Grisel
    
*   11 Gael Varoquaux
    
*   5 Yaroslav Halchenko
    
*   2 Vincent Michel
    
*   1 Chris Filo Gorgolewski
    

Earlier versions[#](https://scikit-learn.org/stable/whats_new/older_versions.html#earlier-versions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

Earlier versions included contributions by Fred Mailhot, David Cooke, David Huard, Dave Morrill, Ed Schofield, Travis Oliphant, Pearu Peterson.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)