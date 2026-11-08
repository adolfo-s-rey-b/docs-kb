[Skip to main content](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/applications/plot_cyclical_feature_engineering.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/applications/plot_cyclical_feature_engineering.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/applications/plot_cyclical_feature_engineering.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/applications/plot_cyclical_feature_engineering.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/applications/plot_cyclical_feature_engineering.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/applications/plot_cyclical_feature_engineering.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#sphx-glr-download-auto-examples-applications-plot-cyclical-feature-engineering-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Time-related feature engineering[#](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#time-related-feature-engineering "Link to this heading")

===============================================================================================================================================================================================

This notebook introduces different strategies to leverage time-related features for a bike sharing demand regression task that is highly dependent on business cycles (days, weeks, months) and yearly season cycles.

In the process, we introduce how to perform periodic feature engineering using the [`sklearn.preprocessing.SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
 class and its `extrapolation="periodic"` option.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Data exploration on the Bike Sharing Demand dataset[#](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#data-exploration-on-the-bike-sharing-demand-dataset "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We start by loading the data from the OpenML repository.

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")

bike\_sharing \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
("Bike\_Sharing\_Demand", version\=2, as\_frame\=True)
df \= bike\_sharing.frame

Copy to clipboard

To get a quick understanding of the periodic patterns of the data, let us have a look at the average demand per hour during a week.

Note that the week starts on a Sunday, during the weekend. We can clearly distinguish the commute patterns in the morning and evenings of the work days and the leisure use of the bikes on the weekends with a more spread peak demand around the middle of the days:

import matplotlib.pyplot as plt

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(12, 4))
average\_week\_demand \= df.groupby(\["weekday", "hour"\])\["count"\].mean()
average\_week\_demand.plot(ax\=ax)
\_ \= ax.set(
    title\="Average hourly bike demand during the week",
    xticks\=\[i \* 24 for i in range(7)\],
    xticklabels\=\["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"\],
    xlabel\="Time of the week",
    ylabel\="Number of bike rentals",
)

Copy to clipboard

![Average hourly bike demand during the week](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_001.png)

The target of the prediction problem is the absolute count of bike rentals on an hourly basis:

df\["count"\].max()

Copy to clipboard

np.int64(977)

Copy to clipboard

Let us rescale the target variable (number of hourly bike rentals) to predict a relative demand so that the mean absolute error is more easily interpreted as a fraction of the maximum demand.

Note

The fit method of the models used in this notebook all minimizes the mean squared error to estimate the conditional mean. The absolute error, however, would estimate the conditional median.

Nevertheless, when reporting performance measures on the test set in the discussion, we choose to focus on the mean absolute error instead of the (root) mean squared error because it is more intuitive to interpret. Note, however, that in this study the best models for one metric are also the best ones in terms of the other metric.

y \= df\["count"\] / df\["count"\].max()

Copy to clipboard

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(12, 4))
y.hist(bins\=30, ax\=ax)
\_ \= ax.set(
    xlabel\="Fraction of rented fleet demand",
    ylabel\="Number of hours",
)

Copy to clipboard

![plot cyclical feature engineering](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_002.png)

The input feature data frame is a time annotated hourly log of variables describing the weather conditions. It includes both numerical and categorical variables. Note that the time information has already been expanded into several complementary columns.

X \= df.drop("count", axis\="columns")
X

Copy to clipboard

|     | season | year | month | hour | holiday | weekday | workingday | weather | temp | feel\_temp | humidity | windspeed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | spring | 0   | 1   | 0   | False | 6   | False | clear | 9.84 | 14.395 | 0.81 | 0.0000 |
| 1   | spring | 0   | 1   | 1   | False | 6   | False | clear | 9.02 | 13.635 | 0.80 | 0.0000 |
| 2   | spring | 0   | 1   | 2   | False | 6   | False | clear | 9.02 | 13.635 | 0.80 | 0.0000 |
| 3   | spring | 0   | 1   | 3   | False | 6   | False | clear | 9.84 | 14.395 | 0.75 | 0.0000 |
| 4   | spring | 0   | 1   | 4   | False | 6   | False | clear | 9.84 | 14.395 | 0.75 | 0.0000 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 17374 | spring | 1   | 12  | 19  | False | 1   | True | misty | 10.66 | 12.880 | 0.60 | 11.0014 |
| 17375 | spring | 1   | 12  | 20  | False | 1   | True | misty | 10.66 | 12.880 | 0.60 | 11.0014 |
| 17376 | spring | 1   | 12  | 21  | False | 1   | True | clear | 10.66 | 12.880 | 0.60 | 11.0014 |
| 17377 | spring | 1   | 12  | 22  | False | 1   | True | clear | 10.66 | 13.635 | 0.56 | 8.9981 |
| 17378 | spring | 1   | 12  | 23  | False | 1   | True | clear | 10.66 | 13.635 | 0.65 | 8.9981 |

17379 rows × 12 columns

  
  

Note

If the time information was only present as a date or datetime column, we could have expanded it into hour-in-the-day, day-in-the-week, day-in-the-month, month-in-the-year using pandas: [https://pandas.pydata.org/pandas-docs/stable/user\_guide/timeseries.html#time-date-components](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-date-components)

We now introspect the distribution of the categorical variables, starting with `"weather"`:

X\["weather"\].value\_counts()

Copy to clipboard

weather
clear         11413
misty          4544
rain           1419
heavy\_rain        3
Name: count, dtype: int64

Copy to clipboard

Since there are only 3 `"heavy_rain"` events, we cannot use this category to train machine learning models with cross validation. Instead, we simplify the representation by collapsing those into the `"rain"` category.

X\["weather"\] \= (
    X\["weather"\]
    .astype(object)
    .replace(to\_replace\="heavy\_rain", value\="rain")
    .astype("category")
)

Copy to clipboard

X\["weather"\].value\_counts()

Copy to clipboard

weather
clear    11413
misty     4544
rain      1422
Name: count, dtype: int64

Copy to clipboard

As expected, the `"season"` variable is well balanced:

X\["season"\].value\_counts()

Copy to clipboard

season
fall      4496
summer    4409
spring    4242
winter    4232
Name: count, dtype: int64

Copy to clipboard

Time-based cross-validation[#](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#time-based-cross-validation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Since the dataset is a time-ordered event log (hourly demand), we will use a time-sensitive cross-validation splitter to evaluate our demand forecasting model as realistically as possible. We use a gap of 2 days between the train and test side of the splits. We also limit the training set size to make the performance of the CV folds more stable.

1000 test datapoints should be enough to quantify the performance of the model. This represents a bit less than a month and a half of contiguous test data:

from sklearn.model\_selection import [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")

ts\_cv \= [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")
(
    n\_splits\=5,
    gap\=48,
    max\_train\_size\=10000,
    test\_size\=1000,
)

Copy to clipboard

Let us manually inspect the various splits to check that the `TimeSeriesSplit` works as we expect, starting with the first split:

all\_splits \= list(ts\_cv.split(X, y))
train\_0, test\_0 \= all\_splits\[0\]

Copy to clipboard

X.iloc\[test\_0\]

Copy to clipboard

|     | season | year | month | hour | holiday | weekday | workingday | weather | temp | feel\_temp | humidity | windspeed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12379 | summer | 1   | 6   | 0   | False | 2   | True | clear | 22.14 | 25.760 | 0.68 | 27.9993 |
| 12380 | summer | 1   | 6   | 1   | False | 2   | True | misty | 21.32 | 25.000 | 0.77 | 22.0028 |
| 12381 | summer | 1   | 6   | 2   | False | 2   | True | rain | 21.32 | 25.000 | 0.72 | 19.9995 |
| 12382 | summer | 1   | 6   | 3   | False | 2   | True | rain | 20.50 | 24.240 | 0.82 | 12.9980 |
| 12383 | summer | 1   | 6   | 4   | False | 2   | True | rain | 20.50 | 24.240 | 0.82 | 12.9980 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 13374 | fall | 1   | 7   | 11  | False | 1   | True | clear | 34.44 | 40.150 | 0.53 | 15.0013 |
| 13375 | fall | 1   | 7   | 12  | False | 1   | True | clear | 34.44 | 39.395 | 0.49 | 8.9981 |
| 13376 | fall | 1   | 7   | 13  | False | 1   | True | clear | 34.44 | 39.395 | 0.49 | 19.0012 |
| 13377 | fall | 1   | 7   | 14  | False | 1   | True | clear | 36.08 | 40.910 | 0.42 | 7.0015 |
| 13378 | fall | 1   | 7   | 15  | False | 1   | True | clear | 35.26 | 40.150 | 0.47 | 16.9979 |

1000 rows × 12 columns

  
  

X.iloc\[train\_0\]

Copy to clipboard

|     | season | year | month | hour | holiday | weekday | workingday | weather | temp | feel\_temp | humidity | windspeed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2331 | summer | 0   | 4   | 1   | False | 2   | True | misty | 25.42 | 31.060 | 0.50 | 6.0032 |
| 2332 | summer | 0   | 4   | 2   | False | 2   | True | misty | 24.60 | 31.060 | 0.53 | 8.9981 |
| 2333 | summer | 0   | 4   | 3   | False | 2   | True | misty | 23.78 | 27.275 | 0.56 | 8.9981 |
| 2334 | summer | 0   | 4   | 4   | False | 2   | True | misty | 22.96 | 26.515 | 0.64 | 8.9981 |
| 2335 | summer | 0   | 4   | 5   | False | 2   | True | misty | 22.14 | 25.760 | 0.68 | 8.9981 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 12326 | summer | 1   | 6   | 19  | False | 6   | False | clear | 26.24 | 31.060 | 0.36 | 11.0014 |
| 12327 | summer | 1   | 6   | 20  | False | 6   | False | clear | 25.42 | 31.060 | 0.35 | 19.0012 |
| 12328 | summer | 1   | 6   | 21  | False | 6   | False | clear | 24.60 | 31.060 | 0.40 | 7.0015 |
| 12329 | summer | 1   | 6   | 22  | False | 6   | False | clear | 23.78 | 27.275 | 0.46 | 8.9981 |
| 12330 | summer | 1   | 6   | 23  | False | 6   | False | clear | 22.96 | 26.515 | 0.52 | 7.0015 |

10000 rows × 12 columns

  
  

We now inspect the last split:

train\_4, test\_4 \= all\_splits\[4\]

Copy to clipboard

X.iloc\[test\_4\]

Copy to clipboard

|     | season | year | month | hour | holiday | weekday | workingday | weather | temp | feel\_temp | humidity | windspeed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16379 | winter | 1   | 11  | 5   | False | 2   | True | misty | 13.94 | 16.665 | 0.66 | 8.9981 |
| 16380 | winter | 1   | 11  | 6   | False | 2   | True | misty | 13.94 | 16.665 | 0.71 | 11.0014 |
| 16381 | winter | 1   | 11  | 7   | False | 2   | True | clear | 13.12 | 16.665 | 0.76 | 6.0032 |
| 16382 | winter | 1   | 11  | 8   | False | 2   | True | clear | 13.94 | 16.665 | 0.71 | 8.9981 |
| 16383 | winter | 1   | 11  | 9   | False | 2   | True | misty | 14.76 | 18.940 | 0.71 | 0.0000 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 17374 | spring | 1   | 12  | 19  | False | 1   | True | misty | 10.66 | 12.880 | 0.60 | 11.0014 |
| 17375 | spring | 1   | 12  | 20  | False | 1   | True | misty | 10.66 | 12.880 | 0.60 | 11.0014 |
| 17376 | spring | 1   | 12  | 21  | False | 1   | True | clear | 10.66 | 12.880 | 0.60 | 11.0014 |
| 17377 | spring | 1   | 12  | 22  | False | 1   | True | clear | 10.66 | 13.635 | 0.56 | 8.9981 |
| 17378 | spring | 1   | 12  | 23  | False | 1   | True | clear | 10.66 | 13.635 | 0.65 | 8.9981 |

1000 rows × 12 columns

  
  

X.iloc\[train\_4\]

Copy to clipboard

|     | season | year | month | hour | holiday | weekday | workingday | weather | temp | feel\_temp | humidity | windspeed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6331 | winter | 0   | 9   | 9   | False | 1   | True | misty | 26.24 | 28.790 | 0.89 | 12.9980 |
| 6332 | winter | 0   | 9   | 10  | False | 1   | True | misty | 26.24 | 28.790 | 0.89 | 12.9980 |
| 6333 | winter | 0   | 9   | 11  | False | 1   | True | clear | 27.88 | 31.820 | 0.79 | 15.0013 |
| 6334 | winter | 0   | 9   | 12  | False | 1   | True | misty | 27.88 | 31.820 | 0.79 | 11.0014 |
| 6335 | winter | 0   | 9   | 13  | False | 1   | True | misty | 28.70 | 33.335 | 0.74 | 11.0014 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 16326 | winter | 1   | 11  | 0   | False | 0   | False | misty | 12.30 | 15.150 | 0.70 | 11.0014 |
| 16327 | winter | 1   | 11  | 1   | False | 0   | False | clear | 12.30 | 14.395 | 0.70 | 12.9980 |
| 16328 | winter | 1   | 11  | 2   | False | 0   | False | clear | 11.48 | 14.395 | 0.81 | 7.0015 |
| 16329 | winter | 1   | 11  | 3   | False | 0   | False | misty | 12.30 | 15.150 | 0.81 | 11.0014 |
| 16330 | winter | 1   | 11  | 4   | False | 0   | False | misty | 12.30 | 14.395 | 0.81 | 12.9980 |

10000 rows × 12 columns

  
  

All is well. We are now ready to do some predictive modeling!

Gradient Boosting[#](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#gradient-boosting "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Gradient Boosting Regression with decision trees is often flexible enough to efficiently handle heterogeneous tabular data with a mix of categorical and numerical features as long as the number of samples is large enough.

Here, we use the modern [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 with native support for categorical features. Therefore, we only need to set `categorical_features="from_dtype"` such that features with categorical dtype are considered categorical features. For reference, we extract the categorical features from the dataframe based on the dtype. The internal trees use a dedicated tree splitting rule for these features.

The numerical variables need no preprocessing and, for the sake of simplicity, we only try the default hyper-parameters for this model:

from sklearn.compose import [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
from sklearn.ensemble import [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
from sklearn.model\_selection import [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")

gbrt \= [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(categorical\_features\="from\_dtype", random\_state\=42)
categorical\_columns \= X.columns\[X.dtypes \== "category"\]
print("Categorical features:", categorical\_columns.tolist())

Copy to clipboard

Categorical features: \['season', 'holiday', 'workingday', 'weather'\]

Copy to clipboard

Let’s evaluate our gradient boosting model with the mean absolute error of the relative demand averaged across our 5 time-based cross-validation splits:

import numpy as np

def evaluate(model, X, y, cv, model\_prop\=None, model\_step\=None):
    cv\_results \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(
        model,
        X,
        y,
        cv\=cv,
        scoring\=\["neg\_mean\_absolute\_error", "neg\_root\_mean\_squared\_error"\],
        return\_estimator\=True,
    )
    if model\_prop is not None:
        if model\_step is not None:
            values \= \[\
                getattr(m\[model\_step\], model\_prop) for m in cv\_results\["estimator"\]\
            \]
        else:
            values \= \[getattr(m, model\_prop) for m in cv\_results\["estimator"\]\]
        print(f"Mean model.{model\_prop} = {[np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
(values)}")
    mae \= \-cv\_results\["test\_neg\_mean\_absolute\_error"\]
    rmse \= \-cv\_results\["test\_neg\_root\_mean\_squared\_error"\]
    print(
        f"Mean Absolute Error:     {mae.mean():.3f} +/- {mae.std():.3f}\\n"
        f"Root Mean Squared Error: {rmse.mean():.3f} +/- {rmse.std():.3f}"
    )
    \# To display the fitted estimator diagrams in the notebook.
    return cv\_results\["estimator"\]\[0\]

evaluate(gbrt, X, y, cv\=ts\_cv, model\_prop\="n\_iter\_")

Copy to clipboard

Mean model.n\_iter\_ = 100.0
Mean Absolute Error:     0.044 +/- 0.003
Root Mean Squared Error: 0.068 +/- 0.005

Copy to clipboard

HistGradientBoostingRegressor(random\_state=42)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

HistGradientBoostingRegressor

[?Documentation for HistGradientBoostingRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo-random number generator to control the subsampling in the  <br>binning process, and the train/validation data split if early stopping  <br>is enabled.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 42  |
|     | [loss loss: {'squared\_error', 'absolute\_error', 'gamma', 'poisson', 'quantile'}, default='squared\_error'  <br>  <br>The loss function to use in the boosting process. Note that the  <br>"squared error", "gamma" and "poisson" losses actually implement  <br>"half least squares loss", "half gamma deviance" and "half poisson  <br>deviance" to simplify the computation of the gradient. Furthermore,  <br>"gamma" and "poisson" losses internally use a log-link, "gamma"  <br>requires \`\`y > 0\`\` and "poisson" requires \`\`y >= 0\`\`.  <br>"quantile" uses the pinball loss.  <br>  <br>.. versionchanged:: 0.23  <br>Added option 'poisson'.  <br>  <br>.. versionchanged:: 1.1  <br>Added option 'quantile'.  <br>  <br>.. versionchanged:: 1.3  <br>Added option 'gamma'.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=loss,-%7B%27squared_error%27%2C%20%27absolute_error%27%2C%20%27gamma%27%2C%20%27poisson%27%2C%20%27quantile%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27squared_error%27) | 'squared\_error' |
|     | [quantile quantile: float, default=None  <br>  <br>If loss is "quantile", this parameter specifies which quantile to be estimated  <br>and must be between 0 and 1.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=quantile,-float%2C%20default%3DNone) | None |
|     | [learning\_rate learning\_rate: float, default=0.1  <br>  <br>The learning rate, also known as \*shrinkage\*. This is used as a  <br>multiplicative factor for the leaves values. Use \`\`1\`\` for no  <br>shrinkage.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=learning_rate,-float%2C%20default%3D0.1) | 0.1 |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>The maximum number of iterations of the boosting process, i.e. the  <br>maximum number of trees.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |
|     | [max\_leaf\_nodes max\_leaf\_nodes: int or None, default=31  <br>  <br>The maximum number of leaves for each tree. Must be strictly greater  <br>than 1. If None, there is no maximum limit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_leaf_nodes,-int%20or%20None%2C%20default%3D31) | 31  |
|     | [max\_depth max\_depth: int or None, default=None  <br>  <br>The maximum depth of each tree. The depth of a tree is the number of  <br>edges to go from the root to the deepest leaf.  <br>Depth isn't constrained by default.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_depth,-int%20or%20None%2C%20default%3DNone) | None |
|     | [min\_samples\_leaf min\_samples\_leaf: int, default=20  <br>  <br>The minimum number of samples per leaf. For small datasets with less  <br>than a few hundred samples, it is recommended to lower this value  <br>since only very shallow trees would be built.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=min_samples_leaf,-int%2C%20default%3D20) | 20  |
|     | [l2\_regularization l2\_regularization: float, default=0  <br>  <br>The L2 regularization parameter penalizing leaves with small hessians.  <br>Use \`\`0\`\` for no regularization (default).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=l2_regularization,-float%2C%20default%3D0) | 0.0 |
|     | [max\_features max\_features: float, default=1.0  <br>  <br>Proportion of randomly chosen features in each and every node split.  <br>This is a form of regularization, smaller values make the trees weaker  <br>learners and might prevent overfitting.  <br>If interaction constraints from \`interaction\_cst\` are present, only allowed  <br>features are taken into account for the subsampling.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_features,-float%2C%20default%3D1.0) | 1.0 |
|     | [max\_bins max\_bins: int, default=255  <br>  <br>The maximum number of bins to use for non-missing values. Before  <br>training, each feature of the input array \`X\` is binned into  <br>integer-valued bins, which allows for a much faster training stage.  <br>Features with a small number of unique values may use less than  <br>\`\`max\_bins\`\` bins. In addition to the \`\`max\_bins\`\` bins, one more bin  <br>is always reserved for missing values. Must be no larger than 255.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_bins,-int%2C%20default%3D255) | 255 |
|     | [categorical\_features categorical\_features: array-like of {bool, int, str} of shape (n\_features) or shape (n\_categorical\_features,), default='from\_dtype'  <br>  <br>Indicates the categorical features.  <br>  <br>\- None : no feature will be considered categorical.  <br>\- boolean array-like : boolean mask indicating categorical features.  <br>\- integer array-like : integer indices indicating categorical  <br>features.  <br>\- str array-like: names of categorical features (assuming the training  <br>data has feature names).  <br>\- \`"from\_dtype"\`: dataframe columns with dtype "Categorical" and "Enum" are  <br>considered to be categorical features. The input must be a dataframe that  <br>is supported by narwhals (or supports it): :func:\`narwhals.from\_native\` must  <br>work. This is the case, for instance, for pandas and polars DataFrames.  <br>  <br>For each categorical feature, there must be at most \`max\_bins\` unique  <br>categories. Negative values for categorical features encoded as numeric  <br>dtypes are treated as missing values. All categorical values are  <br>converted to floating point numbers. This means that categorical values  <br>of 1.0 and 1 are treated as the same category.  <br>  <br>Read more in the :ref:\`User Guide <categorical\_support\_gbdt>\` and  <br>:ref:\`sphx\_glr\_auto\_examples\_ensemble\_plot\_gradient\_boosting\_categorical.py\`.  <br>  <br>.. versionadded:: 0.24  <br>  <br>.. versionchanged:: 1.2  <br>Added support for feature names.  <br>  <br>.. versionchanged:: 1.4  <br>Added \`"from\_dtype"\` option.  <br>  <br>.. versionchanged:: 1.6  <br>The default value changed from \`None\` to \`"from\_dtype"\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=categorical_features,-array-like%20of%20%7Bbool%2C%20int%2C%20str%7D%20of%20shape%20%28n_features%29%20%20%20%20%20%20%20%20%20%20%20%20%20or%20shape%20%28n_categorical_features%2C%29%2C%20default%3D%27from_dtype%27) | 'from\_dtype' |
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features) or dict, default=None  <br>  <br>Monotonic constraint to enforce on each feature are specified using the  <br>following integer values:  <br>  <br>\- 1: monotonic increase  <br>\- 0: no constraint  <br>\- -1: monotonic decrease  <br>  <br>If a dict with str keys, map feature to monotonic constraints by name.  <br>If an array, the features are mapped to constraints by position. See  <br>:ref:\`monotonic\_cst\_features\_names\` for a usage example.  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 0.23  <br>  <br>.. versionchanged:: 1.2  <br>Accept dict of constraints with feature names as keys.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%29%20or%20dict%2C%20default%3DNone) | None |
|     | [interaction\_cst interaction\_cst: {"pairwise", "no\_interactions"} or sequence of lists/tuples/sets of int, default=None  <br>  <br>Specify interaction constraints, the sets of features which can  <br>interact with each other in child node splits.  <br>  <br>Each item specifies the set of feature indices that are allowed  <br>to interact with each other. If there are more features than  <br>specified in these constraints, they are treated as if they were  <br>specified as an additional set.  <br>  <br>The strings "pairwise" and "no\_interactions" are shorthands for  <br>allowing only pairwise or no interactions, respectively.  <br>  <br>For instance, with 5 features in total, \`interaction\_cst=\[{0, 1}\]\`  <br>is equivalent to \`interaction\_cst=\[{0, 1}, {2, 3, 4}\]\`,  <br>and specifies that each branch of a tree will either only split  <br>on features 0 and 1 or only split on features 2, 3 and 4.  <br>  <br>See :ref:\`this example<ice-vs-pdp>\` on how to use \`interaction\_cst\`.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=interaction_cst,-%7B%22pairwise%22%2C%20%22no_interactions%22%7D%20or%20sequence%20of%20lists/tuples/sets%20%20%20%20%20%20%20%20%20%20%20%20%20of%20int%2C%20default%3DNone) | None |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble. For results to be valid, the  <br>estimator should be re-trained on the same data only.  <br>See :term:\`the Glossary <warm\_start>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [early\_stopping early\_stopping: 'auto' or bool, default='auto'  <br>  <br>If 'auto', early stopping is enabled if the sample size is larger than  <br>10000 or if \`X\_val\` and \`y\_val\` are passed to \`fit\`. If True, early stopping  <br>is enabled, otherwise early stopping is disabled.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=early_stopping,-%27auto%27%20or%20bool%2C%20default%3D%27auto%27) | 'auto' |
|     | [scoring scoring: str or callable or None, default='loss'  <br>  <br>Scoring method to use for early stopping. Only used if \`early\_stopping\`  <br>is enabled. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: the :ref:\`coefficient of determination <r2\_score>\`  <br>(:math:\`R^2\`) is used.  <br>\- 'loss': early stopping is checked w.r.t the loss value.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=scoring,-str%20or%20callable%20or%20None%2C%20default%3D%27loss%27) | 'loss' |
|     | [validation\_fraction validation\_fraction: int or float or None, default=0.1  <br>  <br>Proportion (or absolute size) of training data to set aside as  <br>validation data for early stopping. If None, early stopping is done on  <br>the training data.  <br>The value is ignored if either early stopping is not performed, e.g.  <br>\`early\_stopping=False\`, or if \`X\_val\` and \`y\_val\` are passed to fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=validation_fraction,-int%20or%20float%20or%20None%2C%20default%3D0.1) | 0.1 |
|     | [n\_iter\_no\_change n\_iter\_no\_change: int, default=10  <br>  <br>Used to determine when to "early stop". The fitting process is  <br>stopped when none of the last \`\`n\_iter\_no\_change\`\` scores are better  <br>than the \`\`n\_iter\_no\_change - 1\`\` -th-to-last one, up to some  <br>tolerance. Only used if early stopping is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=n_iter_no_change,-int%2C%20default%3D10) | 10  |
|     | [tol tol: float, default=1e-7  <br>  <br>The absolute tolerance to use when comparing scores during early  <br>stopping. The higher the tolerance, the more likely we are to early  <br>stop: higher tolerance means that it will be harder for subsequent  <br>iterations to be considered an improvement upon the reference score.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=tol,-float%2C%20default%3D1e-7) | 1e-07 |
|     | [verbose verbose: int, default=0  <br>  <br>The verbosity level. If not zero, print some information about the  <br>fitting process. \`\`1\`\` prints only summary info, \`\`2\`\` prints info per  <br>iteration.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [do\_early\_stopping\_ do\_early\_stopping\_: bool  <br>  <br>Indicates whether early stopping is used during training.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=do_early_stopping_,-bool) | bool | False |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |
| [is\_categorical\_ is\_categorical\_: ndarray, shape (n\_features, ) or None  <br>  <br>Boolean mask for the categorical features. \`\`None\`\` if there are no  <br>categorical features.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=is_categorical_,-ndarray%2C%20shape%20%28n_features%2C%20%29%20or%20None) | ndarray\[bool\](12,) | \[ True,False,False,...,False,False,False\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=n_features_in_,-int) | int | 12  |
| [n\_iter\_ n\_iter\_: int  <br>  <br>The number of iterations as selected by early stopping, depending on  <br>the \`early\_stopping\` parameter. Otherwise it corresponds to max\_iter.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=n_iter_,-int) | int | 100 |
| [n\_trees\_per\_iteration\_ n\_trees\_per\_iteration\_: int  <br>  <br>The number of tree that are built at each iteration. For regressors,  <br>this is always 1.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=n_trees_per_iteration_,-int) | int | 1   |
| [train\_score\_ train\_score\_: ndarray, shape (n\_iter\_+1,)  <br>  <br>The scores at each iteration on the training data. The first entry  <br>is the score of the ensemble before the first iteration. Scores are  <br>computed according to the \`\`scoring\`\` parameter. If \`\`scoring\`\` is  <br>not 'loss', scores are computed on a subset of at most 10 000  <br>samples. Empty if no early stopping.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=train_score_,-ndarray%2C%20shape%20%28n_iter_%2B1%2C%29) | ndarray\[float64\](0,) | \[\] |
| [validation\_score\_ validation\_score\_: ndarray, shape (n\_iter\_+1,)  <br>  <br>The scores at each iteration on the held-out validation data. The  <br>first entry is the score of the ensemble before the first iteration.  <br>Scores are computed according to the \`\`scoring\`\` parameter. Empty if  <br>no early stopping or if \`\`validation\_fraction\`\` is None.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=validation_score_,-ndarray%2C%20shape%20%28n_iter_%2B1%2C%29) | ndarray\[float64\](0,) | \[\] |

  
  

We see that we set `max_iter` large enough such that early stopping took place.

This model has an average error around 4 to 5% of the maximum demand. This is quite good for a first trial without any hyper-parameter tuning! We just had to make the categorical variables explicit. Note that the time related features are passed as is, i.e. without processing them. But this is not much of a problem for tree-based models as they can learn a non-monotonic relationship between ordinal input features and the target.

This is not the case for linear regression models as we will see in the following.

Naive linear regression[#](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#naive-linear-regression "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As usual for linear models, categorical variables need to be one-hot encoded. For consistency, we scale the numerical features to the same 0-1 range using [`MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
, although in this case it does not impact the results much because they are already on comparable scales:

from sklearn.linear\_model import [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
from sklearn.preprocessing import [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
, [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")

one\_hot\_encoder \= [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
(handle\_unknown\="ignore", sparse\_output\=False)
alphas \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-6, 6, 25)
naive\_linear\_pipeline \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
        transformers\=\[\
            ("categorical", one\_hot\_encoder, categorical\_columns),\
        \],
        remainder\=[MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
(),
        verbose\_feature\_names\_out\=False,
    ),
    [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
(alphas\=alphas),
)

evaluate(
    naive\_linear\_pipeline, X, y, cv\=ts\_cv, model\_prop\="alpha\_", model\_step\="ridgecv"
)

Copy to clipboard

Mean model.alpha\_ = 2.7298221281347037
Mean Absolute Error:     0.142 +/- 0.014
Root Mean Squared Error: 0.184 +/- 0.020

Copy to clipboard

Pipeline(steps=\[('columntransformer',\
                 ColumnTransformer(remainder=MinMaxScaler(),\
                                   transformers=\[('categorical',\
                                                  OneHotEncoder(handle\_unknown='ignore',\
                                                                sparse\_output=False),\
                                                  Index(\['season', 'holiday', 'workingday', 'weather'\], dtype='str'))\],\
                                   verbose\_feature\_names\_out=False)),\
                ('ridgecv',\
                 RidgeCV(alphas=array(\[1.00000000e-06, 3.16227766e-06, 1.00000000e-05, 3.16227766e-05,\
       1.00000000e-04, 3.16227766e-04, 1.00000000e-03, 3.16227766e-03,\
       1.00000000e-02, 3.16227766e-02, 1.00000000e-01, 3.16227766e-01,\
       1.00000000e+00, 3.16227766e+00, 1.00000000e+01, 3.16227766e+01,\
       1.00000000e+02, 3.16227766e+02, 1.00000000e+03, 3.16227766e+03,\
       1.00000000e+04, 3.16227766e+04, 1.00000000e+05, 3.16227766e+05,\
       1.00000000e+06\])))\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('columntransformer', ...), ('ridgecv', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 12  |

columntransformer: ColumnTransformer

[?Documentation for columntransformer: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('categorical', ...)\] |
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | MinMaxScaler() |
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | False |
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 12  |
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'categorical...inMaxScaler()} |
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'ca...al': slice(0, 11, None), 're...er': slice(11, 19, None)} |
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('ca...al', OneHotEncoder...\_output=False), Index(\['seaso..., dtype='str')), ('re...er', MinMaxScaler(), \['year', 'month', 'hour', 'weekday', ...\])\] |\
\
categorical\
\
Index(\['season', 'holiday', 'workingday', 'weather'\], dtype='str')\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | False |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\['fall'... dtype=object), array(\['False... dtype=object), array(\['False... dtype=object), array(\['clear... dtype=object)\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](4,) | \['season','holiday','workingday','weather'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 4   |\
\
11 features\
\
|     |\
| --- |\
| season\_fall |\
| season\_spring |\
| season\_summer |\
| season\_winter |\
| holiday\_False |\
| holiday\_True |\
| workingday\_False |\
| workingday\_True |\
| weather\_clear |\
| weather\_misty |\
| weather\_rain |\
\
remainder\
\
\['year', 'month', 'hour', 'weekday', 'temp', 'feel\_temp', 'humidity', 'windspeed'\]\
\
MinMaxScaler\
\
[?Documentation for MinMaxScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [feature\_range feature\_range: tuple (min, max), default=(0, 1)  <br>  <br>Desired range of transformed data.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=feature_range,-tuple%20%28min%2C%20max%29%2C%20default%3D%280%2C%201%29) | (0, ...) |\
|     | [copy copy: bool, default=True  <br>  <br>Set to False to perform inplace row normalization and avoid a  <br>copy (if the input is already a numpy array).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [clip clip: bool, default=False  <br>  <br>Set to True to clip transformed values of held-out data to  <br>provided \`feature\_range\`.  <br>Since this parameter will clip values, \`inverse\_transform\` may not  <br>be able to restore the original data.  <br>  <br>.. note::  <br>Setting \`clip=True\` does not prevent feature drift (a distribution  <br>shift between training and test data). The transformed values are clipped  <br>to the \`feature\_range\`, which helps avoid unintended behavior in models  <br>sensitive to out-of-range inputs (e.g. linear models). Use with care,  <br>as clipping can distort the distribution of test data.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=clip,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [data\_max\_ data\_max\_: ndarray of shape (n\_features,)  <br>  <br>Per feature maximum seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_max\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_max_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](8,) | \[ 1.,12.,23.,...,50., 1.,57.\] |\
| [data\_min\_ data\_min\_: ndarray of shape (n\_features,)  <br>  <br>Per feature minimum seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_min\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_min_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](8,) | \[0. ,1. ,0. ,...,0.76,0.16,0. \] |\
| [data\_range\_ data\_range\_: ndarray of shape (n\_features,)  <br>  <br>Per feature range \`\`(data\_max\_ - data\_min\_)\`\` seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_range\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_range_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](8,) | \[ 1. ,11. ,23. ,...,49.24, 0.84,57. \] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](8,) | \['year','month','hour',...,'feel\_temp','humidity','windspeed'\] |\
| [min\_ min\_: ndarray of shape (n\_features,)  <br>  <br>Per feature adjustment for minimum. Equivalent to  <br>\`\`min - X.min(axis=0) \* self.scale\_\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=min_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](8,) | \[ 0. ,-0.09, 0. ,...,-0.02,-0.19, 0. \] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=n_features_in_,-int) | int | 8   |\
| [n\_samples\_seen\_ n\_samples\_seen\_: int  <br>  <br>The number of samples processed by the estimator.  <br>It will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=n_samples_seen_,-int) | int | 10000 |\
| [scale\_ scale\_: ndarray of shape (n\_features,)  <br>  <br>Per feature relative scaling of the data. Equivalent to  <br>\`\`(max - min) / (X.max(axis=0) - X.min(axis=0))\`\`  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\* attribute.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](8,) | \[1. ,0.09,0.04,...,0.02,1.19,0.02\] |\
\
8 features\
\
|     |\
| --- |\
| year |\
| month |\
| hour |\
| weekday |\
| temp |\
| feel\_temp |\
| humidity |\
| windspeed |\
\
19 features\
\
|     |\
| --- |\
| season\_fall |\
| season\_spring |\
| season\_summer |\
| season\_winter |\
| holiday\_False |\
| holiday\_True |\
| workingday\_False |\
| workingday\_True |\
| weather\_clear |\
| weather\_misty |\
| weather\_rain |\
| year |\
| month |\
| hour |\
| weekday |\
| temp |\
| feel\_temp |\
| humidity |\
| windspeed |\
\
RidgeCV\
\
[?Documentation for RidgeCV](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [alphas alphas: array-like of shape (n\_alphas,), default=(0.1, 1.0, 10.0)  <br>  <br>Array of alpha values to try.  <br>Regularization strength; must be a positive float. Regularization  <br>improves the conditioning of the problem and reduces the variance of  <br>the estimates. Larger values specify stronger regularization.  <br>Alpha corresponds to \`\`1 / (2C)\`\` in other linear models such as  <br>:class:\`~sklearn.linear\_model.LogisticRegression\` or  <br>:class:\`~sklearn.svm.LinearSVC\`.  <br>If using Leave-One-Out cross-validation, alphas must be strictly positive.  <br>  <br>For an example on how regularization strength affects the model coefficients,  <br>see :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_ridge\_coeffs.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alphas,-array-like%20of%20shape%20%28n_alphas%2C%29%2C%20default%3D%280.1%2C%201.0%2C%2010.0%29) | array(\[1.0000...00000000e+06\]) |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to calculate the intercept for this model. If set  <br>to false, no intercept will be used in calculations  <br>(i.e. data is expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [scoring scoring: str, callable, default=None  <br>  <br>The scoring method to use for cross-validation. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: negative :ref:\`mean squared error <mean\_squared\_error>\` if cv is  <br>None (i.e. when using leave-one-out cross-validation), or  <br>:ref:\`coefficient of determination <r2\_score>\` (:math:\`R^2\`) otherwise.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=scoring,-str%2C%20callable%2C%20default%3DNone) | None |\
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the efficient Leave-One-Out cross-validation  <br>\- integer, to specify the number of folds,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if \`\`y\`\` is binary or multiclass,  <br>:class:\`~sklearn.model\_selection.StratifiedKFold\` is used, else,  <br>:class:\`~sklearn.model\_selection.KFold\` is used.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |\
|     | [gcv\_mode gcv\_mode: {'auto', 'svd', 'eigen'}, default='auto'  <br>  <br>Flag indicating which strategy to use when performing  <br>Leave-One-Out Cross-Validation. Options are::  <br>  <br>'auto' : same as 'eigen'  <br>'svd' : use singular value decomposition of X when X is dense,  <br>fallback to 'eigen' when X is sparse  <br>'eigen' : use eigendecomposition of X X' when n\_samples <= n\_features  <br>or X' X when n\_features < n\_samples  <br>  <br>The 'auto' mode is the default and is intended to pick the cheaper  <br>option depending on the shape and sparsity of the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=gcv_mode,-%7B%27auto%27%2C%20%27svd%27%2C%20%27eigen%27%7D%2C%20default%3D%27auto%27) | None |\
|     | [store\_cv\_results store\_cv\_results: bool, default=False  <br>  <br>Flag indicating if the cross-validation values corresponding to  <br>each alpha should be stored in the \`\`cv\_results\_\`\` attribute (see  <br>below). This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionchanged:: 1.5  <br>Parameter name changed from \`store\_cv\_values\` to \`store\_cv\_results\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=store_cv_results,-bool%2C%20default%3DFalse) | False |\
|     | [alpha\_per\_target alpha\_per\_target: bool, default=False  <br>  <br>Flag indicating whether to optimize the alpha value (picked from the  <br>\`alphas\` parameter list) for each target separately (for multi-output  <br>settings: multiple prediction targets). When set to \`True\`, after  <br>fitting, the \`alpha\_\` attribute will contain a value for each target.  <br>When set to \`False\`, a single alpha is used for all targets.  <br>This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_per_target,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [alpha\_ alpha\_: float or ndarray of shape (n\_targets,)  <br>  <br>Estimated regularization parameter, or, if \`\`alpha\_per\_target=True\`\`,  <br>the estimated regularization parameter for each target.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float | 3.162 |\
| [best\_score\_ best\_score\_: float or ndarray of shape (n\_targets,)  <br>  <br>Score of base estimator with best alpha, or, if  <br>\`\`alpha\_per\_target=True\`\`, a score for each target.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=best_score_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | \-0.01722 |\
| [coef\_ coef\_: ndarray of shape (n\_features) or (n\_targets, n\_features)  <br>  <br>Weight vector(s).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=coef_,-ndarray%20of%20shape%20%28n_features%29%20or%20%28n_targets%2C%20n_features%29) | ndarray\[float64\](19,) | \[-0.03,-0.01, 0.01,..., 0.2 ,-0.16, 0.02\] |\
| [intercept\_ intercept\_: float or ndarray of shape (n\_targets,)  <br>  <br>Independent term in decision function. Set to 0.0 if  <br>\`\`fit\_intercept = False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=intercept_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | \-0.07789 |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=n_features_in_,-int) | int | 19  |\
\
  \
  \
\
It is affirmative to see that the selected `alpha_` is in our specified range.\
\
The performance is not good: the average error is around 14% of the maximum demand. This is more than three times higher than the average error of the gradient boosting model. We can suspect that the naive original encoding (merely min-max scaled) of the periodic time-related features might prevent the linear regression model to properly leverage the time information: linear regression does not automatically model non-monotonic relationships between the input features and the target. Non-linear terms have to be engineered in the input.\
\
For example, the raw numerical encoding of the `"hour"` feature prevents the linear model from recognizing that an increase of hour in the morning from 6 to 8 should have a strong positive impact on the number of bike rentals while an increase of similar magnitude in the evening from 18 to 20 should have a strong negative impact on the predicted number of bike rentals.\
\
Time-steps as categories[#](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#time-steps-as-categories "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Since the time features are encoded in a discrete manner using integers (24 unique values in the “hours” feature), we could decide to treat those as categorical variables using a one-hot encoding and thereby ignore any assumption implied by the ordering of the hour values.\
\
Using one-hot encoding for the time features gives the linear model a lot more flexibility as we introduce one additional feature per discrete time level.\
\
one\_hot\_linear\_pipeline \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
    [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")\
(\
        transformers\=\[\
            ("categorical", one\_hot\_encoder, categorical\_columns),\
            ("one\_hot\_time", one\_hot\_encoder, \["hour", "weekday", "month"\]),\
        \],\
        remainder\=[MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")\
(),\
        verbose\_feature\_names\_out\=False,\
    ),\
    [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")\
(alphas\=alphas),\
)\
\
evaluate(one\_hot\_linear\_pipeline, X, y, cv\=ts\_cv)\
\
Copy to clipboard\
\
Mean Absolute Error:     0.099 +/- 0.011\
Root Mean Squared Error: 0.131 +/- 0.011\
\
Copy to clipboard\
\
Pipeline(steps=\[('columntransformer',\
                 ColumnTransformer(remainder=MinMaxScaler(),\
                                   transformers=\[('categorical',\
                                                  OneHotEncoder(handle\_unknown='ignore',\
                                                                sparse\_output=False),\
                                                  Index(\['season', 'holiday', 'workingday', 'weather'\], dtype='str')),\
                                                 ('one\_hot\_time',\
                                                  OneHotEncoder(handle\_unknown='ignore',\
                                                                sparse\_output=False),\
                                                  \['hour', 'weekday',\
                                                   'month'\])\],\
                                   verbose\_featur...\
                 RidgeCV(alphas=array(\[1.00000000e-06, 3.16227766e-06, 1.00000000e-05, 3.16227766e-05,\
       1.00000000e-04, 3.16227766e-04, 1.00000000e-03, 3.16227766e-03,\
       1.00000000e-02, 3.16227766e-02, 1.00000000e-01, 3.16227766e-01,\
       1.00000000e+00, 3.16227766e+00, 1.00000000e+01, 3.16227766e+01,\
       1.00000000e+02, 3.16227766e+02, 1.00000000e+03, 3.16227766e+03,\
       1.00000000e+04, 3.16227766e+04, 1.00000000e+05, 3.16227766e+05,\
       1.00000000e+06\])))\])\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
Pipeline\
\
[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)\
iFitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('columntransformer', ...), ('ridgecv', ...)\] |\
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |\
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 12  |\
\
columntransformer: ColumnTransformer\
\
[?Documentation for columntransformer: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('categorical', ...), ('one\_hot\_time', ...)\] |\
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | MinMaxScaler() |\
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | False |\
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 12  |\
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'categorical...inMaxScaler()} |\
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'ca...al': slice(0, 11, None), 'on...me': slice(11, 54, None), 're...er': slice(54, 59, None)} |\
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |\
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('ca...al', OneHotEncoder...\_output=False), Index(\['seaso..., dtype='str')), ('on...me', OneHotEncoder...\_output=False), \['hour', 'weekday', 'month'\]), ('re...er', MinMaxScaler(), \['year', 'temp', 'fe...mp', 'hu...ty', ...\])\] |\
\
categorical\
\
Index(\['season', 'holiday', 'workingday', 'weather'\], dtype='str')\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | False |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\['fall'... dtype=object), array(\['False... dtype=object), array(\['False... dtype=object), array(\['clear... dtype=object)\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](4,) | \['season','holiday','workingday','weather'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 4   |\
\
11 features\
\
|     |\
| --- |\
| season\_fall |\
| season\_spring |\
| season\_summer |\
| season\_winter |\
| holiday\_False |\
| holiday\_True |\
| workingday\_False |\
| workingday\_True |\
| weather\_clear |\
| weather\_misty |\
| weather\_rain |\
\
one\_hot\_time\
\
\['hour', 'weekday', 'month'\]\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | False |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\[ 0, 1..., 21, 22, 23\]), array(\[0, 1, 2, 3, 4, 5, 6\]), array(\[ 1, 2..., 10, 11, 12\])\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](3,) | \['hour','weekday','month'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 3   |\
\
43 features\
\
|     |\
| --- |\
| hour\_0 |\
| hour\_1 |\
| hour\_2 |\
| hour\_3 |\
| hour\_4 |\
| hour\_5 |\
| hour\_6 |\
| hour\_7 |\
| hour\_8 |\
| hour\_9 |\
| hour\_10 |\
| hour\_11 |\
| hour\_12 |\
| hour\_13 |\
| hour\_14 |\
| hour\_15 |\
| hour\_16 |\
| hour\_17 |\
| hour\_18 |\
| hour\_19 |\
| hour\_20 |\
| hour\_21 |\
| hour\_22 |\
| hour\_23 |\
| weekday\_0 |\
| weekday\_1 |\
| weekday\_2 |\
| weekday\_3 |\
| weekday\_4 |\
| weekday\_5 |\
| weekday\_6 |\
| month\_1 |\
| month\_2 |\
| month\_3 |\
| month\_4 |\
| month\_5 |\
| month\_6 |\
| month\_7 |\
| month\_8 |\
| month\_9 |\
| month\_10 |\
| month\_11 |\
| month\_12 |\
\
remainder\
\
\['year', 'temp', 'feel\_temp', 'humidity', 'windspeed'\]\
\
MinMaxScaler\
\
[?Documentation for MinMaxScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [feature\_range feature\_range: tuple (min, max), default=(0, 1)  <br>  <br>Desired range of transformed data.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=feature_range,-tuple%20%28min%2C%20max%29%2C%20default%3D%280%2C%201%29) | (0, ...) |\
|     | [copy copy: bool, default=True  <br>  <br>Set to False to perform inplace row normalization and avoid a  <br>copy (if the input is already a numpy array).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [clip clip: bool, default=False  <br>  <br>Set to True to clip transformed values of held-out data to  <br>provided \`feature\_range\`.  <br>Since this parameter will clip values, \`inverse\_transform\` may not  <br>be able to restore the original data.  <br>  <br>.. note::  <br>Setting \`clip=True\` does not prevent feature drift (a distribution  <br>shift between training and test data). The transformed values are clipped  <br>to the \`feature\_range\`, which helps avoid unintended behavior in models  <br>sensitive to out-of-range inputs (e.g. linear models). Use with care,  <br>as clipping can distort the distribution of test data.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=clip,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [data\_max\_ data\_max\_: ndarray of shape (n\_features,)  <br>  <br>Per feature maximum seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_max\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_max_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 1. ,39.36,50. , 1. ,57. \] |\
| [data\_min\_ data\_min\_: ndarray of shape (n\_features,)  <br>  <br>Per feature minimum seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_min\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_min_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[0. ,0.82,0.76,0.16,0. \] |\
| [data\_range\_ data\_range\_: ndarray of shape (n\_features,)  <br>  <br>Per feature range \`\`(data\_max\_ - data\_min\_)\`\` seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_range\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_range_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 1. ,38.54,49.24, 0.84,57. \] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](5,) | \['year','temp','feel\_temp','humidity','windspeed'\] |\
| [min\_ min\_: ndarray of shape (n\_features,)  <br>  <br>Per feature adjustment for minimum. Equivalent to  <br>\`\`min - X.min(axis=0) \* self.scale\_\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=min_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 0. ,-0.02,-0.02,-0.19, 0. \] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=n_features_in_,-int) | int | 5   |\
| [n\_samples\_seen\_ n\_samples\_seen\_: int  <br>  <br>The number of samples processed by the estimator.  <br>It will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=n_samples_seen_,-int) | int | 10000 |\
| [scale\_ scale\_: ndarray of shape (n\_features,)  <br>  <br>Per feature relative scaling of the data. Equivalent to  <br>\`\`(max - min) / (X.max(axis=0) - X.min(axis=0))\`\`  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\* attribute.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[1. ,0.03,0.02,1.19,0.02\] |\
\
5 features\
\
|     |\
| --- |\
| year |\
| temp |\
| feel\_temp |\
| humidity |\
| windspeed |\
\
59 features\
\
|     |\
| --- |\
| season\_fall |\
| season\_spring |\
| season\_summer |\
| season\_winter |\
| holiday\_False |\
| holiday\_True |\
| workingday\_False |\
| workingday\_True |\
| weather\_clear |\
| weather\_misty |\
| weather\_rain |\
| hour\_0 |\
| hour\_1 |\
| hour\_2 |\
| hour\_3 |\
| hour\_4 |\
| hour\_5 |\
| hour\_6 |\
| hour\_7 |\
| hour\_8 |\
| hour\_9 |\
| hour\_10 |\
| hour\_11 |\
| hour\_12 |\
| hour\_13 |\
| hour\_14 |\
| hour\_15 |\
| hour\_16 |\
| hour\_17 |\
| hour\_18 |\
| hour\_19 |\
| hour\_20 |\
| hour\_21 |\
| hour\_22 |\
| hour\_23 |\
| weekday\_0 |\
| weekday\_1 |\
| weekday\_2 |\
| weekday\_3 |\
| weekday\_4 |\
| weekday\_5 |\
| weekday\_6 |\
| month\_1 |\
| month\_2 |\
| month\_3 |\
| month\_4 |\
| month\_5 |\
| month\_6 |\
| month\_7 |\
| month\_8 |\
| month\_9 |\
| month\_10 |\
| month\_11 |\
| month\_12 |\
| year |\
| temp |\
| feel\_temp |\
| humidity |\
| windspeed |\
\
RidgeCV\
\
[?Documentation for RidgeCV](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [alphas alphas: array-like of shape (n\_alphas,), default=(0.1, 1.0, 10.0)  <br>  <br>Array of alpha values to try.  <br>Regularization strength; must be a positive float. Regularization  <br>improves the conditioning of the problem and reduces the variance of  <br>the estimates. Larger values specify stronger regularization.  <br>Alpha corresponds to \`\`1 / (2C)\`\` in other linear models such as  <br>:class:\`~sklearn.linear\_model.LogisticRegression\` or  <br>:class:\`~sklearn.svm.LinearSVC\`.  <br>If using Leave-One-Out cross-validation, alphas must be strictly positive.  <br>  <br>For an example on how regularization strength affects the model coefficients,  <br>see :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_ridge\_coeffs.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alphas,-array-like%20of%20shape%20%28n_alphas%2C%29%2C%20default%3D%280.1%2C%201.0%2C%2010.0%29) | array(\[1.0000...00000000e+06\]) |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to calculate the intercept for this model. If set  <br>to false, no intercept will be used in calculations  <br>(i.e. data is expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [scoring scoring: str, callable, default=None  <br>  <br>The scoring method to use for cross-validation. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: negative :ref:\`mean squared error <mean\_squared\_error>\` if cv is  <br>None (i.e. when using leave-one-out cross-validation), or  <br>:ref:\`coefficient of determination <r2\_score>\` (:math:\`R^2\`) otherwise.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=scoring,-str%2C%20callable%2C%20default%3DNone) | None |\
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the efficient Leave-One-Out cross-validation  <br>\- integer, to specify the number of folds,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if \`\`y\`\` is binary or multiclass,  <br>:class:\`~sklearn.model\_selection.StratifiedKFold\` is used, else,  <br>:class:\`~sklearn.model\_selection.KFold\` is used.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |\
|     | [gcv\_mode gcv\_mode: {'auto', 'svd', 'eigen'}, default='auto'  <br>  <br>Flag indicating which strategy to use when performing  <br>Leave-One-Out Cross-Validation. Options are::  <br>  <br>'auto' : same as 'eigen'  <br>'svd' : use singular value decomposition of X when X is dense,  <br>fallback to 'eigen' when X is sparse  <br>'eigen' : use eigendecomposition of X X' when n\_samples <= n\_features  <br>or X' X when n\_features < n\_samples  <br>  <br>The 'auto' mode is the default and is intended to pick the cheaper  <br>option depending on the shape and sparsity of the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=gcv_mode,-%7B%27auto%27%2C%20%27svd%27%2C%20%27eigen%27%7D%2C%20default%3D%27auto%27) | None |\
|     | [store\_cv\_results store\_cv\_results: bool, default=False  <br>  <br>Flag indicating if the cross-validation values corresponding to  <br>each alpha should be stored in the \`\`cv\_results\_\`\` attribute (see  <br>below). This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionchanged:: 1.5  <br>Parameter name changed from \`store\_cv\_values\` to \`store\_cv\_results\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=store_cv_results,-bool%2C%20default%3DFalse) | False |\
|     | [alpha\_per\_target alpha\_per\_target: bool, default=False  <br>  <br>Flag indicating whether to optimize the alpha value (picked from the  <br>\`alphas\` parameter list) for each target separately (for multi-output  <br>settings: multiple prediction targets). When set to \`True\`, after  <br>fitting, the \`alpha\_\` attribute will contain a value for each target.  <br>When set to \`False\`, a single alpha is used for all targets.  <br>This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_per_target,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [alpha\_ alpha\_: float or ndarray of shape (n\_targets,)  <br>  <br>Estimated regularization parameter, or, if \`\`alpha\_per\_target=True\`\`,  <br>the estimated regularization parameter for each target.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float | 1   |\
| [best\_score\_ best\_score\_: float or ndarray of shape (n\_targets,)  <br>  <br>Score of base estimator with best alpha, or, if  <br>\`\`alpha\_per\_target=True\`\`, a score for each target.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=best_score_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | \-0.008231 |\
| [coef\_ coef\_: ndarray of shape (n\_features) or (n\_targets, n\_features)  <br>  <br>Weight vector(s).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=coef_,-ndarray%20of%20shape%20%28n_features%29%20or%20%28n_targets%2C%20n_features%29) | ndarray\[float64\](59,) | \[ 0.01,-0.03, 0. ,..., 0.18,-0.07,-0.04\] |\
| [intercept\_ intercept\_: float or ndarray of shape (n\_targets,)  <br>  <br>Independent term in decision function. Set to 0.0 if  <br>\`\`fit\_intercept = False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=intercept_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | 0.04408 |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=n_features_in_,-int) | int | 59  |\
\
  \
  \
\
The average error rate of this model is 10% which is much better than using the original (ordinal) encoding of the time feature, confirming our intuition that the linear regression model benefits from the added flexibility to not treat time progression in a monotonic manner.\
\
However, this introduces a very large number of new features. If the time of the day was represented in minutes since the start of the day instead of hours, one-hot encoding would have introduced 1440 features instead of 24. This could cause some significant overfitting. To avoid this we could use [`sklearn.preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")\
 instead to re-bin the number of levels of fine-grained ordinal or numerical variables while still benefitting from the non-monotonic expressivity advantages of one-hot encoding.\
\
Finally, we also observe that one-hot encoding completely ignores the ordering of the hour levels while this could be an interesting inductive bias to preserve to some level. In the following we try to explore smooth, non-monotonic encoding that locally preserves the relative ordering of time features.\
\
Trigonometric features[#](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#trigonometric-features "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
As a first attempt, we can try to encode each of those periodic features using a sine and cosine transformation with the matching period.\
\
Each ordinal time feature is transformed into 2 features that together encode equivalent information in a non-monotonic way, and more importantly without any jump between the first and the last value of the periodic range.\
\
from sklearn.preprocessing import [FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")\
\
def sin\_transformer(period):\
    return [FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")\
(\
        lambda x: [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")\
(x / period \* 2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")\
), feature\_names\_out\="one-to-one"\
    )\
\
def cos\_transformer(period):\
    return [FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")\
(\
        lambda x: [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")\
(x / period \* 2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")\
), feature\_names\_out\="one-to-one"\
    )\
\
Copy to clipboard\
\
Let us visualize the effect of this feature expansion on some synthetic hour data with a bit of extrapolation beyond hour=23:\
\
import pandas as pd\
\
hour\_df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
(26).reshape(\-1, 1),\
    columns\=\["hour"\],\
)\
hour\_df\["hour\_sin"\] \= sin\_transformer(24).fit\_transform(hour\_df)\["hour"\]\
hour\_df\["hour\_cos"\] \= cos\_transformer(24).fit\_transform(hour\_df)\["hour"\]\
hour\_df.plot(x\="hour")\
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Trigonometric encoding for the 'hour' feature")\
\
Copy to clipboard\
\
![Trigonometric encoding for the 'hour' feature](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_003.png)\
\
Let’s use a 2D scatter plot with the hours encoded as colors to better see how this representation maps the 24 hours of the day to a 2D space, akin to some sort of a 24 hour version of an analog clock. Note that the “25th” hour is mapped back to the 1st hour because of the periodic nature of the sine/cosine representation.\
\
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(7, 5))\
sp \= ax.scatter(hour\_df\["hour\_sin"\], hour\_df\["hour\_cos"\], c\=hour\_df\["hour"\])\
ax.set(\
    xlabel\="sin(hour)",\
    ylabel\="cos(hour)",\
)\
\_ \= fig.colorbar(sp)\
\
Copy to clipboard\
\
![plot cyclical feature engineering](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_004.png)\
\
We can now build a feature extraction pipeline using this strategy:\
\
cyclic\_cossin\_transformer \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")\
(\
    transformers\=\[\
        ("categorical", one\_hot\_encoder, categorical\_columns),\
        ("month\_sin", sin\_transformer(12), \["month"\]),\
        ("month\_cos", cos\_transformer(12), \["month"\]),\
        ("weekday\_sin", sin\_transformer(7), \["weekday"\]),\
        ("weekday\_cos", cos\_transformer(7), \["weekday"\]),\
        ("hour\_sin", sin\_transformer(24), \["hour"\]),\
        ("hour\_cos", cos\_transformer(24), \["hour"\]),\
    \],\
    remainder\=[MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")\
(),\
    verbose\_feature\_names\_out\=True,\
)\
cyclic\_cossin\_linear\_pipeline \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
    cyclic\_cossin\_transformer,\
    [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")\
(alphas\=alphas),\
)\
evaluate(cyclic\_cossin\_linear\_pipeline, X, y, cv\=ts\_cv)\
\
Copy to clipboard\
\
Mean Absolute Error:     0.125 +/- 0.014\
Root Mean Squared Error: 0.166 +/- 0.020\
\
Copy to clipboard\
\
Pipeline(steps=\[('columntransformer',\
                 ColumnTransformer(remainder=MinMaxScaler(),\
                                   transformers=\[('categorical',\
                                                  OneHotEncoder(handle\_unknown='ignore',\
                                                                sparse\_output=False),\
                                                  Index(\['season', 'holiday', 'workingday', 'weather'\], dtype='str')),\
                                                 ('month\_sin',\
                                                  FunctionTransformer(feature\_names\_out='one-to-one',\
                                                                      func=<function sin\_transformer.<locals>.<lambda> at 0x7e1...\
                 RidgeCV(alphas=array(\[1.00000000e-06, 3.16227766e-06, 1.00000000e-05, 3.16227766e-05,\
       1.00000000e-04, 3.16227766e-04, 1.00000000e-03, 3.16227766e-03,\
       1.00000000e-02, 3.16227766e-02, 1.00000000e-01, 3.16227766e-01,\
       1.00000000e+00, 3.16227766e+00, 1.00000000e+01, 3.16227766e+01,\
       1.00000000e+02, 3.16227766e+02, 1.00000000e+03, 3.16227766e+03,\
       1.00000000e+04, 3.16227766e+04, 1.00000000e+05, 3.16227766e+05,\
       1.00000000e+06\])))\])\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
Pipeline\
\
[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)\
iFitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('columntransformer', ...), ('ridgecv', ...)\] |\
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |\
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 12  |\
\
columntransformer: ColumnTransformer\
\
[?Documentation for columntransformer: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('categorical', ...), ('month\_sin', ...), ...\] |\
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | MinMaxScaler() |\
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | True |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 12  |\
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'categorical...inMaxScaler()} |\
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'ca...al': slice(0, 11, None), 'ho...os': slice(16, 17, None), 'ho...in': slice(15, 16, None), 'mo...os': slice(12, 13, None), ...} |\
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |\
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('ca...al', OneHotEncoder...\_output=False), Index(\['seaso..., dtype='str')), ('mo...in', FunctionTrans...7e1dbc43da60>), \['month'\]), ('mo...os', FunctionTrans...7e1dbc43db10>), \['month'\]), ('we...in', FunctionTrans...7e1dbc43dbc0>), \['weekday'\]), ...\] |\
\
categorical\
\
Index(\['season', 'holiday', 'workingday', 'weather'\], dtype='str')\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | False |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\['fall'... dtype=object), array(\['False... dtype=object), array(\['False... dtype=object), array(\['clear... dtype=object)\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](4,) | \['season','holiday','workingday','weather'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 4   |\
\
11 features\
\
|     |\
| --- |\
| season\_fall |\
| season\_spring |\
| season\_summer |\
| season\_winter |\
| holiday\_False |\
| holiday\_True |\
| workingday\_False |\
| workingday\_True |\
| weather\_clear |\
| weather\_misty |\
| weather\_rain |\
\
month\_sin\
\
\['month'\]\
\
<lambda>\
\
FunctionTransformer\
\
[?Documentation for FunctionTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [func func: callable, default=None  <br>  <br>The callable to use for the transformation. This will be passed  <br>the same arguments as transform, with args and kwargs forwarded.  <br>If func is None, then func will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=func,-callable%2C%20default%3DNone) | <function sin...x7e1dbc43da60> |\
|     | [feature\_names\_out feature\_names\_out: callable, 'one-to-one' or None, default=None  <br>  <br>Determines the list of feature names that will be returned by the  <br>\`get\_feature\_names\_out\` method. If it is 'one-to-one', then the output  <br>feature names will be equal to the input feature names. If it is a  <br>callable, then it must take two positional arguments: this  <br>\`FunctionTransformer\` (\`self\`) and an array-like of input feature names  <br>(\`input\_features\`). It must return an array-like of output feature  <br>names. The \`get\_feature\_names\_out\` method is only defined if  <br>\`feature\_names\_out\` is not None.  <br>  <br>See \`\`get\_feature\_names\_out\`\` for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_out,-callable%2C%20%27one-to-one%27%20or%20None%2C%20default%3DNone) | 'one-to-one' |\
|     | [inverse\_func inverse\_func: callable, default=None  <br>  <br>The callable to use for the inverse transformation. This will be  <br>passed the same arguments as inverse transform, with args and  <br>kwargs forwarded. If inverse\_func is None, then inverse\_func  <br>will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inverse_func,-callable%2C%20default%3DNone) | None |\
|     | [validate validate: bool, default=False  <br>  <br>Indicate that the input X array should be checked before calling  <br>\`\`func\`\`. The possibilities are:  <br>  <br>\- If False, there is no input validation.  <br>\- If True, then X will be converted to a 2-dimensional NumPy array or  <br>sparse matrix. If the conversion is not possible an exception is  <br>raised.  <br>  <br>.. versionchanged:: 0.22  <br>The default of \`\`validate\`\` changed from True to False.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=validate,-bool%2C%20default%3DFalse) | False |\
|     | [accept\_sparse accept\_sparse: bool, default=False  <br>  <br>Indicate that func accepts a sparse matrix as input. If validate is  <br>False, this has no effect. Otherwise, if accept\_sparse is false,  <br>sparse matrix inputs will cause an exception to be raised.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=accept_sparse,-bool%2C%20default%3DFalse) | False |\
|     | [check\_inverse check\_inverse: bool, default=True  <br>  <br>Whether to check that or \`\`func\`\` followed by \`\`inverse\_func\`\` leads to  <br>the original inputs. It can be used for a sanity check, raising a  <br>warning when the condition is not fulfilled.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=check_inverse,-bool%2C%20default%3DTrue) | True |\
|     | [kw\_args kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=kw_args,-dict%2C%20default%3DNone) | None |\
|     | [inv\_kw\_args inv\_kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to inverse\_func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inv_kw_args,-dict%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\` has feature  <br>names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['month'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
\
1 feature\
\
month\
\
month\_cos\
\
\['month'\]\
\
<lambda>\
\
FunctionTransformer\
\
[?Documentation for FunctionTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [func func: callable, default=None  <br>  <br>The callable to use for the transformation. This will be passed  <br>the same arguments as transform, with args and kwargs forwarded.  <br>If func is None, then func will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=func,-callable%2C%20default%3DNone) | <function cos...x7e1dbc43db10> |\
|     | [feature\_names\_out feature\_names\_out: callable, 'one-to-one' or None, default=None  <br>  <br>Determines the list of feature names that will be returned by the  <br>\`get\_feature\_names\_out\` method. If it is 'one-to-one', then the output  <br>feature names will be equal to the input feature names. If it is a  <br>callable, then it must take two positional arguments: this  <br>\`FunctionTransformer\` (\`self\`) and an array-like of input feature names  <br>(\`input\_features\`). It must return an array-like of output feature  <br>names. The \`get\_feature\_names\_out\` method is only defined if  <br>\`feature\_names\_out\` is not None.  <br>  <br>See \`\`get\_feature\_names\_out\`\` for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_out,-callable%2C%20%27one-to-one%27%20or%20None%2C%20default%3DNone) | 'one-to-one' |\
|     | [inverse\_func inverse\_func: callable, default=None  <br>  <br>The callable to use for the inverse transformation. This will be  <br>passed the same arguments as inverse transform, with args and  <br>kwargs forwarded. If inverse\_func is None, then inverse\_func  <br>will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inverse_func,-callable%2C%20default%3DNone) | None |\
|     | [validate validate: bool, default=False  <br>  <br>Indicate that the input X array should be checked before calling  <br>\`\`func\`\`. The possibilities are:  <br>  <br>\- If False, there is no input validation.  <br>\- If True, then X will be converted to a 2-dimensional NumPy array or  <br>sparse matrix. If the conversion is not possible an exception is  <br>raised.  <br>  <br>.. versionchanged:: 0.22  <br>The default of \`\`validate\`\` changed from True to False.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=validate,-bool%2C%20default%3DFalse) | False |\
|     | [accept\_sparse accept\_sparse: bool, default=False  <br>  <br>Indicate that func accepts a sparse matrix as input. If validate is  <br>False, this has no effect. Otherwise, if accept\_sparse is false,  <br>sparse matrix inputs will cause an exception to be raised.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=accept_sparse,-bool%2C%20default%3DFalse) | False |\
|     | [check\_inverse check\_inverse: bool, default=True  <br>  <br>Whether to check that or \`\`func\`\` followed by \`\`inverse\_func\`\` leads to  <br>the original inputs. It can be used for a sanity check, raising a  <br>warning when the condition is not fulfilled.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=check_inverse,-bool%2C%20default%3DTrue) | True |\
|     | [kw\_args kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=kw_args,-dict%2C%20default%3DNone) | None |\
|     | [inv\_kw\_args inv\_kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to inverse\_func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inv_kw_args,-dict%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\` has feature  <br>names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['month'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
\
1 feature\
\
month\
\
weekday\_sin\
\
\['weekday'\]\
\
<lambda>\
\
FunctionTransformer\
\
[?Documentation for FunctionTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [func func: callable, default=None  <br>  <br>The callable to use for the transformation. This will be passed  <br>the same arguments as transform, with args and kwargs forwarded.  <br>If func is None, then func will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=func,-callable%2C%20default%3DNone) | <function sin...x7e1dbc43dbc0> |\
|     | [feature\_names\_out feature\_names\_out: callable, 'one-to-one' or None, default=None  <br>  <br>Determines the list of feature names that will be returned by the  <br>\`get\_feature\_names\_out\` method. If it is 'one-to-one', then the output  <br>feature names will be equal to the input feature names. If it is a  <br>callable, then it must take two positional arguments: this  <br>\`FunctionTransformer\` (\`self\`) and an array-like of input feature names  <br>(\`input\_features\`). It must return an array-like of output feature  <br>names. The \`get\_feature\_names\_out\` method is only defined if  <br>\`feature\_names\_out\` is not None.  <br>  <br>See \`\`get\_feature\_names\_out\`\` for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_out,-callable%2C%20%27one-to-one%27%20or%20None%2C%20default%3DNone) | 'one-to-one' |\
|     | [inverse\_func inverse\_func: callable, default=None  <br>  <br>The callable to use for the inverse transformation. This will be  <br>passed the same arguments as inverse transform, with args and  <br>kwargs forwarded. If inverse\_func is None, then inverse\_func  <br>will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inverse_func,-callable%2C%20default%3DNone) | None |\
|     | [validate validate: bool, default=False  <br>  <br>Indicate that the input X array should be checked before calling  <br>\`\`func\`\`. The possibilities are:  <br>  <br>\- If False, there is no input validation.  <br>\- If True, then X will be converted to a 2-dimensional NumPy array or  <br>sparse matrix. If the conversion is not possible an exception is  <br>raised.  <br>  <br>.. versionchanged:: 0.22  <br>The default of \`\`validate\`\` changed from True to False.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=validate,-bool%2C%20default%3DFalse) | False |\
|     | [accept\_sparse accept\_sparse: bool, default=False  <br>  <br>Indicate that func accepts a sparse matrix as input. If validate is  <br>False, this has no effect. Otherwise, if accept\_sparse is false,  <br>sparse matrix inputs will cause an exception to be raised.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=accept_sparse,-bool%2C%20default%3DFalse) | False |\
|     | [check\_inverse check\_inverse: bool, default=True  <br>  <br>Whether to check that or \`\`func\`\` followed by \`\`inverse\_func\`\` leads to  <br>the original inputs. It can be used for a sanity check, raising a  <br>warning when the condition is not fulfilled.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=check_inverse,-bool%2C%20default%3DTrue) | True |\
|     | [kw\_args kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=kw_args,-dict%2C%20default%3DNone) | None |\
|     | [inv\_kw\_args inv\_kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to inverse\_func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inv_kw_args,-dict%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\` has feature  <br>names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['weekday'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
\
1 feature\
\
weekday\
\
weekday\_cos\
\
\['weekday'\]\
\
<lambda>\
\
FunctionTransformer\
\
[?Documentation for FunctionTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [func func: callable, default=None  <br>  <br>The callable to use for the transformation. This will be passed  <br>the same arguments as transform, with args and kwargs forwarded.  <br>If func is None, then func will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=func,-callable%2C%20default%3DNone) | <function cos...x7e1dbc43dc70> |\
|     | [feature\_names\_out feature\_names\_out: callable, 'one-to-one' or None, default=None  <br>  <br>Determines the list of feature names that will be returned by the  <br>\`get\_feature\_names\_out\` method. If it is 'one-to-one', then the output  <br>feature names will be equal to the input feature names. If it is a  <br>callable, then it must take two positional arguments: this  <br>\`FunctionTransformer\` (\`self\`) and an array-like of input feature names  <br>(\`input\_features\`). It must return an array-like of output feature  <br>names. The \`get\_feature\_names\_out\` method is only defined if  <br>\`feature\_names\_out\` is not None.  <br>  <br>See \`\`get\_feature\_names\_out\`\` for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_out,-callable%2C%20%27one-to-one%27%20or%20None%2C%20default%3DNone) | 'one-to-one' |\
|     | [inverse\_func inverse\_func: callable, default=None  <br>  <br>The callable to use for the inverse transformation. This will be  <br>passed the same arguments as inverse transform, with args and  <br>kwargs forwarded. If inverse\_func is None, then inverse\_func  <br>will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inverse_func,-callable%2C%20default%3DNone) | None |\
|     | [validate validate: bool, default=False  <br>  <br>Indicate that the input X array should be checked before calling  <br>\`\`func\`\`. The possibilities are:  <br>  <br>\- If False, there is no input validation.  <br>\- If True, then X will be converted to a 2-dimensional NumPy array or  <br>sparse matrix. If the conversion is not possible an exception is  <br>raised.  <br>  <br>.. versionchanged:: 0.22  <br>The default of \`\`validate\`\` changed from True to False.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=validate,-bool%2C%20default%3DFalse) | False |\
|     | [accept\_sparse accept\_sparse: bool, default=False  <br>  <br>Indicate that func accepts a sparse matrix as input. If validate is  <br>False, this has no effect. Otherwise, if accept\_sparse is false,  <br>sparse matrix inputs will cause an exception to be raised.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=accept_sparse,-bool%2C%20default%3DFalse) | False |\
|     | [check\_inverse check\_inverse: bool, default=True  <br>  <br>Whether to check that or \`\`func\`\` followed by \`\`inverse\_func\`\` leads to  <br>the original inputs. It can be used for a sanity check, raising a  <br>warning when the condition is not fulfilled.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=check_inverse,-bool%2C%20default%3DTrue) | True |\
|     | [kw\_args kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=kw_args,-dict%2C%20default%3DNone) | None |\
|     | [inv\_kw\_args inv\_kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to inverse\_func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inv_kw_args,-dict%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\` has feature  <br>names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['weekday'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
\
1 feature\
\
weekday\
\
hour\_sin\
\
\['hour'\]\
\
<lambda>\
\
FunctionTransformer\
\
[?Documentation for FunctionTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [func func: callable, default=None  <br>  <br>The callable to use for the transformation. This will be passed  <br>the same arguments as transform, with args and kwargs forwarded.  <br>If func is None, then func will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=func,-callable%2C%20default%3DNone) | <function sin...x7e1dbc43dd20> |\
|     | [feature\_names\_out feature\_names\_out: callable, 'one-to-one' or None, default=None  <br>  <br>Determines the list of feature names that will be returned by the  <br>\`get\_feature\_names\_out\` method. If it is 'one-to-one', then the output  <br>feature names will be equal to the input feature names. If it is a  <br>callable, then it must take two positional arguments: this  <br>\`FunctionTransformer\` (\`self\`) and an array-like of input feature names  <br>(\`input\_features\`). It must return an array-like of output feature  <br>names. The \`get\_feature\_names\_out\` method is only defined if  <br>\`feature\_names\_out\` is not None.  <br>  <br>See \`\`get\_feature\_names\_out\`\` for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_out,-callable%2C%20%27one-to-one%27%20or%20None%2C%20default%3DNone) | 'one-to-one' |\
|     | [inverse\_func inverse\_func: callable, default=None  <br>  <br>The callable to use for the inverse transformation. This will be  <br>passed the same arguments as inverse transform, with args and  <br>kwargs forwarded. If inverse\_func is None, then inverse\_func  <br>will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inverse_func,-callable%2C%20default%3DNone) | None |\
|     | [validate validate: bool, default=False  <br>  <br>Indicate that the input X array should be checked before calling  <br>\`\`func\`\`. The possibilities are:  <br>  <br>\- If False, there is no input validation.  <br>\- If True, then X will be converted to a 2-dimensional NumPy array or  <br>sparse matrix. If the conversion is not possible an exception is  <br>raised.  <br>  <br>.. versionchanged:: 0.22  <br>The default of \`\`validate\`\` changed from True to False.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=validate,-bool%2C%20default%3DFalse) | False |\
|     | [accept\_sparse accept\_sparse: bool, default=False  <br>  <br>Indicate that func accepts a sparse matrix as input. If validate is  <br>False, this has no effect. Otherwise, if accept\_sparse is false,  <br>sparse matrix inputs will cause an exception to be raised.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=accept_sparse,-bool%2C%20default%3DFalse) | False |\
|     | [check\_inverse check\_inverse: bool, default=True  <br>  <br>Whether to check that or \`\`func\`\` followed by \`\`inverse\_func\`\` leads to  <br>the original inputs. It can be used for a sanity check, raising a  <br>warning when the condition is not fulfilled.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=check_inverse,-bool%2C%20default%3DTrue) | True |\
|     | [kw\_args kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=kw_args,-dict%2C%20default%3DNone) | None |\
|     | [inv\_kw\_args inv\_kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to inverse\_func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inv_kw_args,-dict%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\` has feature  <br>names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['hour'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
\
1 feature\
\
hour\
\
hour\_cos\
\
\['hour'\]\
\
<lambda>\
\
FunctionTransformer\
\
[?Documentation for FunctionTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [func func: callable, default=None  <br>  <br>The callable to use for the transformation. This will be passed  <br>the same arguments as transform, with args and kwargs forwarded.  <br>If func is None, then func will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=func,-callable%2C%20default%3DNone) | <function cos...x7e1dbc43ddd0> |\
|     | [feature\_names\_out feature\_names\_out: callable, 'one-to-one' or None, default=None  <br>  <br>Determines the list of feature names that will be returned by the  <br>\`get\_feature\_names\_out\` method. If it is 'one-to-one', then the output  <br>feature names will be equal to the input feature names. If it is a  <br>callable, then it must take two positional arguments: this  <br>\`FunctionTransformer\` (\`self\`) and an array-like of input feature names  <br>(\`input\_features\`). It must return an array-like of output feature  <br>names. The \`get\_feature\_names\_out\` method is only defined if  <br>\`feature\_names\_out\` is not None.  <br>  <br>See \`\`get\_feature\_names\_out\`\` for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_out,-callable%2C%20%27one-to-one%27%20or%20None%2C%20default%3DNone) | 'one-to-one' |\
|     | [inverse\_func inverse\_func: callable, default=None  <br>  <br>The callable to use for the inverse transformation. This will be  <br>passed the same arguments as inverse transform, with args and  <br>kwargs forwarded. If inverse\_func is None, then inverse\_func  <br>will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inverse_func,-callable%2C%20default%3DNone) | None |\
|     | [validate validate: bool, default=False  <br>  <br>Indicate that the input X array should be checked before calling  <br>\`\`func\`\`. The possibilities are:  <br>  <br>\- If False, there is no input validation.  <br>\- If True, then X will be converted to a 2-dimensional NumPy array or  <br>sparse matrix. If the conversion is not possible an exception is  <br>raised.  <br>  <br>.. versionchanged:: 0.22  <br>The default of \`\`validate\`\` changed from True to False.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=validate,-bool%2C%20default%3DFalse) | False |\
|     | [accept\_sparse accept\_sparse: bool, default=False  <br>  <br>Indicate that func accepts a sparse matrix as input. If validate is  <br>False, this has no effect. Otherwise, if accept\_sparse is false,  <br>sparse matrix inputs will cause an exception to be raised.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=accept_sparse,-bool%2C%20default%3DFalse) | False |\
|     | [check\_inverse check\_inverse: bool, default=True  <br>  <br>Whether to check that or \`\`func\`\` followed by \`\`inverse\_func\`\` leads to  <br>the original inputs. It can be used for a sanity check, raising a  <br>warning when the condition is not fulfilled.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=check_inverse,-bool%2C%20default%3DTrue) | True |\
|     | [kw\_args kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=kw_args,-dict%2C%20default%3DNone) | None |\
|     | [inv\_kw\_args inv\_kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to inverse\_func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inv_kw_args,-dict%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\` has feature  <br>names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['hour'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
\
1 feature\
\
hour\
\
remainder\
\
\['year', 'temp', 'feel\_temp', 'humidity', 'windspeed'\]\
\
MinMaxScaler\
\
[?Documentation for MinMaxScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [feature\_range feature\_range: tuple (min, max), default=(0, 1)  <br>  <br>Desired range of transformed data.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=feature_range,-tuple%20%28min%2C%20max%29%2C%20default%3D%280%2C%201%29) | (0, ...) |\
|     | [copy copy: bool, default=True  <br>  <br>Set to False to perform inplace row normalization and avoid a  <br>copy (if the input is already a numpy array).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [clip clip: bool, default=False  <br>  <br>Set to True to clip transformed values of held-out data to  <br>provided \`feature\_range\`.  <br>Since this parameter will clip values, \`inverse\_transform\` may not  <br>be able to restore the original data.  <br>  <br>.. note::  <br>Setting \`clip=True\` does not prevent feature drift (a distribution  <br>shift between training and test data). The transformed values are clipped  <br>to the \`feature\_range\`, which helps avoid unintended behavior in models  <br>sensitive to out-of-range inputs (e.g. linear models). Use with care,  <br>as clipping can distort the distribution of test data.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=clip,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [data\_max\_ data\_max\_: ndarray of shape (n\_features,)  <br>  <br>Per feature maximum seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_max\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_max_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 1. ,39.36,50. , 1. ,57. \] |\
| [data\_min\_ data\_min\_: ndarray of shape (n\_features,)  <br>  <br>Per feature minimum seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_min\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_min_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[0. ,0.82,0.76,0.16,0. \] |\
| [data\_range\_ data\_range\_: ndarray of shape (n\_features,)  <br>  <br>Per feature range \`\`(data\_max\_ - data\_min\_)\`\` seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_range\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_range_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 1. ,38.54,49.24, 0.84,57. \] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](5,) | \['year','temp','feel\_temp','humidity','windspeed'\] |\
| [min\_ min\_: ndarray of shape (n\_features,)  <br>  <br>Per feature adjustment for minimum. Equivalent to  <br>\`\`min - X.min(axis=0) \* self.scale\_\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=min_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 0. ,-0.02,-0.02,-0.19, 0. \] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=n_features_in_,-int) | int | 5   |\
| [n\_samples\_seen\_ n\_samples\_seen\_: int  <br>  <br>The number of samples processed by the estimator.  <br>It will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=n_samples_seen_,-int) | int | 10000 |\
| [scale\_ scale\_: ndarray of shape (n\_features,)  <br>  <br>Per feature relative scaling of the data. Equivalent to  <br>\`\`(max - min) / (X.max(axis=0) - X.min(axis=0))\`\`  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\* attribute.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[1. ,0.03,0.02,1.19,0.02\] |\
\
5 features\
\
|     |\
| --- |\
| year |\
| temp |\
| feel\_temp |\
| humidity |\
| windspeed |\
\
22 features\
\
|     |\
| --- |\
| categorical\_\_season\_fall |\
| categorical\_\_season\_spring |\
| categorical\_\_season\_summer |\
| categorical\_\_season\_winter |\
| categorical\_\_holiday\_False |\
| categorical\_\_holiday\_True |\
| categorical\_\_workingday\_False |\
| categorical\_\_workingday\_True |\
| categorical\_\_weather\_clear |\
| categorical\_\_weather\_misty |\
| categorical\_\_weather\_rain |\
| month\_sin\_\_month |\
| month\_cos\_\_month |\
| weekday\_sin\_\_weekday |\
| weekday\_cos\_\_weekday |\
| hour\_sin\_\_hour |\
| hour\_cos\_\_hour |\
| remainder\_\_year |\
| remainder\_\_temp |\
| remainder\_\_feel\_temp |\
| remainder\_\_humidity |\
| remainder\_\_windspeed |\
\
RidgeCV\
\
[?Documentation for RidgeCV](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [alphas alphas: array-like of shape (n\_alphas,), default=(0.1, 1.0, 10.0)  <br>  <br>Array of alpha values to try.  <br>Regularization strength; must be a positive float. Regularization  <br>improves the conditioning of the problem and reduces the variance of  <br>the estimates. Larger values specify stronger regularization.  <br>Alpha corresponds to \`\`1 / (2C)\`\` in other linear models such as  <br>:class:\`~sklearn.linear\_model.LogisticRegression\` or  <br>:class:\`~sklearn.svm.LinearSVC\`.  <br>If using Leave-One-Out cross-validation, alphas must be strictly positive.  <br>  <br>For an example on how regularization strength affects the model coefficients,  <br>see :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_ridge\_coeffs.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alphas,-array-like%20of%20shape%20%28n_alphas%2C%29%2C%20default%3D%280.1%2C%201.0%2C%2010.0%29) | array(\[1.0000...00000000e+06\]) |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to calculate the intercept for this model. If set  <br>to false, no intercept will be used in calculations  <br>(i.e. data is expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [scoring scoring: str, callable, default=None  <br>  <br>The scoring method to use for cross-validation. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: negative :ref:\`mean squared error <mean\_squared\_error>\` if cv is  <br>None (i.e. when using leave-one-out cross-validation), or  <br>:ref:\`coefficient of determination <r2\_score>\` (:math:\`R^2\`) otherwise.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=scoring,-str%2C%20callable%2C%20default%3DNone) | None |\
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the efficient Leave-One-Out cross-validation  <br>\- integer, to specify the number of folds,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if \`\`y\`\` is binary or multiclass,  <br>:class:\`~sklearn.model\_selection.StratifiedKFold\` is used, else,  <br>:class:\`~sklearn.model\_selection.KFold\` is used.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |\
|     | [gcv\_mode gcv\_mode: {'auto', 'svd', 'eigen'}, default='auto'  <br>  <br>Flag indicating which strategy to use when performing  <br>Leave-One-Out Cross-Validation. Options are::  <br>  <br>'auto' : same as 'eigen'  <br>'svd' : use singular value decomposition of X when X is dense,  <br>fallback to 'eigen' when X is sparse  <br>'eigen' : use eigendecomposition of X X' when n\_samples <= n\_features  <br>or X' X when n\_features < n\_samples  <br>  <br>The 'auto' mode is the default and is intended to pick the cheaper  <br>option depending on the shape and sparsity of the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=gcv_mode,-%7B%27auto%27%2C%20%27svd%27%2C%20%27eigen%27%7D%2C%20default%3D%27auto%27) | None |\
|     | [store\_cv\_results store\_cv\_results: bool, default=False  <br>  <br>Flag indicating if the cross-validation values corresponding to  <br>each alpha should be stored in the \`\`cv\_results\_\`\` attribute (see  <br>below). This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionchanged:: 1.5  <br>Parameter name changed from \`store\_cv\_values\` to \`store\_cv\_results\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=store_cv_results,-bool%2C%20default%3DFalse) | False |\
|     | [alpha\_per\_target alpha\_per\_target: bool, default=False  <br>  <br>Flag indicating whether to optimize the alpha value (picked from the  <br>\`alphas\` parameter list) for each target separately (for multi-output  <br>settings: multiple prediction targets). When set to \`True\`, after  <br>fitting, the \`alpha\_\` attribute will contain a value for each target.  <br>When set to \`False\`, a single alpha is used for all targets.  <br>This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_per_target,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [alpha\_ alpha\_: float or ndarray of shape (n\_targets,)  <br>  <br>Estimated regularization parameter, or, if \`\`alpha\_per\_target=True\`\`,  <br>the estimated regularization parameter for each target.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float | 1   |\
| [best\_score\_ best\_score\_: float or ndarray of shape (n\_targets,)  <br>  <br>Score of base estimator with best alpha, or, if  <br>\`\`alpha\_per\_target=True\`\`, a score for each target.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=best_score_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | \-0.01384 |\
| [coef\_ coef\_: ndarray of shape (n\_features) or (n\_targets, n\_features)  <br>  <br>Weight vector(s).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=coef_,-ndarray%20of%20shape%20%28n_features%29%20or%20%28n_targets%2C%20n_features%29) | ndarray\[float64\](22,) | \[-0. ,-0.04, 0.01,..., 0.18,-0.03,-0.03\] |\
| [intercept\_ intercept\_: float or ndarray of shape (n\_targets,)  <br>  <br>Independent term in decision function. Set to 0.0 if  <br>\`\`fit\_intercept = False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=intercept_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | 0.04623 |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=n_features_in_,-int) | int | 22  |\
\
  \
  \
\
The performance of our linear regression model with this simple feature engineering is a bit better than using the original ordinal time features but worse than using the one-hot encoded time features. We will further analyze possible reasons for this disappointing outcome at the end of this notebook.\
\
Periodic spline features[#](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#periodic-spline-features "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
We can try an alternative encoding of the periodic time-related features using spline transformations with a large enough number of splines, and as a result a larger number of expanded features compared to the sine/cosine transformation:\
\
from sklearn.preprocessing import [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")\
\
def periodic\_spline\_transformer(period, n\_splines\=None, degree\=3):\
    if n\_splines is None:\
        n\_splines \= period\
    n\_knots \= n\_splines + 1  \# periodic and include\_bias is True\
    return [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")\
(\
        degree\=degree,\
        n\_knots\=n\_knots,\
        knots\=[np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
(0, period, n\_knots).reshape(n\_knots, 1),\
        extrapolation\="periodic",\
        include\_bias\=True,\
    )\
\
Copy to clipboard\
\
Again, let us visualize the effect of this feature expansion on some synthetic hour data with a bit of extrapolation beyond hour=23:\
\
hour\_df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
(0, 26, 1000).reshape(\-1, 1),\
    columns\=\["hour"\],\
)\
splines \= periodic\_spline\_transformer(24, n\_splines\=12).fit\_transform(hour\_df)\
splines\_df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    splines,\
    columns\=\[f"spline\_{i}" for i in range(splines.shape\[1\])\],\
)\
[pd.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html#pandas.concat "pandas.concat")\
(\[hour\_df, splines\_df\], axis\="columns").plot(x\="hour", cmap\=plt.cm.tab20b)\
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Periodic spline-based encoding for the 'hour' feature")\
\
Copy to clipboard\
\
![Periodic spline-based encoding for the 'hour' feature](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_005.png)\
\
Thanks to the use of the `extrapolation="periodic"` parameter, we observe that the feature encoding stays smooth when extrapolating beyond midnight.\
\
We can now build a predictive pipeline using this alternative periodic feature engineering strategy.\
\
It is possible to use fewer splines than discrete levels for those ordinal values. This makes spline-based encoding more efficient than one-hot encoding while preserving most of the expressivity:\
\
cyclic\_spline\_transformer \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")\
(\
    transformers\=\[\
        ("categorical", one\_hot\_encoder, categorical\_columns),\
        ("cyclic\_month", periodic\_spline\_transformer(12, n\_splines\=6), \["month"\]),\
        ("cyclic\_weekday", periodic\_spline\_transformer(7, n\_splines\=3), \["weekday"\]),\
        ("cyclic\_hour", periodic\_spline\_transformer(24, n\_splines\=12), \["hour"\]),\
    \],\
    remainder\=[MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")\
(),\
    verbose\_feature\_names\_out\=False,\
)\
cyclic\_spline\_linear\_pipeline \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
    cyclic\_spline\_transformer,\
    [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")\
(alphas\=alphas),\
)\
evaluate(cyclic\_spline\_linear\_pipeline, X, y, cv\=ts\_cv)\
\
Copy to clipboard\
\
Mean Absolute Error:     0.097 +/- 0.011\
Root Mean Squared Error: 0.132 +/- 0.013\
\
Copy to clipboard\
\
Pipeline(steps=\[('columntransformer',\
                 ColumnTransformer(remainder=MinMaxScaler(),\
                                   transformers=\[('categorical',\
                                                  OneHotEncoder(handle\_unknown='ignore',\
                                                                sparse\_output=False),\
                                                  Index(\['season', 'holiday', 'workingday', 'weather'\], dtype='str')),\
                                                 ('cyclic\_month',\
                                                  SplineTransformer(extrapolation='periodic',\
                                                                    knots=array(\[\[ 0.\],\
       \[ 2.\],\
       \[ 4.\],\
       \[ 6.\],\
       \[ 8.\],\
       \[10.\],\
       \[12.\]\]),\
                                                                    n\_knots...\
                 RidgeCV(alphas=array(\[1.00000000e-06, 3.16227766e-06, 1.00000000e-05, 3.16227766e-05,\
       1.00000000e-04, 3.16227766e-04, 1.00000000e-03, 3.16227766e-03,\
       1.00000000e-02, 3.16227766e-02, 1.00000000e-01, 3.16227766e-01,\
       1.00000000e+00, 3.16227766e+00, 1.00000000e+01, 3.16227766e+01,\
       1.00000000e+02, 3.16227766e+02, 1.00000000e+03, 3.16227766e+03,\
       1.00000000e+04, 3.16227766e+04, 1.00000000e+05, 3.16227766e+05,\
       1.00000000e+06\])))\])\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
Pipeline\
\
[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)\
iFitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('columntransformer', ...), ('ridgecv', ...)\] |\
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |\
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 12  |\
\
columntransformer: ColumnTransformer\
\
[?Documentation for columntransformer: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('categorical', ...), ('cyclic\_month', ...), ...\] |\
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | MinMaxScaler() |\
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | False |\
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 12  |\
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'categorical...inMaxScaler()} |\
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'ca...al': slice(0, 11, None), 'cy...ur': slice(20, 32, None), 'cy...th': slice(11, 17, None), 'cy...ay': slice(17, 20, None), ...} |\
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |\
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('ca...al', OneHotEncoder...\_output=False), Index(\['seaso..., dtype='str')), ('cy...th', SplineTransfo... n\_knots=7), \['month'\]), ('cy...ay', SplineTransfo... n\_knots=4), \['weekday'\]), ('cy...ur', SplineTransfo... n\_knots=13), \['hour'\]), ...\] |\
\
categorical\
\
Index(\['season', 'holiday', 'workingday', 'weather'\], dtype='str')\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | False |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\['fall'... dtype=object), array(\['False... dtype=object), array(\['False... dtype=object), array(\['clear... dtype=object)\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](4,) | \['season','holiday','workingday','weather'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 4   |\
\
11 features\
\
|     |\
| --- |\
| season\_fall |\
| season\_spring |\
| season\_summer |\
| season\_winter |\
| holiday\_False |\
| holiday\_True |\
| workingday\_False |\
| workingday\_True |\
| weather\_clear |\
| weather\_misty |\
| weather\_rain |\
\
cyclic\_month\
\
\['month'\]\
\
SplineTransformer\
\
[?Documentation for SplineTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [n\_knots n\_knots: int, default=5  <br>  <br>Number of knots of the splines if \`knots\` equals one of  <br>{'uniform', 'quantile'}. Must be larger or equal 2. Ignored if \`knots\`  <br>is array-like.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_knots,-int%2C%20default%3D5) | 7   |\
|     | [knots knots: {'uniform', 'quantile'} or array-like of shape (n\_knots, n\_features), default='uniform'  <br>  <br>Set knot positions such that first knot <= features <= last knot.  <br>  <br>\- If 'uniform', \`n\_knots\` number of knots are distributed uniformly  <br>from min to max values of the features.  <br>\- If 'quantile', they are distributed uniformly along the quantiles of  <br>the features.  <br>\- If an array-like is given, it directly specifies the sorted knot  <br>positions including the boundary knots. Note that, internally,  <br>\`degree\` number of knots are added before the first knot, the same  <br>after the last knot.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=knots,-int%2C%20default%3D5) | array(\[\[ 0.\],... \[12.\]\]) |\
|     | [extrapolation extrapolation: {'error', 'constant', 'linear', 'continue', 'periodic'}, default='constant'  <br>  <br>If 'error', values outside the min and max values of the training  <br>features raises a \`ValueError\`. If 'constant', the value of the  <br>splines at minimum and maximum value of the features is used as  <br>constant extrapolation. If 'linear', a linear extrapolation is used.  <br>If 'continue', the splines are extrapolated as is, i.e. option  <br>\`extrapolate=True\` in :class:\`scipy.interpolate.BSpline\`. If  <br>'periodic', periodic splines with a periodicity equal to the distance  <br>between the first and last knot are used. Periodic splines enforce  <br>equal function values and derivatives at the first and last knot.  <br>For example, this makes it possible to avoid introducing an arbitrary  <br>jump between Dec 31st and Jan 1st in spline features derived from a  <br>naturally periodic "day-of-year" input feature. In this case it is  <br>recommended to manually set the knot values to control the period.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=extrapolation,-%7B%27error%27%2C%20%27constant%27%2C%20%27linear%27%2C%20%27continue%27%2C%20%27periodic%27%7D%2C%20%20%20%20%20%20%20%20%20default%3D%27constant%27) | 'periodic' |\
|     | [degree degree: int, default=3  <br>  <br>The polynomial degree of the spline basis. Must be a non-negative  <br>integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=degree,-int%2C%20default%3D3) | 3   |\
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If False, then the last spline element inside the data range  <br>of a feature is dropped. As B-splines sum to one over the spline basis  <br>functions for each data point, they implicitly include a bias term,  <br>i.e. a column of ones. It acts as an intercept term in a linear models.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |\
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to compute, but  <br>may slow down subsequent estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |\
|     | [handle\_missing handle\_missing: {'error', 'zeros'}, default='error'  <br>  <br>Specifies the way missing values are handled.  <br>  <br>\- 'error' : Raise an error if \`np.nan\` values are present during :meth:\`fit\`.  <br>\- 'zeros' : Encode splines of missing values with values \`0\`.  <br>  <br>Note that \`handle\_missing='zeros'\` differs from first imputing missing values  <br>with zeros and then creating the spline basis. The latter creates spline basis  <br>functions which have non-zero values at the missing values  <br>whereas this option simply sets all spline basis function values to zero at the  <br>missing values.  <br>  <br>.. versionadded:: 1.8](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=handle_missing,-%7B%27error%27%2C%20%27zeros%27%7D%2C%20default%3D%27error%27) | 'error' |\
|     | [sparse\_output sparse\_output: bool, default=False  <br>  <br>Will return sparse CSR matrix if set True else will return an array.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=sparse_output,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [bsplines\_ bsplines\_: list of shape (n\_features,)  <br>  <br>List of BSplines objects, one for each feature.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=bsplines_,-list%20of%20shape%20%28n_features%2C%29) | list | \[<scipy.interp...x7e1dbc209cd0>\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['month'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>The total number of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
| [n\_features\_out\_ n\_features\_out\_: int  <br>  <br>The total number of output features, which is computed as  <br>\`n\_features \* n\_splines\`, where \`n\_splines\` is  <br>the number of bases elements of the B-splines,  <br>\`n\_knots + degree - 1\` for non-periodic splines and  <br>\`n\_knots - 1\` for periodic ones.  <br>If \`include\_bias=False\`, then it is only  <br>\`n\_features \* (n\_splines - 1)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_out_,-int) | int | 6   |\
\
6 features\
\
|     |\
| --- |\
| month\_sp\_0 |\
| month\_sp\_1 |\
| month\_sp\_2 |\
| month\_sp\_3 |\
| month\_sp\_4 |\
| month\_sp\_5 |\
\
cyclic\_weekday\
\
\['weekday'\]\
\
SplineTransformer\
\
[?Documentation for SplineTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [n\_knots n\_knots: int, default=5  <br>  <br>Number of knots of the splines if \`knots\` equals one of  <br>{'uniform', 'quantile'}. Must be larger or equal 2. Ignored if \`knots\`  <br>is array-like.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_knots,-int%2C%20default%3D5) | 4   |\
|     | [knots knots: {'uniform', 'quantile'} or array-like of shape (n\_knots, n\_features), default='uniform'  <br>  <br>Set knot positions such that first knot <= features <= last knot.  <br>  <br>\- If 'uniform', \`n\_knots\` number of knots are distributed uniformly  <br>from min to max values of the features.  <br>\- If 'quantile', they are distributed uniformly along the quantiles of  <br>the features.  <br>\- If an array-like is given, it directly specifies the sorted knot  <br>positions including the boundary knots. Note that, internally,  <br>\`degree\` number of knots are added before the first knot, the same  <br>after the last knot.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=knots,-int%2C%20default%3D5) | array(\[\[0. ...\[7. \]\]) |\
|     | [extrapolation extrapolation: {'error', 'constant', 'linear', 'continue', 'periodic'}, default='constant'  <br>  <br>If 'error', values outside the min and max values of the training  <br>features raises a \`ValueError\`. If 'constant', the value of the  <br>splines at minimum and maximum value of the features is used as  <br>constant extrapolation. If 'linear', a linear extrapolation is used.  <br>If 'continue', the splines are extrapolated as is, i.e. option  <br>\`extrapolate=True\` in :class:\`scipy.interpolate.BSpline\`. If  <br>'periodic', periodic splines with a periodicity equal to the distance  <br>between the first and last knot are used. Periodic splines enforce  <br>equal function values and derivatives at the first and last knot.  <br>For example, this makes it possible to avoid introducing an arbitrary  <br>jump between Dec 31st and Jan 1st in spline features derived from a  <br>naturally periodic "day-of-year" input feature. In this case it is  <br>recommended to manually set the knot values to control the period.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=extrapolation,-%7B%27error%27%2C%20%27constant%27%2C%20%27linear%27%2C%20%27continue%27%2C%20%27periodic%27%7D%2C%20%20%20%20%20%20%20%20%20default%3D%27constant%27) | 'periodic' |\
|     | [degree degree: int, default=3  <br>  <br>The polynomial degree of the spline basis. Must be a non-negative  <br>integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=degree,-int%2C%20default%3D3) | 3   |\
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If False, then the last spline element inside the data range  <br>of a feature is dropped. As B-splines sum to one over the spline basis  <br>functions for each data point, they implicitly include a bias term,  <br>i.e. a column of ones. It acts as an intercept term in a linear models.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |\
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to compute, but  <br>may slow down subsequent estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |\
|     | [handle\_missing handle\_missing: {'error', 'zeros'}, default='error'  <br>  <br>Specifies the way missing values are handled.  <br>  <br>\- 'error' : Raise an error if \`np.nan\` values are present during :meth:\`fit\`.  <br>\- 'zeros' : Encode splines of missing values with values \`0\`.  <br>  <br>Note that \`handle\_missing='zeros'\` differs from first imputing missing values  <br>with zeros and then creating the spline basis. The latter creates spline basis  <br>functions which have non-zero values at the missing values  <br>whereas this option simply sets all spline basis function values to zero at the  <br>missing values.  <br>  <br>.. versionadded:: 1.8](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=handle_missing,-%7B%27error%27%2C%20%27zeros%27%7D%2C%20default%3D%27error%27) | 'error' |\
|     | [sparse\_output sparse\_output: bool, default=False  <br>  <br>Will return sparse CSR matrix if set True else will return an array.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=sparse_output,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [bsplines\_ bsplines\_: list of shape (n\_features,)  <br>  <br>List of BSplines objects, one for each feature.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=bsplines_,-list%20of%20shape%20%28n_features%2C%29) | list | \[<scipy.interp...x7e1dfd79e630>\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['weekday'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>The total number of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
| [n\_features\_out\_ n\_features\_out\_: int  <br>  <br>The total number of output features, which is computed as  <br>\`n\_features \* n\_splines\`, where \`n\_splines\` is  <br>the number of bases elements of the B-splines,  <br>\`n\_knots + degree - 1\` for non-periodic splines and  <br>\`n\_knots - 1\` for periodic ones.  <br>If \`include\_bias=False\`, then it is only  <br>\`n\_features \* (n\_splines - 1)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_out_,-int) | int | 3   |\
\
3 features\
\
|     |\
| --- |\
| weekday\_sp\_0 |\
| weekday\_sp\_1 |\
| weekday\_sp\_2 |\
\
cyclic\_hour\
\
\['hour'\]\
\
SplineTransformer\
\
[?Documentation for SplineTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [n\_knots n\_knots: int, default=5  <br>  <br>Number of knots of the splines if \`knots\` equals one of  <br>{'uniform', 'quantile'}. Must be larger or equal 2. Ignored if \`knots\`  <br>is array-like.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_knots,-int%2C%20default%3D5) | 13  |\
|     | [knots knots: {'uniform', 'quantile'} or array-like of shape (n\_knots, n\_features), default='uniform'  <br>  <br>Set knot positions such that first knot <= features <= last knot.  <br>  <br>\- If 'uniform', \`n\_knots\` number of knots are distributed uniformly  <br>from min to max values of the features.  <br>\- If 'quantile', they are distributed uniformly along the quantiles of  <br>the features.  <br>\- If an array-like is given, it directly specifies the sorted knot  <br>positions including the boundary knots. Note that, internally,  <br>\`degree\` number of knots are added before the first knot, the same  <br>after the last knot.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=knots,-int%2C%20default%3D5) | array(\[\[ 0.\],... \[24.\]\]) |\
|     | [extrapolation extrapolation: {'error', 'constant', 'linear', 'continue', 'periodic'}, default='constant'  <br>  <br>If 'error', values outside the min and max values of the training  <br>features raises a \`ValueError\`. If 'constant', the value of the  <br>splines at minimum and maximum value of the features is used as  <br>constant extrapolation. If 'linear', a linear extrapolation is used.  <br>If 'continue', the splines are extrapolated as is, i.e. option  <br>\`extrapolate=True\` in :class:\`scipy.interpolate.BSpline\`. If  <br>'periodic', periodic splines with a periodicity equal to the distance  <br>between the first and last knot are used. Periodic splines enforce  <br>equal function values and derivatives at the first and last knot.  <br>For example, this makes it possible to avoid introducing an arbitrary  <br>jump between Dec 31st and Jan 1st in spline features derived from a  <br>naturally periodic "day-of-year" input feature. In this case it is  <br>recommended to manually set the knot values to control the period.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=extrapolation,-%7B%27error%27%2C%20%27constant%27%2C%20%27linear%27%2C%20%27continue%27%2C%20%27periodic%27%7D%2C%20%20%20%20%20%20%20%20%20default%3D%27constant%27) | 'periodic' |\
|     | [degree degree: int, default=3  <br>  <br>The polynomial degree of the spline basis. Must be a non-negative  <br>integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=degree,-int%2C%20default%3D3) | 3   |\
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If False, then the last spline element inside the data range  <br>of a feature is dropped. As B-splines sum to one over the spline basis  <br>functions for each data point, they implicitly include a bias term,  <br>i.e. a column of ones. It acts as an intercept term in a linear models.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |\
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to compute, but  <br>may slow down subsequent estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |\
|     | [handle\_missing handle\_missing: {'error', 'zeros'}, default='error'  <br>  <br>Specifies the way missing values are handled.  <br>  <br>\- 'error' : Raise an error if \`np.nan\` values are present during :meth:\`fit\`.  <br>\- 'zeros' : Encode splines of missing values with values \`0\`.  <br>  <br>Note that \`handle\_missing='zeros'\` differs from first imputing missing values  <br>with zeros and then creating the spline basis. The latter creates spline basis  <br>functions which have non-zero values at the missing values  <br>whereas this option simply sets all spline basis function values to zero at the  <br>missing values.  <br>  <br>.. versionadded:: 1.8](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=handle_missing,-%7B%27error%27%2C%20%27zeros%27%7D%2C%20default%3D%27error%27) | 'error' |\
|     | [sparse\_output sparse\_output: bool, default=False  <br>  <br>Will return sparse CSR matrix if set True else will return an array.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=sparse_output,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [bsplines\_ bsplines\_: list of shape (n\_features,)  <br>  <br>List of BSplines objects, one for each feature.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=bsplines_,-list%20of%20shape%20%28n_features%2C%29) | list | \[<scipy.interp...x7e1dfd79ca10>\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['hour'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>The total number of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
| [n\_features\_out\_ n\_features\_out\_: int  <br>  <br>The total number of output features, which is computed as  <br>\`n\_features \* n\_splines\`, where \`n\_splines\` is  <br>the number of bases elements of the B-splines,  <br>\`n\_knots + degree - 1\` for non-periodic splines and  <br>\`n\_knots - 1\` for periodic ones.  <br>If \`include\_bias=False\`, then it is only  <br>\`n\_features \* (n\_splines - 1)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_out_,-int) | int | 12  |\
\
12 features\
\
|     |\
| --- |\
| hour\_sp\_0 |\
| hour\_sp\_1 |\
| hour\_sp\_2 |\
| hour\_sp\_3 |\
| hour\_sp\_4 |\
| hour\_sp\_5 |\
| hour\_sp\_6 |\
| hour\_sp\_7 |\
| hour\_sp\_8 |\
| hour\_sp\_9 |\
| hour\_sp\_10 |\
| hour\_sp\_11 |\
\
remainder\
\
\['year', 'temp', 'feel\_temp', 'humidity', 'windspeed'\]\
\
MinMaxScaler\
\
[?Documentation for MinMaxScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [feature\_range feature\_range: tuple (min, max), default=(0, 1)  <br>  <br>Desired range of transformed data.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=feature_range,-tuple%20%28min%2C%20max%29%2C%20default%3D%280%2C%201%29) | (0, ...) |\
|     | [copy copy: bool, default=True  <br>  <br>Set to False to perform inplace row normalization and avoid a  <br>copy (if the input is already a numpy array).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [clip clip: bool, default=False  <br>  <br>Set to True to clip transformed values of held-out data to  <br>provided \`feature\_range\`.  <br>Since this parameter will clip values, \`inverse\_transform\` may not  <br>be able to restore the original data.  <br>  <br>.. note::  <br>Setting \`clip=True\` does not prevent feature drift (a distribution  <br>shift between training and test data). The transformed values are clipped  <br>to the \`feature\_range\`, which helps avoid unintended behavior in models  <br>sensitive to out-of-range inputs (e.g. linear models). Use with care,  <br>as clipping can distort the distribution of test data.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=clip,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [data\_max\_ data\_max\_: ndarray of shape (n\_features,)  <br>  <br>Per feature maximum seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_max\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_max_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 1. ,39.36,50. , 1. ,57. \] |\
| [data\_min\_ data\_min\_: ndarray of shape (n\_features,)  <br>  <br>Per feature minimum seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_min\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_min_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[0. ,0.82,0.76,0.16,0. \] |\
| [data\_range\_ data\_range\_: ndarray of shape (n\_features,)  <br>  <br>Per feature range \`\`(data\_max\_ - data\_min\_)\`\` seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_range\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_range_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 1. ,38.54,49.24, 0.84,57. \] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](5,) | \['year','temp','feel\_temp','humidity','windspeed'\] |\
| [min\_ min\_: ndarray of shape (n\_features,)  <br>  <br>Per feature adjustment for minimum. Equivalent to  <br>\`\`min - X.min(axis=0) \* self.scale\_\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=min_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 0. ,-0.02,-0.02,-0.19, 0. \] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=n_features_in_,-int) | int | 5   |\
| [n\_samples\_seen\_ n\_samples\_seen\_: int  <br>  <br>The number of samples processed by the estimator.  <br>It will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=n_samples_seen_,-int) | int | 10000 |\
| [scale\_ scale\_: ndarray of shape (n\_features,)  <br>  <br>Per feature relative scaling of the data. Equivalent to  <br>\`\`(max - min) / (X.max(axis=0) - X.min(axis=0))\`\`  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\* attribute.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[1. ,0.03,0.02,1.19,0.02\] |\
\
5 features\
\
|     |\
| --- |\
| year |\
| temp |\
| feel\_temp |\
| humidity |\
| windspeed |\
\
37 features\
\
|     |\
| --- |\
| season\_fall |\
| season\_spring |\
| season\_summer |\
| season\_winter |\
| holiday\_False |\
| holiday\_True |\
| workingday\_False |\
| workingday\_True |\
| weather\_clear |\
| weather\_misty |\
| weather\_rain |\
| month\_sp\_0 |\
| month\_sp\_1 |\
| month\_sp\_2 |\
| month\_sp\_3 |\
| month\_sp\_4 |\
| month\_sp\_5 |\
| weekday\_sp\_0 |\
| weekday\_sp\_1 |\
| weekday\_sp\_2 |\
| hour\_sp\_0 |\
| hour\_sp\_1 |\
| hour\_sp\_2 |\
| hour\_sp\_3 |\
| hour\_sp\_4 |\
| hour\_sp\_5 |\
| hour\_sp\_6 |\
| hour\_sp\_7 |\
| hour\_sp\_8 |\
| hour\_sp\_9 |\
| hour\_sp\_10 |\
| hour\_sp\_11 |\
| year |\
| temp |\
| feel\_temp |\
| humidity |\
| windspeed |\
\
RidgeCV\
\
[?Documentation for RidgeCV](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [alphas alphas: array-like of shape (n\_alphas,), default=(0.1, 1.0, 10.0)  <br>  <br>Array of alpha values to try.  <br>Regularization strength; must be a positive float. Regularization  <br>improves the conditioning of the problem and reduces the variance of  <br>the estimates. Larger values specify stronger regularization.  <br>Alpha corresponds to \`\`1 / (2C)\`\` in other linear models such as  <br>:class:\`~sklearn.linear\_model.LogisticRegression\` or  <br>:class:\`~sklearn.svm.LinearSVC\`.  <br>If using Leave-One-Out cross-validation, alphas must be strictly positive.  <br>  <br>For an example on how regularization strength affects the model coefficients,  <br>see :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_ridge\_coeffs.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alphas,-array-like%20of%20shape%20%28n_alphas%2C%29%2C%20default%3D%280.1%2C%201.0%2C%2010.0%29) | array(\[1.0000...00000000e+06\]) |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to calculate the intercept for this model. If set  <br>to false, no intercept will be used in calculations  <br>(i.e. data is expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [scoring scoring: str, callable, default=None  <br>  <br>The scoring method to use for cross-validation. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: negative :ref:\`mean squared error <mean\_squared\_error>\` if cv is  <br>None (i.e. when using leave-one-out cross-validation), or  <br>:ref:\`coefficient of determination <r2\_score>\` (:math:\`R^2\`) otherwise.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=scoring,-str%2C%20callable%2C%20default%3DNone) | None |\
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the efficient Leave-One-Out cross-validation  <br>\- integer, to specify the number of folds,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if \`\`y\`\` is binary or multiclass,  <br>:class:\`~sklearn.model\_selection.StratifiedKFold\` is used, else,  <br>:class:\`~sklearn.model\_selection.KFold\` is used.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |\
|     | [gcv\_mode gcv\_mode: {'auto', 'svd', 'eigen'}, default='auto'  <br>  <br>Flag indicating which strategy to use when performing  <br>Leave-One-Out Cross-Validation. Options are::  <br>  <br>'auto' : same as 'eigen'  <br>'svd' : use singular value decomposition of X when X is dense,  <br>fallback to 'eigen' when X is sparse  <br>'eigen' : use eigendecomposition of X X' when n\_samples <= n\_features  <br>or X' X when n\_features < n\_samples  <br>  <br>The 'auto' mode is the default and is intended to pick the cheaper  <br>option depending on the shape and sparsity of the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=gcv_mode,-%7B%27auto%27%2C%20%27svd%27%2C%20%27eigen%27%7D%2C%20default%3D%27auto%27) | None |\
|     | [store\_cv\_results store\_cv\_results: bool, default=False  <br>  <br>Flag indicating if the cross-validation values corresponding to  <br>each alpha should be stored in the \`\`cv\_results\_\`\` attribute (see  <br>below). This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionchanged:: 1.5  <br>Parameter name changed from \`store\_cv\_values\` to \`store\_cv\_results\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=store_cv_results,-bool%2C%20default%3DFalse) | False |\
|     | [alpha\_per\_target alpha\_per\_target: bool, default=False  <br>  <br>Flag indicating whether to optimize the alpha value (picked from the  <br>\`alphas\` parameter list) for each target separately (for multi-output  <br>settings: multiple prediction targets). When set to \`True\`, after  <br>fitting, the \`alpha\_\` attribute will contain a value for each target.  <br>When set to \`False\`, a single alpha is used for all targets.  <br>This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_per_target,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [alpha\_ alpha\_: float or ndarray of shape (n\_targets,)  <br>  <br>Estimated regularization parameter, or, if \`\`alpha\_per\_target=True\`\`,  <br>the estimated regularization parameter for each target.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float | 1   |\
| [best\_score\_ best\_score\_: float or ndarray of shape (n\_targets,)  <br>  <br>Score of base estimator with best alpha, or, if  <br>\`\`alpha\_per\_target=True\`\`, a score for each target.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=best_score_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | \-0.008547 |\
| [coef\_ coef\_: ndarray of shape (n\_features) or (n\_targets, n\_features)  <br>  <br>Weight vector(s).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=coef_,-ndarray%20of%20shape%20%28n_features%29%20or%20%28n_targets%2C%20n_features%29) | ndarray\[float64\](37,) | \[ 0. ,-0.03, 0.01,..., 0.15,-0.06,-0.04\] |\
| [intercept\_ intercept\_: float or ndarray of shape (n\_targets,)  <br>  <br>Independent term in decision function. Set to 0.0 if  <br>\`\`fit\_intercept = False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=intercept_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | 0.03652 |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=n_features_in_,-int) | int | 37  |\
\
  \
  \
\
Spline features make it possible for the linear model to successfully leverage the periodic time-related features and reduce the error from ~14% to ~10% of the maximum demand, which is similar to what we observed with the one-hot encoded features.\
\
Qualitative analysis of the impact of features on linear model predictions[#](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#qualitative-analysis-of-the-impact-of-features-on-linear-model-predictions "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Here, we want to visualize the impact of the feature engineering choices on the time related shape of the predictions.\
\
To do so we consider an arbitrary time-based split to compare the predictions on a range of held out data points.\
\
naive\_linear\_pipeline.fit(X.iloc\[train\_0\], y.iloc\[train\_0\])\
naive\_linear\_predictions \= naive\_linear\_pipeline.predict(X.iloc\[test\_0\])\
\
one\_hot\_linear\_pipeline.fit(X.iloc\[train\_0\], y.iloc\[train\_0\])\
one\_hot\_linear\_predictions \= one\_hot\_linear\_pipeline.predict(X.iloc\[test\_0\])\
\
cyclic\_cossin\_linear\_pipeline.fit(X.iloc\[train\_0\], y.iloc\[train\_0\])\
cyclic\_cossin\_linear\_predictions \= cyclic\_cossin\_linear\_pipeline.predict(X.iloc\[test\_0\])\
\
cyclic\_spline\_linear\_pipeline.fit(X.iloc\[train\_0\], y.iloc\[train\_0\])\
cyclic\_spline\_linear\_predictions \= cyclic\_spline\_linear\_pipeline.predict(X.iloc\[test\_0\])\
\
Copy to clipboard\
\
We visualize those predictions by zooming on the last 96 hours (4 days) of the test set to get some qualitative insights:\
\
last\_hours \= slice(\-96, None)\
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(12, 4))\
fig.suptitle("Predictions by linear models")\
ax.plot(\
    y.iloc\[test\_0\].values\[last\_hours\],\
    "x-",\
    alpha\=0.2,\
    label\="Actual demand",\
    color\="black",\
)\
ax.plot(naive\_linear\_predictions\[last\_hours\], "x-", label\="Ordinal time features")\
ax.plot(\
    cyclic\_cossin\_linear\_predictions\[last\_hours\],\
    "x-",\
    label\="Trigonometric time features",\
)\
ax.plot(\
    cyclic\_spline\_linear\_predictions\[last\_hours\],\
    "x-",\
    label\="Spline-based time features",\
)\
ax.plot(\
    one\_hot\_linear\_predictions\[last\_hours\],\
    "x-",\
    label\="One-hot time features",\
)\
\_ \= ax.legend()\
\
Copy to clipboard\
\
![Predictions by linear models](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_006.png)\
\
We can draw the following conclusions from the above plot:\
\
*   The **raw ordinal time-related features** are problematic because they do not capture the natural periodicity: we observe a big jump in the predictions at the end of each day when the hour features goes from 23 back to 0. We can expect similar artifacts at the end of each week or each year.\
    \
*   As expected, the **trigonometric features** (sine and cosine) do not have these discontinuities at midnight, but the linear regression model fails to leverage those features to properly model intra-day variations. Using trigonometric features for higher harmonics or additional trigonometric features for the natural period with different phases could potentially fix this problem.\
    \
*   the **periodic spline-based features** fix those two problems at once: they give more expressivity to the linear model by making it possible to focus on specific hours thanks to the use of 12 splines. Furthermore the `extrapolation="periodic"` option enforces a smooth representation between `hour=23` and `hour=0`.\
    \
*   The **one-hot encoded features** behave similarly to the periodic spline-based features but are more spiky: for instance they can better model the morning peak during the week days since this peak lasts shorter than an hour. However, we will see in the following that what can be an advantage for linear models is not necessarily one for more expressive models.\
    \
\
We can also compare the number of features extracted by each feature engineering pipeline:\
\
naive\_linear\_pipeline\[:\-1\].transform(X).shape\
\
Copy to clipboard\
\
(17379, 19)\
\
Copy to clipboard\
\
one\_hot\_linear\_pipeline\[:\-1\].transform(X).shape\
\
Copy to clipboard\
\
(17379, 59)\
\
Copy to clipboard\
\
cyclic\_cossin\_linear\_pipeline\[:\-1\].transform(X).shape\
\
Copy to clipboard\
\
(17379, 22)\
\
Copy to clipboard\
\
cyclic\_spline\_linear\_pipeline\[:\-1\].transform(X).shape\
\
Copy to clipboard\
\
(17379, 37)\
\
Copy to clipboard\
\
This confirms that the one-hot encoding and the spline encoding strategies create a lot more features for the time representation than the alternatives, which in turn gives the downstream linear model more flexibility (degrees of freedom) to avoid underfitting.\
\
Finally, we observe that none of the linear models can approximate the true bike rentals demand, especially for the peaks that can be very sharp at rush hours during the working days but much flatter during the week-ends: the most accurate linear models based on splines or one-hot encoding tend to forecast peaks of commuting-related bike rentals even on the week-ends and under-estimate the commuting-related events during the working days.\
\
These systematic prediction errors reveal a form of under-fitting and can be explained by the lack of interactions terms between features, e.g. “workingday” and features derived from “hours”. This issue will be addressed in the following section.\
\
Modeling pairwise interactions with splines and polynomial features[#](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#modeling-pairwise-interactions-with-splines-and-polynomial-features "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Linear models do not automatically capture interaction effects between input features. It does not help that some features are marginally non-linear as is the case with features constructed by `SplineTransformer` (or one-hot encoding or binning).\
\
However, it is possible to use the `PolynomialFeatures` class on coarse grained spline encoded hours to model the “workingday”/”hours” interaction explicitly without introducing too many new variables:\
\
from sklearn.pipeline import [FeatureUnion](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")\
from sklearn.preprocessing import [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")\
\
hour\_workday\_interaction \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
    [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")\
(\
        \[\
            ("cyclic\_hour", periodic\_spline\_transformer(24, n\_splines\=8), \["hour"\]),\
            (\
                "workingday",\
                [FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")\
(\
                    lambda x: x \== "True", feature\_names\_out\="one-to-one"\
                ),\
                \["workingday"\],\
            ),\
        \],\
        verbose\_feature\_names\_out\=False,\
    ),\
    [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")\
(degree\=2, interaction\_only\=True, include\_bias\=False),\
)\
\
Copy to clipboard\
\
Those features are then combined with the ones already computed in the previous spline-base pipeline. We can observe a nice performance improvement by modeling this pairwise interaction explicitly:\
\
cyclic\_spline\_interactions\_pipeline \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
    [FeatureUnion](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")\
(\
        \[\
            ("marginal", cyclic\_spline\_transformer),\
            ("interactions", hour\_workday\_interaction),\
        \],\
        verbose\_feature\_names\_out\=True,\
    ).set\_output(transform\="pandas"),\
    [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")\
(alphas\=alphas),\
)\
evaluate(cyclic\_spline\_interactions\_pipeline, X, y, cv\=ts\_cv)\
\
Copy to clipboard\
\
Mean Absolute Error:     0.078 +/- 0.009\
Root Mean Squared Error: 0.104 +/- 0.009\
\
Copy to clipboard\
\
Pipeline(steps=\[('featureunion',\
                 FeatureUnion(transformer\_list=\[('marginal',\
                                                 ColumnTransformer(remainder=MinMaxScaler(),\
                                                                   transformers=\[('categorical',\
                                                                                  OneHotEncoder(handle\_unknown='ignore',\
                                                                                                sparse\_output=False),\
                                                                                  Index(\['season', 'holiday', 'workingday', 'weather'\], dtype='str')),\
                                                                                 ('cyclic\_month',\
                                                                                  SplineTransformer(extrapolation='periodic',\
                                                                                                    knots=array(\[\[ 0.\],\
       \[ 2....\
                 RidgeCV(alphas=array(\[1.00000000e-06, 3.16227766e-06, 1.00000000e-05, 3.16227766e-05,\
       1.00000000e-04, 3.16227766e-04, 1.00000000e-03, 3.16227766e-03,\
       1.00000000e-02, 3.16227766e-02, 1.00000000e-01, 3.16227766e-01,\
       1.00000000e+00, 3.16227766e+00, 1.00000000e+01, 3.16227766e+01,\
       1.00000000e+02, 3.16227766e+02, 1.00000000e+03, 3.16227766e+03,\
       1.00000000e+04, 3.16227766e+04, 1.00000000e+05, 3.16227766e+05,\
       1.00000000e+06\])))\])\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
Pipeline\
\
[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)\
iFitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('featureunion', ...), ('ridgecv', ...)\] |\
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |\
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 12  |\
\
featureunion: FeatureUnion\
\
[?Documentation for featureunion: FeatureUnion](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.FeatureUnion.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [transformer\_list transformer\_list: list of (str, transformer) tuples  <br>  <br>List of transformer objects to be applied to the data. The first  <br>half of each tuple is the name of the transformer. The transformer can  <br>be 'drop' for it to be ignored or can be 'passthrough' for features to  <br>be passed unchanged.  <br>  <br>.. versionadded:: 1.1  <br>Added the option \`"passthrough"\`.  <br>  <br>.. versionchanged:: 0.22  <br>Deprecated \`None\` as a transformer in favor of 'drop'.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.FeatureUnion.html#:~:text=transformer_list,-list%20of%20%28str%2C%20transformer%29%20tuples) | \[('marginal', ...), ('interactions', ...)\] |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionchanged:: v0.20  <br>\`n\_jobs\` default changed from 1 to None](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.FeatureUnion.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer.  <br>Keys are transformer names, values the weights.  <br>Raises ValueError if key not present in \`\`transformer\_list\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.FeatureUnion.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.FeatureUnion.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, default=True  <br>  <br>If True, :meth:\`get\_feature\_names\_out\` will prefix all feature names  <br>with the name of the transformer that generated that feature.  <br>If False, :meth:\`get\_feature\_names\_out\` will not prefix any feature  <br>names and will error if feature names are not unique.  <br>  <br>.. versionadded:: 1.5](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.FeatureUnion.html#:~:text=verbose_feature_names_out,-bool%2C%20default%3DTrue) | True |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when  <br>\`X\` has feature names that are all strings.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.FeatureUnion.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first transformer in \`transformer\_list\` exposes such an  <br>attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.FeatureUnion.html#:~:text=n_features_in_,-int) | int | 12  |\
\
marginal\
\
categorical\
\
Index(\['season', 'holiday', 'workingday', 'weather'\], dtype='str')\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | False |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\['fall'... dtype=object), array(\['False... dtype=object), array(\['False... dtype=object), array(\['clear... dtype=object)\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](4,) | \['season','holiday','workingday','weather'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 4   |\
\
11 features\
\
|     |\
| --- |\
| season\_fall |\
| season\_spring |\
| season\_summer |\
| season\_winter |\
| holiday\_False |\
| holiday\_True |\
| workingday\_False |\
| workingday\_True |\
| weather\_clear |\
| weather\_misty |\
| weather\_rain |\
\
cyclic\_month\
\
\['month'\]\
\
SplineTransformer\
\
[?Documentation for SplineTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [n\_knots n\_knots: int, default=5  <br>  <br>Number of knots of the splines if \`knots\` equals one of  <br>{'uniform', 'quantile'}. Must be larger or equal 2. Ignored if \`knots\`  <br>is array-like.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_knots,-int%2C%20default%3D5) | 7   |\
|     | [knots knots: {'uniform', 'quantile'} or array-like of shape (n\_knots, n\_features), default='uniform'  <br>  <br>Set knot positions such that first knot <= features <= last knot.  <br>  <br>\- If 'uniform', \`n\_knots\` number of knots are distributed uniformly  <br>from min to max values of the features.  <br>\- If 'quantile', they are distributed uniformly along the quantiles of  <br>the features.  <br>\- If an array-like is given, it directly specifies the sorted knot  <br>positions including the boundary knots. Note that, internally,  <br>\`degree\` number of knots are added before the first knot, the same  <br>after the last knot.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=knots,-int%2C%20default%3D5) | array(\[\[ 0.\],... \[12.\]\]) |\
|     | [extrapolation extrapolation: {'error', 'constant', 'linear', 'continue', 'periodic'}, default='constant'  <br>  <br>If 'error', values outside the min and max values of the training  <br>features raises a \`ValueError\`. If 'constant', the value of the  <br>splines at minimum and maximum value of the features is used as  <br>constant extrapolation. If 'linear', a linear extrapolation is used.  <br>If 'continue', the splines are extrapolated as is, i.e. option  <br>\`extrapolate=True\` in :class:\`scipy.interpolate.BSpline\`. If  <br>'periodic', periodic splines with a periodicity equal to the distance  <br>between the first and last knot are used. Periodic splines enforce  <br>equal function values and derivatives at the first and last knot.  <br>For example, this makes it possible to avoid introducing an arbitrary  <br>jump between Dec 31st and Jan 1st in spline features derived from a  <br>naturally periodic "day-of-year" input feature. In this case it is  <br>recommended to manually set the knot values to control the period.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=extrapolation,-%7B%27error%27%2C%20%27constant%27%2C%20%27linear%27%2C%20%27continue%27%2C%20%27periodic%27%7D%2C%20%20%20%20%20%20%20%20%20default%3D%27constant%27) | 'periodic' |\
|     | [degree degree: int, default=3  <br>  <br>The polynomial degree of the spline basis. Must be a non-negative  <br>integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=degree,-int%2C%20default%3D3) | 3   |\
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If False, then the last spline element inside the data range  <br>of a feature is dropped. As B-splines sum to one over the spline basis  <br>functions for each data point, they implicitly include a bias term,  <br>i.e. a column of ones. It acts as an intercept term in a linear models.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |\
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to compute, but  <br>may slow down subsequent estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |\
|     | [handle\_missing handle\_missing: {'error', 'zeros'}, default='error'  <br>  <br>Specifies the way missing values are handled.  <br>  <br>\- 'error' : Raise an error if \`np.nan\` values are present during :meth:\`fit\`.  <br>\- 'zeros' : Encode splines of missing values with values \`0\`.  <br>  <br>Note that \`handle\_missing='zeros'\` differs from first imputing missing values  <br>with zeros and then creating the spline basis. The latter creates spline basis  <br>functions which have non-zero values at the missing values  <br>whereas this option simply sets all spline basis function values to zero at the  <br>missing values.  <br>  <br>.. versionadded:: 1.8](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=handle_missing,-%7B%27error%27%2C%20%27zeros%27%7D%2C%20default%3D%27error%27) | 'error' |\
|     | [sparse\_output sparse\_output: bool, default=False  <br>  <br>Will return sparse CSR matrix if set True else will return an array.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=sparse_output,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [bsplines\_ bsplines\_: list of shape (n\_features,)  <br>  <br>List of BSplines objects, one for each feature.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=bsplines_,-list%20of%20shape%20%28n_features%2C%29) | list | \[<scipy.interp...x7e1dbdced250>\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['month'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>The total number of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
| [n\_features\_out\_ n\_features\_out\_: int  <br>  <br>The total number of output features, which is computed as  <br>\`n\_features \* n\_splines\`, where \`n\_splines\` is  <br>the number of bases elements of the B-splines,  <br>\`n\_knots + degree - 1\` for non-periodic splines and  <br>\`n\_knots - 1\` for periodic ones.  <br>If \`include\_bias=False\`, then it is only  <br>\`n\_features \* (n\_splines - 1)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_out_,-int) | int | 6   |\
\
6 features\
\
|     |\
| --- |\
| month\_sp\_0 |\
| month\_sp\_1 |\
| month\_sp\_2 |\
| month\_sp\_3 |\
| month\_sp\_4 |\
| month\_sp\_5 |\
\
cyclic\_weekday\
\
\['weekday'\]\
\
SplineTransformer\
\
[?Documentation for SplineTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [n\_knots n\_knots: int, default=5  <br>  <br>Number of knots of the splines if \`knots\` equals one of  <br>{'uniform', 'quantile'}. Must be larger or equal 2. Ignored if \`knots\`  <br>is array-like.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_knots,-int%2C%20default%3D5) | 4   |\
|     | [knots knots: {'uniform', 'quantile'} or array-like of shape (n\_knots, n\_features), default='uniform'  <br>  <br>Set knot positions such that first knot <= features <= last knot.  <br>  <br>\- If 'uniform', \`n\_knots\` number of knots are distributed uniformly  <br>from min to max values of the features.  <br>\- If 'quantile', they are distributed uniformly along the quantiles of  <br>the features.  <br>\- If an array-like is given, it directly specifies the sorted knot  <br>positions including the boundary knots. Note that, internally,  <br>\`degree\` number of knots are added before the first knot, the same  <br>after the last knot.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=knots,-int%2C%20default%3D5) | array(\[\[0. ...\[7. \]\]) |\
|     | [extrapolation extrapolation: {'error', 'constant', 'linear', 'continue', 'periodic'}, default='constant'  <br>  <br>If 'error', values outside the min and max values of the training  <br>features raises a \`ValueError\`. If 'constant', the value of the  <br>splines at minimum and maximum value of the features is used as  <br>constant extrapolation. If 'linear', a linear extrapolation is used.  <br>If 'continue', the splines are extrapolated as is, i.e. option  <br>\`extrapolate=True\` in :class:\`scipy.interpolate.BSpline\`. If  <br>'periodic', periodic splines with a periodicity equal to the distance  <br>between the first and last knot are used. Periodic splines enforce  <br>equal function values and derivatives at the first and last knot.  <br>For example, this makes it possible to avoid introducing an arbitrary  <br>jump between Dec 31st and Jan 1st in spline features derived from a  <br>naturally periodic "day-of-year" input feature. In this case it is  <br>recommended to manually set the knot values to control the period.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=extrapolation,-%7B%27error%27%2C%20%27constant%27%2C%20%27linear%27%2C%20%27continue%27%2C%20%27periodic%27%7D%2C%20%20%20%20%20%20%20%20%20default%3D%27constant%27) | 'periodic' |\
|     | [degree degree: int, default=3  <br>  <br>The polynomial degree of the spline basis. Must be a non-negative  <br>integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=degree,-int%2C%20default%3D3) | 3   |\
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If False, then the last spline element inside the data range  <br>of a feature is dropped. As B-splines sum to one over the spline basis  <br>functions for each data point, they implicitly include a bias term,  <br>i.e. a column of ones. It acts as an intercept term in a linear models.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |\
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to compute, but  <br>may slow down subsequent estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |\
|     | [handle\_missing handle\_missing: {'error', 'zeros'}, default='error'  <br>  <br>Specifies the way missing values are handled.  <br>  <br>\- 'error' : Raise an error if \`np.nan\` values are present during :meth:\`fit\`.  <br>\- 'zeros' : Encode splines of missing values with values \`0\`.  <br>  <br>Note that \`handle\_missing='zeros'\` differs from first imputing missing values  <br>with zeros and then creating the spline basis. The latter creates spline basis  <br>functions which have non-zero values at the missing values  <br>whereas this option simply sets all spline basis function values to zero at the  <br>missing values.  <br>  <br>.. versionadded:: 1.8](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=handle_missing,-%7B%27error%27%2C%20%27zeros%27%7D%2C%20default%3D%27error%27) | 'error' |\
|     | [sparse\_output sparse\_output: bool, default=False  <br>  <br>Will return sparse CSR matrix if set True else will return an array.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=sparse_output,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [bsplines\_ bsplines\_: list of shape (n\_features,)  <br>  <br>List of BSplines objects, one for each feature.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=bsplines_,-list%20of%20shape%20%28n_features%2C%29) | list | \[<scipy.interp...x7e1dbde30290>\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['weekday'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>The total number of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
| [n\_features\_out\_ n\_features\_out\_: int  <br>  <br>The total number of output features, which is computed as  <br>\`n\_features \* n\_splines\`, where \`n\_splines\` is  <br>the number of bases elements of the B-splines,  <br>\`n\_knots + degree - 1\` for non-periodic splines and  <br>\`n\_knots - 1\` for periodic ones.  <br>If \`include\_bias=False\`, then it is only  <br>\`n\_features \* (n\_splines - 1)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_out_,-int) | int | 3   |\
\
3 features\
\
|     |\
| --- |\
| weekday\_sp\_0 |\
| weekday\_sp\_1 |\
| weekday\_sp\_2 |\
\
cyclic\_hour\
\
\['hour'\]\
\
SplineTransformer\
\
[?Documentation for SplineTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [n\_knots n\_knots: int, default=5  <br>  <br>Number of knots of the splines if \`knots\` equals one of  <br>{'uniform', 'quantile'}. Must be larger or equal 2. Ignored if \`knots\`  <br>is array-like.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_knots,-int%2C%20default%3D5) | 13  |\
|     | [knots knots: {'uniform', 'quantile'} or array-like of shape (n\_knots, n\_features), default='uniform'  <br>  <br>Set knot positions such that first knot <= features <= last knot.  <br>  <br>\- If 'uniform', \`n\_knots\` number of knots are distributed uniformly  <br>from min to max values of the features.  <br>\- If 'quantile', they are distributed uniformly along the quantiles of  <br>the features.  <br>\- If an array-like is given, it directly specifies the sorted knot  <br>positions including the boundary knots. Note that, internally,  <br>\`degree\` number of knots are added before the first knot, the same  <br>after the last knot.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=knots,-int%2C%20default%3D5) | array(\[\[ 0.\],... \[24.\]\]) |\
|     | [extrapolation extrapolation: {'error', 'constant', 'linear', 'continue', 'periodic'}, default='constant'  <br>  <br>If 'error', values outside the min and max values of the training  <br>features raises a \`ValueError\`. If 'constant', the value of the  <br>splines at minimum and maximum value of the features is used as  <br>constant extrapolation. If 'linear', a linear extrapolation is used.  <br>If 'continue', the splines are extrapolated as is, i.e. option  <br>\`extrapolate=True\` in :class:\`scipy.interpolate.BSpline\`. If  <br>'periodic', periodic splines with a periodicity equal to the distance  <br>between the first and last knot are used. Periodic splines enforce  <br>equal function values and derivatives at the first and last knot.  <br>For example, this makes it possible to avoid introducing an arbitrary  <br>jump between Dec 31st and Jan 1st in spline features derived from a  <br>naturally periodic "day-of-year" input feature. In this case it is  <br>recommended to manually set the knot values to control the period.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=extrapolation,-%7B%27error%27%2C%20%27constant%27%2C%20%27linear%27%2C%20%27continue%27%2C%20%27periodic%27%7D%2C%20%20%20%20%20%20%20%20%20default%3D%27constant%27) | 'periodic' |\
|     | [degree degree: int, default=3  <br>  <br>The polynomial degree of the spline basis. Must be a non-negative  <br>integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=degree,-int%2C%20default%3D3) | 3   |\
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If False, then the last spline element inside the data range  <br>of a feature is dropped. As B-splines sum to one over the spline basis  <br>functions for each data point, they implicitly include a bias term,  <br>i.e. a column of ones. It acts as an intercept term in a linear models.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |\
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to compute, but  <br>may slow down subsequent estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |\
|     | [handle\_missing handle\_missing: {'error', 'zeros'}, default='error'  <br>  <br>Specifies the way missing values are handled.  <br>  <br>\- 'error' : Raise an error if \`np.nan\` values are present during :meth:\`fit\`.  <br>\- 'zeros' : Encode splines of missing values with values \`0\`.  <br>  <br>Note that \`handle\_missing='zeros'\` differs from first imputing missing values  <br>with zeros and then creating the spline basis. The latter creates spline basis  <br>functions which have non-zero values at the missing values  <br>whereas this option simply sets all spline basis function values to zero at the  <br>missing values.  <br>  <br>.. versionadded:: 1.8](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=handle_missing,-%7B%27error%27%2C%20%27zeros%27%7D%2C%20default%3D%27error%27) | 'error' |\
|     | [sparse\_output sparse\_output: bool, default=False  <br>  <br>Will return sparse CSR matrix if set True else will return an array.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=sparse_output,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [bsplines\_ bsplines\_: list of shape (n\_features,)  <br>  <br>List of BSplines objects, one for each feature.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=bsplines_,-list%20of%20shape%20%28n_features%2C%29) | list | \[<scipy.interp...x7e1dbde31190>\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['hour'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>The total number of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
| [n\_features\_out\_ n\_features\_out\_: int  <br>  <br>The total number of output features, which is computed as  <br>\`n\_features \* n\_splines\`, where \`n\_splines\` is  <br>the number of bases elements of the B-splines,  <br>\`n\_knots + degree - 1\` for non-periodic splines and  <br>\`n\_knots - 1\` for periodic ones.  <br>If \`include\_bias=False\`, then it is only  <br>\`n\_features \* (n\_splines - 1)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_out_,-int) | int | 12  |\
\
12 features\
\
|     |\
| --- |\
| hour\_sp\_0 |\
| hour\_sp\_1 |\
| hour\_sp\_2 |\
| hour\_sp\_3 |\
| hour\_sp\_4 |\
| hour\_sp\_5 |\
| hour\_sp\_6 |\
| hour\_sp\_7 |\
| hour\_sp\_8 |\
| hour\_sp\_9 |\
| hour\_sp\_10 |\
| hour\_sp\_11 |\
\
remainder\
\
\['year', 'temp', 'feel\_temp', 'humidity', 'windspeed'\]\
\
MinMaxScaler\
\
[?Documentation for MinMaxScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [feature\_range feature\_range: tuple (min, max), default=(0, 1)  <br>  <br>Desired range of transformed data.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=feature_range,-tuple%20%28min%2C%20max%29%2C%20default%3D%280%2C%201%29) | (0, ...) |\
|     | [copy copy: bool, default=True  <br>  <br>Set to False to perform inplace row normalization and avoid a  <br>copy (if the input is already a numpy array).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [clip clip: bool, default=False  <br>  <br>Set to True to clip transformed values of held-out data to  <br>provided \`feature\_range\`.  <br>Since this parameter will clip values, \`inverse\_transform\` may not  <br>be able to restore the original data.  <br>  <br>.. note::  <br>Setting \`clip=True\` does not prevent feature drift (a distribution  <br>shift between training and test data). The transformed values are clipped  <br>to the \`feature\_range\`, which helps avoid unintended behavior in models  <br>sensitive to out-of-range inputs (e.g. linear models). Use with care,  <br>as clipping can distort the distribution of test data.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=clip,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [data\_max\_ data\_max\_: ndarray of shape (n\_features,)  <br>  <br>Per feature maximum seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_max\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_max_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 1. ,39.36,50. , 1. ,57. \] |\
| [data\_min\_ data\_min\_: ndarray of shape (n\_features,)  <br>  <br>Per feature minimum seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_min\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_min_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[0. ,0.82,0.76,0.16,0. \] |\
| [data\_range\_ data\_range\_: ndarray of shape (n\_features,)  <br>  <br>Per feature range \`\`(data\_max\_ - data\_min\_)\`\` seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_range\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_range_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 1. ,38.54,49.24, 0.84,57. \] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](5,) | \['year','temp','feel\_temp','humidity','windspeed'\] |\
| [min\_ min\_: ndarray of shape (n\_features,)  <br>  <br>Per feature adjustment for minimum. Equivalent to  <br>\`\`min - X.min(axis=0) \* self.scale\_\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=min_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 0. ,-0.02,-0.02,-0.19, 0. \] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=n_features_in_,-int) | int | 5   |\
| [n\_samples\_seen\_ n\_samples\_seen\_: int  <br>  <br>The number of samples processed by the estimator.  <br>It will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=n_samples_seen_,-int) | int | 10000 |\
| [scale\_ scale\_: ndarray of shape (n\_features,)  <br>  <br>Per feature relative scaling of the data. Equivalent to  <br>\`\`(max - min) / (X.max(axis=0) - X.min(axis=0))\`\`  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\* attribute.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[1. ,0.03,0.02,1.19,0.02\] |\
\
5 features\
\
|     |\
| --- |\
| year |\
| temp |\
| feel\_temp |\
| humidity |\
| windspeed |\
\
37 features\
\
|     |\
| --- |\
| season\_fall |\
| season\_spring |\
| season\_summer |\
| season\_winter |\
| holiday\_False |\
| holiday\_True |\
| workingday\_False |\
| workingday\_True |\
| weather\_clear |\
| weather\_misty |\
| weather\_rain |\
| month\_sp\_0 |\
| month\_sp\_1 |\
| month\_sp\_2 |\
| month\_sp\_3 |\
| month\_sp\_4 |\
| month\_sp\_5 |\
| weekday\_sp\_0 |\
| weekday\_sp\_1 |\
| weekday\_sp\_2 |\
| hour\_sp\_0 |\
| hour\_sp\_1 |\
| hour\_sp\_2 |\
| hour\_sp\_3 |\
| hour\_sp\_4 |\
| hour\_sp\_5 |\
| hour\_sp\_6 |\
| hour\_sp\_7 |\
| hour\_sp\_8 |\
| hour\_sp\_9 |\
| hour\_sp\_10 |\
| hour\_sp\_11 |\
| year |\
| temp |\
| feel\_temp |\
| humidity |\
| windspeed |\
\
interactions\
\
columntransformer: ColumnTransformer\
\
[?Documentation for columntransformer: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('cyclic\_hour', ...), ('workingday', ...)\] |\
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | False |\
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | 'drop' |\
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 12  |\
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'cyclic\_hour...nder': 'drop'} |\
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'cy...ur': slice(0, 8, None), 're...er': slice(0, 0, None), 'wo...ay': slice(8, 9, None)} |\
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |\
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('cy...ur', SplineTransfo... n\_knots=9), \['hour'\]), ('wo...ay', FunctionTrans...7e1dbc22ec40>), \['wo...ay'\]), ('re...er', 'drop', \['season', 'year', 'month', 'holiday', ...\])\] |\
\
cyclic\_hour\
\
\['hour'\]\
\
SplineTransformer\
\
[?Documentation for SplineTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [n\_knots n\_knots: int, default=5  <br>  <br>Number of knots of the splines if \`knots\` equals one of  <br>{'uniform', 'quantile'}. Must be larger or equal 2. Ignored if \`knots\`  <br>is array-like.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_knots,-int%2C%20default%3D5) | 9   |\
|     | [knots knots: {'uniform', 'quantile'} or array-like of shape (n\_knots, n\_features), default='uniform'  <br>  <br>Set knot positions such that first knot <= features <= last knot.  <br>  <br>\- If 'uniform', \`n\_knots\` number of knots are distributed uniformly  <br>from min to max values of the features.  <br>\- If 'quantile', they are distributed uniformly along the quantiles of  <br>the features.  <br>\- If an array-like is given, it directly specifies the sorted knot  <br>positions including the boundary knots. Note that, internally,  <br>\`degree\` number of knots are added before the first knot, the same  <br>after the last knot.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=knots,-int%2C%20default%3D5) | array(\[\[ 0.\],... \[24.\]\]) |\
|     | [extrapolation extrapolation: {'error', 'constant', 'linear', 'continue', 'periodic'}, default='constant'  <br>  <br>If 'error', values outside the min and max values of the training  <br>features raises a \`ValueError\`. If 'constant', the value of the  <br>splines at minimum and maximum value of the features is used as  <br>constant extrapolation. If 'linear', a linear extrapolation is used.  <br>If 'continue', the splines are extrapolated as is, i.e. option  <br>\`extrapolate=True\` in :class:\`scipy.interpolate.BSpline\`. If  <br>'periodic', periodic splines with a periodicity equal to the distance  <br>between the first and last knot are used. Periodic splines enforce  <br>equal function values and derivatives at the first and last knot.  <br>For example, this makes it possible to avoid introducing an arbitrary  <br>jump between Dec 31st and Jan 1st in spline features derived from a  <br>naturally periodic "day-of-year" input feature. In this case it is  <br>recommended to manually set the knot values to control the period.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=extrapolation,-%7B%27error%27%2C%20%27constant%27%2C%20%27linear%27%2C%20%27continue%27%2C%20%27periodic%27%7D%2C%20%20%20%20%20%20%20%20%20default%3D%27constant%27) | 'periodic' |\
|     | [degree degree: int, default=3  <br>  <br>The polynomial degree of the spline basis. Must be a non-negative  <br>integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=degree,-int%2C%20default%3D3) | 3   |\
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If False, then the last spline element inside the data range  <br>of a feature is dropped. As B-splines sum to one over the spline basis  <br>functions for each data point, they implicitly include a bias term,  <br>i.e. a column of ones. It acts as an intercept term in a linear models.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |\
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to compute, but  <br>may slow down subsequent estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |\
|     | [handle\_missing handle\_missing: {'error', 'zeros'}, default='error'  <br>  <br>Specifies the way missing values are handled.  <br>  <br>\- 'error' : Raise an error if \`np.nan\` values are present during :meth:\`fit\`.  <br>\- 'zeros' : Encode splines of missing values with values \`0\`.  <br>  <br>Note that \`handle\_missing='zeros'\` differs from first imputing missing values  <br>with zeros and then creating the spline basis. The latter creates spline basis  <br>functions which have non-zero values at the missing values  <br>whereas this option simply sets all spline basis function values to zero at the  <br>missing values.  <br>  <br>.. versionadded:: 1.8](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=handle_missing,-%7B%27error%27%2C%20%27zeros%27%7D%2C%20default%3D%27error%27) | 'error' |\
|     | [sparse\_output sparse\_output: bool, default=False  <br>  <br>Will return sparse CSR matrix if set True else will return an array.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=sparse_output,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [bsplines\_ bsplines\_: list of shape (n\_features,)  <br>  <br>List of BSplines objects, one for each feature.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=bsplines_,-list%20of%20shape%20%28n_features%2C%29) | list | \[<scipy.interp...x7e1dbdcee090>\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['hour'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>The total number of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
| [n\_features\_out\_ n\_features\_out\_: int  <br>  <br>The total number of output features, which is computed as  <br>\`n\_features \* n\_splines\`, where \`n\_splines\` is  <br>the number of bases elements of the B-splines,  <br>\`n\_knots + degree - 1\` for non-periodic splines and  <br>\`n\_knots - 1\` for periodic ones.  <br>If \`include\_bias=False\`, then it is only  <br>\`n\_features \* (n\_splines - 1)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_out_,-int) | int | 8   |\
\
8 features\
\
|     |\
| --- |\
| hour\_sp\_0 |\
| hour\_sp\_1 |\
| hour\_sp\_2 |\
| hour\_sp\_3 |\
| hour\_sp\_4 |\
| hour\_sp\_5 |\
| hour\_sp\_6 |\
| hour\_sp\_7 |\
\
workingday\
\
\['workingday'\]\
\
<lambda>\
\
FunctionTransformer\
\
[?Documentation for FunctionTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [func func: callable, default=None  <br>  <br>The callable to use for the transformation. This will be passed  <br>the same arguments as transform, with args and kwargs forwarded.  <br>If func is None, then func will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=func,-callable%2C%20default%3DNone) | <function <la...x7e1dbc22ec40> |\
|     | [feature\_names\_out feature\_names\_out: callable, 'one-to-one' or None, default=None  <br>  <br>Determines the list of feature names that will be returned by the  <br>\`get\_feature\_names\_out\` method. If it is 'one-to-one', then the output  <br>feature names will be equal to the input feature names. If it is a  <br>callable, then it must take two positional arguments: this  <br>\`FunctionTransformer\` (\`self\`) and an array-like of input feature names  <br>(\`input\_features\`). It must return an array-like of output feature  <br>names. The \`get\_feature\_names\_out\` method is only defined if  <br>\`feature\_names\_out\` is not None.  <br>  <br>See \`\`get\_feature\_names\_out\`\` for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_out,-callable%2C%20%27one-to-one%27%20or%20None%2C%20default%3DNone) | 'one-to-one' |\
|     | [inverse\_func inverse\_func: callable, default=None  <br>  <br>The callable to use for the inverse transformation. This will be  <br>passed the same arguments as inverse transform, with args and  <br>kwargs forwarded. If inverse\_func is None, then inverse\_func  <br>will be the identity function.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inverse_func,-callable%2C%20default%3DNone) | None |\
|     | [validate validate: bool, default=False  <br>  <br>Indicate that the input X array should be checked before calling  <br>\`\`func\`\`. The possibilities are:  <br>  <br>\- If False, there is no input validation.  <br>\- If True, then X will be converted to a 2-dimensional NumPy array or  <br>sparse matrix. If the conversion is not possible an exception is  <br>raised.  <br>  <br>.. versionchanged:: 0.22  <br>The default of \`\`validate\`\` changed from True to False.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=validate,-bool%2C%20default%3DFalse) | False |\
|     | [accept\_sparse accept\_sparse: bool, default=False  <br>  <br>Indicate that func accepts a sparse matrix as input. If validate is  <br>False, this has no effect. Otherwise, if accept\_sparse is false,  <br>sparse matrix inputs will cause an exception to be raised.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=accept_sparse,-bool%2C%20default%3DFalse) | False |\
|     | [check\_inverse check\_inverse: bool, default=True  <br>  <br>Whether to check that or \`\`func\`\` followed by \`\`inverse\_func\`\` leads to  <br>the original inputs. It can be used for a sanity check, raising a  <br>warning when the condition is not fulfilled.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=check_inverse,-bool%2C%20default%3DTrue) | True |\
|     | [kw\_args kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=kw_args,-dict%2C%20default%3DNone) | None |\
|     | [inv\_kw\_args inv\_kw\_args: dict, default=None  <br>  <br>Dictionary of additional keyword arguments to pass to inverse\_func.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=inv_kw_args,-dict%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\` has feature  <br>names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['workingday'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
\
1 feature\
\
workingday\
\
9 features\
\
|     |\
| --- |\
| hour\_sp\_0 |\
| hour\_sp\_1 |\
| hour\_sp\_2 |\
| hour\_sp\_3 |\
| hour\_sp\_4 |\
| hour\_sp\_5 |\
| hour\_sp\_6 |\
| hour\_sp\_7 |\
| workingday |\
\
PolynomialFeatures\
\
[?Documentation for PolynomialFeatures](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [interaction\_only interaction\_only: bool, default=False  <br>  <br>If \`True\`, only interaction features are produced: features that are  <br>products of at most \`degree\` \*distinct\* input features, i.e. terms with  <br>power of 2 or higher of the same input feature are excluded:  <br>  <br>\- included: \`x\[0\]\`, \`x\[1\]\`, \`x\[0\] \* x\[1\]\`, etc.  <br>\- excluded: \`x\[0\] \*\* 2\`, \`x\[0\] \*\* 2 \* x\[1\]\`, etc.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=interaction_only,-bool%2C%20default%3DFalse) | True |\
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If \`True\` (default), then include a bias column, the feature in which  <br>all polynomial powers are zero (i.e. a column of ones - acts as an  <br>intercept term in a linear model).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | False |\
|     | [degree degree: int or tuple (min\_degree, max\_degree), default=2  <br>  <br>If a single int is given, it specifies the maximal degree of the  <br>polynomial features. If a tuple \`(min\_degree, max\_degree)\` is passed,  <br>then \`min\_degree\` is the minimum and \`max\_degree\` is the maximum  <br>polynomial degree of the generated features. Note that \`min\_degree=0\`  <br>and \`min\_degree=1\` are equivalent as outputting the degree zero term is  <br>determined by \`include\_bias\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=degree,-int%20or%20tuple%20%28min_degree%2C%20max_degree%29%2C%20default%3D2) | 2   |\
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to  <br>compute, but may slow down subsequent estimators.  <br>  <br>.. versionadded:: 0.21](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](9,) | \['hour\_sp\_0','hour\_sp\_1','hour\_sp\_2',...,'hour\_sp\_6','hour\_sp\_7', 'workingday'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=n_features_in_,-int) | int | 9   |\
| [n\_output\_features\_ n\_output\_features\_: int  <br>  <br>The total number of polynomial output features. The number of output  <br>features is computed by iterating over all suitably sized combinations  <br>of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=n_output_features_,-int) | int | 45  |\
| [powers\_ powers\_: ndarray of shape (\`n\_output\_features\_\`, \`n\_features\_in\_\`)  <br>  <br>\`powers\_\[i, j\]\` is the exponent of the jth input in the ith output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=powers_,-ndarray%20of%20shape%20%28n_output_features_%2C%20n_features_in_%29) | ndarray\[int64\](45, 9) | \[\[1,0,0,...,0,0,0\], \[0,1,0,...,0,0,0\], \[0,0,1,...,0,0,0\], ..., \[0,0,0,...,1,1,0\], \[0,0,0,...,1,0,1\], \[0,0,0,...,0,1,1\]\] |\
\
45 features\
\
|     |\
| --- |\
| hour\_sp\_0 |\
| hour\_sp\_1 |\
| hour\_sp\_2 |\
| hour\_sp\_3 |\
| hour\_sp\_4 |\
| hour\_sp\_5 |\
| hour\_sp\_6 |\
| hour\_sp\_7 |\
| workingday |\
| hour\_sp\_0 hour\_sp\_1 |\
| hour\_sp\_0 hour\_sp\_2 |\
| hour\_sp\_0 hour\_sp\_3 |\
| hour\_sp\_0 hour\_sp\_4 |\
| hour\_sp\_0 hour\_sp\_5 |\
| hour\_sp\_0 hour\_sp\_6 |\
| hour\_sp\_0 hour\_sp\_7 |\
| hour\_sp\_0 workingday |\
| hour\_sp\_1 hour\_sp\_2 |\
| hour\_sp\_1 hour\_sp\_3 |\
| hour\_sp\_1 hour\_sp\_4 |\
| hour\_sp\_1 hour\_sp\_5 |\
| hour\_sp\_1 hour\_sp\_6 |\
| hour\_sp\_1 hour\_sp\_7 |\
| hour\_sp\_1 workingday |\
| hour\_sp\_2 hour\_sp\_3 |\
| hour\_sp\_2 hour\_sp\_4 |\
| hour\_sp\_2 hour\_sp\_5 |\
| hour\_sp\_2 hour\_sp\_6 |\
| hour\_sp\_2 hour\_sp\_7 |\
| hour\_sp\_2 workingday |\
| hour\_sp\_3 hour\_sp\_4 |\
| hour\_sp\_3 hour\_sp\_5 |\
| hour\_sp\_3 hour\_sp\_6 |\
| hour\_sp\_3 hour\_sp\_7 |\
| hour\_sp\_3 workingday |\
| hour\_sp\_4 hour\_sp\_5 |\
| hour\_sp\_4 hour\_sp\_6 |\
| hour\_sp\_4 hour\_sp\_7 |\
| hour\_sp\_4 workingday |\
| hour\_sp\_5 hour\_sp\_6 |\
| hour\_sp\_5 hour\_sp\_7 |\
| hour\_sp\_5 workingday |\
| hour\_sp\_6 hour\_sp\_7 |\
| hour\_sp\_6 workingday |\
| hour\_sp\_7 workingday |\
\
82 features\
\
|     |\
| --- |\
| marginal\_\_season\_fall |\
| marginal\_\_season\_spring |\
| marginal\_\_season\_summer |\
| marginal\_\_season\_winter |\
| marginal\_\_holiday\_False |\
| marginal\_\_holiday\_True |\
| marginal\_\_workingday\_False |\
| marginal\_\_workingday\_True |\
| marginal\_\_weather\_clear |\
| marginal\_\_weather\_misty |\
| marginal\_\_weather\_rain |\
| marginal\_\_month\_sp\_0 |\
| marginal\_\_month\_sp\_1 |\
| marginal\_\_month\_sp\_2 |\
| marginal\_\_month\_sp\_3 |\
| marginal\_\_month\_sp\_4 |\
| marginal\_\_month\_sp\_5 |\
| marginal\_\_weekday\_sp\_0 |\
| marginal\_\_weekday\_sp\_1 |\
| marginal\_\_weekday\_sp\_2 |\
| marginal\_\_hour\_sp\_0 |\
| marginal\_\_hour\_sp\_1 |\
| marginal\_\_hour\_sp\_2 |\
| marginal\_\_hour\_sp\_3 |\
| marginal\_\_hour\_sp\_4 |\
| marginal\_\_hour\_sp\_5 |\
| marginal\_\_hour\_sp\_6 |\
| marginal\_\_hour\_sp\_7 |\
| marginal\_\_hour\_sp\_8 |\
| marginal\_\_hour\_sp\_9 |\
| marginal\_\_hour\_sp\_10 |\
| marginal\_\_hour\_sp\_11 |\
| marginal\_\_year |\
| marginal\_\_temp |\
| marginal\_\_feel\_temp |\
| marginal\_\_humidity |\
| marginal\_\_windspeed |\
| interactions\_\_hour\_sp\_0 |\
| interactions\_\_hour\_sp\_1 |\
| interactions\_\_hour\_sp\_2 |\
| interactions\_\_hour\_sp\_3 |\
| interactions\_\_hour\_sp\_4 |\
| interactions\_\_hour\_sp\_5 |\
| interactions\_\_hour\_sp\_6 |\
| interactions\_\_hour\_sp\_7 |\
| interactions\_\_workingday |\
| interactions\_\_hour\_sp\_0 hour\_sp\_1 |\
| interactions\_\_hour\_sp\_0 hour\_sp\_2 |\
| interactions\_\_hour\_sp\_0 hour\_sp\_3 |\
| interactions\_\_hour\_sp\_0 hour\_sp\_4 |\
| interactions\_\_hour\_sp\_0 hour\_sp\_5 |\
| interactions\_\_hour\_sp\_0 hour\_sp\_6 |\
| interactions\_\_hour\_sp\_0 hour\_sp\_7 |\
| interactions\_\_hour\_sp\_0 workingday |\
| interactions\_\_hour\_sp\_1 hour\_sp\_2 |\
| interactions\_\_hour\_sp\_1 hour\_sp\_3 |\
| interactions\_\_hour\_sp\_1 hour\_sp\_4 |\
| interactions\_\_hour\_sp\_1 hour\_sp\_5 |\
| interactions\_\_hour\_sp\_1 hour\_sp\_6 |\
| interactions\_\_hour\_sp\_1 hour\_sp\_7 |\
| interactions\_\_hour\_sp\_1 workingday |\
| interactions\_\_hour\_sp\_2 hour\_sp\_3 |\
| interactions\_\_hour\_sp\_2 hour\_sp\_4 |\
| interactions\_\_hour\_sp\_2 hour\_sp\_5 |\
| interactions\_\_hour\_sp\_2 hour\_sp\_6 |\
| interactions\_\_hour\_sp\_2 hour\_sp\_7 |\
| interactions\_\_hour\_sp\_2 workingday |\
| interactions\_\_hour\_sp\_3 hour\_sp\_4 |\
| interactions\_\_hour\_sp\_3 hour\_sp\_5 |\
| interactions\_\_hour\_sp\_3 hour\_sp\_6 |\
| interactions\_\_hour\_sp\_3 hour\_sp\_7 |\
| interactions\_\_hour\_sp\_3 workingday |\
| interactions\_\_hour\_sp\_4 hour\_sp\_5 |\
| interactions\_\_hour\_sp\_4 hour\_sp\_6 |\
| interactions\_\_hour\_sp\_4 hour\_sp\_7 |\
| interactions\_\_hour\_sp\_4 workingday |\
| interactions\_\_hour\_sp\_5 hour\_sp\_6 |\
| interactions\_\_hour\_sp\_5 hour\_sp\_7 |\
| interactions\_\_hour\_sp\_5 workingday |\
| interactions\_\_hour\_sp\_6 hour\_sp\_7 |\
| interactions\_\_hour\_sp\_6 workingday |\
| interactions\_\_hour\_sp\_7 workingday |\
\
RidgeCV\
\
[?Documentation for RidgeCV](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [alphas alphas: array-like of shape (n\_alphas,), default=(0.1, 1.0, 10.0)  <br>  <br>Array of alpha values to try.  <br>Regularization strength; must be a positive float. Regularization  <br>improves the conditioning of the problem and reduces the variance of  <br>the estimates. Larger values specify stronger regularization.  <br>Alpha corresponds to \`\`1 / (2C)\`\` in other linear models such as  <br>:class:\`~sklearn.linear\_model.LogisticRegression\` or  <br>:class:\`~sklearn.svm.LinearSVC\`.  <br>If using Leave-One-Out cross-validation, alphas must be strictly positive.  <br>  <br>For an example on how regularization strength affects the model coefficients,  <br>see :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_ridge\_coeffs.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alphas,-array-like%20of%20shape%20%28n_alphas%2C%29%2C%20default%3D%280.1%2C%201.0%2C%2010.0%29) | array(\[1.0000...00000000e+06\]) |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to calculate the intercept for this model. If set  <br>to false, no intercept will be used in calculations  <br>(i.e. data is expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [scoring scoring: str, callable, default=None  <br>  <br>The scoring method to use for cross-validation. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: negative :ref:\`mean squared error <mean\_squared\_error>\` if cv is  <br>None (i.e. when using leave-one-out cross-validation), or  <br>:ref:\`coefficient of determination <r2\_score>\` (:math:\`R^2\`) otherwise.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=scoring,-str%2C%20callable%2C%20default%3DNone) | None |\
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the efficient Leave-One-Out cross-validation  <br>\- integer, to specify the number of folds,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if \`\`y\`\` is binary or multiclass,  <br>:class:\`~sklearn.model\_selection.StratifiedKFold\` is used, else,  <br>:class:\`~sklearn.model\_selection.KFold\` is used.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |\
|     | [gcv\_mode gcv\_mode: {'auto', 'svd', 'eigen'}, default='auto'  <br>  <br>Flag indicating which strategy to use when performing  <br>Leave-One-Out Cross-Validation. Options are::  <br>  <br>'auto' : same as 'eigen'  <br>'svd' : use singular value decomposition of X when X is dense,  <br>fallback to 'eigen' when X is sparse  <br>'eigen' : use eigendecomposition of X X' when n\_samples <= n\_features  <br>or X' X when n\_features < n\_samples  <br>  <br>The 'auto' mode is the default and is intended to pick the cheaper  <br>option depending on the shape and sparsity of the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=gcv_mode,-%7B%27auto%27%2C%20%27svd%27%2C%20%27eigen%27%7D%2C%20default%3D%27auto%27) | None |\
|     | [store\_cv\_results store\_cv\_results: bool, default=False  <br>  <br>Flag indicating if the cross-validation values corresponding to  <br>each alpha should be stored in the \`\`cv\_results\_\`\` attribute (see  <br>below). This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionchanged:: 1.5  <br>Parameter name changed from \`store\_cv\_values\` to \`store\_cv\_results\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=store_cv_results,-bool%2C%20default%3DFalse) | False |\
|     | [alpha\_per\_target alpha\_per\_target: bool, default=False  <br>  <br>Flag indicating whether to optimize the alpha value (picked from the  <br>\`alphas\` parameter list) for each target separately (for multi-output  <br>settings: multiple prediction targets). When set to \`True\`, after  <br>fitting, the \`alpha\_\` attribute will contain a value for each target.  <br>When set to \`False\`, a single alpha is used for all targets.  <br>This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_per_target,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [alpha\_ alpha\_: float or ndarray of shape (n\_targets,)  <br>  <br>Estimated regularization parameter, or, if \`\`alpha\_per\_target=True\`\`,  <br>the estimated regularization parameter for each target.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float | 0.0001 |\
| [best\_score\_ best\_score\_: float or ndarray of shape (n\_targets,)  <br>  <br>Score of base estimator with best alpha, or, if  <br>\`\`alpha\_per\_target=True\`\`, a score for each target.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=best_score_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | \-0.004999 |\
| [coef\_ coef\_: ndarray of shape (n\_features) or (n\_targets, n\_features)  <br>  <br>Weight vector(s).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=coef_,-ndarray%20of%20shape%20%28n_features%29%20or%20%28n_targets%2C%20n_features%29) | ndarray\[float64\](82,) | \[ 0. ,-0.03, 0. ,..., 4.57,-0.18, 0.3 \] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](82,) | \['marginal\_\_season\_fall','marginal\_\_season\_spring', 'marginal\_\_season\_summer',...,'interactions\_\_hour\_sp\_6 hour\_sp\_7', 'interactions\_\_hour\_sp\_6 workingday','interactions\_\_hour\_sp\_7 workingday'\] |\
| [intercept\_ intercept\_: float or ndarray of shape (n\_targets,)  <br>  <br>Independent term in decision function. Set to 0.0 if  <br>\`\`fit\_intercept = False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=intercept_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | 0.05941 |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=n_features_in_,-int) | int | 82  |\
\
  \
  \
\
Modeling non-linear feature interactions with kernels[#](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#modeling-non-linear-feature-interactions-with-kernels "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
The previous analysis highlighted the need to model the interactions between `"workingday"` and `"hours"`. Another example of a such a non-linear interaction that we would like to model could be the impact of the rain that might not be the same during the working days and the week-ends and holidays for instance.\
\
To model all such interactions, we could either use a polynomial expansion on all marginal features at once, after their spline-based expansion. However, this would create a quadratic number of features which can cause overfitting and computational tractability issues.\
\
Alternatively, we can use the Nyström method to compute an approximate polynomial kernel expansion. Let us try the latter:\
\
from sklearn.kernel\_approximation import [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")\
\
cyclic\_spline\_poly\_pipeline \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
    cyclic\_spline\_transformer,\
    [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")\
(kernel\="poly", degree\=2, n\_components\=300, random\_state\=0),\
    [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")\
(alphas\=alphas),\
)\
evaluate(cyclic\_spline\_poly\_pipeline, X, y, cv\=ts\_cv)\
\
Copy to clipboard\
\
Mean Absolute Error:     0.053 +/- 0.002\
Root Mean Squared Error: 0.076 +/- 0.004\
\
Copy to clipboard\
\
Pipeline(steps=\[('columntransformer',\
                 ColumnTransformer(remainder=MinMaxScaler(),\
                                   transformers=\[('categorical',\
                                                  OneHotEncoder(handle\_unknown='ignore',\
                                                                sparse\_output=False),\
                                                  Index(\['season', 'holiday', 'workingday', 'weather'\], dtype='str')),\
                                                 ('cyclic\_month',\
                                                  SplineTransformer(extrapolation='periodic',\
                                                                    knots=array(\[\[ 0.\],\
       \[ 2.\],\
       \[ 4.\],\
       \[ 6.\],\
       \[ 8.\],\
       \[10.\],\
       \[12.\]\]),\
                                                                    n\_knots...\
                 RidgeCV(alphas=array(\[1.00000000e-06, 3.16227766e-06, 1.00000000e-05, 3.16227766e-05,\
       1.00000000e-04, 3.16227766e-04, 1.00000000e-03, 3.16227766e-03,\
       1.00000000e-02, 3.16227766e-02, 1.00000000e-01, 3.16227766e-01,\
       1.00000000e+00, 3.16227766e+00, 1.00000000e+01, 3.16227766e+01,\
       1.00000000e+02, 3.16227766e+02, 1.00000000e+03, 3.16227766e+03,\
       1.00000000e+04, 3.16227766e+04, 1.00000000e+05, 3.16227766e+05,\
       1.00000000e+06\])))\])\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
Pipeline\
\
[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)\
iFitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('columntransformer', ...), ('nystroem', ...), ...\] |\
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |\
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 12  |\
\
columntransformer: ColumnTransformer\
\
[?Documentation for columntransformer: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('categorical', ...), ('cyclic\_month', ...), ...\] |\
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | MinMaxScaler() |\
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | False |\
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 12  |\
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'categorical...inMaxScaler()} |\
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'ca...al': slice(0, 11, None), 'cy...ur': slice(20, 32, None), 'cy...th': slice(11, 17, None), 'cy...ay': slice(17, 20, None), ...} |\
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |\
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('ca...al', OneHotEncoder...\_output=False), Index(\['seaso..., dtype='str')), ('cy...th', SplineTransfo... n\_knots=7), \['month'\]), ('cy...ay', SplineTransfo... n\_knots=4), \['weekday'\]), ('cy...ur', SplineTransfo... n\_knots=13), \['hour'\]), ...\] |\
\
categorical\
\
Index(\['season', 'holiday', 'workingday', 'weather'\], dtype='str')\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | False |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\['fall'... dtype=object), array(\['False... dtype=object), array(\['False... dtype=object), array(\['clear... dtype=object)\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](4,) | \['season','holiday','workingday','weather'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 4   |\
\
11 features\
\
|     |\
| --- |\
| season\_fall |\
| season\_spring |\
| season\_summer |\
| season\_winter |\
| holiday\_False |\
| holiday\_True |\
| workingday\_False |\
| workingday\_True |\
| weather\_clear |\
| weather\_misty |\
| weather\_rain |\
\
cyclic\_month\
\
\['month'\]\
\
SplineTransformer\
\
[?Documentation for SplineTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [n\_knots n\_knots: int, default=5  <br>  <br>Number of knots of the splines if \`knots\` equals one of  <br>{'uniform', 'quantile'}. Must be larger or equal 2. Ignored if \`knots\`  <br>is array-like.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_knots,-int%2C%20default%3D5) | 7   |\
|     | [knots knots: {'uniform', 'quantile'} or array-like of shape (n\_knots, n\_features), default='uniform'  <br>  <br>Set knot positions such that first knot <= features <= last knot.  <br>  <br>\- If 'uniform', \`n\_knots\` number of knots are distributed uniformly  <br>from min to max values of the features.  <br>\- If 'quantile', they are distributed uniformly along the quantiles of  <br>the features.  <br>\- If an array-like is given, it directly specifies the sorted knot  <br>positions including the boundary knots. Note that, internally,  <br>\`degree\` number of knots are added before the first knot, the same  <br>after the last knot.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=knots,-int%2C%20default%3D5) | array(\[\[ 0.\],... \[12.\]\]) |\
|     | [extrapolation extrapolation: {'error', 'constant', 'linear', 'continue', 'periodic'}, default='constant'  <br>  <br>If 'error', values outside the min and max values of the training  <br>features raises a \`ValueError\`. If 'constant', the value of the  <br>splines at minimum and maximum value of the features is used as  <br>constant extrapolation. If 'linear', a linear extrapolation is used.  <br>If 'continue', the splines are extrapolated as is, i.e. option  <br>\`extrapolate=True\` in :class:\`scipy.interpolate.BSpline\`. If  <br>'periodic', periodic splines with a periodicity equal to the distance  <br>between the first and last knot are used. Periodic splines enforce  <br>equal function values and derivatives at the first and last knot.  <br>For example, this makes it possible to avoid introducing an arbitrary  <br>jump between Dec 31st and Jan 1st in spline features derived from a  <br>naturally periodic "day-of-year" input feature. In this case it is  <br>recommended to manually set the knot values to control the period.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=extrapolation,-%7B%27error%27%2C%20%27constant%27%2C%20%27linear%27%2C%20%27continue%27%2C%20%27periodic%27%7D%2C%20%20%20%20%20%20%20%20%20default%3D%27constant%27) | 'periodic' |\
|     | [degree degree: int, default=3  <br>  <br>The polynomial degree of the spline basis. Must be a non-negative  <br>integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=degree,-int%2C%20default%3D3) | 3   |\
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If False, then the last spline element inside the data range  <br>of a feature is dropped. As B-splines sum to one over the spline basis  <br>functions for each data point, they implicitly include a bias term,  <br>i.e. a column of ones. It acts as an intercept term in a linear models.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |\
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to compute, but  <br>may slow down subsequent estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |\
|     | [handle\_missing handle\_missing: {'error', 'zeros'}, default='error'  <br>  <br>Specifies the way missing values are handled.  <br>  <br>\- 'error' : Raise an error if \`np.nan\` values are present during :meth:\`fit\`.  <br>\- 'zeros' : Encode splines of missing values with values \`0\`.  <br>  <br>Note that \`handle\_missing='zeros'\` differs from first imputing missing values  <br>with zeros and then creating the spline basis. The latter creates spline basis  <br>functions which have non-zero values at the missing values  <br>whereas this option simply sets all spline basis function values to zero at the  <br>missing values.  <br>  <br>.. versionadded:: 1.8](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=handle_missing,-%7B%27error%27%2C%20%27zeros%27%7D%2C%20default%3D%27error%27) | 'error' |\
|     | [sparse\_output sparse\_output: bool, default=False  <br>  <br>Will return sparse CSR matrix if set True else will return an array.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=sparse_output,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [bsplines\_ bsplines\_: list of shape (n\_features,)  <br>  <br>List of BSplines objects, one for each feature.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=bsplines_,-list%20of%20shape%20%28n_features%2C%29) | list | \[<scipy.interp...x7e1dbde30a10>\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['month'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>The total number of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
| [n\_features\_out\_ n\_features\_out\_: int  <br>  <br>The total number of output features, which is computed as  <br>\`n\_features \* n\_splines\`, where \`n\_splines\` is  <br>the number of bases elements of the B-splines,  <br>\`n\_knots + degree - 1\` for non-periodic splines and  <br>\`n\_knots - 1\` for periodic ones.  <br>If \`include\_bias=False\`, then it is only  <br>\`n\_features \* (n\_splines - 1)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_out_,-int) | int | 6   |\
\
6 features\
\
|     |\
| --- |\
| month\_sp\_0 |\
| month\_sp\_1 |\
| month\_sp\_2 |\
| month\_sp\_3 |\
| month\_sp\_4 |\
| month\_sp\_5 |\
\
cyclic\_weekday\
\
\['weekday'\]\
\
SplineTransformer\
\
[?Documentation for SplineTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [n\_knots n\_knots: int, default=5  <br>  <br>Number of knots of the splines if \`knots\` equals one of  <br>{'uniform', 'quantile'}. Must be larger or equal 2. Ignored if \`knots\`  <br>is array-like.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_knots,-int%2C%20default%3D5) | 4   |\
|     | [knots knots: {'uniform', 'quantile'} or array-like of shape (n\_knots, n\_features), default='uniform'  <br>  <br>Set knot positions such that first knot <= features <= last knot.  <br>  <br>\- If 'uniform', \`n\_knots\` number of knots are distributed uniformly  <br>from min to max values of the features.  <br>\- If 'quantile', they are distributed uniformly along the quantiles of  <br>the features.  <br>\- If an array-like is given, it directly specifies the sorted knot  <br>positions including the boundary knots. Note that, internally,  <br>\`degree\` number of knots are added before the first knot, the same  <br>after the last knot.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=knots,-int%2C%20default%3D5) | array(\[\[0. ...\[7. \]\]) |\
|     | [extrapolation extrapolation: {'error', 'constant', 'linear', 'continue', 'periodic'}, default='constant'  <br>  <br>If 'error', values outside the min and max values of the training  <br>features raises a \`ValueError\`. If 'constant', the value of the  <br>splines at minimum and maximum value of the features is used as  <br>constant extrapolation. If 'linear', a linear extrapolation is used.  <br>If 'continue', the splines are extrapolated as is, i.e. option  <br>\`extrapolate=True\` in :class:\`scipy.interpolate.BSpline\`. If  <br>'periodic', periodic splines with a periodicity equal to the distance  <br>between the first and last knot are used. Periodic splines enforce  <br>equal function values and derivatives at the first and last knot.  <br>For example, this makes it possible to avoid introducing an arbitrary  <br>jump between Dec 31st and Jan 1st in spline features derived from a  <br>naturally periodic "day-of-year" input feature. In this case it is  <br>recommended to manually set the knot values to control the period.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=extrapolation,-%7B%27error%27%2C%20%27constant%27%2C%20%27linear%27%2C%20%27continue%27%2C%20%27periodic%27%7D%2C%20%20%20%20%20%20%20%20%20default%3D%27constant%27) | 'periodic' |\
|     | [degree degree: int, default=3  <br>  <br>The polynomial degree of the spline basis. Must be a non-negative  <br>integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=degree,-int%2C%20default%3D3) | 3   |\
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If False, then the last spline element inside the data range  <br>of a feature is dropped. As B-splines sum to one over the spline basis  <br>functions for each data point, they implicitly include a bias term,  <br>i.e. a column of ones. It acts as an intercept term in a linear models.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |\
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to compute, but  <br>may slow down subsequent estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |\
|     | [handle\_missing handle\_missing: {'error', 'zeros'}, default='error'  <br>  <br>Specifies the way missing values are handled.  <br>  <br>\- 'error' : Raise an error if \`np.nan\` values are present during :meth:\`fit\`.  <br>\- 'zeros' : Encode splines of missing values with values \`0\`.  <br>  <br>Note that \`handle\_missing='zeros'\` differs from first imputing missing values  <br>with zeros and then creating the spline basis. The latter creates spline basis  <br>functions which have non-zero values at the missing values  <br>whereas this option simply sets all spline basis function values to zero at the  <br>missing values.  <br>  <br>.. versionadded:: 1.8](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=handle_missing,-%7B%27error%27%2C%20%27zeros%27%7D%2C%20default%3D%27error%27) | 'error' |\
|     | [sparse\_output sparse\_output: bool, default=False  <br>  <br>Will return sparse CSR matrix if set True else will return an array.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=sparse_output,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [bsplines\_ bsplines\_: list of shape (n\_features,)  <br>  <br>List of BSplines objects, one for each feature.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=bsplines_,-list%20of%20shape%20%28n_features%2C%29) | list | \[<scipy.interp...x7e1dbde32150>\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['weekday'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>The total number of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
| [n\_features\_out\_ n\_features\_out\_: int  <br>  <br>The total number of output features, which is computed as  <br>\`n\_features \* n\_splines\`, where \`n\_splines\` is  <br>the number of bases elements of the B-splines,  <br>\`n\_knots + degree - 1\` for non-periodic splines and  <br>\`n\_knots - 1\` for periodic ones.  <br>If \`include\_bias=False\`, then it is only  <br>\`n\_features \* (n\_splines - 1)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_out_,-int) | int | 3   |\
\
3 features\
\
|     |\
| --- |\
| weekday\_sp\_0 |\
| weekday\_sp\_1 |\
| weekday\_sp\_2 |\
\
cyclic\_hour\
\
\['hour'\]\
\
SplineTransformer\
\
[?Documentation for SplineTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [n\_knots n\_knots: int, default=5  <br>  <br>Number of knots of the splines if \`knots\` equals one of  <br>{'uniform', 'quantile'}. Must be larger or equal 2. Ignored if \`knots\`  <br>is array-like.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_knots,-int%2C%20default%3D5) | 13  |\
|     | [knots knots: {'uniform', 'quantile'} or array-like of shape (n\_knots, n\_features), default='uniform'  <br>  <br>Set knot positions such that first knot <= features <= last knot.  <br>  <br>\- If 'uniform', \`n\_knots\` number of knots are distributed uniformly  <br>from min to max values of the features.  <br>\- If 'quantile', they are distributed uniformly along the quantiles of  <br>the features.  <br>\- If an array-like is given, it directly specifies the sorted knot  <br>positions including the boundary knots. Note that, internally,  <br>\`degree\` number of knots are added before the first knot, the same  <br>after the last knot.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=knots,-int%2C%20default%3D5) | array(\[\[ 0.\],... \[24.\]\]) |\
|     | [extrapolation extrapolation: {'error', 'constant', 'linear', 'continue', 'periodic'}, default='constant'  <br>  <br>If 'error', values outside the min and max values of the training  <br>features raises a \`ValueError\`. If 'constant', the value of the  <br>splines at minimum and maximum value of the features is used as  <br>constant extrapolation. If 'linear', a linear extrapolation is used.  <br>If 'continue', the splines are extrapolated as is, i.e. option  <br>\`extrapolate=True\` in :class:\`scipy.interpolate.BSpline\`. If  <br>'periodic', periodic splines with a periodicity equal to the distance  <br>between the first and last knot are used. Periodic splines enforce  <br>equal function values and derivatives at the first and last knot.  <br>For example, this makes it possible to avoid introducing an arbitrary  <br>jump between Dec 31st and Jan 1st in spline features derived from a  <br>naturally periodic "day-of-year" input feature. In this case it is  <br>recommended to manually set the knot values to control the period.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=extrapolation,-%7B%27error%27%2C%20%27constant%27%2C%20%27linear%27%2C%20%27continue%27%2C%20%27periodic%27%7D%2C%20%20%20%20%20%20%20%20%20default%3D%27constant%27) | 'periodic' |\
|     | [degree degree: int, default=3  <br>  <br>The polynomial degree of the spline basis. Must be a non-negative  <br>integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=degree,-int%2C%20default%3D3) | 3   |\
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If False, then the last spline element inside the data range  <br>of a feature is dropped. As B-splines sum to one over the spline basis  <br>functions for each data point, they implicitly include a bias term,  <br>i.e. a column of ones. It acts as an intercept term in a linear models.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |\
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to compute, but  <br>may slow down subsequent estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |\
|     | [handle\_missing handle\_missing: {'error', 'zeros'}, default='error'  <br>  <br>Specifies the way missing values are handled.  <br>  <br>\- 'error' : Raise an error if \`np.nan\` values are present during :meth:\`fit\`.  <br>\- 'zeros' : Encode splines of missing values with values \`0\`.  <br>  <br>Note that \`handle\_missing='zeros'\` differs from first imputing missing values  <br>with zeros and then creating the spline basis. The latter creates spline basis  <br>functions which have non-zero values at the missing values  <br>whereas this option simply sets all spline basis function values to zero at the  <br>missing values.  <br>  <br>.. versionadded:: 1.8](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=handle_missing,-%7B%27error%27%2C%20%27zeros%27%7D%2C%20default%3D%27error%27) | 'error' |\
|     | [sparse\_output sparse\_output: bool, default=False  <br>  <br>Will return sparse CSR matrix if set True else will return an array.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=sparse_output,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [bsplines\_ bsplines\_: list of shape (n\_features,)  <br>  <br>List of BSplines objects, one for each feature.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=bsplines_,-list%20of%20shape%20%28n_features%2C%29) | list | \[<scipy.interp...x7e1dbde323f0>\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](1,) | \['hour'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>The total number of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_in_,-int) | int | 1   |\
| [n\_features\_out\_ n\_features\_out\_: int  <br>  <br>The total number of output features, which is computed as  <br>\`n\_features \* n\_splines\`, where \`n\_splines\` is  <br>the number of bases elements of the B-splines,  <br>\`n\_knots + degree - 1\` for non-periodic splines and  <br>\`n\_knots - 1\` for periodic ones.  <br>If \`include\_bias=False\`, then it is only  <br>\`n\_features \* (n\_splines - 1)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_out_,-int) | int | 12  |\
\
12 features\
\
|     |\
| --- |\
| hour\_sp\_0 |\
| hour\_sp\_1 |\
| hour\_sp\_2 |\
| hour\_sp\_3 |\
| hour\_sp\_4 |\
| hour\_sp\_5 |\
| hour\_sp\_6 |\
| hour\_sp\_7 |\
| hour\_sp\_8 |\
| hour\_sp\_9 |\
| hour\_sp\_10 |\
| hour\_sp\_11 |\
\
remainder\
\
\['year', 'temp', 'feel\_temp', 'humidity', 'windspeed'\]\
\
MinMaxScaler\
\
[?Documentation for MinMaxScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [feature\_range feature\_range: tuple (min, max), default=(0, 1)  <br>  <br>Desired range of transformed data.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=feature_range,-tuple%20%28min%2C%20max%29%2C%20default%3D%280%2C%201%29) | (0, ...) |\
|     | [copy copy: bool, default=True  <br>  <br>Set to False to perform inplace row normalization and avoid a  <br>copy (if the input is already a numpy array).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [clip clip: bool, default=False  <br>  <br>Set to True to clip transformed values of held-out data to  <br>provided \`feature\_range\`.  <br>Since this parameter will clip values, \`inverse\_transform\` may not  <br>be able to restore the original data.  <br>  <br>.. note::  <br>Setting \`clip=True\` does not prevent feature drift (a distribution  <br>shift between training and test data). The transformed values are clipped  <br>to the \`feature\_range\`, which helps avoid unintended behavior in models  <br>sensitive to out-of-range inputs (e.g. linear models). Use with care,  <br>as clipping can distort the distribution of test data.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=clip,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [data\_max\_ data\_max\_: ndarray of shape (n\_features,)  <br>  <br>Per feature maximum seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_max\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_max_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 1. ,39.36,50. , 1. ,57. \] |\
| [data\_min\_ data\_min\_: ndarray of shape (n\_features,)  <br>  <br>Per feature minimum seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_min\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_min_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[0. ,0.82,0.76,0.16,0. \] |\
| [data\_range\_ data\_range\_: ndarray of shape (n\_features,)  <br>  <br>Per feature range \`\`(data\_max\_ - data\_min\_)\`\` seen in the data  <br>  <br>.. versionadded:: 0.17  <br>\*data\_range\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=data_range_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 1. ,38.54,49.24, 0.84,57. \] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](5,) | \['year','temp','feel\_temp','humidity','windspeed'\] |\
| [min\_ min\_: ndarray of shape (n\_features,)  <br>  <br>Per feature adjustment for minimum. Equivalent to  <br>\`\`min - X.min(axis=0) \* self.scale\_\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=min_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[ 0. ,-0.02,-0.02,-0.19, 0. \] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=n_features_in_,-int) | int | 5   |\
| [n\_samples\_seen\_ n\_samples\_seen\_: int  <br>  <br>The number of samples processed by the estimator.  <br>It will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=n_samples_seen_,-int) | int | 10000 |\
| [scale\_ scale\_: ndarray of shape (n\_features,)  <br>  <br>Per feature relative scaling of the data. Equivalent to  <br>\`\`(max - min) / (X.max(axis=0) - X.min(axis=0))\`\`  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\* attribute.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.MinMaxScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[1. ,0.03,0.02,1.19,0.02\] |\
\
5 features\
\
|     |\
| --- |\
| year |\
| temp |\
| feel\_temp |\
| humidity |\
| windspeed |\
\
37 features\
\
|     |\
| --- |\
| season\_fall |\
| season\_spring |\
| season\_summer |\
| season\_winter |\
| holiday\_False |\
| holiday\_True |\
| workingday\_False |\
| workingday\_True |\
| weather\_clear |\
| weather\_misty |\
| weather\_rain |\
| month\_sp\_0 |\
| month\_sp\_1 |\
| month\_sp\_2 |\
| month\_sp\_3 |\
| month\_sp\_4 |\
| month\_sp\_5 |\
| weekday\_sp\_0 |\
| weekday\_sp\_1 |\
| weekday\_sp\_2 |\
| hour\_sp\_0 |\
| hour\_sp\_1 |\
| hour\_sp\_2 |\
| hour\_sp\_3 |\
| hour\_sp\_4 |\
| hour\_sp\_5 |\
| hour\_sp\_6 |\
| hour\_sp\_7 |\
| hour\_sp\_8 |\
| hour\_sp\_9 |\
| hour\_sp\_10 |\
| hour\_sp\_11 |\
| year |\
| temp |\
| feel\_temp |\
| humidity |\
| windspeed |\
\
Nystroem\
\
[?Documentation for Nystroem](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [kernel kernel: str or callable, default='rbf'  <br>  <br>Kernel map to be approximated. A callable should accept two arguments  <br>and the keyword arguments passed to this object as \`kernel\_params\`, and  <br>should return a floating point number.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=kernel,-str%20or%20callable%2C%20default%3D%27rbf%27) | 'poly' |\
|     | [degree degree: float, default=None  <br>  <br>Degree of the polynomial kernel. Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=degree,-float%2C%20default%3DNone) | 2   |\
|     | [n\_components n\_components: int, default=100  <br>  <br>Number of features to construct.  <br>How many data points will be used to construct the mapping.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=n_components,-int%2C%20default%3D100) | 300 |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo-random number generator to control the uniform sampling without  <br>replacement of \`n\_components\` of the training data to construct the  <br>basis kernel.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |\
|     | [gamma gamma: float, default=None  <br>  <br>Gamma parameter for the RBF, laplacian, polynomial, exponential chi2  <br>and sigmoid kernels. Interpretation of the default value is left to  <br>the kernel; see the documentation for sklearn.metrics.pairwise.  <br>Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=gamma,-float%2C%20default%3DNone) | None |\
|     | [coef0 coef0: float, default=None  <br>  <br>Zero coefficient for polynomial and sigmoid kernels.  <br>Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=coef0,-float%2C%20default%3DNone) | None |\
|     | [kernel\_params kernel\_params: dict, default=None  <br>  <br>Additional parameters (keyword arguments) for kernel function passed  <br>as callable object.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=kernel_params,-dict%2C%20default%3DNone) | None |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to use for the computation. This works by breaking  <br>down the kernel matrix into \`n\_jobs\` even slices and computing them in  <br>parallel.  <br>  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [component\_indices\_ component\_indices\_: ndarray of shape (n\_components)  <br>  <br>Indices of \`\`components\_\`\` in the training set.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=component_indices_,-ndarray%20of%20shape%20%28n_components%29) | ndarray\[int64\](300,) | \[9394, 898,2398,...,2685,5725,8051\] |\
| [components\_ components\_: ndarray of shape (n\_components, n\_features)  <br>  <br>Subset of training points used to construct the feature map.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=components_,-ndarray%20of%20shape%20%28n_components%2C%20n_features%29) | ndarray\[float64\](300, 37) | \[\[0. ,0. ,1. ,...,0.6 ,0.63,0.33\], \[0. ,0. ,1. ,...,0.51,0.86,0.19\], \[1. ,0. ,0. ,...,0.74,0.7 ,0.3 \], ..., \[1. ,0. ,0. ,...,0.65,0.64,0.11\], \[0. ,0. ,0. ,...,0.43,1. ,0. \], \[0. ,1. ,0. ,...,0.63,0.25,0.12\]\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](37,) | \['season\_fall','season\_spring','season\_summer',...,'feel\_temp','humidity', 'windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=n_features_in_,-int) | int | 37  |\
| [normalization\_ normalization\_: ndarray of shape (n\_components, n\_components)  <br>  <br>Normalization matrix needed for embedding.  <br>Square root of the kernel matrix on \`\`components\_\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=normalization_,-ndarray%20of%20shape%20%28n_components%2C%20n_components%29) | ndarray\[float64\](300, 300) | \[\[ 71.07, 2.07, 11.92,..., -3.79, -1.28, -4.85\], \[ 2.07, 42.81, 2.42,..., 1.85, -1.69, -0.97\], \[ 11.92, 2.42,149.76,...,-20.1 , 0.77, -2.76\], ..., \[ -3.79, 1.85,-20.1 ,...,112.03, -0.52, -2.54\], \[ -1.28, -1.69, 0.77,..., -0.52, 27.07, 1.13\], \[ -4.85, -0.97, -2.76,..., -2.54, 1.13, 82.79\]\] |\
\
100 of 300 features\
\
|     |\
| --- |\
| nystroem0 |\
| nystroem1 |\
| nystroem2 |\
| nystroem3 |\
| nystroem4 |\
| nystroem5 |\
| nystroem6 |\
| nystroem7 |\
| nystroem8 |\
| nystroem9 |\
| nystroem10 |\
| nystroem11 |\
| nystroem12 |\
| nystroem13 |\
| nystroem14 |\
| nystroem15 |\
| nystroem16 |\
| nystroem17 |\
| nystroem18 |\
| nystroem19 |\
| nystroem20 |\
| nystroem21 |\
| nystroem22 |\
| nystroem23 |\
| nystroem24 |\
| nystroem25 |\
| nystroem26 |\
| nystroem27 |\
| nystroem28 |\
| nystroem29 |\
| nystroem30 |\
| nystroem31 |\
| nystroem32 |\
| nystroem33 |\
| nystroem34 |\
| nystroem35 |\
| nystroem36 |\
| nystroem37 |\
| nystroem38 |\
| nystroem39 |\
| nystroem40 |\
| nystroem41 |\
| nystroem42 |\
| nystroem43 |\
| nystroem44 |\
| nystroem45 |\
| nystroem46 |\
| nystroem47 |\
| nystroem48 |\
| nystroem49 |\
| nystroem50 |\
| nystroem51 |\
| nystroem52 |\
| nystroem53 |\
| nystroem54 |\
| nystroem55 |\
| nystroem56 |\
| nystroem57 |\
| nystroem58 |\
| nystroem59 |\
| nystroem60 |\
| nystroem61 |\
| nystroem62 |\
| nystroem63 |\
| nystroem64 |\
| nystroem65 |\
| nystroem66 |\
| nystroem67 |\
| nystroem68 |\
| nystroem69 |\
| nystroem70 |\
| nystroem71 |\
| nystroem72 |\
| nystroem73 |\
| nystroem74 |\
| nystroem75 |\
| nystroem76 |\
| nystroem77 |\
| nystroem78 |\
| nystroem79 |\
| nystroem80 |\
| nystroem81 |\
| nystroem82 |\
| nystroem83 |\
| nystroem84 |\
| nystroem85 |\
| nystroem86 |\
| nystroem87 |\
| nystroem88 |\
| nystroem89 |\
| nystroem90 |\
| nystroem91 |\
| nystroem92 |\
| nystroem93 |\
| nystroem94 |\
| nystroem95 |\
| nystroem96 |\
| nystroem97 |\
| nystroem98 |\
| nystroem99 |\
\
RidgeCV\
\
[?Documentation for RidgeCV](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [alphas alphas: array-like of shape (n\_alphas,), default=(0.1, 1.0, 10.0)  <br>  <br>Array of alpha values to try.  <br>Regularization strength; must be a positive float. Regularization  <br>improves the conditioning of the problem and reduces the variance of  <br>the estimates. Larger values specify stronger regularization.  <br>Alpha corresponds to \`\`1 / (2C)\`\` in other linear models such as  <br>:class:\`~sklearn.linear\_model.LogisticRegression\` or  <br>:class:\`~sklearn.svm.LinearSVC\`.  <br>If using Leave-One-Out cross-validation, alphas must be strictly positive.  <br>  <br>For an example on how regularization strength affects the model coefficients,  <br>see :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_ridge\_coeffs.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alphas,-array-like%20of%20shape%20%28n_alphas%2C%29%2C%20default%3D%280.1%2C%201.0%2C%2010.0%29) | array(\[1.0000...00000000e+06\]) |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to calculate the intercept for this model. If set  <br>to false, no intercept will be used in calculations  <br>(i.e. data is expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [scoring scoring: str, callable, default=None  <br>  <br>The scoring method to use for cross-validation. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: negative :ref:\`mean squared error <mean\_squared\_error>\` if cv is  <br>None (i.e. when using leave-one-out cross-validation), or  <br>:ref:\`coefficient of determination <r2\_score>\` (:math:\`R^2\`) otherwise.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=scoring,-str%2C%20callable%2C%20default%3DNone) | None |\
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the efficient Leave-One-Out cross-validation  <br>\- integer, to specify the number of folds,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if \`\`y\`\` is binary or multiclass,  <br>:class:\`~sklearn.model\_selection.StratifiedKFold\` is used, else,  <br>:class:\`~sklearn.model\_selection.KFold\` is used.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |\
|     | [gcv\_mode gcv\_mode: {'auto', 'svd', 'eigen'}, default='auto'  <br>  <br>Flag indicating which strategy to use when performing  <br>Leave-One-Out Cross-Validation. Options are::  <br>  <br>'auto' : same as 'eigen'  <br>'svd' : use singular value decomposition of X when X is dense,  <br>fallback to 'eigen' when X is sparse  <br>'eigen' : use eigendecomposition of X X' when n\_samples <= n\_features  <br>or X' X when n\_features < n\_samples  <br>  <br>The 'auto' mode is the default and is intended to pick the cheaper  <br>option depending on the shape and sparsity of the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=gcv_mode,-%7B%27auto%27%2C%20%27svd%27%2C%20%27eigen%27%7D%2C%20default%3D%27auto%27) | None |\
|     | [store\_cv\_results store\_cv\_results: bool, default=False  <br>  <br>Flag indicating if the cross-validation values corresponding to  <br>each alpha should be stored in the \`\`cv\_results\_\`\` attribute (see  <br>below). This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionchanged:: 1.5  <br>Parameter name changed from \`store\_cv\_values\` to \`store\_cv\_results\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=store_cv_results,-bool%2C%20default%3DFalse) | False |\
|     | [alpha\_per\_target alpha\_per\_target: bool, default=False  <br>  <br>Flag indicating whether to optimize the alpha value (picked from the  <br>\`alphas\` parameter list) for each target separately (for multi-output  <br>settings: multiple prediction targets). When set to \`True\`, after  <br>fitting, the \`alpha\_\` attribute will contain a value for each target.  <br>When set to \`False\`, a single alpha is used for all targets.  <br>This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_per_target,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [alpha\_ alpha\_: float or ndarray of shape (n\_targets,)  <br>  <br>Estimated regularization parameter, or, if \`\`alpha\_per\_target=True\`\`,  <br>the estimated regularization parameter for each target.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float | 0.0003162 |\
| [best\_score\_ best\_score\_: float or ndarray of shape (n\_targets,)  <br>  <br>Score of base estimator with best alpha, or, if  <br>\`\`alpha\_per\_target=True\`\`, a score for each target.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=best_score_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | \-0.00243 |\
| [coef\_ coef\_: ndarray of shape (n\_features) or (n\_targets, n\_features)  <br>  <br>Weight vector(s).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=coef_,-ndarray%20of%20shape%20%28n_features%29%20or%20%28n_targets%2C%20n_features%29) | ndarray\[float64\](300,) | \[ 4.39, 1.21,-0.28,...,-0.86, 1.09, 6.02\] |\
| [intercept\_ intercept\_: float or ndarray of shape (n\_targets,)  <br>  <br>Independent term in decision function. Set to 0.0 if  <br>\`\`fit\_intercept = False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=intercept_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | 1.956 |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=n_features_in_,-int) | int | 300 |\
\
  \
  \
\
We observe that this model can almost rival the performance of the gradient boosted trees with an average error around 5% of the maximum demand.\
\
Note that while the final step of this pipeline is a linear regression model, the intermediate steps such as the spline feature extraction and the Nyström kernel approximation are highly non-linear. As a result the compound pipeline is much more expressive than a simple linear regression model with raw features.\
\
For the sake of completeness, we also evaluate the combination of one-hot encoding and kernel approximation:\
\
one\_hot\_poly\_pipeline \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
    [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")\
(\
        transformers\=\[\
            ("categorical", one\_hot\_encoder, categorical\_columns),\
            ("one\_hot\_time", one\_hot\_encoder, \["hour", "weekday", "month"\]),\
        \],\
        remainder\="passthrough",\
        verbose\_feature\_names\_out\=False,\
    ),\
    [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")\
(kernel\="poly", degree\=2, n\_components\=300, random\_state\=0),\
    [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")\
(alphas\=alphas),\
).set\_output(transform\="pandas")\
evaluate(one\_hot\_poly\_pipeline, X, y, cv\=ts\_cv)\
\
Copy to clipboard\
\
Mean Absolute Error:     0.082 +/- 0.006\
Root Mean Squared Error: 0.111 +/- 0.011\
\
Copy to clipboard\
\
Pipeline(steps=\[('columntransformer',\
                 ColumnTransformer(remainder='passthrough',\
                                   transformers=\[('categorical',\
                                                  OneHotEncoder(handle\_unknown='ignore',\
                                                                sparse\_output=False),\
                                                  Index(\['season', 'holiday', 'workingday', 'weather'\], dtype='str')),\
                                                 ('one\_hot\_time',\
                                                  OneHotEncoder(handle\_unknown='ignore',\
                                                                sparse\_output=False),\
                                                  \['hour', 'weekday',\
                                                   'month'\])\],\
                                   verbose\_feature...\
                 RidgeCV(alphas=array(\[1.00000000e-06, 3.16227766e-06, 1.00000000e-05, 3.16227766e-05,\
       1.00000000e-04, 3.16227766e-04, 1.00000000e-03, 3.16227766e-03,\
       1.00000000e-02, 3.16227766e-02, 1.00000000e-01, 3.16227766e-01,\
       1.00000000e+00, 3.16227766e+00, 1.00000000e+01, 3.16227766e+01,\
       1.00000000e+02, 3.16227766e+02, 1.00000000e+03, 3.16227766e+03,\
       1.00000000e+04, 3.16227766e+04, 1.00000000e+05, 3.16227766e+05,\
       1.00000000e+06\])))\])\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
Pipeline\
\
[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)\
iFitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('columntransformer', ...), ('nystroem', ...), ...\] |\
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |\
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 12  |\
\
columntransformer: ColumnTransformer\
\
[?Documentation for columntransformer: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('categorical', ...), ('one\_hot\_time', ...)\] |\
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | 'passthrough' |\
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | False |\
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](12,) | \['season','year','month',...,'feel\_temp','humidity','windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 12  |\
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'categorical...'one-to-one')} |\
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'ca...al': slice(0, 11, None), 'on...me': slice(11, 54, None), 're...er': slice(54, 59, None)} |\
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |\
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('ca...al', OneHotEncoder...\_output=False), Index(\['seaso..., dtype='str')), ('on...me', OneHotEncoder...\_output=False), \['hour', 'weekday', 'month'\]), ('re...er', FunctionTrans...='one-to-one'), \['year', 'temp', 'fe...mp', 'hu...ty', ...\])\] |\
\
categorical\
\
Index(\['season', 'holiday', 'workingday', 'weather'\], dtype='str')\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | False |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\['fall'... dtype=object), array(\['False... dtype=object), array(\['False... dtype=object), array(\['clear... dtype=object)\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](4,) | \['season','holiday','workingday','weather'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 4   |\
\
11 features\
\
|     |\
| --- |\
| season\_fall |\
| season\_spring |\
| season\_summer |\
| season\_winter |\
| holiday\_False |\
| holiday\_True |\
| workingday\_False |\
| workingday\_True |\
| weather\_clear |\
| weather\_misty |\
| weather\_rain |\
\
one\_hot\_time\
\
\['hour', 'weekday', 'month'\]\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | False |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\[ 0, 1..., 21, 22, 23\]), array(\[0, 1, 2, 3, 4, 5, 6\]), array(\[ 1, 2..., 10, 11, 12\])\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](3,) | \['hour','weekday','month'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 3   |\
\
43 features\
\
|     |\
| --- |\
| hour\_0 |\
| hour\_1 |\
| hour\_2 |\
| hour\_3 |\
| hour\_4 |\
| hour\_5 |\
| hour\_6 |\
| hour\_7 |\
| hour\_8 |\
| hour\_9 |\
| hour\_10 |\
| hour\_11 |\
| hour\_12 |\
| hour\_13 |\
| hour\_14 |\
| hour\_15 |\
| hour\_16 |\
| hour\_17 |\
| hour\_18 |\
| hour\_19 |\
| hour\_20 |\
| hour\_21 |\
| hour\_22 |\
| hour\_23 |\
| weekday\_0 |\
| weekday\_1 |\
| weekday\_2 |\
| weekday\_3 |\
| weekday\_4 |\
| weekday\_5 |\
| weekday\_6 |\
| month\_1 |\
| month\_2 |\
| month\_3 |\
| month\_4 |\
| month\_5 |\
| month\_6 |\
| month\_7 |\
| month\_8 |\
| month\_9 |\
| month\_10 |\
| month\_11 |\
| month\_12 |\
\
remainder\
\
\['year', 'temp', 'feel\_temp', 'humidity', 'windspeed'\]\
\
passthrough\
\
[?Documentation for FunctionTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html)\
\
5 features\
\
|     |\
| --- |\
| year |\
| temp |\
| feel\_temp |\
| humidity |\
| windspeed |\
\
59 features\
\
|     |\
| --- |\
| season\_fall |\
| season\_spring |\
| season\_summer |\
| season\_winter |\
| holiday\_False |\
| holiday\_True |\
| workingday\_False |\
| workingday\_True |\
| weather\_clear |\
| weather\_misty |\
| weather\_rain |\
| hour\_0 |\
| hour\_1 |\
| hour\_2 |\
| hour\_3 |\
| hour\_4 |\
| hour\_5 |\
| hour\_6 |\
| hour\_7 |\
| hour\_8 |\
| hour\_9 |\
| hour\_10 |\
| hour\_11 |\
| hour\_12 |\
| hour\_13 |\
| hour\_14 |\
| hour\_15 |\
| hour\_16 |\
| hour\_17 |\
| hour\_18 |\
| hour\_19 |\
| hour\_20 |\
| hour\_21 |\
| hour\_22 |\
| hour\_23 |\
| weekday\_0 |\
| weekday\_1 |\
| weekday\_2 |\
| weekday\_3 |\
| weekday\_4 |\
| weekday\_5 |\
| weekday\_6 |\
| month\_1 |\
| month\_2 |\
| month\_3 |\
| month\_4 |\
| month\_5 |\
| month\_6 |\
| month\_7 |\
| month\_8 |\
| month\_9 |\
| month\_10 |\
| month\_11 |\
| month\_12 |\
| year |\
| temp |\
| feel\_temp |\
| humidity |\
| windspeed |\
\
Nystroem\
\
[?Documentation for Nystroem](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [kernel kernel: str or callable, default='rbf'  <br>  <br>Kernel map to be approximated. A callable should accept two arguments  <br>and the keyword arguments passed to this object as \`kernel\_params\`, and  <br>should return a floating point number.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=kernel,-str%20or%20callable%2C%20default%3D%27rbf%27) | 'poly' |\
|     | [degree degree: float, default=None  <br>  <br>Degree of the polynomial kernel. Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=degree,-float%2C%20default%3DNone) | 2   |\
|     | [n\_components n\_components: int, default=100  <br>  <br>Number of features to construct.  <br>How many data points will be used to construct the mapping.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=n_components,-int%2C%20default%3D100) | 300 |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo-random number generator to control the uniform sampling without  <br>replacement of \`n\_components\` of the training data to construct the  <br>basis kernel.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |\
|     | [gamma gamma: float, default=None  <br>  <br>Gamma parameter for the RBF, laplacian, polynomial, exponential chi2  <br>and sigmoid kernels. Interpretation of the default value is left to  <br>the kernel; see the documentation for sklearn.metrics.pairwise.  <br>Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=gamma,-float%2C%20default%3DNone) | None |\
|     | [coef0 coef0: float, default=None  <br>  <br>Zero coefficient for polynomial and sigmoid kernels.  <br>Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=coef0,-float%2C%20default%3DNone) | None |\
|     | [kernel\_params kernel\_params: dict, default=None  <br>  <br>Additional parameters (keyword arguments) for kernel function passed  <br>as callable object.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=kernel_params,-dict%2C%20default%3DNone) | None |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to use for the computation. This works by breaking  <br>down the kernel matrix into \`n\_jobs\` even slices and computing them in  <br>parallel.  <br>  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [component\_indices\_ component\_indices\_: ndarray of shape (n\_components)  <br>  <br>Indices of \`\`components\_\`\` in the training set.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=component_indices_,-ndarray%20of%20shape%20%28n_components%29) | ndarray\[int64\](300,) | \[9394, 898,2398,...,2685,5725,8051\] |\
| [components\_ components\_: ndarray of shape (n\_components, n\_features)  <br>  <br>Subset of training points used to construct the feature map.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=components_,-ndarray%20of%20shape%20%28n_components%2C%20n_features%29) | ndarray\[float64\](300, 59) | \[\[ 0. , 0. , 1. ,...,30.3 , 0.69,19. \], \[ 0. , 0. , 1. ,...,25.76, 0.88,11. \], \[ 1. , 0. , 0. ,...,37.12, 0.75,17. \], ..., \[ 1. , 0. , 0. ,...,32.58, 0.7 , 6. \], \[ 0. , 0. , 0. ,...,21.97, 1. , 0. \], \[ 0. , 1. , 0. ,...,31.82, 0.37, 7. \]\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](59,) | \['season\_fall','season\_spring','season\_summer',...,'feel\_temp','humidity', 'windspeed'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=n_features_in_,-int) | int | 59  |\
| [normalization\_ normalization\_: ndarray of shape (n\_components, n\_components)  <br>  <br>Normalization matrix needed for embedding.  <br>Square root of the kernel matrix on \`\`components\_\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=normalization_,-ndarray%20of%20shape%20%28n_components%2C%20n_components%29) | ndarray\[float64\](300, 300) | \[\[14.11,-0.59, 0.34,..., 0.2 ,-0.49,-0.07\], \[-0.59,11.24, 0.12,...,-0.03, 0.18,-0.09\], \[ 0.34, 0.12,11.45,...,-0.43,-0.15, 0.04\], ..., \[ 0.2 ,-0.03,-0.43,...,11.77,-0.74, 0.35\], \[-0.49, 0.18,-0.15,...,-0.74,10.65, 0.24\], \[-0.07,-0.09, 0.04,..., 0.35, 0.24, 8.52\]\] |\
\
100 of 300 features\
\
|     |\
| --- |\
| nystroem0 |\
| nystroem1 |\
| nystroem2 |\
| nystroem3 |\
| nystroem4 |\
| nystroem5 |\
| nystroem6 |\
| nystroem7 |\
| nystroem8 |\
| nystroem9 |\
| nystroem10 |\
| nystroem11 |\
| nystroem12 |\
| nystroem13 |\
| nystroem14 |\
| nystroem15 |\
| nystroem16 |\
| nystroem17 |\
| nystroem18 |\
| nystroem19 |\
| nystroem20 |\
| nystroem21 |\
| nystroem22 |\
| nystroem23 |\
| nystroem24 |\
| nystroem25 |\
| nystroem26 |\
| nystroem27 |\
| nystroem28 |\
| nystroem29 |\
| nystroem30 |\
| nystroem31 |\
| nystroem32 |\
| nystroem33 |\
| nystroem34 |\
| nystroem35 |\
| nystroem36 |\
| nystroem37 |\
| nystroem38 |\
| nystroem39 |\
| nystroem40 |\
| nystroem41 |\
| nystroem42 |\
| nystroem43 |\
| nystroem44 |\
| nystroem45 |\
| nystroem46 |\
| nystroem47 |\
| nystroem48 |\
| nystroem49 |\
| nystroem50 |\
| nystroem51 |\
| nystroem52 |\
| nystroem53 |\
| nystroem54 |\
| nystroem55 |\
| nystroem56 |\
| nystroem57 |\
| nystroem58 |\
| nystroem59 |\
| nystroem60 |\
| nystroem61 |\
| nystroem62 |\
| nystroem63 |\
| nystroem64 |\
| nystroem65 |\
| nystroem66 |\
| nystroem67 |\
| nystroem68 |\
| nystroem69 |\
| nystroem70 |\
| nystroem71 |\
| nystroem72 |\
| nystroem73 |\
| nystroem74 |\
| nystroem75 |\
| nystroem76 |\
| nystroem77 |\
| nystroem78 |\
| nystroem79 |\
| nystroem80 |\
| nystroem81 |\
| nystroem82 |\
| nystroem83 |\
| nystroem84 |\
| nystroem85 |\
| nystroem86 |\
| nystroem87 |\
| nystroem88 |\
| nystroem89 |\
| nystroem90 |\
| nystroem91 |\
| nystroem92 |\
| nystroem93 |\
| nystroem94 |\
| nystroem95 |\
| nystroem96 |\
| nystroem97 |\
| nystroem98 |\
| nystroem99 |\
\
RidgeCV\
\
[?Documentation for RidgeCV](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [alphas alphas: array-like of shape (n\_alphas,), default=(0.1, 1.0, 10.0)  <br>  <br>Array of alpha values to try.  <br>Regularization strength; must be a positive float. Regularization  <br>improves the conditioning of the problem and reduces the variance of  <br>the estimates. Larger values specify stronger regularization.  <br>Alpha corresponds to \`\`1 / (2C)\`\` in other linear models such as  <br>:class:\`~sklearn.linear\_model.LogisticRegression\` or  <br>:class:\`~sklearn.svm.LinearSVC\`.  <br>If using Leave-One-Out cross-validation, alphas must be strictly positive.  <br>  <br>For an example on how regularization strength affects the model coefficients,  <br>see :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_ridge\_coeffs.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alphas,-array-like%20of%20shape%20%28n_alphas%2C%29%2C%20default%3D%280.1%2C%201.0%2C%2010.0%29) | array(\[1.0000...00000000e+06\]) |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to calculate the intercept for this model. If set  <br>to false, no intercept will be used in calculations  <br>(i.e. data is expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [scoring scoring: str, callable, default=None  <br>  <br>The scoring method to use for cross-validation. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: negative :ref:\`mean squared error <mean\_squared\_error>\` if cv is  <br>None (i.e. when using leave-one-out cross-validation), or  <br>:ref:\`coefficient of determination <r2\_score>\` (:math:\`R^2\`) otherwise.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=scoring,-str%2C%20callable%2C%20default%3DNone) | None |\
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the efficient Leave-One-Out cross-validation  <br>\- integer, to specify the number of folds,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if \`\`y\`\` is binary or multiclass,  <br>:class:\`~sklearn.model\_selection.StratifiedKFold\` is used, else,  <br>:class:\`~sklearn.model\_selection.KFold\` is used.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |\
|     | [gcv\_mode gcv\_mode: {'auto', 'svd', 'eigen'}, default='auto'  <br>  <br>Flag indicating which strategy to use when performing  <br>Leave-One-Out Cross-Validation. Options are::  <br>  <br>'auto' : same as 'eigen'  <br>'svd' : use singular value decomposition of X when X is dense,  <br>fallback to 'eigen' when X is sparse  <br>'eigen' : use eigendecomposition of X X' when n\_samples <= n\_features  <br>or X' X when n\_features < n\_samples  <br>  <br>The 'auto' mode is the default and is intended to pick the cheaper  <br>option depending on the shape and sparsity of the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=gcv_mode,-%7B%27auto%27%2C%20%27svd%27%2C%20%27eigen%27%7D%2C%20default%3D%27auto%27) | None |\
|     | [store\_cv\_results store\_cv\_results: bool, default=False  <br>  <br>Flag indicating if the cross-validation values corresponding to  <br>each alpha should be stored in the \`\`cv\_results\_\`\` attribute (see  <br>below). This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionchanged:: 1.5  <br>Parameter name changed from \`store\_cv\_values\` to \`store\_cv\_results\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=store_cv_results,-bool%2C%20default%3DFalse) | False |\
|     | [alpha\_per\_target alpha\_per\_target: bool, default=False  <br>  <br>Flag indicating whether to optimize the alpha value (picked from the  <br>\`alphas\` parameter list) for each target separately (for multi-output  <br>settings: multiple prediction targets). When set to \`True\`, after  <br>fitting, the \`alpha\_\` attribute will contain a value for each target.  <br>When set to \`False\`, a single alpha is used for all targets.  <br>This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_per_target,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [alpha\_ alpha\_: float or ndarray of shape (n\_targets,)  <br>  <br>Estimated regularization parameter, or, if \`\`alpha\_per\_target=True\`\`,  <br>the estimated regularization parameter for each target.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float | 0.003162 |\
| [best\_score\_ best\_score\_: float or ndarray of shape (n\_targets,)  <br>  <br>Score of base estimator with best alpha, or, if  <br>\`\`alpha\_per\_target=True\`\`, a score for each target.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=best_score_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | \-0.004476 |\
| [coef\_ coef\_: ndarray of shape (n\_features) or (n\_targets, n\_features)  <br>  <br>Weight vector(s).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=coef_,-ndarray%20of%20shape%20%28n_features%29%20or%20%28n_targets%2C%20n_features%29) | ndarray\[float64\](300,) | \[ 0.95,-1.18, 0.44,..., 0.24,-0.49, 3.13\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](300,) | \['nystroem0','nystroem1','nystroem2',...,'nystroem297','nystroem298', 'nystroem299'\] |\
| [intercept\_ intercept\_: float or ndarray of shape (n\_targets,)  <br>  <br>Independent term in decision function. Set to 0.0 if  <br>\`\`fit\_intercept = False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=intercept_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | 0.63 |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=n_features_in_,-int) | int | 300 |\
\
  \
  \
\
While one-hot encoded features were competitive with spline-based features when using linear models, this is no longer the case when using a low-rank approximation of a non-linear kernel: this can be explained by the fact that spline features are smoother and allow the kernel approximation to find a more expressive decision function.\
\
Let us now have a qualitative look at the predictions of the kernel models and of the gradient boosted trees that should be able to better model non-linear interactions between features:\
\
gbrt.fit(X.iloc\[train\_0\], y.iloc\[train\_0\])\
gbrt\_predictions \= gbrt.predict(X.iloc\[test\_0\])\
\
one\_hot\_poly\_pipeline.fit(X.iloc\[train\_0\], y.iloc\[train\_0\])\
one\_hot\_poly\_predictions \= one\_hot\_poly\_pipeline.predict(X.iloc\[test\_0\])\
\
cyclic\_spline\_poly\_pipeline.fit(X.iloc\[train\_0\], y.iloc\[train\_0\])\
cyclic\_spline\_poly\_predictions \= cyclic\_spline\_poly\_pipeline.predict(X.iloc\[test\_0\])\
\
Copy to clipboard\
\
Again we zoom on the last 4 days of the test set:\
\
last\_hours \= slice(\-96, None)\
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(12, 4))\
fig.suptitle("Predictions by non-linear regression models")\
ax.plot(\
    y.iloc\[test\_0\].values\[last\_hours\],\
    "x-",\
    alpha\=0.2,\
    label\="Actual demand",\
    color\="black",\
)\
ax.plot(\
    gbrt\_predictions\[last\_hours\],\
    "x-",\
    label\="Gradient Boosted Trees",\
)\
ax.plot(\
    one\_hot\_poly\_predictions\[last\_hours\],\
    "x-",\
    label\="One-hot + polynomial kernel",\
)\
ax.plot(\
    cyclic\_spline\_poly\_predictions\[last\_hours\],\
    "x-",\
    label\="Splines + polynomial kernel",\
)\
\_ \= ax.legend()\
\
Copy to clipboard\
\
![Predictions by non-linear regression models](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_007.png)\
\
First, note that trees can naturally model non-linear feature interactions since, by default, decision trees are allowed to grow beyond a depth of 2 levels.\
\
Here, we can observe that the combinations of spline features and non-linear kernels works quite well and can almost rival the accuracy of the gradient boosting regression trees.\
\
On the contrary, one-hot encoded time features do not perform that well with the low rank kernel model. In particular, they significantly over-estimate the low demand hours more than the competing models.\
\
We also observe that none of the models can successfully predict some of the peak rentals at the rush hours during the working days. It is possible that access to additional features would be required to further improve the accuracy of the predictions. For instance, it could be useful to have access to the geographical repartition of the fleet at any point in time or the fraction of bikes that are immobilized because they need servicing.\
\
Let us finally get a more quantitative look at the prediction errors of those three models using the true vs predicted demand scatter plots:\
\
from sklearn.metrics import PredictionErrorDisplay\
\
fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(nrows\=2, ncols\=3, figsize\=(13, 7), sharex\=True, sharey\="row")\
fig.suptitle("Non-linear regression models", y\=1.0)\
predictions \= \[\
    one\_hot\_poly\_predictions,\
    cyclic\_spline\_poly\_predictions,\
    gbrt\_predictions,\
\]\
labels \= \[\
    "One hot +\\npolynomial kernel",\
    "Splines +\\npolynomial kernel",\
    "Gradient Boosted\\nTrees",\
\]\
plot\_kinds \= \["actual\_vs\_predicted", "residual\_vs\_predicted"\]\
for axis\_idx, kind in enumerate(plot\_kinds):\
    for ax, pred, label in zip(axes\[axis\_idx\], predictions, labels):\
        disp \= [PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")\
(\
            y\_true\=y.iloc\[test\_0\],\
            y\_pred\=pred,\
            kind\=kind,\
            scatter\_kwargs\={"alpha": 0.3},\
            ax\=ax,\
        )\
        ax.set\_xticks([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
(0, 1, num\=5))\
        if axis\_idx \== 0:\
            ax.set\_yticks([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
(0, 1, num\=5))\
            ax.legend(\
                \["Best model", label\],\
                loc\="upper center",\
                bbox\_to\_anchor\=(0.5, 1.3),\
                ncol\=2,\
            )\
        ax.set\_aspect("equal", adjustable\="box")\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
Copy to clipboard\
\
![Non-linear regression models](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_008.png)\
\
This visualization confirms the conclusions we draw on the previous plot.\
\
All models under-estimate the high demand events (working day rush hours), but gradient boosting a bit less so. The low demand events are well predicted on average by gradient boosting while the one-hot polynomial regression pipeline seems to systematically over-estimate demand in that regime. Overall the predictions of the gradient boosted trees are closer to the diagonal than for the kernel models.\
\
Concluding remarks[#](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#concluding-remarks "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
We note that we could have obtained slightly better results for kernel models by using more components (higher rank kernel approximation) at the cost of longer fit and prediction durations. For large values of `n_components`, the performance of the one-hot encoded features would even match the spline features.\
\
The `Nystroem` + `RidgeCV` regressor could also have been replaced by [`MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")\
 with one or two hidden layers and we would have obtained quite similar results.\
\
The dataset we used in this case study is sampled on an hourly basis. However cyclic spline-based features could model time-within-day or time-within-week very efficiently with finer-grained time resolutions (for instance with measurements taken every minute instead of every hour) without introducing more features. One-hot encoding time representations would not offer this flexibility.\
\
Finally, in this notebook we used `RidgeCV` because it is very efficient from a computational point of view. However, it models the target variable as a Gaussian random variable with constant variance. For positive regression problems, it is likely that using a Poisson or Gamma distribution would make more sense. This could be achieved by using `GridSearchCV(TweedieRegressor(power=2), param_grid({"alpha": alphas}))` instead of `RidgeCV`.\
\
**Total running time of the script:** (0 minutes 15.844 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_cyclical_feature_engineering.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_cyclical_feature_engineering.ipynb)\
\
[`Download Jupyter notebook: plot_cyclical_feature_engineering.ipynb`](https://scikit-learn.org/stable/_downloads/7012baed63b9a27f121bae611b8285c2/plot_cyclical_feature_engineering.ipynb)\
\
[`Download Python source code: plot_cyclical_feature_engineering.py`](https://scikit-learn.org/stable/_downloads/9fcbbc59ab27a20d07e209a711ac4f50/plot_cyclical_feature_engineering.py)\
\
[`Download zipped: plot_cyclical_feature_engineering.zip`](https://scikit-learn.org/stable/_downloads/ed9632132a75f297eac3f60b74cd47aa/plot_cyclical_feature_engineering.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_time_series_lagged_features_thumb.png)\
\
[Lagged features for time series forecasting](https://scikit-learn.org/stable/auto_examples/applications/plot_time_series_lagged_features.html)\
\
Lagged features for time series forecasting\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_categorical_thumb.png)\
\
[Categorical Feature Support in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_categorical.html)\
\
Categorical Feature Support in Gradient Boosting\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_polynomial_interpolation_thumb.png)\
\
[Polynomial and Spline interpolation](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html)\
\
Polynomial and Spline interpolation\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_target_encoder_thumb.png)\
\
[Comparing Target Encoder with Other Encoders](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html)\
\
Comparing Target Encoder with Other Encoders\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/9fcbbc59ab27a20d07e209a711ac4f50/plot_cyclical_feature_engineering.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/7012baed63b9a27f121bae611b8285c2/plot_cyclical_feature_engineering.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/ed9632132a75f297eac3f60b74cd47aa/plot_cyclical_feature_engineering.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_cyclical_feature_engineering.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_cyclical_feature_engineering.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)