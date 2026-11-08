[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.median_absolute_error.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.median_absolute_error.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.median_absolute_error.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.median_absolute_error.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.median_absolute_error.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.median_absolute_error.html)

Collapse Sidebar Expand Sidebar

median\_absolute\_error[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#median-absolute-error "Link to this heading")

======================================================================================================================================================================

sklearn.metrics.median\_absolute\_error(_y\_true_, _y\_pred_, _\*_, _multioutput\='uniform\_average'_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_regression.py#L860)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "Link to this definition")

Median absolute error regression loss.

Median absolute error output is non-negative floating point. The best value is 0.0. Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#median-absolute-error)
.

Parameters:

**y\_true**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Ground truth (correct) target values.

**y\_pred**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Estimated target values.

**multioutput**{‘raw\_values’, ‘uniform\_average’} or array-like of shape (n\_outputs,), default=’uniform\_average’

Defines aggregating of multiple output values. Array-like value defines weights used to average errors.

‘raw\_values’ :

Returns a full set of errors in case of multioutput input.

‘uniform\_average’ :

Errors of all outputs are averaged with uniform weight.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Added in version 0.24.

Returns:

**loss**float or ndarray of floats

If multioutput is ‘raw\_values’, then mean absolute error is returned for each output separately. If multioutput is ‘uniform\_average’ or an ndarray of weights, then the weighted average of all output errors is returned.

Examples

\>>> from sklearn.metrics import median\_absolute\_error
\>>> y\_true \= \[3, \-0.5, 2, 7\]
\>>> y\_pred \= \[2.5, 0.0, 2, 8\]
\>>> median\_absolute\_error(y\_true, y\_pred)
0.5
\>>> y\_true \= \[\[0.5, 1\], \[\-1, 1\], \[7, \-6\]\]
\>>> y\_pred \= \[\[0, 2\], \[\-1, 2\], \[8, \-5\]\]
\>>> median\_absolute\_error(y\_true, y\_pred)
0.75
\>>> median\_absolute\_error(y\_true, y\_pred, multioutput\='raw\_values')
array(\[0.5, 1. \])
\>>> median\_absolute\_error(y\_true, y\_pred, multioutput\=\[0.3, 0.7\])
0.85

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_thumb.png)

[Effect of transforming the targets in regression model](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html)

Effect of transforming the targets in regression model

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_thumb.png)

[Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)

Common pitfalls in the interpretation of coefficients of linear models

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)