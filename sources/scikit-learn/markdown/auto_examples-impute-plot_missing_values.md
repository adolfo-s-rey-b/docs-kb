[Skip to main content](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/impute/plot_missing_values.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/impute/plot_missing_values.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/impute/plot_missing_values.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/impute/plot_missing_values.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/impute/plot_missing_values.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/impute/plot_missing_values.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#sphx-glr-download-auto-examples-impute-plot-missing-values-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Imputing missing values before building an estimator[#](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#imputing-missing-values-before-building-an-estimator "Link to this heading")

===================================================================================================================================================================================================================

Missing values can be replaced by the mean, the median or the most frequent value using the basic [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
.

In this example we will investigate different imputation techniques:

*   imputation by the constant value 0
    
*   imputation by the mean value of each feature
    
*   k nearest neighbor imputation
    
*   iterative imputation
    

In all the cases, for each feature, we add a new feature indicating the missingness.

We will use two datasets: Diabetes dataset which consists of 10 feature variables collected from diabetes patients with an aim to predict disease progression and California housing dataset for which the target is the median house value for California districts.

As neither of these datasets have missing values, we will remove some values to create new versions with artificially missing data. The performance of [`RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
 on the full original dataset is then compared the performance on the altered datasets with the artificially missing values imputed using different techniques.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Download the data and make missing values sets[#](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#download-the-data-and-make-missing-values-sets "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

First we download the two datasets. Diabetes dataset is shipped with scikit-learn. It has 442 entries, each with 10 features. California housing dataset is much larger with 20640 entries and 8 features. It needs to be downloaded. We will only use the first 300 entries for the sake of speeding up the calculations but feel free to use the whole dataset.

import numpy as np

from sklearn.datasets import [fetch\_california\_housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")
, [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")

X\_diabetes, y\_diabetes \= [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
(return\_X\_y\=True)
X\_california, y\_california \= [fetch\_california\_housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")
(return\_X\_y\=True)

X\_diabetes \= X\_diabetes\[:300\]
y\_diabetes \= y\_diabetes\[:300\]
X\_california \= X\_california\[:300\]
y\_california \= y\_california\[:300\]

def add\_missing\_values(X\_full, y\_full, rng):
    n\_samples, n\_features \= X\_full.shape

    \# Add missing values in 75% of the lines
    missing\_rate \= 0.75
    n\_missing\_samples \= int(n\_samples \* missing\_rate)

    missing\_samples \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(n\_samples, dtype\=bool)
    missing\_samples\[:n\_missing\_samples\] \= True

    rng.shuffle(missing\_samples)
    missing\_features \= rng.randint(0, n\_features, n\_missing\_samples)
    X\_missing \= X\_full.copy()
    X\_missing\[missing\_samples, missing\_features\] \= [np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")
    y\_missing \= y\_full.copy()

    return X\_missing, y\_missing

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)
X\_miss\_diabetes, y\_miss\_diabetes \= add\_missing\_values(X\_diabetes, y\_diabetes, rng)
X\_miss\_california, y\_miss\_california \= add\_missing\_values(
    X\_california, y\_california, rng
)

Copy to clipboard

Impute the missing data and score[#](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#impute-the-missing-data-and-score "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now we will write a function which will score the results on the differently imputed data, including the case of no imputation for full data. We will use [`RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
 for the target regression.

from sklearn.ensemble import [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")

\# To use the experimental IterativeImputer, we need to explicitly ask for it:
from sklearn.experimental import enable\_iterative\_imputer  \# noqa: F401
from sklearn.impute import [IterativeImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
, [KNNImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
, [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
from sklearn.model\_selection import [cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")

N\_SPLITS \= 4

def get\_score(X, y, imputer\=None):
    regressor \= [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
(random\_state\=0)
    if imputer is not None:
        estimator \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(imputer, regressor)
    else:
        estimator \= regressor
    scores \= [cross\_val\_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
(
        estimator, X, y, scoring\="neg\_mean\_squared\_error", cv\=N\_SPLITS
    )
    return scores.mean(), scores.std()

x\_labels \= \[\]

mses\_diabetes \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(5)
stds\_diabetes \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(5)
mses\_california \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(5)
stds\_california \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(5)

Copy to clipboard

### Estimate the score[#](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#estimate-the-score "Link to this heading")

First, we want to estimate the score on the original data:

mses\_diabetes\[0\], stds\_diabetes\[0\] \= get\_score(X\_diabetes, y\_diabetes)
mses\_california\[0\], stds\_california\[0\] \= get\_score(X\_california, y\_california)
x\_labels.append("Full Data")

Copy to clipboard

### Replace missing values by 0[#](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#replace-missing-values-by-0 "Link to this heading")

Now we will estimate the score on the data where the missing values are replaced by 0:

imputer \= [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
(strategy\="constant", fill\_value\=0, add\_indicator\=True)
mses\_diabetes\[1\], stds\_diabetes\[1\] \= get\_score(
    X\_miss\_diabetes, y\_miss\_diabetes, imputer
)
mses\_california\[1\], stds\_california\[1\] \= get\_score(
    X\_miss\_california, y\_miss\_california, imputer
)
x\_labels.append("Zero Imputation")

Copy to clipboard

### Impute missing values with mean[#](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#impute-missing-values-with-mean "Link to this heading")

imputer \= [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
(strategy\="mean", add\_indicator\=True)
mses\_diabetes\[2\], stds\_diabetes\[2\] \= get\_score(
    X\_miss\_diabetes, y\_miss\_diabetes, imputer
)
mses\_california\[2\], stds\_california\[2\] \= get\_score(
    X\_miss\_california, y\_miss\_california, imputer
)
x\_labels.append("Mean Imputation")

Copy to clipboard

### kNN-imputation of the missing values[#](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#knn-imputation-of-the-missing-values "Link to this heading")

[`KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
 imputes missing values using the weighted or unweighted mean of the desired number of nearest neighbors. If your features have vastly different scales (as in the California housing dataset), consider re-scaling them to potentially improve performance.

imputer \= [KNNImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
(add\_indicator\=True)
mses\_diabetes\[3\], stds\_diabetes\[3\] \= get\_score(
    X\_miss\_diabetes, y\_miss\_diabetes, imputer
)
mses\_california\[3\], stds\_california\[3\] \= get\_score(
    X\_miss\_california, y\_miss\_california, [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
(), imputer)
)
x\_labels.append("KNN Imputation")

Copy to clipboard

### Iterative imputation of the missing values[#](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#iterative-imputation-of-the-missing-values "Link to this heading")

Another option is the [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
. This uses round-robin regression, modeling each feature with missing values as a function of other features, in turn. We use the class’s default choice of the regressor model ([`BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
) to predict missing feature values. The performance of the predictor may be negatively affected by vastly different scales of the features, so we re-scale the features in the California housing dataset.

imputer \= [IterativeImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
(add\_indicator\=True)

mses\_diabetes\[4\], stds\_diabetes\[4\] \= get\_score(
    X\_miss\_diabetes, y\_miss\_diabetes, imputer
)
mses\_california\[4\], stds\_california\[4\] \= get\_score(
    X\_miss\_california, y\_miss\_california, [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
(), imputer)
)
x\_labels.append("Iterative Imputation")

mses\_diabetes \= mses\_diabetes \* \-1
mses\_california \= mses\_california \* \-1

Copy to clipboard

Plot the results[#](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#plot-the-results "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

Finally we are going to visualize the score:

import matplotlib.pyplot as plt

n\_bars \= len(mses\_diabetes)
xval \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(n\_bars)

colors \= \["r", "g", "b", "orange", "black"\]

\# plot diabetes results
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(12, 6))
ax1 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(121)
for j in xval:
    ax1.barh(
        j,
        mses\_diabetes\[j\],
        xerr\=stds\_diabetes\[j\],
        color\=colors\[j\],
        alpha\=0.6,
        align\="center",
    )

ax1.set\_title("Imputation Techniques with Diabetes Data")
ax1.set\_xlim(left\=[np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
(mses\_diabetes) \* 0.9, right\=[np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(mses\_diabetes) \* 1.1)
ax1.set\_yticks(xval)
ax1.set\_xlabel("MSE")
ax1.invert\_yaxis()
ax1.set\_yticklabels(x\_labels)

\# plot california dataset results
ax2 \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(122)
for j in xval:
    ax2.barh(
        j,
        mses\_california\[j\],
        xerr\=stds\_california\[j\],
        color\=colors\[j\],
        alpha\=0.6,
        align\="center",
    )

ax2.set\_title("Imputation Techniques with California Data")
ax2.set\_yticks(xval)
ax2.set\_xlabel("MSE")
ax2.invert\_yaxis()
ax2.set\_yticklabels(\[""\] \* n\_bars)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Imputation Techniques with Diabetes Data, Imputation Techniques with California Data](https://scikit-learn.org/stable/_images/sphx_glr_plot_missing_values_001.png)

You can also try different techniques. For instance, the median is a more robust estimator for data with high magnitude variables which could dominate results (otherwise known as a ‘long tail’).

**Total running time of the script:** (0 minutes 7.954 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo16.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/impute/plot_missing_values.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo16.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/impute/plot_missing_values.ipynb)

[`Download Jupyter notebook: plot_missing_values.ipynb`](https://scikit-learn.org/stable/_downloads/a440a8b10138c855100ed5820fdb36b6/plot_missing_values.ipynb)

[`Download Python source code: plot_missing_values.py`](https://scikit-learn.org/stable/_downloads/98345ee267d0372eda8faf906905730e/plot_missing_values.py)

[`Download zipped: plot_missing_values.zip`](https://scikit-learn.org/stable/_downloads/1c9575e30c88815f6de0280064b2c594/plot_missing_values.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iterative_imputer_variants_comparison_thumb.png)

[Imputing missing values with variants of IterativeImputer](https://scikit-learn.org/stable/auto_examples/impute/plot_iterative_imputer_variants_comparison.html)

Imputing missing values with variants of IterativeImputer

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_concentration_prior_thumb.png)

[Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture](https://scikit-learn.org/stable/auto_examples/mixture/plot_concentration_prior.html)

Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/98345ee267d0372eda8faf906905730e/plot_missing_values.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/a440a8b10138c855100ed5820fdb36b6/plot_missing_values.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/1c9575e30c88815f6de0280064b2c594/plot_missing_values.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo16.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/impute/plot_missing_values.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo16.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/impute/plot_missing_values.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)