[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_linkage.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_digits_linkage.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_linkage.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_digits_linkage.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_digits_linkage.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_digits_linkage.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_digits_linkage.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_digits_linkage.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_linkage.html#sphx-glr-download-auto-examples-cluster-plot-digits-linkage-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Various Agglomerative Clustering on a 2D embedding of digits[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_linkage.html#various-agglomerative-clustering-on-a-2d-embedding-of-digits "Link to this heading")

====================================================================================================================================================================================================================================

An illustration of various linkage option for agglomerative clustering on a 2D embedding of the digits dataset.

The goal of this example is to show intuitively how the metrics behave, and not to find good clusters for the digits. This is why the example works on a 2D embedding.

What this example shows us is the behavior “rich getting richer” of agglomerative clustering that tends to create uneven cluster sizes.

This behavior is pronounced for the average linkage strategy, that ends up with a couple of clusters with few datapoints.

The case of single linkage is even more pathologic with a very large cluster covering most digits, an intermediate size (clean) cluster with most zero digits and all other clusters being drawn from noise points around the fringes.

The other linkage strategies lead to more evenly distributed clusters that are therefore likely to be less sensible to a random resampling of the dataset.

*   ![ward linkage](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_linkage_001.png)
*   ![average linkage](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_linkage_002.png)
*   ![complete linkage](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_linkage_003.png)
*   ![single linkage](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_linkage_004.png)

Computing embedding
Done.
ward :  0.06s
average :       0.06s
complete :      0.06s
single :        0.02s

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

import numpy as np
from matplotlib import pyplot as plt

from sklearn import datasets, manifold

digits \= [datasets.load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
()
X, y \= digits.data, digits.target
n\_samples, n\_features \= X.shape

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)

\# ----------------------------------------------------------------------
\# Visualize the clustering
def plot\_clustering(X\_red, labels, title\=None):
    x\_min, x\_max \= [np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
(X\_red, axis\=0), [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(X\_red, axis\=0)
    X\_red \= (X\_red \- x\_min) / (x\_max \- x\_min)

    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(6, 4))
    for digit in digits.target\_names:
        [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
            \*X\_red\[y \== digit\].T,
            marker\=f"${digit}$",
            s\=50,
            c\=plt.cm.nipy\_spectral(labels\[y \== digit\] / 10),
            alpha\=0.5,
        )

    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(\[\])
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(\[\])
    if title is not None:
        [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(title, size\=17)
    [plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("off")
    [plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
(rect\=\[0, 0.03, 1, 0.95\])

\# ----------------------------------------------------------------------
\# 2D embedding of the digits dataset
print("Computing embedding")
X\_red \= [manifold.SpectralEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")
(n\_components\=2).fit\_transform(X)
print("Done.")

from sklearn.cluster import [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")

for linkage in ("ward", "average", "complete", "single"):
    clustering \= [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
(linkage\=linkage, n\_clusters\=10)
    t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    clustering.fit(X\_red)
    print("%s :\\t%.2fs" % (linkage, [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0))

    plot\_clustering(X\_red, clustering.labels\_, "%s linkage" % linkage)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 1.282 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_digits_linkage.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_digits_linkage.ipynb)

[`Download Jupyter notebook: plot_digits_linkage.ipynb`](https://scikit-learn.org/stable/_downloads/21ba44171c2107e5285a530bdf3dd0f6/plot_digits_linkage.ipynb)

[`Download Python source code: plot_digits_linkage.py`](https://scikit-learn.org/stable/_downloads/2b34fe5e4c2bfccb9b7dbff3e93ff741/plot_digits_linkage.py)

[`Download zipped: plot_digits_linkage.zip`](https://scikit-learn.org/stable/_downloads/a390b24658dd58aba65067ab405e1ee5/plot_digits_linkage.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linkage_comparison_thumb.png)

[Comparing different hierarchical linkage methods on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html)

Comparing different hierarchical linkage methods on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ward_structured_vs_unstructured_thumb.png)

[Hierarchical clustering with and without structure](https://scikit-learn.org/stable/auto_examples/cluster/plot_ward_structured_vs_unstructured.html)

Hierarchical clustering with and without structure

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stock_market_thumb.png)

[Visualizing the stock market structure](https://scikit-learn.org/stable/auto_examples/applications/plot_stock_market.html)

Visualizing the stock market structure

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/2b34fe5e4c2bfccb9b7dbff3e93ff741/plot_digits_linkage.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/21ba44171c2107e5285a530bdf3dd0f6/plot_digits_linkage.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/a390b24658dd58aba65067ab405e1ee5/plot_digits_linkage.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_digits_linkage.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_digits_linkage.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)