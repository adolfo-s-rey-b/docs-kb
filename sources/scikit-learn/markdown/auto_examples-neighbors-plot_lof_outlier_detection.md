[Skip to main content](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_outlier_detection.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neighbors/plot_lof_outlier_detection.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_outlier_detection.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neighbors/plot_lof_outlier_detection.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neighbors/plot_lof_outlier_detection.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neighbors/plot_lof_outlier_detection.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neighbors/plot_lof_outlier_detection.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neighbors/plot_lof_outlier_detection.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_outlier_detection.html#sphx-glr-download-auto-examples-neighbors-plot-lof-outlier-detection-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Outlier detection with Local Outlier Factor (LOF)[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_outlier_detection.html#outlier-detection-with-local-outlier-factor-lof "Link to this heading")

=====================================================================================================================================================================================================================

The Local Outlier Factor (LOF) algorithm is an unsupervised anomaly detection method which computes the local density deviation of a given data point with respect to its neighbors. It considers as outliers the samples that have a substantially lower density than their neighbors. This example shows how to use LOF for outlier detection which is the default use case of this estimator in scikit-learn. Note that when LOF is used for outlier detection it has no `predict`, `decision_function` and `score_samples` methods. See the [User Guide](https://scikit-learn.org/stable/modules/outlier_detection.html#outlier-detection)
 for details on the difference between outlier detection and novelty detection and how to use LOF for novelty detection.

The number of neighbors considered (parameter `n_neighbors`) is typically set 1) greater than the minimum number of samples a cluster has to contain, so that other samples can be local outliers relative to this cluster, and 2) smaller than the maximum number of close by samples that can potentially be local outliers. In practice, such information is generally not available, and taking `n_neighbors=20` appears to work well in general.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate data with outliers[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_outlier_detection.html#generate-data-with-outliers "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(42)

X\_inliers \= 0.3 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(100, 2)
X\_inliers \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[X\_inliers + 2, X\_inliers \- 2\]
X\_outliers \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(low\=-4, high\=4, size\=(20, 2))
X \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[X\_inliers, X\_outliers\]

n\_outliers \= len(X\_outliers)
ground\_truth \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(len(X), dtype\=int)
ground\_truth\[\-n\_outliers:\] \= \-1

Copy to clipboard

Fit the model for outlier detection (default)[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_outlier_detection.html#fit-the-model-for-outlier-detection-default "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use `fit_predict` to compute the predicted labels of the training samples (when LOF is used for outlier detection, the estimator has no `predict`, `decision_function` and `score_samples` methods).

from sklearn.neighbors import [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")

clf \= [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
(n\_neighbors\=20, contamination\=0.1)
y\_pred \= clf.fit\_predict(X)
n\_errors \= (y\_pred != ground\_truth).sum()
X\_scores \= clf.negative\_outlier\_factor\_

Copy to clipboard

Plot results[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_outlier_detection.html#plot-results "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.legend\_handler import [HandlerPathCollection](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerPathCollection "matplotlib.legend_handler.HandlerPathCollection")

def update\_legend\_marker\_size(handle, orig):
    "Customize size of the legend marker"
    handle.update\_from(orig)
    handle.set\_sizes(\[20\])

[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], color\="k", s\=3.0, label\="Data points")
\# plot circles with radius proportional to the outlier scores
radius \= (X\_scores.max() \- X\_scores) / (X\_scores.max() \- X\_scores.min())
scatter \= [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    X\[:, 0\],
    X\[:, 1\],
    s\=1000 \* radius,
    edgecolors\="r",
    facecolors\="none",
    label\="Outlier scores",
)
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
((\-5, 5))
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
((\-5, 5))
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("prediction errors: %d" % (n\_errors))
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(
    handler\_map\={scatter: [HandlerPathCollection](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerPathCollection "matplotlib.legend_handler.HandlerPathCollection")
(update\_func\=update\_legend\_marker\_size)}
)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Local Outlier Factor (LOF)")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Local Outlier Factor (LOF)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lof_outlier_detection_001.png)

**Total running time of the script:** (0 minutes 0.074 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_lof_outlier_detection.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_lof_outlier_detection.ipynb)

[`Download Jupyter notebook: plot_lof_outlier_detection.ipynb`](https://scikit-learn.org/stable/_downloads/a91fcd567e6bc2540b34f44d599d3531/plot_lof_outlier_detection.ipynb)

[`Download Python source code: plot_lof_outlier_detection.py`](https://scikit-learn.org/stable/_downloads/06d58c7fb0650278c0e3ea127bff7167/plot_lof_outlier_detection.py)

[`Download zipped: plot_lof_outlier_detection.zip`](https://scikit-learn.org/stable/_downloads/80f1673b50d88ee3f77b8540882e9964/plot_lof_outlier_detection.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lof_novelty_detection_thumb.png)

[Novelty detection with Local Outlier Factor (LOF)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_novelty_detection.html)

Novelty detection with Local Outlier Factor (LOF)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)

[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Comparing anomaly detection algorithms for outlier detection on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_wine_thumb.png)

[Outlier detection on a real data set](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html)

Outlier detection on a real data set

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_thumb.png)

[Evaluation of outlier detection estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html)

Evaluation of outlier detection estimators

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/06d58c7fb0650278c0e3ea127bff7167/plot_lof_outlier_detection.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/a91fcd567e6bc2540b34f44d599d3531/plot_lof_outlier_detection.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/80f1673b50d88ee3f77b8540882e9964/plot_lof_outlier_detection.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_lof_outlier_detection.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_lof_outlier_detection.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)