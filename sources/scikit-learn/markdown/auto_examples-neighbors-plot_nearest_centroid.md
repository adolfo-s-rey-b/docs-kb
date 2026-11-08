[Skip to main content](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nearest_centroid.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neighbors/plot_nearest_centroid.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nearest_centroid.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neighbors/plot_nearest_centroid.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neighbors/plot_nearest_centroid.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neighbors/plot_nearest_centroid.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neighbors/plot_nearest_centroid.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neighbors/plot_nearest_centroid.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nearest_centroid.html#sphx-glr-download-auto-examples-neighbors-plot-nearest-centroid-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Nearest Centroid Classification[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nearest_centroid.html#nearest-centroid-classification "Link to this heading")

==============================================================================================================================================================================

Sample usage of the [Nearest Centroid Classifier](https://scikit-learn.org/stable/modules/neighbors.html#nearest-centroid-classifier)
 with different shrink thresholds. It will plot the decision boundaries for each class.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")

from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.neighbors import [NearestCentroid](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")

\# import some data to play with
iris \= [datasets.load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
\# we only take the first two features. We could avoid this ugly
\# slicing by using a two-dim dataset
X \= iris.data\[:, :2\]
y \= iris.target

for shrinkage in \[None, 0.2\]:
    \# we create an instance of Nearest Centroid Classifier and fit the data.
    clf \= [NearestCentroid](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")
(shrink\_threshold\=shrinkage)
    clf.fit(X, y)
    y\_pred \= clf.predict(X)
    acc \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(y \== y\_pred)

    \_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
    disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        clf, X, ax\=ax, response\_method\="predict", alpha\=0.5
    )

    \# Plot also the training points
    cmap \= [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(disp.multiclass\_colors\_)
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], c\=y, cmap\=cmap, edgecolor\="k", s\=20)
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(
        f"3-Class classification (shrink\_threshold={shrinkage})\\nAccuracy: {acc:.2f}"
    )
    [plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

*   ![3-Class classification (shrink_threshold=None) Accuracy: 0.81](https://scikit-learn.org/stable/_images/sphx_glr_plot_nearest_centroid_001.png)
*   ![3-Class classification (shrink_threshold=0.2) Accuracy: 0.82](https://scikit-learn.org/stable/_images/sphx_glr_plot_nearest_centroid_002.png)

**Total running time of the script:** (0 minutes 0.161 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_nearest_centroid.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_nearest_centroid.ipynb)

[`Download Jupyter notebook: plot_nearest_centroid.ipynb`](https://scikit-learn.org/stable/_downloads/06ffeb4f0ded6447302acd5a712f8490/plot_nearest_centroid.ipynb)

[`Download Python source code: plot_nearest_centroid.py`](https://scikit-learn.org/stable/_downloads/1ee82dc6471486cb5b088fc473cd945b/plot_nearest_centroid.py)

[`Download zipped: plot_nearest_centroid.zip`](https://scikit-learn.org/stable/_downloads/603c968ffea3a0291127213cb66729c8/plot_nearest_centroid.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_thumb.png)

[Plot the decision surface of decision trees trained on the iris dataset](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Plot the decision surface of decision trees trained on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_thumb.png)

[Nearest Neighbors Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html)

Nearest Neighbors Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_classification_thumb.png)

[Comparing Nearest Neighbors with and without Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html)

Comparing Nearest Neighbors with and without Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_custom_kernel_thumb.png)

[SVM with custom kernel](https://scikit-learn.org/stable/auto_examples/svm/plot_custom_kernel.html)

SVM with custom kernel

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/1ee82dc6471486cb5b088fc473cd945b/plot_nearest_centroid.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/06ffeb4f0ded6447302acd5a712f8490/plot_nearest_centroid.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/603c968ffea3a0291127213cb66729c8/plot_nearest_centroid.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_nearest_centroid.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_nearest_centroid.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)