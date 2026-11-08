[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.max_error.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.max_error.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.max_error.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.max_error.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.max_error.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.max_error.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.max_error.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.max_error.html)

Collapse Sidebar Expand Sidebar

max\_error[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.max_error.html#max-error "Link to this heading")

=================================================================================================================================

sklearn.metrics.max\_error(_y\_true_, _y\_pred_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_regression.py#L1321)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.max_error.html#sklearn.metrics.max_error "Link to this definition")

The max\_error metric calculates the maximum residual error.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#max-error)
.

Parameters:

**y\_true**array-like of shape (n\_samples,)

Ground truth (correct) target values.

**y\_pred**array-like of shape (n\_samples,)

Estimated target values.

Returns:

**max\_error**float

A positive floating point value (the best value is 0.0).

Examples

\>>> from sklearn.metrics import max\_error
\>>> y\_true \= \[3, 2, 7, 1\]
\>>> y\_pred \= \[4, 2, 7, 1\]
\>>> max\_error(y\_true, y\_pred)
1.0

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)