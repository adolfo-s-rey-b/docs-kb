[Skip to main content](https://scikit-learn.org/stable/api/sklearn.model_selection.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.model_selection.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.model_selection.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.model_selection.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.model_selection.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.model_selection.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.model_selection.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.model_selection.html)

Collapse Sidebar Expand Sidebar

sklearn.model\_selection[#](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "Link to this heading")

====================================================================================================================================================

Tools for model selection, such as cross validation and hyper-parameter tuning.

**User guide.** See the [Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
, [Tuning the hyper-parameters of an estimator](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)
, and [Learning curve](https://scikit-learn.org/stable/modules/learning_curve.html#learning-curve)
 sections for further details.

Splitters[#](https://scikit-learn.org/stable/api/sklearn.model_selection.html#splitters "Link to this heading")

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold") | K-fold iterator variant with non-overlapping groups. |
| [`GroupShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit "sklearn.model_selection.GroupShuffleSplit") | Shuffle-Group(s)-Out cross-validation iterator. |
| [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold") | K-Fold cross-validator. |
| [`LeaveOneGroupOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut "sklearn.model_selection.LeaveOneGroupOut") | Leave One Group Out cross-validator. |
| [`LeaveOneOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#sklearn.model_selection.LeaveOneOut "sklearn.model_selection.LeaveOneOut") | Leave-One-Out cross-validator. |
| [`LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut") | Leave P Group(s) Out cross-validator. |
| [`LeavePOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePOut.html#sklearn.model_selection.LeavePOut "sklearn.model_selection.LeavePOut") | Leave-P-Out cross-validator. |
| [`PredefinedSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.PredefinedSplit.html#sklearn.model_selection.PredefinedSplit "sklearn.model_selection.PredefinedSplit") | Predefined split cross-validator. |
| [`RepeatedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#sklearn.model_selection.RepeatedKFold "sklearn.model_selection.RepeatedKFold") | Repeated K-Fold cross validator. |
| [`RepeatedStratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold "sklearn.model_selection.RepeatedStratifiedKFold") | Repeated class-wise stratified K-Fold cross validator. |
| [`ShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit") | Random permutation cross-validator. |
| [`StratifiedGroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold "sklearn.model_selection.StratifiedGroupKFold") | Class-wise stratified K-Fold iterator variant with non-overlapping groups. |
| [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold") | Class-wise stratified K-Fold cross-validator. |
| [`StratifiedShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit") | Class-wise stratified ShuffleSplit cross-validator. |
| [`TimeSeriesSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit") | Time Series cross-validator. |
| [`check_cv`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.check_cv.html#sklearn.model_selection.check_cv "sklearn.model_selection.check_cv") | Input checker utility for building a cross-validator. |
| [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split") | Split arrays or matrices into random train and test subsets. |

Hyper-parameter optimizers[#](https://scikit-learn.org/stable/api/sklearn.model_selection.html#hyper-parameter-optimizers "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV") | Exhaustive search over specified parameter values for an estimator. |
| [`HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV") | Search over specified parameter values with successive halving. |
| [`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV") | Randomized search on hyper parameters. |
| [`ParameterGrid`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterGrid.html#sklearn.model_selection.ParameterGrid "sklearn.model_selection.ParameterGrid") | Grid of parameters with a discrete number of values for each. |
| [`ParameterSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterSampler.html#sklearn.model_selection.ParameterSampler "sklearn.model_selection.ParameterSampler") | Generator on parameters sampled from given distributions. |
| [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV") | Randomized search on hyper parameters. |

Post-fit model tuning[#](https://scikit-learn.org/stable/api/sklearn.model_selection.html#post-fit-model-tuning "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`FixedThresholdClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier") | Binary classifier that manually sets the decision threshold. |
| [`TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV") | Classifier that post-tunes the decision threshold using cross-validation. |

Model validation[#](https://scikit-learn.org/stable/api/sklearn.model_selection.html#model-validation "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict") | Generate cross-validated estimates for each input data point. |
| [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score") | Evaluate a score by cross-validation. |
| [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate") | Evaluate metric(s) by cross-validation and also record fit/score times. |
| [`learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve") | Learning curve. |
| [`permutation_test_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#sklearn.model_selection.permutation_test_score "sklearn.model_selection.permutation_test_score") | Evaluate the significance of a cross-validated score with permutations. |
| [`validation_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve "sklearn.model_selection.validation_curve") | Validation curve. |

Visualization[#](https://scikit-learn.org/stable/api/sklearn.model_selection.html#visualization "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`LearningCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay "sklearn.model_selection.LearningCurveDisplay") | Learning Curve visualization. |
| [`ValidationCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ValidationCurveDisplay.html#sklearn.model_selection.ValidationCurveDisplay "sklearn.model_selection.ValidationCurveDisplay") | Validation Curve visualization. |