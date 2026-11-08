[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.cross_val_predict.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.cross_val_predict.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.cross_val_predict.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.cross_val_predict.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.cross_val_predict.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.cross_val_predict.html)

Collapse Sidebar Expand Sidebar

cross\_val\_predict[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#cross-val-predict "Link to this heading")

==================================================================================================================================================================

sklearn.model\_selection.cross\_val\_predict(_estimator_, _X_, _y\=None_, _\*_, _groups\=None_, _cv\=None_, _n\_jobs\=None_, _verbose\=0_, _params\=None_, _pre\_dispatch\='2\*n\_jobs'_, _method\='predict'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_validation.py#L1007)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "Link to this definition")

Generate cross-validated estimates for each input data point.

The data is split according to the cv parameter. Each sample belongs to exactly one test set, and its prediction is computed with an estimator fitted on the corresponding training set.

Passing these predictions into an evaluation metric may not be a valid way to measure generalization performance. Results can differ from [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
 and [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
 unless all tests sets have equal size and the metric decomposes over samples.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
.

Parameters:

**estimator**estimator

The estimator instance to use to fit the data. It must implement a `fit` method and the method given by the `method` parameter.

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

The data to fit. Can be, for example a list, or an array at least 2d.

**y**{array-like, sparse matrix} of shape (n\_samples,) or (n\_samples, n\_outputs), default=None

The target variable to try to predict in the case of supervised learning.

**groups**array-like of shape (n\_samples,), default=None

Group labels for the samples used while splitting the dataset into train/test set. Only used in conjunction with a “Group” [cv](https://scikit-learn.org/stable/glossary.html#term-cv)
 instance (e.g., [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
).

Changed in version 1.4: `groups` can only be passed if metadata routing is not enabled via `sklearn.set_config(enable_metadata_routing=True)`. When routing is enabled, pass `groups` alongside other metadata via the `params` argument instead. E.g.: `cross_val_predict(..., params={'groups': groups})`.

**cv**int, cross-validation generator or an iterable, default=None

Determines the cross-validation splitting strategy. Possible inputs for cv are:

*   None, to use the default 5-fold cross validation,
    
*   int, to specify the number of folds in a `(Stratified)KFold`,
    
*   [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter)
    ,
    
*   An iterable that generates (train, test) splits as arrays of indices.
    

For int/None inputs, if the estimator is a classifier and `y` is either binary or multiclass, [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
 is used. In all other cases, [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
 is used. These splitters are instantiated with `shuffle=False` so the splits will be the same across calls.

Refer [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
 for the various cross-validation strategies that can be used here.

Changed in version 0.22: `cv` default value if None changed from 3-fold to 5-fold.

**n\_jobs**int, default=None

Number of jobs to run in parallel. Training the estimator and predicting are parallelized over the cross-validation splits. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**verbose**int, default=0

The verbosity level.

**params**dict, default=None

Parameters to pass to the underlying estimator’s `fit` and the CV splitter.

Added in version 1.4.

**pre\_dispatch**int or str, default=’2\*n\_jobs’

Controls the number of jobs that get dispatched during parallel execution. Reducing this number can be useful to avoid an explosion of memory consumption when more jobs get dispatched than CPUs can process. This parameter can be:

*   None, in which case all the jobs are immediately created and spawned. Use this for lightweight and fast-running jobs, to avoid delays due to on-demand spawning of the jobs
    
*   An int, giving the exact number of total jobs that are spawned
    
*   A str, giving an expression as a function of n\_jobs, as in ‘2\*n\_jobs’
    

**method**{‘predict’, ‘predict\_proba’, ‘predict\_log\_proba’, ‘decision\_function’}, default=’predict’

The method to be invoked by `estimator`.

Returns:

**predictions**ndarray

This is the result of calling `method`. Shape:

*   When `method` is ‘predict’ and in special case where `method` is ‘decision\_function’ and the target is binary: (n\_samples,)
    
*   When `method` is one of {‘predict\_proba’, ‘predict\_log\_proba’, ‘decision\_function’} (unless special case above): (n\_samples, n\_classes)
    
*   If `estimator` is [multioutput](https://scikit-learn.org/stable/glossary.html#term-multioutput)
    , an extra dimension ‘n\_outputs’ is added to the end of each shape above.
    

See also

[`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")

Calculate score for each CV split.

[`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")

Calculate one or more scores and timings for each CV split.

Notes

In the case that one or more classes are absent in a training portion, a default score needs to be assigned to all instances for that class if `method` produces columns per class, as in {‘decision\_function’, ‘predict\_proba’, ‘predict\_log\_proba’}. For `predict_proba` this value is 0. In order to ensure finite output, we approximate negative infinity by the minimum finite float value for the dtype in other cases.

Examples

\>>> from sklearn import datasets, linear\_model
\>>> from sklearn.model\_selection import cross\_val\_predict
\>>> diabetes \= datasets.load\_diabetes()
\>>> X \= diabetes.data\[:150\]
\>>> y \= diabetes.target\[:150\]
\>>> lasso \= linear\_model.Lasso()
\>>> y\_pred \= cross\_val\_predict(lasso, X, y, cv\=3)

Copy to clipboard

For a detailed example of using `cross_val_predict` to visualize prediction errors, please see [Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html#sphx-glr-auto-examples-model-selection-plot-cv-predict-py)
.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_thumb.png)

[Combine predictors using stacking](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)

Combine predictors using stacking

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_predict_thumb.png)

[Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html)

Plotting Cross-Validated Predictions

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)