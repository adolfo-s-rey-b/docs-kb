[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.mean_absolute_error.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.mean_absolute_error.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.mean_absolute_error.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.mean_absolute_error.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.mean_absolute_error.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.mean_absolute_error.html)

Collapse Sidebar Expand Sidebar

mean\_absolute\_error[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#mean-absolute-error "Link to this heading")

================================================================================================================================================================

sklearn.metrics.mean\_absolute\_error(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_, _multioutput\='uniform\_average'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_regression.py#L216)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "Link to this definition")

Mean absolute error regression loss.

The mean absolute error is a non-negative floating point value, where best value is 0.0. Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#mean-absolute-error)
.

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

**loss**float or array of floats

If multioutput is ‘raw\_values’, then mean absolute error is returned for each output separately. If multioutput is ‘uniform\_average’ or an ndarray of weights, then the weighted average of all output errors is returned.

MAE output is non-negative floating point. The best value is 0.0.

Examples

\>>> from sklearn.metrics import mean\_absolute\_error
\>>> y\_true \= \[3, \-0.5, 2, 7\]
\>>> y\_pred \= \[2.5, 0.0, 2, 8\]
\>>> mean\_absolute\_error(y\_true, y\_pred)
0.5
\>>> y\_true \= \[\[0.5, 1\], \[\-1, 1\], \[7, \-6\]\]
\>>> y\_pred \= \[\[0, 2\], \[\-1, 2\], \[8, \-5\]\]
\>>> mean\_absolute\_error(y\_true, y\_pred)
0.75
\>>> mean\_absolute\_error(y\_true, y\_pred, multioutput\='raw\_values')
array(\[0.5, 1. \])
\>>> mean\_absolute\_error(y\_true, y\_pred, multioutput\=\[0.3, 0.7\])
0.85...

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)

[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)

Lagged features for time series forecasting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_thumb.png)

[Poisson regression and non-normal loss](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)

Poisson regression and non-normal loss

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_quantile_regression_thumb.png)

[Quantile regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_quantile_regression.html)

Quantile regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tweedie_regression_insurance_claims_thumb.png)

[Tweedie regression on insurance claims](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)

Tweedie regression on insurance claims

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)