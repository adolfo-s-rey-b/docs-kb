[Skip to main content](https://scikit-learn.org/stable/whats_new/v0.19.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v0.19.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v0.19.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v0.19.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v0.19.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v0.19.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v0.19.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v0.19.html)

Collapse Sidebar Expand Sidebar

Version 0.19[#](https://scikit-learn.org/stable/whats_new/v0.19.html#version-0-19 "Link to this heading")

==========================================================================================================

Version 0.19.2[#](https://scikit-learn.org/stable/whats_new/v0.19.html#version-0-19-2 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**July, 2018**

This release is exclusively in order to support Python 3.7.

### Related changes[#](https://scikit-learn.org/stable/whats_new/v0.19.html#related-changes "Link to this heading")

*   `n_iter_` may vary from previous releases in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     with `solver='lbfgs'` and [`linear_model.HuberRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor")
    . For Scipy <= 1.0.0, the optimizer could perform more than the requested maximum number of iterations. Now both estimators will report at most `max_iter` iterations even if more were performed. [#10723](https://github.com/scikit-learn/scikit-learn/issues/10723)
     by [Joel Nothman](https://joelnothman.com/)
    .
    

Version 0.19.1[#](https://scikit-learn.org/stable/whats_new/v0.19.html#version-0-19-1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**October 23, 2017**

This is a bug-fix release with some minor documentation improvements and enhancements to features released in 0.19.0.

Note there may be minor differences in TSNE output in this release (due to [#9623](https://github.com/scikit-learn/scikit-learn/issues/9623)
), in the case where multiple samples have equal distance to some sample.

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.19.html#changelog "Link to this heading")

#### API changes[#](https://scikit-learn.org/stable/whats_new/v0.19.html#api-changes "Link to this heading")

*   Reverted the addition of `metrics.ndcg_score` and `metrics.dcg_score` which had been merged into version 0.19.0 by error. The implementations were broken and undocumented.
    
*   `return_train_score` which was added to [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    , [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     and [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
     in version 0.19.0 will be changing its default value from True to False in version 0.21. We found that calculating training score could have a great effect on cross validation runtime in some cases. Users should explicitly set `return_train_score` to False if prediction or scoring functions are slow, resulting in a deleterious effect on CV runtime, or to True if they wish to use the calculated scores. [#9677](https://github.com/scikit-learn/scikit-learn/issues/9677)
     by [Kumar Ashutosh](https://github.com/thechargedneutron)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   `correlation_models` and `regression_models` from the legacy gaussian processes implementation have been belatedly deprecated. [#9717](https://github.com/scikit-learn/scikit-learn/issues/9717)
     by [Kumar Ashutosh](https://github.com/thechargedneutron)
    .
    

#### Bug fixes[#](https://scikit-learn.org/stable/whats_new/v0.19.html#bug-fixes "Link to this heading")

*   Avoid integer overflows in [`metrics.matthews_corrcoef`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html#sklearn.metrics.matthews_corrcoef "sklearn.metrics.matthews_corrcoef")
    . [#9693](https://github.com/scikit-learn/scikit-learn/issues/9693)
     by [Sam Steingold](https://github.com/sam-s)
    .
    
*   Fixed a bug in the objective function for [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     (both exact and with the Barnes-Hut approximation) when `n_components >= 3`. [#9711](https://github.com/scikit-learn/scikit-learn/issues/9711)
     by [@goncalo-rodrigues](https://github.com/goncalo-rodrigues)
    .
    
*   Fix regression in [`model_selection.cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
     where it raised an error with `method='predict_proba'` for some probabilistic classifiers. [#9641](https://github.com/scikit-learn/scikit-learn/issues/9641)
     by [James Bourbeau](https://github.com/jrbourbeau)
    .
    
*   Fixed a bug where [`datasets.make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
     modified its input `weights`. [#9865](https://github.com/scikit-learn/scikit-learn/issues/9865)
     by [Sachin Kelkar](https://github.com/s4chin)
    .
    
*   [`model_selection.StratifiedShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")
     now works with multioutput multiclass or multilabel data with more than 1000 columns. [#9922](https://github.com/scikit-learn/scikit-learn/issues/9922)
     by [Charlie Brummitt](https://github.com/crbrummitt)
    .
    
*   Fixed a bug with nested and conditional parameter setting, e.g. setting a pipeline step and its parameter at the same time. [#9945](https://github.com/scikit-learn/scikit-learn/issues/9945)
     by [Andreas Müller](https://amueller.github.io/)
     and [Joel Nothman](https://joelnothman.com/)
    .
    

Regressions in 0.19.0 fixed in 0.19.1:

*   Fixed a bug where parallelised prediction in random forests was not thread-safe and could (rarely) result in arbitrary errors. [#9830](https://github.com/scikit-learn/scikit-learn/issues/9830)
     by [Joel Nothman](https://joelnothman.com/)
    .
    
*   Fix regression in [`model_selection.cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
     where it no longer accepted `X` as a list. [#9600](https://github.com/scikit-learn/scikit-learn/issues/9600)
     by [Rasul Kerimov](https://github.com/CoderINusE)
    .
    
*   Fixed handling of [`model_selection.cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
     for binary classification with `method='decision_function'`. [#9593](https://github.com/scikit-learn/scikit-learn/issues/9593)
     by [Reiichiro Nakano](https://github.com/reiinakano)
     and core devs.
    
*   Fix regression in [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     where it no longer accepted `steps` as a tuple. [#9604](https://github.com/scikit-learn/scikit-learn/issues/9604)
     by [Joris Van den Bossche](https://github.com/jorisvandenbossche)
    .
    
*   Fix bug where `n_iter` was not properly deprecated, leaving `n_iter` unavailable for interim use in [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    , [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
    , [`linear_model.PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier")
    , [`linear_model.PassiveAggressiveRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model.PassiveAggressiveRegressor")
     and [`linear_model.Perceptron`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron")
    . [#9558](https://github.com/scikit-learn/scikit-learn/issues/9558)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Dataset fetchers make sure temporary files are closed before removing them, which caused errors on Windows. [#9847](https://github.com/scikit-learn/scikit-learn/issues/9847)
     by [Joan Massich](https://github.com/massich)
    .
    
*   Fixed a regression in [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     where it no longer supported metrics other than ‘euclidean’ and ‘precomputed’. [#9623](https://github.com/scikit-learn/scikit-learn/issues/9623)
     by [Oli Blum](https://github.com/oliblum90)
    .
    

#### Enhancements[#](https://scikit-learn.org/stable/whats_new/v0.19.html#enhancements "Link to this heading")

*   Our test suite and [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     can now be run without Nose installed. [#9697](https://github.com/scikit-learn/scikit-learn/issues/9697)
     by [Joan Massich](https://github.com/massich)
    .
    
*   To improve usability of version 0.19’s [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     caching, `memory` now allows `joblib.Memory` instances. This make use of the new [`utils.validation.check_memory`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_memory.html#sklearn.utils.validation.check_memory "sklearn.utils.validation.check_memory")
     helper. [#9584](https://github.com/scikit-learn/scikit-learn/issues/9584)
     by [Kumar Ashutosh](https://github.com/thechargedneutron)
    
*   Some fixes to examples: [#9750](https://github.com/scikit-learn/scikit-learn/issues/9750)
    , [#9788](https://github.com/scikit-learn/scikit-learn/issues/9788)
    , [#9815](https://github.com/scikit-learn/scikit-learn/issues/9815)
    
*   Made a FutureWarning in SGD-based estimators less verbose. [#9802](https://github.com/scikit-learn/scikit-learn/issues/9802)
     by [Vrishank Bhardwaj](https://github.com/vrishank97)
    .
    

### Code and Documentation Contributors[#](https://scikit-learn.org/stable/whats_new/v0.19.html#code-and-documentation-contributors "Link to this heading")

With thanks to:

Joel Nothman, Loic Esteve, Andreas Mueller, Kumar Ashutosh, Vrishank Bhardwaj, Hanmin Qin, Rasul Kerimov, James Bourbeau, Nagarjuna Kumar, Nathaniel Saul, Olivier Grisel, Roman Yurchak, Reiichiro Nakano, Sachin Kelkar, Sam Steingold, Yaroslav Halchenko, diegodlh, felix, goncalo-rodrigues, jkleint, oliblum90, pasbi, Anthony Gitter, Ben Lawson, Charlie Brummitt, Didi Bar-Zev, Gael Varoquaux, Joan Massich, Joris Van den Bossche, nielsenmarkus11

Version 0.19[#](https://scikit-learn.org/stable/whats_new/v0.19.html#id1 "Link to this heading")

-------------------------------------------------------------------------------------------------

**August 12, 2017**

### Highlights[#](https://scikit-learn.org/stable/whats_new/v0.19.html#highlights "Link to this heading")

We are excited to release a number of great new features including [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
 for anomaly detection, [`preprocessing.QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
 for robust feature transformation, and the [`multioutput.ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
 meta-estimator to simply account for dependencies between classes in multilabel problems. We have some new algorithms in existing estimators, such as multiplicative update in [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
 and multinomial [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 with L1 loss (use `solver='saga'`).

Cross validation is now able to return the results from multiple metric evaluations. The new [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
 can return many scores on the test data as well as training set performance and timings, and we have extended the `scoring` and `refit` parameters for grid/randomized search [to handle multiple metrics](https://scikit-learn.org/stable/modules/grid_search.html#multimetric-grid-search)
.

You can also learn faster. For instance, the [new option to cache transformations](https://scikit-learn.org/stable/modules/compose.html#pipeline-cache)
 in [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 makes grid search over pipelines including slow transformations much more efficient. And you can predict faster: if you’re sure you know what you’re doing, you can turn off validating that the input is finite using [`config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context")
.

We’ve made some important fixes too. We’ve fixed a longstanding implementation error in [`metrics.average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
, so please be cautious with prior results reported from that function. A number of errors in the [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
 implementation have been fixed, particularly in the default Barnes-Hut approximation. [`semi_supervised.LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
 and [`semi_supervised.LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")
 have had substantial fixes. LabelPropagation was previously broken. LabelSpreading should now correctly respect its alpha parameter.

### Changed models[#](https://scikit-learn.org/stable/whats_new/v0.19.html#changed-models "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     with sparse X and initial centroids given (bug fix)
    
*   [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
     with `scale=True` (bug fix)
    
*   [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     where `min_impurity_split` is used (bug fix)
    
*   gradient boosting `loss='quantile'` (bug fix)
    
*   [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     (bug fix)
    
*   [`feature_selection.SelectFdr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFdr.html#sklearn.feature_selection.SelectFdr "sklearn.feature_selection.SelectFdr")
     (bug fix)
    
*   [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
     (bug fix)
    
*   [`linear_model.LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")
     (bug fix)
    
*   [`linear_model.LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
     (bug fix)
    
*   [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     (bug fix)
    
*   [`neighbors.NearestCentroid`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")
     (bug fix)
    
*   [`semi_supervised.LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
     (bug fix)
    
*   [`semi_supervised.LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")
     (bug fix)
    
*   tree based models where `min_weight_fraction_leaf` is used (enhancement)
    
*   [`model_selection.StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
     with `shuffle=True` (this change, due to [#7823](https://github.com/scikit-learn/scikit-learn/issues/7823)
     was not mentioned in the release notes at the time)
    

Details are listed in the changelog below.

(While we are trying to better inform users by providing this information, we cannot assure that this list is complete.)

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.19.html#id2 "Link to this heading")

#### New features[#](https://scikit-learn.org/stable/whats_new/v0.19.html#new-features "Link to this heading")

Classifiers and regressors

*   Added [`multioutput.ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
     for multi-label classification. By [Adam Kleczewski](https://github.com/adamklec)
    .
    
*   Added solver `'saga'` that implements the improved version of Stochastic Average Gradient, in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    . It allows the use of L1 penalty with multinomial logistic loss, and behaves marginally better than ‘sag’ during the first epochs of ridge and logistic regression. [#8446](https://github.com/scikit-learn/scikit-learn/issues/8446)
     by [Arthur Mensch](https://amensch.fr/)
    .
    

Other estimators

*   Added the [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
     class for anomaly detection based on nearest neighbors. [#5279](https://github.com/scikit-learn/scikit-learn/issues/5279)
     by [Nicolas Goix](https://ngoix.github.io/)
     and [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   Added [`preprocessing.QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
     class and [`preprocessing.quantile_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#sklearn.preprocessing.quantile_transform "sklearn.preprocessing.quantile_transform")
     function for features normalization based on quantiles. [#8363](https://github.com/scikit-learn/scikit-learn/issues/8363)
     by [Denis Engemann](https://github.com/dengemann)
    , [Guillaume Lemaitre](https://github.com/glemaitre)
    , [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    , [Raghav RV](https://github.com/raghavrv)
    , [Thierry Guillemot](https://github.com/tguillemot)
    , and [Gael Varoquaux](https://gael-varoquaux.info/)
    .
    
*   The new solver `'mu'` implements a Multiplicate Update in [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
    , allowing the optimization of all beta-divergences, including the Frobenius norm, the generalized Kullback-Leibler divergence and the Itakura-Saito divergence. [#5295](https://github.com/scikit-learn/scikit-learn/issues/5295)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    

Model selection and evaluation

*   [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     now support simultaneous evaluation of multiple metrics. Refer to the [Specifying multiple metrics for evaluation](https://scikit-learn.org/stable/modules/grid_search.html#multimetric-grid-search)
     section of the user guide for more information. [#7388](https://github.com/scikit-learn/scikit-learn/issues/7388)
     by [Raghav RV](https://github.com/raghavrv)
    
*   Added the [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
     which allows evaluation of multiple metrics. This function returns a dict with more useful information from cross-validation such as the train scores, fit times and score times. Refer to [The cross\_validate function and multiple metric evaluation](https://scikit-learn.org/stable/modules/cross_validation.html#multimetric-cross-validation)
     section of the userguide for more information. [#7388](https://github.com/scikit-learn/scikit-learn/issues/7388)
     by [Raghav RV](https://github.com/raghavrv)
    
*   Added [`metrics.mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html#sklearn.metrics.mean_squared_log_error "sklearn.metrics.mean_squared_log_error")
    , which computes the mean square error of the logarithmic transformation of targets, particularly useful for targets with an exponential trend. [#7655](https://github.com/scikit-learn/scikit-learn/issues/7655)
     by [Karan Desai](https://github.com/karandesai-96)
    .
    
*   Added [`metrics.dcg_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.dcg_score.html#sklearn.metrics.dcg_score "sklearn.metrics.dcg_score")
     and [`metrics.ndcg_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html#sklearn.metrics.ndcg_score "sklearn.metrics.ndcg_score")
    , which compute Discounted cumulative gain (DCG) and Normalized discounted cumulative gain (NDCG). [#7739](https://github.com/scikit-learn/scikit-learn/issues/7739)
     by [David Gasquez](https://github.com/davidgasquez)
    .
    
*   Added the [`model_selection.RepeatedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#sklearn.model_selection.RepeatedKFold "sklearn.model_selection.RepeatedKFold")
     and [`model_selection.RepeatedStratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold "sklearn.model_selection.RepeatedStratifiedKFold")
    . [#8120](https://github.com/scikit-learn/scikit-learn/issues/8120)
     by [Neeraj Gangwar](http://neerajgangwar.in/)
    .
    

Miscellaneous

*   Validation that input data contains no NaN or inf can now be suppressed using [`config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context")
    , at your own risk. This will save on runtime, and may be particularly useful for prediction time. [#7548](https://github.com/scikit-learn/scikit-learn/issues/7548)
     by [Joel Nothman](https://joelnothman.com/)
    .
    
*   Added a test to ensure parameter listing in docstrings matches the function/class signature. [#9206](https://github.com/scikit-learn/scikit-learn/issues/9206)
     by [Alexandre Gramfort](https://alexandre.gramfort.net/)
     and [Raghav RV](https://github.com/raghavrv)
    .
    

#### Enhancements[#](https://scikit-learn.org/stable/whats_new/v0.19.html#id3 "Link to this heading")

Trees and ensembles

*   The `min_weight_fraction_leaf` constraint in tree construction is now more efficient, taking a fast path to declare a node a leaf if its weight is less than 2 \* the minimum. Note that the constructed tree will be different from previous versions where `min_weight_fraction_leaf` is used. [#7441](https://github.com/scikit-learn/scikit-learn/issues/7441)
     by [Nelson Liu](https://github.com/nelson-liu)
    .
    
*   [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     now support sparse input for prediction. [#6101](https://github.com/scikit-learn/scikit-learn/issues/6101)
     by [Ibraim Ganiev](https://github.com/olologin)
    .
    
*   [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     now allows changing estimators by using [`ensemble.VotingClassifier.set_params`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier.set_params "sklearn.ensemble.VotingClassifier.set_params")
    . An estimator can also be removed by setting it to `None`. [#7674](https://github.com/scikit-learn/scikit-learn/issues/7674)
     by [Yichuan Liu](https://github.com/yl565)
    .
    
*   [`tree.export_graphviz`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz "sklearn.tree.export_graphviz")
     now shows configurable number of decimal places. [#8698](https://github.com/scikit-learn/scikit-learn/issues/8698)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Added `flatten_transform` parameter to [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     to change output shape of `transform` method to 2 dimensional. [#7794](https://github.com/scikit-learn/scikit-learn/issues/7794)
     by [Ibraim Ganiev](https://github.com/olologin)
     and [Herilalaina Rakotoarison](https://github.com/herilalaina)
    .
    

Linear, kernelized and related models

*   [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    , [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
    , [`linear_model.PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier")
    , [`linear_model.PassiveAggressiveRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model.PassiveAggressiveRegressor")
     and [`linear_model.Perceptron`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron")
     now expose `max_iter` and `tol` parameters, to handle convergence more precisely. `n_iter` parameter is deprecated, and the fitted estimator exposes a `n_iter_` attribute, with actual number of iterations before convergence. [#5036](https://github.com/scikit-learn/scikit-learn/issues/5036)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Added `average` parameter to perform weight averaging in [`linear_model.PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier")
    . [#4939](https://github.com/scikit-learn/scikit-learn/issues/4939)
     by [Andrea Esuli](https://github.com/aesuli)
    .
    
*   [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
     no longer throws an error when calling `fit` if no inliers are found in its first iteration. Furthermore, causes of skipped iterations are tracked in newly added attributes, `n_skips_*`. [#7914](https://github.com/scikit-learn/scikit-learn/issues/7914)
     by [Michael Horrell](https://github.com/mthorrell)
    .
    
*   In [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
    , method `predict` is a lot faster with `return_std=True`. [#8591](https://github.com/scikit-learn/scikit-learn/issues/8591)
     by [Hadrien Bertrand](https://github.com/hbertrand)
    .
    
*   Added `return_std` to `predict` method of [`linear_model.ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
     and [`linear_model.BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
    . [#7838](https://github.com/scikit-learn/scikit-learn/issues/7838)
     by [Sergey Feldman](https://github.com/sergeyf)
    .
    
*   Memory usage enhancements: Prevent cast from float32 to float64 in: [`linear_model.MultiTaskElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html#sklearn.linear_model.MultiTaskElasticNet "sklearn.linear_model.MultiTaskElasticNet")
    ; [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     when using newton-cg solver; and [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     when using svd, sparse\_cg, cholesky or lsqr solvers. [#8835](https://github.com/scikit-learn/scikit-learn/issues/8835)
    , [#8061](https://github.com/scikit-learn/scikit-learn/issues/8061)
     by [Joan Massich](https://github.com/massich)
     and [Nicolas Cordier](https://github.com/ncordier)
     and [Thierry Guillemot](https://github.com/tguillemot)
    .
    

Other predictors

*   Custom metrics for the [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
     binary trees now have fewer constraints: they must take two 1d-arrays and return a float. [#6288](https://github.com/scikit-learn/scikit-learn/issues/6288)
     by [Jake Vanderplas](https://staff.washington.edu/jakevdp/)
    .
    
*   `algorithm='auto` in [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
     estimators now chooses the most appropriate algorithm for all input types and metrics. [#9145](https://github.com/scikit-learn/scikit-learn/issues/9145)
     by [Herilalaina Rakotoarison](https://github.com/herilalaina)
     and [Reddy Chinthala](https://github.com/preddy5)
    .
    

Decomposition, manifold learning and clustering

*   [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     and [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     now use significantly less memory when assigning data points to their nearest cluster center. [#7721](https://github.com/scikit-learn/scikit-learn/issues/7721)
     by [Jon Crall](https://github.com/Erotemic)
    .
    
*   [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
    , [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
     and [`decomposition.TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
     now expose the singular values from the underlying SVD. They are stored in the attribute `singular_values_`, like in [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
    . [#7685](https://github.com/scikit-learn/scikit-learn/issues/7685)
     by [Tommy Löfstedt](https://github.com/tomlof)
    
*   [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     now faster when `beta_loss=0`. [#9277](https://github.com/scikit-learn/scikit-learn/issues/9277)
     by [@hongkahjun](https://github.com/hongkahjun)
    .
    
*   Memory improvements for method `barnes_hut` in [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     [#7089](https://github.com/scikit-learn/scikit-learn/issues/7089)
     by [Thomas Moreau](https://github.com/tomMoral)
     and [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Optimization schedule improvements for Barnes-Hut [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     so the results are closer to the one from the reference implementation [lvdmaaten/bhtsne](https://github.com/lvdmaaten/bhtsne)
     by [Thomas Moreau](https://github.com/tomMoral)
     and [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Memory usage enhancements: Prevent cast from float32 to float64 in [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     and `decomposition.randomized_svd_low_rank`. [#9067](https://github.com/scikit-learn/scikit-learn/issues/9067)
     by [Raghav RV](https://github.com/raghavrv)
    .
    

Preprocessing and feature selection

*   Added `norm_order` parameter to [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
     to enable selection of the norm order when `coef_` is more than 1D. [#6181](https://github.com/scikit-learn/scikit-learn/issues/6181)
     by [Antoine Wendlinger](https://github.com/antoinewdg)
    .
    
*   Added ability to use sparse matrices in [`feature_selection.f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")
     with `center=True`. [#8065](https://github.com/scikit-learn/scikit-learn/issues/8065)
     by [Daniel LeJeune](https://github.com/acadiansith)
    .
    
*   Small performance improvement to n-gram creation in [`sklearn.feature_extraction.text`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction.text "sklearn.feature_extraction.text")
     by binding methods for loops and special-casing unigrams. [#7567](https://github.com/scikit-learn/scikit-learn/issues/7567)
     by [Jaye Doepke](https://github.com/jtdoepke)
    
*   Relax assumption on the data for the [`kernel_approximation.SkewedChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.SkewedChi2Sampler.html#sklearn.kernel_approximation.SkewedChi2Sampler "sklearn.kernel_approximation.SkewedChi2Sampler")
    . Since the Skewed-Chi2 kernel is defined on the open interval (−skewedness;+∞)d, the transform function should not check whether `X < 0` but whether `X < -self.skewedness`. [#7573](https://github.com/scikit-learn/scikit-learn/issues/7573)
     by [Romain Brault](https://github.com/RomainBrault)
    .
    
*   Made default kernel parameters kernel-dependent in [`kernel_approximation.Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
    . [#5229](https://github.com/scikit-learn/scikit-learn/issues/5229)
     by [Saurabh Bansod](https://github.com/mth4saurabh)
     and [Andreas Müller](https://amueller.github.io/)
    .
    

Model evaluation and meta-estimators

*   [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     is now able to cache transformers within a pipeline by using the `memory` constructor parameter. [#7990](https://github.com/scikit-learn/scikit-learn/issues/7990)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     steps can now be accessed as attributes of its `named_steps` attribute. [#8586](https://github.com/scikit-learn/scikit-learn/issues/8586)
     by [Herilalaina Rakotoarison](https://github.com/herilalaina)
    .
    
*   Added `sample_weight` parameter to [`pipeline.Pipeline.score`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.score "sklearn.pipeline.Pipeline.score")
    . [#7723](https://github.com/scikit-learn/scikit-learn/issues/7723)
     by [Mikhail Korobov](https://github.com/kmike)
    .
    
*   Added ability to set `n_jobs` parameter to [`pipeline.make_union`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_union.html#sklearn.pipeline.make_union "sklearn.pipeline.make_union")
    . A `TypeError` will be raised for any other kwargs. [#8028](https://github.com/scikit-learn/scikit-learn/issues/8028)
     by [Alexander Booth](https://github.com/alexandercbooth)
    .
    
*   [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    , [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     and [`model_selection.cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
     now allow estimators with callable kernels which were previously prohibited. [#8005](https://github.com/scikit-learn/scikit-learn/issues/8005)
     by [Andreas Müller](https://amueller.github.io/)
     .
    
*   [`model_selection.cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
     now returns output of the correct shape for all values of the argument `method`. [#7863](https://github.com/scikit-learn/scikit-learn/issues/7863)
     by [Aman Dalmia](https://github.com/dalmia)
    .
    
*   Added `shuffle` and `random_state` parameters to shuffle training data before taking prefixes of it based on training sizes in [`model_selection.learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
    . [#7506](https://github.com/scikit-learn/scikit-learn/issues/7506)
     by [Narine Kokhlikyan](https://github.com/NarineK)
    .
    
*   [`model_selection.StratifiedShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")
     now works with multioutput multiclass (or multilabel) data. [#9044](https://github.com/scikit-learn/scikit-learn/issues/9044)
     by [Vlad Niculae](https://vene.ro/)
    .
    
*   Speed improvements to [`model_selection.StratifiedShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")
    . [#5991](https://github.com/scikit-learn/scikit-learn/issues/5991)
     by [Arthur Mensch](https://github.com/arthurmensch)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   Add `shuffle` parameter to [`model_selection.train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
    . [#8845](https://github.com/scikit-learn/scikit-learn/issues/8845)
     by [themrmax](https://github.com/themrmax)
    
*   [`multioutput.MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")
     and [`multioutput.MultiOutputClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier")
     now support online learning using `partial_fit`. :issue: `8053` by [Peng Yu](https://github.com/yupbank)
    .
    
*   Add `max_train_size` parameter to [`model_selection.TimeSeriesSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")
     [#8282](https://github.com/scikit-learn/scikit-learn/issues/8282)
     by [Aman Dalmia](https://github.com/dalmia)
    .
    
*   More clustering metrics are now available through [`metrics.get_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html#sklearn.metrics.get_scorer "sklearn.metrics.get_scorer")
     and `scoring` parameters. [#8117](https://github.com/scikit-learn/scikit-learn/issues/8117)
     by [Raghav RV](https://github.com/raghavrv)
    .
    
*   A scorer based on [`metrics.explained_variance_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score "sklearn.metrics.explained_variance_score")
     is also available. [#9259](https://github.com/scikit-learn/scikit-learn/issues/9259)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    

Metrics

*   [`metrics.matthews_corrcoef`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html#sklearn.metrics.matthews_corrcoef "sklearn.metrics.matthews_corrcoef")
     now supports multiclass classification. [#8094](https://github.com/scikit-learn/scikit-learn/issues/8094)
     by [Jon Crall](https://github.com/Erotemic)
    .
    
*   Add `sample_weight` parameter to [`metrics.cohen_kappa_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#sklearn.metrics.cohen_kappa_score "sklearn.metrics.cohen_kappa_score")
    . [#8335](https://github.com/scikit-learn/scikit-learn/issues/8335)
     by [Victor Poughon](https://github.com/vpoughon)
    .
    

Miscellaneous

*   [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     now attempts to ensure that methods transform, predict, etc. do not set attributes on the estimator. [#7533](https://github.com/scikit-learn/scikit-learn/issues/7533)
     by [Ekaterina Krivich](https://github.com/kiote)
    .
    
*   Added type checking to the `accept_sparse` parameter in [`sklearn.utils.validation`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils.validation "sklearn.utils.validation")
     methods. This parameter now accepts only boolean, string, or list/tuple of strings. `accept_sparse=None` is deprecated and should be replaced by `accept_sparse=False`. [#7880](https://github.com/scikit-learn/scikit-learn/issues/7880)
     by [Josh Karnofsky](https://github.com/jkarno)
    .
    
*   Make it possible to load a chunk of an svmlight formatted file by passing a range of bytes to [`datasets.load_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html#sklearn.datasets.load_svmlight_file "sklearn.datasets.load_svmlight_file")
    . [#935](https://github.com/scikit-learn/scikit-learn/issues/935)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   [`dummy.DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
     and [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
     now accept non-finite features. [#8931](https://github.com/scikit-learn/scikit-learn/issues/8931)
     by [@Attractadore](https://github.com/Attractadore)
    .
    

#### Bug fixes[#](https://scikit-learn.org/stable/whats_new/v0.19.html#id4 "Link to this heading")

Trees and ensembles

*   Fixed a memory leak in trees when using trees with `criterion='mae'`. [#8002](https://github.com/scikit-learn/scikit-learn/issues/8002)
     by [Raghav RV](https://github.com/raghavrv)
    .
    
*   Fixed a bug where [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     uses an incorrect formula for the average path length [#8549](https://github.com/scikit-learn/scikit-learn/issues/8549)
     by [Peter Wang](https://github.com/PTRWang)
    .
    
*   Fixed a bug where [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
     throws `ZeroDivisionError` while fitting data with single class labels. [#7501](https://github.com/scikit-learn/scikit-learn/issues/7501)
     by [Dominik Krzeminski](https://github.com/dokato)
    .
    
*   Fixed a bug in [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     where a float being compared to `0.0` using `==` caused a divide by zero error. [#7970](https://github.com/scikit-learn/scikit-learn/issues/7970)
     by [He Chen](https://github.com/chenhe95)
    .
    
*   Fix a bug where [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     ignored the `min_impurity_split` parameter. [#8006](https://github.com/scikit-learn/scikit-learn/issues/8006)
     by [Sebastian Pölsterl](https://github.com/sebp)
    .
    
*   Fixed `oob_score` in [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
    . [#8936](https://github.com/scikit-learn/scikit-learn/issues/8936)
     by [Michael Lewis](https://github.com/mlewis1729)
    
*   Fixed excessive memory usage in prediction for random forests estimators. [#8672](https://github.com/scikit-learn/scikit-learn/issues/8672)
     by [Mike Benfield](https://github.com/mikebenfield)
    .
    
*   Fixed a bug where `sample_weight` as a list broke random forests in Python 2 [#8068](https://github.com/scikit-learn/scikit-learn/issues/8068)
     by [@xor](https://github.com/xor)
    .
    
*   Fixed a bug where [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     fails when `max_features` is less than 1. [#5732](https://github.com/scikit-learn/scikit-learn/issues/5732)
     by [Ishank Gulati](https://github.com/IshankGulati)
    .
    
*   Fix a bug where gradient boosting with `loss='quantile'` computed negative errors for negative values of `ytrue - ypred` leading to wrong values when calling `__call__`. [#8087](https://github.com/scikit-learn/scikit-learn/issues/8087)
     by [Alexis Mignon](https://github.com/AlexisMignon)
    
*   Fix a bug where [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     raises an error when a numpy array is passed in for weights. [#7983](https://github.com/scikit-learn/scikit-learn/issues/7983)
     by [Vincent Pham](https://github.com/vincentpham1991)
    .
    
*   Fixed a bug where [`tree.export_graphviz`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz "sklearn.tree.export_graphviz")
     raised an error when the length of features\_names does not match n\_features in the decision tree. [#8512](https://github.com/scikit-learn/scikit-learn/issues/8512)
     by [Li Li](https://github.com/aikinogard)
    .
    

Linear, kernelized and related models

*   Fixed a bug where [`linear_model.RANSACRegressor.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor.fit "sklearn.linear_model.RANSACRegressor.fit")
     may run until `max_iter` if it finds a large inlier group early. [#8251](https://github.com/scikit-learn/scikit-learn/issues/8251)
     by [@aivision2020](https://github.com/aivision2020)
    .
    
*   Fixed a bug where [`naive_bayes.MultinomialNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB "sklearn.naive_bayes.MultinomialNB")
     and [`naive_bayes.BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
     failed when `alpha=0`. [#5814](https://github.com/scikit-learn/scikit-learn/issues/5814)
     by [Yichuan Liu](https://github.com/yl565)
     and [Herilalaina Rakotoarison](https://github.com/herilalaina)
    .
    
*   Fixed a bug where [`linear_model.LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")
     does not give the same result as the LassoLars implementation available in R (lars library). [#7849](https://github.com/scikit-learn/scikit-learn/issues/7849)
     by [Jair Montoya Martinez](https://github.com/jmontoyam)
    .
    
*   Fixed a bug in `linear_model.RandomizedLasso`, [`linear_model.Lars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html#sklearn.linear_model.Lars "sklearn.linear_model.Lars")
    , [`linear_model.LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")
    , [`linear_model.LarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV "sklearn.linear_model.LarsCV")
     and [`linear_model.LassoLarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV")
    , where the parameter `precompute` was not used consistently across classes, and some values proposed in the docstring could raise errors. [#5359](https://github.com/scikit-learn/scikit-learn/issues/5359)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Fix inconsistent results between [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     and [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     when using `normalize=True`. [#9302](https://github.com/scikit-learn/scikit-learn/issues/9302)
     by [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   Fix a bug where [`linear_model.LassoLars.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars.fit "sklearn.linear_model.LassoLars.fit")
     sometimes left `coef_` as a list, rather than an ndarray. [#8160](https://github.com/scikit-learn/scikit-learn/issues/8160)
     by [CJ Carey](https://github.com/perimosocordiae)
    .
    
*   Fix [`linear_model.BayesianRidge.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge.fit "sklearn.linear_model.BayesianRidge.fit")
     to return ridge parameter `alpha_` and `lambda_` consistent with calculated coefficients `coef_` and `intercept_`. [#8224](https://github.com/scikit-learn/scikit-learn/issues/8224)
     by [Peter Gedeck](https://github.com/gedeck)
    .
    
*   Fixed a bug in [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
     where it returned floats instead of integer classes. [#8676](https://github.com/scikit-learn/scikit-learn/issues/8676)
     by [Vathsala Achar](https://github.com/VathsalaAchar)
    .
    
*   Fix AIC/BIC criterion computation in [`linear_model.LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")
    . [#9022](https://github.com/scikit-learn/scikit-learn/issues/9022)
     by [Alexandre Gramfort](https://alexandre.gramfort.net/)
     and [Mehmet Basbug](https://github.com/mehmetbasbug)
    .
    
*   Fixed a memory leak in our LibLinear implementation. [#9024](https://github.com/scikit-learn/scikit-learn/issues/9024)
     by [Sergei Lebedev](https://github.com/superbobry)
    
*   Fix bug where stratified CV splitters did not work with [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
    . [#8973](https://github.com/scikit-learn/scikit-learn/issues/8973)
     by [Paulo Haddad](https://github.com/paulochf)
    .
    
*   Fixed a bug in [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
     when the standard deviation and covariance predicted without fit would fail with a meaningless error by default. [#6573](https://github.com/scikit-learn/scikit-learn/issues/6573)
     by [Quazi Marufur Rahman](https://github.com/qmaruf)
     and [Manoj Kumar](https://manojbits.wordpress.com/)
    .
    

Other predictors

*   Fix `semi_supervised.BaseLabelPropagation` to correctly implement `LabelPropagation` and `LabelSpreading` as done in the referenced papers. [#9239](https://github.com/scikit-learn/scikit-learn/issues/9239)
     by [Andre Ambrosio Boechat](https://github.com/boechat107)
    , [Utkarsh Upadhyay](https://github.com/musically-ut)
    , and [Joel Nothman](https://joelnothman.com/)
    .
    

Decomposition, manifold learning and clustering

*   Fixed the implementation of [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
    :
    
*   `early_exaggeration` parameter had no effect and is now used for the first 250 optimization iterations.
    
*   Fixed the `AssertionError: Tree consistency failed` exception reported in [#8992](https://github.com/scikit-learn/scikit-learn/issues/8992)
    .
    
*   Improve the learning schedule to match the one from the reference implementation [lvdmaaten/bhtsne](https://github.com/lvdmaaten/bhtsne)
    . by [Thomas Moreau](https://github.com/tomMoral)
     and [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Fix a bug in [`decomposition.LatentDirichletAllocation`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "sklearn.decomposition.LatentDirichletAllocation")
     where the `perplexity` method was returning incorrect results because the `transform` method returns normalized document topic distributions as of version 0.18. [#7954](https://github.com/scikit-learn/scikit-learn/issues/7954)
     by [Gary Foreman](https://github.com/garyForeman)
    .
    
*   Fix output shape and bugs with n\_jobs > 1 in [`decomposition.SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")
     transform and [`decomposition.sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")
     for one-dimensional data and one component. This also impacts the output shape of [`decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
    . [#8086](https://github.com/scikit-learn/scikit-learn/issues/8086)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Fixed the implementation of `explained_variance_` in [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
    , `decomposition.RandomizedPCA` and [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
    . [#9105](https://github.com/scikit-learn/scikit-learn/issues/9105)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   Fixed the implementation of `noise_variance_` in [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
    . [#9108](https://github.com/scikit-learn/scikit-learn/issues/9108)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   Fixed a bug where [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
     gives incorrect result when input is a precomputed sparse matrix with initial rows all zero. [#8306](https://github.com/scikit-learn/scikit-learn/issues/8306)
     by [Akshay Gupta](https://github.com/Akshay0724)
    
*   Fix a bug regarding fitting [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     with a sparse array X and initial centroids, where X’s means were unnecessarily being subtracted from the centroids. [#7872](https://github.com/scikit-learn/scikit-learn/issues/7872)
     by [Josh Karnofsky](https://github.com/jkarno)
    .
    
*   Fixes to the input validation in [`covariance.EllipticEnvelope`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")
    . [#8086](https://github.com/scikit-learn/scikit-learn/issues/8086)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Fixed a bug in [`covariance.MinCovDet`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.MinCovDet.html#sklearn.covariance.MinCovDet "sklearn.covariance.MinCovDet")
     where inputting data that produced a singular covariance matrix would cause the helper method `_c_step` to throw an exception. [#3367](https://github.com/scikit-learn/scikit-learn/issues/3367)
     by [Jeremy Steward](https://github.com/ThatGeoGuy)
    
*   Fixed a bug in [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     affecting convergence of the gradient descent. [#8768](https://github.com/scikit-learn/scikit-learn/issues/8768)
     by [David DeTomaso](https://github.com/deto)
    .
    
*   Fixed a bug in [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     where it stored the incorrect `kl_divergence_`. [#6507](https://github.com/scikit-learn/scikit-learn/issues/6507)
     by [Sebastian Saeger](https://github.com/ssaeger)
    .
    
*   Fixed improper scaling in [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
     with `scale=True`. [#7819](https://github.com/scikit-learn/scikit-learn/issues/7819)
     by [jayzed82](https://github.com/jayzed82)
    .
    
*   [`cluster.SpectralCoclustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering "sklearn.cluster.SpectralCoclustering")
     and [`cluster.SpectralBiclustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering "sklearn.cluster.SpectralBiclustering")
     `fit` method conforms with API by accepting `y` and returning the object. [#6126](https://github.com/scikit-learn/scikit-learn/issues/6126)
    , [#7814](https://github.com/scikit-learn/scikit-learn/issues/7814)
     by [Laurent Direr](https://github.com/ldirer)
     and [Maniteja Nandana](https://github.com/maniteja123)
    .
    
*   Fix bug where [`sklearn.mixture`](https://scikit-learn.org/stable/api/sklearn.mixture.html#module-sklearn.mixture "sklearn.mixture")
     `sample` methods did not return as many samples as requested. [#7702](https://github.com/scikit-learn/scikit-learn/issues/7702)
     by [Levi John Wolf](https://github.com/ljwolf)
    .
    
*   Fixed the shrinkage implementation in [`neighbors.NearestCentroid`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")
    . [#9219](https://github.com/scikit-learn/scikit-learn/issues/9219)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    

Preprocessing and feature selection

*   For sparse matrices, [`preprocessing.normalize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html#sklearn.preprocessing.normalize "sklearn.preprocessing.normalize")
     with `return_norm=True` will now raise a `NotImplementedError` with ‘l1’ or ‘l2’ norm and with norm ‘max’ the norms returned will be the same as for dense matrices. [#7771](https://github.com/scikit-learn/scikit-learn/issues/7771)
     by [Ang Lu](https://github.com/luang008)
    .
    
*   Fix a bug where [`feature_selection.SelectFdr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFdr.html#sklearn.feature_selection.SelectFdr "sklearn.feature_selection.SelectFdr")
     did not exactly implement Benjamini-Hochberg procedure. It formerly may have selected fewer features than it should. [#7490](https://github.com/scikit-learn/scikit-learn/issues/7490)
     by [Peng Meng](https://github.com/mpjlu)
    .
    
*   Fixed a bug where `linear_model.RandomizedLasso` and `linear_model.RandomizedLogisticRegression` break for sparse input. [#8259](https://github.com/scikit-learn/scikit-learn/issues/8259)
     by [Aman Dalmia](https://github.com/dalmia)
    .
    
*   Fix a bug where [`feature_extraction.FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
     mandatorily applied a sparse random projection to the hashed features, preventing the use of [`feature_extraction.text.HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
     in a pipeline with [`feature_extraction.text.TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
    . [#7565](https://github.com/scikit-learn/scikit-learn/issues/7565)
     by [Roman Yurchak](https://github.com/rth)
    .
    
*   Fix a bug where [`feature_selection.mutual_info_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html#sklearn.feature_selection.mutual_info_regression "sklearn.feature_selection.mutual_info_regression")
     did not correctly use `n_neighbors`. [#8181](https://github.com/scikit-learn/scikit-learn/issues/8181)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

Model evaluation and meta-estimators

*   Fixed a bug where `model_selection.BaseSearchCV.inverse_transform` returns `self.best_estimator_.transform()` instead of `self.best_estimator_.inverse_transform()`. [#8344](https://github.com/scikit-learn/scikit-learn/issues/8344)
     by [Akshay Gupta](https://github.com/Akshay0724)
     and [Rasmus Eriksson](https://github.com/MrMjauh)
    .
    
*   Added `classes_` attribute to [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    , [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
    , `grid_search.GridSearchCV`, and `grid_search.RandomizedSearchCV` that matches the `classes_` attribute of `best_estimator_`. [#7661](https://github.com/scikit-learn/scikit-learn/issues/7661)
     and [#8295](https://github.com/scikit-learn/scikit-learn/issues/8295)
     by [Alyssa Batula](https://github.com/abatula)
    , [Dylan Werner-Meier](https://github.com/unautre)
    , and [Stephen Hoover](https://github.com/stephen-hoover)
    .
    
*   Fixed a bug where [`model_selection.validation_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve "sklearn.model_selection.validation_curve")
     reused the same estimator for each parameter value. [#7365](https://github.com/scikit-learn/scikit-learn/issues/7365)
     by [Aleksandr Sandrovskii](https://github.com/Sundrique)
    .
    
*   [`model_selection.permutation_test_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#sklearn.model_selection.permutation_test_score "sklearn.model_selection.permutation_test_score")
     now works with Pandas types. [#5697](https://github.com/scikit-learn/scikit-learn/issues/5697)
     by [Stijn Tonk](https://github.com/equialgo)
    .
    
*   Several fixes to input validation in [`multiclass.OutputCodeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier")
     [#8086](https://github.com/scikit-learn/scikit-learn/issues/8086)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   [`multiclass.OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
    ’s `partial_fit` now ensures all classes are provided up-front. [#6250](https://github.com/scikit-learn/scikit-learn/issues/6250)
     by [Asish Panda](https://github.com/kaichogami)
    .
    
*   Fix [`multioutput.MultiOutputClassifier.predict_proba`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.predict_proba "sklearn.multioutput.MultiOutputClassifier.predict_proba")
     to return a list of 2d arrays, rather than a 3d array. In the case where different target columns had different numbers of classes, a `ValueError` would be raised on trying to stack matrices with different dimensions. [#8093](https://github.com/scikit-learn/scikit-learn/issues/8093)
     by [Peter Bull](https://github.com/pjbull)
    .
    
*   Cross validation now works with Pandas datatypes that have a read-only index. [#9507](https://github.com/scikit-learn/scikit-learn/issues/9507)
     by [Loic Esteve](https://github.com/lesteve)
    .
    

Metrics

*   [`metrics.average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
     no longer linearly interpolates between operating points, and instead weighs precisions by the change in recall since the last operating point, as per the [Wikipedia entry](https://en.wikipedia.org/wiki/Average_precision)
    . ([#7356](https://github.com/scikit-learn/scikit-learn/pull/7356)
    ). By [Nick Dingwall](https://github.com/ndingwall)
     and [Gael Varoquaux](https://gael-varoquaux.info/)
    .
    
*   Fix a bug in `metrics.classification._check_targets` which would return `'binary'` if `y_true` and `y_pred` were both `'binary'` but the union of `y_true` and `y_pred` was `'multiclass'`. [#8377](https://github.com/scikit-learn/scikit-learn/issues/8377)
     by [Loic Esteve](https://github.com/lesteve)
    .
    
*   Fixed an integer overflow bug in [`metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
     and hence [`metrics.cohen_kappa_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#sklearn.metrics.cohen_kappa_score "sklearn.metrics.cohen_kappa_score")
    . [#8354](https://github.com/scikit-learn/scikit-learn/issues/8354)
    , [#7929](https://github.com/scikit-learn/scikit-learn/issues/7929)
     by [Joel Nothman](https://joelnothman.com/)
     and [Jon Crall](https://github.com/Erotemic)
    .
    
*   Fixed passing of `gamma` parameter to the `chi2` kernel in [`metrics.pairwise.pairwise_kernels`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html#sklearn.metrics.pairwise.pairwise_kernels "sklearn.metrics.pairwise.pairwise_kernels")
     [#5211](https://github.com/scikit-learn/scikit-learn/issues/5211)
     by [Nick Rhinehart](https://github.com/nrhine1)
    , [Saurabh Bansod](https://github.com/mth4saurabh)
     and [Andreas Müller](https://amueller.github.io/)
    .
    

Miscellaneous

*   Fixed a bug when [`datasets.make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
     fails when generating more than 30 features. [#8159](https://github.com/scikit-learn/scikit-learn/issues/8159)
     by [Herilalaina Rakotoarison](https://github.com/herilalaina)
    .
    
*   Fixed a bug where [`datasets.make_moons`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")
     gives an incorrect result when `n_samples` is odd. [#8198](https://github.com/scikit-learn/scikit-learn/issues/8198)
     by [Josh Levy](https://github.com/levy5674)
    .
    
*   Some `fetch_` functions in [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
     were ignoring the `download_if_missing` keyword. [#7944](https://github.com/scikit-learn/scikit-learn/issues/7944)
     by [Ralf Gommers](https://github.com/rgommers)
    .
    
*   Fix estimators to accept a `sample_weight` parameter of type `pandas.Series` in their `fit` function. [#7825](https://github.com/scikit-learn/scikit-learn/issues/7825)
     by [Kathleen Chen](https://github.com/kchen17)
    .
    
*   Fix a bug in cases where `numpy.cumsum` may be numerically unstable, raising an exception if instability is identified. [#7376](https://github.com/scikit-learn/scikit-learn/issues/7376)
     and [#7331](https://github.com/scikit-learn/scikit-learn/issues/7331)
     by [Joel Nothman](https://joelnothman.com/)
     and [@yangarbiter](https://github.com/yangarbiter)
    .
    
*   Fix a bug where `base.BaseEstimator.__getstate__` obstructed pickling customizations of child-classes, when used in a multiple inheritance context. [#8316](https://github.com/scikit-learn/scikit-learn/issues/8316)
     by [Holger Peters](https://github.com/HolgerPeters)
    .
    
*   Update Sphinx-Gallery from 0.1.4 to 0.1.7 for resolving links in documentation build with Sphinx>1.5 [#8010](https://github.com/scikit-learn/scikit-learn/issues/8010)
    , [#7986](https://github.com/scikit-learn/scikit-learn/issues/7986)
     by [Oscar Najera](https://github.com/Titan-C)
    
*   Add `data_home` parameter to [`sklearn.datasets.fetch_kddcup99`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99 "sklearn.datasets.fetch_kddcup99")
    . [#9289](https://github.com/scikit-learn/scikit-learn/issues/9289)
     by [Loic Esteve](https://github.com/lesteve)
    .
    
*   Fix dataset loaders using Python 3 version of makedirs to also work in Python 2. [#9284](https://github.com/scikit-learn/scikit-learn/issues/9284)
     by [Sebastin Santy](https://github.com/SebastinSanty)
    .
    
*   Several minor issues were fixed with thanks to the alerts of [lgtm.com](https://lgtm.com/)
    . [#9278](https://github.com/scikit-learn/scikit-learn/issues/9278)
     by [Jean Helie](https://github.com/jhelie)
    , among others.
    

### API changes summary[#](https://scikit-learn.org/stable/whats_new/v0.19.html#api-changes-summary "Link to this heading")

Trees and ensembles

*   Gradient boosting base models are no longer estimators. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   All tree-based estimators now accept a `min_impurity_decrease` parameter in lieu of the `min_impurity_split`, which is now deprecated. The `min_impurity_decrease` helps stop splitting the nodes in which the weighted impurity decrease from splitting is no longer at least `min_impurity_decrease`. [#8449](https://github.com/scikit-learn/scikit-learn/issues/8449)
     by [Raghav RV](https://github.com/raghavrv)
    .
    

Linear, kernelized and related models

*   `n_iter` parameter is deprecated in [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    , [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
    , [`linear_model.PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier")
    , [`linear_model.PassiveAggressiveRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model.PassiveAggressiveRegressor")
     and [`linear_model.Perceptron`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron")
    . By [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    

Other predictors

*   `neighbors.LSHForest` has been deprecated and will be removed in 0.21 due to poor performance. [#9078](https://github.com/scikit-learn/scikit-learn/issues/9078)
     by [Laurent Direr](https://github.com/ldirer)
    .
    
*   [`neighbors.NearestCentroid`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")
     no longer purports to support `metric='precomputed'` which now raises an error. [#8515](https://github.com/scikit-learn/scikit-learn/issues/8515)
     by [Sergul Aydore](https://github.com/sergulaydore)
    .
    
*   The `alpha` parameter of [`semi_supervised.LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")
     now has no effect and is deprecated to be removed in 0.21. [#9239](https://github.com/scikit-learn/scikit-learn/issues/9239)
     by [Andre Ambrosio Boechat](https://github.com/boechat107)
    , [Utkarsh Upadhyay](https://github.com/musically-ut)
    , and [Joel Nothman](https://joelnothman.com/)
    .
    

Decomposition, manifold learning and clustering

*   Deprecate the `doc_topic_distr` argument of the `perplexity` method in [`decomposition.LatentDirichletAllocation`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "sklearn.decomposition.LatentDirichletAllocation")
     because the user no longer has access to the unnormalized document topic distribution needed for the perplexity calculation. [#7954](https://github.com/scikit-learn/scikit-learn/issues/7954)
     by [Gary Foreman](https://github.com/garyForeman)
    .
    
*   The `n_topics` parameter of [`decomposition.LatentDirichletAllocation`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "sklearn.decomposition.LatentDirichletAllocation")
     has been renamed to `n_components` and will be removed in version 0.21. [#8922](https://github.com/scikit-learn/scikit-learn/issues/8922)
     by [@Attractadore](https://github.com/Attractadore)
    .
    
*   [`decomposition.SparsePCA.transform`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA.transform "sklearn.decomposition.SparsePCA.transform")
    ’s `ridge_alpha` parameter is deprecated in preference for class parameter. [#8137](https://github.com/scikit-learn/scikit-learn/issues/8137)
     by [Naoya Kanai](https://github.com/naoyak)
    .
    
*   [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
     now has a `metric_params` parameter. [#8139](https://github.com/scikit-learn/scikit-learn/issues/8139)
     by [Naoya Kanai](https://github.com/naoyak)
    .
    

Preprocessing and feature selection

*   [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
     now has a `partial_fit` method only if the underlying estimator does. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
     now validates the `threshold` parameter and sets the `threshold_` attribute during the call to `fit`, and no longer during the call to `transform`. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   The `non_negative` parameter in [`feature_extraction.FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
     has been deprecated, and replaced with a more principled alternative, `alternate_sign`. [#7565](https://github.com/scikit-learn/scikit-learn/issues/7565)
     by [Roman Yurchak](https://github.com/rth)
    .
    
*   `linear_model.RandomizedLogisticRegression`, and `linear_model.RandomizedLasso` have been deprecated and will be removed in version 0.21. [#8995](https://github.com/scikit-learn/scikit-learn/issues/8995)
     by [Ramana.S](https://github.com/sentient07)
    .
    

Model evaluation and meta-estimators

*   Deprecate the `fit_params` constructor input to the [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     in favor of passing keyword parameters to the `fit` methods of those classes. Data-dependent parameters needed for model training should be passed as keyword arguments to `fit`, and conforming to this convention will allow the hyperparameter selection classes to be used with tools such as [`model_selection.cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
    . [#2879](https://github.com/scikit-learn/scikit-learn/issues/2879)
     by [Stephen Hoover](https://github.com/stephen-hoover)
    .
    
*   In version 0.21, the default behavior of splitters that use the `test_size` and `train_size` parameter will change, such that specifying `train_size` alone will cause `test_size` to be the remainder. [#7459](https://github.com/scikit-learn/scikit-learn/issues/7459)
     by [Nelson Liu](https://github.com/nelson-liu)
    .
    
*   [`multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
     now has `partial_fit`, `decision_function` and `predict_proba` methods only when the underlying estimator does. [#7812](https://github.com/scikit-learn/scikit-learn/issues/7812)
     by [Andreas Müller](https://amueller.github.io/)
     and [Mikhail Korobov](https://github.com/kmike)
    .
    
*   [`multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
     now has a `partial_fit` method only if the underlying estimator does. By [Andreas Müller](https://amueller.github.io/)
    .
    
*   The `decision_function` output shape for binary classification in [`multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
     and [`multiclass.OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
     is now `(n_samples,)` to conform to scikit-learn conventions. [#9100](https://github.com/scikit-learn/scikit-learn/issues/9100)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   The [`multioutput.MultiOutputClassifier.predict_proba`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier.predict_proba "sklearn.multioutput.MultiOutputClassifier.predict_proba")
     function used to return a 3d array (`n_samples`, `n_classes`, `n_outputs`). In the case where different target columns had different numbers of classes, a `ValueError` would be raised on trying to stack matrices with different dimensions. This function now returns a list of arrays where the length of the list is `n_outputs`, and each array is (`n_samples`, `n_classes`) for that particular output. [#8093](https://github.com/scikit-learn/scikit-learn/issues/8093)
     by [Peter Bull](https://github.com/pjbull)
    .
    
*   Replace attribute `named_steps` `dict` to [`utils.Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")
     in [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     to enable tab completion in interactive environment. In the case conflict value on `named_steps` and `dict` attribute, `dict` behavior will be prioritized. [#8481](https://github.com/scikit-learn/scikit-learn/issues/8481)
     by [Herilalaina Rakotoarison](https://github.com/herilalaina)
    .
    

Miscellaneous

*   Deprecate the `y` parameter in `transform` and `inverse_transform`. The method should not accept `y` parameter, as it’s used at the prediction time. [#8174](https://github.com/scikit-learn/scikit-learn/issues/8174)
     by [Tahar Zanouda](https://github.com/tzano)
    , [Alexandre Gramfort](https://alexandre.gramfort.net/)
     and [Raghav RV](https://github.com/raghavrv)
    .
    
*   SciPy >= 0.13.3 and NumPy >= 1.8.2 are now the minimum supported versions for scikit-learn. The following backported functions in [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
     have been removed or deprecated accordingly. [#8854](https://github.com/scikit-learn/scikit-learn/issues/8854)
     and [#8874](https://github.com/scikit-learn/scikit-learn/issues/8874)
     by [Naoya Kanai](https://github.com/naoyak)
    
*   The `store_covariances` and `covariances_` parameters of [`discriminant_analysis.QuadraticDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis "sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis")
     have been renamed to `store_covariance` and `covariance_` to be consistent with the corresponding parameter names of the [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
    . They will be removed in version 0.21. [#7998](https://github.com/scikit-learn/scikit-learn/issues/7998)
     by [Jiacheng](https://github.com/mrbeann)
    
    Removed in 0.19:
    
    *   `utils.fixes.argpartition`
        
    *   `utils.fixes.array_equal`
        
    *   `utils.fixes.astype`
        
    *   `utils.fixes.bincount`
        
    *   `utils.fixes.expit`
        
    *   `utils.fixes.frombuffer_empty`
        
    *   `utils.fixes.in1d`
        
    *   `utils.fixes.norm`
        
    *   `utils.fixes.rankdata`
        
    *   `utils.fixes.safe_copy`
        
    
    Deprecated in 0.19, to be removed in 0.21:
    
    *   `utils.arpack.eigs`
        
    *   `utils.arpack.eigsh`
        
    *   `utils.arpack.svds`
        
    *   `utils.extmath.fast_dot`
        
    *   `utils.extmath.logsumexp`
        
    *   `utils.extmath.norm`
        
    *   `utils.extmath.pinvh`
        
    *   `utils.graph.graph_laplacian`
        
    *   `utils.random.choice`
        
    *   `utils.sparsetools.connected_components`
        
    *   `utils.stats.rankdata`
        
*   Estimators with both methods `decision_function` and `predict_proba` are now required to have a monotonic relation between them. The method `check_decision_proba_consistency` has been added in **utils.estimator\_checks** to check their consistency. [#7578](https://github.com/scikit-learn/scikit-learn/issues/7578)
     by [Shubham Bhardwaj](https://github.com/shubham0704)
    
*   All checks in `utils.estimator_checks`, in particular [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     now accept estimator instances. Most other checks do not accept estimator classes any more. [#9019](https://github.com/scikit-learn/scikit-learn/issues/9019)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   Ensure that estimators’ attributes ending with `_` are not set in the constructor but only in the `fit` method. Most notably, ensemble estimators (deriving from `ensemble.BaseEnsemble`) now only have `self.estimators_` available after `fit`. [#7464](https://github.com/scikit-learn/scikit-learn/issues/7464)
     by [Lars Buitinck](https://github.com/larsmans)
     and [Loic Esteve](https://github.com/lesteve)
    .
    

### Code and Documentation Contributors[#](https://scikit-learn.org/stable/whats_new/v0.19.html#id10 "Link to this heading")

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 0.18, including:

Joel Nothman, Loic Esteve, Andreas Mueller, Guillaume Lemaitre, Olivier Grisel, Hanmin Qin, Raghav RV, Alexandre Gramfort, themrmax, Aman Dalmia, Gael Varoquaux, Naoya Kanai, Tom Dupré la Tour, Rishikesh, Nelson Liu, Taehoon Lee, Nelle Varoquaux, Aashil, Mikhail Korobov, Sebastin Santy, Joan Massich, Roman Yurchak, RAKOTOARISON Herilalaina, Thierry Guillemot, Alexandre Abadie, Carol Willing, Balakumaran Manoharan, Josh Karnofsky, Vlad Niculae, Utkarsh Upadhyay, Dmitry Petrov, Minghui Liu, Srivatsan, Vincent Pham, Albert Thomas, Jake VanderPlas, Attractadore, JC Liu, alexandercbooth, chkoar, Óscar Nájera, Aarshay Jain, Kyle Gilliam, Ramana Subramanyam, CJ Carey, Clement Joudet, David Robles, He Chen, Joris Van den Bossche, Karan Desai, Katie Luangkote, Leland McInnes, Maniteja Nandana, Michele Lacchia, Sergei Lebedev, Shubham Bhardwaj, akshay0724, omtcyfz, rickiepark, waterponey, Vathsala Achar, jbDelafosse, Ralf Gommers, Ekaterina Krivich, Vivek Kumar, Ishank Gulati, Dave Elliott, ldirer, Reiichiro Nakano, Levi John Wolf, Mathieu Blondel, Sid Kapur, Dougal J. Sutherland, midinas, mikebenfield, Sourav Singh, Aseem Bansal, Ibraim Ganiev, Stephen Hoover, AishwaryaRK, Steven C. Howell, Gary Foreman, Neeraj Gangwar, Tahar, Jon Crall, dokato, Kathy Chen, ferria, Thomas Moreau, Charlie Brummitt, Nicolas Goix, Adam Kleczewski, Sam Shleifer, Nikita Singh, Basil Beirouti, Giorgio Patrini, Manoj Kumar, Rafael Possas, James Bourbeau, James A. Bednar, Janine Harper, Jaye, Jean Helie, Jeremy Steward, Artsiom, John Wei, Jonathan LIgo, Jonathan Rahn, seanpwilliams, Arthur Mensch, Josh Levy, Julian Kuhlmann, Julien Aubert, Jörn Hees, Kai, shivamgargsya, Kat Hempstalk, Kaushik Lakshmikanth, Kennedy, Kenneth Lyons, Kenneth Myers, Kevin Yap, Kirill Bobyrev, Konstantin Podshumok, Arthur Imbert, Lee Murray, toastedcornflakes, Lera, Li Li, Arthur Douillard, Mainak Jas, tobycheese, Manraj Singh, Manvendra Singh, Marc Meketon, MarcoFalke, Matthew Brett, Matthias Gilch, Mehul Ahuja, Melanie Goetz, Meng, Peng, Michael Dezube, Michal Baumgartner, vibrantabhi19, Artem Golubin, Milen Paskov, Antonin Carette, Morikko, MrMjauh, NALEPA Emmanuel, Namiya, Antoine Wendlinger, Narine Kokhlikyan, NarineK, Nate Guerin, Angus Williams, Ang Lu, Nicole Vavrova, Nitish Pandey, Okhlopkov Daniil Olegovich, Andy Craze, Om Prakash, Parminder Singh, Patrick Carlson, Patrick Pei, Paul Ganssle, Paulo Haddad, Paweł Lorek, Peng Yu, Pete Bachant, Peter Bull, Peter Csizsek, Peter Wang, Pieter Arthur de Jong, Ping-Yao, Chang, Preston Parry, Puneet Mathur, Quentin Hibon, Andrew Smith, Andrew Jackson, 1kastner, Rameshwar Bhaskaran, Rebecca Bilbro, Remi Rampin, Andrea Esuli, Rob Hall, Robert Bradshaw, Romain Brault, Aman Pratik, Ruifeng Zheng, Russell Smith, Sachin Agarwal, Sailesh Choyal, Samson Tan, Samuël Weber, Sarah Brown, Sebastian Pölsterl, Sebastian Raschka, Sebastian Saeger, Alyssa Batula, Abhyuday Pratap Singh, Sergey Feldman, Sergul Aydore, Sharan Yalburgi, willduan, Siddharth Gupta, Sri Krishna, Almer, Stijn Tonk, Allen Riddell, Theofilos Papapanagiotou, Alison, Alexis Mignon, Tommy Boucher, Tommy Löfstedt, Toshihiro Kamishima, Tyler Folkman, Tyler Lanigan, Alexander Junge, Varun Shenoy, Victor Poughon, Vilhelm von Ehrenheim, Aleksandr Sandrovskii, Alan Yee, Vlasios Vasileiou, Warut Vijitbenjaronk, Yang Zhang, Yaroslav Halchenko, Yichuan Liu, Yuichi Fujikawa, affanv14, aivision2020, xor, andreh7, brady salz, campustrampus, Agamemnon Krasoulis, ditenberg, elena-sharova, filipj8, fukatani, gedeck, guiniol, guoci, hakaa1, hongkahjun, i-am-xhy, jakirkham, jaroslaw-weber, jayzed82, jeroko, jmontoyam, jonathan.striebel, josephsalmon, jschendel, leereeves, martin-hahn, mathurinm, mehak-sachdeva, mlewis1729, mlliou112, mthorrell, ndingwall, nuffe, yangarbiter, plagree, pldtc325, Breno Freitas, Brett Olsen, Brian A. Alfano, Brian Burns, polmauri, Brandon Carter, Charlton Austin, Chayant T15h, Chinmaya Pancholi, Christian Danielsen, Chung Yen, Chyi-Kwei Yau, pravarmahajan, DOHMATOB Elvis, Daniel LeJeune, Daniel Hnyk, Darius Morawiec, David DeTomaso, David Gasquez, David Haberthür, David Heryanto, David Kirkby, David Nicholson, rashchedrin, Deborah Gertrude Digges, Denis Engemann, Devansh D, Dickson, Bob Baxley, Don86, E. Lynch-Klarup, Ed Rogers, Elizabeth Ferriss, Ellen-Co2, Fabian Egli, Fang-Chieh Chou, Bing Tian Dai, Greg Stupp, Grzegorz Szpak, Bertrand Thirion, Hadrien Bertrand, Harizo Rajaona, zxcvbnius, Henry Lin, Holger Peters, Icyblade Dai, Igor Andriushchenko, Ilya, Isaac Laughlin, Iván Vallés, Aurélien Bellet, JPFrancoia, Jacob Schreiber, Asish Mahapatra

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)