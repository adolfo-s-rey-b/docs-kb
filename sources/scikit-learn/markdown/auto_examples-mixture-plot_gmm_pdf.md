[Skip to main content](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_pdf.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/mixture/plot_gmm_pdf.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_pdf.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/mixture/plot_gmm_pdf.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/mixture/plot_gmm_pdf.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/mixture/plot_gmm_pdf.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/mixture/plot_gmm_pdf.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/mixture/plot_gmm_pdf.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_pdf.html#sphx-glr-download-auto-examples-mixture-plot-gmm-pdf-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Density Estimation for a Gaussian mixture[#](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_pdf.html#density-estimation-for-a-gaussian-mixture "Link to this heading")

=======================================================================================================================================================================================

Plot the density estimation of a mixture of two Gaussians. Data is generated from two Gaussians with different centers and covariance matrices.

![Negative log-likelihood predicted by a GMM](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_pdf_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import [LogNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm "matplotlib.colors.LogNorm")

from sklearn import mixture

n\_samples \= 300

\# generate random sample, two components
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)

\# generate spherical data centered on (20, 20)
shifted\_gaussian \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_samples, 2) + [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[20, 20\])

\# generate zero centered stretched Gaussian data
C \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[0.0, \-0.7\], \[3.5, 0.7\]\])
stretched\_gaussian \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_samples, 2), C)

\# concatenate the two datasets into the final training set
X\_train \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(\[shifted\_gaussian, stretched\_gaussian\])

\# fit a Gaussian Mixture Model with two components
clf \= [mixture.GaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
(n\_components\=2, covariance\_type\="full")
clf.fit(X\_train)

\# display predicted scores by the model as a contour plot
x \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-20.0, 30.0)
y \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-20.0, 40.0)
X, Y \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(x, y)
XX \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[X.ravel(), Y.ravel()\]).T
Z \= \-clf.score\_samples(XX)
Z \= Z.reshape(X.shape)

CS \= [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(
    X, Y, Z, norm\=[LogNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm "matplotlib.colors.LogNorm")
(vmin\=1.0, vmax\=1000.0), levels\=[np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(0, 3, 10)
)
CB \= [plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
(CS, shrink\=0.8, extend\="both")
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_train\[:, 0\], X\_train\[:, 1\], 0.8)

[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Negative log-likelihood predicted by a GMM")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.113 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo22.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/mixture/plot_gmm_pdf.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo22.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/mixture/plot_gmm_pdf.ipynb)

[`Download Jupyter notebook: plot_gmm_pdf.ipynb`](https://scikit-learn.org/stable/_downloads/35ec767dbdc0119a20d1fd2022298627/plot_gmm_pdf.ipynb)

[`Download Python source code: plot_gmm_pdf.py`](https://scikit-learn.org/stable/_downloads/6bcd24982ec4dfd9c0179937957b9bbd/plot_gmm_pdf.py)

[`Download zipped: plot_gmm_pdf.zip`](https://scikit-learn.org/stable/_downloads/baf3c3e7a8255dce4078f2fb913ebe12/plot_gmm_pdf.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_thumb.png)

[Gaussian Mixture Model Ellipsoids](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm.html)

Gaussian Mixture Model Ellipsoids

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_sin_thumb.png)

[Gaussian Mixture Model Sine Curve](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_sin.html)

Gaussian Mixture Model Sine Curve

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_weighted_samples_thumb.png)

[SGD: Weighted samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html)

SGD: Weighted samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_xor_thumb.png)

[Illustration of Gaussian process classification (GPC) on the XOR dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html)

Illustration of Gaussian process classification (GPC) on the XOR dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/6bcd24982ec4dfd9c0179937957b9bbd/plot_gmm_pdf.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/35ec767dbdc0119a20d1fd2022298627/plot_gmm_pdf.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/baf3c3e7a8255dce4078f2fb913ebe12/plot_gmm_pdf.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo22.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/mixture/plot_gmm_pdf.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo22.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/mixture/plot_gmm_pdf.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)