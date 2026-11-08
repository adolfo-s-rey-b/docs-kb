[Skip to main content](https://scikit-learn.org/stable/whats_new/v0.14.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v0.14.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v0.14.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v0.14.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v0.14.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v0.14.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v0.14.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v0.14.html)

Collapse Sidebar Expand Sidebar

Version 0.14[#](https://scikit-learn.org/stable/whats_new/v0.14.html#version-0-14 "Link to this heading")

==========================================================================================================

Version 0.14[#](https://scikit-learn.org/stable/whats_new/v0.14.html#changes-0-14 "Link to this heading")

----------------------------------------------------------------------------------------------------------

**August 7, 2013**

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.14.html#changelog "Link to this heading")

*   Missing values with sparse and dense matrices can be imputed with the transformer `preprocessing.Imputer` by [Nicolas Trésegnie](https://github.com/NicolasTr)
    .
    
*   The core implementation of decision trees has been rewritten from scratch, allowing for faster tree induction and lower memory consumption in all tree-based estimators. By [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   Added [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
     and [`ensemble.AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
    , by [Noel Dawe](https://github.com/ndawe)
     and [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    . See the [AdaBoost](https://scikit-learn.org/stable/modules/ensemble.html#adaboost)
     section of the user guide for details and examples.
    
*   Added `grid_search.RandomizedSearchCV` and `grid_search.ParameterSampler` for randomized hyperparameter optimization. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   Added [biclustering](https://scikit-learn.org/stable/modules/biclustering.html#biclustering)
     algorithms (`sklearn.cluster.bicluster.SpectralCoclustering` and `sklearn.cluster.bicluster.SpectralBiclustering`), data generation methods ([`sklearn.datasets.make_biclusters`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_biclusters.html#sklearn.datasets.make_biclusters "sklearn.datasets.make_biclusters")
     and [`sklearn.datasets.make_checkerboard`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_checkerboard.html#sklearn.datasets.make_checkerboard "sklearn.datasets.make_checkerboard")
    ), and scoring metrics ([`sklearn.metrics.consensus_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.consensus_score.html#sklearn.metrics.consensus_score "sklearn.metrics.consensus_score")
    ). By [Kemal Eren](http://www.kemaleren.com/)
    .
    
*   Added [Restricted Boltzmann Machines](https://scikit-learn.org/stable/modules/neural_networks_unsupervised.html#rbm)
     ([`neural_network.BernoulliRBM`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM "sklearn.neural_network.BernoulliRBM")
    ). By [Yann Dauphin](https://ynd.github.io/)
    .
    
*   Python 3 support by [Justin Vincent](https://github.com/justinvf)
    , [Lars Buitinck](https://github.com/larsmans)
    , [Subhodeep Moitra](https://github.com/smoitra87)
     and [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    . All tests now pass under Python 3.3.
    
*   Ability to pass one penalty (alpha value) per target in [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    , by @eickenberg and [Mathieu Blondel](http://www.mblondel.org/)
    .
    
*   Fixed `sklearn.linear_model.stochastic_gradient.py` L2 regularization issue (minor practical significance). By [Norbert Crombach](https://github.com/norbert)
     and [Mathieu Blondel](http://www.mblondel.org/)
     .
    
*   Added an interactive version of [Andreas Müller](https://amueller.github.io/)
    ’s [Machine Learning Cheat Sheet (for scikit-learn)](https://peekaboo-vision.blogspot.de/2013/01/machine-learning-cheat-sheet-for-scikit.html)
     to the documentation. See [Choosing the right estimator](https://scikit-learn.org/stable/machine_learning_map.html#ml-map)
    . By [Jaques Grobler](https://github.com/jaquesgrobler)
    .
    
*   `grid_search.GridSearchCV` and `cross_validation.cross_val_score` now support the use of advanced scoring functions such as area under the ROC curve and f-beta scores. See [The scoring parameter: defining model evaluation rules](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter)
     for details. By [Andreas Müller](https://amueller.github.io/)
     and [Lars Buitinck](https://github.com/larsmans)
    . Passing a function from [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
     as `score_func` is deprecated.
    
*   Multi-label classification output is now supported by [`metrics.accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
    , [`metrics.zero_one_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "sklearn.metrics.zero_one_loss")
    , [`metrics.f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")
    , [`metrics.fbeta_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#sklearn.metrics.fbeta_score "sklearn.metrics.fbeta_score")
    , [`metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
    , [`metrics.precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")
     and [`metrics.recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")
     by [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Two new metrics [`metrics.hamming_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "sklearn.metrics.hamming_loss")
     and `metrics.jaccard_similarity_score` are added with multi-label support by [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Speed and memory usage improvements in [`feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     and [`feature_extraction.text.TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
    , by Jochen Wersdörfer and Roman Sinayev.
    
*   The `min_df` parameter in [`feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     and [`feature_extraction.text.TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
    , which used to be 2, has been reset to 1 to avoid unpleasant surprises (empty vocabularies) for novice users who try it out on tiny document collections. A value of at least 2 is still recommended for practical use.
    
*   [`svm.LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
    , [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     and [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     now have a `sparsify` method that converts their `coef_` into a sparse matrix, meaning stored models trained using these estimators can be made much more compact.
    
*   [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     now produces multiclass probability estimates when trained under log loss or modified Huber loss.
    
*   Hyperlinks to documentation in example code on the website by [Martin Luessi](https://github.com/mluessi)
    .
    
*   Fixed bug in [`preprocessing.MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
     causing incorrect scaling of the features for non-default `feature_range` settings. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   `max_features` in [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
     and all derived ensemble estimators now support percentage values. By [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   Performance improvements in [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
     by [Nelle Varoquaux](https://github.com/nellev)
    .
    
*   [`metrics.accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
     has an option normalize to return the fraction or the number of correctly classified samples by [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Added [`metrics.log_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
     that computes log loss, aka cross-entropy loss. By Jochen Wersdörfer and [Lars Buitinck](https://github.com/larsmans)
    .
    
*   A bug that caused [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
    ’s to output incorrect probabilities has been fixed.
    
*   Feature selectors now share a mixin providing consistent `transform`, `inverse_transform` and `get_support` methods. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   A fitted `grid_search.GridSearchCV` or `grid_search.RandomizedSearchCV` can now generally be pickled. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   Refactored and vectorized implementation of [`metrics.roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
     and [`metrics.precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")
    . By [Joel Nothman](https://joelnothman.com/)
    .
    
*   The new estimator [`sklearn.decomposition.TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
     performs dimensionality reduction using SVD on sparse matrices, and can be used for latent semantic analysis (LSA). By [Lars Buitinck](https://github.com/larsmans)
    .
    
*   Added self-contained example of out-of-core learning on text data [Out-of-core classification of text documents](https://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html#sphx-glr-auto-examples-applications-plot-out-of-core-classification-py)
    . By [Eustache Diemert](https://github.com/oddskool)
    .
    
*   The default number of components for `sklearn.decomposition.RandomizedPCA` is now correctly documented to be `n_features`. This was the default behavior, so programs using it will continue to work as they did.
    
*   [`sklearn.cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     now fits several orders of magnitude faster on sparse data (the speedup depends on the sparsity). By [Lars Buitinck](https://github.com/larsmans)
    .
    
*   Reduce memory footprint of FastICA by [Denis Engemann](https://denis-engemann.de/)
     and [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   Verbose output in `sklearn.ensemble.gradient_boosting` now uses a column format and prints progress in decreasing frequency. It also shows the remaining time. By [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    .
    
*   `sklearn.ensemble.gradient_boosting` provides out-of-bag improvement `oob_improvement_` rather than the OOB score for model selection. An example that shows how to use OOB estimates to select the number of trees was added. By [Peter Prettenhofer](https://sites.google.com/site/peterprettenhofer/)
    .
    
*   Most metrics now support string labels for multiclass classification by [Arnaud Joly](http://www.ajoly.org/)
     and [Lars Buitinck](https://github.com/larsmans)
    .
    
*   New OrthogonalMatchingPursuitCV class by [Alexandre Gramfort](https://alexandre.gramfort.net/)
     and [Vlad Niculae](https://vene.ro/)
    .
    
*   Fixed a bug in `sklearn.covariance.GraphLassoCV`: the ‘alphas’ parameter now works as expected when given a list of values. By Philippe Gervais.
    
*   Fixed an important bug in `sklearn.covariance.GraphLassoCV` that prevented all folds provided by a CV object to be used (only the first 3 were used). When providing a CV object, execution time may thus increase significantly compared to the previous version (bug results are correct now). By Philippe Gervais.
    
*   `cross_validation.cross_val_score` and the `grid_search` module is now tested with multi-output data by [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   [`datasets.make_multilabel_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "sklearn.datasets.make_multilabel_classification")
     can now return the output in label indicator multilabel format by [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   K-nearest neighbors, [`neighbors.KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
     and [`neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
    , and radius neighbors, [`neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
     and [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
     support multioutput data by [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Random state in LibSVM-based estimators ([`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
    , [`svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
    , [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
    , [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
    , [`svm.NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
    ) can now be controlled. This is useful to ensure consistency in the probability estimates for the classifiers trained with `probability=True`. By [Vlad Niculae](https://vene.ro/)
    .
    
*   Out-of-core learning support for discrete naive Bayes classifiers [`sklearn.naive_bayes.MultinomialNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB "sklearn.naive_bayes.MultinomialNB")
     and [`sklearn.naive_bayes.BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
     by adding the `partial_fit` method by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   New website design and navigation by [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    , [Nelle Varoquaux](https://github.com/nellev)
    , Vincent Michel and [Andreas Müller](https://amueller.github.io/)
    .
    
*   Improved documentation on [multi-class, multi-label and multi-output classification](https://scikit-learn.org/stable/modules/multiclass.html#multiclass)
     by [Yannick Schwartz](https://team.inria.fr/parietal/schwarty/)
     and [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Better input and error handling in the [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
     module by [Arnaud Joly](http://www.ajoly.org/)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   Speed optimization of the `hmm` module by [Mikhail Korobov](https://github.com/kmike)
    
*   Significant speed improvements for [`sklearn.cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
     by [cleverless](https://github.com/cleverless)
    

### API changes summary[#](https://scikit-learn.org/stable/whats_new/v0.14.html#api-changes-summary "Link to this heading")

*   The `auc_score` was renamed [`metrics.roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
    .
    
*   Testing scikit-learn with `sklearn.test()` is deprecated. Use `nosetests sklearn` from the command line.
    
*   Feature importances in [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
     and all derived ensemble estimators are now computed on the fly when accessing the `feature_importances_` attribute. Setting `compute_importances=True` is no longer required. By [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   [`linear_model.lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")
     and [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
     can return its results in the same format as that of [`linear_model.lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")
    . This is done by setting the `return_models` parameter to `False`. By [Jaques Grobler](https://github.com/jaquesgrobler)
     and [Alexandre Gramfort](https://alexandre.gramfort.net/)
    
*   `grid_search.IterGrid` was renamed to `grid_search.ParameterGrid`.
    
*   Fixed bug in `KFold` causing imperfect class balance in some cases. By [Alexandre Gramfort](https://alexandre.gramfort.net/)
     and Tadej Janež.
    
*   [`sklearn.neighbors.BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
     has been refactored, and a [`sklearn.neighbors.KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
     has been added which shares the same interface. The Ball Tree now works with a wide variety of distance metrics. Both classes have many new methods, including single-tree and dual-tree queries, breadth-first and depth-first searching, and more advanced queries such as kernel density estimation and 2-point correlation functions. By [Jake Vanderplas](https://staff.washington.edu/jakevdp/)
    
*   Support for scipy.spatial.cKDTree within neighbors queries has been removed, and the functionality replaced with the new [`sklearn.neighbors.KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
     class.
    
*   [`sklearn.neighbors.KernelDensity`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
     has been added, which performs efficient kernel density estimation with a variety of kernels.
    
*   [`sklearn.decomposition.KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
     now always returns output with `n_components` components, unless the new parameter `remove_zero_eig` is set to `True`. This new behavior is consistent with the way kernel PCA was always documented; previously, the removal of components with zero eigenvalues was tacitly performed on all data.
    
*   `gcv_mode="auto"` no longer tries to perform SVD on a densified sparse matrix in [`sklearn.linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
    .
    
*   Sparse matrix support in `sklearn.decomposition.RandomizedPCA` is now deprecated in favor of the new `TruncatedSVD`.
    
*   `cross_validation.KFold` and `cross_validation.StratifiedKFold` now enforce `n_folds >= 2` otherwise a `ValueError` is raised. By [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   [`datasets.load_files`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_files.html#sklearn.datasets.load_files "sklearn.datasets.load_files")
    ’s `charset` and `charset_errors` parameters were renamed `encoding` and `decode_errors`.
    
*   Attribute `oob_score_` in [`sklearn.ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     and [`sklearn.ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     is deprecated and has been replaced by `oob_improvement_` .
    
*   Attributes in OrthogonalMatchingPursuit have been deprecated (copy\_X, Gram, …) and precompute\_gram renamed precompute for consistency. See #2224.
    
*   [`sklearn.preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
     now converts integer input to float, and raises a warning. Previously it rounded for dense integer input.
    
*   [`sklearn.multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
     now has a `decision_function` method. This will return the distance of each sample from the decision boundary for each class, as long as the underlying estimators implement the `decision_function` method. By [Kyle Kastner](https://kastnerkyle.github.io/)
    .
    
*   Better input validation, warning on unexpected shapes for y.
    

### People[#](https://scikit-learn.org/stable/whats_new/v0.14.html#people "Link to this heading")

List of contributors for release 0.14 by number of commits.

*   277 Gilles Louppe
    
*   245 Lars Buitinck
    
*   187 Andreas Mueller
    
*   124 Arnaud Joly
    
*   112 Jaques Grobler
    
*   109 Gael Varoquaux
    
*   107 Olivier Grisel
    
*   102 Noel Dawe
    
*   99 Kemal Eren
    
*   79 Joel Nothman
    
*   75 Jake VanderPlas
    
*   73 Nelle Varoquaux
    
*   71 Vlad Niculae
    
*   65 Peter Prettenhofer
    
*   64 Alexandre Gramfort
    
*   54 Mathieu Blondel
    
*   38 Nicolas Trésegnie
    
*   35 eustache
    
*   27 Denis Engemann
    
*   25 Yann N. Dauphin
    
*   19 Justin Vincent
    
*   17 Robert Layton
    
*   15 Doug Coleman
    
*   14 Michael Eickenberg
    
*   13 Robert Marchman
    
*   11 Fabian Pedregosa
    
*   11 Philippe Gervais
    
*   10 Jim Holmström
    
*   10 Tadej Janež
    
*   10 syhw
    
*   9 Mikhail Korobov
    
*   9 Steven De Gryze
    
*   8 sergeyf
    
*   7 Ben Root
    
*   7 Hrishikesh Huilgolkar
    
*   6 Kyle Kastner
    
*   6 Martin Luessi
    
*   6 Rob Speer
    
*   5 Federico Vaggi
    
*   5 Raul Garreta
    
*   5 Rob Zinkov
    
*   4 Ken Geis
    
*   3 A. Flaxman
    
*   3 Denton Cockburn
    
*   3 Dougal Sutherland
    
*   3 Ian Ozsvald
    
*   3 Johannes Schönberger
    
*   3 Robert McGibbon
    
*   3 Roman Sinayev
    
*   3 Szabo Roland
    
*   2 Diego Molla
    
*   2 Imran Haque
    
*   2 Jochen Wersdörfer
    
*   2 Sergey Karayev
    
*   2 Yannick Schwartz
    
*   2 jamestwebber
    
*   1 Abhijeet Kolhe
    
*   1 Alexander Fabisch
    
*   1 Bastiaan van den Berg
    
*   1 Benjamin Peterson
    
*   1 Daniel Velkov
    
*   1 Fazlul Shahriar
    
*   1 Felix Brockherde
    
*   1 Félix-Antoine Fortin
    
*   1 Harikrishnan S
    
*   1 Jack Hale
    
*   1 JakeMick
    
*   1 James McDermott
    
*   1 John Benediktsson
    
*   1 John Zwinck
    
*   1 Joshua Vredevoogd
    
*   1 Justin Pati
    
*   1 Kevin Hughes
    
*   1 Kyle Kelley
    
*   1 Matthias Ekman
    
*   1 Miroslav Shubernetskiy
    
*   1 Naoki Orii
    
*   1 Norbert Crombach
    
*   1 Rafael Cunha de Almeida
    
*   1 Rolando Espinoza La fuente
    
*   1 Seamus Abshere
    
*   1 Sergey Feldman
    
*   1 Sergio Medina
    
*   1 Stefano Lattarini
    
*   1 Steve Koch
    
*   1 Sturla Molden
    
*   1 Thomas Jarosch
    
*   1 Yaroslav Halchenko
    

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)