[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_regression_multioutput.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_random_forest_regression_multioutput.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_regression_multioutput.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_random_forest_regression_multioutput.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_random_forest_regression_multioutput.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_random_forest_regression_multioutput.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_random_forest_regression_multioutput.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_random_forest_regression_multioutput.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_regression_multioutput.html#sphx-glr-download-auto-examples-ensemble-plot-random-forest-regression-multioutput-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparing random forests and the multi-output meta estimator[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_regression_multioutput.html#comparing-random-forests-and-the-multi-output-meta-estimator "Link to this heading")

===========================================================================================================================================================================================================================================================

An example to compare multi-output regression with random forest and the [multioutput.MultiOutputRegressor](https://scikit-learn.org/stable/modules/multiclass.html#multiclass)
 meta-estimator.

This example illustrates the use of the [multioutput.MultiOutputRegressor](https://scikit-learn.org/stable/modules/multiclass.html#multiclass)
 meta-estimator to perform multi-output regression. A random forest regressor is used, which supports multi-output regression natively, so the results can be compared.

The random forest regressor will only ever predict values within the range of observations or closer to zero for each of the targets. As a result the predictions are biased towards the centre of the circle.

Using a single underlying feature the model learns both the x and y coordinate as output.

![Comparing random forests and the multi-output meta estimator](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_forest_regression_multioutput_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.ensemble import [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.multioutput import [MultiOutputRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")

\# Create a random dataset
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(1)
X \= [np.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
(200 \* rng.rand(600, 1) \- 100, axis\=0)
y \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[[np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")\
 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")\
(X).ravel(), [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")\
 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")\
(X).ravel()\]).T
y += 0.5 \- rng.rand(\*y.shape)

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, train\_size\=400, test\_size\=200, random\_state\=4
)

max\_depth \= 30
regr\_multirf \= [MultiOutputRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")
(
    [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
(n\_estimators\=100, max\_depth\=max\_depth, random\_state\=0)
)
regr\_multirf.fit(X\_train, y\_train)

regr\_rf \= [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
(n\_estimators\=100, max\_depth\=max\_depth, random\_state\=2)
regr\_rf.fit(X\_train, y\_train)

\# Predict on new data
y\_multirf \= regr\_multirf.predict(X\_test)
y\_rf \= regr\_rf.predict(X\_test)

\# Plot the results
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
s \= 50
a \= 0.4
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    y\_test\[:, 0\],
    y\_test\[:, 1\],
    edgecolor\="k",
    c\="navy",
    s\=s,
    marker\="s",
    alpha\=a,
    label\="Data",
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    y\_multirf\[:, 0\],
    y\_multirf\[:, 1\],
    edgecolor\="k",
    c\="cornflowerblue",
    s\=s,
    alpha\=a,
    label\="Multi RF score=%.2f" % regr\_multirf.score(X\_test, y\_test),
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    y\_rf\[:, 0\],
    y\_rf\[:, 1\],
    edgecolor\="k",
    c\="c",
    s\=s,
    marker\="^",
    alpha\=a,
    label\="RF score=%.2f" % regr\_rf.score(X\_test, y\_test),
)
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(\[\-6, 6\])
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(\[\-6, 6\])
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("target 1")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("target 2")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Comparing random forests and the multi-output meta estimator")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.550 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_random_forest_regression_multioutput.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_random_forest_regression_multioutput.ipynb)

[`Download Jupyter notebook: plot_random_forest_regression_multioutput.ipynb`](https://scikit-learn.org/stable/_downloads/11cbd2b41092ecf5ba8083dfb7bae25a/plot_random_forest_regression_multioutput.ipynb)

[`Download Python source code: plot_random_forest_regression_multioutput.py`](https://scikit-learn.org/stable/_downloads/d54072eca33dc111fb8f7a73aedcb488/plot_random_forest_regression_multioutput.py)

[`Download zipped: plot_random_forest_regression_multioutput.zip`](https://scikit-learn.org/stable/_downloads/9db681d93e93ba2254d53b5f5a4403f1/plot_random_forest_regression_multioutput.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_thumb.png)

[Decision Tree Regression](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)

Decision Tree Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_thumb.png)

[Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)

Feature transformations with ensembles of trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_regression_thumb.png)

[Decision Tree Regression with AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html)

Decision Tree Regression with AdaBoost

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_regressor_thumb.png)

[Plot individual and voting regression predictions](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_regressor.html)

Plot individual and voting regression predictions

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/d54072eca33dc111fb8f7a73aedcb488/plot_random_forest_regression_multioutput.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/11cbd2b41092ecf5ba8083dfb7bae25a/plot_random_forest_regression_multioutput.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/9db681d93e93ba2254d53b5f5a4403f1/plot_random_forest_regression_multioutput.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_random_forest_regression_multioutput.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_random_forest_regression_multioutput.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)