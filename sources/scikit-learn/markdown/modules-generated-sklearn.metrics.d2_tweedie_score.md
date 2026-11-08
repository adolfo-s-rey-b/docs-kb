[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_tweedie_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.d2_tweedie_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_tweedie_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.d2_tweedie_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.d2_tweedie_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.d2_tweedie_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.d2_tweedie_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.d2_tweedie_score.html)

Collapse Sidebar Expand Sidebar

d2\_tweedie\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_tweedie_score.html#d2-tweedie-score "Link to this heading")

=======================================================================================================================================================

sklearn.metrics.d2\_tweedie\_score(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_, _power\=0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_regression.py#L1582)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_tweedie_score.html#sklearn.metrics.d2_tweedie_score "Link to this definition")

D2 regression score function, fraction of Tweedie deviance explained.

Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A model that always uses the empirical mean of `y_true` as constant prediction, disregarding the input features, gets a D^2 score of 0.0.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#d2-score)
.

Added in version 1.0.

Parameters:

**y\_true**array-like of shape (n\_samples,)

Ground truth (correct) target values.

**y\_pred**array-like of shape (n\_samples,)

Estimated target values.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

**power**float, default=0

Tweedie power parameter. Either power <= 0 or power >= 1.

The higher `p` the less weight is given to extreme deviations between true and predicted targets.

*   power < 0: Extreme stable distribution. Requires: y\_pred > 0.
    
*   power = 0 : Normal distribution, output corresponds to r2\_score. y\_true and y\_pred can be any real numbers.
    
*   power = 1 : Poisson distribution. Requires: y\_true >= 0 and y\_pred > 0.
    
*   1 < p < 2 : Compound Poisson distribution. Requires: y\_true >= 0 and y\_pred > 0.
    
*   power = 2 : Gamma distribution. Requires: y\_true > 0 and y\_pred > 0.
    
*   power = 3 : Inverse Gaussian distribution. Requires: y\_true > 0 and y\_pred > 0.
    
*   otherwise : Positive stable distribution. Requires: y\_true > 0 and y\_pred > 0.
    

Returns:

**z**float

The D^2 score.

Notes

This is not a symmetric function.

Like R^2, D^2 score may be negative (it need not actually be the square of a quantity D).

This metric is not well-defined for single samples and will return a NaN value if n\_samples is less than two.

References

\[1\]

Eq. (3.11) of Hastie, Trevor J., Robert Tibshirani and Martin J. Wainwright. “Statistical Learning with Sparsity: The Lasso and Generalizations.” (2015). [https://hastie.su.domains/StatLearnSparsity/](https://hastie.su.domains/StatLearnSparsity/)

Examples

\>>> from sklearn.metrics import d2\_tweedie\_score
\>>> y\_true \= \[0.5, 1, 2.5, 7\]
\>>> y\_pred \= \[1, 1, 5, 3.5\]
\>>> d2\_tweedie\_score(y\_true, y\_pred)
0.285...
\>>> d2\_tweedie\_score(y\_true, y\_pred, power\=1)
0.487...
\>>> d2\_tweedie\_score(y\_true, y\_pred, power\=2)
0.630...
\>>> d2\_tweedie\_score(y\_true, y\_true, power\=2)
1.0

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)