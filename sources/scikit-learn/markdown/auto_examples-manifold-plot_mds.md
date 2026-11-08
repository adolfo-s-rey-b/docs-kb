[Skip to main content](https://scikit-learn.org/stable/auto_examples/manifold/plot_mds.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/manifold/plot_mds.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/manifold/plot_mds.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/manifold/plot_mds.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/manifold/plot_mds.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/manifold/plot_mds.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/manifold/plot_mds.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/manifold/plot_mds.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/manifold/plot_mds.html#sphx-glr-download-auto-examples-manifold-plot-mds-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Multi-dimensional scaling[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_mds.html#multi-dimensional-scaling "Link to this heading")

====================================================================================================================================================

An illustration of the metric and non-metric MDS on generated noisy data.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Dataset preparation[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_mds.html#dataset-preparation "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

We start by uniformly generating 20 points in a 2D space.

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.collections import [LineCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")

from sklearn import manifold
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
from sklearn.metrics import euclidean\_distances

\# Generate the data
EPSILON \= [np.finfo](https://numpy.org/doc/stable/reference/generated/numpy.finfo.html#numpy.finfo "numpy.finfo")
([np.float32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
).eps
n\_samples \= 20
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(seed\=3)
X\_true \= rng.randint(0, 20, 2 \* n\_samples).astype(float)
X\_true \= X\_true.reshape((n\_samples, 2))

\# Center the data
X\_true \-= X\_true.mean()

Copy to clipboard

Now we compute pairwise distances between all points and add a small amount of noise to the distance matrix. We make sure to keep the noisy distance matrix symmetric.

\# Compute pairwise Euclidean distances
distances \= euclidean\_distances(X\_true)

\# Add noise to the distances
noise \= rng.rand(n\_samples, n\_samples)
noise \= noise + noise.T
[np.fill\_diagonal](https://numpy.org/doc/stable/reference/generated/numpy.fill_diagonal.html#numpy.fill_diagonal "numpy.fill_diagonal")
(noise, 0)
distances += noise

Copy to clipboard

Here we compute metric, non-metric, and classical MDS of the noisy distance matrix.

mds \= [manifold.MDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
(
    n\_components\=2,
    max\_iter\=3000,
    eps\=1e-9,
    n\_init\=1,
    random\_state\=42,
    metric\="precomputed",
    n\_jobs\=1,
    init\="classical\_mds",
)
X\_mds \= mds.fit(distances).embedding\_

nmds \= [manifold.MDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
(
    n\_components\=2,
    metric\_mds\=False,
    max\_iter\=3000,
    eps\=1e-12,
    metric\="precomputed",
    random\_state\=42,
    n\_jobs\=1,
    n\_init\=1,
    init\="classical\_mds",
)
X\_nmds \= nmds.fit\_transform(distances)

cmds \= [manifold.ClassicalMDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#sklearn.manifold.ClassicalMDS "sklearn.manifold.ClassicalMDS")
(
    n\_components\=2,
    metric\="precomputed",
)
X\_cmds \= cmds.fit\_transform(distances)

Copy to clipboard

Rescaling the non-metric MDS solution to match the spread of the original data.

X\_nmds \*= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
((X\_true\*\*2).sum()) / [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
((X\_nmds\*\*2).sum())

Copy to clipboard

To make the visual comparisons easier, we rotate the original data and all MDS solutions to their PCA axes. And flip horizontal and vertical MDS axes, if needed, to match the original data orientation.

\# Rotate the data (CMDS does not need to be rotated, it is inherently PCA-aligned)
pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=2)
X\_true \= pca.fit\_transform(X\_true)
X\_mds \= pca.fit\_transform(X\_mds)
X\_nmds \= pca.fit\_transform(X\_nmds)

\# Align the sign of PCs
for i in \[0, 1\]:
    if [np.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")
(X\_mds\[:, i\], X\_true\[:, i\])\[0, 1\] < 0:
        X\_mds\[:, i\] \*= \-1
    if [np.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")
(X\_nmds\[:, i\], X\_true\[:, i\])\[0, 1\] < 0:
        X\_nmds\[:, i\] \*= \-1
    if [np.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")
(X\_cmds\[:, i\], X\_true\[:, i\])\[0, 1\] < 0:
        X\_cmds\[:, i\] \*= \-1

Copy to clipboard

Finally, we plot the original data and all MDS reconstructions.

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(1)
ax \= [plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
(\[0.0, 0.0, 1.0, 1.0\])

s \= 100
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_true\[:, 0\], X\_true\[:, 1\], color\="navy", s\=s, lw\=0, label\="True Position")
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_mds\[:, 0\], X\_mds\[:, 1\], color\="turquoise", s\=s, lw\=0, label\="MDS")
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    X\_nmds\[:, 0\], X\_nmds\[:, 1\], color\="darkorange", s\=s, lw\=0, label\="Non-metric MDS"
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    X\_cmds\[:, 0\], X\_cmds\[:, 1\], color\="lightcoral", s\=s, lw\=0, label\="Classical MDS"
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(scatterpoints\=1, loc\="best", shadow\=False)

\# Plot the edges
start\_idx, end\_idx \= X\_mds.nonzero()
\# a sequence of (\*line0\*, \*line1\*, \*line2\*), where::
\#            linen = (x0, y0), (x1, y1), ... (xm, ym)
segments \= \[\
    \[X\_true\[i, :\], X\_true\[j, :\]\] for i in range(len(X\_true)) for j in range(len(X\_true))\
\]
edges \= distances.max() / (distances + EPSILON) \* 100
[np.fill\_diagonal](https://numpy.org/doc/stable/reference/generated/numpy.fill_diagonal.html#numpy.fill_diagonal "numpy.fill_diagonal")
(edges, 0)
edges \= np.abs(edges)
lc \= [LineCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
(
    segments, zorder\=0, cmap\=plt.cm.Blues, norm\=plt.Normalize(0, edges.max())
)
lc.set\_array(edges.flatten())
lc.set\_linewidths([np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
(len(segments), 0.5))
ax.add\_collection(lc)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot mds](https://scikit-learn.org/stable/_images/sphx_glr_plot_mds_001.png)

**Total running time of the script:** (0 minutes 0.170 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo20.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/manifold/plot_mds.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo20.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/manifold/plot_mds.ipynb)

[`Download Jupyter notebook: plot_mds.ipynb`](https://scikit-learn.org/stable/_downloads/a9a5b8f39dd796eae478e4c9c39cd207/plot_mds.ipynb)

[`Download Python source code: plot_mds.py`](https://scikit-learn.org/stable/_downloads/d64ed0728005aaeba058d3ccec909e73/plot_mds.py)

[`Download zipped: plot_mds.zip`](https://scikit-learn.org/stable/_downloads/74b690b6fca856df4027d12c67c15acf/plot_mds.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_thumb.png)

[Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html)

Comparison of Manifold Learning methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_manifold_sphere_thumb.png)

[Manifold Learning methods on a severed sphere](https://scikit-learn.org/stable/auto_examples/manifold/plot_manifold_sphere.html)

Manifold Learning methods on a severed sphere

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_clustering_metrics_thumb.png)

[Agglomerative clustering with different metrics](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_clustering_metrics.html)

Agglomerative clustering with different metrics

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_thumb.png)

[The Johnson-Lindenstrauss bound for embedding with random projections](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)

The Johnson-Lindenstrauss bound for embedding with random projections

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/d64ed0728005aaeba058d3ccec909e73/plot_mds.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/a9a5b8f39dd796eae478e4c9c39cd207/plot_mds.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/74b690b6fca856df4027d12c67c15acf/plot_mds.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo20.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/manifold/plot_mds.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo20.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/manifold/plot_mds.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)