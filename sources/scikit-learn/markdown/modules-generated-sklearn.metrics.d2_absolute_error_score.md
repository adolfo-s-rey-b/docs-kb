[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_absolute_error_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.d2_absolute_error_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_absolute_error_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.d2_absolute_error_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.d2_absolute_error_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.d2_absolute_error_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.d2_absolute_error_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.d2_absolute_error_score.html)

Collapse Sidebar Expand Sidebar

d2\_absolute\_error\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_absolute_error_score.html#d2-absolute-error-score "Link to this heading")

=============================================================================================================================================================================

sklearn.metrics.d2\_absolute\_error\_score(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_, _multioutput\='uniform\_average'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_regression.py#L1870)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_absolute_error_score.html#sklearn.metrics.d2_absolute_error_score "Link to this definition")

D2 regression score function, fraction of absolute error explained.

Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A model that always uses the empirical median of `y_true` as constant prediction, disregarding the input features, gets a D2 score of 0.0.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#d2-score)
.

Added in version 1.1.

Parameters:

**y\_true**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Ground truth (correct) target values.

**y\_pred**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Estimated target values.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**multioutput**{‘raw\_values’, ‘uniform\_average’} or array-like of shape (n\_outputs,), default=’uniform\_average’

Defines aggregating of multiple output values. Array-like value defines weights used to average scores.

‘raw\_values’ :

Returns a full set of errors in case of multioutput input.

‘uniform\_average’ :

Scores of all outputs are averaged with uniform weight.

Returns:

**score**float or ndarray of floats

The D2 score with an absolute error deviance or ndarray of scores if ‘multioutput’ is ‘raw\_values’.

Notes

Like R2, D2 score may be negative (it need not actually be the square of a quantity D).

This metric is not well-defined for single samples and will return a NaN value if n\_samples is less than two.

References

\[1\]

Eq. (3.11) of Hastie, Trevor J., Robert Tibshirani and Martin J. Wainwright. “Statistical Learning with Sparsity: The Lasso and Generalizations.” (2015). [https://hastie.su.domains/StatLearnSparsity/](https://hastie.su.domains/StatLearnSparsity/)

Examples

\>>> from sklearn.metrics import d2\_absolute\_error\_score
\>>> y\_true \= \[3, \-0.5, 2, 7\]
\>>> y\_pred \= \[2.5, 0.0, 2, 8\]
\>>> d2\_absolute\_error\_score(y\_true, y\_pred)
0.764...
\>>> y\_true \= \[\[0.5, 1\], \[\-1, 1\], \[7, \-6\]\]
\>>> y\_pred \= \[\[0, 2\], \[\-1, 2\], \[8, \-5\]\]
\>>> d2\_absolute\_error\_score(y\_true, y\_pred, multioutput\='uniform\_average')
0.691...
\>>> d2\_absolute\_error\_score(y\_true, y\_pred, multioutput\='raw\_values')
array(\[0.8125    , 0.57142857\])
\>>> y\_true \= \[1, 2, 3\]
\>>> y\_pred \= \[1, 2, 3\]
\>>> d2\_absolute\_error\_score(y\_true, y\_pred)
1.0
\>>> y\_true \= \[1, 2, 3\]
\>>> y\_pred \= \[2, 2, 2\]
\>>> d2\_absolute\_error\_score(y\_true, y\_pred)
0.0
\>>> y\_true \= \[1, 2, 3\]
\>>> y\_pred \= \[3, 2, 1\]
\>>> d2\_absolute\_error\_score(y\_true, y\_pred)
\-1.0

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)