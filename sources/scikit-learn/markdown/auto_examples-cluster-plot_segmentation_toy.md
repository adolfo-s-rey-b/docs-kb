[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_segmentation_toy.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_segmentation_toy.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_segmentation_toy.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_segmentation_toy.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_segmentation_toy.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_segmentation_toy.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_segmentation_toy.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_segmentation_toy.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_segmentation_toy.html#sphx-glr-download-auto-examples-cluster-plot-segmentation-toy-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Spectral clustering for image segmentation[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_segmentation_toy.html#spectral-clustering-for-image-segmentation "Link to this heading")

==================================================================================================================================================================================================

In this example, an image with connected circles is generated and spectral clustering is used to separate the circles.

In these settings, the [Spectral clustering](https://scikit-learn.org/stable/modules/clustering.html#spectral-clustering)
 approach solves the problem know as ‘normalized graph cuts’: the image is seen as a graph of connected voxels, and the spectral clustering algorithm amounts to choosing graph cuts defining regions while minimizing the ratio of the gradient along the cut, and the volume of the region.

As the algorithm tries to balance the volume (ie balance the region sizes), if we take circles with different sizes, the segmentation fails.

In addition, as there is no useful information in the intensity of the image, or its gradient, we choose to perform the spectral clustering on a graph that is only weakly informed by the gradient. This is close to performing a Voronoi partition of the graph.

In addition, we use the mask of the objects to restrict the graph to the outline of the objects. In this example, we are interested in separating the objects one from the other, and not from the background.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate the data[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_segmentation_toy.html#generate-the-data "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np

l \= 100
x, y \= [np.indices](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "numpy.indices")
((l, l))

center1 \= (28, 24)
center2 \= (40, 50)
center3 \= (67, 58)
center4 \= (24, 70)

radius1, radius2, radius3, radius4 \= 16, 14, 15, 14

circle1 \= (x \- center1\[0\]) \*\* 2 + (y \- center1\[1\]) \*\* 2 < radius1\*\*2
circle2 \= (x \- center2\[0\]) \*\* 2 + (y \- center2\[1\]) \*\* 2 < radius2\*\*2
circle3 \= (x \- center3\[0\]) \*\* 2 + (y \- center3\[1\]) \*\* 2 < radius3\*\*2
circle4 \= (x \- center4\[0\]) \*\* 2 + (y \- center4\[1\]) \*\* 2 < radius4\*\*2

Copy to clipboard

Plotting four circles[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_segmentation_toy.html#plotting-four-circles "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

img \= circle1 + circle2 + circle3 + circle4

\# We use a mask that limits to the foreground: the problem that we are
\# interested in here is not separating the objects from the background,
\# but separating them one from the other.
mask \= img.astype(bool)

img \= img.astype(float)
img += 1 + 0.2 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(\*img.shape)

Copy to clipboard

Convert the image into a graph with the value of the gradient on the edges.

from sklearn.feature\_extraction import image

graph \= image.img\_to\_graph(img, mask\=mask)

Copy to clipboard

Take a decreasing function of the gradient resulting in a segmentation that is close to a Voronoi partition

graph.data \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(\-graph.data / graph.data.std())

Copy to clipboard

Here we perform spectral clustering using the arpack solver since amg is numerically unstable on this example. We then plot the results.

import matplotlib.pyplot as plt

from sklearn.cluster import [spectral\_clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")

labels \= [spectral\_clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")
(graph, n\_clusters\=4, eigen\_solver\="arpack")
label\_im \= [np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
(mask.shape, \-1.0)
label\_im\[mask\] \= labels

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=2, figsize\=(10, 5))
axs\[0\].matshow(img)
axs\[1\].matshow(label\_im)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot segmentation toy](https://scikit-learn.org/stable/_images/sphx_glr_plot_segmentation_toy_001.png)

Plotting two circles[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_segmentation_toy.html#plotting-two-circles "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

Here we repeat the above process but only consider the first two circles we generated. Note that this results in a cleaner separation between the circles as the region sizes are easier to balance in this case.

img \= circle1 + circle2
mask \= img.astype(bool)
img \= img.astype(float)

img += 1 + 0.2 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(\*img.shape)

graph \= image.img\_to\_graph(img, mask\=mask)
graph.data \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(\-graph.data / graph.data.std())

labels \= [spectral\_clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")
(graph, n\_clusters\=2, eigen\_solver\="arpack")
label\_im \= [np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
(mask.shape, \-1.0)
label\_im\[mask\] \= labels

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=2, figsize\=(10, 5))
axs\[0\].matshow(img)
axs\[1\].matshow(label\_im)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot segmentation toy](https://scikit-learn.org/stable/_images/sphx_glr_plot_segmentation_toy_002.png)

**Total running time of the script:** (0 minutes 0.224 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_segmentation_toy.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_segmentation_toy.ipynb)

[`Download Jupyter notebook: plot_segmentation_toy.ipynb`](https://scikit-learn.org/stable/_downloads/e7311e6599ab6ff3129117a6d8c302ec/plot_segmentation_toy.ipynb)

[`Download Python source code: plot_segmentation_toy.py`](https://scikit-learn.org/stable/_downloads/9cdba5635a180cdcca7d23b9cf18ffac/plot_segmentation_toy.py)

[`Download zipped: plot_segmentation_toy.zip`](https://scikit-learn.org/stable/_downloads/53efb390bba6a1c7eadd27ed210a1830/plot_segmentation_toy.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_segmentation_thumb.png)

[Segmenting the picture of greek coins in regions](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_segmentation.html)

Segmenting the picture of greek coins in regions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tomography_l1_reconstruction_thumb.png)

[Compressive sensing: tomography reconstruction with L1 prior (Lasso)](https://scikit-learn.org/stable/auto_examples/applications/plot_tomography_l1_reconstruction.html)

Compressive sensing: tomography reconstruction with L1 prior (Lasso)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_caching_nearest_neighbors_thumb.png)

[Caching nearest neighbors](https://scikit-learn.org/stable/auto_examples/neighbors/plot_caching_nearest_neighbors.html)

Caching nearest neighbors

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_denoising_thumb.png)

[Image denoising using kernel PCA](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html)

Image denoising using kernel PCA

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/9cdba5635a180cdcca7d23b9cf18ffac/plot_segmentation_toy.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/e7311e6599ab6ff3129117a6d8c302ec/plot_segmentation_toy.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/53efb390bba6a1c7eadd27ed210a1830/plot_segmentation_toy.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_segmentation_toy.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_segmentation_toy.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)