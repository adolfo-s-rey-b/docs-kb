[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html#sphx-glr-download-auto-examples-linear-model-plot-lasso-lasso-lars-elasticnet-path-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Lasso, Lasso-LARS, and Elastic Net paths[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.html#lasso-lasso-lars-and-elastic-net-paths "Link to this heading")

=================================================================================================================================================================================================================

This example shows how to compute the “paths” of coefficients along the Lasso, Lasso-LARS, and Elastic Net regularization paths. In other words, it shows the relationship between the regularization parameter (alpha) and the coefficients.

Lasso and Lasso-LARS impose a sparsity constraint on the coefficients, encouraging some of them to be zero. Elastic Net is a generalization of Lasso that adds an L2 penalty term to the L1 penalty term. This allows for some coefficients to be non-zero while still encouraging sparsity.

Lasso and Elastic Net use a coordinate descent method to compute the paths, while Lasso-LARS uses the LARS algorithm to compute the paths.

The paths are computed using [`lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")
, [`lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")
, and [`enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
.

The results show different comparison plots:

*   Compare Lasso and Lasso-LARS
    
*   Compare Lasso and Elastic Net
    
*   Compare Lasso with positive Lasso
    
*   Compare LARS and Positive LARS
    
*   Compare Elastic Net and positive Elastic Net
    

Each plot shows how the model coefficients vary as the regularization strength changes, offering insight into the behavior of these models under different constraints.

*   ![Lasso and LARS Paths](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lasso_lars_elasticnet_path_001.png)
*   ![Lasso and Elastic-Net Paths](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lasso_lars_elasticnet_path_002.png)
*   ![Lasso and positive Lasso](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lasso_lars_elasticnet_path_003.png)
*   ![LARS and Positive LARS](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lasso_lars_elasticnet_path_004.png)
*   ![Elastic-Net and positive Elastic-Net](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_lasso_lars_elasticnet_path_005.png)

Computing regularization path using the lasso...
Computing regularization path using the positive lasso...
Computing regularization path using the LARS...
Computing regularization path using the positive LARS...
Computing regularization path using the elastic net...
Computing regularization path using the positive elastic net...

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

from itertools import [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle")

import matplotlib.pyplot as plt

from sklearn.datasets import [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
from sklearn.linear\_model import [enet\_path](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
, [lars\_path](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")
, [lasso\_path](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")

X, y \= [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
(return\_X\_y\=True)
X /= X.std(axis\=0)  \# Standardize data (easier to set the l1\_ratio parameter)

\# Compute paths

eps \= 5e-3  \# the smaller it is the longer is the path

print("Computing regularization path using the lasso...")
alphas\_lasso, coefs\_lasso, \_ \= [lasso\_path](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")
(X, y, eps\=eps)

print("Computing regularization path using the positive lasso...")
alphas\_positive\_lasso, coefs\_positive\_lasso, \_ \= [lasso\_path](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")
(
    X, y, eps\=eps, positive\=True
)

print("Computing regularization path using the LARS...")
alphas\_lars, \_, coefs\_lars \= [lars\_path](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")
(X, y, method\="lasso")

print("Computing regularization path using the positive LARS...")
alphas\_positive\_lars, \_, coefs\_positive\_lars \= [lars\_path](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")
(
    X, y, method\="lasso", positive\=True
)

print("Computing regularization path using the elastic net...")
alphas\_enet, coefs\_enet, \_ \= [enet\_path](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
(X, y, eps\=eps, l1\_ratio\=0.8)

print("Computing regularization path using the positive elastic net...")
alphas\_positive\_enet, coefs\_positive\_enet, \_ \= [enet\_path](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
(
    X, y, eps\=eps, l1\_ratio\=0.8, positive\=True
)

\# Display results

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(1)
colors \= [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle")
(\["b", "r", "g", "c", "k"\])
for coef\_lasso, coef\_lars, c in zip(coefs\_lasso, coefs\_lars, colors):
    l1 \= [plt.semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx "matplotlib.pyplot.semilogx")
(alphas\_lasso, coef\_lasso, c\=c)
    l2 \= [plt.semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx "matplotlib.pyplot.semilogx")
(alphas\_lars, coef\_lars, linestyle\="--", c\=c)

[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("alpha")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("coefficients")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Lasso and LARS Paths")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
((l1\[\-1\], l2\[\-1\]), ("Lasso", "LARS"), loc\="lower right")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(2)
colors \= [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle")
(\["b", "r", "g", "c", "k"\])
for coef\_l, coef\_e, c in zip(coefs\_lasso, coefs\_enet, colors):
    l1 \= [plt.semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx "matplotlib.pyplot.semilogx")
(alphas\_lasso, coef\_l, c\=c)
    l2 \= [plt.semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx "matplotlib.pyplot.semilogx")
(alphas\_enet, coef\_e, linestyle\="--", c\=c)

[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("alpha")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("coefficients")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Lasso and Elastic-Net Paths")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
((l1\[\-1\], l2\[\-1\]), ("Lasso", "Elastic-Net"), loc\="lower right")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(3)
for coef\_l, coef\_pl, c in zip(coefs\_lasso, coefs\_positive\_lasso, colors):
    l1 \= [plt.semilogy](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogy.html#matplotlib.pyplot.semilogy "matplotlib.pyplot.semilogy")
(alphas\_lasso, coef\_l, c\=c)
    l2 \= [plt.semilogy](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogy.html#matplotlib.pyplot.semilogy "matplotlib.pyplot.semilogy")
(alphas\_positive\_lasso, coef\_pl, linestyle\="--", c\=c)

[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("alpha")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("coefficients")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Lasso and positive Lasso")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
((l1\[\-1\], l2\[\-1\]), ("Lasso", "positive Lasso"), loc\="lower right")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(4)
colors \= [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle")
(\["b", "r", "g", "c", "k"\])
for coef\_lars, coef\_positive\_lars, c in zip(coefs\_lars, coefs\_positive\_lars, colors):
    l1 \= [plt.semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx "matplotlib.pyplot.semilogx")
(alphas\_lars, coef\_lars, c\=c)
    l2 \= [plt.semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx "matplotlib.pyplot.semilogx")
(alphas\_positive\_lars, coef\_positive\_lars, linestyle\="--", c\=c)

[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("alpha")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("coefficients")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("LARS and Positive LARS")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
((l1\[\-1\], l2\[\-1\]), ("LARS", "Positive LARS"), loc\="lower right")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(5)
for coef\_e, coef\_pe, c in zip(coefs\_enet, coefs\_positive\_enet, colors):
    l1 \= [plt.semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx "matplotlib.pyplot.semilogx")
(alphas\_enet, coef\_e, c\=c)
    l2 \= [plt.semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx "matplotlib.pyplot.semilogx")
(alphas\_positive\_enet, coef\_pe, linestyle\="--", c\=c)

[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("alpha")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("coefficients")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Elastic-Net and positive Elastic-Net")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
((l1\[\-1\], l2\[\-1\]), ("Elastic-Net", "positive Elastic-Net"), loc\="lower right")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.738 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.ipynb)

[`Download Jupyter notebook: plot_lasso_lasso_lars_elasticnet_path.ipynb`](https://scikit-learn.org/stable/_downloads/1a643dc4b5b4cf8540a70446f140456f/plot_lasso_lasso_lars_elasticnet_path.ipynb)

[`Download Python source code: plot_lasso_lasso_lars_elasticnet_path.py`](https://scikit-learn.org/stable/_downloads/45f9e3fbbc43c4136c925352c2c5a632/plot_lasso_lasso_lars_elasticnet_path.py)

[`Download zipped: plot_lasso_lasso_lars_elasticnet_path.zip`](https://scikit-learn.org/stable/_downloads/74a474baa9f199005f835804a7281678/plot_lasso_lasso_lars_elasticnet_path.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_thumb.png)

[L1-based models for Sparse Signals](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html)

L1-based models for Sparse Signals

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_l1_l2_sparsity_thumb.png)

[L1 Penalty and Sparsity in Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_l1_l2_sparsity.html)

L1 Penalty and Sparsity in Logistic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_task_lasso_support_thumb.png)

[Joint feature selection with multi-task Lasso](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html)

Joint feature selection with multi-task Lasso

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_dense_vs_sparse_data_thumb.png)

[Lasso on dense and sparse data](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html)

Lasso on dense and sparse data

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/45f9e3fbbc43c4136c925352c2c5a632/plot_lasso_lasso_lars_elasticnet_path.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/1a643dc4b5b4cf8540a70446f140456f/plot_lasso_lasso_lars_elasticnet_path.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/74a474baa9f199005f835804a7281678/plot_lasso_lasso_lars_elasticnet_path.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_lasso_lasso_lars_elasticnet_path.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)