[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.mean_squared_log_error.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.mean_squared_log_error.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.mean_squared_log_error.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.mean_squared_log_error.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.mean_squared_log_error.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.mean_squared_log_error.html)

Collapse Sidebar Expand Sidebar

mean\_squared\_log\_error[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html#mean-squared-log-error "Link to this heading")

==========================================================================================================================================================================

sklearn.metrics.mean\_squared\_log\_error(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_, _multioutput\='uniform\_average'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_regression.py#L692)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html#sklearn.metrics.mean_squared_log_error "Link to this definition")

Mean squared logarithmic error regression loss.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#mean-squared-log-error)
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

Returns a full set of errors when the input is of multioutput format.

‘uniform\_average’ :

Errors of all outputs are averaged with uniform weight.

Returns:

**loss**float or ndarray of floats

A non-negative floating point value (the best value is 0.0), or an array of floating point values, one for each individual target.

Examples

\>>> from sklearn.metrics import mean\_squared\_log\_error
\>>> y\_true \= \[3, 5, 2.5, 7\]
\>>> y\_pred \= \[2.5, 5, 4, 8\]
\>>> mean\_squared\_log\_error(y\_true, y\_pred)
0.039...
\>>> y\_true \= \[\[0.5, 1\], \[1, 2\], \[7, 6\]\]
\>>> y\_pred \= \[\[0.5, 2\], \[1, 2.5\], \[8, 8\]\]
\>>> mean\_squared\_log\_error(y\_true, y\_pred)
0.044...
\>>> mean\_squared\_log\_error(y\_true, y\_pred, multioutput\='raw\_values')
array(\[0.00462428, 0.08377444\])
\>>> mean\_squared\_log\_error(y\_true, y\_pred, multioutput\=\[0.3, 0.7\])
0.060...

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)