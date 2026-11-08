[Skip to main content](https://scikit-learn.org/stable/auto_examples/impute/plot_iterative_imputer_variants_comparison.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/impute/plot_iterative_imputer_variants_comparison.html#sphx-glr-download-auto-examples-impute-plot-iterative-imputer-variants-comparison-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Imputing missing values with variants of IterativeImputer[#](https://scikit-learn.org/stable/auto_examples/impute/plot_iterative_imputer_variants_comparison.html#imputing-missing-values-with-variants-of-iterativeimputer "Link to this heading")

====================================================================================================================================================================================================================================================

The [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
 class is very flexible - it can be used with a variety of estimators to do round-robin regression, treating every variable as an output in turn.

In this example we compare some estimators for the purpose of missing feature imputation with [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
:

*   [`BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
    : regularized linear regression
    
*   [`RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    : forests of randomized trees regression
    
*   [`make_pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
     ([`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
    , [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    ): a pipeline with the expansion of a degree 2 polynomial kernel and regularized linear regression
    
*   [`KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
    : comparable to other KNN imputation approaches
    

Of particular interest is the ability of [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
 to mimic the behavior of missForest, a popular imputation package for R.

Note that [`KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
 is different from KNN imputation, which learns from samples with missing values by using a distance metric that accounts for missing values, rather than imputing them.

The goal is to compare different estimators to see which one is best for the [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
 when using a [`BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
 estimator on the California housing dataset with a single value randomly removed from each row.

For this particular pattern of missing values we see that [`BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
 and [`RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
 give the best results.

It should be noted that some estimators such as [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 can natively deal with missing features and are often recommended over building pipelines with complex and costly missing values imputation strategies.

![California Housing Regression with Different Imputation Methods](https://scikit-learn.org/stable/_images/sphx_glr_plot_iterative_imputer_variants_comparison_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.datasets import [fetch\_california\_housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")
from sklearn.ensemble import [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")

\# To use this experimental feature, we need to explicitly ask for it:
from sklearn.experimental import enable\_iterative\_imputer  \# noqa: F401
from sklearn.impute import [IterativeImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
, [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
from sklearn.kernel\_approximation import [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
from sklearn.linear\_model import [BayesianRidge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
, [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
from sklearn.model\_selection import [cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
from sklearn.neighbors import [KNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")

N\_SPLITS \= 5

X\_full, y\_full \= [fetch\_california\_housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")
(return\_X\_y\=True)
\# ~2k samples is enough for the purpose of the example.
\# Remove the following two lines for a slower run with different error bars.
X\_full \= X\_full\[::10\]
y\_full \= y\_full\[::10\]
n\_samples, n\_features \= X\_full.shape

def compute\_score\_for(X, y, imputer\=None):
    \# We scale data before imputation and training a target estimator,
    \# because our target estimator and some of the imputers assume
    \# that the features have similar scales.
    if imputer is None:
        estimator \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
(), [BayesianRidge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
())
    else:
        estimator \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
(), imputer, [BayesianRidge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
())
    return [cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
(
        estimator, X, y, scoring\="neg\_mean\_squared\_error", cv\=N\_SPLITS
    )

\# Estimate the score on the entire dataset, with no missing values
score\_full\_data \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    compute\_score\_for(X\_full, y\_full),
    columns\=\["Full Data"\],
)

\# Add a single missing value to each row
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
X\_missing \= X\_full.copy()
y\_missing \= y\_full
missing\_samples \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(n\_samples)
missing\_features \= rng.choice(n\_features, n\_samples, replace\=True)
X\_missing\[missing\_samples, missing\_features\] \= [np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")

\# Estimate the score after imputation (mean and median strategies)
score\_simple\_imputer \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
()
for strategy in ("mean", "median"):
    score\_simple\_imputer\[strategy\] \= compute\_score\_for(
        X\_missing, y\_missing, [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
(strategy\=strategy)
    )

\# Estimate the score after iterative imputation of the missing values
\# with different estimators
named\_estimators \= \[\
    ("Bayesian Ridge", [BayesianRidge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")\
()),\
    (\
        "Random Forest",\
        [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")\
(\
            \# We tuned the hyperparameters of the RandomForestRegressor to get a good\
            \# enough predictive performance for a restricted execution time.\
            n\_estimators\=5,\
            max\_depth\=10,\
            bootstrap\=True,\
            max\_samples\=0.5,\
            n\_jobs\=2,\
            random\_state\=0,\
        ),\
    ),\
    (\
        "Nystroem + Ridge",\
        [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
            [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")\
(kernel\="polynomial", degree\=2, random\_state\=0), [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")\
(alpha\=1e4)\
        ),\
    ),\
    (\
        "k-NN",\
        [KNeighborsRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")\
(n\_neighbors\=10),\
    ),\
\]
score\_iterative\_imputer \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
()
\# Iterative imputer is sensitive to the tolerance and
\# dependent on the estimator used internally.
\# We tuned the tolerance to keep this example run with limited computational
\# resources while not changing the results too much compared to keeping the
\# stricter default value for the tolerance parameter.
tolerances \= (1e-3, 1e-1, 1e-1, 1e-2)
for (name, impute\_estimator), tol in zip(named\_estimators, tolerances):
    score\_iterative\_imputer\[name\] \= compute\_score\_for(
        X\_missing,
        y\_missing,
        [IterativeImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
(
            random\_state\=0, estimator\=impute\_estimator, max\_iter\=40, tol\=tol
        ),
    )

scores \= [pd.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html#pandas.concat "pandas.concat")
(
    \[score\_full\_data, score\_simple\_imputer, score\_iterative\_imputer\],
    keys\=\["Original", "SimpleImputer", "IterativeImputer"\],
    axis\=1,
)

\# plot california housing results
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(13, 6))
means \= \-scores.mean()
errors \= scores.std()
means.plot.barh(xerr\=errors, ax\=ax)
ax.set\_title("California Housing Regression with Different Imputation Methods")
ax.set\_xlabel("MSE (smaller is better)")
ax.set\_yticks([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(means.shape\[0\]))
ax.set\_yticklabels(\[" w/ ".join(label) for label in means.index.tolist()\])
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
(pad\=1)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 5.774 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo16.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/impute/plot_iterative_imputer_variants_comparison.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo16.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/impute/plot_iterative_imputer_variants_comparison.ipynb)

[`Download Jupyter notebook: plot_iterative_imputer_variants_comparison.ipynb`](https://scikit-learn.org/stable/_downloads/067cd5d39b097d2c49dd98f563dac13a/plot_iterative_imputer_variants_comparison.ipynb)

[`Download Python source code: plot_iterative_imputer_variants_comparison.py`](https://scikit-learn.org/stable/_downloads/54823a4305997fc1281f34ce676fb43e/plot_iterative_imputer_variants_comparison.py)

[`Download zipped: plot_iterative_imputer_variants_comparison.zip`](https://scikit-learn.org/stable/_downloads/86c2bd1cbaae0fc61dd3ddfc8ccfe64e/plot_iterative_imputer_variants_comparison.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_missing_values_thumb.png)

[Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html)

Imputing missing values before building an estimator

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_estimator_representation_thumb.png)

[Displaying estimators and complex pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_estimator_representation.html)

Displaying estimators and complex pipelines

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ard_thumb.png)

[Comparing Linear Bayesian Regressors](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html)

Comparing Linear Bayesian Regressors

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/54823a4305997fc1281f34ce676fb43e/plot_iterative_imputer_variants_comparison.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/067cd5d39b097d2c49dd98f563dac13a/plot_iterative_imputer_variants_comparison.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/86c2bd1cbaae0fc61dd3ddfc8ccfe64e/plot_iterative_imputer_variants_comparison.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo16.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/impute/plot_iterative_imputer_variants_comparison.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo16.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/impute/plot_iterative_imputer_variants_comparison.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)