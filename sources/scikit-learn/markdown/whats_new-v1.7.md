[Skip to main content](https://scikit-learn.org/stable/whats_new/v1.7.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v1.7.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v1.7.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v1.7.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v1.7.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v1.7.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v1.7.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v1.7.html)

Collapse Sidebar Expand Sidebar

Version 1.7[#](https://scikit-learn.org/stable/whats_new/v1.7.html#version-1-7 "Link to this heading")

=======================================================================================================

For a short description of the main highlights of the release, please refer to [Release Highlights for scikit-learn 1.7](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html#sphx-glr-auto-examples-release-highlights-plot-release-highlights-1-7-0-py)
.

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 1.7.2[#](https://scikit-learn.org/stable/whats_new/v1.7.html#version-1-7-2 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**September 2025**

### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-compose "Link to this heading")

*   Fix [`compose.TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
     now passes the transformed target to the regressor with the same number of dimensions as the original target. By [kryggird](https://github.com/kryggird)
    . [#31563](https://github.com/scikit-learn/scikit-learn/pull/31563)
    

### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-feature-extraction "Link to this heading")

*   Fix Set the tag `requires_fit=False` for the classes [`feature_extraction.FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
     and [`feature_extraction.text.HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
    . By [hakan çanakcı](https://github.com/hqkqn32)
    . [#31851](https://github.com/scikit-learn/scikit-learn/pull/31851)
    

### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-impute "Link to this heading")

*   Fix Fixed a bug in [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     with `strategy="most_frequent"` when there is a tie in the most frequent value and the input data has mixed types. By [Alexandre Abraham](https://github.com/AlexandreAbraham)
    . [#31820](https://github.com/scikit-learn/scikit-learn/pull/31820)
    

### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-linear-model "Link to this heading")

*   Fix Fixed a bug with `solver="newton-cholesky"` on multi-class problems in [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     and in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     when used with `warm_start=True`. The bug appeared either with `fit_intercept=True` or with `penalty=None` (both resulting in unpenalized parameters for the solver). The coefficients and intercepts of the last class as provided by warm start were partially wrongly overwritten by zero. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#31866](https://github.com/scikit-learn/scikit-learn/pull/31866)
    

### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-pipeline "Link to this heading")

*   Fix [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     now validates that all transformers return 2D outputs and raises an informative error when transformers return 1D outputs, preventing silent failures that previously produced meaningless concatenated results. By [gguiomar](https://github.com/gguiomar)
    . [#31559](https://github.com/scikit-learn/scikit-learn/pull/31559)
    

Version 1.7.1[#](https://scikit-learn.org/stable/whats_new/v1.7.html#version-1-7-1 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**July 2025**

### [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-base "Link to this heading")

*   Fix Fix regression in HTML representation when detecting the non-default parameters that where of array-like types. By [Dea María Léon](https://github.com/deamarialeon)
     [#31528](https://github.com/scikit-learn/scikit-learn/pull/31528)
    

### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#id1 "Link to this heading")

*   Fix [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     now correctly preserves non-default index when mixing pandas Series and Dataframes. By [Nicolas Bolle](https://github.com/nicolas-bolle)
    . [#31079](https://github.com/scikit-learn/scikit-learn/pull/31079)
    

### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-datasets "Link to this heading")

*   Fix Fixed a regression preventing to extract the downloaded dataset in [`datasets.fetch_20newsgroups`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
    , [`datasets.fetch_20newsgroups_vectorized`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized")
    , [`datasets.fetch_lfw_people`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html#sklearn.datasets.fetch_lfw_people "sklearn.datasets.fetch_lfw_people")
     and [`datasets.fetch_lfw_pairs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_pairs.html#sklearn.datasets.fetch_lfw_pairs "sklearn.datasets.fetch_lfw_pairs")
    . This only affects Python versions `>=3.10.0,<=3.10.11` and `>=3.11.0,<=3.11.3`. By [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    . [#31685](https://github.com/scikit-learn/scikit-learn/pull/31685)
    

### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-inspection "Link to this heading")

*   Fix Fix multiple issues in the multiclass setting of [`inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
    :
    
    *   `contour` plotting now correctly shows the decision boundary.
        
    *   `cmap` and `colors` are now properly ignored in favor of `multiclass_colors`.
        
    *   Linear segmented colormaps are now fully supported.
        
    
    By [Yunjie Lin](https://github.com/jshn9515)
     [#31553](https://github.com/scikit-learn/scikit-learn/pull/31553)
    

### [`sklearn.naive_bayes`](https://scikit-learn.org/stable/api/sklearn.naive_bayes.html#module-sklearn.naive_bayes "sklearn.naive_bayes")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-naive-bayes "Link to this heading")

*   Fix [`naive_bayes.CategoricalNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html#sklearn.naive_bayes.CategoricalNB "sklearn.naive_bayes.CategoricalNB")
     now correctly declares that it accepts categorical features in the tags returned by its `__sklearn_tags__` method. By [Olivier Grisel](https://github.com/ogrisel)
     [#31556](https://github.com/scikit-learn/scikit-learn/pull/31556)
    

### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-utils "Link to this heading")

*   Fix Fixed a spurious warning (about the number of unique classes being greater than 50% of the number of samples) that could occur when passing `classes` [`utils.multiclass.type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
    . By [Sascha D. Krauss](https://github.com/saskra)
    . [#31584](https://github.com/scikit-learn/scikit-learn/pull/31584)
    

Version 1.7.0[#](https://scikit-learn.org/stable/whats_new/v1.7.html#version-1-7-0 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**June 2025**

### Changed models[#](https://scikit-learn.org/stable/whats_new/v1.7.html#changed-models "Link to this heading")

*   Fix Change the `ConvergenceWarning` message of estimators that rely on the `"lbfgs"` optimizer internally to be more informative and to avoid suggesting to increase the maximum number of iterations when it is not user-settable or when the convergence problem happens before reaching it. By [Olivier Grisel](https://github.com/ogrisel)
    . [#31316](https://github.com/scikit-learn/scikit-learn/pull/31316)
    

### Changes impacting many modules[#](https://scikit-learn.org/stable/whats_new/v1.7.html#changes-impacting-many-modules "Link to this heading")

*   Sparse update: As part of the SciPy change from spmatrix to sparray, all internal use of sparse now supports both sparray and spmatrix. All manipulations of sparse objects should work for either spmatrix or sparray. This is pass 1 of a migration toward sparray (see [SciPy migration to sparray](https://docs.scipy.org/doc/scipy/reference/sparse.migration_to_sparray.html)
     By [Dan Schult](https://github.com/dschult)
     [#30858](https://github.com/scikit-learn/scikit-learn/pull/30858)
    

### Support for Array API[#](https://scikit-learn.org/stable/whats_new/v1.7.html#support-for-array-api "Link to this heading")

Additional estimators and functions have been updated to include support for all [Array API](https://data-apis.org/array-api/latest/)
 compliant inputs.

See [Array API support (experimental)](https://scikit-learn.org/stable/modules/array_api.html#array-api)
 for more details.

*   Feature [`sklearn.utils.check_consistent_length`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_consistent_length.html#sklearn.utils.check_consistent_length "sklearn.utils.check_consistent_length")
     now supports Array API compatible inputs. By [Stefanie Senger](https://github.com/StefanieSenger)
     [#29519](https://github.com/scikit-learn/scikit-learn/pull/29519)
    
*   Feature [`sklearn.metrics.explained_variance_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score "sklearn.metrics.explained_variance_score")
     and [`sklearn.metrics.mean_pinball_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
     now support Array API compatible inputs. By [Virgil Chan](https://github.com/virchan)
     [#29978](https://github.com/scikit-learn/scikit-learn/pull/29978)
    
*   Feature [`sklearn.metrics.fbeta_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#sklearn.metrics.fbeta_score "sklearn.metrics.fbeta_score")
    , [`sklearn.metrics.precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")
     and [`sklearn.metrics.recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")
     now support Array API compatible inputs. By [Omar Salman](https://github.com/OmarManzoor)
     [#30395](https://github.com/scikit-learn/scikit-learn/pull/30395)
    
*   Feature [`sklearn.utils.extmath.randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
     now support Array API compatible inputs. By [Connor Lane](https://github.com/clane9)
     and [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    . [#30819](https://github.com/scikit-learn/scikit-learn/pull/30819)
    
*   Feature [`sklearn.metrics.hamming_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "sklearn.metrics.hamming_loss")
     now support Array API compatible inputs. By [Thomas Li](https://github.com/lithomas1)
     [#30838](https://github.com/scikit-learn/scikit-learn/pull/30838)
    
*   Feature [`preprocessing.Binarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Binarizer.html#sklearn.preprocessing.Binarizer "sklearn.preprocessing.Binarizer")
     now supports Array API compatible inputs. By [Yaroslav Korobko](https://github.com/Tialo)
    , [Olivier Grisel](https://github.com/ogrisel)
    , and [Thomas Li](https://github.com/lithomas1)
    . [#31190](https://github.com/scikit-learn/scikit-learn/pull/31190)
    
*   Feature [`sklearn.metrics.jaccard_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")
     now supports Array API compatible inputs. By [Omar Salman](https://github.com/OmarManzoor)
     [#31204](https://github.com/scikit-learn/scikit-learn/pull/31204)
    
*   array-api-compat and array-api-extra are now vendored within the scikit-learn source. Users of the experimental array API standard support no longer need to install array-api-compat in their environment. by [Lucas Colley](https://github.com/lucascolley)
     [#30340](https://github.com/scikit-learn/scikit-learn/pull/30340)
    

### Metadata routing[#](https://scikit-learn.org/stable/whats_new/v1.7.html#metadata-routing "Link to this heading")

Refer to the [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

*   Feature [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
     and [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
     now support metadata routing through their `predict`, `predict_proba`, `predict_log_proba` and `decision_function` methods and pass `**params` to the underlying estimators. By [Stefanie Senger](https://github.com/StefanieSenger)
    . [#30833](https://github.com/scikit-learn/scikit-learn/pull/30833)
    

### [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#id2 "Link to this heading")

*   Enhancement [`base.BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
     now has a parameter table added to the estimators HTML representation that can be visualized with jupyter. By [Guillaume Lemaitre](https://github.com/glemaitre)
     and [Dea María Léon](https://github.com/DeaMariaLeon)
     [#30763](https://github.com/scikit-learn/scikit-learn/pull/30763)
    

### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-calibration "Link to this heading")

*   Fix [`CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     now raises `FutureWarning` instead of `UserWarning` when passing `cv="prefit`”. By [Olivier Grisel](https://github.com/ogrisel)
    
*   [`CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     with `method="sigmoid"` no longer crashes when passing `float64`\-dtyped `sample_weight` along with a base estimator that outputs `float32`\-dtyped predictions. By [Olivier Grisel](https://github.com/ogrisel)
     [#30873](https://github.com/scikit-learn/scikit-learn/pull/30873)
    

### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#id3 "Link to this heading")

*   API Change The `force_int_remainder_cols` parameter of [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     and [`compose.make_column_transformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html#sklearn.compose.make_column_transformer "sklearn.compose.make_column_transformer")
     is deprecated and will be removed in 1.9. It has no effect. By [Jérémie du Boisberranger](https://github.com/jeremiedbb)
     [#31167](https://github.com/scikit-learn/scikit-learn/pull/31167)
    

### [`sklearn.covariance`](https://scikit-learn.org/stable/api/sklearn.covariance.html#module-sklearn.covariance "sklearn.covariance")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-covariance "Link to this heading")

*   Fix Support for `n_samples == n_features` in `sklearn.covariance.MinCovDet` has been restored. By [Antony Lee](https://github.com/anntzer)
    . [#30483](https://github.com/scikit-learn/scikit-learn/pull/30483)
    

### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#id4 "Link to this heading")

*   Enhancement New parameter `return_X_y` added to [`datasets.make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
    . The default value of the parameter does not change how the function behaves. By [Success Moses](https://github.com/SuccessMoses)
     and [Adam Cooper](https://github.com/arc12)
     [#30196](https://github.com/scikit-learn/scikit-learn/pull/30196)
    

### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-decomposition "Link to this heading")

*   Feature [`DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
    , [`SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")
     and [`MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
     now have a `inverse_transform` method. By [Rémi Flamary](https://github.com/rflamary)
     [#30443](https://github.com/scikit-learn/scikit-learn/pull/30443)
    

### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-ensemble "Link to this heading")

*   Feature [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     allow for more control over the validation set used for early stopping. You can now pass data to be used for validation directly to `fit` via the arguments `X_val`, `y_val` and `sample_weight_val`. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#27124](https://github.com/scikit-learn/scikit-learn/pull/27124)
    
*   Fix [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     and [`ensemble.VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")
     validate `estimators` to make sure it is a list of tuples. By [Thomas Fan](https://github.com/thomasjpfan)
    . [#30649](https://github.com/scikit-learn/scikit-learn/pull/30649)
    

### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-feature-selection "Link to this heading")

*   Enhancement [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
     now gives access to the ranking and support in each iteration and cv step of feature selection. By [Marie S.](https://github.com/MarieSacksick)
     [#30179](https://github.com/scikit-learn/scikit-learn/pull/30179)
    
*   Fix [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
     now correctly works when the estimator is an instance of [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
     with its `l1_ratio` parameter being an array-like. By [Vasco Pereira](https://github.com/vasco-s-pereira)
    . [#31107](https://github.com/scikit-learn/scikit-learn/pull/31107)
    

### [`sklearn.gaussian_process`](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#module-sklearn.gaussian_process "sklearn.gaussian_process")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-gaussian-process "Link to this heading")

*   Enhancement [`gaussian_process.GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
     now includes a `latent_mean_and_variance` method that exposes the mean and the variance of the latent function, f, used in the Laplace approximation. By [Miguel González Duque](https://github.com/miguelgondu)
     [#22227](https://github.com/scikit-learn/scikit-learn/pull/22227)
    

### [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#id5 "Link to this heading")

*   Enhancement Add `custom_values` parameter in [`inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
    . It enables users to pass their own grid of values at which the partial dependence should be calculated. By [Freddy A. Boulton](https://github.com/freddyaboulton)
     and [Stephen Pardy](https://github.com/stephenpardy)
     [#26202](https://github.com/scikit-learn/scikit-learn/pull/26202)
    
*   Enhancement [`inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
     now supports plotting all classes for multi-class problems when `response_method` is ‘decision\_function’, ‘predict\_proba’ or ‘auto’. By [Lucy Liu](https://github.com/lucyleeow)
     [#29797](https://github.com/scikit-learn/scikit-learn/pull/29797)
    
*   Fix [`inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
     now raises an informative error when passing an empty list as the `categorical_features` parameter. `None` should be used instead to indicate that no categorical features are present. By [Pedro Lopes](https://github.com/pedroL0pes)
    . [#31146](https://github.com/scikit-learn/scikit-learn/pull/31146)
    
*   API Change [`inspection.partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
     does no longer accept integer dtype for numerical feature columns. Explicit conversion to floating point values is now required before calling this tool (and preferably even before fitting the model to inspect). By [Olivier Grisel](https://github.com/ogrisel)
     [#30409](https://github.com/scikit-learn/scikit-learn/pull/30409)
    

### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#id6 "Link to this heading")

*   Enhancement [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     and [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     now accept `l1_ratio=None` when `penalty` is not `"elasticnet"`. By [Marc Bresson](https://github.com/MarcBresson)
    . [#30730](https://github.com/scikit-learn/scikit-learn/pull/30730)
    
*   Efficiency Fitting [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     and [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     with `fit_intercept=True` is faster for sparse input `X` because an unnecessary re-computation of the sum of residuals is avoided. By [Christian Lorentzen](https://github.com/lorentzenchr)
     [#31387](https://github.com/scikit-learn/scikit-learn/pull/31387)
    
*   Fix [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     now properly pass sample weights to [`utils.class_weight.compute_class_weight`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html#sklearn.utils.class_weight.compute_class_weight "sklearn.utils.class_weight.compute_class_weight")
     when fit with `class_weight="balanced"`. By [Shruti Nath](https://github.com/snath-xoc)
     and [Olivier Grisel](https://github.com/ogrisel)
     [#30057](https://github.com/scikit-learn/scikit-learn/pull/30057)
    
*   Fix Added a new parameter `tol` to [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
     that determines the precision of the solution `coef_` when fitting on sparse data. By [Success Moses](https://github.com/SuccessMoses)
     [#30521](https://github.com/scikit-learn/scikit-learn/pull/30521)
    
*   Fix The update and initialization of the hyperparameters now properly handle sample weights in [`linear_model.BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
    . By [Antoine Baker](https://github.com/antoinebaker)
    . [#30644](https://github.com/scikit-learn/scikit-learn/pull/30644)
    
*   Fix [`linear_model.BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
     now uses the full SVD to correctly estimate the posterior covariance matrix `sigma_` when `n_samples < n_features`. By [Antoine Baker](https://github.com/antoinebaker)
     [#31094](https://github.com/scikit-learn/scikit-learn/pull/31094)
    
*   API Change The parameter `n_alphas` has been deprecated in the following classes: [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
     and [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
     and [`linear_model.MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")
     and [`linear_model.MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")
    , and will be removed in 1.9. The parameter `alphas` now supports both integers and array-likes, removing the need for `n_alphas`. From now on, only `alphas` should be set to either indicate the number of alphas to automatically generate (int) or to provide a list of alphas (array-like) to test along the regularization path. By [Siddharth Bansal](https://github.com/KANNAHWORLD)
    . [#30616](https://github.com/scikit-learn/scikit-learn/pull/30616)
    
*   API Change Using the `"liblinear"` solver for multiclass classification with a one-versus-rest scheme in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     is deprecated and will raise an error in version 1.8. Either use a solver which supports the multinomial loss or wrap the estimator in a [`sklearn.multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
     to keep applying a one-versus-rest scheme. By [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    . [#31241](https://github.com/scikit-learn/scikit-learn/pull/31241)
    

### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-manifold "Link to this heading")

*   Enhancement [`manifold.MDS`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
     will switch to use `n_init=1` by default, starting from version 1.9. By [Dmitry Kobak](https://github.com/dkobak)
     [#31117](https://github.com/scikit-learn/scikit-learn/pull/31117)
    
*   Fix [`manifold.MDS`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
     now correctly handles non-metric MDS. Furthermore, the returned stress value now corresponds to the returned embedding and normalized stress is now allowed for metric MDS. By [Dmitry Kobak](https://github.com/dkobak)
     [#30514](https://github.com/scikit-learn/scikit-learn/pull/30514)
    
*   Fix [`manifold.MDS`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
     now uses `eps=1e-6` by default and the convergence criterion was adjusted to make sense for both metric and non-metric MDS and to follow the reference R implementation. The formula for normalized stress was adjusted to follow the original definition by Kruskal. By [Dmitry Kobak](https://github.com/dkobak)
     [#31117](https://github.com/scikit-learn/scikit-learn/pull/31117)
    

### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-metrics "Link to this heading")

*   Feature [`metrics.brier_score_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
     implements the Brier score for multiclass classification problems and adds a `scale_by_half` argument. This metric is notably useful to assess both sharpness and calibration of probabilistic classifiers. See the docstrings for more details. By [Varun Aggarwal](https://github.com/aggvarun01)
    , [Olivier Grisel](https://github.com/ogrisel)
     and [Antoine Baker](https://github.com/antoinebaker)
    . [#22046](https://github.com/scikit-learn/scikit-learn/pull/22046)
    
*   Feature Add class method `from_cv_results` to [`metrics.RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")
    , which allows easy plotting of multiple ROC curves from [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
     results. By [Lucy Liu](https://github.com/lucyleeow)
     [#30399](https://github.com/scikit-learn/scikit-learn/pull/30399)
    
*   Enhancement [`metrics.det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")
    , [`metrics.DetCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_estimator "sklearn.metrics.DetCurveDisplay.from_estimator")
    , and [`metrics.DetCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_estimator "sklearn.metrics.DetCurveDisplay.from_estimator")
     now accept a `drop_intermediate` option to drop thresholds where true positives (tp) do not change from the previous or subsequent thresholds. All points with the same tp value have the same `fnr` and thus same y coordinate in a DET curve. By [Arturo Amor](https://github.com/ArturoAmorQ)
     [#29151](https://github.com/scikit-learn/scikit-learn/pull/29151)
    
*   Enhancement [`class_likelihood_ratios`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#sklearn.metrics.class_likelihood_ratios "sklearn.metrics.class_likelihood_ratios")
     now has a `replace_undefined_by` param. When there is a division by zero, the metric is undefined and the set values are returned for `LR+` and `LR-`. By [Stefanie Senger](https://github.com/StefanieSenger)
     [#29288](https://github.com/scikit-learn/scikit-learn/pull/29288)
    
*   Fix [`metrics.log_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
     now raises a `ValueError` if values of `y_true` are missing in `labels`. By [Varun Aggarwal](https://github.com/aggvarun01)
    , [Olivier Grisel](https://github.com/ogrisel)
     and [Antoine Baker](https://github.com/antoinebaker)
    . [#22046](https://github.com/scikit-learn/scikit-learn/pull/22046)
    
*   Fix [`metrics.det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")
     and [`metrics.DetCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay "sklearn.metrics.DetCurveDisplay")
     now return an extra threshold at infinity where the classifier always predicts the negative class i.e. tps = fps = 0. By [Arturo Amor](https://github.com/ArturoAmorQ)
     [#29151](https://github.com/scikit-learn/scikit-learn/pull/29151)
    
*   Fix [`class_likelihood_ratios`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#sklearn.metrics.class_likelihood_ratios "sklearn.metrics.class_likelihood_ratios")
     now raises `UndefinedMetricWarning` instead of `UserWarning` when a division by zero occurs. By [Stefanie Senger](https://github.com/StefanieSenger)
     [#29288](https://github.com/scikit-learn/scikit-learn/pull/29288)
    
*   Fix [`metrics.RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")
     will no longer set a legend when `label` is `None` in both the `line_kwargs` and the `chance_level_kw`. By [Arturo Amor](https://github.com/ArturoAmorQ)
     [#29727](https://github.com/scikit-learn/scikit-learn/pull/29727)
    
*   Fix Additional `sample_weight` checking has been added to [`metrics.mean_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
    , [`metrics.mean_pinball_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
    , [`metrics.mean_absolute_percentage_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html#sklearn.metrics.mean_absolute_percentage_error "sklearn.metrics.mean_absolute_percentage_error")
    , [`metrics.mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
    , [`metrics.root_mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#sklearn.metrics.root_mean_squared_error "sklearn.metrics.root_mean_squared_error")
    , [`metrics.mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html#sklearn.metrics.mean_squared_log_error "sklearn.metrics.mean_squared_log_error")
    , [`metrics.root_mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_log_error.html#sklearn.metrics.root_mean_squared_log_error "sklearn.metrics.root_mean_squared_log_error")
    , [`metrics.explained_variance_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score "sklearn.metrics.explained_variance_score")
    , [`metrics.r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
    , [`metrics.mean_tweedie_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html#sklearn.metrics.mean_tweedie_deviance "sklearn.metrics.mean_tweedie_deviance")
    , [`metrics.mean_poisson_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html#sklearn.metrics.mean_poisson_deviance "sklearn.metrics.mean_poisson_deviance")
    , [`metrics.mean_gamma_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_gamma_deviance.html#sklearn.metrics.mean_gamma_deviance "sklearn.metrics.mean_gamma_deviance")
     and [`metrics.d2_tweedie_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_tweedie_score.html#sklearn.metrics.d2_tweedie_score "sklearn.metrics.d2_tweedie_score")
    . `sample_weight` can only be 1D, consistent to `y_true` and `y_pred` in length or a scalar. By [Lucy Liu](https://github.com/lucyleeow)
    . [#30886](https://github.com/scikit-learn/scikit-learn/pull/30886)
    
*   Fix [`d2_log_loss_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_log_loss_score.html#sklearn.metrics.d2_log_loss_score "sklearn.metrics.d2_log_loss_score")
     now properly handles the case when `labels` is passed and not all of the labels are present in `y_true`. By [Vassilis Margonis](https://github.com/vmargonis)
     [#30903](https://github.com/scikit-learn/scikit-learn/pull/30903)
    
*   Fix Fix [`metrics.adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")
     numerical issue when number of classes and samples is low. By [Hleb Levitski](https://github.com/glevv)
     [#31065](https://github.com/scikit-learn/scikit-learn/pull/31065)
    
*   API Change The `sparse` parameter of [`metrics.fowlkes_mallows_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fowlkes_mallows_score.html#sklearn.metrics.fowlkes_mallows_score "sklearn.metrics.fowlkes_mallows_score")
     is deprecated and will be removed in 1.9. It has no effect. By [Luc Rocher](https://github.com/cynddl)
    . [#28981](https://github.com/scikit-learn/scikit-learn/pull/28981)
    
*   API Change The `raise_warning` parameter of [`metrics.class_likelihood_ratios`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#sklearn.metrics.class_likelihood_ratios "sklearn.metrics.class_likelihood_ratios")
     is deprecated and will be removed in 1.9. An `UndefinedMetricWarning` will always be raised in case of a division by zero. By [Stefanie Senger](https://github.com/StefanieSenger)
    . [#29288](https://github.com/scikit-learn/scikit-learn/pull/29288)
    
*   API Change In [`sklearn.metrics.RocCurveDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")
    , the argument `y_pred` has been renamed to `y_score` to better reflect its purpose. `y_pred` will be removed in 1.9. By [Bagus Tris Atmaja](https://github.com/bagustris)
     in [#29865](https://github.com/scikit-learn/scikit-learn/pull/29865)
    

### [`sklearn.mixture`](https://scikit-learn.org/stable/api/sklearn.mixture.html#module-sklearn.mixture "sklearn.mixture")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-mixture "Link to this heading")

*   Feature Added an attribute `lower_bounds_` in the `mixture.BaseMixture` class to save the list of lower bounds for each iteration thereby providing insights into the convergence behavior of mixture models like [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
    . By [Manideep Yenugula](https://github.com/myenugula)
     [#28559](https://github.com/scikit-learn/scikit-learn/pull/28559)
    
*   Efficiency Simplified redundant computation when estimating covariances in [`GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     with a `covariance_type="spherical"` or `covariance_type="diag"`. By [Leonce Mekinda](https://github.com/mekleo)
     and [Olivier Grisel](https://github.com/ogrisel)
     [#30414](https://github.com/scikit-learn/scikit-learn/pull/30414)
    
*   Efficiency [`GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     now consistently operates at `float32` precision when fitted with `float32` data to improve training speed and memory efficiency. Previously, part of the computation would be implicitly cast to `float64`. By [Olivier Grisel](https://github.com/ogrisel)
     and [Omar Salman](https://github.com/OmarManzoor)
    . [#30415](https://github.com/scikit-learn/scikit-learn/pull/30415)
    

### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-model-selection "Link to this heading")

*   Fix Hyper-parameter optimizers such as [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     now forward `sample_weight` to the scorer even when metadata routing is not enabled. By [Antoine Baker](https://github.com/antoinebaker)
     [#30743](https://github.com/scikit-learn/scikit-learn/pull/30743)
    

### [`sklearn.multiclass`](https://scikit-learn.org/stable/api/sklearn.multiclass.html#module-sklearn.multiclass "sklearn.multiclass")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-multiclass "Link to this heading")

*   Fix The `predict_proba` method of [`sklearn.multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
     now returns zero for all classes when all inner estimators never predict their positive class. By [Luis M. B. Varona](https://github.com/Luis-Varona)
    , [Marc Bresson](https://github.com/MarcBresson)
    , and [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    . [#31228](https://github.com/scikit-learn/scikit-learn/pull/31228)
    

### [`sklearn.multioutput`](https://scikit-learn.org/stable/api/sklearn.multioutput.html#module-sklearn.multioutput "sklearn.multioutput")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-multioutput "Link to this heading")

*   Enhancement The parameter `base_estimator` has been deprecated in favour of `estimator` for [`multioutput.RegressorChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.RegressorChain.html#sklearn.multioutput.RegressorChain "sklearn.multioutput.RegressorChain")
     and [`multioutput.ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
    . By [Success Moses](https://github.com/SuccessMoses)
     and [dikraMasrour](https://github.com/dikra_masrour)
     [#30152](https://github.com/scikit-learn/scikit-learn/pull/30152)
    

### [`sklearn.neural_network`](https://scikit-learn.org/stable/api/sklearn.neural_network.html#module-sklearn.neural_network "sklearn.neural_network")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-neural-network "Link to this heading")

*   Feature Added support for `sample_weight` in [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     and [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
    . By [Zach Shu](https://github.com/zshu115x)
     and [Christian Lorentzen](https://github.com/lorentzenchr)
     [#30155](https://github.com/scikit-learn/scikit-learn/pull/30155)
    
*   Feature Added parameter for `loss` in [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
     with options `"squared_error"` (default) and `"poisson"` (new). By [Christian Lorentzen](https://github.com/lorentzenchr)
     [#30712](https://github.com/scikit-learn/scikit-learn/pull/30712)
    
*   Fix [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
     now raises an informative error when `early_stopping` is set and the computed validation set is too small. By [David Shumway](https://github.com/davidshumway)
    . [#24788](https://github.com/scikit-learn/scikit-learn/pull/24788)
    

### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#id7 "Link to this heading")

*   Enhancement Expose the `verbose_feature_names_out` argument in the [`pipeline.make_union`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_union.html#sklearn.pipeline.make_union "sklearn.pipeline.make_union")
     function, allowing users to control feature name uniqueness in the [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
    . By [Abhijeetsingh Meena](https://github.com/Ethan0456)
     [#30406](https://github.com/scikit-learn/scikit-learn/pull/30406)
    

### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-preprocessing "Link to this heading")

*   Enhancement [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
     with `strategy="uniform"` now accepts `sample_weight`. Additionally with `strategy="quantile"` the `quantile_method` can now be specified (in the future `quantile_method="averaged_inverted_cdf"` will become the default). By [Shruti Nath](https://github.com/snath-xoc)
     and [Olivier Grisel](https://github.com/ogrisel)
     [#29907](https://github.com/scikit-learn/scikit-learn/pull/29907)
    
*   Fix [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
     now uses weighted resampling when sample weights are given and subsampling is used. This may change results even when not using sample weights, although in absolute and not in terms of statistical properties. By [Shruti Nath](https://github.com/snath-xoc)
     and [Jérémie du Boisberranger](https://github.com/jeremiedbb)
     [#29907](https://github.com/scikit-learn/scikit-learn/pull/29907)
    
*   Fix Now using `scipy.stats.yeojohnson` instead of our own implementation of the Yeo-Johnson transform. Fixed numerical stability (mostly overflows) of the Yeo-Johnson transform with `PowerTransformer(method="yeo-johnson")` when scipy version is `>= 1.12`. Initial PR by [Xuefeng Xu](https://github.com/xuefeng-xu)
     completed by [Mohamed Yaich](https://github.com/yaichm)
    , [Oussama Er-rabie](https://github.com/eroussama)
    , [Mohammed Yaslam Dlimi](https://github.com/Dlimim)
    , [Hamza Zaroual](https://github.com/HamzaLuffy)
    , [Amine Hannoun](https://github.com/AmineHannoun)
     and [Sylvain Marié](https://github.com/smarie)
    . [#31227](https://github.com/scikit-learn/scikit-learn/pull/31227)
    

### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-svm "Link to this heading")

*   Fix [`svm.LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
     now properly passes sample weights to [`utils.class_weight.compute_class_weight`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html#sklearn.utils.class_weight.compute_class_weight "sklearn.utils.class_weight.compute_class_weight")
     when fit with `class_weight="balanced"`. By [Shruti Nath](https://github.com/snath-xoc)
     [#30057](https://github.com/scikit-learn/scikit-learn/pull/30057)
    

### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.7.html#id8 "Link to this heading")

*   Enhancement [`utils.multiclass.type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
     raises a warning when the number of unique classes is greater than 50% of the number of samples. This warning is raised only if `y` has more than 20 samples. By [Rahil Parikh](https://github.com/rprkh)
    . [#26335](https://github.com/scikit-learn/scikit-learn/pull/26335)
    
*   Enhancement :func: `resample` now handles sample weights which allows weighted resampling. By [Shruti Nath](https://github.com/snath-xoc)
     and [Olivier Grisel](https://github.com/ogrisel)
     [#29907](https://github.com/scikit-learn/scikit-learn/pull/29907)
    
*   Enhancement [`utils.class_weight.compute_class_weight`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html#sklearn.utils.class_weight.compute_class_weight "sklearn.utils.class_weight.compute_class_weight")
     now properly accounts for sample weights when using strategy “balanced” to calculate class weights. By [Shruti Nath](https://github.com/snath-xoc)
     [#30057](https://github.com/scikit-learn/scikit-learn/pull/30057)
    
*   Enhancement Warning filters from the main process are propagated to joblib workers. By [Thomas Fan](https://github.com/thomasjpfan)
     [#30380](https://github.com/scikit-learn/scikit-learn/pull/30380)
    
*   Enhancement The private helper function [`utils._safe_indexing`](https://scikit-learn.org/stable/modules/generated/sklearn.utils._safe_indexing.html#sklearn.utils._safe_indexing "sklearn.utils._safe_indexing")
     now officially supports pyarrow data. For instance, passing a pyarrow `Table` as `X` in a [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     is now possible. By [Christian Lorentzen](https://github.com/lorentzenchr)
     [#31040](https://github.com/scikit-learn/scikit-learn/pull/31040)
    
*   Fix In `utils.estimator_checks` we now enforce for binary classifiers a binary `y` by taking the minimum as the negative class instead of the first element, which makes it robust to `y` shuffling. It prevents two checks from wrongly failing on binary classifiers. By [Antoine Baker](https://github.com/antoinebaker)
    . [#30775](https://github.com/scikit-learn/scikit-learn/pull/30775)
    
*   Fix [`utils.extmath.randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")
     and [`utils.extmath.randomized_range_finder`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_range_finder.html#sklearn.utils.extmath.randomized_range_finder "sklearn.utils.extmath.randomized_range_finder")
     now validate their input array to fail early with an informative error message on invalid input. By [Connor Lane](https://github.com/clane9)
    . [#30819](https://github.com/scikit-learn/scikit-learn/pull/30819)
    

Code and documentation contributors

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 1.6, including:

4hm3d, Aaron Schumacher, Abhijeetsingh Meena, Acciaro Gennaro Daniele, Achraf Tasfaout, Adriano Leão, Adrien Linares, Adrin Jalali, Agriya Khetarpal, Aiden Frank, Aitsaid Azzedine Idir, ajay-sentry, Akanksha Mhadolkar, Alexandre Abraham, Alfredo Saucedo, Anderson Chaves, Andres Guzman-Ballen, Aniruddha Saha, antoinebaker, Antony Lee, Arjun S, ArthurDbrn, Arturo, Arturo Amor, ash, Ashton Powell, ayoub.agouzoul, Ayrat, Bagus Tris Atmaja, Benjamin Danek, Boney Patel, Camille Troillard, Chems Ben, Christian Lorentzen, Christian Veenhuis, Christine P. Chai, claudio, Code\_Blooded, Colas, Colin Coe, Connor Lane, Corey Farwell, Daniel Agyapong, Dan Schult, Dea María Léon, Deepak Saldanha, dependabot\[bot\], Dhyey Findoriya, Dimitri Papadopoulos Orfanos, Dmitry Kobak, Domenico, elenafillo, Elham Babaei, emelia-hdz, EmilyXinyi, Emma Carballal, Eric Larson, Eugen-Bleck, Evgeni Burovski, fabianhenning, Gael Varoquaux, GaetandeCast, Gil Ramot, Gonçalo Guiomar, Gordon Grey, Goutam, G Sreeja, Guillaume Lemaitre, Haesun Park, hakan çanakçı, Hanjun Kim, Helder Geovane Gomes de Lima, Henri Bonamy, Hleb Levitski, Hugo Boulenger, IlyaSolomatin, Irene, Jérémie du Boisberranger, Jérôme Dockès, JoaoRodriguesIST, Joel Nothman, Joris Van den Bossche, Josh, jshn9515, KALLA GANASEKHAR, Kevin Klein, Krishnan Vignesh, kryggird, Loic Esteve, Lucas Colley, Luc Rocher, Lucy Liu, Luis M. B. Varona, lunovian, Mamduh Zabidi, Marc Bresson, Marco Edward Gorelli, Marco Maggi, Marek Pokropiński, Maren Westermann, Marie Sacksick, Marija Vlajic, Martin Jurča, Mayank Raj, Michael Burkhart, Miguel González Duque, Mihir Waknis, Miro Hrončok, Mohamed Ali SRIR, Mohamed DHIFALLAH, mohammed benyamna, Mohit Singh Thakur, Mounir Lbath, myenugula, Natalia Mokeeva, Nicolas Bolle, Olivier Grisel, omahs, Omar Salman, Pedro Lopes, Pedro Olivares, Peter Holzer, Prashant Bansal, Preyas Shah, Radovenchyk, Rahil Parikh, Rémi Flamary, Reshama Shaikh, Richard Harris, Rishab Saini, rolandrmgservices, SanchitD, Santiago Castro, Santiago Víquez, saskra, scikit-learn-bot, Scott Huberty, Shashank S, Shaurya Bisht, Shivam, Shruti Nath, Siddharth Bansal, SIKAI ZHANG, Simarjot Sidhu, sisird864, SiyuJin-1, Somdutta Banerjee, Sortofamudkip, sotagg, Sourabh Kumar, Stefan, Stefanie Senger, Stefano Gaspari, Steffen Rehberg, Stephen Pardy, Success Moses, Sylvain Combettes, Tahar Allouche, Thomas J. Fan, Thomas Li, ThorbenMaa, Tim Head, Tingwei Zhu, TJ Norred, Umberto Fasci, UV, Vasco Pereira, Vassilis Margonis, Velislav Babatchev, Victoria Shevchenko, viktor765, Vipsa Kamani, VirenPassi, Virgil Chan, vpz, Xiao Yuan, Yaich Mohamed, Yair Shimony, Yao Xiao, Yaroslav Halchenko, Yulia Vilensky, Yuvi Panda

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)