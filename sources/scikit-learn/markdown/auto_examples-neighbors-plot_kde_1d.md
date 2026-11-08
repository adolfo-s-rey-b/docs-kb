[Skip to main content](https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neighbors/plot_kde_1d.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neighbors/plot_kde_1d.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neighbors/plot_kde_1d.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neighbors/plot_kde_1d.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neighbors/plot_kde_1d.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neighbors/plot_kde_1d.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html#sphx-glr-download-auto-examples-neighbors-plot-kde-1d-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Simple 1D Kernel Density Estimation[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html#simple-1d-kernel-density-estimation "Link to this heading")

============================================================================================================================================================================

This example uses the [`KernelDensity`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
 class to demonstrate the principles of Kernel Density Estimation in one dimension.

The first plot shows one of the problems with using histograms to visualize the density of points in 1D. Intuitively, a histogram can be thought of as a scheme in which a unit “block” is stacked above each point on a regular grid. As the top two panels show, however, the choice of gridding for these blocks can lead to wildly divergent ideas about the underlying shape of the density distribution. If we instead center each block on the point it represents, we get the estimate shown in the bottom left panel. This is a kernel density estimation with a “top hat” kernel. This idea can be generalized to other kernel shapes: the bottom-right panel of the first figure shows a Gaussian kernel density estimate over the same distribution.

Scikit-learn implements efficient kernel density estimation using either a Ball Tree or KD Tree structure, through the [`KernelDensity`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
 estimator. The available kernels are shown in the second figure of this example.

The third figure compares kernel density estimates for a distribution of 100 samples in 1 dimension. Though this example uses 1D distributions, kernel density estimation is easily and efficiently extensible to higher dimensions as well.

*   ![plot kde 1d](https://scikit-learn.org/stable/_images/sphx_glr_plot_kde_1d_001.png)
*   ![Available Kernels](https://scikit-learn.org/stable/_images/sphx_glr_plot_kde_1d_002.png)
*   ![plot kde 1d](https://scikit-learn.org/stable/_images/sphx_glr_plot_kde_1d_003.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import [norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html#scipy.stats.norm "scipy.stats.norm")

from sklearn.neighbors import [KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")

\# ----------------------------------------------------------------------
\# Plot the progression of histograms to kernels
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(1)
N \= 20
X \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(
    ([np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(0, 1, int(0.3 \* N)), [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(5, 1, int(0.7 \* N)))
)\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
X\_plot \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-5, 10, 1000)\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
bins \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-5, 10, 10)

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, sharex\=True, sharey\=True)
fig.subplots\_adjust(hspace\=0.05, wspace\=0.05)

\# histogram 1
ax\[0, 0\].hist(X\[:, 0\], bins\=bins, fc\="#AAAAFF", density\=True)
ax\[0, 0\].text(\-3.5, 0.31, "Histogram")

\# histogram 2
ax\[0, 1\].hist(X\[:, 0\], bins\=bins + 0.75, fc\="#AAAAFF", density\=True)
ax\[0, 1\].text(\-3.5, 0.31, "Histogram, bins shifted")

\# tophat KDE
kde \= [KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
(kernel\="tophat", bandwidth\=0.75).fit(X)
log\_dens \= kde.score\_samples(X\_plot)
ax\[1, 0\].fill(X\_plot\[:, 0\], [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(log\_dens), fc\="#AAAAFF")
ax\[1, 0\].text(\-3.5, 0.31, "Tophat Kernel Density")

\# Gaussian KDE
kde \= [KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
(kernel\="gaussian", bandwidth\=0.75).fit(X)
log\_dens \= kde.score\_samples(X\_plot)
ax\[1, 1\].fill(X\_plot\[:, 0\], [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(log\_dens), fc\="#AAAAFF")
ax\[1, 1\].text(\-3.5, 0.31, "Gaussian Kernel Density")

for axi in ax.ravel():
    axi.plot(X\[:, 0\], [np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
(X.shape\[0\], \-0.01), "+k")
    axi.set\_xlim(\-4, 9)
    axi.set\_ylim(\-0.02, 0.34)

for axi in ax\[:, 0\]:
    axi.set\_ylabel("Normalized Density")

for axi in ax\[1, :\]:
    axi.set\_xlabel("x")

\# ----------------------------------------------------------------------
\# Plot all available kernels
X\_plot \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-6, 6, 1000)\[:, None\]
X\_src \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((1, 1))

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 3, sharex\=True, sharey\=True)
fig.subplots\_adjust(left\=0.05, right\=0.95, hspace\=0.05, wspace\=0.05)

def format\_func(x, loc):
    if x \== 0:
        return "0"
    elif x \== 1:
        return "h"
    elif x \== \-1:
        return "-h"
    else:
        return "%ih" % x

for i, kernel in enumerate(
    \["gaussian", "tophat", "epanechnikov", "exponential", "linear", "cosine"\]
):
    axi \= ax.ravel()\[i\]
    log\_dens \= [KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
(kernel\=kernel).fit(X\_src).score\_samples(X\_plot)
    axi.fill(X\_plot\[:, 0\], [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(log\_dens), "-k", fc\="#AAAAFF")
    axi.text(\-2.6, 0.95, kernel)

    axi.xaxis.set\_major\_formatter(plt.FuncFormatter(format\_func))
    axi.xaxis.set\_major\_locator(plt.MultipleLocator(1))
    axi.yaxis.set\_major\_locator(plt.NullLocator())

    axi.set\_ylim(0, 1.05)
    axi.set\_xlim(\-2.9, 2.9)

ax\[0, 1\].set\_title("Available Kernels")

\# ----------------------------------------------------------------------
\# Plot a 1D density example
N \= 100
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(1)
X \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(
    ([np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(0, 1, int(0.3 \* N)), [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(5, 1, int(0.7 \* N)))
)\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]

X\_plot \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-5, 10, 1000)\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]

true\_dens \= 0.3 \* [norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html#scipy.stats.norm "scipy.stats.norm")
(0, 1).pdf(X\_plot\[:, 0\]) + 0.7 \* [norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html#scipy.stats.norm "scipy.stats.norm")
(5, 1).pdf(X\_plot\[:, 0\])

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
ax.fill(X\_plot\[:, 0\], true\_dens, fc\="black", alpha\=0.2, label\="input distribution")
colors \= \["navy", "cornflowerblue", "darkorange"\]
kernels \= \["gaussian", "tophat", "epanechnikov"\]
lw \= 2

for color, kernel in zip(colors, kernels):
    kde \= [KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
(kernel\=kernel, bandwidth\=0.5).fit(X)
    log\_dens \= kde.score\_samples(X\_plot)
    ax.plot(
        X\_plot\[:, 0\],
        [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(log\_dens),
        color\=color,
        lw\=lw,
        linestyle\="-",
        label\="kernel = '{0}'".format(kernel),
    )

ax.text(6, 0.38, "N={0} points".format(N))

ax.legend(loc\="upper left")
ax.plot(X\[:, 0\], \-0.005 \- 0.01 \* [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
(X.shape\[0\]), "+k")

ax.set\_xlim(\-4, 9)
ax.set\_ylim(\-0.02, 0.4)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.507 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_kde_1d.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_kde_1d.ipynb)

[`Download Jupyter notebook: plot_kde_1d.ipynb`](https://scikit-learn.org/stable/_downloads/7c2f454ae53819802ecec0f2cacd6d51/plot_kde_1d.ipynb)

[`Download Python source code: plot_kde_1d.py`](https://scikit-learn.org/stable/_downloads/8c65925beb12265775bcceee8e0aa90b/plot_kde_1d.py)

[`Download zipped: plot_kde_1d.zip`](https://scikit-learn.org/stable/_downloads/f5437b9b38b73a00640f05b987811126/plot_kde_1d.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_kde_sampling_thumb.png)

[Kernel Density Estimation](https://scikit-learn.org/stable/auto_examples/neighbors/plot_digits_kde_sampling.html)

Kernel Density Estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ard_thumb.png)

[Comparing Linear Bayesian Regressors](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html)

Comparing Linear Bayesian Regressors

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_quantile_thumb.png)

[Prediction Intervals for Gradient Boosting Regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html)

Prediction Intervals for Gradient Boosting Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_thumb.png)

[Importance of Feature Scaling](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html)

Importance of Feature Scaling

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/8c65925beb12265775bcceee8e0aa90b/plot_kde_1d.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/7c2f454ae53819802ecec0f2cacd6d51/plot_kde_1d.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/f5437b9b38b73a00640f05b987811126/plot_kde_1d.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_kde_1d.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_kde_1d.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)