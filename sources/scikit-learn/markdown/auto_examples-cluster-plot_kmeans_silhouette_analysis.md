[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html#sphx-glr-download-auto-examples-cluster-plot-kmeans-silhouette-analysis-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Selecting the number of clusters with silhouette analysis on KMeans clustering[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html#selecting-the-number-of-clusters-with-silhouette-analysis-on-kmeans-clustering "Link to this heading")

====================================================================================================================================================================================================================================================================================

Silhouette analysis can be used to study the separation distance between the resulting clusters. The silhouette plot displays a measure of how close each point in one cluster is to points in the neighboring clusters and thus provides a way to assess parameters like number of clusters visually. This measure has a range of \[-1, 1\].

Silhouette coefficients (as these values are referred to as) near +1 indicate that the sample is far away from the neighboring clusters. A value of 0 indicates that the sample is on or very close to the decision boundary between two neighboring clusters and negative values indicate that those samples might have been assigned to the wrong cluster.

In this example the silhouette analysis is used to choose an optimal value for `n_clusters`. The silhouette plot shows that the `n_clusters` value of 3, 5 and 6 are a bad pick for the given data due to the presence of clusters with below average silhouette scores and also due to wide fluctuations in the size of the silhouette plots. Silhouette analysis is more ambivalent in deciding between 2 and 4.

Also from the thickness of the silhouette plot the cluster size can be visualized. The silhouette plot for cluster 0 when `n_clusters` is equal to 2, is bigger in size owing to the grouping of the 3 sub clusters into one big cluster. However when the `n_clusters` is equal to 4, all the plots are more or less of similar thickness and hence are of similar sizes as can be also verified from the labelled scatter plot on the right.

*   ![Silhouette analysis for KMeans clustering on sample data with n_clusters = 2, The silhouette plot for the various clusters., The visualization of the clustered data.](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_silhouette_analysis_001.png)
*   ![Silhouette analysis for KMeans clustering on sample data with n_clusters = 3, The silhouette plot for the various clusters., The visualization of the clustered data.](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_silhouette_analysis_002.png)
*   ![Silhouette analysis for KMeans clustering on sample data with n_clusters = 4, The silhouette plot for the various clusters., The visualization of the clustered data.](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_silhouette_analysis_003.png)
*   ![Silhouette analysis for KMeans clustering on sample data with n_clusters = 5, The silhouette plot for the various clusters., The visualization of the clustered data.](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_silhouette_analysis_004.png)
*   ![Silhouette analysis for KMeans clustering on sample data with n_clusters = 6, The silhouette plot for the various clusters., The visualization of the clustered data.](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_silhouette_analysis_005.png)

For n\_clusters = 2 The average silhouette\_score is : 0.7049787496083262
For n\_clusters = 3 The average silhouette\_score is : 0.5882004012129721
For n\_clusters = 4 The average silhouette\_score is : 0.6505186632729437
For n\_clusters = 5 The average silhouette\_score is : 0.561464362648773
For n\_clusters = 6 The average silhouette\_score is : 0.4857596147013469

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
from sklearn.metrics import [silhouette\_samples](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html#sklearn.metrics.silhouette_samples "sklearn.metrics.silhouette_samples")
, [silhouette\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")

\# Generating the sample data from make\_blobs
\# This particular setting has one distinct cluster and 3 clusters placed close
\# together.
X, y \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(
    n\_samples\=500,
    n\_features\=2,
    centers\=4,
    cluster\_std\=1,
    center\_box\=(\-10.0, 10.0),
    shuffle\=True,
    random\_state\=1,
)  \# For reproducibility

range\_n\_clusters \= \[2, 3, 4, 5, 6\]

for n\_clusters in range\_n\_clusters:
    \# Create a subplot with 1 row and 2 columns
    fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2)
    fig.set\_size\_inches(18, 7)

    \# The 1st subplot is the silhouette plot
    \# The silhouette coefficient can range from -1, 1 but in this example all
    \# lie within \[-0.1, 1\]
    ax1.set\_xlim(\[\-0.1, 1\])
    \# The (n\_clusters+1)\*10 is for inserting blank space between silhouette
    \# plots of individual clusters, to demarcate them clearly.
    ax1.set\_ylim(\[0, len(X) + (n\_clusters + 1) \* 10\])

    \# Initialize the clusterer with n\_clusters value and a random generator
    \# seed of 10 for reproducibility.
    clusterer \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
(n\_clusters\=n\_clusters, random\_state\=10)
    cluster\_labels \= clusterer.fit\_predict(X)

    \# The silhouette\_score gives the average value for all the samples.
    \# This gives a perspective into the density and separation of the formed
    \# clusters
    silhouette\_avg \= [silhouette\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")
(X, cluster\_labels)
    print(
        "For n\_clusters =",
        n\_clusters,
        "The average silhouette\_score is :",
        silhouette\_avg,
    )

    \# Compute the silhouette scores for each sample
    sample\_silhouette\_values \= [silhouette\_samples](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html#sklearn.metrics.silhouette_samples "sklearn.metrics.silhouette_samples")
(X, cluster\_labels)

    y\_lower \= 10
    for i in range(n\_clusters):
        \# Aggregate the silhouette scores for samples belonging to
        \# cluster i, and sort them
        ith\_cluster\_silhouette\_values \= sample\_silhouette\_values\[cluster\_labels \== i\]

        ith\_cluster\_silhouette\_values.sort()

        size\_cluster\_i \= ith\_cluster\_silhouette\_values.shape\[0\]
        y\_upper \= y\_lower + size\_cluster\_i

        color \= cm.nipy\_spectral(float(i) / n\_clusters)
        ax1.fill\_betweenx(
            [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(y\_lower, y\_upper),
            0,
            ith\_cluster\_silhouette\_values,
            facecolor\=color,
            edgecolor\=color,
            alpha\=0.7,
        )

        \# Label the silhouette plots with their cluster numbers at the middle
        ax1.text(\-0.05, y\_lower + 0.5 \* size\_cluster\_i, str(i))

        \# Compute the new y\_lower for next plot
        y\_lower \= y\_upper + 10  \# 10 for the 0 samples

    ax1.set\_title("The silhouette plot for the various clusters.")
    ax1.set\_xlabel("The silhouette coefficient values")
    ax1.set\_ylabel("Cluster label")

    \# The vertical line for average silhouette score of all the values
    ax1.axvline(x\=silhouette\_avg, color\="red", linestyle\="--")

    ax1.set\_yticks(\[\])  \# Clear the yaxis labels / ticks
    ax1.set\_xticks(\[\-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1\])

    \# 2nd Plot showing the actual clusters formed
    colors \= cm.nipy\_spectral(cluster\_labels.astype(float) / n\_clusters)
    ax2.scatter(
        X\[:, 0\], X\[:, 1\], marker\=".", s\=30, lw\=0, alpha\=0.7, c\=colors, edgecolor\="k"
    )

    \# Labeling the clusters
    centers \= clusterer.cluster\_centers\_
    \# Draw white circles at cluster centers
    ax2.scatter(
        centers\[:, 0\],
        centers\[:, 1\],
        marker\="o",
        c\="white",
        alpha\=1,
        s\=200,
        edgecolor\="k",
    )

    for i, c in enumerate(centers):
        ax2.scatter(c\[0\], c\[1\], marker\="$%d$" % i, alpha\=1, s\=50, edgecolor\="k")

    ax2.set\_title("The visualization of the clustered data.")
    ax2.set\_xlabel("Feature space for the 1st feature")
    ax2.set\_ylabel("Feature space for the 2nd feature")

    [plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
(
        "Silhouette analysis for KMeans clustering on sample data with n\_clusters = %d"
        % n\_clusters,
        fontsize\=14,
        fontweight\="bold",
    )

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 1.105 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_kmeans_silhouette_analysis.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_kmeans_silhouette_analysis.ipynb)

[`Download Jupyter notebook: plot_kmeans_silhouette_analysis.ipynb`](https://scikit-learn.org/stable/_downloads/2434f000f4405168e6285a3e410c709f/plot_kmeans_silhouette_analysis.ipynb)

[`Download Python source code: plot_kmeans_silhouette_analysis.py`](https://scikit-learn.org/stable/_downloads/586f6cb589cefcd68d55348630efbfa0/plot_kmeans_silhouette_analysis.py)

[`Download zipped: plot_kmeans_silhouette_analysis.zip`](https://scikit-learn.org/stable/_downloads/a0e7bd40b2cd97ee01b5c2e0bf212505/plot_kmeans_silhouette_analysis.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bisect_kmeans_thumb.png)

[Bisecting K-Means and Regular K-Means Performance Comparison](https://scikit-learn.org/stable/auto_examples/cluster/plot_bisect_kmeans.html)

Bisecting K-Means and Regular K-Means Performance Comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dbscan_thumb.png)

[Demo of DBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html)

Demo of DBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_digits_thumb.png)

[A demo of K-Means clustering on the handwritten digits data](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html)

A demo of K-Means clustering on the handwritten digits data

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_thumb.png)

[Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

Clustering text documents using k-means

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/586f6cb589cefcd68d55348630efbfa0/plot_kmeans_silhouette_analysis.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/2434f000f4405168e6285a3e410c709f/plot_kmeans_silhouette_analysis.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/a0e7bd40b2cd97ee01b5c2e0bf212505/plot_kmeans_silhouette_analysis.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_kmeans_silhouette_analysis.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_kmeans_silhouette_analysis.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)