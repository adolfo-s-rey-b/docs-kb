[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.cross_validate.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.cross_validate.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.cross_validate.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.cross_validate.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.cross_validate.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.cross_validate.html)

Collapse Sidebar Expand Sidebar

cross\_validate[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#cross-validate "Link to this heading")

========================================================================================================================================================

sklearn.model\_selection.cross\_validate(_estimator_, _X_, _y\=None_, _\*_, _groups\=None_, _scoring\=None_, _cv\=None_, _n\_jobs\=None_, _verbose\=0_, _params\=None_, _pre\_dispatch\='2\*n\_jobs'_, _return\_train\_score\=False_, _return\_estimator\=False_, _return\_indices\=False_, _error\_score\=nan_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_validation.py#L75)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "Link to this definition")

Evaluate metric(s) by cross-validation and also record fit/score times.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#multimetric-cross-validation)
.

Parameters:

**estimator**estimator object implementing ‘fit’

The object to use to fit the data.

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data to fit. Can be for example a list, or an array.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs), default=None

The target variable to try to predict in the case of supervised learning.

**groups**array-like of shape (n\_samples,), default=None

Group labels for the samples used while splitting the dataset into train/test set. Only used in conjunction with a “Group” [cv](https://scikit-learn.org/stable/glossary.html#term-cv)
 instance (e.g., [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
).

Changed in version 1.4: `groups` can only be passed if metadata routing is not enabled via `sklearn.set_config(enable_metadata_routing=True)`. When routing is enabled, pass `groups` alongside other metadata via the `params` argument instead. E.g.: `cross_validate(..., params={'groups': groups})`.

**scoring**str, callable, list, tuple, or dict, default=None

Strategy to evaluate the performance of the `estimator` across cross-validation splits.

If `scoring` represents a single score, one can use:

*   a single string (see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
    );
    
*   a callable (see [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
    ) that returns a single value.
    
*   `None`, the `estimator`’s [default evaluation criterion](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-api-overview)
     is used.
    

If `scoring` represents multiple scores, one can use:

*   a list or tuple of unique strings;
    
*   a callable returning a dictionary where the keys are the metric names and the values are the metric scores;
    
*   a dictionary with metric names as keys and callables as values.
    

See [Specifying multiple metrics for evaluation](https://scikit-learn.org/stable/modules/grid_search.html#multimetric-grid-search)
 for an example.

**cv**int, cross-validation generator or an iterable, default=None

Determines the cross-validation splitting strategy. Possible inputs for cv are:

*   None, to use the default 5-fold cross validation,
    
*   int, to specify the number of folds in a `(Stratified)KFold`,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
    ,
    
*   an iterable yielding (train, test) splits as arrays of indices.
    

For int/None inputs, if the estimator is a classifier and `y` is either binary or multiclass, [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 is used. In all other cases, [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used. These splitters are instantiated with `shuffle=False` so the splits will be the same across calls.

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

Changed in version 0.22: `cv` default value if None changed from 3-fold to 5-fold.

**n\_jobs**int, default=None

Number of jobs to run in parallel. Training the estimator and computing the score are parallelized over the cross-validation splits. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**verbose**int, default=0

The verbosity level.

**params**dict, default=None

Parameters to pass to the underlying estimator’s `fit`, the scorer, and the CV splitter.

Added in version 1.4.

**pre\_dispatch**int or str, default=’2\*n\_jobs’

Controls the number of jobs that get dispatched during parallel execution. Reducing this number can be useful to avoid an explosion of memory consumption when more jobs get dispatched than CPUs can process. This parameter can be:

*   An int, giving the exact number of total jobs that are spawned
    
*   A str, giving an expression as a function of n\_jobs, as in ‘2\*n\_jobs’
    

**return\_train\_score**bool, default=False

Whether to include train scores. Computing training scores is used to get insights on how different parameter settings impact the overfitting/underfitting trade-off. However computing the scores on the training set can be computationally expensive and is not strictly required to select the parameters that yield the best generalization performance.

Added in version 0.19.

Changed in version 0.21: Default value was changed from `True` to `False`

**return\_estimator**bool, default=False

Whether to return the estimators fitted on each split.

Added in version 0.20.

**return\_indices**bool, default=False

Whether to return the train-test indices selected for each split.

Added in version 1.3.

**error\_score**‘raise’ or numeric, default=np.nan

Value to assign to the score if an error occurs in estimator fitting. If set to ‘raise’, the error is raised. If a numeric value is given, FitFailedWarning is raised.

Added in version 0.20.

Returns:

**scores**dict of float arrays of shape (n\_splits,)

Array of scores of the estimator for each run of the cross validation.

A dict of arrays containing the score/time arrays for each scorer is returned. The possible keys for this `dict` are:

`test_score`

The score array for test scores on each cv split. Suffix `_score` in `test_score` changes to a specific metric like `test_r2` or `test_auc` if there are multiple scoring metrics in the scoring parameter.

`train_score`

The score array for train scores on each cv split. Suffix `_score` in `train_score` changes to a specific metric like `train_r2` or `train_auc` if there are multiple scoring metrics in the scoring parameter. This is available only if `return_train_score` parameter is `True`.

`fit_time`

The time for fitting the estimator on the train set for each cv split.

`score_time`

The time for scoring the estimator on the test set for each cv split. (Note: time for scoring on the train set is not included even if `return_train_score` is set to `True`).

`estimator`

The estimator objects for each cv split. This is available only if `return_estimator` parameter is set to `True`.

`indices`

The train/test positional indices for each cv split. A dictionary is returned where the keys are either `"train"` or `"test"` and the associated values are a list of integer-dtyped NumPy arrays with the indices. Available only if `return_indices=True`.

See also

[`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")

Run cross-validation for single metric evaluation.

[`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")

Get predictions from each split of cross-validation for diagnostic purposes.

[`sklearn.metrics.make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")

Make a scorer from a performance metric or loss function.

Examples

\>>> from sklearn import datasets, linear\_model
\>>> from sklearn.model\_selection import cross\_validate
\>>> diabetes \= datasets.load\_diabetes()
\>>> X \= diabetes.data\[:150\]
\>>> y \= diabetes.target\[:150\]
\>>> lasso \= linear\_model.Lasso()

Copy to clipboard

Single metric evaluation using `cross_validate`

\>>> cv\_results \= cross\_validate(lasso, X, y, cv\=3)
\>>> sorted(cv\_results.keys())
\['fit\_time', 'score\_time', 'test\_score'\]
\>>> cv\_results\['test\_score'\]
array(\[0.3315057 , 0.08022103, 0.03531816\])

Copy to clipboard

Multiple metric evaluation using `cross_validate` (please refer the `scoring` parameter doc for more information)

\>>> scores \= cross\_validate(lasso, X, y, cv\=3,
...                         scoring\=('r2', 'neg\_mean\_squared\_error'),
...                         return\_train\_score\=True)
\>>> print(scores\['test\_neg\_mean\_squared\_error'\])
\[-3635.5 -3573.3 -6114.7\]
\>>> print(scores\['train\_r2'\])
\[0.28009951 0.3908844  0.22784907\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)

[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)

Lagged features for time series forecasting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_categorical_thumb.png)

[Categorical Feature Support in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_categorical.html)

Categorical Feature Support in Gradient Boosting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_thumb.png)

[Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html)

Features in Histogram Gradient Boosting Trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_thumb.png)

[Combine predictors using stacking](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)

Combine predictors using stacking

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_thumb.png)

[Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)

Common pitfalls in the interpretation of coefficients of linear models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_quantile_regression_thumb.png)

[Quantile regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_quantile_regression.html)

Quantile regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_metadata_routing_thumb.png)

[Developing Estimators Compliant with Metadata Routing](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_metadata_routing.html)

Developing Estimators Compliant with Metadata Routing

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_predict_thumb.png)

[Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html)

Plotting Cross-Validated Predictions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_likelihood_ratios_thumb.png)

[Class Likelihood Ratios to measure classification performance](https://scikit-learn.org/stable/auto_examples/model_selection/plot_likelihood_ratios.html)

Class Likelihood Ratios to measure classification performance

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_thumb.png)

[Precision-Recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

Precision-Recall

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_crossval_thumb.png)

[Receiver Operating Characteristic (ROC) with cross validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html)

Receiver Operating Characteristic (ROC) with cross validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tuned_decision_threshold_thumb.png)

[Post-hoc tuning the cut-off point of decision function](https://scikit-learn.org/stable/auto_examples/model_selection/plot_tuned_decision_threshold.html)

Post-hoc tuning the cut-off point of decision function

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multiclass_overview_thumb.png)

[Overview of multiclass training meta-estimators](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html)

Overview of multiclass training meta-estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_target_encoder_thumb.png)

[Comparing Target Encoder with Other Encoders](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html)

Comparing Target Encoder with Other Encoders

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_7_0_thumb.png)

[Release Highlights for scikit-learn 1.7](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)

Release Highlights for scikit-learn 1.7

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)