[Skip to main content](https://scikit-learn.org/stable/whats_new/v0.17.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v0.17.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v0.17.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v0.17.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v0.17.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v0.17.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v0.17.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v0.17.html)

Collapse Sidebar Expand Sidebar

Version 0.17[#](https://scikit-learn.org/stable/whats_new/v0.17.html#version-0-17 "Link to this heading")

==========================================================================================================

Version 0.17.1[#](https://scikit-learn.org/stable/whats_new/v0.17.html#version-0-17-1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**February 18, 2016**

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.17.html#changelog "Link to this heading")

#### Bug fixes[#](https://scikit-learn.org/stable/whats_new/v0.17.html#bug-fixes "Link to this heading")

*   Upgrade vendored joblib to version 0.9.4 that fixes an important bug in `joblib.Parallel` that can silently yield to wrong results when working on datasets larger than 1MB: [joblib/joblib](https://github.com/joblib/joblib/blob/0.9.4/CHANGES.rst)
    
*   Fixed reading of Bunch pickles generated with scikit-learn version <= 0.16. This can affect users who have already downloaded a dataset with scikit-learn 0.16 and are loading it with scikit-learn 0.17. See [#6196](https://github.com/scikit-learn/scikit-learn/issues/6196)
     for how this affected [`datasets.fetch_20newsgroups`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
    . By [Loic Esteve](https://github.com/lesteve)
    .
    
*   Fixed a bug that prevented using ROC AUC score to perform grid search on several CPU / cores on large arrays. See [#6147](https://github.com/scikit-learn/scikit-learn/issues/6147)
     By [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Fixed a bug that prevented to properly set the `presort` parameter in [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
    . See [#5857](https://github.com/scikit-learn/scikit-learn/issues/5857)
     By Andrew McCulloh.
    
*   Fixed a joblib error when evaluating the perplexity of a [`decomposition.LatentDirichletAllocation`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "sklearn.decomposition.LatentDirichletAllocation")
     model. See [#6258](https://github.com/scikit-learn/scikit-learn/issues/6258)
     By Chyi-Kwei Yau.
    

Version 0.17[#](https://scikit-learn.org/stable/whats_new/v0.17.html#changes-0-17 "Link to this heading")

----------------------------------------------------------------------------------------------------------

**November 5, 2015**

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.17.html#id2 "Link to this heading")

#### New features[#](https://scikit-learn.org/stable/whats_new/v0.17.html#new-features "Link to this heading")

*   All the Scaler classes but [`preprocessing.RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
     can be fitted online by calling `partial_fit`. By [Giorgio Patrini](https://github.com/giorgiop)
    .
    
*   The new class [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     implements a “majority rule” / “soft voting” ensemble classifier to combine estimators for classification. By [Sebastian Raschka](https://sebastianraschka.com/)
    .
    
*   The new class [`preprocessing.RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
     provides an alternative to [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
     for feature-wise centering and range normalization that is robust to outliers. By [Thomas Unterthiner](https://github.com/untom)
    .
    
*   The new class [`preprocessing.MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")
     provides an alternative to [`preprocessing.MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
     for feature-wise range normalization when the data is already centered or sparse. By [Thomas Unterthiner](https://github.com/untom)
    .
    
*   The new class [`preprocessing.FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
     turns a Python function into a `Pipeline`\-compatible transformer object. By Joe Jevnik.
    
*   The new classes `cross_validation.LabelKFold` and `cross_validation.LabelShuffleSplit` generate train-test folds, respectively similar to `cross_validation.KFold` and `cross_validation.ShuffleSplit`, except that the folds are conditioned on a label array. By [Brian McFee](https://bmcfee.github.io/)
    , [Jean Kossaifi](https://github.com/JeanKossaifi)
     and [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   [`decomposition.LatentDirichletAllocation`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "sklearn.decomposition.LatentDirichletAllocation")
     implements the Latent Dirichlet Allocation topic model with online variational inference. By [Chyi-Kwei Yau](https://github.com/chyikwei)
    , with code based on an implementation by Matt Hoffman. ([#3659](https://github.com/scikit-learn/scikit-learn/issues/3659)
    )
    
*   The new solver `sag` implements a Stochastic Average Gradient descent and is available in both [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    . This solver is very efficient for large datasets. By [Danny Sullivan](https://github.com/dsullivan7)
     and [Tom Dupre la Tour](https://github.com/TomDLT)
    . ([#4738](https://github.com/scikit-learn/scikit-learn/issues/4738)
    )
    
*   The new solver `cd` implements a Coordinate Descent in [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
    . Previous solver based on Projected Gradient is still available setting new parameter `solver` to `pg`, but is deprecated and will be removed in 0.19, along with `decomposition.ProjectedGradientNMF` and parameters `sparseness`, `eta`, `beta` and `nls_max_iter`. New parameters `alpha` and `l1_ratio` control L1 and L2 regularization, and `shuffle` adds a shuffling step in the `cd` solver. By [Tom Dupre la Tour](https://github.com/TomDLT)
     and [Mathieu Blondel](http://www.mblondel.org/)
    .
    

#### Enhancements[#](https://scikit-learn.org/stable/whats_new/v0.17.html#enhancements "Link to this heading")

*   [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     now supports approximate optimization via the Barnes-Hut method, leading to much faster fitting. By Christopher Erick Moody. ([#4025](https://github.com/scikit-learn/scikit-learn/issues/4025)
    )
    
*   [`cluster.MeanShift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")
     now supports parallel execution, as implemented in the `mean_shift` function. By [Martino Sorbaro](https://github.com/martinosorb)
    .
    
*   [`naive_bayes.GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
     now supports fitting with `sample_weight`. By [Jan Hendrik Metzen](https://jmetzen.github.io/)
    .
    
*   [`dummy.DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
     now supports a prior fitting strategy. By [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Added a `fit_predict` method for `mixture.GMM` and subclasses. By [Cory Lorenz](https://github.com/clorenz7)
    .
    
*   Added the [`metrics.label_ranking_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_loss.html#sklearn.metrics.label_ranking_loss "sklearn.metrics.label_ranking_loss")
     metric. By [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   Added the [`metrics.cohen_kappa_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#sklearn.metrics.cohen_kappa_score "sklearn.metrics.cohen_kappa_score")
     metric.
    
*   Added a `warm_start` constructor parameter to the bagging ensemble models to increase the size of the ensemble. By [Tim Head](https://github.com/betatim)
    .
    
*   Added option to use multi-output regression metrics without averaging. By Konstantin Shmelkov and [Michael Eickenberg](https://github.com/eickenberg)
    .
    
*   Added `stratify` option to `cross_validation.train_test_split` for stratified splitting. By Miroslav Batchkarov.
    
*   The [`tree.export_graphviz`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz "sklearn.tree.export_graphviz")
     function now supports aesthetic improvements for [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
     and [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , including options for coloring nodes by their majority class or impurity, showing variable names, and using node proportions instead of raw sample counts. By [Trevor Stephens](https://trevorstephens.com/)
    .
    
*   Improved speed of `newton-cg` solver in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    , by avoiding loss computation. By [Mathieu Blondel](http://www.mblondel.org/)
     and [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   The `class_weight="auto"` heuristic in classifiers supporting `class_weight` was deprecated and replaced by the `class_weight="balanced"` option, which has a simpler formula and interpretation. By [Hanna Wallach](https://dirichlet.net/)
     and [Andreas Müller](https://amueller.github.io/)
    .
    
*   Add `class_weight` parameter to automatically weight samples by class frequency for [`linear_model.PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier")
    . By [Trevor Stephens](https://trevorstephens.com/)
    .
    
*   Added backlinks from the API reference pages to the user guide. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   The `labels` parameter to [`sklearn.metrics.f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")
    , [`sklearn.metrics.fbeta_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#sklearn.metrics.fbeta_score "sklearn.metrics.fbeta_score")
    , [`sklearn.metrics.recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")
     and [`sklearn.metrics.precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")
     has been extended. It is now possible to ignore one or more labels, such as where a multiclass problem has a majority class to ignore. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   Add `sample_weight` support to [`linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
    . By [Trevor Stephens](https://trevorstephens.com/)
    .
    
*   Provide an option for sparse output from [`sklearn.metrics.pairwise.cosine_similarity`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#sklearn.metrics.pairwise.cosine_similarity "sklearn.metrics.pairwise.cosine_similarity")
    . By [Jaidev Deshpande](https://github.com/jaidevd)
    .
    
*   Add [`preprocessing.minmax_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html#sklearn.preprocessing.minmax_scale "sklearn.preprocessing.minmax_scale")
     to provide a function interface for [`preprocessing.MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
    . By [Thomas Unterthiner](https://github.com/untom)
    .
    
*   `dump_svmlight_file` now handles multi-label datasets. By Chih-Wei Chang.
    
*   RCV1 dataset loader ([`sklearn.datasets.fetch_rcv1`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_rcv1.html#sklearn.datasets.fetch_rcv1 "sklearn.datasets.fetch_rcv1")
    ). By [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   The “Wisconsin Breast Cancer” classical two-class classification dataset is now included in scikit-learn, available with [`datasets.load_breast_cancer`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer "sklearn.datasets.load_breast_cancer")
    .
    
*   Upgraded to joblib 0.9.3 to benefit from the new automatic batching of short tasks. This makes it possible for scikit-learn to benefit from parallelism when many very short tasks are executed in parallel, for instance by the `grid_search.GridSearchCV` meta-estimator with `n_jobs > 1` used with a large grid of parameters on a small dataset. By [Vlad Niculae](https://vene.ro/)
    , [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
     and [Loic Esteve](https://github.com/lesteve)
    .
    
*   For more details about changes in joblib 0.9.3 see the release notes: [joblib/joblib](https://github.com/joblib/joblib/blob/master/CHANGES.rst#release-093)
    
*   Improved speed (3 times per iteration) of `decomposition.DictLearning` with coordinate descent method from [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
    . By [Arthur Mensch](https://github.com/arthurmensch)
    .
    
*   Parallel processing (threaded) for queries of nearest neighbors (using the ball-tree) by Nikolay Mayorov.
    
*   Allow [`datasets.make_multilabel_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "sklearn.datasets.make_multilabel_classification")
     to output a sparse `y`. By Kashif Rasul.
    
*   [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
     now accepts a sparse matrix of precomputed distances, allowing memory-efficient distance precomputation. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
     now exposes an `apply` method for retrieving the leaf indices samples are predicted as. By [Daniel Galvez](https://github.com/galv)
     and [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   Speed up decision tree regressors, random forest regressors, extra trees regressors and gradient boosting estimators by computing a proxy of the impurity improvement during the tree growth. The proxy quantity is such that the split that maximizes this value also maximizes the impurity improvement. By [Arnaud Joly](http://www.ajoly.org/)
    , [Jacob Schreiber](https://github.com/jmschrei)
     and [Gilles Louppe](https://www.montefiore.ulg.ac.be/~glouppe/)
    .
    
*   Speed up tree based methods by reducing the number of computations needed when computing the impurity measure taking into account linear relationship of the computed statistics. The effect is particularly visible with extra trees and on datasets with categorical or sparse features. By [Arnaud Joly](http://www.ajoly.org/)
    .
    
*   [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     and [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     now expose an `apply` method for retrieving the leaf indices each sample ends up in under each try. By [Jacob Schreiber](https://github.com/jmschrei)
    .
    
*   Add `sample_weight` support to [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
    . By Sonny Hu. ([##4881](https://github.com/scikit-learn/scikit-learn/issues/#4881)
    )
    
*   Add `n_iter_without_progress` to [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     to control the stopping criterion. By Santi Villalba. ([#5186](https://github.com/scikit-learn/scikit-learn/issues/5186)
    )
    
*   Added optional parameter `random_state` in [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     , to set the seed of the pseudo random generator used in `sag` solver. By [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Added optional parameter `warm_start` in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    . If set to True, the solvers `lbfgs`, `newton-cg` and `sag` will be initialized with the coefficients computed in the previous fit. By [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Added `sample_weight` support to [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     for the `lbfgs`, `newton-cg`, and `sag` solvers. By [Valentin Stolbunov](http://www.vstolbunov.com/)
    . Support added to the `liblinear` solver. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Added optional parameter `presort` to [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     and [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
    , keeping default behavior the same. This allows gradient boosters to turn off presorting when building deep trees or using sparse data. By [Jacob Schreiber](https://github.com/jmschrei)
    .
    
*   Altered [`metrics.roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
     to drop unnecessary thresholds by default. By [Graham Clenaghan](https://github.com/gclenaghan)
    .
    
*   Added [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
     meta-transformer which can be used along with estimators that have `coef_` or `feature_importances_` attribute to select important features of the input data. By [Maheshakya Wijewardena](https://github.com/maheshakya)
    , [Joel Nothman](https://joelnothman.com/)
     and [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Added [`metrics.pairwise.laplacian_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html#sklearn.metrics.pairwise.laplacian_kernel "sklearn.metrics.pairwise.laplacian_kernel")
    . By [Clyde Fare](https://github.com/Clyde-fare)
    .
    
*   `covariance.GraphLasso` allows separate control of the convergence criterion for the Elastic-Net subproblem via the `enet_tol` parameter.
    
*   Improved verbosity in [`decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
    .
    
*   [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
     and [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
     no longer explicitly store the samples used in bagging, resulting in a much reduced memory footprint for storing random forest models.
    
*   Added `positive` option to [`linear_model.Lars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html#sklearn.linear_model.Lars "sklearn.linear_model.Lars")
     and [`linear_model.lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")
     to force coefficients to be positive. ([#5131](https://github.com/scikit-learn/scikit-learn/issues/5131)
    )
    
*   Added the `X_norm_squared` parameter to [`metrics.pairwise.euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html#sklearn.metrics.pairwise.euclidean_distances "sklearn.metrics.pairwise.euclidean_distances")
     to provide precomputed squared norms for `X`.
    
*   Added the `fit_predict` method to [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
    .
    
*   Added the [`preprocessing.minmax_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html#sklearn.preprocessing.minmax_scale "sklearn.preprocessing.minmax_scale")
     function.
    

#### Bug fixes[#](https://scikit-learn.org/stable/whats_new/v0.17.html#id3 "Link to this heading")

*   Fixed non-determinism in [`dummy.DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
     with sparse multi-label output. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   Fixed the output shape of [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
     to `(n_samples, )`. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   Fixed bug in `decomposition.DictLearning` when `n_jobs < 0`. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   Fixed bug where `grid_search.RandomizedSearchCV` could consume a lot of memory for large discrete grids. By [Joel Nothman](https://joelnothman.com/)
    .
    
*   Fixed bug in [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     where `penalty` was ignored in the final fit. By [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    
*   Fixed bug in `ensemble.forest.ForestClassifier` while computing oob\_score and X is a sparse.csc\_matrix. By [Ankur Ankan](https://github.com/ankurankan)
    .
    
*   All regressors now consistently handle and warn when given `y` that is of shape `(n_samples, 1)`. By [Andreas Müller](https://amueller.github.io/)
     and Henry Lin. ([#5431](https://github.com/scikit-learn/scikit-learn/issues/5431)
    )
    
*   Fix in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     cluster reassignment for sparse input by [Lars Buitinck](https://github.com/larsmans)
    .
    
*   Fixed a bug in [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     that could cause asymmetric covariance matrices when using shrinkage. By [Martin Billinger](https://tnsre.embs.org/author/martinbillinger/)
    .
    
*   Fixed `cross_validation.cross_val_predict` for estimators with sparse predictions. By Buddha Prakash.
    
*   Fixed the `predict_proba` method of [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     to use soft-max instead of one-vs-rest normalization. By [Manoj Kumar](https://manojbits.wordpress.com/)
    . ([#5182](https://github.com/scikit-learn/scikit-learn/issues/5182)
    )
    
*   Fixed the `partial_fit` method of [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     when called with `average=True`. By [Andrew Lamb](https://github.com/andylamb)
    . ([#5282](https://github.com/scikit-learn/scikit-learn/issues/5282)
    )
    
*   Dataset fetchers use different filenames under Python 2 and Python 3 to avoid pickling compatibility issues. By [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    . ([#5355](https://github.com/scikit-learn/scikit-learn/issues/5355)
    )
    
*   Fixed a bug in [`naive_bayes.GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
     which caused classification results to depend on scale. By [Jake Vanderplas](https://staff.washington.edu/jakevdp/)
    .
    
*   Fixed temporarily [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    , which was incorrect when fitting the intercept in the case of sparse data. The fix automatically changes the solver to ‘sag’ in this case. [#5360](https://github.com/scikit-learn/scikit-learn/issues/5360)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Fixed a performance bug in `decomposition.RandomizedPCA` on data with a large number of features and fewer samples. ([#4478](https://github.com/scikit-learn/scikit-learn/issues/4478)
    ) By [Andreas Müller](https://amueller.github.io/)
    , [Loic Esteve](https://github.com/lesteve)
     and [Giorgio Patrini](https://github.com/giorgiop)
    .
    
*   Fixed bug in `cross_decomposition.PLS` that yielded unstable and platform dependent output, and failed on `fit_transform`. By [Arthur Mensch](https://github.com/arthurmensch)
    .
    
*   Fixes to the `Bunch` class used to store datasets.
    
*   Fixed `ensemble.plot_partial_dependence` ignoring the `percentiles` parameter.
    
*   Providing a `set` as vocabulary in `CountVectorizer` no longer leads to inconsistent results when pickling.
    
*   Fixed the conditions on when a precomputed Gram matrix needs to be recomputed in [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
    , [`linear_model.OrthogonalMatchingPursuit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html#sklearn.linear_model.OrthogonalMatchingPursuit "sklearn.linear_model.OrthogonalMatchingPursuit")
    , [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     and [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
    .
    
*   Fixed inconsistent memory layout in the coordinate descent solver that affected `linear_model.DictionaryLearning` and `covariance.GraphLasso`. ([#5337](https://github.com/scikit-learn/scikit-learn/issues/5337)
    ) By [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   [`manifold.LocallyLinearEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
     no longer ignores the `reg` parameter.
    
*   Nearest Neighbor estimators with custom distance metrics can now be pickled. ([#4362](https://github.com/scikit-learn/scikit-learn/issues/4362)
    )
    
*   Fixed a bug in [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     where `transformer_weights` were not properly handled when performing grid-searches.
    
*   Fixed a bug in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     when using `class_weight='balanced'` or `class_weight='auto'`. By [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Fixed bug [#5495](https://github.com/scikit-learn/scikit-learn/issues/5495)
     when doing OVR(SVC(decision\_function\_shape=”ovr”)). Fixed by [Elvis Dohmatob](https://github.com/dohmatob)
    .
    

### API changes summary[#](https://scikit-learn.org/stable/whats_new/v0.17.html#api-changes-summary "Link to this heading")

*   Attribute `data_min`, `data_max` and `data_range` in [`preprocessing.MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
     are deprecated and won’t be available from 0.19. Instead, the class now exposes `data_min_`, `data_max_` and `data_range_`. By [Giorgio Patrini](https://github.com/giorgiop)
    .
    
*   All Scaler classes now have an `scale_` attribute, the feature-wise rescaling applied by their `transform` methods. The old attribute `std_` in [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
     is deprecated and superseded by `scale_`; it won’t be available in 0.19. By [Giorgio Patrini](https://github.com/giorgiop)
    .
    
*   [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     and [`svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
     now have an `decision_function_shape` parameter to make their decision function of shape `(n_samples, n_classes)` by setting `decision_function_shape='ovr'`. This will be the default behavior starting in 0.19. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   Passing 1D data arrays as input to estimators is now deprecated as it caused confusion in how the array elements should be interpreted as features or as samples. All data arrays are now expected to be explicitly shaped `(n_samples, n_features)`. By [Vighnesh Birodkar](https://github.com/vighneshbirodkar)
    .
    
*   `lda.LDA` and `qda.QDA` have been moved to [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     and [`discriminant_analysis.QuadraticDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis "sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis")
    .
    
*   The `store_covariance` and `tol` parameters have been moved from the fit method to the constructor in [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     and the `store_covariances` and `tol` parameters have been moved from the fit method to the constructor in [`discriminant_analysis.QuadraticDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis "sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis")
    .
    
*   Models inheriting from `_LearntSelectorMixin` will no longer support the transform methods. (i.e, RandomForests, GradientBoosting, LogisticRegression, DecisionTrees, SVMs and SGD related models). Wrap these models around the metatransfomer [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
     to remove features (according to `coefs_` or `feature_importances_`) which are below a certain threshold value instead.
    
*   [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     re-runs cluster-assignments in case of non-convergence, to ensure consistency of `predict(X)` and `labels_`. By [Vighnesh Birodkar](https://github.com/vighneshbirodkar)
    .
    
*   Classifier and Regressor models are now tagged as such using the `_estimator_type` attribute.
    
*   Cross-validation iterators always provide indices into training and test set, not boolean masks.
    
*   The `decision_function` on all regressors was deprecated and will be removed in 0.19. Use `predict` instead.
    
*   `datasets.load_lfw_pairs` is deprecated and will be removed in 0.19. Use [`datasets.fetch_lfw_pairs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_pairs.html#sklearn.datasets.fetch_lfw_pairs "sklearn.datasets.fetch_lfw_pairs")
     instead.
    
*   The deprecated `hmm` module was removed.
    
*   The deprecated `Bootstrap` cross-validation iterator was removed.
    
*   The deprecated `Ward` and `WardAgglomerative` classes have been removed. Use [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     instead.
    
*   `cross_validation.check_cv` is now a public function.
    
*   The property `residues_` of [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
     is deprecated and will be removed in 0.19.
    
*   The deprecated `n_jobs` parameter of [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
     has been moved to the constructor.
    
*   Removed deprecated `class_weight` parameter from [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    ’s `fit` method. Use the construction parameter instead.
    
*   The deprecated support for the sequence of sequences (or list of lists) multilabel format was removed. To convert to and from the supported binary indicator matrix format, use [`MultiLabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer "sklearn.preprocessing.MultiLabelBinarizer")
    .
    
*   The behavior of calling the `inverse_transform` method of `Pipeline.pipeline` will change in 0.19. It will no longer reshape one-dimensional input to two-dimensional input.
    
*   The deprecated attributes `indicator_matrix_`, `multilabel_` and `classes_` of [`preprocessing.LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
     were removed.
    
*   Using `gamma=0` in [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     and [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
     to automatically set the gamma to `1. / n_features` is deprecated and will be removed in 0.19. Use `gamma="auto"` instead.
    

### Code Contributors[#](https://scikit-learn.org/stable/whats_new/v0.17.html#code-contributors "Link to this heading")

Aaron Schumacher, Adithya Ganesh, akitty, Alexandre Gramfort, Alexey Grigorev, Ali Baharev, Allen Riddell, Ando Saabas, Andreas Mueller, Andrew Lamb, Anish Shah, Ankur Ankan, Anthony Erlinger, Ari Rouvinen, Arnaud Joly, Arnaud Rachez, Arthur Mensch, banilo, Barmaley.exe, benjaminirving, Boyuan Deng, Brett Naul, Brian McFee, Buddha Prakash, Chi Zhang, Chih-Wei Chang, Christof Angermueller, Christoph Gohlke, Christophe Bourguignat, Christopher Erick Moody, Chyi-Kwei Yau, Cindy Sridharan, CJ Carey, Clyde-fare, Cory Lorenz, Dan Blanchard, Daniel Galvez, Daniel Kronovet, Danny Sullivan, Data1010, David, David D Lowe, David Dotson, djipey, Dmitry Spikhalskiy, Donne Martin, Dougal J. Sutherland, Dougal Sutherland, edson duarte, Eduardo Caro, Eric Larson, Eric Martin, Erich Schubert, Fernando Carrillo, Frank C. Eckert, Frank Zalkow, Gael Varoquaux, Ganiev Ibraim, Gilles Louppe, Giorgio Patrini, giorgiop, Graham Clenaghan, Gryllos Prokopis, gwulfs, Henry Lin, Hsuan-Tien Lin, Immanuel Bayer, Ishank Gulati, Jack Martin, Jacob Schreiber, Jaidev Deshpande, Jake Vanderplas, Jan Hendrik Metzen, Jean Kossaifi, Jeffrey04, Jeremy, jfraj, Jiali Mei, Joe Jevnik, Joel Nothman, John Kirkham, John Wittenauer, Joseph, Joshua Loyal, Jungkook Park, KamalakerDadi, Kashif Rasul, Keith Goodman, Kian Ho, Konstantin Shmelkov, Kyler Brown, Lars Buitinck, Lilian Besson, Loic Esteve, Louis Tiao, maheshakya, Maheshakya Wijewardena, Manoj Kumar, MarkTab marktab.net, Martin Ku, Martin Spacek, MartinBpr, martinosorb, MaryanMorel, Masafumi Oyamada, Mathieu Blondel, Matt Krump, Matti Lyra, Maxim Kolganov, mbillinger, mhg, Michael Heilman, Michael Patterson, Miroslav Batchkarov, Nelle Varoquaux, Nicolas, Nikolay Mayorov, Olivier Grisel, Omer Katz, Óscar Nájera, Pauli Virtanen, Peter Fischer, Peter Prettenhofer, Phil Roth, pianomania, Preston Parry, Raghav RV, Rob Zinkov, Robert Layton, Rohan Ramanath, Saket Choudhary, Sam Zhang, santi, saurabh.bansod, scls19fr, Sebastian Raschka, Sebastian Saeger, Shivan Sornarajah, SimonPL, sinhrks, Skipper Seabold, Sonny Hu, sseg, Stephen Hoover, Steven De Gryze, Steven Seguin, Theodore Vasiloudis, Thomas Unterthiner, Tiago Freitas Pereira, Tian Wang, Tim Head, Timothy Hopper, tokoroten, Tom Dupré la Tour, Trevor Stephens, Valentin Stolbunov, Vighnesh Birodkar, Vinayak Mehta, Vincent, Vincent Michel, vstolbunov, wangz10, Wei Xue, Yucheng Low, Yury Zhauniarovich, Zac Stewart, zhai\_pro, Zichen Wang

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)