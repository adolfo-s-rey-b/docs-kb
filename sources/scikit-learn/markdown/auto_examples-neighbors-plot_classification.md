[Skip to main content](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neighbors/plot_classification.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neighbors/plot_classification.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neighbors/plot_classification.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neighbors/plot_classification.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neighbors/plot_classification.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neighbors/plot_classification.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html#sphx-glr-download-auto-examples-neighbors-plot-classification-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Nearest Neighbors Classification[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html#nearest-neighbors-classification "Link to this heading")

==============================================================================================================================================================================

This example shows how to use [`KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
. We train such a classifier on the iris dataset and observe the difference of the decision boundary obtained with regards to the parameter `weights`.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Load the data[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html#load-the-data "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

In this example, we use the iris dataset. We split the data into a train and test dataset.

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

iris \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
(as\_frame\=True)
X \= iris.data\[\["sepal length (cm)", "sepal width (cm)"\]\]
y \= iris.target
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, stratify\=y, random\_state\=0)

Copy to clipboard

K-nearest neighbors classifier[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html#k-nearest-neighbors-classifier "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We want to use a k-nearest neighbors classifier considering a neighborhood of 11 data points. Since our k-nearest neighbors model uses euclidean distance to find the nearest neighbors, it is therefore important to scale the data beforehand. Refer to the example entitled [Importance of Feature Scaling](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html#sphx-glr-auto-examples-preprocessing-plot-scaling-importance-py)
 for more detailed information.

Thus, we use a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 to chain a scaler before to use our classifier.

from sklearn.neighbors import [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

clf \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    steps\=\[("scaler", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
()), ("knn", [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")\
(n\_neighbors\=11))\]
)

Copy to clipboard

Decision boundary[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html#decision-boundary "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

Now, we fit two classifiers with different values of the parameter `weights`. We plot the decision boundary of each classifier as well as the original dataset to observe the difference.

import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.inspection import DecisionBoundaryDisplay

\_, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(12, 5))

for ax, weights in zip(axs, ("uniform", "distance")):
    clf.set\_params(knn\_\_weights\=weights).fit(X\_train, y\_train)
    disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        clf,
        X\_test,
        response\_method\="predict",
        plot\_method\="pcolormesh",
        xlabel\=iris.feature\_names\[0\],
        ylabel\=iris.feature\_names\[1\],
        shading\="auto",
        alpha\=0.5,
        ax\=ax,
    )
    cmap \= [mpl.colors.ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(disp.multiclass\_colors\_)
    scatter \= disp.ax\_.scatter(
        X.iloc\[:, 0\], X.iloc\[:, 1\], c\=y, cmap\=cmap, edgecolors\="k"
    )
    disp.ax\_.legend(
        scatter.legend\_elements()\[0\],
        iris.target\_names,
        loc\="lower right",
        title\="Classes",
    )
    \_ \= disp.ax\_.set\_title(
        f"3-Class classification\\n(k={clf\[\-1\].n\_neighbors}, weights={weights!r})"
    )

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![3-Class classification (k=11, weights='uniform'), 3-Class classification (k=11, weights='distance')](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_001.png)

Conclusion[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html#conclusion "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

We observe that the parameter `weights` has an impact on the decision boundary. When `weights="uniform"` all nearest neighbors will have the same impact on the decision. Whereas when `weights="distance"` the weight given to each neighbor is proportional to the inverse of the distance from that neighbor to the query point.

In some cases, taking the distance into account might improve the model.

**Total running time of the script:** (0 minutes 0.229 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_classification.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_classification.ipynb)

[`Download Jupyter notebook: plot_classification.ipynb`](https://scikit-learn.org/stable/_downloads/47f024d726d245e034c7690b4664721f/plot_classification.ipynb)

[`Download Python source code: plot_classification.py`](https://scikit-learn.org/stable/_downloads/8d0cc737ca20800f70d8aa80d8b8fb7d/plot_classification.py)

[`Download zipped: plot_classification.zip`](https://scikit-learn.org/stable/_downloads/41475a5e6fc6360930267b5cd092c937/plot_classification.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_classification_thumb.png)

[Comparing Nearest Neighbors with and without Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html)

Comparing Nearest Neighbors with and without Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_regression_thumb.png)

[Nearest Neighbors regression](https://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html)

Nearest Neighbors regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nearest_centroid_thumb.png)

[Nearest Centroid Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nearest_centroid.html)

Nearest Centroid Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_thumb.png)

[Plot the decision surface of decision trees trained on the iris dataset](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Plot the decision surface of decision trees trained on the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/8d0cc737ca20800f70d8aa80d8b8fb7d/plot_classification.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/47f024d726d245e034c7690b4664721f/plot_classification.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/41475a5e6fc6360930267b5cd092c937/plot_classification.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_classification.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_classification.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)