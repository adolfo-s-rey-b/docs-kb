[Skip to main content](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neighbors/plot_nca_classification.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neighbors/plot_nca_classification.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neighbors/plot_nca_classification.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neighbors/plot_nca_classification.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neighbors/plot_nca_classification.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neighbors/plot_nca_classification.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html#sphx-glr-download-auto-examples-neighbors-plot-nca-classification-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparing Nearest Neighbors with and without Neighborhood Components Analysis[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html#comparing-nearest-neighbors-with-and-without-neighborhood-components-analysis "Link to this heading")

============================================================================================================================================================================================================================================================================

An example comparing nearest neighbors classification with and without [Neighborhood Components Analysis](https://scikit-learn.org/stable/modules/neighbors.html#nca)
.

It will plot the class decision boundaries given by a Nearest Neighbors classifier when using the Euclidean distance on the original features, versus using the Euclidean distance after the transformation learned by Neighborhood Components Analysis. The latter aims to find a linear transformation that maximises the (stochastic) nearest neighbor classification accuracy on the training set.

*   ![KNN (k = 1)](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_classification_001.png)
*   ![NCA, KNN (k = 1)](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_classification_002.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
from matplotlib.colors import [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")

from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.neighbors import [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
, [NeighborhoodComponentsAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

n\_neighbors \= 1

dataset \= [datasets.load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X, y \= dataset.data, dataset.target

\# we only take two features. We could avoid this ugly
\# slicing by using a two-dim dataset
X \= X\[:, \[0, 2\]\]

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, stratify\=y, test\_size\=0.7, random\_state\=42
)

names \= \["KNN", "NCA, KNN"\]

classifiers \= \[\
    [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
(\
        \[\
            ("scaler", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
()),\
            ("knn", [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")\
(n\_neighbors\=n\_neighbors)),\
        \]\
    ),\
    [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
(\
        \[\
            ("scaler", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
()),\
            ("nca", [NeighborhoodComponentsAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis")\
()),\
            ("knn", [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")\
(n\_neighbors\=n\_neighbors)),\
        \]\
    ),\
\]

for name, clf in zip(names, classifiers):
    clf.fit(X\_train, y\_train)
    score \= clf.score(X\_test, y\_test)

    \_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
    disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        clf,
        X,
        alpha\=0.5,
        ax\=ax,
        response\_method\="predict",
        plot\_method\="pcolormesh",
        shading\="auto",
    )

    \# Plot also the training and testing points
    cmap \= [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(disp.multiclass\_colors\_)
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], c\=y, cmap\=cmap, edgecolor\="k", s\=20)
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(f"{name} (k = {n\_neighbors})")
    [plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(
        0.9,
        0.1,
        f"{score:.2f}",
        size\=15,
        ha\="center",
        va\="center",
        transform\=[plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
().transAxes,
    )

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.160 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_nca_classification.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_nca_classification.ipynb)

[`Download Jupyter notebook: plot_nca_classification.ipynb`](https://scikit-learn.org/stable/_downloads/54c7ea3b3671861fbfb2161a6f0ab6d0/plot_nca_classification.ipynb)

[`Download Python source code: plot_nca_classification.py`](https://scikit-learn.org/stable/_downloads/b7792f6c26a74369f67bbe6f9ac41edf/plot_nca_classification.py)

[`Download zipped: plot_nca_classification.zip`](https://scikit-learn.org/stable/_downloads/8b88532e3291dedc081d198e7ea23254/plot_nca_classification.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_dim_reduction_thumb.png)

[Dimensionality Reduction with Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_dim_reduction.html)

Dimensionality Reduction with Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_thumb.png)

[Nearest Neighbors Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html)

Nearest Neighbors Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_caching_nearest_neighbors_thumb.png)

[Caching nearest neighbors](https://scikit-learn.org/stable/auto_examples/neighbors/plot_caching_nearest_neighbors.html)

Caching nearest neighbors

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_illustration_thumb.png)

[Neighborhood Components Analysis Illustration](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_illustration.html)

Neighborhood Components Analysis Illustration

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/b7792f6c26a74369f67bbe6f9ac41edf/plot_nca_classification.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/54c7ea3b3671861fbfb2161a6f0ab6d0/plot_nca_classification.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/8b88532e3291dedc081d198e7ea23254/plot_nca_classification.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_nca_classification.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_nca_classification.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)