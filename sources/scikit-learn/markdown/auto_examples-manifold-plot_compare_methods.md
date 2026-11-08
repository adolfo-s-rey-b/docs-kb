[Skip to main content](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/manifold/plot_compare_methods.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/manifold/plot_compare_methods.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/manifold/plot_compare_methods.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/manifold/plot_compare_methods.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/manifold/plot_compare_methods.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/manifold/plot_compare_methods.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html#sphx-glr-download-auto-examples-manifold-plot-compare-methods-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparison of Manifold Learning methods[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html#comparison-of-manifold-learning-methods "Link to this heading")

============================================================================================================================================================================================

An illustration of dimensionality reduction on the S-curve dataset with various manifold learning methods.

For a discussion and comparison of these algorithms, see the [manifold module page](https://scikit-learn.org/stable/modules/manifold.html#manifold)

For a similar example, where the methods are applied to a sphere dataset, see [Manifold Learning methods on a severed sphere](https://scikit-learn.org/stable/auto_examples/manifold/plot_manifold_sphere.html#sphx-glr-auto-examples-manifold-plot-manifold-sphere-py)

Note that the purpose of the MDS is to find a low-dimensional representation of the data (here 2D) in which the distances respect well the distances in the original high-dimensional space, unlike other manifold-learning algorithms, it does not seeks an isotropic representation of the data in the low-dimensional space.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Dataset preparation[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html#dataset-preparation "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

We start by generating the S-curve dataset.

import matplotlib.pyplot as plt

\# unused but required import for doing 3d projections with matplotlib < 3.2
import mpl\_toolkits.mplot3d  \# noqa: F401
from matplotlib import ticker

from sklearn import datasets, manifold

n\_samples \= 1500
S\_points, S\_color \= [datasets.make\_s\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_s_curve.html#sklearn.datasets.make_s_curve "sklearn.datasets.make_s_curve")
(n\_samples, random\_state\=0)

Copy to clipboard

Let’s look at the original data. Also define some helping functions, which we will use further on.

def plot\_3d(points, points\_color, title):
    x, y, z \= points.T

    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
        figsize\=(6, 6),
        facecolor\="white",
        tight\_layout\=True,
        subplot\_kw\={"projection": "3d"},
    )
    fig.suptitle(title, size\=16)
    col \= ax.scatter(x, y, z, c\=points\_color, s\=50, alpha\=0.8)
    ax.view\_init(azim\=-60, elev\=9)
    ax.xaxis.set\_major\_locator([ticker.MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(1))
    ax.yaxis.set\_major\_locator([ticker.MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(1))
    ax.zaxis.set\_major\_locator([ticker.MultipleLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MultipleLocator "matplotlib.ticker.MultipleLocator")
(1))

    fig.colorbar(col, ax\=ax, orientation\="horizontal", shrink\=0.6, aspect\=60, pad\=0.01)
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

def plot\_2d(points, points\_color, title):
    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(3, 3), facecolor\="white", constrained\_layout\=True)
    fig.suptitle(title, size\=16)
    add\_2d\_scatter(ax, points, points\_color)
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

def add\_2d\_scatter(ax, points, points\_color, title\=None):
    x, y \= points.T
    ax.scatter(x, y, c\=points\_color, s\=50, alpha\=0.8)
    ax.set\_title(title)
    ax.xaxis.set\_major\_formatter([ticker.NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
    ax.yaxis.set\_major\_formatter([ticker.NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())

plot\_3d(S\_points, S\_color, "Original S-curve samples")

Copy to clipboard

![Original S-curve samples](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_001.png)

Define algorithms for the manifold learning[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html#define-algorithms-for-the-manifold-learning "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Manifold learning is an approach to non-linear dimensionality reduction. Algorithms for this task are based on the idea that the dimensionality of many data sets is only artificially high.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/manifold.html#manifold)
.

n\_neighbors \= 12  \# neighborhood which is used to recover the locally linear structure
n\_components \= 2  \# number of coordinates for the manifold

Copy to clipboard

### Locally Linear Embeddings[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html#locally-linear-embeddings "Link to this heading")

Locally linear embedding (LLE) can be thought of as a series of local Principal Component Analyses which are globally compared to find the best non-linear embedding. Read more in the [User Guide](https://scikit-learn.org/stable/modules/manifold.html#locally-linear-embedding)
.

params \= {
    "n\_neighbors": n\_neighbors,
    "n\_components": n\_components,
    "eigen\_solver": "auto",
    "random\_state": 0,
}

lle\_standard \= [manifold.LocallyLinearEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
(method\="standard", \*\*params)
S\_standard \= lle\_standard.fit\_transform(S\_points)

lle\_ltsa \= [manifold.LocallyLinearEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
(method\="ltsa", \*\*params)
S\_ltsa \= lle\_ltsa.fit\_transform(S\_points)

lle\_hessian \= [manifold.LocallyLinearEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
(method\="hessian", \*\*params)
S\_hessian \= lle\_hessian.fit\_transform(S\_points)

lle\_mod \= [manifold.LocallyLinearEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
(method\="modified", \*\*params)
S\_mod \= lle\_mod.fit\_transform(S\_points)

Copy to clipboard

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
    nrows\=2, ncols\=2, figsize\=(7, 7), facecolor\="white", constrained\_layout\=True
)
fig.suptitle("Locally Linear Embeddings", size\=16)

lle\_methods \= \[\
    ("Standard locally linear embedding", S\_standard),\
    ("Local tangent space alignment", S\_ltsa),\
    ("Hessian eigenmap", S\_hessian),\
    ("Modified locally linear embedding", S\_mod),\
\]
for ax, method in zip(axs.flat, lle\_methods):
    name, points \= method
    add\_2d\_scatter(ax, points, S\_color, name)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Locally Linear Embeddings, Standard locally linear embedding, Local tangent space alignment, Hessian eigenmap, Modified locally linear embedding](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_002.png)

### Isomap Embedding[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html#isomap-embedding "Link to this heading")

Non-linear dimensionality reduction through Isometric Mapping. Isomap seeks a lower-dimensional embedding which maintains geodesic distances between all points. Read more in the [User Guide](https://scikit-learn.org/stable/modules/manifold.html#isomap)
.

isomap \= [manifold.Isomap](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
(n\_neighbors\=n\_neighbors, n\_components\=n\_components, p\=1)
S\_isomap \= isomap.fit\_transform(S\_points)

plot\_2d(S\_isomap, S\_color, "Isomap Embedding")

Copy to clipboard

![Isomap Embedding](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_003.png)

### Multidimensional scaling[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html#multidimensional-scaling "Link to this heading")

Multidimensional scaling (MDS) seeks a low-dimensional representation of the data in which the distances respect well the distances in the original high-dimensional space. Read more in the [User Guide](https://scikit-learn.org/stable/modules/manifold.html#multidimensional-scaling)
.

md\_scaling \= [manifold.MDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
(
    n\_components\=n\_components,
    max\_iter\=50,
    n\_init\=1,
    random\_state\=0,
    init\="classical\_mds",
    normalized\_stress\=False,
)
S\_scaling\_metric \= md\_scaling.fit\_transform(S\_points)

md\_scaling\_nonmetric \= [manifold.MDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
(
    n\_components\=n\_components,
    max\_iter\=50,
    n\_init\=1,
    random\_state\=0,
    normalized\_stress\=False,
    metric\_mds\=False,
    init\="classical\_mds",
)
S\_scaling\_nonmetric \= md\_scaling\_nonmetric.fit\_transform(S\_points)

md\_scaling\_classical \= [manifold.ClassicalMDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#sklearn.manifold.ClassicalMDS "sklearn.manifold.ClassicalMDS")
(n\_components\=n\_components)
S\_scaling\_classical \= md\_scaling\_classical.fit\_transform(S\_points)

Copy to clipboard

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
    nrows\=1, ncols\=3, figsize\=(7, 3.5), facecolor\="white", constrained\_layout\=True
)
fig.suptitle("Multidimensional scaling", size\=16)

mds\_methods \= \[\
    ("Metric MDS", S\_scaling\_metric),\
    ("Non-metric MDS", S\_scaling\_nonmetric),\
    ("Classical MDS", S\_scaling\_classical),\
\]
for ax, method in zip(axs.flat, mds\_methods):
    name, points \= method
    add\_2d\_scatter(ax, points, S\_color, name)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Multidimensional scaling, Metric MDS, Non-metric MDS, Classical MDS](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_004.png)

### Spectral embedding for non-linear dimensionality reduction[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html#spectral-embedding-for-non-linear-dimensionality-reduction "Link to this heading")

This implementation uses Laplacian Eigenmaps, which finds a low dimensional representation of the data using a spectral decomposition of the graph Laplacian. Read more in the [User Guide](https://scikit-learn.org/stable/modules/manifold.html#spectral-embedding)
.

spectral \= [manifold.SpectralEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
(
    n\_components\=n\_components, n\_neighbors\=n\_neighbors, random\_state\=42
)
S\_spectral \= spectral.fit\_transform(S\_points)

plot\_2d(S\_spectral, S\_color, "Spectral Embedding")

Copy to clipboard

![Spectral Embedding](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_005.png)

### T-distributed Stochastic Neighbor Embedding[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html#t-distributed-stochastic-neighbor-embedding "Link to this heading")

It converts similarities between data points to joint probabilities and tries to minimize the Kullback-Leibler divergence between the joint probabilities of the low-dimensional embedding and the high-dimensional data. t-SNE has a cost function that is not convex, i.e. with different initializations we can get different results. Read more in the [User Guide](https://scikit-learn.org/stable/modules/manifold.html#t-sne)
.

t\_sne \= [manifold.TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
(
    n\_components\=n\_components,
    perplexity\=30,
    init\="random",
    max\_iter\=250,
    random\_state\=0,
)
S\_t\_sne \= t\_sne.fit\_transform(S\_points)

plot\_2d(S\_t\_sne, S\_color, "T-distributed Stochastic  \\n Neighbor Embedding")

Copy to clipboard

![T-distributed Stochastic    Neighbor Embedding](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_006.png)

**Total running time of the script:** (0 minutes 17.401 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo20.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/manifold/plot_compare_methods.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo20.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/manifold/plot_compare_methods.ipynb)

[`Download Jupyter notebook: plot_compare_methods.ipynb`](https://scikit-learn.org/stable/_downloads/c8db473878b6afea8e75e36dc828f109/plot_compare_methods.ipynb)

[`Download Python source code: plot_compare_methods.py`](https://scikit-learn.org/stable/_downloads/cda53b33015268619bc212d32b7000b9/plot_compare_methods.py)

[`Download zipped: plot_compare_methods.zip`](https://scikit-learn.org/stable/_downloads/9e97ddcf188484151f4cb4c62e3be741/plot_compare_methods.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_manifold_sphere_thumb.png)

[Manifold Learning methods on a severed sphere](https://scikit-learn.org/stable/auto_examples/manifold/plot_manifold_sphere.html)

Manifold Learning methods on a severed sphere

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stock_market_thumb.png)

[Visualizing the stock market structure](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html)

Visualizing the stock market structure

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_swissroll_thumb.png)

[Swiss Roll And Swiss-Hole Reduction](https://scikit-learn.org/stable/auto_examples/manifold/plot_swissroll.html)

Swiss Roll And Swiss-Hole Reduction

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/cda53b33015268619bc212d32b7000b9/plot_compare_methods.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c8db473878b6afea8e75e36dc828f109/plot_compare_methods.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/9e97ddcf188484151f4cb4c62e3be741/plot_compare_methods.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo20.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/manifold/plot_compare_methods.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo20.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/manifold/plot_compare_methods.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)