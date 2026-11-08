[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_gradient_boosting_quantile.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_gradient_boosting_quantile.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_gradient_boosting_quantile.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_gradient_boosting_quantile.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_gradient_boosting_quantile.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_gradient_boosting_quantile.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html#sphx-glr-download-auto-examples-ensemble-plot-gradient-boosting-quantile-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Prediction Intervals for Gradient Boosting Regression[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html#prediction-intervals-for-gradient-boosting-regression "Link to this heading")

===================================================================================================================================================================================================================================

This example shows how quantile regression can be used to create prediction intervals. See [Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html#sphx-glr-auto-examples-ensemble-plot-hgbt-regression-py)
 for an example showcasing some other features of `HistGradientBoostingRegressor`.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate some data for a synthetic regression problem by applying the function f to uniformly sampled random inputs.

import numpy as np

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

def f(x):
    """The function to predict."""
    return x \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(x)

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)
X \= [np.atleast\_2d](https://numpy.org/doc/stable/reference/generated/numpy.atleast_2d.html#numpy.atleast_2d "numpy.atleast_2d")
(rng.uniform(0, 10.0, size\=1000)).T
expected\_y \= f(X).ravel()

Copy to clipboard

To make the problem interesting, we generate observations of the target y as the sum of a deterministic term computed by the function f and a random noise term that follows a centered [log-normal](https://en.wikipedia.org/wiki/Log-normal_distribution)
. To make this even more interesting we consider the case where the amplitude of the noise depends on the input variable x (heteroscedastic noise).

The lognormal distribution is non-symmetric and long tailed: observing large outliers is likely but it is impossible to observe small outliers.

sigma \= 0.5 + X.ravel() / 10
noise \= rng.lognormal(sigma\=sigma) \- [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(sigma\*\*2 / 2)
y \= expected\_y + noise

Copy to clipboard

Split into train, test datasets:

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=0)

Copy to clipboard

Fitting non-linear quantile and least squares regressors[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html#fitting-non-linear-quantile-and-least-squares-regressors "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Fit gradient boosting models trained with the quantile loss and `alpha=0.05`, `alpha=0.5`, `alpha=0.95`.

The models obtained for `alpha=0.05` and `alpha=0.95` produce a 90% coverage interval (95% - 5% = 90%).

The model trained with `alpha=0.5` produces a regression of the median: on average, there should be the same number of target observations above and below the predicted values.

from sklearn.ensemble import [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
from sklearn.metrics import [mean\_pinball\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
, [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")

all\_models \= {}
common\_params \= dict(
    learning\_rate\=0.05,
    n\_estimators\=200,
    max\_depth\=2,
    min\_samples\_leaf\=9,
    min\_samples\_split\=9,
)
for alpha in \[0.05, 0.5, 0.95\]:
    gbr \= [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
(loss\="quantile", alpha\=alpha, \*\*common\_params)
    all\_models\["q %1.2f" % alpha\] \= gbr.fit(X\_train, y\_train)

Copy to clipboard

Notice that [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 is much faster than [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
 starting with intermediate datasets (`n_samples >= 10_000`), which is not the case of the present example.

For the sake of comparison, we also fit a baseline model trained with the usual (mean) squared error (MSE).

gbr\_ls \= [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
(loss\="squared\_error", \*\*common\_params)
all\_models\["mse"\] \= gbr\_ls.fit(X\_train, y\_train)

Copy to clipboard

Create an evenly spaced evaluation set of input values spanning the \[0, 10\] range.

x\_plot \= [np.atleast\_2d](https://numpy.org/doc/stable/reference/generated/numpy.atleast_2d.html#numpy.atleast_2d "numpy.atleast_2d")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 10, 1000)).T

Copy to clipboard

Plot the true conditional mean function f, the predictions of the conditional mean (loss equals squared error), the conditional median and the conditional 90% interval (from 5th to 95th conditional percentiles).

import matplotlib.pyplot as plt

y\_pred \= all\_models\["mse"\].predict(x\_plot)
y\_lower \= all\_models\["q 0.05"\].predict(x\_plot)
y\_upper \= all\_models\["q 0.95"\].predict(x\_plot)
y\_med \= all\_models\["q 0.50"\].predict(x\_plot)

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 10))
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(x\_plot, f(x\_plot), "black", linewidth\=3, label\=r"$f(x) = x\\,\\sin(x)$")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, y\_test, "b.", markersize\=10, label\="Test observations")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(x\_plot, y\_med, "tab:orange", linewidth\=3, label\="Predicted median")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(x\_plot, y\_pred, "tab:green", linewidth\=3, label\="Predicted mean")
[plt.fill\_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between "matplotlib.pyplot.fill_between")
(
    x\_plot.ravel(), y\_lower, y\_upper, alpha\=0.4, label\="Predicted 90% interval"
)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("$x$")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("$f(x)$")
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(\-10, 25)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper left")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot gradient boosting quantile](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_quantile_001.png)

Comparing the predicted median with the predicted mean, we note that the median is on average below the mean as the noise is skewed towards high values (large outliers). The median estimate also seems to be smoother because of its natural robustness to outliers.

Also observe that the inductive bias of gradient boosting trees is unfortunately preventing our 0.05 quantile to fully capture the sinoisoidal shape of the signal, in particular around x=8. Tuning hyper-parameters can reduce this effect as shown in the last part of this notebook.

Analysis of the error metrics[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html#analysis-of-the-error-metrics "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Measure the models with [`mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
 and [`mean_pinball_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
 metrics on the training dataset.

import pandas as pd

def highlight\_min(x):
    x\_min \= x.min()
    return \["font-weight: bold" if v \== x\_min else "" for v in x\]

results \= \[\]
for name, gbr in sorted(all\_models.items()):
    metrics \= {"model": name}
    y\_pred \= gbr.predict(X\_train)
    for alpha in \[0.05, 0.5, 0.95\]:
        metrics\["pbl=%1.2f" % alpha\] \= [mean\_pinball\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
(y\_train, y\_pred, alpha\=alpha)
    metrics\["MSE"\] \= [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
(y\_train, y\_pred)
    results.append(metrics)

[pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(results).set\_index("model").style.apply(highlight\_min)

Copy to clipboard

|     | pbl=0.05 | pbl=0.50 | pbl=0.95 | MSE |
| --- | --- | --- | --- | --- |
| model |     |     |     |     |
| --- | --- | --- | --- | --- |
| mse | 0.715413 | 0.715413 | 0.715413 | 7.750348 |
| q 0.05 | 0.127128 | 1.253445 | 2.379763 | 18.933253 |
| q 0.50 | 0.305438 | 0.622811 | 0.940184 | 9.827917 |
| q 0.95 | 3.935404 | 2.158830 | 0.382257 | 28.973563 |

  
  

One column shows all models evaluated by the same metric. The minimum number on a column should be obtained when the model is trained and measured with the same metric. This should be always the case on the training set if the training converged.

Note that because the target distribution is asymmetric, the expected conditional mean and conditional median are significantly different and therefore one could not use the squared error model get a good estimation of the conditional median nor the converse.

If the target distribution were symmetric and had no outliers (e.g. with a Gaussian noise), then median estimator and the least squares estimator would have yielded similar predictions.

We then do the same on the test set.

results \= \[\]
for name, gbr in sorted(all\_models.items()):
    metrics \= {"model": name}
    y\_pred \= gbr.predict(X\_test)
    for alpha in \[0.05, 0.5, 0.95\]:
        metrics\["pbl=%1.2f" % alpha\] \= [mean\_pinball\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
(y\_test, y\_pred, alpha\=alpha)
    metrics\["MSE"\] \= [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
(y\_test, y\_pred)
    results.append(metrics)

[pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(results).set\_index("model").style.apply(highlight\_min)

Copy to clipboard

|     | pbl=0.05 | pbl=0.50 | pbl=0.95 | MSE |
| --- | --- | --- | --- | --- |
| model |     |     |     |     |
| --- | --- | --- | --- | --- |
| mse | 0.917281 | 0.767498 | 0.617715 | 6.692901 |
| q 0.05 | 0.144204 | 1.245961 | 2.347717 | 15.648026 |
| q 0.50 | 0.412021 | 0.607752 | 0.803483 | 5.874771 |
| q 0.95 | 4.388465 | 2.373210 | 0.357956 | 35.255370 |

  
  

Errors are higher meaning the models slightly overfitted the data. It still shows that the best test metric is obtained when the model is trained by minimizing this same metric.

Note that the conditional median estimator is competitive with the squared error estimator in terms of MSE on the test set: this can be explained by the fact the squared error estimator is very sensitive to large outliers which can cause significant overfitting. This can be seen on the right hand side of the previous plot. The conditional median estimator is biased (underestimation for this asymmetric noise) but is also naturally robust to outliers and overfits less.

Tuning the hyper-parameters of the quantile regressors[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html#tuning-the-hyper-parameters-of-the-quantile-regressors "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the plot above, we observed that the 5th percentile regressor seems to underfit and could not adapt to sinusoidal shape of the signal.

The hyper-parameters of the model were approximately hand-tuned for the median regressor and there is no reason that the same hyper-parameters are suitable for the 5th percentile regressor.

To confirm this hypothesis, we tune the hyper-parameters of a new regressor of the 5th percentile by selecting the best model parameters by cross-validation on the pinball loss with `alpha=0.05`:

from pprint import [pprint](https://docs.python.org/3/library/pprint.html#pprint.pprint "pprint.pprint")

from sklearn.experimental import enable\_halving\_search\_cv  \# noqa: F401
from sklearn.metrics import [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
from sklearn.model\_selection import [HalvingRandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")

param\_grid \= dict(
    learning\_rate\=\[0.05, 0.1, 0.2\],
    max\_depth\=\[2, 5, 10\],
    min\_samples\_leaf\=\[1, 5, 10, 20\],
    min\_samples\_split\=\[5, 10, 20, 30, 50\],
)
neg\_mean\_pinball\_loss\_05p\_scorer \= [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
(
    [mean\_pinball\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
,
    alpha\=0.05,
    greater\_is\_better\=False,  \# maximize the negative loss
)
gbr \= [GradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
(loss\="quantile", alpha\=0.05, random\_state\=0)
search\_05p \= [HalvingRandomSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
(
    gbr,
    param\_grid,
    resource\="n\_estimators",
    max\_resources\=250,
    min\_resources\=50,
    scoring\=neg\_mean\_pinball\_loss\_05p\_scorer,
    n\_jobs\=2,
    random\_state\=0,
).fit(X\_train, y\_train)
[pprint](https://docs.python.org/3/library/pprint.html#pprint.pprint "pprint.pprint")
(search\_05p.best\_params\_)

Copy to clipboard

{'learning\_rate': 0.2,
 'max\_depth': 2,
 'min\_samples\_leaf': 20,
 'min\_samples\_split': 10,
 'n\_estimators': 150}

Copy to clipboard

We observe that the hyper-parameters that were hand-tuned for the median regressor are in the same range as the hyper-parameters suitable for the 5th percentile regressor.

Let’s now tune the hyper-parameters for the 95th percentile regressor. We need to redefine the `scoring` metric used to select the best model, along with adjusting the `alpha` parameter of the inner gradient boosting estimator itself:

from sklearn.base import clone

neg\_mean\_pinball\_loss\_95p\_scorer \= [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
(
    [mean\_pinball\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
,
    alpha\=0.95,
    greater\_is\_better\=False,  \# maximize the negative loss
)
search\_95p \= clone(search\_05p).set\_params(
    estimator\_\_alpha\=0.95,
    scoring\=neg\_mean\_pinball\_loss\_95p\_scorer,
)
search\_95p.fit(X\_train, y\_train)
[pprint](https://docs.python.org/3/library/pprint.html#pprint.pprint "pprint.pprint")
(search\_95p.best\_params\_)

Copy to clipboard

{'learning\_rate': 0.05,
 'max\_depth': 2,
 'min\_samples\_leaf': 5,
 'min\_samples\_split': 20,
 'n\_estimators': 150}

Copy to clipboard

The result shows that the hyper-parameters for the 95th percentile regressor identified by the search procedure are roughly in the same range as the hand-tuned hyper-parameters for the median regressor and the hyper-parameters identified by the search procedure for the 5th percentile regressor. However, the hyper-parameter searches did lead to an improved 90% coverage interval that is comprised by the predictions of those two tuned quantile regressors. Note that the prediction of the upper 95th percentile has a much coarser shape than the prediction of the lower 5th percentile because of the outliers:

y\_lower\_plot \= search\_05p.predict(x\_plot)
y\_upper\_plot \= search\_95p.predict(x\_plot)

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 10))
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(x\_plot, f(x\_plot), "black", linewidth\=3, label\=r"$f(x) = x\\,\\sin(x)$")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(X\_test, y\_test, "b.", markersize\=10, label\="Test observations")
[plt.fill\_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between "matplotlib.pyplot.fill_between")
(
    x\_plot.ravel(),
    y\_lower\_plot,
    y\_upper\_plot,
    alpha\=0.4,
    label\="Predicted 90% interval",
)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("$x$")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("$f(x)$")
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(\-10, 25)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper left")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Prediction with tuned hyper-parameters")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Prediction with tuned hyper-parameters](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_quantile_002.png)

The plot looks qualitatively better than for the untuned models, especially for the shape of the of lower quantile.

Calibration of the confidence interval[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html#calibration-of-the-confidence-interval "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We can also evaluate the ability of the two extreme quantile estimators at producing well-calibrated predictions of the 90%-coverage interval (conditional on `X`), meaning that on average 90% of the observations should lie within this interval.

To do this we can compute the coverage fraction, i.e. the proportion of observations that fall within the prediction intervals:

def coverage\_fraction(y, y\_low, y\_high):
    return [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
([np.logical\_and](https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html#numpy.logical_and "numpy.logical_and")
(y \>= y\_low, y <= y\_high))

coverage\_fraction(y\_train, search\_05p.predict(X\_train), search\_95p.predict(X\_train))

Copy to clipboard

np.float64(0.9026666666666666)

Copy to clipboard

On the training set the calibration is very close to the expected coverage value of 90%.

coverage\_fraction(y\_test, search\_05p.predict(X\_test), search\_95p.predict(X\_test))

Copy to clipboard

np.float64(0.796)

Copy to clipboard

On the test set, the estimated interval is too narrow to cover 90% of the test points, but it may still hit the right coverage within reasonable statistical uncertainty. We can use [`scipy.stats.bootstrap`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html#scipy.stats.bootstrap "(in SciPy v1.18.0)")
 to measure the variability of the coverage fraction at prediction time, without retraining the models. We use a 95% confidence level for the estimated (bootstrapped) interval of coverage; this is not to be confused with the 90% coverage stemming from our 5% and 95% quantile predictions:

from scipy.stats import [bootstrap](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html#scipy.stats.bootstrap "scipy.stats.bootstrap")

train\_coverage\_bs \= [bootstrap](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html#scipy.stats.bootstrap "scipy.stats.bootstrap")
(
    (
        y\_train,
        search\_05p.predict(X\_train),
        search\_95p.predict(X\_train),
    ),
    coverage\_fraction,
    paired\=True,
    confidence\_level\=0.95,
    n\_resamples\=1000,
)
ci \= train\_coverage\_bs.confidence\_interval
print(
    f"Training-set coverage lies between {ci.low:.1%} and {ci.high:.1%}, "
    f"based on a 95% bootstrap confidence interval."
)

Copy to clipboard

Training-set coverage lies between 88.1% and 92.3%, based on a 95% bootstrap confidence interval.

Copy to clipboard

Notice that the interval contains the target value of 90% coverage.

test\_coverage\_bs \= [bootstrap](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bootstrap.html#scipy.stats.bootstrap "scipy.stats.bootstrap")
(
    (
        y\_test,
        search\_05p.predict(X\_test),
        search\_95p.predict(X\_test),
    ),
    coverage\_fraction,
    paired\=True,
    confidence\_level\=0.95,
    n\_resamples\=1000,
)
ci \= test\_coverage\_bs.confidence\_interval
print(
    f"Test-set coverage lies between {ci.low:.1%} and {ci.high:.1%}, "
    f"based on a 95% bootstrap confidence interval."
)

Copy to clipboard

Test-set coverage lies between 73.8% and 84.4%, based on a 95% bootstrap confidence interval.

Copy to clipboard

The quantile estimates from the tuned models are sadly not well-calibrated on the test set: the width of the estimated confidence interval is too narrow even when taking it’s variations into account.

**Total running time of the script:** (0 minutes 10.924 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_gradient_boosting_quantile.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_gradient_boosting_quantile.ipynb)

[`Download Jupyter notebook: plot_gradient_boosting_quantile.ipynb`](https://scikit-learn.org/stable/_downloads/b5ac5dfd67b0aab146fcb9faaac8480c/plot_gradient_boosting_quantile.ipynb)

[`Download Python source code: plot_gradient_boosting_quantile.py`](https://scikit-learn.org/stable/_downloads/2f3ef774a6d7e52e1e6b7ccbb75d25f0/plot_gradient_boosting_quantile.py)

[`Download zipped: plot_gradient_boosting_quantile.zip`](https://scikit-learn.org/stable/_downloads/2f60e3212e8896cf10a907dfe4a6a631/plot_gradient_boosting_quantile.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_quantile_regression_thumb.png)

[Quantile regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_quantile_regression.html)

Quantile regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)

[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)

Lagged features for time series forecasting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_targets_thumb.png)

[Gaussian Processes regression: basic introductory example](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html)

Gaussian Processes regression: basic introductory example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_thumb.png)

[Combine predictors using stacking](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)

Combine predictors using stacking

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/2f3ef774a6d7e52e1e6b7ccbb75d25f0/plot_gradient_boosting_quantile.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/b5ac5dfd67b0aab146fcb9faaac8480c/plot_gradient_boosting_quantile.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/2f60e3212e8896cf10a907dfe4a6a631/plot_gradient_boosting_quantile.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_gradient_boosting_quantile.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_gradient_boosting_quantile.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)