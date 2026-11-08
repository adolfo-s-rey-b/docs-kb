[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.explained_variance_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.explained_variance_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.explained_variance_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.explained_variance_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.explained_variance_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.explained_variance_score.html)

Collapse Sidebar Expand Sidebar

explained\_variance\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#explained-variance-score "Link to this heading")

===============================================================================================================================================================================

sklearn.metrics.explained\_variance\_score(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_, _multioutput\='uniform\_average'_, _force\_finite\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_regression.py#L996)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score "Link to this definition")

Explained variance regression score function.

Best possible score is 1.0, lower values are worse.

In the particular case when `y_true` is constant, the explained variance score is not finite: it is either `NaN` (perfect predictions) or `-Inf` (imperfect predictions). To prevent such non-finite numbers to pollute higher-level experiments such as a grid search cross-validation, by default these cases are replaced with 1.0 (perfect predictions) or 0.0 (imperfect predictions) respectively. If `force_finite` is set to `False`, this score falls back on the original R2 definition.

Note

The Explained Variance score is similar to the [`R^2 score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
, but the former does not account for systematic offsets in the prediction (such as the intercept in linear models, i.e. different intercepts give the same Explained Variance score). Most often the [`R^2 score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
 should be preferred.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#explained-variance-score)
.

Parameters:

**y\_true**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Ground truth (correct) target values.

**y\_pred**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Estimated target values.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**multioutput**{‘raw\_values’, ‘uniform\_average’, ‘variance\_weighted’} or array-like of shape (n\_outputs,), default=’uniform\_average’

Defines aggregating of multiple output scores. Array-like value defines weights used to average scores.

‘raw\_values’ :

Returns a full set of scores in case of multioutput input.

‘uniform\_average’ :

Scores of all outputs are averaged with uniform weight.

‘variance\_weighted’ :

Scores of all outputs are averaged, weighted by the variances of each individual output.

**force\_finite**bool, default=True

Flag indicating if `NaN` and `-Inf` scores resulting from constant data should be replaced with real numbers (`1.0` if prediction is perfect, `0.0` otherwise). Default is `True`, a convenient setting for hyperparameters’ search procedures (e.g. grid search cross-validation).

Added in version 1.1.

Returns:

**score**float or ndarray of floats

The explained variance or ndarray if ‘multioutput’ is ‘raw\_values’.

See also

[`r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")

Similar metric, but accounting for systematic offsets in prediction.

Notes

This is not a symmetric function.

Examples

\>>> from sklearn.metrics import explained\_variance\_score
\>>> y\_true \= \[3, \-0.5, 2, 7\]
\>>> y\_pred \= \[2.5, 0.0, 2, 8\]
\>>> explained\_variance\_score(y\_true, y\_pred)
0.957...
\>>> y\_true \= \[\[0.5, 1\], \[\-1, 1\], \[7, \-6\]\]
\>>> y\_pred \= \[\[0, 2\], \[\-1, 2\], \[8, \-5\]\]
\>>> explained\_variance\_score(y\_true, y\_pred, multioutput\='uniform\_average')
0.983...
\>>> y\_true \= \[\-2, \-2, \-2\]
\>>> y\_pred \= \[\-2, \-2, \-2\]
\>>> explained\_variance\_score(y\_true, y\_pred)
1.0
\>>> explained\_variance\_score(y\_true, y\_pred, force\_finite\=False)
nan
\>>> y\_true \= \[\-2, \-2, \-2\]
\>>> y\_pred \= \[\-2, \-2, \-2 + 1e-8\]
\>>> explained\_variance\_score(y\_true, y\_pred)
0.0
\>>> explained\_variance\_score(y\_true, y\_pred, force\_finite\=False)
\-inf

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)