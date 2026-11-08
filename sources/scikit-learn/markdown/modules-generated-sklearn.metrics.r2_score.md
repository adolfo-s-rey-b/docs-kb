[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.r2_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.r2_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.r2_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.r2_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.r2_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.r2_score.html)

Collapse Sidebar Expand Sidebar

r2\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#r2-score "Link to this heading")

==============================================================================================================================

sklearn.metrics.r2\_score(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_, _multioutput\='uniform\_average'_, _force\_finite\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_regression.py#L1143)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "Link to this definition")

R2 (coefficient of determination) regression score function.

Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). In the general case when the true y is non-constant, a constant model that always predicts the average y disregarding the input features would get a R2 score of 0.0.

In the particular case when `y_true` is constant, the R2 score is not finite: it is either `NaN` (perfect predictions) or `-Inf` (imperfect predictions). To prevent such non-finite numbers to pollute higher-level experiments such as a grid search cross-validation, by default these cases are replaced with 1.0 (perfect predictions) or 0.0 (imperfect predictions) respectively. You can set `force_finite` to `False` to prevent this fix from happening.

Note: when the prediction residuals have zero mean, the R2 score is identical to the [`Explained Variance score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score "sklearn.metrics.explained_variance_score")
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#r2-score)
.

Parameters:

**y\_true**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Ground truth (correct) target values.

**y\_pred**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)

Estimated target values.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**multioutput**{‘raw\_values’, ‘uniform\_average’, ‘variance\_weighted’}, array-like of shape (n\_outputs,) or None, default=’uniform\_average’

Defines aggregating of multiple output scores. Array-like value defines weights used to average scores. Default is “uniform\_average”.

‘raw\_values’ :

Returns a full set of scores in case of multioutput input.

‘uniform\_average’ :

Scores of all outputs are averaged with uniform weight.

‘variance\_weighted’ :

Scores of all outputs are averaged, weighted by the variances of each individual output.

Changed in version 0.19: Default value of multioutput is ‘uniform\_average’.

**force\_finite**bool, default=True

Flag indicating if `NaN` and `-Inf` scores resulting from constant data should be replaced with real numbers (`1.0` if prediction is perfect, `0.0` otherwise). Default is `True`, a convenient setting for hyperparameters’ search procedures (e.g. grid search cross-validation).

Added in version 1.1.

Returns:

**z**float or ndarray of floats

The R2 score or ndarray of scores if ‘multioutput’ is ‘raw\_values’.

Notes

This is not a symmetric function.

Unlike most other scores, R2 score may be negative (it need not actually be the square of a quantity R).

This metric is not well-defined for single samples and will return a NaN value if n\_samples is less than two.

References

\[1\]

[Wikipedia entry on the Coefficient of determination](https://en.wikipedia.org/wiki/Coefficient_of_determination)

Examples

\>>> from sklearn.metrics import r2\_score
\>>> y\_true \= \[3, \-0.5, 2, 7\]
\>>> y\_pred \= \[2.5, 0.0, 2, 8\]
\>>> r2\_score(y\_true, y\_pred)
0.948...
\>>> y\_true \= \[\[0.5, 1\], \[\-1, 1\], \[7, \-6\]\]
\>>> y\_pred \= \[\[0, 2\], \[\-1, 2\], \[8, \-5\]\]
\>>> r2\_score(y\_true, y\_pred,
...          multioutput\='variance\_weighted')
0.938...
\>>> y\_true \= \[1, 2, 3\]
\>>> y\_pred \= \[1, 2, 3\]
\>>> r2\_score(y\_true, y\_pred)
1.0
\>>> y\_true \= \[1, 2, 3\]
\>>> y\_pred \= \[2, 2, 2\]
\>>> r2\_score(y\_true, y\_pred)
0.0
\>>> y\_true \= \[1, 2, 3\]
\>>> y\_pred \= \[3, 2, 1\]
\>>> r2\_score(y\_true, y\_pred)
\-3.0
\>>> y\_true \= \[\-2, \-2, \-2\]
\>>> y\_pred \= \[\-2, \-2, \-2\]
\>>> r2\_score(y\_true, y\_pred)
1.0
\>>> r2\_score(y\_true, y\_pred, force\_finite\=False)
nan
\>>> y\_true \= \[\-2, \-2, \-2\]
\>>> y\_pred \= \[\-2, \-2, \-2 + 1e-8\]
\>>> r2\_score(y\_true, y\_pred)
0.0
\>>> r2\_score(y\_true, y\_pred, force\_finite\=False)
\-inf

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_thumb.png)

[Effect of transforming the targets in regression model](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html)

Effect of transforming the targets in regression model

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_causal_interpretation_thumb.png)

[Failure of Machine Learning to infer causal effects](https://scikit-learn.org/stable/auto_examples/inspection/plot_causal_interpretation.html)

Failure of Machine Learning to infer causal effects

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_thumb.png)

[L1-based models for Sparse Signals](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html)

L1-based models for Sparse Signals

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nnls_thumb.png)

[Non-negative least squares](https://scikit-learn.org/stable/auto_examples/linear_model/plot_nnls.html)

Non-negative least squares

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ols_ridge_thumb.png)

[Ordinary Least Squares and Ridge Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html)

Ordinary Least Squares and Ridge Regression

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)