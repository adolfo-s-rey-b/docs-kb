[Skip to main content](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_isotonic_regression.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/miscellaneous/plot_isotonic_regression.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_isotonic_regression.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/miscellaneous/plot_isotonic_regression.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/miscellaneous/plot_isotonic_regression.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/miscellaneous/plot_isotonic_regression.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/miscellaneous/plot_isotonic_regression.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/miscellaneous/plot_isotonic_regression.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_isotonic_regression.html#sphx-glr-download-auto-examples-miscellaneous-plot-isotonic-regression-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Isotonic Regression[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_isotonic_regression.html#isotonic-regression "Link to this heading")

=============================================================================================================================================================

An illustration of the isotonic regression on generated data (non-linear monotonic trend with homoscedastic uniform noise).

The isotonic regression algorithm finds a non-decreasing approximation of a function while minimizing the mean squared error on the training data. The benefit of such a non-parametric model is that it does not assume any shape for the target function besides monotonicity. For comparison a linear regression is also presented.

The plot on the right-hand side shows the model prediction function that results from the linear interpolation of threshold points. The threshold points are a subset of the training input observations and their matching target values are computed by the isotonic non-parametric fit.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import [LineCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")

from sklearn.isotonic import [IsotonicRegression](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
from sklearn.linear\_model import [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
from sklearn.utils import [check\_random\_state](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")

n \= 100
x \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(n)
rs \= [check\_random\_state](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")
(0)
y \= rs.randint(\-50, 50, size\=(n,)) + 50.0 \* [np.log1p](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#numpy.log1p "numpy.log1p")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(n))

Copy to clipboard

Fit IsotonicRegression and LinearRegression models:

ir \= [IsotonicRegression](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
(out\_of\_bounds\="clip")
y\_ \= ir.fit\_transform(x, y)

lr \= [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
()
lr.fit(x\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\], y)  \# x needs to be 2d for LinearRegression

Copy to clipboard

LinearRegression()

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

LinearRegression

[?Documentation for LinearRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to calculate the intercept for this model. If set  <br>to False, no intercept will be used in calculations  <br>(i.e. data is expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |
|     | [copy\_X copy\_X: bool, default=True  <br>  <br>If True, X will be copied; else, it may be overwritten.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=copy_X,-bool%2C%20default%3DTrue) | True |
|     | [tol tol: float, default=1e-6  <br>  <br>The precision of the solution (\`coef\_\`) is determined by \`tol\` which  <br>specifies the convergence criterion of the underlying solver. \`tol\` is  <br>set as \`atol\` and \`btol\` of :func:\`scipy.sparse.linalg.lsqr\` when  <br>fitting on sparse training data. \`tol\` is set as \`cond\` of  <br>:func:\`scipy.linalg.lstsq\` when fitting on dense training data.  <br>  <br>.. versionadded:: 1.7  <br>.. versionchanged:: 1.9  <br>Now supported on dense data, interpreted as the \`cond\` parameter.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=tol,-float%2C%20default%3D1e-6) | 1e-06 |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to use for the computation. This will only provide  <br>speedup in case of sufficiently large problems, that is if firstly  <br>\`n\_targets > 1\` and secondly \`X\` is sparse or if \`positive\` is set  <br>to \`True\`. \`\`None\`\` means 1 unless in a  <br>:obj:\`joblib.parallel\_backend\` context. \`\`-1\`\` means using all  <br>processors. See :term:\`Glossary <n\_jobs>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [positive positive: bool, default=False  <br>  <br>When set to \`\`True\`\`, forces the coefficients to be positive. This  <br>option is only supported for dense arrays.  <br>  <br>For a comparison between a linear regression model with positive constraints  <br>on the regression coefficients and a linear regression without such constraints,  <br>see :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_nnls.py\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=positive,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [coef\_ coef\_: array of shape (n\_features, ) or (n\_targets, n\_features)  <br>  <br>Estimated coefficients for the linear regression problem.  <br>If multiple targets are passed during the fit (y 2D), this  <br>is a 2D array of shape (n\_targets, n\_features), while if only  <br>one target is passed, this is a 1D array of length n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=coef_,-array%20of%20shape%20%28n_features%2C%20%29%20or%20%28n_targets%2C%20n_features%29) | ndarray\[float64\](1,) | \[1.31\] |
| [intercept\_ intercept\_: float or array of shape (n\_targets,)  <br>  <br>Independent term in the linear model. Set to 0.0 if  <br>\`fit\_intercept = False\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=intercept_,-float%20or%20array%20of%20shape%20%28n_targets%2C%29) | float64 | 115.1 |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=n_features_in_,-int) | int | 1   |
| [rank\_ rank\_: int  <br>  <br>Rank of matrix \`X\`. Only available when \`X\` is dense.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=rank_,-int) | int64 | np.int64(1) |
| [singular\_ singular\_: array of shape (min(X, y),)  <br>  <br>Singular values of \`X\`. Only available when \`X\` is dense.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LinearRegression.html#:~:text=singular_,-array%20of%20shape%20%28min%28X%2C%20y%29%2C%29) | ndarray\[float64\](1,) | \[288.66\] |

  
  

Plot results:

segments \= \[\[\[i, y\[i\]\], \[i, y\_\[i\]\]\] for i in range(n)\]
lc \= [LineCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
(segments, zorder\=0)
lc.set\_array([np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(len(y)))
lc.set\_linewidths([np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
(n, 0.5))

fig, (ax0, ax1) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(12, 6))

ax0.plot(x, y, "C0.", markersize\=12)
ax0.plot(x, y\_, "C1.-", markersize\=12)
ax0.plot(x, lr.predict(x\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]), "C2-")
ax0.add\_collection(lc)
ax0.legend(("Training data", "Isotonic fit", "Linear fit"), loc\="lower right")
ax0.set\_title("Isotonic regression fit on noisy data (n=%d)" % n)

x\_test \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-10, 110, 1000)
ax1.plot(x\_test, ir.predict(x\_test), "C1-")
ax1.plot(ir.X\_thresholds\_, ir.y\_thresholds\_, "C1.", markersize\=12)
ax1.set\_title("Prediction function (%d thresholds)" % len(ir.X\_thresholds\_))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Isotonic regression fit on noisy data (n=100), Prediction function (36 thresholds)](https://scikit-learn.org/stable/_images/sphx_glr_plot_isotonic_regression_001.png)

Note that we explicitly passed `out_of_bounds="clip"` to the constructor of `IsotonicRegression` to control the way the model extrapolates outside of the range of data observed in the training set. This “clipping” extrapolation can be seen on the plot of the decision function on the right-hand.

**Total running time of the script:** (0 minutes 0.146 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_isotonic_regression.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_isotonic_regression.ipynb)

[`Download Jupyter notebook: plot_isotonic_regression.ipynb`](https://scikit-learn.org/stable/_downloads/f2e78295c97b04635d9e749896f8e08b/plot_isotonic_regression.ipynb)

[`Download Python source code: plot_isotonic_regression.py`](https://scikit-learn.org/stable/_downloads/8209ef76ac59bf01aad3721a522859ef/plot_isotonic_regression.py)

[`Download zipped: plot_isotonic_regression.zip`](https://scikit-learn.org/stable/_downloads/ecddb0e5ddf1515ce4a8abec5287ef30/plot_isotonic_regression.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_thumb.png)

[Effect of transforming the targets in regression model](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html)

Effect of transforming the targets in regression model

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_pipe_thumb.png)

[Pipelining: chaining a PCA and a logistic regression](https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html)

Pipelining: chaining a PCA and a logistic regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)

[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)

Probability Calibration curves

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_thumb.png)

[Probability calibration of classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html)

Probability calibration of classifiers

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/8209ef76ac59bf01aad3721a522859ef/plot_isotonic_regression.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f2e78295c97b04635d9e749896f8e08b/plot_isotonic_regression.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/ecddb0e5ddf1515ce4a8abec5287ef30/plot_isotonic_regression.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_isotonic_regression.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_isotonic_regression.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)