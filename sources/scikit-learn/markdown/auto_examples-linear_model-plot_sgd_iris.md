[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_sgd_iris.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_sgd_iris.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_sgd_iris.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_sgd_iris.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_sgd_iris.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_sgd_iris.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html#sphx-glr-download-auto-examples-linear-model-plot-sgd-iris-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Plot multi-class SGD on the iris dataset[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html#plot-multi-class-sgd-on-the-iris-dataset "Link to this heading")

===========================================================================================================================================================================================

Plot decision surface of multi-class SGD on iris dataset. The hyperplanes corresponding to the three one-versus-all (OVA) classifiers are represented by the dashed lines.

![Decision surface of multi-class SGD](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_iris_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.linear\_model import [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")

\# import some data to play with
iris \= [datasets.load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()

\# we only take the first two features. We could
\# avoid this ugly slicing by using a two-dim dataset
X \= iris.data\[:, :2\]
y \= iris.target
colors \= "byr"

\# shuffle
idx \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(X.shape\[0\])
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(13)
[np.random.shuffle](https://numpy.org/doc/stable/reference/random/generated/numpy.random.shuffle.html#numpy.random.shuffle "numpy.random.shuffle")
(idx)
X \= X\[idx\]
y \= y\[idx\]

\# standardize
mean \= X.mean(axis\=0)
std \= X.std(axis\=0)
X \= (X \- mean) / std

clf \= [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
(alpha\=0.001, max\_iter\=100).fit(X, y)
ax \= [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()
[DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    clf,
    X,
    ax\=ax,
    response\_method\="predict",
    xlabel\=iris.feature\_names\[0\],
    ylabel\=iris.feature\_names\[1\],
)
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

\# Plot also the training points
for i, color in zip(clf.classes\_, colors):
    idx \= (y \== i).nonzero()
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
        X\[idx, 0\],
        X\[idx, 1\],
        c\=color,
        label\=iris.target\_names\[i\],
        edgecolor\="black",
        s\=20,
    )
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Decision surface of multi-class SGD")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")

\# Plot the three one-against-all classifiers
xmin, xmax \= [plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
()
ymin, ymax \= [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
()
coef \= clf.coef\_
intercept \= clf.intercept\_

def plot\_hyperplane(c, color):
    def line(x0):
        return (\-(x0 \* coef\[c, 0\]) \- intercept\[c\]) / coef\[c, 1\]

    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(\[xmin, xmax\], \[line(xmin), line(xmax)\], ls\="--", color\=color)

for i, color in zip(clf.classes\_, colors):
    plot\_hyperplane(i, color)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.117 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sgd_iris.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sgd_iris.ipynb)

[`Download Jupyter notebook: plot_sgd_iris.ipynb`](https://scikit-learn.org/stable/_downloads/97ec5b2cda9af9d409cf94ba3ae5e270/plot_sgd_iris.ipynb)

[`Download Python source code: plot_sgd_iris.py`](https://scikit-learn.org/stable/_downloads/de80e18b1c5bc8b447bbce5b9750c567/plot_sgd_iris.py)

[`Download zipped: plot_sgd_iris.zip`](https://scikit-learn.org/stable/_downloads/6740e8b7b0e74561d2572efc253b6034/plot_sgd_iris.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_thumb.png)

[Plot the decision surface of decision trees trained on the iris dataset](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Plot the decision surface of decision trees trained on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_thumb.png)

[Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)

Principal Component Analysis (PCA) on Iris Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nearest_centroid_thumb.png)

[Nearest Centroid Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nearest_centroid.html)

Nearest Centroid Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_incremental_pca_thumb.png)

[Incremental PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html)

Incremental PCA

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/de80e18b1c5bc8b447bbce5b9750c567/plot_sgd_iris.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/97ec5b2cda9af9d409cf94ba3ae5e270/plot_sgd_iris.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/6740e8b7b0e74561d2572efc253b6034/plot_sgd_iris.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_sgd_iris.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_sgd_iris.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)