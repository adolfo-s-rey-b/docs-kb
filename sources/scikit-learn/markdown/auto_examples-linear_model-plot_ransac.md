[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_ransac.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_ransac.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_ransac.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_ransac.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_ransac.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_ransac.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html#sphx-glr-download-auto-examples-linear-model-plot-ransac-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Robust linear model estimation using RANSAC[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html#robust-linear-model-estimation-using-ransac "Link to this heading")

===============================================================================================================================================================================================

In this example, we see how to robustly fit a linear model to faulty data using the [RANSAC](https://scikit-learn.org/stable/modules/linear_model.html#ransac-regression)
 algorithm.

The ordinary linear regressor is sensitive to outliers, and the fitted line can easily be skewed away from the true underlying relationship of data.

The RANSAC regressor automatically splits the data into inliers and outliers, and the fitted line is determined only by the identified inliers.

![plot ransac](https://scikit-learn.org/stable/_images/sphx_glr_plot_ransac_001.png)

Estimated coefficients (true, linear regression, RANSAC):
82.1903908407869 \[54.17236387\] \[82.08533159\]

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import numpy as np
from matplotlib import pyplot as plt

from sklearn import datasets, linear\_model

n\_samples \= 1000
n\_outliers \= 50

X, y, coef \= [datasets.make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
(
    n\_samples\=n\_samples,
    n\_features\=1,
    n\_informative\=1,
    noise\=10,
    coef\=True,
    random\_state\=0,
)

\# Add outlier data
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)
X\[:n\_outliers\] \= 3 + 0.5 \* [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(size\=(n\_outliers, 1))
y\[:n\_outliers\] \= \-3 + 10 \* [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(size\=n\_outliers)

\# Fit line using all data
lr \= [linear\_model.LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
()
lr.fit(X, y)

\# Robustly fit linear model with RANSAC algorithm
ransac \= [linear\_model.RANSACRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
()
ransac.fit(X, y)
inlier\_mask \= ransac.inlier\_mask\_
outlier\_mask \= [np.logical\_not](https://numpy.org/doc/stable/reference/generated/numpy.logical_not.html#numpy.logical_not "numpy.logical_not")
(inlier\_mask)

\# Predict data of estimated models
line\_X \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(X.min(), X.max())\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
line\_y \= lr.predict(line\_X)
line\_y\_ransac \= ransac.predict(line\_X)

\# Compare estimated coefficients
print("Estimated coefficients (true, linear regression, RANSAC):")
print(coef, lr.coef\_, ransac.estimator\_.coef\_)

lw \= 2
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    X\[inlier\_mask\], y\[inlier\_mask\], color\="yellowgreen", marker\=".", label\="Inliers"
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    X\[outlier\_mask\], y\[outlier\_mask\], color\="gold", marker\=".", label\="Outliers"
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(line\_X, line\_y, color\="navy", linewidth\=lw, label\="Linear regressor")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    line\_X,
    line\_y\_ransac,
    color\="cornflowerblue",
    linewidth\=lw,
    label\="RANSAC regressor",
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="lower right")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Input")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Response")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.095 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_ransac.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_ransac.ipynb)

[`Download Jupyter notebook: plot_ransac.ipynb`](https://scikit-learn.org/stable/_downloads/99ccb624369d00fa81b6030937f80b04/plot_ransac.ipynb)

[`Download Python source code: plot_ransac.py`](https://scikit-learn.org/stable/_downloads/b4762c93d453d21e5679b926dd2c532c/plot_ransac.py)

[`Download zipped: plot_ransac.zip`](https://scikit-learn.org/stable/_downloads/eecca55484b603c335baba1e320dddaf/plot_ransac.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_theilsen_thumb.png)

[Theil-Sen Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html)

Theil-Sen Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_fit_thumb.png)

[Robust linear estimator fitting](https://scikit-learn.org/stable/auto_examples/linear_model/plot_robust_fit.html)

Robust linear estimator fitting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mahalanobis_distances_thumb.png)

[Robust covariance estimation and Mahalanobis distances relevance](https://scikit-learn.org/stable/auto_examples/covariance/plot_mahalanobis_distances.html)

Robust covariance estimation and Mahalanobis distances relevance

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_isolation_forest_thumb.png)

[IsolationForest example](https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html)

IsolationForest example

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/b4762c93d453d21e5679b926dd2c532c/plot_ransac.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/99ccb624369d00fa81b6030937f80b04/plot_ransac.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/eecca55484b603c335baba1e320dddaf/plot_ransac.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_ransac.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_ransac.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)