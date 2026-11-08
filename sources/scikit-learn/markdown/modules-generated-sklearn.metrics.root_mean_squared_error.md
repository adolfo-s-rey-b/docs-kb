[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.root_mean_squared_error.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.root_mean_squared_error.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.root_mean_squared_error.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.root_mean_squared_error.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.root_mean_squared_error.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.root_mean_squared_error.html)

Collapse Sidebar Expand Sidebar

root\_mean\_squared\_error[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#root-mean-squared-error "Link to this heading")

=============================================================================================================================================================================

sklearn.metrics.root\_mean\_squared\_error(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_, _multioutput\='uniform\_average'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_regression.py#L607)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#sklearn.metrics.root_mean_squared_error "Link to this definition")

Root mean squared error regression loss.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#mean-squared-error)
.

Added in version 1.4.

Parameters:

**y\_true**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Ground truth (correct) target values.

**y\_pred**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Estimated target values.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**multioutput**{‘raw\_values’, ‘uniform\_average’} or array-like of shape (n\_outputs,), default=’uniform\_average’

Defines aggregating of multiple output values. Array-like value defines weights used to average errors.

‘raw\_values’ :

Returns a full set of errors in case of multioutput input.

‘uniform\_average’ :

Errors of all outputs are averaged with uniform weight.

Returns:

**loss**float or ndarray of floats

A non-negative floating point value (the best value is 0.0), or an array of floating point values, one for each individual target.

Examples

\>>> from sklearn.metrics import root\_mean\_squared\_error
\>>> y\_true \= \[3, \-0.5, 2, 7\]
\>>> y\_pred \= \[2.5, 0.0, 2, 8\]
\>>> root\_mean\_squared\_error(y\_true, y\_pred)
0.612...
\>>> y\_true \= \[\[0.5, 1\],\[\-1, 1\],\[7, \-6\]\]
\>>> y\_pred \= \[\[0, 2\],\[\-1, 2\],\[8, \-5\]\]
\>>> root\_mean\_squared\_error(y\_true, y\_pred)
0.822...

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)

[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)

Lagged features for time series forecasting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_thumb.png)

[Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html)

Features in Histogram Gradient Boosting Trees

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)