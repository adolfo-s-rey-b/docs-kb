[Skip to main content](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/preprocessing/plot_discretization.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/preprocessing/plot_discretization.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/preprocessing/plot_discretization.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/preprocessing/plot_discretization.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/preprocessing/plot_discretization.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/preprocessing/plot_discretization.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization.html#sphx-glr-download-auto-examples-preprocessing-plot-discretization-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Using KBinsDiscretizer to discretize continuous features[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization.html#using-kbinsdiscretizer-to-discretize-continuous-features "Link to this heading")

==================================================================================================================================================================================================================================

The example compares prediction result of linear regression (linear model) and decision tree (tree based model) with and without discretization of real-valued features.

As is shown in the result before discretization, linear model is fast to build and relatively straightforward to interpret, but can only model linear relationships, while decision tree can build a much more complex model of the data. One way to make linear model more powerful on continuous data is to use discretization (also known as binning). In the example, we discretize the feature and one-hot encode the transformed data. Note that if the bins are not reasonably wide, there would appear to be a substantially increased risk of overfitting, so the discretizer parameters should usually be tuned under cross validation.

After discretization, linear regression and decision tree make exactly the same prediction. As features are constant within each bin, any model must predict the same value for all points within a bin. Compared with the result before discretization, linear model become much more flexible while decision tree gets much less flexible. Note that binning features generally has no beneficial effect for tree-based models, as these models can learn to split up the data anywhere.

![Result before discretization, Result after discretization](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear\_model import [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
from sklearn.preprocessing import [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
from sklearn.tree import [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")

\# construct the dataset
rnd \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)
X \= rnd.uniform(\-3, 3, size\=100)
y \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(X) + rnd.normal(size\=len(X)) / 3
X \= X.reshape(\-1, 1)

\# transform the dataset with KBinsDiscretizer
enc \= [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
(
    n\_bins\=10, encode\="onehot", quantile\_method\="averaged\_inverted\_cdf"
)
X\_binned \= enc.fit\_transform(X)

\# predict with original dataset
fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, sharey\=True, figsize\=(10, 4))
line \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-3, 3, 1000, endpoint\=False).reshape(\-1, 1)
reg \= [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
().fit(X, y)
ax1.plot(line, reg.predict(line), linewidth\=2, color\="green", label\="linear regression")
reg \= [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
(min\_samples\_split\=3, random\_state\=0).fit(X, y)
ax1.plot(line, reg.predict(line), linewidth\=2, color\="red", label\="decision tree")
ax1.plot(X\[:, 0\], y, "o", c\="k")
ax1.legend(loc\="best")
ax1.set\_ylabel("Regression output")
ax1.set\_xlabel("Input feature")
ax1.set\_title("Result before discretization")

\# predict with transformed dataset
line\_binned \= enc.transform(line)
reg \= [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
().fit(X\_binned, y)
ax2.plot(
    line,
    reg.predict(line\_binned),
    linewidth\=2,
    color\="green",
    linestyle\="-",
    label\="linear regression",
)
reg \= [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
(min\_samples\_split\=3, random\_state\=0).fit(X\_binned, y)
ax2.plot(
    line,
    reg.predict(line\_binned),
    linewidth\=2,
    color\="red",
    linestyle\=":",
    label\="decision tree",
)
ax2.plot(X\[:, 0\], y, "o", c\="k")
ax2.vlines(enc.bin\_edges\_\[0\], \*[plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
().get\_ylim(), linewidth\=1, alpha\=0.2)
ax2.legend(loc\="best")
ax2.set\_xlabel("Input feature")
ax2.set\_title("Result after discretization")

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.210 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo28.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/preprocessing/plot_discretization.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/preprocessing/plot_discretization.ipynb)

[`Download Jupyter notebook: plot_discretization.ipynb`](https://scikit-learn.org/stable/_downloads/c4b61c2bcffecd3661bffe3c79ef6e0b/plot_discretization.ipynb)

[`Download Python source code: plot_discretization.py`](https://scikit-learn.org/stable/_downloads/7341736ba71d0e04b4b71061cfe9b78e/plot_discretization.py)

[`Download zipped: plot_discretization.zip`](https://scikit-learn.org/stable/_downloads/2a405f4296fe09a86824e347e7ccf7e5/plot_discretization.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_strategies_thumb.png)

[Demonstrating the different strategies of KBinsDiscretizer](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_strategies.html)

Demonstrating the different strategies of KBinsDiscretizer

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bayesian_ridge_curvefit_thumb.png)

[Curve Fitting with Bayesian Ridge Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html)

Curve Fitting with Bayesian Ridge Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_thumb.png)

[Decision Tree Regression](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html)

Decision Tree Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)

[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)

Gradient Boosting regression

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/7341736ba71d0e04b4b71061cfe9b78e/plot_discretization.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c4b61c2bcffecd3661bffe3c79ef6e0b/plot_discretization.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/2a405f4296fe09a86824e347e7ccf7e5/plot_discretization.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/preprocessing/plot_discretization.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo28.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/preprocessing/plot_discretization.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)