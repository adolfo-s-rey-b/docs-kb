[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html#sphx-glr-download-auto-examples-linear-model-plot-poisson-regression-non-normal-loss-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Poisson regression and non-normal loss[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html#poisson-regression-and-non-normal-loss "Link to this heading")

=================================================================================================================================================================================================================

This example illustrates the use of log-linear Poisson regression on the [French Motor Third-Party Liability Claims dataset](https://www.openml.org/d/41214)
 from [\[1\]](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html#id2)
 and compares it with a linear model fitted with the usual least squared error and a non-linear GBRT model fitted with the Poisson loss (and a log-link).

A few definitions:

*   A **policy** is a contract between an insurance company and an individual: the **policyholder**, that is, the vehicle driver in this case.
    
*   A **claim** is the request made by a policyholder to the insurer to compensate for a loss covered by the insurance.
    
*   The **exposure** is the duration of the insurance coverage of a given policy, in years.
    
*   The claim **frequency** is the number of claims divided by the exposure, typically measured in number of claims per year.
    

In this dataset, each sample corresponds to an insurance policy. Available features include driver age, vehicle age, vehicle power, etc.

Our goal is to predict the expected frequency of claims following car accidents for a new policyholder given the historical data over a population of policyholders.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Copy to clipboard

The French Motor Third-Party Liability Claims dataset[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html#the-french-motor-third-party-liability-claims-dataset "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s load the motor claim dataset from OpenML: [https://www.openml.org/d/41214](https://www.openml.org/d/41214)

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")

df \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(data\_id\=41214, as\_frame\=True).frame
df

Copy to clipboard

|     | IDpol | ClaimNb | Exposure | Area | VehPower | VehAge | DrivAge | BonusMalus | VehBrand | VehGas | Density | Region |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 1.0 | 1   | 0.10000 | D   | 5   | 0   | 55  | 50  | B12 | 'Regular' | 1217 | R82 |
| 1   | 3.0 | 1   | 0.77000 | D   | 5   | 0   | 55  | 50  | B12 | 'Regular' | 1217 | R82 |
| 2   | 5.0 | 1   | 0.75000 | B   | 6   | 2   | 52  | 50  | B12 | 'Diesel' | 54  | R22 |
| 3   | 10.0 | 1   | 0.09000 | B   | 7   | 0   | 46  | 50  | B12 | 'Diesel' | 76  | R72 |
| 4   | 11.0 | 1   | 0.84000 | B   | 7   | 0   | 46  | 50  | B12 | 'Diesel' | 76  | R72 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 678008 | 6114326.0 | 0   | 0.00274 | E   | 4   | 0   | 54  | 50  | B12 | 'Regular' | 3317 | R93 |
| 678009 | 6114327.0 | 0   | 0.00274 | E   | 4   | 0   | 41  | 95  | B12 | 'Regular' | 9850 | R11 |
| 678010 | 6114328.0 | 0   | 0.00274 | D   | 6   | 2   | 45  | 50  | B12 | 'Diesel' | 1323 | R82 |
| 678011 | 6114329.0 | 0   | 0.00274 | B   | 4   | 0   | 60  | 50  | B12 | 'Regular' | 95  | R26 |
| 678012 | 6114330.0 | 0   | 0.00274 | B   | 7   | 6   | 29  | 54  | B12 | 'Diesel' | 65  | R72 |

678013 rows × 12 columns

  
  

The number of claims (`ClaimNb`) is a positive integer that can be modeled as a Poisson distribution. It is then assumed to be the number of discrete events occurring with a constant rate in a given time interval (`Exposure`, in units of years).

Here we want to model the frequency `y = ClaimNb / Exposure` conditionally on `X` via a (scaled) Poisson distribution, and use `Exposure` as `sample_weight`.

df\["Frequency"\] \= df\["ClaimNb"\] / df\["Exposure"\]

print(
    "Average Frequency = {}".format([np.average](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average")
(df\["Frequency"\], weights\=df\["Exposure"\]))
)

print(
    "Fraction of exposure with zero claims = {0:.1%}".format(
        df.loc\[df\["ClaimNb"\] \== 0, "Exposure"\].sum() / df\["Exposure"\].sum()
    )
)

fig, (ax0, ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=3, figsize\=(16, 4))
ax0.set\_title("Number of claims")
\_ \= df\["ClaimNb"\].hist(bins\=30, log\=True, ax\=ax0)
ax1.set\_title("Exposure in years")
\_ \= df\["Exposure"\].hist(bins\=30, log\=True, ax\=ax1)
ax2.set\_title("Frequency (number of claims per year)")
\_ \= df\["Frequency"\].hist(bins\=30, log\=True, ax\=ax2)

Copy to clipboard

![Number of claims, Exposure in years, Frequency (number of claims per year)](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_001.png)

Average Frequency = 0.10070308464041305
Fraction of exposure with zero claims = 93.9%

Copy to clipboard

The remaining columns can be used to predict the frequency of claim events. Those columns are very heterogeneous with a mix of categorical and numeric variables with different scales, possibly very unevenly distributed.

In order to fit linear models with those predictors it is therefore necessary to perform standard feature transformations as follows:

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

log\_scale\_transformer \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    [FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
([np.log](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")
, validate\=False), [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
()
)

linear\_model\_preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
    \[\
        ("passthrough\_numeric", "passthrough", \["BonusMalus"\]),\
        (\
            "binned\_numeric",\
            [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")\
(\
                n\_bins\=10, quantile\_method\="averaged\_inverted\_cdf", random\_state\=0\
            ),\
            \["VehAge", "DrivAge"\],\
        ),\
        ("log\_scaled\_numeric", log\_scale\_transformer, \["Density"\]),\
        (\
            "onehot\_categorical",\
            [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(),\
            \["VehBrand", "VehPower", "VehGas", "Region", "Area"\],\
        ),\
    \],
    remainder\="drop",
)

Copy to clipboard

A constant prediction baseline[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html#a-constant-prediction-baseline "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It is worth noting that more than 93% of policyholders have zero claims. If we were to convert this problem into a binary classification task, it would be significantly imbalanced, and even a simplistic model that would only predict mean can achieve an accuracy of 93%.

To evaluate the pertinence of the used metrics, we will consider as a baseline a “dummy” estimator that constantly predicts the mean frequency of the training sample.

from sklearn.dummy import [DummyRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")

df\_train, df\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(df, test\_size\=0.33, random\_state\=0)

dummy \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("preprocessor", linear\_model\_preprocessor),\
        ("regressor", [DummyRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")\
(strategy\="mean")),\
    \]
).fit(df\_train, df\_train\["Frequency"\], regressor\_\_sample\_weight\=df\_train\["Exposure"\])

Copy to clipboard

Let’s compute the performance of this constant prediction baseline with 3 different regression metrics:

from sklearn.metrics import (
    [mean\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
,
    [mean\_poisson\_deviance](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html#sklearn.metrics.mean_poisson_deviance "sklearn.metrics.mean_poisson_deviance")
,
    [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
,
)

def score\_estimator(estimator, df\_test):
    """Score an estimator on the test set."""
    y\_pred \= estimator.predict(df\_test)

    print(
        "MSE: %.3f"
        % [mean\_squared\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")
(
            df\_test\["Frequency"\], y\_pred, sample\_weight\=df\_test\["Exposure"\]
        )
    )
    print(
        "MAE: %.3f"
        % [mean\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")
(
            df\_test\["Frequency"\], y\_pred, sample\_weight\=df\_test\["Exposure"\]
        )
    )

    \# Ignore non-positive predictions, as they are invalid for
    \# the Poisson deviance.
    mask \= y\_pred \> 0
    if (~mask).any():
        n\_masked, n\_samples \= (~mask).sum(), mask.shape\[0\]
        print(
            "WARNING: Estimator yields invalid, non-positive predictions "
            f" for {n\_masked} samples out of {n\_samples}. These predictions "
            "are ignored when computing the Poisson deviance."
        )

    print(
        "mean Poisson deviance: %.3f"
        % [mean\_poisson\_deviance](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html#sklearn.metrics.mean_poisson_deviance "sklearn.metrics.mean_poisson_deviance")
(
            df\_test\["Frequency"\]\[mask\],
            y\_pred\[mask\],
            sample\_weight\=df\_test\["Exposure"\]\[mask\],
        )
    )

print("Constant mean frequency evaluation:")
score\_estimator(dummy, df\_test)

Copy to clipboard

Constant mean frequency evaluation:
MSE: 0.564
MAE: 0.189
mean Poisson deviance: 0.625

Copy to clipboard

(Generalized) linear models[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html#generalized-linear-models "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We start by modeling the target variable with the (l2 penalized) least squares linear regression model, more commonly known as Ridge regression. We use a low penalization `alpha`, as we expect such a linear model to under-fit on such a large dataset.

from sklearn.linear\_model import [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")

ridge\_glm \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("preprocessor", linear\_model\_preprocessor),\
        ("regressor", [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")\
(alpha\=1e-6)),\
    \]
).fit(df\_train, df\_train\["Frequency"\], regressor\_\_sample\_weight\=df\_train\["Exposure"\])

Copy to clipboard

The Poisson deviance cannot be computed on non-positive values predicted by the model. For models that do return a few non-positive predictions (e.g. [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
) we ignore the corresponding samples, meaning that the obtained Poisson deviance is approximate. An alternative approach could be to use [`TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
 meta-estimator to map `y_pred` to a strictly positive domain.

print("Ridge evaluation:")
score\_estimator(ridge\_glm, df\_test)

Copy to clipboard

Ridge evaluation:
MSE: 0.560
MAE: 0.186
WARNING: Estimator yields invalid, non-positive predictions  for 595 samples out of 223745. These predictions are ignored when computing the Poisson deviance.
mean Poisson deviance: 0.597

Copy to clipboard

Next we fit the Poisson regressor on the target variable. We set the regularization strength `alpha` to approximately 1e-6 over number of samples (i.e. `1e-12`) in order to mimic the Ridge regressor whose L2 penalty term scales differently with the number of samples.

Since the Poisson regressor internally models the log of the expected target value instead of the expected value directly (log vs identity link function), the relationship between X and y is not exactly linear anymore. Therefore the Poisson regressor is called a Generalized Linear Model (GLM) rather than a vanilla linear model as is the case for Ridge regression.

from sklearn.linear\_model import [PoissonRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")

n\_samples \= df\_train.shape\[0\]

poisson\_glm \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("preprocessor", linear\_model\_preprocessor),\
        ("regressor", [PoissonRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")\
(alpha\=1e-12, solver\="newton-cholesky")),\
    \]
)
poisson\_glm.fit(
    df\_train, df\_train\["Frequency"\], regressor\_\_sample\_weight\=df\_train\["Exposure"\]
)

print("PoissonRegressor evaluation:")
score\_estimator(poisson\_glm, df\_test)

Copy to clipboard

PoissonRegressor evaluation:
MSE: 0.560
MAE: 0.186
mean Poisson deviance: 0.594

Copy to clipboard

Gradient Boosting Regression Trees for Poisson regression[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html#gradient-boosting-regression-trees-for-poisson-regression "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Finally, we will consider a non-linear model, namely Gradient Boosting Regression Trees. Tree-based models do not require the categorical data to be one-hot encoded: instead, we can encode each category label with an arbitrary integer using [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
. With this encoding, the trees will treat the categorical features as ordered features, which might not be always a desired behavior. However this effect is limited for deep enough trees which are able to recover the categorical nature of the features. The main advantage of the [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
 over the [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
 is that it will make training faster.

Gradient Boosting also gives the possibility to fit the trees with a Poisson loss (with an implicit log-link function) instead of the default least-squares loss. Here we only fit trees with the Poisson loss to keep this example concise.

from sklearn.ensemble import [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
from sklearn.preprocessing import [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")

tree\_preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
    \[\
        (\
            "categorical",\
            [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")\
(),\
            \["VehBrand", "VehPower", "VehGas", "Region", "Area"\],\
        ),\
        ("numeric", "passthrough", \["VehAge", "DrivAge", "BonusMalus", "Density"\]),\
    \],
    remainder\="drop",
)
poisson\_gbrt \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("preprocessor", tree\_preprocessor),\
        (\
            "regressor",\
            [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")\
(loss\="poisson", max\_leaf\_nodes\=128),\
        ),\
    \]
)
poisson\_gbrt.fit(
    df\_train, df\_train\["Frequency"\], regressor\_\_sample\_weight\=df\_train\["Exposure"\]
)

print("Poisson Gradient Boosted Trees evaluation:")
score\_estimator(poisson\_gbrt, df\_test)

Copy to clipboard

Poisson Gradient Boosted Trees evaluation:
MSE: 0.561
MAE: 0.184
mean Poisson deviance: 0.575

Copy to clipboard

Like the Poisson GLM above, the gradient boosted trees model minimizes the Poisson deviance. However, because of a higher predictive power, it reaches lower values of Poisson deviance.

Evaluating models with a single train / test split is prone to random fluctuations. If computing resources allow, it should be verified that cross-validated performance metrics would lead to similar conclusions.

The qualitative difference between these models can also be visualized by comparing the histogram of observed target values with that of predicted values:

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=4, figsize\=(16, 6), sharey\=True)
fig.subplots\_adjust(bottom\=0.2)
n\_bins \= 20
for row\_idx, label, df in zip(range(2), \["train", "test"\], \[df\_train, df\_test\]):
    df\["Frequency"\].hist(bins\=[np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-1, 30, n\_bins), ax\=axes\[row\_idx, 0\])

    axes\[row\_idx, 0\].set\_title("Data")
    axes\[row\_idx, 0\].set\_yscale("log")
    axes\[row\_idx, 0\].set\_xlabel("y (observed Frequency)")
    axes\[row\_idx, 0\].set\_ylim(\[1e1, 5e5\])
    axes\[row\_idx, 0\].set\_ylabel(label + " samples")

    for idx, model in enumerate(\[ridge\_glm, poisson\_glm, poisson\_gbrt\]):
        y\_pred \= model.predict(df)

        [pd.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
(y\_pred).hist(
            bins\=[np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-1, 4, n\_bins), ax\=axes\[row\_idx, idx + 1\]
        )
        axes\[row\_idx, idx + 1\].set(
            title\=model\[\-1\].\_\_class\_\_.\_\_name\_\_,
            yscale\="log",
            xlabel\="y\_pred (predicted expected Frequency)",
        )
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![Data, Ridge, PoissonRegressor, HistGradientBoostingRegressor, Data, Ridge, PoissonRegressor, HistGradientBoostingRegressor](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_002.png)

The experimental data presents a long tail distribution for `y`. In all models, we predict the expected frequency of a random variable, so we will have necessarily fewer extreme values than for the observed realizations of that random variable. This explains that the mode of the histograms of model predictions doesn’t necessarily correspond to the smallest value. Additionally, the normal distribution used in `Ridge` has a constant variance, while for the Poisson distribution used in `PoissonRegressor` and `HistGradientBoostingRegressor`, the variance is proportional to the predicted expected value.

Thus, among the considered estimators, `PoissonRegressor` and `HistGradientBoostingRegressor` are a-priori better suited for modeling the long tail distribution of the non-negative data as compared to the `Ridge` model which makes a wrong assumption on the distribution of the target variable.

The `HistGradientBoostingRegressor` estimator has the most flexibility and is able to predict higher expected values.

Note that we could have used the least squares loss for the `HistGradientBoostingRegressor` model. This would wrongly assume a normal distributed response variable as does the `Ridge` model, and possibly also lead to slightly negative predictions. However the gradient boosted trees would still perform relatively well and in particular better than `PoissonRegressor` thanks to the flexibility of the trees combined with the large number of training samples.

Evaluation of the calibration of predictions[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html#evaluation-of-the-calibration-of-predictions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To ensure that estimators yield reasonable predictions for different policyholder types, we can bin test samples according to `y_pred` returned by each model. Then for each bin, we compare the mean predicted `y_pred`, with the mean observed target:

from sklearn.utils import [gen\_even\_slices](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_even_slices.html#sklearn.utils.gen_even_slices "sklearn.utils.gen_even_slices")

def \_mean\_frequency\_by\_risk\_group(y\_true, y\_pred, sample\_weight\=None, n\_bins\=100):
    """Compare predictions and observations for bins ordered by y\_pred.

    We order the samples by \`\`y\_pred\`\` and split it in bins.
    In each bin the observed mean is compared with the predicted mean.

    Parameters
    ----------
    y\_true: array-like of shape (n\_samples,)
        Ground truth (correct) target values.
    y\_pred: array-like of shape (n\_samples,)
        Estimated target values.
    sample\_weight : array-like of shape (n\_samples,)
        Sample weights.
    n\_bins: int
        Number of bins to use.

    Returns
    -------
    bin\_centers: ndarray of shape (n\_bins,)
        bin centers
    y\_true\_bin: ndarray of shape (n\_bins,)
        average y\_pred for each bin
    y\_pred\_bin: ndarray of shape (n\_bins,)
        average y\_pred for each bin
    """
    idx\_sort \= [np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
(y\_pred)
    bin\_centers \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 1, 1 / n\_bins) + 0.5 / n\_bins
    y\_pred\_bin \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(n\_bins)
    y\_true\_bin \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(n\_bins)

    for n, sl in enumerate([gen\_even\_slices](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_even_slices.html#sklearn.utils.gen_even_slices "sklearn.utils.gen_even_slices")
(len(y\_true), n\_bins)):
        weights \= sample\_weight\[idx\_sort\]\[sl\]
        y\_pred\_bin\[n\] \= [np.average](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average")
(y\_pred\[idx\_sort\]\[sl\], weights\=weights)
        y\_true\_bin\[n\] \= [np.average](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average")
(y\_true\[idx\_sort\]\[sl\], weights\=weights)
    return bin\_centers, y\_true\_bin, y\_pred\_bin

print(f"Actual number of claims: {df\_test\['ClaimNb'\].sum()}")
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=2, figsize\=(12, 8))
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(wspace\=0.3)

for axi, model in zip(ax.ravel(), \[ridge\_glm, poisson\_glm, poisson\_gbrt, dummy\]):
    y\_pred \= model.predict(df\_test)
    y\_true \= df\_test\["Frequency"\].values
    exposure \= df\_test\["Exposure"\].values
    q, y\_true\_seg, y\_pred\_seg \= \_mean\_frequency\_by\_risk\_group(
        y\_true, y\_pred, sample\_weight\=exposure, n\_bins\=10
    )

    \# Name of the model after the estimator used in the last step of the
    \# pipeline.
    print(f"Predicted number of claims by {model\[\-1\]}: {[np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(y\_pred \* exposure):.1f}")

    axi.plot(q, y\_pred\_seg, marker\="x", linestyle\="--", label\="predictions")
    axi.plot(q, y\_true\_seg, marker\="o", linestyle\="--", label\="observations")
    axi.set\_xlim(0, 1.0)
    axi.set\_ylim(0, 0.5)
    axi.set(
        title\=model\[\-1\],
        xlabel\="Fraction of samples sorted by y\_pred",
        ylabel\="Mean Frequency (y\_pred)",
    )
    axi.legend()
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![Ridge(alpha=1e-06), PoissonRegressor(alpha=1e-12, solver='newton-cholesky'), HistGradientBoostingRegressor(loss='poisson', max_leaf_nodes=128), DummyRegressor()](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_003.png)

Actual number of claims: 11935
Predicted number of claims by Ridge(alpha=1e-06): 11933.4
Predicted number of claims by PoissonRegressor(alpha=1e-12, solver='newton-cholesky'): 11932.0
Predicted number of claims by HistGradientBoostingRegressor(loss='poisson', max\_leaf\_nodes=128): 12158.8
Predicted number of claims by DummyRegressor(): 11931.2

Copy to clipboard

The dummy regression model predicts a constant frequency. This model does not attribute the same tied rank to all samples but is none-the-less globally well calibrated (to estimate the mean frequency of the entire population).

The `Ridge` regression model can predict very low expected frequencies that do not match the data. It can therefore severely under-estimate the risk for some policyholders.

`PoissonRegressor` and `HistGradientBoostingRegressor` show better consistency between predicted and observed targets, especially for low predicted target values.

The sum of all predictions also confirms the calibration issue of the `Ridge` model: it under-estimates by more than 3% the total number of claims in the test set while the other three models can approximately recover the total number of claims of the test portfolio.

Evaluation of the ranking power[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html#evaluation-of-the-ranking-power "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For some business applications, we are interested in the ability of the model to rank the riskiest from the safest policyholders, irrespective of the absolute value of the prediction. In this case, the model evaluation would cast the problem as a ranking problem rather than a regression problem.

To compare the 3 models from this perspective, one can plot the cumulative proportion of claims vs the cumulative proportion of exposure for the test samples order by the model predictions, from safest to riskiest according to each model.

This plot is called a Lorenz curve and can be summarized by the Gini index:

from sklearn.metrics import [auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")

def lorenz\_curve(y\_true, y\_pred, exposure):
    y\_true, y\_pred \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(y\_true), [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(y\_pred)
    exposure \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(exposure)

    \# order samples by increasing predicted risk:
    ranking \= [np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
(y\_pred)
    ranked\_frequencies \= y\_true\[ranking\]
    ranked\_exposure \= exposure\[ranking\]
    cumulated\_claims \= [np.cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")
(ranked\_frequencies \* ranked\_exposure)
    cumulated\_claims /= cumulated\_claims\[\-1\]
    cumulated\_exposure \= [np.cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")
(ranked\_exposure)
    cumulated\_exposure /= cumulated\_exposure\[\-1\]
    return cumulated\_exposure, cumulated\_claims

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(8, 8))

for model in \[dummy, ridge\_glm, poisson\_glm, poisson\_gbrt\]:
    y\_pred \= model.predict(df\_test)
    cum\_exposure, cum\_claims \= lorenz\_curve(
        df\_test\["Frequency"\], y\_pred, df\_test\["Exposure"\]
    )
    gini \= 1 \- 2 \* [auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")
(cum\_exposure, cum\_claims)
    label \= "{} (Gini: {:.2f})".format(model\[\-1\], gini)
    ax.plot(cum\_exposure, cum\_claims, linestyle\="-", label\=label)

\# Oracle model: y\_pred == y\_test
cum\_exposure, cum\_claims \= lorenz\_curve(
    df\_test\["Frequency"\], df\_test\["Frequency"\], df\_test\["Exposure"\]
)
gini \= 1 \- 2 \* [auc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")
(cum\_exposure, cum\_claims)
label \= "Oracle (Gini: {:.2f})".format(gini)
ax.plot(cum\_exposure, cum\_claims, linestyle\="-.", color\="gray", label\=label)

\# Random Baseline
ax.plot(\[0, 1\], \[0, 1\], linestyle\="--", color\="black", label\="Random baseline")
ax.set(
    title\="Lorenz curves by model",
    xlabel\="Cumulative proportion of exposure (from safest to riskiest)",
    ylabel\="Cumulative proportion of claims",
)
ax.legend(loc\="upper left")

Copy to clipboard

![Lorenz curves by model](https://scikit-learn.org/stable/_images/sphx_glr_plot_poisson_regression_non_normal_loss_004.png)

<matplotlib.legend.Legend object at 0x7e1d953806e0>

Copy to clipboard

As expected, the dummy regressor is unable to correctly rank the samples and therefore performs the worst on this plot.

The tree-based model is significantly better at ranking policyholders by risk while the two linear models perform similarly.

All three models are significantly better than chance but also very far from making perfect predictions.

This last point is expected due to the nature of the problem: the occurrence of accidents is mostly dominated by circumstantial causes that are not captured in the columns of the dataset and can indeed be considered as purely random.

The linear models assume no interactions between the input variables which likely causes under-fitting. Inserting a polynomial feature extractor ([`PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
) indeed increases their discrimative power by 2 points of Gini index. In particular it improves the ability of the models to identify the top 5% riskiest profiles.

Main takeaways[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html#main-takeaways "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

*   The performance of the models can be evaluated by their ability to yield well-calibrated predictions and a good ranking.
    
*   The calibration of the model can be assessed by plotting the mean observed value vs the mean predicted value on groups of test samples binned by predicted risk.
    
*   The least squares loss (along with the implicit use of the identity link function) of the Ridge regression model seems to cause this model to be badly calibrated. In particular, it tends to underestimate the risk and can even predict invalid negative frequencies.
    
*   Using the Poisson loss with a log-link can correct these problems and lead to a well-calibrated linear model.
    
*   The Gini index reflects the ability of a model to rank predictions irrespective of their absolute values, and therefore only assess their ranking power.
    
*   Despite the improvement in calibration, the ranking power of both linear models are comparable and well below the ranking power of the Gradient Boosting Regression Trees.
    
*   The Poisson deviance computed as an evaluation metric reflects both the calibration and the ranking power of the model. It also makes a linear assumption on the ideal relationship between the expected value and the variance of the response variable. For the sake of conciseness we did not check whether this assumption holds.
    
*   Traditional regression metrics such as Mean Squared Error and Mean Absolute Error are hard to meaningfully interpret on count values with many zeros.
    

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 17.598 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_poisson_regression_non_normal_loss.ipynb)

[`Download Jupyter notebook: plot_poisson_regression_non_normal_loss.ipynb`](https://scikit-learn.org/stable/_downloads/2e4791a177381a6102b21e44083615c8/plot_poisson_regression_non_normal_loss.ipynb)

[`Download Python source code: plot_poisson_regression_non_normal_loss.py`](https://scikit-learn.org/stable/_downloads/d08611fad91456a69eecccc558014285/plot_poisson_regression_non_normal_loss.py)

[`Download zipped: plot_poisson_regression_non_normal_loss.zip`](https://scikit-learn.org/stable/_downloads/1180cd432166ec9764125420df10ec77/plot_poisson_regression_non_normal_loss.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tweedie_regression_insurance_claims_thumb.png)

[Tweedie regression on insurance claims](https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html)

Tweedie regression on insurance claims

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_thumb.png)

[Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)

Comparison of Calibration of Classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)

[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)

Release Highlights for scikit-learn 0.23

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_thumb.png)

[Combine predictors using stacking](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)

Combine predictors using stacking

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/d08611fad91456a69eecccc558014285/plot_poisson_regression_non_normal_loss.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/2e4791a177381a6102b21e44083615c8/plot_poisson_regression_non_normal_loss.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/1180cd432166ec9764125420df10ec77/plot_poisson_regression_non_normal_loss.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_poisson_regression_non_normal_loss.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)