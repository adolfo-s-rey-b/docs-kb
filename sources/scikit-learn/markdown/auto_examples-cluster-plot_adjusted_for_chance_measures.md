[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_adjusted_for_chance_measures.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_adjusted_for_chance_measures.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_adjusted_for_chance_measures.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_adjusted_for_chance_measures.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_adjusted_for_chance_measures.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_adjusted_for_chance_measures.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html#sphx-glr-download-auto-examples-cluster-plot-adjusted-for-chance-measures-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Adjustment for chance in clustering performance evaluation[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html#adjustment-for-chance-in-clustering-performance-evaluation "Link to this heading")

==============================================================================================================================================================================================================================================

This notebook explores the impact of uniformly-distributed random labeling on the behavior of some clustering evaluation metrics. For such purpose, the metrics are computed with a fixed number of samples and as a function of the number of clusters assigned by the estimator. The example is divided into two experiments:

*   a first experiment with fixed “ground truth labels” (and therefore fixed number of classes) and randomly “predicted labels”;
    
*   a second experiment with varying “ground truth labels”, randomly “predicted labels”. The “predicted labels” have the same number of classes and clusters as the “ground truth labels”.
    

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Defining the list of metrics to evaluate[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html#defining-the-list-of-metrics-to-evaluate "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Clustering algorithms are fundamentally unsupervised learning methods. However, since we assign class labels for the synthetic clusters in this example, it is possible to use evaluation metrics that leverage this “supervised” ground truth information to quantify the quality of the resulting clusters. Examples of such metrics are the following:

*   V-measure, the harmonic mean of completeness and homogeneity;
    
*   Rand index, which measures how frequently pairs of data points are grouped consistently according to the result of the clustering algorithm and the ground truth class assignment;
    
*   Adjusted Rand index (ARI), a chance-adjusted Rand index such that a random cluster assignment has an ARI of 0.0 in expectation;
    
*   Mutual Information (MI) is an information theoretic measure that quantifies how dependent are the two labelings. Note that the maximum value of MI for perfect labelings depends on the number of clusters and samples;
    
*   Normalized Mutual Information (NMI), a Mutual Information defined between 0 (no mutual information) in the limit of large number of data points and 1 (perfectly matching label assignments, up to a permutation of the labels). It is not adjusted for chance: then the number of clustered data points is not large enough, the expected values of MI or NMI for random labelings can be significantly non-zero;
    
*   Adjusted Mutual Information (AMI), a chance-adjusted Mutual Information. Similarly to ARI, random cluster assignment has an AMI of 0.0 in expectation.
    

For more information, see the [Clustering performance evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation)
 module.

from sklearn import metrics

score\_funcs \= \[\
    ("V-measure", [metrics.v\_measure\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")\
),\
    ("Rand index", [metrics.rand\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#sklearn.metrics.rand_score "sklearn.metrics.rand_score")\
),\
    ("ARI", [metrics.adjusted\_rand\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#sklearn.metrics.adjusted_rand_score "sklearn.metrics.adjusted_rand_score")\
),\
    ("MI", [metrics.mutual\_info\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mutual_info_score.html#sklearn.metrics.mutual_info_score "sklearn.metrics.mutual_info_score")\
),\
    ("NMI", [metrics.normalized\_mutual\_info\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#sklearn.metrics.normalized_mutual_info_score "sklearn.metrics.normalized_mutual_info_score")\
),\
    ("AMI", [metrics.adjusted\_mutual\_info\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")\
),\
\]

Copy to clipboard

First experiment: fixed ground truth labels and growing number of clusters[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html#first-experiment-fixed-ground-truth-labels-and-growing-number-of-clusters "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We first define a function that creates uniformly-distributed random labeling.

import numpy as np

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)

def random\_labels(n\_samples, n\_classes):
    return rng.randint(low\=0, high\=n\_classes, size\=n\_samples)

Copy to clipboard

Another function will use the `random_labels` function to create a fixed set of ground truth labels (`labels_a`) distributed in `n_classes` and then score several sets of randomly “predicted” labels (`labels_b`) to assess the variability of a given metric at a given `n_clusters`.

def fixed\_classes\_uniform\_labelings\_scores(
    score\_func, n\_samples, n\_clusters\_range, n\_classes, n\_runs\=5
):
    scores \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((len(n\_clusters\_range), n\_runs))
    labels\_a \= random\_labels(n\_samples\=n\_samples, n\_classes\=n\_classes)

    for i, n\_clusters in enumerate(n\_clusters\_range):
        for j in range(n\_runs):
            labels\_b \= random\_labels(n\_samples\=n\_samples, n\_classes\=n\_clusters)
            scores\[i, j\] \= score\_func(labels\_a, labels\_b)
    return scores

Copy to clipboard

In this first example we set the number of classes (true number of clusters) to `n_classes=10`. The number of clusters varies over the values provided by `n_clusters_range`.

import matplotlib.pyplot as plt
import seaborn as sns

n\_samples \= 1000
n\_classes \= 10
n\_clusters\_range \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(2, 100, 10).astype(int)
plots \= \[\]
names \= \[\]

[sns.color\_palette](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
("colorblind")
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(1)

for marker, (score\_name, score\_func) in zip("d^vx.,", score\_funcs):
    scores \= fixed\_classes\_uniform\_labelings\_scores(
        score\_func, n\_samples, n\_clusters\_range, n\_classes\=n\_classes
    )
    plots.append(
        [plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
            n\_clusters\_range,
            scores.mean(axis\=1),
            scores.std(axis\=1),
            alpha\=0.8,
            linewidth\=1,
            marker\=marker,
        )\[0\]
    )
    names.append(score\_name)

[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    "Clustering measures for random uniform labeling\\n"
    f"against reference assignment with {n\_classes} classes"
)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
(f"Number of clusters (Number of samples is fixed to {n\_samples})")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Score value")
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(bottom\=-0.05, top\=1.05)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(plots, names, bbox\_to\_anchor\=(0.5, 0.5))
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Clustering measures for random uniform labeling against reference assignment with 10 classes](https://scikit-learn.org/stable/_images/sphx_glr_plot_adjusted_for_chance_measures_001.png)

The Rand index saturates for `n_clusters` > `n_classes`. Other non-adjusted measures such as the V-Measure show a linear dependency between the number of clusters and the number of samples.

Adjusted for chance measure, such as ARI and AMI, display some random variations centered around a mean score of 0.0, independently of the number of samples and clusters.

Second experiment: varying number of classes and clusters[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_adjusted_for_chance_measures.html#second-experiment-varying-number-of-classes-and-clusters "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section we define a similar function that uses several metrics to score 2 uniformly-distributed random labelings. In this case, the number of classes and assigned number of clusters are matched for each possible value in `n_clusters_range`.

def uniform\_labelings\_scores(score\_func, n\_samples, n\_clusters\_range, n\_runs\=5):
    scores \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((len(n\_clusters\_range), n\_runs))

    for i, n\_clusters in enumerate(n\_clusters\_range):
        for j in range(n\_runs):
            labels\_a \= random\_labels(n\_samples\=n\_samples, n\_classes\=n\_clusters)
            labels\_b \= random\_labels(n\_samples\=n\_samples, n\_classes\=n\_clusters)
            scores\[i, j\] \= score\_func(labels\_a, labels\_b)
    return scores

Copy to clipboard

In this case, we use `n_samples=100` to show the effect of having a number of clusters similar or equal to the number of samples.

n\_samples \= 100
n\_clusters\_range \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(2, n\_samples, 10).astype(int)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(2)

plots \= \[\]
names \= \[\]

for marker, (score\_name, score\_func) in zip("d^vx.,", score\_funcs):
    scores \= uniform\_labelings\_scores(score\_func, n\_samples, n\_clusters\_range)
    plots.append(
        [plt.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
(
            n\_clusters\_range,
            [np.median](https://numpy.org/doc/stable/reference/generated/numpy.median.html#numpy.median "numpy.median")
(scores, axis\=1),
            scores.std(axis\=1),
            alpha\=0.8,
            linewidth\=2,
            marker\=marker,
        )\[0\]
    )
    names.append(score\_name)

[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
    "Clustering measures for 2 random uniform labelings\\nwith equal number of clusters"
)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
(f"Number of clusters (Number of samples is fixed to {n\_samples})")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Score value")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(plots, names)
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(bottom\=-0.05, top\=1.05)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Clustering measures for 2 random uniform labelings with equal number of clusters](https://scikit-learn.org/stable/_images/sphx_glr_plot_adjusted_for_chance_measures_002.png)

We observe similar results as for the first experiment: adjusted for chance metrics stay constantly near zero while other metrics tend to get larger with finer-grained labelings. The mean V-measure of random labeling increases significantly as the number of clusters is closer to the total number of samples used to compute the measure. Furthermore, raw Mutual Information is unbounded from above and its scale depends on the dimensions of the clustering problem and the cardinality of the ground truth classes. This is why the curve goes off the chart.

Only adjusted measures can hence be safely used as a consensus index to evaluate the average stability of clustering algorithms for a given value of k on various overlapping sub-samples of the dataset.

Non-adjusted clustering evaluation metric can therefore be misleading as they output large values for fine-grained labelings, one could be lead to think that the labeling has captured meaningful groups while they can be totally random. In particular, such non-adjusted metrics should not be used to compare the results of different clustering algorithms that output a different number of clusters.

**Total running time of the script:** (0 minutes 1.177 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_adjusted_for_chance_measures.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_adjusted_for_chance_measures.ipynb)

[`Download Jupyter notebook: plot_adjusted_for_chance_measures.ipynb`](https://scikit-learn.org/stable/_downloads/7c06490f380b1e20e9558c6c5fde70ed/plot_adjusted_for_chance_measures.ipynb)

[`Download Python source code: plot_adjusted_for_chance_measures.py`](https://scikit-learn.org/stable/_downloads/f641388d3d28570ff40709693f9cb7ca/plot_adjusted_for_chance_measures.py)

[`Download zipped: plot_adjusted_for_chance_measures.zip`](https://scikit-learn.org/stable/_downloads/73099ec6cbf7cd0f232cf582342fdfd2/plot_adjusted_for_chance_measures.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dbscan_thumb.png)

[Demo of DBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html)

Demo of DBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_thumb.png)

[Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

Clustering text documents using k-means

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_silhouette_analysis_thumb.png)

[Selecting the number of clusters with silhouette analysis on KMeans clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)

Selecting the number of clusters with silhouette analysis on KMeans clustering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_clustering_metrics_thumb.png)

[Agglomerative clustering with different metrics](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_clustering_metrics.html)

Agglomerative clustering with different metrics

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/f641388d3d28570ff40709693f9cb7ca/plot_adjusted_for_chance_measures.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/7c06490f380b1e20e9558c6c5fde70ed/plot_adjusted_for_chance_measures.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/73099ec6cbf7cd0f232cf582342fdfd2/plot_adjusted_for_chance_measures.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_adjusted_for_chance_measures.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_adjusted_for_chance_measures.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)