[Skip to main content](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neighbors/approximate_nearest_neighbors.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neighbors/approximate_nearest_neighbors.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neighbors/approximate_nearest_neighbors.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neighbors/approximate_nearest_neighbors.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neighbors/approximate_nearest_neighbors.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neighbors/approximate_nearest_neighbors.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html#sphx-glr-download-auto-examples-neighbors-approximate-nearest-neighbors-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Approximate nearest neighbors in TSNE[#](https://scikit-learn.org/stable/auto_examples/neighbors/approximate_nearest_neighbors.html#approximate-nearest-neighbors-in-tsne "Link to this heading")

==================================================================================================================================================================================================

This example presents how to chain KNeighborsTransformer and TSNE in a pipeline. It also shows how to wrap the packages `nmslib` and `pynndescent` to replace KNeighborsTransformer and perform approximate nearest neighbors. These packages can be installed with `pip install nmslib pynndescent`.

Note: In KNeighborsTransformer we use the definition which includes each training point as its own neighbor in the count of `n_neighbors`, and for compatibility reasons, one extra neighbor is computed when `mode == 'distance'`. Please note that we do the same in the proposed `nmslib` wrapper.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

First we try to import the packages and warn the user in case they are missing.

import sys

try:
    import nmslib
except ImportError:
    print("The package 'nmslib' is required to run this example.")
    [sys.exit](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit")
()

try:
    from pynndescent import PyNNDescentTransformer
except ImportError:
    print("The package 'pynndescent' is required to run this example.")
    [sys.exit](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit")
()

Copy to clipboard

We define a wrapper class for implementing the scikit-learn API to the `nmslib`, as well as a loading function.

import joblib
import numpy as np
from scipy.sparse import [csr\_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_array.html#scipy.sparse.csr_array "scipy.sparse.csr_array")

from sklearn.base import [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
, [TransformerMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin")
from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
from sklearn.utils import [shuffle](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#sklearn.utils.shuffle "sklearn.utils.shuffle")

class NMSlibTransformer([TransformerMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin")
, [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
):
    """Wrapper for using nmslib as sklearn's KNeighborsTransformer"""

    def \_\_init\_\_(self, n\_neighbors\=5, metric\="euclidean", method\="sw-graph", n\_jobs\=-1):
        self.n\_neighbors \= n\_neighbors
        self.method \= method
        self.metric \= metric
        self.n\_jobs \= n\_jobs

    def fit(self, X):
        self.n\_samples\_fit\_ \= X.shape\[0\]

        \# see more metric in the manual
        \# https://github.com/nmslib/nmslib/tree/master/manual
        space \= {
            "euclidean": "l2",
            "cosine": "cosinesimil",
            "l1": "l1",
            "l2": "l2",
        }\[self.metric\]

        self.nmslib\_ \= nmslib.init(method\=self.method, space\=space)
        self.nmslib\_.addDataPointBatch(X.copy())
        self.nmslib\_.createIndex()
        return self

    def transform(self, X):
        n\_samples\_transform \= X.shape\[0\]

        \# For compatibility reasons, as each sample is considered as its own
        \# neighbor, one extra neighbor will be computed.
        n\_neighbors \= self.n\_neighbors + 1

        if self.n\_jobs < 0:
            \# Same handling as done in joblib for negative values of n\_jobs:
            \# in particular, \`n\_jobs == -1\` means "as many threads as CPUs".
            num\_threads \= [joblib.cpu\_count](https://joblib.readthedocs.io/en/latest/generated/joblib.cpu_count.html#joblib.cpu_count "joblib.cpu_count")
() + self.n\_jobs + 1
        else:
            num\_threads \= self.n\_jobs

        results \= self.nmslib\_.knnQueryBatch(
            X.copy(), k\=n\_neighbors, num\_threads\=num\_threads
        )
        indices, distances \= zip(\*results)
        indices, distances \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(indices), [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(distances)

        indptr \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, n\_samples\_transform \* n\_neighbors + 1, n\_neighbors)
        kneighbors\_graph \= [csr\_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_array.html#scipy.sparse.csr_array "scipy.sparse.csr_array")
(
            (distances.ravel(), indices.ravel(), indptr),
            shape\=(n\_samples\_transform, self.n\_samples\_fit\_),
        )

        return kneighbors\_graph

def load\_mnist(n\_samples):
    """Load MNIST, shuffle the data, and return only n\_samples."""
    mnist \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
("mnist\_784", as\_frame\=False)
    X, y \= [shuffle](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#sklearn.utils.shuffle "sklearn.utils.shuffle")
(mnist.data, mnist.target, random\_state\=2)
    return X\[:n\_samples\] / 255, y\[:n\_samples\]

Copy to clipboard

We benchmark the different exact/approximate nearest neighbors transformers.

import time

from sklearn.manifold import [TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
from sklearn.neighbors import [KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")

datasets \= \[\
    ("MNIST\_10000", load\_mnist(n\_samples\=10\_000)),\
    ("MNIST\_20000", load\_mnist(n\_samples\=20\_000)),\
\]

max\_iter \= 500
perplexity \= 30
metric \= "euclidean"
\# TSNE requires a certain number of neighbors which depends on the
\# perplexity parameter.
\# Add one since we include each sample as its own neighbor.
n\_neighbors \= int(3.0 \* perplexity + 1) + 1

tsne\_params \= dict(
    init\="random",  \# pca cannot be used with precomputed distances
    perplexity\=perplexity,
    method\="barnes\_hut",
    random\_state\=42,
    max\_iter\=max\_iter,
    learning\_rate\="auto",
)

transformers \= \[\
    (\
        "KNeighborsTransformer",\
        [KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")\
(n\_neighbors\=n\_neighbors, mode\="distance", metric\=metric),\
    ),\
    (\
        "NMSlibTransformer",\
        NMSlibTransformer(n\_neighbors\=n\_neighbors, metric\=metric),\
    ),\
    (\
        "PyNNDescentTransformer",\
        PyNNDescentTransformer(\
            n\_neighbors\=n\_neighbors, metric\=metric, parallel\_batch\_queries\=True\
        ),\
    ),\
\]

for dataset\_name, (X, y) in datasets:
    msg \= f"Benchmarking on {dataset\_name}:"
    print(f"\\n{msg}\\n" + str("-" \* len(msg)))

    for transformer\_name, transformer in transformers:
        longest \= [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(\[len(name) for name, model in transformers\])
        start \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        transformer.fit(X)
        fit\_duration \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start
        print(f"{transformer\_name:<{longest}} {fit\_duration:.3f} sec (fit)")
        start \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        Xt \= transformer.transform(X)
        transform\_duration \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start
        print(f"{transformer\_name:<{longest}} {transform\_duration:.3f} sec (transform)")
        if transformer\_name \== "PyNNDescentTransformer":
            start \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
            Xt \= transformer.transform(X)
            transform\_duration \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start
            print(
                f"{transformer\_name:<{longest}} {transform\_duration:.3f} sec"
                " (transform)"
            )

Copy to clipboard

Sample output:

Benchmarking on MNIST\_10000:
\----------------------------
[KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
  0.007 sec (fit)
[KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
  1.139 sec (transform)
NMSlibTransformer      0.208 sec (fit)
NMSlibTransformer      0.315 sec (transform)
PyNNDescentTransformer 4.823 sec (fit)
PyNNDescentTransformer 4.884 sec (transform)
PyNNDescentTransformer 0.744 sec (transform)

Benchmarking on MNIST\_20000:
\----------------------------
[KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
  0.011 sec (fit)
[KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
  5.769 sec (transform)
NMSlibTransformer      0.733 sec (fit)
NMSlibTransformer      1.077 sec (transform)
PyNNDescentTransformer 14.448 sec (fit)
PyNNDescentTransformer 7.103 sec (transform)
PyNNDescentTransformer 1.759 sec (transform)

Copy to clipboard

Notice that the `PyNNDescentTransformer` takes more time during the first `fit` and the first `transform` due to the overhead of the numba just in time compiler. But after the first call, the compiled Python code is kept in a cache by numba and subsequent calls do not suffer from this initial overhead. Both [`KNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
 and `NMSlibTransformer` are only run once here as they would show more stable `fit` and `transform` times (they don’t have the cold start problem of PyNNDescentTransformer).

import matplotlib.pyplot as plt
from matplotlib.ticker import [NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")

transformers \= \[\
    ("TSNE with internal NearestNeighbors", [TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")\
(metric\=metric, \*\*tsne\_params)),\
    (\
        "TSNE with KNeighborsTransformer",\
        [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
            [KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")\
(\
                n\_neighbors\=n\_neighbors, mode\="distance", metric\=metric\
            ),\
            [TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")\
(metric\="precomputed", \*\*tsne\_params),\
        ),\
    ),\
    (\
        "TSNE with NMSlibTransformer",\
        [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
            NMSlibTransformer(n\_neighbors\=n\_neighbors, metric\=metric),\
            [TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")\
(metric\="precomputed", \*\*tsne\_params),\
        ),\
    ),\
\]

\# init the plot
nrows \= len(datasets)
ncols \= [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(\[1 for name, model in transformers if "TSNE" in name\])
fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
    nrows\=nrows, ncols\=ncols, squeeze\=False, figsize\=(5 \* ncols, 4 \* nrows)
)
axes \= axes.ravel()
i\_ax \= 0

for dataset\_name, (X, y) in datasets:
    msg \= f"Benchmarking on {dataset\_name}:"
    print(f"\\n{msg}\\n" + str("-" \* len(msg)))

    for transformer\_name, transformer in transformers:
        longest \= [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(\[len(name) for name, model in transformers\])
        start \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        Xt \= transformer.fit\_transform(X)
        transform\_duration \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start
        print(
            f"{transformer\_name:<{longest}} {transform\_duration:.3f} sec"
            " (fit\_transform)"
        )

        \# plot TSNE embedding which should be very similar across methods
        axes\[i\_ax\].set\_title(transformer\_name + "\\non " + dataset\_name)
        axes\[i\_ax\].scatter(
            Xt\[:, 0\],
            Xt\[:, 1\],
            c\=y.astype([np.int32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int32 "numpy.int32")
),
            alpha\=0.2,
            cmap\=plt.cm.viridis,
        )
        axes\[i\_ax\].xaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
        axes\[i\_ax\].yaxis.set\_major\_formatter([NullFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.NullFormatter "matplotlib.ticker.NullFormatter")
())
        axes\[i\_ax\].axis("tight")
        i\_ax += 1

fig.tight\_layout()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

Sample output:

Benchmarking on MNIST\_10000:
\----------------------------
[TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
 with internal NearestNeighbors 24.828 sec (fit\_transform)
[TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
 with [KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
     20.111 sec (fit\_transform)
[TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
 with NMSlibTransformer         21.757 sec (fit\_transform)

Benchmarking on MNIST\_20000:
\----------------------------
[TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
 with internal NearestNeighbors 51.955 sec (fit\_transform)
[TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
 with [KNeighborsTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
     50.994 sec (fit\_transform)
[TSNE](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
 with NMSlibTransformer         43.536 sec (fit\_transform)

Copy to clipboard

We can observe that the default [`TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
 estimator with its internal [`NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
 implementation is roughly equivalent to the pipeline with [`TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
 and [`KNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")
 in terms of performance. This is expected because both pipelines rely internally on the same [`NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
 implementation that performs exacts neighbors search. The approximate `NMSlibTransformer` is already slightly faster than the exact search on the smallest dataset but this speed difference is expected to become more significant on datasets with a larger number of samples.

Notice however that not all approximate search methods are guaranteed to improve the speed of the default exact search method: indeed the exact search implementation significantly improved since scikit-learn 1.1. Furthermore, the brute-force exact search method does not require building an index at `fit` time. So, to get an overall performance improvement in the context of the [`TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
 pipeline, the gains of the approximate search at `transform` need to be larger than the extra time spent to build the approximate search index at `fit` time.

Finally, the TSNE algorithm itself is also computationally intensive, irrespective of the nearest neighbors search. So speeding-up the nearest neighbors search step by a factor of 5 would not result in a speed up by a factor of 5 for the overall pipeline.

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/approximate_nearest_neighbors.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/approximate_nearest_neighbors.ipynb)

[`Download Jupyter notebook: approximate_nearest_neighbors.ipynb`](https://scikit-learn.org/stable/_downloads/73ec8f08ae3ece02509539ee03cc3cdd/approximate_nearest_neighbors.ipynb)

[`Download Python source code: approximate_nearest_neighbors.py`](https://scikit-learn.org/stable/_downloads/dcd99fee3ee8ac76b69a1d2d6f5c7e78/approximate_nearest_neighbors.py)

[`Download zipped: approximate_nearest_neighbors.zip`](https://scikit-learn.org/stable/_downloads/a12e68b62bdda2af020f3efce6bb3545/approximate_nearest_neighbors.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_caching_nearest_neighbors_thumb.png)

[Caching nearest neighbors](https://scikit-learn.org/stable/auto_examples/neighbors/plot_caching_nearest_neighbors.html)

Caching nearest neighbors

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_t_sne_perplexity_thumb.png)

[t-SNE: The effect of various perplexity values on the shape](https://scikit-learn.org/stable/auto_examples/manifold/plot_t_sne_perplexity.html)

t-SNE: The effect of various perplexity values on the shape

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_manifold_sphere_thumb.png)

[Manifold Learning methods on a severed sphere](https://scikit-learn.org/stable/auto_examples/manifold/plot_manifold_sphere.html)

Manifold Learning methods on a severed sphere

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_classification_thumb.png)

[Comparing Nearest Neighbors with and without Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html)

Comparing Nearest Neighbors with and without Neighborhood Components Analysis

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/dcd99fee3ee8ac76b69a1d2d6f5c7e78/approximate_nearest_neighbors.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/73ec8f08ae3ece02509539ee03cc3cdd/approximate_nearest_neighbors.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/a12e68b62bdda2af020f3efce6bb3545/approximate_nearest_neighbors.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/approximate_nearest_neighbors.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/approximate_nearest_neighbors.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)