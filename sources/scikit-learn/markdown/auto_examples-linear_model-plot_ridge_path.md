[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_ridge_path.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_ridge_path.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_ridge_path.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_ridge_path.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_ridge_path.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_ridge_path.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html#sphx-glr-download-auto-examples-linear-model-plot-ridge-path-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Plot Ridge coefficients as a function of the regularization[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html#plot-ridge-coefficients-as-a-function-of-the-regularization "Link to this heading")

===================================================================================================================================================================================================================================

Shows the effect of collinearity in the coefficients of an estimator.

[`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
 Regression is the estimator used in this example. Each color represents a different feature of the coefficient vector, and this is displayed as a function of the regularization parameter.

This example also shows the usefulness of applying Ridge regression to highly ill-conditioned matrices. For such matrices, a slight change in the target variable can cause huge variances in the calculated weights. In such cases, it is useful to set a certain regularization (alpha) to reduce this variation (noise).

When alpha is very large, the regularization effect dominates the squared loss function and the coefficients tend to zero. At the end of the path, as alpha tends toward zero and the solution tends towards the ordinary least squares, coefficients exhibit big oscillations. In practice it is necessary to tune alpha in such a way that a balance is maintained between both.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn import linear\_model

\# X is the 10x10 Hilbert matrix
X \= 1.0 / ([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(1, 11) + [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 10)\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\])
y \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(10)

Copy to clipboard

Compute paths[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html#compute-paths "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

n\_alphas \= 200
alphas \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-10, \-2, n\_alphas)

coefs \= \[\]
for a in alphas:
    ridge \= [linear\_model.Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
(alpha\=a, fit\_intercept\=False)
    ridge.fit(X, y)
    coefs.append(ridge.coef\_)

Copy to clipboard

Display results[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html#display-results "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

ax \= [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()

ax.plot(alphas, coefs)
ax.set\_xscale("log")
ax.set\_xlim(ax.get\_xlim()\[::\-1\])  \# reverse axis
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("alpha")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("weights")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Ridge Coefficients vs Regularization Strength (alpha)")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(
    \[f"Feature {i + 1}" for i in range(X.shape\[1\])\], loc\="best", fontsize\="small"
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Ridge Coefficients vs Regularization Strength (alpha)](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_path_001.png)

**Total running time of the script:** (0 minutes 0.372 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_ridge_path.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_ridge_path.ipynb)

[`Download Jupyter notebook: plot_ridge_path.ipynb`](https://scikit-learn.org/stable/_downloads/6caa16249d07b4f3e57d5f3bf102b137/plot_ridge_path.ipynb)

[`Download Python source code: plot_ridge_path.py`](https://scikit-learn.org/stable/_downloads/9d5a4167bc60f250de65fe21497c1eb6/plot_ridge_path.py)

[`Download zipped: plot_ridge_path.zip`](https://scikit-learn.org/stable/_downloads/8b139be9c3b091b5f6bbd2651331dadc/plot_ridge_path.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_coeffs_thumb.png)

[Ridge coefficients as a function of the L2 Regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html)

Ridge coefficients as a function of the L2 Regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_huber_vs_ridge_thumb.png)

[HuberRegressor vs Ridge on dataset with strong outliers](https://scikit-learn.org/stable/auto_examples/linear_model/plot_huber_vs_ridge.html)

HuberRegressor vs Ridge on dataset with strong outliers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_train_error_vs_test_error_thumb.png)

[Effect of model regularization on training and test error](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html)

Effect of model regularization on training and test error

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_thumb.png)

[Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)

Common pitfalls in the interpretation of coefficients of linear models

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/9d5a4167bc60f250de65fe21497c1eb6/plot_ridge_path.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/6caa16249d07b4f3e57d5f3bf102b137/plot_ridge_path.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/8b139be9c3b091b5f6bbd2651331dadc/plot_ridge_path.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_ridge_path.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_ridge_path.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)