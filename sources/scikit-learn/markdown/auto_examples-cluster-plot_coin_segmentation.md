[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_segmentation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_coin_segmentation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_segmentation.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_coin_segmentation.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_coin_segmentation.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_coin_segmentation.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_coin_segmentation.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_coin_segmentation.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_segmentation.html#sphx-glr-download-auto-examples-cluster-plot-coin-segmentation-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Segmenting the picture of greek coins in regions[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_segmentation.html#segmenting-the-picture-of-greek-coins-in-regions "Link to this heading")

===============================================================================================================================================================================================================

This example uses [Spectral clustering](https://scikit-learn.org/stable/modules/clustering.html#spectral-clustering)
 on a graph created from voxel-to-voxel difference on an image to break this image into multiple partly-homogeneous regions.

This procedure (spectral clustering on an image) is an efficient approximate solution for finding normalized graph cuts.

There are three options to assign labels:

*   ‘kmeans’ spectral clustering clusters samples in the embedding space using a kmeans algorithm
    
*   ‘discrete’ iteratively searches for the closest partition space to the embedding space of spectral clustering.
    
*   ‘cluster\_qr’ assigns labels using the QR factorization with pivoting that directly determines the partition in the embedding space.
    

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import time

import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import [gaussian\_filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html#scipy.ndimage.gaussian_filter "scipy.ndimage.gaussian_filter")
from skimage.data import coins
from skimage.transform import rescale

from sklearn.cluster import [spectral\_clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")
from sklearn.feature\_extraction import image

\# load the coins as a numpy array
orig\_coins \= coins()

\# Resize it to 20% of the original size to speed up the processing
\# Applying a Gaussian filter for smoothing prior to down-scaling
\# reduces aliasing artifacts.
smoothened\_coins \= [gaussian\_filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html#scipy.ndimage.gaussian_filter "scipy.ndimage.gaussian_filter")
(orig\_coins, sigma\=2)
rescaled\_coins \= rescale(smoothened\_coins, 0.2, mode\="reflect", anti\_aliasing\=False)

\# Convert the image into a graph with the value of the gradient on the
\# edges.
graph \= image.img\_to\_graph(rescaled\_coins)

\# Take a decreasing function of the gradient: an exponential
\# The smaller beta is, the more independent the segmentation is of the
\# actual image. For beta=1, the segmentation is close to a voronoi
beta \= 10
eps \= 1e-6
graph.data \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(\-beta \* graph.data / graph.data.std()) + eps

\# The number of segmented regions to display needs to be chosen manually.
\# The current version of 'spectral\_clustering' does not support determining
\# the number of good quality clusters automatically.
n\_regions \= 26

Copy to clipboard

Compute and visualize the resulting regions

\# Computing a few extra eigenvectors may speed up the eigen\_solver.
\# The spectral clustering quality may also benefit from requesting
\# extra regions for segmentation.
n\_regions\_plus \= 3

\# Apply spectral clustering using the default eigen\_solver='arpack'.
\# Any implemented solver can be used: eigen\_solver='arpack', 'lobpcg', or 'amg'.
\# Choosing eigen\_solver='amg' requires an extra package called 'pyamg'.
\# The quality of segmentation and the speed of calculations is mostly determined
\# by the choice of the solver and the value of the tolerance 'eigen\_tol'.
\# TODO: varying eigen\_tol seems to have no effect for 'lobpcg' and 'amg' #21243.
for assign\_labels in ("kmeans", "discretize", "cluster\_qr"):
    t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    labels \= [spectral\_clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")
(
        graph,
        n\_clusters\=(n\_regions + n\_regions\_plus),
        eigen\_tol\=1e-7,
        assign\_labels\=assign\_labels,
        random\_state\=42,
    )

    t1 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    labels \= labels.reshape(rescaled\_coins.shape)
    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5, 5))
    [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(rescaled\_coins, cmap\=plt.cm.gray)

    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
    title \= "Spectral clustering: %s, %.2fs" % (assign\_labels, (t1 \- t0))
    print(title)
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(title)
    for l in range(n\_regions):
        colors \= \[plt.cm.nipy\_spectral((l + 4) / float(n\_regions + 4))\]
        [plt.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
(labels \== l, colors\=colors)
        \# To view individual segments as appear comment in plt.pause(0.5)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

\# TODO: After #21194 is merged and #21243 is fixed, check which eigen\_solver
\# is the best and set eigen\_solver='arpack', 'lobpcg', or 'amg' and eigen\_tol
\# explicitly in this example.

Copy to clipboard

*   ![Spectral clustering: kmeans, 0.19s](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_segmentation_001.png)
*   ![Spectral clustering: discretize, 0.08s](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_segmentation_002.png)
*   ![Spectral clustering: cluster_qr, 0.07s](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_segmentation_003.png)

Spectral clustering: kmeans, 0.19s
Spectral clustering: discretize, 0.08s
Spectral clustering: cluster\_qr, 0.07s

Copy to clipboard

**Total running time of the script:** (0 minutes 0.708 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_coin_segmentation.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_coin_segmentation.ipynb)

[`Download Jupyter notebook: plot_coin_segmentation.ipynb`](https://scikit-learn.org/stable/_downloads/006fc185672e58b056a5c134db26935c/plot_coin_segmentation.ipynb)

[`Download Python source code: plot_coin_segmentation.py`](https://scikit-learn.org/stable/_downloads/2e86a4838807f09bbbb529d9643d45ab/plot_coin_segmentation.py)

[`Download zipped: plot_coin_segmentation.zip`](https://scikit-learn.org/stable/_downloads/b12810e5af9bfe7f99d2564c84262560/plot_coin_segmentation.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_segmentation_toy_thumb.png)

[Spectral clustering for image segmentation](https://scikit-learn.org/stable/auto_examples/cluster/plot_segmentation_toy.html)

Spectral clustering for image segmentation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_ward_segmentation_thumb.png)

[A demo of structured Ward hierarchical clustering on an image of coins](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html)

A demo of structured Ward hierarchical clustering on an image of coins

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stock_market_thumb.png)

[Visualizing the stock market structure](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html)

Visualizing the stock market structure

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_image_denoising_thumb.png)

[Image denoising using dictionary learning](https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html)

Image denoising using dictionary learning

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/2e86a4838807f09bbbb529d9643d45ab/plot_coin_segmentation.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/006fc185672e58b056a5c134db26935c/plot_coin_segmentation.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/b12810e5af9bfe7f99d2564c84262560/plot_coin_segmentation.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_coin_segmentation.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_coin_segmentation.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)