[Skip to main content](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/gaussian_process/plot_gpc_xor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/gaussian_process/plot_gpc_xor.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/gaussian_process/plot_gpc_xor.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/gaussian_process/plot_gpc_xor.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/gaussian_process/plot_gpc_xor.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/gaussian_process/plot_gpc_xor.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html#sphx-glr-download-auto-examples-gaussian-process-plot-gpc-xor-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Illustration of Gaussian process classification (GPC) on the XOR dataset[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html#illustration-of-gaussian-process-classification-gpc-on-the-xor-dataset "Link to this heading")

============================================================================================================================================================================================================================================================

This example illustrates GPC on XOR data. Compared are a stationary, isotropic kernel (RBF) and a non-stationary kernel (DotProduct). On this particular dataset, the DotProduct kernel obtains considerably better results because the class-boundaries are linear and coincide with the coordinate axes. In general, stationary kernels often obtain better results.

![302**2 * RBF(length_scale=1.55)  Log-Marginal-Likelihood:-24.237, 316**2 * DotProduct(sigma_0=0.0104) ** 2  Log-Marginal-Likelihood:-9.284](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_xor_001.png)

/home/circleci/project/sklearn/gaussian\_process/kernels.py:455: ConvergenceWarning: The optimal value found for dimension 0 of parameter k1\_\_constant\_value is close to the specified upper bound 100000.0. Increasing the bound and calling fit again may find a better value.
  warnings.warn(

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.gaussian\_process import [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
from sklearn.gaussian\_process.kernels import [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
, [DotProduct](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct "sklearn.gaussian_process.kernels.DotProduct")

xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-3, 3, 50), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-3, 3, 50))
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
X \= rng.randn(200, 2)
Y \= [np.logical\_xor](https://numpy.org/doc/stable/reference/generated/numpy.logical_xor.html#numpy.logical_xor "numpy.logical_xor")
(X\[:, 0\] \> 0, X\[:, 1\] \> 0)

\# fit the model
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 5))
kernels \= \[1.0 \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")\
(length\_scale\=1.15), 1.0 \* [DotProduct](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct "sklearn.gaussian_process.kernels.DotProduct")\
(sigma\_0\=1.0) \*\* 2\]
for i, kernel in enumerate(kernels):
    clf \= [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
(kernel\=kernel, warm\_start\=True).fit(X, Y)

    \# plot the decision function for each datapoint on the grid
    Z \= clf.predict\_proba([np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
((xx.ravel(), yy.ravel())).T)\[:, 1\]
    Z \= Z.reshape(xx.shape)

    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 2, i + 1)
    image \= [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(
        Z,
        interpolation\="nearest",
        extent\=(xx.min(), xx.max(), yy.min(), yy.max()),
        aspect\="auto",
        origin\="lower",
        cmap\=plt.cm.PuOr\_r,
    )
    contours \= [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(xx, yy, Z, levels\=\[0.5\], linewidths\=2, colors\=\["k"\])
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], s\=30, c\=Y, cmap\=plt.cm.Paired, edgecolors\=(0, 0, 0))
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
    [plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
(\[\-3, 3, \-3, 3\])
    [plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
(image)
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
        "%s\\n Log-Marginal-Likelihood:%.3f"
        % (clf.kernel\_, clf.log\_marginal\_likelihood(clf.kernel\_.theta)),
        fontsize\=12,
    )

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.363 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpc_xor.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpc_xor.ipynb)

[`Download Jupyter notebook: plot_gpc_xor.ipynb`](https://scikit-learn.org/stable/_downloads/578d975e1bd2f15587da4ccbce0a7d14/plot_gpc_xor.ipynb)

[`Download Python source code: plot_gpc_xor.py`](https://scikit-learn.org/stable/_downloads/08fc4f471ae40388eb535678346dc9d1/plot_gpc_xor.py)

[`Download zipped: plot_gpc_xor.zip`](https://scikit-learn.org/stable/_downloads/c545073653cd4e480bed940f553b41fc/plot_gpc_xor.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_iris_thumb.png)

[Gaussian process classification (GPC) on iris dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html)

Gaussian process classification (GPC) on iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_weighted_samples_thumb.png)

[SGD: Weighted samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html)

SGD: Weighted samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_thumb.png)

[Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)

Varying regularization in Multi-layer Perceptron

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_strategies_thumb.png)

[Demonstrating the different strategies of KBinsDiscretizer](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_strategies.html)

Demonstrating the different strategies of KBinsDiscretizer

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/08fc4f471ae40388eb535678346dc9d1/plot_gpc_xor.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/578d975e1bd2f15587da4ccbce0a7d14/plot_gpc_xor.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/c545073653cd4e480bed940f553b41fc/plot_gpc_xor.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpc_xor.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpc_xor.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)