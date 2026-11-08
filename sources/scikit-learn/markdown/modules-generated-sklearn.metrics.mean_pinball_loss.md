[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.mean_pinball_loss.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.mean_pinball_loss.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.mean_pinball_loss.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.mean_pinball_loss.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.mean_pinball_loss.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.mean_pinball_loss.html)

Collapse Sidebar Expand Sidebar

mean\_pinball\_loss[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#mean-pinball-loss "Link to this heading")

==========================================================================================================================================================

sklearn.metrics.mean\_pinball\_loss(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_, _alpha\=0.5_, _multioutput\='uniform\_average'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_regression.py#L310)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "Link to this definition")

Pinball loss for quantile regression.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#pinball-loss)
.

Parameters:

**y\_true**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Ground truth (correct) target values.

**y\_pred**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Estimated target values.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**alpha**float, slope of the pinball loss, default=0.5,

This loss is equivalent to [Mean absolute error](https://scikit-learn.org/stable/modules/model_evaluation.html#mean-absolute-error)
 when `alpha=0.5`, `alpha=0.95` is minimized by estimators of the 95th percentile.

**multioutput**{‘raw\_values’, ‘uniform\_average’} or array-like of shape (n\_outputs,), default=’uniform\_average’

Defines aggregating of multiple output values. Array-like value defines weights used to average errors.

‘raw\_values’ :

Returns a full set of errors in case of multioutput input.

‘uniform\_average’ :

Errors of all outputs are averaged with uniform weight.

Returns:

**loss**float or ndarray of floats

If multioutput is ‘raw\_values’, then mean absolute error is returned for each output separately. If multioutput is ‘uniform\_average’ or an ndarray of weights, then the weighted average of all output errors is returned.

The pinball loss output is a non-negative floating point. The best value is 0.0.

Examples

\>>> from sklearn.metrics import mean\_pinball\_loss
\>>> y\_true \= \[1, 2, 3\]
\>>> mean\_pinball\_loss(y\_true, \[0, 2, 3\], alpha\=0.1)
0.03...
\>>> mean\_pinball\_loss(y\_true, \[1, 2, 4\], alpha\=0.1)
0.3...
\>>> mean\_pinball\_loss(y\_true, \[0, 2, 3\], alpha\=0.9)
0.3...
\>>> mean\_pinball\_loss(y\_true, \[1, 2, 4\], alpha\=0.9)
0.03...
\>>> mean\_pinball\_loss(y\_true, y\_true, alpha\=0.1)
0.0
\>>> mean\_pinball\_loss(y\_true, y\_true, alpha\=0.9)
0.0

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)

[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)

Lagged features for time series forecasting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_quantile_thumb.png)

[Prediction Intervals for Gradient Boosting Regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html)

Prediction Intervals for Gradient Boosting Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_thumb.png)

[Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html)

Features in Histogram Gradient Boosting Trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_0_0_thumb.png)

[Release Highlights for scikit-learn 1.0](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html)

Release Highlights for scikit-learn 1.0

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)