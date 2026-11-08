[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.inspection.partial_dependence.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.inspection.partial_dependence.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.inspection.partial_dependence.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.inspection.partial_dependence.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.inspection.partial_dependence.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.inspection.partial_dependence.html)

Collapse Sidebar Expand Sidebar

partial\_dependence[#](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#partial-dependence "Link to this heading")

===============================================================================================================================================================

sklearn.inspection.partial\_dependence(_estimator_, _X_, _features_, _\*_, _sample\_weight\=None_, _categorical\_features\=None_, _feature\_names\=None_, _response\_method\='auto'_, _percentiles\=(0.05, 0.95)_, _grid\_resolution\=100_, _custom\_values\=None_, _method\='auto'_, _kind\='average'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/inspection/_partial_dependence.py#L349)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "Link to this definition")

Partial dependence of `features`.

Partial dependence of a feature (or a set of features) corresponds to the average response of an estimator for each possible value of the feature.

Read more in [Partial Dependence and Individual Conditional Expectation Plots](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#sphx-glr-auto-examples-inspection-plot-partial-dependence-py)
 and the [User Guide](https://scikit-learn.org/stable/modules/partial_dependence.html#partial-dependence)
.

Warning

For [`GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
 and [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
, the `'recursion'` method (used by default) will not account for the `init` predictor of the boosting process. In practice, this will produce the same values as `'brute'` up to a constant offset in the target response, provided that `init` is a constant estimator (which is the default). However, if `init` is not a constant estimator, the partial dependence values are incorrect for `'recursion'` because the offset will be sample-dependent. It is preferable to use the `'brute'` method. Note that this only applies to [`GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
 and [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
, not to [`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 and [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
.

Parameters:

**estimator**BaseEstimator

A fitted estimator object implementing [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
, [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
, or [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
. Multioutput-multiclass classifiers are not supported.

**X**{array-like, sparse matrix or dataframe} of shape (n\_samples, n\_features)

`X` is used to generate a grid of values for the target `features` (where the partial dependence will be evaluated), and also to generate values for the complement features when the `method` is ‘brute’.

**features**array-like of {int, str, bool} or int or str

The feature (e.g. `[0]`) or pair of interacting features (e.g. `[(0, 1)]`) for which the partial dependency should be computed.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights are used to calculate weighted means when averaging the model output. If `None`, then samples are equally weighted. If `sample_weight` is not `None`, then `method` will be set to `'brute'`. Note that `sample_weight` is ignored for `kind='individual'`.

Added in version 1.3.

**categorical\_features**array-like of shape (n\_features,) or shape (n\_categorical\_features,), dtype={bool, int, str}, default=None

Indicates the categorical features.

*   `None`: no feature will be considered categorical;
    
*   boolean array-like: boolean mask of shape `(n_features,)`
    
    indicating which features are categorical. Thus, this array has the same shape has `X.shape[1]`;
    
*   integer or string array-like: integer indices or strings
    
    indicating categorical features.
    

Added in version 1.2.

**feature\_names**array-like of shape (n\_features,), dtype=str, default=None

Name of each feature; `feature_names[i]` holds the name of the feature with index `i`. By default, the name of the feature corresponds to their numerical index for NumPy array and their column name for pandas dataframe.

Added in version 1.2.

**response\_method**{‘auto’, ‘predict\_proba’, ‘decision\_function’}, default=’auto’

Specifies whether to use [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 or [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 as the target response. For regressors this parameter is ignored and the response is always the output of [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
. By default, [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 is tried first and we revert to [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 if it doesn’t exist. If `method` is ‘recursion’, the response is always the output of [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
.

**percentiles**tuple of float, default=(0.05, 0.95)

The lower and upper percentile used to create the extreme values for the grid. Must be in \[0, 1\]. This parameter is overridden by `custom_values` if that parameter is set.

**grid\_resolution**int, default=100

The number of equally spaced points on the grid, for each target feature. This parameter is overridden by `custom_values` if that parameter is set.

**custom\_values**dict

A dictionary mapping the index of an element of `features` to an array of values where the partial dependence should be calculated for that feature. Setting a range of values for a feature overrides `grid_resolution` and `percentiles`.

See [how to use partial\_dependence](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#plt-partial-dependence-custom-values)
 for an example of how this parameter can be used.

Added in version 1.7.

**method**{‘auto’, ‘recursion’, ‘brute’}, default=’auto’

The method used to calculate the averaged predictions:

*   `'recursion'` is only supported for some tree-based estimators (namely [`GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
    , [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
    , [`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
    , [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
    , [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , ) when `kind='average'`. This is more efficient in terms of speed. With this method, the target response of a classifier is always the decision function, not the predicted probabilities. Since the `'recursion'` method implicitly computes the average of the Individual Conditional Expectation (ICE) by design, it is not compatible with ICE and thus `kind` must be `'average'`.
    
*   `'brute'` is supported for any estimator, but is more computationally intensive.
    
*   `'auto'`: the `'recursion'` is used for estimators that support it, and `'brute'` is used otherwise. If `sample_weight` is not `None`, then `'brute'` is used regardless of the estimator.
    

Please see [this note](https://scikit-learn.org/stable/modules/partial_dependence.html#pdp-method-differences)
 for differences between the `'brute'` and `'recursion'` method.

**kind**{‘average’, ‘individual’, ‘both’}, default=’average’

Whether to return the partial dependence averaged across all the samples in the dataset or one value per sample or both. See Returns below.

Note that the fast `method='recursion'` option is only available for `kind='average'` and `sample_weights=None`. Computing individual dependencies and doing weighted averages requires using the slower `method='brute'`.

Added in version 0.24.

Returns:

**predictions**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

individualndarray of shape (n\_outputs, n\_instances, len(values\[0\]), len(values\[1\]), …)

The predictions for all the points in the grid for all samples in X. This is also known as Individual Conditional Expectation (ICE). Only available when `kind='individual'` or `kind='both'`.

averagendarray of shape (n\_outputs, len(values\[0\]), len(values\[1\]), …)

The predictions for all the points in the grid, averaged over all samples in X (or over the training data if `method` is ‘recursion’). Only available when `kind='average'` or `kind='both'`.

grid\_valuesseq of 1d ndarrays

The values with which the grid has been created. The generated grid is a cartesian product of the arrays in `grid_values` where `len(grid_values) == len(features)`. The size of each array `grid_values[j]` is either `grid_resolution`, or the number of unique values in `X[:, j]`, whichever is smaller.

Added in version 1.3.

`n_outputs` corresponds to the number of classes in a multi-class setting, or to the number of tasks for multi-output regression. For classical regression and binary classification `n_outputs==1`. `n_values_feature_j` corresponds to the size `grid_values[j]`.

See also

[`PartialDependenceDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")

Plot Partial Dependence.

[`PartialDependenceDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "sklearn.inspection.PartialDependenceDisplay")

Partial Dependence visualization.

Examples

\>>> X \= \[\[0, 0, 2\], \[1, 0, 0\]\]
\>>> y \= \[0, 1\]
\>>> from sklearn.ensemble import GradientBoostingClassifier
\>>> gb \= GradientBoostingClassifier(random\_state\=0).fit(X, y)
\>>> partial\_dependence(gb, features\=\[0\], X\=X, percentiles\=(0, 1),
...                    grid\_resolution\=2)
(array(\[\[-4.52,  4.52\]\]), \[array(\[ 0.,  1.\])\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_thumb.png)

[Partial Dependence and Individual Conditional Expectation Plots](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html)

Partial Dependence and Individual Conditional Expectation Plots

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)