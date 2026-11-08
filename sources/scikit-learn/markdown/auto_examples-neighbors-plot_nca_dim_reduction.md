[Skip to main content](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_dim_reduction.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neighbors/plot_nca_dim_reduction.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_dim_reduction.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neighbors/plot_nca_dim_reduction.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neighbors/plot_nca_dim_reduction.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neighbors/plot_nca_dim_reduction.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neighbors/plot_nca_dim_reduction.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neighbors/plot_nca_dim_reduction.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_dim_reduction.html#sphx-glr-download-auto-examples-neighbors-plot-nca-dim-reduction-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Dimensionality Reduction with Neighborhood Components Analysis[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_dim_reduction.html#dimensionality-reduction-with-neighborhood-components-analysis "Link to this heading")

=============================================================================================================================================================================================================================================

Sample usage of Neighborhood Components Analysis for dimensionality reduction.

This example compares different (linear) dimensionality reduction methods applied on the Digits data set. The data set contains images of digits from 0 to 9 with approximately 180 samples of each class. Each image is of dimension 8x8 = 64, and is reduced to a two-dimensional data point.

Principal Component Analysis (PCA) applied to this data identifies the combination of attributes (principal components, or directions in the feature space) that account for the most variance in the data. Here we plot the different samples on the 2 first principal components.

Linear Discriminant Analysis (LDA) tries to identify attributes that account for the most variance _between classes_. In particular, LDA, in contrast to PCA, is a supervised method, using known class labels.

Neighborhood Components Analysis (NCA) tries to find a feature space such that a stochastic nearest neighbor algorithm will give the best accuracy. Like LDA, it is a supervised method.

One can see that NCA enforces a clustering of the data that is visually meaningful despite the large reduction in dimension.

*   ![PCA, KNN (k=3) Test accuracy = 0.52](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_dim_reduction_001.png)
*   ![LDA, KNN (k=3) Test accuracy = 0.66](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_dim_reduction_002.png)
*   ![NCA, KNN (k=3) Test accuracy = 0.70](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_dim_reduction_003.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
from sklearn.discriminant\_analysis import [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.neighbors import [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
, [NeighborhoodComponentsAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

n\_neighbors \= 3
random\_state \= 0

\# Load Digits dataset
X, y \= [datasets.load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
(return\_X\_y\=True)

\# Split into train/test
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, test\_size\=0.5, stratify\=y, random\_state\=random\_state
)

dim \= len(X\[0\])
n\_classes \= len([np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(y))

\# Reduce dimension to 2 with PCA
pca \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=2, random\_state\=random\_state))

\# Reduce dimension to 2 with LinearDiscriminantAnalysis
lda \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
(n\_components\=2))

\# Reduce dimension to 2 with NeighborhoodComponentAnalysis
nca \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(),
    [NeighborhoodComponentsAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis")
(n\_components\=2, random\_state\=random\_state),
)

\# Use a nearest neighbor classifier to evaluate the methods
knn \= [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
(n\_neighbors\=n\_neighbors)

\# Make a list of the methods to be compared
dim\_reduction\_methods \= \[("PCA", pca), ("LDA", lda), ("NCA", nca)\]

\# plt.figure()
for i, (name, model) in enumerate(dim\_reduction\_methods):
    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
    \# plt.subplot(1, 3, i + 1, aspect=1)

    \# Fit the method's model
    model.fit(X\_train, y\_train)

    \# Fit a nearest neighbor classifier on the embedded training set
    knn.fit(model.transform(X\_train), y\_train)

    \# Compute the nearest neighbor accuracy on the embedded test set
    acc\_knn \= knn.score(model.transform(X\_test), y\_test)

    \# Embed the data set in 2 dimensions using the fitted model
    X\_embedded \= model.transform(X)

    \# Plot the projected points and show the evaluation score
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_embedded\[:, 0\], X\_embedded\[:, 1\], c\=y, s\=30, cmap\="Set1")
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
        "{}, KNN (k={})\\nTest accuracy = {:.2f}".format(name, n\_neighbors, acc\_knn)
    )
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 1.696 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_nca_dim_reduction.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_nca_dim_reduction.ipynb)

[`Download Jupyter notebook: plot_nca_dim_reduction.ipynb`](https://scikit-learn.org/stable/_downloads/e44c57031af568237dc334b0d317a929/plot_nca_dim_reduction.ipynb)

[`Download Python source code: plot_nca_dim_reduction.py`](https://scikit-learn.org/stable/_downloads/4964d8bc6f2b7f1d6bceb91753b362f0/plot_nca_dim_reduction.py)

[`Download zipped: plot_nca_dim_reduction.zip`](https://scikit-learn.org/stable/_downloads/06c18f4675ecd124f98537d05e10abd0/plot_nca_dim_reduction.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_classification_thumb.png)

[Comparing Nearest Neighbors with and without Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html)

Comparing Nearest Neighbors with and without Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_lda_thumb.png)

[Comparison of LDA and PCA 2D projection of Iris dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html)

Comparison of LDA and PCA 2D projection of Iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_thumb.png)

[Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification](https://scikit-learn.org/stable/auto_examples/classification/plot_lda.html)

Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_illustration_thumb.png)

[Neighborhood Components Analysis Illustration](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_illustration.html)

Neighborhood Components Analysis Illustration

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/4964d8bc6f2b7f1d6bceb91753b362f0/plot_nca_dim_reduction.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/e44c57031af568237dc334b0d317a929/plot_nca_dim_reduction.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/06c18f4675ecd124f98537d05e10abd0/plot_nca_dim_reduction.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_nca_dim_reduction.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_nca_dim_reduction.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)