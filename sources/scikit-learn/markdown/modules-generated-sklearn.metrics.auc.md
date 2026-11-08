[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.auc.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.auc.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.auc.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.auc.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.auc.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.auc.html)

Collapse Sidebar Expand Sidebar

auc[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#auc "Link to this heading")

==============================================================================================================

sklearn.metrics.auc(_x_, _y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_ranking.py#L49)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "Link to this definition")

Compute Area Under the Curve (AUC) using the trapezoidal rule.

This is a general function, given points on a curve. For computing the area under the ROC-curve, see [`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
. For an alternative way to summarize a precision-recall curve, see [`average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
.

Parameters:

**x**array-like of shape (n,)

X coordinates. These must be either monotonic increasing or monotonic decreasing.

**y**array-like of shape (n,)

Y coordinates.

Returns:

**auc**float

Area Under the Curve.

See also

[`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")

Compute the area under the ROC curve.

[`average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")

Compute average precision from prediction scores.

[`precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")

Compute precision-recall pairs for different probability thresholds.

Examples

\>>> import numpy as np
\>>> from sklearn import metrics
\>>> y\_true \= np.array(\[1, 1, 2, 2\])
\>>> y\_score \= np.array(\[0.1, 0.4, 0.35, 0.8\])
\>>> fpr, tpr, thresholds \= metrics.roc\_curve(y\_true, y\_score, pos\_label\=2)
\>>> metrics.auc(fpr, tpr)
0.75

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_species_distribution_modeling_thumb.png)

[Species distribution modeling](https://scikit-learn.org/stable/auto_examples/applications/plot_species_distribution_modeling.html)

Species distribution modeling

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_thumb.png)

[Poisson regression and non-normal loss](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)

Poisson regression and non-normal loss

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tweedie_regression_insurance_claims_thumb.png)

[Tweedie regression on insurance claims](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)

Tweedie regression on insurance claims

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_thumb.png)

[Precision-Recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

Precision-Recall

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_thumb.png)

[Multiclass Receiver Operating Characteristic (ROC)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)

Multiclass Receiver Operating Characteristic (ROC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_crossval_thumb.png)

[Receiver Operating Characteristic (ROC) with cross validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc_crossval.html)

Receiver Operating Characteristic (ROC) with cross validation

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)