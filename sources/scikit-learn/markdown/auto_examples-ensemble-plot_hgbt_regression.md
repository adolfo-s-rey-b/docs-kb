[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_hgbt_regression.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_hgbt_regression.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_hgbt_regression.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_hgbt_regression.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_hgbt_regression.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_hgbt_regression.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html#sphx-glr-download-auto-examples-ensemble-plot-hgbt-regression-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Features in Histogram Gradient Boosting Trees[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html#features-in-histogram-gradient-boosting-trees "Link to this heading")

========================================================================================================================================================================================================

[Histogram-Based Gradient Boosting](https://scikit-learn.org/stable/modules/ensemble.html#histogram-based-gradient-boosting)
 (HGBT) models may be one of the most useful supervised learning models in scikit-learn. They are based on a modern gradient boosting implementation comparable to LightGBM and XGBoost. As such, HGBT models are more feature rich than and often outperform alternative models like random forests, especially when the number of samples is larger than some ten thousands (see [Comparing Random Forests and Histogram Gradient Boosting models](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html#sphx-glr-auto-examples-ensemble-plot-forest-hist-grad-boosting-comparison-py)
).

The top usability features of HGBT models are:

1.  Several available loss functions for mean and quantile regression tasks, see [Quantile loss](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html#quantile-support-hgbdt)
    .
    
2.  [Categorical Features Support](https://scikit-learn.org/stable/modules/ensemble.html#categorical-support-gbdt)
    , see [Categorical Feature Support in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_categorical.html#sphx-glr-auto-examples-ensemble-plot-gradient-boosting-categorical-py)
    .
    
3.  Early stopping.
    
4.  [Missing values support](https://scikit-learn.org/stable/modules/ensemble.html#nan-support-hgbt)
    , which avoids the need for an imputer.
    
5.  [Monotonic Constraints](https://scikit-learn.org/stable/modules/ensemble.html#monotonic-cst-gbdt)
    .
    
6.  [Interaction constraints](https://scikit-learn.org/stable/modules/ensemble.html#interaction-cst-hgbt)
    .
    

This example aims at showcasing all points except 2 and 6 in a real life setting.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Preparing the data[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html#preparing-the-data "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

The [electricity dataset](http://www.openml.org/d/151)
 consists of data collected from the Australian New South Wales Electricity Market. In this market, prices are not fixed and are affected by supply and demand. They are set every five minutes. Electricity transfers to/from the neighboring state of Victoria were done to alleviate fluctuations.

The dataset, originally named ELEC2, contains 45,312 instances dated from 7 May 1996 to 5 December 1998. Each sample of the dataset refers to a period of 30 minutes, i.e. there are 48 instances for each time period of one day. Each sample on the dataset has 7 columns:

*   date: between 7 May 1996 to 5 December 1998. Normalized between 0 and 1;
    
*   day: day of week (1-7);
    
*   period: half hour intervals over 24 hours. Normalized between 0 and 1;
    
*   nswprice/nswdemand: electricity price/demand of New South Wales;
    
*   vicprice/vicdemand: electricity price/demand of Victoria.
    

Originally, it is a classification task, but here we use it for the regression task to predict the scheduled electricity transfer between states.

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")

electricity \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(
    name\="electricity", version\=1, as\_frame\=True, parser\="pandas"
)
df \= electricity.frame

Copy to clipboard

This particular dataset has a stepwise constant target for the first 17,760 samples:

df\["transfer"\]\[:17\_760\].unique()

Copy to clipboard

array(\[0.414912, 0.500526\])

Copy to clipboard

Let us drop those entries and explore the hourly electricity transfer over different days of the week:

import matplotlib.pyplot as plt
import seaborn as sns

df \= electricity.frame.iloc\[17\_760:\]
X \= df.drop(columns\=\["transfer", "class"\])
y \= df\["transfer"\]

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(15, 10))
pointplot \= [sns.lineplot](https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot "seaborn.lineplot")
(x\=df\["period"\], y\=df\["transfer"\], hue\=df\["day"\], ax\=ax)
handles, labels \= ax.get\_legend\_handles\_labels()
ax.set(
    title\="Hourly energy transfer for different days of the week",
    xlabel\="Normalized time of the day",
    ylabel\="Normalized energy transfer",
)
\_ \= ax.legend(handles, \["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"\])

Copy to clipboard

![Hourly energy transfer for different days of the week](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_001.png)

Notice that energy transfer increases systematically during weekends.

Effect of number of trees and early stopping[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html#effect-of-number-of-trees-and-early-stopping "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For the sake of illustrating the effect of the (maximum) number of trees, we train a [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 over the daily electricity transfer using the whole dataset. Then we visualize its predictions depending on the `max_iter` parameter. Here we don’t try to evaluate the performance of the model and its capacity to generalize but rather its capability to learn from the training data.

from sklearn.ensemble import [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, test\_size\=0.4, shuffle\=False)

print(f"Training sample size: {X\_train.shape\[0\]}")
print(f"Test sample size: {X\_test.shape\[0\]}")
print(f"Number of features: {X\_train.shape\[1\]}")

Copy to clipboard

Training sample size: 16531
Test sample size: 11021
Number of features: 7

Copy to clipboard

max\_iter\_list \= \[5, 50\]
average\_week\_demand \= (
    df.loc\[X\_test.index\].groupby(\["day", "period"\], observed\=False)\["transfer"\].mean()
)
colors \= [sns.color\_palette](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette "seaborn.color_palette")
("colorblind")
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(10, 5))
average\_week\_demand.plot(color\=colors\[0\], label\="recorded average", linewidth\=2, ax\=ax)

for idx, max\_iter in enumerate(max\_iter\_list):
    hgbt \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(
        max\_iter\=max\_iter, categorical\_features\=None, random\_state\=42
    )
    hgbt.fit(X\_train, y\_train)

    y\_pred \= hgbt.predict(X\_test)
    prediction\_df \= df.loc\[X\_test.index\].copy()
    prediction\_df\["y\_pred"\] \= y\_pred
    average\_pred \= prediction\_df.groupby(\["day", "period"\], observed\=False)\[\
        "y\_pred"\
    \].mean()
    average\_pred.plot(
        color\=colors\[idx + 1\], label\=f"max\_iter={max\_iter}", linewidth\=2, ax\=ax
    )

ax.set(
    title\="Predicted average energy transfer during the week",
    xticks\=\[(i + 0.2) \* 48 for i in range(7)\],
    xticklabels\=\["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"\],
    xlabel\="Time of the week",
    ylabel\="Normalized energy transfer",
)
\_ \= ax.legend()

Copy to clipboard

![Predicted average energy transfer during the week](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_002.png)

With just a few iterations, HGBT models can achieve convergence (see [Comparing Random Forests and Histogram Gradient Boosting models](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html#sphx-glr-auto-examples-ensemble-plot-forest-hist-grad-boosting-comparison-py)
), meaning that adding more trees does not improve the model anymore. In the figure above, 5 iterations are not enough to get good predictions. With 50 iterations, we are already able to do a good job.

Setting `max_iter` too high might degrade the prediction quality and cost a lot of avoidable computing resources. Therefore, the HGBT implementation in scikit-learn provides an automatic **early stopping** strategy. With it, the model uses a fraction of the training data as internal validation set (`validation_fraction`) and stops training if the validation score does not improve (or degrades) after `n_iter_no_change` iterations up to a certain tolerance (`tol`).

Notice that there is a trade-off between `learning_rate` and `max_iter`: Generally, smaller learning rates are preferable but require more iterations to converge to the minimum loss, while larger learning rates converge faster (less iterations/trees needed) but at the cost of a larger minimum loss.

Because of this high correlation between the learning rate the number of iterations, a good practice is to tune the learning rate along with all (important) other hyperparameters, fit the HBGT on the training set with a large enough value for `max_iter` and determine the best `max_iter` via early stopping and some explicit `validation_fraction`.

common\_params \= {
    "max\_iter": 1\_000,
    "learning\_rate": 0.3,
    "validation\_fraction": 0.2,
    "random\_state": 42,
    "categorical\_features": None,
    "scoring": "neg\_root\_mean\_squared\_error",
}

hgbt \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(early\_stopping\=True, \*\*common\_params)
hgbt.fit(X\_train, y\_train)

\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(\-hgbt.validation\_score\_)
\_ \= ax.set(
    xlabel\="number of iterations",
    ylabel\="root mean squared error",
    title\=f"Loss of hgbt with early stopping (n\_iter={hgbt.n\_iter\_})",
)

Copy to clipboard

![Loss of hgbt with early stopping (n_iter=488)](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_003.png)

We can then overwrite the value for `max_iter` to a reasonable value and avoid the extra computational cost of the inner validation. Rounding up the number of iterations may account for variability of the training set:

import math

common\_params\["max\_iter"\] \= [math.ceil](https://docs.python.org/3/library/math.html#math.ceil "math.ceil")
(hgbt.n\_iter\_ / 100) \* 100
common\_params\["early\_stopping"\] \= False
hgbt \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(\*\*common\_params)

Copy to clipboard

Note

The inner validation done during early stopping is not optimal for time series.

Support for missing values[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html#support-for-missing-values "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

HGBT models have native support of missing values. During training, the tree grower decides where samples with missing values should go (left or right child) at each split, based on the potential gain. When predicting, these samples are sent to the learnt child accordingly. If a feature had no missing values during training, then for prediction, samples with missing values for that feature are sent to the child with the most samples (as seen during fit).

The present example shows how HGBT regressions deal with values missing completely at random (MCAR), i.e. the missingness does not depend on the observed data or the unobserved data. We can simulate such scenario by randomly replacing values from randomly selected features with `nan` values.

import numpy as np

from sklearn.metrics import [root\_mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#sklearn.metrics.root_mean_squared_error "sklearn.metrics.root_mean_squared_error")

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)
first\_week \= slice(0, 336)  \# first week in the test set as 7 \* 48 = 336
missing\_fraction\_list \= \[0, 0.01, 0.03\]

def generate\_missing\_values(X, missing\_fraction):
    total\_cells \= X.shape\[0\] \* X.shape\[1\]
    num\_missing\_cells \= int(total\_cells \* missing\_fraction)
    row\_indices \= rng.choice(X.shape\[0\], num\_missing\_cells, replace\=True)
    col\_indices \= rng.choice(X.shape\[1\], num\_missing\_cells, replace\=True)
    X\_missing \= X.copy()
    X\_missing.iloc\[row\_indices, col\_indices\] \= [np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")
    return X\_missing

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(12, 6))
ax.plot(y\_test.values\[first\_week\], label\="Actual transfer")

for missing\_fraction in missing\_fraction\_list:
    X\_train\_missing \= generate\_missing\_values(X\_train, missing\_fraction)
    X\_test\_missing \= generate\_missing\_values(X\_test, missing\_fraction)
    hgbt.fit(X\_train\_missing, y\_train)
    y\_pred \= hgbt.predict(X\_test\_missing\[first\_week\])
    rmse \= [root\_mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#sklearn.metrics.root_mean_squared_error "sklearn.metrics.root_mean_squared_error")
(y\_test\[first\_week\], y\_pred)
    ax.plot(
        y\_pred\[first\_week\],
        label\=f"missing\_fraction={missing\_fraction}, RMSE={rmse:.3f}",
        alpha\=0.5,
    )
ax.set(
    title\="Daily energy transfer predictions on data with MCAR values",
    xticks\=\[(i + 0.2) \* 48 for i in range(7)\],
    xticklabels\=\["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"\],
    xlabel\="Time of the week",
    ylabel\="Normalized energy transfer",
)
\_ \= ax.legend(loc\="lower right")

Copy to clipboard

![Daily energy transfer predictions on data with MCAR values](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_004.png)

As expected, the model degrades as the proportion of missing values increases.

Support for quantile loss[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html#support-for-quantile-loss "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

The quantile loss in regression enables a view of the variability or uncertainty of the target variable. For instance, predicting the 5th and 95th percentiles can provide a 90% prediction interval, i.e. the range within which we expect a new observed value to fall with 90% probability.

from sklearn.metrics import [mean\_pinball\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")

quantiles \= \[0.95, 0.05\]
predictions \= \[\]

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(12, 6))
ax.plot(y\_test.values\[first\_week\], label\="Actual transfer")

for quantile in quantiles:
    hgbt\_quantile \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(
        loss\="quantile", quantile\=quantile, \*\*common\_params
    )
    hgbt\_quantile.fit(X\_train, y\_train)
    y\_pred \= hgbt\_quantile.predict(X\_test\[first\_week\])

    predictions.append(y\_pred)
    score \= [mean\_pinball\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
(y\_test\[first\_week\], y\_pred)
    ax.plot(
        y\_pred\[first\_week\],
        label\=f"quantile={quantile}, pinball loss={score:.2f}",
        alpha\=0.5,
    )

ax.fill\_between(
    range(len(predictions\[0\]\[first\_week\])),
    predictions\[0\]\[first\_week\],
    predictions\[1\]\[first\_week\],
    color\=colors\[0\],
    alpha\=0.1,
)
ax.set(
    title\="Daily energy transfer predictions with quantile loss",
    xticks\=\[(i + 0.2) \* 48 for i in range(7)\],
    xticklabels\=\["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"\],
    xlabel\="Time of the week",
    ylabel\="Normalized energy transfer",
)
\_ \= ax.legend(loc\="lower right")

Copy to clipboard

![Daily energy transfer predictions with quantile loss](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_005.png)

We observe a tendency to over-estimate the energy transfer. This could be be quantitatively confirmed by computing empirical coverage numbers as done in the [calibration of confidence intervals section](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html#calibration-section)
. Keep in mind that those predicted percentiles are just estimations from a model. One can still improve the quality of such estimations by:

*   collecting more data-points;
    
*   better tuning of the model hyperparameters, see [Prediction Intervals for Gradient Boosting Regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html#sphx-glr-auto-examples-ensemble-plot-gradient-boosting-quantile-py)
    ;
    
*   engineering more predictive features from the same data, see [Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#sphx-glr-auto-examples-applications-plot-cyclical-feature-engineering-py)
    .
    

Monotonic constraints[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html#monotonic-constraints "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

Given specific domain knowledge that requires the relationship between a feature and the target to be monotonically increasing or decreasing, one can enforce such behaviour in the predictions of an HGBT model using monotonic constraints. This makes the model more interpretable and can reduce its variance (and potentially mitigate overfitting) at the risk of increasing bias. Monotonic constraints can also be used to enforce specific regulatory requirements, ensure compliance and align with ethical considerations.

In the present example, the policy of transferring energy from Victoria to New South Wales is meant to alleviate price fluctuations, meaning that the model predictions have to enforce such goal, i.e. transfer should increase with price and demand in New South Wales, but also decrease with price and demand in Victoria, in order to benefit both populations.

If the training data has feature names, it’s possible to specify the monotonic constraints by passing a dictionary with the convention:

*   1: monotonic increase
    
*   0: no constraint
    
*   \-1: monotonic decrease
    

Alternatively, one can pass an array-like object encoding the above convention by position.

from sklearn.inspection import PartialDependenceDisplay

monotonic\_cst \= {
    "date": 0,
    "day": 0,
    "period": 0,
    "nswdemand": 1,
    "nswprice": 1,
    "vicdemand": \-1,
    "vicprice": \-1,
}
hgbt\_no\_cst \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(
    categorical\_features\=None, random\_state\=42
).fit(X, y)
hgbt\_cst \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(
    monotonic\_cst\=monotonic\_cst, categorical\_features\=None, random\_state\=42
).fit(X, y)

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, figsize\=(15, 10))
disp \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    hgbt\_no\_cst,
    X,
    features\=\["nswdemand", "nswprice"\],
    line\_kw\={"linewidth": 2, "label": "unconstrained", "color": "tab:blue"},
    ax\=ax\[0\],
)
[PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    hgbt\_cst,
    X,
    features\=\["nswdemand", "nswprice"\],
    line\_kw\={"linewidth": 2, "label": "constrained", "color": "tab:orange"},
    ax\=disp.axes\_,
)
disp \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    hgbt\_no\_cst,
    X,
    features\=\["vicdemand", "vicprice"\],
    line\_kw\={"linewidth": 2, "label": "unconstrained", "color": "tab:blue"},
    ax\=ax\[1\],
)
[PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    hgbt\_cst,
    X,
    features\=\["vicdemand", "vicprice"\],
    line\_kw\={"linewidth": 2, "label": "constrained", "color": "tab:orange"},
    ax\=disp.axes\_,
)
\_ \= [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()

Copy to clipboard

![plot hgbt regression](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_006.png)

Observe that `nswdemand` and `vicdemand` seem already monotonic without constraint. This is a good example to show that the model with monotonicity constraints is “overconstraining”.

Additionally, we can verify that the predictive quality of the model is not significantly degraded by introducing the monotonic constraints. For such purpose we use [`TimeSeriesSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")
 cross-validation to estimate the variance of the test score. By doing so we guarantee that the training data does not succeed the testing data, which is crucial when dealing with data that have a temporal relationship.

from sklearn.metrics import [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
, [root\_mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#sklearn.metrics.root_mean_squared_error "sklearn.metrics.root_mean_squared_error")
from sklearn.model\_selection import [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")
, [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")

ts\_cv \= [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")
(n\_splits\=5, gap\=48, test\_size\=336)  \# a week has 336 samples
scorer \= [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
([root\_mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#sklearn.metrics.root_mean_squared_error "sklearn.metrics.root_mean_squared_error")
)

cv\_results \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(hgbt\_no\_cst, X, y, cv\=ts\_cv, scoring\=scorer)
rmse \= cv\_results\["test\_score"\]
print(f"RMSE without constraints = {rmse.mean():.3f} +/- {rmse.std():.3f}")

cv\_results \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(hgbt\_cst, X, y, cv\=ts\_cv, scoring\=scorer)
rmse \= cv\_results\["test\_score"\]
print(f"RMSE with constraints    = {rmse.mean():.3f} +/- {rmse.std():.3f}")

Copy to clipboard

RMSE without constraints = 0.109 +/- 0.037
RMSE with constraints    = 0.108 +/- 0.036

Copy to clipboard

That being said, notice the comparison is between two different models that may be optimized by a different combination of hyperparameters. That is the reason why we do no use the `common_params` in this section as done before.

**Total running time of the script:** (0 minutes 18.920 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_hgbt_regression.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_hgbt_regression.ipynb)

[`Download Jupyter notebook: plot_hgbt_regression.ipynb`](https://scikit-learn.org/stable/_downloads/cb9a8a373677fb481fe43a11d8fa0e94/plot_hgbt_regression.ipynb)

[`Download Python source code: plot_hgbt_regression.py`](https://scikit-learn.org/stable/_downloads/d108f2283ac3905eb623b32d42217a2b/plot_hgbt_regression.py)

[`Download zipped: plot_hgbt_regression.zip`](https://scikit-learn.org/stable/_downloads/ef504a3cb245a55fde178198c8218b4a/plot_hgbt_regression.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)

[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)

Lagged features for time series forecasting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_thumb.png)

[Combine predictors using stacking](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)

Combine predictors using stacking

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_monotonic_constraints_thumb.png)

[Monotonic Constraints](https://scikit-learn.org/stable/auto_examples/ensemble/plot_monotonic_constraints.html)

Monotonic Constraints

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_hist_grad_boosting_comparison_thumb.png)

[Comparing Random Forests and Histogram Gradient Boosting models](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html)

Comparing Random Forests and Histogram Gradient Boosting models

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/d108f2283ac3905eb623b32d42217a2b/plot_hgbt_regression.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/cb9a8a373677fb481fe43a11d8fa0e94/plot_hgbt_regression.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/ef504a3cb245a55fde178198c8218b4a/plot_hgbt_regression.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_hgbt_regression.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_hgbt_regression.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)