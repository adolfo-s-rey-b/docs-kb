[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.mean_tweedie_deviance.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.mean_tweedie_deviance.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.mean_tweedie_deviance.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.mean_tweedie_deviance.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.mean_tweedie_deviance.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.mean_tweedie_deviance.html)

Collapse Sidebar Expand Sidebar

mean\_tweedie\_deviance[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html#mean-tweedie-deviance "Link to this heading")

======================================================================================================================================================================

sklearn.metrics.mean\_tweedie\_deviance(_y\_true_, _y\_pred_, _\*_, _sample\_weight\=None_, _power\=0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_regression.py#L1398)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html#sklearn.metrics.mean_tweedie_deviance "Link to this definition")

Mean Tweedie deviance regression loss.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#mean-tweedie-deviance)
.

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
    
*   power = 0 : Normal distribution, output corresponds to mean\_squared\_error. y\_true and y\_pred can be any real numbers.
    
*   power = 1 : Poisson distribution. Requires: y\_true >= 0 and y\_pred > 0.
    
*   1 < p < 2 : Compound Poisson distribution. Requires: y\_true >= 0 and y\_pred > 0.
    
*   power = 2 : Gamma distribution. Requires: y\_true > 0 and y\_pred > 0.
    
*   power = 3 : Inverse Gaussian distribution. Requires: y\_true > 0 and y\_pred > 0.
    
*   otherwise : Positive stable distribution. Requires: y\_true > 0 and y\_pred > 0.
    

Returns:

**loss**float

A non-negative floating point value (the best value is 0.0).

Examples

\>>> from sklearn.metrics import mean\_tweedie\_deviance
\>>> y\_true \= \[2, 0, 1, 4\]
\>>> y\_pred \= \[0.5, 0.5, 2., 2.\]
\>>> mean\_tweedie\_deviance(y\_true, y\_pred, power\=1)
1.4260...

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tweedie_regression_insurance_claims_thumb.png)

[Tweedie regression on insurance claims](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)

Tweedie regression on insurance claims

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)