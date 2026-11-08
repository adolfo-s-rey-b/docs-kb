[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_huber_vs_ridge.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_huber_vs_ridge.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_huber_vs_ridge.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_huber_vs_ridge.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_huber_vs_ridge.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_huber_vs_ridge.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_huber_vs_ridge.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_huber_vs_ridge.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_huber_vs_ridge.html#sphx-glr-download-auto-examples-linear-model-plot-huber-vs-ridge-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

HuberRegressor vs Ridge on dataset with strong outliers[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_huber_vs_ridge.html#huberregressor-vs-ridge-on-dataset-with-strong-outliers "Link to this heading")

===============================================================================================================================================================================================================================

Fit Ridge and HuberRegressor on a dataset with outliers.

The example shows that the predictions in ridge are strongly influenced by the outliers present in the dataset. The Huber regressor is less influenced by the outliers since the model uses the linear loss for these. As the parameter epsilon is increased for the Huber regressor, the decision function approaches that of the ridge.

![Comparison of HuberRegressor vs Ridge](https://scikit-learn.org/stable/_images/sphx_glr_plot_huber_vs_ridge_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
from sklearn.linear\_model import [HuberRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor")
, [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")

\# Generate toy data.
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
X, y \= [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
(
    n\_samples\=20, n\_features\=1, random\_state\=0, noise\=4.0, bias\=100.0
)

\# Add four strong outliers to the dataset.
X\_outliers \= rng.normal(0, 0.5, size\=(4, 1))
y\_outliers \= rng.normal(0, 2.0, size\=4)
X\_outliers\[:2, :\] += X.max() + X.mean() / 4.0
X\_outliers\[2:, :\] += X.min() \- X.mean() / 4.0
y\_outliers\[:2\] += y.min() \- y.mean() / 4.0
y\_outliers\[2:\] += y.max() + y.mean() / 4.0
X \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
((X, X\_outliers))
y \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
((y, y\_outliers))
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y, "b.")

\# Fit the huber regressor over a series of epsilon values.
colors \= \["r-", "b-", "y-", "m-"\]

x \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(X.min(), X.max(), 7)
epsilon\_values \= \[1, 1.5, 1.75, 1.9\]
for k, epsilon in enumerate(epsilon\_values):
    huber \= [HuberRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor")
(alpha\=0.0, epsilon\=epsilon)
    huber.fit(X, y)
    coef\_ \= huber.coef\_ \* x + huber.intercept\_
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(x, coef\_, colors\[k\], label\="huber loss, %s" % epsilon)

\# Fit a ridge regressor to compare it to huber regressor.
ridge \= [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
(alpha\=0.0, random\_state\=0)
ridge.fit(X, y)
coef\_ridge \= ridge.coef\_
coef\_ \= ridge.coef\_ \* x + ridge.intercept\_
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(x, coef\_, "g-", label\="ridge regression")

[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Comparison of HuberRegressor vs Ridge")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("X")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("y")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\=0)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.124 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_huber_vs_ridge.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_huber_vs_ridge.ipynb)

[`Download Jupyter notebook: plot_huber_vs_ridge.ipynb`](https://scikit-learn.org/stable/_downloads/c6a456b2390718e4dc79945608262e0b/plot_huber_vs_ridge.ipynb)

[`Download Python source code: plot_huber_vs_ridge.py`](https://scikit-learn.org/stable/_downloads/9676f328f9e6c3e55f218a33cea5586f/plot_huber_vs_ridge.py)

[`Download zipped: plot_huber_vs_ridge.zip`](https://scikit-learn.org/stable/_downloads/85657ba7194505e55a2b4b79bdf37ce4/plot_huber_vs_ridge.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_path_thumb.png)

[Plot Ridge coefficients as a function of the regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html)

Plot Ridge coefficients as a function of the regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ols_ridge_thumb.png)

[Ordinary Least Squares and Ridge Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html)

Ordinary Least Squares and Ridge Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_gpr_krr_thumb.png)

[Comparison of kernel ridge and Gaussian process regression](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html)

Comparison of kernel ridge and Gaussian process regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_agglomeration_vs_univariate_selection_thumb.png)

[Feature agglomeration vs. univariate selection](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html)

Feature agglomeration vs. univariate selection

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/9676f328f9e6c3e55f218a33cea5586f/plot_huber_vs_ridge.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c6a456b2390718e4dc79945608262e0b/plot_huber_vs_ridge.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/85657ba7194505e55a2b4b79bdf37ce4/plot_huber_vs_ridge.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_huber_vs_ridge.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_huber_vs_ridge.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)