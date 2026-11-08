[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_robust_fit.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_robust_fit.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_robust_fit.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_robust_fit.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_robust_fit.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_robust_fit.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_robust_fit.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_robust_fit.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_robust_fit.html#sphx-glr-download-auto-examples-linear-model-plot-robust-fit-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Robust linear estimator fitting[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_robust_fit.html#robust-linear-estimator-fitting "Link to this heading")

===========================================================================================================================================================================

Here a sine function is fit with a polynomial of order 3, for values close to zero.

Robust fitting is demonstrated in different situations:

*   No measurement errors, only modelling errors (fitting a sine with a polynomial)
    
*   Measurement errors in X
    
*   Measurement errors in y
    

The median absolute deviation to non corrupt new data is used to judge the quality of the prediction.

What we can see that:

*   RANSAC is good for strong outliers in the y direction
    
*   TheilSen is good for small outliers, both in direction X and y, but has a break point above which it performs worse than OLS.
    
*   The scores of HuberRegressor may not be compared directly to both TheilSen and RANSAC because it does not attempt to completely filter the outliers but lessen their effect.
    

*   ![Modeling Errors Only](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_fit_001.png)
*   ![Corrupt X, Small Deviants](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_fit_002.png)
*   ![Corrupt y, Small Deviants](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_fit_003.png)
*   ![Corrupt X, Large Deviants](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_fit_004.png)
*   ![Corrupt y, Large Deviants](https://scikit-learn.org/stable/_images/sphx_glr_plot_robust_fit_005.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import numpy as np
from matplotlib import pyplot as plt

from sklearn.linear\_model import (
    [HuberRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor")
,
    [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
,
    [RANSACRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
,
    [TheilSenRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "sklearn.linear_model.TheilSenRegressor")
,
)
from sklearn.metrics import [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(42)

X \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(size\=400)
y \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(X)
\# Make sure that it X is 2D
X \= X\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]

X\_test \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(size\=200)
y\_test \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(X\_test)
X\_test \= X\_test\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]

y\_errors \= y.copy()
y\_errors\[::3\] \= 3

X\_errors \= X.copy()
X\_errors\[::3\] \= 3

y\_errors\_large \= y.copy()
y\_errors\_large\[::3\] \= 10

X\_errors\_large \= X.copy()
X\_errors\_large\[::3\] \= 10

estimators \= \[\
    ("OLS", [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")\
()),\
    ("Theil-Sen", [TheilSenRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "sklearn.linear_model.TheilSenRegressor")\
(random\_state\=42)),\
    ("RANSAC", [RANSACRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")\
(random\_state\=42)),\
    ("HuberRegressor", [HuberRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor")\
()),\
\]
colors \= {
    "OLS": "turquoise",
    "Theil-Sen": "gold",
    "RANSAC": "lightgreen",
    "HuberRegressor": "black",
}
linestyle \= {"OLS": "-", "Theil-Sen": "-.", "RANSAC": "--", "HuberRegressor": "--"}
lw \= 3

x\_plot \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(X.min(), X.max())
for title, this\_X, this\_y in \[\
    ("Modeling Errors Only", X, y),\
    ("Corrupt X, Small Deviants", X\_errors, y),\
    ("Corrupt y, Small Deviants", X, y\_errors),\
    ("Corrupt X, Large Deviants", X\_errors\_large, y),\
    ("Corrupt y, Large Deviants", X, y\_errors\_large),\
\]:
    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5, 4))
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(this\_X\[:, 0\], this\_y, "b+")

    for name, estimator in estimators:
        model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
(3), estimator)
        model.fit(this\_X, this\_y)
        mse \= [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
(model.predict(X\_test), y\_test)
        y\_plot \= model.predict(x\_plot\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\])
        [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
            x\_plot,
            y\_plot,
            color\=colors\[name\],
            linestyle\=linestyle\[name\],
            linewidth\=lw,
            label\="%s: error = %.3f" % (name, mse),
        )

    legend\_title \= "Error of Mean\\nAbsolute Deviation\\nto Non-corrupt Data"
    legend \= [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(
        loc\="upper right", frameon\=False, title\=legend\_title, prop\=dict(size\="x-small")
    )
    [plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(\-4, 10.2)
    [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(\-2, 10.2)
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(title)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 2.189 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_robust_fit.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_robust_fit.ipynb)

[`Download Jupyter notebook: plot_robust_fit.ipynb`](https://scikit-learn.org/stable/_downloads/c93b4e0b422f79bfcb544a032cebe455/plot_robust_fit.ipynb)

[`Download Python source code: plot_robust_fit.py`](https://scikit-learn.org/stable/_downloads/a58a561a3187398ccd5be0dc2e18e01d/plot_robust_fit.py)

[`Download zipped: plot_robust_fit.zip`](https://scikit-learn.org/stable/_downloads/a444bb0cccc6e91b6043fdced497ce82/plot_robust_fit.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_theilsen_thumb.png)

[Theil-Sen Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html)

Theil-Sen Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ransac_thumb.png)

[Robust linear model estimation using RANSAC](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html)

Robust linear model estimation using RANSAC

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ard_thumb.png)

[Comparing Linear Bayesian Regressors](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html)

Comparing Linear Bayesian Regressors

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_huber_vs_ridge_thumb.png)

[HuberRegressor vs Ridge on dataset with strong outliers](https://scikit-learn.org/stable/auto_examples/linear_model/plot_huber_vs_ridge.html)

HuberRegressor vs Ridge on dataset with strong outliers

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/a58a561a3187398ccd5be0dc2e18e01d/plot_robust_fit.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c93b4e0b422f79bfcb544a032cebe455/plot_robust_fit.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/a444bb0cccc6e91b6043fdced497ce82/plot_robust_fit.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_robust_fit.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_robust_fit.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)