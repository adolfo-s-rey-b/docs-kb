[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_mini_batch_kmeans.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_mini_batch_kmeans.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_mini_batch_kmeans.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_mini_batch_kmeans.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_mini_batch_kmeans.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_mini_batch_kmeans.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html#sphx-glr-download-auto-examples-cluster-plot-mini-batch-kmeans-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparison of the K-Means and MiniBatchKMeans clustering algorithms[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html#comparison-of-the-k-means-and-minibatchkmeans-clustering-algorithms "Link to this heading")

=====================================================================================================================================================================================================================================================

We want to compare the performance of the MiniBatchKMeans and KMeans: the MiniBatchKMeans is faster, but gives slightly different results (see [Mini Batch K-Means](https://scikit-learn.org/stable/modules/clustering.html#mini-batch-kmeans)
).

We will cluster a set of data, first with KMeans and then with MiniBatchKMeans, and plot the results. We will also plot the points that are labelled differently between the two algorithms.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate the data[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html#generate-the-data "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

We start by generating the blobs of data to be clustered.

import numpy as np

from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)

batch\_size \= 45
centers \= \[\[1, 1\], \[\-1, \-1\], \[1, \-1\]\]
n\_clusters \= len(centers)
X, labels\_true \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=3000, centers\=centers, cluster\_std\=0.7)

Copy to clipboard

Compute clustering with KMeans[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html#compute-clustering-with-kmeans "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import time

from sklearn.cluster import [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")

k\_means \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(init\="k-means++", n\_clusters\=3, n\_init\=10)
t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
k\_means.fit(X)
t\_batch \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0

Copy to clipboard

Compute clustering with MiniBatchKMeans[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html#compute-clustering-with-minibatchkmeans "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.cluster import [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")

mbk \= [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
(
    init\="k-means++",
    n\_clusters\=3,
    batch\_size\=batch\_size,
    n\_init\=10,
    max\_no\_improvement\=10,
    verbose\=0,
)
t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
mbk.fit(X)
t\_mini\_batch \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0

Copy to clipboard

Establishing parity between clusters[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html#establishing-parity-between-clusters "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We want to have the same color for the same cluster from both the MiniBatchKMeans and the KMeans algorithm. Let’s pair the cluster centers per closest one.

from sklearn.metrics.pairwise import [pairwise\_distances\_argmin](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "sklearn.metrics.pairwise_distances_argmin")

k\_means\_cluster\_centers \= k\_means.cluster\_centers\_
order \= [pairwise\_distances\_argmin](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "sklearn.metrics.pairwise_distances_argmin")
(k\_means.cluster\_centers\_, mbk.cluster\_centers\_)
mbk\_means\_cluster\_centers \= mbk.cluster\_centers\_\[order\]

k\_means\_labels \= [pairwise\_distances\_argmin](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "sklearn.metrics.pairwise_distances_argmin")
(X, k\_means\_cluster\_centers)
mbk\_means\_labels \= [pairwise\_distances\_argmin](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "sklearn.metrics.pairwise_distances_argmin")
(X, mbk\_means\_cluster\_centers)

Copy to clipboard

Plotting the results[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html#plotting-the-results "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 3))
fig.subplots\_adjust(left\=0.02, right\=0.98, bottom\=0.05, top\=0.9)
colors \= \["#4EACC5", "#FF9C34", "#4E9A06"\]

\# KMeans
ax \= fig.add\_subplot(1, 3, 1)
for k, col in zip(range(n\_clusters), colors):
    my\_members \= k\_means\_labels \== k
    cluster\_center \= k\_means\_cluster\_centers\[k\]
    ax.plot(X\[my\_members, 0\], X\[my\_members, 1\], "w", markerfacecolor\=col, marker\=".")
    ax.plot(
        cluster\_center\[0\],
        cluster\_center\[1\],
        "o",
        markerfacecolor\=col,
        markeredgecolor\="k",
        markersize\=6,
    )
ax.set\_title("KMeans")
ax.set\_xticks(())
ax.set\_yticks(())
[plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(\-3.5, 1.8, "train time: %.2fs\\ninertia: %f" % (t\_batch, k\_means.inertia\_))

\# MiniBatchKMeans
ax \= fig.add\_subplot(1, 3, 2)
for k, col in zip(range(n\_clusters), colors):
    my\_members \= mbk\_means\_labels \== k
    cluster\_center \= mbk\_means\_cluster\_centers\[k\]
    ax.plot(X\[my\_members, 0\], X\[my\_members, 1\], "w", markerfacecolor\=col, marker\=".")
    ax.plot(
        cluster\_center\[0\],
        cluster\_center\[1\],
        "o",
        markerfacecolor\=col,
        markeredgecolor\="k",
        markersize\=6,
    )
ax.set\_title("MiniBatchKMeans")
ax.set\_xticks(())
ax.set\_yticks(())
[plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(\-3.5, 1.8, "train time: %.2fs\\ninertia: %f" % (t\_mini\_batch, mbk.inertia\_))

\# Initialize the different array to all False
different \= mbk\_means\_labels \== 4
ax \= fig.add\_subplot(1, 3, 3)

for k in range(n\_clusters):
    different += (k\_means\_labels \== k) != (mbk\_means\_labels \== k)

identical \= [np.logical\_not](https://numpy.org/doc/stable/reference/generated/numpy.logical_not.html#numpy.logical_not "numpy.logical_not")
(different)
ax.plot(X\[identical, 0\], X\[identical, 1\], "w", markerfacecolor\="#bbbbbb", marker\=".")
ax.plot(X\[different, 0\], X\[different, 1\], "w", markerfacecolor\="m", marker\=".")
ax.set\_title("Difference")
ax.set\_xticks(())
ax.set\_yticks(())

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![KMeans, MiniBatchKMeans, Difference](https://scikit-learn.org/stable/_images/sphx_glr_plot_mini_batch_kmeans_001.png)

**Total running time of the script:** (0 minutes 0.196 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_mini_batch_kmeans.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_mini_batch_kmeans.ipynb)

[`Download Jupyter notebook: plot_mini_batch_kmeans.ipynb`](https://scikit-learn.org/stable/_downloads/1f948ff6f5face5a362672c4e36dd01e/plot_mini_batch_kmeans.ipynb)

[`Download Python source code: plot_mini_batch_kmeans.py`](https://scikit-learn.org/stable/_downloads/3735f7086bbd0007cd42d2c1f2b96f47/plot_mini_batch_kmeans.py)

[`Download zipped: plot_mini_batch_kmeans.zip`](https://scikit-learn.org/stable/_downloads/5c5a28f56fff2d59a099a9617c8f1b5a/plot_mini_batch_kmeans.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_stability_low_dim_dense_thumb.png)

[Empirical evaluation of the impact of k-means initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)

Empirical evaluation of the impact of k-means initialization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_birch_vs_minibatchkmeans_thumb.png)

[Compare BIRCH and MiniBatchKMeans](https://scikit-learn.org/stable/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html)

Compare BIRCH and MiniBatchKMeans

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mean_shift_thumb.png)

[A demo of the mean-shift clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html)

A demo of the mean-shift clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_digits_thumb.png)

[A demo of K-Means clustering on the handwritten digits data](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html)

A demo of K-Means clustering on the handwritten digits data

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/3735f7086bbd0007cd42d2c1f2b96f47/plot_mini_batch_kmeans.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/1f948ff6f5face5a362672c4e36dd01e/plot_mini_batch_kmeans.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/5c5a28f56fff2d59a099a9617c8f1b5a/plot_mini_batch_kmeans.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_mini_batch_kmeans.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_mini_batch_kmeans.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)