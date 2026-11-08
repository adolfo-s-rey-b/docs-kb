[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_bisect_kmeans.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_bisect_kmeans.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_bisect_kmeans.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_bisect_kmeans.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_bisect_kmeans.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_bisect_kmeans.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_bisect_kmeans.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_bisect_kmeans.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_bisect_kmeans.html#sphx-glr-download-auto-examples-cluster-plot-bisect-kmeans-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Bisecting K-Means and Regular K-Means Performance Comparison[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_bisect_kmeans.html#bisecting-k-means-and-regular-k-means-performance-comparison "Link to this heading")

===================================================================================================================================================================================================================================

This example shows differences between Regular K-Means algorithm and Bisecting K-Means.

While K-Means clusterings are different when increasing n\_clusters, Bisecting K-Means clustering builds on top of the previous ones. As a result, it tends to create clusters that have a more regular large-scale structure. This difference can be visually observed: for all numbers of clusters, there is a dividing line cutting the overall data cloud in two for BisectingKMeans, which is not present for regular K-Means.

![Bisecting K-Means : 4 clusters, Bisecting K-Means : 8 clusters, Bisecting K-Means : 16 clusters, K-Means : 4 clusters, K-Means : 8 clusters, K-Means : 16 clusters](https://scikit-learn.org/stable/_images/sphx_glr_plot_bisect_kmeans_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt

from sklearn.cluster import [BisectingKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans")
, [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")

\# Generate sample data
n\_samples \= 10000
random\_state \= 0

X, \_ \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=n\_samples, centers\=2, random\_state\=random\_state)

\# Number of cluster centers for KMeans and BisectingKMeans
n\_clusters\_list \= \[4, 8, 16\]

\# Algorithms to compare
clustering\_algorithms \= {
    "Bisecting K-Means": [BisectingKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans")
,
    "K-Means": [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
,
}

\# Make subplots for each variant
fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
    len(clustering\_algorithms), len(n\_clusters\_list), figsize\=(12, 5)
)

axs \= axs.T

for i, (algorithm\_name, Algorithm) in enumerate(clustering\_algorithms.items()):
    for j, n\_clusters in enumerate(n\_clusters\_list):
        algo \= Algorithm(n\_clusters\=n\_clusters, random\_state\=random\_state, n\_init\=3)
        algo.fit(X)
        centers \= algo.cluster\_centers\_

        axs\[j, i\].scatter(X\[:, 0\], X\[:, 1\], s\=10, c\=algo.labels\_)
        axs\[j, i\].scatter(centers\[:, 0\], centers\[:, 1\], c\="r", s\=20)

        axs\[j, i\].set\_title(f"{algorithm\_name} : {n\_clusters} clusters")

\# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label\_outer()
    ax.set\_xticks(\[\])
    ax.set\_yticks(\[\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 1.029 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_bisect_kmeans.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_bisect_kmeans.ipynb)

[`Download Jupyter notebook: plot_bisect_kmeans.ipynb`](https://scikit-learn.org/stable/_downloads/13db5212719118ea59532c291af3a8f9/plot_bisect_kmeans.ipynb)

[`Download Python source code: plot_bisect_kmeans.py`](https://scikit-learn.org/stable/_downloads/73962cec5f14b10630f1a505fe761ab7/plot_bisect_kmeans.py)

[`Download zipped: plot_bisect_kmeans.zip`](https://scikit-learn.org/stable/_downloads/3d6718e20e6b7b05b7cdaa333a6d05a4/plot_bisect_kmeans.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_assumptions_thumb.png)

[Demonstration of k-means assumptions](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html)

Demonstration of k-means assumptions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_plusplus_thumb.png)

[An example of K-Means++ initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_plusplus.html)

An example of K-Means++ initialization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mini_batch_kmeans_thumb.png)

[Comparison of the K-Means and MiniBatchKMeans clustering algorithms](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html)

Comparison of the K-Means and MiniBatchKMeans clustering algorithms

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_stability_low_dim_dense_thumb.png)

[Empirical evaluation of the impact of k-means initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)

Empirical evaluation of the impact of k-means initialization

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/73962cec5f14b10630f1a505fe761ab7/plot_bisect_kmeans.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/13db5212719118ea59532c291af3a8f9/plot_bisect_kmeans.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/3d6718e20e6b7b05b7cdaa333a6d05a4/plot_bisect_kmeans.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_bisect_kmeans.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_bisect_kmeans.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)