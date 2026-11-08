[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_adaboost_regression.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_adaboost_regression.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_adaboost_regression.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_adaboost_regression.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_adaboost_regression.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_adaboost_regression.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html#sphx-glr-download-auto-examples-ensemble-plot-adaboost-regression-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Decision Tree Regression with AdaBoost[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html#decision-tree-regression-with-adaboost "Link to this heading")

==============================================================================================================================================================================================

A decision tree is boosted using the AdaBoost.R2 [\[1\]](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html#id2)
 algorithm on a 1D sinusoidal dataset with a small amount of Gaussian noise. 299 boosts (300 decision trees) is compared with a single decision tree regressor. As the number of boosts is increased the regressor can fit more detail.

See [Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html#sphx-glr-auto-examples-ensemble-plot-hgbt-regression-py)
 for an example showcasing the benefits of using more efficient regression models such as `HistGradientBoostingRegressor`.

Preparing the data[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html#preparing-the-data "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

First, we prepare dummy data with a sinusoidal relationship and some gaussian noise.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import numpy as np

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(1)
X \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 6, 100)\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
y \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(X).ravel() + [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(6 \* X).ravel() + rng.normal(0, 0.1, X.shape\[0\])

Copy to clipboard

Training and prediction with DecisionTree and AdaBoost Regressors[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html#training-and-prediction-with-decisiontree-and-adaboost-regressors "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now, we define the classifiers and fit them to the data. Then we predict on that same data to see how well they could fit it. The first regressor is a `DecisionTreeRegressor` with `max_depth=4`. The second regressor is an `AdaBoostRegressor` with a `DecisionTreeRegressor` of `max_depth=4` as base learner and will be built with `n_estimators=300` of those base learners.

from sklearn.ensemble import [AdaBoostRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
from sklearn.tree import [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")

regr\_1 \= [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
(max\_depth\=4)

regr\_2 \= [AdaBoostRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")
(
    [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
(max\_depth\=4), n\_estimators\=300, random\_state\=rng
)

regr\_1.fit(X, y)
regr\_2.fit(X, y)

y\_1 \= regr\_1.predict(X)
y\_2 \= regr\_2.predict(X)

Copy to clipboard

Plotting the results[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html#plotting-the-results "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

Finally, we plot how well our two regressors, single decision tree regressor and AdaBoost regressor, could fit the data.

import matplotlib.pyplot as plt
import seaborn as sns

colors \= [sns.color\_palette](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
("colorblind")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X, y, color\=colors\[0\], label\="training samples")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y\_1, color\=colors\[1\], label\="n\_estimators=1", linewidth\=2)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y\_2, color\=colors\[2\], label\="n\_estimators=300", linewidth\=2)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("data")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("target")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Boosted Decision Tree Regression")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Boosted Decision Tree Regression](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_regression_001.png)

**Total running time of the script:** (0 minutes 0.523 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_adaboost_regression.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_adaboost_regression.ipynb)

[`Download Jupyter notebook: plot_adaboost_regression.ipynb`](https://scikit-learn.org/stable/_downloads/38e826c9e3778d7de78b2fc671fd7903/plot_adaboost_regression.ipynb)

[`Download Python source code: plot_adaboost_regression.py`](https://scikit-learn.org/stable/_downloads/2da78c80da33b4e0d313b0a90b923ec8/plot_adaboost_regression.py)

[`Download zipped: plot_adaboost_regression.zip`](https://scikit-learn.org/stable/_downloads/72de0e9b7e7a5e07ea3b341b61af5277/plot_adaboost_regression.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_thumb.png)

[Decision Tree Regression](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)

Decision Tree Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_iris_thumb.png)

[Plot the decision surfaces of ensembles of trees on the iris dataset](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html)

Plot the decision surfaces of ensembles of trees on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_thumb.png)

[Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)

Feature transformations with ensembles of trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_regressor_thumb.png)

[Plot individual and voting regression predictions](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_regressor.html)

Plot individual and voting regression predictions

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/2da78c80da33b4e0d313b0a90b923ec8/plot_adaboost_regression.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/38e826c9e3778d7de78b2fc671fd7903/plot_adaboost_regression.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/72de0e9b7e7a5e07ea3b341b61af5277/plot_adaboost_regression.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_adaboost_regression.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_adaboost_regression.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)