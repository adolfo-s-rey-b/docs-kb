[Skip to main content](https://scikit-learn.org/stable/whats_new/v1.6.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v1.6.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v1.6.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v1.6.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v1.6.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v1.6.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v1.6.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v1.6.html)

Collapse Sidebar Expand Sidebar

Version 1.6[#](https://scikit-learn.org/stable/whats_new/v1.6.html#version-1-6 "Link to this heading")

=======================================================================================================

For a short description of the main highlights of the release, please refer to [Release Highlights for scikit-learn 1.6](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html#sphx-glr-auto-examples-release-highlights-plot-release-highlights-1-6-0-py)
.

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 1.6.1[#](https://scikit-learn.org/stable/whats_new/v1.6.html#version-1-6-1 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**January 2025**

### Changed models[#](https://scikit-learn.org/stable/whats_new/v1.6.html#changed-models "Link to this heading")

*   Fix The `tags.input_tags.sparse` flag was corrected for a majority of estimators. By [Antoine Baker](https://github.com/antoinebaker)
     [#30187](https://github.com/scikit-learn/scikit-learn/pull/30187)
    

### Changes impacting many modules[#](https://scikit-learn.org/stable/whats_new/v1.6.html#changes-impacting-many-modules "Link to this heading")

*   Fix `_more_tags`, `_get_tags`, and `_safe_tags` are now raising a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "(in Python v3.14)")
     instead of a [`FutureWarning`](https://docs.python.org/3/library/exceptions.html#FutureWarning "(in Python v3.14)")
     to only notify developers instead of end-users. By [Guillaume Lemaitre](https://github.com/glemaitre)
     in [#30573](https://github.com/scikit-learn/scikit-learn/pull/30573)
    

### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-metrics "Link to this heading")

*   Fix Fix regression when scikit-learn metric called on PyTorch CPU tensors would raise an error (with array API dispatch disabled which is the default). By [Loïc Estève](https://github.com/lesteve)
     [#30454](https://github.com/scikit-learn/scikit-learn/pull/30454)
    

### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-model-selection "Link to this heading")

*   Fix [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
    , [`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
    , and [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
     now accept `params=None` when metadata routing is enabled. By [Adrin Jalali](https://github.com/adrinjalali)
     [#30451](https://github.com/scikit-learn/scikit-learn/pull/30451)
    

### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-tree "Link to this heading")

*   Fix Use `log2` instead of `ln` for building trees to maintain behavior of previous versions. By [Thomas Fan](https://github.com/thomasjpfan)
     [#30557](https://github.com/scikit-learn/scikit-learn/pull/30557)
    

### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-utils "Link to this heading")

*   Enhancement `utils.estimator_checks.check_estimator_sparse_tag` ensures that the estimator tag `input_tags.sparse` is consistent with its `fit` method (accepting sparse input `X` or raising the appropriate error). By [Antoine Baker](https://github.com/antoinebaker)
     [#30187](https://github.com/scikit-learn/scikit-learn/pull/30187)
    
*   Fix Raise a `DeprecationWarning` when there is no concrete implementation of `__sklearn_tags__` in the MRO of the estimator. We request to inherit from `BaseEstimator` that implements `__sklearn_tags__`. By [Guillaume Lemaitre](https://github.com/glemaitre)
     [#30516](https://github.com/scikit-learn/scikit-learn/pull/30516)
    

Version 1.6.0[#](https://scikit-learn.org/stable/whats_new/v1.6.html#version-1-6-0 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**December 2024**

### Changes impacting many modules[#](https://scikit-learn.org/stable/whats_new/v1.6.html#id1 "Link to this heading")

*   Enhancement `__sklearn_tags__` was introduced for setting tags in estimators. More details in [Estimator Tags](https://scikit-learn.org/stable/developers/develop.html#estimator-tags)
    . By [Thomas Fan](https://github.com/thomasjpfan)
     and [Adrin Jalali](https://github.com/adrinjalali)
     [#29677](https://github.com/scikit-learn/scikit-learn/pull/29677)
    
*   Enhancement Scikit-learn classes and functions can be used while only having a `import sklearn` import line. For example, `import sklearn; sklearn.svm.SVC()` now works. By [Thomas Fan](https://github.com/thomasjpfan)
     [#29793](https://github.com/scikit-learn/scikit-learn/pull/29793)
    
*   Fix Classes [`metrics.ConfusionMatrixDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay "sklearn.metrics.ConfusionMatrixDisplay")
    , [`metrics.RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")
    , [`calibration.CalibrationDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay "sklearn.calibration.CalibrationDisplay")
    , [`metrics.PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")
    , [`metrics.PredictionErrorDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay "sklearn.metrics.PredictionErrorDisplay")
     and [`inspection.PartialDependenceDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "sklearn.inspection.PartialDependenceDisplay")
     now properly handle Matplotlib aliases for style parameters (e.g., `c` and `color`, `ls` and `linestyle`, etc). By [Joseph Barbier](https://github.com/JosephBARBIERDARNAL)
     [#30023](https://github.com/scikit-learn/scikit-learn/pull/30023)
    
*   API Change [`utils.validation.validate_data`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.validate_data.html#sklearn.utils.validation.validate_data "sklearn.utils.validation.validate_data")
     is introduced and replaces previously private `base.BaseEstimator._validate_data` method. This is intended for third party estimator developers, who should use this function in most cases instead of [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     and [`utils.check_X_y`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html#sklearn.utils.check_X_y "sklearn.utils.check_X_y")
    . By [Adrin Jalali](https://github.com/adrinjalali)
     [#29696](https://github.com/scikit-learn/scikit-learn/pull/29696)
    

### Support for Array API[#](https://scikit-learn.org/stable/whats_new/v1.6.html#support-for-array-api "Link to this heading")

Additional estimators and functions have been updated to include support for all [Array API](https://data-apis.org/array-api/latest/)
 compliant inputs.

See [Array API support (experimental)](https://scikit-learn.org/stable/modules/array_api.html#array-api)
 for more details.

*   Feature [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
    , [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
    , [`model_selection.HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
     and [`model_selection.HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
     now support Array API compatible inputs when their base estimators do. By [Tim Head](https://github.com/betatim)
     and [Olivier Grisel](https://github.com/ogrisel)
     [#27096](https://github.com/scikit-learn/scikit-learn/pull/27096)
    
*   Feature [`sklearn.metrics.f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")
     now supports Array API compatible inputs. By [Omar Salman](https://github.com/OmarManzoor)
     [#27369](https://github.com/scikit-learn/scikit-learn/pull/27369)
    
*   Feature [`preprocessing.LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder")
     now supports Array API compatible inputs. By [Omar Salman](https://github.com/OmarManzoor)
     [#27381](https://github.com/scikit-learn/scikit-learn/pull/27381)
    
*   Feature [`sklearn.metrics.mean_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
     now supports Array API compatible inputs. By [Edoardo Abati](https://github.com/EdAbati)
     [#27736](https://github.com/scikit-learn/scikit-learn/pull/27736)
    
*   Feature [`sklearn.metrics.mean_tweedie_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html#sklearn.metrics.mean_tweedie_deviance "sklearn.metrics.mean_tweedie_deviance")
     now supports Array API compatible inputs. By [Thomas Li](https://github.com/lithomas1)
     [#28106](https://github.com/scikit-learn/scikit-learn/pull/28106)
    
*   Feature [`sklearn.metrics.pairwise.cosine_similarity`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#sklearn.metrics.pairwise.cosine_similarity "sklearn.metrics.pairwise.cosine_similarity")
     now supports Array API compatible inputs. By [Edoardo Abati](https://github.com/EdAbati)
     [#29014](https://github.com/scikit-learn/scikit-learn/pull/29014)
    
*   Feature [`sklearn.metrics.pairwise.paired_cosine_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_cosine_distances.html#sklearn.metrics.pairwise.paired_cosine_distances "sklearn.metrics.pairwise.paired_cosine_distances")
     now supports Array API compatible inputs. By [Edoardo Abati](https://github.com/EdAbati)
     [#29112](https://github.com/scikit-learn/scikit-learn/pull/29112)
    
*   Feature `sklearn.metrics.cluster.entropy` now supports Array API compatible inputs. By [Yaroslav Korobko](https://github.com/Tialo)
     [#29141](https://github.com/scikit-learn/scikit-learn/pull/29141)
    
*   Feature [`sklearn.metrics.mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
     now supports Array API compatible inputs. By [Yaroslav Korobko](https://github.com/Tialo)
     [#29142](https://github.com/scikit-learn/scikit-learn/pull/29142)
    
*   Feature [`sklearn.metrics.pairwise.additive_chi2_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html#sklearn.metrics.pairwise.additive_chi2_kernel "sklearn.metrics.pairwise.additive_chi2_kernel")
     now supports Array API compatible inputs. By [Yaroslav Korobko](https://github.com/Tialo)
     [#29144](https://github.com/scikit-learn/scikit-learn/pull/29144)
    
*   Feature [`sklearn.metrics.d2_tweedie_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_tweedie_score.html#sklearn.metrics.d2_tweedie_score "sklearn.metrics.d2_tweedie_score")
     now supports Array API compatible inputs. By [Emily Chen](https://github.com/EmilyXinyi)
     [#29207](https://github.com/scikit-learn/scikit-learn/pull/29207)
    
*   Feature [`sklearn.metrics.max_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.max_error.html#sklearn.metrics.max_error "sklearn.metrics.max_error")
     now supports Array API compatible inputs. By [Edoardo Abati](https://github.com/EdAbati)
     [#29212](https://github.com/scikit-learn/scikit-learn/pull/29212)
    
*   Feature [`sklearn.metrics.mean_poisson_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html#sklearn.metrics.mean_poisson_deviance "sklearn.metrics.mean_poisson_deviance")
     now supports Array API compatible inputs. By [Emily Chen](https://github.com/EmilyXinyi)
     [#29227](https://github.com/scikit-learn/scikit-learn/pull/29227)
    
*   Feature [`sklearn.metrics.mean_gamma_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_gamma_deviance.html#sklearn.metrics.mean_gamma_deviance "sklearn.metrics.mean_gamma_deviance")
     now supports Array API compatible inputs. By [Emily Chen](https://github.com/EmilyXinyi)
     [#29239](https://github.com/scikit-learn/scikit-learn/pull/29239)
    
*   Feature [`sklearn.metrics.pairwise.cosine_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_distances.html#sklearn.metrics.pairwise.cosine_distances "sklearn.metrics.pairwise.cosine_distances")
     now supports Array API compatible inputs. By [Emily Chen](https://github.com/EmilyXinyi)
     [#29265](https://github.com/scikit-learn/scikit-learn/pull/29265)
    
*   Feature [`sklearn.metrics.pairwise.chi2_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.chi2_kernel.html#sklearn.metrics.pairwise.chi2_kernel "sklearn.metrics.pairwise.chi2_kernel")
     now supports Array API compatible inputs. By [Yaroslav Korobko](https://github.com/Tialo)
     [#29267](https://github.com/scikit-learn/scikit-learn/pull/29267)
    
*   Feature [`sklearn.metrics.mean_absolute_percentage_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html#sklearn.metrics.mean_absolute_percentage_error "sklearn.metrics.mean_absolute_percentage_error")
     now supports Array API compatible inputs. By [Emily Chen](https://github.com/EmilyXinyi)
     [#29300](https://github.com/scikit-learn/scikit-learn/pull/29300)
    
*   Feature [`sklearn.metrics.pairwise.paired_euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_euclidean_distances.html#sklearn.metrics.pairwise.paired_euclidean_distances "sklearn.metrics.pairwise.paired_euclidean_distances")
     now supports Array API compatible inputs. By [Emily Chen](https://github.com/EmilyXinyi)
     [#29389](https://github.com/scikit-learn/scikit-learn/pull/29389)
    
*   Feature [`sklearn.metrics.pairwise.euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html#sklearn.metrics.pairwise.euclidean_distances "sklearn.metrics.pairwise.euclidean_distances")
     and [`sklearn.metrics.pairwise.rbf_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html#sklearn.metrics.pairwise.rbf_kernel "sklearn.metrics.pairwise.rbf_kernel")
     now support Array API compatible inputs. By [Omar Salman](https://github.com/OmarManzoor)
     [#29433](https://github.com/scikit-learn/scikit-learn/pull/29433)
    
*   Feature [`sklearn.metrics.pairwise.linear_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.linear_kernel.html#sklearn.metrics.pairwise.linear_kernel "sklearn.metrics.pairwise.linear_kernel")
    , [`sklearn.metrics.pairwise.sigmoid_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html#sklearn.metrics.pairwise.sigmoid_kernel "sklearn.metrics.pairwise.sigmoid_kernel")
    , and [`sklearn.metrics.pairwise.polynomial_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html#sklearn.metrics.pairwise.polynomial_kernel "sklearn.metrics.pairwise.polynomial_kernel")
     now support Array API compatible inputs. By [Omar Salman](https://github.com/OmarManzoor)
     [#29475](https://github.com/scikit-learn/scikit-learn/pull/29475)
    
*   Feature [`sklearn.metrics.mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html#sklearn.metrics.mean_squared_log_error "sklearn.metrics.mean_squared_log_error")
     and [`sklearn.metrics.root_mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_log_error.html#sklearn.metrics.root_mean_squared_log_error "sklearn.metrics.root_mean_squared_log_error")
     now support Array API compatible inputs. By [Virgil Chan](https://github.com/virchan)
     [#29709](https://github.com/scikit-learn/scikit-learn/pull/29709)
    
*   Feature [`preprocessing.MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
     with `clip=True` now supports Array API compatible inputs. By [Shreekant Nandiyawar](https://github.com/Shree7676)
     [#29751](https://github.com/scikit-learn/scikit-learn/pull/29751)
    
*   Support for the soon to be deprecated `cupy.array_api` module has been removed in favor of directly supporting the top level `cupy` module, possibly via the `array_api_compat.cupy` compatibility wrapper. By [Olivier Grisel](https://github.com/ogrisel)
     [#29639](https://github.com/scikit-learn/scikit-learn/pull/29639)
    

### Metadata routing[#](https://scikit-learn.org/stable/whats_new/v1.6.html#metadata-routing "Link to this heading")

Refer to the [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

*   Feature [`semi_supervised.SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
     now supports metadata routing. The fit method now accepts `**fit_params` which are passed to the underlying estimators via their `fit` methods. In addition, the [`predict`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier.predict "sklearn.semi_supervised.SelfTrainingClassifier.predict")
    , [`predict_proba`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier.predict_proba "sklearn.semi_supervised.SelfTrainingClassifier.predict_proba")
    , [`predict_log_proba`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier.predict_log_proba "sklearn.semi_supervised.SelfTrainingClassifier.predict_log_proba")
    , [`score`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier.score "sklearn.semi_supervised.SelfTrainingClassifier.score")
     and [`decision_function`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier.decision_function "sklearn.semi_supervised.SelfTrainingClassifier.decision_function")
     methods also accept `**params` which are passed to the underlying estimators via their respective methods. By [Adam Li](https://github.com/adam2392)
     [#28494](https://github.com/scikit-learn/scikit-learn/pull/28494)
    
*   Feature [`ensemble.StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")
     and [`ensemble.StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")
     now support metadata routing and pass `**fit_params` to the underlying estimators via their `fit` methods. By [Stefanie Senger](https://github.com/StefanieSenger)
     [#28701](https://github.com/scikit-learn/scikit-learn/pull/28701)
    
*   Feature [`model_selection.learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
     now supports metadata routing for the `fit` method of its estimator and for its underlying CV splitter and scorer. By [Stefanie Senger](https://github.com/StefanieSenger)
     [#28975](https://github.com/scikit-learn/scikit-learn/pull/28975)
    
*   Feature [`compose.TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
     now supports metadata routing in its [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor.fit "sklearn.compose.TransformedTargetRegressor.fit")
     and [`predict`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor.predict "sklearn.compose.TransformedTargetRegressor.predict")
     methods and routes the corresponding params to the underlying regressor. By [Omar Salman](https://github.com/OmarManzoor)
     [#29136](https://github.com/scikit-learn/scikit-learn/pull/29136)
    
*   Feature [`feature_selection.SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
     now supports metadata routing in its `fit` method and passes the corresponding params to the [`model_selection.cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
     function. By [Omar Salman](https://github.com/OmarManzoor)
     [#29260](https://github.com/scikit-learn/scikit-learn/pull/29260)
    
*   Feature [`model_selection.permutation_test_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#sklearn.model_selection.permutation_test_score "sklearn.model_selection.permutation_test_score")
     now supports metadata routing for the `fit` method of its estimator and for its underlying CV splitter and scorer. By [Adam Li](https://github.com/adam2392)
     [#29266](https://github.com/scikit-learn/scikit-learn/pull/29266)
    
*   Feature [`feature_selection.RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
     and [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
     now support metadata routing. By [Omar Salman](https://github.com/OmarManzoor)
     [#29312](https://github.com/scikit-learn/scikit-learn/pull/29312)
    
*   Feature [`model_selection.validation_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve "sklearn.model_selection.validation_curve")
     now supports metadata routing for the `fit` method of its estimator and for its underlying CV splitter and scorer. By [Stefanie Senger](https://github.com/StefanieSenger)
     [#29329](https://github.com/scikit-learn/scikit-learn/pull/29329)
    
*   Fix Metadata is routed correctly to grouped CV splitters via [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     and [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
     and `UnsetMetadataPassedError` is fixed for [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
     with default scoring. By [Stefanie Senger](https://github.com/StefanieSenger)
     [#29634](https://github.com/scikit-learn/scikit-learn/pull/29634)
    
*   Fix Many method arguments which shouldn’t be included in the routing mechanism are now excluded and the `set_{method}_request` methods are not generated for them. By [Adrin Jalali](https://github.com/adrinjalali)
     [#29920](https://github.com/scikit-learn/scikit-learn/pull/29920)
    

### Dropping official support for PyPy[#](https://scikit-learn.org/stable/whats_new/v1.6.html#dropping-official-support-for-pypy "Link to this heading")

Due to limited maintainer resources and small number of users, official PyPy support has been dropped. Some parts of scikit-learn may still work but PyPy is not tested anymore in the scikit-learn Continuous Integration. By [Loïc Estève](https://github.com/lesteve)
 [#29128](https://github.com/scikit-learn/scikit-learn/pull/29128)

### Dropping support for building with setuptools[#](https://scikit-learn.org/stable/whats_new/v1.6.html#dropping-support-for-building-with-setuptools "Link to this heading")

From scikit-learn 1.6 onwards, support for building with setuptools has been removed. Meson is the only supported way to build scikit-learn. By [Loïc Estève](https://github.com/lesteve)
 [#29400](https://github.com/scikit-learn/scikit-learn/pull/29400)

### Free-threaded CPython 3.13 support[#](https://scikit-learn.org/stable/whats_new/v1.6.html#free-threaded-cpython-3-13-support "Link to this heading")

scikit-learn has preliminary support for free-threaded CPython, in particular free-threaded wheels are available for all of our supported platforms.

Free-threaded (also known as nogil) CPython 3.13 is an experimental version of CPython 3.13 which aims at enabling efficient multi-threaded use cases by removing the Global Interpreter Lock (GIL).

For more details about free-threaded CPython see [py-free-threading doc](https://py-free-threading.github.io/)
, in particular [how to install a free-threaded CPython](https://py-free-threading.github.io/installing_cpython/)
 and [Ecosystem compatibility tracking](https://py-free-threading.github.io/tracking/)
.

Feel free to try free-threaded on your use case and report any issues!

By [Loïc Estève](https://github.com/lesteve)
 and many other people in the wider Scientific Python and CPython ecosystem, for example [Nathan Goldbaum](https://github.com/ngoldbaum)
, [Ralf Gommers](https://github.com/rgommers)
, [Edgar Andrés Margffoy Tuay](https://github.com/andfoy)
. [#30360](https://github.com/scikit-learn/scikit-learn/pull/30360)

### [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-base "Link to this heading")

*   Enhancement Added a function [`base.is_clusterer`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_clusterer.html#sklearn.base.is_clusterer "sklearn.base.is_clusterer")
     which determines whether a given estimator is of category clusterer. By [Christian Veenhuis](https://github.com/ChVeen)
     [#28936](https://github.com/scikit-learn/scikit-learn/pull/28936)
    
*   API Change Passing a class object to [`is_classifier`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_classifier.html#sklearn.base.is_classifier "sklearn.base.is_classifier")
    , [`is_regressor`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_regressor.html#sklearn.base.is_regressor "sklearn.base.is_regressor")
    , and [`is_outlier_detector`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_outlier_detector.html#sklearn.base.is_outlier_detector "sklearn.base.is_outlier_detector")
     is now deprecated. Pass an instance instead. By [Adrin Jalali](https://github.com/adrinjalali)
     [#30122](https://github.com/scikit-learn/scikit-learn/pull/30122)
    

### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-calibration "Link to this heading")

*   API Change `cv="prefit"` is deprecated for [`CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
    . Use [`FrozenEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
     instead, as `CalibratedClassifierCV(FrozenEstimator(estimator))`. By [Adrin Jalali](https://github.com/adrinjalali)
     [#30171](https://github.com/scikit-learn/scikit-learn/pull/30171)
    

### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-cluster "Link to this heading")

*   API Change The `copy` parameter of [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
     was deprecated in 1.6 and will be removed in 1.8. It has no effect as the estimator does not perform in-place operations on the input data. By [Yao Xiao](https://github.com/Charlie-XIAO)
     [#29124](https://github.com/scikit-learn/scikit-learn/pull/29124)
    

### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-compose "Link to this heading")

*   Enhancement [`sklearn.compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     `verbose_feature_names_out` now accepts string format or callable to generate feature names. By [Marc Bresson](https://github.com/MarcBresson)
     [#28934](https://github.com/scikit-learn/scikit-learn/pull/28934)
    

### [`sklearn.covariance`](https://scikit-learn.org/stable/api/sklearn.covariance.html#module-sklearn.covariance "sklearn.covariance")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-covariance "Link to this heading")

*   Efficiency [`covariance.MinCovDet`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.MinCovDet.html#sklearn.covariance.MinCovDet "sklearn.covariance.MinCovDet")
     fitting is now slightly faster. By [Antony Lee](https://github.com/anntzer)
     [#29835](https://github.com/scikit-learn/scikit-learn/pull/29835)
    

### [`sklearn.cross_decomposition`](https://scikit-learn.org/stable/api/sklearn.cross_decomposition.html#module-sklearn.cross_decomposition "sklearn.cross_decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-cross-decomposition "Link to this heading")

*   Fix [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
     properly raises an error when `n_components` is larger than `n_samples`. By [Thomas Fan](https://github.com/thomasjpfan)
     [#29710](https://github.com/scikit-learn/scikit-learn/pull/29710)
    

### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-datasets "Link to this heading")

*   Feature [`datasets.fetch_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html#sklearn.datasets.fetch_file "sklearn.datasets.fetch_file")
     allows downloading arbitrary data-file from the web. It handles local caching, integrity checks with SHA256 digests and automatic retries in case of HTTP errors. By [Olivier Grisel](https://github.com/ogrisel)
     [#29354](https://github.com/scikit-learn/scikit-learn/pull/29354)
    

### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-decomposition "Link to this heading")

*   Enhancement [`LatentDirichletAllocation`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "sklearn.decomposition.LatentDirichletAllocation")
     now has a `normalize` parameter in [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.transform "sklearn.decomposition.LatentDirichletAllocation.transform")
     and [`fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation.fit_transform "sklearn.decomposition.LatentDirichletAllocation.fit_transform")
     methods to control whether the document topic distribution is normalized. By [Adrin Jalali](https://github.com/adrinjalali)
     [#30097](https://github.com/scikit-learn/scikit-learn/pull/30097)
    
*   Fix [`IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
     will now only raise a `ValueError` when the number of samples in the input data to `partial_fit` is less than the number of components on the first call to `partial_fit`. Subsequent calls to `partial_fit` no longer face this restriction. By [Thomas Gessey-Jones](https://github.com/ThomasGesseyJonesPX)
     [#30224](https://github.com/scikit-learn/scikit-learn/pull/30224)
    

### [`sklearn.discriminant_analysis`](https://scikit-learn.org/stable/api/sklearn.discriminant_analysis.html#module-sklearn.discriminant_analysis "sklearn.discriminant_analysis")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-discriminant-analysis "Link to this heading")

*   Fix [`discriminant_analysis.QuadraticDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis "sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis")
     will now cause `LinAlgWarning` in case of collinear variables. These errors can be silenced using the `reg_param` attribute. By [Alihan Zihna](https://github.com/azihna)
     [#19731](https://github.com/scikit-learn/scikit-learn/pull/19731)
    

### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-ensemble "Link to this heading")

*   Feature [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
     and [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
     now support missing-values in the data matrix `X`. Missing-values are handled by randomly moving all of the samples to the left, or right child node as the tree is traversed. By [Adam Li](https://github.com/adam2392)
     [#28268](https://github.com/scikit-learn/scikit-learn/pull/28268)
    
*   Efficiency Small runtime improvement of fitting [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     by parallelizing the initial search for bin thresholds. By [Christian Lorentzen](https://github.com/lorentzenchr)
     [#28064](https://github.com/scikit-learn/scikit-learn/pull/28064)
    
*   Efficiency [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     now runs parallel jobs during [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
     offering a speedup of up to 2-4x on sample sizes larger than 2000 using `joblib`. By [Adam Li](https://github.com/adam2392)
     and [Sérgio Pereira](https://github.com/sergiormpereira)
     [#28622](https://github.com/scikit-learn/scikit-learn/pull/28622)
    
*   Enhancement The verbosity of [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
     and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
     got a more granular control. Now, `verbose = 1` prints only summary messages, `verbose >= 2` prints the full information as before. By [Christian Lorentzen](https://github.com/lorentzenchr)
     [#28179](https://github.com/scikit-learn/scikit-learn/pull/28179)
    
*   API Change The parameter `algorithm` of [`ensemble.AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
     is deprecated and will be removed in 1.8. By [Jérémie du Boisberranger](https://github.com/jeremiedbb)
     [#29997](https://github.com/scikit-learn/scikit-learn/pull/29997)
    

### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-feature-extraction "Link to this heading")

*   Fix [`feature_extraction.text.TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
     now correctly preserves the `dtype` of `idf_` based on the input data. By [Guillaume Lemaitre](https://github.com/glemaitre)
     [#30022](https://github.com/scikit-learn/scikit-learn/pull/30022)
    

### [`sklearn.frozen`](https://scikit-learn.org/stable/api/sklearn.frozen.html#module-sklearn.frozen "sklearn.frozen")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-frozen "Link to this heading")

*   Major Feature [`FrozenEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
     is now introduced which allows freezing an estimator. This means calling `.fit` on it has no effect, and doing a `clone(frozenestimator)` returns the same estimator instead of an unfitted clone. [#29705](https://github.com/scikit-learn/scikit-learn/pull/29705)
     By [Adrin Jalali](https://github.com/adrinjalali)
     [#29705](https://github.com/scikit-learn/scikit-learn/pull/29705)
    

### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-impute "Link to this heading")

*   Fix [`impute.KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
     excludes samples with nan distances when computing the mean value for uniform weights. By [Xuefeng Xu](https://github.com/xuefeng-xu)
     [#29135](https://github.com/scikit-learn/scikit-learn/pull/29135)
    
*   Fix When `min_value` and `max_value` are array-like and some features are dropped due to `keep_empty_features=False`, [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     no longer raises an error and now indexes correctly. By [Guntitat Sawadwuthikul](https://github.com/gunsodo)
     [#29451](https://github.com/scikit-learn/scikit-learn/pull/29451)
    
*   Fix Fixed [`impute.IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
     to make sure that it does not skip the iterative process when `keep_empty_features` is set to `True`. By [Arif Qodari](https://github.com/arifqodari)
     [#29779](https://github.com/scikit-learn/scikit-learn/pull/29779)
    
*   API Change Add a warning in [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     when `keep_empty_feature=False` and `strategy="constant"`. In this case empty features are not dropped and this behaviour will change in 1.8. By [Arthur Courselle](https://github.com/ArthurCourselle)
     and [Simon Riou](https://github.com/simon-riou)
     [#29950](https://github.com/scikit-learn/scikit-learn/pull/29950)
    

### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-linear-model "Link to this heading")

*   Enhancement The `solver="newton-cholesky"` in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     is extended to support the full multinomial loss in a multiclass setting. By [Christian Lorentzen](https://github.com/lorentzenchr)
     [#28840](https://github.com/scikit-learn/scikit-learn/pull/28840)
    
*   Fix In [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
     and [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
    , after `fit`, the `coef_` attribute is now of shape `(n_samples,)` like other linear models. By [Maxwell Liu](https://github.com/MaxwellLZH)
    , [Guillaume Lemaitre](https://github.com/glemaitre)
    , and [Adrin Jalali](https://github.com/adrinjalali)
     [#19746](https://github.com/scikit-learn/scikit-learn/pull/19746)
    
*   Fix [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     corrects sample weight handling for the calculation of test scores. By [Shruti Nath](https://github.com/snath-xoc)
     [#29419](https://github.com/scikit-learn/scikit-learn/pull/29419)
    
*   Fix [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
     and [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
     now take sample weights into accounts to define the search grid for the internally tuned `alpha` hyper-parameter. By [John Hopfensperger](https://github.com/s-banach)
     and [Shruti Nath](https://github.com/snath-xoc)
     [#29442](https://github.com/scikit-learn/scikit-learn/pull/29442)
    
*   Fix [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    , [`linear_model.PoissonRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")
    , [`linear_model.GammaRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html#sklearn.linear_model.GammaRegressor "sklearn.linear_model.GammaRegressor")
    , [`linear_model.TweedieRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html#sklearn.linear_model.TweedieRegressor "sklearn.linear_model.TweedieRegressor")
     now take sample weights into account to decide when to fall back to `solver='lbfgs'` whenever `solver='newton-cholesky'` becomes numerically unstable. By [Antoine Baker](https://github.com/antoinebaker)
     [#29818](https://github.com/scikit-learn/scikit-learn/pull/29818)
    
*   Fix [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     now properly uses predictions on the same scale as the target seen during `fit`. These predictions are stored in `cv_results_` when `scoring != None`. Previously, the predictions were rescaled by the square root of the sample weights and offset by the mean of the target, leading to an incorrect estimate of the score. By [Guillaume Lemaitre](https://github.com/glemaitre)
    , [Jérôme Dockes](https://github.com/jeromedockes)
     and [Hanmin Qin](https://github.com/qinhanmin2014)
     [#29842](https://github.com/scikit-learn/scikit-learn/pull/29842)
    
*   Fix [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     now properly supports custom multioutput scorers by letting the scorer manage the multioutput averaging. Previously, the predictions and true targets were both squeezed to a 1D array before computing the error. By [Guillaume Lemaitre](https://github.com/glemaitre)
     [#29884](https://github.com/scikit-learn/scikit-learn/pull/29884)
    
*   Fix [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
     now sets the `cond` parameter when calling the `scipy.linalg.lstsq` solver on dense input data. This ensures more numerically robust results on rank-deficient data. In particular, it empirically fixes the expected equivalence property between fitting with reweighted or with repeated data points. By [Antoine Baker](https://github.com/antoinebaker)
     [#30040](https://github.com/scikit-learn/scikit-learn/pull/30040)
    
*   Fix [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     and other linear models that accept `solver="newton-cholesky"` now report the correct number of iterations when they fall back to the `"lbfgs"` solver because of a rank deficient Hessian matrix. By [Olivier Grisel](https://github.com/ogrisel)
     [#30100](https://github.com/scikit-learn/scikit-learn/pull/30100)
    
*   Fix [`SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
     now correctly inherits from [`OutlierMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.OutlierMixin.html#sklearn.base.OutlierMixin "sklearn.base.OutlierMixin")
     and the tags are correctly set. By [Guillaume Lemaitre](https://github.com/glemaitre)
     [#30227](https://github.com/scikit-learn/scikit-learn/pull/30227)
    
*   API Change Deprecates `copy_X` in [`linear_model.TheilSenRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "sklearn.linear_model.TheilSenRegressor")
     as the parameter has no effect. `copy_X` will be removed in 1.8. By [Adam Li](https://github.com/adam2392)
     [#29105](https://github.com/scikit-learn/scikit-learn/pull/29105)
    

### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-manifold "Link to this heading")

*   Efficiency [`manifold.locally_linear_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#sklearn.manifold.locally_linear_embedding "sklearn.manifold.locally_linear_embedding")
     and [`manifold.LocallyLinearEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
     now allocate more efficiently the memory of sparse matrices in the Hessian, Modified and LTSA methods. By [Giorgio Angelotti](https://github.com/giorgioangel)
     [#28096](https://github.com/scikit-learn/scikit-learn/pull/28096)
    

### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#id2 "Link to this heading")

*   Efficiency [`sklearn.metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
     is now faster by caching classification labels. By [Adrin Jalali](https://github.com/adrinjalali)
     [#29738](https://github.com/scikit-learn/scikit-learn/pull/29738)
    
*   Enhancement [`metrics.RocCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")
    , [`metrics.RocCurveDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")
    , [`metrics.PrecisionRecallDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
    , and [`metrics.PrecisionRecallDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")
     now accept a new keyword `despine` to remove the top and right spines of the plot in order to make it clearer. By [Yao Xiao](https://github.com/Charlie-XIAO)
     [#26367](https://github.com/scikit-learn/scikit-learn/pull/26367)
    
*   Enhancement [`sklearn.metrics.check_scoring`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.check_scoring.html#sklearn.metrics.check_scoring "sklearn.metrics.check_scoring")
     now accepts `raise_exc` to specify whether to raise an exception if a subset of the scorers in multimetric scoring fails or to return an error code. By [Stefanie Senger](https://github.com/StefanieSenger)
     [#28992](https://github.com/scikit-learn/scikit-learn/pull/28992)
    
*   Fix [`metrics.roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
     will now correctly return np.nan and warn user if only one class is present in the labels. By [Hleb Levitski](https://github.com/glevv)
     and [Janez Demšar](https://github.com/janezd)
     [#27412](https://github.com/scikit-learn/scikit-learn/pull/27412)
    , [#30013](https://github.com/scikit-learn/scikit-learn/pull/30013)
    
*   Fix The functions [`metrics.mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html#sklearn.metrics.mean_squared_log_error "sklearn.metrics.mean_squared_log_error")
     and [`metrics.root_mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_log_error.html#sklearn.metrics.root_mean_squared_log_error "sklearn.metrics.root_mean_squared_log_error")
     now check whether the inputs are within the correct domain for the function y\=log⁡(1+x), rather than y\=log⁡(x). The functions [`metrics.mean_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
    , [`metrics.mean_absolute_percentage_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html#sklearn.metrics.mean_absolute_percentage_error "sklearn.metrics.mean_absolute_percentage_error")
    , [`metrics.mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
     and [`metrics.root_mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#sklearn.metrics.root_mean_squared_error "sklearn.metrics.root_mean_squared_error")
     now explicitly check whether a scalar will be returned when `multioutput=uniform_average`. By [Virgil Chan](https://github.com/virchan)
     [#29709](https://github.com/scikit-learn/scikit-learn/pull/29709)
    
*   API Change The `assert_all_finite` parameter of functions `metrics.pairwise.check_pairwise_arrays` and [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     is renamed into `ensure_all_finite`. `force_all_finite` will be removed in 1.8. By [Jérémie du Boisberranger](https://github.com/jeremiedb)
     [#29404](https://github.com/scikit-learn/scikit-learn/pull/29404)
    
*   API Change `scoring="neg_max_error"` should be used instead of `scoring="max_error"` which is now deprecated. By [Farid “Freddie” Taba](https://github.com/artificialfintelligence)
     [#29462](https://github.com/scikit-learn/scikit-learn/pull/29462)
    
*   API Change The default value of the `response_method` parameter of [`metrics.make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
     will change from `None` to `"predict"` and `None` will be removed in 1.8. In the meantime, `None` is equivalent to `"predict"`. By [Jérémie du Boisberranger](https://github.com/jeremiedb)
     [#30001](https://github.com/scikit-learn/scikit-learn/pull/30001)
    

### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#id3 "Link to this heading")

*   Enhancement [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
     now has the ability to shuffle groups into different folds when `shuffle=True`. By [Zachary Vealey](https://github.com/zvealey)
     [#28519](https://github.com/scikit-learn/scikit-learn/pull/28519)
    
*   Enhancement There is no need to call `fit` on a [`FixedThresholdClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")
     if the underlying estimator is already fitted. By [Adrin Jalali](https://github.com/adrinjalali)
     [#30172](https://github.com/scikit-learn/scikit-learn/pull/30172)
    
*   Fix Improve error message when [`model_selection.RepeatedStratifiedKFold.split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold.split "sklearn.model_selection.RepeatedStratifiedKFold.split")
     is called without a `y` argument By [Anurag Varma](https://github.com/Anurag-Varma)
     [#29402](https://github.com/scikit-learn/scikit-learn/pull/29402)
    

### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-neighbors "Link to this heading")

*   Enhancement [`neighbors.NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
    , [`neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
    , [`neighbors.KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
    , [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
    , [`neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
    , [`neighbors.KNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
    , [`neighbors.RadiusNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer "sklearn.neighbors.RadiusNeighborsTransformer")
    , and [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
     now work with `metric="nan_euclidean"`, supporting `nan` inputs. By [Carlo Lemos](https://github.com/vitaliset)
    , [Guillaume Lemaitre](https://github.com/glemaitre)
    , and [Adrin Jalali](https://github.com/adrinjalali)
     [#25330](https://github.com/scikit-learn/scikit-learn/pull/25330)
    
*   Enhancement Add [`neighbors.NearestCentroid.decision_function`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid.decision_function "sklearn.neighbors.NearestCentroid.decision_function")
    , [`neighbors.NearestCentroid.predict_proba`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid.predict_proba "sklearn.neighbors.NearestCentroid.predict_proba")
     and [`neighbors.NearestCentroid.predict_log_proba`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid.predict_log_proba "sklearn.neighbors.NearestCentroid.predict_log_proba")
     to the [`neighbors.NearestCentroid`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")
     estimator class. Support the case when `X` is sparse and `shrinking_threshold` is not `None` in [`neighbors.NearestCentroid`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")
    . By [Matthew Ning](https://github.com/NoPenguinsLand)
     [#26689](https://github.com/scikit-learn/scikit-learn/pull/26689)
    
*   Enhancement Make `predict`, `predict_proba`, and `score` of [`neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
     and [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
     accept `X=None` as input. In this case predictions for all training set points are returned, and points are not included into their own neighbors. By [Dmitry Kobak](https://github.com/dkobak)
     [#30047](https://github.com/scikit-learn/scikit-learn/pull/30047)
    
*   Fix [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
     raises a warning in the `fit` method when duplicate values in the training data lead to inaccurate outlier detection. By [Henrique Caroço](https://github.com/HenriqueProj)
     [#28773](https://github.com/scikit-learn/scikit-learn/pull/28773)
    

### [`sklearn.neural_network`](https://scikit-learn.org/stable/api/sklearn.neural_network.html#module-sklearn.neural_network "sklearn.neural_network")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-neural-network "Link to this heading")

*   Fix [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
     does no longer crash when the model diverges and that `early_stopping` is enabled. By [Marc Bresson](https://github.com/MarcBresson)
     [#29773](https://github.com/scikit-learn/scikit-learn/pull/29773)
    

### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-pipeline "Link to this heading")

*   Major Feature [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     can now transform metadata up to the step requiring the metadata, which can be set using the `transform_input` parameter. By [Adrin Jalali](https://github.com/adrinjalali)
     [#28901](https://github.com/scikit-learn/scikit-learn/pull/28901)
    
*   Enhancement [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     now warns about not being fitted before calling methods that require the pipeline to be fitted. This warning will become an error in 1.8. By [Adrin Jalali](https://github.com/adrinjalali)
     [#29868](https://github.com/scikit-learn/scikit-learn/pull/29868)
    
*   Fix Fixed an issue with tags and estimator type of [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     when pipeline is empty. This allows the HTML representation of an empty pipeline to be rendered correctly. By [Gennaro Daniele Acciaro](https://github.com/gdacciaro)
     [#30203](https://github.com/scikit-learn/scikit-learn/pull/30203)
    

### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-preprocessing "Link to this heading")

*   Enhancement Added `warn` option to `handle_unknown` parameter in [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
    . By [Hleb Levitski](https://github.com/glevv)
     [#28637](https://github.com/scikit-learn/scikit-learn/pull/28637)
    
*   Enhancement The HTML representation of [`preprocessing.FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
     will show the function name in the label. By [Yao Xiao](https://github.com/Charlie-XIAO)
     [#29158](https://github.com/scikit-learn/scikit-learn/pull/29158)
    
*   Fix [`preprocessing.PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
     now uses `scipy.special.inv_boxcox` to output `nan` if the input of BoxCox’s inverse is invalid. By [Xuefeng Xu](https://github.com/xuefeng-xu)
     [#27875](https://github.com/scikit-learn/scikit-learn/pull/27875)
    

### [`sklearn.semi_supervised`](https://scikit-learn.org/stable/api/sklearn.semi_supervised.html#module-sklearn.semi_supervised "sklearn.semi_supervised")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-semi-supervised "Link to this heading")

*   API Change [`semi_supervised.SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
     deprecated the `base_estimator` parameter in favor of `estimator`. By [Adam Li](https://github.com/adam2392)
     [#28494](https://github.com/scikit-learn/scikit-learn/pull/28494)
    

### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#id4 "Link to this heading")

*   Feature [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
     and [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
     now support missing-values in the data matrix `X`. Missing-values are handled by randomly moving all of the samples to the left, or right child node as the tree is traversed. By [Adam Li](https://github.com/adam2392)
     and [Loïc Estève](https://github.com/lesteve)
     [#27966](https://github.com/scikit-learn/scikit-learn/pull/27966)
    , [#30318](https://github.com/scikit-learn/scikit-learn/pull/30318)
    
*   Fix Escape double quotes for labels and feature names when exporting trees to Graphviz format. By [Santiago M. Mola](https://github.com/smola)
    . [#17575](https://github.com/scikit-learn/scikit-learn/pull/17575)
    

### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v1.6.html#id5 "Link to this heading")

*   Enhancement [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     now accepts `ensure_non_negative` to check for negative values in the passed array, until now only available through calling `utils.check_non_negative`. By [Tamara Atanasoska](https://github.com/tamaraatanasoska)
     [#29540](https://github.com/scikit-learn/scikit-learn/pull/29540)
    
*   Enhancement [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     and [`parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks")
     now check and fail if the classifier has the `tags.classifier_tags.multi_class = False` tag but does not fail on multi-class data. By [Adrin Jalali](https://github.com/adrinjalali)
     [#29874](https://github.com/scikit-learn/scikit-learn/pull/29874)
    
*   Enhancement [`utils.validation.check_is_fitted`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
     now passes on stateless estimators. An estimator can indicate it’s stateless by setting the `requires_fit` tag. See [Estimator Tags](https://scikit-learn.org/stable/developers/develop.html#estimator-tags)
     for more information. By [Adrin Jalali](https://github.com/adrinjalali)
     [#29880](https://github.com/scikit-learn/scikit-learn/pull/29880)
    
*   Enhancement Changes to [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     and [`parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks")
    .
    
    *   [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
         introduces new arguments: `on_skip`, `on_fail`, and `callback` to control the behavior of the check runner. Refer to the API documentation for more details.
        
    *   `generate_only=True` is deprecated in [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
        . Use [`estimator_checks_generator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.estimator_checks_generator.html#sklearn.utils.estimator_checks.estimator_checks_generator "sklearn.utils.estimator_checks.estimator_checks_generator")
         instead.
        
    *   The `_xfail_checks` estimator tag is now removed, and now in order to indicate which tests are expected to fail, you can pass a dictionary to the [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
         as the `expected_failed_checks` parameter. Similarly, the `expected_failed_checks` parameter in [`parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks")
         can be used, which is a callable returning a dictionary of the form:
        
        {
            "check\_name": "reason to mark this check as xfail",
        }
        
        Copy to clipboard
        
    
    By [Adrin Jalali](https://github.com/adrinjalali)
     [#30149](https://github.com/scikit-learn/scikit-learn/pull/30149)
    
*   Fix [`utils.estimator_checks.parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks")
     and [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     now support estimators that have `set_output` called on them. By [Adrin Jalali](https://github.com/adrinjalali)
     [#29869](https://github.com/scikit-learn/scikit-learn/pull/29869)
    
*   API Change The `assert_all_finite` parameter of functions [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
    , [`utils.check_X_y`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html#sklearn.utils.check_X_y "sklearn.utils.check_X_y")
    , [`utils.as_float_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.as_float_array.html#sklearn.utils.as_float_array "sklearn.utils.as_float_array")
     is renamed into `ensure_all_finite`. `force_all_finite` will be removed in 1.8. By [Jérémie du Boisberranger](https://github.com/jeremiedb)
     [#29404](https://github.com/scikit-learn/scikit-learn/pull/29404)
    
*   API Change `utils.estimator_checks.check_sample_weights_invariance` replaced by `utils.estimator_checks.check_sample_weight_equivalence_on_dense_data` which uses integer (including zero) weights and `utils.estimator_checks.check_sample_weight_equivalence_on_sparse_data` which does the same on sparse data. By [Antoine Baker](https://github.com/antoinebaker)
     [#29818](https://github.com/scikit-learn/scikit-learn/pull/29818)
    , [#30137](https://github.com/scikit-learn/scikit-learn/pull/30137)
    
*   API Change Using `_estimator_type` to set the estimator type is deprecated. Inherit from [`ClassifierMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin")
    , [`RegressorMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#sklearn.base.RegressorMixin "sklearn.base.RegressorMixin")
    , [`TransformerMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin")
    , or [`OutlierMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.OutlierMixin.html#sklearn.base.OutlierMixin "sklearn.base.OutlierMixin")
     instead. Alternatively, you can set `estimator_type` in [`Tags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Tags.html#sklearn.utils.Tags "sklearn.utils.Tags")
     in the `__sklearn_tags__` method. By [Adrin Jalali](https://github.com/adrinjalali)
     [#30122](https://github.com/scikit-learn/scikit-learn/pull/30122)
    

Code and documentation contributors

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 1.5, including:

Aaron Schumacher, Abdulaziz Aloqeely, abhi-jha, Acciaro Gennaro Daniele, Adam J. Stewart, Adam Li, Adeel Hassan, Adeyemi Biola, Aditi Juneja, Adrin Jalali, Aisha, Akanksha Mhadolkar, Akihiro Kuno, Alberto Torres, alexqiao, Alihan Zihna, Aniruddha Saha, antoinebaker, Antony Lee, Anurag Varma, Arif Qodari, Arthur Courselle, ArthurDbrn, Arturo Amor, Aswathavicky, Audrey Flanders, aurelienmorgan, Austin, awwwyan, AyGeeEm, a.zy.lee, baggiponte, BlazeStorm001, bme-git, Boney Patel, brdav, Brigitta Sipőcz, Cailean Carter, Camille Troillard, Carlo Lemos, Christian Lorentzen, Christian Veenhuis, Christine P. Chai, claudio, Conrad Stevens, datarollhexasphericon, Davide Chicco, David Matthew Cherney, Dea María Léon, Deepak Saldanha, Deepyaman Datta, dependabot\[bot\], dinga92, Dmitry Kobak, Domenico, Drew Craeton, dymil, Edoardo Abati, EmilyXinyi, Eric Larson, Evelyn, fabianhenning, Farid “Freddie” Taba, Gael Varoquaux, Giorgio Angelotti, Hleb Levitski, Guillaume Lemaitre, Guntitat Sawadwuthikul, Haesun Park, Hanjun Kim, Henrique Caroço, hhchen1105, Hugo Boulenger, Ilya Komarov, Inessa Pawson, Ivan Pan, Ivan Wiryadi, Jaimin Chauhan, Jakob Bull, James Lamb, Janez Demšar, Jérémie du Boisberranger, Jérôme Dockès, Jirair Aroyan, João Morais, Joe Cainey, Joel Nothman, John Enblom, JorgeCardenas, Joseph Barbier, jpienaar-tuks, Julian Chan, K.Bharat Reddy, Kevin Doshi, Lars, Loic Esteve, Lucas Colley, Lucy Liu, lunovian, Marc Bresson, Marco Edward Gorelli, Marco Maggi, Marco Wolsza, Maren Westermann, MarieS-WiMLDS, Martin Helm, Mathew Shen, mathurinm, Matthew Feickert, Maxwell Liu, Meekail Zain, Michael Dawson, Miguel Cárdenas, m-maggi, mrastgoo, Natalia Mokeeva, Nathan Goldbaum, Nathan Orgera, nbrown-ScottLogic, Nikita Chistyakov, Nithish Bolleddula, Noam Keidar, NoPenguinsLand, Norbert Preining, notPlancha, Olivier Grisel, Omar Salman, ParsifalXu, Piotr, Priyank Shroff, Priyansh Gupta, Quentin Barthélemy, Rachit23110261, Rahil Parikh, raisadz, Rajath, renaissance0ne, Reshama Shaikh, Roberto Rosati, Robert Pollak, rwelsch427, Santiago Castro, Santiago M. Mola, scikit-learn-bot, sean moiselle, SHREEKANT VITTHAL NANDIYAWAR, Shruti Nath, Søren Bredlund Caspersen, Stefanie Senger, Stefano Gaspari, Steffen Schneider, Štěpán Sršeň, Sylvain Combettes, Tamara, Thomas, Thomas Gessey-Jones, Thomas J. Fan, Thomas Li, ThorbenMaa, Tialo, Tim Head, Tuhin Sharma, Tushar Parimi, Umberto Fasci, UV, vedpawar2254, Velislav Babatchev, Victoria Shevchenko, viktor765, Vince Carey, Virgil Chan, Wang Jiayi, Xiao Yuan, Xuefeng Xu, Yao Xiao, yareyaredesuyo, Zachary Vealey, Ziad Amerr

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)