[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_gradient_boosting_regression.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_gradient_boosting_regression.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_gradient_boosting_regression.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_gradient_boosting_regression.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_gradient_boosting_regression.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_gradient_boosting_regression.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html#sphx-glr-download-auto-examples-ensemble-plot-gradient-boosting-regression-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Gradient Boosting regression[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html#gradient-boosting-regression "Link to this heading")

===================================================================================================================================================================================

This example demonstrates Gradient Boosting to produce a predictive model from an ensemble of weak predictive models. Gradient boosting can be used for regression and classification problems. Here, we will train a model to tackle a diabetes regression task. We will obtain the results from [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
 with least squares loss and 500 regression trees of depth 4.

Note: For larger datasets (n\_samples >= 10000), please refer to [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
. See [Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html#sphx-glr-auto-examples-ensemble-plot-hgbt-regression-py)
 for an example showcasing some other advantages of `HistGradientBoostingRegressor`.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, ensemble
from sklearn.inspection import [permutation\_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
from sklearn.metrics import [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.utils.fixes import parse\_version

Copy to clipboard

Load the data[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html#load-the-data "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

First we need to load the data.

diabetes \= [datasets.load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
()
X, y \= diabetes.data, diabetes.target

Copy to clipboard

Data preprocessing[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html#data-preprocessing "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

Next, we will split our dataset to use 90% for training and leave the rest for testing. We will also set the regression model parameters. You can play with these parameters to see how the results change.

`n_estimators` : the number of boosting stages that will be performed. Later, we will plot deviance against boosting iterations.

`max_depth` : limits the number of nodes in the tree. The best value depends on the interaction of the input variables.

`min_samples_split` : the minimum number of samples required to split an internal node.

`learning_rate` : how much the contribution of each tree will shrink.

`loss` : loss function to optimize. The least squares function is used in this case however, there are many other options (see [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
 ).

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, test\_size\=0.1, random\_state\=13
)

params \= {
    "n\_estimators": 500,
    "max\_depth": 4,
    "min\_samples\_split": 5,
    "learning\_rate": 0.01,
    "loss": "squared\_error",
}

Copy to clipboard

Fit regression model[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html#fit-regression-model "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now we will initiate the gradient boosting regressors and fit it with our training data. Let’s also look and the mean squared error on the test data.

reg \= [ensemble.GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
(\*\*params)
reg.fit(X\_train, y\_train)

mse \= [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
(y\_test, reg.predict(X\_test))
print("The mean squared error (MSE) on test set: {:.4f}".format(mse))

Copy to clipboard

The mean squared error (MSE) on test set: 3009.3069

Copy to clipboard

Plot training deviance[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html#plot-training-deviance "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Finally, we will visualize the results. To do that we will first compute the test set deviance and then plot it against boosting iterations.

test\_score \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((params\["n\_estimators"\],), dtype\=[np.float64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
for i, y\_pred in enumerate(reg.staged\_predict(X\_test)):
    test\_score\[i\] \= [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
(y\_test, y\_pred)

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(6, 6))
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 1, 1)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Deviance")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(params\["n\_estimators"\]) + 1,
    reg.train\_score\_,
    "b-",
    label\="Training Set Deviance",
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(params\["n\_estimators"\]) + 1, test\_score, "r-", label\="Test Set Deviance"
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper right")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Boosting Iterations")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Deviance")
fig.tight\_layout()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Deviance](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_001.png)

Plot feature importance[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html#plot-feature-importance "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Warning

Careful, impurity-based feature importances can be misleading for **high cardinality** features (many unique values). As an alternative, the permutation importances of `reg` can be computed on a held out test set. See [Permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html#permutation-importance)
 for more details.

For this example, the impurity-based and permutation methods identify the same 2 strongly predictive features but not in the same order. The third most predictive feature, “bp”, is also the same for the 2 methods. The remaining features are less predictive and the error bars of the permutation plot show that they overlap with 0.

feature\_importance \= reg.feature\_importances\_
sorted\_idx \= [np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
(feature\_importance)
pos \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(sorted\_idx.shape\[0\]) + 0.5
fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(12, 6))
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 2, 1)
[plt.barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html#matplotlib.pyplot.barh "matplotlib.pyplot.barh")
(pos, feature\_importance\[sorted\_idx\], align\="center")
[plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(pos, [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(diabetes.feature\_names)\[sorted\_idx\])
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Feature Importance (MDI)")

result \= [permutation\_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
(
    reg, X\_test, y\_test, n\_repeats\=10, random\_state\=42, n\_jobs\=2
)
sorted\_idx \= result.importances\_mean.argsort()
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 2, 2)

\# \`labels\` argument in boxplot is deprecated in matplotlib 3.9 and has been
\# renamed to \`tick\_labels\`. The following code handles this, but as a
\# scikit-learn user you probably can write simpler code by using \`labels=...\`
\# (matplotlib < 3.9) or \`tick\_labels=...\` (matplotlib >= 3.9).
tick\_labels\_parameter\_name \= (
    "tick\_labels"
    if parse\_version(matplotlib.\_\_version\_\_) \>= parse\_version("3.9")
    else "labels"
)
tick\_labels\_dict \= {
    tick\_labels\_parameter\_name: [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(diabetes.feature\_names)\[sorted\_idx\]
}
\# \`vert\` was deprecated in matplotlib 3.11 and is replaced by \`orientation\`,
\# which is available since matplotlib 3.10. The following code handles this, but
\# as a scikit-learn user you probably can write simpler code by using
\# \`vert=False\` (matplotlib < 3.11) or \`orientation="horizontal"\`
\# (matplotlib >= 3.10).
orientation\_dict \= (
    {"orientation": "horizontal"}
    if parse\_version(matplotlib.\_\_version\_\_) \>= parse\_version("3.10")
    else {"vert": False}
)
[plt.boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "matplotlib.pyplot.boxplot")
(result.importances\[sorted\_idx\].T, \*\*orientation\_dict, \*\*tick\_labels\_dict)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Permutation Importance (test set)")
fig.tight\_layout()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Feature Importance (MDI), Permutation Importance (test set)](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_002.png)

**Total running time of the script:** (0 minutes 1.232 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_gradient_boosting_regression.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_gradient_boosting_regression.ipynb)

[`Download Jupyter notebook: plot_gradient_boosting_regression.ipynb`](https://scikit-learn.org/stable/_downloads/c536eb92f539255e80e2b3ef5200e7a1/plot_gradient_boosting_regression.ipynb)

[`Download Python source code: plot_gradient_boosting_regression.py`](https://scikit-learn.org/stable/_downloads/e0186b37c52cdb964f7759aac5fbb9b9/plot_gradient_boosting_regression.py)

[`Download zipped: plot_gradient_boosting_regression.zip`](https://scikit-learn.org/stable/_downloads/512757d5cc898dc59c01eb79cc80a273/plot_gradient_boosting_regression.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_multicollinear_thumb.png)

[Permutation Importance with Multicollinear or Correlated Features](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html)

Permutation Importance with Multicollinear or Correlated Features

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_thumb.png)

[Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)

Permutation Importance vs Random Forest Feature Importance (MDI)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regularization_thumb.png)

[Gradient Boosting regularization](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regularization.html)

Gradient Boosting regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_importances_thumb.png)

[Feature importances with a forest of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html)

Feature importances with a forest of trees

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/e0186b37c52cdb964f7759aac5fbb9b9/plot_gradient_boosting_regression.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c536eb92f539255e80e2b3ef5200e7a1/plot_gradient_boosting_regression.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/512757d5cc898dc59c01eb79cc80a273/plot_gradient_boosting_regression.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_gradient_boosting_regression.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_gradient_boosting_regression.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)