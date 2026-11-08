[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_mean_shift.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_mean_shift.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_mean_shift.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_mean_shift.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_mean_shift.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_mean_shift.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html#sphx-glr-download-auto-examples-cluster-plot-mean-shift-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

A demo of the mean-shift clustering algorithm[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html#a-demo-of-the-mean-shift-clustering-algorithm "Link to this heading")

==================================================================================================================================================================================================

Reference:

Dorin Comaniciu and Peter Meer, “Mean Shift: A robust approach toward feature space analysis”. IEEE Transactions on Pattern Analysis and Machine Intelligence. 2002. pp. 603-619.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import numpy as np

from sklearn.cluster import [MeanShift](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")
, [estimate\_bandwidth](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.estimate_bandwidth.html#sklearn.cluster.estimate_bandwidth "sklearn.cluster.estimate_bandwidth")
from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")

Copy to clipboard

Generate sample data[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html#generate-sample-data "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

centers \= \[\[1, 1\], \[\-1, \-1\], \[1, \-1\]\]
X, \_ \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=10000, centers\=centers, cluster\_std\=0.6)

Copy to clipboard

Compute clustering with MeanShift[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html#compute-clustering-with-meanshift "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\# The following bandwidth can be automatically detected using
bandwidth \= [estimate\_bandwidth](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.estimate_bandwidth.html#sklearn.cluster.estimate_bandwidth "sklearn.cluster.estimate_bandwidth")
(X, quantile\=0.2, n\_samples\=500)

ms \= [MeanShift](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")
(bandwidth\=bandwidth, bin\_seeding\=True)
ms.fit(X)
labels \= ms.labels\_
cluster\_centers \= ms.cluster\_centers\_

labels\_unique \= [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(labels)
n\_clusters\_ \= len(labels\_unique)

print("number of estimated clusters : %d" % n\_clusters\_)

Copy to clipboard

number of estimated clusters : 3

Copy to clipboard

Plot result[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html#plot-result "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(1)
[plt.clf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clf.html#matplotlib.pyplot.clf "matplotlib.pyplot.clf")
()

colors \= \["#dede00", "#377eb8", "#f781bf"\]
markers \= \["x", "o", "^"\]

for k, col in zip(range(n\_clusters\_), colors):
    my\_members \= labels \== k
    cluster\_center \= cluster\_centers\[k\]
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\[my\_members, 0\], X\[my\_members, 1\], markers\[k\], color\=col)
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
        cluster\_center\[0\],
        cluster\_center\[1\],
        markers\[k\],
        markerfacecolor\=col,
        markeredgecolor\="k",
        markersize\=14,
    )
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Estimated number of clusters: %d" % n\_clusters\_)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Estimated number of clusters: 3](https://scikit-learn.org/stable/_images/sphx_glr_plot_mean_shift_001.png)

**Total running time of the script:** (0 minutes 0.513 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_mean_shift.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_mean_shift.ipynb)

[`Download Jupyter notebook: plot_mean_shift.ipynb`](https://scikit-learn.org/stable/_downloads/43f17c8225b2c8e15e22a7edf7adb8b5/plot_mean_shift.ipynb)

[`Download Python source code: plot_mean_shift.py`](https://scikit-learn.org/stable/_downloads/585914164dc34984e397f8d3d61849a5/plot_mean_shift.py)

[`Download zipped: plot_mean_shift.zip`](https://scikit-learn.org/stable/_downloads/de462b38777cec6da8a8387da7db8f3a/plot_mean_shift.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_affinity_propagation_thumb.png)

[Demo of affinity propagation clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html)

Demo of affinity propagation clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mini_batch_kmeans_thumb.png)

[Comparison of the K-Means and MiniBatchKMeans clustering algorithms](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html)

Comparison of the K-Means and MiniBatchKMeans clustering algorithms

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dbscan_thumb.png)

[Demo of DBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html)

Demo of DBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_plusplus_thumb.png)

[An example of K-Means++ initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_plusplus.html)

An example of K-Means++ initialization

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/585914164dc34984e397f8d3d61849a5/plot_mean_shift.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/43f17c8225b2c8e15e22a7edf7adb8b5/plot_mean_shift.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/de462b38777cec6da8a8387da7db8f3a/plot_mean_shift.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_mean_shift.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_mean_shift.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)