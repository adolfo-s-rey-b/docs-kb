[Skip to main content](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_illustration.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neighbors/plot_nca_illustration.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_illustration.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neighbors/plot_nca_illustration.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neighbors/plot_nca_illustration.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neighbors/plot_nca_illustration.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neighbors/plot_nca_illustration.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neighbors/plot_nca_illustration.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_illustration.html#sphx-glr-download-auto-examples-neighbors-plot-nca-illustration-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Neighborhood Components Analysis Illustration[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_illustration.html#neighborhood-components-analysis-illustration "Link to this heading")

==========================================================================================================================================================================================================

This example illustrates a learned distance metric that maximizes the nearest neighbors classification accuracy. It provides a visual representation of this metric compared to the original point space. Please refer to the [User Guide](https://scikit-learn.org/stable/modules/neighbors.html#nca)
 for more information.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from scipy.special import [logsumexp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.logsumexp.html#scipy.special.logsumexp "scipy.special.logsumexp")

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.neighbors import [NeighborhoodComponentsAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis")

Copy to clipboard

Original points[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_illustration.html#original-points "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

First we create a data set of 9 samples from 3 classes, and plot the points in the original space. For this example, we focus on the classification of point no. 3. The thickness of a link between point no. 3 and another point is proportional to their distance.

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(
    n\_samples\=9,
    n\_features\=2,
    n\_informative\=2,
    n\_redundant\=0,
    n\_classes\=3,
    n\_clusters\_per\_class\=1,
    class\_sep\=1.0,
    random\_state\=0,
)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(1)
ax \= [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()
for i in range(X.shape\[0\]):
    ax.text(X\[i, 0\], X\[i, 1\], str(i), va\="center", ha\="center")
    ax.scatter(X\[i, 0\], X\[i, 1\], s\=300, c\=cm.Set1(y\[\[i\]\]), alpha\=0.4)

ax.set\_title("Original points")
ax.axes.get\_xaxis().set\_visible(False)
ax.axes.get\_yaxis().set\_visible(False)
ax.axis("equal")  \# so that boundaries are displayed correctly as circles

def link\_thickness\_i(X, i):
    diff\_embedded \= X\[i\] \- X
    dist\_embedded \= [np.einsum](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")
("ij,ij->i", diff\_embedded, diff\_embedded)
    dist\_embedded\[i\] \= [np.inf](https://numpy.org/doc/stable/reference/constants.html#numpy.inf "numpy.inf")

    \# compute exponentiated distances (use the log-sum-exp trick to
    \# avoid numerical instabilities
    exp\_dist\_embedded \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(\-dist\_embedded \- [logsumexp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.logsumexp.html#scipy.special.logsumexp "scipy.special.logsumexp")
(\-dist\_embedded))
    return exp\_dist\_embedded

def relate\_point(X, i, ax):
    pt\_i \= X\[i\]
    for j, pt\_j in enumerate(X):
        thickness \= link\_thickness\_i(X, i)
        if i != j:
            line \= (\[pt\_i\[0\], pt\_j\[0\]\], \[pt\_i\[1\], pt\_j\[1\]\])
            ax.plot(\*line, c\=cm.Set1(y\[j\]), linewidth\=5 \* thickness\[j\])

i \= 3
relate\_point(X, i, ax)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Original points](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_illustration_001.png)

Learning an embedding[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_illustration.html#learning-an-embedding "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

We use [`NeighborhoodComponentsAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis")
 to learn an embedding and plot the points after the transformation. We then take the embedding and find the nearest neighbors.

nca \= [NeighborhoodComponentsAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis")
(max\_iter\=30, random\_state\=0)
nca \= nca.fit(X, y)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(2)
ax2 \= [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()
X\_embedded \= nca.transform(X)
relate\_point(X\_embedded, i, ax2)

for i in range(len(X)):
    ax2.text(X\_embedded\[i, 0\], X\_embedded\[i, 1\], str(i), va\="center", ha\="center")
    ax2.scatter(X\_embedded\[i, 0\], X\_embedded\[i, 1\], s\=300, c\=cm.Set1(y\[\[i\]\]), alpha\=0.4)

ax2.set\_title("NCA embedding")
ax2.axes.get\_xaxis().set\_visible(False)
ax2.axes.get\_yaxis().set\_visible(False)
ax2.axis("equal")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![NCA embedding](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_illustration_002.png)

**Total running time of the script:** (0 minutes 0.107 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_nca_illustration.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_nca_illustration.ipynb)

[`Download Jupyter notebook: plot_nca_illustration.ipynb`](https://scikit-learn.org/stable/_downloads/19e9c0cb24a132133cef3b311caaf199/plot_nca_illustration.ipynb)

[`Download Python source code: plot_nca_illustration.py`](https://scikit-learn.org/stable/_downloads/3c0067f1f85f236ccc8a25c1245347e8/plot_nca_illustration.py)

[`Download zipped: plot_nca_illustration.zip`](https://scikit-learn.org/stable/_downloads/0a3f5445678ab43e77a0d7602ce7e53a/plot_nca_illustration.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_classification_thumb.png)

[Comparing Nearest Neighbors with and without Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html)

Comparing Nearest Neighbors with and without Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_dim_reduction_thumb.png)

[Dimensionality Reduction with Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_dim_reduction.html)

Dimensionality Reduction with Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lle_digits_thumb.png)

[Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html)

Manifold learning on handwritten digits: Locally Linear Embedding, Isomap...

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_concentration_prior_thumb.png)

[Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture](https://scikit-learn.org/stable/auto_examples/mixture/plot_concentration_prior.html)

Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/3c0067f1f85f236ccc8a25c1245347e8/plot_nca_illustration.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/19e9c0cb24a132133cef3b311caaf199/plot_nca_illustration.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/0a3f5445678ab43e77a0d7602ce7e53a/plot_nca_illustration.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_nca_illustration.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_nca_illustration.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)