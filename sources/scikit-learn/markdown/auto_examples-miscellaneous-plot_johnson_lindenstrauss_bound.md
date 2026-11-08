[Skip to main content](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html#sphx-glr-download-auto-examples-miscellaneous-plot-johnson-lindenstrauss-bound-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

The Johnson-Lindenstrauss bound for embedding with random projections[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html#the-johnson-lindenstrauss-bound-for-embedding-with-random-projections "Link to this heading")

=========================================================================================================================================================================================================================================================================

The [Johnson-Lindenstrauss lemma](https://en.wikipedia.org/wiki/%20Johnson%E2%80%93Lindenstrauss_lemma)
 states that any high dimensional dataset can be randomly projected into a lower dimensional Euclidean space while controlling the distortion in the pairwise distances.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import sys
from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [fetch\_20newsgroups\_vectorized](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized")
, [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
from sklearn.metrics.pairwise import euclidean\_distances
from sklearn.random\_projection import (
    [SparseRandomProjection](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection")
,
    [johnson\_lindenstrauss\_min\_dim](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html#sklearn.random_projection.johnson_lindenstrauss_min_dim "sklearn.random_projection.johnson_lindenstrauss_min_dim")
,
)

Copy to clipboard

Theoretical bounds[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html#theoretical-bounds "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

The distortion introduced by a random projection `p` is asserted by the fact that `p` is defining an eps-embedding with good probability as defined by:

(1−eps)‖u−v‖2<‖p(u)−p(v)‖2<(1+eps)‖u−v‖2

Where `u` and `v` are any rows taken from a dataset of shape `(n_samples, n_features)` and `p` is a projection by a random Gaussian `N(0, 1)` matrix of shape `(n_components, n_features)` (or a sparse Achlioptas matrix).

The minimum number of components to guarantees the eps-embedding is given by:

n\_components≥4log(n\_samples)/(eps2/2−eps3/3)

The first plot shows that with an increasing number of samples `n_samples`, the minimal number of dimensions `n_components` increased logarithmically in order to guarantee an `eps`\-embedding.

\# range of admissible distortions
eps\_range \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.1, 0.99, 5)
colors \= plt.cm.Blues([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.3, 1.0, len(eps\_range)))

\# range of number of samples (observation) to embed
n\_samples\_range \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(1, 9, 9)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
for eps, color in zip(eps\_range, colors):
    min\_n\_components \= [johnson\_lindenstrauss\_min\_dim](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html#sklearn.random_projection.johnson_lindenstrauss_min_dim "sklearn.random_projection.johnson_lindenstrauss_min_dim")
(n\_samples\_range, eps\=eps)
    [plt.loglog](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.loglog.html#matplotlib.pyplot.loglog "matplotlib.pyplot.loglog")
(n\_samples\_range, min\_n\_components, color\=color)

[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(\[f"eps = {eps:0.1f}" for eps in eps\_range\], loc\="lower right")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Number of observations to eps-embed")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Minimum number of dimensions")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Johnson-Lindenstrauss bounds:\\nn\_samples vs n\_components")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Johnson-Lindenstrauss bounds: n_samples vs n_components](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_001.png)

The second plot shows that an increase of the admissible distortion `eps` allows to reduce drastically the minimal number of dimensions `n_components` for a given number of samples `n_samples`

\# range of admissible distortions
eps\_range \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.01, 0.99, 100)

\# range of number of samples (observation) to embed
n\_samples\_range \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(2, 6, 5)
colors \= plt.cm.Blues([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.3, 1.0, len(n\_samples\_range)))

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
for n\_samples, color in zip(n\_samples\_range, colors):
    min\_n\_components \= [johnson\_lindenstrauss\_min\_dim](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html#sklearn.random_projection.johnson_lindenstrauss_min_dim "sklearn.random_projection.johnson_lindenstrauss_min_dim")
(n\_samples, eps\=eps\_range)
    [plt.semilogy](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogy.html#matplotlib.pyplot.semilogy "matplotlib.pyplot.semilogy")
(eps\_range, min\_n\_components, color\=color)

[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(\[f"n\_samples = {n}" for n in n\_samples\_range\], loc\="upper right")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Distortion eps")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Minimum number of dimensions")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Johnson-Lindenstrauss bounds:\\nn\_components vs eps")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Johnson-Lindenstrauss bounds: n_components vs eps](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_002.png)

Empirical validation[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html#empirical-validation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

We validate the above bounds on the 20 newsgroups text document (TF-IDF word frequencies) dataset or on the digits dataset:

*   for the 20 newsgroups dataset some 300 documents with 100k features in total are projected using a sparse random matrix to smaller euclidean spaces with various values for the target number of dimensions `n_components`.
    
*   for the digits dataset, some 8x8 gray level pixels data for 300 handwritten digits pictures are randomly projected to spaces for various larger number of dimensions `n_components`.
    

The default dataset is the 20 newsgroups dataset. To run the example on the digits dataset, pass the `--use-digits-dataset` command line argument to this script.

if "--use-digits-dataset" in [sys.argv](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
:
    data \= [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
().data\[:300\]
else:
    data \= [fetch\_20newsgroups\_vectorized](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized")
().data\[:300\]

Copy to clipboard

For each value of `n_components`, we plot:

*   2D distribution of sample pairs with pairwise distances in original and projected spaces as x- and y-axis respectively.
    
*   1D histogram of the ratio of those distances (projected / original).
    

n\_samples, n\_features \= data.shape
print(
    f"Embedding {n\_samples} samples with dim {n\_features} using various "
    "random projections"
)

n\_components\_range \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[300, 1\_000, 10\_000\])
dists \= euclidean\_distances(data, squared\=True).ravel()

\# select only non-identical samples pairs
nonzero \= dists != 0
dists \= dists\[nonzero\]

for n\_components in n\_components\_range:
    t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    rp \= [SparseRandomProjection](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection")
(n\_components\=n\_components)
    projected\_data \= rp.fit\_transform(data)
    print(
        f"Projected {n\_samples} samples from {n\_features} to {n\_components} in "
        f"{[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0:0.3f}s"
    )
    if hasattr(rp, "components\_"):
        n\_bytes \= rp.components\_.data.nbytes
        n\_bytes += rp.components\_.indices.nbytes
        print(f"Random matrix with size: {n\_bytes / 1e6:0.3f} MB")

    projected\_dists \= euclidean\_distances(projected\_data, squared\=True).ravel()\[nonzero\]

    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
    min\_dist \= min(projected\_dists.min(), dists.min())
    max\_dist \= max(projected\_dists.max(), dists.max())
    [plt.hexbin](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hexbin.html#matplotlib.pyplot.hexbin "matplotlib.pyplot.hexbin")
(
        dists,
        projected\_dists,
        gridsize\=100,
        cmap\=plt.cm.PuBu,
        extent\=\[min\_dist, max\_dist, min\_dist, max\_dist\],
    )
    [plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Pairwise squared distances in original space")
    [plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Pairwise squared distances in projected space")
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Pairwise distances distribution for n\_components=%d" % n\_components)
    cb \= [plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
()
    cb.set\_label("Sample pairs counts")

    rates \= projected\_dists / dists
    print(f"Mean distances rate: {[np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(rates):.2f} ({[np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")
(rates):.2f})")

    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
    [plt.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist")
(rates, bins\=50, range\=(0.0, 2.0), edgecolor\="k", density\=True)
    [plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Squared distances rate: projected / original")
    [plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Distribution of samples pairs")
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Histogram of pairwise distance rates for n\_components=%d" % n\_components)

    \# TODO: compute the expected value of eps and add them to the previous plot
    \# as vertical lines / region

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

*   ![Pairwise distances distribution for n_components=300](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_003.png)
*   ![Histogram of pairwise distance rates for n_components=300](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_004.png)
*   ![Pairwise distances distribution for n_components=1000](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_005.png)
*   ![Histogram of pairwise distance rates for n_components=1000](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_006.png)
*   ![Pairwise distances distribution for n_components=10000](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_007.png)
*   ![Histogram of pairwise distance rates for n_components=10000](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_008.png)

Embedding 300 samples with dim 130107 using various random projections
Projected 300 samples from 130107 to 300 in 0.229s
Random matrix with size: 1.293 MB
Mean distances rate: 1.01 (0.16)
Projected 300 samples from 130107 to 1000 in 0.764s
Random matrix with size: 4.333 MB
Mean distances rate: 1.00 (0.09)
Projected 300 samples from 130107 to 10000 in 7.545s
Random matrix with size: 43.239 MB
Mean distances rate: 1.01 (0.03)

Copy to clipboard

We can see that for low values of `n_components` the distribution is wide with many distorted pairs and a skewed distribution (due to the hard limit of zero ratio on the left as distances are always positives) while for larger values of `n_components` the distortion is controlled and the distances are well preserved by the random projection.

Remarks[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html#remarks "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

According to the JL lemma, projecting 300 samples without too much distortion will require at least several thousands dimensions, irrespective of the number of features of the original dataset.

Hence using random projections on the digits dataset which only has 64 features in the input space does not make sense: it does not allow for dimensionality reduction in this case.

On the twenty newsgroups on the other hand the dimensionality can be decreased from 56,436 down to 10,000 while reasonably preserving pairwise distances.

**Total running time of the script:** (0 minutes 10.815 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.ipynb)

[`Download Jupyter notebook: plot_johnson_lindenstrauss_bound.ipynb`](https://scikit-learn.org/stable/_downloads/285b194a4740110cb23e241031123972/plot_johnson_lindenstrauss_bound.ipynb)

[`Download Python source code: plot_johnson_lindenstrauss_bound.py`](https://scikit-learn.org/stable/_downloads/cba66f803bb263f8032bc4d46368e20b/plot_johnson_lindenstrauss_bound.py)

[`Download zipped: plot_johnson_lindenstrauss_bound.zip`](https://scikit-learn.org/stable/_downloads/477739095a6a24d74492bccf73397462/plot_johnson_lindenstrauss_bound.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_thumb.png)

[Demo of HDBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html)

Demo of HDBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lw_vs_oas_thumb.png)

[Ledoit-Wolf vs OAS estimation](https://scikit-learn.org/stable/auto_examples/covariance/plot_lw_vs_oas.html)

Ledoit-Wolf vs OAS estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mds_thumb.png)

[Multi-dimensional scaling](https://scikit-learn.org/stable/auto_examples/manifold/plot_mds.html)

Multi-dimensional scaling

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/cba66f803bb263f8032bc4d46368e20b/plot_johnson_lindenstrauss_bound.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/285b194a4740110cb23e241031123972/plot_johnson_lindenstrauss_bound.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/477739095a6a24d74492bccf73397462/plot_johnson_lindenstrauss_bound.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)