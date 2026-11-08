[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_coin_ward_segmentation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_coin_ward_segmentation.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_coin_ward_segmentation.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_coin_ward_segmentation.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_coin_ward_segmentation.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_coin_ward_segmentation.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html#sphx-glr-download-auto-examples-cluster-plot-coin-ward-segmentation-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

A demo of structured Ward hierarchical clustering on an image of coins[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html#a-demo-of-structured-ward-hierarchical-clustering-on-an-image-of-coins "Link to this heading")

================================================================================================================================================================================================================================================================

Compute the segmentation of a 2D image with Ward hierarchical clustering. The clustering is spatially constrained in order for each segmented region to be in one piece.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate data[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html#generate-data "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

from skimage.data import coins

orig\_coins \= coins()

Copy to clipboard

Resize it to 20% of the original size to speed up the processing Applying a Gaussian filter for smoothing prior to down-scaling reduces aliasing artifacts.

import numpy as np
from scipy.ndimage import [gaussian\_filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html#scipy.ndimage.gaussian_filter "scipy.ndimage.gaussian_filter")
from skimage.transform import rescale

smoothened\_coins \= [gaussian\_filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html#scipy.ndimage.gaussian_filter "scipy.ndimage.gaussian_filter")
(orig\_coins, sigma\=2)
rescaled\_coins \= rescale(
    smoothened\_coins,
    0.2,
    mode\="reflect",
    anti\_aliasing\=False,
)

X \= [np.reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")
(rescaled\_coins, (\-1, 1))

Copy to clipboard

Define structure of the data[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html#define-structure-of-the-data "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Pixels are connected to their neighbors.

from sklearn.feature\_extraction.image import grid\_to\_graph

connectivity \= grid\_to\_graph(\*rescaled\_coins.shape)

Copy to clipboard

Compute clustering[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html#compute-clustering "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

import time as time

from sklearn.cluster import [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")

print("Compute structured hierarchical clustering...")
st \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
n\_clusters \= 27  \# number of regions
ward \= [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
(
    n\_clusters\=n\_clusters, linkage\="ward", connectivity\=connectivity
)
ward.fit(X)
label \= [np.reshape](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")
(ward.labels\_, rescaled\_coins.shape)
print(f"Elapsed time: {[time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- st:.3f}s")
print(f"Number of pixels: {label.size}")
print(f"Number of clusters: {[np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(label).size}")

Copy to clipboard

Compute structured hierarchical clustering...
Elapsed time: 0.189s
Number of pixels: 4697
Number of clusters: 27

Copy to clipboard

Plot the results on an image[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html#plot-the-results-on-an-image "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Agglomerative clustering is able to segment each coin however, we have had to use a `n_cluster` larger than the number of coins because the segmentation is finding a large in the background.

import matplotlib.pyplot as plt

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5, 5))
[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(rescaled\_coins, cmap\=plt.cm.gray)
for l in range(n\_clusters):
    [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(
        label \== l,
        colors\=\[\
            plt.cm.nipy\_spectral(l / float(n\_clusters)),\
        \],
    )
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("off")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot coin ward segmentation](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_ward_segmentation_001.png)

**Total running time of the script:** (0 minutes 0.353 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_coin_ward_segmentation.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_coin_ward_segmentation.ipynb)

[`Download Jupyter notebook: plot_coin_ward_segmentation.ipynb`](https://scikit-learn.org/stable/_downloads/c8c7c5458b84586cacd8498015126bc4/plot_coin_ward_segmentation.ipynb)

[`Download Python source code: plot_coin_ward_segmentation.py`](https://scikit-learn.org/stable/_downloads/5eeecece5c41d6edcf4555b5e7c34350/plot_coin_ward_segmentation.py)

[`Download zipped: plot_coin_ward_segmentation.zip`](https://scikit-learn.org/stable/_downloads/1969c243dbe2c542ebd3887f2ecde211/plot_coin_ward_segmentation.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ward_structured_vs_unstructured_thumb.png)

[Hierarchical clustering with and without structure](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)

Hierarchical clustering with and without structure

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linkage_comparison_thumb.png)

[Comparing different hierarchical linkage methods on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html)

Comparing different hierarchical linkage methods on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_agglomerative_clustering_metrics_thumb.png)

[Agglomerative clustering with different metrics](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_clustering_metrics.html)

Agglomerative clustering with different metrics

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/5eeecece5c41d6edcf4555b5e7c34350/plot_coin_ward_segmentation.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c8c7c5458b84586cacd8498015126bc4/plot_coin_ward_segmentation.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/1969c243dbe2c542ebd3887f2ecde211/plot_coin_ward_segmentation.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_coin_ward_segmentation.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_coin_ward_segmentation.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)