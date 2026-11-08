[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_dbscan.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_dbscan.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_dbscan.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_dbscan.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_dbscan.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_dbscan.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-download-auto-examples-cluster-plot-dbscan-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Demo of DBSCAN clustering algorithm[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#demo-of-dbscan-clustering-algorithm "Link to this heading")

==========================================================================================================================================================================

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) finds core samples in regions of high density and expands clusters from them. This algorithm is good for data which contains clusters of similar density.

See the [Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py)
 example for a demo of different clustering algorithms on 2D datasets.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Data generation[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#data-generation "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

We use [`make_blobs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
 to create 3 synthetic clusters.

from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

centers \= \[\[1, 1\], \[\-1, \-1\], \[1, \-1\]\]
X, labels\_true \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(
    n\_samples\=750, centers\=centers, cluster\_std\=0.4, random\_state\=0
)

X \= [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
().fit\_transform(X)

Copy to clipboard

We can visualize the resulting data:

import matplotlib.pyplot as plt

[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\])
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot dbscan](https://scikit-learn.org/stable/_images/sphx_glr_plot_dbscan_001.png)

Compute DBSCAN[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#compute-dbscan "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

One can access the labels assigned by [`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
 using the `labels_` attribute. Noisy samples are given the label −1.

import numpy as np

from sklearn import metrics
from sklearn.cluster import [DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")

db \= [DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
(eps\=0.3, min\_samples\=10).fit(X)
labels \= db.labels\_

\# Number of clusters in labels, ignoring noise if present.
n\_clusters\_ \= len(set(labels)) \- (1 if \-1 in labels else 0)
n\_noise\_ \= list(labels).count(\-1)

print("Estimated number of clusters: %d" % n\_clusters\_)
print("Estimated number of noise points: %d" % n\_noise\_)

Copy to clipboard

Estimated number of clusters: 3
Estimated number of noise points: 18

Copy to clipboard

Clustering algorithms are fundamentally unsupervised learning methods. However, since [`make_blobs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
 gives access to the true labels of the synthetic clusters, it is possible to use evaluation metrics that leverage this “supervised” ground truth information to quantify the quality of the resulting clusters. Examples of such metrics are the homogeneity, completeness, V-measure, Rand-Index, Adjusted Rand-Index and Adjusted Mutual Information (AMI).

If the ground truth labels are not known, evaluation can only be performed using the model results itself. In that case, the Silhouette Coefficient comes in handy.

For more information, see the [Adjustment for chance in clustering performance evaluation](https://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html#sphx-glr-auto-examples-cluster-plot-adjusted-for-chance-measures-py)
 example or the [Clustering performance evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation)
 module.

print(f"Homogeneity: {[metrics.homogeneity\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html#sklearn.metrics.homogeneity_score "sklearn.metrics.homogeneity_score")
(labels\_true, labels):.3f}")
print(f"Completeness: {[metrics.completeness\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.completeness_score.html#sklearn.metrics.completeness_score "sklearn.metrics.completeness_score")
(labels\_true, labels):.3f}")
print(f"V-measure: {[metrics.v\_measure\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")
(labels\_true, labels):.3f}")
print(f"Adjusted Rand Index: {[metrics.adjusted\_rand\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#sklearn.metrics.adjusted_rand_score "sklearn.metrics.adjusted_rand_score")
(labels\_true, labels):.3f}")
print(
    "Adjusted Mutual Information:"
    f" {[metrics.adjusted\_mutual\_info\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")
(labels\_true, labels):.3f}"
)
print(f"Silhouette Coefficient: {[metrics.silhouette\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")
(X, labels):.3f}")

Copy to clipboard

Homogeneity: 0.953
Completeness: 0.883
V-measure: 0.917
Adjusted Rand Index: 0.952
Adjusted Mutual Information: 0.916
Silhouette Coefficient: 0.626

Copy to clipboard

Plot results[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#plot-results "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

Core samples (large dots) and non-core samples (small dots) are color-coded according to the assigned cluster. Samples tagged as noise are represented in black.

unique\_labels \= set(labels)
core\_samples\_mask \= [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
(labels, dtype\=bool)
core\_samples\_mask\[db.core\_sample\_indices\_\] \= True

colors \= \[plt.cm.Spectral(each) for each in [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
(0, 1, len(unique\_labels))\]
for k, col in zip(unique\_labels, colors):
    if k \== \-1:
        \# Black used for noise.
        col \= \[0, 0, 0, 1\]

    class\_member\_mask \= labels \== k

    xy \= X\[class\_member\_mask & core\_samples\_mask\]
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
        xy\[:, 0\],
        xy\[:, 1\],
        "o",
        markerfacecolor\=tuple(col),
        markeredgecolor\="k",
        markersize\=14,
    )

    xy \= X\[class\_member\_mask & ~core\_samples\_mask\]
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
        xy\[:, 0\],
        xy\[:, 1\],
        "o",
        markerfacecolor\=tuple(col),
        markeredgecolor\="k",
        markersize\=6,
    )

[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(f"Estimated number of clusters: {n\_clusters\_}")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Estimated number of clusters: 3](https://scikit-learn.org/stable/_images/sphx_glr_plot_dbscan_002.png)

**Total running time of the script:** (0 minutes 0.165 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_dbscan.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_dbscan.ipynb)

[`Download Jupyter notebook: plot_dbscan.ipynb`](https://scikit-learn.org/stable/_downloads/23a5a575578f08cc0071cc070953a655/plot_dbscan.ipynb)

[`Download Python source code: plot_dbscan.py`](https://scikit-learn.org/stable/_downloads/0b802e24fdcd192a452e91580f278039/plot_dbscan.py)

[`Download zipped: plot_dbscan.zip`](https://scikit-learn.org/stable/_downloads/c23136a84c063f9259187cbd78ec30ed/plot_dbscan.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_affinity_propagation_thumb.png)

[Demo of affinity propagation clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html)

Demo of affinity propagation clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_thumb.png)

[Demo of HDBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html)

Demo of HDBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adjusted_for_chance_measures_thumb.png)

[Adjustment for chance in clustering performance evaluation](https://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html)

Adjustment for chance in clustering performance evaluation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mean_shift_thumb.png)

[A demo of the mean-shift clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html)

A demo of the mean-shift clustering algorithm

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/0b802e24fdcd192a452e91580f278039/plot_dbscan.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/23a5a575578f08cc0071cc070953a655/plot_dbscan.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/c23136a84c063f9259187cbd78ec30ed/plot_dbscan.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_dbscan.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_dbscan.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)