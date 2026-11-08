[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html#sphx-glr-download-auto-examples-linear-model-plot-tweedie-regression-insurance-claims-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Tweedie regression on insurance claims[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html#tweedie-regression-on-insurance-claims "Link to this heading")

==================================================================================================================================================================================================================

This example illustrates the use of Poisson, Gamma and Tweedie regression on the [French Motor Third-Party Liability Claims dataset](https://www.openml.org/d/41214)
, and is inspired by an R tutorial [\[1\]](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html#id2)
.

In this dataset, each sample corresponds to an insurance policy, i.e. a contract within an insurance company and an individual (policyholder). Available features include driver age, vehicle age, vehicle power, etc.

A few definitions: a _claim_ is the request made by a policyholder to the insurer to compensate for a loss covered by the insurance. The _claim amount_ is the amount of money that the insurer must pay. The _exposure_ is the duration of the insurance coverage of a given policy, in years.

Here our goal is to predict the expected value, i.e. the mean, of the total claim amount per exposure unit also referred to as the pure premium.

There are several possibilities to do that, two of which are:

1.  Model the number of claims with a Poisson distribution, and the average claim amount per claim, also known as severity, as a Gamma distribution and multiply the predictions of both in order to get the total claim amount.
    
2.  Model the total claim amount per exposure directly, typically with a Tweedie distribution of Tweedie power p∈(1,2).
    

In this example we will illustrate both approaches. We start by defining a few helper functions for loading the data and visualizing results.

from functools import [partial](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
from sklearn.metrics import (
    [mean\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
,
    [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
,
    [mean\_tweedie\_deviance](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html#sklearn.metrics.mean_tweedie_deviance "sklearn.metrics.mean_tweedie_deviance")
,
)

def load\_mtpl2(n\_samples\=None):
    """Fetch the French Motor Third-Party Liability Claims dataset.

    Parameters
    ----------
    n\_samples: int, default=None
      number of samples to select (for faster run time). Full dataset has
      678013 samples.
    """
    \# freMTPL2freq dataset from https://www.openml.org/d/41214
    df\_freq \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(data\_id\=41214, as\_frame\=True).data
    df\_freq\["IDpol"\] \= df\_freq\["IDpol"\].astype(int)
    df\_freq.set\_index("IDpol", inplace\=True)

    \# freMTPL2sev dataset from https://www.openml.org/d/41215
    df\_sev \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(data\_id\=41215, as\_frame\=True).data

    \# sum ClaimAmount over identical IDs
    df\_sev \= df\_sev.groupby("IDpol").sum()

    df \= df\_freq.join(df\_sev, how\="left")
    df\["ClaimAmount"\] \= df\["ClaimAmount"\].fillna(0)

    \# unquote string fields
    for column\_name in df.columns\[\[t is object for t in df.dtypes.values\]\]:
        df\[column\_name\] \= df\[column\_name\].str.strip("'")
    return df.iloc\[:n\_samples\]

def plot\_obs\_pred(
    df,
    feature,
    weight,
    observed,
    predicted,
    y\_label\=None,
    title\=None,
    ax\=None,
    fill\_legend\=False,
):
    """Plot observed and predicted - aggregated per feature level.

    Parameters
    ----------
    df : DataFrame
        input data
    feature: str
        a column name of df for the feature to be plotted
    weight : str
        column name of df with the values of weights or exposure
    observed : str
        a column name of df with the observed target
    predicted : DataFrame
        a dataframe, with the same index as df, with the predicted target
    fill\_legend : bool, default=False
        whether to show fill\_between legend
    """
    \# aggregate observed and predicted variables by feature level
    df\_ \= df.loc\[:, \[feature, weight\]\].copy()
    df\_\["observed"\] \= df\[observed\] \* df\[weight\]
    df\_\["predicted"\] \= predicted \* df\[weight\]
    df\_ \= (
        df\_.groupby(\[feature\])\[\[weight, "observed", "predicted"\]\]
        .sum()
        .assign(observed\=lambda x: x\["observed"\] / x\[weight\])
        .assign(predicted\=lambda x: x\["predicted"\] / x\[weight\])
    )

    ax \= df\_.loc\[:, \["observed", "predicted"\]\].plot(style\=".", ax\=ax)
    y\_max \= df\_.loc\[:, \["observed", "predicted"\]\].values.max() \* 0.8
    p2 \= ax.fill\_between(
        df\_.index,
        0,
        y\_max \* df\_\[weight\] / df\_\[weight\].values.max(),
        color\="g",
        alpha\=0.1,
    )
    if fill\_legend:
        ax.legend(\[p2\], \["{} distribution".format(feature)\])
    ax.set(
        ylabel\=y\_label if y\_label is not None else None,
        title\=title if title is not None else "Train: Observed vs Predicted",
    )

def score\_estimator(
    estimator,
    X\_train,
    X\_test,
    df\_train,
    df\_test,
    target,
    weights,
    tweedie\_powers\=None,
):
    """Evaluate an estimator on train and test sets with different metrics"""

    metrics \= \[\
        ("D² explained", None),  \# Use default scorer if it exists\
        ("mean abs. error", [mean\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")\
),\
        ("mean squared error", [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")\
),\
    \]
    if tweedie\_powers:
        metrics += \[\
            (\
                "mean Tweedie dev p={:.4f}".format(power),\
                [partial](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")\
([mean\_tweedie\_deviance](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html#sklearn.metrics.mean_tweedie_deviance "sklearn.metrics.mean_tweedie_deviance")\
, power\=power),\
            )\
            for power in tweedie\_powers\
        \]

    res \= \[\]
    for subset\_label, X, df in \[\
        ("train", X\_train, df\_train),\
        ("test", X\_test, df\_test),\
    \]:
        y, \_weights \= df\[target\], df\[weights\]
        for score\_label, metric in metrics:
            if isinstance(estimator, tuple) and len(estimator) \== 2:
                \# Score the model consisting of the product of frequency and
                \# severity models.
                est\_freq, est\_sev \= estimator
                y\_pred \= est\_freq.predict(X) \* est\_sev.predict(X)
            else:
                y\_pred \= estimator.predict(X)

            if metric is None:
                if not hasattr(estimator, "score"):
                    continue
                score \= estimator.score(X, y, sample\_weight\=\_weights)
            else:
                score \= metric(y, y\_pred, sample\_weight\=\_weights)

            res.append({"subset": subset\_label, "metric": score\_label, "score": score})

    res \= (
        [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(res)
        .set\_index(\["metric", "subset"\])
        .score.unstack(\-1)
        .round(4)
        .loc\[:, \["train", "test"\]\]
    )
    return res

Copy to clipboard

Loading datasets, basic feature extraction and target definitions[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html#loading-datasets-basic-feature-extraction-and-target-definitions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We construct the freMTPL2 dataset by joining the freMTPL2freq table, containing the number of claims (`ClaimNb`), with the freMTPL2sev table, containing the claim amount (`ClaimAmount`) for the same policy ids (`IDpol`).

from sklearn.compose import [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import (
    [FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
,
    [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
,
    [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
,
    [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
,
)

df \= load\_mtpl2()

\# Correct for unreasonable observations (that might be data error)
\# and a few exceptionally large claim amounts
df\["ClaimNb"\] \= df\["ClaimNb"\].clip(upper\=4)
df\["Exposure"\] \= df\["Exposure"\].clip(upper\=1)
df\["ClaimAmount"\] \= df\["ClaimAmount"\].clip(upper\=200000)
\# If the claim amount is 0, then we do not count it as a claim. The loss function
\# used by the severity model needs strictly positive claim amounts. This way
\# frequency and severity are more consistent with each other.
df.loc\[(df\["ClaimAmount"\] \== 0) & (df\["ClaimNb"\] \>= 1), "ClaimNb"\] \= 0

log\_scale\_transformer \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    [FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
(func\=[np.log](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")
), [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
()
)

column\_trans \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
    \[\
        (\
            "binned\_numeric",\
            [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")\
(\
                n\_bins\=10, quantile\_method\="averaged\_inverted\_cdf", random\_state\=0\
            ),\
            \["VehAge", "DrivAge"\],\
        ),\
        (\
            "onehot\_categorical",\
            [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(),\
            \["VehBrand", "VehPower", "VehGas", "Region", "Area"\],\
        ),\
        ("passthrough\_numeric", "passthrough", \["BonusMalus"\]),\
        ("log\_scaled\_numeric", log\_scale\_transformer, \["Density"\]),\
    \],
    remainder\="drop",
)
X \= column\_trans.fit\_transform(df)

\# Insurances companies are interested in modeling the Pure Premium, that is
\# the expected total claim amount per unit of exposure for each policyholder
\# in their portfolio:
df\["PurePremium"\] \= df\["ClaimAmount"\] / df\["Exposure"\]

\# This can be indirectly approximated by a 2-step modeling: the product of the
\# Frequency times the average claim amount per claim:
df\["Frequency"\] \= df\["ClaimNb"\] / df\["Exposure"\]
df\["AvgClaimAmount"\] \= df\["ClaimAmount"\] / [np.fmax](https://numpy.org/doc/stable/reference/generated/numpy.fmax.html#numpy.fmax "numpy.fmax")
(df\["ClaimNb"\], 1)

with [pd.option\_context](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.option_context.html#pandas.option_context "pandas.option_context")
("display.max\_columns", 15):
    print(df\[df.ClaimAmount \> 0\].head())

Copy to clipboard

       ClaimNb  Exposure Area  VehPower  VehAge  DrivAge  BonusMalus VehBrand  \\
IDpol
139          1      0.75    F         7       1       61          50      B12
190          1      0.14    B        12       5       50          60      B12
414          1      0.14    E         4       0       36          85      B12
424          2      0.62    F        10       0       51         100      B12
463          1      0.31    A         5       0       45          50      B12

          VehGas  Density Region  ClaimAmount   PurePremium  Frequency  \\
IDpol
139    'Regular'    27000    R11       303.00    404.000000   1.333333
190     'Diesel'       56    R25      1981.84  14156.000000   7.142857
414    'Regular'     4792    R11      1456.55  10403.928571   7.142857
424    'Regular'    27000    R11     10834.00  17474.193548   3.225806
463    'Regular'       12    R73      3986.67  12860.225806   3.225806

       AvgClaimAmount
IDpol
139            303.00
190           1981.84
414           1456.55
424           5417.00
463           3986.67

Copy to clipboard

Frequency model – Poisson distribution[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html#frequency-model-poisson-distribution "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The number of claims (`ClaimNb`) is a positive integer (0 included). Thus, this target can be modelled by a Poisson distribution. It is then assumed to be the number of discrete events occurring with a constant rate in a given time interval (`Exposure`, in units of years). Here we model the frequency `y = ClaimNb / Exposure`, which is still a (scaled) Poisson distribution, and use `Exposure` as `sample_weight`.

from sklearn.linear\_model import [PoissonRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

df\_train, df\_test, X\_train, X\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(df, X, random\_state\=0)

Copy to clipboard

Let us keep in mind that despite the seemingly large number of data points in this dataset, the number of evaluation points where the claim amount is non-zero is quite small:

len(df\_test)

Copy to clipboard

169504

Copy to clipboard

len(df\_test\[df\_test\["ClaimAmount"\] \> 0\])

Copy to clipboard

6237

Copy to clipboard

As a consequence, we expect a significant variability in our evaluation upon random resampling of the train test split.

The parameters of the model are estimated by minimizing the Poisson deviance on the training set via a Newton solver. Some of the features are collinear (e.g. because we did not drop any categorical level in the `OneHotEncoder`), we use a weak L2 penalization to avoid numerical issues.

glm\_freq \= [PoissonRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")
(alpha\=1e-4, solver\="newton-cholesky")
glm\_freq.fit(X\_train, df\_train\["Frequency"\], sample\_weight\=df\_train\["Exposure"\])

scores \= score\_estimator(
    glm\_freq,
    X\_train,
    X\_test,
    df\_train,
    df\_test,
    target\="Frequency",
    weights\="Exposure",
)
print("Evaluation of PoissonRegressor on target Frequency")
print(scores)

Copy to clipboard

Evaluation of PoissonRegressor on target Frequency
subset               train    test
metric
D² explained        0.0448  0.0427
mean abs. error     0.1379  0.1378
mean squared error  0.2441  0.2246

Copy to clipboard

Note that the score measured on the test set is surprisingly better than on the training set. This might be specific to this random train-test split. Proper cross-validation could help us to assess the sampling variability of these results.

We can visually compare observed and predicted values, aggregated by the drivers age (`DrivAge`), vehicle age (`VehAge`) and the insurance bonus/malus (`BonusMalus`).

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, nrows\=2, figsize\=(16, 8))
fig.subplots\_adjust(hspace\=0.3, wspace\=0.2)

plot\_obs\_pred(
    df\=df\_train,
    feature\="DrivAge",
    weight\="Exposure",
    observed\="Frequency",
    predicted\=glm\_freq.predict(X\_train),
    y\_label\="Claim Frequency",
    title\="train data",
    ax\=ax\[0, 0\],
)

plot\_obs\_pred(
    df\=df\_test,
    feature\="DrivAge",
    weight\="Exposure",
    observed\="Frequency",
    predicted\=glm\_freq.predict(X\_test),
    y\_label\="Claim Frequency",
    title\="test data",
    ax\=ax\[0, 1\],
    fill\_legend\=True,
)

plot\_obs\_pred(
    df\=df\_test,
    feature\="VehAge",
    weight\="Exposure",
    observed\="Frequency",
    predicted\=glm\_freq.predict(X\_test),
    y\_label\="Claim Frequency",
    title\="test data",
    ax\=ax\[1, 0\],
    fill\_legend\=True,
)

plot\_obs\_pred(
    df\=df\_test,
    feature\="BonusMalus",
    weight\="Exposure",
    observed\="Frequency",
    predicted\=glm\_freq.predict(X\_test),
    y\_label\="Claim Frequency",
    title\="test data",
    ax\=ax\[1, 1\],
    fill\_legend\=True,
)

Copy to clipboard

![train data, test data, test data, test data](https://scikit-learn.org/stable/_images/sphx_glr_plot_tweedie_regression_insurance_claims_001.png)

According to the observed data, the frequency of accidents is higher for drivers younger than 30 years old, and is positively correlated with the `BonusMalus` variable. Our model is able to mostly correctly model this behaviour.

Severity Model - Gamma distribution[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html#severity-model-gamma-distribution "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The mean claim amount or severity (`AvgClaimAmount`) can be empirically shown to follow approximately a Gamma distribution. We fit a GLM model for the severity with the same features as the frequency model.

Note:

*   We filter out `ClaimAmount == 0` as the Gamma distribution has support on (0,∞), not \[0,∞).\
    \
*   We use `ClaimNb` as `sample_weight` to account for policies that contain more than one claim.\
    \
\
from sklearn.linear\_model import [GammaRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html#sklearn.linear_model.GammaRegressor "sklearn.linear_model.GammaRegressor")\
\
mask\_train \= df\_train\["ClaimAmount"\] \> 0\
mask\_test \= df\_test\["ClaimAmount"\] \> 0\
\
glm\_sev \= [GammaRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html#sklearn.linear_model.GammaRegressor "sklearn.linear_model.GammaRegressor")\
(alpha\=10.0, solver\="newton-cholesky")\
\
glm\_sev.fit(\
    X\_train\[mask\_train.values\],\
    df\_train.loc\[mask\_train, "AvgClaimAmount"\],\
    sample\_weight\=df\_train.loc\[mask\_train, "ClaimNb"\],\
)\
\
scores \= score\_estimator(\
    glm\_sev,\
    X\_train\[mask\_train.values\],\
    X\_test\[mask\_test.values\],\
    df\_train\[mask\_train\],\
    df\_test\[mask\_test\],\
    target\="AvgClaimAmount",\
    weights\="ClaimNb",\
)\
print("Evaluation of GammaRegressor on target AvgClaimAmount")\
print(scores)\
\
Copy to clipboard\
\
Evaluation of GammaRegressor on target AvgClaimAmount\
subset                     train          test\
metric\
D² explained        3.900000e-03  4.400000e-03\
mean abs. error     1.756752e+03  1.744055e+03\
mean squared error  5.801775e+07  5.030676e+07\
\
Copy to clipboard\
\
Those values of the metrics are not necessarily easy to interpret. It can be insightful to compare them with a model that does not use any input features and always predicts a constant value, i.e. the average claim amount, in the same setting:\
\
from sklearn.dummy import [DummyRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")\
\
dummy\_sev \= [DummyRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")\
(strategy\="mean")\
dummy\_sev.fit(\
    X\_train\[mask\_train.values\],\
    df\_train.loc\[mask\_train, "AvgClaimAmount"\],\
    sample\_weight\=df\_train.loc\[mask\_train, "ClaimNb"\],\
)\
\
scores \= score\_estimator(\
    dummy\_sev,\
    X\_train\[mask\_train.values\],\
    X\_test\[mask\_test.values\],\
    df\_train\[mask\_train\],\
    df\_test\[mask\_test\],\
    target\="AvgClaimAmount",\
    weights\="ClaimNb",\
)\
print("Evaluation of a mean predictor on target AvgClaimAmount")\
print(scores)\
\
Copy to clipboard\
\
Evaluation of a mean predictor on target AvgClaimAmount\
subset                     train          test\
metric\
D² explained        0.000000e+00 -0.000000e+00\
mean abs. error     1.756687e+03  1.744497e+03\
mean squared error  5.803882e+07  5.033764e+07\
\
Copy to clipboard\
\
We conclude that the claim amount is very challenging to predict. Still, the [`GammaRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html#sklearn.linear_model.GammaRegressor "sklearn.linear_model.GammaRegressor")\
 is able to leverage some information from the input features to slightly improve upon the mean baseline in terms of D².\
\
Note that the resulting model is the average claim amount per claim. As such, it is conditional on having at least one claim, and cannot be used to predict the average claim amount per policy. For this, it needs to be combined with a claims frequency model.\
\
print(\
    "Mean AvgClaim Amount per policy:              %.2f "\
    % df\_train\["AvgClaimAmount"\].mean()\
)\
print(\
    "Mean AvgClaim Amount | NbClaim > 0:           %.2f"\
    % df\_train\["AvgClaimAmount"\]\[df\_train\["AvgClaimAmount"\] \> 0\].mean()\
)\
print(\
    "Predicted Mean AvgClaim Amount | NbClaim > 0: %.2f"\
    % glm\_sev.predict(X\_train).mean()\
)\
print(\
    "Predicted Mean AvgClaim Amount (dummy) | NbClaim > 0: %.2f"\
    % dummy\_sev.predict(X\_train).mean()\
)\
\
Copy to clipboard\
\
Mean AvgClaim Amount per policy:              71.78\
Mean AvgClaim Amount | NbClaim > 0:           1951.21\
Predicted Mean AvgClaim Amount | NbClaim > 0: 1940.95\
Predicted Mean AvgClaim Amount (dummy) | NbClaim > 0: 1978.59\
\
Copy to clipboard\
\
We can visually compare observed and predicted values, aggregated for the drivers age (`DrivAge`).\
\
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(ncols\=1, nrows\=2, figsize\=(16, 6))\
\
plot\_obs\_pred(\
    df\=df\_train.loc\[mask\_train\],\
    feature\="DrivAge",\
    weight\="Exposure",\
    observed\="AvgClaimAmount",\
    predicted\=glm\_sev.predict(X\_train\[mask\_train.values\]),\
    y\_label\="Average Claim Severity",\
    title\="train data",\
    ax\=ax\[0\],\
)\
\
plot\_obs\_pred(\
    df\=df\_test.loc\[mask\_test\],\
    feature\="DrivAge",\
    weight\="Exposure",\
    observed\="AvgClaimAmount",\
    predicted\=glm\_sev.predict(X\_test\[mask\_test.values\]),\
    y\_label\="Average Claim Severity",\
    title\="test data",\
    ax\=ax\[1\],\
    fill\_legend\=True,\
)\
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")\
()\
\
Copy to clipboard\
\
![train data, test data](https://scikit-learn.org/stable/_images/sphx_glr_plot_tweedie_regression_insurance_claims_002.png)\
\
Overall, the drivers age (`DrivAge`) has a weak impact on the claim severity, both in observed and predicted data.\
\
Pure Premium Modeling via a Product Model vs single TweedieRegressor[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html#pure-premium-modeling-via-a-product-model-vs-single-tweedieregressor "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
As mentioned in the introduction, the total claim amount per unit of exposure can be modeled as the product of the prediction of the frequency model by the prediction of the severity model.\
\
Alternatively, one can directly model the total loss with a unique Compound Poisson Gamma generalized linear model (with a log link function). This model is a special case of the Tweedie GLM with a “power” parameter p∈(1,2). Here, we fix apriori the `power` parameter of the Tweedie model to some arbitrary value (1.9) in the valid range. Ideally one would select this value via grid-search by minimizing the negative log-likelihood of the Tweedie model, but unfortunately the current implementation does not allow for this (yet).\
\
We will compare the performance of both approaches. To quantify the performance of both models, one can compute the mean deviance of the train and test data assuming a Compound Poisson-Gamma distribution of the total claim amount. This is equivalent to a Tweedie distribution with a `power` parameter between 1 and 2.\
\
The [`sklearn.metrics.mean_tweedie_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html#sklearn.metrics.mean_tweedie_deviance "sklearn.metrics.mean_tweedie_deviance")\
 depends on a `power` parameter. As we do not know the true value of the `power` parameter, we here compute the mean deviances for a grid of possible values, and compare the models side by side, i.e. we compare them at identical values of `power`. Ideally, we hope that one model will be consistently better than the other, regardless of `power`.\
\
from sklearn.linear\_model import [TweedieRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html#sklearn.linear_model.TweedieRegressor "sklearn.linear_model.TweedieRegressor")\
\
glm\_pure\_premium \= [TweedieRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html#sklearn.linear_model.TweedieRegressor "sklearn.linear_model.TweedieRegressor")\
(power\=1.9, alpha\=0.1, solver\="newton-cholesky")\
glm\_pure\_premium.fit(\
    X\_train, df\_train\["PurePremium"\], sample\_weight\=df\_train\["Exposure"\]\
)\
\
tweedie\_powers \= \[1.5, 1.7, 1.8, 1.9, 1.99, 1.999, 1.9999\]\
\
scores\_product\_model \= score\_estimator(\
    (glm\_freq, glm\_sev),\
    X\_train,\
    X\_test,\
    df\_train,\
    df\_test,\
    target\="PurePremium",\
    weights\="Exposure",\
    tweedie\_powers\=tweedie\_powers,\
)\
\
scores\_glm\_pure\_premium \= score\_estimator(\
    glm\_pure\_premium,\
    X\_train,\
    X\_test,\
    df\_train,\
    df\_test,\
    target\="PurePremium",\
    weights\="Exposure",\
    tweedie\_powers\=tweedie\_powers,\
)\
\
scores \= [pd.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html#pandas.concat "pandas.concat")\
(\
    \[scores\_product\_model, scores\_glm\_pure\_premium\],\
    axis\=1,\
    sort\=True,\
    keys\=("Product Model", "TweedieRegressor"),\
)\
print("Evaluation of the Product Model and the Tweedie Regressor on target PurePremium")\
with [pd.option\_context](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.option_context.html#pandas.option_context "pandas.option_context")\
("display.expand\_frame\_repr", False):\
    print(scores)\
\
Copy to clipboard\
\
Evaluation of the Product Model and the Tweedie Regressor on target PurePremium\
                          Product Model               TweedieRegressor\
subset                            train          test            train          test\
metric\
D² explained                        NaN           NaN     1.640000e-02  1.370000e-02\
mean Tweedie dev p=1.5000  7.670090e+01  7.616900e+01     7.640460e+01  7.641980e+01\
mean Tweedie dev p=1.7000  3.695810e+01  3.683920e+01     3.682720e+01  3.692730e+01\
mean Tweedie dev p=1.8000  3.046050e+01  3.040490e+01     3.037490e+01  3.045690e+01\
mean Tweedie dev p=1.9000  3.387610e+01  3.384970e+01     3.382040e+01  3.388020e+01\
mean Tweedie dev p=1.9900  2.015718e+02  2.015412e+02     2.015342e+02  2.015600e+02\
mean Tweedie dev p=1.9990  1.914574e+03  1.914370e+03     1.914537e+03  1.914388e+03\
mean Tweedie dev p=1.9999  1.904751e+04  1.904556e+04     1.904747e+04  1.904558e+04\
mean abs. error            2.730129e+02  2.722124e+02     2.740176e+02  2.731633e+02\
mean squared error         3.295040e+07  3.212197e+07     3.295518e+07  3.213087e+07\
\
Copy to clipboard\
\
In this example, both modeling approaches yield comparable performance metrics. For implementation reasons, the percentage of explained variance D2 is not available for the product model.\
\
We can additionally validate these models by comparing observed and predicted total claim amount over the test and train subsets. We see that, on average, both model tend to underestimate the total claim (but this behavior depends on the amount of regularization).\
\
res \= \[\]\
for subset\_label, X, df in \[\
    ("train", X\_train, df\_train),\
    ("test", X\_test, df\_test),\
\]:\
    exposure \= df\["Exposure"\].values\
    res.append(\
        {\
            "subset": subset\_label,\
            "observed": df\["ClaimAmount"\].values.sum(),\
            "predicted, frequency\*severity model": [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")\
(\
                exposure \* glm\_freq.predict(X) \* glm\_sev.predict(X)\
            ),\
            "predicted, tweedie, power=%.2f" % glm\_pure\_premium.power: [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")\
(\
                exposure \* glm\_pure\_premium.predict(X)\
            ),\
        }\
    )\
\
print([pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(res).set\_index("subset").T)\
\
Copy to clipboard\
\
subset                                      train          test\
observed                             3.917618e+07  1.299546e+07\
predicted, frequency\*severity model  3.916579e+07  1.313280e+07\
predicted, tweedie, power=1.90       3.952914e+07  1.325666e+07\
\
Copy to clipboard\
\
Finally, we can compare the two models using a plot of cumulative claims: for each model, the policyholders are ranked from safest to riskiest based on the model predictions and the cumulative proportion of claim amounts is plotted against the cumulative proportion of exposure. This plot is often called the ordered Lorenz curve of the model.\
\
The Gini coefficient (based on the area between the curve and the diagonal) can be used as a model selection metric to quantify the ability of the model to rank policyholders. Note that this metric does not reflect the ability of the models to make accurate predictions in terms of absolute value of total claim amounts but only in terms of relative amounts as a ranking metric. The Gini coefficient is upper bounded by 1.0 but even an oracle model that ranks the policyholders by the observed claim amounts cannot reach a score of 1.0.\
\
We observe that both models are able to rank policyholders by riskiness significantly better than chance although they are also both far from the oracle model due to the natural difficulty of the prediction problem from a few features: most accidents are not predictable and can be caused by environmental circumstances that are not described at all by the input features of the models.\
\
Note that the Gini index only characterizes the ranking performance of the model but not its calibration: any monotonic transformation of the predictions leaves the Gini index of the model unchanged.\
\
Finally one should highlight that the Compound Poisson Gamma model that is directly fit on the pure premium is operationally simpler to develop and maintain as it consists of a single scikit-learn estimator instead of a pair of models, each with its own set of hyperparameters.\
\
from sklearn.metrics import [auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")\
\
def lorenz\_curve(y\_true, y\_pred, exposure):\
    y\_true, y\_pred \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")\
(y\_true), [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")\
(y\_pred)\
    exposure \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")\
(exposure)\
\
    \# order samples by increasing predicted risk:\
    ranking \= [np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")\
(y\_pred)\
    ranked\_exposure \= exposure\[ranking\]\
    ranked\_pure\_premium \= y\_true\[ranking\]\
    cumulative\_claim\_amount \= [np.cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")\
(ranked\_pure\_premium \* ranked\_exposure)\
    cumulative\_claim\_amount /= cumulative\_claim\_amount\[\-1\]\
    cumulative\_exposure \= [np.cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")\
(ranked\_exposure)\
    cumulative\_exposure /= cumulative\_exposure\[\-1\]\
    return cumulative\_exposure, cumulative\_claim\_amount\
\
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(8, 8))\
\
y\_pred\_product \= glm\_freq.predict(X\_test) \* glm\_sev.predict(X\_test)\
y\_pred\_total \= glm\_pure\_premium.predict(X\_test)\
\
for label, y\_pred in \[\
    ("Frequency \* Severity model", y\_pred\_product),\
    ("Compound Poisson Gamma", y\_pred\_total),\
\]:\
    cum\_exposure, cum\_claims \= lorenz\_curve(\
        df\_test\["PurePremium"\], y\_pred, df\_test\["Exposure"\]\
    )\
    gini \= 1 \- 2 \* [auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")\
(cum\_exposure, cum\_claims)\
    label += " (Gini index: {:.3f})".format(gini)\
    ax.plot(cum\_exposure, cum\_claims, linestyle\="-", label\=label)\
\
\# Oracle model: y\_pred == y\_test\
cum\_exposure, cum\_claims \= lorenz\_curve(\
    df\_test\["PurePremium"\], df\_test\["PurePremium"\], df\_test\["Exposure"\]\
)\
gini \= 1 \- 2 \* [auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")\
(cum\_exposure, cum\_claims)\
label \= "Oracle (Gini index: {:.3f})".format(gini)\
ax.plot(cum\_exposure, cum\_claims, linestyle\="-.", color\="gray", label\=label)\
\
\# Random baseline\
ax.plot(\[0, 1\], \[0, 1\], linestyle\="--", color\="black", label\="Random baseline")\
ax.set(\
    title\="Lorenz Curves",\
    xlabel\=(\
        "Cumulative proportion of exposure\\n(ordered by model from safest to riskiest)"\
    ),\
    ylabel\="Cumulative proportion of claim amounts",\
)\
ax.legend(loc\="upper left")\
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")\
()\
\
Copy to clipboard\
\
![Lorenz Curves](https://scikit-learn.org/stable/_images/sphx_glr_plot_tweedie_regression_insurance_claims_003.png)\
\
\[\]\
\
Copy to clipboard\
\
**Total running time of the script:** (0 minutes 6.779 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_tweedie_regression_insurance_claims.ipynb)\
\
[`Download Jupyter notebook: plot_tweedie_regression_insurance_claims.ipynb`](https://scikit-learn.org/stable/_downloads/a97bf662e52d471b04e1ab480c0ad7f2/plot_tweedie_regression_insurance_claims.ipynb)\
\
[`Download Python source code: plot_tweedie_regression_insurance_claims.py`](https://scikit-learn.org/stable/_downloads/86c888008757148890daaf43d664fa71/plot_tweedie_regression_insurance_claims.py)\
\
[`Download zipped: plot_tweedie_regression_insurance_claims.zip`](https://scikit-learn.org/stable/_downloads/f0ca25cfb6bdf6b7e17e64061d600126/plot_tweedie_regression_insurance_claims.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_thumb.png)\
\
[Poisson regression and non-normal loss](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)\
\
Poisson regression and non-normal loss\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_thumb.png)\
\
[Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)\
\
Comparison of Calibration of Classifiers\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_map_data_to_normal_thumb.png)\
\
[Map data to a normal distribution](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_map_data_to_normal.html)\
\
Map data to a normal distribution\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_predict_thumb.png)\
\
[Plotting Cross-Validated Predictions](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_predict.html)\
\
Plotting Cross-Validated Predictions\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/86c888008757148890daaf43d664fa71/plot_tweedie_regression_insurance_claims.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/a97bf662e52d471b04e1ab480c0ad7f2/plot_tweedie_regression_insurance_claims.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/f0ca25cfb6bdf6b7e17e64061d600126/plot_tweedie_regression_insurance_claims.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_tweedie_regression_insurance_claims.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)