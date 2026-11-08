[Skip to main content](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_isoprobability.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/gaussian_process/plot_gpc_isoprobability.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_isoprobability.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/gaussian_process/plot_gpc_isoprobability.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/gaussian_process/plot_gpc_isoprobability.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/gaussian_process/plot_gpc_isoprobability.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/gaussian_process/plot_gpc_isoprobability.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/gaussian_process/plot_gpc_isoprobability.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_isoprobability.html#sphx-glr-download-auto-examples-gaussian-process-plot-gpc-isoprobability-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Iso-probability lines for Gaussian Processes classification (GPC)[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_isoprobability.html#iso-probability-lines-for-gaussian-processes-classification-gpc "Link to this heading")

=========================================================================================================================================================================================================================================================

A two-dimensional classification example showing iso-probability lines for the predicted probabilities.

![plot gpc isoprobability](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_isoprobability_001.png)

Learned kernel: 0.0256\*\*2 \* DotProduct(sigma\_0=5.72) \*\* 2

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt

from sklearn.gaussian\_process import [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
from sklearn.gaussian\_process.kernels import ConstantKernel as [C](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ConstantKernel.html#sklearn.gaussian_process.kernels.ConstantKernel "sklearn.gaussian_process.kernels.ConstantKernel")
from sklearn.gaussian\_process.kernels import [DotProduct](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct "sklearn.gaussian_process.kernels.DotProduct")

\# A few constants
lim \= 8

def g(x):
    """The function to predict (classification will then consist in predicting
    whether g(x) <= 0 or not)"""
    return 5.0 \- x\[:, 1\] \- 0.5 \* x\[:, 0\] \*\* 2.0

\# Design of experiments
X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(
    \[\
        \[\-4.61611719, \-6.00099547\],\
        \[4.10469096, 5.32782448\],\
        \[0.00000000, \-0.50000000\],\
        \[\-6.17289014, \-4.6984743\],\
        \[1.3109306, \-6.93271427\],\
        \[\-5.03823144, 3.10584743\],\
        \[\-2.87600388, 6.74310541\],\
        \[5.21301203, 4.26386883\],\
    \]
)

\# Observations
y \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(g(X) \> 0, dtype\=int)

\# Instantiate and fit Gaussian Process Model
kernel \= [C](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ConstantKernel.html#sklearn.gaussian_process.kernels.ConstantKernel "sklearn.gaussian_process.kernels.ConstantKernel")
(0.1, (1e-5, [np.inf](https://numpy.org/doc/stable/reference/constants.html#numpy.inf "numpy.inf")
)) \* [DotProduct](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct "sklearn.gaussian_process.kernels.DotProduct")
(sigma\_0\=0.1) \*\* 2
gp \= [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
(kernel\=kernel)
gp.fit(X, y)
print("Learned kernel: %s " % gp.kernel\_)

\# Evaluate real function and the predicted probability
res \= 50
x1, x2 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-lim, lim, res), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-lim, lim, res))
xx \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(\[x1.reshape(x1.size), x2.reshape(x2.size)\]).T

y\_true \= g(xx)
y\_prob \= gp.predict\_proba(xx)\[:, 1\]
y\_true \= y\_true.reshape((res, res))
y\_prob \= y\_prob.reshape((res, res))

\# Plot the probabilistic classification iso-values
fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(1)
ax \= fig.gca()
ax.axes.set\_aspect("equal")
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(\[\])
[plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(\[\])
ax.set\_xticklabels(\[\])
ax.set\_yticklabels(\[\])
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("$x\_1$")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("$x\_2$")

cax \= [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(y\_prob, cmap\=cm.gray\_r, alpha\=0.8, extent\=(\-lim, lim, \-lim, lim))
norm \= plt.matplotlib.colors.Normalize(vmin\=0.0, vmax\=0.9)
cb \= [plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
(cax, ticks\=\[0.0, 0.2, 0.4, 0.6, 0.8, 1.0\], norm\=norm)
cb.set\_label(r"${\\rm \\mathbb{P}}\\left\[\\widehat{G}(\\mathbf{x}) \\leq 0\\right\]$")
[plt.clim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clim.html#matplotlib.pyplot.clim "matplotlib.pyplot.clim")
(0, 1)

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\[y <= 0, 0\], X\[y <= 0, 1\], "r.", markersize\=12)

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\[y \> 0, 0\], X\[y \> 0, 1\], "b.", markersize\=12)

[plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(x1, x2, y\_true, \[0.0\], colors\="k", linestyles\="dashdot")

cs \= [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(x1, x2, y\_prob, \[0.666\], colors\="b", linestyles\="solid")
[plt.clabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html#matplotlib.pyplot.clabel "matplotlib.pyplot.clabel")
(cs, fontsize\=11)

cs \= [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(x1, x2, y\_prob, \[0.5\], colors\="k", linestyles\="dashed")
[plt.clabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html#matplotlib.pyplot.clabel "matplotlib.pyplot.clabel")
(cs, fontsize\=11)

cs \= [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(x1, x2, y\_prob, \[0.334\], colors\="r", linestyles\="solid")
[plt.clabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html#matplotlib.pyplot.clabel "matplotlib.pyplot.clabel")
(cs, fontsize\=11)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.123 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpc_isoprobability.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpc_isoprobability.ipynb)

[`Download Jupyter notebook: plot_gpc_isoprobability.ipynb`](https://scikit-learn.org/stable/_downloads/f927b32733adb25c5c8208225278f50c/plot_gpc_isoprobability.ipynb)

[`Download Python source code: plot_gpc_isoprobability.py`](https://scikit-learn.org/stable/_downloads/e071b915e9660d5d0bb53ca12695c133/plot_gpc_isoprobability.py)

[`Download zipped: plot_gpc_isoprobability.zip`](https://scikit-learn.org/stable/_downloads/45165f5550aea2cda6696d5586546067/plot_gpc_isoprobability.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_separating_hyperplane_thumb.png)

[SGD: Maximum margin separating hyperplane](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_separating_hyperplane.html)

SGD: Maximum margin separating hyperplane

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_twoclass_thumb.png)

[Two-class AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_twoclass.html)

Two-class AdaBoost

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_xor_thumb.png)

[Illustration of Gaussian process classification (GPC) on the XOR dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html)

Illustration of Gaussian process classification (GPC) on the XOR dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_pdf_thumb.png)

[Density Estimation for a Gaussian mixture](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_pdf.html)

Density Estimation for a Gaussian mixture

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/e071b915e9660d5d0bb53ca12695c133/plot_gpc_isoprobability.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f927b32733adb25c5c8208225278f50c/plot_gpc_isoprobability.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/45165f5550aea2cda6696d5586546067/plot_gpc_isoprobability.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpc_isoprobability.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpc_isoprobability.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)