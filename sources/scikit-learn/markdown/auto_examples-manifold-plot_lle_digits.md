[Skip to main content](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/manifold/plot_lle_digits.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/manifold/plot_lle_digits.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/manifold/plot_lle_digits.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/manifold/plot_lle_digits.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/manifold/plot_lle_digits.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/manifold/plot_lle_digits.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html#sphx-glr-download-auto-examples-manifold-plot-lle-digits-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html#manifold-learning-on-handwritten-digits-locally-linear-embedding-isomap "Link to this heading")

==========================================================================================================================================================================================================================================================

We illustrate various embedding techniques on the digits dataset.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Load digits dataset[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html#load-digits-dataset "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

We will load the digits dataset and only use six first of the ten available classes.

from sklearn.datasets import [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")

digits \= [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
(n\_class\=6)
X, y \= digits.data, digits.target
n\_samples, n\_features \= X.shape
n\_neighbors \= 30

Copy to clipboard

We can plot the first hundred digits from this data set.

import matplotlib.pyplot as plt

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=10, ncols\=10, figsize\=(6, 6))
for idx, ax in enumerate(axs.ravel()):
    ax.imshow(X\[idx\].reshape((8, 8)), cmap\=plt.cm.binary)
    ax.axis("off")
\_ \= fig.suptitle("A selection from the 64-dimensional digits dataset", fontsize\=16)

Copy to clipboard

![A selection from the 64-dimensional digits dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_001.png)

Helper function to plot embedding[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html#helper-function-to-plot-embedding "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Below, we will use different techniques to embed the digits dataset. We will plot the projection of the original data onto each embedding. It will allow us to check whether or digits are grouped together in the embedding space, or scattered across it.

import numpy as np
from matplotlib import offsetbox

from sklearn.preprocessing import [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")

def plot\_embedding(X, title):
    \_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
    X \= [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
().fit\_transform(X)

    for digit in digits.target\_names:
        ax.scatter(
            \*X\[y \== digit\].T,
            marker\=f"${digit}$",
            s\=60,
            color\=plt.cm.Dark2(digit),
            alpha\=0.425,
            zorder\=2,
        )
    shown\_images \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[1.0, 1.0\]\])  \# just something big
    for i in range(X.shape\[0\]):
        \# plot every digit on the embedding
        \# show an annotation box for a group of digits
        dist \= [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
((X\[i\] \- shown\_images) \*\* 2, 1)
        if [np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
(dist) < 4e-3:
            \# don't show points that are too close
            continue
        shown\_images \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[shown\_images, \[X\[i\]\]\], axis\=0)
        imagebox \= [offsetbox.AnnotationBbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")
(
            [offsetbox.OffsetImage](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "matplotlib.offsetbox.OffsetImage")
(digits.images\[i\], cmap\=plt.cm.gray\_r), X\[i\]
        )
        imagebox.set(zorder\=1)
        ax.add\_artist(imagebox)

    ax.set\_title(title)
    ax.axis("off")

Copy to clipboard

Embedding techniques comparison[#](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html#embedding-techniques-comparison "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Below, we compare different techniques. However, there are a couple of things to note:

*   the [`RandomTreesEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")
     is not technically a manifold embedding method, as it learn a high-dimensional representation on which we apply a dimensionality reduction method. However, it is often useful to cast a dataset into a representation in which the classes are linearly-separable.
    
*   the [`LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     and the [`NeighborhoodComponentsAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis")
    , are supervised dimensionality reduction method, i.e. they make use of the provided labels, contrary to other methods.
    
*   the [`TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
     is initialized with the embedding that is generated by PCA in this example. It ensures global stability of the embedding, i.e., the embedding does not depend on random initialization.
    

from sklearn.decomposition import [TruncatedSVD](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
from sklearn.discriminant\_analysis import [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
from sklearn.ensemble import [RandomTreesEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")
from sklearn.manifold import (
    [MDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
,
    [TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
,
    [ClassicalMDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#sklearn.manifold.ClassicalMDS "sklearn.manifold.ClassicalMDS")
,
    [Isomap](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
,
    [LocallyLinearEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
,
    [SpectralEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
,
)
from sklearn.neighbors import [NeighborhoodComponentsAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.random\_projection import [SparseRandomProjection](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection")

embeddings \= {
    "Random projection embedding": [SparseRandomProjection](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection")
(
        n\_components\=2, random\_state\=42
    ),
    "Truncated SVD embedding": [TruncatedSVD](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
(n\_components\=2),
    "Linear Discriminant Analysis embedding": [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
(
        n\_components\=2
    ),
    "Isomap embedding": [Isomap](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")
(n\_neighbors\=n\_neighbors, n\_components\=2),
    "Standard LLE embedding": [LocallyLinearEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
(
        n\_neighbors\=n\_neighbors, n\_components\=2, method\="standard"
    ),
    "Modified LLE embedding": [LocallyLinearEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
(
        n\_neighbors\=n\_neighbors, n\_components\=2, method\="modified"
    ),
    "Hessian LLE embedding": [LocallyLinearEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
(
        n\_neighbors\=n\_neighbors, n\_components\=2, method\="hessian"
    ),
    "LTSA LLE embedding": [LocallyLinearEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")
(
        n\_neighbors\=n\_neighbors, n\_components\=2, method\="ltsa"
    ),
    "Metric MDS embedding": [MDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
(n\_components\=2, n\_init\=1, init\="classical\_mds"),
    "Non-metric MDS embedding": [MDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")
(
        n\_components\=2, n\_init\=1, init\="classical\_mds", metric\_mds\=False
    ),
    "Classical MDS embedding": [ClassicalMDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#sklearn.manifold.ClassicalMDS "sklearn.manifold.ClassicalMDS")
(n\_components\=2),
    "Random Trees embedding": [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
        [RandomTreesEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")
(n\_estimators\=200, max\_depth\=5, random\_state\=0),
        [TruncatedSVD](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
(n\_components\=2),
    ),
    "Spectral embedding": [SpectralEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
(
        n\_components\=2, random\_state\=0, eigen\_solver\="arpack"
    ),
    "t-SNE embedding": [TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
(
        n\_components\=2,
        max\_iter\=500,
        n\_iter\_without\_progress\=150,
        n\_jobs\=2,
        random\_state\=0,
    ),
    "NCA embedding": [NeighborhoodComponentsAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis")
(
        n\_components\=2, init\="pca", random\_state\=0
    ),
}

Copy to clipboard

Once we declared all the methods of interest, we can run and perform the projection of the original data. We will store the projected data as well as the computational time needed to perform each projection.

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

projections, timing \= {}, {}
for name, transformer in embeddings.items():
    if name.startswith("Linear Discriminant Analysis"):
        data \= X.copy()
        data.flat\[:: X.shape\[1\] + 1\] += 0.01  \# Make X invertible
    else:
        data \= X

    print(f"Computing {name}...")
    start\_time \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    projections\[name\] \= transformer.fit\_transform(data, y)
    timing\[name\] \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start\_time

Copy to clipboard

Computing Random projection embedding...
Computing Truncated SVD embedding...
Computing Linear Discriminant Analysis embedding...
Computing Isomap embedding...
Computing Standard LLE embedding...
Computing Modified LLE embedding...
Computing Hessian LLE embedding...
Computing LTSA LLE embedding...
Computing Metric MDS embedding...
Computing Non-metric MDS embedding...
Computing Classical MDS embedding...
Computing Random Trees embedding...
Computing Spectral embedding...
Computing t-SNE embedding...
Computing NCA embedding...

Copy to clipboard

Finally, we can plot the resulting projection given by each method.

for name in timing:
    title \= f"{name} (time {timing\[name\]:.3f}s)"
    plot\_embedding(projections\[name\], title)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

*   ![Random projection embedding (time 0.001s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_002.png)
*   ![Truncated SVD embedding (time 0.003s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_003.png)
*   ![Linear Discriminant Analysis embedding (time 0.006s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_004.png)
*   ![Isomap embedding (time 0.346s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_005.png)
*   ![Standard LLE embedding (time 0.187s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_006.png)
*   ![Modified LLE embedding (time 2.434s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_007.png)
*   ![Hessian LLE embedding (time 1.811s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_008.png)
*   ![LTSA LLE embedding (time 2.090s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_009.png)
*   ![Metric MDS embedding (time 2.393s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_010.png)
*   ![Non-metric MDS embedding (time 16.625s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_011.png)
*   ![Classical MDS embedding (time 0.105s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_012.png)
*   ![Random Trees embedding (time 0.252s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_013.png)
*   ![Spectral embedding (time 0.145s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_014.png)
*   ![t-SNE embedding (time 2.413s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_015.png)
*   ![NCA embedding (time 2.716s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_016.png)

**Total running time of the script:** (0 minutes 35.116 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo20.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/manifold/plot_lle_digits.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo20.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/manifold/plot_lle_digits.ipynb)

[`Download Jupyter notebook: plot_lle_digits.ipynb`](https://scikit-learn.org/stable/_downloads/1e0968da80ca868bbdf21c1d0547f68c/plot_lle_digits.ipynb)

[`Download Python source code: plot_lle_digits.py`](https://scikit-learn.org/stable/_downloads/9d97cc4ed755b7f2c7f9311bccc89a00/plot_lle_digits.py)

[`Download zipped: plot_lle_digits.zip`](https://scikit-learn.org/stable/_downloads/31e6facb4e4fb576c8a7d28e24eaba3b/plot_lle_digits.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stock_market_thumb.png)

[Visualizing the stock market structure](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html)

Visualizing the stock market structure

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_methods_thumb.png)

[Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html)

Comparison of Manifold Learning methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_linkage_thumb.png)

[Various Agglomerative Clustering on a 2D embedding of digits](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_linkage.html)

Various Agglomerative Clustering on a 2D embedding of digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_thumb.png)

[Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)

Feature transformations with ensembles of trees

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/9d97cc4ed755b7f2c7f9311bccc89a00/plot_lle_digits.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/1e0968da80ca868bbdf21c1d0547f68c/plot_lle_digits.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/31e6facb4e4fb576c8a7d28e24eaba3b/plot_lle_digits.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo20.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/manifold/plot_lle_digits.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo20.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/manifold/plot_lle_digits.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)