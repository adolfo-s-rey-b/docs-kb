[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_ard.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_ard.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_ard.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_ard.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_ard.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_ard.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#sphx-glr-download-auto-examples-linear-model-plot-ard-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparing Linear Bayesian Regressors[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#comparing-linear-bayesian-regressors "Link to this heading")

==============================================================================================================================================================================

This example compares two different bayesian regressors:

*   an [Automatic Relevance Determination - ARD](https://scikit-learn.org/stable/modules/linear_model.html#automatic-relevance-determination)
    
*   a [Bayesian Ridge Regression](https://scikit-learn.org/stable/modules/linear_model.html#bayesian-ridge-regression)
    

In the first part, we use an [Ordinary Least Squares](https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares)
 (OLS) model as a baseline for comparing the models’ coefficients with respect to the true coefficients. Thereafter, we show that the estimation of such models is done by iteratively maximizing the marginal log-likelihood of the observations.

In the last section we plot predictions and uncertainties for the ARD and the Bayesian Ridge regressions using a polynomial feature expansion to fit a non-linear relationship between `X` and `y`.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Models robustness to recover the ground truth weights[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#models-robustness-to-recover-the-ground-truth-weights "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Generate synthetic dataset[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#generate-synthetic-dataset "Link to this heading")

We generate a dataset where `X` and `y` are linearly linked: 10 of the features of `X` will be used to generate `y`. The other features are not useful at predicting `y`. In addition, we generate a dataset where `n_samples == n_features`. Such a setting is challenging for an OLS model and leads potentially to arbitrary large weights. Having a prior on the weights and a penalty alleviates the problem. Finally, gaussian noise is added.

from sklearn.datasets import [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")

X, y, true\_weights \= [make\_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
(
    n\_samples\=100,
    n\_features\=100,
    n\_informative\=10,
    noise\=8,
    coef\=True,
    random\_state\=42,
)

Copy to clipboard

### Fit the regressors[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#fit-the-regressors "Link to this heading")

We now fit both Bayesian models and the OLS to later compare the models’ coefficients.

import pandas as pd

from sklearn.linear\_model import [ARDRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
, [BayesianRidge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
, [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")

olr \= [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
().fit(X, y)
brr \= [BayesianRidge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
(compute\_score\=True, max\_iter\=30).fit(X, y)
ard \= [ARDRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
(compute\_score\=True, max\_iter\=30).fit(X, y)
df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    {
        "Weights of true generative process": true\_weights,
        "ARDRegression": ard.coef\_,
        "BayesianRidge": brr.coef\_,
        "LinearRegression": olr.coef\_,
    }
)

Copy to clipboard

### Plot the true and estimated coefficients[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#plot-the-true-and-estimated-coefficients "Link to this heading")

Now we compare the coefficients of each model with the weights of the true generative model.

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import [SymLogNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 6))
ax \= [sns.heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html#seaborn.heatmap "seaborn.heatmap")
(
    df.T,
    norm\=[SymLogNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")
(linthresh\=10e-4, vmin\=-80, vmax\=80),
    cbar\_kws\={"label": "coefficients' values"},
    cmap\="seismic\_r",
)
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("linear model")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("coefficients")
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
(rect\=(0, 0, 1, 0.95))
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Models' coefficients")

Copy to clipboard

![Models' coefficients](https://scikit-learn.org/stable/_images/sphx_glr_plot_ard_001.png)

Due to the added noise, none of the models recover the true weights. Indeed, all models always have more than 10 non-zero coefficients. Compared to the OLS estimator, the coefficients using a Bayesian Ridge regression are slightly shifted toward zero, which stabilises them. The ARD regression provides a sparser solution: some of the non-informative coefficients are set exactly to zero, while shifting others closer to zero. Some non-informative coefficients are still present and retain large values.

### Plot the marginal log-likelihood[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#plot-the-marginal-log-likelihood "Link to this heading")

import numpy as np

ard\_scores \= \-[np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(ard.scores\_)
brr\_scores \= \-[np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(brr.scores\_)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(ard\_scores, color\="navy", label\="ARD")
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(brr\_scores, color\="red", label\="BayesianRidge")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Log-likelihood")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("Iterations")
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(1, 30)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Models log-likelihood")

Copy to clipboard

![Models log-likelihood](https://scikit-learn.org/stable/_images/sphx_glr_plot_ard_002.png)

Indeed, both models minimize the log-likelihood up to an arbitrary cutoff defined by the `max_iter` parameter.

Bayesian regressions with polynomial feature expansion[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#bayesian-regressions-with-polynomial-feature-expansion "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Generate synthetic dataset[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#id1 "Link to this heading")

We create a target that is a non-linear function of the input feature. Noise following a standard uniform distribution is added.

from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
, [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
n\_samples \= 110

\# sort the data to make plotting easier later
X \= [np.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
(\-10 \* rng.rand(n\_samples) + 10)
noise \= rng.normal(0, 1, n\_samples) \* 1.35
y \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(X) \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(X) + noise
full\_data \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
({"input\_feature": X, "target": y})
X \= X.reshape((\-1, 1))

\# extrapolation
X\_plot \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(10, 10.4, 10)
y\_plot \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(X\_plot) \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(X\_plot)
X\_plot \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
((X, X\_plot.reshape((\-1, 1))))
y\_plot \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
((y \- noise, y\_plot))

Copy to clipboard

### Fit the regressors[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#id2 "Link to this heading")

Here we try a degree 10 polynomial to potentially overfit, though the bayesian linear models regularize the size of the polynomial coefficients. As `fit_intercept=True` by default for [`ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
 and [`BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
, then [`PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
 should not introduce an additional bias feature. By setting `return_std=True`, the bayesian regressors return the standard deviation of the posterior distribution for the model parameters.

ard\_poly \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
(degree\=10, include\_bias\=False),
    [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(),
    [ARDRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
(),
).fit(X, y)
brr\_poly \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
(degree\=10, include\_bias\=False),
    [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(),
    [BayesianRidge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
(),
).fit(X, y)

y\_ard, y\_ard\_std \= ard\_poly.predict(X\_plot, return\_std\=True)
y\_brr, y\_brr\_std \= brr\_poly.predict(X\_plot, return\_std\=True)

Copy to clipboard

### Plotting polynomial regressions with std errors of the scores[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#plotting-polynomial-regressions-with-std-errors-of-the-scores "Link to this heading")

ax \= [sns.scatterplot](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot "seaborn.scatterplot")
(
    data\=full\_data, x\="input\_feature", y\="target", color\="black", alpha\=0.75
)
ax.plot(X\_plot, y\_plot, color\="black", label\="Ground Truth")
ax.plot(X\_plot, y\_brr, color\="red", label\="BayesianRidge with polynomial features")
ax.plot(X\_plot, y\_ard, color\="navy", label\="ARD with polynomial features")
ax.fill\_between(
    X\_plot.ravel(),
    y\_ard \- y\_ard\_std,
    y\_ard + y\_ard\_std,
    color\="navy",
    alpha\=0.3,
)
ax.fill\_between(
    X\_plot.ravel(),
    y\_brr \- y\_brr\_std,
    y\_brr + y\_brr\_std,
    color\="red",
    alpha\=0.3,
)
ax.legend()
\_ \= ax.set\_title("Polynomial fit of a non-linear feature")

Copy to clipboard

![Polynomial fit of a non-linear feature](https://scikit-learn.org/stable/_images/sphx_glr_plot_ard_003.png)

The error bars represent one standard deviation of the predicted gaussian distribution of the query points. Notice that the ARD regression captures the ground truth the best when using the default parameters in both models, but further reducing the `lambda_init` hyperparameter of the Bayesian Ridge can reduce its bias (see example [Curve Fitting with Bayesian Ridge Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html#sphx-glr-auto-examples-linear-model-plot-bayesian-ridge-curvefit-py)
). Finally, due to the intrinsic limitations of a polynomial regression, both models fail when extrapolating.

**Total running time of the script:** (0 minutes 0.713 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_ard.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_ard.ipynb)

[`Download Jupyter notebook: plot_ard.ipynb`](https://scikit-learn.org/stable/_downloads/c5d41d4d7d1dab3e49804c2e2c4222e8/plot_ard.ipynb)

[`Download Python source code: plot_ard.py`](https://scikit-learn.org/stable/_downloads/892d774326b523935a603b8700193195/plot_ard.py)

[`Download zipped: plot_ard.zip`](https://scikit-learn.org/stable/_downloads/c38a99335d08742ba0737174364ad279/plot_ard.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_thumb.png)

[L1-based models for Sparse Signals](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html)

L1-based models for Sparse Signals

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_polynomial_interpolation_thumb.png)

[Polynomial and Spline interpolation](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html)

Polynomial and Spline interpolation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_weighted_samples_thumb.png)

[SVM: Weighted samples](https://scikit-learn.org/stable/auto_examples/svm/plot_weighted_samples.html)

SVM: Weighted samples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_coeffs_thumb.png)

[Ridge coefficients as a function of the L2 Regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html)

Ridge coefficients as a function of the L2 Regularization

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/892d774326b523935a603b8700193195/plot_ard.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c5d41d4d7d1dab3e49804c2e2c4222e8/plot_ard.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/c38a99335d08742ba0737174364ad279/plot_ard.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_ard.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_ard.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)