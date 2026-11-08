[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_hdbscan.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_hdbscan.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_hdbscan.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_hdbscan.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_hdbscan.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_hdbscan.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html#sphx-glr-download-auto-examples-cluster-plot-hdbscan-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Demo of HDBSCAN clustering algorithm[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html#demo-of-hdbscan-clustering-algorithm "Link to this heading")

=============================================================================================================================================================================

In this demo we will take a look at [`cluster.HDBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
 from the perspective of generalizing the [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
 algorithm. We’ll compare both algorithms on specific datasets. Finally we’ll evaluate HDBSCAN’s sensitivity to certain hyperparameters.

We first define a couple utility functions for convenience.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import [DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
, [HDBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")

def plot(X, labels, probabilities\=None, parameters\=None, ground\_truth\=False, ax\=None):
    if ax is None:
        \_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(10, 4))
    labels \= labels if labels is not None else [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(X.shape\[0\])
    probabilities \= probabilities if probabilities is not None else [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(X.shape\[0\])
    \# Black removed and is used for noise instead.
    unique\_labels \= set(labels)
    colors \= \[plt.cm.Spectral(each) for each in [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
(0, 1, len(unique\_labels))\]
    \# The probability of a point belonging to its labeled cluster determines
    \# the size of its marker
    proba\_map \= {idx: probabilities\[idx\] for idx in range(len(labels))}
    for k, col in zip(unique\_labels, colors):
        if k \== \-1:
            \# Black used for noise.
            col \= \[0, 0, 0, 1\]

        class\_index \= (labels \== k).nonzero()\[0\]
        for ci in class\_index:
            ax.plot(
                X\[ci, 0\],
                X\[ci, 1\],
                "x" if k \== \-1 else "o",
                markerfacecolor\=tuple(col),
                markeredgecolor\="k",
                markersize\=4 if k \== \-1 else 1 + 5 \* proba\_map\[ci\],
            )
    n\_clusters\_ \= len(set(labels)) \- (1 if \-1 in labels else 0)
    preamble \= "True" if ground\_truth else "Estimated"
    title \= f"{preamble} number of clusters: {n\_clusters\_}"
    if parameters is not None:
        parameters\_str \= ", ".join(f"{k}\={v}" for k, v in parameters.items())
        title += f" | {parameters\_str}"
    ax.set\_title(title)
    [plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

Generate sample data[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html#generate-sample-data "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

One of the greatest advantages of HDBSCAN over DBSCAN is its out-of-the-box robustness. It’s especially remarkable on heterogeneous mixtures of data. Like DBSCAN, it can model arbitrary shapes and distributions, however unlike DBSCAN it does not require specification of an arbitrary and sensitive `eps` hyperparameter.

For example, below we generate a dataset from a mixture of three bi-dimensional and isotropic Gaussian distributions.

centers \= \[\[1, 1\], \[\-1, \-1\], \[1.5, \-1.5\]\]
X, labels\_true \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(
    n\_samples\=750, centers\=centers, cluster\_std\=\[0.4, 0.1, 0.75\], random\_state\=0
)
plot(X, labels\=labels\_true, ground\_truth\=True)

Copy to clipboard

![True number of clusters: 3](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_001.png)

Scale Invariance[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html#scale-invariance "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

It’s worth remembering that, while DBSCAN provides a default value for `eps` parameter, it hardly has a proper default value and must be tuned for the specific dataset at use.

As a simple demonstration, consider the clustering for a `eps` value tuned for one dataset, and clustering obtained with the same value but applied to rescaled versions of the dataset.

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 1, figsize\=(10, 12))
dbs \= [DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
(eps\=0.3)
for idx, scale in enumerate(\[1, 0.5, 3\]):
    dbs.fit(X \* scale)
    plot(X \* scale, dbs.labels\_, parameters\={"scale": scale, "eps": 0.3}, ax\=axes\[idx\])

Copy to clipboard

![Estimated number of clusters: 3 | scale=1, eps=0.3, Estimated number of clusters: 1 | scale=0.5, eps=0.3, Estimated number of clusters: 11 | scale=3, eps=0.3](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_002.png)

Indeed, in order to maintain the same results we would have to scale `eps` by the same factor.

fig, axis \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 1, figsize\=(12, 5))
dbs \= [DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
(eps\=0.9).fit(3 \* X)
plot(3 \* X, dbs.labels\_, parameters\={"scale": 3, "eps": 0.9}, ax\=axis)

Copy to clipboard

![Estimated number of clusters: 3 | scale=3, eps=0.9](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_003.png)

While standardizing data (e.g. using [`sklearn.preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
) helps mitigate this problem, great care must be taken to select the appropriate value for `eps`.

HDBSCAN is much more robust in this sense: HDBSCAN can be seen as clustering over all possible values of `eps` and extracting the best clusters from all possible clusters (see [User Guide](https://scikit-learn.org/stable/modules/clustering.html#hdbscan)
). One immediate advantage is that HDBSCAN is scale-invariant.

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 1, figsize\=(10, 12))
hdb \= [HDBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
(copy\=True)
for idx, scale in enumerate(\[1, 0.5, 3\]):
    hdb.fit(X \* scale)
    plot(
        X \* scale,
        hdb.labels\_,
        hdb.probabilities\_,
        ax\=axes\[idx\],
        parameters\={"scale": scale},
    )

Copy to clipboard

![Estimated number of clusters: 3 | scale=1, Estimated number of clusters: 3 | scale=0.5, Estimated number of clusters: 3 | scale=3](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_004.png)

Multi-Scale Clustering[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html#multi-scale-clustering "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

HDBSCAN is much more than scale invariant though – it is capable of multi-scale clustering, which accounts for clusters with varying density. Traditional DBSCAN assumes that any potential clusters are homogeneous in density. HDBSCAN is free from such constraints. To demonstrate this we consider the following dataset

centers \= \[\[\-0.85, \-0.85\], \[\-0.85, 0.85\], \[3, 3\], \[3, \-3\]\]
X, labels\_true \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(
    n\_samples\=750, centers\=centers, cluster\_std\=\[0.2, 0.35, 1.35, 1.35\], random\_state\=0
)
plot(X, labels\=labels\_true, ground\_truth\=True)

Copy to clipboard

![True number of clusters: 4](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_005.png)

This dataset is more difficult for DBSCAN due to the varying densities and spatial separation:

*   If `eps` is too large then we risk falsely clustering the two dense clusters as one since their mutual reachability will extend clusters.
    
*   If `eps` is too small, then we risk fragmenting the sparser clusters into many false clusters.
    

Not to mention this requires manually tuning choices of `eps` until we find a tradeoff that we are comfortable with.

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1, figsize\=(10, 8))
params \= {"eps": 0.7}
dbs \= [DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
(\*\*params).fit(X)
plot(X, dbs.labels\_, parameters\=params, ax\=axes\[0\])
params \= {"eps": 0.3}
dbs \= [DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
(\*\*params).fit(X)
plot(X, dbs.labels\_, parameters\=params, ax\=axes\[1\])

Copy to clipboard

![Estimated number of clusters: 3 | eps=0.7, Estimated number of clusters: 14 | eps=0.3](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_006.png)

To properly cluster the two dense clusters, we would need a smaller value of epsilon, however at `eps=0.3` we are already fragmenting the sparse clusters, which would only become more severe as we decrease epsilon. Indeed it seems that DBSCAN is incapable of simultaneously separating the two dense clusters while preventing the sparse clusters from fragmenting. Let’s compare with HDBSCAN.

hdb \= [HDBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
(copy\=True).fit(X)
plot(X, hdb.labels\_, hdb.probabilities\_)

Copy to clipboard

![Estimated number of clusters: 4](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_007.png)

HDBSCAN is able to adapt to the multi-scale structure of the dataset without requiring parameter tuning. While any sufficiently interesting dataset will require tuning, this case demonstrates that HDBSCAN can yield qualitatively better classes of clusterings without users’ intervention which are inaccessible via DBSCAN.

Hyperparameter Robustness[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html#hyperparameter-robustness "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

Ultimately tuning will be an important step in any real world application, so let’s take a look at some of the most important hyperparameters for HDBSCAN. While HDBSCAN is free from the `eps` parameter of DBSCAN, it does still have some hyperparameters like `min_cluster_size` and `min_samples` which tune its results regarding density. We will however see that HDBSCAN is relatively robust to various real world examples thanks to those parameters whose clear meaning helps tuning them.

### `min_cluster_size`[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html#min-cluster-size "Link to this heading")

`min_cluster_size` is the minimum number of samples in a group for that group to be considered a cluster.

Clusters smaller than the ones of this size will be left as noise. The default value is 5. This parameter is generally tuned to larger values as needed. Smaller values will likely to lead to results with fewer points labeled as noise. However values which too small will lead to false sub-clusters being picked up and preferred. Larger values tend to be more robust with respect to noisy datasets, e.g. high-variance clusters with significant overlap.

PARAM \= ({"min\_cluster\_size": 5}, {"min\_cluster\_size": 3}, {"min\_cluster\_size": 25})
fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 1, figsize\=(10, 12))
for i, param in enumerate(PARAM):
    hdb \= [HDBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
(copy\=True, \*\*param).fit(X)
    labels \= hdb.labels\_

    plot(X, labels, hdb.probabilities\_, param, ax\=axes\[i\])

Copy to clipboard

![Estimated number of clusters: 4 | min_cluster_size=5, Estimated number of clusters: 90 | min_cluster_size=3, Estimated number of clusters: 4 | min_cluster_size=25](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_008.png)

### `min_samples`[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html#min-samples "Link to this heading")

`min_samples` is the number of samples in a neighborhood for a point to be considered as a core point, including the point itself. `min_samples` defaults to `min_cluster_size`. Similarly to `min_cluster_size`, larger values for `min_samples` increase the model’s robustness to noise, but risks ignoring or discarding potentially valid but small clusters. `min_samples` better be tuned after finding a good value for `min_cluster_size`.

PARAM \= (
    {"min\_cluster\_size": 20, "min\_samples": 5},
    {"min\_cluster\_size": 20, "min\_samples": 3},
    {"min\_cluster\_size": 20, "min\_samples": 25},
)
fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 1, figsize\=(10, 12))
for i, param in enumerate(PARAM):
    hdb \= [HDBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
(copy\=True, \*\*param).fit(X)
    labels \= hdb.labels\_

    plot(X, labels, hdb.probabilities\_, param, ax\=axes\[i\])

Copy to clipboard

![Estimated number of clusters: 4 | min_cluster_size=20, min_samples=5, Estimated number of clusters: 4 | min_cluster_size=20, min_samples=3, Estimated number of clusters: 4 | min_cluster_size=20, min_samples=25](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_009.png)

### `dbscan_clustering`[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html#dbscan-clustering "Link to this heading")

During `fit`, `HDBSCAN` builds a single-linkage tree which encodes the clustering of all points across all values of [`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
’s `eps` parameter. We can thus plot and evaluate these clusterings efficiently without fully recomputing intermediate values such as core-distances, mutual-reachability, and the minimum spanning tree. All we need to do is specify the `cut_distance` (equivalent to `eps`) we want to cluster with.

PARAM \= (
    {"cut\_distance": 0.1},
    {"cut\_distance": 0.5},
    {"cut\_distance": 1.0},
)
hdb \= [HDBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
(copy\=True)
hdb.fit(X)
fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(len(PARAM), 1, figsize\=(10, 12))
for i, param in enumerate(PARAM):
    labels \= hdb.dbscan\_clustering(\*\*param)

    plot(X, labels, hdb.probabilities\_, param, ax\=axes\[i\])

Copy to clipboard

![Estimated number of clusters: 3 | cut_distance=0.1, Estimated number of clusters: 3 | cut_distance=0.5, Estimated number of clusters: 1 | cut_distance=1.0](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_010.png)

**Total running time of the script:** (0 minutes 12.603 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_hdbscan.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_hdbscan.ipynb)

[`Download Jupyter notebook: plot_hdbscan.ipynb`](https://scikit-learn.org/stable/_downloads/f92fcbee358b8c7063475033e6e9cde0/plot_hdbscan.ipynb)

[`Download Python source code: plot_hdbscan.py`](https://scikit-learn.org/stable/_downloads/ddc1f7dc483de25e01897025606d794f/plot_hdbscan.py)

[`Download zipped: plot_hdbscan.zip`](https://scikit-learn.org/stable/_downloads/5318b93274c12da04cc124d3efa940af/plot_hdbscan.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_3_0_thumb.png)

[Release Highlights for scikit-learn 1.3](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)

Release Highlights for scikit-learn 1.3

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dbscan_thumb.png)

[Demo of DBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html)

Demo of DBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_thumb.png)

[The Johnson-Lindenstrauss bound for embedding with random projections](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)

The Johnson-Lindenstrauss bound for embedding with random projections

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/ddc1f7dc483de25e01897025606d794f/plot_hdbscan.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f92fcbee358b8c7063475033e6e9cde0/plot_hdbscan.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/5318b93274c12da04cc124d3efa940af/plot_hdbscan.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_hdbscan.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_hdbscan.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)