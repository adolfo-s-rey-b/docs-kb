[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_kmeans_digits.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_kmeans_digits.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_kmeans_digits.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_kmeans_digits.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_kmeans_digits.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_kmeans_digits.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#sphx-glr-download-auto-examples-cluster-plot-kmeans-digits-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

A demo of K-Means clustering on the handwritten digits data[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#a-demo-of-k-means-clustering-on-the-handwritten-digits-data "Link to this heading")

=================================================================================================================================================================================================================================

In this example we compare the various initialization strategies for K-means in terms of runtime and quality of the results.

As the ground truth is known here, we also apply different cluster quality metrics to judge the goodness of fit of the cluster labels to the ground truth.

Cluster quality metrics evaluated (see [Clustering performance evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation)
 for definitions and discussions of the metrics):

| Shorthand | full name |
| --- | --- |
| homo | homogeneity score |
| compl | completeness score |
| v-meas | V measure |
| ARI | adjusted Rand index |
| AMI | adjusted mutual information |
| silhouette | silhouette coefficient |

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Load the dataset[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#load-the-dataset "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

We will start by loading the `digits` dataset. This dataset contains handwritten digits from 0 to 9. In the context of clustering, one would like to group images such that the handwritten digits on the image are the same.

import numpy as np

from sklearn.datasets import [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")

data, labels \= [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
(return\_X\_y\=True)
(n\_samples, n\_features), n\_digits \= data.shape, [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(labels).size

print(f"# digits: {n\_digits}; # samples: {n\_samples}; # features {n\_features}")

Copy to clipboard

\# digits: 10; # samples: 1797; # features 64

Copy to clipboard

Define our evaluation benchmark[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#define-our-evaluation-benchmark "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We will first our evaluation benchmark. During this benchmark, we intend to compare different initialization methods for KMeans. Our benchmark will:

*   create a pipeline which will scale the data using a [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
    ;
    
*   train and time the pipeline fitting;
    
*   measure the performance of the clustering obtained via different metrics.
    

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

from sklearn import metrics
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

def bench\_k\_means(kmeans, name, data, labels):
    """Benchmark to evaluate the KMeans initialization methods.

    Parameters
    ----------
    kmeans : KMeans instance
        A :class:\`~sklearn.cluster.KMeans\` instance with the initialization
        already set.
    name : str
        Name given to the strategy. It will be used to show the results in a
        table.
    data : ndarray of shape (n\_samples, n\_features)
        The data to cluster.
    labels : ndarray of shape (n\_samples,)
        The labels used to compute the clustering metrics which requires some
        supervision.
    """
    t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    estimator \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), kmeans).fit(data)
    fit\_time \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
    results \= \[name, fit\_time, estimator\[\-1\].inertia\_\]

    \# Define the metrics which require only the true labels and estimator
    \# labels
    clustering\_metrics \= \[\
        [metrics.homogeneity\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html#sklearn.metrics.homogeneity_score "sklearn.metrics.homogeneity_score")\
,\
        [metrics.completeness\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.completeness_score.html#sklearn.metrics.completeness_score "sklearn.metrics.completeness_score")\
,\
        [metrics.v\_measure\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")\
,\
        [metrics.adjusted\_rand\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#sklearn.metrics.adjusted_rand_score "sklearn.metrics.adjusted_rand_score")\
,\
        [metrics.adjusted\_mutual\_info\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")\
,\
    \]
    results += \[m(labels, estimator\[\-1\].labels\_) for m in clustering\_metrics\]

    \# The silhouette score requires the full dataset
    results += \[\
        [metrics.silhouette\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")\
(\
            data,\
            estimator\[\-1\].labels\_,\
            metric\="euclidean",\
            sample\_size\=300,\
        )\
    \]

    \# Show the results
    formatter\_result \= (
        "{:9s}\\t{:.3f}s\\t{:.0f}\\t{:.3f}\\t{:.3f}\\t{:.3f}\\t{:.3f}\\t{:.3f}\\t{:.3f}"
    )
    print(formatter\_result.format(\*results))

Copy to clipboard

Run the benchmark[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#run-the-benchmark "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

We will compare three approaches:

*   an initialization using `k-means++`. This method is stochastic and we will run the initialization 4 times;
    
*   a random initialization. This method is stochastic as well and we will run the initialization 4 times;
    
*   an initialization based on a [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     projection. Indeed, we will use the components of the [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     to initialize KMeans. This method is deterministic and a single initialization suffice.
    

from sklearn.cluster import [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

print(82 \* "\_")
print("init\\t\\ttime\\tinertia\\thomo\\tcompl\\tv-meas\\tARI\\tAMI\\tsilhouette")

kmeans \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(init\="k-means++", n\_clusters\=n\_digits, n\_init\=4, random\_state\=0)
bench\_k\_means(kmeans\=kmeans, name\="k-means++", data\=data, labels\=labels)

kmeans \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(init\="random", n\_clusters\=n\_digits, n\_init\=4, random\_state\=0)
bench\_k\_means(kmeans\=kmeans, name\="random", data\=data, labels\=labels)

pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=n\_digits).fit(data)
kmeans \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(init\=pca.components\_, n\_clusters\=n\_digits, n\_init\=1)
bench\_k\_means(kmeans\=kmeans, name\="PCA-based", data\=data, labels\=labels)

print(82 \* "\_")

Copy to clipboard

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
init            time    inertia homo    compl   v-meas  ARI     AMI     silhouette
k-means++       0.027s  69545   0.598   0.645   0.621   0.469   0.617   0.171
random          0.031s  69735   0.681   0.723   0.701   0.574   0.698   0.173
PCA-based       0.011s  69513   0.600   0.647   0.622   0.468   0.618   0.162
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Copy to clipboard

Visualize the results on PCA-reduced data[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html#visualize-the-results-on-pca-reduced-data "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
 allows to project the data from the original 64-dimensional space into a lower dimensional space. Subsequently, we can use [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
 to project into a 2-dimensional space and plot the data and the clusters in this new space.

import matplotlib.pyplot as plt

from sklearn.inspection import DecisionBoundaryDisplay

reduced\_data \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=2).fit\_transform(data)
kmeans \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(init\="k-means++", n\_clusters\=n\_digits, n\_init\=4, random\_state\=42)
kmeans.fit(reduced\_data)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()

[DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    kmeans,
    reduced\_data,
    ax\=[plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
(),
    response\_method\="predict",
    alpha\=0.8,
    plot\_method\="pcolormesh",
    grid\_resolution\=1000,
)

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(reduced\_data\[:, 0\], reduced\_data\[:, 1\], "k.", markersize\=2)
\# Plot the centroids as a white X
centroids \= kmeans.cluster\_centers\_
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    centroids\[:, 0\],
    centroids\[:, 1\],
    marker\="x",
    s\=169,
    linewidths\=3,
    color\="w",
    zorder\=10,
)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    "K-means clustering on the digits dataset (PCA-reduced data)\\n"
    "Centroids are marked with white cross"
)
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
[plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![K-means clustering on the digits dataset (PCA-reduced data) Centroids are marked with white cross](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_digits_001.png)

**Total running time of the script:** (0 minutes 0.902 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_kmeans_digits.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_kmeans_digits.ipynb)

[`Download Jupyter notebook: plot_kmeans_digits.ipynb`](https://scikit-learn.org/stable/_downloads/6bf322ce1724c13e6e0f8f719ebd253c/plot_kmeans_digits.ipynb)

[`Download Python source code: plot_kmeans_digits.py`](https://scikit-learn.org/stable/_downloads/5a87b25ba023ee709595b8d02049f021/plot_kmeans_digits.py)

[`Download zipped: plot_kmeans_digits.zip`](https://scikit-learn.org/stable/_downloads/1393861b58df827d4c681b80a5be2472/plot_kmeans_digits.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_thumb.png)

[Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

Clustering text documents using k-means

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mini_batch_kmeans_thumb.png)

[Comparison of the K-Means and MiniBatchKMeans clustering algorithms](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html)

Comparison of the K-Means and MiniBatchKMeans clustering algorithms

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_stability_low_dim_dense_thumb.png)

[Empirical evaluation of the impact of k-means initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_stability_low_dim_dense.html)

Empirical evaluation of the impact of k-means initialization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_init_thumb.png)

[GMM Initialization Methods](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_init.html)

GMM Initialization Methods

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/5a87b25ba023ee709595b8d02049f021/plot_kmeans_digits.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/6bf322ce1724c13e6e0f8f719ebd253c/plot_kmeans_digits.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/1393861b58df827d4c681b80a5be2472/plot_kmeans_digits.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_kmeans_digits.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_kmeans_digits.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)