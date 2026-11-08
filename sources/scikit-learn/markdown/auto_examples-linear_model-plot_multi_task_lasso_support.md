[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_multi_task_lasso_support.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_multi_task_lasso_support.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_multi_task_lasso_support.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_multi_task_lasso_support.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_multi_task_lasso_support.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_multi_task_lasso_support.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html#sphx-glr-download-auto-examples-linear-model-plot-multi-task-lasso-support-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Joint feature selection with multi-task Lasso[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html#joint-feature-selection-with-multi-task-lasso "Link to this heading")

=====================================================================================================================================================================================================================

The multi-task lasso allows to fit multiple regression problems jointly enforcing the selected features to be the same across tasks. This example simulates sequential measurements, each task is a time instant, and the relevant features vary in amplitude over time while being the same. The multi-task lasso imposes that features that are selected at one time point are select for all time point. This makes feature selection by the Lasso more stable.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate data[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html#generate-data "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)

\# Generate some 2D coefficients with sine waves with random frequency and phase
n\_samples, n\_features, n\_tasks \= 100, 30, 40
n\_relevant\_features \= 5
coef \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((n\_tasks, n\_features))
times \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
, n\_tasks)
for k in range(n\_relevant\_features):
    coef\[:, k\] \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
((1.0 + rng.randn(1)) \* times + 3 \* rng.randn(1))

X \= rng.randn(n\_samples, n\_features)
Y \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(X, coef.T) + rng.randn(n\_samples, n\_tasks)

Copy to clipboard

Fit models[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html#fit-models "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.linear\_model import [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
, [MultiTaskLasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model.MultiTaskLasso")

coef\_lasso\_ \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[[Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")\
(alpha\=0.5).fit(X, y).coef\_ for y in Y.T\])
coef\_multi\_task\_lasso\_ \= [MultiTaskLasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model.MultiTaskLasso")
(alpha\=1.0).fit(X, Y).coef\_

Copy to clipboard

Plot support and time series[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html#plot-support-and-time-series "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 5))
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 2, 1)
[plt.spy](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.spy.html#matplotlib.pyplot.spy "matplotlib.pyplot.spy")
(coef\_lasso\_)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Feature")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Time (or Task)")
[plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(10, 5, "Lasso")
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 2, 2)
[plt.spy](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.spy.html#matplotlib.pyplot.spy "matplotlib.pyplot.spy")
(coef\_multi\_task\_lasso\_)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Feature")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Time (or Task)")
[plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(10, 5, "MultiTaskLasso")
fig.suptitle("Coefficient non-zero location")

feature\_to\_plot \= 0
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
lw \= 2
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(coef\[:, feature\_to\_plot\], color\="seagreen", linewidth\=lw, label\="Ground truth")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    coef\_lasso\_\[:, feature\_to\_plot\], color\="cornflowerblue", linewidth\=lw, label\="Lasso"
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    coef\_multi\_task\_lasso\_\[:, feature\_to\_plot\],
    color\="gold",
    linewidth\=lw,
    label\="MultiTaskLasso",
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper center")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(\[\-1.1, 1.1\])
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

*   ![Coefficient non-zero location](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_task_lasso_support_001.png)
*   ![plot multi task lasso support](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_task_lasso_support_002.png)

**Total running time of the script:** (0 minutes 0.268 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_multi_task_lasso_support.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_multi_task_lasso_support.ipynb)

[`Download Jupyter notebook: plot_multi_task_lasso_support.ipynb`](https://scikit-learn.org/stable/_downloads/f1a137ac46ba39a9ac507c515d184d90/plot_multi_task_lasso_support.ipynb)

[`Download Python source code: plot_multi_task_lasso_support.py`](https://scikit-learn.org/stable/_downloads/2f0720ee8bdf39051b71d0070814a47b/plot_multi_task_lasso_support.py)

[`Download zipped: plot_multi_task_lasso_support.zip`](https://scikit-learn.org/stable/_downloads/8f282611d5fe24935e33b3c53d30ab1b/plot_multi_task_lasso_support.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_thumb.png)

[L1-based models for Sparse Signals](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html)

L1-based models for Sparse Signals

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_dense_vs_sparse_data_thumb.png)

[Lasso on dense and sparse data](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html)

Lasso on dense and sparse data

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lasso_lars_elasticnet_path_thumb.png)

[Lasso, Lasso-LARS, and Elastic Net paths](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)

Lasso, Lasso-LARS, and Elastic Net paths

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_model_selection_thumb.png)

[Lasso model selection: AIC-BIC / cross-validation](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html)

Lasso model selection: AIC-BIC / cross-validation

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/2f0720ee8bdf39051b71d0070814a47b/plot_multi_task_lasso_support.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f1a137ac46ba39a9ac507c515d184d90/plot_multi_task_lasso_support.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/8f282611d5fe24935e33b3c53d30ab1b/plot_multi_task_lasso_support.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_multi_task_lasso_support.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_multi_task_lasso_support.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)