[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_kmeans_assumptions.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_kmeans_assumptions.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_kmeans_assumptions.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_kmeans_assumptions.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_kmeans_assumptions.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_kmeans_assumptions.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#sphx-glr-download-auto-examples-cluster-plot-kmeans-assumptions-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Demonstration of k-means assumptions[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#demonstration-of-k-means-assumptions "Link to this heading")

========================================================================================================================================================================================

This example is meant to illustrate situations where k-means produces unintuitive and possibly undesirable clusters.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Data generation[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#data-generation "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

The function [`make_blobs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
 generates isotropic (spherical) gaussian blobs. To obtain anisotropic (elliptical) gaussian blobs one has to define a linear `transformation`.

import numpy as np

from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")

n\_samples \= 1500
random\_state \= 170
transformation \= \[\[0.60834549, \-0.63667341\], \[\-0.40887718, 0.85253229\]\]

X, y \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=n\_samples, random\_state\=random\_state)
X\_aniso \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(X, transformation)  \# Anisotropic blobs
X\_varied, y\_varied \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(
    n\_samples\=n\_samples, cluster\_std\=\[1.0, 2.5, 0.5\], random\_state\=random\_state
)  \# Unequal variance
X\_filtered \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(
    (X\[y \== 0\]\[:500\], X\[y \== 1\]\[:100\], X\[y \== 2\]\[:10\])
)  \# Unevenly sized blobs
y\_filtered \= \[0\] \* 500 + \[1\] \* 100 + \[2\] \* 10

Copy to clipboard

We can visualize the resulting data:

import matplotlib.pyplot as plt

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=2, figsize\=(12, 12))

axs\[0, 0\].scatter(X\[:, 0\], X\[:, 1\], c\=y)
axs\[0, 0\].set\_title("Mixture of Gaussian Blobs")

axs\[0, 1\].scatter(X\_aniso\[:, 0\], X\_aniso\[:, 1\], c\=y)
axs\[0, 1\].set\_title("Anisotropically Distributed Blobs")

axs\[1, 0\].scatter(X\_varied\[:, 0\], X\_varied\[:, 1\], c\=y\_varied)
axs\[1, 0\].set\_title("Unequal Variance")

axs\[1, 1\].scatter(X\_filtered\[:, 0\], X\_filtered\[:, 1\], c\=y\_filtered)
axs\[1, 1\].set\_title("Unevenly Sized Blobs")

[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
("Ground truth clusters").set\_y(0.95)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Ground truth clusters, Mixture of Gaussian Blobs, Anisotropically Distributed Blobs, Unequal Variance, Unevenly Sized Blobs](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_assumptions_001.png)

Fit models and plot results[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#fit-models-and-plot-results "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

The previously generated data is now used to show how [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
 behaves in the following scenarios:

*   Non-optimal number of clusters: in a real setting there is no uniquely defined **true** number of clusters. An appropriate number of clusters has to be decided from data-based criteria and knowledge of the intended goal.
    
*   Anisotropically distributed blobs: k-means consists of minimizing sample’s euclidean distances to the centroid of the cluster they are assigned to. As a consequence, k-means is more appropriate for clusters that are isotropic and normally distributed (i.e. spherical gaussians).
    
*   Unequal variance: k-means is equivalent to taking the maximum likelihood estimator for a “mixture” of k gaussian distributions with the same variances but with possibly different means.
    
*   Unevenly sized blobs: there is no theoretical result about k-means that states that it requires similar cluster sizes to perform well, yet minimizing euclidean distances does mean that the more sparse and high-dimensional the problem is, the higher is the need to run the algorithm with different centroid seeds to ensure a global minimal inertia.
    

from sklearn.cluster import [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")

common\_params \= {
    "n\_init": "auto",
    "random\_state": random\_state,
}

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=2, figsize\=(12, 12))

y\_pred \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(n\_clusters\=2, \*\*common\_params).fit\_predict(X)
axs\[0, 0\].scatter(X\[:, 0\], X\[:, 1\], c\=y\_pred)
axs\[0, 0\].set\_title("Non-optimal Number of Clusters")

y\_pred \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(n\_clusters\=3, \*\*common\_params).fit\_predict(X\_aniso)
axs\[0, 1\].scatter(X\_aniso\[:, 0\], X\_aniso\[:, 1\], c\=y\_pred)
axs\[0, 1\].set\_title("Anisotropically Distributed Blobs")

y\_pred \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(n\_clusters\=3, \*\*common\_params).fit\_predict(X\_varied)
axs\[1, 0\].scatter(X\_varied\[:, 0\], X\_varied\[:, 1\], c\=y\_pred)
axs\[1, 0\].set\_title("Unequal Variance")

y\_pred \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(n\_clusters\=3, \*\*common\_params).fit\_predict(X\_filtered)
axs\[1, 1\].scatter(X\_filtered\[:, 0\], X\_filtered\[:, 1\], c\=y\_pred)
axs\[1, 1\].set\_title("Unevenly Sized Blobs")

[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
("Unexpected KMeans clusters").set\_y(0.95)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Unexpected KMeans clusters, Non-optimal Number of Clusters, Anisotropically Distributed Blobs, Unequal Variance, Unevenly Sized Blobs](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_assumptions_002.png)

Possible solutions[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#possible-solutions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

For an example on how to find a correct number of blobs, see [Selecting the number of clusters with silhouette analysis on KMeans clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html#sphx-glr-auto-examples-cluster-plot-kmeans-silhouette-analysis-py)
. In this case it suffices to set `n_clusters=3`.

y\_pred \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(n\_clusters\=3, \*\*common\_params).fit\_predict(X)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], c\=y\_pred)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Optimal Number of Clusters")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Optimal Number of Clusters](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_assumptions_003.png)

To deal with unevenly sized blobs one can increase the number of random initializations. In this case we set `n_init=10` to avoid finding a sub-optimal local minimum. For more details see [Clustering sparse data with k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#kmeans-sparse-high-dim)
.

y\_pred \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(n\_clusters\=3, n\_init\=10, random\_state\=random\_state).fit\_predict(
    X\_filtered
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_filtered\[:, 0\], X\_filtered\[:, 1\], c\=y\_pred)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Unevenly Sized Blobs \\nwith several initializations")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Unevenly Sized Blobs  with several initializations](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_assumptions_004.png)

As anisotropic and unequal variances are real limitations of the k-means algorithm, here we propose instead the use of [`GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
, which also assumes gaussian clusters but does not impose any constraints on their variances. Notice that one still has to find the correct number of blobs (see [Gaussian Mixture Model Selection](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html#sphx-glr-auto-examples-mixture-plot-gmm-selection-py)
).

For an example on how other clustering methods deal with anisotropic or unequal variance blobs, see the example [Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html#sphx-glr-auto-examples-cluster-plot-cluster-comparison-py)
.

from sklearn.mixture import [GaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")

fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=2, figsize\=(12, 6))

y\_pred \= [GaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
(n\_components\=3).fit\_predict(X\_aniso)
ax1.scatter(X\_aniso\[:, 0\], X\_aniso\[:, 1\], c\=y\_pred)
ax1.set\_title("Anisotropically Distributed Blobs")

y\_pred \= [GaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
(n\_components\=3).fit\_predict(X\_varied)
ax2.scatter(X\_varied\[:, 0\], X\_varied\[:, 1\], c\=y\_pred)
ax2.set\_title("Unequal Variance")

[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
("Gaussian mixture clusters").set\_y(0.95)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Gaussian mixture clusters, Anisotropically Distributed Blobs, Unequal Variance](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_assumptions_005.png)

Final remarks[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#final-remarks "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

In high-dimensional spaces, Euclidean distances tend to become inflated (not shown in this example). Running a dimensionality reduction algorithm prior to k-means clustering can alleviate this problem and speed up the computations (see the example [Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#sphx-glr-auto-examples-text-plot-document-clustering-py)
).

In the case where clusters are known to be isotropic, have similar variance and are not too sparse, the k-means algorithm is quite effective and is one of the fastest clustering algorithms available. This advantage is lost if one has to restart it several times to avoid convergence to a local minimum.

**Total running time of the script:** (0 minutes 1.087 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_kmeans_assumptions.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_kmeans_assumptions.ipynb)

[`Download Jupyter notebook: plot_kmeans_assumptions.ipynb`](https://scikit-learn.org/stable/_downloads/b05e6cdf6d51481f37bf29b0bb92995e/plot_kmeans_assumptions.ipynb)

[`Download Python source code: plot_kmeans_assumptions.py`](https://scikit-learn.org/stable/_downloads/5d2d581a4569eb0718dbdb8abf7cbbdf/plot_kmeans_assumptions.py)

[`Download zipped: plot_kmeans_assumptions.zip`](https://scikit-learn.org/stable/_downloads/1929d77b217d252c180ea45cab60f1c0/plot_kmeans_assumptions.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bisect_kmeans_thumb.png)

[Bisecting K-Means and Regular K-Means Performance Comparison](https://scikit-learn.org/stable/auto_examples/cluster/plot_bisect_kmeans.html)

Bisecting K-Means and Regular K-Means Performance Comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linkage_comparison_thumb.png)

[Comparing different hierarchical linkage methods on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html)

Comparing different hierarchical linkage methods on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_predict_thumb.png)

[Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html)

Plotting Cross-Validated Predictions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_digits_thumb.png)

[A demo of K-Means clustering on the handwritten digits data](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html)

A demo of K-Means clustering on the handwritten digits data

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/5d2d581a4569eb0718dbdb8abf7cbbdf/plot_kmeans_assumptions.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/b05e6cdf6d51481f37bf29b0bb92995e/plot_kmeans_assumptions.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/1929d77b217d252c180ea45cab60f1c0/plot_kmeans_assumptions.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_kmeans_assumptions.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_kmeans_assumptions.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)