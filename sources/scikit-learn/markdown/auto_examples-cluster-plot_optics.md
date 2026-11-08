[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_optics.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_optics.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_optics.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_optics.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_optics.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_optics.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_optics.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_optics.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_optics.html#sphx-glr-download-auto-examples-cluster-plot-optics-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Demo of OPTICS clustering algorithm[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_optics.html#demo-of-optics-clustering-algorithm "Link to this heading")

==========================================================================================================================================================================

Finds core samples of high density and expands clusters from them. This example uses data that is generated so that the clusters have different densities.

The [`OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
 is first used with its Xi cluster detection method, and then setting specific thresholds on the reachability, which corresponds to [`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
. We can see that the different clusters of OPTICS’s Xi method can be recovered with different choices of thresholds in DBSCAN.

![Reachability Plot, Automatic Clustering OPTICS, Clustering at 0.5 epsilon cut DBSCAN, Clustering at 2.0 epsilon cut DBSCAN](https://scikit-learn.org/stable/_images/sphx_glr_plot_optics_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import [OPTICS](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
, [cluster\_optics\_dbscan](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_dbscan.html#sklearn.cluster.cluster_optics_dbscan "sklearn.cluster.cluster_optics_dbscan")

\# Generate sample data

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)
n\_points\_per\_cluster \= 250

C1 \= \[\-5, \-2\] + 0.8 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_points\_per\_cluster, 2)
C2 \= \[4, \-1\] + 0.1 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_points\_per\_cluster, 2)
C3 \= \[1, \-2\] + 0.2 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_points\_per\_cluster, 2)
C4 \= \[\-2, 3\] + 0.3 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_points\_per\_cluster, 2)
C5 \= \[3, \-2\] + 1.6 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_points\_per\_cluster, 2)
C6 \= \[5, 6\] + 2 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_points\_per\_cluster, 2)
X \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
((C1, C2, C3, C4, C5, C6))

clust \= [OPTICS](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")
(min\_samples\=50, xi\=0.05, min\_cluster\_size\=0.05)

\# Run the fit
clust.fit(X)

labels\_050 \= [cluster\_optics\_dbscan](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_dbscan.html#sklearn.cluster.cluster_optics_dbscan "sklearn.cluster.cluster_optics_dbscan")
(
    reachability\=clust.reachability\_,
    core\_distances\=clust.core\_distances\_,
    ordering\=clust.ordering\_,
    eps\=0.5,
)
labels\_200 \= [cluster\_optics\_dbscan](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_dbscan.html#sklearn.cluster.cluster_optics_dbscan "sklearn.cluster.cluster_optics_dbscan")
(
    reachability\=clust.reachability\_,
    core\_distances\=clust.core\_distances\_,
    ordering\=clust.ordering\_,
    eps\=2,
)

space \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(X))
reachability \= clust.reachability\_\[clust.ordering\_\]
labels \= clust.labels\_\[clust.ordering\_\]

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 7))
G \= [gridspec.GridSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
(2, 3)
ax1 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(G\[0, :\])
ax2 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(G\[1, 0\])
ax3 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(G\[1, 1\])
ax4 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(G\[1, 2\])

\# Reachability plot
colors \= \["g.", "r.", "b.", "y.", "c."\]
for klass, color in enumerate(colors):
    Xk \= space\[labels \== klass\]
    Rk \= reachability\[labels \== klass\]
    ax1.plot(Xk, Rk, color, alpha\=0.3)
ax1.plot(space\[labels \== \-1\], reachability\[labels \== \-1\], "k.", alpha\=0.3)
ax1.plot(space, [np.full\_like](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like "numpy.full_like")
(space, 2.0, dtype\=float), "k-", alpha\=0.5)
ax1.plot(space, [np.full\_like](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like "numpy.full_like")
(space, 0.5, dtype\=float), "k-.", alpha\=0.5)
ax1.set\_ylabel("Reachability (epsilon distance)")
ax1.set\_title("Reachability Plot")

\# OPTICS
colors \= \["g.", "r.", "b.", "y.", "c."\]
for klass, color in enumerate(colors):
    Xk \= X\[clust.labels\_ \== klass\]
    ax2.plot(Xk\[:, 0\], Xk\[:, 1\], color, alpha\=0.3)
ax2.plot(X\[clust.labels\_ \== \-1, 0\], X\[clust.labels\_ \== \-1, 1\], "k+", alpha\=0.1)
ax2.set\_title("Automatic Clustering\\nOPTICS")

\# DBSCAN at 0.5
colors \= \["g.", "r.", "b.", "c."\]
for klass, color in enumerate(colors):
    Xk \= X\[labels\_050 \== klass\]
    ax3.plot(Xk\[:, 0\], Xk\[:, 1\], color, alpha\=0.3)
ax3.plot(X\[labels\_050 \== \-1, 0\], X\[labels\_050 \== \-1, 1\], "k+", alpha\=0.1)
ax3.set\_title("Clustering at 0.5 epsilon cut\\nDBSCAN")

\# DBSCAN at 2.
colors \= \["g.", "m.", "y.", "c."\]
for klass, color in enumerate(colors):
    Xk \= X\[labels\_200 \== klass\]
    ax4.plot(Xk\[:, 0\], Xk\[:, 1\], color, alpha\=0.3)
ax4.plot(X\[labels\_200 \== \-1, 0\], X\[labels\_200 \== \-1, 1\], "k+", alpha\=0.1)
ax4.set\_title("Clustering at 2.0 epsilon cut\\nDBSCAN")

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 1.779 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_optics.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_optics.ipynb)

[`Download Jupyter notebook: plot_optics.ipynb`](https://scikit-learn.org/stable/_downloads/8025056f1d24411e898c2d0086371880/plot_optics.ipynb)

[`Download Python source code: plot_optics.py`](https://scikit-learn.org/stable/_downloads/fe139d44b92c775a3b44dcefd61ea1bb/plot_optics.py)

[`Download zipped: plot_optics.zip`](https://scikit-learn.org/stable/_downloads/47f00be4ac7158f9188c680e1a05ef7b/plot_optics.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_thumb.png)

[Demo of HDBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html)

Demo of HDBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_self_training_varying_threshold_thumb.png)

[Effect of varying threshold for self-training](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)

Effect of varying threshold for self-training

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dbscan_thumb.png)

[Demo of DBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html)

Demo of DBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_concentration_prior_thumb.png)

[Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture](https://scikit-learn.org/stable/auto_examples/mixture/plot_concentration_prior.html)

Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/fe139d44b92c775a3b44dcefd61ea1bb/plot_optics.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/8025056f1d24411e898c2d0086371880/plot_optics.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/47f00be4ac7158f9188c680e1a05ef7b/plot_optics.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_optics.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_optics.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)