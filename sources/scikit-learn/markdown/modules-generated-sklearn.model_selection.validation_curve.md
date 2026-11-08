[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.validation_curve.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.validation_curve.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.validation_curve.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.validation_curve.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.validation_curve.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.validation_curve.html)

Collapse Sidebar Expand Sidebar

validation\_curve[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#validation-curve "Link to this heading")

==============================================================================================================================================================

sklearn.model\_selection.validation\_curve(_estimator_, _X_, _y_, _\*_, _param\_name_, _param\_range_, _groups\=None_, _cv\=None_, _scoring\=None_, _n\_jobs\=None_, _pre\_dispatch\='all'_, _verbose\=0_, _error\_score\=nan_, _params\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_validation.py#L2265)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve "Link to this definition")

Validation curve.

Determine training and test scores for varying parameter values.

Compute scores for an estimator with different values of a specified parameter. This is similar to grid search with one parameter. However, this will also compute training scores and is merely a utility for plotting the results.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/learning_curve.html#validation-curve)
.

Parameters:

**estimator**object type that implements the “fit” method

An object of that type which is cloned for each validation. It must also implement “predict” unless `scoring` is a callable that doesn’t rely on “predict” to compute a score.

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training vector, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs) or None

Target relative to X for classification or regression; None for unsupervised learning.

**param\_name**str

Name of the parameter that will be varied.

**param\_range**array-like of shape (n\_values,)

The values of the parameter that will be evaluated.

**groups**array-like of shape (n\_samples,), default=None

Group labels for the samples used while splitting the dataset into train/test set. Only used in conjunction with a “Group” [cv](https://scikit-learn.org/stable/glossary.html#term-cv)
 instance (e.g., [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")
).

Changed in version 1.6: `groups` can only be passed if metadata routing is not enabled via `sklearn.set_config(enable_metadata_routing=True)`. When routing is enabled, pass `groups` alongside other metadata via the `params` argument instead. E.g.: `validation_curve(..., params={'groups': groups})`.

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

**scoring**str or callable, default=None

Scoring method to use to evaluate the training and test sets.

*   str: see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
     for options.
    
*   callable: a scorer callable object (e.g., function) with signature `scorer(estimator, X, y)`. See [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
     for details.
    
*   `None`: the `estimator`’s [default evaluation criterion](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-api-overview)
     is used.
    

**n\_jobs**int, default=None

Number of jobs to run in parallel. Training the estimator and computing the score are parallelized over the combinations of each parameter value and each cross-validation split. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**pre\_dispatch**int or str, default=’all’

Number of predispatched jobs for parallel execution (default is all). The option can reduce the allocated memory. The str can be an expression like ‘2\*n\_jobs’.

**verbose**int, default=0

Controls the verbosity: the higher, the more messages.

**error\_score**‘raise’ or numeric, default=np.nan

Value to assign to the score if an error occurs in estimator fitting. If set to ‘raise’, the error is raised. If a numeric value is given, FitFailedWarning is raised.

Added in version 0.20.

**params**dict, default=None

Parameters to pass to the estimator, scorer and cross-validation object.

*   If `enable_metadata_routing=False` (default): Parameters directly passed to the `fit` method of the estimator.
    
*   If `enable_metadata_routing=True`: Parameters safely routed to the `fit` method of the estimator, to the scorer and to the cross-validation object. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
     for more details.
    

Added in version 1.6.

Returns:

**train\_scores**array of shape (n\_ticks, n\_cv\_folds)

Scores on training sets.

**test\_scores**array of shape (n\_ticks, n\_cv\_folds)

Scores on test set.

See also

[`ValidationCurveDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ValidationCurveDisplay.html#sklearn.model_selection.ValidationCurveDisplay.from_estimator "sklearn.model_selection.ValidationCurveDisplay.from_estimator")

Plot the validation curve given an estimator, the data, and the parameter to vary.

Notes

See [Effect of model regularization on training and test error](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html#sphx-glr-auto-examples-model-selection-plot-train-error-vs-test-error-py)

Examples

\>>> import numpy as np
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.model\_selection import validation\_curve
\>>> from sklearn.linear\_model import LogisticRegression
\>>> X, y \= make\_classification(n\_samples\=1\_000, random\_state\=0)
\>>> logistic\_regression \= LogisticRegression()
\>>> param\_name, param\_range \= "C", np.logspace(\-8, 3, 10)
\>>> train\_scores, test\_scores \= validation\_curve(
...     logistic\_regression, X, y, param\_name\=param\_name, param\_range\=param\_range
... )
\>>> print(f"The average train accuracy is {train\_scores.mean():.2f}")
The average train accuracy is 0.81
\>>> print(f"The average test accuracy is {test\_scores.mean():.2f}")
The average test accuracy is 0.81

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_scale_c_thumb.png)

[Scaling the regularization parameter for SVCs](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html)

Scaling the regularization parameter for SVCs

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)