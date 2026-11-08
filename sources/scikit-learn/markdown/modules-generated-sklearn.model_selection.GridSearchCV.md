[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.GridSearchCV.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.GridSearchCV.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.GridSearchCV.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.GridSearchCV.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.GridSearchCV.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.GridSearchCV.html)

Collapse Sidebar Expand Sidebar

GridSearchCV[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#gridsearchcv "Link to this heading")

=================================================================================================================================================

class sklearn.model\_selection.GridSearchCV(_estimator_, _param\_grid_, _\*_, _scoring\=None_, _n\_jobs\=None_, _refit\=True_, _cv\=None_, _verbose\=0_, _pre\_dispatch\='2\*n\_jobs'_, _error\_score\=nan_, _return\_train\_score\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L1346)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "Link to this definition")

Exhaustive search over specified parameter values for an estimator.

Important members are fit, predict.

GridSearchCV implements a “fit” and a “score” method. It also implements “score\_samples”, “predict”, “predict\_proba”, “decision\_function”, “transform” and “inverse\_transform” if they are implemented in the estimator used.

The parameters of the estimator used to apply these methods are optimized by cross-validated grid-search over a parameter grid.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)
.

Parameters:

**estimator**estimator object

This is assumed to implement the scikit-learn estimator interface. Either estimator needs to provide a `score` function, or `scoring` must be passed.

**param\_grid**dict or list of dictionaries

Dictionary with parameters names (`str`) as keys and lists of parameter settings to try as values, or a list of such dictionaries, in which case the grids spanned by each dictionary in the list are explored. This enables searching over any sequence of parameter settings.

**scoring**str, callable, list, tuple or dict, default=None

Strategy to evaluate the performance of the cross-validated model on the test set.

If `scoring` represents a single score, one can use:

*   a single string (see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
    );
    
*   a callable (see [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
    ) that returns a single value;
    
*   `None`, the `estimator`’s [default evaluation criterion](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-api-overview)
     is used.
    

If `scoring` represents multiple scores, one can use:

*   a list or tuple of unique strings;
    
*   a callable returning a dictionary where the keys are the metric names and the values are the metric scores;
    
*   a dictionary with metric names as keys and callables as values.
    

See [Specifying multiple metrics for evaluation](https://scikit-learn.org/stable/modules/grid_search.html#multimetric-grid-search)
 for an example.

**n\_jobs**int, default=None

Number of jobs to run in parallel. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

Changed in version v0.20: `n_jobs` default changed from 1 to None

**refit**bool, str, or callable, default=True

Refit an estimator using the best found parameters on the whole dataset.

For multiple metric evaluation, this needs to be a `str` denoting the scorer that would be used to find the best parameters for refitting the estimator at the end.

Where there are considerations other than maximum score in choosing a best estimator, `refit` can be set to a function which returns the selected `best_index_` given `cv_results_`. In that case, the `best_estimator_` and `best_params_` will be set according to the returned `best_index_` while the `best_score_` attribute will not be available.

The refitted estimator is made available at the `best_estimator_` attribute and permits using `predict` directly on this `GridSearchCV` instance.

Also for multiple metric evaluation, the attributes `best_index_`, `best_score_` and `best_params_` will only be available if `refit` is set and all of them will be determined w.r.t this specific scorer.

See `scoring` parameter to know more about multiple metric evaluation.

See [Custom refit strategy of a grid search with cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html#sphx-glr-auto-examples-model-selection-plot-grid-search-digits-py)
 to see how to design a custom selection strategy using a callable via `refit`.

See [this example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#sphx-glr-auto-examples-model-selection-plot-grid-search-refit-callable-py)
 for an example of how to use `refit=callable` to balance model complexity and cross-validated score.

Changed in version 0.20: Support for callable added.

**cv**int, cross-validation generator or an iterable, default=None

Determines the cross-validation splitting strategy. Possible inputs for cv are:

*   None, to use the default 5-fold cross validation,
    
*   integer, to specify the number of folds in a `(Stratified)KFold`,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
    ,
    
*   an iterable yielding (train, test) splits as arrays of indices.
    

For integer/None inputs, if the estimator is a classifier and `y` is either binary or multiclass, [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 is used. In all other cases, [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used. These splitters are instantiated with `shuffle=False` so the splits will be the same across calls.

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

Changed in version 0.22: `cv` default value if None changed from 3-fold to 5-fold.

**verbose**int, default=0

Controls the verbosity of information printed during fitting, with higher values yielding more detailed logging.

*   0 : no messages are printed;
    
*   \>=1 : summary of the total number of fits;
    
*   \>=2 : computation time for each fold and parameter candidate;
    
*   \>=3 : fold indices and scores;
    
*   \>=10 : parameter candidate indices and START messages before each fit.
    

**pre\_dispatch**int, or str, default=’2\*n\_jobs’

Controls the number of jobs that get dispatched during parallel execution. Reducing this number can be useful to avoid an explosion of memory consumption when more jobs get dispatched than CPUs can process. This parameter can be:

*   None, in which case all the jobs are immediately created and spawned. Use this for lightweight and fast-running jobs, to avoid delays due to on-demand spawning of the jobs
    
*   An int, giving the exact number of total jobs that are spawned
    
*   A str, giving an expression as a function of n\_jobs, as in ‘2\*n\_jobs’
    

**error\_score**‘raise’ or numeric, default=np.nan

Value to assign to the score if an error occurs in estimator fitting. If set to ‘raise’, the error is raised. If a numeric value is given, FitFailedWarning is raised. This parameter does not affect the refit step, which will always raise the error.

**return\_train\_score**bool, default=False

If `False`, the `cv_results_` attribute will not include training scores. Computing training scores is used to get insights on how different parameter settings impact the overfitting/underfitting trade-off. However computing the scores on the training set can be computationally expensive and is not strictly required to select the parameters that yield the best generalization performance.

Added in version 0.19.

Changed in version 0.21: Default value was changed from `True` to `False`

Attributes:

**cv\_results\_**dict of numpy (masked) ndarrays

A dict with keys as column headers and values as columns, that can be imported into a pandas `DataFrame`.

For instance the below given table

| param\_kernel | param\_gamma | param\_degree | split0\_test\_score | …   | rank\_t… |
| --- | --- | --- | --- | --- | --- |
| ‘poly’ | –   | 2   | 0.80 | …   | 2   |
| ‘poly’ | –   | 3   | 0.70 | …   | 4   |
| ‘rbf’ | 0.1 | –   | 0.80 | …   | 3   |
| ‘rbf’ | 0.2 | –   | 0.93 | …   | 1   |

will be represented by a `cv_results_` dict of:

{
'param\_kernel': masked\_array(data \= \['poly', 'poly', 'rbf', 'rbf'\],
                             mask \= \[False False False False\]...)
'param\_gamma': masked\_array(data \= \[\-- \-- 0.1 0.2\],
                            mask \= \[ True  True False False\]...),
'param\_degree': masked\_array(data \= \[2.0 3.0 \-- \--\],
                             mask \= \[False False  True  True\]...),
'split0\_test\_score'  : \[0.80, 0.70, 0.80, 0.93\],
'split1\_test\_score'  : \[0.82, 0.50, 0.70, 0.78\],
'mean\_test\_score'    : \[0.81, 0.60, 0.75, 0.85\],
'std\_test\_score'     : \[0.01, 0.10, 0.05, 0.08\],
'rank\_test\_score'    : \[2, 4, 3, 1\],
'split0\_train\_score' : \[0.80, 0.92, 0.70, 0.93\],
'split1\_train\_score' : \[0.82, 0.55, 0.70, 0.87\],
'mean\_train\_score'   : \[0.81, 0.74, 0.70, 0.90\],
'std\_train\_score'    : \[0.01, 0.19, 0.00, 0.03\],
'mean\_fit\_time'      : \[0.73, 0.63, 0.43, 0.49\],
'std\_fit\_time'       : \[0.01, 0.02, 0.01, 0.01\],
'mean\_score\_time'    : \[0.01, 0.06, 0.04, 0.04\],
'std\_score\_time'     : \[0.00, 0.00, 0.00, 0.01\],
'params'             : \[{'kernel': 'poly', 'degree': 2}, ...\],
}

Copy to clipboard

For an example of visualization and interpretation of GridSearch results, see [Statistical comparison of models using grid search](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#sphx-glr-auto-examples-model-selection-plot-grid-search-stats-py)
.

NOTE

The key `'params'` is used to store a list of parameter settings dicts for all the parameter candidates.

The `mean_fit_time`, `std_fit_time`, `mean_score_time` and `std_score_time` are all in seconds.

For multi-metric evaluation, the scores for all the scorers are available in the `cv_results_` dict at the keys ending with that scorer’s name (`'_<scorer_name>'`) instead of `'_score'` shown above. (‘split0\_test\_precision’, ‘mean\_train\_precision’ etc.)

**best\_estimator\_**estimator

Estimator that was chosen by the search, i.e. estimator which gave highest score (or smallest loss if specified) on the left out data. Not available if `refit=False`.

See `refit` parameter for more information on allowed values.

**best\_score\_**float

Mean cross-validated score of the best\_estimator

For multi-metric evaluation, this is present only if `refit` is specified.

This attribute is not available if `refit` is a function.

**best\_params\_**dict

Parameter setting that gave the best results on the hold out data.

For multi-metric evaluation, this is present only if `refit` is specified.

**best\_index\_**int

The index (of the `cv_results_` arrays) which corresponds to the best candidate parameter setting.

The dict at `search.cv_results_['params'][search.best_index_]` gives the parameter setting for the best model, that gives the highest mean score (`search.best_score_`).

For multi-metric evaluation, this is present only if `refit` is specified.

**scorer\_**function or a dict

Scorer function used on the held out data to choose the best parameters for the model.

For multi-metric evaluation, this attribute holds the validated `scoring` dict which maps the scorer key to the scorer callable.

**n\_splits\_**int

The number of cross-validation splits (folds/iterations).

**refit\_time\_**float

Seconds used for refitting the best model on the whole dataset.

This is present only if `refit` is not False.

Added in version 0.20.

**multimetric\_**bool

Whether or not the scorers compute several metrics.

`classes_`ndarray of shape (n\_classes,)

Class labels.

`n_features_in_`int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Only defined if `best_estimator_` is defined (see the documentation for the `refit` parameter for more details) and that `best_estimator_` exposes `feature_names_in_` when fit.

Added in version 1.0.

See also

[`ParameterGrid`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterGrid.html#sklearn.model_selection.ParameterGrid "sklearn.model_selection.ParameterGrid")

Generates all the combinations of a hyperparameter grid.

[`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

Utility function to split the data into a development set usable for fitting a GridSearchCV instance and an evaluation set for its final evaluation.

[`sklearn.metrics.make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")

Make a scorer from a performance metric or loss function.

Notes

The parameters selected are those that maximize the score of the left out data, unless an explicit score is passed in which case it is used instead.

If `n_jobs` was set to a value higher than one, the data is copied for each point in the grid (and not `n_jobs` times). This is done for efficiency reasons if individual jobs take very little time, but may raise errors if the dataset is large and not enough memory is available. A workaround in this case is to set `pre_dispatch`. Then, the memory is copied only `pre_dispatch` many times. A reasonable value for `pre_dispatch` is `2 * n_jobs`.

Examples

\>>> from sklearn import svm, datasets
\>>> from sklearn.model\_selection import GridSearchCV
\>>> iris \= datasets.load\_iris()
\>>> parameters \= {'kernel':('linear', 'rbf'), 'C':\[1, 10\]}
\>>> svc \= svm.SVC()
\>>> clf \= GridSearchCV(svc, parameters)
\>>> clf.fit(iris.data, iris.target)
GridSearchCV(estimator=SVC(),
             param\_grid={'C': \[1, 10\], 'kernel': ('linear', 'rbf')})
\>>> sorted(clf.cv\_results\_.keys())
\['mean\_fit\_time', 'mean\_score\_time', 'mean\_test\_score',...\
 'param\_C', 'param\_kernel', 'params',...\
 'rank\_test\_score', 'split0\_test\_score',...\
 'split2\_test\_score', ...\
 'std\_fit\_time', 'std\_score\_time', 'std\_test\_score'\]

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L680)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.decision_function "Link to this definition")

Call decision\_function on the estimator with the best found parameters.

Only available if `refit=True` and the underlying estimator supports `decision_function`.

Parameters:

**X**indexable, length n\_samples

Must fulfill the input assumptions of the underlying estimator.

Returns:

**y\_score**ndarray of shape (n\_samples,) or (n\_samples, n\_classes) or (n\_samples, n\_classes \* (n\_classes-1) / 2)

Result of the decision function for `X` based on the estimator with the best found parameters.

fit(_X_, _y\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L960)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.fit "Link to this definition")

Run fit with all sets of parameters.

Parameters:

**X**array-like of shape (n\_samples, n\_features) or (n\_samples, n\_samples)

Training vectors, where `n_samples` is the number of samples and `n_features` is the number of features. For precomputed kernel or distance matrix, the expected shape of X is (n\_samples, n\_samples).

**y**array-like of shape (n\_samples, n\_output) or (n\_samples,), default=None

Target relative to X for classification or regression; None for unsupervised learning.

**\*\*params**dict of str -> object

Parameters passed to the `fit` method of the estimator, the scorer, and the CV splitter.

If a fit parameter is an array-like whose length is equal to `num_samples` then it will be split by cross-validation along with `X` and `y`. For example, the [sample\_weight](https://scikit-learn.org/stable/glossary.html#term-sample_weight)
 parameter is split because `len(sample_weights) = len(X)`. However, this behavior does not apply to `groups` which is passed to the splitter configured via the `cv` parameter of the constructor. Thus, `groups` is used _to perform the split_ and determines which samples are assigned to the each side of the a split.

Returns:

**self**object

Instance of fitted estimator.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L1299)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.4.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L729)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.inverse_transform "Link to this definition")

Call inverse\_transform on the estimator with the best found params.

Only available if the underlying estimator implements `inverse_transform` and `refit=True`.

Parameters:

**X**indexable, length n\_samples

Must fulfill the input assumptions of the underlying estimator.

Returns:

**X\_original**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

Result of the `inverse_transform` function for `X` based on the estimator with the best found parameters.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L608)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.predict "Link to this definition")

Call predict on the estimator with the best found parameters.

Only available if `refit=True` and the underlying estimator supports `predict`.

Parameters:

**X**indexable, length n\_samples

Must fulfill the input assumptions of the underlying estimator.

Returns:

**y\_pred**ndarray of shape (n\_samples,)

The predicted labels or values for `X` based on the estimator with the best found parameters.

predict\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L655)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.predict_log_proba "Link to this definition")

Call predict\_log\_proba on the estimator with the best found parameters.

Only available if `refit=True` and the underlying estimator supports `predict_log_proba`.

Parameters:

**X**indexable, length n\_samples

Must fulfill the input assumptions of the underlying estimator.

Returns:

**y\_pred**ndarray of shape (n\_samples,) or (n\_samples, n\_classes)

Predicted class log-probabilities for `X` based on the estimator with the best found parameters. The order of the classes corresponds to that in the fitted attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L630)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.predict_proba "Link to this definition")

Call predict\_proba on the estimator with the best found parameters.

Only available if `refit=True` and the underlying estimator supports `predict_proba`.

Parameters:

**X**indexable, length n\_samples

Must fulfill the input assumptions of the underlying estimator.

Returns:

**y\_pred**ndarray of shape (n\_samples,) or (n\_samples, n\_classes)

Predicted class probabilities for `X` based on the estimator with the best found parameters. The order of the classes corresponds to that in the fitted attribute [classes\_](https://scikit-learn.org/stable/glossary.html#term-classes_)
.

score(_X_, _y\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L503)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.score "Link to this definition")

Return the score on the given data, if the estimator has been refit.

This uses the score defined by `scoring` where provided, and the `best_estimator_.score` method otherwise.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples, n\_output) or (n\_samples,), default=None

Target relative to X for classification or regression; None for unsupervised learning.

**\*\*params**dict

Parameters to be passed to the underlying scorer(s).

Added in version 1.4: Only available if `enable_metadata_routing=True`. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**score**float

The score defined by `scoring` if provided, and the `best_estimator_.score` method otherwise.

score\_samples(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L583)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.score_samples "Link to this definition")

Call score\_samples on the estimator with the best found parameters.

Only available if `refit=True` and the underlying estimator supports `score_samples`.

Added in version 0.24.

Parameters:

**X**iterable

Data to predict on. Must fulfill input requirements of the underlying estimator.

Returns:

**y\_score**ndarray of shape (n\_samples,)

The `best_estimator_.score_samples` method.

set\_callbacks(_\*callbacks_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/callback/_callback_support.py#L18)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.set_callbacks "Link to this definition")

Set callbacks for the estimator.

Parameters:

**\*callbacks**callback instances

The callbacks to set.

Returns:

**self**estimator instance

The estimator instance itself.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L705)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV.transform "Link to this definition")

Call transform on the estimator with the best found parameters.

Only available if the underlying estimator supports `transform` and `refit=True`.

Parameters:

**X**indexable, length n\_samples

Must fulfill the input assumptions of the underlying estimator.

Returns:

**Xt**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

`X` transformed in the new space based on the estimator with the best found parameters.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_thumb.png)

[Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)

Analysis of the convergence of penalized logistic regression models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_agglomeration_vs_univariate_selection_thumb.png)

[Feature agglomeration vs. univariate selection](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)

Feature agglomeration vs. univariate selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_mixed_types_thumb.png)

[Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)

Column Transformer with Mixed Types

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_reduction_thumb.png)

[Selecting dimensionality reduction with Pipeline and GridSearchCV](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html)

Selecting dimensionality reduction with Pipeline and GridSearchCV

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_pipe_thumb.png)

[Pipelining: chaining a PCA and a logistic regression](https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html)

Pipelining: chaining a PCA and a logistic regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_union_thumb.png)

[Concatenating multiple feature extraction methods](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html)

Concatenating multiple feature extraction methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_covariance_estimation_thumb.png)

[Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html)

Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_fa_model_selection_thumb.png)

[Model selection with Probabilistic PCA and Factor Analysis (FA)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html)

Model selection with Probabilistic PCA and Factor Analysis (FA)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_hist_grad_boosting_comparison_thumb.png)

[Comparing Random Forests and Histogram Gradient Boosting models](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)

Comparing Random Forests and Histogram Gradient Boosting models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_ridge_regression_thumb.png)

[Comparison of kernel ridge regression and SVR](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_ridge_regression.html)

Comparison of kernel ridge regression and SVR

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pipeline_display_thumb.png)

[Displaying Pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html)

Displaying Pipelines

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_selection_thumb.png)

[Gaussian Mixture Model Selection](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html)

Gaussian Mixture Model Selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_thumb.png)

[Post-tuning the decision threshold for cost-sensitive learning](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Post-tuning the decision threshold for cost-sensitive learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_digits_thumb.png)

[Custom refit strategy of a grid search with cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html)

Custom refit strategy of a grid search with cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_refit_callable_thumb.png)

[Balance model complexity and cross-validated score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html)

Balance model complexity and cross-validated score

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_stats_thumb.png)

[Statistical comparison of models using grid search](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html)

Statistical comparison of models using grid search

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_text_feature_extraction_thumb.png)

[Sample pipeline for text feature extraction and evaluation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)

Sample pipeline for text feature extraction and evaluation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_metric_evaluation_thumb.png)

[Demonstration of multi-metric evaluation on cross\_val\_score and GridSearchCV](https://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html)

Demonstration of multi-metric evaluation on cross\_val\_score and GridSearchCV

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nested_cross_validation_iris_thumb.png)

[Nested versus non-nested cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html)

Nested versus non-nested cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_randomized_search_thumb.png)

[Comparing randomized search and grid search for hyperparameter estimation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_randomized_search.html)

Comparing randomized search and grid search for hyperparameter estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_successive_halving_heatmap_thumb.png)

[Comparison between grid search and successive halving](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_heatmap.html)

Comparison between grid search and successive halving

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multiclass_overview_thumb.png)

[Overview of multiclass training meta-estimators](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html)

Overview of multiclass training meta-estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_caching_nearest_neighbors_thumb.png)

[Caching nearest neighbors](https://scikit-learn.org/stable/auto_examples/neighbors/plot_caching_nearest_neighbors.html)

Caching nearest neighbors

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_kde_sampling_thumb.png)

[Kernel Density Estimation](https://scikit-learn.org/stable/auto_examples/neighbors/plot_digits_kde_sampling.html)

Kernel Density Estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_classification_thumb.png)

[Feature discretization](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html)

Feature discretization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbf_parameters_thumb.png)

[RBF SVM parameters](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html)

RBF SVM parameters

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_kernels_thumb.png)

[Plot classification boundaries with different SVM Kernels](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html)

Plot classification boundaries with different SVM Kernels

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)