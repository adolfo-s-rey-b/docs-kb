[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_nnls.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_nnls.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_nnls.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_nnls.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_nnls.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_nnls.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_nnls.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_nnls.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_nnls.html#sphx-glr-download-auto-examples-linear-model-plot-nnls-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Non-negative least squares[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_nnls.html#non-negative-least-squares "Link to this heading")

===========================================================================================================================================================

In this example, we fit a linear model with positive constraints on the regression coefficients and compare the estimated coefficients to a classic linear regression.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import [r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")

Copy to clipboard

Generate some random data

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(42)

n\_samples, n\_features \= 200, 50
X \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_samples, n\_features)
true\_coef \= 3 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n\_features)
\# Threshold coefficients to render them non-negative
true\_coef\[true\_coef < 0\] \= 0
y \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(X, true\_coef)

\# Add some noise
y += 5 \* [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(size\=(n\_samples,))

Copy to clipboard

Split the data in train set and test set

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, test\_size\=0.5)

Copy to clipboard

Fit the Non-Negative least squares.

from sklearn.linear\_model import [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")

reg\_nnls \= [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
(positive\=True)
y\_pred\_nnls \= reg\_nnls.fit(X\_train, y\_train).predict(X\_test)
r2\_score\_nnls \= [r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
(y\_test, y\_pred\_nnls)
print("NNLS R2 score", r2\_score\_nnls)

Copy to clipboard

NNLS R2 score 0.8225220806196525

Copy to clipboard

Fit an OLS.

reg\_ols \= [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
()
y\_pred\_ols \= reg\_ols.fit(X\_train, y\_train).predict(X\_test)
r2\_score\_ols \= [r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
(y\_test, y\_pred\_ols)
print("OLS R2 score", r2\_score\_ols)

Copy to clipboard

OLS R2 score 0.7436926291700342

Copy to clipboard

Comparing the regression coefficients between OLS and NNLS, we can observe they are highly correlated (the dashed line is the identity relation), but the non-negative constraint shrinks some to 0. The Non-Negative Least squares inherently yield sparse results.

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
ax.plot(reg\_ols.coef\_, reg\_nnls.coef\_, linewidth\=0, marker\=".")

low\_x, high\_x \= ax.get\_xlim()
low\_y, high\_y \= ax.get\_ylim()
low \= max(low\_x, low\_y)
high \= min(high\_x, high\_y)
ax.plot(\[low, high\], \[low, high\], ls\="--", c\=".3", alpha\=0.5)
ax.set\_xlabel("OLS regression coefficients", fontweight\="bold")
ax.set\_ylabel("NNLS regression coefficients", fontweight\="bold")

Copy to clipboard

![plot nnls](https://scikit-learn.org/stable/_images/sphx_glr_plot_nnls_001.png)

Text(55.722222222222214, 0.5, 'NNLS regression coefficients')

Copy to clipboard

**Total running time of the script:** (0 minutes 0.068 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_nnls.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_nnls.ipynb)

[`Download Jupyter notebook: plot_nnls.ipynb`](https://scikit-learn.org/stable/_downloads/581dc0b49de1be345ed0b6010e5f873d/plot_nnls.ipynb)

[`Download Python source code: plot_nnls.py`](https://scikit-learn.org/stable/_downloads/055e50ba9fa8c7dcf45dc8f1f32a0243/plot_nnls.py)

[`Download zipped: plot_nnls.zip`](https://scikit-learn.org/stable/_downloads/27a5c8b09da77b54a3849bd8e0ff0d31/plot_nnls.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ols_ridge_thumb.png)

[Ordinary Least Squares and Ridge Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html)

Ordinary Least Squares and Ridge Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_train_error_vs_test_error_thumb.png)

[Effect of model regularization on training and test error](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html)

Effect of model regularization on training and test error

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_causal_interpretation_thumb.png)

[Failure of Machine Learning to infer causal effects](https://scikit-learn.org/stable/auto_examples/inspection/plot_causal_interpretation.html)

Failure of Machine Learning to infer causal effects

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ard_thumb.png)

[Comparing Linear Bayesian Regressors](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html)

Comparing Linear Bayesian Regressors

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/055e50ba9fa8c7dcf45dc8f1f32a0243/plot_nnls.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/581dc0b49de1be345ed0b6010e5f873d/plot_nnls.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/27a5c8b09da77b54a3849bd8e0ff0d31/plot_nnls.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_nnls.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_nnls.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)