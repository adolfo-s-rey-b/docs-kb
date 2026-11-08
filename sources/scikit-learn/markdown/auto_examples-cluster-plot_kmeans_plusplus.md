[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_plusplus.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_kmeans_plusplus.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_plusplus.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_kmeans_plusplus.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_kmeans_plusplus.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_kmeans_plusplus.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_kmeans_plusplus.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_kmeans_plusplus.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_plusplus.html#sphx-glr-download-auto-examples-cluster-plot-kmeans-plusplus-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

An example of K-Means++ initialization[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_plusplus.html#an-example-of-k-means-initialization "Link to this heading")

=======================================================================================================================================================================================

An example to show the output of the [`sklearn.cluster.kmeans_plusplus`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.kmeans_plusplus.html#sklearn.cluster.kmeans_plusplus "sklearn.cluster.kmeans_plusplus")
 function for generating initial seeds for clustering.

K-Means++ is used as the default initialization for [K-means](https://scikit-learn.org/stable/modules/clustering.html#k-means)
.

![K-Means++ Initialization](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_plusplus_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt

from sklearn.cluster import [kmeans\_plusplus](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.kmeans_plusplus.html#sklearn.cluster.kmeans_plusplus "sklearn.cluster.kmeans_plusplus")
from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")

\# Generate sample data
n\_samples \= 4000
n\_components \= 4

X, y\_true \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(
    n\_samples\=n\_samples, centers\=n\_components, cluster\_std\=0.60, random\_state\=0
)
X \= X\[:, ::\-1\]

\# Calculate seeds from k-means++
centers\_init, indices \= [kmeans\_plusplus](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.kmeans_plusplus.html#sklearn.cluster.kmeans_plusplus "sklearn.cluster.kmeans_plusplus")
(X, n\_clusters\=4, random\_state\=0)

\# Plot init seeds along side sample data
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(1)
colors \= \["#4EACC5", "#FF9C34", "#4E9A06", "m"\]

for k, col in enumerate(colors):
    cluster\_data \= y\_true \== k
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[cluster\_data, 0\], X\[cluster\_data, 1\], c\=col, marker\=".", s\=10)

[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(centers\_init\[:, 0\], centers\_init\[:, 1\], c\="b", s\=50)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("K-Means++ Initialization")
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(\[\])
[plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(\[\])
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.045 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_kmeans_plusplus.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_kmeans_plusplus.ipynb)

[`Download Jupyter notebook: plot_kmeans_plusplus.ipynb`](https://scikit-learn.org/stable/_downloads/77b640d8771f7ecdeb2dbc948ebce90a/plot_kmeans_plusplus.ipynb)

[`Download Python source code: plot_kmeans_plusplus.py`](https://scikit-learn.org/stable/_downloads/fa03fd57e0f1a2cd66f3693283f7a6b3/plot_kmeans_plusplus.py)

[`Download zipped: plot_kmeans_plusplus.zip`](https://scikit-learn.org/stable/_downloads/2153fd2d9ab25873fb0a10316b24a9fe/plot_kmeans_plusplus.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bisect_kmeans_thumb.png)

[Bisecting K-Means and Regular K-Means Performance Comparison](https://scikit-learn.org/stable/auto_examples/cluster/plot_bisect_kmeans.html)

Bisecting K-Means and Regular K-Means Performance Comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_init_thumb.png)

[GMM Initialization Methods](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_init.html)

GMM Initialization Methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_digits_thumb.png)

[A demo of K-Means clustering on the handwritten digits data](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html)

A demo of K-Means clustering on the handwritten digits data

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mini_batch_kmeans_thumb.png)

[Comparison of the K-Means and MiniBatchKMeans clustering algorithms](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html)

Comparison of the K-Means and MiniBatchKMeans clustering algorithms

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/fa03fd57e0f1a2cd66f3693283f7a6b3/plot_kmeans_plusplus.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/77b640d8771f7ecdeb2dbc948ebce90a/plot_kmeans_plusplus.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/2153fd2d9ab25873fb0a10316b24a9fe/plot_kmeans_plusplus.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_kmeans_plusplus.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_kmeans_plusplus.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)