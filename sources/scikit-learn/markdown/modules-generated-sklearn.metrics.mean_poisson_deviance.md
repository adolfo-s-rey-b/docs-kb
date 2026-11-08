[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.mean_poisson_deviance.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.mean_poisson_deviance.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.mean_poisson_deviance.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.mean_poisson_deviance.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.mean_poisson_deviance.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.mean_poisson_deviance.html)

Collapse Sidebar Expand Sidebar

mean\_poisson\_deviance[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html#mean-poisson-deviance "Link to this heading")

======================================================================================================================================================================

sklearn.metrics.mean\_poisson\_deviance(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_regression.py#L1495)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html#sklearn.metrics.mean_poisson_deviance "Link to this definition")

Mean Poisson deviance regression loss.

Poisson deviance is equivalent to the Tweedie deviance with the power parameter `power=1`.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#mean-tweedie-deviance)
.

Parameters:

**y\_true**array-like of shape (n\_samples,)

Ground truth (correct) target values. Requires y\_true >= 0.

**y\_pred**array-like of shape (n\_samples,)

Estimated target values. Requires y\_pred > 0.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**loss**float

A non-negative floating point value (the best value is 0.0).

Examples

\>>> from sklearn.metrics import mean\_poisson\_deviance
\>>> y\_true \= \[2, 0, 1, 4\]
\>>> y\_pred \= \[0.5, 0.5, 2., 2.\]
\>>> mean\_poisson\_deviance(y\_true, y\_pred)
1.4260...

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_thumb.png)

[Poisson regression and non-normal loss](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)

Poisson regression and non-normal loss

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)