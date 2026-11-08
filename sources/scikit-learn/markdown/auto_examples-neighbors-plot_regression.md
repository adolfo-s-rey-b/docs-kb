[Skip to main content](https://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neighbors/plot_regression.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neighbors/plot_regression.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neighbors/plot_regression.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neighbors/plot_regression.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neighbors/plot_regression.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neighbors/plot_regression.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html#sphx-glr-download-auto-examples-neighbors-plot-regression-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Nearest Neighbors regression[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html#nearest-neighbors-regression "Link to this heading")

==================================================================================================================================================================

Demonstrate the resolution of a regression problem using a k-Nearest Neighbor and the interpolation of the target using both barycenter and constant weights.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate sample data[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html#generate-sample-data "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

Here we generate a few data points to use to train the model. We also generate data in the whole range of the training data to visualize how the model would react in that whole region.

import matplotlib.pyplot as plt
import numpy as np

from sklearn import neighbors

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
X\_train \= [np.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
(5 \* rng.rand(40, 1), axis\=0)
X\_test \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 5, 500)\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
y \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(X\_train).ravel()

\# Add noise to targets
y\[::5\] += 1 \* (0.5 \- [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(8))

Copy to clipboard

Fit regression model[#](https://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html#fit-regression-model "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

Here we train a model and visualize how `uniform` and `distance` weights in prediction effect predicted values.

n\_neighbors \= 5

for i, weights in enumerate(\["uniform", "distance"\]):
    knn \= [neighbors.KNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
(n\_neighbors, weights\=weights)
    y\_ \= knn.fit(X\_train, y).predict(X\_test)

    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 1, i + 1)
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_train, y, color\="darkorange", label\="data")
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, y\_, color\="navy", label\="prediction")
    [plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
    [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("KNeighborsRegressor (k = %i, weights = '%s')" % (n\_neighbors, weights))

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![KNeighborsRegressor (k = 5, weights = 'uniform'), KNeighborsRegressor (k = 5, weights = 'distance')](https://scikit-learn.org/stable/_images/sphx_glr_plot_regression_001.png)

**Total running time of the script:** (0 minutes 0.182 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_regression.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_regression.ipynb)

[`Download Jupyter notebook: plot_regression.ipynb`](https://scikit-learn.org/stable/_downloads/8daa075623a97eefa5be2c4a6eb55992/plot_regression.ipynb)

[`Download Python source code: plot_regression.py`](https://scikit-learn.org/stable/_downloads/437df39fcde24ead7b91917f2133a53c/plot_regression.py)

[`Download zipped: plot_regression.zip`](https://scikit-learn.org/stable/_downloads/66bd3d78a17dbf797557992df72ff73e/plot_regression.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_thumb.png)

[Nearest Neighbors Classification](https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html)

Nearest Neighbors Classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nca_classification_thumb.png)

[Comparing Nearest Neighbors with and without Neighborhood Components Analysis](https://scikit-learn.org/stable/auto_examples/neighbors/plot_nca_classification.html)

Comparing Nearest Neighbors with and without Neighborhood Components Analysis

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_weighted_samples_thumb.png)

[SVM: Weighted samples](https://scikit-learn.org/stable/auto_examples/svm/plot_weighted_samples.html)

SVM: Weighted samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_caching_nearest_neighbors_thumb.png)

[Caching nearest neighbors](https://scikit-learn.org/stable/auto_examples/neighbors/plot_caching_nearest_neighbors.html)

Caching nearest neighbors

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/437df39fcde24ead7b91917f2133a53c/plot_regression.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/8daa075623a97eefa5be2c4a6eb55992/plot_regression.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/66bd3d78a17dbf797557992df72ff73e/plot_regression.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo26.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neighbors/plot_regression.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo26.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neighbors/plot_regression.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)