[Skip to main content](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/compose/plot_transformed_target.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/compose/plot_transformed_target.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/compose/plot_transformed_target.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/compose/plot_transformed_target.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/compose/plot_transformed_target.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/compose/plot_transformed_target.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html#sphx-glr-download-auto-examples-compose-plot-transformed-target-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Effect of transforming the targets in regression model[#](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html#effect-of-transforming-the-targets-in-regression-model "Link to this heading")

============================================================================================================================================================================================================================

In this example, we give an overview of [`TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
. We use two examples to illustrate the benefit of transforming the targets before learning a linear regression model. The first example uses synthetic data while the second example is based on the Ames housing data set.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Synthetic example[#](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html#synthetic-example "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

A synthetic random regression dataset is generated. The targets `y` are modified by:

1.  translating all targets such that all entries are non-negative (by adding the absolute value of the lowest `y`) and
    
2.  applying an exponential function to obtain non-linear targets which cannot be fitted using a simple linear model.
    

Therefore, a logarithmic (`np.log1p`) and an exponential function (`np.expm1`) will be used to transform the targets before training a linear regression model and using it for prediction.

import numpy as np

from sklearn.datasets import [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")

X, y \= [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
(n\_samples\=10\_000, noise\=100, random\_state\=0)
y \= [np.expm1](https://numpy.org/doc/stable/reference/generated/numpy.expm1.html#numpy.expm1 "numpy.expm1")
((y + abs(y.min())) / 200)
y\_trans \= [np.log1p](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#numpy.log1p "numpy.log1p")
(y)

Copy to clipboard

Below we plot the probability density functions of the target before and after applying the logarithmic functions.

import matplotlib.pyplot as plt

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

f, (ax0, ax1) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2)

ax0.hist(y, bins\=100, density\=True)
ax0.set\_xlim(\[0, 2000\])
ax0.set\_ylabel("Probability")
ax0.set\_xlabel("Target")
ax0.set\_title("Target distribution")

ax1.hist(y\_trans, bins\=100, density\=True)
ax1.set\_ylabel("Probability")
ax1.set\_xlabel("Target")
ax1.set\_title("Transformed target distribution")

f.suptitle("Synthetic data", y\=1.05)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=0)

Copy to clipboard

![Synthetic data, Target distribution, Transformed target distribution](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_001.png)

At first, a linear model will be applied on the original targets. Due to the non-linearity, the model trained will not be precise during prediction. Subsequently, a logarithmic function is used to linearize the targets, allowing better prediction even with a similar linear model as reported by the median absolute error (MedAE).

from sklearn.metrics import [median\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")
, [r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")

def compute\_score(y\_true, y\_pred):
    return {
        "R2": f"{[r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
(y\_true, y\_pred):.3f}",
        "MedAE": f"{[median\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")
(y\_true, y\_pred):.3f}",
    }

Copy to clipboard

from sklearn.compose import [TransformedTargetRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
from sklearn.linear\_model import [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
from sklearn.metrics import PredictionErrorDisplay

f, (ax0, ax1) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, sharey\=True)

ridge\_cv \= [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
().fit(X\_train, y\_train)
y\_pred\_ridge \= ridge\_cv.predict(X\_test)

ridge\_cv\_with\_trans\_target \= [TransformedTargetRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
(
    regressor\=[RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
(), func\=[np.log1p](https://numpy.org/doc/stable/reference/generated/numpy.log1p.html#numpy.log1p "numpy.log1p")
, inverse\_func\=[np.expm1](https://numpy.org/doc/stable/reference/generated/numpy.expm1.html#numpy.expm1 "numpy.expm1")
).fit(X\_train, y\_train)
y\_pred\_ridge\_with\_trans\_target \= ridge\_cv\_with\_trans\_target.predict(X\_test)

[PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")
(
    y\_test,
    y\_pred\_ridge,
    kind\="actual\_vs\_predicted",
    ax\=ax0,
    scatter\_kwargs\={"alpha": 0.5},
)
[PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")
(
    y\_test,
    y\_pred\_ridge\_with\_trans\_target,
    kind\="actual\_vs\_predicted",
    ax\=ax1,
    scatter\_kwargs\={"alpha": 0.5},
)

\# Add the score in the legend of each axis
for ax, y\_pred in zip(\[ax0, ax1\], \[y\_pred\_ridge, y\_pred\_ridge\_with\_trans\_target\]):
    for name, score in compute\_score(y\_test, y\_pred).items():
        ax.plot(\[\], \[\], " ", label\=f"{name}\={score}")
    ax.legend(loc\="upper left")

ax0.set\_title("Ridge regression \\n without target transformation")
ax1.set\_title("Ridge regression \\n with target transformation")
f.suptitle("Synthetic data", y\=1.05)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![Synthetic data, Ridge regression   without target transformation, Ridge regression   with target transformation](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_002.png)

Real-world data set[#](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html#real-world-data-set "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

In a similar manner, the Ames housing data set is used to show the impact of transforming the targets before learning a model. In this example, the target to be predicted is the selling price of each house.

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
from sklearn.preprocessing import [quantile\_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#sklearn.preprocessing.quantile_transform "sklearn.preprocessing.quantile_transform")

ames \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(name\="house\_prices", as\_frame\=True)
\# Keep only numeric columns
X \= ames.data.select\_dtypes([np.number](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.number "numpy.number")
)
\# Remove columns with NaN or Inf values
X \= X.drop(columns\=\["LotFrontage", "GarageYrBlt", "MasVnrArea"\])
\# Let the price be in k$
y \= ames.target / 1000
y\_trans \= [quantile\_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#sklearn.preprocessing.quantile_transform "sklearn.preprocessing.quantile_transform")
(
    y.to\_frame(), n\_quantiles\=900, output\_distribution\="normal", copy\=True
).squeeze()

Copy to clipboard

A [`QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
 is used to normalize the target distribution before applying a [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
 model.

f, (ax0, ax1) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2)

ax0.hist(y, bins\=100, density\=True)
ax0.set\_ylabel("Probability")
ax0.set\_xlabel("Target")
ax0.set\_title("Target distribution")

ax1.hist(y\_trans, bins\=100, density\=True)
ax1.set\_ylabel("Probability")
ax1.set\_xlabel("Target")
ax1.set\_title("Transformed target distribution")

f.suptitle("Ames housing data: selling price", y\=1.05)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![Ames housing data: selling price, Target distribution, Transformed target distribution](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_003.png)

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=1)

Copy to clipboard

The effect of the transformer is weaker than on the synthetic data. However, the transformation results in an increase in R2 and large decrease of the MedAE. The residual plot (predicted target - true target vs predicted target) without target transformation takes on a curved, ‘reverse smile’ shape due to residual values that vary depending on the value of predicted target. With target transformation, the shape is more linear indicating better model fit.

from sklearn.preprocessing import [QuantileTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")

f, (ax0, ax1) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, sharey\="row", figsize\=(6.5, 8))

ridge\_cv \= [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
().fit(X\_train, y\_train)
y\_pred\_ridge \= ridge\_cv.predict(X\_test)

ridge\_cv\_with\_trans\_target \= [TransformedTargetRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
(
    regressor\=[RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
(),
    transformer\=[QuantileTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
(n\_quantiles\=900, output\_distribution\="normal"),
).fit(X\_train, y\_train)
y\_pred\_ridge\_with\_trans\_target \= ridge\_cv\_with\_trans\_target.predict(X\_test)

\# plot the actual vs predicted values
[PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")
(
    y\_test,
    y\_pred\_ridge,
    kind\="actual\_vs\_predicted",
    ax\=ax0\[0\],
    scatter\_kwargs\={"alpha": 0.5},
)
[PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")
(
    y\_test,
    y\_pred\_ridge\_with\_trans\_target,
    kind\="actual\_vs\_predicted",
    ax\=ax0\[1\],
    scatter\_kwargs\={"alpha": 0.5},
)

\# Add the score in the legend of each axis
for ax, y\_pred in zip(\[ax0\[0\], ax0\[1\]\], \[y\_pred\_ridge, y\_pred\_ridge\_with\_trans\_target\]):
    for name, score in compute\_score(y\_test, y\_pred).items():
        ax.plot(\[\], \[\], " ", label\=f"{name}\={score}")
    ax.legend(loc\="upper left")

ax0\[0\].set\_title("Ridge regression \\n without target transformation")
ax0\[1\].set\_title("Ridge regression \\n with target transformation")

\# plot the residuals vs the predicted values
[PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")
(
    y\_test,
    y\_pred\_ridge,
    kind\="residual\_vs\_predicted",
    ax\=ax1\[0\],
    scatter\_kwargs\={"alpha": 0.5},
)
[PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")
(
    y\_test,
    y\_pred\_ridge\_with\_trans\_target,
    kind\="residual\_vs\_predicted",
    ax\=ax1\[1\],
    scatter\_kwargs\={"alpha": 0.5},
)
ax1\[0\].set\_title("Ridge regression \\n without target transformation")
ax1\[1\].set\_title("Ridge regression \\n with target transformation")

f.suptitle("Ames housing data: selling price", y\=1.05)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Ames housing data: selling price, Ridge regression   without target transformation, Ridge regression   with target transformation, Ridge regression   without target transformation, Ridge regression   with target transformation](https://scikit-learn.org/stable/_images/sphx_glr_plot_transformed_target_004.png)

**Total running time of the script:** (0 minutes 1.265 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo6.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/compose/plot_transformed_target.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo6.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/compose/plot_transformed_target.ipynb)

[`Download Jupyter notebook: plot_transformed_target.ipynb`](https://scikit-learn.org/stable/_downloads/ea57d7ab1588de8f5bd1afc68f20de2f/plot_transformed_target.ipynb)

[`Download Python source code: plot_transformed_target.py`](https://scikit-learn.org/stable/_downloads/93d55b9dcb06fda6f82b4d16c9a3a70d/plot_transformed_target.py)

[`Download zipped: plot_transformed_target.zip`](https://scikit-learn.org/stable/_downloads/47511aeb2706f3183261493a52ece97b/plot_transformed_target.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_isotonic_regression_thumb.png)

[Isotonic Regression](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_isotonic_regression.html)

Isotonic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_pipe_thumb.png)

[Pipelining: chaining a PCA and a logistic regression](https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html)

Pipelining: chaining a PCA and a logistic regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_predict_thumb.png)

[Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html)

Plotting Cross-Validated Predictions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_thumb.png)

[Using KBinsDiscretizer to discretize continuous features](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization.html)

Using KBinsDiscretizer to discretize continuous features

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/93d55b9dcb06fda6f82b4d16c9a3a70d/plot_transformed_target.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/ea57d7ab1588de8f5bd1afc68f20de2f/plot_transformed_target.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/47511aeb2706f3183261493a52ece97b/plot_transformed_target.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo6.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/compose/plot_transformed_target.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo6.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/compose/plot_transformed_target.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)