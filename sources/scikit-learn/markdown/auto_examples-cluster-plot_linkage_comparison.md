[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_linkage_comparison.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_linkage_comparison.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_linkage_comparison.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_linkage_comparison.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_linkage_comparison.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_linkage_comparison.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html#sphx-glr-download-auto-examples-cluster-plot-linkage-comparison-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparing different hierarchical linkage methods on toy datasets[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html#comparing-different-hierarchical-linkage-methods-on-toy-datasets "Link to this heading")

================================================================================================================================================================================================================================================

This example shows characteristics of different linkage methods for hierarchical clustering on datasets that are “interesting” but still in 2D.

The main observations to make are:

*   single linkage is fast, and can perform well on non-globular data, but it performs poorly in the presence of noise.
    
*   average and complete linkage perform well on cleanly separated globular clusters, but have mixed results otherwise.
    
*   Ward is the most effective method for noisy data.
    

While these examples give some intuition about the algorithms, this intuition might not apply to very high dimensional data.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import time
import warnings
from itertools import [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle")
, [islice](https://docs.python.org/3/library/itertools.html#itertools.islice "itertools.islice")

import matplotlib.pyplot as plt
import numpy as np

from sklearn import cluster, [datasets](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

Copy to clipboard

Generate datasets. We choose the size big enough to see the scalability of the algorithms, but not too big to avoid too long running times

n\_samples \= 1500
noisy\_circles \= [datasets.make\_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
(
    n\_samples\=n\_samples, factor\=0.5, noise\=0.05, random\_state\=170
)
noisy\_moons \= [datasets.make\_moons](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")
(n\_samples\=n\_samples, noise\=0.05, random\_state\=170)
blobs \= [datasets.make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=n\_samples, random\_state\=170)
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(170)
no\_structure \= rng.rand(n\_samples, 2), None

\# Anisotropicly distributed data
X, y \= [datasets.make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=n\_samples, random\_state\=170)
transformation \= \[\[0.6, \-0.6\], \[\-0.4, 0.8\]\]
X\_aniso \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(X, transformation)
aniso \= (X\_aniso, y)

\# blobs with varied variances
varied \= [datasets.make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(
    n\_samples\=n\_samples, cluster\_std\=\[1.0, 2.5, 0.5\], random\_state\=170
)

Copy to clipboard

Run the clustering and plot

\# Set up cluster parameters
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(9 \* 1.3 + 2, 14.5))
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(
    left\=0.02, right\=0.98, bottom\=0.001, top\=0.96, wspace\=0.05, hspace\=0.01
)

plot\_num \= 1

default\_base \= {"n\_neighbors": 10, "n\_clusters": 3}

[datasets](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
 \= \[\
    (noisy\_circles, {"n\_clusters": 2}),\
    (noisy\_moons, {"n\_clusters": 2}),\
    (varied, {"n\_neighbors": 2}),\
    (aniso, {"n\_neighbors": 2}),\
    (blobs, {}),\
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

    \# ============
    \# Create cluster objects
    \# ============
    ward \= [cluster.AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
(
        n\_clusters\=params\["n\_clusters"\], linkage\="ward"
    )
    complete \= [cluster.AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
(
        n\_clusters\=params\["n\_clusters"\], linkage\="complete"
    )
    average \= [cluster.AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
(
        n\_clusters\=params\["n\_clusters"\], linkage\="average"
    )
    single \= [cluster.AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
(
        n\_clusters\=params\["n\_clusters"\], linkage\="single"
    )

    clustering\_algorithms \= (
        ("Single Linkage", single),
        ("Average Linkage", average),
        ("Complete Linkage", complete),
        ("Ward Linkage", ward),
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

![Single Linkage, Average Linkage, Complete Linkage, Ward Linkage](https://scikit-learn.org/stable/_images/sphx_glr_plot_linkage_comparison_001.png)

**Total running time of the script:** (0 minutes 1.796 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_linkage_comparison.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_linkage_comparison.ipynb)

[`Download Jupyter notebook: plot_linkage_comparison.ipynb`](https://scikit-learn.org/stable/_downloads/be7e9c5a81790b318c3a8028ced647ff/plot_linkage_comparison.ipynb)

[`Download Python source code: plot_linkage_comparison.py`](https://scikit-learn.org/stable/_downloads/2338f6e7d44c2931a41926d4f9726d9b/plot_linkage_comparison.py)

[`Download zipped: plot_linkage_comparison.zip`](https://scikit-learn.org/stable/_downloads/7d5f3165d85bdb2073881abde39f904b/plot_linkage_comparison.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_linkage_thumb.png)

[Various Agglomerative Clustering on a 2D embedding of digits](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_linkage.html)

Various Agglomerative Clustering on a 2D embedding of digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ward_structured_vs_unstructured_thumb.png)

[Hierarchical clustering with and without structure](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)

Hierarchical clustering with and without structure

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_ward_segmentation_thumb.png)

[A demo of structured Ward hierarchical clustering on an image of coins](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html)

A demo of structured Ward hierarchical clustering on an image of coins

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/2338f6e7d44c2931a41926d4f9726d9b/plot_linkage_comparison.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/be7e9c5a81790b318c3a8028ced647ff/plot_linkage_comparison.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/7d5f3165d85bdb2073881abde39f904b/plot_linkage_comparison.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_linkage_comparison.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_linkage_comparison.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)