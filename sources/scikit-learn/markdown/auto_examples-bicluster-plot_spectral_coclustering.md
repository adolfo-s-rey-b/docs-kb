[Skip to main content](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_coclustering.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/bicluster/plot_spectral_coclustering.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_coclustering.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/bicluster/plot_spectral_coclustering.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/bicluster/plot_spectral_coclustering.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/bicluster/plot_spectral_coclustering.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/bicluster/plot_spectral_coclustering.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/bicluster/plot_spectral_coclustering.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_coclustering.html#sphx-glr-download-auto-examples-bicluster-plot-spectral-coclustering-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

A demo of the Spectral Co-Clustering algorithm[#](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_coclustering.html#a-demo-of-the-spectral-co-clustering-algorithm "Link to this heading")

=================================================================================================================================================================================================================

This example demonstrates how to generate a dataset and bicluster it using the Spectral Co-Clustering algorithm.

The dataset is generated using the `make_biclusters` function, which creates a matrix of small values and implants bicluster with large values. The rows and columns are then shuffled and passed to the Spectral Co-Clustering algorithm. Rearranging the shuffled matrix to make biclusters contiguous shows how accurately the algorithm found the biclusters.

*   ![Original dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_coclustering_001.png)
*   ![Shuffled dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_coclustering_002.png)
*   ![After biclustering; rearranged to show biclusters](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_coclustering_003.png)

consensus score: 1.000

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import numpy as np
from matplotlib import pyplot as plt

from sklearn.cluster import [SpectralCoclustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering "sklearn.cluster.SpectralCoclustering")
from sklearn.datasets import [make\_biclusters](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_biclusters.html#sklearn.datasets.make_biclusters "sklearn.datasets.make_biclusters")
from sklearn.metrics import [consensus\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.consensus_score.html#sklearn.metrics.consensus_score "sklearn.metrics.consensus_score")

data, rows, columns \= [make\_biclusters](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_biclusters.html#sklearn.datasets.make_biclusters "sklearn.datasets.make_biclusters")
(
    shape\=(300, 300), n\_clusters\=5, noise\=5, shuffle\=False, random\_state\=0
)

[plt.matshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html#matplotlib.pyplot.matshow "matplotlib.pyplot.matshow")
(data, cmap\=plt.cm.Blues)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Original dataset")

\# shuffle clusters
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
row\_idx \= rng.permutation(data.shape\[0\])
col\_idx \= rng.permutation(data.shape\[1\])
data \= data\[row\_idx\]\[:, col\_idx\]

[plt.matshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html#matplotlib.pyplot.matshow "matplotlib.pyplot.matshow")
(data, cmap\=plt.cm.Blues)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Shuffled dataset")

model \= [SpectralCoclustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering "sklearn.cluster.SpectralCoclustering")
(n\_clusters\=5, random\_state\=0)
model.fit(data)
score \= [consensus\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.consensus_score.html#sklearn.metrics.consensus_score "sklearn.metrics.consensus_score")
(model.biclusters\_, (rows\[:, row\_idx\], columns\[:, col\_idx\]))

print("consensus score: {:.3f}".format(score))

fit\_data \= data\[[np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")\
(model.row\_labels\_)\]
fit\_data \= fit\_data\[:, [np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")\
(model.column\_labels\_)\]

[plt.matshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html#matplotlib.pyplot.matshow "matplotlib.pyplot.matshow")
(fit\_data, cmap\=plt.cm.Blues)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("After biclustering; rearranged to show biclusters")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.274 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo1.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/bicluster/plot_spectral_coclustering.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo1.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/bicluster/plot_spectral_coclustering.ipynb)

[`Download Jupyter notebook: plot_spectral_coclustering.ipynb`](https://scikit-learn.org/stable/_downloads/ee8e74bb66ae2967f890e19f28090b37/plot_spectral_coclustering.ipynb)

[`Download Python source code: plot_spectral_coclustering.py`](https://scikit-learn.org/stable/_downloads/bc8849a7cb8ea7a8dc7237431b95a1cc/plot_spectral_coclustering.py)

[`Download zipped: plot_spectral_coclustering.zip`](https://scikit-learn.org/stable/_downloads/3019a99f3f124514f9a0650bcb33fa27/plot_spectral_coclustering.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_biclustering_thumb.png)

[A demo of the Spectral Biclustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_biclustering.html)

A demo of the Spectral Biclustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bicluster_newsgroups_thumb.png)

[Biclustering documents with the Spectral Co-clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_bicluster_newsgroups.html)

Biclustering documents with the Spectral Co-clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_segmentation_thumb.png)

[Segmenting the picture of greek coins in regions](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_segmentation.html)

Segmenting the picture of greek coins in regions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_ward_segmentation_thumb.png)

[A demo of structured Ward hierarchical clustering on an image of coins](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html)

A demo of structured Ward hierarchical clustering on an image of coins

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/bc8849a7cb8ea7a8dc7237431b95a1cc/plot_spectral_coclustering.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/ee8e74bb66ae2967f890e19f28090b37/plot_spectral_coclustering.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/3019a99f3f124514f9a0650bcb33fa27/plot_spectral_coclustering.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo1.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/bicluster/plot_spectral_coclustering.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo1.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/bicluster/plot_spectral_coclustering.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)