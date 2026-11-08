[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_train_error_vs_test_error.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_train_error_vs_test_error.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_train_error_vs_test_error.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_train_error_vs_test_error.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_train_error_vs_test_error.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_train_error_vs_test_error.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html#sphx-glr-download-auto-examples-model-selection-plot-train-error-vs-test-error-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Effect of model regularization on training and test error[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html#effect-of-model-regularization-on-training-and-test-error "Link to this heading")

=================================================================================================================================================================================================================================================

In this example, we evaluate the impact of the regularization parameter in a linear model called [`ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
. To carry out this evaluation, we use a validation curve using [`ValidationCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ValidationCurveDisplay.html#sklearn.model_selection.ValidationCurveDisplay "sklearn.model_selection.ValidationCurveDisplay")
. This curve shows the training and test scores of the model for different values of the regularization parameter.

Once we identify the optimal regularization parameter, we compare the true and estimated coefficients of the model to determine if the model is able to recover the coefficients from the noisy input data.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate sample data[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html#generate-sample-data "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

We generate a regression dataset that contains many features relative to the number of samples. However, only 10% of the features are informative. In this context, linear models exposing L1 penalization are commonly used to recover a sparse set of coefficients.

from sklearn.datasets import [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

n\_samples\_train, n\_samples\_test, n\_features \= 150, 300, 500
X, y, true\_coef \= [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
(
    n\_samples\=n\_samples\_train + n\_samples\_test,
    n\_features\=n\_features,
    n\_informative\=50,
    shuffle\=False,
    noise\=1.0,
    coef\=True,
    random\_state\=42,
)
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, train\_size\=n\_samples\_train, test\_size\=n\_samples\_test, shuffle\=False
)

Copy to clipboard

Model definition[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html#model-definition "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

Here, we do not use a model that only exposes an L1 penalty. Instead, we use an [`ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
 model that exposes both L1 and L2 penalties.

We fix the `l1_ratio` parameter such that the solution found by the model is still sparse. Therefore, this type of model tries to find a sparse solution but at the same time also tries to shrink all coefficients towards zero.

In addition, we force the coefficients of the model to be positive since we know that `make_regression` generates a response with a positive signal. So we use this pre-knowledge to get a better model.

from sklearn.linear\_model import [ElasticNet](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")

enet \= [ElasticNet](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
(l1\_ratio\=0.9, positive\=True, max\_iter\=10\_000)

Copy to clipboard

Evaluate the impact of the regularization parameter[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html#evaluate-the-impact-of-the-regularization-parameter "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To evaluate the impact of the regularization parameter, we use a validation curve. This curve shows the training and test scores of the model for different values of the regularization parameter.

The regularization `alpha` is a parameter applied to the coefficients of the model: when it tends to zero, no regularization is applied and the model tries to fit the training data with the least amount of error. However, it leads to overfitting when features are noisy. When `alpha` increases, the model coefficients are constrained, and thus the model cannot fit the training data as closely, avoiding overfitting. However, if too much regularization is applied, the model underfits the data and is not able to properly capture the signal.

The validation curve helps in finding a good trade-off between both extremes: the model is not regularized and thus flexible enough to fit the signal, but not too flexible to overfit. The [`ValidationCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ValidationCurveDisplay.html#sklearn.model_selection.ValidationCurveDisplay "sklearn.model_selection.ValidationCurveDisplay")
 allows us to display the training and validation scores across a range of alpha values.

import numpy as np

from sklearn.model\_selection import ValidationCurveDisplay

alphas \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-5, 1, 60)
disp \= [ValidationCurveDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ValidationCurveDisplay.html#sklearn.model_selection.ValidationCurveDisplay.from_estimator "sklearn.model_selection.ValidationCurveDisplay.from_estimator")
(
    enet,
    X\_train,
    y\_train,
    param\_name\="alpha",
    param\_range\=alphas,
    scoring\="r2",
    n\_jobs\=2,
    score\_type\="both",
)
disp.ax\_.set(
    title\=r"Validation Curve for ElasticNet (R$^2$ Score)",
    xlabel\=r"alpha (regularization strength)",
    ylabel\="R$^2$ Score",
)

test\_scores\_mean \= disp.test\_scores.mean(axis\=1)
idx\_avg\_max\_test\_score \= [np.argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax")
(test\_scores\_mean)
disp.ax\_.vlines(
    alphas\[idx\_avg\_max\_test\_score\],
    disp.ax\_.get\_ylim()\[0\],
    test\_scores\_mean\[idx\_avg\_max\_test\_score\],
    color\="k",
    linewidth\=2,
    linestyle\="--",
    label\=f"Optimum on test\\n$\\\\alpha$ = {alphas\[idx\_avg\_max\_test\_score\]:.2e}",
)
\_ \= disp.ax\_.legend(loc\="lower right")

Copy to clipboard

![Validation Curve for ElasticNet (R$^2$ Score)](https://scikit-learn.org/stable/_images/sphx_glr_plot_train_error_vs_test_error_001.png)

To find the optimal regularization parameter, we can select the value of `alpha` that maximizes the validation score.

Coefficients comparison[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html#coefficients-comparison "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now that we have identified the optimal regularization parameter, we can compare the true coefficients and the estimated coefficients.

First, let’s set the regularization parameter to the optimal value and fit the model on the training data. In addition, we’ll show the test score for this model.

enet.set\_params(alpha\=alphas\[idx\_avg\_max\_test\_score\]).fit(X\_train, y\_train)
print(
    f"Test score: {enet.score(X\_test, y\_test):.3f}",
)

Copy to clipboard

Test score: 0.884

Copy to clipboard

Now, we plot the true coefficients and the estimated coefficients.

import matplotlib.pyplot as plt

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(12, 6), sharex\=True, sharey\=True)
for ax, coef, title in zip(axs, \[true\_coef, enet.coef\_\], \["True", "Model"\]):
    ax.stem(coef)
    ax.set(
        title\=f"{title} Coefficients",
        xlabel\="Feature Index",
        ylabel\="Coefficient Value",
    )
fig.suptitle(
    "Comparison of the coefficients of the true generative model and \\n"
    "the estimated elastic net coefficients"
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Comparison of the coefficients of the true generative model and  the estimated elastic net coefficients, True Coefficients, Model Coefficients](https://scikit-learn.org/stable/_images/sphx_glr_plot_train_error_vs_test_error_002.png)

While the original coefficients are sparse, the estimated coefficients are not as sparse. The reason is that we fixed the `l1_ratio` parameter to 0.9. We could force the model to get a sparser solution by increasing the `l1_ratio` parameter.

However, we observed that for the estimated coefficients that are close to zero in the true generative model, our model shrinks them towards zero. So we don’t recover the true coefficients, but we get a sensible outcome in line with the performance obtained on the test set.

**Total running time of the script:** (0 minutes 5.986 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_train_error_vs_test_error.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_train_error_vs_test_error.ipynb)

[`Download Jupyter notebook: plot_train_error_vs_test_error.ipynb`](https://scikit-learn.org/stable/_downloads/b49810e68af99a01e25ba2dfc951b687/plot_train_error_vs_test_error.ipynb)

[`Download Python source code: plot_train_error_vs_test_error.py`](https://scikit-learn.org/stable/_downloads/dcb776e3eb7cce048909ddcd70100917/plot_train_error_vs_test_error.py)

[`Download zipped: plot_train_error_vs_test_error.zip`](https://scikit-learn.org/stable/_downloads/899ea87b7908a2db16ce24485576e5db/plot_train_error_vs_test_error.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_coeffs_thumb.png)

[Ridge coefficients as a function of the L2 Regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html)

Ridge coefficients as a function of the L2 Regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_path_thumb.png)

[Plot Ridge coefficients as a function of the regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html)

Plot Ridge coefficients as a function of the regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_thumb.png)

[L1-based models for Sparse Signals](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html)

L1-based models for Sparse Signals

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_path_thumb.png)

[Regularization path of L1- Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html)

Regularization path of L1- Logistic Regression

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/dcb776e3eb7cce048909ddcd70100917/plot_train_error_vs_test_error.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/b49810e68af99a01e25ba2dfc951b687/plot_train_error_vs_test_error.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/899ea87b7908a2db16ce24485576e5db/plot_train_error_vs_test_error.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_train_error_vs_test_error.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_train_error_vs_test_error.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)