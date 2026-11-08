[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_embedding.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_random_forest_embedding.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_embedding.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_random_forest_embedding.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_random_forest_embedding.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_random_forest_embedding.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_random_forest_embedding.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_random_forest_embedding.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_embedding.html#sphx-glr-download-auto-examples-ensemble-plot-random-forest-embedding-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Hashing feature transformation using Totally Random Trees[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_embedding.html#hashing-feature-transformation-using-totally-random-trees "Link to this heading")

========================================================================================================================================================================================================================================

RandomTreesEmbedding provides a way to map data to a very high-dimensional, sparse representation, which might be beneficial for classification. The mapping is completely unsupervised and very efficient.

This example visualizes the partitions given by several trees and shows how the transformation can also be used for non-linear dimensionality reduction or non-linear classification.

Points that are neighboring often share the same leaf of a tree and therefore share large parts of their hashed representation. This allows to separate two concentric circles simply based on the principal components of the transformed data with truncated SVD.

In high-dimensional spaces, linear classifiers often achieve excellent accuracy. For sparse binary data, BernoulliNB is particularly well-suited. The bottom row compares the decision boundary obtained by BernoulliNB in the transformed space with an ExtraTreesClassifier forests learned on the original data.

![Original Data (2d), Truncated SVD reduction (2d) of transformed data (74d), Naive Bayes on Transformed data, ExtraTrees predictions](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_forest_embedding_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [make\_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
from sklearn.decomposition import [TruncatedSVD](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
from sklearn.ensemble import [ExtraTreesClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
, [RandomTreesEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")
from sklearn.naive\_bayes import [BernoulliNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")

\# make a synthetic dataset
X, y \= [make\_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
(factor\=0.5, random\_state\=0, noise\=0.05)

\# use RandomTreesEmbedding to transform data
hasher \= [RandomTreesEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")
(n\_estimators\=10, random\_state\=0, max\_depth\=3)
X\_transformed \= hasher.fit\_transform(X)

\# Visualize result after dimensionality reduction using truncated SVD
svd \= [TruncatedSVD](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")
(n\_components\=2)
X\_reduced \= svd.fit\_transform(X\_transformed)

\# Learn a Naive Bayes classifier on the transformed data
nb \= [BernoulliNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
()
nb.fit(X\_transformed, y)

\# Learn an ExtraTreesClassifier for comparison
trees \= [ExtraTreesClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
(max\_depth\=3, n\_estimators\=10, random\_state\=0)
trees.fit(X, y)

\# scatter plot of original and reduced data
fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(9, 8))

ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(221)
ax.scatter(X\[:, 0\], X\[:, 1\], c\=y, s\=50, edgecolor\="k")
ax.set\_title("Original Data (2d)")
ax.set\_xticks(())
ax.set\_yticks(())

ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(222)
ax.scatter(X\_reduced\[:, 0\], X\_reduced\[:, 1\], c\=y, s\=50, edgecolor\="k")
ax.set\_title(
    "Truncated SVD reduction (2d) of transformed data (%dd)" % X\_transformed.shape\[1\]
)
ax.set\_xticks(())
ax.set\_yticks(())

\# Plot the decision in original space. For that, we will assign a color
\# to each point in the mesh \[x\_min, x\_max\]x\[y\_min, y\_max\].
h \= 0.01
x\_min, x\_max \= X\[:, 0\].min() \- 0.5, X\[:, 0\].max() + 0.5
y\_min, y\_max \= X\[:, 1\].min() \- 0.5, X\[:, 1\].max() + 0.5
xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(x\_min, x\_max, h), [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(y\_min, y\_max, h))

\# transform grid using RandomTreesEmbedding
transformed\_grid \= hasher.transform([np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[xx.ravel(), yy.ravel()\])
y\_grid\_pred \= nb.predict\_proba(transformed\_grid)\[:, 1\]

ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(223)
ax.set\_title("Naive Bayes on Transformed data")
ax.pcolormesh(xx, yy, y\_grid\_pred.reshape(xx.shape))
ax.scatter(X\[:, 0\], X\[:, 1\], c\=y, s\=50, edgecolor\="k")
ax.set\_ylim(\-1.4, 1.4)
ax.set\_xlim(\-1.4, 1.4)
ax.set\_xticks(())
ax.set\_yticks(())

\# transform grid using ExtraTreesClassifier
y\_grid\_pred \= trees.predict\_proba([np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[xx.ravel(), yy.ravel()\])\[:, 1\]

ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(224)
ax.set\_title("ExtraTrees predictions")
ax.pcolormesh(xx, yy, y\_grid\_pred.reshape(xx.shape))
ax.scatter(X\[:, 0\], X\[:, 1\], c\=y, s\=50, edgecolor\="k")
ax.set\_ylim(\-1.4, 1.4)
ax.set\_xlim(\-1.4, 1.4)
ax.set\_xticks(())
ax.set\_yticks(())

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.412 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_random_forest_embedding.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_random_forest_embedding.ipynb)

[`Download Jupyter notebook: plot_random_forest_embedding.ipynb`](https://scikit-learn.org/stable/_downloads/b22a06b90f4e4dff100e395092c650be/plot_random_forest_embedding.ipynb)

[`Download Python source code: plot_random_forest_embedding.py`](https://scikit-learn.org/stable/_downloads/58eb7f19c96d77148277d974aa5c112e/plot_random_forest_embedding.py)

[`Download zipped: plot_random_forest_embedding.zip`](https://scikit-learn.org/stable/_downloads/37d005a18100ae3c52b798da37735337/plot_random_forest_embedding.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_thumb.png)

[Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)

Varying regularization in Multi-layer Perceptron

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_iris_thumb.png)

[Gaussian process classification (GPC) on iris dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html)

Gaussian process classification (GPC) on iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_classification_thumb.png)

[Feature discretization](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_classification.html)

Feature discretization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_strategies_thumb.png)

[Demonstrating the different strategies of KBinsDiscretizer](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_strategies.html)

Demonstrating the different strategies of KBinsDiscretizer

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/58eb7f19c96d77148277d974aa5c112e/plot_random_forest_embedding.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/b22a06b90f4e4dff100e395092c650be/plot_random_forest_embedding.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/37d005a18100ae3c52b798da37735337/plot_random_forest_embedding.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_random_forest_embedding.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_random_forest_embedding.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)