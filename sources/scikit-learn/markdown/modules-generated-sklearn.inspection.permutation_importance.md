[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.inspection.permutation_importance.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.inspection.permutation_importance.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.inspection.permutation_importance.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.inspection.permutation_importance.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.inspection.permutation_importance.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.inspection.permutation_importance.html)

Collapse Sidebar Expand Sidebar

permutation\_importance[#](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#permutation-importance "Link to this heading")

===========================================================================================================================================================================

sklearn.inspection.permutation\_importance(_estimator_, _X_, _y_, _\*_, _scoring\=None_, _n\_repeats\=5_, _n\_jobs\=None_, _random\_state\=None_, _sample\_weight\=None_, _max\_samples\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/inspection/_permutation_importance.py#L114)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "Link to this definition")

Permutation importance for feature evaluation [\[BRE\]](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#rd9e56ef97513-bre)
.

The [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator)
 is required to be a fitted estimator. `X` can be the data set used to train the estimator or a hold-out set. The permutation importance of a feature is calculated as follows. First, a baseline metric, defined by [scoring](https://scikit-learn.org/stable/glossary.html#term-scoring)
, is evaluated on a (potentially different) dataset defined by the `X`. Next, a feature column from the validation set is permuted and the metric is evaluated again. The permutation importance is defined to be the difference between the baseline metric and metric from permutating the feature column.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/permutation_importance.html#permutation-importance)
.

Parameters:

**estimator**object

An estimator that has already been [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted)
 and is compatible with [scorer](https://scikit-learn.org/stable/glossary.html#term-scorer)
.

**X**ndarray or DataFrame, shape (n\_samples, n\_features)

Data on which permutation importance will be computed.

**y**array-like or None, shape (n\_samples, ) or (n\_samples, n\_classes)

Targets for supervised or `None` for unsupervised.

**scoring**str, callable, list, tuple, or dict, default=None

Scorer to use. If `scoring` represents a single score, one can use:

*   str: see [String name scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-string-names)
     for options.
    
*   callable: a scorer callable object (e.g., function) with signature `scorer(estimator, X, y)`. See [Callable scorers](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-callable)
     for details.
    
*   `None`: the `estimator`’s [default evaluation criterion](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-api-overview)
     is used.
    

If `scoring` represents multiple scores, one can use:

*   a list or tuple of unique strings;
    
*   a callable returning a dictionary where the keys are the metric names and the values are the metric scores;
    
*   a dictionary with metric names as keys and callables as values.
    

Passing multiple scores to `scoring` is more efficient than calling `permutation_importance` for each of the scores as it reuses predictions to avoid redundant computation.

**n\_repeats**int, default=5

Number of times to permute a feature.

**n\_jobs**int or None, default=None

Number of jobs to run in parallel. The computation is done by computing permutation score for each columns and parallelized over the columns. `None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**random\_state**int, RandomState instance, default=None

Pseudo-random number generator to control the permutations of each feature. Pass an int to get reproducible results across function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights used in scoring.

Added in version 0.24.

**max\_samples**int or float, default=1.0

The number of samples to draw from X to compute feature importance in each repeat (without replacement).

*   If int, then draw `max_samples` samples.
    
*   If float, then draw `max_samples * X.shape[0]` samples.
    
*   If `max_samples` is equal to `1.0` or `X.shape[0]`, all samples will be used.
    

While using this option may provide less accurate importance estimates, it keeps the method tractable when evaluating feature importance on large datasets. In combination with `n_repeats`, this allows to control the computational speed vs statistical accuracy trade-off of this method.

Added in version 1.0.

Returns:

**result**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")
 or dict of such instances

Dictionary-like object, with the following attributes.

importances\_meanndarray of shape (n\_features, )

Mean of feature importance over `n_repeats`.

importances\_stdndarray of shape (n\_features, )

Standard deviation over `n_repeats`.

importancesndarray of shape (n\_features, n\_repeats)

Raw permutation importance scores.

If there are multiple scoring metrics in the scoring parameter `result` is a dict with scorer names as keys (e.g. ‘roc\_auc’) and `Bunch` objects like above as values.

References

\[[BRE](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#id1)\
\]

[L. Breiman, “Random Forests”, Machine Learning, 45(1), 5-32, 2001.](https://doi.org/10.1023/A:1010933404324)

Examples

\>>> from sklearn.linear\_model import LogisticRegression
\>>> from sklearn.inspection import permutation\_importance
\>>> X \= \[\[1, 9, 9\],\[1, 9, 9\],\[1, 9, 9\],\
...      \[0, 9, 9\],\[0, 9, 9\],\[0, 9, 9\]\]
\>>> y \= \[1, 1, 1, 0, 0, 0\]
\>>> clf \= LogisticRegression().fit(X, y)
\>>> result \= permutation\_importance(clf, X, y, n\_repeats\=10,
...                                 random\_state\=0)
\>>> result.importances\_mean
array(\[0.4666, 0.       , 0.       \])
\>>> result.importances\_std
array(\[0.2211, 0.       , 0.       \])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_importances_thumb.png)

[Feature importances with a forest of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html)

Feature importances with a forest of trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)

[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)

Gradient Boosting regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_thumb.png)

[Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)

Permutation Importance vs Random Forest Feature Importance (MDI)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_multicollinear_thumb.png)

[Permutation Importance with Multicollinear or Correlated Features](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html)

Permutation Importance with Multicollinear or Correlated Features

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)