[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html#sphx-glr-download-auto-examples-cluster-plot-kmeans-stability-low-dim-dense-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Empirical evaluation of the impact of k-means initialization[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html#empirical-evaluation-of-the-impact-of-k-means-initialization "Link to this heading")

====================================================================================================================================================================================================================================================

Evaluate the ability of k-means initializations strategies to make the algorithm convergence robust, as measured by the relative standard deviation of the inertia of the clustering (i.e. the sum of squared distances to the nearest cluster center).

The first plot shows the best inertia reached for each combination of the model (`KMeans` or `MiniBatchKMeans`), and the init method (`init="random"` or `init="k-means++"`) for increasing values of the `n_init` parameter that controls the number of initializations.

The second plot demonstrates one single run of the `MiniBatchKMeans` estimator using a `init="random"` and `n_init=1`. This run leads to a bad convergence (local optimum), with estimated centers stuck between ground truth clusters.

The dataset used for evaluation is a 2D grid of isotropic Gaussian clusters widely spaced.

*   ![Mean inertia for various k-means init across 5 runs](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_stability_low_dim_dense_001.png)
*   ![Example cluster allocation with a single random init with MiniBatchKMeans](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_stability_low_dim_dense_002.png)

Evaluation of KMeans with k-means++ init
Evaluation of KMeans with random init
Evaluation of MiniBatchKMeans with k-means++ init
Evaluation of MiniBatchKMeans with random init

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
, [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
from sklearn.utils import [check\_random\_state](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")
, [shuffle](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#sklearn.utils.shuffle "sklearn.utils.shuffle")

random\_state \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)

\# Number of run (with randomly generated dataset) for each strategy so as
\# to be able to compute an estimate of the standard deviation
n\_runs \= 5

\# k-means models can do several random inits so as to be able to trade
\# CPU time for convergence robustness
n\_init\_range \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[1, 5, 10, 15, 20\])

\# Datasets generation parameters
n\_samples\_per\_center \= 100
grid\_size \= 3
scale \= 0.1
n\_clusters \= grid\_size\*\*2

def make\_data(random\_state, n\_samples\_per\_center, grid\_size, scale):
    random\_state \= [check\_random\_state](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")
(random\_state)
    centers \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[i, j\] for i in range(grid\_size) for j in range(grid\_size)\])
    n\_clusters\_true, n\_features \= centers.shape

    noise \= random\_state.normal(
        scale\=scale, size\=(n\_samples\_per\_center, centers.shape\[1\])
    )

    X \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[c + noise for c in centers\])
    y \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[\[i\] \* n\_samples\_per\_center for i in range(n\_clusters\_true)\])
    return [shuffle](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#sklearn.utils.shuffle "sklearn.utils.shuffle")
(X, y, random\_state\=random\_state)

\# Part 1: Quantitative evaluation of various init methods

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
plots \= \[\]
legends \= \[\]

cases \= \[\
    ([KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")\
, "k-means++", {}, "^-"),\
    ([KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")\
, "random", {}, "o-"),\
    ([MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")\
, "k-means++", {"max\_no\_improvement": 3}, "x-"),\
    ([MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")\
, "random", {"max\_no\_improvement": 3, "init\_size": 500}, "d-"),\
\]

for factory, init, params, format in cases:
    print("Evaluation of %s with %s init" % (factory.\_\_name\_\_, init))
    inertia \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
((len(n\_init\_range), n\_runs))

    for run\_id in range(n\_runs):
        X, y \= make\_data(run\_id, n\_samples\_per\_center, grid\_size, scale)
        for i, n\_init in enumerate(n\_init\_range):
            km \= factory(
                n\_clusters\=n\_clusters,
                init\=init,
                random\_state\=run\_id,
                n\_init\=n\_init,
                \*\*params,
            ).fit(X)
            inertia\[i, run\_id\] \= km.inertia\_
    p \= [plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
        n\_init\_range, inertia.mean(axis\=1), inertia.std(axis\=1), fmt\=format
    )
    plots.append(p\[0\])
    legends.append("%s with %s init" % (factory.\_\_name\_\_, init))

[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("n\_init")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("inertia")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(plots, legends)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Mean inertia for various k-means init across %d runs" % n\_runs)

\# Part 2: Qualitative visual inspection of the convergence

X, y \= make\_data(random\_state, n\_samples\_per\_center, grid\_size, scale)
km \= [MiniBatchKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
(
    n\_clusters\=n\_clusters, init\="random", n\_init\=1, random\_state\=random\_state
).fit(X)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
for k in range(n\_clusters):
    my\_members \= km.labels\_ \== k
    color \= cm.nipy\_spectral(float(k) / n\_clusters, 1)
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\[my\_members, 0\], X\[my\_members, 1\], ".", c\=color)
    cluster\_center \= km.cluster\_centers\_\[k\]
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
        cluster\_center\[0\],
        cluster\_center\[1\],
        "o",
        markerfacecolor\=color,
        markeredgecolor\="k",
        markersize\=6,
    )
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
        "Example cluster allocation with a single random init\\nwith MiniBatchKMeans"
    )

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 1.250 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_kmeans_stability_low_dim_dense.ipynb)

[`Download Jupyter notebook: plot_kmeans_stability_low_dim_dense.ipynb`](https://scikit-learn.org/stable/_downloads/7e9cf82b8b60275dd7851470d151af5f/plot_kmeans_stability_low_dim_dense.ipynb)

[`Download Python source code: plot_kmeans_stability_low_dim_dense.py`](https://scikit-learn.org/stable/_downloads/4b8d8f0d50e5aa937ac9571a35eadc28/plot_kmeans_stability_low_dim_dense.py)

[`Download zipped: plot_kmeans_stability_low_dim_dense.zip`](https://scikit-learn.org/stable/_downloads/7b4d196feed2f34aae28e18d96971f8d/plot_kmeans_stability_low_dim_dense.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mini_batch_kmeans_thumb.png)

[Comparison of the K-Means and MiniBatchKMeans clustering algorithms](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html)

Comparison of the K-Means and MiniBatchKMeans clustering algorithms

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_digits_thumb.png)

[A demo of K-Means clustering on the handwritten digits data](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html)

A demo of K-Means clustering on the handwritten digits data

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bisect_kmeans_thumb.png)

[Bisecting K-Means and Regular K-Means Performance Comparison](https://scikit-learn.org/stable/auto_examples/cluster/plot_bisect_kmeans.html)

Bisecting K-Means and Regular K-Means Performance Comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_thumb.png)

[Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

Clustering text documents using k-means

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/4b8d8f0d50e5aa937ac9571a35eadc28/plot_kmeans_stability_low_dim_dense.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/7e9cf82b8b60275dd7851470d151af5f/plot_kmeans_stability_low_dim_dense.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/7b4d196feed2f34aae28e18d96971f8d/plot_kmeans_stability_low_dim_dense.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_kmeans_stability_low_dim_dense.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)