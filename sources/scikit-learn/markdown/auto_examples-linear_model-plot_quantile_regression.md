[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_quantile_regression.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_quantile_regression.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_quantile_regression.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_quantile_regression.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_quantile_regression.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_quantile_regression.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_quantile_regression.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_quantile_regression.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_quantile_regression.html#sphx-glr-download-auto-examples-linear-model-plot-quantile-regression-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Quantile regression[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_quantile_regression.html#quantile-regression "Link to this heading")

============================================================================================================================================================

This example illustrates how quantile regression can predict non-trivial conditional quantiles.

The left figure shows the case when the error distribution is normal, but has non-constant variance, i.e. with heteroscedasticity.

The right figure shows an example of an asymmetric error distribution, namely the Pareto distribution.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Dataset generation[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_quantile_regression.html#dataset-generation "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

To illustrate the behaviour of quantile regression, we will generate two synthetic datasets. The true generative random processes for both datasets will be composed by the same expected value with a linear relationship with a single feature `x`.

import numpy as np

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)
x \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(start\=0, stop\=10, num\=100)
X \= x\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
y\_true\_mean \= 10 + 0.5 \* x

Copy to clipboard

We will create two subsequent problems by changing the distribution of the target `y` while keeping the same expected value:

*   in the first case, a heteroscedastic Normal noise is added;
    
*   in the second case, an asymmetric Pareto noise is added.
    

y\_normal \= y\_true\_mean + rng.normal(loc\=0, scale\=0.5 + 0.5 \* x, size\=x.shape\[0\])
a \= 5
y\_pareto \= y\_true\_mean + 10 \* (rng.pareto(a, size\=x.shape\[0\]) \- 1 / (a \- 1))

Copy to clipboard

Let’s first visualize the datasets as well as the distribution of the residuals `y - mean(y)`.

import matplotlib.pyplot as plt

\_, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=2, figsize\=(15, 11), sharex\="row", sharey\="row")

axs\[0, 0\].plot(x, y\_true\_mean, label\="True mean")
axs\[0, 0\].scatter(x, y\_normal, color\="black", alpha\=0.5, label\="Observations")
axs\[1, 0\].hist(y\_true\_mean \- y\_normal, edgecolor\="black")

axs\[0, 1\].plot(x, y\_true\_mean, label\="True mean")
axs\[0, 1\].scatter(x, y\_pareto, color\="black", alpha\=0.5, label\="Observations")
axs\[1, 1\].hist(y\_true\_mean \- y\_pareto, edgecolor\="black")

axs\[0, 0\].set\_title("Dataset with heteroscedastic Normal distributed targets")
axs\[0, 1\].set\_title("Dataset with asymmetric Pareto distributed target")
axs\[1, 0\].set\_title(
    "Residuals distribution for heteroscedastic Normal distributed targets"
)
axs\[1, 1\].set\_title("Residuals distribution for asymmetric Pareto distributed target")
axs\[0, 0\].legend()
axs\[0, 1\].legend()
axs\[0, 0\].set\_ylabel("y")
axs\[1, 0\].set\_ylabel("Counts")
axs\[0, 1\].set\_xlabel("x")
axs\[0, 0\].set\_xlabel("x")
axs\[1, 0\].set\_xlabel("Residuals")
\_ \= axs\[1, 1\].set\_xlabel("Residuals")

Copy to clipboard

![Dataset with heteroscedastic Normal distributed targets, Dataset with asymmetric Pareto distributed target, Residuals distribution for heteroscedastic Normal distributed targets, Residuals distribution for asymmetric Pareto distributed target](https://scikit-learn.org/stable/_images/sphx_glr_plot_quantile_regression_001.png)

With the heteroscedastic Normal distributed target, we observe that the variance of the noise is increasing when the value of the feature `x` is increasing.

With the asymmetric Pareto distributed target, we observe that the positive residuals are bounded.

These types of noisy targets make the estimation via [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
 less efficient, i.e. we need more data to get stable results and, in addition, large outliers can have a huge impact on the fitted coefficients. (Stated otherwise: in a setting with constant variance, ordinary least squares estimators converge much faster to the _true_ coefficients with increasing sample size.)

In this asymmetric setting, the median or different quantiles give additional insights. On top of that, median estimation is much more robust to outliers and heavy tailed distributions. But note that extreme quantiles are estimated by very few data points. 95% quantile are more or less estimated by the 5% largest values and thus also a bit sensitive outliers.

In the remainder of this tutorial, we will show how [`QuantileRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
 can be used in practice and give the intuition into the properties of the fitted models. Finally, we will compare the both [`QuantileRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
 and [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
.

Fitting a `QuantileRegressor`[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_quantile_regression.html#fitting-a-quantileregressor "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section, we want to estimate the conditional median as well as a low and high quantile fixed at 5% and 95%, respectively. Thus, we will get three linear models, one for each quantile.

We will use the quantiles at 5% and 95% to find the outliers in the training sample beyond the central 90% interval.

from sklearn.linear\_model import [QuantileRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")

quantiles \= \[0.05, 0.5, 0.95\]
predictions \= {}
out\_bounds\_predictions \= [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
(y\_true\_mean, dtype\=[np.bool\_](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool_ "numpy.bool_")
)
for quantile in quantiles:
    qr \= [QuantileRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
(quantile\=quantile, alpha\=0)
    y\_pred \= qr.fit(X, y\_normal).predict(X)
    predictions\[quantile\] \= y\_pred

    if quantile \== min(quantiles):
        out\_bounds\_predictions \= [np.logical\_or](https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html#numpy.logical_or "numpy.logical_or")
(
            out\_bounds\_predictions, y\_pred \>= y\_normal
        )
    elif quantile \== max(quantiles):
        out\_bounds\_predictions \= [np.logical\_or](https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html#numpy.logical_or "numpy.logical_or")
(
            out\_bounds\_predictions, y\_pred <= y\_normal
        )

Copy to clipboard

Now, we can plot the three linear models and the distinguished samples that are within the central 90% interval from samples that are outside this interval.

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y\_true\_mean, color\="black", linestyle\="dashed", label\="True mean")

for quantile, y\_pred in predictions.items():
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y\_pred, label\=f"Quantile: {quantile}")

[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    x\[out\_bounds\_predictions\],
    y\_normal\[out\_bounds\_predictions\],
    color\="black",
    marker\="+",
    alpha\=0.5,
    label\="Outside interval",
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    x\[~out\_bounds\_predictions\],
    y\_normal\[~out\_bounds\_predictions\],
    color\="black",
    alpha\=0.5,
    label\="Inside interval",
)

[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("x")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("y")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Quantiles of heteroscedastic Normal distributed target")

Copy to clipboard

![Quantiles of heteroscedastic Normal distributed target](https://scikit-learn.org/stable/_images/sphx_glr_plot_quantile_regression_002.png)

Since the noise is still Normally distributed, in particular is symmetric, the true conditional mean and the true conditional median coincide. Indeed, we see that the estimated median almost hits the true mean. We observe the effect of having an increasing noise variance on the 5% and 95% quantiles: the slopes of those quantiles are very different and the interval between them becomes wider with increasing `x`.

To get an additional intuition regarding the meaning of the 5% and 95% quantiles estimators, one can count the number of samples above and below the predicted quantiles (represented by a cross on the above plot), considering that we have a total of 100 samples.

We can repeat the same experiment using the asymmetric Pareto distributed target.

quantiles \= \[0.05, 0.5, 0.95\]
predictions \= {}
out\_bounds\_predictions \= [np.zeros\_like](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
(y\_true\_mean, dtype\=[np.bool\_](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool_ "numpy.bool_")
)
for quantile in quantiles:
    qr \= [QuantileRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
(quantile\=quantile, alpha\=0)
    y\_pred \= qr.fit(X, y\_pareto).predict(X)
    predictions\[quantile\] \= y\_pred

    if quantile \== min(quantiles):
        out\_bounds\_predictions \= [np.logical\_or](https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html#numpy.logical_or "numpy.logical_or")
(
            out\_bounds\_predictions, y\_pred \>= y\_pareto
        )
    elif quantile \== max(quantiles):
        out\_bounds\_predictions \= [np.logical\_or](https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html#numpy.logical_or "numpy.logical_or")
(
            out\_bounds\_predictions, y\_pred <= y\_pareto
        )

Copy to clipboard

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y\_true\_mean, color\="black", linestyle\="dashed", label\="True mean")

for quantile, y\_pred in predictions.items():
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X, y\_pred, label\=f"Quantile: {quantile}")

[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    x\[out\_bounds\_predictions\],
    y\_pareto\[out\_bounds\_predictions\],
    color\="black",
    marker\="+",
    alpha\=0.5,
    label\="Outside interval",
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    x\[~out\_bounds\_predictions\],
    y\_pareto\[~out\_bounds\_predictions\],
    color\="black",
    alpha\=0.5,
    label\="Inside interval",
)

[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("x")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("y")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Quantiles of asymmetric Pareto distributed target")

Copy to clipboard

![Quantiles of asymmetric Pareto distributed target](https://scikit-learn.org/stable/_images/sphx_glr_plot_quantile_regression_003.png)

Due to the asymmetry of the distribution of the noise, we observe that the true mean and estimated conditional median are different. We also observe that each quantile model has different parameters to better fit the desired quantile. Note that ideally, all quantiles would be parallel in this case, which would become more visible with more data points or less extreme quantiles, e.g. 10% and 90%.

Comparing `QuantileRegressor` and `LinearRegression`[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_quantile_regression.html#comparing-quantileregressor-and-linearregression "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section, we will linger on the difference regarding the loss functions that [`QuantileRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
 and [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
 are minimizing.

Indeed, [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
 is a least squares approach minimizing the mean squared error (MSE) between the training and predicted targets. In contrast, [`QuantileRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
 with `quantile=0.5` minimizes the mean absolute error (MAE) instead.

Why does it matter? The loss functions specify what exactly the model is aiming to predict, see [user guide on the choice of scoring function](https://scikit-learn.org/stable/modules/model_evaluation.html#which-scoring-function)
. In short, a model minimizing MSE predicts the mean (expectation) and a model minimizing MAE predicts the median.

Let’s compute the training errors of such models in terms of mean squared error and mean absolute error. We will use the asymmetric Pareto distributed target to make it more interesting as mean and median are not equal.

from sklearn.linear\_model import [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
from sklearn.metrics import [mean\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
, [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")

linear\_regression \= [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
()
quantile\_regression \= [QuantileRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
(quantile\=0.5, alpha\=0)

y\_pred\_lr \= linear\_regression.fit(X, y\_pareto).predict(X)
y\_pred\_qr \= quantile\_regression.fit(X, y\_pareto).predict(X)

print(
    "Training error (in-sample performance)\\n"
    f"{'model':<20}   MAE   MSE\\n"
    f"{linear\_regression.\_\_class\_\_.\_\_name\_\_:<20} "
    f"{[mean\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
(y\_pareto, y\_pred\_lr):5.3f} "
    f"{[mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
(y\_pareto, y\_pred\_lr):5.3f}\\n"
    f"{quantile\_regression.\_\_class\_\_.\_\_name\_\_:<20} "
    f"{[mean\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
(y\_pareto, y\_pred\_qr):5.3f} "
    f"{[mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
(y\_pareto, y\_pred\_qr):5.3f}"
)

Copy to clipboard

Training error (in-sample performance)
model                  MAE   MSE
LinearRegression     1.805 6.486
QuantileRegressor    1.670 7.025

Copy to clipboard

On the training set, we see that MAE is lower for [`QuantileRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
 than [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
. In contrast to that, MSE is lower for [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
 than [`QuantileRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
. These results confirms that MAE is the loss minimized by [`QuantileRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor")
 while MSE is the loss minimized [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
.

We can make a similar evaluation by looking at the test error obtained by cross-validation.

from sklearn.model\_selection import [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")

cv\_results\_lr \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(
    linear\_regression,
    X,
    y\_pareto,
    cv\=3,
    scoring\=\["neg\_mean\_absolute\_error", "neg\_mean\_squared\_error"\],
)
cv\_results\_qr \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(
    quantile\_regression,
    X,
    y\_pareto,
    cv\=3,
    scoring\=\["neg\_mean\_absolute\_error", "neg\_mean\_squared\_error"\],
)
print(
    "Test error (cross-validated performance)\\n"
    f"{'model':<20}   MAE   MSE\\n"
    f"{linear\_regression.\_\_class\_\_.\_\_name\_\_:<20} "
    f"{\-cv\_results\_lr\['test\_neg\_mean\_absolute\_error'\].mean():5.3f} "
    f"{\-cv\_results\_lr\['test\_neg\_mean\_squared\_error'\].mean():5.3f}\\n"
    f"{quantile\_regression.\_\_class\_\_.\_\_name\_\_:<20} "
    f"{\-cv\_results\_qr\['test\_neg\_mean\_absolute\_error'\].mean():5.3f} "
    f"{\-cv\_results\_qr\['test\_neg\_mean\_squared\_error'\].mean():5.3f}"
)

Copy to clipboard

Test error (cross-validated performance)
model                  MAE   MSE
LinearRegression     1.732 6.690
QuantileRegressor    1.679 7.129

Copy to clipboard

We reach similar conclusions on the out-of-sample evaluation.

**Total running time of the script:** (0 minutes 0.568 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_quantile_regression.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_quantile_regression.ipynb)

[`Download Jupyter notebook: plot_quantile_regression.ipynb`](https://scikit-learn.org/stable/_downloads/10754505339af88c10b8a48127535a4a/plot_quantile_regression.ipynb)

[`Download Python source code: plot_quantile_regression.py`](https://scikit-learn.org/stable/_downloads/8a712694e4d011e8f35bfcb1b1b5fc82/plot_quantile_regression.py)

[`Download zipped: plot_quantile_regression.zip`](https://scikit-learn.org/stable/_downloads/fe37211a08cbe6f8ecd8d5469e297219/plot_quantile_regression.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_quantile_thumb.png)

[Prediction Intervals for Gradient Boosting Regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html)

Prediction Intervals for Gradient Boosting Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_1_0_thumb.png)

[Release Highlights for scikit-learn 1.1](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)

Release Highlights for scikit-learn 1.1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)

[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)

Lagged features for time series forecasting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_predict_thumb.png)

[Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html)

Plotting Cross-Validated Predictions

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/8a712694e4d011e8f35bfcb1b1b5fc82/plot_quantile_regression.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/10754505339af88c10b8a48127535a4a/plot_quantile_regression.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/fe37211a08cbe6f8ecd8d5469e297219/plot_quantile_regression.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_quantile_regression.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_quantile_regression.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)