[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_early_stopping.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_sgd_early_stopping.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_early_stopping.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_sgd_early_stopping.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_sgd_early_stopping.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_sgd_early_stopping.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_sgd_early_stopping.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_sgd_early_stopping.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_early_stopping.html#sphx-glr-download-auto-examples-linear-model-plot-sgd-early-stopping-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Early stopping of Stochastic Gradient Descent[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_early_stopping.html#early-stopping-of-stochastic-gradient-descent "Link to this heading")

===============================================================================================================================================================================================================

Stochastic Gradient Descent is an optimization technique which minimizes a loss function in a stochastic fashion, performing a gradient descent step sample by sample. In particular, it is a very efficient method to fit linear models.

As a stochastic method, the loss function is not necessarily decreasing at each iteration, and convergence is only guaranteed in expectation. For this reason, monitoring the convergence on the loss function can be difficult.

Another approach is to monitor convergence on a validation score. In this case, the input data is split into a training set and a validation set. The model is then fitted on the training set and the stopping criterion is based on the prediction score computed on the validation set. This enables us to find the least number of iterations which is sufficient to build a model that generalizes well to unseen data and reduces the chance of over-fitting the training data.

This early stopping strategy is activated if `early_stopping=True`; otherwise the stopping criterion only uses the training loss on the entire input data. To better control the early stopping strategy, we can specify a parameter `validation_fraction` which set the fraction of the input dataset that we keep aside to compute the validation score. The optimization will continue until the validation score did not improve by at least `tol` during the last `n_iter_no_change` iterations. The actual number of iterations is available at the attribute `n_iter_`.

This example illustrates how the early stopping can used in the [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 model to achieve almost the same accuracy as compared to a model built without early stopping. This can significantly reduce training time. Note that scores differ between the stopping criteria even from early iterations because some of the training data is held out with the validation stopping criterion.

*   ![Train score, Test score](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_early_stopping_001.png)
*   ![n_iter_, Fit time (sec)](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_early_stopping_002.png)

No stopping criterion: .................................................
Training loss: .................................................
Validation score: .................................................

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import sys
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn import linear\_model
from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
from sklearn.exceptions import [ConvergenceWarning](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.utils import [shuffle](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#sklearn.utils.shuffle "sklearn.utils.shuffle")
from sklearn.utils.\_testing import ignore\_warnings

def load\_mnist(n\_samples\=None, class\_0\="0", class\_1\="8"):
    """Load MNIST, select two classes, shuffle and return only n\_samples."""
    \# Load data from http://openml.org/d/554
    mnist \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
("mnist\_784", version\=1, as\_frame\=False)

    \# take only two classes for binary classification
    mask \= [np.logical\_or](https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html#numpy.logical_or "numpy.logical_or")
(mnist.target \== class\_0, mnist.target \== class\_1)

    X, y \= [shuffle](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#sklearn.utils.shuffle "sklearn.utils.shuffle")
(mnist.data\[mask\], mnist.target\[mask\], random\_state\=42)
    if n\_samples is not None:
        X, y \= X\[:n\_samples\], y\[:n\_samples\]
    return X, y

@ignore\_warnings(category\=[ConvergenceWarning](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
)
def fit\_and\_score(estimator, max\_iter, X\_train, X\_test, y\_train, y\_test):
    """Fit the estimator on the train set and score it on both sets"""
    estimator.set\_params(max\_iter\=max\_iter)
    estimator.set\_params(random\_state\=0)

    start \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    estimator.fit(X\_train, y\_train)

    fit\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start
    n\_iter \= estimator.n\_iter\_
    train\_score \= estimator.score(X\_train, y\_train)
    test\_score \= estimator.score(X\_test, y\_test)

    return fit\_time, n\_iter, train\_score, test\_score

\# Define the estimators to compare
estimator\_dict \= {
    "No stopping criterion": [linear\_model.SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
(n\_iter\_no\_change\=3),
    "Training loss": [linear\_model.SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
(
        early\_stopping\=False, n\_iter\_no\_change\=3, tol\=0.1
    ),
    "Validation score": [linear\_model.SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
(
        early\_stopping\=True, n\_iter\_no\_change\=3, tol\=0.0001, validation\_fraction\=0.2
    ),
}

\# Load the dataset
X, y \= load\_mnist(n\_samples\=10000)
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, test\_size\=0.5, random\_state\=0)

results \= \[\]
for estimator\_name, estimator in estimator\_dict.items():
    print(estimator\_name + ": ", end\="")
    for max\_iter in range(1, 50):
        print(".", end\="")
        sys.stdout.flush()

        fit\_time, n\_iter, train\_score, test\_score \= fit\_and\_score(
            estimator, max\_iter, X\_train, X\_test, y\_train, y\_test
        )

        results.append(
            (estimator\_name, max\_iter, fit\_time, n\_iter, train\_score, test\_score)
        )
    print("")

\# Transform the results in a pandas dataframe for easy plotting
columns \= \[\
    "Stopping criterion",\
    "max\_iter",\
    "Fit time (sec)",\
    "n\_iter\_",\
    "Train score",\
    "Test score",\
\]
results\_df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(results, columns\=columns)

\# Define what to plot
lines \= "Stopping criterion"
x\_axis \= "max\_iter"
styles \= \["-.", "--", "-"\]

\# First plot: train and test scores
fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=2, sharey\=True, figsize\=(12, 4))
for ax, y\_axis in zip(axes, \["Train score", "Test score"\]):
    for style, (criterion, group\_df) in zip(styles, results\_df.groupby(lines)):
        group\_df.plot(x\=x\_axis, y\=y\_axis, label\=criterion, ax\=ax, style\=style)
    ax.set\_title(y\_axis)
    ax.legend(title\=lines)
fig.tight\_layout()

\# Second plot: n\_iter and fit time
fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=2, figsize\=(12, 4))
for ax, y\_axis in zip(axes, \["n\_iter\_", "Fit time (sec)"\]):
    for style, (criterion, group\_df) in zip(styles, results\_df.groupby(lines)):
        group\_df.plot(x\=x\_axis, y\=y\_axis, label\=criterion, ax\=ax, style\=style)
    ax.set\_title(y\_axis)
    ax.legend(title\=lines)
fig.tight\_layout()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 27.034 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sgd_early_stopping.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sgd_early_stopping.ipynb)

[`Download Jupyter notebook: plot_sgd_early_stopping.ipynb`](https://scikit-learn.org/stable/_downloads/389fb4950ddfe12a741e6ac5b7d79193/plot_sgd_early_stopping.ipynb)

[`Download Python source code: plot_sgd_early_stopping.py`](https://scikit-learn.org/stable/_downloads/b4d6bfda6769cc5cc1cf25427dec34d6/plot_sgd_early_stopping.py)

[`Download zipped: plot_sgd_early_stopping.zip`](https://scikit-learn.org/stable/_downloads/770d16dafa0c41ebe338b3627690c266/plot_sgd_early_stopping.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_early_stopping_thumb.png)

[Early stopping in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html)

Early stopping in Gradient Boosting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_model_selection_thumb.png)

[Lasso model selection: AIC-BIC / cross-validation](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html)

Lasso model selection: AIC-BIC / cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scoring_monitor_thumb.png)

[Analysis of the convergence of penalized logistic regression models](https://scikit-learn.org/stable/auto_examples/callbacks/plot_scoring_monitor.html)

Analysis of the convergence of penalized logistic regression models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_thumb.png)

[Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html)

Features in Histogram Gradient Boosting Trees

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/b4d6bfda6769cc5cc1cf25427dec34d6/plot_sgd_early_stopping.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/389fb4950ddfe12a741e6ac5b7d79193/plot_sgd_early_stopping.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/770d16dafa0c41ebe338b3627690c266/plot_sgd_early_stopping.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sgd_early_stopping.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sgd_early_stopping.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)