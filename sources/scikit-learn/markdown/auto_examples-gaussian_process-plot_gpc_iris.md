[Skip to main content](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/gaussian_process/plot_gpc_iris.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/gaussian_process/plot_gpc_iris.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/gaussian_process/plot_gpc_iris.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/gaussian_process/plot_gpc_iris.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/gaussian_process/plot_gpc_iris.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/gaussian_process/plot_gpc_iris.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html#sphx-glr-download-auto-examples-gaussian-process-plot-gpc-iris-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Gaussian process classification (GPC) on iris dataset[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html#gaussian-process-classification-gpc-on-iris-dataset "Link to this heading")

=======================================================================================================================================================================================================================

This example illustrates the predicted probability of GPC for an isotropic and anisotropic RBF kernel on a two-dimensional version for the iris-dataset. The anisotropic RBF kernel obtains slightly higher log-marginal-likelihood by assigning different length-scales to the two feature dimensions.

![Isotropic RBF, LML: -48.316, Anisotropic RBF, LML: -47.888](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_iris_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.gaussian\_process import [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
from sklearn.gaussian\_process.kernels import [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")

\# import some data to play with
iris \= [datasets.load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X \= iris.data\[:, :2\]  \# we only take the first two features.
y \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(iris.target, dtype\=int)

h \= 0.02  \# step size in the mesh

kernel \= 1.0 \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
(\[1.0\])
gpc\_rbf\_isotropic \= [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
(kernel\=kernel).fit(X, y)
kernel \= 1.0 \* [RBF](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")
(\[1.0, 1.0\])
gpc\_rbf\_anisotropic \= [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
(kernel\=kernel).fit(X, y)

\# create a mesh to plot in
x\_min, x\_max \= X\[:, 0\].min() \- 1, X\[:, 0\].max() + 1
y\_min, y\_max \= X\[:, 1\].min() \- 1, X\[:, 1\].max() + 1
xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(x\_min, x\_max, h), [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(y\_min, y\_max, h))

titles \= \["Isotropic RBF", "Anisotropic RBF"\]
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 5))
for i, clf in enumerate((gpc\_rbf\_isotropic, gpc\_rbf\_anisotropic)):
    \# Plot the predicted probabilities. For that, we will assign a color to
    \# each point in the mesh \[x\_min, m\_max\]x\[y\_min, y\_max\].
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 2, i + 1)

    Z \= clf.predict\_proba([np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[xx.ravel(), yy.ravel()\])

    \# Put the result into a color plot
    Z \= Z.reshape((xx.shape\[0\], xx.shape\[1\], 3))
    [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(Z, extent\=(x\_min, x\_max, y\_min, y\_max), origin\="lower")

    \# Plot also the training points
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], c\=[np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\["r", "g", "b"\])\[y\], edgecolors\=(0, 0, 0))
    [plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Sepal length")
    [plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Sepal width")
    [plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(xx.min(), xx.max())
    [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(yy.min(), yy.max())
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
        "%s, LML: %.3f" % (titles\[i\], clf.log\_marginal\_likelihood(clf.kernel\_.theta))
    )

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 3.211 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpc_iris.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpc_iris.ipynb)

[`Download Jupyter notebook: plot_gpc_iris.ipynb`](https://scikit-learn.org/stable/_downloads/a2f99bb3ce0cbeefa9d2e44fe9daf4cd/plot_gpc_iris.ipynb)

[`Download Python source code: plot_gpc_iris.py`](https://scikit-learn.org/stable/_downloads/44d6b1038c2225e954af6a4f193c2a94/plot_gpc_iris.py)

[`Download zipped: plot_gpc_iris.zip`](https://scikit-learn.org/stable/_downloads/6cf81265f73116706dcf276ed0aa52df/plot_gpc_iris.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_xor_thumb.png)

[Illustration of Gaussian process classification (GPC) on the XOR dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_xor.html)

Illustration of Gaussian process classification (GPC) on the XOR dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_thumb.png)

[Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)

Varying regularization in Multi-layer Perceptron

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_iris_thumb.png)

[Plot the decision surfaces of ensembles of trees on the iris dataset](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html)

Plot the decision surfaces of ensembles of trees on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_forest_embedding_thumb.png)

[Hashing feature transformation using Totally Random Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_embedding.html)

Hashing feature transformation using Totally Random Trees

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/44d6b1038c2225e954af6a4f193c2a94/plot_gpc_iris.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/a2f99bb3ce0cbeefa9d2e44fe9daf4cd/plot_gpc_iris.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/6cf81265f73116706dcf276ed0aa52df/plot_gpc_iris.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpc_iris.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpc_iris.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)