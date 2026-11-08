[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html)

Collapse Sidebar Expand Sidebar

HalvingGridSearchCV[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#halvinggridsearchcv "Link to this heading")

======================================================================================================================================================================

class sklearn.model\_selection.HalvingGridSearchCV(_estimator_, _param\_grid_, _\*_, _factor\=3_, _resource\='n\_samples'_, _max\_resources\='auto'_, _min\_resources\='exhaust'_, _aggressive\_elimination\=False_, _cv\=5_, _scoring\=None_, _refit\=True_, _error\_score\=nan_, _return\_train\_score\=True_, _random\_state\=None_, _n\_jobs\=None_, _verbose\=0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search_successive_halving.py#L391)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "Link to this definition")

Search over specified parameter values with successive halving.

The search strategy starts evaluating all the candidates with a small amount of resources and iteratively selects the best candidates, using more and more resources.

Read more in the [User guide](https://scikit-learn.org/stable/modules/grid_search.html#successive-halving-user-guide)
.

Note

This estimator is still **experimental** for now: the predictions and the API might change without any deprecation cycle. To use it, you need to explicitly import `enable_halving_search_cv`:

\>>> \# explicitly require this experimental feature
\>>> from sklearn.experimental import enable\_halving\_search\_cv \# noqa
\>>> \# now you can import normally from model\_selection
\>>> from sklearn.model\_selection import HalvingGridSearchCV

Copy to clipboard

Parameters:

**estimator**estimator object

This is assumed to implement the scikit-learn estimator interface. Either estimator needs to provide a `score` function, or `scoring` must be passed.

**param\_grid**dict or list of dictionaries

Dictionary with parameters names (string) as keys and lists of parameter settings to try as values, or a list of such dictionaries, in which case the grids spanned by each dictionary in the list are explored. This enables searching over any sequence of parameter settings.

**factor**int or float, default=3

The ‘halving’ parameter, which determines the proportion of candidates that are selected for each subsequent iteration. For example, `factor=3` means that only one third of the candidates are selected.

**resource**`'n_samples'` or str, default=’n\_samples’

Defines the resource that increases with each iteration. By default, the resource is the number of samples. It can also be set to any parameter of the base estimator that accepts positive integer values, e.g. ‘n\_iterations’ or ‘n\_estimators’ for a gradient boosting estimator. In this case `max_resources` cannot be ‘auto’ and must be set explicitly.

**max\_resources**int, default=’auto’

The maximum amount of resource that any candidate is allowed to use for a given iteration. By default, this is set to `n_samples` when `resource='n_samples'` (default), else an error is raised.

**min\_resources**{‘exhaust’, ‘smallest’} or int, default=’exhaust’

The minimum amount of resource that any candidate is allowed to use for a given iteration. Equivalently, this defines the amount of resources `r0` that are allocated for each candidate at the first iteration.

*   ‘smallest’ is a heuristic that sets `r0` to a small value:
    
    *   `n_splits * 2` when `resource='n_samples'` for a regression problem
        
    *   `n_classes * n_splits * 2` when `resource='n_samples'` for a classification problem
        
    *   `1` when `resource != 'n_samples'`
        
*   ‘exhaust’ will set `r0` such that the **last** iteration uses as much resources as possible. Namely, the last iteration will use the highest value smaller than `max_resources` that is a multiple of both `min_resources` and `factor`. In general, using ‘exhaust’ leads to a more accurate estimator, but is slightly more time consuming.
    

Note that the amount of resources used at each iteration is always a multiple of `min_resources`.

**aggressive\_elimination**bool, default=False

This is only relevant in cases where there isn’t enough resources to reduce the remaining candidates to at most `factor` after the last iteration. If `True`, then the search process will ‘replay’ the first iteration for as long as needed until the number of candidates is small enough. This is `False` by default, which means that the last iteration may evaluate more than `factor` candidates. See [Aggressive elimination of candidates](https://scikit-learn.org/stable/modules/grid_search.html#aggressive-elimination)
 for more details.

**cv**int, cross-validation generator or iterable, default=5

Determines the cross-validation splitting strategy. Possible inputs for cv are:

*   integer, to specify the number of folds in a `(Stratified)KFold`,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
    ,
    
*   an iterable yielding (train, test) splits as arrays of indices.
    

For integer/None inputs, if the estimator is a classifier and `y` is either binary or multiclass, [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 is used. In all other cases, [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used. These splitters are instantiated with `shuffle=False` so the splits will be the same across calls.

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

Note

Due to implementation details, the folds produced by `cv` must be the same across multiple calls to `cv.split()`. For built-in `scikit-learn` iterators, this can be achieved by deactivating shuffling (`shuffle=False`), or by setting the `cv`’s `random_state` parameter to an integer.

**scoring**str or callable, default=None

Scoring method to use to evaluate the predictions on the test set.

*   str: see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
     for options.
    
*   callable: a scorer callable object (e.g., function) with signature `scorer(estimator, X, y)`. See [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
     for details.
    
*   `None`: the `estimator`’s [default evaluation criterion](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-api-overview)
     is used.
    

**refit**bool or callable, default=True

Refit an estimator using the best found parameters on the whole dataset.

Where there are considerations other than maximum score in choosing a best estimator, `refit` can be set to a function which returns the selected `best_index_` given `cv_results_`. In that case, the `best_estimator_` and `best_params_` will be set according to the returned `best_index_` while the `best_score_` attribute will not be available.

The refitted estimator is made available at the `best_estimator_` attribute and permits using `predict` directly on this `HalvingGridSearchCV` instance.

See [this example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html#sphx-glr-auto-examples-model-selection-plot-grid-search-refit-callable-py)
 for an example of how to use `refit=callable` to balance model complexity and cross-validated score.

**error\_score**‘raise’ or numeric

Value to assign to the score if an error occurs in estimator fitting. If set to ‘raise’, the error is raised. If a numeric value is given, FitFailedWarning is raised. This parameter does not affect the refit step, which will always raise the error. Default is `np.nan`.

**return\_train\_score**bool, default=True

If `False`, the `cv_results_` attribute will not include training scores. Computing training scores is used to get insights on how different parameter settings impact the overfitting/underfitting trade-off. However computing the scores on the training set can be computationally expensive and is not strictly required to select the parameters that yield the best generalization performance.

**random\_state**int, RandomState instance or None, default=None

Pseudo random number generator state used for subsampling the dataset when `resources != 'n_samples'`. Ignored otherwise. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**n\_jobs**int or None, default=None

Number of jobs to run in parallel. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**verbose**int

Controls the verbosity: the higher, the more messages.

Attributes:

**n\_resources\_**list of int

The amount of resources used at each iteration.

**n\_candidates\_**list of int

The number of candidate parameters that were evaluated at each iteration.

**n\_remaining\_candidates\_**int

The number of candidate parameters that are left after the last iteration. It corresponds to `ceil(n_candidates[-1] / factor)`

**max\_resources\_**int

The maximum number of resources that any candidate is allowed to use for a given iteration. Note that since the number of resources used at each iteration must be a multiple of `min_resources_`, the actual number of resources used at the last iteration may be smaller than `max_resources_`.

**min\_resources\_**int

The amount of resources that are allocated for each candidate at the first iteration.

**n\_iterations\_**int

The actual number of iterations that were run. This is equal to `n_required_iterations_` if `aggressive_elimination` is `True`. Else, this is equal to `min(n_possible_iterations_, n_required_iterations_)`.

**n\_possible\_iterations\_**int

The number of iterations that are possible starting with `min_resources_` resources and without exceeding `max_resources_`.

**n\_required\_iterations\_**int

The number of iterations that are required to end up with less than `factor` candidates at the last iteration, starting with `min_resources_` resources. This will be smaller than `n_possible_iterations_` when there isn’t enough resources.

**cv\_results\_**dict of numpy (masked) ndarrays

A dict with keys as column headers and values as columns, that can be imported into a pandas `DataFrame`. It contains lots of information for analysing the results of a search. Please refer to the [User guide](https://scikit-learn.org/stable/modules/grid_search.html#successive-halving-cv-results)
 for details. For an example of analysing `cv_results_`, see [Statistical comparison of models using grid search](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html#sphx-glr-auto-examples-model-selection-plot-grid-search-stats-py)
.

**best\_estimator\_**estimator or dict

Estimator that was chosen by the search, i.e. estimator which gave highest score (or smallest loss if specified) on the left out data, in the last halving iteration. Not available if `refit=False`.

Note

`best_estimator_` reflects the winner of the final iteration only. `cv_results_` may contain candidates with a higher `rank_test_score`, but those scores were obtained with fewer resources and are less reliable. To inspect final-iteration results explicitly, filter `cv_results_` by `cv_results_['iter'] == n_iterations_ - 1`.

**best\_score\_**float

Mean cross-validated score of the `best_estimator_`, computed over the candidates from the last halving iteration only.

**best\_params\_**dict

Parameter setting that gave the best results on the hold out data in the last halving iteration.

**best\_index\_**int

The index (of the `cv_results_` arrays) which corresponds to the best candidate parameter setting.

The dict at `search.cv_results_['params'][search.best_index_]` gives the parameter setting for the best model, that gives the highest mean score (`search.best_score_`).

**scorer\_**function or a dict

Scorer function used on the held out data to choose the best parameters for the model.

**n\_splits\_**int

The number of cross-validation splits (folds/iterations).

**refit\_time\_**float

Seconds used for refitting the best model on the whole dataset.

This is present only if `refit` is not False.

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

[`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")

Random search over a set of parameters using successive halving.

Notes

The parameters selected are those that maximize the score of the held-out data, according to the scoring parameter.

All parameter combinations scored with a NaN will share the lowest rank.

Examples

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.ensemble import RandomForestClassifier
\>>> from sklearn.experimental import enable\_halving\_search\_cv  \# noqa
\>>> from sklearn.model\_selection import HalvingGridSearchCV
...
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> clf \= RandomForestClassifier(random\_state\=0)
...
\>>> param\_grid \= {"max\_depth": \[3, None\],
...               "min\_samples\_split": \[5, 10\]}
\>>> search \= HalvingGridSearchCV(clf, param\_grid, resource\='n\_estimators',
...                              max\_resources\=10,
...                              random\_state\=0).fit(X, y)
\>>> search.best\_params\_
{'max\_depth': None, 'min\_samples\_split': 10, 'n\_estimators': 9}

Copy to clipboard

decision\_function(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L680)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV.decision_function "Link to this definition")

Call decision\_function on the estimator with the best found parameters.

Only available if `refit=True` and the underlying estimator supports `decision_function`.

Parameters:

**X**indexable, length n\_samples

Must fulfill the input assumptions of the underlying estimator.

Returns:

**y\_score**ndarray of shape (n\_samples,) or (n\_samples, n\_classes) or (n\_samples, n\_classes \* (n\_classes-1) / 2)

Result of the decision function for `X` based on the estimator with the best found parameters.

fit(_X_, _y\=None_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search_successive_halving.py#L216)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV.fit "Link to this definition")

Run fit with all sets of parameters.

Parameters:

**X**array-like, shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like, shape (n\_samples,) or (n\_samples, n\_output), optional

Target relative to X for classification or regression; None for unsupervised learning.

**\*\*params**dict of string -> object

Parameters passed to the `fit` method of the estimator.

Returns:

**self**object

Instance of fitted estimator.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L1299)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.4.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L729)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV.inverse_transform "Link to this definition")

Call inverse\_transform on the estimator with the best found params.

Only available if the underlying estimator implements `inverse_transform` and `refit=True`.

Parameters:

**X**indexable, length n\_samples

Must fulfill the input assumptions of the underlying estimator.

Returns:

**X\_original**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

Result of the `inverse_transform` function for `X` based on the estimator with the best found parameters.

predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L608)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV.predict "Link to this definition")

Call predict on the estimator with the best found parameters.

Only available if `refit=True` and the underlying estimator supports `predict`.

Parameters:

**X**indexable, length n\_samples

Must fulfill the input assumptions of the underlying estimator.

Returns:

**y\_pred**ndarray of shape (n\_samples,)

The predicted labels or values for `X` based on the estimator with the best found parameters.

predict\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L655)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV.predict_log_proba "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV.predict_proba "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV.score "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV.score_samples "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV.set_callbacks "Link to this definition")

Set callbacks for the estimator.

Parameters:

**\*callbacks**callback instances

The callbacks to set.

Returns:

**self**estimator instance

The estimator instance itself.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV.set_params "Link to this definition")

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
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV.transform "Link to this definition")

Call transform on the estimator with the best found parameters.

Only available if the underlying estimator supports `transform` and `refit=True`.

Parameters:

**X**indexable, length n\_samples

Must fulfill the input assumptions of the underlying estimator.

Returns:

**Xt**{ndarray, sparse matrix} of shape (n\_samples, n\_features)

`X` transformed in the new space based on the estimator with the best found parameters.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_successive_halving_heatmap_thumb.png)

[Comparison between grid search and successive halving](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_heatmap.html)

Comparison between grid search and successive halving

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_successive_halving_iterations_thumb.png)

[Successive Halving Iterations](https://scikit-learn.org/stable/auto_examples/model_selection/plot_successive_halving_iterations.html)

Successive Halving Iterations

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)