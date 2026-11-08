[Skip to main content](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/applications/plot_time_series_lagged_features.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/applications/plot_time_series_lagged_features.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/applications/plot_time_series_lagged_features.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/applications/plot_time_series_lagged_features.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/applications/plot_time_series_lagged_features.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/applications/plot_time_series_lagged_features.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html#sphx-glr-download-auto-examples-applications-plot-time-series-lagged-features-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Lagged features for time series forecasting[#](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html#lagged-features-for-time-series-forecasting "Link to this heading")

====================================================================================================================================================================================================================

This example demonstrates how Polars-engineered lagged features can be used for time series forecasting with [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 on the Bike Sharing Demand dataset.

See the example on [Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#sphx-glr-auto-examples-applications-plot-cyclical-feature-engineering-py)
 for some data exploration on this dataset and a demo on periodic feature engineering.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Analyzing the Bike Sharing Demand dataset[#](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html#analyzing-the-bike-sharing-demand-dataset "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We start by loading the data from the OpenML repository as a raw parquet file to illustrate how to work with an arbitrary parquet file instead of hiding this step in a convenience tool such as `sklearn.datasets.fetch_openml`.

The URL of the parquet file can be found in the JSON description of the Bike Sharing Demand dataset with id 44063 on openml.org ([https://openml.org/search?type=data&status=active&id=44063](https://openml.org/search?type=data&status=active&id=44063)
).

The `sha256` hash of the file is also provided to ensure the integrity of the downloaded file.

import numpy as np
import polars as pl

from sklearn.datasets import [fetch\_file](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html#sklearn.datasets.fetch_file "sklearn.datasets.fetch_file")

pl.Config.set\_fmt\_str\_lengths(20)

bike\_sharing\_data\_file \= [fetch\_file](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html#sklearn.datasets.fetch_file "sklearn.datasets.fetch_file")
(
    "https://data.openml.org/datasets/0004/44063/dataset\_44063.pq",
    sha256\="d120af76829af0d256338dc6dd4be5df4fd1f35bf3a283cab66a51c1c6abd06a",
)
bike\_sharing\_data\_file

Copy to clipboard

PosixPath('/home/circleci/scikit\_learn\_data/data.openml.org/datasets\_0004\_44063/dataset\_44063.pq')

Copy to clipboard

We load the parquet file with Polars for feature engineering. Polars automatically caches common subexpressions which are reused in multiple expressions (like `pl.col("count").shift(1)` below). See [https://docs.pola.rs/user-guide/lazy/optimizations/](https://docs.pola.rs/user-guide/lazy/optimizations/)
 for more information.

df \= pl.read\_parquet(bike\_sharing\_data\_file)

Copy to clipboard

Next, we take a look at the statistical summary of the dataset so that we can better understand the data that we are working with.

import polars.selectors as cs

summary \= df.select(cs.numeric()).describe()
summary

Copy to clipboard

shape: (9, 8)

| statistic | month | hour | temp | feel\_temp | humidity | windspeed | count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| str | f64 | f64 | f64 | f64 | f64 | f64 | f64 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "count" | 17379.0 | 17379.0 | 17379.0 | 17379.0 | 17379.0 | 17379.0 | 17379.0 |
| "null\_count" | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| "mean" | 6.537775 | 11.546752 | 20.376474 | 23.788755 | 0.627229 | 12.73654 | 189.463088 |
| "std" | 3.438776 | 6.914405 | 7.894801 | 8.592511 | 0.19293 | 8.196795 | 181.387599 |
| "min" | 1.0 | 0.0 | 0.82 | 0.0 | 0.0 | 0.0 | 1.0 |
| "25%" | 4.0 | 6.0 | 13.94 | 16.665 | 0.48 | 7.0015 | 40.0 |
| "50%" | 7.0 | 12.0 | 20.5 | 24.24 | 0.63 | 12.998 | 142.0 |
| "75%" | 10.0 | 18.0 | 27.06 | 31.06 | 0.78 | 16.9979 | 281.0 |
| "max" | 12.0 | 23.0 | 41.0 | 50.0 | 1.0 | 56.9969 | 977.0 |

  
  

Let us look at the count of the seasons `"fall"`, `"spring"`, `"summer"` and `"winter"` present in the dataset to confirm they are balanced.

import matplotlib.pyplot as plt

df\["season"\].value\_counts()

Copy to clipboard

shape: (4, 2)

| season | count |
| --- | --- |
| cat | u32 |
| --- | --- |
| "3" | 4232 |
| "0" | 4496 |
| "1" | 4242 |
| "2" | 4409 |

  
  

Generating Polars-engineered lagged features[#](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html#generating-polars-engineered-lagged-features "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s consider the problem of predicting the demand at the next hour given past demands. Since the demand is a continuous variable, one could intuitively use any regression model. However, we do not have the usual `(X_train, y_train)` dataset. Instead, we just have the `y_train` demand data sequentially organized by time.

lagged\_df \= df.select(
    "count",
    \*\[pl.col("count").shift(i).alias(f"lagged\_count\_{i}h") for i in \[1, 2, 3\]\],
    lagged\_count\_1d\=pl.col("count").shift(24),
    lagged\_count\_1d\_1h\=pl.col("count").shift(24 + 1),
    lagged\_count\_7d\=pl.col("count").shift(7 \* 24),
    lagged\_count\_7d\_1h\=pl.col("count").shift(7 \* 24 + 1),
    lagged\_mean\_24h\=pl.col("count").shift(1).rolling\_mean(24),
    lagged\_max\_24h\=pl.col("count").shift(1).rolling\_max(24),
    lagged\_min\_24h\=pl.col("count").shift(1).rolling\_min(24),
    lagged\_mean\_7d\=pl.col("count").shift(1).rolling\_mean(7 \* 24),
    lagged\_max\_7d\=pl.col("count").shift(1).rolling\_max(7 \* 24),
    lagged\_min\_7d\=pl.col("count").shift(1).rolling\_min(7 \* 24),
)
lagged\_df.tail(10)

Copy to clipboard

shape: (10, 14)

| count | lagged\_count\_1h | lagged\_count\_2h | lagged\_count\_3h | lagged\_count\_1d | lagged\_count\_1d\_1h | lagged\_count\_7d | lagged\_count\_7d\_1h | lagged\_mean\_24h | lagged\_max\_24h | lagged\_min\_24h | lagged\_mean\_7d | lagged\_max\_7d | lagged\_min\_7d |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| i64 | i64 | i64 | i64 | i64 | i64 | i64 | i64 | f64 | i64 | i64 | f64 | i64 | i64 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 247 | 203 | 224 | 157 | 160 | 169 | 70  | 135 | 93.5 | 224 | 1   | 67.732143 | 271 | 1   |
| 315 | 247 | 203 | 224 | 138 | 160 | 46  | 70  | 97.125 | 247 | 1   | 68.785714 | 271 | 1   |
| 214 | 315 | 247 | 203 | 133 | 138 | 33  | 46  | 104.5 | 315 | 1   | 70.386905 | 315 | 1   |
| 164 | 214 | 315 | 247 | 123 | 133 | 33  | 33  | 107.875 | 315 | 1   | 71.464286 | 315 | 1   |
| 122 | 164 | 214 | 315 | 125 | 123 | 26  | 33  | 109.583333 | 315 | 1   | 72.244048 | 315 | 1   |
| 119 | 122 | 164 | 214 | 102 | 125 | 26  | 26  | 109.458333 | 315 | 1   | 72.815476 | 315 | 1   |
| 89  | 119 | 122 | 164 | 72  | 102 | 18  | 26  | 110.166667 | 315 | 1   | 73.369048 | 315 | 1   |
| 90  | 89  | 119 | 122 | 47  | 72  | 23  | 18  | 110.875 | 315 | 1   | 73.791667 | 315 | 1   |
| 61  | 90  | 89  | 119 | 36  | 47  | 22  | 23  | 112.666667 | 315 | 1   | 74.190476 | 315 | 1   |
| 49  | 61  | 90  | 89  | 49  | 36  | 12  | 22  | 113.708333 | 315 | 1   | 74.422619 | 315 | 1   |

  
  

Watch out however, the first lines have undefined values because their own past is unknown. This depends on how much lag we used:

lagged\_df.head(10)

Copy to clipboard

shape: (10, 14)

| count | lagged\_count\_1h | lagged\_count\_2h | lagged\_count\_3h | lagged\_count\_1d | lagged\_count\_1d\_1h | lagged\_count\_7d | lagged\_count\_7d\_1h | lagged\_mean\_24h | lagged\_max\_24h | lagged\_min\_24h | lagged\_mean\_7d | lagged\_max\_7d | lagged\_min\_7d |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| i64 | i64 | i64 | i64 | i64 | i64 | i64 | i64 | f64 | i64 | i64 | f64 | i64 | i64 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16  | null | null | null | null | null | null | null | null | null | null | null | null | null |
| 40  | 16  | null | null | null | null | null | null | null | null | null | null | null | null |
| 32  | 40  | 16  | null | null | null | null | null | null | null | null | null | null | null |
| 13  | 32  | 40  | 16  | null | null | null | null | null | null | null | null | null | null |
| 1   | 13  | 32  | 40  | null | null | null | null | null | null | null | null | null | null |
| 1   | 1   | 13  | 32  | null | null | null | null | null | null | null | null | null | null |
| 2   | 1   | 1   | 13  | null | null | null | null | null | null | null | null | null | null |
| 3   | 2   | 1   | 1   | null | null | null | null | null | null | null | null | null | null |
| 8   | 3   | 2   | 1   | null | null | null | null | null | null | null | null | null | null |
| 14  | 8   | 3   | 2   | null | null | null | null | null | null | null | null | null | null |

  
  

We can now separate the lagged features in a matrix `X` and the target variable (the counts to predict) in an array of the same first dimension `y`.

lagged\_df \= lagged\_df.drop\_nulls()
X \= lagged\_df.drop("count")
y \= lagged\_df\["count"\]
print("X shape: {}\\ny shape: {}".format(X.shape, y.shape))

Copy to clipboard

X shape: (17210, 13)
y shape: (17210,)

Copy to clipboard

Naive evaluation of the next hour bike demand regression[#](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html#naive-evaluation-of-the-next-hour-bike-demand-regression "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s randomly split our tabularized dataset to train a gradient boosting regression tree (GBRT) model and evaluate it using Mean Absolute Percentage Error (MAPE). If our model is aimed at forecasting (i.e., predicting future data from past data), we should not use training data that are ulterior to the testing data. In time series machine learning the “i.i.d” (independent and identically distributed) assumption does not hold true as the data points are not independent and have a temporal relationship.

from sklearn.ensemble import [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, test\_size\=0.2, random\_state\=42
)

model \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
().fit(X\_train, y\_train)

Copy to clipboard

Taking a look at the performance of the model.

from sklearn.metrics import [mean\_absolute\_percentage\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html#sklearn.metrics.mean_absolute_percentage_error "sklearn.metrics.mean_absolute_percentage_error")

y\_pred \= model.predict(X\_test)
[mean\_absolute\_percentage\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html#sklearn.metrics.mean_absolute_percentage_error "sklearn.metrics.mean_absolute_percentage_error")
(y\_test, y\_pred)

Copy to clipboard

0.39639694633413675

Copy to clipboard

Proper next hour forecasting evaluation[#](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html#proper-next-hour-forecasting-evaluation "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s use a proper evaluation splitting strategies that takes into account the temporal structure of the dataset to evaluate our model’s ability to predict data points in the future (to avoid cheating by reading values from the lagged features in the training set).

from sklearn.model\_selection import [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")

ts\_cv \= [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")
(
    n\_splits\=3,  \# to keep the notebook fast enough on common laptops
    gap\=48,  \# 2 days data gap between train and test
    max\_train\_size\=10000,  \# keep train sets of comparable sizes
    test\_size\=3000,  \# for 2 or 3 digits of precision in scores
)
all\_splits \= list(ts\_cv.split(X, y))

Copy to clipboard

Training the model and evaluating its performance based on MAPE.

train\_idx, test\_idx \= all\_splits\[0\]
X\_train, X\_test \= X\[train\_idx, :\], X\[test\_idx, :\]
y\_train, y\_test \= y\[train\_idx\], y\[test\_idx\]

model \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
().fit(X\_train, y\_train)
y\_pred \= model.predict(X\_test)
[mean\_absolute\_percentage\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html#sklearn.metrics.mean_absolute_percentage_error "sklearn.metrics.mean_absolute_percentage_error")
(y\_test, y\_pred)

Copy to clipboard

0.45822977660508035

Copy to clipboard

The generalization error measured via a shuffled trained test split is too optimistic. The generalization via a time-based split is likely to be more representative of the true performance of the regression model. Let’s assess this variability of our error evaluation with proper cross-validation:

from sklearn.model\_selection import [cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")

cv\_mape\_scores \= \-[cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
(
    model, X, y, cv\=ts\_cv, scoring\="neg\_mean\_absolute\_percentage\_error"
)
cv\_mape\_scores

Copy to clipboard

array(\[0.45822978, 0.2825124 , 0.36374485\])

Copy to clipboard

The variability across splits is quite large! In a real life setting it would be advised to use more splits to better assess the variability. Let’s report the mean CV scores and their standard deviation from now on.

print(f"CV MAPE: {cv\_mape\_scores.mean():.3f} ± {cv\_mape\_scores.std():.3f}")

Copy to clipboard

CV MAPE: 0.368 ± 0.072

Copy to clipboard

We can compute several combinations of evaluation metrics and loss functions, which are reported a bit below.

from collections import [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")

from sklearn.metrics import (
    [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
,
    [mean\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
,
    [mean\_pinball\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
,
    [root\_mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#sklearn.metrics.root_mean_squared_error "sklearn.metrics.root_mean_squared_error")
,
)
from sklearn.model\_selection import [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")

def consolidate\_scores(cv\_results, scores, metric):
    if metric \== "MAPE":
        scores\[metric\].append(f"{value.mean():.2f} ± {value.std():.2f}")
    else:
        scores\[metric\].append(f"{value.mean():.1f} ± {value.std():.1f}")

    return scores

scoring \= {
    "MAPE": [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
([mean\_absolute\_percentage\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html#sklearn.metrics.mean_absolute_percentage_error "sklearn.metrics.mean_absolute_percentage_error")
),
    "RMSE": [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
([root\_mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#sklearn.metrics.root_mean_squared_error "sklearn.metrics.root_mean_squared_error")
),
    "MAE": [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
([mean\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
),
    "pinball\_loss\_05": [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
([mean\_pinball\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
, alpha\=0.05),
    "pinball\_loss\_50": [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
([mean\_pinball\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
, alpha\=0.50),
    "pinball\_loss\_95": [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
([mean\_pinball\_loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")
, alpha\=0.95),
}
loss\_functions \= \["squared\_error", "poisson", "absolute\_error"\]
scores \= [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")
(list)
for loss\_func in loss\_functions:
    model \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(loss\=loss\_func)
    cv\_results \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(
        model,
        X,
        y,
        cv\=ts\_cv,
        scoring\=scoring,
        n\_jobs\=2,
    )
    time \= cv\_results\["fit\_time"\]
    scores\["loss"\].append(loss\_func)
    scores\["fit\_time"\].append(f"{time.mean():.2f} ± {time.std():.2f} s")

    for key, value in cv\_results.items():
        if key.startswith("test\_"):
            metric \= key.split("test\_")\[1\]
            scores \= consolidate\_scores(cv\_results, scores, metric)

Copy to clipboard

Modeling predictive uncertainty via quantile regression[#](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html#modeling-predictive-uncertainty-via-quantile-regression "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Instead of modeling the expected value of the distribution of Y|X like the least squares and Poisson losses do, one could try to estimate quantiles of the conditional distribution.

Y|X\=xi is expected to be a random variable for a given data point xi because we expect that the number of rentals cannot be 100% accurately predicted from the features. It can be influenced by other variables not properly captured by the existing lagged features. For instance whether or not it will rain in the next hour cannot be fully anticipated from the past hours bike rental data. This is what we call aleatoric uncertainty.

Quantile regression makes it possible to give a finer description of that distribution without making strong assumptions on its shape.

quantile\_list \= \[0.05, 0.5, 0.95\]

for quantile in quantile\_list:
    model \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(loss\="quantile", quantile\=quantile)
    cv\_results \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(
        model,
        X,
        y,
        cv\=ts\_cv,
        scoring\=scoring,
        n\_jobs\=2,
    )
    time \= cv\_results\["fit\_time"\]
    scores\["fit\_time"\].append(f"{time.mean():.2f} ± {time.std():.2f} s")

    scores\["loss"\].append(f"quantile {int(quantile \* 100)}")
    for key, value in cv\_results.items():
        if key.startswith("test\_"):
            metric \= key.split("test\_")\[1\]
            scores \= consolidate\_scores(cv\_results, scores, metric)

scores\_df \= pl.DataFrame(scores)
scores\_df

Copy to clipboard

shape: (6, 8)

| loss | fit\_time | MAPE | RMSE | MAE | pinball\_loss\_05 | pinball\_loss\_50 | pinball\_loss\_95 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| str | str | str | str | str | str | str | str |
| --- | --- | --- | --- | --- | --- | --- | --- |
| "squared\_error" | "0.29 ± 0.01 s" | "0.37 ± 0.07" | "63.0 ± 3.8" | "39.5 ± 2.9" | "17.9 ± 1.5" | "19.7 ± 1.5" | "21.6 ± 2.9" |
| "poisson" | "0.31 ± 0.01 s" | "0.32 ± 0.07" | "63.8 ± 3.8" | "39.1 ± 2.6" | "17.0 ± 1.6" | "19.5 ± 1.3" | "22.1 ± 2.1" |
| "absolute\_error" | "0.41 ± 0.01 s" | "0.32 ± 0.06" | "64.0 ± 3.5" | "39.4 ± 2.6" | "16.9 ± 0.8" | "19.7 ± 1.3" | "22.5 ± 2.6" |
| "quantile 5" | "0.47 ± 0.00 s" | "0.41 ± 0.01" | "145.0 ± 21.5" | "92.2 ± 16.6" | "5.9 ± 0.8" | "46.1 ± 8.3" | "86.4 ± 15.8" |
| "quantile 50" | "0.52 ± 0.01 s" | "0.32 ± 0.06" | "64.0 ± 3.5" | "39.4 ± 2.6" | "16.9 ± 0.8" | "19.7 ± 1.3" | "22.5 ± 2.6" |
| "quantile 95" | "0.47 ± 0.02 s" | "1.09 ± 0.29" | "101.0 ± 9.3" | "72.9 ± 6.5" | "63.7 ± 7.9" | "36.5 ± 3.3" | "9.2 ± 1.4" |

  
  

Let us take a look at the losses that minimise each metric.

def min\_arg(col):
    col\_split \= pl.col(col).str.split(" ")
    return pl.arg\_sort\_by(
        col\_split.list.get(0).cast(pl.Float64),
        col\_split.list.get(2).cast(pl.Float64),
    ).first()

scores\_df.select(
    pl.col("loss").get(min\_arg(col\_name)).alias(col\_name)
    for col\_name in scores\_df.columns
    if col\_name != "loss"
)

Copy to clipboard

shape: (1, 7)

| fit\_time | MAPE | RMSE | MAE | pinball\_loss\_05 | pinball\_loss\_50 | pinball\_loss\_95 |
| --- | --- | --- | --- | --- | --- | --- |
| str | str | str | str | str | str | str |
| --- | --- | --- | --- | --- | --- | --- |
| "squared\_error" | "absolute\_error" | "squared\_error" | "poisson" | "quantile 5" | "poisson" | "quantile 95" |

  
  

Even if the score distributions overlap due to the variance in the dataset, it is true that the average RMSE is lower when `loss="squared_error"`, whereas the average MAPE is lower when `loss="absolute_error"` as expected. That is also the case for the Mean Pinball Loss with the quantiles 5 and 95. The score corresponding to the 50 quantile loss is overlapping with the score obtained by minimizing other loss functions, which is also the case for the MAE.

A qualitative look at the predictions[#](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html#a-qualitative-look-at-the-predictions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We can now visualize the performance of the model with regards to the 5th percentile, median and the 95th percentile:

all\_splits \= list(ts\_cv.split(X, y))
train\_idx, test\_idx \= all\_splits\[0\]

X\_train, X\_test \= X\[train\_idx, :\], X\[test\_idx, :\]
y\_train, y\_test \= y\[train\_idx\], y\[test\_idx\]

max\_iter \= 50
gbrt\_mean\_poisson \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(loss\="poisson", max\_iter\=max\_iter)
gbrt\_mean\_poisson.fit(X\_train, y\_train)
mean\_predictions \= gbrt\_mean\_poisson.predict(X\_test)

gbrt\_median \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(
    loss\="quantile", quantile\=0.5, max\_iter\=max\_iter
)
gbrt\_median.fit(X\_train, y\_train)
median\_predictions \= gbrt\_median.predict(X\_test)

gbrt\_percentile\_5 \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(
    loss\="quantile", quantile\=0.05, max\_iter\=max\_iter
)
gbrt\_percentile\_5.fit(X\_train, y\_train)
percentile\_5\_predictions \= gbrt\_percentile\_5.predict(X\_test)

gbrt\_percentile\_95 \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(
    loss\="quantile", quantile\=0.95, max\_iter\=max\_iter
)
gbrt\_percentile\_95.fit(X\_train, y\_train)
percentile\_95\_predictions \= gbrt\_percentile\_95.predict(X\_test)

Copy to clipboard

We can now take a look at the predictions made by the regression models:

last\_hours \= slice(\-96, None)
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(15, 7))
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Predictions by regression models")
ax.plot(
    y\_test\[last\_hours\],
    "x-",
    alpha\=0.2,
    label\="Actual demand",
    color\="black",
)
ax.plot(
    median\_predictions\[last\_hours\],
    "^-",
    label\="GBRT median",
)
ax.plot(
    mean\_predictions\[last\_hours\],
    "x-",
    label\="GBRT mean (Poisson)",
)
ax.fill\_between(
    [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(96),
    percentile\_5\_predictions\[last\_hours\],
    percentile\_95\_predictions\[last\_hours\],
    alpha\=0.3,
    label\="GBRT 90% interval",
)
\_ \= ax.legend()

Copy to clipboard

![Predictions by regression models](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_001.png)

Here it’s interesting to notice that the blue area between the 5% and 95% percentile estimators has a width that varies with the time of the day:

*   At night, the blue band is much narrower: the pair of models is quite certain that there will be a small number of bike rentals. And furthermore these seem correct in the sense that the actual demand stays in that blue band.
    
*   During the day, the blue band is much wider: the uncertainty grows, probably because of the variability of the weather that can have a very large impact, especially on week-ends.
    
*   We can also see that during week-days, the commute pattern is still visible in the 5% and 95% estimations.
    
*   Finally, it is expected that 10% of the time, the actual demand does not lie between the 5% and 95% percentile estimates. On this test span, the actual demand seems to be higher, especially during the rush hours. It might reveal that our 95% percentile estimator underestimates the demand peaks. This could be be quantitatively confirmed by computing empirical coverage numbers as done in the [calibration of confidence intervals](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html#calibration-section)
    .
    

Looking at the performance of non-linear regression models vs the best models:

from sklearn.metrics import PredictionErrorDisplay

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=3, figsize\=(15, 6), sharey\=True)
fig.suptitle("Non-linear regression models")
predictions \= \[\
    median\_predictions,\
    percentile\_5\_predictions,\
    percentile\_95\_predictions,\
\]
labels \= \[\
    "Median",\
    "5th percentile",\
    "95th percentile",\
\]
for ax, pred, label in zip(axes, predictions, labels):
    [PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")
(
        y\_true\=y\_test,
        y\_pred\=pred,
        kind\="residual\_vs\_predicted",
        scatter\_kwargs\={"alpha": 0.3},
        ax\=ax,
    )
    ax.set(xlabel\="Predicted demand", ylabel\="True demand")
    ax.legend(\["Best model", label\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Non-linear regression models](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_002.png)

Conclusion[#](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html#conclusion "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

Through this example we explored time series forecasting using lagged features. We compared a naive regression (using the standardized [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
) with a proper time series evaluation strategy using [`TimeSeriesSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")
. We observed that the model trained using [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
, having a default value of `shuffle` set to `True` produced an overly optimistic Mean Average Percentage Error (MAPE). The results produced from the time-based split better represent the performance of our time-series regression model. We also analyzed the predictive uncertainty of our model via Quantile Regression. Predictions based on the 5th and 95th percentile using `loss="quantile"` provide us with a quantitative estimate of the uncertainty of the forecasts made by our time series regression model. Uncertainty estimation can also be performed using [MAPIE](https://mapie.readthedocs.io/en/latest/index.html)
, that provides an implementation based on recent work on conformal prediction methods and estimates both aleatoric and epistemic uncertainty at the same time. Furthermore, functionalities provided by [sktime](https://www.sktime.net/en/latest/users.html)
 can be used to extend scikit-learn estimators by making use of recursive time series forecasting, that enables dynamic predictions of future values.

**Total running time of the script:** (0 minutes 8.186 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_time_series_lagged_features.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_time_series_lagged_features.ipynb)

[`Download Jupyter notebook: plot_time_series_lagged_features.ipynb`](https://scikit-learn.org/stable/_downloads/6953689dfdc5dd401dda89604bbdaefb/plot_time_series_lagged_features.ipynb)

[`Download Python source code: plot_time_series_lagged_features.py`](https://scikit-learn.org/stable/_downloads/983937feb1a5f82dab78ed11a2af1217/plot_time_series_lagged_features.py)

[`Download zipped: plot_time_series_lagged_features.zip`](https://scikit-learn.org/stable/_downloads/b55408ba1cd122d5939c6ec627dc6a10/plot_time_series_lagged_features.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_refit_callable_thumb.png)

[Balance model complexity and cross-validated score](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_refit_callable.html)

Balance model complexity and cross-validated score

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_quantile_thumb.png)

[Prediction Intervals for Gradient Boosting Regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_quantile.html)

Prediction Intervals for Gradient Boosting Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hgbt_regression_thumb.png)

[Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html)

Features in Histogram Gradient Boosting Trees

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/983937feb1a5f82dab78ed11a2af1217/plot_time_series_lagged_features.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/6953689dfdc5dd401dda89604bbdaefb/plot_time_series_lagged_features.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/b55408ba1cd122d5939c6ec627dc6a10/plot_time_series_lagged_features.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_time_series_lagged_features.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_time_series_lagged_features.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)