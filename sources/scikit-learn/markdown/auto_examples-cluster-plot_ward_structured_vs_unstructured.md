[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html#sphx-glr-download-auto-examples-cluster-plot-ward-structured-vs-unstructured-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Hierarchical clustering with and without structure[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html#hierarchical-clustering-with-and-without-structure "Link to this heading")

=================================================================================================================================================================================================================================

This example demonstrates hierarchical clustering with and without connectivity constraints. It shows the effect of imposing a connectivity graph to capture local structure in the data. Without connectivity constraints, the clustering is based purely on distance, while with constraints, the clustering respects local structure.

For more information, see [Hierarchical clustering](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)
.

There are two advantages of imposing connectivity. First, clustering with sparse connectivity matrices is faster in general.

Second, when using a connectivity matrix, single, average and complete linkage are unstable and tend to create a few clusters that grow very quickly. Indeed, average and complete linkage fight this percolation behavior by considering all the distances between two clusters when merging them (while single linkage exaggerates the behaviour by considering only the shortest distance between clusters). The connectivity graph breaks this mechanism for average and complete linkage, making them resemble the more brittle single linkage. This effect is more pronounced for very sparse graphs (try decreasing the number of neighbors in `kneighbors_graph`) and with complete linkage. In particular, having a very small number of neighbors in the graph, imposes a geometry that is close to that of single linkage, which is well known to have this percolation instability.

The effect of imposing connectivity is illustrated on two different but similar datasets which show a spiral structure. In the first example we build a Swiss roll dataset and run hierarchical clustering on the position of the data. Here, we compare unstructured Ward clustering with a structured variant that enforces k-Nearest Neighbors connectivity. In the second example we include the effects of applying a such a connectivity graph to single, average and complete linkage.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate the Swiss Roll dataset.[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html#generate-the-swiss-roll-dataset "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import time

from sklearn.cluster import [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
from sklearn.datasets import [make\_swiss\_roll](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#sklearn.datasets.make_swiss_roll "sklearn.datasets.make_swiss_roll")

n\_samples \= 1500
noise \= 0.05
X1, \_ \= [make\_swiss\_roll](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#sklearn.datasets.make_swiss_roll "sklearn.datasets.make_swiss_roll")
(n\_samples, noise\=noise)
X1\[:, 1\] \*= 0.5  \# Make the roll thinner

Copy to clipboard

Compute clustering without connectivity constraints[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html#compute-clustering-without-connectivity-constraints "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Compute unstructured hierarchical clustering...")
st \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
ward\_unstructured \= [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
(n\_clusters\=6, linkage\="ward").fit(X1)
elapsed\_time\_unstructured \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- st
label\_unstructured \= ward\_unstructured.labels\_
print(f"Elapsed time: {elapsed\_time\_unstructured:.2f}s")
print(f"Number of points: {label\_unstructured.size}")

Copy to clipboard

Compute unstructured hierarchical clustering...
Elapsed time: 0.04s
Number of points: 1500

Copy to clipboard

Plot unstructured clustering result

import matplotlib.pyplot as plt
import numpy as np

fig1 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
ax1 \= fig1.add\_subplot(111, projection\="3d", elev\=7, azim\=-80)
ax1.set\_position(\[0, 0, 0.95, 1\])
for l in [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(label\_unstructured):
    ax1.scatter(
        X1\[label\_unstructured \== l, 0\],
        X1\[label\_unstructured \== l, 1\],
        X1\[label\_unstructured \== l, 2\],
        color\=plt.cm.jet(float(l) / [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(label\_unstructured + 1)),
        s\=20,
        edgecolor\="k",
    )
\_ \= fig1.suptitle(
    f"Without connectivity constraints (time {elapsed\_time\_unstructured:.2f}s)"
)

Copy to clipboard

![Without connectivity constraints (time 0.04s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_ward_structured_vs_unstructured_001.png)

Compute clustering with connectivity constraints[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html#compute-clustering-with-connectivity-constraints "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.neighbors import [kneighbors\_graph](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html#sklearn.neighbors.kneighbors_graph "sklearn.neighbors.kneighbors_graph")

connectivity \= [kneighbors\_graph](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html#sklearn.neighbors.kneighbors_graph "sklearn.neighbors.kneighbors_graph")
(X1, n\_neighbors\=10, include\_self\=False)

print("Compute structured hierarchical clustering...")
st \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
ward\_structured \= [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
(
    n\_clusters\=6, connectivity\=connectivity, linkage\="ward"
).fit(X1)
elapsed\_time\_structured \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- st
label\_structured \= ward\_structured.labels\_
print(f"Elapsed time: {elapsed\_time\_structured:.2f}s")
print(f"Number of points: {label\_structured.size}")

Copy to clipboard

Compute structured hierarchical clustering...
Elapsed time: 0.05s
Number of points: 1500

Copy to clipboard

Plot structured clustering result

fig2 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
ax2 \= fig2.add\_subplot(111, projection\="3d", elev\=7, azim\=-80)
ax2.set\_position(\[0, 0, 0.95, 1\])
for l in [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(label\_structured):
    ax2.scatter(
        X1\[label\_structured \== l, 0\],
        X1\[label\_structured \== l, 1\],
        X1\[label\_structured \== l, 2\],
        color\=plt.cm.jet(float(l) / [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(label\_structured + 1)),
        s\=20,
        edgecolor\="k",
    )
\_ \= fig2.suptitle(
    f"With connectivity constraints (time {elapsed\_time\_structured:.2f}s)"
)

Copy to clipboard

![With connectivity constraints (time 0.05s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_ward_structured_vs_unstructured_002.png)

Generate 2D spiral dataset.[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html#generate-2d-spiral-dataset "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

n\_samples \= 1500
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)
t \= 1.5 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* (1 + 3 \* [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(1, n\_samples))
x \= t \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(t)
y \= t \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(t)

X2 \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
((x, y))
X2 += 0.7 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(2, n\_samples)
X2 \= X2.T

Copy to clipboard

Capture local connectivity using a graph[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html#capture-local-connectivity-using-a-graph "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Larger number of neighbors will give more homogeneous clusters to the cost of computation time. A very large number of neighbors gives more evenly distributed cluster sizes, but may not impose the local manifold structure of the data.

knn\_graph \= [kneighbors\_graph](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html#sklearn.neighbors.kneighbors_graph "sklearn.neighbors.kneighbors_graph")
(X2, 30, include\_self\=False)

Copy to clipboard

### Plot clustering with and without structure[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html#plot-clustering-with-and-without-structure "Link to this heading")

fig3 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 12))
subfigs \= fig3.subfigures(4, 1)
params \= \[\
    (None, 30),\
    (None, 3),\
    (knn\_graph, 30),\
    (knn\_graph, 3),\
\]

for subfig, (connectivity, n\_clusters) in zip(subfigs, params):
    axs \= subfig.subplots(1, 4, sharey\=True)
    for index, linkage in enumerate(("average", "complete", "ward", "single")):
        model \= [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
(
            linkage\=linkage, connectivity\=connectivity, n\_clusters\=n\_clusters
        )
        t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        model.fit(X2)
        elapsed\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
        axs\[index\].scatter(
            X2\[:, 0\], X2\[:, 1\], c\=model.labels\_, cmap\=plt.cm.nipy\_spectral
        )
        axs\[index\].set\_title(
            "linkage=%s\\n(time %.2fs)" % (linkage, elapsed\_time),
            fontdict\=dict(verticalalignment\="top"),
        )
        axs\[index\].set\_aspect("equal")
        axs\[index\].axis("off")

        subfig.subplots\_adjust(bottom\=0, top\=0.83, wspace\=0, left\=0, right\=1)
        subfig.suptitle(
            "n\_cluster=%i, connectivity=%r" % (n\_clusters, connectivity is not None),
            size\=17,
        )

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![linkage=average (time 0.04s), linkage=complete (time 0.03s), linkage=ward (time 0.04s), linkage=single (time 0.01s), linkage=average (time 0.04s), linkage=complete (time 0.03s), linkage=ward (time 0.04s), linkage=single (time 0.01s), linkage=average (time 0.10s), linkage=complete (time 0.10s), linkage=ward (time 0.13s), linkage=single (time 0.02s), linkage=average (time 0.10s), linkage=complete (time 0.10s), linkage=ward (time 0.14s), linkage=single (time 0.02s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_ward_structured_vs_unstructured_003.png)

**Total running time of the script:** (0 minutes 2.096 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_ward_structured_vs_unstructured.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_ward_structured_vs_unstructured.ipynb)

[`Download Jupyter notebook: plot_ward_structured_vs_unstructured.ipynb`](https://scikit-learn.org/stable/_downloads/e1d99a2f5c5c55550ce32108208f6477/plot_ward_structured_vs_unstructured.ipynb)

[`Download Python source code: plot_ward_structured_vs_unstructured.py`](https://scikit-learn.org/stable/_downloads/4b5360e26b661e574ee526b19eee216f/plot_ward_structured_vs_unstructured.py)

[`Download zipped: plot_ward_structured_vs_unstructured.zip`](https://scikit-learn.org/stable/_downloads/3d67d60c4ffe2f928db30cd3174e5389/plot_ward_structured_vs_unstructured.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_ward_segmentation_thumb.png)

[A demo of structured Ward hierarchical clustering on an image of coins](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html)

A demo of structured Ward hierarchical clustering on an image of coins

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linkage_comparison_thumb.png)

[Comparing different hierarchical linkage methods on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html)

Comparing different hierarchical linkage methods on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_linkage_thumb.png)

[Various Agglomerative Clustering on a 2D embedding of digits](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_linkage.html)

Various Agglomerative Clustering on a 2D embedding of digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/4b5360e26b661e574ee526b19eee216f/plot_ward_structured_vs_unstructured.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/e1d99a2f5c5c55550ce32108208f6477/plot_ward_structured_vs_unstructured.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/3d67d60c4ffe2f928db30cd3174e5389/plot_ward_structured_vs_unstructured.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_ward_structured_vs_unstructured.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_ward_structured_vs_unstructured.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)