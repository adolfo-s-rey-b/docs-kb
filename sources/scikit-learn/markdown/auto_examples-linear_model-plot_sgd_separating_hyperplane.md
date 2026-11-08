[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_separating_hyperplane.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_sgd_separating_hyperplane.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_separating_hyperplane.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_sgd_separating_hyperplane.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_sgd_separating_hyperplane.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_sgd_separating_hyperplane.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_sgd_separating_hyperplane.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_sgd_separating_hyperplane.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_separating_hyperplane.html#sphx-glr-download-auto-examples-linear-model-plot-sgd-separating-hyperplane-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

SGD: Maximum margin separating hyperplane[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_separating_hyperplane.html#sgd-maximum-margin-separating-hyperplane "Link to this heading")

=============================================================================================================================================================================================================

Plot the maximum margin separating hyperplane within a two-class separable dataset using a linear Support Vector Machines classifier trained using SGD.

![plot sgd separating hyperplane](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_separating_hyperplane_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
from sklearn.linear\_model import [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")

\# we create 50 separable points
X, Y \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=50, centers\=2, random\_state\=0, cluster\_std\=0.60)

\# fit the model
clf \= [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
(loss\="hinge", alpha\=0.01, max\_iter\=200)

clf.fit(X, Y)

\# plot the line, the points, and the nearest vectors to the plane
xx \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-1, 5, 10)
yy \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-1, 5, 10)

X1, X2 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(xx, yy)
Z \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
(X1.shape)
for (i, j), val in [np.ndenumerate](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html#numpy.ndenumerate "numpy.ndenumerate")
(X1):
    x1 \= val
    x2 \= X2\[i, j\]
    p \= clf.decision\_function(\[\[x1, x2\]\])
    Z\[i, j\] \= p\[0\]
levels \= \[\-1.0, 0.0, 1.0\]
linestyles \= \["dashed", "solid", "dashed"\]
colors \= "k"
[plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(X1, X2, Z, levels, colors\=colors, linestyles\=linestyles)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], c\=Y, cmap\=plt.cm.Paired, edgecolor\="black", s\=20)

[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.067 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sgd_separating_hyperplane.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sgd_separating_hyperplane.ipynb)

[`Download Jupyter notebook: plot_sgd_separating_hyperplane.ipynb`](https://scikit-learn.org/stable/_downloads/305aa8bba883838e1ca0d690e78e9fbd/plot_sgd_separating_hyperplane.ipynb)

[`Download Python source code: plot_sgd_separating_hyperplane.py`](https://scikit-learn.org/stable/_downloads/600083c06dc28955779ad845ac1dde60/plot_sgd_separating_hyperplane.py)

[`Download zipped: plot_sgd_separating_hyperplane.zip`](https://scikit-learn.org/stable/_downloads/80b08d3f67c5579a3b581e92003ce6c3/plot_sgd_separating_hyperplane.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_isoprobability_thumb.png)

[Iso-probability lines for Gaussian Processes classification (GPC)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_isoprobability.html)

Iso-probability lines for Gaussian Processes classification (GPC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_thumb.png)

[SVM: Maximum margin separating hyperplane](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane.html)

SVM: Maximum margin separating hyperplane

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_twoclass_thumb.png)

[Two-class AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_twoclass.html)

Two-class AdaBoost

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_weighted_samples_thumb.png)

[SGD: Weighted samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html)

SGD: Weighted samples

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/600083c06dc28955779ad845ac1dde60/plot_sgd_separating_hyperplane.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/305aa8bba883838e1ca0d690e78e9fbd/plot_sgd_separating_hyperplane.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/80b08d3f67c5579a3b581e92003ce6c3/plot_sgd_separating_hyperplane.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sgd_separating_hyperplane.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sgd_separating_hyperplane.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)