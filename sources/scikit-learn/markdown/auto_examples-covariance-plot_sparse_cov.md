[Skip to main content](https://scikit-learn.org/stable/auto_examples/covariance/plot_sparse_cov.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/covariance/plot_sparse_cov.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/covariance/plot_sparse_cov.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/covariance/plot_sparse_cov.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/covariance/plot_sparse_cov.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/covariance/plot_sparse_cov.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/covariance/plot_sparse_cov.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/covariance/plot_sparse_cov.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/covariance/plot_sparse_cov.html#sphx-glr-download-auto-examples-covariance-plot-sparse-cov-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Sparse inverse covariance estimation[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_sparse_cov.html#sparse-inverse-covariance-estimation "Link to this heading")

===================================================================================================================================================================================

Using the GraphicalLasso estimator to learn a covariance and sparse precision from a small number of samples.

To estimate a probabilistic model (e.g. a Gaussian model), estimating the precision matrix, that is the inverse covariance matrix, is as important as estimating the covariance matrix. Indeed a Gaussian model is parametrized by the precision matrix.

To be in favorable recovery conditions, we sample the data from a model with a sparse inverse covariance matrix. In addition, we ensure that the data is not too much correlated (limiting the largest coefficient of the precision matrix) and that there a no small coefficients in the precision matrix that cannot be recovered. In addition, with a small number of observations, it is easier to recover a correlation matrix rather than a covariance, thus we scale the time series.

Here, the number of samples is slightly larger than the number of dimensions, thus the empirical covariance is still invertible. However, as the observations are strongly correlated, the empirical covariance matrix is ill-conditioned and as a result its inverse –the empirical precision matrix– is very far from the ground truth.

If we use l2 shrinkage, as with the Ledoit-Wolf estimator, as the number of samples is small, we need to shrink a lot. As a result, the Ledoit-Wolf precision is fairly close to the ground truth precision, that is not far from being diagonal, but the off-diagonal structure is lost.

The l1-penalized estimator can recover part of this off-diagonal structure. It learns a sparse precision. It is not able to recover the exact sparsity pattern: it detects too many non-zero coefficients. However, the highest non-zero coefficients of the l1 estimated correspond to the non-zero coefficients in the ground truth. Finally, the coefficients of the l1 precision estimate are biased toward zero: because of the penalty, they are all smaller than the corresponding ground truth value, as can be seen on the figure.

Note that, the color range of the precision matrices is tweaked to improve readability of the figure. The full range of values of the empirical precision is not displayed.

The alpha parameter of the GraphicalLasso setting the sparsity of the model is set by internal cross-validation in the GraphicalLassoCV. As can be seen on figure 2, the grid to compute the cross-validation score is iteratively refined in the neighborhood of the maximum.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate the data[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_sparse_cov.html#generate-the-data "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np
from scipy import linalg

from sklearn.datasets import [make\_sparse\_spd\_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html#sklearn.datasets.make_sparse_spd_matrix "sklearn.datasets.make_sparse_spd_matrix")

n\_samples \= 60
n\_features \= 20

prng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(1)
prec \= [make\_sparse\_spd\_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html#sklearn.datasets.make_sparse_spd_matrix "sklearn.datasets.make_sparse_spd_matrix")
(
    n\_features, alpha\=0.98, smallest\_coef\=0.4, largest\_coef\=0.7, random\_state\=prng
)
cov \= [linalg.inv](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html#scipy.linalg.inv "scipy.linalg.inv")
(prec)
d \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
([np.diag](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")
(cov))
cov /= d
cov /= d\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
prec \*= d
prec \*= d\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
X \= prng.multivariate\_normal([np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(n\_features), cov, size\=n\_samples)
X \-= X.mean(axis\=0)
X /= X.std(axis\=0)

Copy to clipboard

Estimate the covariance[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_sparse_cov.html#estimate-the-covariance "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.covariance import [GraphicalLassoCV](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")
, [ledoit\_wolf](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf.html#sklearn.covariance.ledoit_wolf "sklearn.covariance.ledoit_wolf")

emp\_cov \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(X.T, X) / n\_samples

model \= [GraphicalLassoCV](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")
()
model.fit(X)
cov\_ \= model.covariance\_
prec\_ \= model.precision\_

lw\_cov\_, \_ \= [ledoit\_wolf](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf.html#sklearn.covariance.ledoit_wolf "sklearn.covariance.ledoit_wolf")
(X)
lw\_prec\_ \= [linalg.inv](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html#scipy.linalg.inv "scipy.linalg.inv")
(lw\_cov\_)

Copy to clipboard

Plot the results[#](https://scikit-learn.org/stable/auto_examples/covariance/plot_sparse_cov.html#plot-the-results "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 6))
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(left\=0.02, right\=0.98)

\# plot the covariances
covs \= \[\
    ("Empirical", emp\_cov),\
    ("Ledoit-Wolf", lw\_cov\_),\
    ("GraphicalLassoCV", cov\_),\
    ("True", cov),\
\]
vmax \= cov\_.max()
for i, (name, this\_cov) in enumerate(covs):
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 4, i + 1)
    [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(
        this\_cov, interpolation\="nearest", vmin\=-vmax, vmax\=vmax, cmap\=plt.cm.RdBu\_r
    )
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("%s covariance" % name)

\# plot the precisions
precs \= \[\
    ("Empirical", [linalg.inv](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html#scipy.linalg.inv "scipy.linalg.inv")\
(emp\_cov)),\
    ("Ledoit-Wolf", lw\_prec\_),\
    ("GraphicalLasso", prec\_),\
    ("True", prec),\
\]
vmax \= 0.9 \* prec\_.max()
for i, (name, this\_prec) in enumerate(precs):
    ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 4, i + 5)
    [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(
        [np.ma.masked\_equal](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_equal.html#numpy.ma.masked_equal "numpy.ma.masked_equal")
(this\_prec, 0),
        interpolation\="nearest",
        vmin\=-vmax,
        vmax\=vmax,
        cmap\=plt.cm.RdBu\_r,
    )
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("%s precision" % name)
    if hasattr(ax, "set\_facecolor"):
        ax.set\_facecolor(".7")
    else:
        ax.set\_axis\_bgcolor(".7")

Copy to clipboard

![Empirical covariance, Ledoit-Wolf covariance, GraphicalLassoCV covariance, True covariance, Empirical precision, Ledoit-Wolf precision, GraphicalLasso precision, True precision](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_cov_001.png)

\# plot the model selection metric
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(4, 3))
[plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
(\[0.2, 0.15, 0.75, 0.7\])
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(model.cv\_results\_\["alphas"\], model.cv\_results\_\["mean\_test\_score"\], "o-")
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")
(model.alpha\_, color\=".5")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Model selection")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Cross-validation score")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("alpha")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Model selection](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_cov_002.png)

**Total running time of the script:** (0 minutes 0.628 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo7.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/covariance/plot_sparse_cov.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo7.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/covariance/plot_sparse_cov.ipynb)

[`Download Jupyter notebook: plot_sparse_cov.ipynb`](https://scikit-learn.org/stable/_downloads/493307eb257cfb3d4e056ee73a41842e/plot_sparse_cov.ipynb)

[`Download Python source code: plot_sparse_cov.py`](https://scikit-learn.org/stable/_downloads/ef716d06d01e43235aa0be61f66bd68d/plot_sparse_cov.py)

[`Download zipped: plot_sparse_cov.zip`](https://scikit-learn.org/stable/_downloads/a32d6321e82346eded216e3c68f044c6/plot_sparse_cov.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_thumb.png)

[Precision-Recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

Precision-Recall

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_covariance_estimation_thumb.png)

[Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood](https://scikit-learn.org/stable/auto_examples/covariance/plot_covariance_estimation.html)

Shrinkage covariance estimation: LedoitWolf vs OAS and max-likelihood

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_qda_thumb.png)

[Linear and Quadratic Discriminant Analysis with covariance ellipsoid](https://scikit-learn.org/stable/auto_examples/classification/plot_lda_qda.html)

Linear and Quadratic Discriminant Analysis with covariance ellipsoid

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lw_vs_oas_thumb.png)

[Ledoit-Wolf vs OAS estimation](https://scikit-learn.org/stable/auto_examples/covariance/plot_lw_vs_oas.html)

Ledoit-Wolf vs OAS estimation

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/ef716d06d01e43235aa0be61f66bd68d/plot_sparse_cov.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/493307eb257cfb3d4e056ee73a41842e/plot_sparse_cov.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/a32d6321e82346eded216e3c68f044c6/plot_sparse_cov.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo7.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/covariance/plot_sparse_cov.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo7.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/covariance/plot_sparse_cov.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)