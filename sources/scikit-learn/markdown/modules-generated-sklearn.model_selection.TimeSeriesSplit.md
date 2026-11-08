[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)

Collapse Sidebar Expand Sidebar

TimeSeriesSplit[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#timeseriessplit "Link to this heading")

==========================================================================================================================================================

class sklearn.model\_selection.TimeSeriesSplit(_n\_splits\=5_, _\*_, _max\_train\_size\=None_, _test\_size\=None_, _gap\=0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1116)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "Link to this definition")

Time Series cross-validator.

Provides train/test indices to split time-ordered data, where other cross-validation methods are inappropriate, as they would lead to training on future data and evaluating on past data. To ensure comparable metrics across folds, samples must be equally spaced. Once this condition is met, each test set covers the same time duration, while the train set size accumulates data from previous splits.

This cross-validation object is a variation of [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
. In the k-th split, it returns the first k folds as the train set and the (k+1)-th fold as the test set.

Note that, unlike standard cross-validation methods, successive training sets are supersets of those that come before them.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#time-series-split)
.

For visualisation of cross-validation behaviour and comparison between common scikit-learn split methods refer to [Visualizing cross-validation behavior in scikit-learn](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#sphx-glr-auto-examples-model-selection-plot-cv-indices-py)

Added in version 0.18.

Parameters:

**n\_splits**int, default=5

Number of splits. Must be at least 2.

Changed in version 0.22: `n_splits` default value changed from 3 to 5.

**max\_train\_size**int, default=None

Maximum size for a single training set.

**test\_size**int, default=None

Used to limit the size of the test set. Defaults to `n_samples // (n_splits + 1)`, which is the maximum allowed value with `gap=0`.

Added in version 0.24.

**gap**int, default=0

Number of samples to exclude from the end of each train set before the test set.

Added in version 0.24.

Notes

The training set has size `i * n_samples // (n_splits + 1) + n_samples % (n_splits + 1)` in the `i` th split, with a test set of size `n_samples//(n_splits + 1)` by default, where `n_samples` is the number of samples. Note that this formula is only valid when `test_size` and `max_train_size` are left to their default values.

Examples

\>>> import numpy as np
\>>> from sklearn.model\_selection import TimeSeriesSplit
\>>> X \= np.array(\[\[1, 2\], \[3, 4\], \[1, 2\], \[3, 4\], \[1, 2\], \[3, 4\]\])
\>>> y \= np.array(\[1, 2, 3, 4, 5, 6\])
\>>> tscv \= TimeSeriesSplit()
\>>> print(tscv)
TimeSeriesSplit(gap=0, max\_train\_size=None, n\_splits=5, test\_size=None)
\>>> for i, (train\_index, test\_index) in enumerate(tscv.split(X)):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}")
...     print(f"  Test:  index={test\_index}")
Fold 0:
  Train: index=\[0\]
  Test:  index=\[1\]
Fold 1:
  Train: index=\[0 1\]
  Test:  index=\[2\]
Fold 2:
  Train: index=\[0 1 2\]
  Test:  index=\[3\]
Fold 3:
  Train: index=\[0 1 2 3\]
  Test:  index=\[4\]
Fold 4:
  Train: index=\[0 1 2 3 4\]
  Test:  index=\[5\]
\>>> \# Fix test\_size to 2 with 12 samples
\>>> X \= np.random.randn(12, 2)
\>>> y \= np.random.randint(0, 2, 12)
\>>> tscv \= TimeSeriesSplit(n\_splits\=3, test\_size\=2)
\>>> for i, (train\_index, test\_index) in enumerate(tscv.split(X)):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}")
...     print(f"  Test:  index={test\_index}")
Fold 0:
  Train: index=\[0 1 2 3 4 5\]
  Test:  index=\[6 7\]
Fold 1:
  Train: index=\[0 1 2 3 4 5 6 7\]
  Test:  index=\[8 9\]
Fold 2:
  Train: index=\[0 1 2 3 4 5 6 7 8 9\]
  Test:  index=\[10 11\]
\>>> \# Add in a 2 period gap
\>>> tscv \= TimeSeriesSplit(n\_splits\=3, test\_size\=2, gap\=2)
\>>> for i, (train\_index, test\_index) in enumerate(tscv.split(X)):
...     print(f"Fold {i}:")
...     print(f"  Train: index={train\_index}")
...     print(f"  Test:  index={test\_index}")
Fold 0:
  Train: index=\[0 1 2 3\]
  Test:  index=\[6 7\]
Fold 1:
  Train: index=\[0 1 2 3 4 5\]
  Test:  index=\[8 9\]
Fold 2:
  Train: index=\[0 1 2 3 4 5 6 7\]
  Test:  index=\[10 11\]

Copy to clipboard

For a more extended example see [Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#sphx-glr-auto-examples-applications-plot-cyclical-feature-engineering-py)
.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_n\_splits(_X\=None_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L414)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit.get_n_splits "Link to this definition")

Returns the number of splitting iterations as set with the `n_splits` param when instantiating the cross-validator.

Parameters:

**X**array-like of shape (n\_samples, n\_features), default=None

Always ignored, exists for API compatibility.

**y**array-like of shape (n\_samples,), default=None

Always ignored, exists for API compatibility.

**groups**array-like of shape (n\_samples,), default=None

Always ignored, exists for API compatibility.

Returns:

**n\_splits**int

Returns the number of splitting iterations in the cross-validator.

split(_X_, _y\=None_, _groups\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_split.py#L1245)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit.split "Link to this definition")

Generate indices to split data into training and test set.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Training data, where `n_samples` is the number of samples and `n_features` is the number of features.

**y**array-like of shape (n\_samples,), default=None

Always ignored, exists for API compatibility.

**groups**array-like of shape (n\_samples,), default=None

Always ignored, exists for API compatibility.

Yields:

**train**ndarray

The training set indices for that split.

**test**ndarray

The testing set indices for that split.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)

[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)

Lagged features for time series forecasting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_thumb.png)

[Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html)

Features in Histogram Gradient Boosting Trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_thumb.png)

[L1-based models for Sparse Signals](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html)

L1-based models for Sparse Signals

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_thumb.png)

[Visualizing cross-validation behavior in scikit-learn](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html)

Visualizing cross-validation behavior in scikit-learn

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)