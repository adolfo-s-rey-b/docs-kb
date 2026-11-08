[Skip to main content](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_novelty_detection.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neighbors/plot_lof_novelty_detection.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_novelty_detection.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neighbors/plot_lof_novelty_detection.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neighbors/plot_lof_novelty_detection.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neighbors/plot_lof_novelty_detection.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neighbors/plot_lof_novelty_detection.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neighbors/plot_lof_novelty_detection.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_novelty_detection.html#sphx-glr-download-auto-examples-neighbors-plot-lof-novelty-detection-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Novelty detection with Local Outlier Factor (LOF)[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_novelty_detection.html#novelty-detection-with-local-outlier-factor-lof "Link to this heading")

=====================================================================================================================================================================================================================

The Local Outlier Factor (LOF) algorithm is an unsupervised anomaly detection method which computes the local density deviation of a given data point with respect to its neighbors. It considers as outliers the samples that have a substantially lower density than their neighbors. This example shows how to use LOF for novelty detection. Note that when LOF is used for novelty detection you MUST not use predict, decision\_function and score\_samples on the training set as this would lead to wrong results. You must only use these methods on new unseen data (which are not in the training set). See [User Guide](https://scikit-learn.org/stable/modules/outlier_detection.html#outlier-detection)
: for details on the difference between outlier detection and novelty detection and how to use LOF for outlier detection.

The number of neighbors considered, (parameter n\_neighbors) is typically set 1) greater than the minimum number of samples a cluster has to contain, so that other samples can be local outliers relative to this cluster, and 2) smaller than the maximum number of close by samples that can potentially be local outliers. In practice, such information is generally not available, and taking n\_neighbors=20 appears to work well in general.

![Novelty Detection with LOF](https://scikit-learn.org/stable/_images/sphx_glr_plot_lof_novelty_detection_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np

from sklearn.neighbors import [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(42)

xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-5, 5, 500), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-5, 5, 500))
\# Generate normal (not abnormal) training observations
X \= 0.3 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(100, 2)
X\_train \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[X + 2, X \- 2\]
\# Generate new normal (not abnormal) observations
X \= 0.3 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(20, 2)
X\_test \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[X + 2, X \- 2\]
\# Generate some abnormal novel observations
X\_outliers \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(low\=-4, high\=4, size\=(20, 2))

\# fit the model for novelty detection (novelty=True)
clf \= [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
(n\_neighbors\=20, novelty\=True, contamination\=0.1)
clf.fit(X\_train)
\# DO NOT use predict, decision\_function and score\_samples on X\_train as this
\# would give wrong results but only on new unseen data (not used in X\_train),
\# e.g. X\_test, X\_outliers or the meshgrid
y\_pred\_test \= clf.predict(X\_test)
y\_pred\_outliers \= clf.predict(X\_outliers)
n\_error\_test \= y\_pred\_test\[y\_pred\_test \== \-1\].size
n\_error\_outliers \= y\_pred\_outliers\[y\_pred\_outliers \== 1\].size

\# plot the learned frontier, the points, and the nearest vectors to the plane
Z \= clf.decision\_function([np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[xx.ravel(), yy.ravel()\])
Z \= Z.reshape(xx.shape)

[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Novelty Detection with LOF")
[plt.contourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
(xx, yy, Z, levels\=[np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(Z.min(), 0, 7), cmap\=plt.cm.PuBu)
a \= [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(xx, yy, Z, levels\=\[0\], linewidths\=2, colors\="darkred")
[plt.contourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
(xx, yy, Z, levels\=\[0, Z.max()\], colors\="palevioletred")

s \= 40
b1 \= [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_train\[:, 0\], X\_train\[:, 1\], c\="white", s\=s, edgecolors\="k")
b2 \= [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_test\[:, 0\], X\_test\[:, 1\], c\="blueviolet", s\=s, edgecolors\="k")
c \= [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_outliers\[:, 0\], X\_outliers\[:, 1\], c\="gold", s\=s, edgecolors\="k")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
((\-5, 5))
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
((\-5, 5))
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(
    \[[mlines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[\], \[\], color\="darkred"), b1, b2, c\],
    \[\
        "learned frontier",\
        "training observations",\
        "new regular observations",\
        "new abnormal observations",\
    \],
    loc\=(1.05, 0.4),
    prop\=[matplotlib.font\_manager.FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
(size\=11),
)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
(
    "errors novel regular: %d/40 ; errors novel abnormal: %d/40"
    % (n\_error\_test, n\_error\_outliers)
)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.665 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_lof_novelty_detection.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_lof_novelty_detection.ipynb)

[`Download Jupyter notebook: plot_lof_novelty_detection.ipynb`](https://scikit-learn.org/stable/_downloads/1ecb1284f0b785cd0011e155bf44657c/plot_lof_novelty_detection.ipynb)

[`Download Python source code: plot_lof_novelty_detection.py`](https://scikit-learn.org/stable/_downloads/42b321f3e1d8c7a657ebec98c5d6ea0d/plot_lof_novelty_detection.py)

[`Download zipped: plot_lof_novelty_detection.zip`](https://scikit-learn.org/stable/_downloads/eeecd96e36ce9fc8a3bb2061edde8dbc/plot_lof_novelty_detection.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lof_outlier_detection_thumb.png)

[Outlier detection with Local Outlier Factor (LOF)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_outlier_detection.html)

Outlier detection with Local Outlier Factor (LOF)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_oneclass_thumb.png)

[One-class SVM with non-linear kernel (RBF)](https://scikit-learn.org/stable/auto_examples/svm/plot_oneclass.html)

One-class SVM with non-linear kernel (RBF)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)

[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Comparing anomaly detection algorithms for outlier detection on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgdocsvm_vs_ocsvm_thumb.png)

[One-Class SVM versus One-Class SVM using Stochastic Gradient Descent](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html)

One-Class SVM versus One-Class SVM using Stochastic Gradient Descent

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/42b321f3e1d8c7a657ebec98c5d6ea0d/plot_lof_novelty_detection.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/1ecb1284f0b785cd0011e155bf44657c/plot_lof_novelty_detection.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/eeecd96e36ce9fc8a3bb2061edde8dbc/plot_lof_novelty_detection.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_lof_novelty_detection.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_lof_novelty_detection.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)