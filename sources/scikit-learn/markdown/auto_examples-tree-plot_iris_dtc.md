[Skip to main content](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/tree/plot_iris_dtc.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/tree/plot_iris_dtc.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/tree/plot_iris_dtc.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/tree/plot_iris_dtc.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/tree/plot_iris_dtc.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/tree/plot_iris_dtc.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html#sphx-glr-download-auto-examples-tree-plot-iris-dtc-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Plot the decision surface of decision trees trained on the iris dataset[#](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html#plot-the-decision-surface-of-decision-trees-trained-on-the-iris-dataset "Link to this heading")

=================================================================================================================================================================================================================================================

Plot the decision surface of a decision tree trained on pairs of features of the iris dataset.

See [decision tree](https://scikit-learn.org/stable/modules/tree.html#tree)
 for more information on the estimator.

For each pair of iris features, the decision tree learns decision boundaries made of combinations of simple thresholding rules inferred from the training samples.

We also show the tree structure of a model built on all of the features.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

First load the copy of the Iris dataset shipped with scikit-learn:

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")

iris \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()

Copy to clipboard

Display the decision functions of trees trained on all pairs of features.

import matplotlib.pyplot as plt
from matplotlib.colors import [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")

from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.tree import [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")

for pairidx, pair in enumerate(\[\[0, 1\], \[0, 2\], \[0, 3\], \[1, 2\], \[1, 3\], \[2, 3\]\]):
    \# We only take the two corresponding features
    X \= iris.data\[:, pair\]
    y \= iris.target

    \# Train
    clf \= [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
().fit(X, y)

    \# Plot the decision boundary
    ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 3, pairidx + 1)
    [plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
(h\_pad\=0.5, w\_pad\=0.5, pad\=2.5)
    disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        clf,
        X,
        response\_method\="predict",
        ax\=ax,
        xlabel\=iris.feature\_names\[pair\[0\]\],
        ylabel\=iris.feature\_names\[pair\[1\]\],
        alpha\=0.5,
    )

    \# Plot the training points
    scatter \= disp.ax\_.scatter(
        X\[:, 0\],
        X\[:, 1\],
        c\=y,
        cmap\=[ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(disp.multiclass\_colors\_),
        edgecolor\="black",
        s\=15,
    )

[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")
("Decision surface of decision trees trained on pairs of features")
[plt.figlegend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figlegend.html#matplotlib.pyplot.figlegend "matplotlib.pyplot.figlegend")
(
    scatter.legend\_elements()\[0\],
    iris.target\_names,
    loc\="lower center",
    ncols\=len(iris.target\_names),
)
\_ \= [plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

Copy to clipboard

![Decision surface of decision trees trained on pairs of features](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_001.png)

Display the structure of a single decision tree trained on all the features together.

from sklearn.tree import [plot\_tree](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
clf \= [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
().fit(iris.data, iris.target)
[plot\_tree](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree")
(clf, filled\=True)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Decision tree trained on all the iris features")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Decision tree trained on all the iris features](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_002.png)

**Total running time of the script:** (0 minutes 0.832 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo33.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/tree/plot_iris_dtc.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo33.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/tree/plot_iris_dtc.ipynb)

[`Download Jupyter notebook: plot_iris_dtc.ipynb`](https://scikit-learn.org/stable/_downloads/bc4cacb86f284cd0b3913166a69c9fb2/plot_iris_dtc.ipynb)

[`Download Python source code: plot_iris_dtc.py`](https://scikit-learn.org/stable/_downloads/00ae629d652473137a3905a5e08ea815/plot_iris_dtc.py)

[`Download zipped: plot_iris_dtc.zip`](https://scikit-learn.org/stable/_downloads/bbfe808211963096bb78580f7fc28b10/plot_iris_dtc.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_thumb.png)

[Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)

Principal Component Analysis (PCA) on Iris Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nearest_centroid_thumb.png)

[Nearest Centroid Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nearest_centroid.html)

Nearest Centroid Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_iris_thumb.png)

[Plot multi-class SGD on the iris dataset](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html)

Plot multi-class SGD on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_incremental_pca_thumb.png)

[Incremental PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html)

Incremental PCA

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/00ae629d652473137a3905a5e08ea815/plot_iris_dtc.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/bc4cacb86f284cd0b3913166a69c9fb2/plot_iris_dtc.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/bbfe808211963096bb78580f7fc28b10/plot_iris_dtc.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo33.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/tree/plot_iris_dtc.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo33.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/tree/plot_iris_dtc.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)