[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_affinity_propagation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_affinity_propagation.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_affinity_propagation.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_affinity_propagation.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_affinity_propagation.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_affinity_propagation.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html#sphx-glr-download-auto-examples-cluster-plot-affinity-propagation-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Demo of affinity propagation clustering algorithm[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html#demo-of-affinity-propagation-clustering-algorithm "Link to this heading")

====================================================================================================================================================================================================================

Reference: Brendan J. Frey and Delbert Dueck, “Clustering by Passing Messages Between Data Points”, Science Feb. 2007

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import numpy as np

from sklearn import metrics
from sklearn.cluster import [AffinityPropagation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")

Copy to clipboard

Generate sample data[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html#generate-sample-data "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

centers \= \[\[1, 1\], \[\-1, \-1\], \[1, \-1\]\]
X, labels\_true \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(
    n\_samples\=300, centers\=centers, cluster\_std\=0.5, random\_state\=0
)

Copy to clipboard

Compute Affinity Propagation[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html#compute-affinity-propagation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

af \= [AffinityPropagation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
(preference\=-50, random\_state\=0).fit(X)
cluster\_centers\_indices \= af.cluster\_centers\_indices\_
labels \= af.labels\_

n\_clusters\_ \= len(cluster\_centers\_indices)

print("Estimated number of clusters: %d" % n\_clusters\_)
print("Homogeneity: %0.3f" % [metrics.homogeneity\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html#sklearn.metrics.homogeneity_score "sklearn.metrics.homogeneity_score")
(labels\_true, labels))
print("Completeness: %0.3f" % [metrics.completeness\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.completeness_score.html#sklearn.metrics.completeness_score "sklearn.metrics.completeness_score")
(labels\_true, labels))
print("V-measure: %0.3f" % [metrics.v\_measure\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")
(labels\_true, labels))
print("Adjusted Rand Index: %0.3f" % [metrics.adjusted\_rand\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#sklearn.metrics.adjusted_rand_score "sklearn.metrics.adjusted_rand_score")
(labels\_true, labels))
print(
    "Adjusted Mutual Information: %0.3f"
    % [metrics.adjusted\_mutual\_info\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")
(labels\_true, labels)
)
print(
    "Silhouette Coefficient: %0.3f"
    % [metrics.silhouette\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")
(X, labels, metric\="sqeuclidean")
)

Copy to clipboard

Estimated number of clusters: 3
Homogeneity: 0.872
Completeness: 0.872
V-measure: 0.872
Adjusted Rand Index: 0.912
Adjusted Mutual Information: 0.871
Silhouette Coefficient: 0.753

Copy to clipboard

Plot result[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html#plot-result "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

[plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
("all")
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(1)
[plt.clf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clf.html#matplotlib.pyplot.clf "matplotlib.pyplot.clf")
()

colors \= plt.cycler("color", plt.cm.viridis([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 4)))

for k, col in zip(range(n\_clusters\_), colors):
    class\_members \= labels \== k
    cluster\_center \= X\[cluster\_centers\_indices\[k\]\]
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
        X\[class\_members, 0\], X\[class\_members, 1\], color\=col\["color"\], marker\="."
    )
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
        cluster\_center\[0\], cluster\_center\[1\], s\=14, color\=col\["color"\], marker\="o"
    )
    for x in X\[class\_members\]:
        [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
            \[cluster\_center\[0\], x\[0\]\], \[cluster\_center\[1\], x\[1\]\], color\=col\["color"\]
        )

[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Estimated number of clusters: %d" % n\_clusters\_)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Estimated number of clusters: 3](https://scikit-learn.org/stable/_images/sphx_glr_plot_affinity_propagation_001.png)

**Total running time of the script:** (0 minutes 0.264 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_affinity_propagation.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_affinity_propagation.ipynb)

[`Download Jupyter notebook: plot_affinity_propagation.ipynb`](https://scikit-learn.org/stable/_downloads/91999ecc168932f9034d0cbc1cc248fa/plot_affinity_propagation.ipynb)

[`Download Python source code: plot_affinity_propagation.py`](https://scikit-learn.org/stable/_downloads/2f930acda654766f8ba0fee08887bb41/plot_affinity_propagation.py)

[`Download zipped: plot_affinity_propagation.zip`](https://scikit-learn.org/stable/_downloads/579bd5b3e1f615788637846e3011bb6f/plot_affinity_propagation.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dbscan_thumb.png)

[Demo of DBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html)

Demo of DBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mean_shift_thumb.png)

[A demo of the mean-shift clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html)

A demo of the mean-shift clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mini_batch_kmeans_thumb.png)

[Comparison of the K-Means and MiniBatchKMeans clustering algorithms](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html)

Comparison of the K-Means and MiniBatchKMeans clustering algorithms

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_plusplus_thumb.png)

[An example of K-Means++ initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_plusplus.html)

An example of K-Means++ initialization

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/2f930acda654766f8ba0fee08887bb41/plot_affinity_propagation.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/91999ecc168932f9034d0cbc1cc248fa/plot_affinity_propagation.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/579bd5b3e1f615788637846e3011bb6f/plot_affinity_propagation.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_affinity_propagation.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_affinity_propagation.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)