[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.RANSACRegressor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.RANSACRegressor.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.RANSACRegressor.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.RANSACRegressor.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.RANSACRegressor.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.RANSACRegressor.html)

Collapse Sidebar Expand Sidebar

RANSACRegressor[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#ransacregressor "Link to this heading")

=======================================================================================================================================================

class sklearn.linear\_model.RANSACRegressor(_estimator\=None_, _\*_, _min\_samples\=None_, _residual\_threshold\=None_, _is\_data\_valid\=None_, _is\_model\_valid\=None_, _max\_trials\=100_, _max\_skips\=inf_, _stop\_n\_inliers\=inf_, _stop\_score\=inf_, _stop\_probability\=0.99_, _loss\='absolute\_error'_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_ransac.py#L81)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "Link to this definition")

RANSAC (RANdom SAmple Consensus) algorithm.

RANSAC is an iterative algorithm for the robust estimation of parameters from a subset of inliers from the complete data set.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#ransac-regression)
.

Parameters:

**estimator**object, default=None

Base estimator object which implements the following methods:

*   `fit(X, y)`: Fit model to given training data and target values.
    
*   `score(X, y)`: Returns the mean accuracy on the given test data, which is used for the stop criterion defined by `stop_score`. Additionally, the score is used to decide which of two equally large consensus sets is chosen as the better one.
    
*   `predict(X)`: Returns predicted values using the linear model, which is used to compute residual error using loss function.
    

If `estimator` is None, then [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
 is used for target values of dtype float.

Note that the current implementation only supports regression estimators.

**min\_samples**int (>= 1) or float (\[0, 1\]), default=None

Minimum number of samples chosen randomly from original data. Treated as an absolute number of samples for `min_samples >= 1`, treated as a relative number `ceil(min_samples * X.shape[0])` for `min_samples < 1`. This is typically chosen as the minimal number of samples necessary to estimate the given `estimator`. By default a [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
 estimator is assumed and `min_samples` is chosen as `X.shape[1] + 1`. This parameter is highly dependent upon the model, so if a `estimator` other than [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
 is used, the user must provide a value.

**residual\_threshold**float, default=None

Maximum residual for a data sample to be classified as an inlier. By default the threshold is chosen as the MAD (median absolute deviation) of the target values `y`. Points whose residuals are strictly equal to the threshold are considered as inliers.

**is\_data\_valid**callable, default=None

This function is called with the randomly selected data before the model is fitted to it: `is_data_valid(X, y)`. If its return value is False the current randomly chosen sub-sample is skipped.

**is\_model\_valid**callable, default=None

This function is called with the estimated model and the randomly selected data: `is_model_valid(model, X, y)`. If its return value is False the current randomly chosen sub-sample is skipped. Rejecting samples with this function is computationally costlier than with `is_data_valid`. `is_model_valid` should therefore only be used if the estimated model is needed for making the rejection decision.

**max\_trials**int, default=100

Maximum number of iterations for random sample selection.

**max\_skips**int, default=np.inf

Maximum number of iterations that can be skipped due to finding zero inliers or invalid data defined by `is_data_valid` or invalid models defined by `is_model_valid`.

Added in version 0.19.

**stop\_n\_inliers**int, default=np.inf

Stop iteration if at least this number of inliers are found.

**stop\_score**float, default=np.inf

Stop iteration if score is greater equal than this threshold.

**stop\_probability**float in range \[0, 1\], default=0.99

RANSAC iteration stops if at least one outlier-free set of the training data is sampled in RANSAC. This requires to generate at least N samples (iterations):

N \>= log(1 \- probability) / log(1 \- e\*\*m)

Copy to clipboard

where the probability (confidence) is typically set to high value such as 0.99 (the default) and e is the current fraction of inliers w.r.t. the total number of samples.

**loss**str, callable, default=’absolute\_error’

String inputs, ‘absolute\_error’ and ‘squared\_error’ are supported which find the absolute error and squared error per sample respectively.

If `loss` is a callable, then it should be a function that takes two arrays as inputs, the true and predicted value and returns a 1-D array with the i-th value of the array corresponding to the loss on `X[i]`.

If the loss on a sample is greater than the `residual_threshold`, then this sample is classified as an outlier.

Added in version 0.18.

**random\_state**int, RandomState instance, default=None

The generator used to initialize the centers. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Attributes:

**estimator\_**object

Final model fitted on the inliers predicted by the “best” model found during RANSAC sampling (copy of the `estimator` object).

**n\_trials\_**int

Number of random selection trials until one of the stop criteria is met. It is always `<= max_trials`.

**inlier\_mask\_**bool array of shape \[n\_samples\]

Boolean mask of inliers classified as `True`.

**n\_skips\_no\_inliers\_**int

Number of iterations skipped due to finding zero inliers.

Added in version 0.19.

**n\_skips\_invalid\_data\_**int

Number of iterations skipped due to invalid data defined by `is_data_valid`.

Added in version 0.19.

**n\_skips\_invalid\_model\_**int

Number of iterations skipped due to an invalid model defined by `is_model_valid`.

Added in version 0.19.

**n\_features\_in\_**int

Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
.

Added in version 0.24.

**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)

Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
. Defined only when `X` has feature names that are all strings.

Added in version 1.0.

See also

[`HuberRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor")

Linear regression model that is robust to outliers.

[`TheilSenRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "sklearn.linear_model.TheilSenRegressor")

Theil-Sen Estimator robust multivariate regression model.

[`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")

Fitted by minimizing a regularized empirical loss with SGD.

References

\[1\]

[https://en.wikipedia.org/wiki/RANSAC](https://en.wikipedia.org/wiki/RANSAC)

\[2\]

[https://www.sri.com/wp-content/uploads/2021/12/ransac-publication.pdf](https://www.sri.com/wp-content/uploads/2021/12/ransac-publication.pdf)

\[3\]

[https://bmva-archive.org.uk/bmvc/2009/Papers/Paper355/Paper355.pdf](https://bmva-archive.org.uk/bmvc/2009/Papers/Paper355/Paper355.pdf)

Examples

\>>> from sklearn.linear\_model import RANSACRegressor
\>>> from sklearn.datasets import make\_regression
\>>> X, y \= make\_regression(
...     n\_samples\=200, n\_features\=2, noise\=4.0, random\_state\=0)
\>>> reg \= RANSACRegressor(random\_state\=0).fit(X, y)
\>>> reg.score(X, y)
0.9885
\>>> reg.predict(X\[:1,\])
array(\[-31.9417\])

Copy to clipboard

For a more detailed example, see [Robust linear model estimation using RANSAC](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html#sphx-glr-auto-examples-linear-model-plot-ransac-py)

fit(_X_, _y_, _sample\_weight\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_ransac.py#L317)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor.fit "Link to this definition")

Fit estimator using RANSAC algorithm.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Training data.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_targets)

Target values.

**sample\_weight**array-like of shape (n\_samples,), default=None

Individual weights for each sample raises error if sample\_weight is passed and estimator fit method does not support it.

Added in version 0.18.

**\*\*fit\_params**dict

Parameters routed to the `fit` method of the sub-estimator via the metadata routing API.

Added in version 1.5: Only available if `sklearn.set_config(enable_metadata_routing=True)` is set. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**self**object

Fitted `RANSACRegressor` estimator.

Raises:

ValueError

If no valid consensus set could be found. This occurs if `is_data_valid` and `is_model_valid` return False for all `max_trials` randomly chosen sub-samples.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_ransac.py#L697)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Added in version 1.5.

Returns:

**routing**MetadataRouter

A [`MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

predict(_X_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_ransac.py#L605)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor.predict "Link to this definition")

Predict using the estimated model.

This is a wrapper for `estimator_.predict(X)`.

Parameters:

**X**{array-like or sparse matrix} of shape (n\_samples, n\_features)

Input data.

**\*\*params**dict

Parameters routed to the `predict` method of the sub-estimator via the metadata routing API.

Added in version 1.5: Only available if `sklearn.set_config(enable_metadata_routing=True)` is set. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**y**array, shape = \[n\_samples\] or \[n\_samples, n\_targets\]

Returns predicted values.

score(_X_, _y_, _\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_ransac.py#L651)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor.score "Link to this definition")

Return the score of the prediction.

This is a wrapper for `estimator_.score(X, y)`.

Parameters:

**X**{array-like or sparse matrix} of shape (n\_samples, n\_features)

Training data.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_targets)

Target values.

**\*\*params**dict

Parameters routed to the `score` method of the sub-estimator via the metadata routing API.

Added in version 1.5: Only available if `sklearn.set_config(enable_metadata_routing=True)` is set. See [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

Returns:

**z**float

Score of the prediction.

set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 \= '$UNCHANGED$'_) → [RANSACRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model._ransac.RANSACRegressor")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor.set_fit_request "Link to this definition")

Configure whether metadata should be requested to be passed to the `fit` method.

Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

The options for each parameter are:

*   `True`: metadata is requested, and passed to `fit` if provided. The request is ignored if metadata is not provided.
    
*   `False`: metadata is not requested and the meta-estimator will not pass it to `fit`.
    
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.
    
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.
    

The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.

Added in version 1.3.

Parameters:

**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED

Metadata routing for `sample_weight` parameter in `fit`.

Returns:

**self**object

The updated object.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ransac_thumb.png)

[Robust linear model estimation using RANSAC](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html)

Robust linear model estimation using RANSAC

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_fit_thumb.png)

[Robust linear estimator fitting](https://scikit-learn.org/stable/auto_examples/linear_model/plot_robust_fit.html)

Robust linear estimator fitting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_theilsen_thumb.png)

[Theil-Sen Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html)

Theil-Sen Regression

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)