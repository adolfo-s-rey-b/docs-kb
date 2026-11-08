[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.inspection.PartialDependenceDisplay.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.inspection.PartialDependenceDisplay.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.inspection.PartialDependenceDisplay.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.inspection.PartialDependenceDisplay.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.inspection.PartialDependenceDisplay.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.inspection.PartialDependenceDisplay.html)

Collapse Sidebar Expand Sidebar

PartialDependenceDisplay[#](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#partialdependencedisplay "Link to this heading")

================================================================================================================================================================================

class sklearn.inspection.PartialDependenceDisplay(_pd\_results_, _\*_, _features_, _feature\_names_, _target\_idx_, _deciles_, _kind\='average'_, _subsample\=1000_, _random\_state\=None_, _is\_categorical\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/inspection/_plot/partial_dependence.py#L22)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "Link to this definition")

Partial Dependence Plot (PDP) and Individual Conditional Expectation (ICE).

It is recommended to use [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
 to create a [`PartialDependenceDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "sklearn.inspection.PartialDependenceDisplay")
. All parameters are stored as attributes.

For general information regarding `scikit-learn` visualization tools, see the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For guidance on interpreting these plots, refer to the [Inspection Guide](https://scikit-learn.org/stable/modules/partial_dependence.html#partial-dependence)
.

For an example on how to use this class, see the following example: [Advanced Plotting With Partial Dependence](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html#sphx-glr-auto-examples-inspection-plot-partial-dependence-visualization-api-py)
.

Added in version 0.22.

Parameters:

**pd\_results**list of Bunch

Results of [`partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
 for `features`.

**features**list of (int,) or list of (int, int)

Indices of features for a given plot. A tuple of one integer will plot a partial dependence curve of one feature. A tuple of two integers will plot a two-way partial dependence curve as a contour plot.

**feature\_names**list of str

Feature names corresponding to the indices in `features`.

**target\_idx**int

*   In a multiclass setting, specifies the class for which the PDPs should be computed. Note that for binary classification, the positive class (index 1) is always used.
    
*   In a multioutput setting, specifies the task for which the PDPs should be computed.
    

Ignored in binary classification or classical regression settings.

**deciles**dict

Deciles for feature indices in `features`.

**kind**{‘average’, ‘individual’, ‘both’} or list of such str, default=’average’

Whether to plot the partial dependence averaged across all the samples in the dataset or one line per sample or both.

*   `kind='average'` results in the traditional PD plot;
    
*   `kind='individual'` results in the ICE plot;
    
*   `kind='both'` results in plotting both the ICE and PD on the same plot.
    

A list of such strings can be provided to specify `kind` on a per-plot basis. The length of the list should be the same as the number of interaction requested in `features`.

Note

ICE (‘individual’ or ‘both’) is not a valid option for 2-ways interactions plot. As a result, an error will be raised. 2-ways interaction plots should always be configured to use the ‘average’ kind instead.

Note

The fast `method='recursion'` option is only available for `kind='average'` and `sample_weights=None`. Computing individual dependencies and doing weighted averages requires using the slower `method='brute'`.

Added in version 0.24: Add `kind` parameter with `'average'`, `'individual'`, and `'both'` options.

Added in version 1.1: Add the possibility to pass a list of string specifying `kind` for each plot.

**subsample**float, int or None, default=1000

Sampling for ICE curves when `kind` is ‘individual’ or ‘both’. If float, should be between 0.0 and 1.0 and represent the proportion of the dataset to be used to plot ICE curves. If int, represents the maximum absolute number of samples to use.

Note that the full dataset is still used to calculate partial dependence when `kind='both'`.

Added in version 0.24.

**random\_state**int, RandomState instance or None, default=None

Controls the randomness of the selected samples when subsamples is not `None`. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
 for details.

Added in version 0.24.

**is\_categorical**list of (bool,) or list of (bool, bool), default=None

Whether each target feature in `features` is categorical or not. The list should be same size as `features`. If `None`, all features are assumed to be continuous.

Added in version 1.2.

Attributes:

**bounding\_ax\_**matplotlib Axes or None

If `ax` is an axes or None, the `bounding_ax_` is the axes where the grid of partial dependence plots are drawn. If `ax` is a list of axes or a numpy array of axes, `bounding_ax_` is None.

**axes\_**ndarray of matplotlib Axes

If `ax` is an axes or None, `axes_[i, j]` is the axes on the i-th row and j-th column. If `ax` is a list of axes, `axes_[i]` is the i-th item in `ax`. Elements that are None correspond to a nonexisting axes in that position.

**lines\_**ndarray of matplotlib Artists

If `ax` is an axes or None, `lines_[i, j]` is the partial dependence curve on the i-th row and j-th column. If `ax` is a list of axes, `lines_[i]` is the partial dependence curve corresponding to the i-th item in `ax`. Elements that are None correspond to a nonexisting axes or an axes that does not include a line plot.

**deciles\_vlines\_**ndarray of matplotlib LineCollection

If `ax` is an axes or None, `vlines_[i, j]` is the line collection representing the x axis deciles of the i-th row and j-th column. If `ax` is a list of axes, `vlines_[i]` corresponds to the i-th item in `ax`. Elements that are None correspond to a nonexisting axes or an axes that does not include a PDP plot.

Added in version 0.23.

**deciles\_hlines\_**ndarray of matplotlib LineCollection

If `ax` is an axes or None, `vlines_[i, j]` is the line collection representing the y axis deciles of the i-th row and j-th column. If `ax` is a list of axes, `vlines_[i]` corresponds to the i-th item in `ax`. Elements that are None correspond to a nonexisting axes or an axes that does not include a 2-way plot.

Added in version 0.23.

**contours\_**ndarray of matplotlib Artists

If `ax` is an axes or None, `contours_[i, j]` is the partial dependence plot on the i-th row and j-th column. If `ax` is a list of axes, `contours_[i]` is the partial dependence plot corresponding to the i-th item in `ax`. Elements that are None correspond to a nonexisting axes or an axes that does not include a contour plot.

**bars\_**ndarray of matplotlib Artists

If `ax` is an axes or None, `bars_[i, j]` is the partial dependence bar plot on the i-th row and j-th column (for a categorical feature). If `ax` is a list of axes, `bars_[i]` is the partial dependence bar plot corresponding to the i-th item in `ax`. Elements that are None correspond to a nonexisting axes or an axes that does not include a bar plot.

Added in version 1.2.

**heatmaps\_**ndarray of matplotlib Artists

If `ax` is an axes or None, `heatmaps_[i, j]` is the partial dependence heatmap on the i-th row and j-th column (for a pair of categorical features) . If `ax` is a list of axes, `heatmaps_[i]` is the partial dependence heatmap corresponding to the i-th item in `ax`. Elements that are None correspond to a nonexisting axes or an axes that does not include a heatmap.

Added in version 1.2.

**figure\_**matplotlib Figure

Figure containing partial dependence plots.

See also

[`partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")

Compute Partial Dependence values.

[`PartialDependenceDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")

Plot Partial Dependence.

Examples

\>>> import numpy as np
\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_friedman1
\>>> from sklearn.ensemble import GradientBoostingRegressor
\>>> from sklearn.inspection import PartialDependenceDisplay
\>>> from sklearn.inspection import partial\_dependence
\>>> X, y \= make\_friedman1()
\>>> clf \= GradientBoostingRegressor(n\_estimators\=10).fit(X, y)
\>>> features, feature\_names \= \[(0,)\], \[f"Features #{i}" for i in range(X.shape\[1\])\]
\>>> deciles \= {0: np.linspace(0, 1, num\=5)}
\>>> pd\_results \= partial\_dependence(
...     clf, X, features\=0, kind\="average", grid\_resolution\=5)
\>>> display \= PartialDependenceDisplay(
...     \[pd\_results\], features\=features, feature\_names\=feature\_names,
...     target\_idx\=0, deciles\=deciles
... )
\>>> display.plot(pdp\_lim\={1: (\-1.38, 0.66)})
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-inspection-PartialDependenceDisplay-1.png](https://scikit-learn.org/stable/_images/sklearn-inspection-PartialDependenceDisplay-1.png)

classmethod from\_estimator(_estimator_, _X_, _features_, _\*_, _sample\_weight\=None_, _categorical\_features\=None_, _feature\_names\=None_, _target\=None_, _response\_method\='auto'_, _n\_cols\=3_, _grid\_resolution\=100_, _percentiles\=(0.05, 0.95)_, _custom\_values\=None_, _method\='auto'_, _n\_jobs\=None_, _verbose\=0_, _line\_kw\=None_, _ice\_lines\_kw\=None_, _pd\_line\_kw\=None_, _contour\_kw\=None_, _ax\=None_, _kind\='average'_, _centered\=False_, _subsample\=1000_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/inspection/_plot/partial_dependence.py#L244)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "Link to this definition")

Partial dependence (PD) and individual conditional expectation (ICE) plots.

Partial dependence plots, individual conditional expectation plots, or an overlay of both can be plotted by setting the `kind` parameter. This method generates one plot for each entry in `features`. The plots are arranged in a grid with `n_cols` columns. For one-way partial dependence plots, the deciles of the feature values are shown on the x-axis. For two-way plots, the deciles are shown on both axes and PDPs are contour plots.

For general information regarding `scikit-learn` visualization tools, see the [Visualization Guide](https://scikit-learn.org/stable/visualizations.html#visualizations)
. For guidance on interpreting these plots, refer to the [Inspection Guide](https://scikit-learn.org/stable/modules/partial_dependence.html#partial-dependence)
.

For an example on how to use this class method, see [Partial Dependence and Individual Conditional Expectation Plots](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#sphx-glr-auto-examples-inspection-plot-partial-dependence-py)
.

Note

[`PartialDependenceDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
 does not support using the same axes with multiple calls. To plot the partial dependence for multiple estimators, please pass the axes created by the first call to the second call:

\>>> from sklearn.inspection import PartialDependenceDisplay
\>>> from sklearn.datasets import make\_friedman1
\>>> from sklearn.linear\_model import LinearRegression
\>>> from sklearn.ensemble import RandomForestRegressor
\>>> X, y \= make\_friedman1()
\>>> est1 \= LinearRegression().fit(X, y)
\>>> est2 \= RandomForestRegressor().fit(X, y)
\>>> disp1 \= PartialDependenceDisplay.from\_estimator(est1, X,
...                                                 \[1, 2\])
\>>> disp2 \= PartialDependenceDisplay.from\_estimator(est2, X, \[1, 2\],
...                                                 ax\=disp1.axes\_)

Copy to clipboard

Warning

For [`GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
 and [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
, the `'recursion'` method (used by default) will not account for the `init` predictor of the boosting process. In practice, this will produce the same values as `'brute'` up to a constant offset in the target response, provided that `init` is a constant estimator (which is the default). However, if `init` is not a constant estimator, the partial dependence values are incorrect for `'recursion'` because the offset will be sample-dependent. It is preferable to use the `'brute'` method. Note that this only applies to [`GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
 and [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
, not to [`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 and [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
.

Added in version 1.0.

Parameters:

**estimator**BaseEstimator

A fitted estimator object implementing [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
, [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
, or [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
. Multioutput-multiclass classifiers are not supported.

**X**{array-like, dataframe} of shape (n\_samples, n\_features)

`X` is used to generate a grid of values for the target `features` (where the partial dependence will be evaluated), and also to generate values for the complement features when the `method` is `'brute'`.

**features**list of {int, str, pair of int, pair of str}

The target features for which to create the PDPs. If `features[i]` is an integer or a string, a one-way PDP is created; if `features[i]` is a tuple, a two-way PDP is created (only supported with `kind='average'`). Each tuple must be of size 2. If any entry is a string, then it must be in `feature_names`.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights are used to calculate weighted means when averaging the model output. If `None`, then samples are equally weighted. If `sample_weight` is not `None`, then `method` will be set to `'brute'`. Note that `sample_weight` is ignored for `kind='individual'`.

Added in version 1.3.

**categorical\_features**array-like of shape (n\_features,) or shape (n\_categorical\_features,), dtype={bool, int, str}, default=None

Indicates the categorical features.

*   `None`: no feature will be considered categorical;
    
*   boolean array-like: boolean mask of shape `(n_features,)` indicating which features are categorical. Thus, this array has the same shape has `X.shape[1]`;
    
*   integer or string array-like: integer indices or strings indicating categorical features.
    

Added in version 1.2.

**feature\_names**array-like of shape (n\_features,), dtype=str, default=None

Name of each feature; `feature_names[i]` holds the name of the feature with index `i`. By default, the name of the feature corresponds to their numerical index for NumPy array and their column name for pandas dataframe.

**target**int, default=None

*   In a multiclass setting, specifies the class for which the PDPs should be computed. Note that for binary classification, the positive class (index 1) is always used.
    
*   In a multioutput setting, specifies the task for which the PDPs should be computed.
    

Ignored in binary classification or classical regression settings.

**response\_method**{‘auto’, ‘predict\_proba’, ‘decision\_function’}, default=’auto’

Specifies whether to use [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 or [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 as the target response. For regressors this parameter is ignored and the response is always the output of [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
. By default, [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 is tried first and we revert to [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 if it doesn’t exist. If `method` is `'recursion'`, the response is always the output of [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
.

**n\_cols**int, default=3

The maximum number of columns in the grid plot. Only active when `ax` is a single axis or `None`.

**grid\_resolution**int, default=100

The number of equally spaced points on the axes of the plots, for each target feature. This parameter is overridden by `custom_values` if that parameter is set.

**percentiles**tuple of float, default=(0.05, 0.95)

The lower and upper percentile used to create the extreme values for the PDP axes. Must be in \[0, 1\]. This parameter is overridden by `custom_values` if that parameter is set.

**custom\_values**dict

A dictionary mapping the index of an element of `features` to an array of values where the partial dependence should be calculated for that feature. Setting a range of values for a feature overrides `grid_resolution` and `percentiles`.

Added in version 1.7.

**method**str, default=’auto’

The method used to calculate the averaged predictions:

*   `'recursion'` is only supported for some tree-based estimators (namely [`GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
    , [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
    , [`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
    , [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
    , [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    , [`RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
     but is more efficient in terms of speed. With this method, the target response of a classifier is always the decision function, not the predicted probabilities. Since the `'recursion'` method implicitly computes the average of the ICEs by design, it is not compatible with ICE and thus `kind` must be `'average'`.
    
*   `'brute'` is supported for any estimator, but is more computationally intensive.
    
*   `'auto'`: the `'recursion'` is used for estimators that support it, and `'brute'` is used otherwise. If `sample_weight` is not `None`, then `'brute'` is used regardless of the estimator.
    

Please see [this note](https://scikit-learn.org/stable/modules/partial_dependence.html#pdp-method-differences)
 for differences between the `'brute'` and `'recursion'` method.

**n\_jobs**int, default=None

The number of CPUs to use to compute the partial dependences. Computation is parallelized over features specified by the `features` parameter.

`None` means 1 unless in a [`joblib.parallel_backend`](https://joblib.readthedocs.io/en/latest/generated/joblib.parallel_backend.html#joblib.parallel_backend "(in joblib v1.7)")
 context. `-1` means using all processors. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
 for more details.

**verbose**int, default=0

Verbose output during PD computations.

**line\_kw**dict, default=None

Dict with keywords passed to the `matplotlib.pyplot.plot` call. For one-way partial dependence plots. It can be used to define common properties for both `ice_lines_kw` and `pdp_line_kw`.

**ice\_lines\_kw**dict, default=None

Dictionary with keywords passed to the `matplotlib.pyplot.plot` call. For ICE lines in the one-way partial dependence plots. The key value pairs defined in `ice_lines_kw` takes priority over `line_kw`.

**pd\_line\_kw**dict, default=None

Dictionary with keywords passed to the `matplotlib.pyplot.plot` call. For partial dependence in one-way partial dependence plots. The key value pairs defined in `pd_line_kw` takes priority over `line_kw`.

**contour\_kw**dict, default=None

Dict with keywords passed to the `matplotlib.pyplot.contourf` call. For two-way partial dependence plots.

**ax**Matplotlib axes or array-like of Matplotlib axes, default=None

*   If a single axis is passed in, it is treated as a bounding axes and a grid of partial dependence plots will be drawn within these bounds. The `n_cols` parameter controls the number of columns in the grid.
    
*   If an array-like of axes are passed in, the partial dependence plots will be drawn directly into these axes.
    
*   If `None`, a figure and a bounding axes is created and treated as the single axes case.
    

**kind**{‘average’, ‘individual’, ‘both’}, default=’average’

Whether to plot the partial dependence averaged across all the samples in the dataset or one line per sample or both.

*   `kind='average'` results in the traditional PD plot;
    
*   `kind='individual'` results in the ICE plot.
    

Note that the fast `method='recursion'` option is only available for `kind='average'` and `sample_weights=None`. Computing individual dependencies and doing weighted averages requires using the slower `method='brute'`.

**centered**bool, default=False

If `True`, the ICE and PD lines will start at the origin of the y-axis. By default, no centering is done.

Added in version 1.1.

**subsample**float, int or None, default=1000

Sampling for ICE curves when `kind` is ‘individual’ or ‘both’. If `float`, should be between 0.0 and 1.0 and represent the proportion of the dataset to be used to plot ICE curves. If `int`, represents the absolute number samples to use.

Note that the full dataset is still used to calculate averaged partial dependence when `kind='both'`.

**random\_state**int, RandomState instance or None, default=None

Controls the randomness of the selected samples when subsamples is not `None` and `kind` is either `'both'` or `'individual'`. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
 for details.

Returns:

**display**[`PartialDependenceDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "sklearn.inspection.PartialDependenceDisplay")

See also

[`partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")

Compute Partial Dependence values.

Examples

\>>> import matplotlib.pyplot as plt
\>>> from sklearn.datasets import make\_friedman1
\>>> from sklearn.ensemble import GradientBoostingRegressor
\>>> from sklearn.inspection import PartialDependenceDisplay
\>>> X, y \= make\_friedman1()
\>>> clf \= GradientBoostingRegressor(n\_estimators\=10).fit(X, y)
\>>> PartialDependenceDisplay.from\_estimator(clf, X, \[0, (0, 1)\])
<...>
\>>> plt.show()

Copy to clipboard

![../../_images/sklearn-inspection-PartialDependenceDisplay-2.png](https://scikit-learn.org/stable/_images/sklearn-inspection-PartialDependenceDisplay-2.png)

plot(_\*_, _ax\=None_, _n\_cols\=3_, _line\_kw\=None_, _ice\_lines\_kw\=None_, _pd\_line\_kw\=None_, _contour\_kw\=None_, _bar\_kw\=None_, _heatmap\_kw\=None_, _pdp\_lim\=None_, _centered\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/inspection/_plot/partial_dependence.py#L1133)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.plot "Link to this definition")

Plot partial dependence plots.

Parameters:

**ax**Matplotlib axes or array-like of Matplotlib axes, default=None

*   If a single axis is passed in, it is treated as a bounding axes
    
    and a grid of partial dependence plots will be drawn within these bounds. The `n_cols` parameter controls the number of columns in the grid.
    
*   If an array-like of axes are passed in, the partial dependence
    
    plots will be drawn directly into these axes.
    
*   If `None`, a figure and a bounding axes is created and treated
    
    as the single axes case.
    

**n\_cols**int, default=3

The maximum number of columns in the grid plot. Only active when `ax` is a single axes or `None`.

**line\_kw**dict, default=None

Dict with keywords passed to the `matplotlib.pyplot.plot` call. For one-way partial dependence plots.

**ice\_lines\_kw**dict, default=None

Dictionary with keywords passed to the `matplotlib.pyplot.plot` call. For ICE lines in the one-way partial dependence plots. The key value pairs defined in `ice_lines_kw` takes priority over `line_kw`.

Added in version 1.0.

**pd\_line\_kw**dict, default=None

Dictionary with keywords passed to the `matplotlib.pyplot.plot` call. For partial dependence in one-way partial dependence plots. The key value pairs defined in `pd_line_kw` takes priority over `line_kw`.

Added in version 1.0.

**contour\_kw**dict, default=None

Dict with keywords passed to the `matplotlib.pyplot.contourf` call for two-way partial dependence plots.

**bar\_kw**dict, default=None

Dict with keywords passed to the `matplotlib.pyplot.bar` call for one-way categorical partial dependence plots.

Added in version 1.2.

**heatmap\_kw**dict, default=None

Dict with keywords passed to the `matplotlib.pyplot.imshow` call for two-way categorical partial dependence plots.

Added in version 1.2.

**pdp\_lim**dict, default=None

Global min and max average predictions, such that all plots will have the same scale and y limits. `pdp_lim[1]` is the global min and max for single partial dependence curves. `pdp_lim[2]` is the global min and max for two-way partial dependence curves. If `None` (default), the limit will be inferred from the global minimum and maximum of all predictions.

Added in version 1.1.

**centered**bool, default=False

If `True`, the ICE and PD lines will start at the origin of the y-axis. By default, no centering is done.

Added in version 1.1.

Returns:

**display**[`PartialDependenceDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "sklearn.inspection.PartialDependenceDisplay")

Returns a [`PartialDependenceDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "sklearn.inspection.PartialDependenceDisplay")
 object that contains the partial dependence plots.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_thumb.png)

[Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html)

Features in Histogram Gradient Boosting Trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_monotonic_constraints_thumb.png)

[Monotonic Constraints](https://scikit-learn.org/stable/auto_examples/ensemble/plot_monotonic_constraints.html)

Monotonic Constraints

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_thumb.png)

[Partial Dependence and Individual Conditional Expectation Plots](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html)

Partial Dependence and Individual Conditional Expectation Plots

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_visualization_api_thumb.png)

[Advanced Plotting With Partial Dependence](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html)

Advanced Plotting With Partial Dependence

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)

[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)

Release Highlights for scikit-learn 0.23

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)

[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)

Release Highlights for scikit-learn 1.2

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)