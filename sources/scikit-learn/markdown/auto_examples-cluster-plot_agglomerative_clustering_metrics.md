[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_clustering_metrics.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_agglomerative_clustering_metrics.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_clustering_metrics.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_agglomerative_clustering_metrics.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_agglomerative_clustering_metrics.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_agglomerative_clustering_metrics.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_agglomerative_clustering_metrics.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_agglomerative_clustering_metrics.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_clustering_metrics.html#sphx-glr-download-auto-examples-cluster-plot-agglomerative-clustering-metrics-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Agglomerative clustering with different metrics[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_clustering_metrics.html#agglomerative-clustering-with-different-metrics "Link to this heading")

============================================================================================================================================================================================================================

Demonstrates the effect of different metrics on the hierarchical clustering.

The example is engineered to show the effect of the choice of different metrics. It is applied to waveforms, which can be seen as high-dimensional vector. Indeed, the difference between metrics is usually more pronounced in high dimension (in particular for euclidean and cityblock).

We generate data from three groups of waveforms. Two of the waveforms (waveform 1 and waveform 2) are proportional one to the other. The cosine distance is invariant to a scaling of the data, as a result, it cannot distinguish these two waveforms. Thus even with no noise, clustering using this distance will not separate out waveform 1 and 2.

We add observation noise to these waveforms. We generate very sparse noise: only 6% of the time points contain noise. As a result, the l1 norm of this noise (ie “cityblock” distance) is much smaller than its l2 norm (“euclidean” distance). This can be seen on the inter-class distance matrices: the values on the diagonal, that characterize the spread of the class, are much bigger for the Euclidean distance than for the cityblock distance.

When we apply clustering to the data, we find that the clustering reflects what was in the distance matrices. Indeed, for the Euclidean distance, the classes are ill-separated because of the noise, and thus the clustering does not separate the waveforms. For the cityblock distance, the separation is good and the waveform classes are recovered. Finally, the cosine distance does not separate at all waveform 1 and 2, thus the clustering puts them in the same cluster.

*   ![Ground truth](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_clustering_metrics_001.png)
*   ![Interclass cosine distances](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_clustering_metrics_002.png)
*   ![Interclass euclidean distances](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_clustering_metrics_003.png)
*   ![Interclass cityblock distances](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_clustering_metrics_004.png)
*   ![AgglomerativeClustering(metric=cosine)](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_clustering_metrics_005.png)
*   ![AgglomerativeClustering(metric=euclidean)](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_clustering_metrics_006.png)
*   ![AgglomerativeClustering(metric=cityblock)](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_clustering_metrics_007.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.patheffects as PathEffects
import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
from sklearn.metrics import [pairwise\_distances](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)

\# Generate waveform data
n\_features \= 2000
t \= [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, n\_features)

def sqr(x):
    return [np.sign](https://numpy.org/doc/stable/reference/generated/numpy.sign.html#numpy.sign "numpy.sign")
([np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(x))

X \= list()
y \= list()
for i, (phi, a) in enumerate(\[(0.5, 0.15), (0.5, 0.6), (0.3, 0.2)\]):
    for \_ in range(30):
        phase\_noise \= 0.01 \* [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
()
        amplitude\_noise \= 0.04 \* [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
()
        additional\_noise \= 1 \- 2 \* [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(n\_features)
        \# Make the noise sparse
        additional\_noise\[np.abs(additional\_noise) < 0.997\] \= 0

        X.append(
            12
            \* (
                (a + amplitude\_noise) \* (sqr(6 \* (t + phi + phase\_noise)))
                + additional\_noise
            )
        )
        y.append(i)

X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(X)
y \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(y)

n\_clusters \= 3

labels \= ("Waveform 1", "Waveform 2", "Waveform 3")

colors \= \["#f7bd01", "#377eb8", "#f781bf"\]

\# Plot the ground-truth labelling
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
(\[0, 0, 1, 1\])
for l, color, n in zip(range(n\_clusters), colors, labels):
    lines \= [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\[y \== l\].T, c\=color, alpha\=0.5)
    lines\[0\].set\_label(n)

[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="best")

[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("off")
[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
("Ground truth", size\=20, y\=1)

\# Plot the distances
for index, metric in enumerate(\["cosine", "euclidean", "cityblock"\]):
    avg\_dist \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((n\_clusters, n\_clusters))
    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5, 4.5))
    for i in range(n\_clusters):
        for j in range(n\_clusters):
            avg\_dist\[i, j\] \= [pairwise\_distances](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
(
                X\[y \== i\], X\[y \== j\], metric\=metric
            ).mean()
    avg\_dist /= avg\_dist.max()
    for i in range(n\_clusters):
        for j in range(n\_clusters):
            t \= [plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(
                i,
                j,
                "%5.3f" % avg\_dist\[i, j\],
                verticalalignment\="center",
                horizontalalignment\="center",
            )
            t.set\_path\_effects(
                \[[PathEffects.withStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withStroke "matplotlib.patheffects.withStroke")\
(linewidth\=5, foreground\="w", alpha\=0.5)\]
            )

    [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(avg\_dist, interpolation\="nearest", cmap\="cividis", vmin\=0)
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(range(n\_clusters), labels, rotation\=45)
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(range(n\_clusters), labels)
    [plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
()
    [plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
("Interclass %s distances" % metric, size\=18, y\=1)
    [plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

\# Plot clustering results
for index, metric in enumerate(\["cosine", "euclidean", "cityblock"\]):
    model \= [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
(
        n\_clusters\=n\_clusters, linkage\="average", metric\=metric
    )
    model.fit(X)
    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
    [plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
(\[0, 0, 1, 1\])
    for l, color in zip([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(model.n\_clusters), colors):
        [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\[model.labels\_ \== l\].T, c\=color, alpha\=0.5)
    [plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
    [plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("off")
    [plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
("AgglomerativeClustering(metric=%s)" % metric, size\=20, y\=1)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 1.106 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_agglomerative_clustering_metrics.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_agglomerative_clustering_metrics.ipynb)

[`Download Jupyter notebook: plot_agglomerative_clustering_metrics.ipynb`](https://scikit-learn.org/stable/_downloads/e7d5500e87a046a110ca0daebd702588/plot_agglomerative_clustering_metrics.ipynb)

[`Download Python source code: plot_agglomerative_clustering_metrics.py`](https://scikit-learn.org/stable/_downloads/bc88e7ec572d6d2d2ff19cf0d75265c9/plot_agglomerative_clustering_metrics.py)

[`Download zipped: plot_agglomerative_clustering_metrics.zip`](https://scikit-learn.org/stable/_downloads/eeee1f686d08b12fa5d592cccddded23/plot_agglomerative_clustering_metrics.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_ward_segmentation_thumb.png)

[A demo of structured Ward hierarchical clustering on an image of coins](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html)

A demo of structured Ward hierarchical clustering on an image of coins

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linkage_comparison_thumb.png)

[Comparing different hierarchical linkage methods on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html)

Comparing different hierarchical linkage methods on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ward_structured_vs_unstructured_thumb.png)

[Hierarchical clustering with and without structure](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)

Hierarchical clustering with and without structure

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_silhouette_analysis_thumb.png)

[Selecting the number of clusters with silhouette analysis on KMeans clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)

Selecting the number of clusters with silhouette analysis on KMeans clustering

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/bc88e7ec572d6d2d2ff19cf0d75265c9/plot_agglomerative_clustering_metrics.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/e7d5500e87a046a110ca0daebd702588/plot_agglomerative_clustering_metrics.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/eeee1f686d08b12fa5d592cccddded23/plot_agglomerative_clustering_metrics.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_agglomerative_clustering_metrics.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_agglomerative_clustering_metrics.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)