[Skip to main content](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/svm/plot_svm_scale_c.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/svm/plot_svm_scale_c.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/svm/plot_svm_scale_c.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/svm/plot_svm_scale_c.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/svm/plot_svm_scale_c.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/svm/plot_svm_scale_c.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html#sphx-glr-download-auto-examples-svm-plot-svm-scale-c-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Scaling the regularization parameter for SVCs[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html#scaling-the-regularization-parameter-for-svcs "Link to this heading")

===============================================================================================================================================================================================

The following example illustrates the effect of scaling the regularization parameter when using [Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html#svm)
 for [classification](https://scikit-learn.org/stable/modules/svm.html#svm-classification)
. For SVC classification, we are interested in a risk minimization for the equation:

C∑i\=1,nL(f(xi),yi)+Ω(w)

where

*   C is used to set the amount of regularization
    
*   L is a `loss` function of our samples and our model parameters.
    
*   Ω is a `penalty` function of our model parameters
    

If we consider the loss function to be the individual error per sample, then the data-fit term, or the sum of the error for each sample, increases as we add more samples. The penalization term, however, does not increase.

When using, for example, [cross validation](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)
, to set the amount of regularization with `C`, there would be a different amount of samples between the main problem and the smaller problems within the folds of the cross validation.

Since the loss function depends on the amount of samples, the latter influences the selected value of `C`. The question that arises is “How do we optimally adjust C to account for the different amount of training samples?”

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Data generation[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html#data-generation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

In this example we investigate the effect of reparametrizing the regularization parameter `C` to account for the number of samples when using either L1 or L2 penalty. For such purpose we create a synthetic dataset with a large number of features, out of which only a few are informative. We therefore expect the regularization to shrink the coefficients towards zero (L2 penalty) or exactly zero (L1 penalty).

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")

n\_samples, n\_features \= 100, 300
X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(
    n\_samples\=n\_samples, n\_features\=n\_features, n\_informative\=5, random\_state\=1
)

Copy to clipboard

L1-penalty case[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html#l1-penalty-case "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

In the L1 case, theory says that provided a strong regularization, the estimator cannot predict as well as a model knowing the true distribution (even in the limit where the sample size grows to infinity) as it may set some weights of otherwise predictive features to zero, which induces a bias. It does say, however, that it is possible to find the right set of non-zero parameters as well as their signs by tuning `C`.

We define a linear SVC with the L1 penalty.

from sklearn.svm import [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")

model\_l1 \= [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
(penalty\="l1", loss\="squared\_hinge", dual\=False, tol\=1e-3)

Copy to clipboard

We compute the mean test score for different values of `C` via cross-validation.

import numpy as np
import pandas as pd

from sklearn.model\_selection import [ShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")
, [validation\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve "sklearn.model_selection.validation_curve")

Cs \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-2.3, \-1.3, 10)
train\_sizes \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.3, 0.7, 3)
labels \= \[f"fraction: {train\_size}" for train\_size in train\_sizes\]
shuffle\_params \= {
    "test\_size": 0.3,
    "n\_splits": 150,
    "random\_state": 1,
}

results \= {"C": Cs}
for label, train\_size in zip(labels, train\_sizes):
    cv \= [ShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")
(train\_size\=train\_size, \*\*shuffle\_params)
    train\_scores, test\_scores \= [validation\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve "sklearn.model_selection.validation_curve")
(
        model\_l1,
        X,
        y,
        param\_name\="C",
        param\_range\=Cs,
        cv\=cv,
        n\_jobs\=2,
    )
    results\[label\] \= test\_scores.mean(axis\=1)
results \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(results)

Copy to clipboard

import matplotlib.pyplot as plt

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=2, sharey\=True, figsize\=(12, 6))

\# plot results without scaling C
results.plot(x\="C", ax\=axes\[0\], logx\=True)
axes\[0\].set\_ylabel("CV score")
axes\[0\].set\_title("No scaling")

for label in labels:
    best\_C \= results.loc\[results\[label\].idxmax(), "C"\]
    axes\[0\].axvline(x\=best\_C, linestyle\="--", color\="grey", alpha\=0.7)

\# plot results by scaling C
for train\_size\_idx, label in enumerate(labels):
    train\_size \= train\_sizes\[train\_size\_idx\]
    results\_scaled \= results\[\[label\]\].assign(
        C\_scaled\=Cs \* float(n\_samples \* [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(train\_size))
    )
    results\_scaled.plot(x\="C\_scaled", ax\=axes\[1\], logx\=True, label\=label)
    best\_C\_scaled \= results\_scaled\["C\_scaled"\].loc\[results\[label\].idxmax()\]
    axes\[1\].axvline(x\=best\_C\_scaled, linestyle\="--", color\="grey", alpha\=0.7)

axes\[1\].set\_title("Scaling C by sqrt(1 / n\_samples)")

\_ \= fig.suptitle("Effect of scaling C with L1 penalty")

Copy to clipboard

![Effect of scaling C with L1 penalty, No scaling, Scaling C by sqrt(1 / n_samples)](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_scale_c_001.png)

In the region of small `C` (strong regularization) all the coefficients learned by the models are zero, leading to severe underfitting. Indeed, the accuracy in this region is at the chance level.

Using the default scale results in a somewhat stable optimal value of `C`, whereas the transition out of the underfitting region depends on the number of training samples. The reparameterization leads to even more stable results.

See e.g. theorem 3 of [On the prediction performance of the Lasso](https://arxiv.org/abs/1402.1700)
 or [Simultaneous analysis of Lasso and Dantzig selector](https://arxiv.org/abs/0801.1095)
 where the regularization parameter is always assumed to be proportional to 1 / sqrt(n\_samples).

L2-penalty case[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html#l2-penalty-case "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

We can do a similar experiment with the L2 penalty. In this case, the theory says that in order to achieve prediction consistency, the penalty parameter should be kept constant as the number of samples grow.

model\_l2 \= [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
(penalty\="l2", loss\="squared\_hinge", dual\=True)
Cs \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-8, 4, 11)

labels \= \[f"fraction: {train\_size}" for train\_size in train\_sizes\]
results \= {"C": Cs}
for label, train\_size in zip(labels, train\_sizes):
    cv \= [ShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")
(train\_size\=train\_size, \*\*shuffle\_params)
    train\_scores, test\_scores \= [validation\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve "sklearn.model_selection.validation_curve")
(
        model\_l2,
        X,
        y,
        param\_name\="C",
        param\_range\=Cs,
        cv\=cv,
        n\_jobs\=2,
    )
    results\[label\] \= test\_scores.mean(axis\=1)
results \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(results)

Copy to clipboard

import matplotlib.pyplot as plt

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=2, sharey\=True, figsize\=(12, 6))

\# plot results without scaling C
results.plot(x\="C", ax\=axes\[0\], logx\=True)
axes\[0\].set\_ylabel("CV score")
axes\[0\].set\_title("No scaling")

for label in labels:
    best\_C \= results.loc\[results\[label\].idxmax(), "C"\]
    axes\[0\].axvline(x\=best\_C, linestyle\="--", color\="grey", alpha\=0.8)

\# plot results by scaling C
for train\_size\_idx, label in enumerate(labels):
    results\_scaled \= results\[\[label\]\].assign(
        C\_scaled\=Cs \* float(n\_samples \* [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(train\_sizes\[train\_size\_idx\]))
    )
    results\_scaled.plot(x\="C\_scaled", ax\=axes\[1\], logx\=True, label\=label)
    best\_C\_scaled \= results\_scaled\["C\_scaled"\].loc\[results\[label\].idxmax()\]
    axes\[1\].axvline(x\=best\_C\_scaled, linestyle\="--", color\="grey", alpha\=0.8)
axes\[1\].set\_title("Scaling C by sqrt(1 / n\_samples)")

fig.suptitle("Effect of scaling C with L2 penalty")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Effect of scaling C with L2 penalty, No scaling, Scaling C by sqrt(1 / n_samples)](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_scale_c_002.png)

For the L2 penalty case, the reparameterization seems to have a smaller impact on the stability of the optimal value for the regularization. The transition out of the overfitting region occurs in a more spread range and the accuracy does not seem to be degraded up to chance level.

Try increasing the value to `n_splits=1_000` for better results in the L2 case, which is not shown here due to the limitations on the documentation builder.

**Total running time of the script:** (0 minutes 24.825 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_svm_scale_c.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_svm_scale_c.ipynb)

[`Download Jupyter notebook: plot_svm_scale_c.ipynb`](https://scikit-learn.org/stable/_downloads/1ed4d16a866c9fe4d86a05477e6d0664/plot_svm_scale_c.ipynb)

[`Download Python source code: plot_svm_scale_c.py`](https://scikit-learn.org/stable/_downloads/71939e5f0d3f41f3e224fafac2fea9f2/plot_svm_scale_c.py)

[`Download zipped: plot_svm_scale_c.zip`](https://scikit-learn.org/stable/_downloads/b327cd0a0802e17daefbd5de7ade2705/plot_svm_scale_c.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_l1_l2_sparsity_thumb.png)

[L1 Penalty and Sparsity in Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html)

L1 Penalty and Sparsity in Logistic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_coeffs_thumb.png)

[Ridge coefficients as a function of the L2 Regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html)

Ridge coefficients as a function of the L2 Regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_train_error_vs_test_error_thumb.png)

[Effect of model regularization on training and test error](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html)

Effect of model regularization on training and test error

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_thumb.png)

[Importance of Feature Scaling](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html)

Importance of Feature Scaling

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/71939e5f0d3f41f3e224fafac2fea9f2/plot_svm_scale_c.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/1ed4d16a866c9fe4d86a05477e6d0664/plot_svm_scale_c.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/b327cd0a0802e17daefbd5de7ade2705/plot_svm_scale_c.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_svm_scale_c.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_svm_scale_c.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)