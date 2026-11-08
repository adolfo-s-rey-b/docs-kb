[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_gamma_deviance.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.mean_gamma_deviance.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_gamma_deviance.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.mean_gamma_deviance.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.mean_gamma_deviance.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.mean_gamma_deviance.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.mean_gamma_deviance.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.mean_gamma_deviance.html)

Collapse Sidebar Expand Sidebar

mean\_gamma\_deviance[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_gamma_deviance.html#mean-gamma-deviance "Link to this heading")

================================================================================================================================================================

sklearn.metrics.mean\_gamma\_deviance(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_regression.py#L1538)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_gamma_deviance.html#sklearn.metrics.mean_gamma_deviance "Link to this definition")

Mean Gamma deviance regression loss.

Gamma deviance is equivalent to the Tweedie deviance with the power parameter `power=2`. It is invariant to scaling of the target variable, and measures relative errors.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#mean-tweedie-deviance)
.

Parameters:

**y\_true**array-like of shape (n\_samples,)

Ground truth (correct) target values. Requires y\_true > 0.

**y\_pred**array-like of shape (n\_samples,)

Estimated target values. Requires y\_pred > 0.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**loss**float

A non-negative floating point value (the best value is 0.0).

Examples

\>>> from sklearn.metrics import mean\_gamma\_deviance
\>>> y\_true \= \[2, 0.5, 1, 4\]
\>>> y\_pred \= \[0.5, 0.5, 2., 2.\]
\>>> mean\_gamma\_deviance(y\_true, y\_pred)
1.0568...

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)