[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html#sphx-glr-download-auto-examples-cluster-plot-birch-vs-minibatchkmeans-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Compare BIRCH and MiniBatchKMeans[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html#compare-birch-and-minibatchkmeans "Link to this heading")

========================================================================================================================================================================================

This example compares the timing of BIRCH (with and without the global clustering step) and MiniBatchKMeans on a synthetic dataset having 25,000 samples and 2 features generated using make\_blobs.

Both `MiniBatchKMeans` and `BIRCH` are very scalable algorithms and could run efficiently on hundreds of thousands or even millions of datapoints. We chose to limit the dataset size of this example in the interest of keeping our Continuous Integration resource usage reasonable but the interested reader might enjoy editing this script to rerun it with a larger value for `n_samples`.

If `n_clusters` is set to None, the data is reduced from 25,000 samples to a set of 158 clusters. This can be viewed as a preprocessing step before the final (global) clustering step that further reduces these 158 clusters to 100 clusters.

![BIRCH without global clustering, BIRCH with global clustering, MiniBatchKMeans](https://scikit-learn.org/stable/_images/sphx_glr_plot_birch_vs_minibatchkmeans_001.png)

BIRCH without global clustering as the final step took 0.54 seconds
n\_clusters : 158
BIRCH with global clustering as the final step took 0.51 seconds
n\_clusters : 100
Time taken to run MiniBatchKMeans 0.22 seconds

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

from itertools import [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle")
from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
from joblib import [cpu\_count](https://joblib.readthedocs.io/en/latest/generated/joblib.cpu_count.html#joblib.cpu_count "joblib.cpu_count")

from sklearn.cluster import [Birch](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
, [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")

\# Generate centers for the blobs so that it forms a 10 X 10 grid.
xx \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-22, 22, 10)
yy \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-22, 22, 10)
xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(xx, yy)
n\_centers \= [np.hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
(([np.ravel](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")
(xx)\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\], [np.ravel](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")
(yy)\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]))

\# Generate blobs to do a comparison between MiniBatchKMeans and BIRCH.
X, y \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=25000, centers\=n\_centers, random\_state\=0)

\# Use all colors that matplotlib provides by default.
colors\_ \= [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle")
(colors.cnames.keys())

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(12, 4))
fig.subplots\_adjust(left\=0.04, right\=0.98, bottom\=0.1, top\=0.9)

\# Compute clustering with BIRCH with and without the final clustering step
\# and plot.
birch\_models \= \[\
    [Birch](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")\
(threshold\=1.7, n\_clusters\=None),\
    [Birch](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")\
(threshold\=1.7, n\_clusters\=100),\
\]
final\_step \= \["without global clustering", "with global clustering"\]

for ind, (birch\_model, info) in enumerate(zip(birch\_models, final\_step)):
    t \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    birch\_model.fit(X)
    print("BIRCH %s as the final step took %0.2f seconds" % (info, ([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t)))

    \# Plot result
    labels \= birch\_model.labels\_
    centroids \= birch\_model.subcluster\_centers\_
    n\_clusters \= [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(labels).size
    print("n\_clusters : %d" % n\_clusters)

    ax \= fig.add\_subplot(1, 3, ind + 1)
    for this\_centroid, k, col in zip(centroids, range(n\_clusters), colors\_):
        mask \= labels \== k
        ax.scatter(X\[mask, 0\], X\[mask, 1\], c\="w", edgecolor\=col, marker\=".", alpha\=0.5)
        if birch\_model.n\_clusters is None:
            ax.scatter(this\_centroid\[0\], this\_centroid\[1\], marker\="+", c\="k", s\=25)
    ax.set\_ylim(\[\-25, 25\])
    ax.set\_xlim(\[\-25, 25\])
    ax.set\_autoscaley\_on(False)
    ax.set\_title("BIRCH %s" % info)

\# Compute clustering with MiniBatchKMeans.
mbk \= [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
(
    init\="k-means++",
    n\_clusters\=100,
    batch\_size\=256 \* [cpu\_count](https://joblib.readthedocs.io/en/latest/generated/joblib.cpu_count.html#joblib.cpu_count "joblib.cpu_count")
(),
    n\_init\=10,
    max\_no\_improvement\=10,
    verbose\=0,
    random\_state\=0,
)
t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
mbk.fit(X)
t\_mini\_batch \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
print("Time taken to run MiniBatchKMeans %0.2f seconds" % t\_mini\_batch)
mbk\_means\_labels\_unique \= [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(mbk.labels\_)

ax \= fig.add\_subplot(1, 3, 3)
for this\_centroid, k, col in zip(mbk.cluster\_centers\_, range(n\_clusters), colors\_):
    mask \= mbk.labels\_ \== k
    ax.scatter(X\[mask, 0\], X\[mask, 1\], marker\=".", c\="w", edgecolor\=col, alpha\=0.5)
    ax.scatter(this\_centroid\[0\], this\_centroid\[1\], marker\="+", c\="k", s\=25)
ax.set\_xlim(\[\-25, 25\])
ax.set\_ylim(\[\-25, 25\])
ax.set\_title("MiniBatchKMeans")
ax.set\_autoscaley\_on(False)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 2.700 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_birch_vs_minibatchkmeans.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_birch_vs_minibatchkmeans.ipynb)

[`Download Jupyter notebook: plot_birch_vs_minibatchkmeans.ipynb`](https://scikit-learn.org/stable/_downloads/a373b9fdc21005d9a66ecf3df90eb49a/plot_birch_vs_minibatchkmeans.ipynb)

[`Download Python source code: plot_birch_vs_minibatchkmeans.py`](https://scikit-learn.org/stable/_downloads/e3c29fcee17ffb4a67e11b147b8a86bb/plot_birch_vs_minibatchkmeans.py)

[`Download zipped: plot_birch_vs_minibatchkmeans.zip`](https://scikit-learn.org/stable/_downloads/1003e2b79d0fc902b8f0cbd0f449fd06/plot_birch_vs_minibatchkmeans.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mini_batch_kmeans_thumb.png)

[Comparison of the K-Means and MiniBatchKMeans clustering algorithms](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html)

Comparison of the K-Means and MiniBatchKMeans clustering algorithms

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_stability_low_dim_dense_thumb.png)

[Empirical evaluation of the impact of k-means initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)

Empirical evaluation of the impact of k-means initialization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_clustering_metrics_thumb.png)

[Agglomerative clustering with different metrics](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_clustering_metrics.html)

Agglomerative clustering with different metrics

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/e3c29fcee17ffb4a67e11b147b8a86bb/plot_birch_vs_minibatchkmeans.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/a373b9fdc21005d9a66ecf3df90eb49a/plot_birch_vs_minibatchkmeans.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/1003e2b79d0fc902b8f0cbd0f449fd06/plot_birch_vs_minibatchkmeans.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_birch_vs_minibatchkmeans.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_birch_vs_minibatchkmeans.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)