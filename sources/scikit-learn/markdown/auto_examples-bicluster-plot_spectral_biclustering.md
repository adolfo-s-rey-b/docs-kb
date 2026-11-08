[Skip to main content](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_biclustering.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/bicluster/plot_spectral_biclustering.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_biclustering.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/bicluster/plot_spectral_biclustering.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/bicluster/plot_spectral_biclustering.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/bicluster/plot_spectral_biclustering.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/bicluster/plot_spectral_biclustering.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/bicluster/plot_spectral_biclustering.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_biclustering.html#sphx-glr-download-auto-examples-bicluster-plot-spectral-biclustering-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

A demo of the Spectral Biclustering algorithm[#](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_biclustering.html#a-demo-of-the-spectral-biclustering-algorithm "Link to this heading")

===============================================================================================================================================================================================================

This example demonstrates how to generate a checkerboard dataset and bicluster it using the [`SpectralBiclustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering "sklearn.cluster.SpectralBiclustering")
 algorithm. The spectral biclustering algorithm is specifically designed to cluster data by simultaneously considering both the rows (samples) and columns (features) of a matrix. It aims to identify patterns not only between samples but also within subsets of samples, allowing for the detection of localized structure within the data. This makes spectral biclustering particularly well-suited for datasets where the order or arrangement of features is fixed, such as in images, time series, or genomes.

The data is generated, then shuffled and passed to the spectral biclustering algorithm. The rows and columns of the shuffled matrix are then rearranged to plot the biclusters found.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate sample data[#](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_biclustering.html#generate-sample-data "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

We generate the sample data using the [`make_checkerboard`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_checkerboard.html#sklearn.datasets.make_checkerboard "sklearn.datasets.make_checkerboard")
 function. Each pixel within `shape=(300, 300)` represents with its color a value from a uniform distribution. The noise is added from a normal distribution, where the value chosen for `noise` is the standard deviation.

As you can see, the data is distributed over 12 cluster cells and is relatively well distinguishable.

from matplotlib import pyplot as plt

from sklearn.datasets import [make\_checkerboard](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_checkerboard.html#sklearn.datasets.make_checkerboard "sklearn.datasets.make_checkerboard")

n\_clusters \= (4, 3)
data, rows, columns \= [make\_checkerboard](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_checkerboard.html#sklearn.datasets.make_checkerboard "sklearn.datasets.make_checkerboard")
(
    shape\=(300, 300), n\_clusters\=n\_clusters, noise\=10, shuffle\=False, random\_state\=42
)

[plt.matshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html#matplotlib.pyplot.matshow "matplotlib.pyplot.matshow")
(data, cmap\=plt.cm.Blues)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Original dataset")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Original dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_biclustering_001.png)

We shuffle the data and the goal is to reconstruct it afterwards using [`SpectralBiclustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering "sklearn.cluster.SpectralBiclustering")
.

import numpy as np

\# Creating lists of shuffled row and column indices
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
row\_idx\_shuffled \= rng.permutation(data.shape\[0\])
col\_idx\_shuffled \= rng.permutation(data.shape\[1\])

Copy to clipboard

We redefine the shuffled data and plot it. We observe that we lost the structure of original data matrix.

data \= data\[row\_idx\_shuffled\]\[:, col\_idx\_shuffled\]

[plt.matshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html#matplotlib.pyplot.matshow "matplotlib.pyplot.matshow")
(data, cmap\=plt.cm.Blues)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Shuffled dataset")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Shuffled dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_biclustering_002.png)

Fitting `SpectralBiclustering`[#](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_biclustering.html#fitting-spectralbiclustering "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We fit the model and compare the obtained clusters with the ground truth. Note that when creating the model we specify the same number of clusters that we used to create the dataset (`n_clusters = (4, 3)`), which will contribute to obtain a good result.

from sklearn.cluster import [SpectralBiclustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering "sklearn.cluster.SpectralBiclustering")
from sklearn.metrics import [consensus\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.consensus_score.html#sklearn.metrics.consensus_score "sklearn.metrics.consensus_score")

model \= [SpectralBiclustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering "sklearn.cluster.SpectralBiclustering")
(n\_clusters\=n\_clusters, method\="log", random\_state\=0)
model.fit(data)

\# Compute the similarity of two sets of biclusters
score \= [consensus\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.consensus_score.html#sklearn.metrics.consensus_score "sklearn.metrics.consensus_score")
(
    model.biclusters\_, (rows\[:, row\_idx\_shuffled\], columns\[:, col\_idx\_shuffled\])
)
print(f"consensus score: {score:.1f}")

Copy to clipboard

consensus score: 1.0

Copy to clipboard

The score is between 0 and 1, where 1 corresponds to a perfect matching. It shows the quality of the biclustering.

Plotting results[#](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_biclustering.html#plotting-results "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

Now, we rearrange the data based on the row and column labels assigned by the [`SpectralBiclustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering "sklearn.cluster.SpectralBiclustering")
 model in ascending order and plot again. The `row_labels_` range from 0 to 3, while the `column_labels_` range from 0 to 2, representing a total of 4 clusters per row and 3 clusters per column.

\# Reordering first the rows and then the columns.
reordered\_rows \= data\[[np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")\
(model.row\_labels\_)\]
reordered\_data \= reordered\_rows\[:, [np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")\
(model.column\_labels\_)\]

[plt.matshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html#matplotlib.pyplot.matshow "matplotlib.pyplot.matshow")
(reordered\_data, cmap\=plt.cm.Blues)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("After biclustering; rearranged to show biclusters")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![After biclustering; rearranged to show biclusters](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_biclustering_003.png)

As a last step, we want to demonstrate the relationships between the row and column labels assigned by the model. Therefore, we create a grid with [`numpy.outer`](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer "(in NumPy v2.5)")
, which takes the sorted `row_labels_` and `column_labels_` and adds 1 to each to ensure that the labels start from 1 instead of 0 for better visualization.

[plt.matshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html#matplotlib.pyplot.matshow "matplotlib.pyplot.matshow")
(
    [np.outer](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer "numpy.outer")
([np.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
(model.row\_labels\_) + 1, [np.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
(model.column\_labels\_) + 1),
    cmap\=plt.cm.Blues,
)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Checkerboard structure of rearranged data")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Checkerboard structure of rearranged data](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_biclustering_004.png)

The outer product of the row and column label vectors shows a representation of the checkerboard structure, where different combinations of row and column labels are represented by different shades of blue.

**Total running time of the script:** (0 minutes 0.446 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo1.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/bicluster/plot_spectral_biclustering.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo1.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/bicluster/plot_spectral_biclustering.ipynb)

[`Download Jupyter notebook: plot_spectral_biclustering.ipynb`](https://scikit-learn.org/stable/_downloads/6b00e458f3e282f1cc421f077b2fcad1/plot_spectral_biclustering.ipynb)

[`Download Python source code: plot_spectral_biclustering.py`](https://scikit-learn.org/stable/_downloads/ac19db97f4bbd077ccffef2736ed5f3d/plot_spectral_biclustering.py)

[`Download zipped: plot_spectral_biclustering.zip`](https://scikit-learn.org/stable/_downloads/f66c3a9f3631c05c52d31172371922ab/plot_spectral_biclustering.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_coclustering_thumb.png)

[A demo of the Spectral Co-Clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_coclustering.html)

A demo of the Spectral Co-Clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_silhouette_analysis_thumb.png)

[Selecting the number of clusters with silhouette analysis on KMeans clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)

Selecting the number of clusters with silhouette analysis on KMeans clustering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linkage_comparison_thumb.png)

[Comparing different hierarchical linkage methods on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html)

Comparing different hierarchical linkage methods on toy datasets

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/ac19db97f4bbd077ccffef2736ed5f3d/plot_spectral_biclustering.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/6b00e458f3e282f1cc421f077b2fcad1/plot_spectral_biclustering.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/f66c3a9f3631c05c52d31172371922ab/plot_spectral_biclustering.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo1.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/bicluster/plot_spectral_biclustering.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo1.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/bicluster/plot_spectral_biclustering.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)