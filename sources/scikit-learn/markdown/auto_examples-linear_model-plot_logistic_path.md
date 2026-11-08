[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_logistic_path.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_logistic_path.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_logistic_path.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_logistic_path.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_logistic_path.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_logistic_path.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html#sphx-glr-download-auto-examples-linear-model-plot-logistic-path-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Regularization path of L1- Logistic Regression[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html#regularization-path-of-l1-logistic-regression "Link to this heading")

===========================================================================================================================================================================================================

Train l1-penalized logistic regression models on a binary classification problem derived from the Iris dataset.

The models are ordered from strongest regularized to least regularized. The 4 coefficients of the models are collected and plotted as a “regularization path”: on the left-hand side of the figure (strong regularizers), all the coefficients are exactly 0. When regularization gets progressively looser, coefficients can get non-zero values one after the other.

Here we choose the liblinear solver because it can efficiently optimize for the Logistic Regression loss with a non-smooth, sparsity inducing l1 penalty.

Also note that we set a low value for the tolerance to make sure that the model has converged before collecting the coefficients.

We also use warm\_start=True which means that the coefficients of the models are reused to initialize the next model fit to speed-up the computation of the full-path.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Load data[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html#load-data "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

from sklearn import datasets

iris \= [datasets.load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X \= iris.data
y \= iris.target
feature\_names \= iris.feature\_names

Copy to clipboard

Here we remove the third class to make the problem a binary classification

X \= X\[y != 2\]
y \= y\[y != 2\]

Copy to clipboard

Compute regularization path[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html#compute-regularization-path "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np

from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
from sklearn.svm import [l1\_min\_c](https://scikit-learn.org/stable/modules/generated/sklearn.svm.l1_min_c.html#sklearn.svm.l1_min_c "sklearn.svm.l1_min_c")

cs \= [l1\_min\_c](https://scikit-learn.org/stable/modules/generated/sklearn.svm.l1_min_c.html#sklearn.svm.l1_min_c "sklearn.svm.l1_min_c")
(X, y, loss\="log") \* [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(0, 1, 16)

Copy to clipboard

Create a pipeline with `StandardScaler` and `LogisticRegression`, to normalize the data before fitting a linear model, in order to speed-up convergence and make the coefficients comparable. Also, as a side effect, since the data is now centered around 0, we don’t need to fit an intercept.

clf \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(),
    [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(
        l1\_ratio\=1,
        solver\="liblinear",
        tol\=1e-6,
        max\_iter\=int(1e6),
        warm\_start\=True,
        fit\_intercept\=False,
    ),
)
coefs\_ \= \[\]
for c in cs:
    clf.set\_params(logisticregression\_\_C\=c)
    clf.fit(X, y)
    coefs\_.append(clf\["logisticregression"\].coef\_.ravel().copy())

coefs\_ \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(coefs\_)

Copy to clipboard

Plot regularization path[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_path.html#plot-regularization-path "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

\# Colorblind-friendly palette (IBM Color Blind Safe palette)
colors \= \["#648FFF", "#785EF0", "#DC267F", "#FE6100"\]

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 6))
for i in range(coefs\_.shape\[1\]):
    [plt.semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx "matplotlib.pyplot.semilogx")
(cs, coefs\_\[:, i\], marker\="o", color\=colors\[i\], label\=feature\_names\[i\])

ymin, ymax \= [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("C")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Coefficients")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Logistic Regression Path")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Logistic Regression Path](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_path_001.png)

**Total running time of the script:** (0 minutes 0.177 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_logistic_path.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_logistic_path.ipynb)

[`Download Jupyter notebook: plot_logistic_path.ipynb`](https://scikit-learn.org/stable/_downloads/0b601219a14824c971bbf8bb797e8973/plot_logistic_path.ipynb)

[`Download Python source code: plot_logistic_path.py`](https://scikit-learn.org/stable/_downloads/33d1c05f40549996ff7b58dfd3eb9d23/plot_logistic_path.py)

[`Download zipped: plot_logistic_path.zip`](https://scikit-learn.org/stable/_downloads/2e18b618565acbb9b5918136a879a534/plot_logistic_path.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_coeffs_thumb.png)

[Ridge coefficients as a function of the L2 Regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html)

Ridge coefficients as a function of the L2 Regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_train_error_vs_test_error_thumb.png)

[Effect of model regularization on training and test error](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html)

Effect of model regularization on training and test error

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_path_thumb.png)

[Plot Ridge coefficients as a function of the regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html)

Plot Ridge coefficients as a function of the regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_l1_l2_sparsity_thumb.png)

[L1 Penalty and Sparsity in Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html)

L1 Penalty and Sparsity in Logistic Regression

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/33d1c05f40549996ff7b58dfd3eb9d23/plot_logistic_path.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/0b601219a14824c971bbf8bb797e8973/plot_logistic_path.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/2e18b618565acbb9b5918136a879a534/plot_logistic_path.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_logistic_path.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_logistic_path.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)