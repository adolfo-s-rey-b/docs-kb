[Skip to main content](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/gaussian_process/plot_gpc.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/gaussian_process/plot_gpc.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/gaussian_process/plot_gpc.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/gaussian_process/plot_gpc.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/gaussian_process/plot_gpc.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/gaussian_process/plot_gpc.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc.html#sphx-glr-download-auto-examples-gaussian-process-plot-gpc-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Probabilistic predictions with Gaussian process classification (GPC)[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc.html#probabilistic-predictions-with-gaussian-process-classification-gpc "Link to this heading")

================================================================================================================================================================================================================================================

This example illustrates the predicted probability of GPC for an RBF kernel with different choices of the hyperparameters. The first figure shows the predicted probability of GPC with arbitrarily chosen hyperparameters and with the hyperparameters corresponding to the maximum log-marginal-likelihood (LML).

While the hyperparameters chosen by optimizing LML have a considerable larger LML, they perform slightly worse according to the log-loss on test data. The figure shows that this is because they exhibit a steep change of the class probabilities at the class boundaries (which is good) but have predicted probabilities close to 0.5 far away from the class boundaries (which is bad) This undesirable effect is caused by the Laplace approximation used internally by GPC.

The second figure shows the log-marginal-likelihood for different choices of the kernel’s hyperparameters, highlighting the two choices of the hyperparameters used in the first figure by black dots.

*   ![plot gpc](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_001.png)
*   ![Log-marginal-likelihood](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_002.png)

Log Marginal Likelihood (initial): -17.598
Log Marginal Likelihood (optimized): -3.875
Accuracy: 1.000 (initial) 1.000 (optimized)
Log-loss: 0.214 (initial) 0.319 (optimized)

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import numpy as np
from matplotlib import pyplot as plt

from sklearn.gaussian\_process import [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
from sklearn.gaussian\_process.kernels import [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
from sklearn.metrics import [accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
, [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")

\# Generate data
train\_size \= 50
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
X \= rng.uniform(0, 5, 100)\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
y \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(X\[:, 0\] \> 2.5, dtype\=int)

\# Specify Gaussian Processes with fixed and optimized hyperparameters
gp\_fix \= [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
(kernel\=1.0 \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
(length\_scale\=1.0), optimizer\=None)
gp\_fix.fit(X\[:train\_size\], y\[:train\_size\])

gp\_opt \= [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
(kernel\=1.0 \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
(length\_scale\=1.0))
gp\_opt.fit(X\[:train\_size\], y\[:train\_size\])

print(
    "Log Marginal Likelihood (initial): %.3f"
    % gp\_fix.log\_marginal\_likelihood(gp\_fix.kernel\_.theta)
)
print(
    "Log Marginal Likelihood (optimized): %.3f"
    % gp\_opt.log\_marginal\_likelihood(gp\_opt.kernel\_.theta)
)

print(
    "Accuracy: %.3f (initial) %.3f (optimized)"
    % (
        [accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
(y\[:train\_size\], gp\_fix.predict(X\[:train\_size\])),
        [accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
(y\[:train\_size\], gp\_opt.predict(X\[:train\_size\])),
    )
)
print(
    "Log-loss: %.3f (initial) %.3f (optimized)"
    % (
        [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
(y\[:train\_size\], gp\_fix.predict\_proba(X\[:train\_size\])\[:, 1\]),
        [log\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
(y\[:train\_size\], gp\_opt.predict\_proba(X\[:train\_size\])\[:, 1\]),
    )
)

\# Plot posteriors
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    X\[:train\_size, 0\], y\[:train\_size\], c\="k", label\="Train data", edgecolors\=(0, 0, 0)
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    X\[train\_size:, 0\], y\[train\_size:\], c\="g", label\="Test data", edgecolors\=(0, 0, 0)
)
X\_ \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 5, 100)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    X\_,
    gp\_fix.predict\_proba(X\_\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\])\[:, 1\],
    "r",
    label\="Initial kernel: %s" % gp\_fix.kernel\_,
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    X\_,
    gp\_opt.predict\_proba(X\_\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\])\[:, 1\],
    "b",
    label\="Optimized kernel: %s" % gp\_opt.kernel\_,
)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Feature")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Class 1 probability")
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(0, 5)
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(\-0.25, 1.5)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="best")

\# Plot LML landscape
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
theta0 \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(0, 8, 30)
theta1 \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-1, 1, 29)
Theta0, Theta1 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(theta0, theta1)
LML \= \[\
    \[\
        gp\_opt.log\_marginal\_likelihood([np.log](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")\
(\[Theta0\[i, j\], Theta1\[i, j\]\]))\
        for i in range(Theta0.shape\[0\])\
    \]\
    for j in range(Theta0.shape\[1\])\
\]
LML \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(LML).T
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(gp\_fix.kernel\_.theta)\[0\], [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(gp\_fix.kernel\_.theta)\[1\], "ko", zorder\=10
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(gp\_opt.kernel\_.theta)\[0\], [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(gp\_opt.kernel\_.theta)\[1\], "ko", zorder\=10
)
[plt.pcolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolor.html#matplotlib.pyplot.pcolor "matplotlib.pyplot.pcolor")
(Theta0, Theta1, LML)
[plt.xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xscale.html#matplotlib.pyplot.xscale "matplotlib.pyplot.xscale")
("log")
[plt.yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html#matplotlib.pyplot.yscale "matplotlib.pyplot.yscale")
("log")
[plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Magnitude")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Length-scale")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Log-marginal-likelihood")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 2.038 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpc.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpc.ipynb)

[`Download Jupyter notebook: plot_gpc.ipynb`](https://scikit-learn.org/stable/_downloads/60bf71ece62c4a5b5fe3e40007de265b/plot_gpc.ipynb)

[`Download Python source code: plot_gpc.py`](https://scikit-learn.org/stable/_downloads/a4394ee28b22f6d8930db11a3e185ba8/plot_gpc.py)

[`Download zipped: plot_gpc.zip`](https://scikit-learn.org/stable/_downloads/dc6079cc1c70df637397032629974c2c/plot_gpc.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_thumb.png)

[Ability of Gaussian process regression (GPR) to estimate data noise-level](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy.html)

Ability of Gaussian process regression (GPR) to estimate data noise-level

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_xor_thumb.png)

[Illustration of Gaussian process classification (GPC) on the XOR dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html)

Illustration of Gaussian process classification (GPC) on the XOR dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_scale_c_thumb.png)

[Scaling the regularization parameter for SVCs](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html)

Scaling the regularization parameter for SVCs

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_iris_thumb.png)

[Gaussian process classification (GPC) on iris dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html)

Gaussian process classification (GPC) on iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/a4394ee28b22f6d8930db11a3e185ba8/plot_gpc.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/60bf71ece62c4a5b5fe3e40007de265b/plot_gpc.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/dc6079cc1c70df637397032629974c2c/plot_gpc.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpc.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpc.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)