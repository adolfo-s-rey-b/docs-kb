[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_dendrogram.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_agglomerative_dendrogram.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_dendrogram.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_agglomerative_dendrogram.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_agglomerative_dendrogram.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_agglomerative_dendrogram.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_agglomerative_dendrogram.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_agglomerative_dendrogram.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_dendrogram.html#sphx-glr-download-auto-examples-cluster-plot-agglomerative-dendrogram-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Plot Hierarchical Clustering Dendrogram[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_dendrogram.html#plot-hierarchical-clustering-dendrogram "Link to this heading")

====================================================================================================================================================================================================

This example plots the corresponding dendrogram of a hierarchical clustering using AgglomerativeClustering and the dendrogram method available in scipy.

![Hierarchical Clustering Dendrogram](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_dendrogram_001.png)

import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import [dendrogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html#scipy.cluster.hierarchy.dendrogram "scipy.cluster.hierarchy.dendrogram")

from sklearn.cluster import [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")

def plot\_dendrogram(model, \*\*kwargs):
    \# Create linkage matrix and then plot the dendrogram

    \# create the counts of samples under each node
    counts \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(model.children\_.shape\[0\])
    n\_samples \= len(model.labels\_)
    for i, merge in enumerate(model.children\_):
        current\_count \= 0
        for child\_idx in merge:
            if child\_idx < n\_samples:
                current\_count += 1  \# leaf node
            else:
                current\_count += counts\[child\_idx \- n\_samples\]
        counts\[i\] \= current\_count

    linkage\_matrix \= [np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(
        \[model.children\_, model.distances\_, counts\]
    ).astype(float)

    \# Plot the corresponding dendrogram
    [dendrogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html#scipy.cluster.hierarchy.dendrogram "scipy.cluster.hierarchy.dendrogram")
(linkage\_matrix, \*\*kwargs)

iris \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X \= iris.data

\# setting distance\_threshold=0 ensures we compute the full tree.
model \= [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
(distance\_threshold\=0, n\_clusters\=None)

model \= model.fit(X)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Hierarchical Clustering Dendrogram")
\# plot the top three levels of the dendrogram
plot\_dendrogram(model, truncate\_mode\="level", p\=3)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Number of points in node (or index of point if no parenthesis).")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.106 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_agglomerative_dendrogram.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_agglomerative_dendrogram.ipynb)

[`Download Jupyter notebook: plot_agglomerative_dendrogram.ipynb`](https://scikit-learn.org/stable/_downloads/72d877fe6a0a97bfa8950a086a14a445/plot_agglomerative_dendrogram.ipynb)

[`Download Python source code: plot_agglomerative_dendrogram.py`](https://scikit-learn.org/stable/_downloads/4cb9ca0dda94124c7cb99dcaae983dab/plot_agglomerative_dendrogram.py)

[`Download zipped: plot_agglomerative_dendrogram.zip`](https://scikit-learn.org/stable/_downloads/6f4d2fbb0386afc6ddc42f47a6c85a7c/plot_agglomerative_dendrogram.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_unveil_tree_structure_thumb.png)

[Understanding the decision tree structure](https://scikit-learn.org/stable/auto_examples/tree/plot_unveil_tree_structure.html)

Understanding the decision tree structure

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_ward_segmentation_thumb.png)

[A demo of structured Ward hierarchical clustering on an image of coins](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html)

A demo of structured Ward hierarchical clustering on an image of coins

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linkage_comparison_thumb.png)

[Comparing different hierarchical linkage methods on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html)

Comparing different hierarchical linkage methods on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ward_structured_vs_unstructured_thumb.png)

[Hierarchical clustering with and without structure](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)

Hierarchical clustering with and without structure

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/4cb9ca0dda94124c7cb99dcaae983dab/plot_agglomerative_dendrogram.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/72d877fe6a0a97bfa8950a086a14a445/plot_agglomerative_dendrogram.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/6f4d2fbb0386afc6ddc42f47a6c85a7c/plot_agglomerative_dendrogram.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_agglomerative_dendrogram.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_agglomerative_dendrogram.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)