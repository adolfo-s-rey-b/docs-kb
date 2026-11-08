[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_cluster_comparison.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_cluster_comparison.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_cluster_comparison.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_cluster_comparison.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_cluster_comparison.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_cluster_comparison.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-download-auto-examples-cluster-plot-cluster-comparison-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparing different clustering algorithms on toy datasets[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#comparing-different-clustering-algorithms-on-toy-datasets "Link to this heading")

==================================================================================================================================================================================================================================

This example shows characteristics of different clustering algorithms on datasets that are “interesting” but still in 2D. With the exception of the last dataset, the parameters of each of these dataset-algorithm pairs has been tuned to produce good clustering results. Some algorithms are more sensitive to parameter values than others.

The last dataset is an example of a ‘null’ situation for clustering: the data is homogeneous, and there is no good clustering. For this example, the null dataset uses the same parameters as the dataset in the row above it, which represents a mismatch in the parameter values and the data structure.

While these examples give some intuition about the algorithms, this intuition might not apply to very high dimensional data.

![MiniBatch KMeans, Affinity Propagation, MeanShift, Spectral Clustering, Ward, Agglomerative Clustering, DBSCAN, HDBSCAN, OPTICS, BIRCH, Gaussian Mixture](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import time
import warnings
from itertools import [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle")
, [islice](https://docs.python.org/3/library/itertools.html#itertools.islice "itertools.islice")

import matplotlib.pyplot as plt
import numpy as np

from sklearn import cluster, [datasets](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
, mixture
from sklearn.neighbors import [kneighbors\_graph](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html#sklearn.neighbors.kneighbors_graph "sklearn.neighbors.kneighbors_graph")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

\# ============
\# Generate datasets. We choose the size big enough to see the scalability
\# of the algorithms, but not too big to avoid too long running times
\# ============
n\_samples \= 500
seed \= 30
noisy\_circles \= [datasets.make\_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
(
    n\_samples\=n\_samples, factor\=0.5, noise\=0.05, random\_state\=seed
)
noisy\_moons \= [datasets.make\_moons](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")
(n\_samples\=n\_samples, noise\=0.05, random\_state\=seed)
blobs \= [datasets.make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=n\_samples, random\_state\=seed)
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(seed)
no\_structure \= rng.rand(n\_samples, 2), None

\# Anisotropicly distributed data
random\_state \= 170
X, y \= [datasets.make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=n\_samples, random\_state\=random\_state)
transformation \= \[\[0.6, \-0.6\], \[\-0.4, 0.8\]\]
X\_aniso \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(X, transformation)
aniso \= (X\_aniso, y)

\# blobs with varied variances
varied \= [datasets.make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(
    n\_samples\=n\_samples, cluster\_std\=\[1.0, 2.5, 0.5\], random\_state\=random\_state
)

\# ============
\# Set up cluster parameters
\# ============
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(9 \* 2 + 3, 13))
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(
    left\=0.02, right\=0.98, bottom\=0.001, top\=0.95, wspace\=0.05, hspace\=0.01
)

plot\_num \= 1

default\_base \= {
    "quantile": 0.3,
    "eps": 0.3,
    "damping": 0.9,
    "preference": \-200,
    "n\_neighbors": 3,
    "n\_clusters": 3,
    "min\_samples": 7,
    "xi": 0.05,
    "min\_cluster\_size": 0.1,
    "allow\_single\_cluster": True,
    "hdbscan\_min\_cluster\_size": 15,
    "hdbscan\_min\_samples": 3,
    "random\_state": 42,
}

[datasets](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
 \= \[\
    (\
        noisy\_circles,\
        {\
            "damping": 0.77,\
            "preference": \-240,\
            "quantile": 0.2,\
            "n\_clusters": 2,\
            "min\_samples": 7,\
            "xi": 0.08,\
        },\
    ),\
    (\
        noisy\_moons,\
        {\
            "damping": 0.75,\
            "preference": \-220,\
            "n\_clusters": 2,\
            "min\_samples": 7,\
            "xi": 0.1,\
        },\
    ),\
    (\
        varied,\
        {\
            "eps": 0.18,\
            "n\_neighbors": 2,\
            "min\_samples": 7,\
            "xi": 0.01,\
            "min\_cluster\_size": 0.2,\
        },\
    ),\
    (\
        aniso,\
        {\
            "eps": 0.15,\
            "n\_neighbors": 2,\
            "min\_samples": 7,\
            "xi": 0.1,\
            "min\_cluster\_size": 0.2,\
        },\
    ),\
    (blobs, {"min\_samples": 7, "xi": 0.1, "min\_cluster\_size": 0.2}),\
    (no\_structure, {}),\
\]

for i\_dataset, (dataset, algo\_params) in enumerate([datasets](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
):
    \# update parameters with dataset-specific values
    params \= default\_base.copy()
    params.update(algo\_params)

    X, y \= dataset

    \# normalize dataset for easier parameter selection
    X \= [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
().fit\_transform(X)

    \# estimate bandwidth for mean shift
    bandwidth \= [cluster.estimate\_bandwidth](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.estimate_bandwidth.html#sklearn.cluster.estimate_bandwidth "sklearn.cluster.estimate_bandwidth")
(X, quantile\=params\["quantile"\])

    \# connectivity matrix for structured Ward
    connectivity \= [kneighbors\_graph](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html#sklearn.neighbors.kneighbors_graph "sklearn.neighbors.kneighbors_graph")
(
        X, n\_neighbors\=params\["n\_neighbors"\], include\_self\=False
    )
    \# make connectivity symmetric
    connectivity \= 0.5 \* (connectivity + connectivity.T)

    \# ============
    \# Create cluster objects
    \# ============
    ms \= [cluster.MeanShift](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")
(bandwidth\=bandwidth, bin\_seeding\=True)
    two\_means \= [cluster.MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
(
        n\_clusters\=params\["n\_clusters"\],
        random\_state\=params\["random\_state"\],
    )
    ward \= [cluster.AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
(
        n\_clusters\=params\["n\_clusters"\], linkage\="ward", connectivity\=connectivity
    )
    spectral \= [cluster.SpectralClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")
(
        n\_clusters\=params\["n\_clusters"\],
        eigen\_solver\="arpack",
        affinity\="nearest\_neighbors",
        random\_state\=params\["random\_state"\],
    )
    dbscan \= [cluster.DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
(eps\=params\["eps"\])
    hdbscan \= [cluster.HDBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
(
        min\_samples\=params\["hdbscan\_min\_samples"\],
        min\_cluster\_size\=params\["hdbscan\_min\_cluster\_size"\],
        allow\_single\_cluster\=params\["allow\_single\_cluster"\],
        copy\=True,
    )
    optics \= [cluster.OPTICS](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
(
        min\_samples\=params\["min\_samples"\],
        xi\=params\["xi"\],
        min\_cluster\_size\=params\["min\_cluster\_size"\],
    )
    affinity\_propagation \= [cluster.AffinityPropagation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
(
        damping\=params\["damping"\],
        preference\=params\["preference"\],
        random\_state\=params\["random\_state"\],
    )
    average\_linkage \= [cluster.AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
(
        linkage\="average",
        metric\="cityblock",
        n\_clusters\=params\["n\_clusters"\],
        connectivity\=connectivity,
    )
    birch \= [cluster.Birch](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
(n\_clusters\=params\["n\_clusters"\])
    gmm \= [mixture.GaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
(
        n\_components\=params\["n\_clusters"\],
        covariance\_type\="full",
        random\_state\=params\["random\_state"\],
    )

    clustering\_algorithms \= (
        ("MiniBatch\\nKMeans", two\_means),
        ("Affinity\\nPropagation", affinity\_propagation),
        ("MeanShift", ms),
        ("Spectral\\nClustering", spectral),
        ("Ward", ward),
        ("Agglomerative\\nClustering", average\_linkage),
        ("DBSCAN", dbscan),
        ("HDBSCAN", hdbscan),
        ("OPTICS", optics),
        ("BIRCH", birch),
        ("Gaussian\\nMixture", gmm),
    )

    for name, algorithm in clustering\_algorithms:
        t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()

        \# catch warnings related to kneighbors\_graph
        with [warnings.catch\_warnings](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings")
():
            [warnings.filterwarnings](https://docs.python.org/3/library/warnings.html#warnings.filterwarnings "warnings.filterwarnings")
(
                "ignore",
                message\="the number of connected components of the "
                "connectivity matrix is \[0-9\]{1,2}"
                " > 1. Completing it to avoid stopping the tree early.",
                category\=UserWarning,
            )
            [warnings.filterwarnings](https://docs.python.org/3/library/warnings.html#warnings.filterwarnings "warnings.filterwarnings")
(
                "ignore",
                message\="Graph is not fully connected, spectral embedding"
                " may not work as expected.",
                category\=UserWarning,
            )
            algorithm.fit(X)

        t1 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        if hasattr(algorithm, "labels\_"):
            y\_pred \= algorithm.labels\_.astype(int)
        else:
            y\_pred \= algorithm.predict(X)

        [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(len([datasets](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
), len(clustering\_algorithms), plot\_num)
        if i\_dataset \== 0:
            [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(name, size\=18)

        colors \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(
            list(
                [islice](https://docs.python.org/3/library/itertools.html#itertools.islice "itertools.islice")
(
                    [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle")
(
                        \[\
                            "#377eb8",\
                            "#ff7f00",\
                            "#4daf4a",\
                            "#f781bf",\
                            "#a65628",\
                            "#984ea3",\
                            "#999999",\
                            "#e41a1c",\
                            "#dede00",\
                        \]
                    ),
                    int(max(y\_pred) + 1),
                )
            )
        )
        \# add black color for outliers (if any)
        colors \= [np.append](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")
(colors, \["#000000"\])
        [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], s\=10, color\=colors\[y\_pred\])

        [plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(\-2.5, 2.5)
        [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(\-2.5, 2.5)
        [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
        [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
        [plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(
            0.99,
            0.01,
            ("%.2fs" % (t1 \- t0)).lstrip("0"),
            transform\=[plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
().transAxes,
            size\=15,
            horizontalalignment\="right",
        )
        plot\_num += 1

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 6.118 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_cluster_comparison.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_cluster_comparison.ipynb)

[`Download Jupyter notebook: plot_cluster_comparison.ipynb`](https://scikit-learn.org/stable/_downloads/803ca1bcd8dd2c364836a6784144355b/plot_cluster_comparison.ipynb)

[`Download Python source code: plot_cluster_comparison.py`](https://scikit-learn.org/stable/_downloads/d5b3a28a1dd21d46ab866e29825586b7/plot_cluster_comparison.py)

[`Download zipped: plot_cluster_comparison.zip`](https://scikit-learn.org/stable/_downloads/899c34960ade693d4b26e3b301f99416/plot_cluster_comparison.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linkage_comparison_thumb.png)

[Comparing different hierarchical linkage methods on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html)

Comparing different hierarchical linkage methods on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ward_structured_vs_unstructured_thumb.png)

[Hierarchical clustering with and without structure](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)

Hierarchical clustering with and without structure

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_thumb.png)

[Demo of HDBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html)

Demo of HDBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_ward_segmentation_thumb.png)

[A demo of structured Ward hierarchical clustering on an image of coins](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html)

A demo of structured Ward hierarchical clustering on an image of coins

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/d5b3a28a1dd21d46ab866e29825586b7/plot_cluster_comparison.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/803ca1bcd8dd2c364836a6784144355b/plot_cluster_comparison.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/899c34960ade693d4b26e3b301f99416/plot_cluster_comparison.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_cluster_comparison.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_cluster_comparison.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)