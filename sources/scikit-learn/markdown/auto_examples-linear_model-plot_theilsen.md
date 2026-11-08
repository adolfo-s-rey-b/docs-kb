[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_theilsen.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_theilsen.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_theilsen.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_theilsen.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_theilsen.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_theilsen.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html#sphx-glr-download-auto-examples-linear-model-plot-theilsen-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Theil-Sen Regression[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html#theil-sen-regression "Link to this heading")

===================================================================================================================================================

Computes a Theil-Sen Regression on a synthetic dataset.

See [Theil-Sen estimator: generalized-median-based estimator](https://scikit-learn.org/stable/modules/linear_model.html#theil-sen-regression)
 for more information on the regressor.

Compared to the OLS (ordinary least squares) estimator, the Theil-Sen estimator is robust against outliers. It has a breakdown point of about 29.3% in case of a simple linear regression which means that it can tolerate arbitrary corrupted data (outliers) of up to 29.3% in the two-dimensional case.

The estimation of the model is done by calculating the slopes and intercepts of a subpopulation of all possible combinations of p subsample points. If an intercept is fitted, p must be greater than or equal to n\_features + 1. The final slope and intercept is then defined as the spatial median of these slopes and intercepts.

In certain cases Theil-Sen performs better than [RANSAC](https://scikit-learn.org/stable/modules/linear_model.html#ransac-regression)
 which is also a robust method. This is illustrated in the second example below where outliers with respect to the x-axis perturb RANSAC. Tuning the `residual_threshold` parameter of RANSAC remedies this but in general a priori knowledge about the data and the nature of the outliers is needed. Due to the computational complexity of Theil-Sen it is recommended to use it only for small problems in terms of number of samples and features. For larger problems the `max_subpopulation` parameter restricts the magnitude of all possible combinations of p subsample points to a randomly chosen subset and therefore also limits the runtime. Therefore, Theil-Sen is applicable to larger problems with the drawback of losing some of its mathematical properties since it then works on a random subset.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import time

import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear\_model import [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
, [RANSACRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
, [TheilSenRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "sklearn.linear_model.TheilSenRegressor")

estimators \= \[\
    ("OLS", [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")\
()),\
    ("Theil-Sen", [TheilSenRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "sklearn.linear_model.TheilSenRegressor")\
(random\_state\=42)),\
    ("RANSAC", [RANSACRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")\
(random\_state\=42)),\
\]
colors \= {"OLS": "turquoise", "Theil-Sen": "gold", "RANSAC": "lightgreen"}
lw \= 2

Copy to clipboard

Outliers only in the y direction[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html#outliers-only-in-the-y-direction "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)
n\_samples \= 200
\# Linear model y = 3\*x + N(2, 0.1\*\*2)
x \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_samples)
w \= 3.0
c \= 2.0
noise \= 0.1 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_samples)
y \= w \* x + c + noise
\# 10% outliers
y\[\-20:\] += \-20 \* x\[\-20:\]
X \= x\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]

[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(x, y, color\="indigo", marker\="x", s\=40)
line\_x \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\-3, 3\])
for name, estimator in estimators:
    t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    estimator.fit(X, y)
    elapsed\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
    y\_pred \= estimator.predict(line\_x.reshape(2, 1))
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
        line\_x,
        y\_pred,
        color\=colors\[name\],
        linewidth\=lw,
        label\="%s (fit time: %.2fs)" % (name, elapsed\_time),
    )

[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper right")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Corrupt y")

Copy to clipboard

![Corrupt y](https://scikit-learn.org/stable/_images/sphx_glr_plot_theilsen_001.png)

Outliers in the X direction[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html#outliers-in-the-x-direction "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)
\# Linear model y = 3\*x + N(2, 0.1\*\*2)
x \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_samples)
noise \= 0.1 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_samples)
y \= 3 \* x + 2 + noise
\# 10% outliers
x\[\-20:\] \= 9.9
y\[\-20:\] += 22
X \= x\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(x, y, color\="indigo", marker\="x", s\=40)

line\_x \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\-3, 10\])
for name, estimator in estimators:
    t0 \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    estimator.fit(X, y)
    elapsed\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
    y\_pred \= estimator.predict(line\_x.reshape(2, 1))
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
        line\_x,
        y\_pred,
        color\=colors\[name\],
        linewidth\=lw,
        label\="%s (fit time: %.2fs)" % (name, elapsed\_time),
    )

[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper left")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Corrupt x")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Corrupt x](https://scikit-learn.org/stable/_images/sphx_glr_plot_theilsen_002.png)

**Total running time of the script:** (0 minutes 0.556 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_theilsen.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_theilsen.ipynb)

[`Download Jupyter notebook: plot_theilsen.ipynb`](https://scikit-learn.org/stable/_downloads/16260993c16a6d249d6df4cb11cf8174/plot_theilsen.ipynb)

[`Download Python source code: plot_theilsen.py`](https://scikit-learn.org/stable/_downloads/b0bb69a4a4a86dd9c76717ff515593af/plot_theilsen.py)

[`Download zipped: plot_theilsen.zip`](https://scikit-learn.org/stable/_downloads/07882f339cdda68a73e6335f34418af6/plot_theilsen.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ransac_thumb.png)

[Robust linear model estimation using RANSAC](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html)

Robust linear model estimation using RANSAC

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_fit_thumb.png)

[Robust linear estimator fitting](https://scikit-learn.org/stable/auto_examples/linear_model/plot_robust_fit.html)

Robust linear estimator fitting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_thumb.png)

[Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html)

Compare the effect of different scalers on data with outliers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ols_ridge_thumb.png)

[Ordinary Least Squares and Ridge Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html)

Ordinary Least Squares and Ridge Regression

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/b0bb69a4a4a86dd9c76717ff515593af/plot_theilsen.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/16260993c16a6d249d6df4cb11cf8174/plot_theilsen.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/07882f339cdda68a73e6335f34418af6/plot_theilsen.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_theilsen.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_theilsen.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)