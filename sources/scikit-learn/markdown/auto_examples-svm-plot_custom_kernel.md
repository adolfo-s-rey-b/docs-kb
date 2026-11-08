[Skip to main content](https://scikit-learn.org/stable/auto_examples/svm/plot_custom_kernel.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/svm/plot_custom_kernel.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/svm/plot_custom_kernel.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/svm/plot_custom_kernel.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/svm/plot_custom_kernel.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/svm/plot_custom_kernel.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/svm/plot_custom_kernel.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/svm/plot_custom_kernel.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/svm/plot_custom_kernel.html#sphx-glr-download-auto-examples-svm-plot-custom-kernel-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

SVM with custom kernel[#](https://scikit-learn.org/stable/auto_examples/svm/plot_custom_kernel.html#svm-with-custom-kernel "Link to this heading")

===================================================================================================================================================

Simple usage of [Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html#svm)
 classifier with a custom kernel. It will plot the decision surface and highlight the support vectors.

![3-Class classification using Support Vector Machine with custom kernel](https://scikit-learn.org/stable/_images/sphx_glr_plot_custom_kernel_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, svm
from sklearn.inspection import DecisionBoundaryDisplay

\# Import some data to play with.
iris \= [datasets.load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X \= iris.data\[:, :2\]  \# We only take the first two features. We could
\# avoid this ugly slicing by using a two-dim dataset.
Y \= iris.target

def my\_kernel(X, Y):
    """
    We create a custom kernel:

                 (2  0)
    k(X, Y) = X  (    ) Y.T
                 (0  1)
    """
    M \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[2, 0\], \[0, 1.0\]\])
    return [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
([np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(X, M), Y.T)

\# We create an instance of SVC with that kernel and fit it on the data.
clf \= [svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(kernel\=my\_kernel)
clf.fit(X, Y)

ax \= [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()
[DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    clf,
    X,
    multiclass\_colors\="Paired",
    ax\=ax,
    response\_method\="predict",
    plot\_method\="pcolormesh",
    shading\="auto",
    alpha\=0.5,
)

\# Plot the training points
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], c\=Y, cmap\=plt.cm.Paired)
\# Highlight the support vectors
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    X\[clf.support\_, 0\],
    X\[clf.support\_, 1\],
    facecolor\="none",
    edgecolors\="k",
)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("3-Class classification using Support Vector Machine with custom kernel")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.100 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_custom_kernel.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_custom_kernel.ipynb)

[`Download Jupyter notebook: plot_custom_kernel.ipynb`](https://scikit-learn.org/stable/_downloads/1160eee327e01cad702c4964e1c69f45/plot_custom_kernel.ipynb)

[`Download Python source code: plot_custom_kernel.py`](https://scikit-learn.org/stable/_downloads/31b78d45b09682c72f57e77cf94a939e/plot_custom_kernel.py)

[`Download zipped: plot_custom_kernel.zip`](https://scikit-learn.org/stable/_downloads/c19d26d7653b439c29998e17425b7dad/plot_custom_kernel.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_thumb.png)

[Plot different SVM classifiers in the iris dataset](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html)

Plot different SVM classifiers in the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_thumb.png)

[SVM: Maximum margin separating hyperplane](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane.html)

SVM: Maximum margin separating hyperplane

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linearsvc_support_vectors_thumb.png)

[Plot the support vectors in LinearSVC](https://scikit-learn.org/stable/auto_examples/svm/plot_linearsvc_support_vectors.html)

Plot the support vectors in LinearSVC

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nearest_centroid_thumb.png)

[Nearest Centroid Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nearest_centroid.html)

Nearest Centroid Classification

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/31b78d45b09682c72f57e77cf94a939e/plot_custom_kernel.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/1160eee327e01cad702c4964e1c69f45/plot_custom_kernel.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/c19d26d7653b439c29998e17425b7dad/plot_custom_kernel.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_custom_kernel.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_custom_kernel.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)